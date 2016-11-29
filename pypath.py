import os
import argparse


def main(args):
    outFile = None
    if args.output:
        outFile = open(args.output, 'w')

    path = createPath(args.directory, outFile)
    if args.show:
        print ('\n'.join(path))


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
        files = os.listdir(dirPath.strip())
    except OSError:
        return

    for file in files:
        levelLine = formatLine(levelAligner, fileIndicator, file, level)
        pathMap.append(levelLine)

        generatePath(os.path.join(dirPath, file), levelAligner,
                     fileIndicator, level+1, pathMap)

    return pathMap


def formatLine(levelAligner, fileIndicator, filename, level):
    aligner = levelAligner if level > 0 else ""
    return aligner + (" "*level) + fileIndicator + filename

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory",
                        help="Create the path tree for the directory " +
                             "with this path. If omitted, creates for " +
                             "current directory",
                        nargs='?', default='.')
    parser.add_argument("-o", "--output",
                        help="Name of the output file " +
                             "(overwritten if present, created if not)")
    parser.add_argument("-s", "--show",
                        help="Print the output to terminal",
                        action="store_true")
    args = parser.parse_args()
    main(args)
