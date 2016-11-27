from os import listdir, path
from sys import argv

if (not len(argv) > 1):
    print "Please provide a directory path as an argument"
    exit()

dirPath = argv[1].strip()

levelAligner = '|';
fileIndicator = '|-';

def printPath(dir, level=0):
    files = []
    try:
        files = listdir(dir)
    except OSError:
        return

    for file in files:
        print ((levelAligner if level > 0 else "") +
            (" "*level)+fileIndicator+file)
        printPath(path.join(dir, file), level+1)

printPath(dirPath);

