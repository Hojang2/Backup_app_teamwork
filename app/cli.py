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
        if "win" in self.platform:
            self.tmp = "\\"
        elif self.platform == "linux":
            self.tmp = "/"

        self.path = path
        self.output = output
        self.rest = rest
        
        self.paths = {}
        self.dirs = {}

    def backup(self):
        """
        Method for backing up directory
        from path to file, that will be stored
        in output directory
        :return:
        """
        self.get_tree()
        name = "{}Backup_{}.backup".format(self.output, time.ctime())
        name = name.replace(" ", "_").replace(":", "_")
        with open(name, "bw") as output:
            for directory in self.dirs.keys():
                output.write("{}\n".format(directory).encode())


                
            for path in self.paths.keys():
                files = self.paths[path]
                tmp = ""
                if path != self.path:
                    tmp = self.tmp

                for file in files:
                    try:
                        f = open("{}{}{}".format(path, tmp, file), "rb")
                        print('Backing up ' + file)
                        output.write(b"*" * 16 + b"\n")
                        output.write("{}{}{}\n".format(path, tmp, file).encode())
                        output.write(b"*" * 16 + b"\n")
                        output.write(f.read() + b"\n")
                        f.close()
                
                    except FileNotFoundError as error:

                        print(error)
                        print("File {}{}{} wasn't found".format(path, tmp, file))

                    except OSError as error:

                        print(error)
                        print("File {}{}{} wasn't found".format(path, tmp, file))
                

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





