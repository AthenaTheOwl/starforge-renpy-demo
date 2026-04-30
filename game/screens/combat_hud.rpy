## combat_hud.rpy — Narrative combat HUD overlay
##
## Shows party HP, enemy HP, heat gauge, and CLI meter during combat.

screen combat_hud(combat):
    zorder 80
    modal False

    ## Party HP bars (top-left)
    vbox:
        xpos 20
        ypos 20
        spacing 6

        text "{size=-2}{color=#4a90d9}PARTY{/color}{/size}"

        for char_id in combat.party_hp:
            $ _hp = combat.party_hp[char_id]
            $ _max_hp = combat.party_max_hp.get(char_id, 100)
            $ _name = char_id.title()
            $ _pct = float(_hp) / float(_max_hp) if _max_hp > 0 else 0.0

            hbox:
                spacing 8

                text "[_name]":
                    size 18
                    color "#c0c0d0"
                    min_width 80

                bar:
                    value _pct
                    range 1.0
                    xsize 120
                    ysize 12
                    yalign 0.5
                    left_bar Solid("#2ecc71" if _pct > 0.5 else ("#e67e22" if _pct > 0.25 else "#e74c3c"))
                    right_bar Solid("#1a1a2e")

                text "[_hp]/[_max_hp]":
                    size 16
                    color "#808090"

    ## Enemy HP bars (top-right)
    vbox:
        xalign 1.0
        xoffset -20
        ypos 20
        spacing 6

        text "{size=-2}{color=#e74c3c}ENEMIES{/color}{/size}":
            xalign 1.0

        for enemy_key in combat.enemy_hp:
            $ _ehp = combat.enemy_hp[enemy_key]
            $ _emax = combat.enemy_max_hp.get(enemy_key, 50)
            $ _ename = combat.enemy_names.get(enemy_key, enemy_key)
            $ _epct = float(_ehp) / float(_emax) if _emax > 0 else 0.0

            hbox:
                spacing 8
                xalign 1.0

                text "[_ename]":
                    size 18
                    color "#c0c0d0"
                    min_width 100

                bar:
                    value _epct
                    range 1.0
                    xsize 120
                    ysize 12
                    yalign 0.5
                    left_bar Solid("#e74c3c")
                    right_bar Solid("#1a1a2e")

                text "[_ehp]/[_emax]":
                    size 16
                    color "#808090"

    ## Heat and CLI (bottom-left, above textbox)
    hbox:
        xpos 20
        yalign 1.0
        yoffset -290
        spacing 30

        if hasattr(combat, 'heat'):
            vbox:
                text "{size=-2}{color=#e67e22}HEAT{/color}{/size}"
                $ _heat = combat.heat.get(combat.active_character, 0)
                bar:
                    value _heat
                    range 5
                    xsize 100
                    ysize 10
                    left_bar Solid("#e67e22" if _heat < 4 else "#e74c3c")
                    right_bar Solid("#1a1a2e")

        if hasattr(combat, 'cli'):
            vbox:
                text "{size=-2}{color=#9b59b6}CLI{/color}{/size}"
                bar:
                    value combat.cli
                    range 10.0
                    xsize 100
                    ysize 10
                    left_bar Solid("#9b59b6")
                    right_bar Solid("#1a1a2e")
