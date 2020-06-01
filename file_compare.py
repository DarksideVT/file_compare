"""import filecmp
from filecmp import dircmp
def print_diff_files (dcmp):
    for name in dcmp.diff_files:
         print("diff_file %s found in %s and %s" % (name, dcmp.left,
               dcmp.right))
    for sub_dcmp in dcmp.subdirs.values():
         print_diff_files(sub_dcmp)
dcmp = dircmp('F:\BitWarden - Copy', 'F:\BitWarden') 
print_diff_files(dcmp)"""

import filecmp
import os

leftDir = ["F:\Test\Test1"]
rightDir = ["F:\Test\Test2"]

LISTOFDIFFERENCES = []

#Gets list of currentDir contents
def list_of_folder_contents(currentDir):
    contents = os.listdir(currentDir)
    return contents

#Checks if currentDir is a directory 
def is_dir(currentDir):
    if os.path.isdir(currentDir) == True:
        return True
    else:
        return False

#Checks if currentDir is NOT a directory output list of Files
'''def is_not_dir(currentDir):
    files = []
    for currentFile in list_of_folder_contents(currentDir):
        if (os.path.isdir(currentDir + "/" + currentFile)) == False:
            files.append(currentFile)
    return files
'''

#Gets left dir list
def left_dir(leftDir, rightDir):
    result = filecmp.dircmp(leftDir, rightDir)
    return result.left_list

#Gets right dir list
def right_dir(leftDir, rightDir):
    result = filecmp.dircmp(leftDir, rightDir)
    return result.right_list

#Gets list of things only in left
def left_dir_only(leftDir, rightDir):
    result = filecmp.dircmp(leftDir, rightDir)
    return result.left_only

#Gets list of things only in right
def right_dir_only(leftDir, rightDir):
    result = filecmp.dircmp(leftDir, rightDir)
    return result.right_only

def list_of_subdirectories(leftDir):
    subdirectories = []
    for currentDir in list_of_folder_contents(leftDir):
        if is_dir(leftDir + "\\" + currentDir) == True:
            subdirectories.append(str(leftDir + "\\" + currentDir))
    return subdirectories
    
'''#Brings leftDir one level deaper for all directories
def go_deeper(leftDir):
    directories = list_of_subdirectories(leftDir)
    for currentFile in directories:
        return currentFile
'''
#Removes missing files listOne if listTwo doesn't have the file
def remove_missing_from_listOne(listOne, listTwo):
    newList = listOne
    for listOneTemp in listOne:
        if listOneTemp not in listTwo:
            newList.remove(listOneTemp)
    return newList

#Returns list of files on next level
def list_of_next_level(directory):
    newDirList = []
    if list_of_subdirectories(directory) != None:
        for subdirectory in list_of_subdirectories(directory):
            newDirList.append(directory + subdirectory)
        return newDirList

def go_to_next_directory(leftDir):
    counter = 0
    while counter <= len(leftDir) :
        index = (len(leftDir) - 1)
        if leftDir[index] == rightDir[index]:
            counter =+ 1
            return (leftDir + '\\' + leftDir[index])
        else:
            return leftDir


#Check if the directory is the same
def are_the_dir_the_same(leftDir, rightDir):
    leftDirList = list_of_folder_contents(leftDir)
    rightDirList = list_of_folder_contents(rightDir)
    if leftDirList == rightDirList:
        return True
    else:
        return False

#Returns different contents in directory
def diff_or_not(leftDir, rightDir):
    if left_dir_only(leftDir, rightDir) != []:
        return left_dir_only(leftDir, rightDir)
    else:
        return None

'''#Creates list of missing files
def output_for_file(leftDir, rightDir):
    global LISTOFDIFFERENCES
    if diff_or_not(leftDir, rightDir) == None:
        print("Nothing to see here")
    else:
        for currentFile in diff_or_not(leftDir, rightDir):
            LISTOFDIFFERENCES.append(leftDir + "\\" + currentFile)'''

#Appends global lost of missing files
def append_missing(leftDir,rightDir):
    global LISTOFDIFFERENCES
    for missingFile in left_dir_only(leftDir, rightDir):
        LISTOFDIFFERENCES.append(leftDir + '\\' + missingFile)

#Prints a list
def output_list(outputList):
    for x in outputList:
        print(x, end='\n')

'''def run(leftDir, rightDir):
    global LISTOFDIFFERENCES
    append_missing(leftDir, rightDir)
    for content in list_of_subdirectories(leftDir):
        append_missing(leftDir, rightDir)
        leftDir = go_deeper(leftDir)
        rightDir = leftDir
    output_list(LISTOFDIFFERENCES)
def debug(leftDir, rightDir):
    for files in list_of_folder_contents(leftDir):
        print(files)'''

def run(leftDir, rightDir):
    global LISTOFDIFFERENCES

    
#output_list(list_of_subdirectories(leftDir))
#run(leftDir, rightDir)
output_list(list_of_next_level(leftDir))
#print()