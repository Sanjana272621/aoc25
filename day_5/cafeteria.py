def cafeteria():
    with open("day5_input.txt", "r") as f:
    #with open("sample.txt", "r") as f:
        input_list = f.read().splitlines()
        fresh_count = 0
        fresh_end, id_beg = 0, 0
        
        for i in range(len(input_list)):
            if input_list[i] == "":
                fresh_end = i
                id_beg = i + 1

        fresh = input_list[:fresh_end]
        available = input_list[id_beg:]

        for id in available:
            break_all = False 
            for i in fresh:
                start, end = i.split("-")
                if int(id) in range(int(start), int(end)+1):
                    fresh_count += 1 
                    break_all = True 
                    break 
                
                if break_all:
                    break
        
        return fresh_count

if __name__ == "__main__":
    print(cafeteria())
    