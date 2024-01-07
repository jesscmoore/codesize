import glob
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

LARGE_FILE_LIMIT = 500
STDOUT_WIDTH = 65
FILENAME_COL_WIDTH = STDOUT_WIDTH - 6

parser = ArgumentParser(
    description=f"Large file size threshold. Default: {LARGE_FILE_LIMIT}",  # noqa: E501
    formatter_class=ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "large_file_limit",
    type=int,
    nargs="?",
    default=LARGE_FILE_LIMIT,
    help="Large file limit. Default: {LARGE_FILE_LIMIT}",
)

args = parser.parse_args()
large_file_limit_user = args.large_file_limit

# Use user supplied large file limit if provided
if large_file_limit_user:
    large_file_limit = large_file_limit_user
else:
    large_file_limit = LARGE_FILE_LIMIT

# Get file size for all files in project recursively
file_sizes = {}
for file in glob.iglob("." + "/**/*.py", recursive=True):
    with open(file, "rb") as f:
        file_sizes[file] = sum(1 for line in f)

# Sort recursively by size
file_sizes = dict(
    sorted(file_sizes.items(), key=lambda item: item[1], reverse=True)
)

# Subset files with size greater than LARGE_FILE_LIMIT
large_files = {}
for k, v in file_sizes.items():
    if v >= large_file_limit:
        large_files[k] = v

# Print to stdout
print(f"{'File'.ljust(FILENAME_COL_WIDTH)}  Size")
print("-" * STDOUT_WIDTH)
for key, value in large_files.items():
    print(f"{key.ljust(FILENAME_COL_WIDTH)}  {value}")
print("")
print(f"Large files: {len(large_files)}")
