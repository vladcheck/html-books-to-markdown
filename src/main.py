from settings import settings

from features.tags import *
from features.chapters import *
from features.paths import prepare_dist_folder
from features.post_processing import post_process


def main():
    prepare_dist_folder()

    stdin = open(
        f"{settings["stdin"]["path"]}/{settings["stdin"]["name"]}",
        "r",
        encoding=settings["stdin"]["encoding"],
    )
    stdout = open(
        f"{settings["stdout"]["path"]}/{settings["stdout"]["name"]}",
        "w+",
        encoding=settings["stdout"]["encoding"],
    )

    parse_tags(stdin, stdout)
    post_process()

    print("Done.")

if __name__ == "__main__":
    main()
