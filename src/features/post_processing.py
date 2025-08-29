import os
import re

char_map = {
    "&lt;": "<",
    "h&gt;": ">",
    "&nbsp;": " ",
    "&amp;": "&",
    "–": "-",
    "’": "'",
}


re_styles = re.compile(r"<style.*style>", re.S)
re_scripts = re.compile(r"<script.*script>", re.S)
re_doctype = re.compile(r"")
re_extra_spaces = re.compile(r"\s{2,}")


def remove_styles(content: str) -> str:
    return re.sub(re_styles, "", content)


def remove_scripts(content: str) -> str:
    return re.sub(re_scripts, "", content)


def remove_extra_spaces(line: str) -> str:
    return re.sub(re_extra_spaces, " ", line)


def replace_special_characters(line: str) -> str:
    for [pattern, char] in char_map.items():
        line = line.replace(pattern, char)
    return line


def post_process():
    print("Starting post processing...")
    for filename in os.listdir("./dist"):
        file = open(f"./dist/{filename}", "r", encoding="utf8")  # TODO: Use settings[]
        content = file.read()
        content = remove_scripts(content)
        content = remove_styles(content)
        content = replace_special_characters(content)
        content = remove_extra_spaces(content)
        file.close()

        file = open(f"./dist/{filename}", "w", encoding="utf8")  # TODO: Use settings[]
        file.write(content)
        file.close()
    print("Post processing ended successfully.")


# post_process()
