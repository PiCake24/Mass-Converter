import concurrent.futures
import subprocess


def unpack_all_wad(champion_map, python_path, league_path):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for champion in champion_map:
            print(f"Submitting unpack task for {champion}")
            future = executor.submit(unpack_wad, python_path, league_path, champion)
            futures.append(future)

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Unpacking task completed for {result}")
            except Exception as e:
                print(f"Exception occurred: {e}")

    print("All unpack tasks completed.")


def unpack_wad(python_path, league_path, champion):
    command = [
        "cdtb", "wad-extract", f'{league_path}\\{champion}.wad.client'
    ]
    process = subprocess.Popen(command, cwd=python_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    exit_code = process.returncode
    if exit_code != 0:
        print(f"Error extracting WAD for {champion}: {stderr.decode('utf-8')}")