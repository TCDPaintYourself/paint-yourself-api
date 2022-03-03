from enum import Enum


class StyledImageThemeEnum(str, Enum):
    """Enum containing the allowed themes."""

    van_gogh = "van-gogh"
    claude_monet = "claude-monet"
    rembrandt = "rembrandt"
    whistler = "whistler"
    picasso = "picasso"
    da_vinci = "da-vinci"
    caravaggio = "caravaggio"
