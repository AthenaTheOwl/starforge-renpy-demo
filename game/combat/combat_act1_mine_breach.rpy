## combat_act1_mine_breach.rpy — Narrative combat: Mine Anomaly Breach
## Enemies: 4x Corporate Trooper, 1x Corporate Drone Controller, 1x Corporate Retrieval Agent, 6x Lattice Shard, 2x Lattice Shell, 1x Lattice Echo
## Auto-generated skeleton — add flavor text

label combat_act1_mine_breach:
    $ _nc = NarrativeCombat("act1_mine_breach")
    show screen combat_hud(_nc)

    "The shard's activation has triggered a cascade. Corp retrieval teams converge on Subsection 7-Gamma, followed by Lattice entities drawn to the resonance signature."

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
        $ game_state.mark_encounter_cleared("act1_mine_breach")
        $ party_manager.award_xp(150)
        $ game_state.set_flag("mine_breach_survived")
        "{i}Victory. The threat is neutralized.{/i}"
        $ persistent.combat_victories = (persistent.combat_victories or 0) + 1
    else:
        ## Failure is interesting — not game over
        $ game_state.set_flag("act1_mine_breach_lost")
        "{i}Everything goes dark. Someone drags you to cover.{/i}"
        $ persistent.combat_defeats = (persistent.combat_defeats or 0) + 1

    return
