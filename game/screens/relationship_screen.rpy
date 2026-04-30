## relationship_screen.rpy — Character affinity and relationship tier viewer

screen relationship_screen():
    tag menu
    use game_menu(_("Relationships"), scroll="viewport"):
        style_prefix "rel"

        vbox:
            spacing 20

            for char_id in ["elia", "elisira", "vesper", "jalen", "nyx", "rho"]:
                $ _aff = relationship_manager.get_affinity(char_id)
                $ _tier = relationship_manager.get_tier_name(char_id)
                $ _name = relationship_manager.CHARACTERS[char_id]["name"]
                $ _pct = float(_aff) / 100.0

                frame:
                    xsize 600
                    padding (20, 15, 20, 15)
                    background Solid("#1a1a2e")

                    vbox:
                        spacing 8

                        hbox:
                            text "[_name]":
                                size 26
                                color "#c0c0d0"

                            text "  [_tier]":
                                size 20
                                color "#4a90d9"
                                yalign 0.5

                        bar:
                            value _pct
                            range 1.0
                            xsize 560
                            ysize 14
                            left_bar Solid("#4a90d9")
                            right_bar Solid("#0a0a0f")

                        ## Tier markers
                        hbox:
                            spacing 0
                            xsize 560

                            text "0":
                                size 14
                                color "#606060"
                                xpos 0

                            text "10":
                                size 14
                                color "#606060"
                                xpos int(560 * 0.10) - 8

                            text "25":
                                size 14
                                color "#606060"
                                xpos int(560 * 0.25) - 8

                            text "45":
                                size 14
                                color "#606060"
                                xpos int(560 * 0.45) - 8

                            text "70":
                                size 14
                                color "#606060"
                                xpos int(560 * 0.70) - 8

            ## AI Citizens (collapsed)
            null height 10
            text "{size=-2}{color=#43d4a8}AI Citizens{/color}{/size}"

            for char_id in ["waffle", "bubbles", "cinnamon", "souffle"]:
                if char_id in relationship_manager.CHARACTERS:
                    $ _aff = relationship_manager.get_affinity(char_id)
                    $ _tier = relationship_manager.get_tier_name(char_id)
                    $ _name = relationship_manager.CHARACTERS[char_id]["name"]

                    hbox:
                        spacing 15
                        text "[_name]":
                            size 20
                            color "#808090"
                            min_width 120
                        text "[_tier] ([_aff])":
                            size 18
                            color "#43d4a8"
