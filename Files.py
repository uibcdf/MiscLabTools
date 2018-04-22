import sys, os, glob
import natsort

def CheckIsDir(dir_path=None):
    return os.path.isdir(dir_path)

def CheckIsFile(file_path=None):
    return os.path.isfile(file_path)

def CheckDirExists(dir_path=None):
    is_dir=False
    exists=os.path.exists(dir_path)
    if exists:
        is_dir=CheckIsDir(dir_path)
    #raise error or warning especificando si no existe o existe pero no es dir
    return is_dir

def CheckFileExists(file_path=None):
    is_file=False
    exists=os.path.exists(file_path)
    if exists:
        is_file=CheckIsFile(file_path)
    return is_file

def MakeFile(file_path=None):
    if not CheckFileExists(file_path):
        open(file_path, 'w').close()
    else:
        #raise warning or error
        pass
    pass

def MakeDir(dir_path=None):
    if not CheckDirExists(dir_path):
        os.makedirs(dir_path)
    else:
        #raise warning or error
        pass
    pass

# def DirToDict(dir_path=None):

#     directory = {}

#     for dirname, dirnames, filenames in os.walk(dir_path):
#         dn = os.path.basename(dirname)
#         directory[dn] = []

#         if dirnames:
#             for d in dirnames:
#                 directory[dn].append(DirToDict(dir_path=os.path.join(dir_path, d)))

#             for f in filenames:
#                 directory[dn].append(f)
#         else:
#             directory[dn] = filenames

#         return directory


def DirToDict(dir_path=None):

    directory = {}

    for dirname, dirnames, filenames in os.walk(dir_path):
        dn = os.path.basename(dirname)
        directory[dn] = []

        if dirnames:
            for d in dirnames:
                directory[dn].append(DirToDict(dir_path=os.path.join(dir_path, d)))

            for f in filenames:
                directory[dn].append(f)
        else:
            directory[dn] = filenames

        return directory

