## combat_act1_station_justice.rpy — Narrative combat: Station Justice Contract
## Chapter 19 combat encounter

label combat_act1_station_justice:
    $ _nc = NarrativeCombat("act1_station_justice")
    show screen combat_hud(_nc)

    narrator "{i}The station's so-called justice involves enforcers who don't ask questions. Today, the questions are yours.{/i}"

    menu:
        "Choose your approach:"

        "Confront the enforcers directly [[Combat vs DC 14]]":
            $ _sc = skill_check("combat", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}Success. The path forward opens.{/i}"
            else:
                narrator "{i}It doesn't go as planned. But you adapt.{/i}"

        "Use the station's own protocols against them [[Intelligence vs DC 13]]":
            $ _sc = skill_check("intelligence", 13, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}The approach works. Better than expected.{/i}"
            else:
                narrator "{i}Close. Not close enough.{/i}"

        "Create a diversion — buy time for the client [[Deception vs DC 12]]":
            $ _sc = skill_check("deception", 12, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}Unconventional. Effective.{/i}"
            else:
                narrator "{i}The gamble doesn't pay off. Fallback positions.{/i}"

    $ game_state.mark_encounter_cleared("act1_station_justice")
    hide screen combat_hud
    narrator "{i}Justice served. Not the station's kind — yours.{/i}"
    return
