def secretEntrance():
    with open("day1_input.txt", "r") as f:

        position = 50
        count = 0

        for instruction in f:
            if instruction[0] == "L":
                position -= int(instruction[1:])%100
            else:
                position += int(instruction[1:])
            position %= 100
            if position == 0:
                count += 1

        return(count)

if __name__ == "__main__":
    print(secretEntrance())
    print(-60%100)
