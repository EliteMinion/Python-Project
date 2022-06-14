def preference_input():
    exteriorcolor = ["Obsidian black", "Solid gray", "Patagonia red", "Spectral blue", "Polar white"]
    wheels = ["Cross spoke", "Twin spoke"]
    exteriorextras = ["Carbon lip", "Carbon diffuser", "Small carbon spoiler"]
    interiorcolor = ["Deep white", "Yacht blue", "Classic red", "Leather black", "Siena brown"]
    extras = ["Seat heaters", "AC cooling", "Mini fridge"]

    ext_col = 0
    wheel = 0
    ext_ext = 0
    int_col = 0
    ext = 0

    while ext_col < 1 or ext_col > 6:
        ext_col = int(input("Choose external colour(1-Obsidian black(default);2-Solid gray;3-Patagonian red;4-Spectral blue;5-Polar white;6-skip):"))
    while wheel < 1 or wheel > 3:
        wheel = int(input("Choose wheel spoke type(1-Cross spokes(default);2-Twin spokes;3-skip):"))
    while ext_ext < 1 or ext_ext > 4:
        ext_ext = int(input("Choose exterior extras(1-Carbon lip;2-Carbon diffuser;3-Small carbon spoiler;8-skip):"))
    while int_col < 1 or int_col > 6:
        int_col = int(input("Choose interior colour(1-Deep white;2-Yacht blue;3-Classic red;4-Leather black(default);5-Siena brown;6-skip):"))
    while ext < 1 or ext > 4:
        ext = int(input("Choose extras(1-Seat heaters;2-AC Cooling;3-Mini fridge;8-skip):"))

    if ext_col == 1: exterior_color = exteriorcolor[0]
    if ext_col == 2: exterior_color = exteriorcolor[1]
    if ext_col == 3: exterior_color = exteriorcolor[2]
    if ext_col == 4: exterior_color = exteriorcolor[3]
    if ext_col == 5: exterior_color = exteriorcolor[4]
    if ext_col == 6: exterior_color = exteriorcolor[0]

    if wheel == 1: wheels_type = wheels[0]
    if wheel == 2: wheels_type = wheels[1]
    if wheel == 3: wheels_type = wheels[0]

    if ext_ext == 1: exterior_extras = exteriorextras[0]
    if ext_ext == 2: exterior_extras = exteriorextras[1]
    if ext_ext == 3: exterior_extras = exteriorextras[2]
    if ext_ext == 8: exterior_extras = "None"

    if int_col == 1: interior_color = interiorcolor[0]
    if int_col == 2: interior_color = interiorcolor[1]
    if int_col == 3: interior_color = interiorcolor[2]
    if int_col == 4: interior_color = interiorcolor[3]
    if int_col == 5: interior_color = interiorcolor[4]
    if int_col == 6: interior_color = interiorcolor[3]

    if ext == 1: car_extras = extras[0]
    if ext == 2: car_extras = extras[1]
    if ext == 3: car_extras = extras[2]
    if ext == 8: car_extras = "None"

    final_config = [exterior_color, wheels_type, exterior_extras, interior_color,car_extras]

    return final_config


class car:
    def __init__(self, exterior_color, wheels_type, exterior_extras, interior_color, car_extras):
        self.exterior_color = exterior_color
        self.wheels_type = wheels_type
        self.exterior_extras = exterior_extras
        self.interior_color = interior_color
        self.car_extras = car_extras

    def file_input(self):
        file = open("Car configuration.txt", "w")
        file.write("                     Car configuration")

        file.close()
        file = open("Car configuration.txt", "a")

        file.write("\n")
        file.write("\n")
        file.write("\n")

        file.write("Exterior color:" + self.exterior_color)
        file.write("\n")

        file.write("Wheels type:" + self.wheels_type)
        file.write("\n")

        file.write("Exterior extras" + self.exterior_extras)
        file.write("\n")

        file.write("Interior color:" + self.interior_color)
        file.write("\n")

        file.write("Car extras:" + self.car_extras)
        file.write("\n")

        file.write("\n")
        file.write("Thanks for choosing our services!")

        file.close()
        file_read = open("Car configuration.txt", "r")

        print(file_read)


config_data = preference_input()

car_config = car(config_data[0], config_data[1], config_data[2], config_data[3], config_data[4])

car_config.file_input()

