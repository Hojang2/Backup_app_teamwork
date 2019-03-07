# -*- encoding: utf-8 -*-
import os


class Client:

    def __init__(self, platform, path, output):

        self.platform = platform
        self.path = path
        self.output = output
        self.files = []

    def backup(self):
        self.get_tree()
        print(self.files)

    def get_tree(self):

        for path, dirs, files in os.walk(self.path):
            self.files.append((path, dirs, files))
