import filecmp
import os
import time

leftDir = "Z:\\"
rightDir = "F:\Test\Test2"
OUTPUTFILELOCATION = []
LISTOFDIFFERENCES = []
QUEUE = []
NUMBEROFFOLDERS = []

def output_list(outputList):
    for x in outputList:
        print(x, end='\n')

def does_output_exists():
    if os.path.exists("./output.txt") == True:
        print("Seems you have an 'output.txt' file here already, please delete or rename it then run the application again. ")
        return exit()

def write_to_file(inputText):
    if os.path.exists("./output.txt") == True:
        with open("output.txt", "a") as outputFile:
            for test in inputText:
                outputFile.write(test + "\n")
    else:
        with open("output.txt", "w") as outputFile:
            for test in inputText:
                outputFile.write(test + "\n")

def is_it_a_multiple_of_fifty(inputNumber):
    if (inputNumber % 50) == 0:
        return True
    else:
        return False

def create_folder_queue(rootDirectory):
    global QUEUE
    global NUMBEROFFOLDERS
    counter = 0
    for root, directories, filenames in os.walk(rootDirectory):
        for directory in directories:
            QUEUE.append(os.path.join(root, directory))
            counter += 1
            if is_it_a_multiple_of_fifty(counter) == True:
                print("There are " + str(counter) + " files so far.")
    NUMBEROFFOLDERS = counter

def run():
    global QUEUE
    does_output_exists()
    rootDir = input("What is the root directory you want to find all the folders in?")
    create_folder_queue(rootDir)
    #print(QUEUE)
    write_to_file(QUEUE)

run()
#print(is_it_a_multiple_of_five(10))
#create_file_queue(leftDir)
#write_to_file(QUEUE)
#output_list()
#print("Starting to remove")
'''while counter >= 1:
    print("Removing " + QUEUE.pop(0))
    counter -= 1'''
