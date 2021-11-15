def adjacent_diagonal_cells(mat, cell):
    cells = []

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i, j) == (0, 0):
                continue

            x = cell[0] + i
            y = cell[1] + j

            if y > -1 and x > -1 and y < len(mat) and x < len(mat[y]):
                cells.append((x, y))

    return cells

def adjacent_cells(mat, cell):
    cells = []

    for couple in ((0, -1), (-1, 0), (1, 0), (0, 1)):

        x = cell[0] + couple[0]
        y = cell[1] + couple[1]

        if y > -1 and x > -1 and y < len(mat) and x < len(mat[y]):
            cells.append((x, y))

    return cells
