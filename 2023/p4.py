with open(r"C:\Users\Amaar Chughtai\Desktop\USACO\data.txt", "r") as f:
    cards = []
    for i in f.read().splitlines():
        temp = [int(i.split(":")[0].split(" ")[-1])]
        nums = i.split(":")[1].strip().split("|")[0].strip().split(" ")
        for j in i.split(":")[1].strip().split("|")[1].strip().split(" "):
            if j!="":
                if j in nums:
                    temp.append(temp[-1]+1)
        count = cards.count(temp[0]) + 1
        cards.append(temp[0])
        for j in range(1,len(temp)):
            for r in range(count):
                cards.append(temp[j])
        
        
    print(len(cards))