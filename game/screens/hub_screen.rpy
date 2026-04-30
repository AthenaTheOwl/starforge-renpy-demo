## hub_screen.rpy — Chapter hub for optional dialogue selection
##
## Shows available optional dialogues with NEW badges, lock icons, and advance button.

screen hub_screen(chapter_num, available_scenes):
    modal True
    style_prefix "hub"

    add Solid("#0a0a0fee")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        yminimum 400
        padding (40, 40, 40, 40)
        background Solid("#1a1a2eee")

        vbox:
            spacing 20

            ## Header
            text "{size=+6}[CHAPTER_SEQUENCE[chapter_num]['title']]{/size}":
                color "#4a90d9"
                xalign 0.5

            text "Optional conversations available:":
                color "#808090"
                size 22
                xalign 0.5

            null height 10

            ## Dialogue buttons
            vbox:
                spacing 8

                for d_id in CHAPTER_SEQUENCE[chapter_num].get("optional_scenes", []):
                    $ _d_name = get_dialogue_display_name(d_id)
                    $ _d_played = game_state.has_played_dialogue(d_id)
                    $ _d_available = is_dialogue_available(d_id)
                    $ _d_lock = get_dialogue_lock_reason(d_id)

                    if not _d_played:
                        if _d_available:
                            textbutton "{color=#d4a843}[NEW]{/color} [_d_name]":
                                action Return("play:" + d_id)
                                xsize 700
                                text_size 24
                                text_color "#c0c0d0"
                                text_hover_color "#4a90d9"
                                background Solid("#252540")
                                hover_background Solid("#303060")
                                padding (20, 12, 20, 12)
                        else:
                            textbutton "{color=#555555}{icon=lock} [_d_name]{/color}":
                                action NullAction()
                                xsize 700
                                text_size 24
                                text_color "#555555"
                                background Solid("#1a1a25")
                                padding (20, 12, 20, 12)
                                tooltip "Locked"
                    else:
                        textbutton "{color=#606060}[_d_name] (done){/color}":
                            action NullAction()
                            xsize 700
                            text_size 24
                            text_color "#404050"
                            background Solid("#151520")
                            padding (20, 12, 20, 12)

            null height 20

            ## Advance button
            textbutton "Continue Story":
                action Return("advance")
                xalign 0.5
                text_size 26
                text_color "#d4a843"
                text_hover_color "#f1c40f"
                background Solid("#2a2a1e")
                hover_background Solid("#3a3a2e")
                padding (40, 12, 40, 12)
