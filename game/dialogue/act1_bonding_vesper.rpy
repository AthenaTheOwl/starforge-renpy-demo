## act1_bonding_vesper.rpy — Auto-generated from act1_bonding_vesper.json
## 31 dialogue nodes

label act1_bonding_vesper:
    $ game_state.mark_dialogue_played("act1_bonding_vesper")
    jump act1_bonding_vesper_start

label act1_bonding_vesper_start:
    "The safehouse is a ruin of broken permacrete and charred datascreens. Vesper kneels beside a cracked relay terminal, cataloging damage with the precision of someone who counts every cost.

Avyanna approaches, footsteps careful on debris. The mission went clean — mostly. But Vesper's silence feels weighted."
    jump act1_bonding_vesper_opening

label act1_bonding_vesper_opening:
    vesper "That exit vector you chose. {i}Third-floor balcony, not the ground entrance.{/i} Smart."
    jump act1_bonding_vesper_opening_response

label act1_bonding_vesper_opening_response:
    menu:
        "You were watching my positioning?":
            jump act1_bonding_vesper_watching_confirm
        "Ground was a killbox. Seemed obvious.":
            jump act1_bonding_vesper_tactical_mind
        "{i}Say nothing. Wait.{/i}":
            jump act1_bonding_vesper_silence_noted

label act1_bonding_vesper_watching_confirm:
    vesper "I watch everyone's positioning. It's what keeps us alive. But you? You weren't just following orders. You were {i}reading the field{/i}."
    jump act1_bonding_vesper_assessment

label act1_bonding_vesper_tactical_mind:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Obvious to someone who understands sightlines and crossfire. Most people panic when the shooting starts. You {i}calculate{/i}."
    jump act1_bonding_vesper_assessment

label act1_bonding_vesper_silence_noted:
    vesper "{i}Vesper's eyes flick up — sharp, assessing.{/i}

Careful. That's good. But you don't have to guard yourself here. Not with me."
    jump act1_bonding_vesper_assessment

label act1_bonding_vesper_assessment:
    vesper "The way you moved when their reinforcements arrived. You didn't freeze. You pivoted, reassessed, took the high ground. That's not luck. That's instinct."
    jump act1_bonding_vesper_assessment_choice

label act1_bonding_vesper_assessment_choice:
    menu:
        "[Tactics] Break down the engagement angles":
            $ _sc_result = skill_check("tactics", 10, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_bonding_vesper_skill_check_tactics_success
            else:
                jump act1_bonding_vesper_skill_check_tactics_failure
        "Why does it matter?":
            jump act1_bonding_vesper_why_matters
        "I just did what made sense.":
            jump act1_bonding_vesper_modest_deflect

label act1_bonding_vesper_skill_check_tactics_success:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    avyanna "They came from the south corridor — two-man teams, staggered entry. If I'd held the ground floor, I'd be caught between their advance and the primary exit. Balcony gave me elevation, clear retreat, and forced them into a choke point."
    jump act1_bonding_vesper_impressed

label act1_bonding_vesper_skill_check_tactics_failure:
    avyanna "I saw them coming from the corridor... it seemed like the balcony was safer? Less exposure, I think."
    jump act1_bonding_vesper_why_matters

label act1_bonding_vesper_why_matters:
    vesper "Because tactical instinct like that? It's rare. And it's {i}wasted{/i} if it's not refined."
    jump act1_bonding_vesper_offer_lead_in

label act1_bonding_vesper_modest_deflect:
    vesper "What makes sense to you would get most people killed. You're thinking three steps ahead without realizing it."
    jump act1_bonding_vesper_offer_lead_in

label act1_bonding_vesper_impressed:
    vesper "{i}Vesper stands, brushing dust from her coat. Her expression shifts — not quite a smile, but something close.{/i}

Exactly. Most people see a firefight. You see a {i}system{/i}. Inputs, variables, outcomes."
    jump act1_bonding_vesper_offer_lead_in

label act1_bonding_vesper_offer_lead_in:
    vesper "I've been doing this for fifteen years. Corps, freelance, wet work I don't talk about. I know talent when I see it."
    jump act1_bonding_vesper_offer

label act1_bonding_vesper_offer:
    vesper "I want to train you. Not as a project — as an investment in someone who already belongs here. Tactical doctrine, engagement planning, threat assessment. The skills that turn instinct into certainty."
    jump act1_bonding_vesper_offer_response

label act1_bonding_vesper_offer_response:
    menu:
        "I accept. Teach me.":
            jump act1_bonding_vesper_acceptance_direct
        "What would you expect from me?":
            jump act1_bonding_vesper_expectations_question
        "Why invest in me specifically?":
            jump act1_bonding_vesper_why_me
        "I need time to think.":
            jump act1_bonding_vesper_need_time

label act1_bonding_vesper_acceptance_direct:
    $ game_state.set_flag("vesper_bonded")
    $ relationship_manager.process_reputation_affinity("vesper", 3)
    vesper "{i}Vesper nods once — crisp, final.{/i}

Good. We start tomorrow. Bring questions, not excuses."
    return

label act1_bonding_vesper_expectations_question:
    vesper "Honesty. Focus. The willingness to admit when you're wrong — and the discipline to fix it. I don't train people who waste my time."
    jump act1_bonding_vesper_expectations_followup

label act1_bonding_vesper_expectations_followup:
    menu:
        "I can do that. Let's begin.":
            jump act1_bonding_vesper_acceptance_after_expectations
        "That's a lot to ask.":
            jump act1_bonding_vesper_lot_to_ask

label act1_bonding_vesper_acceptance_after_expectations:
    $ game_state.set_flag("vesper_bonded")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "Then we have an understanding. Tomorrow, 0600. Don't be late."
    return

label act1_bonding_vesper_lot_to_ask:
    vesper "It is. But you've already been doing it without knowing. I'm just making it {i}conscious{/i}."
    jump act1_bonding_vesper_lot_to_ask_choice

label act1_bonding_vesper_lot_to_ask_choice:
    menu:
        "Alright. I'm in.":
            jump act1_bonding_vesper_acceptance_after_hesitation
        "I need to consider this.":
            jump act1_bonding_vesper_patience

label act1_bonding_vesper_acceptance_after_hesitation:
    $ game_state.set_flag("vesper_bonded")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Smart choice. We'll make you sharper than any blade in the void."
    return

label act1_bonding_vesper_why_me:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Because you remind me of someone I used to know. Someone who died because they had instinct but not {i}discipline{/i}. I won't let that happen twice."
    jump act1_bonding_vesper_why_me_followup

label act1_bonding_vesper_why_me_followup:
    menu:
        "Then I won't let you down.":
            jump act1_bonding_vesper_acceptance_honor
        "I'm not them.":
            jump act1_bonding_vesper_not_them

label act1_bonding_vesper_acceptance_honor:
    $ game_state.set_flag("vesper_bonded")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}Vesper's hand rests briefly on Clarity's grip — a gesture of trust.{/i}

I know you won't. Tomorrow. 0600."
    return

label act1_bonding_vesper_not_them:
    vesper "No. You're not. And that's exactly why this matters. You get to {i}survive{/i}."
    jump act1_bonding_vesper_not_them_choice

label act1_bonding_vesper_not_them_choice:
    menu:
        "Alright. Teach me.":
            jump act1_bonding_vesper_acceptance_survival
        "I need time.":
            jump act1_bonding_vesper_patience

label act1_bonding_vesper_acceptance_survival:
    $ game_state.set_flag("vesper_bonded")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Good. We start at dawn."
    return

label act1_bonding_vesper_need_time:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Fair. This isn't a small thing. But don't take {i}too{/i} long — instinct without training gets people killed."
    return

label act1_bonding_vesper_patience:
    vesper "Take your time. The offer stands. But remember — in this life, hesitation is measured in bodies."
    return
