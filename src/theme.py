"""Design system for 'TUNTAS' — a B5 practical problem-solving book.

B5 = 176 x 250 mm. All sizes in millimetres are converted via mm().
"""
from reportlab.lib.colors import HexColor
from reportlab.lib.units import mm

# ---------------------------------------------------------------- geometry
PAGE_W = 176 * mm
PAGE_H = 250 * mm

MARGIN_TOP = 17 * mm
MARGIN_BOTTOM = 17 * mm
MARGIN_INNER = 20 * mm
MARGIN_OUTER = 16 * mm

LIVE_W = PAGE_W - MARGIN_INNER - MARGIN_OUTER

BLEED = 3 * mm

# ---------------------------------------------------------------- palette
INK = HexColor("#141821")
NAVY = HexColor("#152746")
NAVY_DEEP = HexColor("#0C1B33")
ACCENT = HexColor("#E8503A")      # coral - energy, hooks, D-steps
ACCENT_SOFT = HexColor("#FDEAE6")
TEAL = HexColor("#0F7B6C")        # tools, frameworks
TEAL_SOFT = HexColor("#E3F2EF")
AMBER = HexColor("#C98A0B")       # insight / best practice
AMBER_SOFT = HexColor("#FDF3DC")
VIOLET = HexColor("#5B4B9E")
VIOLET_SOFT = HexColor("#EDE9F7")
GREY = HexColor("#6C7480")
GREY_LIGHT = HexColor("#E4E7EC")
PAPER = HexColor("#FFFFFF")
SOFT = HexColor("#F6F4EF")
CREAM = HexColor("#FBF9F4")
LINE = HexColor("#D8D3C7")
GREEN = HexColor("#1E7A45")
GREEN_SOFT = HexColor("#E4F3E9")
RED = HexColor("#B3331F")
RED_SOFT = HexColor("#FBE7E3")

# ---------------------------------------------------------------- type
FONT_SERIF = "Lora"
FONT_SERIF_IT = "Lora-It"
FONT_SERIF_B = "Lora-Bold"
FONT_SERIF_BI = "Lora-BoldIt"
FONT_SANS = "Inter"
FONT_SANS_M = "Inter-Md"
FONT_SANS_SB = "Inter-Sb"
FONT_SANS_B = "Inter-Bold"

SIZE_BODY = 9.7
LEAD_BODY = 15.0

SIZE_H1 = 30
SIZE_H2 = 16
SIZE_H3 = 11.5
SIZE_SMALL = 7.8
SIZE_TINY = 6.8
SIZE_CAPTION = 8.2
SIZE_PULL = 15

# ---------------------------------------------------------------- D-step colours
STEP_COLORS = {
    "D1": HexColor("#E8503A"),
    "D2": HexColor("#E07A1F"),
    "D3": HexColor("#C9A227"),
    "D4": HexColor("#2F8F5B"),
    "D5": HexColor("#0F7B6C"),
    "D6": HexColor("#2C6BA8"),
    "D7": HexColor("#5B4B9E"),
}
