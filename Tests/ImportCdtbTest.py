import os
import shutil
import unittest

from MainControl.Import import unpack_file, download_hashes


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.folder_path = r'D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data'
        if os.path.exists(self.folder_path):
            shutil.rmtree(self.folder_path)

    def test_main(self):
        download_hashes()
        unpack_file("D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\Akali.wad.client", "D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions")
        self.assertTrue(os.path.exists("D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\data"))


if __name__ == '__main__':
    unittest.main()
