###
### ColorMap class for loading color maps from CSV files
### and accessing their values.
###
### Mark Phillips <mphillip@unca.edu>
### Fri Sep 17 16:07:05 2010
###
class ColorMap:
    ###
    ### Create a new ColorMap object by loading it from a CSV file
    ###
    def __init__(self, filename):
        f = open(filename)
        self.colors = []
        try:
            for line in f:
                line = line.strip(" \t\n")
                if line.startswith("#"): continue
                fields = line.split(",")
                values = []
                self.colors.append(IndexedColor(int(fields[0]), int(fields[1]), int(fields[2]), int(fields[3])))
        finally:
            f.close()

    ###
    ### Return the color corresponding to value x, where x is a number between
    ### 0 and 1.  x=0 corresponds to the first color in the ColorMap, x=1
    ### corresponds to the last, and numbers in between are interpolated
    ### accordingly.
    ###
    def getColor(self,x):
        v = float(x) * len(self.colors)-1
        i = int(v+0.5)
        if i >= len(self.colors): i = len(self.colors) - 1
        if i <= 0: i = 0
        return self.colors[i]

    ###
    ### Print out the entire color map, for debugging
    ###
    def dump(self):
        for color in self.colors:
            print "(%3d,%3d,%3d,%3d)" % (color.i, color.r, color.g, color.b)

###
### A little utility class for storing indexed colors.
### (An "indexed color" is just an R,G,B color together with
### an index value 'i'.)
###
class IndexedColor:
    def __init__(self, i,r,g,b):
        self.i = i
        self.r = r
        self.g = g
        self.b = b
