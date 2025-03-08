import os
import typing


def to_gum_option(opt: str) -> str:
    if opt.__contains__("foreground") or opt.__contains__("background"):
        replaced = opt.replace("_", ".")
        prefixed = "--" + replaced
        return prefixed
    elif opt.__contains__("_"):
        replaced = opt.replace("_", "-")
        prefixed = "--" + replaced
        return prefixed

    prefixed = "--" + opt
    return prefixed


def convert_to_str(v: object) -> str:
    if isinstance(v, bool):
        stringified = str(v)
        lowercased = stringified.lower()
        return lowercased
    if isinstance(v, str):
        return '"' + v + '"'
    if isinstance(v, int):
        return str(v)


def choose(lst: list[str], **kwargs) -> None:
    possible_opts = {
        "ordered": bool,
        "height": int,
        "cursor": str,
        "show_help": bool,
        "no_show_help": bool,
        "timeout": str,
        "header": str,
        "cursor_prefix": str,
        "selected_prefix": str,
        "unselected_prefix": str,
        "selected": str,
        "input_delimiter": str,
        "output_delimiter": str,
        "label_delimiter": str,
        "strip_ansi": bool,
        "no_strip_ansi": bool,
        # Selection
        "limit": int,
        "no_limit": bool,
        "select_if_one": bool,
        # Style
        "cursor_foreground": str,
        "cursor_background": str,
        "header_foreground": str,
        "header_background": str,
        "item_foreground": str,
        "item_background": str,
        "selected_foreground": str,
        "selected_background": str,
    }

    default_values = {
        "ordered": False,
        "height": 10,
        "cursor": "> ",
        "show_help": True,
        "no_show_help": False,
        "timeout": "0s",
        "header": "Choose:",
        "cursor_prefix": "• ",
        "selected_prefix": "✓ ",
        "unselected_prefix": "• ",
        "selected": ",...",
        "input_delimiter": "\\n",
        "output_delimiter": "\n",
        "label_delimiter": "",
        "strip_ansi": True,
        "no_strip_ansi": False,
        # Selection
        "limit": 1,
        "no_limit": False,
        "select_if_one": False,
        # Style
        "cursor_foreground": "212",
        "cursor_background": "",
        "header_foreground": "99",
        "header_background": "",
        "item_foreground": "",
        "item_background": "",
        "selected_foreground": "212",
        "selected_background": "",
    }

    """
    turn those dicts into sets then do a `-` operation (set difference operation)
    with the user-passed options and allowed options, if there is a difference, 
    that means the user passed something that is not available.
    """

    invalid_option = set(kwargs) - set(possible_opts)
    if invalid_option:
        raise ValueError("invalid option name")

    for key, value in kwargs.items():
        option_type: type = possible_opts[key]
        if not isinstance(value, option_type):
            raise TypeError(f"Invalid type for {option_type}")

    default_values.update(kwargs)

    cmd: str = "gum choose "

    for key, value in default_values.items():
        gum_opt = to_gum_option(key)
        pair = gum_opt + "=" + convert_to_str(value)
        cmd = cmd + pair + " "

    opt = " ".join(lst)

    os.system(f"{cmd} {opt}")


def confirm():
    pass


def file():
    pass


def filter():
    pass


def format():
    pass


def input():
    pass


def join():
    pass


def pager():
    pass


def spin():
    pass


def style():
    pass


def table():
    pass


def write():
    pass


def log():
    pass


def version_check():
    pass


def gum_cmd_help(gum_command: str):
    commands = [
        "choose",
        "confirm",
        "file",
        "filter",
        "format",
        "input",
        "join",
        "pager",
        "spin",
        "style",
        "table",
        "write",
        "log",
        "version-check",
    ]
    if gum_command not in commands:
        raise ValueError(f"ERROR: command {gum_command} is not a gum command!")
    os.system(f"gum {gum_command} --help")


def main():
    choose(["foo", "bar", "baz", "bah"], limit=2)


if __name__ == "__main__":
    main()
