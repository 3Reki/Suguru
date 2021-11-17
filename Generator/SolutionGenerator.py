import random
import time
import operator

class Grid:

    def __init__(self, regions, size_x, size_y):
        self.regions = sort_regions(regions)
        self.cell_index = [0, -1]
        self.previous_cell_index = []
        self.mat = [[-1 for i in range(size_x)] for j in range(size_y)]

    def get_next_cell(self):
        self.previous_cell_index.append(list(self.cell_index))
        if self.cell_index[1] + 1 >= len(self.regions[self.cell_index[0]]):
            if self.cell_index[0] + 1 >= len(self.regions):
                return False

            self.cell_index[0] += 1
            self.cell_index[1] = 0
        else:
            self.cell_index[1] += 1

        return self.regions[self.cell_index[0]][self.cell_index[1]]

    def revert_cell(self):
        self.cell_index = self.previous_cell_index.pop()

    def get_region(self):
        return list(self.regions[self.cell_index[0]])

def choose_number(grid, cell):
    #print(cell)
    if cell is False:
        #print("isok")
        return True

    potential_nb = get_allowed_numbers(grid, cell)
    next = grid.get_next_cell()


    while len(potential_nb) > 0:
        choice_index = random.randint(0, len(potential_nb) - 1)
        choice = potential_nb.pop(choice_index)

        grid.mat[cell[1]][cell[0]] = choice
        #print(mat)

        #print(str(cell) + " done: " + str(choice))
        done = choose_number(grid, next)

        if done:
            return True

    #print("ah shit stop : " + str(cell))
    grid.mat[cell[1]][cell[0]] = -1
    #print(mat)
    grid.revert_cell()
    return False

def get_allowed_numbers(grid, cell):
    region = grid.get_region()
    potential_nb = set([i for i in range(1, len(region) + 1)])
    region.remove(cell)
    affecting_cells = set(region)
    affecting_nb = set()

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i, j) == (0, 0):
                continue

            cell_x = cell[0] + i
            cell_y = cell[1] + j

            if cell_y > -1 and cell_x > -1 and cell_y < len(grid.mat) and cell_x < len(grid.mat[cell_y]):
                affecting_cells.add((cell_x, cell_y))


    for other_cell in affecting_cells:
        if other_cell == cell:
            continue

        value = grid.mat[other_cell[1]][other_cell[0]]

        if value != -1:
            affecting_nb.add(value)

    potential_nb = potential_nb.difference(affecting_nb)

    return list(potential_nb)

def sort_regions(r):
    lst = []
    for region in r:
        lst.append(sorted(region, key=operator.itemgetter(1, 0)))

    return sorted(lst, key=lambda r: (len(r), r[0][1], r[0][0]))

def create_number_grid(r, size_x, size_y, random_seed = None):
    # TODO: case prioritaire ?
    grid = Grid(r, size_x, size_y)

    random.seed(random_seed)
    if choose_number(grid, grid.get_next_cell()):
        return grid.mat

    return False


if __name__ == '__main__':
    start = time.time()
    create_number_grid([
        [(1, 3)],
        [(4, 0), (5, 0)],
        [(6, 0), (6, 1), (6, 2)],
        [(3, 1), (2, 2), (3, 2), (3, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1)],
        [(0, 1), (1, 1), (0, 2), (1, 2), (0, 3)],
        [(4, 1), (5, 1), (4, 2), (5, 2), (4, 3)],
        [(2, 3), (0, 4), (1, 4), (2, 4), (3, 4)],
        [(5, 3), (6, 3), (4, 4), (5, 4), (6, 4)]
    ], 7, 5)

    print("Done in " + str(time.time() - start) + " seconds")
