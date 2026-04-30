## act1_deep_nyx.rpy — Auto-generated from act1_deep_nyx.json
## 260 dialogue nodes

label act1_deep_nyx:
    $ game_state.mark_dialogue_played("act1_deep_nyx")
    jump act1_deep_nyx_start

label act1_deep_nyx_start:
    if game_state.has_flag("bee_revealed"):
        "{i}Late cycle. The maintenance deck hums with engine noise. Nyx stands alone, hands pressed to the bulkhead, and the space around her shimmers. The shard in your chest responds immediately — recognition, curiosity. It knows what Nyx is doing. Perhaps it's done similar things before.{/i}"
    else:
        "{i}Late cycle. The ship's maintenance deck, where the hum of engines makes conversation difficult for most people. But Nyx is here, alone, hands pressed against a bulkhead. She's not repairing anything mechanical — she's doing something else. Something to the space itself. The air shimmers faintly around her fingers.{/i}"
    jump act1_deep_nyx_avyanna_approach

label act1_deep_nyx_avyanna_approach:
    avyanna "{i}I approach quietly. The presence behind my eyes is unusually focused, watching Nyx with something like... recognition?{/i} You're working late."
    jump act1_deep_nyx_nyx_doesnt_turn

label act1_deep_nyx_nyx_doesnt_turn:
    nyx "{i}Doesn't turn, but acknowledges.{/i} The lattice here is degrading. Old damage — pre-war construction flaws compounded by decades of strain. {i}A pause.{/i} If I don't reinforce it, we'll have a hull breach in six months. Maybe less."
    jump act1_deep_nyx_avyanna_watches

label act1_deep_nyx_avyanna_watches:
    avyanna "You can see that? Damage that hasn't happened yet?"
    jump act1_deep_nyx_nyx_turns

label act1_deep_nyx_nyx_turns:
    nyx "{i}Finally turning to face you. She looks tired. More tired than you've seen her.{/i} I can see the pattern leading to it. Probability waves collapsing toward failure. {i}A slight smile, deflecting.{/i} Exciting work. Really thrilling stuff."
    jump act1_deep_nyx_choice_opening

label act1_deep_nyx_choice_opening:
    if game_state.has_flag("first_watch_visited_nyx"):
        "{i}You've been here before — sitting watch with Nyx, observing her work. But tonight feels different. The usual composure is cracking at the edges. She's tired. Not just physically. Something deeper.{/i}"
    else:
        "{i}Something feels different tonight. Nyx is usually composed, distant. But there's a weariness here. A weight she's carrying. The question is whether you acknowledge it or let her hide behind deflection.{/i}"
    menu:
        "[Empathy DC 14] 'You're not just tired. Something's bothering you.'":
            $ _sc_result = skill_check("empathy", 14, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_nyx_empathy_success
            else:
                jump act1_deep_nyx_empathy_failure
        "'Can I help? With the lattice work, I mean.'":
            jump act1_deep_nyx_offer_help
        "'You don't have to do this alone. The repairs, I mean.'":
            jump act1_deep_nyx_gentle_observation

label act1_deep_nyx_empathy_success:
    "{i}You watch her carefully. The way she holds herself — shoulders too straight, jaw too tight. The weariness isn't physical exhaustion. It's something older. Something she's been carrying for a long time. And tonight, for some reason, the weight is too much to hide.{/i}"
    jump act1_deep_nyx_empathy_avyanna

label act1_deep_nyx_empathy_avyanna:
    avyanna "You're not just tired. Something's bothering you. Has been for a while."
    jump act1_deep_nyx_nyx_deflects

label act1_deep_nyx_nyx_deflects:
    nyx "{i}She looks away, jaw tightening further.{/i} I'm fine. Just lattice work. It's draining, that's all."
    jump act1_deep_nyx_empathy_press

label act1_deep_nyx_empathy_press:
    avyanna "Nyx. {i}Quiet, but firm.{/i} I've seen you do lattice work before. This isn't that."
    jump act1_deep_nyx_nyx_breaks

label act1_deep_nyx_nyx_breaks:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}A long silence. Then, quietly:{/i} Today's the anniversary. Of when I left the Writbound Order. {i}She leans against the bulkhead, suddenly looking smaller.{/i} Seven years. You'd think it would stop mattering."
    jump act1_deep_nyx_writbound_revealed

label act1_deep_nyx_empathy_failure:
    "{i}You try to read her, but Nyx's control is too good. Whatever she's feeling, it's locked behind practiced discipline. She's had years to perfect this mask.{/i}"
    jump act1_deep_nyx_empathy_fail_observe

label act1_deep_nyx_empathy_fail_observe:
    avyanna "You seem... different tonight. More tired."
    jump act1_deep_nyx_nyx_minimal_answer

label act1_deep_nyx_nyx_minimal_answer:
    nyx "{i}A slight shrug.{/i} Long day. Lattice work is exhausting. {i}She turns back to the bulkhead.{/i} I should finish this."
    jump act1_deep_nyx_choice_after_deflection

label act1_deep_nyx_offer_help:
    avyanna "Can I help? With the lattice work, I mean. You've been teaching me."
    jump act1_deep_nyx_nyx_considers_help

label act1_deep_nyx_nyx_considers_help:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She looks at you for a long moment, considering.{/i} This is... advanced work. Structural reinforcement. But... {i}A pause.{/i} Yes. Actually. Your shard might be useful here. It has an intuitive grasp of resonance patterns."
    jump act1_deep_nyx_work_together

label act1_deep_nyx_gentle_observation:
    avyanna "You don't have to do this alone. The repairs. The lattice work. Any of it."
    jump act1_deep_nyx_nyx_pause

label act1_deep_nyx_nyx_pause:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She stops, hands falling away from the bulkhead. For a moment she just stands there, back to you.{/i} I'm used to working alone. {i}Quieter.{/i} I've been alone for a long time."
    jump act1_deep_nyx_avyanna_stays

label act1_deep_nyx_avyanna_stays:
    avyanna "{i}I don't leave. Just stay, quiet, present.{/i}"
    jump act1_deep_nyx_nyx_turns_vulnerable

label act1_deep_nyx_nyx_turns_vulnerable:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She turns, and something in her expression has shifted. The mask is slipping.{/i} Today's the anniversary. Seven years since I left the Writbound Order. {i}A bitter smile.{/i} Since I ran away, more accurately."
    jump act1_deep_nyx_writbound_revealed

label act1_deep_nyx_writbound_revealed:
    "{i}The Writbound Order. You've heard of them — memory archivists, lattice manipulators, keepers of pre-war knowledge. But also rumors of darker practices. Memory modification. Thought control. Nyx... was one of them.{/i}"
    jump act1_deep_nyx_avyanna_writbound_reaction

label act1_deep_nyx_avyanna_writbound_reaction:
    avyanna "You were Writbound? {i}Trying to keep judgment out of my voice.{/i} I didn't know."
    jump act1_deep_nyx_nyx_bitter_laugh

label act1_deep_nyx_nyx_bitter_laugh:
    nyx "{i}A laugh, sharp and bitter.{/i} Most people don't. I don't advertise it. {i}She slides down the wall, sitting on the deck, suddenly exhausted.{/i} I was a Resonance Theorist. Talented, apparently. Promising. They recruited me young — fifteen. Told me I had a gift."
    jump act1_deep_nyx_choice_respond_writbound

label act1_deep_nyx_choice_respond_writbound:
    "{i}Nyx is opening up — really opening up — in a way she never has before. How you respond here matters.{/i}"
    menu:
        "'What happened? Why did you leave?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_why_left
        "[Sit beside her] 'You don't have to tell me if it's too hard.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_offer_space
        "'Fifteen is too young to make that choice. They took advantage of you.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_validate_anger

label act1_deep_nyx_ask_why_left:
    avyanna "What happened? Why did you leave?"
    jump act1_deep_nyx_nyx_explains_order

label act1_deep_nyx_offer_space:
    "{i}You sit down beside her, not too close, just... present. Offering companionship without demanding confession.{/i}"
    jump act1_deep_nyx_avyanna_sits

label act1_deep_nyx_avyanna_sits:
    avyanna "{i}Sitting beside her.{/i} You don't have to tell me if it's too hard. But I'm here if you want to."
    jump act1_deep_nyx_nyx_grateful

label act1_deep_nyx_nyx_grateful:
    nyx "{i}She glances at you, something softening in her expression.{/i} Thank you. {i}A breath.{/i} But I... I think I need to say it. I haven't talked about this in years."
    jump act1_deep_nyx_nyx_explains_order

label act1_deep_nyx_validate_anger:
    avyanna "Fifteen is too young to make that choice. They took advantage of you."
    jump act1_deep_nyx_nyx_considers_anger

label act1_deep_nyx_nyx_considers_anger:
    nyx "{i}She looks surprised, then thoughtful.{/i} I... yes. I suppose they did. {i}A pause.{/i} I always told myself I chose it freely. That I wanted the knowledge. But... {i}Quieter.{/i} I was a child. I didn't understand what I was agreeing to."
    jump act1_deep_nyx_nyx_explains_order

label act1_deep_nyx_nyx_explains_order:
    nyx "The Writbound don't just study the lattice. They manipulate it. Reality, memory, thought — it's all patterns that can be rewritten. {i}Her voice is distant, clinical.{/i} They called it necessary. Preserving knowledge. Preventing dangerous information from spreading. Protecting humanity."
    jump act1_deep_nyx_nyx_darker_truth

label act1_deep_nyx_nyx_darker_truth:
    nyx "{i}A bitter edge.{/i} But preservation requires control. And control requires... sacrifice. {i}She looks at her hands.{/i} We modified memories. Removed traumatic events, suppressed dangerous research, edited personalities. All for the greater good."
    jump act1_deep_nyx_avyanna_horror

label act1_deep_nyx_avyanna_horror:
    avyanna "{i}A chill runs through me.{/i} You... changed people's minds? Against their will?"
    jump act1_deep_nyx_nyx_admission

label act1_deep_nyx_nyx_admission:
    nyx "{i}She won't look at you.{/i} Yes. I did. For three years. {i}A long silence.{/i} I told myself it was necessary. That I was helping. That the Order knew best. {i}Her voice cracks slightly.{/i} I was very good at lying to myself."
    jump act1_deep_nyx_choice_judgment

label act1_deep_nyx_choice_judgment:
    "{i}This is the heart of it. Nyx is confessing something she considers unforgivable. How you respond will shape everything between you.{/i}"
    menu:
        "'You were eighteen. They manipulated you into doing terrible things.'":
            $ game_state.set_flag("nyx_forgiven")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_forgive_youth
        "'But you left. That took courage. You recognized it was wrong.'":
            $ game_state.set_flag("nyx_validated")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_validate_leaving
        "'That's... hard to hear. I need a moment to process this.'":
            $ relationship_manager.process_reputation_affinity("nyx", -1)
            jump act1_deep_nyx_need_processing

label act1_deep_nyx_forgive_youth:
    avyanna "You were eighteen. Still practically a child. They manipulated you into doing terrible things. That doesn't make you the monster — it makes them the monsters."
    jump act1_deep_nyx_nyx_tears

label act1_deep_nyx_nyx_tears:
    nyx "{i}She closes her eyes. When she opens them again, there's moisture at the corners.{/i} I've never... {i}Her voice is unsteady.{/i} I've carried this guilt for seven years. Told myself I didn't deserve forgiveness. That I was complicit."
    jump act1_deep_nyx_avyanna_comfort

label act1_deep_nyx_avyanna_comfort:
    avyanna "{i}I reach out, carefully, giving her time to pull away. She doesn't. My hand settles on her shoulder.{/i} You were a victim too. And you got out. That matters."
    jump act1_deep_nyx_nyx_release

label act1_deep_nyx_nyx_release:
    nyx "{i}She leans into the contact, just slightly. A small surrender.{/i} Thank you. {i}A shaky breath.{/i} I don't know if I believe it yet. But thank you for saying it."
    jump act1_deep_nyx_memory_trauma_reveal

label act1_deep_nyx_validate_leaving:
    avyanna "But you left. You recognized it was wrong and you walked away. That took real courage."
    jump act1_deep_nyx_nyx_leaving_story

label act1_deep_nyx_nyx_leaving_story:
    nyx "{i}A bitter smile.{/i} I didn't walk. I ran. {i}A pause.{/i} There was a subject — a young woman who'd witnessed a corporate massacre. The Order wanted to remove her memories, make her forget. She'd be safer that way, they said. Compliant."
    jump act1_deep_nyx_nyx_refusal

label act1_deep_nyx_nyx_refusal:
    nyx "I looked at her and saw myself. Eighteen, terrified, being told this was for my own good. {i}Her jaw tightens.{/i} I refused the assignment. They said I'd be disciplined. I said I'd leave. They said... {i}A pause.{/i} They said they'd help me understand. Make me more cooperative."
    jump act1_deep_nyx_avyanna_realizes

label act1_deep_nyx_avyanna_realizes:
    avyanna "They were going to modify your memories. Your mind."
    jump act1_deep_nyx_nyx_confirms

label act1_deep_nyx_nyx_confirms:
    nyx "{i}A nod.{/i} I ran that night. Took nothing but my research and whatever credits I could steal. {i}Quieter.{/i} They tried to stop me. I had to... hurt people. Friends. To escape."
    jump act1_deep_nyx_memory_trauma_reveal

label act1_deep_nyx_need_processing:
    avyanna "That's... that's hard to hear. I need a moment to process this."
    jump act1_deep_nyx_nyx_understands

label act1_deep_nyx_nyx_understands:
    nyx "{i}She nods, expression closing off again.{/i} Of course. That's fair. {i}She starts to stand.{/i} I should finish the repairs anyway."
    jump act1_deep_nyx_choice_stop_them

label act1_deep_nyx_choice_stop_them:
    "{i}She's retreating. Shutting down. You can let her go, or you can push through your discomfort and stay present.{/i}"
    menu:
        "'Wait. Don't go. I'm processing, but I'm not leaving.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_stay_present
        "'I think we both need space right now.'":
            $ relationship_manager.process_reputation_affinity("nyx", -2)
            jump act1_deep_nyx_mutual_space

label act1_deep_nyx_stay_present:
    avyanna "Wait. Don't go. {i}I catch her hand.{/i} I'm processing, but I'm not leaving. This doesn't change... us. The crew."
    jump act1_deep_nyx_nyx_cautious_return

label act1_deep_nyx_nyx_cautious_return:
    nyx "{i}She stops, looking down at where you're holding her hand.{/i} You don't have to —"
    jump act1_deep_nyx_avyanna_insists

label act1_deep_nyx_avyanna_insists:
    avyanna "I know. I'm choosing to. {i}Meeting her eyes.{/i} Tell me the rest. Please."
    jump act1_deep_nyx_nyx_sits_again

label act1_deep_nyx_nyx_sits_again:
    nyx "{i}She sits back down, closer this time. Still cautious, but willing to trust.{/i} Alright. {i}A breath.{/i} Alright."
    jump act1_deep_nyx_memory_trauma_reveal

label act1_deep_nyx_mutual_space:
    avyanna "I think... we both need some space right now. To process."
    jump act1_deep_nyx_nyx_withdraws

label act1_deep_nyx_nyx_withdraws:
    $ game_state.set_flag("deep_nyx_partial")
    nyx "{i}She nods, expression neutral.{/i} Of course. Space. Yes. {i}She turns away, already rebuilding her walls.{/i} Goodnight, Avyanna."
    return

label act1_deep_nyx_memory_trauma_reveal:
    nyx "{i}Her voice drops lower.{/i} The worst part? They did catch me once. Before I fully escaped. {i}She touches her temple.{/i} They tried to edit me. Remove my doubts. My guilt. Make me a perfect little theorist again."
    jump act1_deep_nyx_avyanna_alarmed

label act1_deep_nyx_avyanna_alarmed:
    avyanna "Did it work? Are you —"
    jump act1_deep_nyx_nyx_interrupted

label act1_deep_nyx_nyx_interrupted:
    $ game_state.set_flag("nyx_shared_writbound")
    nyx "{i}Shaking her head.{/i} No. It... I have natural resistance to lattice manipulation. Probably why I'm good at it myself. {i}A pause.{/i} But they got partway through. There are gaps now. Holes in my memory. I don't know what I've forgotten."
    jump act1_deep_nyx_memory_consequences

label act1_deep_nyx_memory_consequences:
    nyx "Sometimes I remember fragments. A face I should know but don't. A skill I have but can't recall learning. {i}Her hands are shaking slightly.{/i} They took pieces of me. And I'll never get them back."
    jump act1_deep_nyx_avyanna_response_trauma

label act1_deep_nyx_avyanna_response_trauma:
    avyanna "{i}The shard in my chest aches with sympathetic pain. Loss. Violation. Things it understands intimately.{/i} I'm so sorry. That's... I can't imagine."
    jump act1_deep_nyx_nyx_laughs_darkly

label act1_deep_nyx_nyx_laughs_darkly:
    nyx "{i}A dark laugh.{/i} The irony is I do this to the ship. To the lattice. I manipulate, reinforce, edit reality. Every time I do it, I remember what was done to me. {i}Meeting your eyes.{/i} But I do it anyway. Because someone has to. Because we need it to survive."
    jump act1_deep_nyx_choice_understanding

label act1_deep_nyx_choice_understanding:
    "{i}This is why Nyx is the way she is. Controlled. Distant. Precise. She's using her trauma as a tool, transmuting violation into skill. It's survival. It's also slowly eating her alive.{/i}"
    menu:
        "'That's not ironic. That's you taking power back from them.'":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_reframe_power
        "'Does it hurt? Using lattice manipulation after what they did?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_if_hurts
        "'You're not them. The way you use it — it's different. It's about care.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_validate_difference

label act1_deep_nyx_reframe_power:
    avyanna "That's not ironic. That's you taking power back from them. Using what they taught you, but on your terms. For people you've chosen."
    jump act1_deep_nyx_nyx_stunned

label act1_deep_nyx_nyx_stunned:
    nyx "{i}She stares at you, something shifting in her expression.{/i} I... I never thought of it that way. {i}A pause, then quieter.{/i} I always thought it made me complicit. Still using their methods."
    jump act1_deep_nyx_avyanna_explains

label act1_deep_nyx_avyanna_explains:
    avyanna "A knife can be used to hurt or heal. It's not the tool — it's the choice. You're choosing to protect. That's the opposite of what they did."
    jump act1_deep_nyx_nyx_accepts

label act1_deep_nyx_nyx_accepts:
    nyx "{i}She closes her eyes, breathing carefully.{/i} Thank you. {i}When she opens them again, something has eased.{/i} I needed to hear that. From someone I trust."
    jump act1_deep_nyx_inside_the_order

label act1_deep_nyx_ask_if_hurts:
    avyanna "Does it hurt? Using lattice manipulation after what they did to you?"
    jump act1_deep_nyx_nyx_admits_pain

label act1_deep_nyx_nyx_admits_pain:
    nyx "{i}A long pause.{/i} Yes. Every time. {i}She looks at her hands.{/i} It's like... picking at a wound that won't quite heal. But it's also the only thing I'm good at. The only way I can be useful."
    jump act1_deep_nyx_avyanna_protests

label act1_deep_nyx_avyanna_protests:
    avyanna "You're useful because you're you. Not because of what you can do to reality. We value you, Nyx. Not just your skills."
    jump act1_deep_nyx_nyx_uncertain

label act1_deep_nyx_nyx_uncertain:
    nyx "{i}She looks uncertain, like she wants to believe it but can't quite.{/i} I... thank you. I'll try to remember that."
    jump act1_deep_nyx_inside_the_order

label act1_deep_nyx_validate_difference:
    avyanna "You're not them. The way you use it — it's different. When you work on the ship, when you teach me, it's about care. About consent. That's the opposite of violation."
    jump act1_deep_nyx_nyx_emotional

label act1_deep_nyx_nyx_emotional:
    nyx "{i}Her composure finally cracks. She presses her hands to her face, shoulders shaking.{/i} I try. I try so hard to do it differently. To never be like them. But I'm so afraid I'll —"
    jump act1_deep_nyx_avyanna_reassures

label act1_deep_nyx_avyanna_reassures:
    avyanna "{i}I move closer, offering presence without demanding anything.{/i} You won't. You ask permission. You explain. You give people agency. That's the difference."
    jump act1_deep_nyx_nyx_recovers

label act1_deep_nyx_nyx_recovers:
    nyx "{i}She lowers her hands, wiping at her eyes.{/i} Sorry. I don't usually... {i}A breath.{/i} Thank you. For understanding. For not running."
    jump act1_deep_nyx_inside_the_order

label act1_deep_nyx_inside_the_order:
    "{i}A silence settles. Nyx stares at her hands — the faint luminescence beneath the skin, the lattice residue that never fully fades. The maintenance deck groans around you, steel and light and the deep vibration of engines. Nyx looks like she wants to say more.{/i}"
    jump act1_deep_nyx_choice_press_order

label act1_deep_nyx_choice_press_order:
    "{i}There's more to this story. You can feel it. The Order, the rituals, the binding itself — Nyx has barely scratched the surface.{/i}"
    menu:
        "'What was it like inside? The Order itself.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_inside_order
        "[Insight DC 13] Study the way Nyx holds her hands — the glow beneath the skin.":
            $ _sc_result = skill_check("insight", 13, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_nyx_insight_hands_success
            else:
                jump act1_deep_nyx_insight_hands_failure
        "'You don't have to keep going. We can stop here.'":
            jump act1_deep_nyx_offer_stop_order

label act1_deep_nyx_ask_inside_order:
    avyanna "What was it like inside? The Order itself. Where they kept you."
    jump act1_deep_nyx_nyx_describes_order

label act1_deep_nyx_nyx_describes_order:
    nyx "{i}Her eyes go distant.{/i} Beautiful. That was the worst part. The Spire of Remembrance — their headquarters — was the most beautiful place I've ever seen. Crystal walls that sang when you walked past them. Libraries of stolen memory preserved in lattice-glass. Gardens where thought itself bloomed in colors that don't have names."
    jump act1_deep_nyx_nyx_order_darker

label act1_deep_nyx_nyx_order_darker:
    nyx "We wore white. All of us. Initiates, theorists, archivists. White robes, bare feet on cold stone. They said it kept us grounded. Humble. {i}A bitter twist to her mouth.{/i} It kept us cold. Dependent. Hard to run when you have no shoes and no possessions."
    jump act1_deep_nyx_nyx_order_routine

label act1_deep_nyx_nyx_order_routine:
    nyx "Days started with meditation at fourth bell. Then study — lattice theory, resonance harmonics, memory architecture. We ate together. Prayed together. Slept in dormitories with no doors. Privacy was considered a weakness. A place for doubt to fester."
    jump act1_deep_nyx_nyx_order_binding_intro

label act1_deep_nyx_nyx_order_binding_intro:
    nyx "{i}Her voice drops.{/i} And then there was the Binding. The ritual that made us Writbound."
    jump act1_deep_nyx_avyanna_asks_binding

label act1_deep_nyx_avyanna_asks_binding:
    avyanna "{i}Quietly.{/i} What did they do to you?"
    jump act1_deep_nyx_nyx_describes_binding

label act1_deep_nyx_nyx_describes_binding:
    nyx "They open the lattice inside you. Not gently — not the way I teach you. They crack you open. Force the pathways wider than they're meant to go. It's like... {i}She searches for words.{/i} Imagine every nerve in your body becoming a doorway. Every thought becoming a corridor someone else can walk through."
    jump act1_deep_nyx_nyx_binding_pain

label act1_deep_nyx_nyx_binding_pain:
    nyx "It took three days. I screamed for the first two. {i}Said flatly, like reciting weather data.{/i} On the third day, the lattice settled into the new configuration. The pain stopped. The power began. {i}She flexes her fingers and a faint, sickly glow traces the veins beneath her skin.{/i} And part of me has been burning ever since."
    jump act1_deep_nyx_choice_binding_reaction

label act1_deep_nyx_choice_binding_reaction:
    "{i}Nyx's hands glow faintly in the dim maintenance deck. The light is wrong somehow — not warm, not cold, but something between states. The shard in your chest hums a low, discordant note. Recognition. Warning.{/i}"
    menu:
        "'Three days. They tortured you for three days and called it a gift.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_call_it_torture
        "[Empathy DC 15] Reach for her glowing hands.":
            $ _sc_result = skill_check("empathy", 15, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_nyx_reach_for_hands_success
            else:
                jump act1_deep_nyx_reach_for_hands_failure
        "'The burning — is it still happening? Right now?'":
            jump act1_deep_nyx_ask_burning

label act1_deep_nyx_call_it_torture:
    avyanna "Three days. They tortured you for three days and called it a gift."
    jump act1_deep_nyx_nyx_never_named

label act1_deep_nyx_nyx_never_named:
    nyx "{i}A flicker of something raw crosses her face.{/i} I never... no one's ever called it that before. Not out loud. {i}A pause.{/i} The Order called it an awakening. An honor. The highest privilege a theorist could receive. {i}Quieter.{/i} We thanked them afterward. That was the protocol."
    jump act1_deep_nyx_the_physical_cost

label act1_deep_nyx_reach_for_hands_success:
    "{i}You reach out slowly, giving her every chance to pull away. Your fingers close around her wrists — gently, carefully. The glow flares at your touch, then... softens. The shard responds, sending a wash of warmth through your hands. Nyx gasps.{/i}"
    jump act1_deep_nyx_nyx_startled_touch

label act1_deep_nyx_nyx_startled_touch:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "{i}Staring at where your hands meet hers.{/i} What are you... {i}She trails off, eyes widening.{/i} The burning. It's... quieter. How are you doing that?"
    jump act1_deep_nyx_avyanna_doesnt_know

label act1_deep_nyx_avyanna_doesnt_know:
    avyanna "{i}Honestly.{/i} I don't know. The shard is doing something. It felt... right."
    jump act1_deep_nyx_nyx_wonder

label act1_deep_nyx_nyx_wonder:
    $ game_state.set_flag("nyx_shard_soothed")
    nyx "{i}She doesn't pull away. Her expression is something between wonder and grief.{/i} Seven years. Seven years of burning and you just... {i}A breath that shakes.{/i} Don't let go. Not yet. Please."
    jump act1_deep_nyx_the_physical_cost

label act1_deep_nyx_reach_for_hands_failure:
    "{i}You reach for her hands, but Nyx flinches back instinctively. The glow flares brighter — defensive, reactive. Old reflexes from a place where touch meant control.{/i}"
    jump act1_deep_nyx_nyx_apologizes_flinch

label act1_deep_nyx_nyx_apologizes_flinch:
    nyx "{i}She pulls back, clutching her hands to her chest.{/i} Sorry. I'm sorry. I didn't mean — {i}A steadying breath.{/i} It's a reflex. In the Order, physical contact during lattice work was... not voluntary."
    jump act1_deep_nyx_avyanna_backs_off

label act1_deep_nyx_avyanna_backs_off:
    avyanna "No, I'm sorry. I should have asked first."
    jump act1_deep_nyx_nyx_recovers_flinch

label act1_deep_nyx_nyx_recovers_flinch:
    nyx "{i}A small, genuine smile — the first tonight.{/i} See? That. Asking. That's the difference between you and them. {i}She settles her hands in her lap, the glow fading.{/i} The Writbound never asked."
    jump act1_deep_nyx_the_physical_cost

label act1_deep_nyx_ask_burning:
    avyanna "The burning — is it still happening? Right now? As we speak?"
    jump act1_deep_nyx_nyx_admits_burning

label act1_deep_nyx_nyx_admits_burning:
    nyx "{i}She holds up her hands. In the dim light of the maintenance deck, you can see the glow pulsing faintly beneath the skin, tracing the lines of veins and tendons.{/i} Always. Low-grade, most of the time. Like holding your hands too close to a fire. But when I use the lattice — when I do heavy work — it flares. {i}She clenches her fists.{/i} It's getting worse."
    jump act1_deep_nyx_the_physical_cost

label act1_deep_nyx_the_physical_cost:
    "{i}Nyx is quiet for a moment. She pulls up the sleeve of her left arm. In the low light, you can see it clearly now — a network of pale, luminescent lines beneath the skin, tracing from wrist to elbow like a map of rivers seen from orbit. Some of them pulse. Some of them flicker. A few have gone dark entirely.{/i}"
    jump act1_deep_nyx_nyx_shows_damage

label act1_deep_nyx_nyx_shows_damage:
    nyx "The Binding didn't just open my lattice pathways. It fused them to my nervous system. Permanently. {i}She traces a dark line on her forearm.{/i} These are the ones that have burned out. Dead channels. They don't come back."
    jump act1_deep_nyx_avyanna_cost_reaction

label act1_deep_nyx_avyanna_cost_reaction:
    avyanna "{i}My stomach drops.{/i} Burned out? Nyx, what does that mean for you?"
    jump act1_deep_nyx_nyx_clinical_cost

label act1_deep_nyx_nyx_clinical_cost:
    nyx "{i}Clinical. Detached. The way she talks about things too painful to feel.{/i} Nerve damage, eventually. Loss of fine motor control. Chronic pain that escalates over time. And at some point, when enough pathways burn out, I won't be able to do lattice work at all. {i}A pause.{/i} Or move my hands. Whichever comes first."
    jump act1_deep_nyx_choice_cost_response

label act1_deep_nyx_choice_cost_response:
    if game_state.has_flag("nyx_shard_soothed"):
        "{i}Your hands are still touching hers. The shard pulses — distress, determination. It understood what Nyx just said. And it wants to help. Desperately.{/i}"
    else:
        "{i}The maintenance deck feels colder. The hum of the engines sounds like a funeral dirge. Nyx is telling you she's dying — slowly, by inches, every time she uses the gift that was forced on her.{/i}"
    menu:
        "'Is there a way to stop it? Reverse it?'":
            jump act1_deep_nyx_ask_reversal
        "'How long? How much time do you have?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_timeline
        "'Does anyone else on the crew know?'":
            jump act1_deep_nyx_ask_who_knows

label act1_deep_nyx_ask_reversal:
    avyanna "Is there a way to stop it? Reverse the damage?"
    jump act1_deep_nyx_nyx_reversal_answer

label act1_deep_nyx_nyx_reversal_answer:
    nyx "{i}A thin smile.{/i} In theory? The Order claims to have stabilization techniques. Rituals that slow the degradation. {i}The smile fades.{/i} But those require returning to the Spire. Submitting to their authority again. And I suspect their 'stabilization' comes with... conditions."
    jump act1_deep_nyx_nyx_alternative

label act1_deep_nyx_nyx_alternative:
    nyx "I've been researching alternatives. Herbs — certain compounds that dampen lattice conductivity. Crystals that can absorb excess resonance. {i}She gestures to a small alcove you hadn't noticed, tucked behind a bulkhead panel. Inside: dried herb bundles, pale crystals arranged in careful geometric patterns, and a notebook filled with dense, tiny handwriting.{/i} My medbay. Such as it is."
    jump act1_deep_nyx_avyanna_sees_alcove

label act1_deep_nyx_avyanna_sees_alcove:
    avyanna "{i}I look at the alcove — the careful arrangement, the worn edges of the notebook, the crystals placed with obsessive precision. This isn't new. Nyx has been managing this alone for years.{/i} How long have you been doing this?"
    jump act1_deep_nyx_nyx_alcove_answer

label act1_deep_nyx_nyx_alcove_answer:
    nyx "Since the second year. When the tremors started. {i}She holds out a hand, palm up, and you can see it — a faint tremor in her fingers. Barely perceptible unless you're looking.{/i} The herbs help. The crystals absorb some of the bleed. It's not a cure. It's... management."
    jump act1_deep_nyx_ask_timeline_merge

label act1_deep_nyx_ask_timeline:
    avyanna "How long? How much time do you have before it —"
    jump act1_deep_nyx_nyx_timeline

label act1_deep_nyx_nyx_timeline:
    nyx "{i}She looks at you steadily.{/i} At the current rate of degradation? If I stop all lattice work entirely, maybe fifteen years before the nerve damage becomes debilitating. {i}A pause.{/i} If I keep working at this pace — reinforcing the ship, shielding the crew, training you — five. Maybe seven."
    jump act1_deep_nyx_avyanna_timeline_horror

label act1_deep_nyx_avyanna_timeline_horror:
    avyanna "{i}Five years. Seven at most. The number lands like a physical blow.{/i} Nyx..."
    jump act1_deep_nyx_nyx_pragmatic

label act1_deep_nyx_nyx_pragmatic:
    nyx "{i}Measured. Pragmatic. The tone of someone who's had this conversation with themselves a thousand times.{/i} I made the calculation. The crew needs the lattice work. The ship needs it. If I stop, people die — just more slowly. {i}A thin smile.{/i} I chose the faster burn and the living crew."
    jump act1_deep_nyx_ask_timeline_merge

label act1_deep_nyx_ask_who_knows:
    avyanna "Does anyone else know? About the degradation?"
    jump act1_deep_nyx_nyx_who_knows

label act1_deep_nyx_nyx_who_knows:
    nyx "Elisira suspects. She's noticed the tremors. Asked me about them once — I deflected. {i}A pause.{/i} Rho has seen my alcove. They think it's religious paraphernalia. I haven't corrected them."
    jump act1_deep_nyx_nyx_who_knows_cont

label act1_deep_nyx_nyx_who_knows_cont:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Quieter.{/i} You're the first person I've told. The full truth. {i}She looks at you, and there's something naked in her expression — trust, freely given, for perhaps the first time since she left the Spire.{/i} I don't know why tonight. Maybe the anniversary. Maybe you."
    jump act1_deep_nyx_ask_timeline_merge

label act1_deep_nyx_ask_timeline_merge:
    "{i}The weight of what Nyx has shared settles between you. The alcove with its herbs and crystals. The tremors. The countdown she carries in silence. But Nyx straightens slightly, some of the old composure returning — not as a wall, but as scaffolding. She has more to say.{/i}"
    jump act1_deep_nyx_nyx_escape_intro

label act1_deep_nyx_nyx_escape_intro:
    nyx "{i}She pulls her sleeve back down, hiding the lattice lines.{/i} You asked what it was like inside. I should tell you what it was like getting out."
    jump act1_deep_nyx_choice_escape_approach

label act1_deep_nyx_choice_escape_approach:
    "{i}Nyx's jaw is set. This is the part of the story she's been circling — the escape. The night she ran.{/i}"
    menu:
        "'Tell me. I want to understand.'":
            jump act1_deep_nyx_nyx_escape_begins
        "[Insight DC 14] 'There was someone else, wasn't there? Someone who helped you escape.'":
            $ _sc_result = skill_check("insight", 14, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_nyx_insight_helper_success
            else:
                jump act1_deep_nyx_insight_helper_failure

label act1_deep_nyx_nyx_escape_begins:
    nyx "It was a rest-night. Third bell. The Spire runs on strict schedules — everyone asleep by second bell, waking at fourth. That two-bell window was all I had. {i}Her voice is low, rhythmic, like she's reliving it.{/i} I'd been planning for weeks. Smuggling supplies into a maintenance shaft. A change of clothes. Shoes. You don't realize how important shoes are until you don't have them."
    jump act1_deep_nyx_nyx_escape_tunnel

label act1_deep_nyx_nyx_escape_tunnel:
    nyx "The Spire's lattice network is its security system. Every doorway, every corridor — warded. Monitored. {i}A grim smile.{/i} But I was a Resonance Theorist. I knew the patterns better than the people who built them. I'd found a blind spot — a maintenance tunnel where the lattice strands had decayed."
    jump act1_deep_nyx_nyx_escape_help

label act1_deep_nyx_nyx_escape_help:
    nyx "{i}Her voice catches.{/i} I didn't do it alone. There was someone — another theorist. Archivist Maren. She was older. Had been Writbound for twenty years. She'd seen what the Order was becoming and couldn't leave herself. Too deep. Too far gone. The Binding had her too thoroughly. {i}A pause heavy with grief.{/i} But she could help me leave."
    jump act1_deep_nyx_nyx_escape_maren

label act1_deep_nyx_nyx_escape_maren:
    nyx "Maren disabled the corridor wards for exactly ninety seconds. She told me to run and not look back. Told me she'd cover my absence until morning. {i}Her voice is barely audible.{/i} I asked her to come with me. She said her lattice was too degraded. That she'd die within a month outside the Spire's stabilization fields."
    jump act1_deep_nyx_nyx_escape_running

label act1_deep_nyx_nyx_escape_running:
    nyx "So I ran. Through the tunnel, out through a drainage shaft, into the city. Barefoot, terrified, carrying a bag of stolen research and borrowed clothes. {i}She closes her eyes.{/i} I heard the alarm go off when I was six blocks away. The sound of the Spire's resonance bells — I still hear them sometimes. In dreams."
    jump act1_deep_nyx_choice_maren_response

label act1_deep_nyx_choice_maren_response:
    "{i}Maren. A woman who couldn't save herself but chose to save someone else. The kind of sacrifice that leaves a debt you can never repay.{/i}"
    menu:
        "'What happened to Maren?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_about_maren
        "'She gave you your life back. That was her choice — and it was a good one.'":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_honor_maren
        "'Do you think they punished her? For helping you?'":
            jump act1_deep_nyx_ask_maren_punishment

label act1_deep_nyx_ask_about_maren:
    avyanna "What happened to Maren? After you left?"
    jump act1_deep_nyx_nyx_maren_fate

label act1_deep_nyx_nyx_maren_fate:
    nyx "{i}A long silence. Her hands glow brighter — stress response.{/i} I don't know. {i}The words come out tight, controlled.{/i} I tried to find out. For years. Sent messages through back channels, bribed information brokers. Nothing. The Order is very good at making people disappear. {i}Quieter.{/i} She might be dead. She might be edited — her memories of me erased, her personality rewritten into compliance. I don't know which is worse."
    jump act1_deep_nyx_nyx_maren_guilt

label act1_deep_nyx_nyx_maren_guilt:
    nyx "She's one of the gaps. One of the memory holes. I know she existed because I wrote her name down — forced myself to remember before they could take it. But her face... {i}She presses her fingers to her temples.{/i} It's blurred. Like looking through frosted glass. They took the details. Left just enough to hurt."
    jump act1_deep_nyx_the_anniversary_bridge

label act1_deep_nyx_honor_maren:
    avyanna "She gave you your life back. That was her choice — a conscious, deliberate act of love. Don't carry guilt for someone else's courage."
    jump act1_deep_nyx_nyx_maren_tears

label act1_deep_nyx_nyx_maren_tears:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Her composure shatters. Tears — real, unguarded tears — track down her face. Her hands glow bright enough to cast shadows on the deck plating.{/i} She... {i}A ragged breath.{/i} She used to call me little resonance. Said I vibrated with potential. Said I was the best argument she'd ever seen for the Order being wrong."
    jump act1_deep_nyx_nyx_maren_recovery

label act1_deep_nyx_nyx_maren_recovery:
    nyx "{i}She wipes her eyes with the back of her glowing hand, leaving faint trails of light on her skin.{/i} I can't even remember her face clearly anymore. They took that. But they couldn't take what she meant. {i}Steadier.{/i} I carry her forward. In my work. In how I choose to use what the Order taught me."
    jump act1_deep_nyx_the_anniversary_bridge

label act1_deep_nyx_ask_maren_punishment:
    avyanna "Do you think they punished her? For helping you escape?"
    jump act1_deep_nyx_nyx_maren_punishment

label act1_deep_nyx_nyx_maren_punishment:
    nyx "{i}Her jaw tightens. The glow in her hands flares, then dims as she forces control.{/i} The Order doesn't punish. They correct. {i}The word drips with venom.{/i} If they caught her, they would have edited her. Removed the compassion that made her help me. Made her loyal. Compliant. A better servant."
    jump act1_deep_nyx_nyx_maren_worse

label act1_deep_nyx_nyx_maren_worse:
    nyx "That's worse than death. That's erasing someone while leaving their body walking around. A puppet wearing a friend's face. {i}She meets your eyes.{/i} That's what I ran from. That's what they would have done to me."
    jump act1_deep_nyx_the_anniversary_bridge

label act1_deep_nyx_insight_helper_success:
    avyanna "There was someone else, wasn't there? Someone who helped you get out. You couldn't have done it alone — not against their wards."
    jump act1_deep_nyx_nyx_insight_stunned

label act1_deep_nyx_nyx_insight_stunned:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "{i}She stares at you, startled.{/i} How did you... {i}A breath.{/i} Yes. Her name was Maren. Archivist Maren. She'd been Writbound for twenty years."
    jump act1_deep_nyx_nyx_escape_maren

label act1_deep_nyx_insight_helper_failure:
    avyanna "There was someone else, wasn't there? Someone who helped you?"
    jump act1_deep_nyx_nyx_deflects_helper

label act1_deep_nyx_nyx_deflects_helper:
    nyx "{i}A flicker of something — surprise, guardedness — passes over her face.{/i} What makes you say that?"
    jump act1_deep_nyx_avyanna_intuition

label act1_deep_nyx_avyanna_intuition:
    avyanna "Just a feeling. The way you talk about it — there's grief for someone specific."
    jump act1_deep_nyx_nyx_escape_begins

label act1_deep_nyx_insight_hands_success:
    "{i}You study Nyx's hands — really study them. The glow isn't decorative or incidental. It pulses in rhythm with her breathing, brighter when she's tense, dimmer when she calms. And the dark lines threading beneath the skin... those aren't veins. They're dead channels. Burned-out pathways. Whatever Nyx's magic is, it's consuming her from the inside.{/i}"
    jump act1_deep_nyx_avyanna_notices_hands

label act1_deep_nyx_avyanna_notices_hands:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    avyanna "Your hands. The glow — it's not just residue from the lattice work. It's permanent. And those dark lines... {i}Quietly.{/i} Nyx, what's happening to you?"
    jump act1_deep_nyx_nyx_caught_hands

label act1_deep_nyx_nyx_caught_hands:
    nyx "{i}She looks down at her hands, startled — as if she'd forgotten someone might notice. Then a long, tired exhalation.{/i} You're more perceptive than I gave you credit for. {i}She flexes her fingers, and the glow flares, then fades.{/i} It's called lattice degradation. A gift from the Writbound Order. Let me tell you about it."
    jump act1_deep_nyx_nyx_describes_order

label act1_deep_nyx_insight_hands_failure:
    "{i}You watch her hands, trying to read the glow, but Nyx notices your attention and tucks her hands into her sleeves — a practiced gesture. Whatever you almost saw, she's hidden it.{/i}"
    jump act1_deep_nyx_avyanna_hands_miss

label act1_deep_nyx_avyanna_hands_miss:
    avyanna "Your hands were glowing. Is that normal? From the lattice work?"
    jump act1_deep_nyx_nyx_hands_deflect

label act1_deep_nyx_nyx_hands_deflect:
    nyx "{i}A practiced shrug.{/i} Residual resonance. It fades. {i}But her hands stay hidden, and her jaw is tight.{/i} It's nothing to worry about."
    jump act1_deep_nyx_ask_inside_order

label act1_deep_nyx_offer_stop_order:
    avyanna "You don't have to keep going. We can stop here. You've already shared so much."
    jump act1_deep_nyx_nyx_needs_to_continue

label act1_deep_nyx_nyx_needs_to_continue:
    nyx "{i}She shakes her head.{/i} No. I've been carrying this alone for seven years. Silence hasn't made it lighter. {i}She looks at you with something fragile and resolute.{/i} I want you to know. All of it. If we're going to trust each other — really trust each other — you deserve the truth."
    jump act1_deep_nyx_nyx_describes_order

label act1_deep_nyx_the_anniversary_bridge:
    "{i}The maintenance deck is quieter now. Even the engine hum seems muted, as if the ship itself is listening. Nyx sits with her back against the bulkhead, the faint lattice-glow in her hands pulsing slowly, like a heartbeat. Seven years. Tonight marks seven years since she ran through a drainage shaft in stolen shoes.{/i}"
    jump act1_deep_nyx_nyx_anniversary

label act1_deep_nyx_nyx_anniversary:
    nyx "Seven years. {i}She says it like testing a wound.{/i} Every year I tell myself it'll be the last time I count. That I'll stop marking the date. Move forward. {i}A thin, self-aware smile.{/i} Every year I'm wrong."
    jump act1_deep_nyx_nyx_anniversary_ritual

label act1_deep_nyx_nyx_anniversary_ritual:
    nyx "I have a ritual. Every anniversary, I come to the lowest part of whatever ship or station I'm on and I do maintenance work. The most thankless, invisible labor I can find. Hull reinforcement. Waste system calibration. Lattice repair in places no one will ever see."
    jump act1_deep_nyx_avyanna_asks_why_ritual

label act1_deep_nyx_avyanna_asks_why_ritual:
    avyanna "Why? As penance?"
    jump act1_deep_nyx_nyx_explains_ritual

label act1_deep_nyx_nyx_explains_ritual:
    nyx "{i}She considers this.{/i} Partly. But mostly because the Order valued spectacle. Grand rituals, beautiful architecture, public demonstrations of power. Everything they did was designed to be seen. To impress. To control through awe. {i}She runs a hand along the rough bulkhead.{/i} This is the opposite. Work that matters because it's needed, not because anyone will applaud."
    jump act1_deep_nyx_nyx_anniversary_meaning

label act1_deep_nyx_nyx_anniversary_meaning:
    nyx "Seven years of freedom. Seven years of choosing what to do with hands that were trained for violation. {i}Her voice is measured but raw underneath.{/i} Some years it feels like an achievement. Other years it feels like I'm still running. Like the Spire is just beyond the next bulkhead, waiting."
    jump act1_deep_nyx_choice_anniversary

label act1_deep_nyx_choice_anniversary:
    "{i}The anniversary. Not a celebration, not quite a mourning. Something in between — a reckoning. You can feel how much this night costs Nyx. The careful composure, the clinical recitation, the moments where emotion breaks through like light through cracked glass.{/i}"
    menu:
        "'Seven years of choosing. That's not running — that's living.'":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_reframe_anniversary
        "'What would you tell the version of yourself who ran? If you could go back?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_past_self
        "'Maybe the counting is okay. It means you remember. And remembering matters.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_validate_counting

label act1_deep_nyx_reframe_anniversary:
    avyanna "Seven years of choosing. Every single day, you've chosen who to be. What to do with your hands and your knowledge and your time. That's not running. That's living."
    jump act1_deep_nyx_nyx_reframe_response

label act1_deep_nyx_nyx_reframe_response:
    nyx "{i}She goes very still. The glow in her hands dims to almost nothing — the closest thing to calm you've seen from her tonight.{/i} Living. {i}She repeats it like she's tasting the word, finding it strange.{/i} I've been so focused on what I left that I forgot to name what I have."
    jump act1_deep_nyx_nyx_looks_around

label act1_deep_nyx_nyx_looks_around:
    nyx "{i}She looks around the maintenance deck — the tools, the lattice-glass crystals in her alcove, the worn bulkheads she's been quietly reinforcing for months.{/i} A crew that trusts me. Work that matters. Someone sitting beside me on the worst night of my year, listening without flinching. {i}She looks at you.{/i} That's not nothing."
    jump act1_deep_nyx_bee_fear_transition

label act1_deep_nyx_ask_past_self:
    avyanna "What would you tell the version of yourself who ran? If you could go back to that drainage shaft and speak to her?"
    jump act1_deep_nyx_nyx_past_self

label act1_deep_nyx_nyx_past_self:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}A long silence. When she speaks, her voice is rough.{/i} I'd tell her it's going to hurt. For a long time. That freedom isn't the same as safety, and autonomy comes with a weight the Order never prepared you for. {i}A pause.{/i} And I'd tell her to keep running. That in seven years, she'll be sitting on a maintenance deck with someone who sees her — really sees her — and it will be worth every scar."
    jump act1_deep_nyx_bee_fear_transition

label act1_deep_nyx_validate_counting:
    avyanna "Maybe the counting is okay. Maybe it means you remember what you survived and what it cost. Forgetting would be easier, but remembering... that's brave."
    jump act1_deep_nyx_nyx_counting_response

label act1_deep_nyx_nyx_counting_response:
    nyx "{i}A breath of laughter — genuine, surprised.{/i} Brave. I've never thought of it as brave. I always thought it was weakness. An inability to let go. {i}She looks at her hands, the faint tremor, the dying glow.{/i} But maybe you're right. Maybe remembering is its own kind of courage."
    jump act1_deep_nyx_bee_fear_transition

label act1_deep_nyx_bee_fear_transition:
    if game_state.has_flag("bee_revealed"):
        "{i}Bee pulses once — bright, insistent. It has something to communicate. And Nyx sees it, the glow through your shirt, and her face goes pale.{/i}"
    else:
        "{i}Something shifts in the air. The shard in your chest — Bee — stirs. Not in alarm, but in recognition. It has been listening. Understanding more than you realized. And Nyx senses it. Her eyes fix on your chest, where the shard rests, and her expression changes. Fear. Clear, undisguised fear.{/i}"
    jump act1_deep_nyx_nyx_sees_bee

label act1_deep_nyx_nyx_sees_bee:
    nyx "{i}Staring at your chest, where the shard's faint glow pulses beneath your clothing.{/i} It's listening. Your shard — Bee. It's been listening this whole time."
    jump act1_deep_nyx_avyanna_confirms_bee

label act1_deep_nyx_avyanna_confirms_bee:
    avyanna "Yes. It... understands, I think. It's been quiet. Respectful. But it's paying attention."
    jump act1_deep_nyx_nyx_bee_fear

label act1_deep_nyx_nyx_bee_fear:
    nyx "{i}She draws back slightly. The fear in her eyes is sharp, immediate.{/i} Avyanna... do you understand what Bee is? What it's doing to you?"
    jump act1_deep_nyx_choice_bee_challenge

label act1_deep_nyx_choice_bee_challenge:
    "{i}Nyx's fear is real. Not of Bee specifically, but of what Bee represents — something bound to you, changing you, expanding your capabilities at a cost you might not fully understand. Parallels to her own story that are impossible to ignore.{/i}"
    menu:
        "'It's different. Bee chose me. I chose Bee. There was consent.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_defend_bee_consent
        "'You see parallels. Between your Binding and Bee.'":
            jump act1_deep_nyx_acknowledge_parallel
        "[Empathy DC 16] 'You're afraid for me. Not of Bee — for me.'":
            $ _sc_result = skill_check("empathy", 16, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_nyx_empathy_bee_success
            else:
                jump act1_deep_nyx_empathy_bee_failure

label act1_deep_nyx_defend_bee_consent:
    avyanna "It's different. Bee chose me. I chose Bee. There was consent. Nobody forced this."
    jump act1_deep_nyx_nyx_bee_counter

label act1_deep_nyx_nyx_bee_counter:
    nyx "{i}She holds up a hand — not dismissing, but asking you to hear her.{/i} I know. I know it feels different. And maybe it is. But Avyanna — {i}She leans forward, intense.{/i} I was fifteen and I thought I chose the Order freely. I was wrong. Sometimes we consent to things we don't fully understand. And by the time we understand... {i}She touches the dark lines on her arm.{/i} It's too late to unchoose."
    jump act1_deep_nyx_nyx_bee_specific_fear

label act1_deep_nyx_acknowledge_parallel:
    avyanna "You see parallels. Between your Binding and what Bee is doing to me."
    jump act1_deep_nyx_nyx_parallel_confirm

label act1_deep_nyx_nyx_parallel_confirm:
    nyx "{i}A sharp nod.{/i} Yes. A foreign presence bound to your lattice, expanding your capabilities, changing your perception. Power that comes with a cost you can't fully quantify yet. {i}Her voice is tight with restrained fear.{/i} The mechanism is different. The dynamic might be different. But the shape of it — Avyanna, the shape of it is the same."
    jump act1_deep_nyx_nyx_bee_specific_fear

label act1_deep_nyx_empathy_bee_success:
    avyanna "You're afraid for me. Not of Bee — for me. Because you see yourself."
    jump act1_deep_nyx_nyx_bee_raw

label act1_deep_nyx_nyx_bee_raw:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "{i}The fear in her eyes turns to something rawer. Her hands glow bright — stress, pain, old terror.{/i} Yes. Yes. I look at you and I see myself at fifteen, bonded to something I didn't understand, told it was a gift, told I was special. And seven years later I'm sitting on a maintenance deck with dead nerves in my arms and holes in my memory. {i}Her voice breaks.{/i} I can't watch that happen to you. I won't."
    jump act1_deep_nyx_nyx_bee_specific_fear

label act1_deep_nyx_empathy_bee_failure:
    avyanna "You're worried about Bee. About what it's doing."
    jump act1_deep_nyx_nyx_bee_correction

label act1_deep_nyx_nyx_bee_correction:
    nyx "{i}Sharper than she intended.{/i} I'm worried about you. The shard is a variable, an unknown. But you — you're someone I — {i}She stops, recalibrates.{/i} You matter. To the crew. To the mission. To me. And I've seen what unchecked lattice bonding does to a person."
    jump act1_deep_nyx_nyx_bee_specific_fear

label act1_deep_nyx_nyx_bee_specific_fear:
    nyx "I watch you, Avyanna. I see the shard's influence growing — your perception sharpening, your lattice sensitivity expanding. You're becoming something more. But more always has a cost. {i}She holds up her trembling hand.{/i} This is what more looks like, eventually."
    jump act1_deep_nyx_choice_bee_resolution

label act1_deep_nyx_choice_bee_resolution:
    "{i}Nyx is terrified — not in the abstract way of theoretical concern, but in the visceral way of someone who has lived the consequences. She's asking you to take this seriously. To recognize the danger in the gift.{/i}"
    menu:
        "'Then help me. Monitor me. If you see me changing — really changing — tell me.'":
            $ game_state.set_flag("nyx_bee_watchguard")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_ask_nyx_monitor
        "'Bee isn't the Order. But you're right — I need to be careful. We both do.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_careful_agreement
        "'I hear you. But I trust Bee. And I trust myself. Can you trust me on this?'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_trust

label act1_deep_nyx_ask_nyx_monitor:
    avyanna "Then help me. Be my watchguard. Monitor what Bee is doing — you understand lattice bonding better than anyone. If you see me changing, losing myself, becoming something I wouldn't choose — tell me. Stop me."
    jump act1_deep_nyx_nyx_monitor_accept

label act1_deep_nyx_nyx_monitor_accept:
    nyx "{i}The fear in her expression doesn't disappear, but something else joins it — purpose. Relief. A role she understands, one that transforms helpless worry into active protection.{/i} Yes. I can do that. I will do that. {i}She meets your eyes.{/i} And you'll listen? If I raise concerns? You won't dismiss them?"
    jump act1_deep_nyx_avyanna_promises

label act1_deep_nyx_avyanna_promises:
    avyanna "I promise. No dismissals. If you see something, I listen. Full stop."
    jump act1_deep_nyx_nyx_watchguard_seal

label act1_deep_nyx_nyx_watchguard_seal:
    nyx "{i}A breath she's been holding for what feels like hours finally releases.{/i} Thank you. {i}A small, fragile smile.{/i} Maren was my watchguard. Once. Before the Order took that from her. I'll do better. I'll do it right."
    jump act1_deep_nyx_teaching_transition

label act1_deep_nyx_careful_agreement:
    avyanna "Bee isn't the Order. The circumstances are different, the relationship is different. But you're right — I need to be careful. We both do. I won't be reckless with this."
    jump act1_deep_nyx_nyx_careful_nod

label act1_deep_nyx_nyx_careful_nod:
    nyx "{i}She nods slowly.{/i} Careful is good. Careful I can work with. {i}A pause.{/i} I'll help you understand what's happening — the lattice changes, the bonding progression. Knowledge is better than ignorance. The Order taught me that much, at least."
    jump act1_deep_nyx_teaching_transition

label act1_deep_nyx_ask_trust:
    avyanna "I hear you. Your fear is valid and I respect it. But I trust Bee. And I trust myself. Can you trust me on this? Even when it scares you?"
    jump act1_deep_nyx_nyx_trust_struggle

label act1_deep_nyx_nyx_trust_struggle:
    nyx "{i}A long silence. She wrestles with it visibly — fear against respect, protectiveness against autonomy. Finally:{/i} I trust you. {i}Carefully.{/i} I don't trust the situation. But I trust you. And I'll... try to separate the two."
    jump act1_deep_nyx_nyx_trust_condition

label act1_deep_nyx_nyx_trust_condition:
    nyx "But Avyanna — if I see something, I will say something. Not as judgment. Not as control. As someone who cares about you and has seen what unchecked bonding does. {i}Quieter.{/i} Promise me you'll hear me out when that happens."
    jump act1_deep_nyx_avyanna_trust_promise

label act1_deep_nyx_avyanna_trust_promise:
    avyanna "I promise."
    jump act1_deep_nyx_teaching_transition

label act1_deep_nyx_teaching_transition:
    "{i}Something has shifted between you. The fear isn't gone, but it's shared now — carried together instead of borne alone. Nyx straightens, and a new energy enters her posture. Not clinical distance, but focused intention. The theorist emerging from behind the wounded person.{/i}"
    jump act1_deep_nyx_nyx_teaching_offer

label act1_deep_nyx_nyx_teaching_offer:
    nyx "{i}She stands, offering you a hand up.{/i} Since we're both awake and I've thoroughly ruined the mood for sleep — {i}A trace of her usual dry humor.{/i} — let me show you something. Something real about the lattice. Not theory. Practice."
    jump act1_deep_nyx_choice_teaching

label act1_deep_nyx_choice_teaching:
    "{i}Nyx is offering a gift — not just knowledge, but trust. Teaching you the thing that was used to hurt her. Choosing to transform violation into education.{/i}"
    menu:
        "'Yes. Show me.'":
            jump act1_deep_nyx_teaching_begins
        "'Are you sure? After everything tonight — you should rest.'":
            jump act1_deep_nyx_concern_for_nyx

label act1_deep_nyx_teaching_begins:
    avyanna "Yes. Show me."
    jump act1_deep_nyx_nyx_teaching_setup

label act1_deep_nyx_concern_for_nyx:
    avyanna "Are you sure? You've been doing lattice work all night. And after everything you've told me — you should rest."
    jump act1_deep_nyx_nyx_teaching_insists

label act1_deep_nyx_nyx_teaching_insists:
    nyx "{i}That small, rare smile again.{/i} This isn't work. This is... {i}She searches for the word.{/i} This is the part that doesn't hurt. Teaching someone who wants to learn. Freely. Without coercion. {i}A breath.{/i} Let me have this. Please."
    jump act1_deep_nyx_nyx_teaching_setup

label act1_deep_nyx_nyx_teaching_setup:
    "{i}Nyx moves to the alcove — her hidden medbay. She selects a crystal, pale blue and roughly the size of a thumb, and a bundle of dried herbs that smell of ozone and sage. She places these on the deck between you, then sits cross-legged, facing you. The maintenance deck becomes a ritual space — improvised, intimate, real.{/i}"
    jump act1_deep_nyx_nyx_teaching_crystal

label act1_deep_nyx_nyx_teaching_crystal:
    nyx "{i}Holding up the crystal.{/i} Lattice-glass. It stores resonance patterns — like a battery for reality's underlying structure. The Order used them for memory extraction. I use them for... this. {i}She places it between you both, and it begins to glow softly.{/i} Close your eyes. Put your hands on either side of the crystal. Don't touch it — just feel."
    jump act1_deep_nyx_avyanna_tries

label act1_deep_nyx_avyanna_tries:
    avyanna "{i}I close my eyes. My hands hover around the crystal. At first, nothing. Then —{/i}"
    jump act1_deep_nyx_lattice_sensation

label act1_deep_nyx_lattice_sensation:
    "{i}The world opens. Not visually — something deeper. You feel the lattice. Not as an abstraction but as a living presence. Threads of connection running through everything — the deck, the walls, the air, you, Nyx. The crystal amplifies your perception, and suddenly you can sense the ship as a single, breathing entity. Every weld, every rivet, every person sleeping in their bunks. All connected. All part of the pattern.{/i}"
    jump act1_deep_nyx_avyanna_overwhelmed

label act1_deep_nyx_avyanna_overwhelmed:
    avyanna "{i}My breath catches.{/i} I can feel... everything. The crew. Jalen dreaming. Elisira reading. Rho... Rho is awake too, in the engine room."
    jump act1_deep_nyx_nyx_guides

label act1_deep_nyx_nyx_guides:
    nyx "{i}Her voice is steady, guiding. The teacher, not the victim.{/i} Good. Now — feel the connections between them. Not the people themselves, but the bonds. The lattice threads that tie us together. See how they're woven?"
    jump act1_deep_nyx_avyanna_sees_bonds

label act1_deep_nyx_avyanna_sees_bonds:
    avyanna "{i}I can see them — feel them — threads of light and meaning running between every person on the ship. Some thick and warm, others thin and fragile. Some frayed. Some new.{/i} They're beautiful. But some of them are... damaged?"
    jump act1_deep_nyx_nyx_explains_damage

label act1_deep_nyx_nyx_explains_damage:
    nyx "Damage is natural. Relationships strain. Trust breaks. People hurt each other. {i}She pauses.{/i} But look closer. At the damaged threads. What do you see at the edges?"
    jump act1_deep_nyx_avyanna_sees_repair

label act1_deep_nyx_avyanna_sees_repair:
    avyanna "{i}I look — feel — and there it is. At the frayed edges of damaged connections: tiny, deliberate stitches of light. Repairs.{/i} Someone's been fixing them. The damaged bonds. Stitching them back together."
    jump act1_deep_nyx_nyx_admits_repairs

label act1_deep_nyx_nyx_admits_repairs:
    nyx "{i}Quiet.{/i} Yes. {i}A pause.{/i} That's me. That's what I do. When the crew fights, when trust fractures, when someone is hurting and pulling away — I reinforce the lattice between them. Gently. Without anyone knowing. {i}She looks down.{/i} It's the opposite of what the Order trained me for. And it costs me every time."
    jump act1_deep_nyx_choice_teaching_response

label act1_deep_nyx_choice_teaching_response:
    "{i}You can feel it now — Nyx's presence in the lattice. Not controlling, not dominating, but tending. Like a gardener in a web of light. Every stitch costs her a flicker of her fading pathways, and she does it anyway. Quietly. Without asking for gratitude.{/i}"
    menu:
        "'You're holding us together. Literally. Nyx — that's extraordinary.'":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_honor_the_work
        "'Let me help. Teach me to do this. Share the cost.'":
            $ game_state.set_flag("nyx_lattice_training")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_offer_share_cost
        "'Does the crew know? That you're spending yourself for them?'":
            jump act1_deep_nyx_ask_crew_knowledge

label act1_deep_nyx_honor_the_work:
    avyanna "You're holding us together. Literally. Every day, without anyone knowing, you're spending yourself to keep us whole. {i}My voice is thick.{/i} That's extraordinary, Nyx."
    jump act1_deep_nyx_nyx_dismisses_gently

label act1_deep_nyx_nyx_dismisses_gently:
    nyx "{i}She shakes her head, but she's smiling — not the bitter smile, not the deflecting one, but something genuine.{/i} It's just work. Someone has to do it. {i}But her eyes are bright.{/i} Though it's... nice. Being seen doing it. Even once."
    jump act1_deep_nyx_resolution_bridge

label act1_deep_nyx_offer_share_cost:
    avyanna "Then let me help. Teach me to do this — the mending, the reinforcement. If Bee and I can share the cost, maybe it slows your degradation. Maybe we carry it together."
    jump act1_deep_nyx_nyx_considers_sharing

label act1_deep_nyx_nyx_considers_sharing:
    nyx "{i}Her expression cycles through surprise, calculation, hope, and fear in rapid succession.{/i} The shard might actually... {i}She looks at the crystal between you, still glowing, then at you.{/i} It would be dangerous. You'd be taking on lattice stress your body wasn't built for. But with Bee as a buffer... {i}A breath.{/i} It could work. It might actually work."
    jump act1_deep_nyx_nyx_agrees_sharing

label act1_deep_nyx_nyx_agrees_sharing:
    nyx "We'll start slow. Meditation and sensing first, then basic reinforcement. I'll monitor your lattice pathways — watch for degradation. {i}Firm.{/i} If I see any damage, we stop. No arguments. Agreed?"
    jump act1_deep_nyx_avyanna_agrees_sharing

label act1_deep_nyx_avyanna_agrees_sharing:
    avyanna "Agreed. No arguments."
    jump act1_deep_nyx_resolution_bridge

label act1_deep_nyx_ask_crew_knowledge:
    avyanna "Does the crew know? That you're spending yourself for them? Burning out your pathways to keep everyone connected?"
    jump act1_deep_nyx_nyx_crew_answer

label act1_deep_nyx_nyx_crew_answer:
    nyx "{i}A soft laugh.{/i} No. And I'd prefer they didn't. {i}She sees your expression and holds up a hand.{/i} Not out of secrecy. Out of... {i}She searches for the word.{/i} Respect. If they knew, they'd feel guilty. They'd try to stop me. Or worse — they'd treat me differently. Carefully. Like I'm fragile."
    jump act1_deep_nyx_nyx_crew_reason

label act1_deep_nyx_nyx_crew_reason:
    nyx "I'm not fragile. I'm choosing. Every stitch, every reinforcement — it's my choice. Mine. Not the Order's, not obligation's. Mine. {i}She looks at you steadily.{/i} That's the most important thing I took from the Spire. The right to choose what I spend myself on."
    jump act1_deep_nyx_resolution_bridge

label act1_deep_nyx_resolution_bridge:
    "{i}The crystal between you fades as the lattice perception gently recedes. The maintenance deck reasserts itself — steel, shadow, engine hum. But something has changed. The space between you and Nyx feels different. Denser. More real. A bond reinforced not by lattice manipulation but by truth, freely shared.{/i}"
    jump act1_deep_nyx_nyx_resolution_quiet

label act1_deep_nyx_nyx_resolution_quiet:
    nyx "{i}She gathers the crystal and herbs, returning them to the alcove with careful, practiced movements. When she turns back, her expression is open in a way you've never seen. Vulnerable, yes, but also resolved.{/i} Thank you. For staying. For listening. For not flinching."
    jump act1_deep_nyx_choice_resolution

label act1_deep_nyx_choice_resolution:
    "{i}The night is ending. Soon the ship will wake, and Nyx will rebuild her composure, settle back into the measured precision the crew knows. But this moment — this truth between you — will remain. Nyx has one more thing to offer. You can feel it.{/i}"
    menu:
        "'Thank you for trusting me. I know that wasn't easy.'":
            jump act1_deep_nyx_thank_trust
        "'Is there anything you need? Right now, tonight?'":
            jump act1_deep_nyx_ask_what_needed
        "'Next anniversary, you're not doing this alone. I'll be here.'":
            $ game_state.set_flag("nyx_anniversary_promise")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_promise_next_year

label act1_deep_nyx_thank_trust:
    avyanna "Thank you for trusting me. I know how much that cost you. I won't waste it."
    jump act1_deep_nyx_nyx_offers_ward

label act1_deep_nyx_ask_what_needed:
    avyanna "Is there anything you need? Right now, tonight?"
    jump act1_deep_nyx_nyx_needs_nothing

label act1_deep_nyx_nyx_needs_nothing:
    nyx "{i}She considers it. Honestly, openly, without deflection.{/i} This was enough. More than enough. {i}A breath.{/i} But there is something I want to give you. If you'll accept it."
    jump act1_deep_nyx_nyx_offers_ward

label act1_deep_nyx_promise_next_year:
    avyanna "Next anniversary, you're not doing this alone. I'll be here. Same deck, same hour. You're not carrying this by yourself anymore."
    jump act1_deep_nyx_nyx_next_year

label act1_deep_nyx_nyx_next_year:
    nyx "{i}Something in her breaks open — not in pain, but in relief. Like a door long shut swinging wide.{/i} You mean that. {i}Not a question. She can feel the truth of it in the lattice between you.{/i} I... {i}She closes her eyes.{/i} Thank you. Yes. I'd like that very much."
    jump act1_deep_nyx_nyx_offers_ward

label act1_deep_nyx_nyx_offers_ward:
    nyx "{i}She reaches into the alcove and produces a small crystal — not the teaching one, but something different. Darker, denser, with a faint inner light that pulses in time with her heartbeat.{/i} This is a ward-stone. I grew it from my own lattice resonance. It took three months."
    jump act1_deep_nyx_nyx_ward_explanation

label act1_deep_nyx_nyx_ward_explanation:
    nyx "If anyone tries to manipulate your lattice — edit your memories, alter your thoughts, control your mind — this will shatter. The resonance pulse will disrupt the attack. Buy you time to fight back. {i}She holds it out to you.{/i} I made it for... I was going to give it to you eventually. Tonight seems right."
    jump act1_deep_nyx_choice_ward

label act1_deep_nyx_choice_ward:
    "{i}The ward-stone rests in Nyx's palm, pulsing with her heartbeat. Three months of work. Part of her own fading lattice, given freely. This is the most personal thing Nyx could offer — a piece of herself, shaped into protection for you.{/i}"
    menu:
        "Accept the ward-stone. 'I'll carry it. Always.'":
            $ game_state.set_flag("nyx_ward_accepted")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_accept_ward
        "'Nyx — this is part of you. Part of your lattice. Are you sure?'":
            jump act1_deep_nyx_question_ward_cost

label act1_deep_nyx_accept_ward:
    avyanna "{i}I take it. The crystal is warm — body-warm — and the moment it touches my skin, I feel a resonance. Nyx's presence. Careful, precise, protective. A piece of her, entrusted to me.{/i} I'll carry it. Always."
    jump act1_deep_nyx_nyx_ward_final

label act1_deep_nyx_question_ward_cost:
    avyanna "Nyx — this is part of you. Part of your lattice. Given what you told me about degradation, about the pathways burning out — can you afford this?"
    jump act1_deep_nyx_nyx_ward_honest

label act1_deep_nyx_nyx_ward_honest:
    nyx "{i}She meets your eyes with absolute honesty.{/i} No. I probably can't. It cost me. {i}A pause.{/i} But keeping you safe is worth a few fewer years of fine motor control. That's my choice. Let me make it."
    jump act1_deep_nyx_avyanna_takes_ward

label act1_deep_nyx_avyanna_takes_ward:
    avyanna "{i}I take it carefully, reverently, understanding the weight of what she's given.{/i} I'll earn this. I promise."
    jump act1_deep_nyx_nyx_ward_final

label act1_deep_nyx_nyx_ward_final:
    nyx "{i}She watches you hold the ward-stone, and her expression holds something you've never seen in Nyx before: peace. Imperfect, temporary, fragile — but real.{/i} You already have. {i}Quietly.{/i} You already have."
    jump act1_deep_nyx_final_truth

label act1_deep_nyx_final_truth:
    "{i}The maintenance deck is silent except for the engines. The herbs in Nyx's alcove perfume the recycled air with ozone and sage. In a few hours, the ship will wake. Nyx will slip back behind her composure, her precision, her measured distance. But something fundamental has changed. A wall has come down, and neither of you will pretend it's still standing.{/i}"
    jump act1_deep_nyx_nyx_final_words

label act1_deep_nyx_nyx_final_words:
    nyx "{i}She leans back against the bulkhead, the tremor in her hands quiet for the first time tonight. The glow has faded to almost nothing.{/i} Avyanna? {i}Soft, almost too quiet to hear over the engines.{/i}"
    jump act1_deep_nyx_avyanna_final_listen

label act1_deep_nyx_avyanna_final_listen:
    avyanna "Yes?"
    jump act1_deep_nyx_nyx_final_confession

label act1_deep_nyx_nyx_final_confession:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "Seven years ago, I ran from people who wanted to own me. I've spent every day since then alone — choosing alone, working alone, burning alone. {i}A pause. When she speaks again, her voice is raw and certain.{/i} I don't want to be alone anymore. Not with you here. Not with this crew. {i}The barest trace of a smile.{/i} That's the most dangerous thing I've ever said."
    jump act1_deep_nyx_choice_final

label act1_deep_nyx_choice_final:
    "{i}The last confession. Not of guilt or trauma, but of want. Of hope. The most frightening thing a person who's been hurt can do — choose vulnerability again.{/i}"
    menu:
        "'You're not alone. Not anymore. That's a promise, not a platitude.'":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_final_promise
        "[Stay silent. Move closer. Let presence be the answer.]":
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_final_silence
        "'Dangerous is good. Dangerous means it matters.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_final_dangerous

label act1_deep_nyx_final_promise:
    avyanna "You're not alone. Not anymore. {i}I hold up the ward-stone — her heartbeat pulsing in my palm.{/i} That's a promise, not a platitude."
    jump act1_deep_nyx_final_scene

label act1_deep_nyx_final_silence:
    "{i}You don't speak. Words would be too much and not enough. Instead, you shift closer until your shoulder touches hers. The ward-stone glows between your hands. The shard hums — soft, warm, approving. The lattice between you strengthens on its own, without manipulation, without effort. Just two people choosing to be close.{/i}"
    jump act1_deep_nyx_final_scene

label act1_deep_nyx_final_dangerous:
    avyanna "Dangerous is good. Dangerous means it matters. {i}I catch her eye.{/i} And for the record — I don't want you alone either."
    jump act1_deep_nyx_final_scene

label act1_deep_nyx_final_scene:
    $ game_state.set_flag("deep_nyx_complete")
    "{i}The maintenance deck. Late cycle. Two people sitting against a bulkhead in the belly of a ship, surrounded by herbs and crystals and the hum of engines that sound, just for a moment, like singing. Nyx's hands are still. The tremor is quiet. The glow has faded. And for the first time in seven years, the anniversary doesn't end with Nyx alone in the dark.{/i}"
    return

label act1_deep_nyx_work_together:
    "{i}Nyx guides you through the basics — placing your hands on the bulkhead, sensing the stress patterns in the metal. The shard helps, feeding you intuition about where to focus. It's slow work, meditative. You fall into comfortable silence.{/i}"
    jump act1_deep_nyx_work_revelation

label act1_deep_nyx_work_revelation:
    nyx "{i}After a while, quietly.{/i} This is why I do it. Not the repairs — the connection. Feeling the ship respond. Knowing I'm helping. {i}A pause.{/i} It's the opposite of what the Writbound did. They took. This is giving."
    jump act1_deep_nyx_avyanna_questions_writbound

label act1_deep_nyx_avyanna_questions_writbound:
    avyanna "The Writbound? {i}Carefully, not pushing.{/i} You've never mentioned them before."
    jump act1_deep_nyx_nyx_freezes

label act1_deep_nyx_nyx_freezes:
    nyx "{i}Her hands still on the bulkhead. A long silence.{/i} No. I haven't. {i}Another pause, then quietly.{/i} Today's the anniversary. Seven years since I left."
    jump act1_deep_nyx_writbound_revealed

label act1_deep_nyx_choice_after_deflection:
    "{i}Nyx is shutting you out. You can push, or you can give her space. But pushing might be what she needs — someone who cares enough to see through the walls.{/i}"
    menu:
        "'Nyx, please. I'm not leaving. Talk to me.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_gentle_insistence
        "'Alright. But I'm here if you need me.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_respectful_distance

label act1_deep_nyx_gentle_insistence:
    avyanna "Nyx. Please. {i}I step closer.{/i} I'm not leaving. Whatever it is, you don't have to carry it alone."
    jump act1_deep_nyx_nyx_walls_crack

label act1_deep_nyx_nyx_walls_crack:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She stops, shoulders sagging slightly.{/i} You're persistent. {i}A long moment, then:{/i} Today's the anniversary. Seven years since I left the Writbound Order."
    jump act1_deep_nyx_writbound_revealed

label act1_deep_nyx_respectful_distance:
    avyanna "Alright. But I'm here if you need me. Anytime."
    jump act1_deep_nyx_nyx_appreciates

label act1_deep_nyx_nyx_appreciates:
    $ game_state.set_flag("deep_nyx_partial")
    nyx "{i}She glances at you, something grateful in her expression.{/i} Thank you. {i}She returns to the lattice work, but the tension has eased slightly.{/i} I'll remember that."
    return

label act1_deep_nyx_offer_training_path:
    nyx "{i}She's quiet for a moment, then looks at you with new determination.{/i} I want to teach you. Really teach you. Not just basic resonance awareness — deep lattice work. How to read the patterns. How to reinforce them. {i}A pause.{/i} How to protect yourself from manipulation like what was done to me."
    jump act1_deep_nyx_avyanna_surprised

label act1_deep_nyx_avyanna_surprised:
    avyanna "That's... advanced. Are you sure? After everything you've told me?"
    jump act1_deep_nyx_nyx_certain

label act1_deep_nyx_nyx_certain:
    nyx "{i}She nods.{/i} Especially after everything I've told you. The Writbound might come for you eventually. The shard makes you valuable. Makes you a target. {i}Meeting your eyes directly.{/i} I want you prepared. I want you safe. From them and from anyone else who'd try to control you."
    jump act1_deep_nyx_lattice_personal

label act1_deep_nyx_lattice_personal:
    nyx "The lattice isn't just academic theory. It's personal. It's the fabric of connection — between people, places, moments. {i}She gestures at the space around you.{/i} When I work on the ship, I'm not just fixing metal. I'm reinforcing the bonds that hold us together. The crew, the journey, the meaning we make."
    jump act1_deep_nyx_lattice_philosophy

label act1_deep_nyx_lattice_philosophy:
    nyx "The Writbound see it as something to control. But it's not. It's alive. Responsive. It wants connection, not domination. {i}Quieter.{/i} Your shard understands that instinctively. That's why it hasn't hurt you. It's seeking connection, not control."
    jump act1_deep_nyx_choice_training

label act1_deep_nyx_choice_training:
    "{i}Nyx is offering something profound. Not just training, but her philosophy. A different way of understanding the lattice than what the Writbound taught. Personal. Relational. Based on trust, not domination.{/i}"
    menu:
        "'Yes. Teach me. I want to understand the way you do.'":
            $ game_state.set_flag("nyx_lattice_training")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_deep_nyx_accept_training
        "'I want to learn. But I'm afraid of becoming like them — the Writbound.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_express_training_fear
        "'Can the shard help? It seems to understand lattice work already.'":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_deep_nyx_ask_shard_training

label act1_deep_nyx_accept_training:
    avyanna "Yes. Teach me. I want to understand the way you do — connection, not control."
    jump act1_deep_nyx_nyx_teaching_begins

label act1_deep_nyx_nyx_teaching_begins:
    nyx "{i}Her expression opens into something rare — genuine warmth.{/i} Good. We'll start tomorrow. Meditation first, learning to sense the lattice without forcing it. Then resonance work. Then, eventually, defensive techniques. {i}A slight smile.{/i} You'll be better than I was at your stage. You have better teachers than I did."
    jump act1_deep_nyx_training_moment

label act1_deep_nyx_training_moment:
    "{i}Nyx reaches out, takes your hand. Her fingers are warm. Solid. Real. She closes her eyes, and suddenly you feel it — the lattice. Not as abstract theory, but as lived experience. The connections between you and Nyx, you and the ship, you and everyone aboard. A web of meaning, shimmering and alive.{/i}"
    jump act1_deep_nyx_avyanna_feels_it

label act1_deep_nyx_avyanna_feels_it:
    avyanna "{i}I gasp softly.{/i} I can feel it. Everyone. Everything. We're all connected."
    jump act1_deep_nyx_nyx_confirms_feeling

label act1_deep_nyx_nyx_confirms_feeling:
    $ game_state.set_flag("deep_nyx_complete")
    nyx "{i}She opens her eyes, still holding your hand.{/i} Yes. That's the lattice. That's what the Writbound tried to control and what we're going to protect. {i}A pause.{/i} Together."
    return

label act1_deep_nyx_express_training_fear:
    avyanna "I want to learn. But I'm afraid. What if I become like them — the Writbound? What if power corrupts me?"
    jump act1_deep_nyx_nyx_addresses_fear

label act1_deep_nyx_nyx_addresses_fear:
    nyx "{i}She takes your concern seriously.{/i} That fear is good. It means you have a moral compass. The Writbound lost theirs — or never had them. {i}A pause.{/i} I'll teach you with safeguards. We'll establish ethical boundaries first. You'll never work alone until you're ready."
    jump act1_deep_nyx_nyx_promise

label act1_deep_nyx_nyx_promise:
    nyx "And if I ever see you slipping toward their methods — control, violation, domination — I'll stop you. I promise. {i}Her voice is firm.{/i} I won't let you become what I escaped."
    jump act1_deep_nyx_avyanna_accepts_safeguards

label act1_deep_nyx_avyanna_accepts_safeguards:
    avyanna "Alright. With those safeguards... yes. I'll learn."
    jump act1_deep_nyx_nyx_teaching_begins

label act1_deep_nyx_ask_shard_training:
    avyanna "Can the shard help? It already seems to understand lattice work. Maybe it could... guide the process?"
    jump act1_deep_nyx_nyx_intrigued

label act1_deep_nyx_nyx_intrigued:
    nyx "{i}She looks intrigued.{/i} That's... actually brilliant. The shard has primordial knowledge of lattice structures. If we treat it as a partner rather than a tool... {i}She smiles slightly.{/i} Yes. Let's try that. A three-way collaboration — you, me, and Bee."
    jump act1_deep_nyx_shard_responds

label act1_deep_nyx_shard_responds:
    "{i}The shard pulses warmly in your chest. Agreement. Enthusiasm. It wants to help. It wants to teach you how to be whole — body, mind, and lattice. Together.{/i}"
    jump act1_deep_nyx_nyx_teaching_begins
