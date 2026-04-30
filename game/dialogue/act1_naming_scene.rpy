## act1_naming_scene.rpy — Auto-generated from act1_naming_scene.json
## 50 dialogue nodes

label act1_naming_scene:
    $ game_state.mark_dialogue_played("act1_naming_scene")
    jump act1_naming_scene_start

label act1_naming_scene_start:
    "{i}Day nine. Dinner. The galley is loud in the way a safe place gets loud — arguments that don't end in blood, opinions spoken like they won't be used as weapons.{/i}"
    jump act1_naming_scene_common_room_settle

label act1_naming_scene_common_room_settle:
    "{i}The Lumen Thief's common room smells like reclaimed coffee and scorched protein. Rho and Jalen are deep into something about coolant pressure. Nyx is cross-legged in the corner, eyes closed, lips moving. Vesper reads — or pretends to. The post-rescue quiet has calcified into routine. Nine days of not dying will do that.{/i}"
    jump act1_naming_scene_crew_gives_space

label act1_naming_scene_crew_gives_space:
    "{i}Elia catches Elisira's eye. Some signal passes between them — married-people semaphore. One by one, the crew finds reasons to drift. Rho suddenly needs to check the port thruster. Jalen remembers a critical firmware update. Nyx opens her eyes, reads the room, and simply leaves. Only Vesper stays, but she's already invisible behind her book.{/i}"
    jump act1_naming_scene_elia_offer_setup

label act1_naming_scene_elia_offer_setup:
    elia "{i}She sets down her fork. The table goes quiet — not fearful quiet, but attentive quiet.{/i} We need to talk about your name."
    jump act1_naming_scene_avyanna_confused

label act1_naming_scene_avyanna_confused:
    avyanna "My... name?"
    jump act1_naming_scene_elisira_number_context

label act1_naming_scene_elisira_number_context:
    elisira "Extraction subjects aren't given names. They're given designators. Yours was Worker 477 — a sequential integer assigned at intake. It corresponds to nothing. It means nothing. That was by design."
    jump act1_naming_scene_elia_explains

label act1_naming_scene_elia_explains:
    elia "Worker 477. That's what they gave you. A number on a ledger. We don't use those here."
    jump act1_naming_scene_player_feels_about_name

label act1_naming_scene_player_feels_about_name:
    "{i}A name. You've never had one that wasn't a barcode. The idea sits in your chest like something swallowed wrong.{/i}"
    menu:
        "'I don't need a name. I've survived fine without one.'":
            $ game_state.set_flag("resistant_to_name")
            jump act1_naming_scene_resistant_response
        "'Please. I've wanted — I didn't know I wanted one until now.'":
            $ game_state.set_flag("eager_for_name")
            $ relationship_manager.process_reputation_affinity("elia", 1)
            $ relationship_manager.process_reputation_affinity("elisira", 1)
            jump act1_naming_scene_eager_response
        "'I don't understand. What does having a name change?'":
            $ game_state.set_flag("confused_about_name")
            jump act1_naming_scene_confused_response

label act1_naming_scene_resistant_response:
    avyanna "I don't need a name. Numbers work. Numbers don't pretend to be something they're not."
    jump act1_naming_scene_elia_gentle_push

label act1_naming_scene_elia_gentle_push:
    elia "{i}She doesn't flinch.{/i} Numbers work for inventory. You're not inventory. Not anymore."
    jump act1_naming_scene_elisira_clarifies

label act1_naming_scene_eager_response:
    avyanna "Please. {i}The word comes out cracked. Raw. You didn't rehearse it because you didn't know you'd need to.{/i} I want one."
    jump act1_naming_scene_elisira_clarifies

label act1_naming_scene_confused_response:
    avyanna "I don't understand. A name is just — it's a label. What does it change?"
    jump act1_naming_scene_elisira_explains_meaning

label act1_naming_scene_elisira_explains_meaning:
    elisira "A designator tells the system where to file you. A name tells {i}you{/i} who you are when the system isn't looking. The difference is ontological."
    jump act1_naming_scene_elisira_clarifies

label act1_naming_scene_elisira_clarifies:
    elisira "We'd like to offer you a stable attachment structure without coercion, contingent on your autonomous choice to —"
    jump act1_naming_scene_elia_interrupts

label act1_naming_scene_elia_interrupts:
    elia "{i}Cutting in.{/i} What she means is: we want to adopt you. Give you our name. Lagrange. If you want it."
    jump act1_naming_scene_lagrange_meaning

label act1_naming_scene_lagrange_meaning:
    elisira "Lagrange — it isn't a bloodline. It's a claiming word. In the old Drift dialect, it meant 'the still point between two bodies in motion.' A place of balance. We give it to those we choose as crew. As family."
    jump act1_naming_scene_elia_name_offer

label act1_naming_scene_elia_name_offer:
    elia "{i}She reaches across the table. Not to touch — just to close distance.{/i} We had a name picked. Avyanna. In the same dialect, it means 'one who carries light she didn't steal.'"
    jump act1_naming_scene_rho_reaction

label act1_naming_scene_rho_reaction:
    rho "{i}Mouth full of protein, completely unrepentant.{/i} You both suck at this. It's kind of adorable."
    jump act1_naming_scene_jalen_reaction

label act1_naming_scene_jalen_reaction:
    jalen "I'm logging this as 'parental units experiencing turbulence.'"
    jump act1_naming_scene_waffle_comment

label act1_naming_scene_waffle_comment:
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: turbulence confirmed | RECOMMENDATION: seatbelts | COMMENT: also popcorn}}{/i}}"
    jump act1_naming_scene_avyanna_reaction

label act1_naming_scene_avyanna_reaction:
    "{i}Your heart is pounding. They're offering you a name. A family. A belonging that isn't ownership. The presence behind your eyes pulses — something that might be encouragement.{/i}"
    menu:
        "Accept the name. 'Avyanna Lagrange. I... I want that.'":
            $ game_state.set_flag("accepted_name_immediately")
            $ relationship_manager.process_reputation_affinity("elia", 2)
            $ relationship_manager.process_reputation_affinity("elisira", 2)
            jump act1_naming_scene_accept_immediate
        "Ask what it means. 'What does the name cost?'":
            $ game_state.set_flag("asked_name_cost")
            jump act1_naming_scene_ask_cost
        "Suggest a change. 'Could I... keep part of it? Make it mine?'":
            $ game_state.set_flag("suggested_name_modification")
            jump act1_naming_scene_suggest_modification
        "Hesitate. 'I need to think about it.'":
            $ game_state.set_flag("hesitated_on_name")
            jump act1_naming_scene_hesitate

label act1_naming_scene_accept_immediate:
    avyanna "Avyanna Lagrange. {i}The words feel strange in your mouth. Heavy with something that isn't debt.{/i} I want that."
    jump act1_naming_scene_vesper_accept_response

label act1_naming_scene_vesper_accept_response:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}She watches from across the table. Something in her expression shifts — recognition, maybe. The particular attention of someone cataloging a moment she doesn't want to forget.{/i} It suits you."
    jump act1_naming_scene_elia_welcome

label act1_naming_scene_suggest_modification:
    avyanna "Could I — keep the shape of it? Avyanna. But make it mine. Carry it differently, maybe."
    jump act1_naming_scene_elia_modification_response

label act1_naming_scene_elia_modification_response:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "{i}A slow smile. Not indulgent — proud.{/i} That's exactly what a name is for. You take it and make it yours. However it fits."
    jump act1_naming_scene_elisira_modification_nod

label act1_naming_scene_elisira_modification_nod:
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "Linguistically, a name is a living structure. It's supposed to be shaped by the one who carries it. You're already doing it right."
    jump act1_naming_scene_modification_accept

label act1_naming_scene_modification_accept:
    "{i}You turn it over in your mind. Avyanna Lagrange. Not a number. Not a designation. Yours — in your own way, on your own terms.{/i}"
    jump act1_naming_scene_elia_welcome

label act1_naming_scene_ask_cost:
    avyanna "What does the name cost?"
    jump act1_naming_scene_elia_cost_response

label act1_naming_scene_elia_cost_response:
    elia "{i}Her expression softens — not pity, but understanding.{/i} Nothing. It costs nothing. That's the point."
    jump act1_naming_scene_vesper_cost_response

label act1_naming_scene_vesper_cost_response:
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "A name isn't a contract. It's not terms and conditions. It's just... yours. To carry or set down whenever you choose."
    jump act1_naming_scene_accept_after_question

label act1_naming_scene_accept_after_question:
    "{i}The presence behind your eyes pulses warmly. No cost. No invoice. Just a name, offered freely.{/i}"
    menu:
        "'Then yes. Avyanna Lagrange.'":
            $ game_state.set_flag("accepted_name")
            $ relationship_manager.process_reputation_affinity("elia", 2)
            $ relationship_manager.process_reputation_affinity("elisira", 2)
            jump act1_naming_scene_elia_welcome
        "'I still need time.'":
            jump act1_naming_scene_time_response

label act1_naming_scene_hesitate:
    avyanna "I need to think about it. {i}The words come out small. Defensive. The Kennel voice — the one that knows every gift is a leash.{/i}"
    jump act1_naming_scene_elia_patient

label act1_naming_scene_elia_patient:
    elia "Take your time. The offer doesn't expire."
    jump act1_naming_scene_vesper_patient

label act1_naming_scene_vesper_patient:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Her eyes meet yours across the table. No pressure. No disappointment. Just steady presence.{/i} When you're ready. Not before."
    jump act1_naming_scene_time_response

label act1_naming_scene_time_response:
    $ game_state.set_flag("naming_complete")
    "{i}The crew returns to dinner as if nothing world-changing just happened. Rho argues with Jalen about protein storage. Nyx explains something incomprehensible. Elia and Elisira sit close.

And you sit among them, holding a name you haven't decided to keep yet, wondering if this is what belonging feels like.{/i}"
    return

label act1_naming_scene_elia_welcome:
    elia "{i}A nod. Simple. Final.{/i} Welcome to the family, Avyanna Lagrange."
    jump act1_naming_scene_crew_reactions_ceremony

label act1_naming_scene_crew_reactions_ceremony:
    "{i}The common room shifts. Something unspoken moves through it — the crew recognizing a threshold crossed.{/i}"
    menu:
        "Look at Vesper.":
            $ relationship_manager.process_reputation_affinity("vesper", 1)
            jump act1_naming_scene_vesper_ceremony_reaction
        "Look at Rho.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_naming_scene_rho_ceremony_reaction
        "Look at Nyx.":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_naming_scene_nyx_ceremony_reaction

label act1_naming_scene_vesper_ceremony_reaction:
    vesper "{i}She raises her glass — half-empty, something amber. Her eyes don't leave yours.{/i} To Avyanna Lagrange. May she be more trouble than her mothers can handle."
    jump act1_naming_scene_rho_grunt_approval

label act1_naming_scene_rho_ceremony_reaction:
    rho "{i}He sets down his mug with deliberate weight. For Rho, this is a standing ovation.{/i} Lagrange. Good. Now eat your dinner before it gets cold."
    jump act1_naming_scene_nyx_ritual_gesture

label act1_naming_scene_nyx_ceremony_reaction:
    nyx "{i}She presses two fingers to her lips, then opens her hand toward you — palm up, fingers spread. An old gesture. You don't know what it means, but you feel it land somewhere behind your ribs.{/i} The pattern knows your name now. It always did."
    jump act1_naming_scene_vesper_raises_glass

label act1_naming_scene_rho_grunt_approval:
    rho "{i}He lifts his mug an inch off the table. Barely. The absolute minimum required gesture of solidarity.{/i} Don't let it go to your head, kid."
    jump act1_naming_scene_nyx_ritual_gesture

label act1_naming_scene_nyx_ritual_gesture:
    nyx "{i}She traces a small sigil in the air with one finger — something half-remembered, half-invented. Her lips move without sound.{/i} Named and witnessed. The pattern holds."
    jump act1_naming_scene_vesper_raises_glass

label act1_naming_scene_vesper_raises_glass:
    vesper "{i}She raises her glass. The amber liquid catches the overhead light.{/i} To the newest Lagrange. Welcome to the mess."
    jump act1_naming_scene_bee_naming_response

label act1_naming_scene_bee_naming_response:
    bee "{{BEE:: PATTERN RECOGNIZED — designation Worker 477 deprecated | new index: Avyanna Lagrange | cross-reference: family unit, chosen | note: pattern consistency increased by 1.7 standard deviations | status: nomenclature accepted}}"
    jump act1_naming_scene_crew_welcome

label act1_naming_scene_crew_welcome:
    "{i}Rho raises his coffee mug. Jalen nods without looking up from his datapad. Nyx smiles in a way that suggests the universe has become slightly more elegant.{/i}"
    jump act1_naming_scene_bubbles_naming_welcome

label act1_naming_scene_bubbles_naming_welcome:
    bubbles "{i}Warm, through the speakers:{/i} Avyanna Lagrange. I've updated your crew profile. It looks beautiful there."
    jump act1_naming_scene_waffle_naming_update

label act1_naming_scene_waffle_naming_update:
    waffle "{i}}{{WAFFLE.BAT// REGISTRY_UPDATE: Worker 477 → Avyanna Lagrange | STATUS: crew, family, home | PERSONAL_NOTE: welcome. truly.}}{/i}}"
    jump act1_naming_scene_cinnamon_naming_ack

label act1_naming_scene_cinnamon_naming_ack:
    cinnamon "Lagrange. Noted. Good name."
    jump act1_naming_scene_naming_final

label act1_naming_scene_naming_final:
    $ game_state.set_flag("has_lagrange_name")
    "{i}The presence behind your eyes pulses once — warm, patient, approving. Whatever it is, wherever it came from, it seems to agree: this name fits.{/i}"
    jump act1_naming_scene_naming_complete_flag

label act1_naming_scene_naming_complete_flag:
    $ game_state.set_flag("naming_complete")
    "{i}You are Avyanna Lagrange. Not because someone filed the paperwork. Because people who owe you nothing offered you everything, and you let them.{/i}"
    return
