import shutil
import unittest
import os

from Deprecated.unpackChampions import unpack_all_wad


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.folder_path = r'D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\akali.wad'
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)

    def test_method_x(self):
        # Call method x which should create the file
        champion_map = {"akali": 1}
        python_path = r"C:\Users\Yanni\AppData\Local\Programs\Python\Python310\Scripts"
        league_path = r"D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions"
        unpack_all_wad(champion_map, python_path, league_path)

        # Check if the file exists after method x is called
        self.assertTrue(os.path.exists(self.folder_path))


if __name__ == '__main__':
    unittest.main()
