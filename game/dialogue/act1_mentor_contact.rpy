## act1_mentor_contact.rpy — Auto-generated from act1_mentor_contact.json
## 34 dialogue nodes

label act1_mentor_contact:
    $ game_state.mark_dialogue_played("act1_mentor_contact")
    jump act1_mentor_contact_start

label act1_mentor_contact_start:
    "{i}The comms panel crackles. Not the usual hiss of empty channels—something else. A deliberate signal, encrypted, threading through frequencies the ship shouldn't be monitoring.{/i}"
    jump act1_mentor_contact_waffle_alert

label act1_mentor_contact_waffle_alert:
    waffle "Unknown transmission. Source: {b}redacted{/b}. Encryption: custom. Not Guild. Not Compact. Someone built this specifically to reach us."
    jump act1_mentor_contact_signal_incoming

label act1_mentor_contact_signal_incoming:
    "{i}Static blooms, then clears just enough to carry a voice—low, careful, masked beneath layers of noise.{/i}"
    jump act1_mentor_contact_mentor_greeting

label act1_mentor_contact_mentor_greeting:
    unknown "{i}[Static]{/i} —listening? Good. Don't respond yet. Just hear this: {b}the girl you rescued from Site K-9 is more valuable than you know.{/b}"
    jump act1_mentor_contact_mentor_warning

label act1_mentor_contact_mentor_warning:
    unknown "Corporate interest in Avyanna isn't coincidence. They know what she's carrying. They'll come for her. Not now—but soon. When they do, it won't be a raid. It'll be {b}legal extraction{/b}."
    jump act1_mentor_contact_elia_listens

label act1_mentor_contact_elia_listens:
    elia "{i}Jaw tight, hand near her blade.{/i} Who the hell is this?"
    jump act1_mentor_contact_mentor_deflect

label act1_mentor_contact_mentor_deflect:
    unknown "Someone who wants her to survive. Someone who's been watching the Kennel for fifteen years. {i}[Static surge]{/i} —doesn't matter who I am. What matters is {b}she's a target{/b}."
    jump act1_mentor_contact_mentor_reveal_shard

label act1_mentor_contact_mentor_reveal_shard:
    unknown "The shard in her spine? Pre-Synthetic. Primordial. The Debtors want it back. Aurum Extraction wants compensation. The Compact will call it {b}controlled substance trafficking{/b}."
    jump act1_mentor_contact_mentor_lattice_hint

label act1_mentor_contact_mentor_lattice_hint:
    unknown "But the shard isn't what makes her dangerous. It's what it woke up. {i}[Static crackle]{/i} Her resonance with the Lattice—that's why they took her in the first place. That's why {b}extraction{/b} wasn't random."
    jump act1_mentor_contact_bee_agitation_early

label act1_mentor_contact_bee_agitation_early:
    "{{BEE:: lattice resonance referenced — unknown source | ELEVATED | pattern matches restricted K-9 documentation}}"
    jump act1_mentor_contact_mentor_preextraction

label act1_mentor_contact_mentor_preextraction:
    unknown "Before they pulled her out of wherever she was born, she was {b}flagged{/b}. A Lattice-sensitive child, manifesting at age three. The Debtors bid on her like cattle at market. Aurum won."
    jump act1_mentor_contact_mentor_targeted

label act1_mentor_contact_mentor_targeted:
    unknown "She wasn't rescued from K-9, not really. She was {b}moved{/b}. From one cage to a smaller one. The shard was their leash. And now that she's loose— {i}[static hiss]{/i} —they want their investment back."
    jump act1_mentor_contact_player_choice

label act1_mentor_contact_player_choice:
    "{i}The voice waits. Elia looks at you. The choice is yours.{/i}"
    menu:
        "[Trust] Ask them what we should do.":
            $ game_state.set_flag("mentor_trusted")
            $ game_state.set_flag("rep_unknown_ally", game_state.get_flag("rep_unknown_ally", 0) + 1)
            jump act1_mentor_contact_trust_response
        "[Demand Answers] Who are you? Why should we believe this?":
            $ game_state.set_flag("mentor_questioned")
            jump act1_mentor_contact_demand_response
        "[Cut Transmission] This is manipulation. End it now.":
            $ game_state.set_flag("mentor_rejected")
            jump act1_mentor_contact_cut_response
        "[Trace Signal] Keep them talking. Waffle—lock onto that signal.":
            $ game_state.set_flag("mentor_traced")
            jump act1_mentor_contact_trace_attempt

label act1_mentor_contact_trust_response:
    unknown "{i}A pause. The static shifts—something like relief.{/i} Smart. Keep her off station registries. Stay mobile. Don't let her touch Compact medical scanners. And when the time comes... trust the shard."
    jump act1_mentor_contact_trust_followup

label act1_mentor_contact_trust_followup:
    $ game_state.set_flag("mentor_contacted")
    unknown "I'll contact you again when it's safe. Until then—{b}keep her hidden. Keep her learning.{/b}"
    jump act1_mentor_contact_mentor_crew_warning

label act1_mentor_contact_demand_response:
    unknown "{i}A sound that might be a laugh, distorted through static.{/i} Fair question. I'm someone who failed to get her out sooner. Someone who's trying to make that right."
    jump act1_mentor_contact_demand_followup

label act1_mentor_contact_demand_followup:
    $ game_state.set_flag("mentor_contacted")
    unknown "Believe me or don't. But {b}watch the corporate feeds{/b}. Watch for Aurum Extraction filing debt recovery claims. You'll see I'm right."
    jump act1_mentor_contact_mentor_crew_warning

label act1_mentor_contact_cut_response:
    elia "{i}She kills the transmission with a single gesture.{/i} If they wanted to help, they'd show their face. We don't trust shadows."
    jump act1_mentor_contact_cut_followup

label act1_mentor_contact_cut_followup:
    $ game_state.set_flag("mentor_contacted")
    waffle "Signal terminated. Source remains unknown. {i}[Beat.]{/i} Recommendation: Monitor corporate feeds anyway. Just in case."
    jump act1_mentor_contact_bee_react_cut

label act1_mentor_contact_trace_attempt:
    waffle "Attempting signal lock... Encryption is layered, rotating. I need more time. {b}Keep them talking.{/b}"
    $ _sc_result = skill_check("tech", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_mentor_contact_trace_success
    else:
        jump act1_mentor_contact_trace_failure

label act1_mentor_contact_trace_success:
    waffle "Partial lock acquired. Signal origin: {b}Crucible Station, Sublevel 9{/b}. Residential block. Registered to a dead woman—expired thirty years ago. Whoever this is, they've been a ghost a long time."
    jump act1_mentor_contact_trace_reaction

label act1_mentor_contact_trace_failure:
    waffle "Lost it. Encryption rotated faster than I could pin. All I caught was a region tag—somewhere in the Crucible cluster. Could be anyone."
    jump act1_mentor_contact_trace_reaction

label act1_mentor_contact_trace_reaction:
    $ game_state.set_flag("mentor_contacted")
    unknown "{i}The voice turns colder.{/i} Clever. Doesn't matter. You won't find me unless I want to be found. But I'll forgive the attempt—because you're going to need what I say next."
    jump act1_mentor_contact_mentor_crew_warning

label act1_mentor_contact_mentor_crew_warning:
    $ game_state.set_flag("mentor_warning_heard")
    unknown "{i}[Static drops to a whisper.]{/i} One more thing. Someone on your crew isn't what they seem. I don't know who. The signal noise makes it hard to be sure. But {b}someone close to you has a second loyalty.{/b}"
    jump act1_mentor_contact_mentor_crew_warning_2

label act1_mentor_contact_mentor_crew_warning_2:
    unknown "Could be debt. Could be ideology. Could be blackmail. Doesn't matter. When Aurum comes knocking, someone on that ship is going to open the door. {i}[The static swells.]{/i} Watch for it."
    jump act1_mentor_contact_signal_death

label act1_mentor_contact_signal_death:
    "{i}The transmission collapses—not cut, not faded. Shredded. The encryption eats itself, leaving nothing but dead air and the faint smell of overheated circuitry.{/i}"
    jump act1_mentor_contact_bee_react_full

label act1_mentor_contact_bee_react_full:
    "{{BEE:: UNKNOWN CONTACT TERMINATED | AGITATED | lattice resonance claims require verification — crew integrity warning logged — recommend heightened monitoring of all shipboard communications}}"
    jump act1_mentor_contact_elia_aftermath

label act1_mentor_contact_elia_aftermath:
    elia "{i}She stares at the dead comms panel for a long moment.{/i} Someone on the crew. That's a hell of a parting gift. Could be nothing. Could be the kind of nothing that gets us killed."
    jump act1_mentor_contact_aftermath_choice

label act1_mentor_contact_aftermath_choice:
    "{i}The silence on the bridge is thick enough to cut. Elia watches you, waiting.{/i}"
    menu:
        "[Cautious] We tell no one about this. Not until we know more.":
            jump act1_mentor_contact_aftermath_secret
        "[Open] We tell the crew. If someone's compromised, transparency is our best weapon.":
            jump act1_mentor_contact_aftermath_open
        "[Dismissive] It's paranoia bait. Classic destabilization. Ignore it.":
            jump act1_mentor_contact_aftermath_dismiss

label act1_mentor_contact_aftermath_secret:
    $ game_state.set_flag("mentor_warning_secret")
    elia "Agreed. We keep this between us. I'll watch. You watch. And if anyone so much as breathes wrong near a comm terminal— {i}she draws a finger across her throat.{/i}"
    return

label act1_mentor_contact_aftermath_open:
    $ game_state.set_flag("mentor_warning_shared")
    elia "{i}She exhales through her teeth.{/i} Risky. If the mole is real, we just told them we know. But if it makes them slip up... fine. Your call, Captain."
    return

label act1_mentor_contact_aftermath_dismiss:
    $ game_state.set_flag("mentor_warning_dismissed")
    elia "Maybe. {i}She doesn't look convinced.{/i} But I'm sleeping with one eye open anyway. Old habit. {i}She turns and walks off the bridge without another word.{/i}"
    return

label act1_mentor_contact_bee_react_cut:
    "{{BEE:: transmission terminated prematurely | AGITATED | partial data captured — lattice resonance claims flagged for review — insufficient information to assess threat level}}"
    jump act1_mentor_contact_elia_aftermath_cut

label act1_mentor_contact_elia_aftermath_cut:
    elia "{i}She flexes her hand, knuckles white.{/i} We cut them off before they finished. Might have been the right call. Might have cost us something. Either way—we watch our backs."
    return
