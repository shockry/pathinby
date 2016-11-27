from os import listdir, path
from sys import argv


def main(args):
    # If no directory is specified, use current directory
    dirPath = '.'
    if (len(args) > 1):
        dirPath = args[1]
    print ('\n'.join(createPath(dirPath)))


def createPath(dirPath='.', levelAligner='|', fileIndicator='|-',
               level=0, pathMap=None):
    if pathMap is None:
        pathMap = []
    files = []
    # If directory, get visit its contents, otherwise just return
    try:
        files = listdir(dirPath.strip())
    except OSError:
        return

    for file in files:
        pathMap.append((levelAligner if level > 0 else "") +
                       (" "*level)+fileIndicator+file)

        createPath(path.join(dirPath, file), levelAligner, fileIndicator,
                   level+1, pathMap)

    return pathMap

if __name__ == "__main__":
    main(argv)
