def giftShop():
    with open("day2_input.txt", "r") as f:

        ranges = f.read().split(",")
        total = 0 

        for indrange in ranges:
            [start, end] = indrange.split("-")
            if len(start) == len(end):
                if len(start)%2 == 0:
                    for i in range(int(start[:int(len(start)/2)]), int(end[int(len(end)/2)])):
                        print(start, end, i)

if __name__ == "__main__":
    giftShop()
