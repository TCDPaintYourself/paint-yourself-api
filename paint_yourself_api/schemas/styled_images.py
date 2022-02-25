from enum import Enum


class StyledImageThemeEnum(str, Enum):
    """Enum containing the allowed themes."""

    van_gogh = "Van Gogh"
    claude_monet = "Claude Monet"
    rembrandt = "Rembrandt"
    whistler = "Whistler"
    picasso = "Picasso"
    da_vinci = "Da Vinci"
    caravaggio = "Caravaggio"
