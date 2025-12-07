def giftShop():
    with open("day2_input.txt", "r") as f:

        ranges = f.read().split(",")
        total = 0 

        for indrange in ranges:
            [start, end] = indrange.split("-")
            start = int(start)
            end = int(end)
            for i in range(start, end+1):
                for j in range(len(str(i))//2):
                    if i == int(str(i)[:j+1]*(len(str(i))//(j+1))):
                        total += i
                        break
        return total

if __name__ == "__main__":
    print(giftShop())