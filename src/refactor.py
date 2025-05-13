# Thank you https://github.com/maysara-elshewehy for making this good code divider.

# ╔══════════════════════════════════════ imports ══════════════════════════════════════╗
import os
# ╚══════════════════════════════════════ imports ══════════════════════════════════════╝

# ╔══════════════════════════════════════ type aliases ══════════════════════════════════════╗

# all supported types of an option in `gum`
type SupportedOptionTypes = str | int | bool
# all supported types of a parameter in `gum`
type SupportedParameterTypes = str | list[str] | None

# ╚══════════════════════════════════════ type aliases ══════════════════════════════════════╝


# ╔══════════════════════════════════════ Classes ══════════════════════════════════════╗
class GumCommandBuilder:
    """
    `GumCommandBuilder` is an abstraction on how to invoke `gum` from python.
    """

    def __init__(
        self,
        subcommand: str,
        allowed_opts: dict[str, type],
    ) -> None:
        """
        Initialize `GumCommandBuilder`.

        Args:
            `subcommand`: which subcommand of gum the user wants to invoke
            `allowed_opts`: all possible options for that subcommand
        """

        self.subcommand: str = subcommand
        self.possible_opts: dict[str, type] = allowed_opts
        self.args: list[tuple[str, str]] = []

    def add_args(self, optname: str, value: SupportedOptionTypes):
        """
        A method to add user-defined **kwargs into GumCommandBuilder's arguments list
        """
        # Checks if `optname` is a valid option in accordance to `self.possible_opts` in `self.subcommand`.
        if optname not in self.possible_opts:
            raise KeyError("[ERROR]: invalid option")

        # Checks if the type of some value of an `optname` is in accordance to the value of `self.possible_opts[optname]` which is a type.
        if not isinstance(value, self.possible_opts[optname]):
            raise ValueError("[ERROR]: invalid value")

        stringified_value: str = GumCommandBuilder.stringify_opt_value(value)

        self.args.append((optname, stringified_value))

    def execute(self, param: SupportedParameterTypes = None):
        """

        A method to execute all a gum command needs (options and parameter)

        Args:
            `param`: the parameter for a given subcommand
        """
        # The command to execute in a process
        to_execute: str = "gum " + self.subcommand + " "

        # Appends all options in `self.args` in a long option format with a value associated with it (--<flag-name>=<flag-value>)
        for optname, value in self.args:
            # TODO: convert the snake-cased option name into an option that `gum` can parse.
            if GumCommandBuilder.is_long_dot_option(optname):
                first_dash = optname.find("_")
                second_dash = optname.find("_", first_dash + 1)

                before_second_dash = optname[:second_dash]
                before_second_dash = before_second_dash.replace("_", "-")
                after_second_dash = optname[second_dash + 1 :]

                return f"--{before_second_dash}.{after_second_dash}={value}"

            elif GumCommandBuilder.is_short_dot_option(optname):
                dot_opt: str = optname.replace("_", ".")
                return f"--{dot_opt}={value} "

            # If its not a short or a long option it implies that the option is just a normal long option.
            to_execute += f"--{optname}={value} "

        # Checks if `param` is present and has the expected value
        if isinstance(param, str):
            to_execute += param
        elif isinstance(param, list) and all(isinstance(item, str) for item in param):
            for pr in param:
                to_execute += pr + " "

        # Executes the command without getting the output
        os.system(to_execute)

    def execute_with_ret(self, param: SupportedParameterTypes = None) -> str:
        """
        A method to execute all a gum command needs (options and parameter) and returns its output

        Args:
            `param`: the parameter for a given subcommand
        """

        # The command to execute in a process
        to_execute: str = "gum " + self.subcommand + " "

        # Appends all options in `self.args` in a long option format with a value associated with it (--<flag-name>=<flag-value>)
        for optname, value in self.args:
            # TODO: convert the snake-cased option name into an option that `gum` can parse.
            if GumCommandBuilder.is_long_dot_option(optname):
                first_dash = optname.find("_")
                second_dash = optname.find("_", first_dash + 1)

                before_second_dash = optname[:second_dash]
                before_second_dash = before_second_dash.replace("_", "-")
                after_second_dash = optname[second_dash + 1 :]

                return f"--{before_second_dash}.{after_second_dash}={value}"

            elif GumCommandBuilder.is_short_dot_option(optname):
                dot_opt: str = optname.replace("_", ".")
                return f"--{dot_opt}={value} "

            # If its not a short or a long option it implies that the option is just a normal long option.
            to_execute += f"--{optname}={value} "

        # checks if `param` is present and has the expected value
        if isinstance(param, str):
            to_execute += param
        elif isinstance(param, list) and all(isinstance(item, str) for item in param):
            for pr in param:
                to_execute += pr + " "

        # Executes the command and gets the output
        return os.popen(to_execute).read().strip()

    # Convenience function to convert `SupportedOptionTypes` into a `str`
    @classmethod
    def stringify_opt_value(cls, value: SupportedOptionTypes) -> str:
        # It's important to handle `bool` before handling `int` because a `bool` is just a number
        if isinstance(value, str):
            return f'"{value}"'
        elif isinstance(value, bool):
            return str(value).lower()
        elif isinstance(value, int):
            return str(value)

    @classmethod
    def is_long_dot_option(cls, optname: str) -> bool:
        idx: int = optname.find("_")
        if idx == -1:
            return False
        beginning: str = optname[:idx]
        match beginning:
            case "cursor":
                rest: str = optname[idx + 1 :]

                queries: list[str] = [
                    "text_foreground",
                    "text_background",
                    "line_number_foreground",
                    "line_number_background",
                    "line_foreground",
                    "line_foreground",
                ]

                for query in queries:
                    if query in rest:
                        return True
                return False
            case "file":
                rest: str = optname[idx + 1 :]
                return True if "size" in rest else False
            case "match":
                rest: str = optname[idx + 1 :]
                return True if "highlight" in rest else False
            case "selected":
                rest: str = optname[idx + 1 :]
                return True if "indicator" in rest else False
            case "unselected":
                rest: str = optname[idx + 1 :]
                return True if "prefix" in rest else False
            case _:
                return False

    @classmethod
    def is_short_dot_option(cls, optname: str) -> bool:
        idx: int = optname.find("_")
        if idx == -1:
            return False
        beginning: str = optname[:idx]
        match beginning:
            case "base":
                return True
            case "border":
                return True
            case "cell":
                return True
            case "cursor":
                return True
            case "directory":
                return True
            case "file":
                return True
            case "header":
                return True
            case "help":
                return True
            case "item":
                return True
            case "indicator":
                return True
            case "text":
                return True
            case "key":
                return True
            case "level":
                return True
            case "match":
                return True
            case "message":
                return True
            case "permissions":
                return True
            case "placeholder":
                return True
            case "prefix":
                return True
            case "prompt":
                return True
            case "selected":
                return True
            case "separator":
                return True
            case "spinner":
                return True
            case "symlink":
                return True
            case "time":
                return True
            case "title":
                return True
            case "unselected":
                return True
            case "value":
                return True
            case _:
                return False


class GumWrappers: ...


# ╚══════════════════════════════════════ classes ══════════════════════════════════════╝
