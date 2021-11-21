import utils
import operator

class Region:
    region_count = 0

    def __init__(self, cells):
        Region.region_count += 1
        self.id = self.region_count
        self.adj_done_region_count = 0
        self.cell_count = len(cells)
        self.cells = cells

    def _cmp_regions(self, other, operator):
        if self.adj_done_region_count == 0:
            if other.adj_done_region_count == 0:
                return operator(self.cell_count, other.cell_count)

            return operator(other.adj_done_region_count, self.adj_done_region_count)

        if other.adj_done_region_count == 0:
            return operator(other.adj_done_region_count, self.adj_done_region_count)

        return operator((self.cell_count, -self.adj_done_region_count),
                        (other.cell_count, -other.adj_done_region_count))

    def __lt__(self, other):
        return self._cmp_regions(other, operator.lt)

    def __le__(self, other):
        return self._cmp_regions(other, operator.le)

    def __eq__(self, other):
        return self._cmp_regions(other, operator.eq)

    def __ne__(self, other):
        return self._cmp_regions(other, operator.ne)

    def __ge__(self, other):
        return self._cmp_regions(other, operator.ge)

    def __gt__(self, other):
        return self._cmp_regions(other, operator.gt)

    def __repr__(self):
        return "Region %s: adjacent regions=%s, cells=%s" % (self.id, self.adj_done_region_count, self.cells)


def _reorder(mat, regions, new_order, current):
    new_order.append(current)

    if len(regions) == 1:
        return list(new_order)

    adj_regions = get_adjacent_region(mat, regions, current)

    for r in adj_regions:
        r.adj_done_region_count += 1

    regions.sort()
    return _reorder(mat, regions, new_order, regions.pop(0))

def get_adjacent_region(mat, regions, current):
    adj_cells = set()
    adj_regions_ids = set()

    for cell in current.cells:
        adj_cells = adj_cells.union(utils.adjacent_diagonal_cells(mat, cell))

    if current.cell_count > 1:
        for cell in current.cells:
            adj_cells.remove(cell)

    for cell in adj_cells:
        adj_regions_ids.add(mat[cell[1]][cell[0]])

    return list(filter(lambda r: r.id in adj_regions_ids, regions))

def create_mat(grid_size, regions):
    if grid_size == None:
        raise ValueError("grid_size must be defined by a tuple if mat is None")
    mat = [[None for i in range(grid_size[0])] for j in range(grid_size[1])]

    for r in regions:
        for cell in r.cells:
            mat[cell[1]][cell[0]] = r.id

    return mat

"""
grid_size or mat must be given for sort_regions to work
"""
def sort_regions(init_regions, grid_size = None, mat = None):
    lst = []
    for r in init_regions:
        lst.append(Region(sorted(r, key=operator.itemgetter(1, 0))))

    regions = sorted(lst, key=lambda r: (r.cell_count, r.cells[0][1], r.cells[0][0]))

    if mat == None:
        mat = create_mat(grid_size, regions)

    new_regions = _reorder(mat, regions, [], regions.pop(0))
    new_regions.append(regions[0])

    return list(map(lambda r: r.cells, new_regions))
