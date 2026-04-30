## memories_screen.rpy — Memories gallery for NG+ cross-playthrough moments
##
## Displays recorded story memories in a scrollable list with gothic-noir styling.

screen memories():
    tag menu
    use game_menu(_("Memories"), scroll="viewport"):
        style_prefix "memories"

        vbox:
            spacing 20

            text "Echoes of Past Journeys":
                style "memories_heading"

            if persistent.memories:
                for mem_id, mem_data in persistent.memories.items():
                    frame:
                        style "memories_entry_frame"
                        vbox:
                            spacing 6
                            if isinstance(mem_data, dict):
                                text mem_data.get("title", mem_id.replace("_", " ").title()):
                                    style "memories_title"
                                text mem_data.get("text", ""):
                                    style "memories_text"
                            else:
                                # Legacy format: plain string
                                text mem_id.replace("_", " ").title():
                                    style "memories_title"
                                text str(mem_data):
                                    style "memories_text"
            else:
                text "No memories yet. Complete chapters to unlock them.":
                    style "memories_text"

style memories_heading:
    color "#d4a843"
    size 32
    bold True
    xalign 0.5

style memories_entry_frame:
    background Solid("#12121a")
    padding (20, 16, 20, 16)
    xfill True

style memories_title:
    color "#d4a843"
    size 22
    bold True

style memories_text:
    color "#b0b0c0"
    size 18

style memories_vbox:
    xfill True
