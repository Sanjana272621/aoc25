def secretEntrance_part2():
    with open("day1_input.txt", "r") as f:
        position = 50
        count = 0

        for instruction in f:
            oldpos = position
            if instruction[0] == "L":
                count += int(instruction[1:])//100
                position -= int(instruction[1:])%100
                
                if (oldpos - int(instruction[1:])%100) <= 0 and oldpos!=0:
                    count += 1
            else: 
                count += int(instruction[1:])//100
                position += int(instruction[1:])
                
                if (oldpos + int(instruction[1:])%100) >= 100 :
                    count += 1
            position %= 100
            
        return(count)

if __name__ == "__main__":
    print(secretEntrance_part2())
