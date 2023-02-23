import shelve
import os


def run():
    with shelve.open("all_localisations", writeback=True) as loc:
        all_files = [f for f in os.listdir("./content/localisation/")]
        for file_name in all_files:
            with open("./content/localisation/" + file_name, "r", encoding='utf-8-sig') as file:
                for line in file:
                    line = line.split("#")[0].strip()
                    if line == "" or line == "l_english:":
                        continue
                    key_val = line.split(" ", 1)
                    try:
                        key = key_val[0]
                        val = key_val[1]
                        key = key.split(":")[0]
                        loc[key] = val
                    except IndexError:
                        print(file_name, line)
            loc.sync()


run()
