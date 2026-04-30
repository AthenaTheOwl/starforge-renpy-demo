## screens.rpy — Core screen definitions for Starforge Canticles
##
## Minimal screens.rpy — provides the essential screens Ren'Py requires.
## Custom screens (hub, dice roll, combat HUD) live in game/screens/.

################################################################################
## Say Screen — displays dialogue
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#0a0a0fcc")

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize None
    ypos gui.name_ypos
    padding (5, 5, 5, 5)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    color gui.name_text_color
    size gui.name_text_size

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.text_xpos
    xanchor gui.text_xalign
    ypos gui.text_ypos
    xsize gui.dialogue_width
    color gui.text_color

style button:
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2a1ecc")
    selected_hover_background Solid("#3a3a2ecc")
    insensitive_background Solid("#0f0f16aa")
    selected_insensitive_background Solid("#161620aa")
    padding (12, 6, 12, 6)

style button_text:
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
    insensitive_color gui.insensitive_color

################################################################################
## Choice Screen — displays player choices
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        ypos 405
        yanchor 0.5
        spacing 12

        for i in items:
            textbutton i.caption action i.action:
                style "choice_button"

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 12

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize gui.choice_button_width
    padding (20, 8, 20, 8)
    background Solid("#1a1a2ecc")
    hover_background Solid("#2a2a4ecc")

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color
    size gui.choice_button_text_size

################################################################################
## Quick Menu
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -8

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

style quick_button:
    properties gui.button_properties("quick_button")
    background Solid("#101018cc")
    hover_background Solid("#1b1b2ecc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0c0c12aa")
    selected_insensitive_background Solid("#1a1810aa")
    padding (12, 6, 12, 6)

style quick_button_text:
    properties gui.text_properties("quick_button")
    size gui.quick_button_text_size
    idle_color gui.quick_button_text_idle_color
    hover_color gui.hover_color
    selected_color gui.quick_button_text_selected_color

default quick_menu = True

init python:
    config.overlay_screens.append("quick_menu")

################################################################################
## Main Menu
################################################################################

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add Solid("#0a0a0f")

    frame:
        pass

    vbox:
        xalign 0.5
        yalign 0.3

        text "{size=+20}STARFORGE CANTICLES{/size}":
            xalign 0.5
            color "#4a90d9"

        null height 10

        text "Gothic-noir space opera":
            xalign 0.5
            size 22
            color "#808090"

        null height 6

        text "Act 1: The Lumen Thief" xalign 0.5 size 20 color "#d4a843"

    text "v0.1 — Early Development" xalign 0.05 yalign 0.95 size 14 color "#404050"

    vbox:
        xalign 0.5
        yalign 0.65
        spacing 12

        textbutton _("New Game") action Start():
            xalign 0.5
        textbutton _("Load Game") action ShowMenu("load"):
            xalign 0.5
        textbutton _("Preferences") action ShowMenu("preferences"):
            xalign 0.5
        if persistent.memories:
            textbutton _("Memories") action ShowMenu("memories"):
                xalign 0.5
        textbutton _("Quit") action Quit(confirm=not main_menu):
            xalign 0.5

    ## NG+ indicator
    if persistent.playthrough_count and persistent.playthrough_count > 0:
        text "NG+ (Playthrough [persistent.playthrough_count + 1])":
            xalign 0.95
            yalign 0.95
            size 18
            color "#d4a843"

style main_menu_frame:
    xsize 420
    yfill True
    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)
    xalign 1.0

################################################################################
## Game Menu (base for save, load, preferences)
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add Solid("#0a0a0f")

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title:
        style "game_menu_label"

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background Solid("#0a0a0fdd")

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 50
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45

style return_button_text:
    properties gui.text_properties("navigation_button")
    color gui.idle_color
    hover_color gui.hover_color

################################################################################
## File Slots (Save/Load)
################################################################################

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            grid 3 3:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 15

                for i in range(1, 10):
                    button:
                        action FileAction(i)
                        has vbox

                        add FileScreenshot(i):
                            xsize gui.slot_button_width - 30
                            ysize (gui.slot_button_width - 30) * 9 // 16

                        text FileTime(i, format=_("{#file_time}%%A, %%B %%d %%Y, %%H:%%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(i):
                            style "slot_name_text"

                        $ _save_info = FileJson(i)
                        if _save_info:
                            text "Chapter [_save_info.get('chapter', '?')]":
                                style "slot_chapter_text"

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing 12

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style slot_button:
    properties gui.button_properties("slot_button")
    xsize gui.slot_button_width
    background Solid("#1a1a2e")
    hover_background Solid("#2a2a4e")
    padding (15, 15, 15, 15)

style slot_button_text:
    properties gui.text_properties("slot_button")
    color gui.idle_small_color

style slot_time_text:
    size gui.slot_button_text_size
    color gui.idle_small_color

style slot_name_text:
    size gui.slot_button_text_size
    color gui.accent_color

style slot_chapter_text:
    size 16
    color "#4a90d9"

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

################################################################################
## Preferences
################################################################################

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height 15

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                vbox:
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")

style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    yalign 1.0
    color gui.accent_color
    size 24

style radio_button:
    properties gui.button_properties("radio_button")
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0f0f16aa")

style radio_button_text:
    properties gui.text_properties("radio_button")
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style check_button:
    properties gui.button_properties("check_button")
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0f0f16aa")

style check_button_text:
    properties gui.text_properties("check_button")
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style bar:
    ysize 18
    left_bar Solid("#4a90d9")
    right_bar Solid("#1a1a2e")

style vbar:
    xsize 18
    top_bar Solid("#4a90d9")
    bottom_bar Solid("#1a1a2e")

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Solid("#11111a")
    thumb Solid("#4a90d9")

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Solid("#11111a")
    thumb Solid("#4a90d9")

style slider:
    ysize 18
    base_bar Solid("#1a1a2e")
    thumb Solid("#d4a843")

style vslider:
    xsize 18
    base_bar Solid("#1a1a2e")
    thumb Solid("#d4a843")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    background Solid("#d4a843")
    hover_background Solid("#f1c40f")
    selected_background Solid("#f1c40f")
    insensitive_background Solid("#6f5d22")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_pref_vbox:
    xsize 600

################################################################################
## History
################################################################################

screen history():
    tag menu
    use game_menu(_("History"), scroll="vpgrid"):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False
                        xpos gui.history_name_xpos
                        ypos gui.history_name_ypos
                        xanchor gui.history_name_xalign
                        xsize gui.history_name_width

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags) if gui.history_allow_tags else h.what
                text what:
                    substitute False
                    xpos gui.history_text_xpos
                    ypos gui.history_text_ypos
                    xanchor gui.history_text_xalign
                    xsize gui.history_text_width

        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = set()

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    color gui.accent_color

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    color gui.text_color

################################################################################
## Confirm
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add Solid("#0a0a0faa")

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame:
    background Solid("#1a1a2eee")
    padding (60, 60, 60, 60)
    xalign .5
    yalign .5

style confirm_prompt:
    xalign 0.5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color gui.text_color
    size 30

style confirm_button:
    properties gui.button_properties("confirm_button")
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0f0f16aa")
    padding (16, 8, 16, 8)

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    color gui.idle_color
    hover_color gui.hover_color

################################################################################
## Navigation
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Relationships") action ShowMenu("relationship_screen")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0f0f16aa")
    padding (18, 10, 18, 10)

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

################################################################################
## Skip Indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "..." at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "..." at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "..." at delayed_blink(0.4, 1.0) style "skip_triangle"

style skip_frame:
    ypos 15
    background Solid("#0a0a0fcc")
    padding (24, 8, 75, 8)

style skip_text:
    size 24
    color gui.accent_color

style skip_triangle:
    font "DejaVuSans.ttf"
    size 24
    color gui.accent_color

################################################################################
## Notify
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame:
    ypos 68
    background Solid("#0a0a0fcc")
    padding (24, 8, 60, 8)

style notify_text:
    properties gui.text_properties("notify")
    color gui.accent_color

################################################################################
## NVL (not used but required by Ren'Py)
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing 15

        use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

style nvl_window:
    xfill True
    yfill True
    background Solid("#0a0a0fdd")
    padding (30, 30, 30, 30)

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos 645
    xanchor 1.0
    ypos 0
    xsize 225

style nvl_dialogue:
    xpos 675
    ypos 12
    xsize 885

style nvl_button:
    properties gui.button_properties("nvl_button")
    background Solid("#14141fcc")
    hover_background Solid("#24243fcc")
    selected_background Solid("#2a2414dd")
    selected_hover_background Solid("#3a3218dd")
    insensitive_background Solid("#0f0f16aa")
    padding (18, 10, 18, 10)
    xpos 675

style nvl_button_text:
    properties gui.text_properties("nvl_button")
