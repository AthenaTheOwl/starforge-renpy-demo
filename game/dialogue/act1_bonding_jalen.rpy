## act1_bonding_jalen.rpy — Auto-generated from act1_bonding_jalen.json
## 28 dialogue nodes

label act1_bonding_jalen:
    $ game_state.mark_dialogue_played("act1_bonding_jalen")
    jump act1_bonding_jalen_start

label act1_bonding_jalen_start:
    "{i}Maintenance corridor, deck three. Jalen is crouched beside an open access panel, datapads scattered around him, muttering to himself with the particular intensity of someone who's forgotten the rest of the ship exists.{/i}"
    jump act1_bonding_jalen_jalen_discovery

label act1_bonding_jalen_jalen_discovery:
    jalen "{i}Not looking up, voice rapid and excited.{/i} This is—this isn't background noise. This is structured data. Hidden in the telemetry we pulled from that last mission. Someone embedded a monitoring array in the station systems and disguised it as routine diagnostics. {i}He finally looks up, eyes bright.{/i} Oh. Avyanna. Perfect timing. Look at this."
    jump act1_bonding_jalen_avyanna_response_discovery

label act1_bonding_jalen_avyanna_response_discovery:
    avyanna "{i}Careful. He's excited, but I don't know what he's found.{/i} I... saw you were working on something. What is it?"
    jump act1_bonding_jalen_jalen_explanation

label act1_bonding_jalen_jalen_explanation:
    jalen "It's beautiful. Whoever built this was a genius. They embedded resonance sensors in standard station infrastructure—temperature, pressure, Lattice coherence, all feeding into a hidden database. {i}Gesturing rapidly.{/i} The company has no idea. They've been sitting on intelligence infrastructure for years and treating it like maintenance logs."
    menu:
        "[Tech] Examine the interface. Try to understand what he's seeing.":
            $ _sc_result = skill_check("tech", 10, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_bonding_jalen_tech_success
            else:
                jump act1_bonding_jalen_tech_failure
        "Why is this important? What does it do?":
            jump act1_bonding_jalen_ask_importance
        "Should we share this with the others?":
            jump act1_bonding_jalen_ask_sharing

label act1_bonding_jalen_tech_success:
    "{i}You lean closer to the datapad. The interface is elegant—data streams flowing in patterns that almost make sense. You recognize fragments: resonance signatures, structural stress markers, something that looks like predictive modeling. This isn't monitoring. This is analysis. Someone was studying the Lattice itself through station operations.{/i}"
    jump act1_bonding_jalen_tech_interpretation

label act1_bonding_jalen_tech_interpretation:
    avyanna "It's not just monitoring. It's learning. Tracking patterns in the Lattice and predicting... something. Failures? Opportunities?"
    jump act1_bonding_jalen_jalen_excited

label act1_bonding_jalen_jalen_excited:
    $ relationship_manager.process_reputation_affinity("jalen", 3)
    jalen "{i}Eyes widening, almost bouncing.{/i} Yes! Exactly! You see it! This array was predicting Lattice events before they happened. Whoever built this knew things the corporations are still guessing at. {i}A pause, suddenly serious.{/i} And if we can access the full database, we might know them too."
    jump act1_bonding_jalen_offer_proposition

label act1_bonding_jalen_tech_failure:
    "{i}You try to make sense of the interface, but it's too complex. Data flows in patterns you can't parse. Whatever Jalen sees, it's beyond your current understanding.{/i}"
    jump act1_bonding_jalen_tech_admission

label act1_bonding_jalen_tech_admission:
    avyanna "I don't understand what I'm looking at. It's too complex."
    jump act1_bonding_jalen_jalen_patient

label act1_bonding_jalen_jalen_patient:
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "{i}No judgment, just enthusiasm redirected.{/i} That's okay! I can teach you. This is advanced stuff—took me years to get comfortable with Lattice telemetry. But you have the instinct. I can see it in how you're tracking the data flow. {i}A beat.{/i} You're trying to understand, not just observe. That's the important part."
    jump act1_bonding_jalen_offer_proposition

label act1_bonding_jalen_ask_importance:
    avyanna "Why is this important? What does it actually do?"
    jump act1_bonding_jalen_jalen_importance_answer

label act1_bonding_jalen_jalen_importance_answer:
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "It gives us leverage. Knowledge the corporations don't have. Predictive capabilities they'd kill for. {i}A pause, his expression shifting more serious.{/i} But more than that—it's proof that someone else was fighting this fight before us. We're not the first. That matters."
    jump act1_bonding_jalen_offer_proposition

label act1_bonding_jalen_ask_sharing:
    avyanna "Should we share this with the others? Elia, or...?"
    jump act1_bonding_jalen_jalen_sharing_answer

label act1_bonding_jalen_jalen_sharing_answer:
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "Absolutely. I'll brief everyone once I've decoded more of it. Elia will want tactical applications, Vesper will appreciate the precision of the design. {i}He meets your eyes.{/i} But I wanted to show you first. You're crew. This kind of discovery—it belongs to all of us."
    jump act1_bonding_jalen_offer_proposition

label act1_bonding_jalen_offer_proposition:
    jalen "{i}Standing, brushing dust off his clothes.{/i} I've been thinking. You've got an instinct for this kind of work. The way you approach problems, ask the right questions. {i}Gesturing at the datapads.{/i} Let me teach you properly. Navigation, systems theory, Lattice fundamentals. The real stuff. You're crew. You should know how this ship works."
    jump act1_bonding_jalen_avyanna_proposition_reaction

label act1_bonding_jalen_avyanna_proposition_reaction:
    "{i}He's offering you something more than survival training. He's offering you knowledge. The chance to understand the systems that once controlled you. The presence behind your eyes pulses—interested, curious.{/i}"
    menu:
        "Accept. 'I want to learn. Teach me.'":
            $ game_state.set_flag("jalen_bonded")
            $ relationship_manager.process_reputation_affinity("jalen", 2)
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_bonding_jalen_accept_immediate
        "Ask about the crew. 'Do the others... do they think I'm ready for this?'":
            jump act1_bonding_jalen_ask_crew
        "Express doubt. 'I'm not smart enough for this kind of work.'":
            jump act1_bonding_jalen_express_doubt

label act1_bonding_jalen_accept_immediate:
    avyanna "I want to learn. Teach me. {i}The words feel like choosing a future instead of just surviving a present.{/i}"
    jump act1_bonding_jalen_jalen_acceptance

label act1_bonding_jalen_jalen_acceptance:
    jalen "{i}A grin, bright and genuine.{/i} Yes! Okay, this is great. We'll start with basic systems theory, then move into navigation fundamentals, then—{i}He catches himself.{/i} Sorry. I get ahead of myself. This is going to be amazing. You're going to love this."
    return

label act1_bonding_jalen_ask_crew:
    avyanna "Do the others... do they think I'm ready for this?"
    jump act1_bonding_jalen_jalen_crew_description

label act1_bonding_jalen_jalen_crew_description:
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "Elia trusts my judgment on tech matters. Always has. And Vesper mentioned you handled the combat systems training faster than expected. {i}A pause, something softer in his expression.{/i} But this isn't about them. This is about you and me. You're crew. That means I teach you what I know. That's how this works."
    jump act1_bonding_jalen_crew_followup

label act1_bonding_jalen_crew_followup:
    "{i}He means it. You can hear it in his voice—genuine conviction. This isn't charity or obligation. He actually wants to share this with you.{/i}"
    menu:
        "'Then yes. I want to learn.'":
            $ game_state.set_flag("jalen_bonded")
            $ relationship_manager.process_reputation_affinity("jalen", 3)
            jump act1_bonding_jalen_accept_after_crew
        "'I need time to think about it.'":
            jump act1_bonding_jalen_need_time

label act1_bonding_jalen_accept_after_crew:
    avyanna "Then yes. I want to learn."
    jump act1_bonding_jalen_jalen_acceptance

label act1_bonding_jalen_express_doubt:
    avyanna "I'm not smart enough for this kind of work. You're talking about things I don't understand."
    jump act1_bonding_jalen_jalen_doubt_response

label act1_bonding_jalen_jalen_doubt_response:
    $ relationship_manager.process_reputation_affinity("jalen", 3)
    jalen "{i}Immediate, almost fierce.{/i} That's what they want you to think. The systems. The corporations. Keep people believing they're not smart enough, not capable enough, not worthy enough to understand. {i}A beat, gentler.{/i} But you asked the right questions just now. You tracked the logic. Intelligence isn't about what you already know. It's about being willing to learn."
    jump act1_bonding_jalen_doubt_followup

label act1_bonding_jalen_doubt_followup:
    "{i}His conviction is absolute. He genuinely believes you can learn this. That you're capable. The presence behind your eyes pulses—something that might be hope.{/i}"
    menu:
        "'Then teach me. I want to try.'":
            $ game_state.set_flag("jalen_bonded")
            $ relationship_manager.process_reputation_affinity("jalen", 4)
            jump act1_bonding_jalen_accept_after_doubt
        "'I appreciate that. But I need time to think.'":
            jump act1_bonding_jalen_need_time

label act1_bonding_jalen_accept_after_doubt:
    avyanna "Then teach me. I want to try."
    jump act1_bonding_jalen_jalen_acceptance

label act1_bonding_jalen_need_time:
    avyanna "I need some time. To think about this."
    jump act1_bonding_jalen_jalen_patience

label act1_bonding_jalen_jalen_patience:
    jalen "{i}A nod, understanding.{/i} Sure, of course. No pressure. {i}He turns back to the datapads, already getting distracted by the data.{/i} I'll be here when you're ready. Probably still trying to crack this encryption."
    return
