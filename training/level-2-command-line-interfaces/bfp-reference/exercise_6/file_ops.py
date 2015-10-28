"""
This modules provides various function for operating on
"""

def copy_files(files: list, destination: str, new_filenames: list=None):
    """
    Copy files to a given destination.

    First attempt to copy the file while maintaining current permissions.
    If this fails, it attempt to copy without maintaining permissions.

    """

    for file in files:

        if new_filenames is not None:
            try:
                file_destination = "{}/{}".format(
                    destination, new_filenames[files.index(file)])
            except IndexError:
                print("No matching new name found for file: {}".format(file))
                continue
        else:
            file_destination = destination

        operation_result = subprocess.check_output(
            args=['cp', '-vp', file, file_destination],
            stderr=subprocess.STDOUT)

        print(operation_result.decode('utf-8').strip('\n'))