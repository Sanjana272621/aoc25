def cafeteria():
    with open("day5_input.txt", "r") as f:
        input_list = f.read().splitlines()
        fresh_count = 0
        fresh_end, id_beg = 0, 0
        
        for i in range(len(input_list)):
            if input_list[i] == "":
                fresh_end = i
                id_beg = i + 1

        fresh = input_list[:fresh_end]
        available = input_list[id_beg:]

        for i in fresh:
            print(i)
        print(available)
        return fresh_count
    

if __name__ == "__main__":
    print(cafeteria())
    