def giftShop():
    with open("day2_input.txt", "r") as f:

        ranges = f.read().split(",")
        total = 0 

        for indrange in ranges:
            [start, end] = indrange.split("-")
            start = int(start)
            end = int(end)
            for i in range(start, end+1):
                if len(str(i))%2 == 0:
                    if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
                        total += i
        return total

if __name__ == "__main__":
    print(giftShop())
