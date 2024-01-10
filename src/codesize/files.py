import glob

LARGE_FILE_LIMIT = 500


def list_file_sizes(ext: str = "py"):
    """List file length.

    Find all files matching file `extension`
    and returns a dictionary of the file name and
    number of lines.

    Args:
        ext: String of the file extension.

    Returns:
        A dict mapping of filename to file number of lines
        where the file number of lines is always an integer.
        For example
        {'file1.py': 0, 'file2.py': 84}
    """
    file_sizes = {}
    for file in glob.iglob("." + "/**/*." + ext, recursive=True):
        with open(file, "rb") as f:
            file_sizes[file] = sum(1 for line in f)

    return file_sizes


def large(limit: int = LARGE_FILE_LIMIT, ext: str = "py"):
    """Print large files.

    Prints a list of large files in
    descending order by size.

    Args:
        limit: Threshold. Files with greater or equal to `limit`
            lines will be printed. Default: 500.
        ext: String of the file extension. Default: 'py'.
    """
    STDOUT_WIDTH = 65
    FILENAME_COL_WIDTH = STDOUT_WIDTH - 6

    file_sizes = list_file_sizes(ext=ext)

    # Sort recursively by size
    file_sizes = dict(
        sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)
    )

    # Subset files with size greater than LARGE_FILE_LIMIT
    large_files = {}
    for k, v in file_sizes.items():
        if v >= limit:
            large_files[k] = v

    # Print to stdout
    print(f"{'File'.ljust(FILENAME_COL_WIDTH)}  Size")
    print("-" * STDOUT_WIDTH)
    for key, value in large_files.items():
        print(f"{key.ljust(FILENAME_COL_WIDTH)}  {value}")
    print("")
    print(f"Large files: {len(large_files)}")
