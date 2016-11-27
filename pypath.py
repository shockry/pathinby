from os import listdir, path
from sys import argv


def main(args):
    # If no directory is specified, use current directory
    dirPath = '.'
    if len(args) > 1:
        dirPath = args[1]

    outFile = None
    if len(args) > 2:
        outFile = open(args[2], 'w')

    print ('\n'.join(createPath(dirPath, outFile)))


def createPath(dirPath='.', outFile=None, levelAligner='|',
               fileIndicator='|-'):
    path = generatePath(dirPath, levelAligner, fileIndicator)

    if outFile is not None and not outFile.closed:
        outFile.write('\n'.join(path))
        outFile.close()
    return path


def generatePath(dirPath, levelAligner,
                 fileIndicator, level=0, pathMap=None):
    if pathMap is None:
        pathMap = []
    files = []

    # If directory, get visit its contents, otherwise just return
    try:
        files = listdir(dirPath.strip())
    except OSError:
        return

    for file in files:
        levelLine = formatLine(levelAligner, fileIndicator, file, level)
        pathMap.append(levelLine)

        generatePath(path.join(dirPath, file), levelAligner,
                     fileIndicator, level+1, pathMap)

    return pathMap


def formatLine(levelAligner, fileIndicator, filename, level):
    aligner = levelAligner if level > 0 else ""
    return aligner + (" "*level) + fileIndicator + filename

if __name__ == "__main__":
    main(argv)
