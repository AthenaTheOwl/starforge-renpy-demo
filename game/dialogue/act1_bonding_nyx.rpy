## act1_bonding_nyx.rpy — Auto-generated from act1_bonding_nyx.json
## 29 dialogue nodes

label act1_bonding_nyx:
    $ game_state.mark_dialogue_played("act1_bonding_nyx")
    jump act1_bonding_nyx_start

label act1_bonding_nyx_start:
    "{i}Abandoned memorial shrine. Candles long dead. Dust settling on offerings no one remembers. Nyx stands at the center, fingers tracing patterns in the air—not physically moving debris, but doing something to the space itself. She doesn't turn when you approach, but you know she knows you're there.{/i}"
    jump act1_bonding_nyx_nyx_acknowledgment

label act1_bonding_nyx_nyx_acknowledgment:
    nyx "{i}Still focused on her work, voice calm and distant.{/i} The lattice here is knotted. Someone died badly. The echo hasn't settled. {i}Finally turning to face you.{/i} You feel it too. I can tell by how you're standing."
    jump act1_bonding_nyx_avyanna_response_acknowledgment

label act1_bonding_nyx_avyanna_response_acknowledgment:
    avyanna "{i}The presence behind my eyes has been restless since we entered. Something in this place resonates wrong.{/i} I feel... something. I don't know what."
    jump act1_bonding_nyx_nyx_observation

label act1_bonding_nyx_nyx_observation:
    nyx "Grief. Old and unprocessed. It saturates the space. {i}A pause, head tilting slightly.{/i} You're sensitive to it. The thing in your chest makes you a receiver for resonances most people can't detect. {i}Meeting your eyes directly.{/i} That's dangerous. But also valuable."
    menu:
        "[Empathy] Try to understand what she's feeling here.":
            $ _sc_result = skill_check("empathy", 10, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_bonding_nyx_empathy_success
            else:
                jump act1_bonding_nyx_empathy_failure
        "Why are you here? What are you doing?":
            jump act1_bonding_nyx_ask_purpose
        "The thing in my chest... what do you know about it?":
            jump act1_bonding_nyx_ask_shard

label act1_bonding_nyx_empathy_success:
    "{i}You watch Nyx more carefully. The way she holds herself—precise, controlled, but there's tension underneath. She's not just observing the grief in this space. She's holding herself separate from it. Deliberately. Like someone who knows what it's like to be consumed by emotion and refuses to let it happen again.{/i}"
    jump act1_bonding_nyx_empathy_insight

label act1_bonding_nyx_empathy_insight:
    avyanna "You're not fixing this because it's a problem. You're fixing it because leaving grief unresolved... that hurts you. Personally."
    jump act1_bonding_nyx_nyx_surprised

label act1_bonding_nyx_nyx_surprised:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "{i}Something flickers across her face—surprise, then a slow, considering nod.{/i} Yes. Unresolved resonance creates... noise. It makes the lattice harder to read. Harder to think through. {i}A pause, quieter.{/i} And yes, it bothers me. I prefer elegance to chaos."
    jump act1_bonding_nyx_offer_training

label act1_bonding_nyx_empathy_failure:
    "{i}You try to read Nyx's emotional state, but she's too controlled. Whatever she's feeling, it's locked away behind layers of discipline and distance.{/i}"
    jump act1_bonding_nyx_empathy_uncertain

label act1_bonding_nyx_empathy_uncertain:
    avyanna "I can't tell what you're feeling. You're too... calm."
    jump act1_bonding_nyx_nyx_explanation

label act1_bonding_nyx_nyx_explanation:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}A slight smile, not quite warm but not cold either.{/i} That's intentional. Emotional regulation is necessary when you manipulate reality. Too much feeling, and the lattice responds unpredictably. {i}A beat.{/i} But you're right to look. Most people don't try."
    jump act1_bonding_nyx_offer_training

label act1_bonding_nyx_ask_purpose:
    avyanna "Why are you here? What are you doing?"
    jump act1_bonding_nyx_nyx_purpose_answer

label act1_bonding_nyx_nyx_purpose_answer:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "Cleaning. Someone left damage here—emotional, lattice-level. If I don't smooth it out, it'll compound. Create interference. Eventually collapse into something worse. {i}Gesturing at the space.{/i} This is maintenance. The universe prefers order, but it won't enforce it on its own."
    jump act1_bonding_nyx_offer_training

label act1_bonding_nyx_ask_shard:
    avyanna "The thing in my chest... what do you know about it?"
    jump act1_bonding_nyx_nyx_shard_answer

label act1_bonding_nyx_nyx_shard_answer:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Direct, clinical.{/i} It's old. Primordial, probably. Not hostile—it's had plenty of opportunities to harm you and hasn't. But it's learning. Adapting to you. {i}A pause.{/i} The question isn't what it wants. It's what you'll become together."
    jump act1_bonding_nyx_offer_training

label act1_bonding_nyx_offer_training:
    nyx "{i}She finishes whatever she was doing to the space. The air feels clearer, less oppressive.{/i} I've been meaning to start your resonance training. You're already sensing more than you realize. {i}Meeting your eyes again.{/i} I'd rather you understood it than feared it."
    jump act1_bonding_nyx_avyanna_training_reaction

label act1_bonding_nyx_avyanna_training_reaction:
    "{i}Training. Not study, not observation—teaching. Nyx is offering to share her expertise, crew helping crew. But her careful distance remains. This is trust, but measured. Extended only as far as you're willing to meet her.{/i}"
    menu:
        "Accept. 'I want to understand. Teach me.'":
            $ game_state.set_flag("nyx_bonded")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_bonding_nyx_accept_immediate
        "Ask about trust. 'Would you trust me with this? Given what's inside me?'":
            jump act1_bonding_nyx_ask_trust
        "Express fear. 'What if I can't control it? What if I hurt someone?'":
            jump act1_bonding_nyx_express_fear

label act1_bonding_nyx_accept_immediate:
    avyanna "I want to understand. Teach me. {i}The words feel like choosing to face the thing you've been avoiding.{/i}"
    jump act1_bonding_nyx_nyx_acceptance

label act1_bonding_nyx_nyx_acceptance:
    nyx "{i}A nod. Simple. Final.{/i} Good. We'll start with resonance awareness exercises. Learning to distinguish your feelings from lattice feedback. {i}A pause, something almost gentle.{/i} You won't be alone in this. I understand what it's like to carry something vast."
    return

label act1_bonding_nyx_ask_trust:
    avyanna "Would you trust me with this? Given what's inside me? Knowing it could be dangerous?"
    jump act1_bonding_nyx_nyx_trust_answer

label act1_bonding_nyx_nyx_trust_answer:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}She considers the question seriously.{/i} Trust is provisional. It's built through consistent behavior, not granted wholesale. {i}A beat.{/i} But yes, I trust you. Provisionally. Because you're asking the question. Because you're worried about harming others. That suggests a moral framework I can work with."
    jump act1_bonding_nyx_trust_followup

label act1_bonding_nyx_trust_followup:
    "{i}It's not the warm reassurance you might have wanted. But it's honest. Nyx isn't pretending the risk doesn't exist. She's just willing to work with you on managing it.{/i}"
    menu:
        "'That's fair. I'll work to earn more than provisional trust.'":
            $ game_state.set_flag("nyx_bonded")
            $ relationship_manager.process_reputation_affinity("nyx", 3)
            jump act1_bonding_nyx_accept_after_trust
        "'I need time to think about this.'":
            jump act1_bonding_nyx_need_time

label act1_bonding_nyx_accept_after_trust:
    avyanna "That's fair. I'll work to earn more than provisional trust."
    jump act1_bonding_nyx_nyx_acceptance

label act1_bonding_nyx_express_fear:
    avyanna "What if I can't control it? What if I hurt someone? The crew. You."
    jump act1_bonding_nyx_nyx_fear_response

label act1_bonding_nyx_nyx_fear_response:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Her expression shifts—not dismissive, but firm.{/i} Then we'll work on control together. The thing inside you responds to your intent, your emotional state. {i}A pause.{/i} Fear is reasonable. But it's not predictive. You haven't hurt anyone yet. That suggests the entity aligns with your values, not against them."
    jump act1_bonding_nyx_fear_followup

label act1_bonding_nyx_fear_followup:
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "Besides, I can contain lattice-level threats. If you lose control, I'll intervene. You're not doing this unsupervised. {i}Something almost warm in her voice.{/i} You're not alone with this burden."
    jump act1_bonding_nyx_fear_decision

label act1_bonding_nyx_fear_decision:
    "{i}She means it. You can see it in the steadiness of her gaze. She's not afraid of you. She's prepared to help you. There's a difference.{/i}"
    menu:
        "'Then I'll trust you to help me. I accept.'":
            $ game_state.set_flag("nyx_bonded")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_bonding_nyx_accept_after_fear
        "'I appreciate that. But I still need time.'":
            jump act1_bonding_nyx_need_time

label act1_bonding_nyx_accept_after_fear:
    avyanna "Then I'll trust you to help me. I accept."
    jump act1_bonding_nyx_nyx_acceptance

label act1_bonding_nyx_need_time:
    avyanna "I need some time. To think about this."
    jump act1_bonding_nyx_nyx_patience

label act1_bonding_nyx_nyx_patience:
    nyx "{i}A nod, no disappointment.{/i} Time is reasonable. Take what you need. {i}She returns to examining the shrine, already refocusing on the lattice work.{/i} Find me when you've decided."
    return
