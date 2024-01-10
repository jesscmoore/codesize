from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from codesize import files

LARGE_FILE_LIMIT = 500
EXT = "py"

parser = ArgumentParser(
    description=f"Provide large file size threshold (default: "
    f"{LARGE_FILE_LIMIT}) and "
    f"filename extension (default: {EXT})",
    formatter_class=ArgumentDefaultsHelpFormatter,
)
parser.add_argument(
    "large_file_limit",
    type=int,
    nargs="?",
    default=LARGE_FILE_LIMIT,
    help="Large file limit. Default: {LARGE_FILE_LIMIT}",
)

parser.add_argument(
    "ext",
    type=str,
    nargs="?",
    default=EXT,
    help="Filename extension. Default: {EXT}",
)

args = parser.parse_args()
large_file_limit_user = args.large_file_limit

# Use user supplied large file limit if provided
if large_file_limit_user:
    large_file_limit = large_file_limit_user
else:
    large_file_limit = LARGE_FILE_LIMIT

ext_user = args.ext
# Use user supplied large file limit if provided
if ext_user:
    ext = ext_user
else:
    ext = EXT


files.large(limit=large_file_limit, ext=ext)
