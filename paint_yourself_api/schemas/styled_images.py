from enum import Enum


class StyledImageThemeEnum(str, Enum):
    """Enum containing the allowed themes."""

    VAN_GOGH = "van-gogh"
    CLAUDE_MONET = "claude-monet"
    REMBRANDT = "rembrandt"
    WHISTLER = "whistler"
    PICASSO = "picasso"
    DA_VINCI = "da-vinci"
    CARAVAGGIO = "caravaggio"
