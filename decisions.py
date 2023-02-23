import defaults
from dictionaries import mission_req_exceptions
import shelve
import re


class DecisionPage(defaults.Page):
    directory = "./wiki/decisions/"

    def __init__(self, page_name):
        super().__init__(page_name)

        filename = "./content/decisions/" + self.page_name + ".txt"
        self.decision_dict = self.read_file(filename)
        self.decision_titles = {}
        self.decision_descs = {}
        self.decision_tips = {}

        self.page_name = re.sub(r'(?<!^)(?=[A-Z])', '_', page_name)
        if not self.page_name.endswith("Decisions"):
            self.page_name += "_Decisions"
        self.page_path = self.directory + self.page_name + ".md"

        with shelve.open("all_localisations") as loc:
            for tree in self.decision_dict:
                for decision in self.decision_dict[tree]:
                    decision_dict_curr = self.decision_dict[tree][decision]
                    if type(decision_dict_curr) is dict:
                        try:
                            self.decision_titles[decision] = loc[decision + "_title"].strip('"')
                        except KeyError:
                            print("Missing localisation: " + decision + "_desc")
                            self.decision_titles[decision] = "Missing localisation: " + decision + "_title"

                        try:
                            self.decision_descs[decision] = loc[decision + "_desc"].strip('"')
                        except KeyError:
                            print("Missing localisation: " + decision + "_desc")
                            self.decision_descs[decision] = "Missing localisation: " + decision + "_desc"

                        if "effect" in decision_dict_curr:
                            tt_key = "custom_tooltip"
                            while tt_key in decision_dict_curr["effect"]:
                                unloc_tip = decision_dict_curr["effect"][tt_key]
                                try:
                                    self.decision_tips[unloc_tip] = loc[unloc_tip].strip('"')
                                except KeyError:
                                    print("Missing localisation: " + unloc_tip)
                                    self.decision_tips[unloc_tip] = "Missing localisation: " + unloc_tip
                                tt_key += " "

    def create(self):
        super().create()
        has_ids = False
        with open(self.page_path, "a", encoding="utf-8") as page:
            page.write("This is a list of all [decisions](decisions.md) in the category \"{0}\"\n".format(
                self.page_name
            ))
            for tree in self.decision_dict:
                page.write("\n| Decision | Completion requirements | Effects | Requirements to appear |\n"
                           "| ----- | ------ | ----- | ------ |\n")
                for decision in self.decision_dict[tree]:
                    decision_dict = self.decision_dict[tree][decision]
                    if type(decision_dict) is dict:
                        if decision in ["potential_on_load", "potential"]:
                            continue

                        requirements_txt = ""
                        if "allow" in decision_dict:
                            requirements_txt = self.format_conditions(decision_dict["allow"])

                        prerequisites_txt = ""
                        if "potential" in decision_dict:
                            prerequisites_txt = self.format_conditions(decision_dict["potential"])

                        effects_txt = ""
                        if "effect" in decision_dict:
                            effects_txt, effects_ids = self.format_effects(decision_dict["effect"])
                            has_ids = has_ids or effects_ids
                            for tt in self.decision_tips:
                                effects_txt = effects_txt.replace(tt, self.decision_tips[tt])

                        page.write(
                            "| <a name=\"" + decision + "\">" + self.decision_titles[decision] + "</a><br />*" +
                            self.decision_descs[decision] + "* | " + requirements_txt +
                            " | " + effects_txt + " | " + prerequisites_txt + " |\n")
        print("Finished " + self.page_name)
        return self.page_path, has_ids
