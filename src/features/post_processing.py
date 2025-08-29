from settings import settings


def remove_styles(filename: str) -> None:
    stdin = open(
        filename,
        "r+",
        encoding="utf8",
    )
    stdout = open(
        "temp." + filename,
        "w+",
        encoding="utf8",
    )

    in_styles = False

    for line in stdin.readlines():
        if "<style" in line:
            in_styles = True
        elif "</style" in line:
            in_styles = False

        if in_styles:
            stdout.write("")
        else:
            stdout.write(line)

    stdin.close()
    stdout.close()


def post_processing():
    stdout_filename = settings["stdout"]["name"]
    remove_styles(stdout_filename)
