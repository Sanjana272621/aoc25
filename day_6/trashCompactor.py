def trashCompactor():
    with open("day6_input.txt", "r") as f:
        input_list = f.read().splitlines()
        input_list = [x.split() for x in input_list]
        total = 0
        
        for col in range(len(input_list[0])):
            oper = input_list[-1][col]
            col_total = 0 if oper == "+" else 1

            for row in range(len(input_list)-1):
                if oper == "+":
                    col_total += int(input_list[row][col])
                else:
                    col_total *= int(input_list[row][col]) 
            total += col_total

        return total

if __name__ == "__main__":
    print(trashCompactor())
    