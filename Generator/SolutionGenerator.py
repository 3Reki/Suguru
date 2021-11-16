import random
import time
import operator

def ChooseNumber(cell):
    #print(cell)
    if cell is False:
        #print("isok")
        return True

    potential_nb = GetAllowedNumbers(cell)
    next = GetNextCell()


    while len(potential_nb) > 0:
        choice_index = random.randint(0, len(potential_nb) - 1)
        choice = potential_nb.pop(choice_index)

        mat[cell[1]][cell[0]] = choice
        #print(mat)

        #print(str(cell) + " done: " + str(choice))
        done = ChooseNumber(next)

        if done:
            return True

    #print("ah shit stop : " + str(cell))
    mat[cell[1]][cell[0]] = -1
    #print(mat)
    RevertCell()
    return False

def GetAllowedNumbers(cell):
    region = GetRegion()
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

            if cell_y > -1 and cell_x > -1 and cell_y < len(mat) and cell_x < len(mat[cell_y]):
                affecting_cells.add((cell_x, cell_y))


    for other_cell in affecting_cells:
        if other_cell == cell:
            continue

        value = mat[other_cell[1]][other_cell[0]]

        if value != -1:
            affecting_nb.add(value)

    potential_nb = potential_nb.difference(affecting_nb)

    return list(potential_nb)

def GetRegion():
    return list(regions[cellIndex[0]])

def GetNextCell():
    previous_cell_index.append(list(cellIndex))
    if cellIndex[1] + 1 >= len(regions[cellIndex[0]]):
        if cellIndex[0] + 1 >= len(regions):
            return False

        cellIndex[0] += 1
        cellIndex[1] = 0
    else:
        cellIndex[1] += 1

    return regions[cellIndex[0]][cellIndex[1]]

def RevertCell():
    global cellIndex
    cellIndex = previous_cell_index.pop()

def sort_regions(r):
    lst = []
    for region in r:
        lst.append(sorted(region, key=operator.itemgetter(1, 0)))

    return sorted(lst, key=lambda r: (len(r), r[0][1], r[0][0]))

def create_number_grid(r = None, size_x = 7, size_y = 5, random_seed = None):
    global regions
    if r is None:
        regions = [
            [(1, 3)],
            [(4, 0), (5, 0)],
            [(6, 0), (6, 1), (6, 2)],
            [(3, 1), (2, 2), (3, 2), (3, 3)],
            [(0, 0), (1, 0), (2, 0), (3, 0), (2, 1)],
            [(0, 1), (1, 1), (0, 2), (1, 2), (0, 3)],
            [(4, 1), (5, 1), (4, 2), (5, 2), (4, 3)],
            [(2, 3), (0, 4), (1, 4), (2, 4), (3, 4)],
            [(5, 3), (6, 3), (4, 4), (5, 4), (6, 4)]
        ]
    else:
        regions = sort_regions(r)

    # TODO: case prioritaire ?
    '''regions = [
        [(2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (0, 2), (1, 2)]
    ]'''

    global cellIndex
    cellIndex = [0, -1]

    global previous_cell_index
    previous_cell_index = []

    global mat
    mat = [[-1 for _ in range(size_x)] for __ in range(size_y)]
    #mat[0][4] = 2
    #mat[3][3] = 1

    random.seed(random_seed)
    if ChooseNumber(GetNextCell()):
        return mat

    return False


if __name__ == '__main__':
    start = time.time()
    create_number_grid()

    print("Done in " + str(time.time() - start) + " seconds")
