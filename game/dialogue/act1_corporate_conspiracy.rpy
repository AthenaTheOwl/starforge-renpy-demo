## act1_corporate_conspiracy.rpy — Auto-generated from act1_corporate_conspiracy.json
## 35 dialogue nodes

label act1_corporate_conspiracy:
    $ game_state.mark_dialogue_played("act1_corporate_conspiracy")
    jump act1_corporate_conspiracy_start

label act1_corporate_conspiracy_start:
    "{i}Jalen's workshop. Datapads scattered across the table, glowing with corporate feeds, manifests, financial trails. He looks up when you enter. His expression is wrong—not fear, but something worse. Certainty.{/i}"
    jump act1_corporate_conspiracy_jalen_greeting

label act1_corporate_conspiracy_jalen_greeting:
    jalen "Avyanna. Good. You should hear this. {i}[He gestures to a chair.]{/i} Sit down."
    jump act1_corporate_conspiracy_avyanna_concern

label act1_corporate_conspiracy_avyanna_concern:
    avyanna "What's wrong?"
    jump act1_corporate_conspiracy_jalen_reveal_start

label act1_corporate_conspiracy_jalen_reveal_start:
    jalen "I've been tracking corporate filings. Cross-referencing Aurum Extraction's debt recovery claims with Compact medical research permits. {i}[He turns a datapad toward you.]{/i} Look at this."
    jump act1_corporate_conspiracy_data_display

label act1_corporate_conspiracy_data_display:
    "{i}The screen shows a web of connections: Aurum Extraction, three medical research fronts, a Debtor shell corporation, and—buried at the center—a single word. {b}Primordial.{/b}{/i}"
    jump act1_corporate_conspiracy_jalen_explanation_1

label act1_corporate_conspiracy_jalen_explanation_1:
    jalen "Aurum wasn't mining aurum at Site K-9. They were excavating {b}Primordial relics{/b}. The ore was cover. The real operation was Lattice extraction."
    jump act1_corporate_conspiracy_jalen_explanation_2

label act1_corporate_conspiracy_jalen_explanation_2:
    jalen "They found something down there. Something old. Pre-Synthetic. And when you touched it—{i}[He looks at you.]{/i}—you became their primary asset."
    jump act1_corporate_conspiracy_avyanna_processing

label act1_corporate_conspiracy_avyanna_processing:
    avyanna "{i}Voice thin.{/i} They knew. They knew what it was."
    jump act1_corporate_conspiracy_jalen_confirmation

label act1_corporate_conspiracy_jalen_confirmation:
    jalen "They knew. And they let you touch it anyway. {i}[He swipes to another file.]{/i} Here—medical recovery permits filed three days after we extracted you. {b}'Debt recovery and asset reclamation.'{/b}"
    jump act1_corporate_conspiracy_conspiracy_depth

label act1_corporate_conspiracy_conspiracy_depth:
    jalen "It gets worse. The Debtor shell corporation owns a majority stake in Aurum. They're not just extracting ore—they're extracting {b}Primordial fragments to study resistance to the Synthetic overlay{/b}."
    jump act1_corporate_conspiracy_conspiracy_target

label act1_corporate_conspiracy_conspiracy_target:
    jalen "You're not just a debt. You're a {b}research target{/b}. They want the shard. They want to know how it bonded. They want to replicate it."
    jump act1_corporate_conspiracy_elia_arrives

label act1_corporate_conspiracy_elia_arrives:
    "{i}The workshop door slides open. Elia steps in, a datapad clutched in one hand. She's read something — her jaw is tight, eyes sharp with a cold fury you haven't seen before.{/i}"
    jump act1_corporate_conspiracy_elia_reaction_01

label act1_corporate_conspiracy_elia_reaction_01:
    elia "Jalen sent me a copy. {i}[She sets the datapad down, carefully, like she's afraid she'll break it if she doesn't.]{/i} I've seen corporate ugliness before. Wage theft, forced labor, AI exploitation. But this..."
    jump act1_corporate_conspiracy_elia_reaction_02

label act1_corporate_conspiracy_elia_reaction_02:
    elia "They {i}engineered{/i} the exposure. The safety protocols at K-9 were deliberately downgraded three weeks before your shift rotation. Jalen found the maintenance order — signed by someone in Aurum's 'research division.' They {i}wanted{/i} someone to touch it."
    jump act1_corporate_conspiracy_elia_reaction_03

label act1_corporate_conspiracy_elia_reaction_03:
    elia "{i}Her voice drops, hard and quiet.{/i} You weren't an accident, Avyanna. You were an experiment. And they didn't even have the decency to tell you."
    jump act1_corporate_conspiracy_new_evidence_discovery

label act1_corporate_conspiracy_new_evidence_discovery:
    jalen "{i}[He pulls up one more file — this one encrypted, recently cracked.]{/i} There's something else. I found a shipping manifest routed through a Compact waystation. Aurum was moving sealed crates labeled 'geological samples' to a black-site facility in the Reach Terminus sector."
    jump act1_corporate_conspiracy_new_evidence_02

label act1_corporate_conspiracy_new_evidence_02:
    jalen "The crate weights don't match geological samples. They match {b}cryogenic containment units{/b}. Someone — or some {i}thing{/i} — was being transported alongside those relics. And the manifests were filed under your employee ID, Avyanna. Backdated."
    jump act1_corporate_conspiracy_new_evidence_03

label act1_corporate_conspiracy_new_evidence_03:
    avyanna "{i}A cold knot in the stomach.{/i} They used my credentials. To cover their tracks. If anyone investigates, {i}I'm{/i} the one who signed for illegal cargo."
    jump act1_corporate_conspiracy_bee_analysis

label act1_corporate_conspiracy_bee_analysis:
    "{{BEE:: Corporate data cross-reference complete | STATUS: Pattern confirmed | DETAIL: Aurum Extraction, Debtor Holdings, and Compact Medical Research Division 7 share 14 board members. Shell corporation nesting depth: 6 layers. Financial trail terminates at a classified Consortium defense account. This is not corporate greed — this is state-sponsored weapons research using Primordial artifacts as substrate.}}"
    jump act1_corporate_conspiracy_jalen_bee_react

label act1_corporate_conspiracy_jalen_bee_react:
    jalen "{i}[Reading the BEE output, his face goes pale.]{/i} Consortium defense. This goes higher than corporate. This is {i}government{/i}."
    jump act1_corporate_conspiracy_player_choice

label act1_corporate_conspiracy_player_choice:
    "{i}The weight of it settles. You're not free. You're fugitive property carrying contraband. The choice is how you respond.{/i}"
    menu:
        "[Caution] We hide. Stay off grids. Don't give them a target.":
            $ game_state.set_flag("conspiracy_revealed")
            $ game_state.set_flag("rep_corporate_heat", game_state.get_flag("rep_corporate_heat", 0) + 0)
            jump act1_corporate_conspiracy_caution_response
        "[Aggression] We hit them first. Expose this publicly.":
            $ game_state.set_flag("conspiracy_revealed")
            $ game_state.set_flag("rep_corporate_heat", game_state.get_flag("rep_corporate_heat", 0) + 2)
            jump act1_corporate_conspiracy_aggression_response
        "[Investigation] We need more data. Find their weak points.":
            $ game_state.set_flag("conspiracy_revealed")
            $ game_state.set_flag("rep_corporate_heat", game_state.get_flag("rep_corporate_heat", 0) + 1)
            jump act1_corporate_conspiracy_investigation_response
        "[Defiance] They made me into a weapon. Fine. Let them regret it.":
            $ game_state.set_flag("conspiracy_revealed")
            $ game_state.set_flag("rep_corporate_heat", game_state.get_flag("rep_corporate_heat", 0) + 1)
            jump act1_corporate_conspiracy_defiance_response

label act1_corporate_conspiracy_caution_response:
    jalen "{i}Nodding slowly.{/i} Smart. We stay mobile. Minimal station time. No Compact medical scans. I can scrub our trails—make us harder to track."
    jump act1_corporate_conspiracy_caution_vesper

label act1_corporate_conspiracy_caution_vesper:
    vesper "{i}From the doorway—when did she arrive?{/i} Caution buys time. Time lets us prepare. I'll vet contracts more carefully—no clients with corporate ties."
    jump act1_corporate_conspiracy_caution_outcome

label act1_corporate_conspiracy_caution_outcome:
    jalen "It's not a permanent solution. But it's survivable. {i}[He looks at you.]{/i} You okay with being a ghost?"
    return

label act1_corporate_conspiracy_aggression_response:
    jalen "{i}Eyebrows raised.{/i} Bold. And risky. If we go public, they'll accelerate extraction. Legal enforcement, bounty hunters—everything."
    jump act1_corporate_conspiracy_aggression_vesper

label act1_corporate_conspiracy_aggression_vesper:
    vesper "{i}Stepping into the room.{/i} But public exposure limits their options. They can't quietly disappear you if the galaxy is watching. {i}[Beat.]{/i} We'd need ironclad evidence. And a platform they can't suppress."
    jump act1_corporate_conspiracy_aggression_jalen

label act1_corporate_conspiracy_aggression_jalen:
    jalen "I can build the case. Manifests, permits, financial trails. But once we file, there's no taking it back. {i}[He looks at you.]{/i} You'd be painting a target on your back."
    jump act1_corporate_conspiracy_aggression_choice

label act1_corporate_conspiracy_aggression_choice:
    avyanna "{i}Jaw set.{/i} I've been a target since I touched that shard. At least this way, I'm fighting back."
    return

label act1_corporate_conspiracy_investigation_response:
    jalen "{i}A grim smile.{/i} My preferred approach. We need more than suspicion—we need proof. Names, dates, contracts. Everything that makes this stick."
    jump act1_corporate_conspiracy_investigation_vesper

label act1_corporate_conspiracy_investigation_vesper:
    vesper "{i}Joining the table.{/i} Investigation takes time. And resources. But it gives us leverage—something to negotiate with if they come for us."
    jump act1_corporate_conspiracy_investigation_plan

label act1_corporate_conspiracy_investigation_plan:
    jalen "I'll keep digging. Financial networks, shell corporations, research permits. We find the weak points—the places where exposure would cost them more than extraction."
    jump act1_corporate_conspiracy_investigation_vesper_addition

label act1_corporate_conspiracy_investigation_vesper_addition:
    vesper "And I'll start building exit strategies. Safe houses, alternate identities, extraction routes. If this goes wrong, we need options. {i}[She looks at you.]{/i} You're not going back."
    return

label act1_corporate_conspiracy_defiance_response:
    avyanna "{i}Something shifts in her posture. Not anger — resolve. The kind forged in the same furnace as the shard in her chest.{/i} They made me into a weapon. They spent resources, manipulated safety protocols, ruined my life to create... this. Fine."
    jump act1_corporate_conspiracy_defiance_elia

label act1_corporate_conspiracy_defiance_elia:
    elia "{i}A sharp look — measuring, then approving.{/i} That's not recklessness talking. That's someone who's done being afraid."
    jump act1_corporate_conspiracy_defiance_jalen

label act1_corporate_conspiracy_defiance_jalen:
    $ game_state.set_flag("chose_defiance")
    $ relationship_manager.process_reputation_affinity("elia", 1)
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "{i}Quietly.{/i} Defiance without strategy is just noise. But defiance {i}with{/i} strategy... that's revolution. {i}[He leans forward.]{/i} Tell me what you need. I'll make it happen."
    return
