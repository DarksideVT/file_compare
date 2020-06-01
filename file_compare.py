import filecmp
import os

LEFTDIR = None
RIGHTDIR = None
OUTPUTFILELOCATION = "./"
QUEUEONENAME = "directory_one.txt"
QUEUETWONAME = "directory_two.txt"

def output_list(outputList):
    for x in outputList:
        print(x, end='\n')

def does_output_exists():
    global QUEUEONENAME
    global QUEUETWONAME
    if os.path.exists(OUTPUTFILELOCATION + QUEUEONENAME) == True or os.path.exists(OUTPUTFILELOCATION + QUEUETWONAME) == True:
        print("Seems you have an 'output_one.txt' or 'output_two.txt' file here already, please delete or rename them then run the application again. ")
        return exit()

def write_to_file(inputText,fileName):
    with open(fileName, "a") as outputFile:
        for test in inputText:
            try:
                outputFile.write(test + "\n")
            except:
                continue

def check_up_counter(inputNumber):
    if (inputNumber % 1000) == 0:
        return True
    else:
        return False

def create_queue(rootDirectory):
    queue = [None]
    counter = 0
    for root, directories, filenames in os.walk(rootDirectory):
        for directory in directories:
            queue.append(os.path.join(root, directory))
            counter += 1
            if check_up_counter(counter) == True:
                print("There are %d files so far" % counter)
        for filename in filenames:
            queue.append(os.path.join(root, filename))
            counter += 1
            if check_up_counter(counter) == True:
                print("There are %d files so far" % counter)
    print("The total number of contents in '%s' is: %d" % (rootDirectory, counter))
    with open("differences.txt", "a") as outputFile:
        outputFile.write("Total files in %s are: %d\n" % (rootDirectory, counter))
    return queue

def list_diff(list1, list2): 
	return (list(set(list1) - set(list2)))

def run():
    global LEFTDIR
    global RIGHTDIR
    does_output_exists()
    #Comment out LEFTDIR and RIGHTDIR here to use hard coded directories at beginning of script
    LEFTDIR = input("What is the root directory for the left side? ")
    RIGHTDIR = input("What is the root directory for the right side? ")
    queueone = create_queue(LEFTDIR)
    write_to_file(queueone, QUEUEONENAME)
    queuetwo = create_queue(RIGHTDIR)
    write_to_file(queuetwo, QUEUETWONAME)
    write_to_file(list_diff(queueone, queuetwo), "differences.txt")

run()
