from io import TextIOWrapper
from settings import settings

import re

re_chapter_name = re.compile(r"(?<=<h[1-2]>)[\w\d\s\-,';\.]*")


def is_new_chapter(line: str) -> bool:
    line = line.lstrip()
    return (
        line.startswith("# ")
        or line.startswith("<h1>")
        or line.startswith("## ")
        or line.startswith("<h2>")
    )


def switch_streams(stdout, current_line: str) -> TextIOWrapper:
    match = re_chapter_name.search(current_line)
    chapter_name: str

    if match:
        stdout.close()
        chapter_name = "".join(match.group(0))
        return open(
            f"{settings["stdout"]["path"]}/{chapter_name}.md",
            "w+",
            encoding=settings["stdout"]["encoding"],
        )
    else:
        return stdout
