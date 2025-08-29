# HTML files to Markdown converter

> The project is licensed under [BSD 3-Clause License](./LICENSE.md).

It's a python script that converts `.htm` and `.html` files to markdown format (original files are preserved).

## Features

- Removes HTML-tags (NOT ALL);
- Divides single htm document by multiple headings (not yet controllable) into multiple files, ex. if the file features multiple `<h1>` or `<h2>` tags, the content below respective headers will be extracted into separate files. This lets you have multiple small files instead of a giant one;

### Supported platforms

| Platform      | Supported | Tested |
| ------------- | --------- | ------ |
| Windows 10/11 | Yes       | ✅     |
| Linux         | N/A       | ❌     |
| MacOS         | N/A       | ❌     |

## Restrictions

- Doesn't support any external data (images, PDFs, etc.);

## Known issues

1. A ton of tags are not yet supported;
2. `<sup>` and `<sub>` are parsed incorrectly;
3. Doesn't ask user for data (file path, encoding, etc.), everything is configured via `src/settings.py` or elsewhere;
4. Can't parse colons (:) inside chapter names, so the headings of files are cut off up to the colon;
5. Doesn't keep links (`<a href="...">`);
6. Doesn't parse multiline quotes and cites properly (only first line is parsed in a special way);
7. Sometimes incorrectly parses multiline code blocks (skips triple-backticks);
8. `<ol>` lists are treated as `<ul>`;

## TBD

1. User guide;
2. Documentation;
3. Progress bars in terminal;
