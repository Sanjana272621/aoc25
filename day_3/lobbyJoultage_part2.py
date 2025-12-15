def lobbyJoultage():
    with open("day3_input.txt", "r") as f:
        banks = f.read().splitlines()

    K = 12
    total = 0

    for bank in banks:
        stack = []
        to_remove = len(bank) - K  

        for ch in bank:
            while stack and to_remove > 0 and stack[-1] < ch:
                stack.pop()
                to_remove -= 1

            stack.append(ch)

        best = int("".join(stack[:K]))
        total += best

    return total


if __name__ == "__main__":
    print(lobbyJoultage())
