## act1_bonding_elisira.rpy — Auto-generated from act1_bonding_elisira.json
## 30 dialogue nodes

label act1_bonding_elisira:
    $ game_state.mark_dialogue_played("act1_bonding_elisira")
    jump act1_bonding_elisira_start

label act1_bonding_elisira_start:
    "{i}Lumen Thief bridge. Post-boarding action. Debris still cooling in corridors behind you. Elisira stands near the console, hands at her sides, pistols visible but not drawn. She's watching you with the particular attention of someone cataloging capability, not threat.{/i}"
    jump act1_bonding_elisira_elisira_opening

label act1_bonding_elisira_elisira_opening:
    elisira "You stabilized the cargo bay containment field. I watched the sensor trace. Precision work. Efficient."
    jump act1_bonding_elisira_avyanna_deflect

label act1_bonding_elisira_avyanna_deflect:
    avyanna "{i}Uncertain. She's cataloging me. That's never comfortable.{/i} I just... did what needed doing."
    jump act1_bonding_elisira_elisira_assessment

label act1_bonding_elisira_elisira_assessment:
    elisira "That's the answer I wanted. No performance. No embellishment. You assessed, you acted, you didn't wait for permission. {i}A pause. Something in her expression shifts—not warmth, but acknowledgment.{/i} You've been doing that since you came aboard. Initiative without grandstanding."
    menu:
        "[Insight] Read her intent. What is she actually saying?":
            $ _sc_result = skill_check("insight", 10, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_bonding_elisira_insight_success
            else:
                jump act1_bonding_elisira_insight_failure
        "Is this... feedback? Or something else?":
            jump act1_bonding_elisira_direct_question
        "I'm just doing my part. Nothing special.":
            jump act1_bonding_elisira_deflect_capability

label act1_bonding_elisira_insight_success:
    "{i}You watch the way she stands. Not blocking exits—giving you space. The way her hands stay visible, no sudden movements. The careful calibration of someone who knows what trust looks like and is deliberately offering it. She's not evaluating your performance. She's acknowledging you've already passed.{/i}"
    jump act1_bonding_elisira_insight_response

label act1_bonding_elisira_insight_response:
    avyanna "You're not assessing me. You're... telling me I've earned something."
    jump act1_bonding_elisira_elisira_impressed

label act1_bonding_elisira_elisira_impressed:
    $ relationship_manager.process_reputation_affinity("elisira", 3)
    elisira "{i}A flicker of something—surprise, maybe. Approval.{/i} Yes. Exactly that. You've been crew since the day we pulled you out. But trust is different. Trust is earned, not given. You've earned it. I wanted you to know that."
    jump act1_bonding_elisira_offer_terms

label act1_bonding_elisira_insight_failure:
    "{i}You try to read her expression, but Elisira is practiced at hiding. All you see is the surface—professional, composed, unreadable. Whatever her intent, she's not revealing it yet.{/i}"
    jump act1_bonding_elisira_elisira_clarifies

label act1_bonding_elisira_elisira_clarifies:
    elisira "You've been crew since we pulled you aboard. But crew and {i}trusted{/i} crew are different things. You've moved from one category to the other. I wanted to acknowledge that."
    jump act1_bonding_elisira_offer_terms

label act1_bonding_elisira_direct_question:
    avyanna "Is this... feedback? Or something else?"
    jump act1_bonding_elisira_elisira_direct_answer

label act1_bonding_elisira_elisira_direct_answer:
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "Recognition. You have skills we need. Pattern recognition. Technical intuition. The ability to act under pressure without collapsing. {i}A pause.{/i} More than that—you use those skills without waiting to be told. That's rare."
    jump act1_bonding_elisira_offer_terms

label act1_bonding_elisira_deflect_capability:
    avyanna "I'm just doing my part. Nothing special."
    jump act1_bonding_elisira_elisira_deflect_response

label act1_bonding_elisira_elisira_deflect_response:
    elisira "That's exactly what makes it special. {i}She gestures toward the corridor where the boarding action happened.{/i} You didn't freeze. You didn't wait for orders. You saw what needed doing and you did it. That's trust-worthy."
    jump act1_bonding_elisira_offer_terms

label act1_bonding_elisira_offer_terms:
    elisira "You already have equal share in crew decisions. Your own quarters. Medical care. Food that isn't designed to keep you barely functional. {i}A beat.{/i} But I wanted to be clear: those aren't provisional. You're not on trial anymore. You're crew. Full weight, full trust."
    jump act1_bonding_elisira_avyanna_terms_reaction

label act1_bonding_elisira_avyanna_terms_reaction:
    "{i}The words land differently than you expected. Not an offer—an acknowledgment. She's not giving you something new. She's telling you that what you already have is permanent. The presence behind your eyes pulses—cautious, hopeful.{/i}"
    menu:
        "Acknowledge. 'Thank you. That... means something.'":
            $ game_state.set_flag("elisira_bonded")
            $ relationship_manager.process_reputation_affinity("elisira", 2)
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_bonding_elisira_accept_immediately
        "Question. 'What changed? Why tell me now?'":
            jump act1_bonding_elisira_question_cost
        "Test the boundary. 'And if I wanted to leave?'":
            jump act1_bonding_elisira_test_refusal

label act1_bonding_elisira_accept_immediately:
    avyanna "Thank you. That... means something. {i}The words feel strange. Like claiming something you're not sure you deserve, but want anyway.{/i}"
    jump act1_bonding_elisira_elisira_acceptance

label act1_bonding_elisira_elisira_acceptance:
    elisira "{i}A nod. Final. No ceremony.{/i} Good. Keep doing what you're doing. {i}She turns to leave, then pauses.{/i} You've earned your place here. Don't forget that."
    return

label act1_bonding_elisira_question_cost:
    avyanna "What changed? Why tell me now?"
    jump act1_bonding_elisira_elisira_cost_answer

label act1_bonding_elisira_elisira_cost_answer:
    $ relationship_manager.process_reputation_affinity("elisira", 2)
    elisira "{i}Something in her expression shifts—not evasion, but consideration.{/i} Time and observation. You could have leveraged your position. Used your skills as bargaining chips. Held back when things got dangerous. You didn't. That told me what I needed to know."
    jump act1_bonding_elisira_cost_followup

label act1_bonding_elisira_cost_followup:
    "{i}She's being honest. Not flattering you, just stating what she observed. Trust earned through action, not words.{/i}"
    menu:
        "'I appreciate that. Knowing where I stand.'":
            $ game_state.set_flag("elisira_bonded")
            $ relationship_manager.process_reputation_affinity("elisira", 3)
            jump act1_bonding_elisira_accept_after_cost
        "'I... wasn't sure you noticed.'":
            jump act1_bonding_elisira_vulnerability

label act1_bonding_elisira_accept_after_cost:
    avyanna "I appreciate that. Knowing where I stand."
    jump act1_bonding_elisira_elisira_acceptance

label act1_bonding_elisira_vulnerability:
    avyanna "I... wasn't sure you noticed. Or if it mattered."
    jump act1_bonding_elisira_elisira_vulnerability_response

label act1_bonding_elisira_elisira_vulnerability_response:
    $ game_state.set_flag("elisira_bonded")
    $ relationship_manager.process_reputation_affinity("elisira", 3)
    elisira "{i}A rare softness in her expression.{/i} I notice. Elia notices. We both do. You matter. Your contributions matter. {i}A pause.{/i} That's why I'm telling you this."
    jump act1_bonding_elisira_vulnerability_accept

label act1_bonding_elisira_vulnerability_accept:
    avyanna "{i}Something loosens in your chest. Relief, maybe. Or the beginning of belonging.{/i} Thank you."
    jump act1_bonding_elisira_elisira_acceptance

label act1_bonding_elisira_test_refusal:
    avyanna "And if I wanted to leave? What happens then?"
    jump act1_bonding_elisira_elisira_refusal_answer

label act1_bonding_elisira_elisira_refusal_answer:
    $ relationship_manager.process_reputation_affinity("elisira", 2)
    elisira "{i}She meets your eyes. No threat. No pressure. Just information.{/i} We'd drop you at the next station. Give you a stipend for transit and lodging. Provide references if you need work. {i}A beat.{/i} You'd leave as crew, not as a liability. The trust doesn't reverse just because you choose a different path."
    jump act1_bonding_elisira_refusal_response

label act1_bonding_elisira_refusal_response:
    "{i}She means it. You can see it in the way she's already mentally planning the logistics—not with resentment, but with the same care she'd give any crew member. The trust is real. And it's yours to keep, even if you leave.{/i}"
    menu:
        "'I'm not going anywhere. Just... needed to know.'":
            $ game_state.set_flag("elisira_bonded")
            $ relationship_manager.process_reputation_affinity("elisira", 3)
            jump act1_bonding_elisira_accept_after_test
        "'That's... good to know. Thank you.'":
            jump act1_bonding_elisira_measured_acceptance

label act1_bonding_elisira_accept_after_test:
    avyanna "I'm not going anywhere. Just... needed to know the boundaries were real."
    jump act1_bonding_elisira_elisira_acceptance

label act1_bonding_elisira_measured_acceptance:
    avyanna "That's... good to know. Thank you for being clear about it."
    jump act1_bonding_elisira_elisira_measured_response

label act1_bonding_elisira_elisira_measured_response:
    $ game_state.set_flag("elisira_bonded")
    $ relationship_manager.process_reputation_affinity("elisira", 2)
    elisira "{i}A nod.{/i} Autonomy matters. You're crew, not property. I want you to know that explicitly. {i}She turns to leave.{/i} The choice is always yours."
    return
