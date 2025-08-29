# HTML files to Markdown converter

It's a python script that converts `.htm` files to markdown format.

## Features

- Removes HTML-tags (NOT ALL);
- Divides single htm document by multiple headings (not yet controllable) into multiple files, ex. if the file features multiple `<h1>` or `<h2>` tags, the content below respective headers will be extracted into separate files. This lets you have multiple small files instead of a giant one;
  - **There is a caveat: the converter can't parse colons (:) yet, so the headings will be cut off up to the colon**

## Supported platforms

| Platform      | Supported | Tested |
| ------------- | --------- | ------ |
| Windows 10/11 | Yes       | ✅     |
| Linux         | N/A       | ❌     |
| MacOS         | N/A       | ❌     |

The project is licensed under [BSD 3-Clause License](./LICENSE.md).
