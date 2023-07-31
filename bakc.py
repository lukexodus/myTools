#! python3

# bakc.py -- Copies an entire folder and its contents into
# a ZIP file whose filename increments by one.

import zipfile, os

excludedFolders = ['node_modules', 'public', 'venv', '.mypy_cache', '.idea']

def folderIsExcluded(folderName):
    for excludedFolder in excludedFolders:
        if excludedFolder in folderName:
            return True
    return False

current_file_path = os.path.abspath(__file__)
directory_of_python_file = os.path.dirname(current_file_path)

folderToBackup = directory_of_python_file
destinationFolder = 'E:\\Backups\\codes\\myTools'

def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    # folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should used based on
    # what files already exist.

    number = 1

    while True:
        zipFilename = os.path.join(destinationFolder, os.path.basename(folder)) + '_' + str(number) + '.zip'

        if not os.path.exists(zipFilename):
            print(zipFilename)
            break
        number = number + 1


    # Create the ZIP file.

    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.

    for foldername, subfolders, filenames in os.walk(folder):
        if folderIsExcluded(foldername):
            continue
        print('Adding files in %s...' % (foldername))

        # Add the current folder to the ZIP file.
        try:
            backupZip.write(foldername)
        except Exception as e:
            print(f"Unable to add folder {foldername}: {e}")

        # Add all the files in this folder to the ZIP file.

        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
                
            file_path = os.path.join(foldername, filename)
            try:
                backupZip.write(file_path)
            except Exception as e:
                print(f"Unable to add file {file_path}: {e}")

    backupZip.close()
    print('Done.')


backupToZip(folderToBackup)