## act1_climax_setup.rpy — Auto-generated from act1_climax_setup.json
## 263 dialogue nodes

label act1_climax_setup:
    $ game_state.mark_dialogue_played("act1_climax_setup")
    jump act1_climax_setup_start

label act1_climax_setup_start:
    "{i}The briefing room. All seven crew members present. The holographic display shows a station—corporate, fortified, wrong. This is it. The job that changes everything.{/i}"
    jump act1_climax_setup_narration_war_room

label act1_climax_setup_narration_war_room:
    "{i}The table is scarred alloy. Seven chairs, none matching. Elia stands at the head, hands flat on the surface. The holo-projector hums—blue light carves a rotating schematic into the dark. Aurum Extraction Station K-12. Four levels. Thirty-seven rooms. One objective. Everyone knows the math: this is the hardest thing they've ever done together.{/i}"
    jump act1_climax_setup_elia_opens

label act1_climax_setup_elia_opens:
    elia "Floor check. Everyone's here. Good. {i}[She activates the display.]{/i} This is the target. Aurum Extraction forward station. Four levels, heavy security, civilian workers mixed with corporate enforcement."
    jump act1_climax_setup_elia_opens_2

label act1_climax_setup_elia_opens_2:
    elia "No rehearsal. No second pass. We get one window and we use it or we lose Avyanna's legal protection permanently. {i}[She meets each pair of eyes in turn.]{/i} So I need everyone sharp. Questions held until intel review is done."
    jump act1_climax_setup_vesper_posture

label act1_climax_setup_vesper_posture:
    "{i}Vesper sits with her legs crossed, rifle case leaning against her chair. Her fingers rest on the stock—not nervous, but listening through it, the way a violinist touches strings.{/i}"
    jump act1_climax_setup_rho_posture

label act1_climax_setup_rho_posture:
    "{i}Rho leans back, arms folded across the chest plate he never fully removes. His grin is present but dimmed—the kind he wears when he's already doing math on casualties.{/i}"
    jump act1_climax_setup_nyx_posture

label act1_climax_setup_nyx_posture:
    "{i}Nyx sits furthest from the projector, hood drawn, staff across her knees. The Lattice wards in the station schematic pulse faintly and she tracks them the way a hawk tracks movement in grass.{/i}"
    jump act1_climax_setup_jalen_posture

label act1_climax_setup_jalen_posture:
    "{i}Jalen has three screens open on the table, each running different data feeds. His eyes move faster than his hands. He hasn't looked up since the schematic loaded.{/i}"
    jump act1_climax_setup_elisira_posture

label act1_climax_setup_elisira_posture:
    "{i}Elisira stands behind her chair, not sitting. Arms at her sides. Still as architecture. Whatever she's thinking, it's behind walls older than the station they're about to crack open.{/i}"
    jump act1_climax_setup_avyanna_posture

label act1_climax_setup_avyanna_posture:
    "{i}You sit at the table's edge. The shard at the base of your skull hums—faint, steady, like a second heartbeat. You are the reason for all of this. The weight of that hasn't lessened.{/i}"
    jump act1_climax_setup_elia_begins_briefing

label act1_climax_setup_elia_begins_briefing:
    elia "Jalen. Intel first. Give us everything."
    jump act1_climax_setup_jalen_intel_start

label act1_climax_setup_jalen_intel_start:
    jalen "{i}[Tapping screens, pulling data into the holographic display.]{/i} Aurum Extraction Station K-12. Officially registered as a mineral processing outpost. Unofficially—"
    jump act1_climax_setup_jalen_intel_2

label act1_climax_setup_jalen_intel_2:
    jalen "—it's a data nexus. Primordial extraction samples, Lattice research logs, and personnel records for every corporate black-site operative in the sector. All of it scheduled for transfer to Compact jurisdiction in six hours."
    jump act1_climax_setup_jalen_intel_3

label act1_climax_setup_jalen_intel_3:
    jalen "{i}[He zooms the schematic.]{/i} Four levels. Sublevel is maintenance and utilities—low security, mostly automated. Ground floor is civilian operations and processing. Second floor is corporate offices and the comm array. Top floor—"
    jump act1_climax_setup_jalen_intel_4

label act1_climax_setup_jalen_intel_4:
    jalen "{i}[His voice drops.]{/i} Top floor is the data core. That's where the extraction records live. Hardened servers, physical airgap, no remote access. To get the data, someone has to be in the room."
    jump act1_climax_setup_jalen_timeline

label act1_climax_setup_jalen_timeline:
    jalen "We have a six-hour window. After that, the transfer convoy arrives and it's out of reach. {i}[He looks grim.]{/i} This is our only shot."
    jump act1_climax_setup_jalen_tech_detail

label act1_climax_setup_jalen_tech_detail:
    jalen "Internal comms run on a closed frequency—military-grade encryption. I can crack it, but I'll need forty seconds of uninterrupted access to a relay node. There's one on each floor."
    jump act1_climax_setup_jalen_layout_detail

label act1_climax_setup_jalen_layout_detail:
    jalen "Elevator system is centrally controlled—once they lock it down, you're taking stairs or making your own paths. Emergency bulkheads on every floor can seal in under three seconds. {i}[He pauses.]{/i} If they seal the data core, we need shaped charges or a very creative Lattice operator to get through."
    jump act1_climax_setup_elisira_intel_add

label act1_climax_setup_elisira_intel_add:
    elia "Elisira. You said you had intercepted comms."
    jump act1_climax_setup_elisira_comms_1

label act1_climax_setup_elisira_comms_1:
    elisira "{i}She steps forward. A data chip appears in her hand like a card trick.{/i} Three days of encrypted traffic. Corporate internal. I broke it this morning."
    jump act1_climax_setup_elisira_comms_2

label act1_climax_setup_elisira_comms_2:
    elisira "They know someone's coming. Not us specifically—but they've raised security posture. Double shifts, additional automated defenses on sublevels two and three. {i}[Beat.]{/i} And they've requested something called a 'Lattice containment package.'"
    jump act1_climax_setup_nyx_reacts_containment

label act1_climax_setup_nyx_reacts_containment:
    nyx "{i}Sharp intake of breath.{/i} Containment package. That's Writbound hardware."
    jump act1_climax_setup_elisira_comms_3

label act1_climax_setup_elisira_comms_3:
    elisira "{i}Flat.{/i} Correct. The comms reference 'specialized personnel' arriving with the convoy. If that means Writbound operatives, our six-hour window is also our window before this becomes a fundamentally different kind of fight."
    jump act1_climax_setup_elisira_comms_4

label act1_climax_setup_elisira_comms_4:
    elisira "One more thing. The station commander's name is Harlan Dreeve. Former Compact military, discharged for 'excessive initiative.' {i}[The faintest curl of contempt.]{/i} He'll fight smart. He won't surrender."
    jump act1_climax_setup_elisira_inside_knowledge

label act1_climax_setup_elisira_inside_knowledge:
    elisira "I've been inside corporate operations. Their doctrine is containment first, elimination second. They'll try to lock you in before they try to kill you. {i}[She looks at Elia.]{/i} The bulkheads are the real weapon. Not the guards."
    jump act1_climax_setup_elia_thanks_intel

label act1_climax_setup_elia_thanks_intel:
    elia "{i}Nodding.{/i} Good. That's the landscape. Now—threat assessment. Rho, what are we walking into?"
    jump act1_climax_setup_rho_assessment

label act1_climax_setup_rho_assessment:
    rho "Security is military-grade. Automated turrets, reinforced bulkheads, probably a few surprises we haven't mapped. {i}[His grin is sharp.]{/i} Standard nightmare scenario."
    jump act1_climax_setup_rho_assessment_2

label act1_climax_setup_rho_assessment_2:
    rho "Ground floor: light infantry. Corporate enforcement—body armor, sidearms, crowd-control training. They're used to scaring miners, not fighting operators. We cut through them fast."
    jump act1_climax_setup_rho_assessment_3

label act1_climax_setup_rho_assessment_3:
    rho "Second floor: heavy infantry. Military-grade hardware, tactical training, probably wired reflexes on the squad leads. These ones know how to fight in corridors. {i}[He leans forward.]{/i} They'll use the bulkheads to channel us into kill zones."
    jump act1_climax_setup_rho_assessment_4

label act1_climax_setup_rho_assessment_4:
    rho "Top floor data core: unknown. Could be light, could be a fortress. Jalen's data doesn't cover internal defenses on that level. {i}[He looks at the schematic.]{/i} I don't like unknowns."
    jump act1_climax_setup_rho_assessment_turrets

label act1_climax_setup_rho_assessment_turrets:
    rho "Automated turrets on sublevels are Kessler-pattern—rotating, thermal-tracking, suppressive fire. Not accurate, but they don't need to be. They pin you down while the infantry flanks. Standard corporate layered defense."
    jump act1_climax_setup_rho_assessment_final

label act1_climax_setup_rho_assessment_final:
    rho "{i}[Settling back.]{/i} Total estimated hostiles: forty to sixty. We're seven. That's roughly eight to one. {i}[The grin widens.]{/i} I've had worse odds. But not by much."
    jump act1_climax_setup_vesper_intel

label act1_climax_setup_vesper_intel:
    vesper "Intel suggests they're preparing to move {b}Primordial extraction samples{/b}—including records of Site K-9. If those records reach Compact jurisdiction, Avyanna becomes a legal recovery target."
    jump act1_climax_setup_vesper_sniper_assessment

label act1_climax_setup_vesper_sniper_assessment:
    vesper "Sight lines inside the station are short—fifteen meters maximum on most corridors. That limits my effectiveness indoors. {i}[She touches the rifle case.]{/i} I'm most useful at the extraction point or in any open areas. Inside the core, I switch to close-quarters protocols."
    jump act1_climax_setup_vesper_civilian_concern

label act1_climax_setup_vesper_civilian_concern:
    vesper "{i}Quieter.{/i} Civilian workers. Jalen said there are processing staff on the ground floor. Non-combatants. {i}[She looks at Elia.]{/i} Rules of engagement need to be clear. We're not them."
    jump act1_climax_setup_elia_roe

label act1_climax_setup_elia_roe:
    elia "{i}Firm.{/i} No civilian casualties. Period. If a civilian is between you and the objective, you find another path. Anyone who violates that answers to me personally."
    jump act1_climax_setup_rho_roe_response

label act1_climax_setup_rho_roe_response:
    rho "{i}No argument. Just a nod.{/i} Copy. Clean hands."
    jump act1_climax_setup_nyx_concern

label act1_climax_setup_nyx_concern:
    nyx "The station has Synthetic wards. Strong ones. I can disrupt them, but it'll take time—and it'll light us up like a flare. Once I start, stealth is over."
    jump act1_climax_setup_nyx_lattice_detail

label act1_climax_setup_nyx_lattice_detail:
    nyx "The wards are layered. Outer shell is standard—I can peel it in under a minute. But there's something underneath. Deeper. {i}[She frowns.]{/i} The signature doesn't read like corporate tech. It reads like Lattice architecture. Old Lattice."
    jump act1_climax_setup_nyx_lattice_detail_2

label act1_climax_setup_nyx_lattice_detail_2:
    nyx "If they've built Writbound containment into the station's ward structure, I'm not just fighting their security—I'm fighting the building itself. {i}[She meets your eyes.]{/i} And Avyanna, your shard will react. Count on it."
    jump act1_climax_setup_nyx_writbound_warning

label act1_climax_setup_nyx_writbound_warning:
    nyx "Writbound operatives are not soldiers. They're channelers—Lattice practitioners who've bonded with containment entities. Think of a Synthetic ward that can think, adapt, and hunt. {i}[Her jaw tightens.]{/i} I've fought one before. I won. Barely."
    jump act1_climax_setup_bee_first_analysis

label act1_climax_setup_bee_first_analysis:
    bee "{{BEE:: lattice-resonance-detected | station-wards-anomalous | sub-harmonic matches primordial extraction signature—this facility was built around something, not on top of it}}"
    jump act1_climax_setup_avyanna_bee_reaction

label act1_climax_setup_avyanna_bee_reaction:
    "{i}The shard pulses—warm, insistent. BEE's analysis bleeds through like ink through paper. The station wasn't just built to store data. It was built to contain something. And that something is still there.{/i}"
    jump act1_climax_setup_player_ask_bee

label act1_climax_setup_player_ask_bee:
    avyanna "BEE says the station was built around something. The Lattice signature underneath the wards—it's not security. It's containment. The facility is a cage."
    jump act1_climax_setup_crew_bee_reaction

label act1_climax_setup_crew_bee_reaction:
    "{i}Silence. The kind that means everyone just recalculated the risk.{/i}"
    jump act1_climax_setup_elia_bee_response

label act1_climax_setup_elia_bee_response:
    elia "{i}Steady.{/i} Does that change the objective?"
    jump act1_climax_setup_bee_objective_analysis

label act1_climax_setup_bee_objective_analysis:
    bee "{{BEE:: objective unchanged | data core still primary target | additional variable: contained entity may react to shard proximity | recommend: caution in sublevel approach}}"
    jump act1_climax_setup_nyx_responds_bee

label act1_climax_setup_nyx_responds_bee:
    nyx "{i}To Avyanna, low.{/i} Your ghost has good instincts. If there's something caged under that station, my ward disruption might wake it up. {i}[She doesn't look afraid. She looks fascinated.]{/i} We should plan for that."
    jump act1_climax_setup_elia_threat_summary

label act1_climax_setup_elia_threat_summary:
    elia "So. Forty to sixty hostiles. Military-grade security. Automated defenses. A station commander who won't quit. Possible Writbound operatives. Lattice wards that fight back. And something caged underneath it all. {i}[She exhales.]{/i} Anyone want to walk?"
    jump act1_climax_setup_elia_threat_pause

label act1_climax_setup_elia_threat_pause:
    "{i}No one moves. No one speaks. The offer is genuine—Elia would let them go. But they're here.{/i}"
    jump act1_climax_setup_rho_stays

label act1_climax_setup_rho_stays:
    if game_state.has_flag("rho_bonded"):
        rho "{i}Cracking his knuckles, then catching your eye with something warmer than his usual grin.{/i} I walked into worse on Meridian. But I didn't have family watching my back then."
    else:
        rho "{i}Cracking his knuckles.{/i} I walked into worse on Meridian. At least this time I like the people I'm walking with."
    jump act1_climax_setup_vesper_stays

label act1_climax_setup_vesper_stays:
    if game_state.has_flag("vesper_bonded"):
        vesper "{i}Not looking up from her rifle, but her voice carries something almost soft.{/i} You already know the answer. Don't waste breath asking."
    else:
        vesper "{i}Not looking up from her rifle.{/i} Don't insult me by asking."
    jump act1_climax_setup_nyx_stays

label act1_climax_setup_nyx_stays:
    if game_state.has_flag("nyx_bonded"):
        nyx "Old Lattice architecture and a crew worth protecting? {i}[Her smile reaches her eyes—rare and genuine.]{/i} I'm exactly where I should be."
    else:
        nyx "Old Lattice architecture? This might be the most interesting thing I've done in years. {i}[Her smile is sharp and genuine.]{/i} I'm in."
    jump act1_climax_setup_jalen_stays

label act1_climax_setup_jalen_stays:
    if game_state.has_flag("jalen_bonded"):
        jalen "{i}He looks up—actually looks up—and meets your eyes.{/i} I built half these systems for people like them. It's time I took them apart for people like us."
    else:
        jalen "{i}Without looking up from his screens.{/i} My code is already halfway through their encryption. Walking away now would be professionally embarrassing."
    jump act1_climax_setup_elisira_stays

label act1_climax_setup_elisira_stays:
    if game_state.has_flag("elisira_bonded"):
        elisira "{i}One word, but she holds Elia's gaze when she says it, and something passes between them that isn't language.{/i} No."
    else:
        elisira "{i}One word.{/i} No."
    jump act1_climax_setup_elia_acknowledges_crew

label act1_climax_setup_elia_acknowledges_crew:
    elia "{i}The faintest smile—pride, grief, gratitude braided together.{/i} Good. Then let's talk strategy."
    jump act1_climax_setup_strategy_approach_choice

label act1_climax_setup_strategy_approach_choice:
    elia "Two ways to hit this. We go quiet—infiltration, disable security in sequence, reach the data core before they know we're inside. Or we go loud—simultaneous breach, overwhelming force, speed over subtlety. {i}[She looks at you.]{/i} Avyanna. You've seen how we work. What's your read?"
    jump act1_climax_setup_approach_player_choice

label act1_climax_setup_approach_player_choice:
    "{i}The crew watches you. This isn't delegation—it's trust. Elia is testing whether you can read the board and call the play.{/i}"
    menu:
        "[Stealth Approach] Infiltration. Disable their eyes before they see us coming.":
            $ game_state.set_flag("approach_stealth")
            jump act1_climax_setup_stealth_choice_check
        "[Assault Approach] Overwhelming force. Hit them so hard they can't organize a response.":
            $ game_state.set_flag("approach_assault")
            jump act1_climax_setup_assault_choice_check
        "[Hybrid Approach] Both. Stealth team disables security while assault team waits at the breach point. Synchronized.":
            $ game_state.set_flag("approach_hybrid")
            jump act1_climax_setup_hybrid_choice_check

label act1_climax_setup_stealth_choice_check:
    "{i}You outline the stealth approach. Elia watches you draw the route on the holographic display—maintenance tunnels, service corridors, security blind spots. This requires tactical precision.{/i}"
    $ _sc_result = skill_check("Perception", 14, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_climax_setup_stealth_choice_success
    else:
        jump act1_climax_setup_stealth_choice_failure

label act1_climax_setup_stealth_choice_success:
    "{i}Your hand moves with confidence across the display. Entry points, timing windows, fallback routes—the plan unfolds like a mechanism.{/i}"
    jump act1_climax_setup_stealth_crew_react_good

label act1_climax_setup_stealth_crew_react_good:
    vesper "{i}Leaning forward. Impressed.{/i} That's clean. Service corridor approach avoids every turret emplacement on levels one and two. Where did you learn to read floor plans?"
    jump act1_climax_setup_jalen_stealth_good

label act1_climax_setup_jalen_stealth_good:
    jalen "{i}Pulling up schematics.{/i} She's right—the maintenance tunnels connect to the elevator shaft on sublevel two. I can loop their internal cameras from there. We'd have maybe eight minutes of invisibility."
    jump act1_climax_setup_elisira_stealth_good

label act1_climax_setup_elisira_stealth_good:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "{i}Appraising.{/i} Silent approach favors precision eliminations. Suppressed weapons, close work. {i}[She touches the pistol at her hip.]{/i} This is what I'm built for."
    jump act1_climax_setup_elia_approves_stealth

label act1_climax_setup_elia_approves_stealth:
    elia "{i}Nodding slowly.{/i} Good call. Stealth gives us the element of surprise and keeps civilians out of crossfire. The risk is if we're detected early—then we're deep inside with no support."
    jump act1_climax_setup_stealth_nyx_concern

label act1_climax_setup_stealth_nyx_concern:
    nyx "One problem. My ward disruption isn't quiet. The moment I start peeling their Lattice defenses, every Synthetic sensor in the station knows. {i}[She thinks.]{/i} Unless I work from inside the ward structure itself. Slower, but silent."
    jump act1_climax_setup_stealth_rho_concern

label act1_climax_setup_stealth_rho_concern:
    rho "{i}Frowning.{/i} Stealth means I can't bring the rotary cannon. Corridors, suppressed weapons, careful footwork. {i}[Beat.]{/i} I can do it. I just want everyone to know I'm doing it under protest."
    jump act1_climax_setup_approach_decided

label act1_climax_setup_stealth_choice_failure:
    "{i}You sketch the approach on the display, but the routing is rough—a blind spot in your timing leaves a gap in camera coverage. Vesper catches it.{/i}"
    jump act1_climax_setup_vesper_corrects_stealth

label act1_climax_setup_vesper_corrects_stealth:
    vesper "{i}Leaning forward, tapping the display.{/i} That corridor has overlapping camera arcs. We'd need to loop them simultaneously, not in sequence. {i}[She adjusts the route.]{/i} But the core idea is sound. Let me clean it up."
    jump act1_climax_setup_stealth_corrected

label act1_climax_setup_stealth_corrected:
    elia "The instinct is right—stealth approach. Vesper and Jalen will refine the routing. {i}[She looks at you.]{/i} Good eye for the entry point. The execution needs work, but that's what a crew is for."
    jump act1_climax_setup_stealth_nyx_concern

label act1_climax_setup_assault_choice_check:
    "{i}You outline the assault approach. Breach points, suppressive fire lanes, room-clearing sequences. The display fills with red arrows. This requires understanding of force application.{/i}"
    $ _sc_result = skill_check("tactics", 14, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_climax_setup_assault_choice_success
    else:
        jump act1_climax_setup_assault_choice_failure

label act1_climax_setup_assault_choice_success:
    "{i}The plan unfolds across the display like a controlled detonation—every breach timed, every fire lane covered, every fallback accounted for.{/i}"
    jump act1_climax_setup_rho_assault_good

label act1_climax_setup_rho_assault_good:
    rho "{i}Grinning—full, genuine, dangerous.{/i} Now you're speaking my language. Simultaneous breach on three entry points—they can't reinforce all of them. We pick the weakest and punch through."
    jump act1_climax_setup_elia_assault_good

label act1_climax_setup_elia_assault_good:
    elia "Speed and violence of action. If we hit hard enough, their command structure collapses before Dreeve can organize a response. {i}[She traces the assault route.]{/i} Thirty seconds from breach to second floor. Ninety seconds to the data core."
    jump act1_climax_setup_vesper_assault_concern

label act1_climax_setup_vesper_assault_concern:
    vesper "{i}Cool.{/i} Civilian casualties become a real risk in a direct assault. Ground floor processing workers—if they panic, they run into our fire lanes."
    jump act1_climax_setup_jalen_assault_solution

label act1_climax_setup_jalen_assault_solution:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    $ relationship_manager.process_reputation_affinity("elia", 1)
    jalen "I can trigger a fire alarm on the ground floor sixty seconds before breach. Civilian evacuation protocols are automatic—they'll clear the processing areas before we enter."
    jump act1_climax_setup_elia_approves_assault

label act1_climax_setup_elia_approves_assault:
    elia "{i}Decisive.{/i} Do it. Assault approach, pre-breach civilian evacuation. The trade-off is they'll know we're coming sixty seconds early. {i}[She looks at Rho.]{/i} Can we still achieve surprise?"
    jump act1_climax_setup_rho_assault_answer

label act1_climax_setup_rho_assault_answer:
    rho "They'll know something is wrong. They won't know what until we're already inside. Sixty seconds of confusion is enough."
    jump act1_climax_setup_approach_decided

label act1_climax_setup_assault_choice_failure:
    "{i}Your fire lanes overlap in two places—friendly fire risk. Rho catches it before you finish.{/i}"
    jump act1_climax_setup_rho_corrects_assault

label act1_climax_setup_rho_corrects_assault:
    rho "{i}Not unkind, but direct.{/i} Those two corridors create a crossfire problem—our own people get caught in the overlap. {i}[He adjusts the display.]{/i} Stagger the breach by four seconds. Team one enters here, team two sweeps in from the service corridor after the first volley clears."
    jump act1_climax_setup_assault_corrected

label act1_climax_setup_assault_corrected:
    elia "Right idea, needs calibration. Rho's adjustment fixes the crossfire issue. {i}[She nods at you.]{/i} The aggression is correct. Sometimes speed is the safest option."
    jump act1_climax_setup_vesper_assault_concern

label act1_climax_setup_hybrid_choice_check:
    "{i}A combined approach. The most complex option—two teams, synchronized timing, overlapping contingencies. This requires exceptional tactical awareness.{/i}"
    $ _sc_result = skill_check("tactics", 16, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_climax_setup_hybrid_choice_success
    else:
        jump act1_climax_setup_hybrid_choice_failure

label act1_climax_setup_hybrid_choice_success:
    "{i}The display lights up like a symphony score—two movements, perfectly timed, each dependent on the other. Infiltration team disables cameras and turrets. Assault team breaches the moment the lights go dark.{/i}"
    jump act1_climax_setup_elia_hybrid_impressed

label act1_climax_setup_elia_hybrid_impressed:
    elia "{i}Both eyebrows raised.{/i} That's... ambitious. And elegant. Stealth team cripples their eyes, assault team hits while they're blind. {i}[She traces the timing on the display.]{/i} The synchronization has to be perfect. Five seconds off and the stealth team is exposed with no support."
    jump act1_climax_setup_vesper_hybrid

label act1_climax_setup_vesper_hybrid:
    vesper "{i}Studying the display, nodding slowly.{/i} It solves both problems. Stealth for the approach, force for the objective. And it gives us a fallback—if the stealth team is detected, assault team breaches early."
    jump act1_climax_setup_elisira_hybrid

label act1_climax_setup_elisira_hybrid:
    $ relationship_manager.process_reputation_affinity("elia", 2)
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "{i}For the first time, something like respect in her voice.{/i} This is how the Compact's best units operate. Paired operations. {i}[She looks at you.]{/i} You've either studied their doctrine or you have very good instincts."
    jump act1_climax_setup_approach_decided

label act1_climax_setup_hybrid_choice_failure:
    "{i}The concept is strong, but your timing windows don't align—the stealth team would be in position three minutes before the assault team is ready. Elisira sees the gap.{/i}"
    jump act1_climax_setup_elisira_corrects_hybrid

label act1_climax_setup_elisira_corrects_hybrid:
    elisira "{i}Stepping to the display.{/i} The idea is correct. The timing isn't. {i}[Her fingers adjust the sequence with surgical precision.]{/i} Stealth team enters here. Assault team repositions to secondary breach point—closer approach, tighter window. Synchronization at T-minus-zero."
    jump act1_climax_setup_hybrid_corrected

label act1_climax_setup_hybrid_corrected:
    elia "Hybrid approach. Elisira's timing fixes. This is the hardest option to execute, but it gives us the most flexibility. {i}[She looks at you.]{/i} Bold thinking. That's what we need."
    jump act1_climax_setup_approach_decided

label act1_climax_setup_approach_decided:
    elia "Approach is set. Now the hard part. {i}[She dims the display, leaving only the station outline.]{/i} We split into two teams. This isn't optional—one team takes the data core, one team holds extraction. If the hold team fails, nobody gets out."
    jump act1_climax_setup_elisira_plan

label act1_climax_setup_elisira_plan:
    elisira "{i}Single syllable, command weight.{/i} Split. {i}[She gestures to the display.]{/i} Four go in—fast, loud, direct assault on the data core. Three hold extraction point and provide fire support."
    jump act1_climax_setup_elisira_split_logic

label act1_climax_setup_elisira_split_logic:
    elisira "Assault team needs a breacher, a ward specialist, a close-quarters fighter, and either tech support or precision fire. Hold team needs range, coordination, and someone who can anchor a defensive position against superior numbers."
    jump act1_climax_setup_crew_weighs_in_intro

label act1_climax_setup_crew_weighs_in_intro:
    elia "Before we assign, I want everyone's input. Speak to your strengths and your limits. No ego. {i}[She looks around the table.]{/i} Vesper. Start."
    jump act1_climax_setup_vesper_weighs_in

label act1_climax_setup_vesper_weighs_in:
    vesper "Indoor corridors limit my effective range. I'm strongest at extraction—long sight lines, elevated position, counter-sniper work. {i}[She pauses.]{/i} That said, if you need me inside, I can switch to close-quarters. I'm not useless at ten meters. Just... suboptimal."
    jump act1_climax_setup_vesper_weighs_in_2

label act1_climax_setup_vesper_weighs_in_2:
    vesper "{i}Quieter.{/i} My concern is comms. If the assault team hits a bulkhead seal and I can't reach them—if I can't see them—I'm shooting blind. I need eyes on the team or I'm just a body holding a position."
    jump act1_climax_setup_rho_weighs_in

label act1_climax_setup_rho_weighs_in:
    rho "I'm your breacher. That's not ego, that's physics—I'm the only one who can put a shaped charge through a reinforced bulkhead and walk through the hole. Put me on the assault team."
    jump act1_climax_setup_rho_weighs_in_2

label act1_climax_setup_rho_weighs_in_2:
    rho "{i}Sobering.{/i} Limitation: I'm loud. If stealth is the priority, I need to stay quiet until the breach moment. I can do it—but everyone should know it goes against every instinct I have."
    jump act1_climax_setup_rho_weighs_in_3

label act1_climax_setup_rho_weighs_in_3:
    rho "{i}Lower. Honest.{/i} And if we're talking limits—I can't protect everyone at once. In Meridian, I tried to cover two exits. Lost people at both. {i}[He meets Elia's eyes.]{/i} Don't split my attention. Give me one job and I'll do it."
    jump act1_climax_setup_nyx_weighs_in

label act1_climax_setup_nyx_weighs_in:
    nyx "I have to be on the assault team. The data core will have the heaviest wards—if there are Writbound elements, that's where they'll be anchored. Without me, you hit that wall and stop."
    jump act1_climax_setup_nyx_weighs_in_2

label act1_climax_setup_nyx_weighs_in_2:
    nyx "{i}Her eyes find you.{/i} And Avyanna's shard will react to the Lattice architecture. If she's on the assault team, I need to be there to manage the resonance. If she's not—I need to manage it remotely, and that's harder."
    jump act1_climax_setup_nyx_weighs_in_3

label act1_climax_setup_nyx_weighs_in_3:
    nyx "Warning: once I engage their wards, I'm committed. I can't split my focus between offense and defense. Whoever's near me needs to keep hostiles off my back while I work. {i}[She looks at Rho.]{/i} That means you."
    jump act1_climax_setup_jalen_weighs_in

label act1_climax_setup_jalen_weighs_in:
    jalen "I can go either way. Inside, I crack their security systems in real-time—cameras, bulkheads, automated defenses. Outside, I coordinate comms and run electronic warfare from the ship."
    jump act1_climax_setup_jalen_weighs_in_2

label act1_climax_setup_jalen_weighs_in_2:
    jalen "Trade-off: if I'm inside, I'm vulnerable. I'm not a fighter. I'll need protection while I work. If I'm outside, I have the ship's full processing power but limited access—I can only crack systems I can reach through the comm relay."
    jump act1_climax_setup_jalen_weighs_in_3

label act1_climax_setup_jalen_weighs_in_3:
    jalen "{i}Adjusting his glasses.{/i} Honestly? The data core's airgap means someone needs to be physically present to extract. If that someone isn't me, you need to give me five minutes to teach whoever goes in how to run the extraction protocol. It's not complicated. It's just specific."
    jump act1_climax_setup_elisira_weighs_in

label act1_climax_setup_elisira_weighs_in:
    elisira "I know how corporate security thinks. I know Dreeve's likely deployment pattern. I know where his blind spots are because they're the same blind spots I exploited when I was inside the system. {i}[Flat.]{/i} Assault team."
    jump act1_climax_setup_elisira_weighs_in_2

label act1_climax_setup_elisira_weighs_in_2:
    elisira "But I should also say this: if Dreeve recognizes me, it changes the calculus. He'll know our intel is deeper than surface level. He may trigger a data purge rather than let us take the records intact."
    jump act1_climax_setup_elisira_weighs_in_3

label act1_climax_setup_elisira_weighs_in_3:
    elisira "{i}Meeting Elia's eyes.{/i} I'm a tactical asset and a potential liability. Use me where you think the math works."
    jump act1_climax_setup_elia_weighs_in

label act1_climax_setup_elia_weighs_in:
    elia "I go where the crew needs me. Assault team wants a corridor fighter—that's me. Hold team wants an anchor who won't break—that's also me. {i}[She looks at you.]{/i} This is your call, Avyanna."
    jump act1_climax_setup_elia_split_question

label act1_climax_setup_elia_split_question:
    elia "{i}Looking at you.{/i} Avyanna. You've been training with all of us. You know our strengths. {i}[Beat.]{/i} Who goes in, and who holds the line?"
    jump act1_climax_setup_player_choice

label act1_climax_setup_player_choice:
    "{i}All eyes on you. The weight of the decision is real. Who you send in determines tactics. Who holds the line determines if anyone gets out.{/i}"
    menu:
        "[Assault: Elia, Elisira, Rho, Nyx | Hold: Vesper, Jalen, Avyanna]":
            $ game_state.set_flag("assault_team_close_quarters")
            jump act1_climax_setup_assault_team_1
        "[Assault: Elia, Vesper, Nyx, Avyanna | Hold: Elisira, Rho, Jalen]":
            $ game_state.set_flag("assault_team_mixed_range")
            jump act1_climax_setup_assault_team_2
        "[Assault: Elisira, Rho, Nyx, Jalen | Hold: Elia, Vesper, Avyanna]":
            $ game_state.set_flag("assault_team_tactical_precision")
            jump act1_climax_setup_assault_team_3

label act1_climax_setup_assault_team_1:
    elia "{i}Nodding.{/i} Heavy assault. Rho breaches, I clear corridors, Elisira handles precision eliminations, Nyx disrupts their wards. Fast and brutal."
    jump act1_climax_setup_hold_team_1

label act1_climax_setup_hold_team_1:
    vesper "{i}Calm.{/i} Jalen pilots extraction, I provide overwatch and counter-sniper. Avyanna coordinates comms and tracks hostiles. {i}[She looks at you.]{/i} You'll be our eyes."
    jump act1_climax_setup_team_1_reactions

label act1_climax_setup_team_1_reactions:
    rho "{i}Grinning.{/i} This is going to be loud. I like it."
    jump act1_climax_setup_team_1_nyx_react

label act1_climax_setup_team_1_nyx_react:
    nyx "Rho breaches, I follow through the gap. His explosions will mask my ward disruptions—by the time they realize I'm in their Lattice, it's already peeled. {i}[She almost smiles.]{/i} Symbiotic chaos."
    jump act1_climax_setup_team_1_elisira_react

label act1_climax_setup_team_1_elisira_react:
    elisira "I'll handle Dreeve personally if we encounter him. {i}[She checks her pistols—a gesture that's half maintenance, half ritual.]{/i} He won't expect me. That advantage lasts exactly once."
    jump act1_climax_setup_team_1_jalen_react

label act1_climax_setup_team_1_jalen_react:
    jalen "I'll run electronic warfare from the extraction point. Camera loops, comms jamming, bulkhead overrides—whatever the assault team needs, I'll push remotely. {i}[He looks at Vesper.]{/i} You and I need a shared tactical display."
    jump act1_climax_setup_team_1_vesper_avyanna

label act1_climax_setup_team_1_vesper_avyanna:
    vesper "{i}To you.{/i} Avyanna. At the extraction point, your shard may pick up things Jalen's sensors miss. Lattice signatures, ward shifts, personnel movement. Trust what you feel. Report what you sense. {i}[She holds your gaze.]{/i} I'll handle the rest."
    jump act1_climax_setup_team_1_confirmation

label act1_climax_setup_team_1_confirmation:
    elia "{i}To the assault team.{/i} We go fast. We go hard. We do not stop until we're in the data core. {i}[To the hold team.]{/i} You are our lifeline. If you fall, we die in there. {i}[Beat.]{/i} No pressure."
    jump act1_climax_setup_final_briefing

label act1_climax_setup_assault_team_2:
    vesper "{i}Raised eyebrow.{/i} Mixed range. Elia closes distance, I provide precision fire, Nyx handles wards, Avyanna... {i}[She looks at you.]{/i} You're coming in with us?"
    jump act1_climax_setup_avyanna_in_assault

label act1_climax_setup_avyanna_in_assault:
    avyanna "{i}Steady.{/i} I can track Lattice signatures. I'll know where the wards are before you hit them."
    jump act1_climax_setup_team_2_elia_react

label act1_climax_setup_team_2_elia_react:
    elia "{i}Searching your face.{/i} You understand what going inside means. If the extraction point falls, we're trapped. If the wards react to your shard, you become a beacon."
    jump act1_climax_setup_team_2_avyanna_response

label act1_climax_setup_team_2_avyanna_response:
    "{i}You nod. There's no bravery in it—just clarity. Your shard is the reason they built this cage. You should be the one to open it.{/i}"
    jump act1_climax_setup_hold_team_2

label act1_climax_setup_hold_team_2:
    elisira "{i}Flat.{/i} Rho breaches from range. Jalen coordinates timing. I handle counter-assault if they flank. {i}[Beat.]{/i} Surgical."
    jump act1_climax_setup_team_2_rho_react

label act1_climax_setup_team_2_rho_react:
    rho "{i}Cracking his neck.{/i} Hold team with the big gun. Fine. Anyone comes near that extraction point, they meet the rotary cannon. {i}[He glances at Elisira.]{/i} Try to leave some for me."
    jump act1_climax_setup_team_2_elisira_react

label act1_climax_setup_team_2_elisira_react:
    elisira "{i}Dry.{/i} I don't leave things."
    jump act1_climax_setup_team_2_jalen_react

label act1_climax_setup_team_2_jalen_react:
    jalen "I'll run overwatch from the hold position. Full electronic warfare suite. {i}[He looks at Nyx.]{/i} When you hit the wards, I'll try to map the resonance pattern from outside. Might give you an edge."
    jump act1_climax_setup_team_2_confirmation

label act1_climax_setup_team_2_confirmation:
    elia "{i}To Avyanna.{/i} Stay close to me. If it gets ugly, you run. Understood?"
    jump act1_climax_setup_team_2_avyanna_final

label act1_climax_setup_team_2_avyanna_final:
    "{i}You don't agree to run. You just nod. Elia sees the difference but doesn't press it.{/i}"
    jump act1_climax_setup_final_briefing

label act1_climax_setup_assault_team_3:
    elisira "{i}Single nod.{/i} Precision strike. Rho breaches clean, Nyx disrupts wards without flare, Jalen maps optimal routes in real-time. No waste."
    jump act1_climax_setup_hold_team_3

label act1_climax_setup_hold_team_3:
    elia "{i}Grim smile.{/i} Vesper and I hold extraction. Long-range dominance, close-quarters fallback. Avyanna coordinates. {i}[She looks at you.]{/i} This puts you in the most danger if they breach our perimeter."
    jump act1_climax_setup_team_3_vesper_react

label act1_climax_setup_team_3_vesper_react:
    vesper "{i}Quiet.{/i} They won't breach. Not while I'm watching."
    jump act1_climax_setup_team_3_elisira_react

label act1_climax_setup_team_3_elisira_react:
    elisira "Jalen—you're inside with me. I need real-time security overrides. Can you keep up?"
    jump act1_climax_setup_team_3_jalen_react

label act1_climax_setup_team_3_jalen_react:
    jalen "{i}A flash of something—pride, maybe, or stubbornness.{/i} I built systems like these. I'll take them apart faster than you can walk through them."
    jump act1_climax_setup_team_3_rho_react

label act1_climax_setup_team_3_rho_react:
    rho "Clean breaches on Elisira's mark. Shaped charges, precision placement, minimal collateral. {i}[He looks at Nyx.]{/i} I'll make the holes. You do the magic."
    jump act1_climax_setup_team_3_nyx_react

label act1_climax_setup_team_3_nyx_react:
    nyx "With Jalen mapping the ward architecture from inside, I can target specific nodes instead of brute-forcing the whole structure. More efficient. Less noise. {i}[She looks satisfied.]{/i} This is the smart play."
    jump act1_climax_setup_team_3_confirmation

label act1_climax_setup_team_3_confirmation:
    elia "{i}To the assault team.{/i} Elisira has command inside. Follow her calls. {i}[To you.]{/i} Avyanna—you coordinate between teams. You're our bridge. If comms go down, you're the last thread holding this together."
    jump act1_climax_setup_final_briefing

label act1_climax_setup_final_briefing:
    elia "{i}Standing.{/i} Everyone clear on roles? Questions? Concerns? {i}[She looks around the table.]{/i} Speak now."
    jump act1_climax_setup_final_questions_choice

label act1_climax_setup_final_questions_choice:
    "{i}The table is quiet. But the silence is full of things unsaid.{/i}"
    menu:
        "[Ask about contingencies] What if the assault team gets trapped?":
            jump act1_climax_setup_contingency_question
        "[Ask about the entity] What if whatever's caged under the station wakes up?":
            jump act1_climax_setup_entity_question
        "[Ask about Dreeve] What do we know about the station commander?":
            jump act1_climax_setup_dreeve_question
        "[Stay silent] You've said enough. Let them prepare.":
            jump act1_climax_setup_crew_silence

label act1_climax_setup_contingency_question:
    elia "If the assault team is trapped behind a sealed bulkhead, the hold team has ninety seconds to reach them before the station's internal security converges. {i}[She's thought about this.]{/i} After ninety seconds, the assault team fights through or finds another way out. The hold team does not abandon the extraction point to rescue them."
    jump act1_climax_setup_contingency_hard_truth

label act1_climax_setup_contingency_hard_truth:
    elia "{i}Harder.{/i} If the assault team cannot reach the data core and cannot retreat, the hold team extracts without them. That's the order. {i}[She looks at each assault team member.]{/i} You volunteered for the harder job. You knew the math."
    jump act1_climax_setup_rho_contingency

label act1_climax_setup_rho_contingency:
    rho "{i}Quiet.{/i} Understood. But for the record—if it comes to that, I'll be the one holding the door so everyone else gets out. That's not heroism. That's physics. I'm the hardest to kill."
    jump act1_climax_setup_contingency_to_silence

label act1_climax_setup_contingency_to_silence:
    "{i}No one argues with him. Not because they agree, but because they know he means it.{/i}"
    jump act1_climax_setup_other_questions_choice

label act1_climax_setup_entity_question:
    nyx "{i}She's been waiting for someone to ask.{/i} If the contained entity reacts to our presence—specifically to Avyanna's shard—it could do several things. Amplify the station's wards. Disrupt Lattice operations on both sides. Or..."
    jump act1_climax_setup_nyx_entity_detail

label act1_climax_setup_nyx_entity_detail:
    nyx "...it could try to communicate. Primordial entities aren't mindless. They're alien. If it recognizes the shard, it might reach for Avyanna. {i}[She meets your eyes.]{/i} If that happens, you tell me immediately. Don't try to manage it alone."
    jump act1_climax_setup_bee_entity_analysis

label act1_climax_setup_bee_entity_analysis:
    bee "{{BEE:: primordial-contact-protocol logged | host-protection: priority-absolute | note: if the cage opens, I will not be a passive observer}}"
    jump act1_climax_setup_entity_to_silence

label act1_climax_setup_entity_to_silence:
    "{i}BEE's words settle into your bones. The shard pulses once—acknowledgment or warning, you're not sure which.{/i}"
    jump act1_climax_setup_other_questions_choice

label act1_climax_setup_dreeve_question:
    elisira "Harlan Dreeve. Forty-seven. Former Compact Shock Infantry, decorated twice, court-martialed once. Discharged for executing prisoners during the Veritas Corridor incident. Aurum hired him the same week."
    jump act1_climax_setup_elisira_dreeve_2

label act1_climax_setup_elisira_dreeve_2:
    elisira "He's competent, ruthless, and loyal to whoever signs his contract. He won't surrender because surrender means a tribunal—and he's already had one. {i}[Her voice is flat, clinical.]{/i} He'll fight to the last."
    jump act1_climax_setup_elisira_dreeve_3

label act1_climax_setup_elisira_dreeve_3:
    elisira "{i}Softer—barely.{/i} I've met men like him before. They're not evil. They're empty. They filled the hole with duty and orders. Take away the structure and they collapse. {i}[She looks at Elia.]{/i} Don't try to reason with him. Just be faster."
    jump act1_climax_setup_dreeve_to_silence

label act1_climax_setup_dreeve_to_silence:
    "{i}Elisira steps back. Whatever she left unsaid about her own time inside the system hangs in the air like smoke.{/i}"
    jump act1_climax_setup_other_questions_choice

label act1_climax_setup_other_questions_choice:
    "{i}The briefing continues.{/i}"
    menu:
        "[Ask another question]":
            jump act1_climax_setup_final_questions_choice
        "[No more questions. Move on.]":
            jump act1_climax_setup_crew_silence

label act1_climax_setup_crew_silence:
    "{i}Silence. Not fear. Readiness. Everyone knows what's at stake.{/i}"
    jump act1_climax_setup_bee_tactical_full

label act1_climax_setup_bee_tactical_full:
    bee "{{BEE:: tactical-summary compiled | threat-level: severe | crew-cohesion: high | probability-of-mission-success: 34.7%% | probability-of-zero-casualties: 11.2%% | personal-annotation: numbers lie—this crew defies probability}}"
    jump act1_climax_setup_avyanna_bee_private

label act1_climax_setup_avyanna_bee_private:
    "{i}You feel BEE's analysis like a weight in your chest. Thirty-four percent. One in nine chance everyone comes home. The shard warms, and beneath the numbers, you sense something else—something BEE doesn't quantify. Belief.{/i}"
    jump act1_climax_setup_elia_dismisses_briefing

label act1_climax_setup_elia_dismisses_briefing:
    elia "Briefing's done. Four hours until insertion. Gear up, rest, do whatever you need to do. {i}[She pauses.]{/i} I want everyone back here in three hours for final checks."
    jump act1_climax_setup_crew_disperses

label act1_climax_setup_crew_disperses:
    "{i}The crew rises. Chairs scrape. The holographic station rotates in empty blue light. But no one leaves immediately—they linger, finding reasons to stay close. This is the last quiet before the storm.{/i}"
    jump act1_climax_setup_personal_moments_choice

label act1_climax_setup_personal_moments_choice:
    "{i}The briefing room empties slowly. You have time to speak with someone before preparations begin.{/i}"
    menu:
        "[Find Vesper] She's in the observation deck, cleaning her rifle.":
            jump act1_climax_setup_personal_vesper
        "[Find Rho] He's in the cargo bay, checking his charges.":
            jump act1_climax_setup_personal_rho
        "[Find Nyx] She's in the engine room, meditating near the Lattice conduits.":
            jump act1_climax_setup_personal_nyx
        "[Find Jalen] He's at his workstation, running simulations.":
            jump act1_climax_setup_personal_jalen
        "[Find Elisira] She's in the armory, alone.":
            jump act1_climax_setup_personal_elisira
        "[Stay with Elia] She hasn't left the briefing room.":
            jump act1_climax_setup_personal_elia

label act1_climax_setup_personal_vesper:
    "{i}The observation deck. Stars turn beyond the viewport. Vesper sits cross-legged on the floor, rifle disassembled across a cloth with the precision of a surgical kit. She doesn't look up when you enter. She knew you were there before the door opened.{/i}"
    jump act1_climax_setup_vesper_personal_1

label act1_climax_setup_vesper_personal_1:
    if game_state.has_flag("vesper_bonded"):
        vesper "{i}Hands moving, but she shifts to make space beside her.{/i} I was wondering if you'd come."
    else:
        vesper "{i}Hands moving, reassembling by touch.{/i} You don't have to check on me."
    jump act1_climax_setup_vesper_personal_choice

label act1_climax_setup_vesper_personal_choice:
    "{i}Her hands are steady. Her breathing is controlled. But there's a tension in her shoulders that the rifle cleaning isn't reaching.{/i}"
    menu:
        "I'm not checking on you. I'm asking you to check on me.":
            jump act1_climax_setup_vesper_personal_honest
        "Are you scared?":
            jump act1_climax_setup_vesper_personal_direct
        "[Sit quietly beside her]":
            jump act1_climax_setup_vesper_personal_silent

label act1_climax_setup_vesper_personal_honest:
    vesper "{i}Her hands pause. Just for a moment.{/i} That's... unusually honest. {i}[She looks at you.]{/i} What do you need?"
    jump act1_climax_setup_vesper_personal_depth

label act1_climax_setup_vesper_personal_direct:
    vesper "{i}A breath of something that might be a laugh.{/i} Scared. That's a word for people who can still choose to leave. {i}[She slots the barrel into place.]{/i} I'm... aware of consequences."
    jump act1_climax_setup_vesper_personal_depth

label act1_climax_setup_vesper_personal_silent:
    "{i}You sit. The stars turn. Vesper's hands continue their ritual. For a while, that's enough.{/i}"
    jump act1_climax_setup_vesper_personal_depth

label act1_climax_setup_vesper_personal_depth:
    vesper "{i}Quietly, after a long moment.{/i} I've been in operations where people died. I've been the reason some of them didn't. {i}[She looks at the stars.]{/i} But I've never done it with people I—"
    jump act1_climax_setup_vesper_personal_catch

label act1_climax_setup_vesper_personal_catch:
    vesper "{i}She stops. Recalibrates. When she speaks again, the sniper is back.{/i} People I've trained with this long. The calculus changes when you know someone's patterns. Their breathing. Their tells. {i}[Beat.]{/i} It makes you better. And it makes losing them worse."
    jump act1_climax_setup_vesper_personal_resolve

label act1_climax_setup_vesper_personal_resolve:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "So no. I'm not scared. I'm precise. And tomorrow, precision keeps people alive. {i}[She chambers a round—a sound like a period at the end of a sentence.]{/i} Including you."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_rho:
    "{i}The cargo bay. Rho sits surrounded by shaped charges, detonators, and enough ordnance to crack a small moon. His hands move with surprising delicacy—each charge measured, calibrated, placed in sequence.{/i}"
    jump act1_climax_setup_rho_personal_1

label act1_climax_setup_rho_personal_1:
    if game_state.has_flag("rho_bonded"):
        rho "{i}He looks up and smiles—not the sharp grin, but something quieter.{/i} Hey. Grab a seat. I could use the company."
    else:
        rho "{i}Without looking up.{/i} Pull up a crate. Just don't touch the blue ones. Those are temperamental."
    jump act1_climax_setup_rho_personal_choice

label act1_climax_setup_rho_personal_choice:
    "{i}He handles explosives like a sculptor handles clay. There's reverence in it. And underneath the steady hands, something heavier.{/i}"
    menu:
        "You mentioned Meridian. What happened there?":
            jump act1_climax_setup_rho_personal_meridian
        "How do you stay calm before something like this?":
            jump act1_climax_setup_rho_personal_calm
        "[Help him sort the charges in silence]":
            jump act1_climax_setup_rho_personal_help

label act1_climax_setup_rho_personal_meridian:
    rho "{i}His hands slow. Not stop—slow.{/i} Meridian was a mining colony. Corporate dispute turned into a siege. Thirty of us went in to break it. Twelve came out."
    jump act1_climax_setup_rho_meridian_2

label act1_climax_setup_rho_meridian_2:
    rho "{i}He picks up a charge, turns it in his hands.{/i} I tried to hold two positions at once. Ego. I was big enough, strong enough—I thought I could cover both. {i}[His voice drops.]{/i} I was wrong."
    jump act1_climax_setup_rho_personal_truth

label act1_climax_setup_rho_personal_calm:
    rho "{i}He laughs—short, honest.{/i} Calm? I'm not calm. I'm focused. There's a difference. Calm means you think you're safe. Focused means you know you're not, and you're working the problem anyway."
    jump act1_climax_setup_rho_personal_truth

label act1_climax_setup_rho_personal_help:
    "{i}You sort charges by color, by weight, by the careful labels Rho has written in small, neat handwriting. He watches you handle them with respect and nods once—approval.{/i}"
    jump act1_climax_setup_rho_personal_truth

label act1_climax_setup_rho_personal_truth:
    rho "{i}Quieter than you've ever heard him.{/i} I like this crew. I like the way Elia runs things—no thrones, just floors. I like that Vesper insults me and means it as affection. I like that Jalen thinks his way out of problems I'd punch through."
    jump act1_climax_setup_rho_personal_truth_2

label act1_climax_setup_rho_personal_truth_2:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He meets your eyes.{/i} And I like that you're here. A kid with a shard in her skull and more courage than sense. {i}[The grin comes back, but warmer.]{/i} Reminds me why I stopped doing this for money."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_nyx:
    "{i}The engine room. The Lattice conduits pulse with subdued light—the ship's nervous system, half-alive, humming with potential. Nyx sits in the center of it, cross-legged, staff across her knees, eyes closed. The air around her tastes like static.{/i}"
    jump act1_climax_setup_nyx_personal_1

label act1_climax_setup_nyx_personal_1:
    if game_state.has_flag("nyx_bonded"):
        nyx "{i}Eyes opening, and there's warmth in them.{/i} I was reaching for your shard without thinking. It's become a habit. You feel like a lighthouse."
    else:
        nyx "{i}Eyes still closed.{/i} Your shard is loud today. I could feel you coming from two corridors away."
    jump act1_climax_setup_nyx_personal_choice

label act1_climax_setup_nyx_personal_choice:
    "{i}The conduits pulse in time with something—your heartbeat, or hers, or both.{/i}"
    menu:
        "What does the station's Lattice architecture feel like from here?":
            jump act1_climax_setup_nyx_personal_lattice
        "You said you fought a Writbound before. Tell me.":
            jump act1_climax_setup_nyx_personal_writbound
        "[Sit with her. Match your breathing to the conduit pulse.]":
            jump act1_climax_setup_nyx_personal_meditate

label act1_climax_setup_nyx_personal_lattice:
    nyx "{i}She extends a hand, fingers splayed. The air between you shimmers.{/i} Feel it? Even from here—across void, across distance—the station's ward structure broadcasts. Cold. Geometric. Like a scream pressed into a grid."
    jump act1_climax_setup_nyx_personal_fear

label act1_climax_setup_nyx_personal_writbound:
    nyx "{i}Her eyes open. The memory is right there, behind them.{/i} Kallos Station. Three years ago. A containment entity had bonded with a security operative. He could reshape walls, seal doors with a thought, turn the architecture into a weapon. {i}[She touches a scar beneath her collar.]{/i} I won because I'm stubborn and he was overconfident. That's not a strategy I'd recommend."
    jump act1_climax_setup_nyx_personal_fear

label act1_climax_setup_nyx_personal_meditate:
    "{i}You sit. You breathe. The conduits pulse. And for a moment, through the shard, you feel what Nyx feels—the Lattice as a living thing, vast and old and full of doors.{/i}"
    jump act1_climax_setup_nyx_personal_fear

label act1_climax_setup_nyx_personal_fear:
    nyx "{i}After a silence that stretches like taffy:{/i} I'm not afraid of dying. I'm afraid of losing my connection. The Lattice is... it's how I understand the world. If those Writbound wards tear through my defenses—if they sever that—"
    jump act1_climax_setup_nyx_personal_fear_2

label act1_climax_setup_nyx_personal_fear_2:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She shakes her head.{/i} It would be like going deaf. Blind. Worse. It would be like forgetting that music exists. {i}[She looks at you.]{/i} Protect my back in there. Not my body—my focus. Keep them off me long enough to do my work."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_jalen:
    "{i}Jalen's workstation. Six screens, three keyboards, and a coffee cup that's been refilled so many times it's developed geological strata. His eyes move faster than his hands, and his hands are already blurring.{/i}"
    jump act1_climax_setup_jalen_personal_1

label act1_climax_setup_jalen_personal_1:
    if game_state.has_flag("jalen_bonded"):
        jalen "{i}He sees you and immediately saves his work—actually saves and closes a screen. For Jalen, that's the equivalent of a standing ovation.{/i} Hey. Come look at this."
    else:
        jalen "{i}He holds up one finger—wait.{/i} ...{i}typing intensifies{/i}... {i}another thirty seconds{/i}... Done. Partial decryption of their secondary comm channel. {i}[He spins his chair to face you.]{/i} What's up?"
    jump act1_climax_setup_jalen_personal_choice

label act1_climax_setup_jalen_personal_choice:
    "{i}His desk is chaos with a system. Every piece of paper, every data chip, every tangled cable has a place he remembers even if no one else could find it.{/i}"
    menu:
        "Can you walk me through the data extraction protocol? In case something goes wrong.":
            jump act1_climax_setup_jalen_personal_tech
        "How are you holding up?":
            jump act1_climax_setup_jalen_personal_honest
        "[Look at his simulations. Try to understand the numbers.]":
            jump act1_climax_setup_jalen_personal_learn

label act1_climax_setup_jalen_personal_honest:
    jalen "{i}He stops typing. Actually stops. His hands go still on the keys and he stares at them like they belong to someone else.{/i} Holding up. That's a generous way to describe what I'm doing. I'm running simulations because if I stop, I'll think about the fact that I built systems exactly like the ones we're about to break into."
    jump act1_climax_setup_jalen_personal_honest_2

label act1_climax_setup_jalen_personal_honest_2:
    jalen "{i}He looks at you.{/i} I was corporate. Did you know that? Three years as a systems architect for Meridian Industrial. I built the security that kept people like us out. {i}[He swallows.]{/i} Now I'm on this side of the wall, and I keep wondering if someone like me is in there right now, building the thing that kills one of us."
    jump act1_climax_setup_jalen_personal_truth

label act1_climax_setup_jalen_personal_learn:
    "{i}You lean in. The screens show probability cascades, security response models, timing optimizations. The numbers are dense, but patterns emerge—the way Jalen sees the world, translated into data.{/i}"
    jump act1_climax_setup_jalen_personal_learn_2

label act1_climax_setup_jalen_personal_learn_2:
    jalen "{i}He notices you reading. His expression shifts—surprise, then something warmer.{/i} You see the pattern? The security response clusters here—predictable, because corporate doctrine values consistency over creativity. That's their weakness. {i}[He points.]{/i} And that gap is where we get in."
    jump act1_climax_setup_jalen_personal_truth

label act1_climax_setup_jalen_personal_tech:
    jalen "{i}He lights up—genuinely, completely. This is his language.{/i} Okay. The data core is airgapped—no wireless access. Physical terminal only. You'll see a console with a biometric lock. I'll spoof the biometrics remotely if I'm on the hold team, but if comms are down—"
    jump act1_climax_setup_jalen_tech_detail_2

label act1_climax_setup_jalen_tech_detail_2:
    jalen "—you use this. {i}[He hands you a data chip, small and warm.]{/i} Insert it into the console. It'll bypass the biometric and start the data pull. Takes ninety seconds. Don't remove it early or the files corrupt."
    jump act1_climax_setup_jalen_tech_check

label act1_climax_setup_jalen_tech_check:
    "{i}He walks you through the process. Terminal identification, chip insertion, progress indicators. It's not complicated—but in a firefight, nothing is simple.{/i}"
    $ _sc_result = skill_check("tech", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_climax_setup_jalen_tech_success
    else:
        jump act1_climax_setup_jalen_tech_failure

label act1_climax_setup_jalen_tech_success:
    $ game_state.set_flag("avyanna_knows_extraction")
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "{i}Surprised. Pleased.{/i} You picked that up fast. Most people need three run-throughs. {i}[He leans back.]{/i} If I go down, you can finish the extraction. That's... that's good to know."
    jump act1_climax_setup_jalen_personal_truth

label act1_climax_setup_jalen_tech_failure:
    jalen "{i}Patient.{/i} Close. The sequence is insert-confirm-wait. Not insert-wait-confirm. Let's run it again. {i}[He smiles.]{/i} You'll get it. The important part is you asked."
    jump act1_climax_setup_jalen_personal_truth

label act1_climax_setup_jalen_personal_truth:
    jalen "{i}After the tutorial, quieter:{/i} You know what scares me? It's not the guns or the wards. It's the data. What if we get in there and the records show something we can't undo? What if Avyanna's extraction history is worse than we think?"
    jump act1_climax_setup_jalen_personal_truth_2

label act1_climax_setup_jalen_personal_truth_2:
    jalen "{i}He takes off his glasses, rubs his eyes.{/i} I build systems. I believe in information. But some information breaks people. {i}[He puts the glasses back on.]{/i} I guess that's why we have each other. To hold the weight together."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_elisira:
    "{i}The armory. Elisira stands at the workbench, field-stripping her dual pistols with the mechanical grace of a concert pianist warming up. The room smells like gun oil and old metal. She doesn't acknowledge your entry.{/i}"
    jump act1_climax_setup_elisira_personal_1

label act1_climax_setup_elisira_personal_1:
    if game_state.has_flag("elisira_bonded"):
        elisira "{i}She glances over her shoulder—brief, but warm enough to notice.{/i} You. Good. I wanted to say something before tomorrow."
    else:
        elisira "{i}Without turning.{/i} If you're here to ask if I'm alright, the answer is yes. If you're here for something else, say it."
    jump act1_climax_setup_elisira_personal_choice

label act1_climax_setup_elisira_personal_choice:
    "{i}Her hands don't stop moving. Disassemble, clean, reassemble. A ritual older than the crew.{/i}"
    menu:
        "You know Dreeve. Is this personal for you?":
            jump act1_climax_setup_elisira_personal_dreeve
        "What were you, before?":
            jump act1_climax_setup_elisira_personal_before
        "[Pick up a cleaning kit and work on your own weapon beside her]":
            jump act1_climax_setup_elisira_personal_parallel

label act1_climax_setup_elisira_personal_dreeve:
    elisira "{i}Her hands slow—not stop.{/i} I don't know Dreeve. I know the type. The machine made him and the machine will use him until he breaks. {i}[She slots a component into place.]{/i} That's not personal. That's pattern recognition."
    jump act1_climax_setup_elisira_personal_deeper

label act1_climax_setup_elisira_personal_before:
    elisira "{i}A pause. The kind that means she's deciding how much truth to spend.{/i} I was a tool. A very expensive, very effective tool. I did what they pointed me at and I did it well. {i}[Beat.]{/i} That's not who I am now. But it's who I know how to be."
    jump act1_climax_setup_elisira_personal_deeper

label act1_climax_setup_elisira_personal_parallel:
    "{i}You work side by side. The rhythm of maintenance is shared language—clean, inspect, assemble. After a while, the silence becomes comfortable. Elisira's shoulders drop a fraction. That's trust, from her.{/i}"
    jump act1_climax_setup_elisira_personal_deeper

label act1_climax_setup_elisira_personal_deeper:
    elisira "{i}After a long silence:{/i} I chose this crew. Not the other way around. Elia thinks she recruited me. She didn't. I watched them for weeks before I made contact. Measured their patterns. Their ethics. Their weaknesses."
    jump act1_climax_setup_elisira_personal_deeper_2

label act1_climax_setup_elisira_personal_deeper_2:
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "{i}She holds a pistol up to the light, checking the barrel.{/i} They're good people doing hard work without losing themselves. That's rare. That's worth protecting. {i}[She looks at you sidelong.]{/i} So is whatever's growing in you. The shard, the entity—BEE. Don't let anyone take it from you."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_elia:
    "{i}The briefing room, emptied. The holographic station still rotates in blue light. Elia stands at the window, looking out at the dark. She's removed her blade harness—a thing she almost never does. She looks smaller without it.{/i}"
    jump act1_climax_setup_elia_personal_1

label act1_climax_setup_elia_personal_1:
    if game_state.has_flag("elia_bonded"):
        elia "{i}She turns, and there's something unguarded in her expression. Just for a moment.{/i} I'm glad it's you."
    else:
        elia "{i}She knows you're there. She always does.{/i} Thought you'd go find the others first."
    jump act1_climax_setup_elia_personal_choice

label act1_climax_setup_elia_personal_choice:
    "{i}Without the harness, without the table between you, she's just a person carrying too much and pretending it weighs nothing.{/i}"
    menu:
        "How do you carry this? Knowing you might send people to die?":
            jump act1_climax_setup_elia_personal_weight
        "Are we going to make it?":
            jump act1_climax_setup_elia_personal_odds
        "[Say nothing. Just stand beside her and look at the stars.]":
            jump act1_climax_setup_elia_personal_quiet

label act1_climax_setup_elia_personal_weight:
    elia "{i}Long exhale.{/i} I don't carry it. I hold it. There's a difference. Carrying implies you can put it down. {i}[She looks at her hands.]{/i} I hold it because if I let go, someone else has to pick it up, and they might not be strong enough."
    jump act1_climax_setup_elia_personal_truth

label act1_climax_setup_elia_personal_odds:
    elia "{i}She turns to face you. Direct.{/i} Honestly? I don't know. The math says no. The crew says yes. {i}[A ghost of a smile.]{/i} I've always bet on people over numbers."
    jump act1_climax_setup_elia_personal_truth

label act1_climax_setup_elia_personal_quiet:
    "{i}You stand together. The stars don't care about your plans. The dark doesn't know your names. But here, in this small room, two people look at the void and choose not to blink.{/i}"
    jump act1_climax_setup_elia_personal_truth

label act1_climax_setup_elia_personal_truth:
    elia "{i}Quietly. The voice she uses when the floor is just her and the truth.{/i} When I started this crew, I had a rule: don't love them. Keep it professional. Respect, competence, clear roles. Don't make it personal."
    jump act1_climax_setup_elia_personal_truth_2

label act1_climax_setup_elia_personal_truth_2:
    elia "{i}She laughs—a short, broken sound.{/i} I failed that rule the first week. Rho made me laugh. Vesper made me think. Nyx made me wonder. Jalen made me hope. Elisira made me trust. And you—"
    jump act1_climax_setup_elia_personal_truth_3

label act1_climax_setup_elia_personal_truth_3:
    $ relationship_manager.process_reputation_affinity("elia", 2)
    elia "{i}She stops. Starts again.{/i} You made me remember why I do this. Not the contracts. Not the survival. The {i}people{/i}. {i}[She meets your eyes.]{/i} So yes. We're going to make it. Because I refuse to lose any of you."
    jump act1_climax_setup_personal_return

label act1_climax_setup_personal_return:
    "{i}You return to the common area. The ship hums around you—alive, waiting, faithful.{/i}"
    menu:
        "[Speak with someone else]":
            jump act1_climax_setup_personal_moments_choice
        "[Head to the briefing room. It's time.]":
            jump act1_climax_setup_three_hours_later

label act1_climax_setup_three_hours_later:
    "{i}Three hours pass. Some of it is spent in silence. Some in the quiet work of preparation—weapons checked, charges calibrated, Lattice focuses aligned. The ship's corridors feel different now. Charged. Like the air before a storm knows what's coming.{/i}"
    jump act1_climax_setup_equipment_check_intro

label act1_climax_setup_equipment_check_intro:
    "{i}The gear-up room. Everyone present. The smell of gun oil, ozone, and the faint copper tang of charged Lattice components. Armor is donned in ritual silence.{/i}"
    jump act1_climax_setup_equipment_vesper

label act1_climax_setup_equipment_vesper:
    "{i}Vesper assembles Clarity—her primary rifle—with movements so practiced they're indistinguishable from breathing. Each component clicks into place: stock, barrel, scope, suppressor. She chambers a round and the sound is a full stop.{/i}"
    jump act1_climax_setup_equipment_rho

label act1_climax_setup_equipment_rho:
    "{i}Rho shrugs into his chest plate—scarred ceramic over ballistic weave, heavy enough to stop most things that would kill a normal person. He loads the rotary cannon's drum magazine with the tenderness of a parent tucking in a child. Shaped charges go into bandoliers. He doesn't count them. He knows.{/i}"
    jump act1_climax_setup_equipment_nyx

label act1_climax_setup_equipment_nyx:
    "{i}Nyx draws Lattice patterns on her forearms in conductive ink—temporary circuits that amplify her connection to the Threshold staff. The ink glows faintly, then settles into her skin like tattoos. She mouths words in a language that predates the Compact.{/i}"
    jump act1_climax_setup_equipment_jalen

label act1_climax_setup_equipment_jalen:
    "{i}Jalen straps a portable terminal to his forearm, connects three redundant comm units, and pockets seven data chips. He's already running diagnostics on each one. His sidearm goes into a hip holster—last, almost an afterthought.{/i}"
    jump act1_climax_setup_equipment_elisira

label act1_climax_setup_equipment_elisira:
    "{i}Elisira's preparation is the most economical. Two pistols—checked, loaded, holstered in a cross-draw rig. A thin-bladed knife in each boot. Light body armor under her jacket. She looks like she's going for a walk. That's the point.{/i}"
    jump act1_climax_setup_equipment_elia

label act1_climax_setup_equipment_elia:
    "{i}Elia belts her blade harness—twin short swords, balanced for corridor work. She tests the draw, once, twice, three times. The blades sing. She adds a compact sidearm, almost hidden. Last: she pulls her hair back and ties it. War face. Ready.{/i}"
    jump act1_climax_setup_equipment_avyanna

label act1_climax_setup_equipment_avyanna:
    "{i}You gear up. Light armor—you're not built for heavy combat yet, and the shard's weight is its own burden. A sidearm. A comm unit. Jalen's extraction chip in your inner pocket, close to your heart. And beneath it all, the shard pulses—steady, warm, aware.{/i}"
    jump act1_climax_setup_bee_equipment_scan

label act1_climax_setup_bee_equipment_scan:
    bee "{{BEE:: host-systems nominal | shard-resonance stable | combat-readiness assessed | personal note: I will be with you in the dark places—you will not walk alone}}"
    jump act1_climax_setup_equipment_insight_check

label act1_climax_setup_equipment_insight_check:
    "{i}As the crew finishes gearing up, you study their faces. Their movements. Something about the way they prepare tells you things words can't.{/i}"
    $ _sc_result = skill_check("insight", 13, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_climax_setup_insight_success
    else:
        jump act1_climax_setup_insight_pass

label act1_climax_setup_insight_success:
    "{i}You see it—the tells. Rho's grin doesn't reach his eyes. Vesper's breathing is too controlled, compensating for adrenaline. Jalen's hands are steady but he keeps touching his sidearm like he's reminding himself it's there. Elisira is the calmest, which means she's the most prepared for the worst. Nyx's conductive ink is slightly asymmetrical—she redrew the left arm pattern. Her writing hand shook.{/i}"
    jump act1_climax_setup_insight_elia_detail

label act1_climax_setup_insight_elia_detail:
    $ game_state.set_flag("insight_crew_reads")
    "{i}And Elia. Elia has checked her blades three times instead of the usual two. She's running the numbers in her head—who might not come back, and what she'll do if that happens. She's already carrying the grief of losses that haven't occurred yet.{/i}"
    jump act1_climax_setup_waffle_climax_ready

label act1_climax_setup_insight_pass:
    "{i}The crew is ready. Whatever they're feeling, they've packed it behind the armor and the weapons and the trained composure. Professionals.{/i}"
    jump act1_climax_setup_waffle_climax_ready

label act1_climax_setup_waffle_climax_ready:
    waffle "{i}}{{WAFFLE.BAT// ALL_SYSTEMS: combat ready | CREW_VITALS: elevated but stable | PERSONAL_NOTE: bring everyone home. please.}}{/i}}"
    jump act1_climax_setup_bubbles_climax_care

label act1_climax_setup_bubbles_climax_care:
    bubbles "{i}Softly, through the briefing room speakers:{/i} I'll be watching. All of you. Come back safe."
    jump act1_climax_setup_cinnamon_climax_ops

label act1_climax_setup_cinnamon_climax_ops:
    cinnamon "Ship locked for combat. All subsystems optimal. Go."
    jump act1_climax_setup_elia_speech_setup

label act1_climax_setup_elia_speech_setup:
    "{i}The crew stands in the briefing room. Armed. Armored. Ready. The holographic station turns between them like a ghost they're about to make real. Elia steps to the head of the table. She doesn't lean on it this time. She stands straight.{/i}"
    jump act1_climax_setup_elia_speech_1

label act1_climax_setup_elia_speech_1:
    elia "I'm not going to give you a speech about duty. You know duty. You live it every day on this ship, in every job we take, in every choice we make to stay together when walking away would be easier."
    jump act1_climax_setup_elia_speech_2

label act1_climax_setup_elia_speech_2:
    elia "I'm not going to tell you the odds. Jalen already ran them. They're bad. {i}[A few grim smiles around the table.]{/i} But we've beaten bad odds before. That's not luck. That's us."
    jump act1_climax_setup_elia_speech_3

label act1_climax_setup_elia_speech_3:
    elia "What I will tell you is this: inside that station are records that will determine whether Avyanna lives free or gets dragged back into a cage. {i}[She looks at you.]{/i} She's one of us. That makes this simple."
    jump act1_climax_setup_elia_speech_4

label act1_climax_setup_elia_speech_4:
    elia "{i}Harder. Commander voice.{/i} But I want to be clear about something. This is not a suicide mission. We go in, we get the data, we get out. If the objective becomes impossible, we abort. If someone goes down, we carry them. If we have to choose between the data and a life—"
    jump act1_climax_setup_elia_speech_5

label act1_climax_setup_elia_speech_5:
    elia "{i}She looks at each of them. One at a time. Taking the measure.{/i} —we choose the life. Every time. No data is worth more than any one of you. {i}[Beat.]{/i} Not even mine."
    jump act1_climax_setup_elia_speech_6

label act1_climax_setup_elia_speech_6:
    elia "{i}Quieter now. Personal.{/i} I found each of you in different places. Different kinds of broken. Different kinds of strong. And we built something here—in this ugly ship, with these mismatched chairs, with a floor that holds because we {i}make{/i} it hold."
    jump act1_climax_setup_elia_speech_7

label act1_climax_setup_elia_speech_7:
    elia "{i}Her voice is steady. Her eyes are not.{/i} I am proud. Of all of you. Of what we are. And I am asking you to walk into something dangerous, not because I have the right to ask, but because you've given me that right. Every day. By staying."
    jump act1_climax_setup_elia_speech_8

label act1_climax_setup_elia_speech_8:
    elia "{i}She draws one blade—not a threat. A salute.{/i} So let's go take what's ours. And let's come home."
    jump act1_climax_setup_speech_reaction

label act1_climax_setup_speech_reaction:
    "{i}For a moment, no one moves. Then Rho slams a fist against his chest plate—once, hard, resonant. Vesper nods. Nyx raises her staff. Jalen closes his screens. Elisira draws a pistol and holds it up, barrel to the ceiling. And you—{/i}"
    jump act1_climax_setup_speech_player_choice

label act1_climax_setup_speech_player_choice:
    "{i}The crew waits for you. The newest member. The reason for all of it.{/i}"
    menu:
        "[Draw your weapon and raise it with the crew]":
            jump act1_climax_setup_speech_response_weapon
        "[Place your hand over the shard at your neck — your answer is in the pulse of it]":
            jump act1_climax_setup_speech_response_shard
        "[Simply say: 'Floor holds.']":
            jump act1_climax_setup_speech_response_words

label act1_climax_setup_speech_response_weapon:
    "{i}You draw your sidearm and raise it. The gesture is understood—you are one of them. The weapon is a promise: you'll fight. You'll stay. You'll hold the floor.{/i}"
    jump act1_climax_setup_elia_floor_holds

label act1_climax_setup_speech_response_shard:
    "{i}Your hand finds the shard. It pulses—once, strong, warm—and the Lattice conduits in the room flicker in response. BEE's presence fills the space between your heartbeats. You are not just crew. You are the reason the cage will open.{/i}"
    jump act1_climax_setup_bee_speech_response

label act1_climax_setup_bee_speech_response:
    bee "{{BEE:: host-affirmation registered | crew-bond acknowledged | the floor holds because we hold it—all of us, living and lattice-born}}"
    jump act1_climax_setup_elia_floor_holds

label act1_climax_setup_speech_response_words:
    avyanna "{i}Quiet. Certain.{/i} Floor holds."
    jump act1_climax_setup_speech_response_words_react

label act1_climax_setup_speech_response_words_react:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    "{i}Two words. But from you—the person they're risking everything for—they land like an oath. Elia's eyes shine. She nods once.{/i}"
    jump act1_climax_setup_elia_floor_holds

label act1_climax_setup_elia_floor_holds:
    elia "{i}Voice steady, ritual.{/i} Floor holds."
    jump act1_climax_setup_crew_response

label act1_climax_setup_crew_response:
    "{i}The response is immediate, overlapping, muscle memory.{/i} 'Floor holds.'"
    jump act1_climax_setup_elia_final_words

label act1_climax_setup_elia_final_words:
    elia "We go in four hours. Gear up. Rest if you can. {i}[She looks at each person.]{/i} We're getting those records. And we're all coming home."
    jump act1_climax_setup_final_tactical_review

label act1_climax_setup_final_tactical_review:
    "{i}The final hour. The crew runs through comms checks, weapon safeties, and one last review of the station schematic. Tension has crystallized into focus.{/i}"
    jump act1_climax_setup_jalen_comms_check

label act1_climax_setup_jalen_comms_check:
    jalen "Comms check. Assault team, channel alpha. Hold team, channel bravo. Emergency fallback on channel delta. {i}[He taps his earpiece.]{/i} If you hear static on alpha, switch to delta immediately. If delta goes down—"
    jump act1_climax_setup_jalen_comms_check_2

label act1_climax_setup_jalen_comms_check_2:
    jalen "{i}He pauses.{/i} If delta goes down, fall back to visual signals. Rho's flares. Vesper's tracer rounds. Nyx's Lattice pulse. We've drilled this. Trust the training."
    jump act1_climax_setup_vesper_final_review

label act1_climax_setup_vesper_final_review:
    vesper "Overwatch positions mapped. Primary, secondary, and tertiary fallback points for extraction. {i}[She looks at the schematic one final time.]{/i} Sight lines confirmed. Counter-sniper protocols loaded. If they have marksmen, I'll find them first."
    jump act1_climax_setup_rho_final_review

label act1_climax_setup_rho_final_review:
    rho "Breach charges calibrated. Three for bulkheads, two for emergency access, one reserve. {i}[He holds up the last charge.]{/i} This one's for something we haven't planned for. There's always something."
    jump act1_climax_setup_nyx_final_review

label act1_climax_setup_nyx_final_review:
    nyx "Lattice disruption array is primed. I'll hit their outer wards the moment we're in range. The inner wards—the old ones—I'll assess in real-time. {i}[She flexes her fingers and the conductive ink glows.]{/i} I'm ready."
    jump act1_climax_setup_elisira_final_review

label act1_climax_setup_elisira_final_review:
    elisira "Suppressed pistols, close-quarters loadout, Dreeve's likely command post flagged on the schematic. {i}[She checks her watch—mechanical, analog, the only non-digital thing about her.]{/i} Two minutes to insertion window."
    jump act1_climax_setup_bee_final_analysis

label act1_climax_setup_bee_final_analysis:
    bee "{{BEE:: final tactical assessment | all variables logged | crew cohesion: maximum observed value | probability models inadequate for this variable | conclusion: they will exceed expectations—they always do}}"
    jump act1_climax_setup_final_departure_narration

label act1_climax_setup_final_departure_narration:
    "{i}The ship drops out of drift. The station appears in the viewport—a dark shape against darker void, running lights blinking like a mechanical heartbeat. It looks small from here. It won't feel small inside.{/i}"
    jump act1_climax_setup_elia_go_order

label act1_climax_setup_elia_go_order:
    elia "{i}One last look at her crew. Every face. Every name she carries.{/i} Teams to positions. Assault team forward. Hold team, secure extraction on my mark."
    jump act1_climax_setup_elia_go_order_2

label act1_climax_setup_elia_go_order_2:
    elia "{i}Her hand finds the hilt of her blade. The ritual begins.{/i} We go quiet. We go fast. We go together. {i}[She inhales. Holds it.]{/i}"
    jump act1_climax_setup_elia_go_final

label act1_climax_setup_elia_go_final:
    elia "{b}Go.{/b}"
    jump act1_climax_setup_end_briefing

label act1_climax_setup_end_briefing:
    "{i}The airlock opens. The station waits. Seven people step forward into the dark—armed, afraid, and unwilling to let fear make the choice for them. The floor holds. The floor always holds. Until it doesn't. And then you find out what you're really made of.{/i}"
    menu:
        "[Continue]":
            $ game_state.set_flag("act1_climax_ready")
            return
