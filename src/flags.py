subcommands_options: dict[str, dict[str, type]] = {
    "choose": {
        "ordered": bool,  # False
        "height": int,  # 10
        "cursor": str,  # "> "
        "no_show_help": bool,
        "show_help": bool,
        "timeout": str,  # "0s"
        "header": str,  # "Choose:"
        "cursor_prefix": str,  # "• "
        "selected_prefix": str,  # "✓ "
        "unselected_prefix": str,  # "• "
        "selected": str,  # ",..."
        "input_delimiter": str,  # "\\n"
        "output_delimiter": str,  # "\\n"
        "label_delimiter": str,  # ""
        "no_strip_ansi": bool,  # False
        "strip_ansi": bool,  # False
        "limit": int,  # 1
        "no_limit": bool,  # False
        "select_if_one": bool,  # False
        "cursor_foreground": str,  # "212"
        "cursor_background": str,  # ""
        "header_foreground": str,  # "99"
        "header_background": str,  # ""
        "item_foreground": str,  # ""
        "item_background": str,  # ""
        "selected_foreground": str,  # "212"
        "selected_background": str,  # ""
    },
    "confirm": {
        "default": bool,
        "show_output": bool,
        "affirmative": str,
        "negative": str,
        "no_show_help": bool,
        "show_help": bool,
        "timeout": str,
        "prompt-foreground": str,  # "#7571F9"
        "prompt-background": str,  # ""
        "selected-foreground": str,  # "230"
        "selected-background": str,  # "212"
        "unselected-foreground": str,  # "254"
        "unselected-background": str,  # "235"
    },
    "file": {
        "cursor": str,  # ">"
        "all": bool,
        "no_permissions": bool,
        "permissions": bool,
        "no_size": bool,
        "size": bool,
        "file": str,
        "directory": str,
        "no_show_help": bool,
        "show_help": bool,
        "timeout": str,  # "0s"
        "header": str,  # ""
        "height": int,  # 10
        "cursor_foreground": str,  # "212"
        "cursor_background": str,  # ""
        "symlink_foreground": str,  # "36"
        "symlink_background": str,  # ""
        "directory_foreground": str,  # "99"
        "directory_background": str,  # ""
        "file_foreground": str,  # ""
        "file_background": str,  # ""
        "permissions_foreground": str,  # "242"
        "permissions_background": str,  # ""
        "selected_foreground": str,  # "212"
        "selected_background": str,  # ""
        "file-size_foreground": str,  # "240"
        "file-size_background": str,  # ""
        "header_foreground": str,  # 99
        "header_background": str,  # ""
    },
    "filter": {
        # flags
        "indicator": str,
        "selected": str,
        "no_show_help": bool,
        "show_help": bool,
        "selected_prefix": str,
        "unselected_prefix": str,
        "header": str,
        "placeholder": str,
        "prompt": str,
        "width": int,
        "height": int,
        "value": str,
        "reverse": bool,
        "no_fuzzy": bool,
        "fuzzy": bool,
        "no_fuzzy_sort": bool,
        "fuzzy_sort": bool,
        "timeout": str,
        "input_delimiter": str,
        "output_delimiter": str,
        # Style flags
        "indicator_foreground": str,
        "indicator_background": str,
        "selected_indicator_foreground": str,
        "selected_indicator_background": str,
        "unselected_prefix_foreground": str,
        "unselected_prefix_background": str,
        "header_foreground": str,
        "header_background": str,
        "text_foreground": str,
        "text_background": str,
        "cursor_text_foreground": str,
        "cursor_text_background": str,
        "match_foreground": str,
        "match_background": str,
        "prompt_foreground": str,
        "prompt_background": str,
        "placeholder_foreground": str,
        "placeholder_background": str,
        # Selection
        "limit": int,
        "no_limit": bool,
        "select_if_one": bool,
        "no_strict": bool,
        "strict": bool,
    },
    "format": {
        "theme": str,  # pink
        "language": str,  # ""
        "no_strip_ansi": bool,
        "strip_ansi": bool,
        "type": str,  # "markdown"
    },
    "input": {
        "placeholder": str,  #  "Type something_.."
        "prompt": str,  # "> "
        "cursor_mode": str,  # "blink"
        "value": str,  # ""
        "char_limit": int,  # 400
        "width": int,  # 0
        "password": bool,
        "no_show_help": bool,
        "show_help": bool,
        "header": str,  # ""
        "timeout": str,  # "0s"
        "no_strip_ansi": bool,
        "strip_ansi": bool,
        "prompt_foreground": str,  # ""
        "prompt_background": str,  # ""
        "placeholder_foreground": str,  # "240"
        "placeholder_background": str,  # ""
        "cursor_foreground": str,  # "212"
        "cursor_background": str,  # ""
        "header_foreground": str,  # "240"
        "header_background": str,  # ""
    },
    "join": {
        "align": str,  # "left"
        "horizontal": bool,
        "vertical": bool,
    },
    "pager": {
        "showline_numbers": bool,
        "no_soft_wrap": bool,
        "soft_wrap": bool,
        "timeout": str,  # "0s"
        "foreground": str,  # ""
        "background": str,  # ""
        "line_number_foreground": str,  # "237"
        "line_number_background": str,  # ""
        "match_foreground": str,  # "212"
        "match_background": str,  # ""
        "match_highlight_foreground": str,  # "235"
        "match_highlight_background": str,  # "225"
        "help_foreground": str,  # "241"
        "help_background": str,
    },
    "spin": {
        "show_output": bool,
        "show_error": bool,
        "show_stdout": bool,
        "show_stderr": bool,
        "spinner": str,  # "dot"
        "title": str,  # "Loading..."
        "align": str,  # "left"
        "timeout": str,  # "0s"
    },
    "table": {
        "separator": str,  # ","
        "columns": str,
        "widths": str,
        "height": int,  # 0
        "print": bool,
        "file": str,  # ""
        "border": str,  # "rounded"
        "no_show_help": bool,
        "show_help": bool,
        "no_hide_count": bool,
        "hide_count": bool,
        "lazy_quotes": bool,
        "fields_per_record": int,  # 0
        "return_column": int,  # 0
        "timeout": str,  # "0s"
        "border_foreground": str,  # ""
        "border_background": str,  # ""
        "cell_foreground": str,  # ""
        "cell_background": str,  # ""
        "header_foreground": str,  # ""
        "header_background": str,  # ""
        "selected_foreground": str,  # ""
        "selected_background": str,  # ""
    },
    "write": {
        "width": int,  # 0
        "height": int,  # 5
        "header": str,  # ""
        "placeholder": str,  # "Write something_.."
        "prompt": str,  # "|  "
        "show_cursor_line": bool,
        "show_line_numbers": bool,
        "value": str,  # ""
        "char_limit": int,  # 0
        "max_lines": int,  # 0
        "no_show_help": bool,
        "show_help": bool,
        "cursor_mode": str,  # "blink"
        "timeout": str,  # "0s"
        "no_strip_ansi": bool,
        "strip_ansi": bool,
        "base_foreground": str,  # ""
        "base_background": str,  # ""
        "cursor_line_number_foreground": str,  # "7"
        "cursor_line_number_background": str,  # ""
        "cursor_line_foreground": str,  # ""
        "cursor_line_background": str,  # ""
        "cursor_foreground": str,  # "212"
        "cursor_background": str,  # ""
        "end_of_buffer_foreground": str,  # "0"
        "end_of_buffer_background": str,  # ""
        "line_number_foreground": str,  # "7"
        "line_number_background": str,  # ""
        "header_foreground": str,  # "240"
        "header_background": str,  # ""
        "placeholder_foreground": str,  # "240"
        "placeholder_background": str,  # ""
        "prompt_foreground": str,  # "7"
        "prompt_background": str,  # ""
    },
    "log": {
        "file": str,  # ""
        "format": bool,
        "formatter": str,  # "text"
        "level": str,  # "none"
        "prefix": str,  # ""
        "structured": bool,
        "time": str,  # ""
        "min_level": str,  # ""
        "level_foreground": str,  # ""
        "level_background": str,  # ""
        "time_foreground": str,  # ""
        "time_background": str,  # ""
        "prefix_foreground": str,  # ""
        "prefix_background": str,  # ""
        "message_foreground": str,  # ""
        "message_background": str,  # ""
        "key_foreground": str,  # ""
        "key_background": str,  # ""
        "value_foreground": str,  # ""
        "value_background": str,  # ""
        "separator_foreground": str,  # ""
        "separator_background": str,  # ""
    },
    "version_check": {
        "help": bool,
        "version": bool,
    },
}
