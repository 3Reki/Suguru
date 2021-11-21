import random
import time
import operator
import utils
import soln_gen_region_formatter as formatter


class Grid:
    def __init__(self, regions, size_x, size_y):
        self.regions = regions
        #utils.print_mat(self.regions)
        self.cell_index = [0, -1]
        self.previous_cell_index = []
        self.mat = [[-1 for i in range(size_x)] for j in range(size_y)]

    def get_next_cell(self):
        self.previous_cell_index.append(list(self.cell_index))
        if self.cell_index[1] + 1 >= len(self.regions[self.cell_index[0]]):
            # Next region
            if self.cell_index[0] + 1 >= len(self.regions):
                # All cells done
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


class Timer:
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.start = time.time()

    def is_over(self):
        return False if self.time_limit is None else time.time() - self.start >= self.time_limit


def choose_number(grid, cell, timer):
    #print(cell)
    if cell is False:
        #print("isok")
        return True

    if timer.is_over():
        return False

    potential_nb = get_allowed_numbers(grid, cell)
    next = grid.get_next_cell()


    while len(potential_nb) > 0:
        choice_index = random.randint(0, len(potential_nb) - 1)
        choice = potential_nb.pop(choice_index)

        grid.mat[cell[1]][cell[0]] = choice
        #utils.print_mat(grid.mat)

        #print(str(cell) + " done: " + str(choice))
        done = choose_number(grid, next, timer)

        if timer.is_over():
            return False

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
    affecting_cells = set(region).union(set(utils.adjacent_diagonal_cells(grid.mat, cell)))
    affecting_nb = set()

    for other_cell in affecting_cells:
        if other_cell == cell:
            continue

        value = grid.mat[other_cell[1]][other_cell[0]]

        if value != -1:
            affecting_nb.add(value)

    potential_nb = potential_nb.difference(affecting_nb)

    return list(potential_nb)

def create_number_grid(regions, size_x, size_y, random_seed = None, time_limit = None, regions_ordered = False):
    # TODO: case prioritaire ?
    r = formatter.sort_regions(regions, (size_x, size_y)) \
        if not regions_ordered \
        else regions
    grid = Grid(r, size_x, size_y)

    random.seed(random_seed)
    if choose_number(grid, grid.get_next_cell(), Timer(time_limit)):
        return grid.mat

    return False


if __name__ == '__main__':
    for i in range(100):
        start = time.time()
        seed = random.randrange(10000)

        print(seed)

        res = create_number_grid(
            [[(3, 0), (3, 1)],
            [(4, 0), (5, 0), (4, 1), (5, 1)],
            [(3, 2), (4, 2), (5, 2), (3, 3), (4, 3), (5, 3)],
            [(5, 4), (5, 5), (5, 6), (5, 7)],
            [(2, 2), (2, 3), (2, 4), (3, 4), (4, 4), (4, 5)],
            [(0, 5), (1, 5), (2, 5), (3, 5)],
            [(0, 6), (1, 6), (0, 7), (1, 7)],
            [(2, 6), (3, 6), (4, 6), (2, 7), (3, 7), (4, 7)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (0, 3), (1, 3), (0, 4), (1, 4)]],
            6, 8, seed, regions_ordered = True)

        print("Done in " + str(time.time() - start) + " seconds")
        if res:
            utils.print_mat(res)
        else:
            print(False)
