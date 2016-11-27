from os import listdir, path
from sys import argv

def main(argv):
    #If no directory is specified, use current directory
    dir = '.'
    if (len(argv) > 1):
        dir = argv[1]
    print '\n'.join(createPath())

def createPath(dir='.', levelAligner='|', fileIndicator='|-',
        level=0, pathMap=[]):
    files = []
    #If directory, get visit its contents, otherwise just return
    try:
        files = listdir(dir.strip())
    except OSError:
        return

    for file in files:
        pathMap.append((levelAligner if level > 0 else "") +
            (" "*level)+fileIndicator+file)
        
        createPath(path.join(dir, file), levelAligner, fileIndicator,
            level+1, pathMap)

    return pathMap

if __name__ == "__main__":
    main(argv)
