## combat_act1_tutorial.rpy — Narrative combat: Tutorial Engagement
## Enemies: 2x Corporate Trooper
## Auto-generated skeleton — add flavor text

label combat_act1_tutorial:
    $ _nc = NarrativeCombat("act1_tutorial")
    show screen combat_hud(_nc)

    "Standard corporate patrol intercepted near the cargo bay. Two troopers providing basic combat training opportunity."

label .round_1:
    $ _nc.advance_round()

    menu:
        "Choose your action:"

        "Strike the nearest enemy [Attack vs DC 12]":
            $ _enemies = _nc.get_living_enemy_keys()
            if _enemies:
                $ _target = _enemies[0]
                $ _result = _nc.resolve_attack("avyanna", "strike", _target)
                call screen dice_roll_screen
                if _result["hit"]:
                    "{i}The strike connects. [_result['damage']] damage.{/i}"
                else:
                    "{i}The strike misses. The enemy sidesteps.{/i}"

        "Hold position and assess [No roll — safe option]":
            "{i}You hold back, watching for an opening.{/i}"

        "Coordinate the crew [Tactics vs DC 14]":
            $ _sc = skill_check("tactics", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                "{i}The crew moves as one. Coordinated fire drops an enemy.{/i}"
                $ _enemies = _nc.get_living_enemy_keys()
                if _enemies:
                    $ _nc.enemy_hp[_enemies[0]] = max(0, _nc.enemy_hp[_enemies[0]] - 15)
            else:
                "{i}The coordination falters. The enemy exploits the gap.{/i}"

    ## Enemy response
    $ _threat = _nc.enemy_threatens()
    if _threat["damage"] > 0:
        "{i}[_threat['narrative']] [_threat['damage']] damage to [_threat['target_name']].{/i}"

    if _nc.is_combat_over():
        jump .combat_end

    jump .round_2

label .round_2:
    $ _nc.advance_round()

    menu:
        "Choose your action:"

        "Strike the nearest enemy [Attack vs DC 12]":
            $ _enemies = _nc.get_living_enemy_keys()
            if _enemies:
                $ _target = _enemies[0]
                $ _result = _nc.resolve_attack("avyanna", "strike", _target)
                call screen dice_roll_screen
                if _result["hit"]:
                    "{i}The strike connects. [_result['damage']] damage.{/i}"
                else:
                    "{i}The strike misses. The enemy sidesteps.{/i}"

        "Hold position and assess [No roll — safe option]":
            "{i}You hold back, watching for an opening.{/i}"

        "Coordinate the crew [Tactics vs DC 14]":
            $ _sc = skill_check("tactics", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                "{i}The crew moves as one. Coordinated fire drops an enemy.{/i}"
                $ _enemies = _nc.get_living_enemy_keys()
                if _enemies:
                    $ _nc.enemy_hp[_enemies[0]] = max(0, _nc.enemy_hp[_enemies[0]] - 15)
            else:
                "{i}The coordination falters. The enemy exploits the gap.{/i}"

    ## Enemy response
    $ _threat = _nc.enemy_threatens()
    if _threat["damage"] > 0:
        "{i}[_threat['narrative']] [_threat['damage']] damage to [_threat['target_name']].{/i}"

    if _nc.is_combat_over():
        jump .combat_end

    jump .round_3

label .round_3:
    $ _nc.advance_round()

    menu:
        "Choose your action:"

        "Strike the nearest enemy [Attack vs DC 12]":
            $ _enemies = _nc.get_living_enemy_keys()
            if _enemies:
                $ _target = _enemies[0]
                $ _result = _nc.resolve_attack("avyanna", "strike", _target)
                call screen dice_roll_screen
                if _result["hit"]:
                    "{i}The strike connects. [_result['damage']] damage.{/i}"
                else:
                    "{i}The strike misses. The enemy sidesteps.{/i}"

        "Hold position and assess [No roll — safe option]":
            "{i}You hold back, watching for an opening.{/i}"

        "Coordinate the crew [Tactics vs DC 14]":
            $ _sc = skill_check("tactics", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                "{i}The crew moves as one. Coordinated fire drops an enemy.{/i}"
                $ _enemies = _nc.get_living_enemy_keys()
                if _enemies:
                    $ _nc.enemy_hp[_enemies[0]] = max(0, _nc.enemy_hp[_enemies[0]] - 15)
            else:
                "{i}The coordination falters. The enemy exploits the gap.{/i}"

    ## Enemy response
    $ _threat = _nc.enemy_threatens()
    if _threat["damage"] > 0:
        "{i}[_threat['narrative']] [_threat['damage']] damage to [_threat['target_name']].{/i}"

    if _nc.is_combat_over():
        jump .combat_end

    jump .round_4

label .round_4:
    $ _nc.advance_round()

    menu:
        "Choose your action:"

        "Strike the nearest enemy [Attack vs DC 12]":
            $ _enemies = _nc.get_living_enemy_keys()
            if _enemies:
                $ _target = _enemies[0]
                $ _result = _nc.resolve_attack("avyanna", "strike", _target)
                call screen dice_roll_screen
                if _result["hit"]:
                    "{i}The strike connects. [_result['damage']] damage.{/i}"
                else:
                    "{i}The strike misses. The enemy sidesteps.{/i}"

        "Hold position and assess [No roll — safe option]":
            "{i}You hold back, watching for an opening.{/i}"

        "Coordinate the crew [Tactics vs DC 14]":
            $ _sc = skill_check("tactics", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                "{i}The crew moves as one. Coordinated fire drops an enemy.{/i}"
                $ _enemies = _nc.get_living_enemy_keys()
                if _enemies:
                    $ _nc.enemy_hp[_enemies[0]] = max(0, _nc.enemy_hp[_enemies[0]] - 15)
            else:
                "{i}The coordination falters. The enemy exploits the gap.{/i}"

    ## Enemy response
    $ _threat = _nc.enemy_threatens()
    if _threat["damage"] > 0:
        "{i}[_threat['narrative']] [_threat['damage']] damage to [_threat['target_name']].{/i}"

    if _nc.is_combat_over():
        jump .combat_end

    jump .round_5

label .round_5:
    $ _nc.advance_round()

    menu:
        "Choose your action:"

        "Strike the nearest enemy [Attack vs DC 12]":
            $ _enemies = _nc.get_living_enemy_keys()
            if _enemies:
                $ _target = _enemies[0]
                $ _result = _nc.resolve_attack("avyanna", "strike", _target)
                call screen dice_roll_screen
                if _result["hit"]:
                    "{i}The strike connects. [_result['damage']] damage.{/i}"
                else:
                    "{i}The strike misses. The enemy sidesteps.{/i}"

        "Hold position and assess [No roll — safe option]":
            "{i}You hold back, watching for an opening.{/i}"

        "Coordinate the crew [Tactics vs DC 14]":
            $ _sc = skill_check("tactics", 14, "avyanna")
            if _sc == "SUCCESS" or _sc == "CRITICAL_SUCCESS":
                "{i}The crew moves as one. Coordinated fire drops an enemy.{/i}"
                $ _enemies = _nc.get_living_enemy_keys()
                if _enemies:
                    $ _nc.enemy_hp[_enemies[0]] = max(0, _nc.enemy_hp[_enemies[0]] - 15)
            else:
                "{i}The coordination falters. The enemy exploits the gap.{/i}"

    ## Enemy response
    $ _threat = _nc.enemy_threatens()
    if _threat["damage"] > 0:
        "{i}[_threat['narrative']] [_threat['damage']] damage to [_threat['target_name']].{/i}"

    if _nc.is_combat_over():
        jump .combat_end

    ## Extended combat — loop back
    jump .round_5

label .combat_end:
    hide screen combat_hud

    if _nc.victory:
        $ game_state.mark_encounter_cleared("act1_tutorial")
        $ party_manager.award_xp(100)
        $ game_state.set_flag("tutorial_complete")
        "{i}Victory. The threat is neutralized.{/i}"
        $ persistent.combat_victories = (persistent.combat_victories or 0) + 1
    else:
        ## Failure is interesting — not game over
        $ game_state.set_flag("act1_tutorial_lost")
        "{i}Everything goes dark. Someone drags you to cover.{/i}"
        $ persistent.combat_defeats = (persistent.combat_defeats or 0) + 1

    return
