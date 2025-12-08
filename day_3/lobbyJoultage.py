def lobbyJoultage():
    with open("day3_input.txt", "r") as f:
        banks = f.read().split("\n")
        total = 0 

        for bank in banks:
            max1, max2 = 0,0 
            max1ind, max2ind = -1, -1 
            for i in range(len(bank)):
                if int(bank[i]) > int(max1):
                    max2, max1 = max1, bank[i]
                    max2ind, max1ind = max1ind, i 
                elif int(bank[i]) > int(max2):
                    max2, max2ind = bank[i], i 
            if max2ind > max1ind:
                total += int(max1+max2)
            elif max1ind == len(bank)-1:
                total += int(max2 + max1)
            else:
                maxafter = max(bank[max1ind+1:])
                total += int(max1+maxafter)
        return total

if __name__ == "__main__":
    print(lobbyJoultage())
    