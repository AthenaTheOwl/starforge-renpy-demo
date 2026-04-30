## gui.rpy — Gothic-noir cyberpunk theme for Starforge Canticles

init python:
    gui.init(1920, 1080)

## Colors — dark hull plating, cold steel blue accents, amber speaker names
define gui.accent_color = "#4a90d9"
define gui.idle_color = "#808090"
define gui.idle_small_color = "#606070"
define gui.hover_color = "#4a90d9"
define gui.selected_color = "#d4a843"
define gui.insensitive_color = "#40404080"
define gui.muted_color = "#505064"
define gui.hover_muted_color = "#606078"

define gui.text_color = "#c0c0d0"
define gui.interface_text_color = "#c0c0d0"

## Textbox
define gui.textbox_height = 278
define gui.textbox_yalign = 1.0

## Speaker name
define gui.name_text_color = "#d4a843"
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.name_text_size = 30

## Dialogue text
define gui.text_xpos = 402
define gui.text_ypos = 60
define gui.text_xalign = 0.0
define gui.text_size = 28
define gui.text_font = "DejaVuSans.ttf"
define gui.dialogue_width = 1116

## Button defaults
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_font = gui.text_font
define gui.button_text_size = gui.text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Choice buttons
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = 28
define gui.choice_button_text_xalign = 0.0
define gui.choice_button_text_idle_color = "#808090"
define gui.choice_button_text_hover_color = "#4a90d9"
define gui.choice_button_text_insensitive_color = "#40404080"

## Slot buttons (save/load)
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 20
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

## Navigation
define gui.navigation_xpos = 60
define gui.navigation_ypos = 0.5
define gui.navigation_spacing = 6

## Scrollbar
define gui.scrollbar_size = 18
define gui.scrollbar_tile = False

## Quick menu text
define gui.quick_button_text_size = 20
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Dialogue window background
init python:
    config.window = None

## Background color for letterboxing
define gui.game_menu_background = "#0a0a0f"
define gui.main_menu_background = "#0a0a0f"

## Spacing
define gui.pref_button_spacing = 0
define gui.page_spacing = 0
define gui.pref_spacing = 15

## Frame styling
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.skip_frame_borders = Borders(24, 8, 75, 8)
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Bar styling
define gui.bar_size = 38
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.bar_tile = False
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vbar_tile = False

## History
define config.history_length = 250
define gui.history_height = 210
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0

## NVL
define gui.nvl_height = 180

## Transitions
define slow_fade = Fade(0.5, 0.5, 0.5)
define chapter_fade = Fade(1.0, 1.0, 1.0)
define quick_dissolve = Dissolve(0.3)
define scene_dissolve = Dissolve(0.8)
