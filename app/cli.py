# -*- encoding: utf-8 -*-
import os
import time


class Client:

    def __init__(self, platform, path, output):

        self.platform = platform
        self.path = path
        self.output = output
        self.files = []

    def backup(self):
        self.get_tree()
        t = time.clock()
        name = "{}Backup_{}.backup".format(self.output, time.ctime())
        name = name.replace(" ", "_").replace(":", "-")
        with open(name, "wb") as f:
            for file in self.files:
                try:
                    ff = open(file, "rb")
                    print('Backing up ' + file)
                    f.write(ff.read())
                    ff.close()
                except FileNotFoundError as e:
                    print("File {} wasn't found".format(file))
                except OSError as e:
                    print("File {} wasn't found".format(file))

        print("Backup finished in {}".format(time.clock()))

    def get_tree(self):

        for path, dirs, files in os.walk(self.path):
            for file in files:
                if "win" in self.platform:
                    self.files.append(path + "\\" + file)
                else:
                    self.files.append(path + "/" + file)
