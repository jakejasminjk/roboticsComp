#!/usr/bin/env python
import sys
from PIL import Image
import queue
import os

#clear data file
open("data.txt", "w").close()

start = (int(sys.argv[3]),int(sys.argv[4]))
end = (int(sys.argv[5]), int(sys.argv[6]))

def iswhite(value):
    if value == (255,255,255):
        return True

def getadjacent(n):
    x,y = n
    return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

def BFS(start, end, pixels):

    lqueue = queue.Queue()
    lqueue.put([start]) # Wrapping the start tuple in a list

    while not lqueue.empty():

        path = lqueue.get()
        pixel = path[-1]

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent
            if iswhite(pixels[x,y]):
                #Marks a white visited pixel grey. This removes the need for a visited list,
                #but this requires a second load of the image file from disk before drawing a path
                pixels[x,y] = (127,127,127)
                new_path = list(path)
                new_path.append(adjacent)
                lqueue.put(new_path)

    print("Queue has been exhausted. No Path was found.")


# if __name__ == '__main__':
#
#     # call with: python mazesolver.py <mazefile> <outputfile>[.jpg|.png|etc.]
#     base_img = Image.open(sys.argv[1])
#     base_pixels = base_img.load()
#
#     path = BFS(start, end, base_pixels)
#
#     path_img = Image.open(sys.argv[1])
#     path_pixels = path_img.load()
#
#     for position in path:
#         x,y = position
#         path_pixels[x,y] = (255,0,0) # red
#     print(path)
#     path_img.save(sys.argv[2])

# invoke: python mazesolver.py <mazefile> <outputfile>[.jpg|.png|etc.]
base_img = Image.open(sys.argv[1])
base_pixels = base_img.load()

path = BFS(start, end, base_pixels)

path_img = Image.open(sys.argv[1])
path_pixels = path_img.load()

#Important
for position in path:
    x,y = position
    path_pixels[x,y] = (255,0,0) # red
    with open('./data.txt', 'a') as f1:
        content = "{0},{1}".format(x/20, y/9)
        f1.write(content + os.linesep)

print(path)
path_img.save(sys.argv[2])
