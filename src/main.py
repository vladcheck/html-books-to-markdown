from const import *
from settings import settings

from features.tags import *
from features.utils import *
from features.chapters import *
from features.paths import prepare_dist_folder


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

    for line in stdin.readlines():
        line = replace_special_characters(line)

        if should_line_be_removed(line) == "":
            stdout.write("")
            continue

        if is_new_chapter(line):
            stdout = switch_streams(stdout, line)
            print("New chapter started")

        line = parse_html_tags(line)
        line = remove_extra_spaces(line)

        stdout.write(line)

    stdin.close()
    stdout.close()
    print("Stage 1 done")

    # post_processing()
    # print("Post processing done")

    print("Execution ended.")


main()
