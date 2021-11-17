import random
import time
import Utils as utils
import SolutionGenerator as tester

class Grid:

    def __init__(self, size_x, size_y, max_region_size):
        self.max_region_size = max_region_size
        self.mat = [[-1 for i in range(size_x)] for i in range(size_y)]
        self.regions = []
        self.region_count = 0
        self.empty_cells_count = size_x * size_y

    def set_cell_region(self, cell, region_number):
        self.mat[cell[1]][cell[0]] = region_number
        self.regions[region_number - 1].add_cell(cell)
        self.empty_cells_count -= 1

    def get_cell_region(self, cell):
        return self.mat[cell[1]][cell[0]]

    def get_sixe_x(self):
        return len(self.mat[0])

    def get_sixe_y(self):
        return len(self.mat)

    def is_full(self):
        return self.empty_cells_count == 0

    def is_cell_set(self, cell):
        return self.mat[cell[1]][cell[0]] != -1

    def new_region(self):
        self.region_count += 1
        self.regions.append(Region(self.region_count))
        return self.regions[self.region_count - 1]



class Region:

    def __init__(self, number):
        self.number = number
        self.cells = []
        self.cell_count = 0

    def add_cell(self, cell):
        self.cells.append(cell)
        self.cell_count += 1


"""
# TODO: Chance de stopper region (1/12, 1/9, 1/6, 1/4), privilégier case isolées
et repartir des cases isolées
"""
def create_grid(size_x = 5, size_y = 7, max_region_size = 5):
    grid = Grid(size_x, size_y, max_region_size)

    populate_grid(grid, get_random_cell(grid), grid.new_region())

    return grid


def populate_grid(grid, cell, region):
    #print(cell)
    grid.set_cell_region(cell, region.number)

    if grid.is_full():
        return

    next = get_next_cell(grid, cell, region)
    next_cell = next[0]

    if next[1]:
        next_region = grid.new_region()
        #print(next_region.number)
    else:
        next_region = region

    populate_grid(grid, next_cell, next_region)


"""
Returns a cell and True if a change of region must be done
"""
def get_next_cell(grid, cell, region):
    if region.cell_count >= grid.max_region_size:
        return (get_random_cell(grid), True)
    poss_cells = utils.adjacent_cells(grid.mat, cell)

    for i in range(len(poss_cells) - 1, -1, -1):
        if grid.is_cell_set(poss_cells[i]):
            poss_cells.pop(i)

    if len(poss_cells) == 0:
        return (get_random_cell(grid), True)

    return (random.choice(poss_cells), False)


def get_random_cell(grid):
    cell_nbr = random.randint(1, grid.empty_cells_count)
    size_x = grid.get_sixe_x()
    i = 0

    while i < cell_nbr:
        cell = (i % size_x, i // size_x)

        if grid.get_cell_region(cell) != -1:
            cell_nbr += 1

            if cell_nbr > len(grid.mat[0]) * len(grid.mat):
                print("cell_nbr to high")

        i += 1

    #print(cell)
    return cell

def test_generator(nb_attempts = 100):
    start = time.time()
    ok_count = 0
    regions = []

    for i in range(nb_attempts):
        res = create_grid()
        seed = random.randrange(10000)
        regions.clear()

        for region in res.regions:
            regions.append(region.cells)

        sg_start = time.time()
        test = tester.create_number_grid(regions, res.get_sixe_x(), res.get_sixe_y(), seed)

        sg_length = time.time() - sg_start
        if sg_length > 10:
            print("Grid took " + str(sg_length) + "s to complete, result=" + str(test != False))
            print(regions, seed)

        if test != False:
            ok_count += 1

        print(ok_count, i)


    print("Valid grids : " + str(ok_count) + "/" + str(nb_attempts))
    print("Done in " + str(time.time() - start) + " seconds")



if __name__ == '__main__':
    test_generator()
