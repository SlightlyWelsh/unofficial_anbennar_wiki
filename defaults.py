import os.path
from slugify import slugify

from dictionaries import trigger_dict, country_tags, trigger_bools, effect_dict, limits_dict, flags


class Page:
    directory = "./wiki/"

    def __init__(self, page_name):
        self.page_name = page_name
        self.page_path = self.directory + self.page_name + ".md"

    def create(self):
        is_dup = False
        if len(self.page_path) > 200:
            self.page_path = self.page_path[:200]
        while os.path.exists(self.page_path):
            is_dup = True
            if self.page_name.split("_")[-1].isdigit():
                self.page_name = "_".join(self.page_name.split("_")[:-1]) + str(int(self.page_name.split("_")[-1]) + 1)
            else:
                self.page_name = self.page_name + "_1"
                with open(self.directory + "_".join(self.page_name.split("_")[:-1]) + ".md", "a") as base:
                    base.write("\n\n#Pages with same name:\nThe following pages have the same name as this page:\n")
            self.page_path = self.directory + self.page_name + ".md"
            with open(self.directory + "_".join(self.page_name.split("_")[:-1]) + ".md", "a") as base:
                base.write(" - [" + self.page_name + "](" + self.page_name + ".md)\n")
        with open(self.page_path, "w") as page:
            page.seek(0)
            page.truncate()
            if is_dup:
                page.write("This page has the same name as others. For full listing see bottom of [the base page]("
                           + "_".join(self.page_name.split("_")[:-1]) + ".md).\n\n")

    def read_file(self, filename):
        page_dict = {}
        trimmed_text = ""
        with open(filename, "r") as page_text:
            for line in page_text:
                line = line.split("#")[0]
                line = line.replace("\t", " ").strip()
                if line != "":
                    trimmed_text += "\n" + line
        current_dict = page_dict
        higher_dicts = []
        i = 1
        lines = trimmed_text.split("\n")
        for line in lines:
            next_line = '' if i == len(lines) else lines[i]
            current_dict, higher_dicts = self.parse_line(current_dict, higher_dicts, line, next_line)
            i += 1
        return page_dict

    def parse_line(self, current_dict, higher_dicts, line, nextline):
        if "=" in line:
            # Time to assign
            while line.startswith("}"):
                # Close off any dicts one above us
                current_dict = higher_dicts.pop()
                line = line[1:].strip()
            # Get the key/val pair
            assignment = [a.strip() for a in line.split("=", 1)]
            key = assignment[0]
            if "{" in key:
                key_parts = key.split("{")
                key = key_parts[0].strip()
                new_val = "{" + key_parts[1].strip() + " = " + assignment[1]
                assignment = [key, new_val]
            while key in current_dict:
                # make sure key doesn't overwrite existing keys
                key += " "
            if assignment[1].strip("} ") == '':
                # sometimes a dict name is given on one line, then opened on the next
                return self.parse_line(current_dict, higher_dicts, line + nextline, '')
            if len(assignment[1].split("=")) > 1 and "{" not in assignment[1].split("=")[0]:
                # we have multiple assignments in this line, split before them and deal with them later at **
                old_assignment = assignment[1][:]
                while old_assignment.endswith("}"):
                    old_assignment = old_assignment[:-1].strip()
                assignment[1] = assignment[1].split("=", 1)[0].strip().split(" ")[0]
                assignment.append(old_assignment[len(assignment[1]):].strip())
            if assignment[1].startswith("{"):
                # we have a dict, drill down into it
                current_dict[key] = {}
                higher_dicts.append(current_dict)
                current_dict = current_dict[key]
                if len(assignment[1]) > 1:
                    # There's stuff in this dict on this line, deal with it
                    split_assign = assignment[1].split("}", 1)
                    sub_line = split_assign[0].strip("} ")[1:]
                    current_dict, higher_dicts = self.parse_line(current_dict, higher_dicts, sub_line, nextline)
                    if len(split_assign) > 1 and any(char.isalnum() for char in split_assign[1]):
                        # there's other stuff on this line, outside our new dict, deal with it
                        while True:
                            current_dict = higher_dicts.pop()
                            if not split_assign[1].strip().startswith("}"):
                                break
                            split_assign[1] = split_assign[1].replace("}", "", 1)
                        current_dict, higher_dicts = self.parse_line(
                            current_dict, higher_dicts, split_assign[1].strip("{} "), nextline)
            else:
                # the line where we actually write key/val pairs to the dictionary
                current_dict[key] = assignment[1].strip("} ")
            if len(assignment) == 3:
                # ** deal with the multiple assignments
                self.parse_line(current_dict, higher_dicts, assignment[2], nextline)
        elif any(char.isalnum() for char in line):
            # deal with assignments without =
            if "{" in line and line.split("{")[0] != "":
                line = line.replace(" {", "= {", 1)  # If there's no = before {, add it and try again
                return self.parse_line(current_dict, higher_dicts, line, nextline)
            if len(line.strip("} ").split(" ")) > 1:
                # close off dicts before dealing with stuff after them
                current_dict[line.strip("} ").split(" ")[0]] = None
                self.parse_line(current_dict, higher_dicts, " ".join(line.strip("} ").split(" ")[1:]), nextline)
            else:
                # deal with valueless assignments
                current_dict[line.strip("} ")] = None
        while line.endswith("}"):
            # close off dicts
            current_dict = higher_dicts.pop()
            line = line[:-1].strip()
        return current_dict, higher_dicts

    def format_conditions(self, triggers):
        text = ""
        for trig in triggers:
            if type(triggers[trig]) is str and triggers[trig] in country_tags:
                triggers[trig] = country_tags[triggers[trig]]
            if trig in trigger_dict:
                if type(triggers[trig]) is dict:
                    text += "<li>" + trigger_dict[trig][1] + ":</li><ul>"
                    text += self.format_conditions(triggers[trig]) + "</ul>"
                else:
                    text += "<li>" + trigger_dict[trig][0].format(triggers[trig]) + "</li>"
            elif trig in trigger_bools and triggers[trig] in ["yes", "no"]:
                line = trigger_bools[trig][0] if triggers[trig] == "yes" else trigger_bools[trig][1]
                text += "<li>" + line + "</li>"
            elif trig in flags:
                if trig.startswith("had"):
                    duration_key = [key for key in triggers[trig] if key != "flag"][0]
                    flag_page = self.crossref_flag(triggers[trig]["flag"].strip())
                    text += "<li>" + trig.replace("_", " ") + " [" + triggers[trig]["flag"] + "]("
                    text += flag_page + ") for " + triggers[trig][duration_key] + " " + duration_key + "</li>"
                else:
                    flag_page = self.crossref_flag(triggers[trig].strip())
                    text += "<li>" + trig.replace("_", " ") + " ["
                    text += triggers[trig].strip() + "](" + flag_page + ")</li>"
            else:
                if type(triggers[trig]) is dict:
                    text += "<li>" + trig.replace("_", " ").strip() + ":</li><ul>"
                    text += self.format_conditions(triggers[trig]) + "</ul>"
                elif triggers[trig].replace(".", "", 1).isdigit():
                    if trig.startswith("owns"):
                        text += "<li>" + trig.replace("_", " ") + " " + triggers[trig] + "</li>"
                    else:
                        text += "<li>" + trig.replace("_", " ") + " is at least " + triggers[trig] + "</li>"
                elif trig.startswith("has"):
                    text += "<li>" + trig.replace("_", " ") + " " + triggers[trig] + "</li>"
                else:
                    text += "<li>" + trig.replace("_", " ") + " is " + triggers[trig] + "</li>"
        return text

    def format_limit_phrase(self, phrase_key, phrase, is_or=False, is_not=False):
        if type(phrase) is dict and phrase_key not in flags:
            phrase_text = "`"
            for inner_phrase in phrase:
                if inner_phrase.strip() == "NOT":
                    phrase_text += self.format_limit_phrase("", phrase[inner_phrase], is_or, True).replace("  ", " ")
                elif inner_phrase.strip() == "OR":
                    phrase_text += self.format_limit_phrase("", phrase[inner_phrase], True, is_not).replace("  ", " ")
                else:
                    link_word = " does not have " if is_not else " has "
                    if phrase_key == "limit":
                        phrase_text += link_word
                    else:
                        phrase_text += phrase_key.strip().replace("_", " ") + link_word
                    phrase_text += self.format_limit_phrase(inner_phrase, phrase[inner_phrase], False, False)
            if phrase_key == "limit":
                return phrase_text.replace("limit", "", 1).strip().strip("andor").strip("` ,;") + ":"
            else:
                return phrase_text.strip().strip("andor").strip("` ,;") + "; and "
        else:
            if phrase_key in limits_dict:
                end_word = ", or " if is_or else ", and "
                custom_phrase = limits_dict[phrase_key][1] if is_not else limits_dict[phrase_key][0]
                return custom_phrase + phrase.strip().replace("_", " ") + end_word
            elif phrase_key in trigger_bools and phrase in ["yes", "no"]:
                end_word = ", or " if is_or else ", and "
                custom_phrase = trigger_bools[phrase_key][0] if phrase == "yes" else trigger_bools[phrase_key][1]
                return custom_phrase + end_word
            elif phrase_key in flags:
                link_word = " is not [" if is_not else " is ["
                end_word = ", or " if is_or else ", and "
                if phrase_key.startswith("had"):
                    duration_key = [key for key in phrase if key != "flag"][0]
                    flag_page = self.crossref_flag(phrase["flag"].strip())
                    phrase_text = phrase_key.strip().replace("_", " ") + link_word + phrase["flag"].strip()
                    phrase_text += "](" + flag_page + ") for " + phrase[duration_key] + " " + duration_key + end_word
                    return phrase_text
                else:
                    flag_page = self.crossref_flag(phrase.strip())
                    phrase_text = phrase_key.strip().replace("_", " ") + link_word
                    phrase_text += phrase.strip() + "](" + flag_page + ")" + end_word
                    return phrase_text
            else:
                link_word = " is not " if is_not else " is "
                end_word = ", or " if is_or else ", and "
                return phrase_key.strip().replace("_", " ") + link_word + phrase.strip().replace("_", " ") + end_word

    def replace_if_has(self, text):
        text = text.replace("If if", "If")
        text = text.replace("If else if", "Else if")
        text = text.replace("has has", "has")
        text = text.replace("has does not have", "does not have")
        text = text.replace("does not have has", "does not have")
        text = text.replace("has is", "is")
        text = text.replace("does not have is", "does not have")
        return text

    def format_effects(self, effects):
        text = ""
        has_ids = False
        for e_name in effects:
            e_item = effects[e_name]
            if e_name.strip() in effect_dict:
                e_str, e_ids = effect_dict[e_name.strip()]
                for e_id in e_ids:
                    if e_id == "duration":
                        if "duration" not in e_item or int(e_item["duration"]) < 0:
                            e_item[e_id] = "until otherwise removed"
                        elif (int(e_item[e_id]) % 365) == 0:
                            e_item[e_id] = "for " + str(int(int(e_item[e_id]) / 365)) + " years"
                        else:
                            e_item[e_id] = "for " + e_item[e_id] + " days"
                    elif e_id == "id":
                        has_ids = True
                        e_item[e_id] = "\u02FB" + e_item[e_id] + "\u02FC"
                e_parts = [e_item[e_id] for e_id in e_ids]
                text += f"<li>{e_str.format(*e_parts)}</li>"
            elif e_name.strip() in flags and e_name.strip().startswith("had"):
                duration_key = [key for key in e_item if key != "flag"][0]
                flag_page = self.crossref_flag(e_item["flag"])
                text += (f"<li>{e_name.replace('_', ' ').strip()}[{e_item['flag'].strip()}]({flag_page}) for "
                         f"{e_item[duration_key]} {duration_key}</li>")
            elif e_name.strip() in flags:
                flag_page = self.crossref_flag(e_item)
                text += f"<li>{e_name.replace('_', ' ').strip()} [{e_item.strip()}]({flag_page})</li>"
            elif e_name.strip() in ["country_event", "province_event"]:
                duration = " immediately "
                if "random" in e_item:
                    days = e_item["days"] if "days" in e_item else "0"
                    duration = f" in {days} to {e_item['random']} days"
                elif "days" in e_item:
                    duration = f" in {e_item['days']} days"
                id_text = e_item['id'].strip()
                text += f"<li>fire {e_name.replace('_', ' ').strip()} [{id_text}]({id_text}_slug){duration}</li>"
            else:
                if type(e_item) is dict:
                    if "limit" in e_item:
                        conditions_text = self.format_limit_phrase("limit", e_item["limit"])
                        if e_name.strip() == "IF":
                            conditions_text = "If " + self.replace_if_has(conditions_text)
                        else:
                            conditions_text = "If " + e_name.strip().replace("_", " ") + " " + conditions_text
                            conditions_text = self.replace_if_has(conditions_text)
                        e_item.pop("limit")
                        recurse_text, recurse_ids = self.format_effects(e_item)
                        has_ids = has_ids or recurse_ids
                        text += f"<li>{conditions_text}</li><ul>{recurse_text}</ul>"
                    else:
                        recurse_text, recurse_ids = self.format_effects(e_item)
                        has_ids = has_ids or recurse_ids
                        text += f"<li>{e_name.replace('_', ' ').strip()}:</li><ul>{recurse_text}</ul>"
                elif type(e_item) is str:
                    text += f"<li>{e_name.replace('_', ' ').strip()} = {e_item}</li>"
                elif type(e_item) == type(None):
                    text += f"<li>{e_name.replace('_', ' ').strip()}</li>"
                else:
                    raise TypeError(f"Invalid Type {type(e_item)}, should be dict, str or None.")

        return text, has_ids

    def format_mtth(self, mtth_dict):
        mtth_unit = [unit for unit in mtth_dict if unit in ["days", "weeks", "months", "years"]][0]
        mtth_text = "Base time = {0} {1}\n".format(mtth_dict[mtth_unit], mtth_unit)
        modifiers = {key: mtth_dict[key] for key in mtth_dict if key.strip() == "modifier"}
        if len(modifiers) > 0:
            for mod in modifiers:
                mod_dict = {key: modifiers[mod][key] for key in modifiers[mod] if key != "factor"}
                mtth_text += " - Multiplied by " + modifiers[mod]["factor"] + " if "
                mtth_text += self.replace_if_has(self.format_limit_phrase("limit", mod_dict).strip(":")) + "\n"
        return mtth_text

    def format_ai_chance(self, ai_chance_dict):
        ai_chance_text = "AI weights this option at {}\n".format(ai_chance_dict["factor"])
        modifiers = {key: ai_chance_dict[key] for key in ai_chance_dict if key.strip() == "modifier"}
        if len(modifiers) > 0:
            for mod in modifiers:
                mod_dict = {key: modifiers[mod][key] for key in modifiers[mod] if key != "factor"}
                ai_chance_text += " - Multiplied by " + modifiers[mod]["factor"] + " if "
                ai_chance_text += self.replace_if_has(self.format_limit_phrase("limit", mod_dict).strip(":")) + "\n"
        return ai_chance_text

    def format_random_list(self, rand_list):
        list_text = ""
        has_ids = False
        i = 1
        for rand_item in rand_list:
            list_text += "Outcome " + str(i) + ":\n\n"
            i += 1
            outcome = rand_list[rand_item]
            if "trigger" in outcome:
                list_text += "Available if " + self.format_conditions(outcome["trigger"]) + "\n\n"

            modifiers = {key: outcome[key] for key in outcome if key.strip() == "modifier"}
            if len(modifiers) > 0:
                for mod in modifiers:
                    list_text += "The weight of this outcome is " + rand_item + "\n"
                    mod_dict = {key: modifiers[mod][key] for key in modifiers[mod] if key != "factor"}
                    list_text += " - Multiplied by " + modifiers[mod]["factor"] + " if "
                    list_text += self.replace_if_has(self.format_limit_phrase("limit", mod_dict).strip(":")) + "\n\n"
            else:
                list_text += "The weight of this outcome is 1\n\n"

            effects = {key: outcome[key] for key in outcome if key != "trigger" and key not in modifiers}
            effect_text, effect_recurse = self.format_effects(effects)
            has_ids = has_ids or effect_recurse
            list_text += "This outcome causes the following effects:<ul>" + effect_text + "</ul>\n"
        return list_text, has_ids

    def crossref_flag(self, flag):
        flag_dirs = "./wiki/flags/"
        try:
            flag_page_path = flag_dirs + slugify(flag, separator="_") + ".md"
        except TypeError as e:
            print(flag)
            raise e
        if not os.path.exists(flag_page_path):
            with open(flag_page_path, "w") as flag_page:
                flag_page.write("This flag is used in the following pages:\n")
                flag_page.write(" - [" + self.page_name + "](.." + self.page_path[6:] + ")\n")
        else:
            with open(flag_page_path, "r+") as flag_page:
                flag_text = " - [" + self.page_name + "](.." + self.page_path[6:] + ")\n"
                flag_page_text = flag_page.read()
                if flag_text not in flag_page_text:
                    flag_page.write(flag_text)
        return ".." + flag_page_path[6:]
