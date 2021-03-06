# Multiprocessing File Hasher B

import hashlib
import os
import sys
import time
import multiprocessing

# Create a constant for the local directory
HASHDIR = '/hashtest/'

#
# hashFile Function, designed for multiprocessing
#
# Input: Full Pathname of the file to hash
#
#
def hashFile(fileName):

    try:

        fp = open(fileName, 'rb')

        # Then Read the contents into a buffer
        fileContents = fp.read()

        # Close the file
        fp.close()

        # Create a hasher object of type sha256
        hasher = hashlib.sha256()

        # Hash the contents of the buffer
        hasher.update(fileContents)

        print(fileName, hasher.hexdigest())

        # Delete the hasher object
        del hasher

    except:
        # If any exceptions occur notify the user and exit
        print('File Processing Error')
        sys.exit(0)

    return True

#
# Create Main Function
#

if __name__ == '__main__':


    # Obtain the list of files in the HASHDIR
    listOfFiles = os.listdir(HASHDIR)

    # Mark the starting time of the main loop
    startTime = time.time()

    # Create a process Pool with 4 processes mapping to
    # the 4 cores on my laptop
    coreCount = multiprocessing.cpu_count()
    corePool = multiprocessing.Pool(processes=4)

    # Map the corePool to the hashFile function
    results = corePool.map(hashFile, (HASHDIR+listOfFiles[0],\
                                     HASHDIR+listOfFiles[1],\
                                     HASHDIR+listOfFiles[2],\
                                     HASHDIR+listOfFiles[3],))

    # Once all the files have been hashed and results printed
    # I calculate the elapsed time
    elapsedTime = time.time() - startTime
    print('Elapsed Time:', elapsedTime, 'Seconds')

