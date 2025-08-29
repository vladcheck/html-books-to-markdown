import os
import re
from features.const import HTML_ENTITY_TO_SYMBOL

re_styles = re.compile(r"<style.*style>", re.S)
re_scripts = re.compile(r"<script.*script>", re.S)
re_doctype = re.compile(r"")
re_extra_spaces = re.compile(r"\s{2,}")


def remove_styles(content: str) -> str:
    return re.sub(re_styles, "", content)


def remove_scripts(content: str) -> str:
    return re.sub(re_scripts, "", content)


def replace_special_characters(line: str) -> str:
    for [pattern, char] in HTML_ENTITY_TO_SYMBOL.items():
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
        file.close()

        file = open(f"./dist/{filename}", "w", encoding="utf8")  # TODO: Use settings[]
        file.write(content)
        file.close()
    print("Post processing ended successfully.")

if __name__ == "__main__":
    post_process()
