# -*- encoding: utf-8 -*-

"""
Module with Client
"""

import os
import time
import gzip


class Client:
    """
    Client class
    contain methods:backup, get_tree, restore
    """

    def __init__(self, platform, path, output, rest, compression):
        """
        Class Initialization
        :param platform:
        :param path:
        :param output:
        :param restore:
        """

        self.compression = compression
        self.platform = platform
        if "win" in self.platform:
            self.tmp = "\\"
        elif self.platform == "linux":
            self.tmp = "/"

        self.path = path
        if not self.path.endswith(self.tmp) and ".backup" not in self.path:
            self.path += self.tmp
        self.output = output
        if not self.output.endswith(self.tmp):
            self.output += self.tmp

        if rest:
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
        name = name.replace(" ", "_").replace(":", "_")
        if self.compression:
            print("compressed")
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

                try:
                    data = open("{}{}{}".format(path, tmp, file), "rb")
                    print('Backing up ' + file)
                    output.write(b"*" * 128 + b"\n")
                    output.write("{}{}{}\n".format(path, tmp, file)
                                 .replace(self.path, "")
                                 .encode())
                    output.write(b"*" * 128 + b"\n")
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

    def restore(self):
        """
        Method for restoring backup.
        Work as reversed backup method and
        takes the same arguments
        as path and output,
        but path is now path to the file, not directory
        :return:
        """

        for i in range(len(self.dirs)):
            try:
                os.mkdir(self.output + self.dirs[i].decode("utf8"))

            except FileExistsError as error:
                print(error)
        for i in range(len(self.paths)):
            try:
                with open(self.output.encode() +
                          self.paths[i], "bw") as output:
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
            if self.compression:
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
        print(len(backup))
        for i in range(0, len(backup)-1, 2):

            self.paths.append(backup[i].replace(b"\n", b""))
            self.files.append(backup[i + 1])
