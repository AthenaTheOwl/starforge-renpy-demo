## act1_party_split_briefing.rpy — Auto-generated from act1_party_split_briefing.json
## 131 dialogue nodes

label act1_party_split_briefing:
    $ game_state.mark_dialogue_played("act1_party_split_briefing")
    jump act1_party_split_briefing_start

label act1_party_split_briefing_start:
    "{i}The war room aboard the Lumen Thief. Harsh overhead lighting cuts sharp shadows across the central holo-table. Star charts and facility schematics hover in pale blue wireframe. Coffee dregs and stimulant wrappers litter every surface. Nobody has slept. Nobody pretends they will.{/i}"
    jump act1_party_split_briefing_elia_calls_order

label act1_party_split_briefing_elia_calls_order:
    elia "{i}Rapping her knuckles on the table.{/i} Everyone in. Seal the door. This is the last time we go over this—so listen like your life depends on it, because it does."
    jump act1_party_split_briefing_crew_assembles

label act1_party_split_briefing_crew_assembles:
    "{i}They file in. Rho leans against the bulkhead, arms folded across his chest plate. Vesper takes the chair furthest from the door—old sniper habit, eyes on every exit. Nyx perches on the edge of the table itself, staff across her knees. Jalen slides into his tech station, fingers already dancing across three screens. Elisira stands at parade rest beside the holo-table, datapad in hand.{/i}"
    jump act1_party_split_briefing_elisira_intel_intro

label act1_party_split_briefing_elisira_intel_intro:
    elisira "{i}Activating the holo-table. A facility schematic blooms into view—layered, detailed, annotated in her precise handwriting.{/i} I pulled this from a dead-drop my contact embedded in the Lattice's procurement chain. It cost them their cover. Let's not waste it."
    jump act1_party_split_briefing_facility_overview

label act1_party_split_briefing_facility_overview:
    "{i}The hologram rotates. A fortified compound—part research lab, part military installation. Three concentric rings of defense. Underground levels descending into bedrock. Ward signatures pulse in angry red along every chokepoint.{/i}"
    jump act1_party_split_briefing_elisira_layout_detail

label act1_party_split_briefing_elisira_layout_detail:
    elisira "Designation: Site Onyx. Three perimeter rings. Outer ring is automated—turrets, sensor nets, drone patrols on six-minute cycles. Middle ring is personnel—guards rotating in four-hour shifts. Inner ring..."
    jump act1_party_split_briefing_elisira_layout_inner

label act1_party_split_briefing_elisira_layout_inner:
    elisira "{i}Zooming in. The innermost structure pulses with ward-light.{/i} Inner ring is where it gets ugly. Lattice-woven barriers. Threshold locks that require living ward-signatures to pass. And the command center sits three levels below ground."
    jump act1_party_split_briefing_bee_tactical_overlay

label act1_party_split_briefing_bee_tactical_overlay:
    bee "{{BEE:: FACILITY_ANALYSIS: Site Onyx defensive topology mapped | STATUS: 94.2%% schema confidence | DETAIL: subsurface resonance patterns suggest additional ward layers not visible on procurement schematics—recommend caution at depth}}"
    jump act1_party_split_briefing_nyx_ward_warning

label act1_party_split_briefing_nyx_ward_warning:
    nyx "{i}Leaning forward, staff humming faintly.{/i} Those Lattice barriers aren't standard containment wards. I've seen this signature pattern before—they're layered. Break one, two more activate underneath. Like a hydra made of bad math."
    jump act1_party_split_briefing_nyx_ward_detail

label act1_party_split_briefing_nyx_ward_detail:
    if game_state.has_flag("nyx_trust_high"):
        nyx "I've been studying the resonance patterns BEE flagged. I think I can unravel them—but I'll need time and no one shooting at me while I work."
    elif game_state.has_flag("nyx_trust_low"):
        nyx "I can probably crack them. Probably. No guarantees when the Lattice is involved."
    else:
        nyx "And the threshold locks? They'll burn out anyone who tries to brute-force them. I'm talking neural scorching. Permanent damage. We need finesse, not firepower, for those."
    jump act1_party_split_briefing_player_ask_nyx_detail

label act1_party_split_briefing_player_ask_nyx_detail:
    menu:
        "How long to dismantle each ward layer?":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_party_split_briefing_nyx_time_estimate
        "What happens if you can't crack them?":
            jump act1_party_split_briefing_nyx_contingency
        "We'll make sure you have the time. What do you need?":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_party_split_briefing_nyx_requirements

label act1_party_split_briefing_nyx_time_estimate:
    nyx "Three minutes per layer if I'm undisturbed. Six if someone's shooting. Infinite if I'm dead. So—priorities."
    jump act1_party_split_briefing_vesper_strategy_intro

label act1_party_split_briefing_nyx_contingency:
    nyx "{i}A flicker of something dark behind her eyes.{/i} Then we find another way in. Or we don't get in at all. The Lattice doesn't leave back doors—they leave traps that look like back doors."
    jump act1_party_split_briefing_vesper_strategy_intro

label act1_party_split_briefing_nyx_requirements:
    nyx "{i}Surprised—then a careful nod.{/i} Silence. Proximity to the ward anchor points. And someone watching my back who won't panic when the light show starts."
    jump act1_party_split_briefing_vesper_strategy_intro

label act1_party_split_briefing_vesper_strategy_intro:
    vesper "{i}Standing, moving to the holo-table. She traces a route along the facility's eastern approach.{/i} Here's how I see it. Two teams. One loud, one quiet. The loud team hits the outer ring hard—draws every guard, every drone, every automated response to the eastern perimeter."
    jump act1_party_split_briefing_vesper_strategy_detail

label act1_party_split_briefing_vesper_strategy_detail:
    vesper "Meanwhile, the quiet team slips in through the maintenance conduits on the western subsurface level. Jalen's scans show a thirty-second gap in the sensor net during shift rotation. That's our window."
    jump act1_party_split_briefing_rho_disagrees

label act1_party_split_briefing_rho_disagrees:
    rho "{i}Pushing off the bulkhead, jaw set.{/i} Thirty seconds. You want to thread a needle in thirty seconds while people are shooting at us on the other side of the building. That's not a plan—that's a prayer."
    jump act1_party_split_briefing_rho_counter_proposal

label act1_party_split_briefing_rho_counter_proposal:
    if game_state.has_flag("rho_trust_high"):
        rho "I've run breaches like this before. On Kael-7. We lost zero—because we didn't give them time to think."
    elif game_state.has_flag("rho_trust_low"):
        rho "I know what I'm talking about. You want surgical? Fine. But don't come crying when surgical gets people killed."
    else:
        rho "I say we hit them with everything. Blow the eastern wall, pour through before they can regroup. Speed and violence. By the time they figure out what's happening, we're already inside."
    jump act1_party_split_briefing_vesper_rho_tension

label act1_party_split_briefing_vesper_rho_tension:
    vesper "{i}Cold and precise.{/i} Speed and violence gets people killed when the building is laced with wards that trigger on kinetic impact. You blow that wall, Nyx's hydra wakes up, and we're fighting the building and the garrison."
    jump act1_party_split_briefing_rho_fires_back

label act1_party_split_briefing_rho_fires_back:
    rho "{i}Voice rising.{/i} And your thirty-second window gets one team killed if the timing's off by three seconds. At least my plan keeps us together—"
    jump act1_party_split_briefing_elia_intervenes

label act1_party_split_briefing_elia_intervenes:
    elia "{i}Flat. Final.{/i} Enough. Both of you."
    jump act1_party_split_briefing_elia_takes_control

label act1_party_split_briefing_elia_takes_control:
    elia "{i}Looking between them.{/i} You're both right. And you're both wrong. A full assault triggers the wards. A pure stealth approach leaves no fallback if something goes sideways. So we do both—but we do it smart."
    jump act1_party_split_briefing_player_tactics_check

label act1_party_split_briefing_player_tactics_check:
    "{i}Elia looks to you. The crew follows her gaze. This is where your input matters.{/i}"
    menu:
        "[Diplomacy] Propose a coordinated timing strategy—assault draws response exactly when infiltration needs the gap widened.":
            $ _sc_result = skill_check("Diplomacy", 14, "avyanna")
            return
        "Vesper's right—stealth first, force only as backup.":
            $ relationship_manager.process_reputation_affinity("vesper", 1)
            jump act1_party_split_briefing_side_with_vesper
        "Rho has a point—overwhelming force means fewer variables.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_party_split_briefing_side_with_rho

label act1_party_split_briefing_tactics_success:
    $ game_state.set_flag("briefing_tactics_passed")
    "{i}You sketch a timing overlay on the holo-table. Assault hits at T-zero. Infiltration moves at T-plus-fifteen, when the garrison has fully committed east. A rolling distraction that builds, giving the quiet team progressively more room.{/i}"
    jump act1_party_split_briefing_crew_impressed

label act1_party_split_briefing_crew_impressed:
    elisira "{i}Studying the overlay. A single nod.{/i} Staggered escalation. The garrison commits deeper with each wave, pulling further from the western approach. It's clean."
    jump act1_party_split_briefing_elia_approves_tactics

label act1_party_split_briefing_elia_approves_tactics:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    $ relationship_manager.process_reputation_affinity("rho", 1)
    elia "{i}A ghost of a smile.{/i} That's the plan, then. Vesper, Rho—you both get your wish. Just on a timer."
    jump act1_party_split_briefing_jalen_tech_options

label act1_party_split_briefing_tactics_failure:
    "{i}Your timing proposal has gaps—Elisira spots the overlap where both teams would be exposed simultaneously. The crew exchanges glances.{/i}"
    jump act1_party_split_briefing_elisira_corrects

label act1_party_split_briefing_elisira_corrects:
    $ game_state.set_flag("briefing_elisira_corrected")
    elisira "{i}Gently adjusting your overlay.{/i} The concept is sound, but the timing needs refinement. Here—if we offset the second wave by ninety seconds, the gap closes."
    jump act1_party_split_briefing_elia_approves_corrected

label act1_party_split_briefing_elia_approves_corrected:
    elia "Good bones. Elisira's adjustment seals it. We run with this."
    jump act1_party_split_briefing_jalen_tech_options

label act1_party_split_briefing_side_with_vesper:
    vesper "{i}A measured nod.{/i} Stealth gets us to the objective without waking the whole compound. The assault team holds ready as contingency—overwhelming force in reserve, not as an opening move."
    jump act1_party_split_briefing_rho_reluctant_agree_vesper

label act1_party_split_briefing_rho_reluctant_agree_vesper:
    $ game_state.set_flag("briefing_stealth_priority")
    rho "{i}Jaw working. Then a sharp exhale.{/i} Fine. But the second something goes wrong, I'm coming through that wall whether there are wards or not."
    jump act1_party_split_briefing_jalen_tech_options

label act1_party_split_briefing_side_with_rho:
    rho "{i}A sharp, approving nod.{/i} Hit them hard enough that they're too busy surviving to notice anyone slipping through the cracks. Classic hammer-and-scalpel."
    jump act1_party_split_briefing_vesper_reluctant_agree_rho

label act1_party_split_briefing_vesper_reluctant_agree_rho:
    $ game_state.set_flag("briefing_assault_priority")
    vesper "{i}Lips thin. But she adjusts.{/i} Then we build in more redundancy for the infiltration route. If the assault is the primary action, the quiet team needs three exit paths, not one."
    jump act1_party_split_briefing_jalen_tech_options

label act1_party_split_briefing_jalen_tech_options:
    jalen "{i}Spinning a display toward the group. Three options shimmer in green wireframe.{/i} Tech support. I've been working on some things. Pick your poison."
    jump act1_party_split_briefing_jalen_options_detail

label act1_party_split_briefing_jalen_options_detail:
    jalen "Option one: I loop their sensor net. Gives infiltration team ghost status for about eight minutes before they detect the spoof. Option two: I crash their comms—garrison can't coordinate, but they'll know something's wrong immediately. Option three: I piggyback on their drone network and feed false positional data."
    jump act1_party_split_briefing_player_tech_choice

label act1_party_split_briefing_player_tech_choice:
    menu:
        "[Tech] Can you run the sensor loop AND the drone piggyback simultaneously?":
            $ _sc_result = skill_check("tech", 12, "avyanna")
            return
        "Sensor loop. Ghost the infiltration team.":
            $ game_state.set_flag("briefing_sensor_loop")
            jump act1_party_split_briefing_jalen_sensor_loop
        "Crash their comms. Blind and deaf is better than invisible.":
            $ game_state.set_flag("briefing_comms_crash")
            jump act1_party_split_briefing_jalen_comms_crash
        "Drone piggyback. Make them chase ghosts.":
            $ game_state.set_flag("briefing_drone_spoof")
            jump act1_party_split_briefing_jalen_drone_spoof

label act1_party_split_briefing_jalen_dual_tech_success:
    $ game_state.set_flag("briefing_dual_tech")
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "{i}Eyes lighting up.{/i} You know what—yeah. If I reroute the buffer through BEE's processing matrix, I can stagger them. Sensor loop first, drone piggyback kicks in when the loop degrades. Seamless handoff."
    jump act1_party_split_briefing_bee_confirms_dual

label act1_party_split_briefing_bee_confirms_dual:
    bee "{{BEE:: PROCESSING_ALLOCATION: approved | STATUS: matrix capacity sufficient for dual-channel operation | DETAIL: estimated coverage extension from 8 minutes to 14.7 minutes with cascaded handoff protocol}}"
    jump act1_party_split_briefing_team_composition_intro

label act1_party_split_briefing_jalen_dual_tech_fail:
    jalen "{i}Frowning, running numbers.{/i} I... wish. But the bandwidth isn't there. Running both would create interference patterns they'd detect faster than running neither. Pick one, and I'll make it count."
    jump act1_party_split_briefing_player_tech_fallback

label act1_party_split_briefing_player_tech_fallback:
    menu:
        "Sensor loop. Ghost the infiltration team.":
            $ game_state.set_flag("briefing_sensor_loop")
            jump act1_party_split_briefing_jalen_sensor_loop
        "Drone piggyback. Make them chase phantoms.":
            $ game_state.set_flag("briefing_drone_spoof")
            jump act1_party_split_briefing_jalen_drone_spoof

label act1_party_split_briefing_jalen_sensor_loop:
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "Sensor loop it is. Eight minutes of invisibility. After that, you're on your own eyes and instincts. Use every second."
    jump act1_party_split_briefing_team_composition_intro

label act1_party_split_briefing_jalen_comms_crash:
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "Comms crash. When it hits, they'll have about forty-five seconds of total chaos. No orders, no coordination, no calling reinforcements. Make those forty-five seconds ugly."
    jump act1_party_split_briefing_team_composition_intro

label act1_party_split_briefing_jalen_drone_spoof:
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "Drone spoof, locked. Their own surveillance will tell them we're hitting from the north while we're already inside from the west. Beautiful misdirection."
    jump act1_party_split_briefing_team_composition_intro

label act1_party_split_briefing_team_composition_intro:
    elia "{i}Pulling up the crew roster on the holo-table. Seven names. Two columns.{/i} Two teams. Infiltration gets in quiet, reaches the command center, pulls the data. Assault holds the perimeter, draws fire, and covers extraction. Who goes where matters."
    jump act1_party_split_briefing_elisira_strengths_briefing

label act1_party_split_briefing_elisira_strengths_briefing:
    elisira "For infiltration, you want precision shooters, ward-breakers, and someone who can navigate the subsurface layout. For assault, you want firepower, durability, and the ability to hold a position under sustained pressure."
    jump act1_party_split_briefing_character_strengths_overview

label act1_party_split_briefing_character_strengths_overview:
    "{i}The holo-table lights each crew member's profile as Elisira speaks. Combat ratings, specializations, equipment loadouts—all rendered in cold blue light.{/i}"
    jump act1_party_split_briefing_elisira_assessments

label act1_party_split_briefing_elisira_assessments:
    elisira "Rho—heavy weapons, breaching, sustained fire. Born for assault. Vesper—precision marksmanship, overwatch, counter-sniper. Valuable either side, but her range makes her devastating on assault perimeter. Nyx—ward disruption is non-negotiable for infiltration. She goes quiet side."
    jump act1_party_split_briefing_elisira_assessments_2

label act1_party_split_briefing_elisira_assessments_2:
    elisira "Jalen—tech support operates remotely, but physical placement matters for signal strength. Closer to the facility core means stronger spoofing. Elia—close-quarters specialist. Either role, but her blade work shines in corridors. And myself—I can lead either team."
    jump act1_party_split_briefing_elisira_assessments_avyanna

label act1_party_split_briefing_elisira_assessments_avyanna:
    elisira "{i}Looking at you.{/i} Avyanna—your shard resonance gives you ward sensitivity. You'll feel Lattice traps before anyone else. That makes you an asset on infiltration. But the call is yours."
    jump act1_party_split_briefing_player_insight_check

label act1_party_split_briefing_player_insight_check:
    "{i}You study the facility layout, the crew profiles, the ward signatures. Something about the defensive pattern nags at you.{/i}"
    menu:
        "[Insight] Study the ward pattern more closely—something doesn't add up.":
            $ _sc_result = skill_check("insight", 12, "avyanna")
            return
        "Stick with Elisira's assessment. She knows what she's doing.":
            jump act1_party_split_briefing_team_assignment_choice

label act1_party_split_briefing_insight_success:
    $ game_state.set_flag("briefing_ward_insight")
    avyanna "{i}Tracing the ward pattern on the holo-table.{/i} Wait. These ward signatures—they're not just defensive. They're channeling something. The inner ring isn't protecting the command center. It's feeding it. If the assault team hits the outer wards hard enough, it might actually strengthen the inner barriers."
    jump act1_party_split_briefing_nyx_confirms_insight

label act1_party_split_briefing_nyx_confirms_insight:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Eyes widening.{/i} She's right. Sympathetic resonance. The outer wards are tethered to the inner ones. Kinetic disruption on the perimeter would cascade inward as reinforcement. The assault team needs to suppress, not destroy—or I'll be cracking twice the barriers underground."
    jump act1_party_split_briefing_elia_adjusts_plan

label act1_party_split_briefing_elia_adjusts_plan:
    elia "{i}Nodding slowly.{/i} Good catch. Rho—you heard her. Assault team suppresses, doesn't shatter. Controlled violence. Can you do that?"
    jump act1_party_split_briefing_rho_controlled_violence

label act1_party_split_briefing_rho_controlled_violence:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}A beat. Then a grudging nod.{/i} Controlled violence. I can do controlled. Might not enjoy it as much."
    jump act1_party_split_briefing_team_assignment_choice

label act1_party_split_briefing_insight_failure:
    "{i}The ward patterns blur together. You sense something beneath the surface, but it slips away before you can articulate it. The feeling of almost-knowing lingers like a word on the tip of your tongue.{/i}"
    jump act1_party_split_briefing_team_assignment_choice

label act1_party_split_briefing_team_assignment_choice:
    elia "{i}Arms crossed.{/i} I have a recommended split. But you've earned a voice in this, Avyanna. How do you want to run it?"
    jump act1_party_split_briefing_player_team_choice

label act1_party_split_briefing_player_team_choice:
    menu:
        "Infiltration: Nyx, Elisira, Jalen, and me. Assault: Elia, Rho, Vesper. Close-quarters dominance on the perimeter.":
            $ game_state.set_flag("assault_team_close_quarters")
            jump act1_party_split_briefing_assault_cq_reaction
        "Infiltration: Nyx, Elisira, Rho, and me. Assault: Elia, Vesper, Jalen, Avyanna coordinating. Mixed-range flexibility.":
            $ game_state.set_flag("assault_team_mixed_range")
            jump act1_party_split_briefing_assault_mixed_reaction
        "Infiltration: Nyx, Elisira, Jalen, Rho. Assault: Elia, Vesper, and me. Tactical precision underground, I hold the line above.":
            $ game_state.set_flag("assault_team_tactical_precision")
            jump act1_party_split_briefing_assault_precision_reaction
        "Go with Elia's recommendation.":
            jump act1_party_split_briefing_elia_default_split

label act1_party_split_briefing_assault_cq_reaction:
    rho "Perimeter assault with Elia and Vesper. Close, mid, and long range covered. {i}Cracking his knuckles.{/i} They won't get past us."
    jump act1_party_split_briefing_vesper_cq_react

label act1_party_split_briefing_vesper_cq_react:
    if game_state.has_flag("vesper_trust_high"):
        vesper "I'll keep every exit covered. Nobody flanks us. Nobody."
    elif game_state.has_flag("vesper_trust_low"):
        vesper "Standard overwatch. Don't get in my sight lines."
    else:
        vesper "Overwatch on the assault. I'll keep their heads down while you two close the distance. Clean geometry."
    jump act1_party_split_briefing_gear_check_intro

label act1_party_split_briefing_assault_mixed_reaction:
    elia "Mixed composition gives us flexibility. Vesper on overwatch, me on close-quarters anchor, Jalen managing comms from the assault position. Avyanna coordinates between teams."
    jump act1_party_split_briefing_jalen_mixed_react

label act1_party_split_briefing_jalen_mixed_react:
    jalen "{i}Nodding, already recalculating signal routes.{/i} If I'm topside with the assault team, my spoofing range increases by forty percent. Closer to the facility's broadcast array means better signal injection."
    jump act1_party_split_briefing_gear_check_intro

label act1_party_split_briefing_assault_precision_reaction:
    elisira "Surgical team below. Nyx for wards, Jalen for tech, Rho for breaching—and I lead. Above ground, Elia and Vesper hold with Avyanna."
    jump act1_party_split_briefing_elia_precision_react

label act1_party_split_briefing_elia_precision_react:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "{i}A slow nod.{/i} You want to be on the line. I respect that. Vesper and I will make sure nobody comes through that perimeter."
    jump act1_party_split_briefing_gear_check_intro

label act1_party_split_briefing_elia_default_split:
    $ game_state.set_flag("assault_team_close_quarters")
    elia "My recommendation: Nyx, Elisira, and Jalen on infiltration with Avyanna. Myself, Rho, and Vesper on assault. It plays to everyone's strengths."
    jump act1_party_split_briefing_gear_check_intro

label act1_party_split_briefing_gear_check_intro:
    elia "Gear check. Every piece of equipment, every charge, every med-kit—verified and verified again. Assault team, what's your loadout?"
    jump act1_party_split_briefing_gear_assault_check

label act1_party_split_briefing_gear_assault_check:
    "{i}Equipment spreads across the table. Ammunition counts, explosive charges, suppression grenades, emergency beacons. The smell of gun oil and ozone fills the room.{/i}"
    jump act1_party_split_briefing_rho_gear

label act1_party_split_briefing_rho_gear:
    rho "Rotary cannon—full drum, two spares. Six shaped charges, four concussion grenades. Armor's been patched and sealed. {i}Patting his chest plate.{/i} She'll hold."
    jump act1_party_split_briefing_vesper_gear

label act1_party_split_briefing_vesper_gear:
    if game_state.has_flag("vesper_trust_high"):
        vesper "{i}Quieter.{/i} And a second medkit. In case someone else needs it more than I do."
    elif game_state.has_flag("vesper_trust_low"):
        vesper "And a second sidearm. Redundancy."
    else:
        vesper "Clarity and Witness—both zeroed at range. Two hundred rounds standard, forty armor-piercing. Ghillie mesh for the overwatch position. Emergency sidearm."
    jump act1_party_split_briefing_elia_gear

label act1_party_split_briefing_elia_gear:
    elia "{i}Drawing one blade, inspecting the edge.{/i} Twin blades. Sharpened this morning. Four flash charges for corridor work. Light armor—I need mobility more than plating."
    jump act1_party_split_briefing_gear_infiltration_check

label act1_party_split_briefing_gear_infiltration_check:
    elia "Infiltration team. Loadout."
    jump act1_party_split_briefing_nyx_gear

label act1_party_split_briefing_nyx_gear:
    nyx "Threshold staff—fully charged. Ward disruption kit: three resonance dampeners, two null-anchors, one emergency collapse sigil. {i}She hesitates.{/i} And the shard fragment, in case I need to improvise."
    jump act1_party_split_briefing_elisira_gear

label act1_party_split_briefing_elisira_gear:
    elisira "Dual pistols, suppressed. Sixty rounds subsonic, twenty standard. Lockpick set—both mechanical and electronic. Facility map loaded to three separate devices in case we lose one."
    jump act1_party_split_briefing_jalen_gear

label act1_party_split_briefing_jalen_gear:
    jalen "Mobile tech rig. Signal jammer, spoofing suite, three bypass modules. {i}Holding up a small device.{/i} And this—a localized EMP. One shot. Kills everything electronic in a twenty-meter radius, including my own gear. Absolute last resort."
    jump act1_party_split_briefing_bee_gear_analysis

label act1_party_split_briefing_bee_gear_analysis:
    bee "{{BEE:: LOADOUT_ASSESSMENT: all teams within operational parameters | STATUS: ammunition reserves at 94%% optimal | DETAIL: recommend infiltration team carry additional null-anchors—subsurface ward density exceeds initial projections by factor of 1.4}}"
    jump act1_party_split_briefing_nyx_extra_anchors

label act1_party_split_briefing_nyx_extra_anchors:
    nyx "{i}Pulling two more null-anchors from the supply locker.{/i} BEE's right. Better to have them and not need them. {i}Tucking them into her belt.{/i} That's five total. Should be enough. Has to be enough."
    jump act1_party_split_briefing_personal_moments_intro

label act1_party_split_briefing_personal_moments_intro:
    "{i}The briefing winds down. Equipment checked, plans locked, contingencies mapped. A strange quiet settles—the kind that lives between the last order and the first step into danger. People drift into pairs. Small conversations. The words that matter.{/i}"
    jump act1_party_split_briefing_vesper_rho_moment

label act1_party_split_briefing_vesper_rho_moment:
    "{i}Vesper and Rho stand apart by the weapons rack. They don't look at each other. They don't need to.{/i}"
    jump act1_party_split_briefing_rho_to_vesper

label act1_party_split_briefing_rho_to_vesper:
    rho "{i}Low, only for her.{/i} If the line breaks—"
    jump act1_party_split_briefing_vesper_to_rho

label act1_party_split_briefing_vesper_to_rho:
    vesper "{i}Cutting him off.{/i} It won't."
    jump act1_party_split_briefing_rho_vesper_silence

label act1_party_split_briefing_rho_vesper_silence:
    "{i}A pause. Rho nods. Something passes between them that words would only diminish.{/i}"
    jump act1_party_split_briefing_jalen_nyx_moment

label act1_party_split_briefing_jalen_nyx_moment:
    jalen "{i}Sliding a small device across the table to Nyx.{/i} Here. Emergency comms relay. If everything else goes dark, this runs on ward energy. Your staff should keep it powered."
    jump act1_party_split_briefing_nyx_accepts_device

label act1_party_split_briefing_nyx_accepts_device:
    nyx "{i}Turning it over in her fingers.{/i} You built this? When?"
    jump act1_party_split_briefing_jalen_shrugs

label act1_party_split_briefing_jalen_shrugs:
    jalen "{i}Shrugging.{/i} Couldn't sleep. Figured one of us should make something useful out of insomnia."
    jump act1_party_split_briefing_elisira_elia_moment

label act1_party_split_briefing_elisira_elia_moment:
    "{i}Elisira and Elia stand over the holo-table, the facility map still rotating between them. Their reflections ghost across the blue light.{/i}"
    jump act1_party_split_briefing_elisira_to_elia

label act1_party_split_briefing_elisira_to_elia:
    elisira "{i}Quietly.{/i} This is the one, isn't it. The mission we don't come back from unchanged."
    jump act1_party_split_briefing_elia_to_elisira

label act1_party_split_briefing_elia_to_elisira:
    elia "{i}A breath.{/i} We come back. All of us. That's the only version of this I'm willing to plan for."
    jump act1_party_split_briefing_player_personal_moment

label act1_party_split_briefing_player_personal_moment:
    "{i}The quiet stretches. Someone is going to find you before you find them.{/i}"
    menu:
        "Find a quiet corner alone. Collect your thoughts.":
            jump act1_party_split_briefing_avyanna_alone
        "Check on the crew. Make sure everyone's okay.":
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_party_split_briefing_avyanna_checks_crew
        "Study the facility map one more time.":
            jump act1_party_split_briefing_avyanna_studies_map

label act1_party_split_briefing_avyanna_alone:
    "{i}You find a corner near the viewport. Stars drift past—indifferent to what's about to happen. Your shard pulses once against your chest. Warm. Almost like a heartbeat.{/i}"
    jump act1_party_split_briefing_elia_finds_you

label act1_party_split_briefing_avyanna_checks_crew:
    "{i}You make the rounds. A nod to Rho. A touch on Jalen's shoulder. A look that says everything to Nyx. The crew notices. They always notice.{/i}"
    jump act1_party_split_briefing_elia_finds_you

label act1_party_split_briefing_avyanna_studies_map:
    $ game_state.set_flag("briefing_map_studied")
    "{i}The facility turns slowly in blue light. You memorize corridors, chokepoints, ward junctions. If something goes wrong, you want to know every path by heart.{/i}"
    jump act1_party_split_briefing_elia_finds_you

label act1_party_split_briefing_elia_finds_you:
    if game_state.has_flag("elia_trust_high"):
        elia "{i}Her hand finds your shoulder. Brief. Warm. The grip of someone who means it.{/i} Whatever happens in there—you've already proven you belong on this crew. Don't forget that."
    elif game_state.has_flag("elia_trust_low"):
        elia "{i}Arms folded. Professional distance. But she came to find you, and that says something.{/i} Stay sharp. Follow the plan. We'll get through this."
    else:
        elia "{i}Appearing beside you. She moves like smoke when she wants to.{/i} You ready?"
    jump act1_party_split_briefing_player_responds_elia

label act1_party_split_briefing_player_responds_elia:
    menu:
        "Ready. Floor holds.":
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_party_split_briefing_elia_final_check
        "I'm terrified. But I trust this crew.":
            $ relationship_manager.process_reputation_affinity("elia", 2)
            jump act1_party_split_briefing_elia_honesty_response
        "Let's bring them hell.":
            jump act1_party_split_briefing_elia_final_check

label act1_party_split_briefing_elia_honesty_response:
    elia "{i}Something softens in her expression. Just for a moment.{/i} Good. Terrified means you understand the stakes. And trust... trust is the only thing that's going to get us through those walls."
    jump act1_party_split_briefing_elia_final_check

label act1_party_split_briefing_elia_final_check:
    elia "Final positions. Assault team, sound off."
    jump act1_party_split_briefing_assault_sound_off_start

label act1_party_split_briefing_assault_sound_off_start:
    "{i}The assault team responds based on earlier choices. Each member acknowledges their role with practiced brevity.{/i}"
    if game_state.has_flag("assault_team_close_quarters"):
        jump act1_party_split_briefing_assault_cq_sound_off
    elif game_state.has_flag("assault_team_mixed_range"):
        jump act1_party_split_briefing_assault_mixed_sound_off
    elif game_state.has_flag("assault_team_tactical_precision"):
        jump act1_party_split_briefing_assault_precision_sound_off
    else:
        jump act1_party_split_briefing_assault_cq_sound_off

label act1_party_split_briefing_assault_cq_sound_off:
    rho "Breach and suppress. Rotary cannon loaded, charges prepped. Ready."
    jump act1_party_split_briefing_assault_cq_elia

label act1_party_split_briefing_assault_cq_elia:
    elia "Corridor clearing. Close-quarters dominance. Blades sharp. Ready."
    jump act1_party_split_briefing_assault_cq_elisira

label act1_party_split_briefing_assault_cq_elisira:
    elisira "Precision eliminations. Dual pistols, suppressed. Ready."
    jump act1_party_split_briefing_assault_cq_nyx

label act1_party_split_briefing_assault_cq_nyx:
    nyx "Ward disruption. Threshold staff active. Ready to light them up."
    jump act1_party_split_briefing_hold_team_sound_off

label act1_party_split_briefing_assault_mixed_sound_off:
    elia "Close-quarters anchor. I'll clear the path. Ready."
    jump act1_party_split_briefing_assault_mixed_vesper

label act1_party_split_briefing_assault_mixed_vesper:
    vesper "Precision fire. Counter-sniper. Clarity and Witness loaded. Ready."
    jump act1_party_split_briefing_assault_mixed_nyx

label act1_party_split_briefing_assault_mixed_nyx:
    nyx "Ward disruption and locality adjustments. Ready to bend their doors."
    jump act1_party_split_briefing_assault_mixed_avyanna

label act1_party_split_briefing_assault_mixed_avyanna:
    avyanna "{i}Voice steadier than she feels.{/i} Lattice tracking. I'll map their wards. Ready."
    jump act1_party_split_briefing_hold_team_sound_off

label act1_party_split_briefing_assault_precision_sound_off:
    elisira "Surgical strike lead. Dual pistols. Precision only. Ready."
    jump act1_party_split_briefing_assault_precision_rho

label act1_party_split_briefing_assault_precision_rho:
    rho "Clean breaches. Shaped charges, minimal collateral. Ready."
    jump act1_party_split_briefing_assault_precision_nyx

label act1_party_split_briefing_assault_precision_nyx:
    nyx "Ward disruption without signature flare. Stealth variant protocols. Ready."
    jump act1_party_split_briefing_assault_precision_jalen

label act1_party_split_briefing_assault_precision_jalen:
    jalen "Real-time route optimization. Mapping exits as we go. Ready."
    jump act1_party_split_briefing_hold_team_sound_off

label act1_party_split_briefing_hold_team_sound_off:
    elia "Hold team, sound off."
    jump act1_party_split_briefing_hold_sound_off_start

label act1_party_split_briefing_hold_sound_off_start:
    "{i}The hold team responds. Positions locked. Roles clear.{/i}"
    if game_state.has_flag("assault_team_close_quarters"):
        jump act1_party_split_briefing_hold_cq_sound_off
    elif game_state.has_flag("assault_team_mixed_range"):
        jump act1_party_split_briefing_hold_mixed_sound_off
    elif game_state.has_flag("assault_team_tactical_precision"):
        jump act1_party_split_briefing_hold_precision_sound_off
    else:
        jump act1_party_split_briefing_hold_cq_sound_off

label act1_party_split_briefing_hold_cq_sound_off:
    vesper "Overwatch. Counter-sniper. Long-range dominance. Ready."
    jump act1_party_split_briefing_hold_cq_jalen

label act1_party_split_briefing_hold_cq_jalen:
    jalen "Extraction pilot. Ship prepped, engines hot. Ready to fly the exit."
    jump act1_party_split_briefing_hold_cq_avyanna

label act1_party_split_briefing_hold_cq_avyanna:
    avyanna "{i}Hands steady on her comms tablet.{/i} Coordination. Hostile tracking. Comms relay. Ready."
    jump act1_party_split_briefing_final_acknowledgments

label act1_party_split_briefing_hold_mixed_sound_off:
    elisira "Perimeter defense. Counter-assault protocols. Ready."
    jump act1_party_split_briefing_hold_mixed_rho

label act1_party_split_briefing_hold_mixed_rho:
    rho "Long-range breach support. Shaped charges on standby. Ready."
    jump act1_party_split_briefing_hold_mixed_jalen

label act1_party_split_briefing_hold_mixed_jalen:
    jalen "Timing coordination. Extraction ready. Ready to pull you out."
    jump act1_party_split_briefing_final_acknowledgments

label act1_party_split_briefing_hold_precision_sound_off:
    elia "Extraction defense. Close-quarters fallback. Ready."
    jump act1_party_split_briefing_hold_precision_vesper

label act1_party_split_briefing_hold_precision_vesper:
    vesper "Long-range dominance. No one gets close. Ready."
    jump act1_party_split_briefing_hold_precision_avyanna

label act1_party_split_briefing_hold_precision_avyanna:
    avyanna "{i}Gripping her tablet.{/i} Coordination. Hostile tracking. I'll keep you all connected. Ready."
    jump act1_party_split_briefing_final_acknowledgments

label act1_party_split_briefing_final_acknowledgments:
    elia "{i}Looking at each person.{/i} Roles are clear. Timing is tight. If anything goes wrong, we adapt—but we don't leave anyone behind."
    jump act1_party_split_briefing_waffle_briefing_status

label act1_party_split_briefing_waffle_briefing_status:
    waffle "{i}}{{WAFFLE.BAT// TACTICAL_SUMMARY: all teams assigned | COMMS_STATUS: encrypted channels active | NOTE: I will be monitoring all channels. You are not alone in there.}}{/i}}"
    jump act1_party_split_briefing_bubbles_briefing_prep

label act1_party_split_briefing_bubbles_briefing_prep:
    bubbles "{i}Through speakers:{/i} Medical kits staged at both insertion points. Emergency extraction protocols loaded. Be safe out there."
    jump act1_party_split_briefing_cinnamon_briefing_ready

label act1_party_split_briefing_cinnamon_briefing_ready:
    cinnamon "Ship systems locked for combat ops. Drill bay sealed. All non-essential subsystems powered down. Ready."
    jump act1_party_split_briefing_vesper_addition

label act1_party_split_briefing_vesper_addition:
    vesper "Extraction window is six hours. We hit hard, we hit fast, we get out. No heroics. No unnecessary risks."
    jump act1_party_split_briefing_rho_grin

label act1_party_split_briefing_rho_grin:
    rho "{i}Grinning, but his eyes are serious.{/i} And if they try to stop us, we remind them why the Lumen Thief has a reputation."
    jump act1_party_split_briefing_elisira_final

label act1_party_split_briefing_elisira_final:
    elisira "{i}Single syllable, weight of command.{/i} Together."
    jump act1_party_split_briefing_elia_floor_holds_call

label act1_party_split_briefing_elia_floor_holds_call:
    elia "{i}Voice steady, ritual weight.{/i} Floor holds."
    jump act1_party_split_briefing_crew_floor_holds_response

label act1_party_split_briefing_crew_floor_holds_response:
    "{i}The response is immediate. Overlapping. Muscle memory. No one asked permission. No one gave orders. The pattern just happened.{/i}"
    jump act1_party_split_briefing_all_voices

label act1_party_split_briefing_all_voices:
    all_crew "{b}Floor holds.{/b}"
    jump act1_party_split_briefing_moment_of_silence

label act1_party_split_briefing_moment_of_silence:
    "{i}Silence. Not fear. Solidarity. Every person here chose this. Every person here knows what's at stake.{/i}"
    jump act1_party_split_briefing_elia_move_out

label act1_party_split_briefing_elia_move_out:
    elia "{i}Strapping her blades.{/i} Move out in ten. Let's bring them hell."
    jump act1_party_split_briefing_end_scene

label act1_party_split_briefing_end_scene:
    "{i}The crew disperses to final preparations. The weight of the moment hangs in the air. This is it. The climax. The fight that changes everything.{/i}"
    menu:
        "[Continue]":
            $ game_state.set_flag("act1_team_briefing_complete")
            return
