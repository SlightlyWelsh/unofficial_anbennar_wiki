import defaults
from dictionaries import mission_req_exceptions
import shelve


class MissionPage(defaults.Page):
    directory = "./wiki/missions/"

    def __init__(self, page_name):
        super().__init__(page_name)

        self.nation = " ".join(self.page_name.split("_")[:-1])
        self.nation_page = "_".join(self.page_name.split("_")[:-1]) + ".md"

        filename = "./content/missions/" + self.page_name + ".txt"
        self.mission_dict = self.read_file(filename)
        self.mission_titles = {}
        self.mission_descs = {}
        self.mission_tips = {}
        with shelve.open("all_localisations") as loc:
            for tree in self.mission_dict:
                for mission in self.mission_dict[tree]:
                    mission_dict_curr = self.mission_dict[tree][mission]
                    if type(mission_dict_curr) is dict and mission not in ["potential_on_load", "potential"]:
                        try:
                            self.mission_titles[mission] = loc[mission + "_title"].strip('"')
                        except KeyError:
                            print("Missing localisation: " + mission + "_title")
                            self.mission_titles[mission] = "Missing localisation: " + mission + "_title"
                        try:
                            self.mission_descs[mission] = loc[mission + "_desc"].strip('"')
                        except KeyError:
                            print("Missing localisation: " + mission + "_desc")
                            self.mission_descs[mission] = "Missing localisation: " + mission + "_desc"
                        if "effect" in mission_dict_curr:
                            tt_key = "custom_tooltip"
                            while tt_key in mission_dict_curr["effect"]:
                                unloc_tip = mission_dict_curr["effect"][tt_key]
                                try:
                                    self.mission_tips[unloc_tip] = loc[unloc_tip].strip('"')
                                except KeyError:
                                    print("Missing localisation: " + unloc_tip)
                                    self.mission_tips[unloc_tip] = "Missing localisation: " + unloc_tip
                                tt_key += " "

    def create(self):
        super().create()
        has_ids = False
        with open(self.page_path, "a", encoding="utf-8") as page:
            page.write("This is a list of all [missions](missions.md) of [{0}]({1})\n".format(
                self.nation, self.nation_page
            ))
            for tree in self.mission_dict:
                page.write("\n| Mission | Completion requirements | Effects | Prerequisites |\n"
                           "| ----- | ------ | ----- | ------ |\n")
                for mission in self.mission_dict[tree]:
                    mission_dict = self.mission_dict[tree][mission]
                    if type(mission_dict) is dict:
                        if mission in ["potential_on_load", "potential"]:
                            continue

                        requirements_txt = ""
                        if "trigger" in mission_dict:
                            requirements_txt = self.format_conditions(mission_dict["trigger"])

                        prerequisites_txt = ""
                        if "required_missions" in mission_dict:
                            for req in mission_dict["required_missions"]:
                                if req in mission_req_exceptions:
                                    prerequisites_txt += mission_req_exceptions[req]
                                else:
                                    try:
                                        req_title = self.mission_titles[req]
                                        prerequisites_txt += "[" + req_title + "](#" + req + ")<br />"
                                    except KeyError:
                                        prerequisites_txt += req.replace("_", " ") + "<br />"

                        effects_txt = ""
                        if "effect" in mission_dict:
                            effects_txt, effects_ids = self.format_effects(mission_dict["effect"])
                            has_ids = has_ids or effects_ids
                            for tt in self.mission_tips:
                                effects_txt.replace(tt, self.mission_tips[tt])

                        page.write(
                            "| <a name=\"" + mission + "\">" + self.mission_titles[mission] + "</a><br />*" +
                            self.mission_descs[mission] + "* | " + requirements_txt +
                            " | " + effects_txt + " | " + prerequisites_txt + " |\n")
        return self.page_path, has_ids
