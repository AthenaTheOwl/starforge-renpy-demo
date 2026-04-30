## bee_overlay.rpy — BEE protocol display overlay
##
## Shows BEE:: protocol messages in amber monospace style above the textbox.

screen bee_overlay(bee_data):
    zorder 90
    modal False

    if bee_data:
        frame:
            xalign 0.5
            yalign 0.68
            xsize 900
            padding (20, 12, 20, 12)
            background Solid("#0a0a0fdd")

            vbox:
                spacing 4

                ## Protocol header
                text "{size=-4}{color=#f1c40f80}BEE PROTOCOL{/color}{/size}":
                    xalign 0.0

                ## Message
                if bee_data.get("message", ""):
                    text "{color=#f1c40f}[bee_data['message']]{/color}":
                        size 22

                ## Status line
                if bee_data.get("status", ""):
                    text "{color=#f1c40f80}[bee_data['status']]{/color}":
                        size 18

                ## Detail line
                if bee_data.get("detail", ""):
                    text "{color=#f1c40f60}[bee_data['detail']]{/color}":
                        size 16
