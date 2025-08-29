import re
from const import TAGS_FOR_REMOVAL

re_tag_attributes = re.compile(r"(?<=<\w)?\ ([\w=\"'#\-\s]*)(?=>)\s?")


def tag_replace(line: str, tag: str, repl1: str = "", repl2: str = "") -> str:
    return line.replace(f"<{tag}>", repl1).replace(f"</{tag}>", repl2)


def tag_delete(line: str, tag: str) -> str:
    return line.replace(f"<{tag}>", "").replace(f"</{tag}>", "")


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

    line = tag_replace(line, "br", "\n")

    line = tag_replace(line, "td", "| ", " |")
    line = tag_replace(line, "th", "| ", " |")
    line = tag_replace(line, "tr", "| --- |", "| --- |")

    return line
