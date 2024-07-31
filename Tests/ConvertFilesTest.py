import os
import shutil
import unittest

import MainControl.ConvertFiles
from MainControl.SearchForDependencyPrograms import search_for_ritobin


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.folder_path = r'D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data\characters\akali\skins\skin0.py'
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)

    def test_main(self):
        ritobinPath = r"D:\Programs verknuepfng\Programs\ritobin\ritobin_cli.exe"
        MainControl.ConvertFiles.ritobin(ritobinPath,r"D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions", "akali", 0)
        self.assertTrue(os.path.exists(r'D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data\characters\akali\skins\skin0.py'))


if __name__ == '__main__':
    unittest.main()
