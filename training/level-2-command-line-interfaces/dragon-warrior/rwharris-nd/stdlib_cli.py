"""This module provides a CLI that..."""

import file_ops


if __name__ == '__main__':
    program_arguments = file_ops.return_args()
    file_ops.copy_files(
        program_arguments.filenames,
        program_arguments.destination)

# print(program_arguments)