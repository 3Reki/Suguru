import sys
import random
import time
import utils

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
        value = self.mat[cell[1]][cell[0]]
        return self.regions[value-1] if value != -1 else None

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

    def reset(self):
        size = (self.get_sixe_x(), self.get_sixe_y())
        self.mat = [[-1 for i in range(size[0])] for i in range(size[1])]
        self.regions = []
        self.region_count = 0
        self.empty_cells_count = size[0] * size[1]



class Region:

    def __init__(self, number):
        self.number = number
        self.cells = []
        self.cell_count = 0

    def add_cell(self, cell):
        self.cells.append(cell)
        self.cell_count += 1


def create_grid(size_x = 5, size_y = 7, max_region_size = 5):
    grid = Grid(size_x, size_y, max_region_size)

    cell = get_random_cell(grid)
    neighbors = set(utils.adjacent_diagonal_cells(grid.mat, cell))

    while populate_grid(grid, cell, grid.new_region(), neighbors, 0) is False:
        grid.reset()
        #print("reset")

    return grid


def populate_grid(grid, cell, region, region_neighbors, r_min_size):
    #print(cell)
    grid.set_cell_region(cell, region.number)

    cell_neighbors = utils.adjacent_diagonal_cells(grid.mat, cell)
    region_neighbors = region_neighbors.intersection(cell_neighbors)

    if r_min_size < grid.max_region_size:
        r_min_size = get_region_minimum_size(grid, cell, r_min_size, cell_neighbors)

    if grid.is_full():
        return is_region_valid(grid, region, region_neighbors, r_min_size)

    next = get_next_cell(grid, cell, region)
    next_cell = next[0]

    if next[1]:
        if not is_region_valid(grid, region, region_neighbors, r_min_size):
            return False

        next_region = grid.new_region()
        region_neighbors = set([(x, y) for x in range(grid.get_sixe_x()) for y in range(grid.get_sixe_y())])
        r_min_size = 1
        #print(next_region.number)
    else:
        next_region = region

    return populate_grid(grid, next_cell, next_region, region_neighbors, r_min_size)


"""
Returns a cell and True if a change of region must be done
"""
def get_next_cell(grid, cell, region):
    if region.cell_count == grid.max_region_size:
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

        if grid.is_cell_set(cell):
            cell_nbr += 1

            if cell_nbr > len(grid.mat[0]) * len(grid.mat):
                print("cell_nbr to high")

        i += 1

    #print(cell)
    return cell


def get_region_minimum_size(grid, cell, r_min_size, cell_neighbors):
    r_dico = dict()

    for o_cell in cell_neighbors:
        o_region = grid.get_cell_region(o_cell)

        if o_region != None:
            r_dico[o_region] = r_dico[o_region] + 1 if (o_region in r_dico) else 1

    for o_region, count in r_dico.items():
        #print(cell, o_region.number)
        if o_region.cell_count == count:
            r_min_size = max(r_min_size, count + 1)

    return r_min_size


def is_region_valid(grid, region, region_neighbors, r_min_size):
    if region.cell_count < r_min_size:
        #print("Some cell of " + str(region.cells) + " got surrounded by a larger region")
        #utils.print_mat(grid.mat)
        return False

    if len(region_neighbors) > 0:
        if region.cell_count == grid.max_region_size:
            #print("5 cells around one : " + str(region_neighbors))
            return False

        #print(region_neighbors, cell, region.cells, region.number)
        #utils.print_mat(grid.mat)
        for o_cell in region_neighbors:
            o_region = grid.get_cell_region(o_cell)

            if o_region != None and o_region.cell_count <= region.cell_count:
                #print(o_region.cells, region.cells)
                #print("Cell " + str(o_cell) + " of max value " + str(o_region.cell_count) + " surrounded by region of size " + str(region.cell_count))
                return False

    return True



if __name__ == '__main__':
    res = create_grid()
    utils.print_mat(res.mat)
