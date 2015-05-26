import argparse
import subprocess
from string import lower

from AutoFileUtilities import *
from string_manipulation import remove_List_From_String


class FileManager(Auto_File_Utility):
    """
    Provide functionality for various file operations.

    Provide methods corresponding to a variety of file related operations
    that take place on a single server.

    """

    def __init__(self):
        # TODO: I don't think this is the correct way to call the parent.
        Auto_File_Utility.__init__(
            self,
            'Generic File Management API',
            'Provides a command line interface for various file operations.')
        self.display_Program_Information()
        self.program_arguments = None
        self.evaluate_command_line_arguments()

    def evaluate_command_line_arguments(self):
        """
        Generate command line interface and parses the input.

        """
        # Define 'parent' parser which will be inherited by sub-command parsers.
        parent_parser = argparse.ArgumentParser(add_help=False)
        parent_parser.add_argument(
            "filename_location",
            help="Name & location of file(s) being operated on.")

        arguments_parser = argparse.ArgumentParser()
        subparsers = arguments_parser.add_subparsers(help='Available Commands')

        # Subparser for moving files.
        # todo: Consider the duplication between this and move_file_parser.
        copy_file_parser = subparsers.add_parser(
            'copy',
            help='Copy a file.',
            parents=[parent_parser])
        copy_file_parser.add_argument(
            'dest_filename',
            help='Name & location of destination file.')
        copy_file_parser.set_defaults(operation='copy')

        # Subparser for deleting files.
        delete_file_parser = subparsers.add_parser(
            'delete',
           help='Delete a file.',
           parents=[parent_parser])

        delete_file_parser.set_defaults(operation='delete')

        # GPG Decryption Subparser
        gpg_encryption_parser = subparsers.add_parser(
            'gpg_encrypt',
            help='Encrypt a file with GPG.',
            parents=[parent_parser])

        gpg_encryption_parser.add_argument(
            'recipient_key',
            help='Name of recipient''s public key.')

        gpg_encryption_parser.set_defaults(operation='gpg_encrypt')

        # GPG Decryption Subparser
        gpg_decryption_parser = subparsers.add_parser(
            'gpg_decrypt',
            help='Decrypt a GPG encoded file.',
            parents=[parent_parser])

        gpg_decryption_parser.add_argument(
            '--passphrase',
            help='Decryption Passphrase')

        gpg_decryption_parser.set_defaults(operation='gpg_decrypt')

        # GUNZIP Subparser
        gunzip_file_parser = subparsers.add_parser(
            'gunzip',
            help='Unzip a file archive.',
            parents=[parent_parser])

        gunzip_file_parser.set_defaults(operation='gunzip')

        # GZIP Subparser
        gzip_file_parser = subparsers.add_parser(
            'gzip',
            help='Zip a file(s) into an archive.',
            parents=[parent_parser])

        gzip_file_parser.set_defaults(operation='gzip')
        
        # UNZIP Subparser
        unzip_file_parser = subparsers.add_parser(
            'unzip',
            help='Unzip a file archive.',
            parents=[parent_parser])

        unzip_file_parser.set_defaults(operation='unzip')

        # ZIP Subparser
        zip_file_parser = subparsers.add_parser(
            'zip',
            help='Zip a file(s) into an archive.',
            parents=[parent_parser])

        zip_file_parser.set_defaults(operation='zip')

        # Subparser for moving files.
        move_file_parser = subparsers.add_parser(
            'move',
            help='Move a file.',
            parents=[parent_parser])

        move_file_parser.add_argument(
            'dest_filename',
            help='Name & location of destination file.')

        move_file_parser.set_defaults(operation='move')

        self.program_arguments = arguments_parser.parse_args()

    def execute_file_operation(self):
        """
        Dispatch method calls for various file operations and handle
        operation exceptions.

        """
        self.get_filelist(self.program_arguments.filename_location)
        print '-- Start OS Output --'

        try:
            if lower(self.program_arguments.operation) == 'copy':
                operation_to_execute = self.copy_file
            elif lower(self.program_arguments.operation) == 'delete':
                operation_to_execute = self.delete_file
            elif lower(self.program_arguments.operation) == 'gpg_encrypt':
                operation_to_execute = self.gpg_encrypt_file
            elif lower(self.program_arguments.operation) == 'gpg_decrypt':
                operation_to_execute = self.gpg_decrypt_file
            elif lower(self.program_arguments.operation) == 'gunzip':
                operation_to_execute = self.gunzip_file
            elif lower(self.program_arguments.operation) == 'gzip':
                operation_to_execute = self.gzip_file
            elif lower(self.program_arguments.operation) == 'zip':
                operation_to_execute = self.zip_file
            elif lower(self.program_arguments.operation) == 'unzip':
                operation_to_execute = self.unzip_file
            elif lower(self.program_arguments.operation) == 'move':
                operation_to_execute = self.move_file
                
            print("Operation Selected: {}".format(operation_to_execute))

            for self.current_file in self.filelist:
                operation_to_execute()

            self.last_operation_status = 0

        except subprocess.CalledProcessError as subprocess_error:
            print subprocess_error
            print subprocess_error.output
            self.last_operation_status = 1

        except EnvironmentError as environment_error:
            print environment_error.message
            self.last_operation_status = 1

        print '-- End OS Output --'

        self.display_Program_Summary()

    def copy_file(self):
        """
        Copy a file(s) from one location to another.

        First attempt to copy the file while maintaining current permissions.
        If this fails, it attempt to copy without maintaining permissions.

        """
        try:
            operation_result = subprocess.check_output(
                ['cp', '-vp', self.current_file,
                 self.program_arguments.dest_filename],
                stderr=subprocess.STDOUT)

        except subprocess.CalledProcessError:
            operation_result = subprocess.check_output(
                ['cp', '-v', self.current_file,
                 self.program_arguments.dest_filename],
                stderr=subprocess.STDOUT)

        print operation_result

    def delete_file(self):
        """
        Delete a file(s).

        """
        print(
            subprocess.check_output(
                ['rm', '-vvv', self.current_file],
                stderr=subprocess.STDOUT))

    def gpg_encrypt_file(self):
        """
        Encrypt one or more files using GPG.
        """
        print 'Encrypting: ' + self.current_file
        print(
            subprocess.check_output(
                ['gpg',
                '-vvv',
                '--encrypt',
                '--always-trust',
                '--yes',
                '--batch',
                '--recipient',
                self.program_arguments.recipient_key,
                self.current_file],
                stderr=subprocess.STDOUT))

    def gpg_decrypt_file(self):
        """
        Decrypt files encoded using PGP/GPG.

        """
        print 'Decrypting: ' + self.current_file
        unencrypted_filename = remove_List_From_String(
            self.current_file,
            ['.gpg', '.pgp'])

        operation_arguments = [
            'gpg',
            '-vvv',
            '--decrypt',
            '--yes',
            '--batch',
            '--output',
            unencrypted_filename,
            self.current_file]

        if self.program_arguments.passphrase:
            operation_arguments.insert(2, '--passphrase')
            operation_arguments.insert(3, self.program_arguments.passphrase)

        print(
            subprocess.check_output(
                operation_arguments,
                stderr=subprocess.STDOUT))

    def gzip_file(self):
        """
        Compress individual files into individual archives.

        """
        print(
            subprocess.check_output(
                ['gzip', '-vr', self.current_file],
                stderr=subprocess.STDOUT))

    def gunzip_file(self):
        """
        Unpack an archive file.

        """
        print(
            subprocess.check_output(
                ['gunzip', '-vr', self.current_file],
                stderr=subprocess.STDOUT))

    def zip_file(self):
        """
        Compress individual files into individual archives.

        """
        print("Attempt zip on: {}".format(self.current_file))
        print(
            subprocess.check_output(
                ['zip', self.current_file],
                stderr=subprocess.STDOUT))

    def unzip_file(self):
        """
        Unpack an archive file.

        """
        print("Attempt zip on: {}".format(self.current_file))
        print(
            subprocess.check_output(
                ['unzip', self.current_file],
                stderr=subprocess.STDOUT))

    def move_file(self):
        """
        Move a file from one location to another.

        Can also be used to rename a file.

        """
        print(
            subprocess.check_output(
                ['mv', '-v', self.current_file,
                 self.program_arguments.dest_filename],
                stderr=subprocess.STDOUT))

if __name__ == "__main__":    
    file_manager = FileManager()
    file_manager.execute_file_operation()
    file_manager.display_Program_Summary()
