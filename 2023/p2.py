with open(r"C:\Users\Amaar Chughtai\Desktop\Advent of Code\data.txt", "r") as f:
    new_arr = f.read().split("\n")

    total = 0
    for line in new_arr:
        max_r = 0
        max_g = 0
        max_b = 0

        game_data = line.split(" ")
        game_id = game_data[1][0:game_data[1].index(":")]
        cubes = line[len(game_id) + 7:].split(";")

        for subset in cubes:
            if "," in subset:
                subset = subset.split(",")
            else:
                subset = [subset]

            count_r = count_g = count_b = 0
            for cube in subset:
                if "blue" in cube:
                    count_b = int(cube[0:cube.index("b")].strip())
                elif "red" in cube:
                    count_r = int(cube[0:cube.index("r")].strip())
                elif "green" in cube:
                    count_g = int(cube[0:cube.index("g")].strip())

            max_r = max(max_r, count_r)
            max_g = max(max_g, count_g)
            max_b = max(max_b, count_b)

        total += max_r * max_g * max_b

    print(total)
