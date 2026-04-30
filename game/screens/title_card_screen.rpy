## title_card_screen.rpy — Chapter title card overlay

screen title_card(chapter_num, chapter_title):
    zorder 100
    modal False

    add Solid("#0a0a0f")

    vbox:
        xalign 0.5
        yalign 0.45
        spacing 15

        if chapter_num == 0:
            text "Prologue":
                size 48
                color "#4a90d9"
                xalign 0.5
        else:
            text "Chapter [chapter_num]":
                size 48
                color "#4a90d9"
                xalign 0.5

        text "[chapter_title]":
            size 36
            color "#d4a843"
            xalign 0.5

    timer 3.0 action Hide("title_card")
