import missions
import events
import decisions
import os
import re
import pickle

if __name__ == '__main__':
    with open("event_ids.txt", "rb") as event_file:
        event_file_dict = pickle.load(event_file)
    with open("save_file.txt", "r") as save_file:
        save = save_file.read()
    with open("id_files.txt", "rb") as id_file:
        files_with_ids = pickle.load(id_file)
    if save.startswith("event"):
        counter = int(save[5:])
        i = 0
        event_files = [f[:-4] for f in os.listdir("./content/events/")
                       if os.path.isfile(os.path.join("./content/events/", f))]
        for file in event_files:
            if i < counter:
                i += 1
                continue
            try:
                _ev_dict = events.EventFile(file).create()
            except Exception as e:
                with open("save_file.txt", "w") as save_file:
                    save_file.write(f"event{i}")
                with open("id_files.txt", "wb") as id_file:
                    pickle.dump(files_with_ids, id_file)
                with open("event_ids.txt", "wb") as event_file:
                    pickle.dump(event_file_dict, event_file)
                raise e
            for _id in _ev_dict:
                _path, _title, _has_ids = _ev_dict[_id]
                event_file_dict[_id] = (_path, _title)
                if _has_ids:
                    files_with_ids.append(_path)
            print("Finished " + file)
            i += 1
        save = "mission0"
        with open("id_files.txt", "wb") as id_file:
            pickle.dump(files_with_ids, id_file)
        with open("event_ids.txt", "wb") as event_file:
            pickle.dump(event_file_dict, event_file)

    if save.startswith("mission"):
        counter = int(save[7:])
        i = 0
        mission_files = [f[:-4] for f in os.listdir("./content/missions/")
                         if os.path.isfile(os.path.join("./content/missions/", f))]
        for file in mission_files:
            if i < counter:
                i += 1
                continue
            try:
                _path, _has_ids = missions.MissionPage(file).create()
            except Exception as e:
                with open("save_file.txt", "w") as save_file:
                    save_file.write(f"mission{i}")
                with open("id_files.txt", "wb") as id_file:
                    pickle.dump(files_with_ids, id_file)
                raise e
            if _has_ids:
                files_with_ids.append(_path)
            print("Finished " + file)
            i += 1
        save = "decision0"
        with open("id_files.txt", "wb") as id_file:
            pickle.dump(files_with_ids, id_file)

    if save.startswith("decision"):
        counter = int(save[8:])
        i = 0
        decision_files = [f[:-4] for f in os.listdir("./content/decisions/")
                          if os.path.isfile(os.path.join("./content/decisions/", f))]
        for file in decision_files:
            if i < counter:
                i += 1
                continue
            try:
                _path, _has_ids = decisions.DecisionPage(file).create()
            except Exception as e:
                with open("save_file.txt", "w") as save_file:
                    save_file.write(f"decision{i}")
                with open("id_files.txt", "wb") as id_file:
                    pickle.dump(files_with_ids, id_file)
                raise e
            if _has_ids:
                files_with_ids.append(_path)
            print("Finished " + file)
            i += 1
        save = "crosslink0"
        with open("id_files.txt", "wb") as id_file:
            pickle.dump(files_with_ids, id_file)

    if save.startswith("crosslink"):
        files_with_ids = [*set(files_with_ids)]
        counter = int(save[9:])
        i = 0
        for file in files_with_ids:
            if i < counter:
                i += 1
                continue
            try:
                with open(file, "r", encoding="utf-8") as o_file:
                    f_text = o_file.read()
                ev_id_matches = re.finditer("(\u02FB([^\u02FC]*)\u02FC)", f_text)
                ev_ids = list(reversed([i for i in ev_id_matches]))
                for ev_id in ev_ids:
                    if ev_id.group(2).split(".")[0] == "patrons_events":
                        ev_path, ev_name = event_file_dict[f'castonath_patricians_events.{ev_id.group(2).split(".")[1]}']
                    try:
                        ev_path, ev_name = event_file_dict[ev_id.group(2)]
                    except KeyError:
                        ev_path, ev_name = event_file_dict[f'"{ev_id.group(2)}"']
                    f_text = f_text[0:ev_id.start(0)] + "[" + ev_name + "](.." + ev_path[6:] + ")" + f_text[ev_id.end(0):]
                with open(file, "w", encoding="utf-8") as o_file:
                    o_file.write(f_text)
            except Exception as e:
                with open("save_file.txt", "w") as save_file:
                    save_file.write(f"crosslink{i}")
                raise e
            i += 1
