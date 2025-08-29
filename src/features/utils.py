import re
from const import char_map


def remove_extra_spaces(line: str) -> str:
    while re.match(r"\s\s", line):
        line = re.sub(r"\s\s", " ", line)
    return line


def should_line_be_removed(line: str) -> bool:
    if re.search(r"^<img.*\/?>.*", line) != None:
        return True
    if "<!DOCTYPE>" in line:
        return True
    return False


def replace_special_characters(line: str) -> str:

    for [pattern, char] in char_map.items():
        line = line.replace(pattern, char)
    return line
