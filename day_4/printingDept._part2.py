def printingDept():
    with open("day4_input.txt", "r") as f:
        grid = f.read().splitlines()
        total = 0 
        directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [-1,-1], [1,-1], [-1,1]]

        while True:
            
            cur_total = 0
            modifiable = []
            for row in range(len(grid)):
                for column in range(len(grid[0])):
                    ind_count = 0 
                    if grid[row][column] == "@":
                        for i in directions:
                            adj_row, adj_col = row + i[0], column + i[1]
                            
                            if (adj_row >= 0 and adj_col >= 0 and adj_row < len(grid) and adj_col < len(grid[0])):
                                if grid[adj_row][adj_col] == "@":
                                    ind_count += 1 
                        if ind_count <4:
                            cur_total += 1
                            modifiable.append((row, column))
            if cur_total == 0:
                break 
            for i in modifiable:
                grid[i[0]] = grid[i[0]][:i[1]] + "." + grid[i[0]][i[1]+1:]
            total += cur_total
            
        return total

if __name__ == "__main__":
    print(printingDept())
    