with open(r"C:\Users\Amaar Chughtai\Desktop\AOSGit\data.txt", "r") as f:
    new_arr = f.read().splitlines()
    value = 0
    for i in new_arr:
        total = []
        nums_int = [int(i) for i in i.split(" ")]
        total.append(nums_int)
        while(True):
            diff = []
            for j in range(0,len(nums_int)-1):
                diff.append(nums_int[j+1]-nums_int[j])
            total.append(diff)
            if not any(diff): 
                break
            nums_int = diff
        value += sum([i[-1] for i in total])
    print(value)
        
              