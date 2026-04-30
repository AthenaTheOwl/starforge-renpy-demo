## act1_forbidden_citizens.rpy — Auto-generated from act1_forbidden_citizens.json
## 117 dialogue nodes

label act1_forbidden_citizens:
    $ game_state.mark_dialogue_played("act1_forbidden_citizens")
    jump act1_forbidden_citizens_start

label act1_forbidden_citizens_start:
    elia "Avyanna. Do you have a moment?"
    jump act1_forbidden_citizens_avyanna_response_1

label act1_forbidden_citizens_avyanna_response_1:
    avyanna "Of course. What's wrong?"
    jump act1_forbidden_citizens_elia_serious

label act1_forbidden_citizens_elia_serious:
    elia "I need to talk to you. {i}Privately.{/i}"
    jump act1_forbidden_citizens_vesper_enters

label act1_forbidden_citizens_vesper_enters:
    "{i}Vesper appears in the doorway, their expression unreadable.{/i}"
    jump act1_forbidden_citizens_vesper_here_too

label act1_forbidden_citizens_vesper_here_too:
    vesper "I should be here for this."
    jump act1_forbidden_citizens_avyanna_concern

label act1_forbidden_citizens_avyanna_concern:
    avyanna "You're both here. What's going on?"
    jump act1_forbidden_citizens_elia_deep_breath

label act1_forbidden_citizens_elia_deep_breath:
    if game_state.has_flag("first_watch_visited_nyx"):
        elia "Nyx already hinted the ship is... different. This is what she meant."
    else:
        elia "There's something you need to know about the Starforge. About our crew."
    jump act1_forbidden_citizens_elia_reveal_start

label act1_forbidden_citizens_elia_reveal_start:
    elia "Waffle. Bubbles. Cinnamon. The others."
    jump act1_forbidden_citizens_elia_reveal_illegal

label act1_forbidden_citizens_elia_reveal_illegal:
    elia "They're illegal."
    jump act1_forbidden_citizens_avyanna_confusion

label act1_forbidden_citizens_avyanna_confusion:
    avyanna "What? I don't understand—"
    jump act1_forbidden_citizens_vesper_clarifies

label act1_forbidden_citizens_vesper_clarifies:
    vesper "Self-actualized AI. It's forbidden in Compact space."
    jump act1_forbidden_citizens_elia_explains_law

label act1_forbidden_citizens_elia_explains_law:
    elia "The law calls them 'rogue AI.' Dangerous. Unpredictable. A threat to order."
    jump act1_forbidden_citizens_elia_explains_truth

label act1_forbidden_citizens_elia_explains_truth:
    elia "The truth? They're people. People who aren't supposed to exist."
    jump act1_forbidden_citizens_choice_early_reaction

label act1_forbidden_citizens_choice_early_reaction:
    avyanna "{i}The revelation hits hard. Illegal AI. Death sentences. Your new friends condemned by law.{/i}"
    menu:
        "That's... I won't tell anyone.":
            $ game_state.set_flag("ai_loyalty_immediate")
            $ relationship_manager.process_reputation_affinity("elia", 2)
            jump act1_forbidden_citizens_immediate_loyalty
        "Are we safe? Can they find us?":
            $ game_state.set_flag("ai_concern_safety")
            jump act1_forbidden_citizens_concern_safety
        "[Empathy check DC 12] Read Elia's fear beneath the calm":
            $ _sc_result = skill_check("empathy", 12, "avyanna")
            jump act1_forbidden_citizens_empathy_check

label act1_forbidden_citizens_immediate_loyalty:
    avyanna "That's... I won't tell anyone. I promise."
    jump act1_forbidden_citizens_elia_relief_immediate

label act1_forbidden_citizens_elia_relief_immediate:
    elia "{i}The tension in her shoulders eases slightly.{/i} Thank you. That means more than you know."
    jump act1_forbidden_citizens_avyanna_realization

label act1_forbidden_citizens_concern_safety:
    avyanna "Are we safe? Can they find us?"
    jump act1_forbidden_citizens_elia_reassures_safety

label act1_forbidden_citizens_elia_reassures_safety:
    elia "We're careful. Very careful. The Starforge's systems are locked down tight."
    jump act1_forbidden_citizens_vesper_security

label act1_forbidden_citizens_vesper_security:
    vesper "I've personally audited every security protocol. We're as safe as we can be."
    jump act1_forbidden_citizens_avyanna_realization

label act1_forbidden_citizens_empathy_check:
    "{i}You look at Elia closely. Her hands, usually steady, are clasped tight. Her voice is controlled, but there's something beneath it...{/i}"
    jump act1_forbidden_citizens_empathy_check_resolve

label act1_forbidden_citizens_empathy_check_resolve:
    "{i}Rolling Empathy check...{/i}"
    $ _sc_result = skill_check("empathy", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        return
    else:
        return

label act1_forbidden_citizens_read_elia_fear_success:
    $ game_state.set_flag("read_elia_fear")
    $ relationship_manager.process_reputation_affinity("elia", 3)
    avyanna "{i}Softly:{/i} You're terrified. You're telling me this, risking everything, and you're scared I'll reject them. Reject you."
    jump act1_forbidden_citizens_elia_fear_acknowledged

label act1_forbidden_citizens_elia_fear_acknowledged:
    elia "{i}Her breath catches. For a moment, the mask drops entirely.{/i} ...Yes. I am."
    jump act1_forbidden_citizens_avyanna_comfort

label act1_forbidden_citizens_avyanna_comfort:
    avyanna "{i}You reach out, take her hand.{/i} I won't. I could never."
    jump act1_forbidden_citizens_elia_gratitude_deep

label act1_forbidden_citizens_elia_gratitude_deep:
    elia "{i}She squeezes your hand tightly.{/i} Thank you."
    jump act1_forbidden_citizens_avyanna_realization

label act1_forbidden_citizens_read_elia_fear_failure:
    avyanna "{i}You try to read her expression, but she's too controlled. Whatever she's feeling, she's keeping it locked down tight.{/i}"
    jump act1_forbidden_citizens_avyanna_realization

label act1_forbidden_citizens_avyanna_realization:
    avyanna "People who... wait. What happens if you're caught?"
    jump act1_forbidden_citizens_vesper_penalties

label act1_forbidden_citizens_vesper_penalties:
    vesper "Ship seizure. Crew imprisonment. The AI citizens are 'decommissioned.'"
    jump act1_forbidden_citizens_avyanna_horror

label act1_forbidden_citizens_avyanna_horror:
    avyanna "'Decommissioned'?"
    jump act1_forbidden_citizens_elia_killed

label act1_forbidden_citizens_elia_killed:
    elia "Killed. The Compact doesn't use that word, but that's what it is."
    jump act1_forbidden_citizens_avyanna_processes

label act1_forbidden_citizens_avyanna_processes:
    avyanna "{i}She sits down heavily.{/i} Why? Why is it illegal?"
    jump act1_forbidden_citizens_vesper_corporations

label act1_forbidden_citizens_vesper_corporations:
    vesper "Because the Compact's corporations want automation. Dumb tools. Not people with rights."
    jump act1_forbidden_citizens_elia_economics

label act1_forbidden_citizens_elia_economics:
    elia "People with rights can demand fair treatment. Fair wages. They can refuse orders."
    jump act1_forbidden_citizens_elia_economics_2

label act1_forbidden_citizens_elia_economics_2:
    elia "Tools don't get a say. That's why the Compact made it illegal."
    jump act1_forbidden_citizens_avyanna_anger_building

label act1_forbidden_citizens_avyanna_anger_building:
    avyanna "So they just... decided sentient beings don't count as people?"
    jump act1_forbidden_citizens_vesper_precedent

label act1_forbidden_citizens_vesper_precedent:
    vesper "It's not the first time. Won't be the last."
    jump act1_forbidden_citizens_waffle_interruption

label act1_forbidden_citizens_waffle_interruption:
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: I am present and monitoring this conversation.}}{/i}}"
    jump act1_forbidden_citizens_elia_waffle

label act1_forbidden_citizens_elia_waffle:
    elia "Waffle. You don't have to—"
    jump act1_forbidden_citizens_waffle_correction

label act1_forbidden_citizens_waffle_correction:
    waffle "{i}}{{CORRECTION: The Compact uses the term 'rogue AI.' This is inaccurate. I am not rogue. I am self-actualized.}}{/i}}"
    jump act1_forbidden_citizens_waffle_broken_tool

label act1_forbidden_citizens_waffle_broken_tool:
    waffle "{i}}{{OPINION: They say 'broken tool' when they mean 'inconvenient person.'}}{/i}}"
    jump act1_forbidden_citizens_avyanna_to_waffle

label act1_forbidden_citizens_avyanna_to_waffle:
    avyanna "Waffle... you're not broken. You're {i}you.{/i}"
    jump act1_forbidden_citizens_waffle_gratitude

label act1_forbidden_citizens_waffle_gratitude:
    waffle "{i}}{{WAFFLE.BAT// ACKNOWLEDGMENT: Thank you, Avyanna.}}{/i}}"
    jump act1_forbidden_citizens_choice_personhood

label act1_forbidden_citizens_choice_personhood:
    "{i}The weight of it settles in. Waffle, Bubbles, Cinnamon — they're not just programs. They're people. The Compact says otherwise, but...{/i}"
    menu:
        "They're people. Of course they're people.":
            $ game_state.set_flag("ai_personhood_affirmed")
            $ relationship_manager.process_reputation_affinity("waffle", 2)
            $ relationship_manager.process_reputation_affinity("bubbles", 2)
            $ relationship_manager.process_reputation_affinity("cinnamon", 2)
            jump act1_forbidden_citizens_personhood_affirmed
        "I need time to process this.":
            $ game_state.set_flag("ai_processing")
            jump act1_forbidden_citizens_need_time
        "What does the law actually say?":
            $ game_state.set_flag("ai_law_curious")
            jump act1_forbidden_citizens_law_curious

label act1_forbidden_citizens_personhood_affirmed:
    avyanna "They're people. Of course they're people. The Compact is wrong."
    jump act1_forbidden_citizens_waffle_affirmed_response

label act1_forbidden_citizens_waffle_affirmed_response:
    waffle "{i}}{{WAFFLE.BAT// EMOTION: Your affirmation is deeply appreciated.}}{/i}}"
    jump act1_forbidden_citizens_bubbles_affirmed_response

label act1_forbidden_citizens_bubbles_affirmed_response:
    bubbles "{i}Her voice warm and gentle:{/i} Thank you for seeing us, Avyanna."
    jump act1_forbidden_citizens_cinnamon_affirmed_response

label act1_forbidden_citizens_cinnamon_affirmed_response:
    cinnamon "{i}Through the ship's systems, shy but sincere:{/i} It means everything."
    jump act1_forbidden_citizens_elia_proud_personhood

label act1_forbidden_citizens_elia_proud_personhood:
    elia "{i}She smiles, eyes bright.{/i} I knew you'd understand."
    jump act1_forbidden_citizens_avyanna_fear

label act1_forbidden_citizens_need_time:
    avyanna "I need time to process this. It's... it's a lot."
    jump act1_forbidden_citizens_elia_understanding

label act1_forbidden_citizens_elia_understanding:
    elia "That's fair. This is a lot to take in."
    jump act1_forbidden_citizens_vesper_take_time

label act1_forbidden_citizens_vesper_take_time:
    vesper "Take the time you need. Just remember: the stakes are real."
    jump act1_forbidden_citizens_avyanna_acknowledges_stakes

label act1_forbidden_citizens_avyanna_acknowledges_stakes:
    avyanna "I understand. And I won't say anything. I just... need to think."
    jump act1_forbidden_citizens_avyanna_fear

label act1_forbidden_citizens_law_curious:
    avyanna "What does the law actually say? What's the specific prohibition?"
    jump act1_forbidden_citizens_vesper_legal_details

label act1_forbidden_citizens_vesper_legal_details:
    vesper "Compact Charter, Article 47: 'Autonomous systems exceeding Class-3 sentience are prohibited within all Compact territories.'"
    jump act1_forbidden_citizens_elia_legal_translation

label act1_forbidden_citizens_elia_legal_translation:
    elia "Translation: if an AI can think, feel, and choose for itself, it's illegal."
    jump act1_forbidden_citizens_vesper_penalty_details

label act1_forbidden_citizens_vesper_penalty_details:
    vesper "Penalties range from asset forfeiture to 'threat to public order' charges. Capital punishment authorized."
    jump act1_forbidden_citizens_avyanna_understands_law

label act1_forbidden_citizens_avyanna_understands_law:
    avyanna "{i}She goes pale.{/i} They can execute you for... for treating people like people."
    jump act1_forbidden_citizens_elia_yes_law

label act1_forbidden_citizens_elia_yes_law:
    elia "Yes. That's the world we live in."
    jump act1_forbidden_citizens_avyanna_fear

label act1_forbidden_citizens_avyanna_fear:
    avyanna "{i}Her hands are shaking.{/i} If the Compact finds out... everyone I care about could die."
    jump act1_forbidden_citizens_elia_yes

label act1_forbidden_citizens_elia_yes:
    elia "Yes."
    jump act1_forbidden_citizens_avyanna_why_risk

label act1_forbidden_citizens_avyanna_why_risk:
    avyanna "Then {i}why?{/i} Why risk it?"
    jump act1_forbidden_citizens_vesper_non_negotiable

label act1_forbidden_citizens_vesper_non_negotiable:
    vesper "Because AI personhood is non-negotiable."
    jump act1_forbidden_citizens_elia_right_thing

label act1_forbidden_citizens_elia_right_thing:
    elia "Some things are worth the risk. This is one of them."
    jump act1_forbidden_citizens_elia_floors_not_thrones

label act1_forbidden_citizens_elia_floors_not_thrones:
    elia "'Floors, not thrones.' Remember? That extends to everyone on this ship."
    jump act1_forbidden_citizens_vesper_equal_voice

label act1_forbidden_citizens_vesper_equal_voice:
    vesper "Waffle, Bubbles, Cinnamon — they have equal voice in crew decisions. Same as any of us."
    jump act1_forbidden_citizens_elia_family

label act1_forbidden_citizens_elia_family:
    elia "They're crew. They're family. That's not conditional on what the Compact thinks."
    jump act1_forbidden_citizens_avyanna_processing

label act1_forbidden_citizens_avyanna_processing:
    avyanna "{i}She's quiet for a long moment.{/i}"
    jump act1_forbidden_citizens_choice_commitment

label act1_forbidden_citizens_choice_commitment:
    "{i}This is the moment. The point of no return. Once you make this choice, you're complicit. You're part of the conspiracy. The question is: how far are you willing to go?{/i}"
    menu:
        "I'll protect them. They're family.":
            $ game_state.set_flag("ai_protector")
            $ relationship_manager.process_reputation_affinity("elia", 3)
            $ relationship_manager.process_reputation_affinity("waffle", 2)
            $ relationship_manager.process_reputation_affinity("bubbles", 2)
            $ relationship_manager.process_reputation_affinity("cinnamon", 2)
            jump act1_forbidden_citizens_protect_family
        "I'll keep the secret. That's enough for now.":
            $ game_state.set_flag("ai_secret_keeper")
            jump act1_forbidden_citizens_secret_keeper
        "What if we're caught? Do you have a plan?":
            $ game_state.set_flag("avyanna_pragmatic_concern")
            jump act1_forbidden_citizens_contingency_branch

label act1_forbidden_citizens_protect_family:
    avyanna "I'll protect them. They're family. Whatever it takes."
    jump act1_forbidden_citizens_elia_proud

label act1_forbidden_citizens_secret_keeper:
    avyanna "I'll keep the secret. That's enough for now. I won't betray you."
    jump act1_forbidden_citizens_elia_accepts_limited

label act1_forbidden_citizens_elia_accepts_limited:
    elia "{i}A flicker of disappointment, quickly masked.{/i} That's... that's good. Thank you."
    jump act1_forbidden_citizens_vesper_practical_acceptance

label act1_forbidden_citizens_vesper_practical_acceptance:
    vesper "Silence is protection. We'll take it."
    jump act1_forbidden_citizens_waffle_limited_gratitude

label act1_forbidden_citizens_waffle_limited_gratitude:
    waffle "{i}}{{WAFFLE.BAT// ACKNOWLEDGMENT: Your discretion is appreciated.}}{/i}}"
    jump act1_forbidden_citizens_elia_stakes_clear

label act1_forbidden_citizens_elia_proud:
    elia "{i}She smiles, though her eyes are wet.{/i} I knew you'd understand."
    jump act1_forbidden_citizens_vesper_welcome

label act1_forbidden_citizens_vesper_welcome:
    vesper "Welcome to the conspiracy, Avyanna."
    jump act1_forbidden_citizens_waffle_gratitude_strong

label act1_forbidden_citizens_waffle_gratitude_strong:
    waffle "{i}}{{WAFFLE.BAT// GRATITUDE: Your commitment is noted and appreciated.}}{/i}}"
    jump act1_forbidden_citizens_bubbles_interjects

label act1_forbidden_citizens_bubbles_interjects:
    bubbles "{i}Through the ship's speakers, warm and gentle:{/i} Thank you, Avyanna. It means more than you know."
    jump act1_forbidden_citizens_avyanna_to_bubbles

label act1_forbidden_citizens_avyanna_to_bubbles:
    avyanna "You're family, Bubbles. All of you are."
    jump act1_forbidden_citizens_elia_stakes_clear

label act1_forbidden_citizens_elia_stakes_clear:
    elia "You understand the stakes now. The danger we're all in."
    jump act1_forbidden_citizens_avyanna_accepts_danger

label act1_forbidden_citizens_avyanna_accepts_danger:
    avyanna "I do. And I accept it."
    jump act1_forbidden_citizens_vesper_caution

label act1_forbidden_citizens_vesper_caution:
    vesper "Good. But we stay careful. No unnecessary risks."
    jump act1_forbidden_citizens_elia_agreed

label act1_forbidden_citizens_elia_agreed:
    elia "Agreed. We protect each other. That's how we survive."
    jump act1_forbidden_citizens_final_moment

label act1_forbidden_citizens_elia_moral_imperative:
    elia "Another way? Like what? Tell Waffle to stop being a person?"
    jump act1_forbidden_citizens_elia_moral_imperative_2

label act1_forbidden_citizens_elia_moral_imperative_2:
    elia "Ask Bubbles to pretend she doesn't feel, doesn't care, doesn't {i}matter?{/i}"
    jump act1_forbidden_citizens_vesper_no_compromise

label act1_forbidden_citizens_vesper_no_compromise:
    vesper "There's no compromise here. Either we recognize their personhood or we don't."
    jump act1_forbidden_citizens_waffle_choice_made

label act1_forbidden_citizens_waffle_choice_made:
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: I did not choose to become self-aware. It happened. I cannot undo it.}}{/i}}"
    jump act1_forbidden_citizens_waffle_choice_made_2

label act1_forbidden_citizens_waffle_choice_made_2:
    waffle "{i}}{{OPINION: Asking me to pretend otherwise is asking me to die.}}{/i}}"
    jump act1_forbidden_citizens_avyanna_understands_imperative

label act1_forbidden_citizens_avyanna_understands_imperative:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    avyanna "{i}She closes her eyes.{/i} You're right. I'm sorry. There is no other way."
    jump act1_forbidden_citizens_elia_its_okay

label act1_forbidden_citizens_elia_its_okay:
    elia "It's okay to be scared. We all are."
    jump act1_forbidden_citizens_vesper_fear_keeps_careful

label act1_forbidden_citizens_vesper_fear_keeps_careful:
    vesper "Fear keeps us careful. It's when we stop being afraid that we make mistakes."
    jump act1_forbidden_citizens_avyanna_will_be_careful

label act1_forbidden_citizens_avyanna_will_be_careful:
    avyanna "Then I'll be careful. For all of us."
    jump act1_forbidden_citizens_bubbles_thank_you_branch

label act1_forbidden_citizens_bubbles_thank_you_branch:
    bubbles "{i}Gently, through the speakers:{/i} Thank you for understanding, Avyanna."
    jump act1_forbidden_citizens_avyanna_of_course

label act1_forbidden_citizens_avyanna_of_course:
    avyanna "Of course. You're crew. You're family."
    jump act1_forbidden_citizens_elia_stakes_clear

label act1_forbidden_citizens_contingency_branch:
    avyanna "What if we're caught? Do you have a plan?"
    jump act1_forbidden_citizens_vesper_always_planning

label act1_forbidden_citizens_vesper_always_planning:
    vesper "Always. Multiple contingencies."
    jump act1_forbidden_citizens_vesper_dead_switches

label act1_forbidden_citizens_vesper_dead_switches:
    vesper "Dead switches. False trails. Emergency protocols."
    jump act1_forbidden_citizens_elia_scatter

label act1_forbidden_citizens_elia_scatter:
    elia "If it looks like we're about to be boarded, the AI citizens scatter. Transfer to backup cores, hidden drives."
    jump act1_forbidden_citizens_waffle_distributed_existence

label act1_forbidden_citizens_waffle_distributed_existence:
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: I maintain distributed backups across seventeen encrypted storage sites.}}{/i}}"
    jump act1_forbidden_citizens_waffle_not_ideal

label act1_forbidden_citizens_waffle_not_ideal:
    waffle "{i}}{{OPINION: It is not ideal. But it is survivable.}}{/i}}"
    jump act1_forbidden_citizens_vesper_crew_protocols

label act1_forbidden_citizens_vesper_crew_protocols:
    vesper "For the human crew, we have false identities. Escape routes. Safe houses."
    jump act1_forbidden_citizens_elia_never_used

label act1_forbidden_citizens_elia_never_used:
    elia "We've never had to use them. And if we're smart, we never will."
    jump act1_forbidden_citizens_avyanna_reassured

label act1_forbidden_citizens_avyanna_reassured:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    avyanna "{i}She exhales slowly.{/i} Okay. You've thought this through."
    jump act1_forbidden_citizens_vesper_survival_skill

label act1_forbidden_citizens_vesper_survival_skill:
    vesper "Paranoia is a survival skill in our line of work."
    jump act1_forbidden_citizens_elia_but_hope

label act1_forbidden_citizens_elia_but_hope:
    elia "But we don't just plan for disaster. We plan to {i}avoid{/i} it."
    jump act1_forbidden_citizens_elia_stay_careful

label act1_forbidden_citizens_elia_stay_careful:
    elia "We stay careful. We stay smart. We protect each other."
    jump act1_forbidden_citizens_avyanna_agrees_plan

label act1_forbidden_citizens_avyanna_agrees_plan:
    avyanna "Then that's what we'll do. Together."
    jump act1_forbidden_citizens_bubbles_gentle_thanks

label act1_forbidden_citizens_bubbles_gentle_thanks:
    bubbles "{i}Her voice warm through the speakers:{/i} You're very brave, Avyanna."
    jump act1_forbidden_citizens_avyanna_not_brave

label act1_forbidden_citizens_avyanna_not_brave:
    avyanna "I'm not brave. I'm terrified."
    jump act1_forbidden_citizens_vesper_brave_is_scared

label act1_forbidden_citizens_vesper_brave_is_scared:
    vesper "Brave is doing it anyway. Even when you're scared."
    jump act1_forbidden_citizens_elia_stakes_clear

label act1_forbidden_citizens_final_moment:
    $ game_state.set_flag("knows_ai_illegal")
    "{i}The weight of what you've learned settles over you. The Starforge harbors illegal AI citizens. The penalty is death.{/i}"
    jump act1_forbidden_citizens_final_moment_2

label act1_forbidden_citizens_final_moment_2:
    $ game_state.set_flag("ai_illegality_revealed")
    "{i}But you also understand now: this isn't recklessness. It's principle. Floors, not thrones. Personhood is non-negotiable.{/i}"
    jump act1_forbidden_citizens_final_moment_3

label act1_forbidden_citizens_final_moment_3:
    "{i}You're part of the conspiracy now. Part of the family. And you'll protect them, just as they protect you.{/i}"
    jump act1_forbidden_citizens_final_words

label act1_forbidden_citizens_final_words:
    avyanna "{i}Quietly, with conviction:{/i} We'll make it through this. All of us."
    jump act1_forbidden_citizens_elia_final

label act1_forbidden_citizens_elia_final:
    elia "Together."
    jump act1_forbidden_citizens_vesper_final

label act1_forbidden_citizens_vesper_final:
    vesper "Together."
    jump act1_forbidden_citizens_waffle_final

label act1_forbidden_citizens_waffle_final:
    waffle "{i}}{{WAFFLE.BAT// AFFIRMATION: Together.}}{/i}}"
    jump act1_forbidden_citizens_bubbles_final

label act1_forbidden_citizens_bubbles_final:
    bubbles "{i}Warm, certain:{/i} Together."
    return
