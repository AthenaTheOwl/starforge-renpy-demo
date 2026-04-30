## combat_act1_breach_hymn.rpy — Narrative combat: Breach Hymn
## Chapter 16 combat encounter

label combat_act1_breach_hymn:
    $ _nc = NarrativeCombat("act1_breach_hymn")
    show screen combat_hud(_nc)

    narrator "{i}The hull breach alarm screams. Hostiles pouring through the gap in the Lumen Thief's skin.{/i}"

    menu:
        "Choose your approach:"

        "Seal the breach while fighting [[Engineering vs DC 14]]":
            $ _sc = skill_check("engineering", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}Success. The path forward opens.{/i}"
            else:
                narrator "{i}It doesn't go as planned. But you adapt.{/i}"

        "Hold the corridor — let no one through [[Combat vs DC 13]]":
            $ _sc = skill_check("combat", 13, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}The approach works. Better than expected.{/i}"
            else:
                narrator "{i}Close. Not close enough.{/i}"

        "Vent the section — risky but decisive [[Tactics vs DC 15]]":
            $ _sc = skill_check("tactics", 15, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}Unconventional. Effective.{/i}"
            else:
                narrator "{i}The gamble doesn't pay off. Fallback positions.{/i}"

    $ game_state.mark_encounter_cleared("act1_breach_hymn")
    hide screen combat_hud
    narrator "{i}The breach is sealed. The ship holds. The crew holds.{/i}"
    return
