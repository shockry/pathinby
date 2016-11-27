from os import listdir, path

dirPath = raw_input().strip()

def printPath(dir, level=0):
    files = []
    try:
        files = listdir(dir)
    except OSError:
        return

    for file in files:
        print ("-"*level)+file
        printPath(path.join(dir, file), level+1)

printPath(dirPath);

