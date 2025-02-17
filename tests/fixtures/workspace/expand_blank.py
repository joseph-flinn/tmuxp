"""Expected expanded configuration for empty workspace panes."""

from __future__ import annotations

expected = {
    "session_name": "Blank pane test",
    "windows": [
        {
            "window_name": "Blank pane test",
            "panes": [
                {"shell_command": []},
                {"shell_command": []},
                {"shell_command": []},
            ],
        },
        {
            "window_name": "More blank panes",
            "panes": [
                {"shell_command": []},
                {"shell_command": []},
                {"shell_command": []},
            ],
        },
        {
            "window_name": "Empty string (return)",
            "panes": [
                {"shell_command": [{"cmd": ""}]},
                {"shell_command": [{"cmd": ""}]},
                {"shell_command": [{"cmd": ""}]},
            ],
        },
        {
            "window_name": "Blank with options",
            "panes": [
                {"shell_command": [], "focus": True},
                {"shell_command": [], "start_directory": "/tmp"},
            ],
        },
    ],
}
