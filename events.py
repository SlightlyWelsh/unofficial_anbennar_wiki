import defaults
import shelve
from slugify import slugify


class EventFile(defaults.Page):
    def __init__(self, page_name):
        super().__init__(page_name)
        file_name = "./content/events/" + page_name + ".txt"
        self.events_dict = self.read_file(file_name)

    def create(self):
        return_dict = {}
        for event in self.events_dict:
            if type(self.events_dict[event]) is dict:
                _id, _path, _title, _has_ids = EventPage(self.events_dict[event]).create()
                return_dict[_id] = (_path, _title, _has_ids)
        return return_dict


class EventPage(defaults.Page):
    directory = "./wiki/events/"

    def __init__(self, event_dict):
        self.event_title = ""
        self.event_desc = ""
        self.option_names = {}
        self.event_dict = event_dict

        with shelve.open("all_localisations") as loc:
            title_id = event_dict["title"].strip('"')
            try:
                self.event_title = loc[title_id].strip('"')
            except KeyError:
                print("Missing localisation: " + title_id)
                self.event_title = "Missing localisation: " + title_id.replace(".", "_")

            desc_id = event_dict["title"].strip('"')
            try:
                self.event_desc = loc[desc_id].strip('"')
            except KeyError:
                print("Missing localisation: " + desc_id)
                self.event_title = "Missing localisation: " + desc_id.replace(".", "_")

            for option in event_dict:
                if option.strip() == "option":
                    if "name" in event_dict[option]:
                        op_id = event_dict[option]["name"].strip('"')
                        try:
                            self.option_names[op_id] = loc[op_id].strip('"')
                        except KeyError:
                            print("Missing localisation: " + op_id)
                            self.option_names[op_id] = "Missing localisation: " + op_id.replace(".", "_")
                    else:
                        op_id = "Unnamed Option"
                        while op_id in self.option_names:
                            if op_id.endswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
                                op_id = op_id.split("_")[0] + "_" + str(int(op_id.split("_")[1]) + 1)
                            else:
                                op_id = "Unnamed Option_1"
                        event_dict[option]["name"] = op_id
                        self.option_names[op_id] = op_id

        page_name = slugify(self.event_title.strip(), separator="_")
        super().__init__(page_name)

    def create(self):
        super().create()
        has_ids = False
        with open(self.page_path, "a", encoding="utf-8") as page:
            page.write("#Information\n - Title: {}\n - ID: {}\n".format(self.event_title, self.event_dict["id"]))
            page.write("#Description\n" + self.event_desc + "\n")

            if "mean_time_to_happen" in self.event_dict:
                page.write("#Mean Time to Happen:\n" +
                           self.format_mtth(self.event_dict["mean_time_to_happen"]) + "\n")

            page.write("#Options\n")
            for option in self.event_dict:
                if option.strip() == "option":
                    option_dict = self.event_dict[option]
                    page.write("\n___\n##" + self.option_names[option_dict["name"].strip('"')] + "\n")

                    if "trigger" in option_dict:
                        page.write("\n###Available if:\n" + self.format_conditions(option_dict["trigger"]) + "\n")

                    if "ai_chance" in option_dict:
                        page.write("\n###AI weighting:\n" + self.format_ai_chance(option_dict["ai_chance"]) + "\n")

                    if "random_list" in option_dict:
                        list_text, list_ids = self.format_random_list(option_dict["random_list"])
                        has_ids = has_ids or list_ids
                        page.write("\n###One of the following randomly happens:\n" + list_text)

                    effects_dict = {key: option_dict[key] for key in option_dict if key.strip() not in [
                        "name", "trigger", "ai_chance", "random_list"]}
                    if len(effects_dict) > 0:
                        effect_text, effect_ids = self.format_effects(effects_dict)
                        has_ids = has_ids or effect_ids
                        page.write("\n###Efects:<ul>" + effect_text + "</ul>\n")
        return self.event_dict["id"], self.page_path, self.event_title, has_ids
