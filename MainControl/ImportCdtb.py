from cdtb.hashes import (
    default_hashfile,
    default_hash_dir,
    update_default_hashfile,
)
from cdtb.wad import Wad


def download_hashes():
    default_hash_dir.mkdir(parents=True, exist_ok=True)
    hash_files = [
        'hashes.binentries.txt',
        'hashes.binfields.txt',
        'hashes.binhashes.txt',
        'hashes.bintypes.txt',
        'hashes.game.txt',
        'hashes.lcu.txt',
        'hashes.rst.txt',
    ]
    for basename in hash_files:
        update_default_hashfile(basename)


def unpack_file(filepath, outputpath):

    hashfile = default_hashfile(filepath)

    wad = Wad(filepath, hashes=hashfile.load())

    wad.guess_extensions()
    wad.extract(outputpath, overwrite=True)

unpack_file("D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions\Akali.wad.client", "D:\Riot Games\League of Legends\Game\DATA\FINAL\Champions")
