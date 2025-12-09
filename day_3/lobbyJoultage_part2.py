import heapq
def lobbyJoultage():
    #with open("day3_input.txt", "r") as f:
    with open("sample.txt", "r") as f:
        banks = f.read().split("\n")
        total = 0 

        for bank in banks:
            #putting 1 to 12 in heap 
            heap = []
            for i in range(1, 13):
                heapq.heappush(heap, [int(bank[-i]), len(bank)-i]) 
            heapq.heapify(heap)
            print(heap)

            biggest = int(bank[-i])
            for i in range(len(bank)-13, -1, -1):
                if (int(bank[i]) > heap[0][0]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, int(bank[i]))
                    heapq.heapify(heap)
                    biggest = int(bank[i]) 
            print(heap)
        return total

if __name__ == "__main__":
    print(lobbyJoultage())
    