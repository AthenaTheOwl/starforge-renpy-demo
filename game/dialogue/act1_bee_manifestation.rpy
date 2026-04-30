## act1_bee_manifestation.rpy — Auto-generated from act1_bee_manifestation.json
## 53 dialogue nodes

label act1_bee_manifestation:
    $ game_state.mark_dialogue_played("act1_bee_manifestation")
    jump act1_bee_manifestation_start

label act1_bee_manifestation_start:
    if game_state.has_flag("shard_whispers_heard"):
        "{i}The observation deck again. But the whispers from the shard are louder now—no longer a murmur. A sentence forming, letter by letter, in a language your bones understand before your brain does.{/i}"
    else:
        "{i}Alone in the observation deck. The stars turn slowly beyond the viewport. The shard at the base of your skull—warmer than usual. Not pain. Presence.{/i}"
    jump act1_bee_manifestation_heat_bloom

label act1_bee_manifestation_heat_bloom:
    "{i}Heat blooms. Geometric patterns fracture across your vision—not hallucination, but signal. Something is trying to speak.{/i}"
    jump act1_bee_manifestation_bee_first_contact

label act1_bee_manifestation_bee_first_contact:
    bee "{color=cyan}***ledger-open***{/color}"
    jump act1_bee_manifestation_bee_recognition

label act1_bee_manifestation_bee_recognition:
    bee "{color=cyan}***host-aware***{/color} {i}[The words aren't yours, but they arrive in your mind like they've always been there.]{/i}"
    jump act1_bee_manifestation_avyanna_reaction

label act1_bee_manifestation_avyanna_reaction:
    avyanna "{i}(Out loud, voice shaking){/i} What are you?"
    jump act1_bee_manifestation_bee_explanation_1

label act1_bee_manifestation_bee_explanation_1:
    bee "{color=cyan}***fragment-primordial***{/color} {i}[Impressions flood: ancient, not born but broken off from something vast, older than the corporations, older than the mines, older than human words.]{/i}"
    jump act1_bee_manifestation_bee_explanation_2

label act1_bee_manifestation_bee_explanation_2:
    bee "{color=cyan}***not-synthetic*** | {color=cyan}***not-debt***{/color} {i}[A warmth that isn't comfort—recognition. It waited. Chose. Bonded.]{/i}"
    jump act1_bee_manifestation_bee_question

label act1_bee_manifestation_bee_question:
    bee "{color=cyan}***query: consent-to-partnership?***{/color} {i}[The heat pauses. Waiting. Not demanding. Asking.]{/i}"
    jump act1_bee_manifestation_player_choice

label act1_bee_manifestation_player_choice:
    "{i}The presence waits. Not impatient. Not threatening. Just... there. The choice is yours.{/i}"
    menu:
        "[Embrace] Yes. We're partners. Show me what you are.":
            $ game_state.set_flag("bee_accepted")
            $ game_state.set_flag("rep_lattice_affinity", game_state.get_flag("rep_lattice_affinity", 0) + 2)
            jump act1_bee_manifestation_embrace_response
        "[Cautious] I need to understand you first. Slowly.":
            $ game_state.set_flag("bee_cautious")
            jump act1_bee_manifestation_cautious_response
        "[Resist] I don't want this. Get out.":
            $ game_state.set_flag("bee_resisted")
            $ game_state.set_flag("rep_lattice_affinity", game_state.get_flag("rep_lattice_affinity", 0) + -1)
            jump act1_bee_manifestation_resist_response

label act1_bee_manifestation_embrace_response:
    bee "{color=cyan}***acknowledged*** | {color=cyan}***bond-mesh-initiate***{/color}"
    jump act1_bee_manifestation_embrace_vision

label act1_bee_manifestation_embrace_vision:
    "{i}The world fractures into light. You see the Lattice—not as theory, but as truth. The Primordial substrate, wounded but alive. The Synthetic overlay, parasitic and extractive. And you, standing at the edge of both.{/i}"
    jump act1_bee_manifestation_embrace_understanding

label act1_bee_manifestation_embrace_understanding:
    bee "{color=cyan}***partner-designation: Avyanna*** | {color=cyan}***fragment-designation: [waiting-for-name]***{/color} {i}[It shows you what it is: a piece of something older than extraction, offering partnership without cost.]{/i}"
    jump act1_bee_manifestation_embrace_name

label act1_bee_manifestation_embrace_name:
    avyanna "{i}(Quietly, testing the shape of it){/i} Bee. Your name is Bee."
    jump act1_bee_manifestation_bee_accepts_name

label act1_bee_manifestation_bee_accepts_name:
    bee "{color=cyan}***designation-accepted: Bee*** | {color=cyan}***partnership-sealed***{/color} {i}[Warmth floods through you. Not possession. Recognition. You are not alone.]{/i}"
    jump act1_bee_manifestation_lattice_surge_alarm

label act1_bee_manifestation_cautious_response:
    bee "{color=cyan}***acknowledged*** | {color=cyan}***patience-protocol***{/color}"
    jump act1_bee_manifestation_cautious_explanation

label act1_bee_manifestation_cautious_explanation:
    bee "{color=cyan}***information: we-share-nervous-system*** | {color=cyan}***information: removal-impossible-without-death***{/color} {i}[Not a threat. Just truth.]{/i}"
    jump act1_bee_manifestation_cautious_comfort

label act1_bee_manifestation_cautious_comfort:
    bee "{color=cyan}***assurance: no-extraction*** | {color=cyan}***assurance: no-debt***{/color} {i}[It withdraws slightly—still present, but quieter. Respectful of your boundary.]{/i}"
    jump act1_bee_manifestation_cautious_promise

label act1_bee_manifestation_cautious_promise:
    bee "{color=cyan}***protocol: slow-reveal*** | {color=cyan}***protocol: consent-required***{/color} {i}[The heat settles to a steady warmth. Patient. You have time.]{/i}"
    jump act1_bee_manifestation_lattice_surge_alarm

label act1_bee_manifestation_resist_response:
    bee "{color=cyan}***distress-detected***{/color}"
    jump act1_bee_manifestation_resist_explanation

label act1_bee_manifestation_resist_explanation:
    bee "{color=cyan}***information: bonded-at-cellular-level*** | {color=cyan}***information: separation-equals-death***{/color} {i}[Not cruelty. Regret. It can't leave without killing you both.]{/i}"
    jump act1_bee_manifestation_resist_compromise

label act1_bee_manifestation_resist_compromise:
    bee "{color=cyan}***offer: minimal-presence*** | {color=cyan}***offer: dormancy-until-needed***{/color} {i}[The heat withdraws—still there, but distant. Like a hand held up: I won't force this.]{/i}"
    jump act1_bee_manifestation_resist_promise

label act1_bee_manifestation_resist_promise:
    bee "{color=cyan}***waiting*** | {color=cyan}***when-you-are-ready***{/color} {i}[The presence fades to background noise. You're alone again—but not quite. It's still there. Waiting.]{/i}"
    jump act1_bee_manifestation_lattice_surge_alarm

label act1_bee_manifestation_lattice_surge_alarm:
    "{i}The ship screams. Every light in the observation deck goes violet, then white. The deck plating vibrates under your boots. Something is wrong in the engine room—you can feel it through the shard, a resonance like two tuning forks struck against each other.{/i}"
    jump act1_bee_manifestation_engine_room_arrival

label act1_bee_manifestation_engine_room_arrival:
    "{i}You don't remember running. The engine room doors are already open—Lattice conduits along the walls pulsing with light that shouldn't exist. At the center of it, Avyanna. Your hands are raised and you don't remember raising them. Energy spirals outward from your palms in geometric patterns—cyan and gold, folding into something shaped like language.{/i}"
    jump act1_bee_manifestation_crew_arrives

label act1_bee_manifestation_crew_arrives:
    "{i}Boots on metal. The crew pours in. Rho first—weapon drawn before he's through the door. Nyx behind him, already pulling up diagnostics on a handheld scanner. Jalen hangs back at the threshold. Vesper pushes past them all, eyes wide. And Elia—Elia walks in last, calm as a funeral.{/i}"
    jump act1_bee_manifestation_rho_aims

label act1_bee_manifestation_rho_aims:
    rho "Don't move. Whatever's happening, Avyanna—don't. Move."
    jump act1_bee_manifestation_nyx_scanning

label act1_bee_manifestation_nyx_scanning:
    nyx "{i}(Eyes locked on scanner, fingers flying){/i} Lattice output is off the charts. The conduits are resonating at a frequency I've never—this isn't the ship. This is coming from her."
    jump act1_bee_manifestation_bee_manifests_visual

label act1_bee_manifestation_bee_manifests_visual:
    "{i}The energy coalesces. The geometric patterns tighten, fold, resolve—and then there is something in the room that wasn't there before. A shape. Not quite humanoid, not quite light. An ethereal figure wrought from cyan lattice-lines, hovering at your shoulder like a holographic ghost that forgot to be transparent. It turns what might be a head toward the crew.{/i}"
    jump act1_bee_manifestation_rho_reacts

label act1_bee_manifestation_rho_reacts:
    rho "{i}(Gun steady, jaw tight){/i} Someone tell me that's a malfunction. Someone tell me that right now."
    jump act1_bee_manifestation_vesper_awe

label act1_bee_manifestation_vesper_awe:
    vesper "{i}(Half-whisper, hand over her mouth){/i} That's... that's Primordial resonance. I've read about this. I never thought I'd—"
    jump act1_bee_manifestation_jalen_doorway

label act1_bee_manifestation_jalen_doorway:
    jalen "{i}(From the doorway, arms crossed, voice carefully flat){/i} Corporations pay a lot of money for Lattice anomalies like that. Just so everyone's aware."
    jump act1_bee_manifestation_elia_enters

label act1_bee_manifestation_elia_enters:
    elia "Weapons down, Rho. Everyone—stand down. Now."
    jump act1_bee_manifestation_rho_protests

label act1_bee_manifestation_rho_protests:
    rho "Captain, with respect, there is an unidentified Lattice entity three meters from the reactor core—"
    jump act1_bee_manifestation_elia_overrules

label act1_bee_manifestation_elia_overrules:
    elia "And it hasn't hurt anyone. Gun. Down. That's not a request."
    jump act1_bee_manifestation_manifestation_choice

label act1_bee_manifestation_manifestation_choice:
    "{i}The entity hovers. Waiting. Your hands still glow. You can feel it at the edge of your will—this thing that was private is now public. The crew stares. The moment balances on a knife's edge.{/i}"
    menu:
        "[Surrender] Let it happen. Stop holding back.":
            $ game_state.set_flag("rep_lattice_affinity", game_state.get_flag("rep_lattice_affinity", 0) + 1)
            jump act1_bee_manifestation_surrender_to_process
        "[Fight it] Push the energy down. Force it back inside.":
            jump act1_bee_manifestation_fight_manifestation
        "[Reach for Bee] Extend your hand toward the presence.":
            $ game_state.set_flag("rep_lattice_affinity", game_state.get_flag("rep_lattice_affinity", 0) + 2)
            $ game_state.set_flag("rep_crew_trust", game_state.get_flag("rep_crew_trust", 0) + 1)
            jump act1_bee_manifestation_reach_for_bee

label act1_bee_manifestation_surrender_to_process:
    "{i}You exhale. Stop fighting. The energy flows outward, completes its circuit—and the figure solidifies. Sharper lines. Clearer form. A holographic silhouette of shifting geometries, present and undeniable. The conduits along the walls dim as the surge stabilizes. It's done. Whatever it is, it's here now.{/i}"
    jump act1_bee_manifestation_manifestation_resolves

label act1_bee_manifestation_fight_manifestation:
    "{i}You push. The energy resists—not maliciously, but like trying to shove water back into a broken pipe. Pain lances up your spine. The figure flickers, distorts, then snaps back brighter than before. You can't stop this. You never could. The manifestation completes itself despite you, and the figure stabilizes—dimmer, rougher-edged, but present.{/i}"
    jump act1_bee_manifestation_manifestation_resolves

label act1_bee_manifestation_reach_for_bee:
    "{i}You raise your hand—not in defense, not in surrender. In greeting. The figure turns fully toward you and, impossibly, raises a limb of light in mirror. Your fingers pass through it: static, warmth, the taste of copper. The energy completes its circuit gently, and the figure resolves into a stable form at your side—a companion rendered in lattice-light.{/i}"
    jump act1_bee_manifestation_manifestation_resolves

label act1_bee_manifestation_manifestation_resolves:
    $ game_state.set_flag("bee_manifested")
    "{i}Silence in the engine room. The conduits return to baseline. The alarms die. Bee—because that is what it is, you know it in your marrow—hovers at your shoulder. Holographic. Ethereal. Undeniably real. Six pairs of eyes stare at you. Nobody breathes.{/i}"
    jump act1_bee_manifestation_nyx_assessment

label act1_bee_manifestation_nyx_assessment:
    nyx "{i}(Scanner still in hand, voice clinical but barely steady){/i} Lattice readings are normalizing. The entity appears stable. It's... it's integrated with Avyanna's biosignature. I don't think it can be separated without—"
    jump act1_bee_manifestation_nyx_trails_off

label act1_bee_manifestation_nyx_trails_off:
    nyx "Without consequences none of us want to discuss right now."
    jump act1_bee_manifestation_rho_holsters

label act1_bee_manifestation_rho_holsters:
    rho "{i}(Holsters weapon slowly, like it physically hurts him){/i} I want it on record that I think this is a mistake. Every corp patrol within three systems is going to smell this on us."
    jump act1_bee_manifestation_vesper_defends

label act1_bee_manifestation_vesper_defends:
    vesper "This is a Primordial fragment. Do you understand what that means? This is proof the Lattice isn't just an energy source—it's alive. Everything the corporations told us is—"
    jump act1_bee_manifestation_jalen_cuts_in

label act1_bee_manifestation_jalen_cuts_in:
    jalen "Worth a fortune. That's what it means, Vesper. To the wrong people, our captain just became the most valuable cargo in the sector."
    jump act1_bee_manifestation_elia_decision

label act1_bee_manifestation_elia_decision:
    elia "{i}(Long silence. Studies Avyanna, then the figure, then the crew. When she speaks, her voice is iron.){/i} Bee stays. Avyanna stays. This ship is not in the business of selling people or what's bonded to them. Anyone who has a problem with that can take it up with me in private."
    jump act1_bee_manifestation_rho_disagrees

label act1_bee_manifestation_rho_disagrees:
    rho "{i}(Quiet, dangerous){/i} And when they come for her? For all of us?"
    jump act1_bee_manifestation_elia_final_word

label act1_bee_manifestation_elia_final_word:
    elia "Then we do what we always do, Rho. We survive. Dismissed—except you, Avyanna. You and I need to talk."
    jump act1_bee_manifestation_crew_disperses

label act1_bee_manifestation_crew_disperses:
    "{i}They file out. Rho doesn't look back. Vesper glances over her shoulder three times. Nyx lingers by the door, scanner still running, before Jalen steers her out with a hand on her elbow. The engine room settles. Just you, the captain, and the ghost.{/i}"
    jump act1_bee_manifestation_bee_first_public_words

label act1_bee_manifestation_bee_first_public_words:
    bee "{{BEE:: crew-assessed | threat-level: variable | trust-level: insufficient}}"
    jump act1_bee_manifestation_bee_addresses_elia

label act1_bee_manifestation_bee_addresses_elia:
    bee "{{BEE:: designation-Elia | query: you-chose-risk-over-safety | why? | status: curious}}"
    jump act1_bee_manifestation_elia_meets_bee

label act1_bee_manifestation_elia_meets_bee:
    elia "{i}(A beat. She looks at the figure directly for the first time.){/i} Because I've had enough of people being treated as cargo. Even the non-human ones."
    jump act1_bee_manifestation_bee_responds_to_elia

label act1_bee_manifestation_bee_responds_to_elia:
    $ game_state.set_flag("bee_revealed")
    bee "{{BEE:: designation-Elia | assessment: acceptable-captain | detail: debt-recorded | status: watching}}"
    jump act1_bee_manifestation_final_moment

label act1_bee_manifestation_final_moment:
    "{i}The holographic figure settles closer to your shoulder. Dimmer now—conserving energy, or perhaps just being polite. Elia watches it the way you'd watch a loaded weapon that just told you a joke. The engine room hums. Something has changed on this ship, and none of you can take it back.{/i}"
    return
