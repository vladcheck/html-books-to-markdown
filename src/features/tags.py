import re
from .const import TAGS_FOR_REMOVAL
from .chapters import is_new_chapter, switch_streams

re_tag_attributes = re.compile(r"(?:\w+=\".+\"\s*)+")


def tag_replace(line: str, tag: str, repl1: str = "", repl2: str = "") -> str:
    return re.sub(rf"<{tag}\s*\/?>", repl1, line).replace(f"</{tag}>", repl2)


def tag_delete(line: str, tag: str) -> str:
    return re.sub(rf"<{tag}\s*\/?>", "", line).replace(f"</{tag}>", "")


def sanitize_tags(line: str) -> str:
    return re.sub(re_tag_attributes, "", line)


def parse_html_tags(line: str) -> str:

    line = sanitize_tags(line)

    for tag in TAGS_FOR_REMOVAL:
        line = tag_delete(line, tag)

    line = tag_replace(line, "title", "\n# ", "\n")
    line = tag_replace(line, "h1", "\n# ", "\n")
    line = tag_replace(line, "h2", "\n## ", "\n")
    line = tag_replace(line, "h3", "\n### ", "\n")
    line = tag_replace(line, "h4", "\n#### ", "\n")
    line = tag_replace(line, "h5", "\n##### ", "\n")
    line = tag_replace(line, "h6", "\n###### ", "\n")

    line = tag_replace(line, "li", "- ")

    line = tag_replace(line, "code", "`", "`")
    line = tag_replace(line, "pre", "\n```\n", "\n```\n")

    line = tag_replace(line, "em", "*", "*")
    line = tag_replace(line, "b", "**", "**")
    line = tag_replace(line, "i", "*", "*")
    line = tag_replace(line, "strong", "**", "**")

    line = tag_replace(line, "blockquote", "> ")
    line = tag_replace(line, "cite", "> ")
    line = tag_replace(line, "caption", "> ")
    line = tag_replace(line, "figcaption", "> ")

    line = tag_replace(line, "br", "\n")

    line = tag_replace(line, "td", "| ", " |")
    line = tag_replace(line, "th", "| ", " |")
    line = tag_replace(line, "tr", "| --- |", "| --- |")

    line = tag_replace(line, "sub", "^")
    line = tag_replace(line, "sup", "_")

    return line


def parse_tags(stdin, stdout):
    print("Parsing tags...")

    for line in stdin.readlines():
        if is_new_chapter(line):
            stdout = switch_streams(stdout, line)

        line = parse_html_tags(line)
        stdout.write(line)

    stdin.close()
    stdout.close()
    print("Tags parsed successfully.")
