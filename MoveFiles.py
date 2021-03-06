######################################################################
# Function		: Create dirs based on image file extensions and move
#                 the corresponding files to those dirs
# Date			: 5-Jun-17
# Improvements	:
# 				1. Function
# 				2. Process CR2, DNG and move to RAW dir
# 				3. Process TIFF and move to TIFF dir
######################################################################

import sys
# import platform
import os
import os.path
import glob
import shutil

jpglist = ['.jpg', '.JPG', '.jpeg', '.JPEG']
rawlist = ['.NEF', '.CR2', '.dng', '.DNG','.heic','.HEIC']
tiflist = ['.tif', '.TIF', '.tiff', '.TIFF']

def createDir(cpath, ctype):
    destdir = os.path.join(cpath, ctype.upper())

    if (os.path.exists(destdir)):
        print('%s exists' % destdir)
    else:
        os.mkdir(destdir)
        print('%s created' % destdir)
        print()

    return (destdir)

def printMsg(fname, dirname):
    path, filename = os.path.split(fname)
    print('%s file moved to %s' % (path + filename, dirname))

def moveFiles(path, destdir):
    try:
        files = glob.glob(path)

    except:
        print('No such files')

    else:
        movecount = 0

        for file in files:
            shutil.move(file, destdir)
            # printMsg(file, destdir)
            movecount += 1

        if (movecount > 0):
            print('%s file(s) moved' % movecount)

if __name__ == '__main__':
    # platfrm = platform.system()
    # print (platform.system())

    # set working dir
    if (len(sys.argv) == 1):
        # if (platfrm == "Windows")
        # path = 'C:\\Users\\Vinod\\Dropbox\\Python\\Learning\\Completed\\MoveFiles\\'
        path = '/Volumes/Seagate Working Disk/My Photos/Singapore/Gardens By The Bay 2017'
        # else:
        # path = '/Users/vinodverghese/Dropbox/'
    elif (len(sys.argv) > 1):
        path = str(sys.argv[1])

        if not (os.path.exists(path)):
            print('%s does not exist' % path)
            sys.exit(99)

    print('Working directory : %s' % path)
    print()

    # get all files in path
    allfiles = os.listdir(path)

    # check file extension and set flag
    lrflag = False
    jpgflag = False
    rawflag = False
    tifflag = False

    # get file extensions and set flags
    for file in allfiles:
        if (file[:3] == 'LR-') and (not lrflag):
            lrflag = True

        ext = os.path.splitext(file)[1]

        if (ext in jpglist) and (not jpgflag):
            jpgflag = True

        if (ext in rawlist) and (not rawflag):
            rawflag = True

        if (ext in tiflist) and (not tifflag):
            tifflag = True

    # create and move files based on the flags
    # print(lrflag)
    # print(jpgflag)
    # print(rawflag)

    # create LR directory and move LR-* files
    if (lrflag):
        destdir = createDir(path, 'LR')

        extn = 'LR-*'

        LRdir = os.path.join(path, extn)
        moveFiles(LRdir, destdir)

    # create JPG directory and move jpg files
    if (jpgflag):
        destdir = createDir(path, 'JPG')

        for ext in jpglist:
            extn = '*' + ext

            jpgdir = os.path.join(path, extn)
            # print(jpgdir)
            moveFiles(jpgdir, destdir)

    # create RAW directory and move raw files
    if (rawflag):
        destdir = createDir(path, 'RAW')

        for ext in rawlist:
            extn = '*' + ext

            rawdir = os.path.join(path, extn)
            # print(rawdir)
            moveFiles(rawdir, destdir)

            rawdir = os.path.join(path, '*.xmp')
            # print(rawdir)
            moveFiles(rawdir, destdir)

    # create TIFF directory and move tiff files
    if (tifflag):
        destdir = createDir(path, 'TIFF')

        for ext in tiflist:
            extn = '*' + ext

            rawdir = os.path.join(path, extn)
            # print(rawdir)
            moveFiles(rawdir, destdir)
