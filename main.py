import json
import cities
import weather_static


class Main:
    save = {}
    cities_obj = []
    settings_obj = []
    save_file = "save.json"

    def __init__(self):
        self.save["cities"] = []
        self.save = self.load_save()
        for item in self.save["cities"]:
            self.cities_obj.append(cities.City(item["name"], item["country"]))

        if not self.save["settings"]:
            self.initialize_settings()
        # else:
        #     for item in self.save["settings"]:
        #         self.settings_obj.append(settings.Setting(item, self.save["settings"][item]))
        #     for item in self.settings_obj:
        #         if item.name == "dev":
        #             if item.value:
        print(self.save["settings"])

    def initialize_settings(self):
        # self.settings_obj.append(settings.Setting("default_code", "DE"))
        # self.settings_obj.append(settings.Setting("dev", False))
        self.save["settings"] = {
            "dev": False,
            "default_country": "DE"
        }

    def load_save(self):
        try:
            save = open(self.save_file)
            return json.load(save)
        except IOError:
            print("No save found")
            self.initialize_settings()
            return self.save

    def add_city(self, name, country_code):
        city = weather_static.query_city(name, country_code)
        if city != 0:
            self.cities_obj.append(city)
            self.save["cities"].append({
                "name": city.name,
                "country": city.country_code
            })
        else:
            print("No city found")

    def remove_city(self, index):
        self.cities_obj.remove(self.cities_obj[index])
        self.save["cities"].remove(self.save["cities"][index])

    def save_event(self):
        # print(self.cities_list)
        with open(self.save_file, "w") as f:
            json.dump(self.save, f)
            f.close()
        quit()
