"""Internal, :const:`typing.TYPE_CHECKING` guarded :term:`typings <annotation>`.

These are _not_ to be imported at runtime as `typing_extensions` is not
bundled with tmuxp. Usage example:

>>> import typing as t

>>> if t.TYPE_CHECKING:
...     from tmuxp._internal.types import PluginConfigSchema
...
"""

from __future__ import annotations

from typing_extensions import NotRequired, TypedDict


class PluginConfigSchema(TypedDict):
    plugin_name: NotRequired[str]
    tmux_min_version: NotRequired[str]
    tmux_max_version: NotRequired[str]
    tmux_version_incompatible: NotRequired[list[str]]
    libtmux_min_version: NotRequired[str]
    libtmux_max_version: NotRequired[str]
    libtmux_version_incompatible: NotRequired[list[str]]
    tmuxp_min_version: NotRequired[str]
    tmuxp_max_version: NotRequired[str]
    tmuxp_version_incompatible: NotRequired[list[str]]
