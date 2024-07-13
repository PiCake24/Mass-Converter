import shutil
import unittest
import os

from MainControl.getPythonPath import get_python_path_windows
from MainControl.unpackChampions import unpack_all_wad


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.folder_path = r'D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\akali.wad'

    def test_method_x(self):
        # Check if the file exists and delete it if it does
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)

        # Call method x which should create the file
        champion_map = {"akali": 1}
        python_path = r"C:\Users\Yanni\AppData\Local\Programs\Python\Python310\Scripts"
        league_path = r"D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions"
        unpack_all_wad(champion_map, python_path, league_path)

        # Check if the file exists after method x is called
        self.assertTrue(os.path.exists(self.folder_path))


if __name__ == '__main__':
    unittest.main()
