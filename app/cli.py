# -*- encoding: utf-8 -*-

"""
Module with Client
"""

import os
import time


class Client:
    """
    Client class
    contain methods:
        backup
        get_tree
        restore
    """

    def __init__(self, platform, path, output, rest):
        """
        Class Initialization
        :param platform:
        :param path:
        :param output:
        :param restore:
        """
        self.platform = platform
        self.path = path
        self.output = output
        self.rest = rest
        self.files = []
        self.paths = []
        self.dirs = []

    def backup(self):
        """
        Method for backing up directory
        from path to file, that will be stored
        in output directory
        :return:
        """
        self.get_tree()
        print(self.files)
        name = "{}Backup_{}.backup".format(self.output, time.ctime())
        name = name.replace(" ", "_").replace(":", "_")
        with open(name, "bw") as output_file:
            for directory in self.dirs:
                output_file.write(directory.encode() + b"\n")
            for i in range(len(self.files)):
                try:
                    tmp = open(self.files[i], "rb")
                    print('Backing up ' + self.files[i])
                    output_file.write(b"******************************************\n")
                    output_file.write(self.files[i].replace(self.path, "").encode() + b"\n")
                    output_file.write(b"******************************************\n")
                    output_file.write(tmp.read())
                    tmp.close()
                except FileNotFoundError as error:

                    print(error)
                    print("File {} wasn't found".format(self.files[i]))

                except OSError as error:

                    print(error)
                    print("File {} wasn't found".format(self.files[i]))


        print("Backup finished in {}".format(time.clock()))

    def get_tree(self):
        """
        Method for getting all directories and
        subdirectories as self.files and self.paths
        :return:
        """

        for path, dirs, files in os.walk(self.path):

            for dir in dirs:
                if dir not in self.dirs:
                    dir = (path + "/" + dir).replace(self.path, "")
                    if dir[0] == "/":
                        dir = dir[1:]
                    self.dirs.append(dir)

            for file in files:
                if file not in self.files:
                    self.files.append((path + file))

    def restore(self):
        """
        Method for restoring backup.
        Work as reversed backup method and
        takes the same arguments
        as path and output,
        but path is now path to the file, not directory
        :return:
        """
        with open(self.path, "rb") as file:
            backup = file.read()
        self.split_backup(backup)
        print(self.dirs)
        for i in range(len(self.dirs)):
            try:
                os.mkdir(self.output + self.dirs[i].decode("utf8"))

            except FileExistsError as e:
                print(e)
        for i in range(len(self.paths)):
            with open(self.output.encode() + self.paths[i], "bw") as f:
                f.write(self.files[i])

    def split_backup(self, backup):
        backup = backup.split(b"******************************************\n")
        self.dirs = []
        backup[0] = backup[0].split(b"\n")[:-1]
        for i in backup[0]:
            self.dirs.append(i)

        for i in range(1, (len(backup)//2)+1, 2):
            self.paths.append(backup[i].replace(b"\n", b""))
            self.files.append(backup[i + 1])





