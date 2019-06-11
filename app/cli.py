# -*- encoding: utf-8 -*-

"""
Module with Client
"""

import os
import time
import gzip

import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random


class Client:
    """
    Client class
    contain methods:backup, get_tree, restore
    """

    def __init__(self, settings):
        """
        Class Initialization
        :param platform:
        :param path:
        :param output:
        :param restore:
        """

        self.options = {}
        self.options["compression"] = settings["compression"]
        self.options["encryption"] = settings["encryption"]

        if "win" in settings["platform"]:
            self.tmp = "\\"
        else:
            self.tmp = "/"

        self.path = settings["path"]
        if not self.path.endswith(self.tmp) and ".backup" not in self.path:
            self.path += self.tmp

        self.output = settings["output"]

        if not self.output.endswith(self.tmp):
            self.output += self.tmp

        if settings["restore"]:
            self.paths = []
            self.dirs = []
            self.files = []
        else:
            self.paths = {}
            self.dirs = {}
            self.files = None

    def backup(self):
        """"
        Method for backing up directory
        from path to file, that will be stored
        in output directory
        :return:
        """
        name = "{}Backup_{}.backup".format(self.output, time.ctime())
        if self.options["encryption"]:
            password = self.get_password()
        name = name.replace(" ", "_").replace(":", "_")
        if self.options["compression"]:
            name += ".gz"
            output = gzip.open(name, "wb")
        else:
            output = open(name, "wb")

        for directory in self.dirs.keys():
            if directory != self.path:
                print("{}\n".format(directory.replace(self.path, "")))
                output.write("{}\n".format(directory
                                           .replace(self.path, ""))
                             .encode())

        for path in self.paths:
            files = self.paths[path]
            tmp = ""
            if path != self.path:
                tmp = self.tmp

            for file in files:
                name = "{}{}{}".format(path, tmp, file)
                try:
                    data = open(name, "rb")
                    print('Backing up: ' + name)
                    output.write(b"*" * 128 + b"\n")
                    output.write(name
                                 .replace(self.path, "")
                                 .encode())
                    output.write(b"*" * 128 + b"\n")
                    if self.options["encryption"]:
                        output.write((self.encrypt(password,
                                                   data.read() + b"\n"))
                                     .encode())
                    else:
                        output.write(data.read() + b"\n")
                    data.close()

                except FileNotFoundError as error:

                    print(error)
                    print("File {}{}{} wasn't found"
                          .format(path, tmp, file))

                except OSError as error:

                    print(error)
                    print("File {}{}{} wasn't found"
                          .format(path, tmp, file))
        output.close()
        print("Backup finished in {}".format(time.clock()))

    def get_tree(self):
        """
        Method for getting all directories and
        subdirectories as self.files and self.paths
        :return:
        """

        for path, dirs, files in os.walk(self.path):
            self.paths[path] = files
            self.dirs[path] = dirs

    @staticmethod
    def get_password():
        """
        Runs in loop before gets input longer than 0
        """
        while True:
            password = input("Password: ")
            if len(password) != "":
                break
        return password

    def restore(self):
        """
        Method for restoring backup.
        Work as reversed backup method and
        takes the same arguments
        as path and output,
        but path is now path to the file, not directory
        :return:
        """
        if self.options["encryption"]:
            password = self.get_password()

        for i in range(len(self.dirs)):
            name = self.output + self.dirs[i].decode("utf8")
            try:
                print("creating directory: " + name)
                os.mkdir(name)

            except FileExistsError as error:
                print(error)

        for i in range(len(self.paths)):
            name = self.output.encode() + self.paths[i]
            try:
                print("Restoring file: " + name.decode("utf8"))
                with open(name, "bw") as output:

                    if self.options["encryption"]:
                        output.write((self.decrypt(password, self.files[i])))
                    else:
                        output.write(self.files[i])

            except ValueError as error:
                print("Some error")

    def split_backup(self):

        """
        Method that reads all backup data and splits
        them into name of files as self.files and
        directories where are files stored as self.dirs.
        """
        try:
            if self.options["compression"]:
                file = gzip.open(self.path, "rb")
            else:
                file = open(self.path, "rb")
            backup = file.read()
        except FileNotFoundError as error:
            print(error)
        file.close()
        backup = backup.split(b"*" * 128 + b"\n")

        self.dirs = backup[0].split(b"\n")[:-1]
        del backup[0]
        for i in range(0, len(backup)-1, 2):

            self.paths.append(backup[i].replace(b"\n", b""))
            self.files.append(backup[i + 1])

    @staticmethod
    def encrypt(key, source):
        """
        Method for encryption of source
        by key
        """
        key = SHA256.new(key.encode()).digest()
        tmp = Random.new().read(AES.block_size)
        encryptor = AES.new(key, AES.MODE_CBC, tmp)
        padding = AES.block_size - len(source) % AES.block_size
        source += bytes([padding]) * padding
        data = tmp + encryptor.encrypt(source)
        return base64.b64encode(data).decode("utf8")

    @staticmethod
    def decrypt(key, source):
        """
        Method for decrypting source
        by key
        """
        source = base64.b64decode(source)
        key = SHA256.new(key.encode()).digest()
        tmp = source[:AES.block_size]
        decryptor = AES.new(key, AES.MODE_CBC, tmp)
        data = decryptor.decrypt(source[AES.block_size:])
        padding = data[-1]
        if data[-padding:] != bytes([padding]) * padding:
            raise ValueError("Invalid padding...")
        return data[:-padding]
