import unittest

from MainControl.CheckAndInstallDependencies import check_ctdb, install_dependencies


class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_main(self):
        install_dependencies()
        self.assertEqual(True, check_ctdb())


if __name__ == '__main__':
    unittest.main()
