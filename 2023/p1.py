with open(r"C:\Users\Amaar Chughtai\Desktop\Advent of Code\data.txt", "r") as f:
    x = f.read()
    new_arr = x.split("\n")
    all_nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0, '': 0}

    ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    total = 0
    temp = 0
    first_word_part = ""
    second_word_part = ""

    for i in new_arr:
        max_idx = 0
        min_idx = len(i)

        min_idx2 = len(i)
        max_idx2 = 0

        for j in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
            temp = i.find(j)
            if temp < min_idx and temp != -1:
                min_idx = temp
                first_word_part = j

        for j in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
            temp = i.rfind(j)
            if temp > max_idx and temp != -1:
                max_idx = temp
                second_word_part = j

        for j in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            temp = i.find(j)
            if temp < min_idx2 and temp != -1:
                min_idx2 = temp
                if min_idx2 < min_idx:
                    first_word_part = j

        for j in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            temp = i.rfind(j)
            if temp > max_idx2 and temp != -1:
                max_idx2 = temp
                if max_idx2 > max_idx:
                    second_word_part = j
        try:
            first_word_part = str(all_nums[first_word_part])
        except Exception as e:
            pass
        try:
            second_word_part = str(all_nums[second_word_part])
        except Exception as e:
            pass
        total += int(first_word_part + second_word_part)
print(total)