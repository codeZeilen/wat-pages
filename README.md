# wat pages

This is the collection of pages used in the [wat](https://github.com/codeZeilen/wat) CLI tool.

Currently, it only contains the pages on names in the filesystem (`fs-path-pages`). 

## Page Format

The pages are written in Markdown. Pages can have a header. 

```
---
license: root directory descriptions originally created by contributors to the Ubuntu documentation wiki and based on https://help.ubuntu.com/community/LinuxFilesystemTreeOverview.
path: /bin
---

/bin is a place for most commonly used terminal commands, like ls, mount, rm, etc.
```

Filesystem pages can have two header fields:
 - path (required):  The path the page describes. It can include single globs, e.g. `/home/*/.bashrc`. If you want the page to refer to a single name, simple use the name as the path, e.g. `.gitignore`.
 - license (optional): If the page content is not original, you can specify the license and source of the content.

The *filename* of a page corresponds to the path with asterisks replaced by the word `glob` and slashes replaced by dashes, except for the first slash, e.g. `/home/*/.bashrc` becomes `home-glob-.bashrc.md`.

