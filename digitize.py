# Imports the monkeyrunner modules used by this program

import time
import sys
import subprocess

import numpy as np

WIDTH = 1080
HEIGHT= 1920

COLORS = {
            "604de8" : "RED",
            "7d54a4" : "PURPLE",
            "75ac2c" : "GREEN",
            "c9bd7b" : "BLUE",
            "6ccdfe" : "YELLOW",
         }
COLOR_IDS = dict([(k,v) for k,v in zip(COLORS.keys(), range(1, len(COLORS) + 1))])

class Dot(object):
    def __init__(self, data):
        self.hexcolor = "".join(["%x" % cc for cc in data[0][:3]])
        self.color_id = COLOR_IDS[self.hexcolor]
        self.x = data[1]
        self.y = data[2]

class Dots(object):
    def __init__(self, points):
        self.dot_list = [Dot(p) for p in points]

        # np array, shape <nb_of_points> x 2
        self.mat = np.array([(d.x, d.y) for d in self.dot_list])

        # This rounds off glitches of point coordinates on the same axis
        self.rmat = self.mat / 10
        self.cols = np.unique(self.rmat[:, 0]).size
        self.rows = np.unique(self.rmat[:, 1]).size

    def dump(self):
        for dot in self.dot_list:
            print "(%4d, %4d) (Color: %s, ID: %2d)" % (dot.x, dot.y,
            COLORS[dot.hexcolor], dot.color_id)

output = subprocess.Popen(["./contours", sys.argv[1]], stdout=subprocess.PIPE).communicate()[0]
dots = Dots(eval(output))

dots.dump()

grid = np.zeros((WIDTH, HEIGHT), dtype=np.uint8)
for dot in dots.dot_list:
    grid[dot.x, dot.y] = dot.color_id

print "%d dots. " % np.sum(grid > 0)
print "Ideal grid size: %d x %d" % (dots.rows, dots.cols)
