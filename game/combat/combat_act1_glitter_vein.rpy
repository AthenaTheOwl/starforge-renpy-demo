## combat_act1_glitter_vein.rpy — Narrative combat: Glitter Vein Contract
## Chapter 4 combat encounter

label combat_act1_glitter_vein:
    $ _nc = NarrativeCombat("act1_glitter_vein")
    show screen combat_hud(_nc)

    narrator "{i}The Glitter Vein mine is contested territory. Armed claim-jumpers block the way forward.{/i}"

    menu:
        "Choose your approach:"

        "Direct engagement — clear the corridor":
            $ _result = _nc.resolve_attack("avyanna", "strike", "claim_jumper_1")
            call screen dice_roll_screen
            if _result["hit"]:
                narrator "{i}The strike connects. The corridor opens.{/i}"
            else:
                narrator "{i}They push back. Harder than expected.{/i}"

        "Coordinate with Rho — suppressive fire":
            $ _sc = skill_check("tactics", 13, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}Rho's cannon persuades them to reconsider their life choices.{/i}"
            else:
                narrator "{i}The coordination breaks down under fire.{/i}"

        "Find an alternate route — avoid the fight":
            $ _sc = skill_check("perception", 12, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                narrator "{i}A maintenance shaft. Tight, but passable. The jumpers never see you.{/i}"
                $ game_state.set_flag("glitter_vein_stealth")
            else:
                narrator "{i}No route. You'll have to go through them.{/i}"

    $ game_state.mark_encounter_cleared("act1_glitter_vein")
    hide screen combat_hud
    narrator "{i}The Glitter Vein is secured. The contract holds.{/i}"
    return
