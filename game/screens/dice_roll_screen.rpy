## dice_roll_screen.rpy — Animated d20 skill check display
##
## Shows: [die face] + [modifier] = [total] vs DC [threshold]
## Color-coded: green=success, red=failure, gold=crit

screen dice_roll_screen():
    zorder 150
    modal False

    if last_skill_check:
        $ _check = last_skill_check
        $ _result = _check.get("result", "FAILURE")
        $ _die = _check.get("die_roll", 0)
        $ _mod = _check.get("stat_value", 0)
        $ _total = _check.get("total", 0)
        $ _dc = _check.get("threshold", 10)
        $ _stat = _check.get("stat", "???")
        $ _char = _check.get("character", "???")

        # Result color
        if _result == "CRITICAL_SUCCESS":
            $ _color = "#f1c40f"
            $ _label = "CRITICAL SUCCESS!"
        elif _result == "SUCCESS":
            $ _color = "#2ecc71"
            $ _label = "SUCCESS"
        elif _result == "CRITICAL_FAILURE":
            $ _color = "#e74c3c"
            $ _label = "CRITICAL FAILURE"
        else:
            $ _color = "#e74c3c"
            $ _label = "FAILURE"

        frame:
            xalign 0.5
            yalign 0.3
            padding (40, 30, 40, 30)
            background Solid("#0a0a0fee")

            vbox:
                spacing 12
                xalign 0.5

                ## Stat and character
                text "[_stat.title()] Check ([_char.title()])":
                    color "#808090"
                    size 22
                    xalign 0.5

                ## Dice roll breakdown
                hbox:
                    xalign 0.5
                    spacing 8

                    ## d20 result
                    frame:
                        padding (15, 10, 15, 10)
                        if _die == 20:
                            background Solid("#f1c40f33")
                        elif _die == 1:
                            background Solid("#e74c3c33")
                        else:
                            background Solid("#1a1a2e")

                        text "[_die]":
                            size 48
                            xalign 0.5
                            if _die == 20:
                                color "#f1c40f"
                            elif _die == 1:
                                color "#e74c3c"
                            else:
                                color "#c0c0d0"

                    text "+":
                        size 36
                        color "#808090"
                        yalign 0.5

                    ## Modifier
                    frame:
                        padding (15, 10, 15, 10)
                        background Solid("#1a1a2e")

                        text "[_mod]":
                            size 48
                            color "#4a90d9"
                            xalign 0.5

                    text "=":
                        size 36
                        color "#808090"
                        yalign 0.5

                    ## Total
                    frame:
                        padding (15, 10, 15, 10)
                        background Solid("#1a1a2e")

                        text "[_total]":
                            size 48
                            color "[_color]"
                            xalign 0.5

                    text "vs DC":
                        size 24
                        color "#808090"
                        yalign 0.5

                    ## DC
                    frame:
                        padding (15, 10, 15, 10)
                        background Solid("#1a1a2e")

                        text "[_dc]":
                            size 48
                            color "#c0c0d0"
                            xalign 0.5

                ## Result label
                text "[_label]":
                    size 32
                    color "[_color]"
                    xalign 0.5
                    bold True
