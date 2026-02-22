import arcade
import re
import ast


W, H = 1200, 720
TITLE = "Level Editor (Arcade) — GD-like"

CELL = 60

GRID_W = 32
GRID_H = 14

PANEL_H = 180
TOPBAR_H = 62

BG = (10, 10, 10)
GRID_LINE = (40, 40, 40)
UI_BG = (18, 18, 18)
UI_CARD = (26, 26, 26)
UI_BORDER = (80, 80, 80)
UI_TEXT = (235, 235, 235)
UI_TEXT_MUTED = (160, 160, 160)
ACCENT = (90, 255, 120)

CAM_SPEED_CELLS = 14.0
CAM_SPEED_FAST = 30.0

TOOLS = [
    ("Куб",           ("block", None, None)),
    ("Прозр. блок",   ("emptyblock", None, None)),
    ("Полублок ↑",    ("halfblock", None, "up")),
    ("Полублок ↓",    ("halfblock", None, "down")),
    ("Шип ↑",         ("spike", "up", None)),
    ("Шип ↓",         ("spike", "down", None)),
    ("Шип ←",         ("spike", "left", None)),
    ("Шип →",         ("spike", "right", None)),
    ("Мини ↑ (ниж)",  ("smallspike", "up", "down")),
    ("Мини ↓ (верх)", ("smallspike", "down", "up")),
    ("Мини ← (ниж)",  ("smallspike", "left", "down")),
    ("Мини → (ниж)",  ("smallspike", "right", "down")),
]


def clamp(v, a, b):
    return max(a, min(b, v))


def tri_points(x, y, w, h, direction: str):
    d = (direction or "up").lower()
    pad = 6
    if d == "up":
        return (x + pad, y), (x + w - pad, y), (x + w / 2, y + h - pad)
    if d == "down":
        return (x + pad, y + h), (x + w - pad, y + h), (x + w / 2, y + pad)
    if d == "left":
        return (x + w, y + pad), (x + w, y + h - pad), (x + pad, y + h / 2)
    return (x, y + pad), (x, y + h - pad), (x + w - pad, y + h / 2)


def format_level(level_list):
    lines = ["LEVEL = ["]
    for entry in level_list:
        lines.append(f"    {entry},")
    lines.append("]")
    return "\n".join(lines)


def _tk_clip_set(text: str):
    try:
        import tkinter as tk
        r = tk.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()
        return True
    except Exception:
        return False


def _tk_clip_get():
    try:
        import tkinter as tk
        r = tk.Tk()
        r.withdraw()
        text = r.clipboard_get()
        r.destroy()
        return text
    except Exception:
        return ""


def parse_level_from_text(text: str):
    if not text:
        return None

    t = text.strip()

    m = re.search(r"LEVEL\s*=\s*(\[[\s\S]*\])", t)
    if m:
        t = m.group(1).strip()

    if not (t.startswith("[") and t.endswith("]")):
        if "(" in t and ")" in t:
            t = "[" + t + "]"

    try:
        val = ast.literal_eval(t)
    except Exception:
        return None

    if not isinstance(val, list):
        return None

    out = []
    for item in val:
        if isinstance(item, (tuple, list)) and len(item) >= 3:
            out.append(tuple(item))
    return out


class UIButton:
    def __init__(self, x, y, w, h, text):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.text = text
        self.hover = False

    def contains(self, mx, my):
        return self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h

    def draw(self):
        bg = (40, 40, 40) if not self.hover else (55, 55, 55)
        arcade.draw_lbwh_rectangle_filled(self.x, self.y, self.w, self.h, bg)
        arcade.draw_lbwh_rectangle_outline(self.x, self.y, self.w, self.h, (235, 235, 235), border_width=2)
        arcade.draw_text(
            self.text,
            self.x + self.w / 2,
            self.y + self.h / 2,
            (240, 240, 240),
            16,
            anchor_x="center",
            anchor_y="center",
        )


class ToolButton:
    def __init__(self, x, y, w, h, label, tool):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.label = label
        self.tool = tool
        self.hover = False

    def contains(self, mx, my):
        return self.x <= mx <= self.x + self.w and self.y <= my <= self.y + self.h

    def draw(self, selected=False):
        bg = UI_CARD
        if selected:
            bg = (34, 52, 34)
        elif self.hover:
            bg = (34, 34, 34)

        arcade.draw_lbwh_rectangle_filled(self.x, self.y, self.w, self.h, bg)
        arcade.draw_lbwh_rectangle_outline(
            self.x, self.y, self.w, self.h,
            ACCENT if selected else UI_BORDER,
            border_width=2
        )

        icon_x = self.x + 10
        icon_y = self.y + 10
        icon_w = 44
        icon_h = self.h - 20
        kind, d, half = self.tool

        arcade.draw_lbwh_rectangle_outline(icon_x, icon_y, icon_w, icon_h, (70, 70, 70), border_width=1)

        if kind == "block":
            arcade.draw_lbwh_rectangle_filled(icon_x + 2, icon_y + 2, icon_w - 4, icon_h - 4, (60, 60, 60))
            arcade.draw_lbwh_rectangle_outline(icon_x + 2, icon_y + 2, icon_w - 4, icon_h - 4, (150, 150, 150), 2)
        elif kind == "emptyblock":
            arcade.draw_lbwh_rectangle_outline(icon_x + 2, icon_y + 2, icon_w - 4, icon_h - 4, (230, 230, 230), 2)
            arcade.draw_lbwh_rectangle_outline(icon_x + 6, icon_y + 6, icon_w - 12, icon_h - 12, (120, 120, 120), 1)
        elif kind == "halfblock":
            hh = (icon_h - 4) / 2
            by = icon_y + 2 + (hh if half == "up" else 0)
            arcade.draw_lbwh_rectangle_filled(icon_x + 2, by, icon_w - 4, hh, (60, 60, 60))
            arcade.draw_lbwh_rectangle_outline(icon_x + 2, by, icon_w - 4, hh, (150, 150, 150), 2)
        elif kind in ("spike", "smallspike"):
            y0 = icon_y + 2
            h0 = icon_h - 4
            if kind == "smallspike":
                h0 = (icon_h - 4) / 2
                y0 = icon_y + 2 + (h0 if half == "up" else 0)
            p1, p2, p3 = tri_points(icon_x + 2, y0, icon_w - 4, h0, d or "up")
            arcade.draw_triangle_filled(*p1, *p2, *p3, (230, 230, 230))

        arcade.draw_text(
            self.label,
            self.x + 64,
            self.y + self.h / 2,
            UI_TEXT,
            14,
            anchor_y="center",
        )


class LevelEditor(arcade.Window):
    def __init__(self):
        super().__init__(W, H, TITLE, resizable=True, update_rate=1 / 60)
        arcade.set_background_color(BG)

        self.cam_cell_x = 0.0
        self.cells = {}
        self.tool_buttons = []
        self.selected_tool_idx = 0

        self.btn_save = UIButton(0, 0, 140, 38, "Сохранить")
        self.btn_load = UIButton(0, 0, 140, 38, "Загрузить")

        self.hover_cell = None
        self.pan_active = False
        self.move_left = False
        self.move_right = False

        self.sel_active = False
        self.sel_start = None
        self.sel_end = None
        self.selected_cells = set()

        self.clip_payload = None
        self._rebuild_ui()

    def _topbar_y(self):
        return max(0, self.height - TOPBAR_H)

    def _grid_origin(self):
        ox = 18
        oy = PANEL_H + 14
        return ox, oy

    def _grid_rect(self):
        ox, oy = self._grid_origin()
        gw = GRID_W * CELL
        gh = GRID_H * CELL
        return ox, oy, gw, gh

    def _rebuild_ui(self):
        topbar_y = self._topbar_y()
        btn_y = clamp(topbar_y + (TOPBAR_H - 38) / 2, 2, max(2, self.height - 40))
        self.btn_save = UIButton(14, btn_y, 150, 38, "Сохранить")
        self.btn_load = UIButton(14 + 160, btn_y, 150, 38, "Загрузить")

        self.tool_buttons.clear()
        pad_x = 18
        btn_w = 240
        btn_h = 40
        col_gap = 12
        row_gap = 10

        max_cols = max(1, (self.width - 2 * pad_x) // (btn_w + col_gap))
        col = 0
        row = 0
        base_y = 18

        for label, tool in TOOLS:
            bx = pad_x + col * (btn_w + col_gap)
            by = base_y + row * (btn_h + row_gap)
            self.tool_buttons.append(ToolButton(bx, by, btn_w, btn_h, label, tool))
            col += 1
            if col >= max_cols:
                col = 0
                row += 1

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self._rebuild_ui()

    def on_draw(self):
        self.clear()

def main():
    LevelEditor()
    arcade.run()


if __name__ == "__main__":
    main()