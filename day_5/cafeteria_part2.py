def cafeteria():
    with open("day5_input.txt", "r") as f:
        input_list = f.read().splitlines()
        new_list = []
        fresh_count = 0 

        range_list = []
        end_flag = False 

        for x in input_list:
            if x == "":
                end_flag = True 
                continue
            if not(end_flag):
                x = x.split("-")
                range_list.append([min(int(x[0]), int(x[1])), max(int(x[0]), int(x[1]))]) 
            else:
                new_list.append(int(x))
            
        range_list.sort() 

        range_list.sort(key=lambda x: int(x[0]))
        merged = [range_list[0]]

        for start, end in range_list[1:]:
            if int(start) <= int(merged[-1][1]) + 1:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        for start, end in merged:
            fresh_count += (end - start)+1

        return fresh_count

if __name__ == "__main__":
    print(cafeteria())
    