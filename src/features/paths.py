import os
import shutil


def prepare_dist_folder():
    if os.path.exists("./dist"):
        shutil.rmtree("./dist")
    os.mkdir("./dist")
