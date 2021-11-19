import sys
import random
import time
import utils
import math
import grid_generator as grid_gen
import solution_generator as soln_gen

class Tester:

    """
    def t_grid_validity_and_time(nb_attempts = 100):
        start = time.time()
        ok_count = 0
        regions = []

        for i in range(nb_attempts):
            res = grid_gen.create_grid()

            #print("Grid " + str(i + 1) + " ok")
            seed = random.randrange(10000)
            regions.clear()

            for region in res.regions:
                regions.append(region.cells)

            sg_start = time.time()
            test = soln_gen.create_number_grid(regions, res.get_sixe_x(), res.get_sixe_y(), seed, 10000)

            sg_length = time.time() - sg_start
            if sg_length > 10:
                print("Grid took too long") #+ str(sg_length) + "s to complete, result=" + str(test != False))
                #print(regions, seed)

            if test != False:
                ok_count += 1

            print(ok_count, i)


        print("Valid grids : " + str(ok_count) + "/" + str(nb_attempts))
        print("Done in " + str(time.time() - start) + " seconds")
    """

    def t_long_soln_gen(self, nb_grid = 10, min_time = 10, max_time = 60):
        regions = []
        init_size_x, init_size_y, init_max_region_size = 5, 7, 5
        nb_tried = 0
        values = [(6, 7, 5), (6, 8, 6), (7, 8, 6)]

        while nb_grid > 0:
            size_x = min(init_size_x + int(nb_tried >= 50) + (nb_tried - 50)//100, 9)
            size_y = min(init_size_y + nb_tried//100, 10)
            max_region_size = min(init_max_region_size + nb_tried//100, 8)
            res = grid_gen.create_grid(size_x, size_y, max_region_size)
            seed = random.randrange(10000)
            regions.clear()

            for region in res.regions:
                regions.append(region.cells)

            sg_start = time.time()
            test = soln_gen.create_number_grid(regions, size_x, size_y, seed, max_time)
            sg_length = time.time() - sg_start

            if sg_length > min_time:
                if sg_length > max_time:
                    print("Grid took too long")
                print("Over " + str(sg_length) + "s to complete, result=" + str(test != False))
                print(regions, seed, size_x, size_y)
                nb_grid -= 1

            nb_tried += 1


if __name__ == '__main__':
    getattr(Tester, sys.argv[1])(Tester())
