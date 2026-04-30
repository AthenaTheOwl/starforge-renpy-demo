## act1_bonding_rho.rpy — Auto-generated from act1_bonding_rho.json
## 28 dialogue nodes

label act1_bonding_rho:
    $ game_state.mark_dialogue_played("act1_bonding_rho")
    jump act1_bonding_rho_start

label act1_bonding_rho_start:
    "The galley is quiet after the chaos. Emergency lights have dimmed to normal. Rho sits at the table, his massive frame somehow fitting into the corner booth. His rotary cannon rests against the wall, within reach but not threatening. He looks up as you enter."
    jump act1_bonding_rho_rho_opening

label act1_bonding_rho_rho_opening:
    rho "Sit. I've been meaning to talk to you."
    jump act1_bonding_rho_avyanna_sits

label act1_bonding_rho_avyanna_sits:
    "You slide into the booth across from him. Up close, you can see the wear on his armor—scratches that tell stories, scorch marks that whisper of close calls. His eyes are tired but warm."
    jump act1_bonding_rho_rho_reflection

label act1_bonding_rho_rho_reflection:
    rho "I've been watching how you handle things. The crew, the fights, the hard calls. You don't flinch. You don't run. That matters more than you know."
    jump act1_bonding_rho_rho_continues

label act1_bonding_rho_rho_continues:
    rho "I don't say this to everyone who walks onto this ship. Hell, I barely say it at all. But you're already one of us, Avyanna. I wanted you to know what that means. {i}What it really means.{/i}"
    menu:
        "What does it cost you?":
            jump act1_bonding_rho_ask_cost
        "Why does loyalty matter so much to you?":
            jump act1_bonding_rho_ask_loyalty
        "What comes first for you—mission or crew?":
            jump act1_bonding_rho_ask_priorities

label act1_bonding_rho_ask_cost:
    rho "Cost? {i}Everything.{/i} I keep count, you know. Every life I've taken. Forty-seven souls before I met this crew. Seventy-three now. Each one a weight I carry. Each one a choice I made to protect the people who matter."
    jump act1_bonding_rho_cost_reflection

label act1_bonding_rho_cost_reflection:
    rho "Some nights I see their faces. Raiders, corpo enforcers, cultists—doesn't matter. They all had names once. But I'd do it again. Every single time. Because the alternative is losing someone I care about."
    menu:
        "That's a heavy burden to bear.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_heavy_burden
        "You shouldn't have to carry that alone.":
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_bonding_rho_not_alone
        "At least you remember them.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_remembering

label act1_bonding_rho_ask_loyalty:
    rho "Because I've seen what happens when it breaks. I came up through the Frontier Militia—good people, strong bonds. Then command decided we were expendable. Sent us into a meat grinder for a corpo contract."
    jump act1_bonding_rho_loyalty_story

label act1_bonding_rho_loyalty_story:
    rho "Lost half my squad in an hour. The other half scattered to the void when they realized we'd been sold. I found this crew after that. Nyx doesn't trade lives for credits. She fights {i}for{/i} us, not {i}with{/i} us."
    menu:
        "Trust is earned through action.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_trust_earned
        "You've built something better here.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_something_better
        "I understand that kind of betrayal.":
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_bonding_rho_shared_betrayal

label act1_bonding_rho_ask_priorities:
    rho "Crew. Always crew. The mission can go to hell if it means saving one of ours. Some people call that soft. I call it human."
    jump act1_bonding_rho_priorities_explanation

label act1_bonding_rho_priorities_explanation:
    rho "We're not corpo drones. We're not disposable assets. Every person on this ship chose to be here, and I choose them back. Every. Single. Day. That's what makes us strong—not firepower, not tactics. {i}Trust.{/i}"
    menu:
        "That's a dangerous way to fight.":
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_bonding_rho_dangerous_way
        "It's also what keeps us alive.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_keeps_alive
        "I'd make the same choice.":
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_bonding_rho_same_choice

label act1_bonding_rho_heavy_burden:
    rho "It is. But burdens are easier when you're not carrying them for nothing. I carry mine for people like you. For Nyx, Vesper, Jalen. Makes the weight bearable."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_not_alone:
    rho "{i}His expression softens.{/i} Maybe I don't anymore. That's... that's new. Thank you for that, Avyanna."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_remembering:
    rho "Yeah. I owe them that much. Every name, every face—it's a promise I made to myself. I won't forget the cost of protecting what matters."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_trust_earned:
    rho "Exactly. And you've earned it. The way you fight, the way you stand with us—that's not something I see often. You're solid, Avyanna."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_something_better:
    rho "We have. And now you're part of it. That's not small. That's everything."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_shared_betrayal:
    rho "{i}He meets your eyes, recognition flashing there.{/i} Then you know why I'll never let it happen again. Not to you. Not to anyone on this ship."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_dangerous_way:
    rho "Maybe. But I've seen the alternative—cold, calculated, everyone expendable. I'd rather die fighting for people I love than live treating them like assets."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_keeps_alive:
    rho "Exactly. We watch each other's backs because we {i}care{/i}, not because it's tactical. That's the difference between surviving and living."
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_same_choice:
    rho "{i}He grins—genuine, warm.{/i} I knew you would. That's why I'm telling you this. You're not just here because you can fight. You're here because you're {i}one of us.{/i}"
    jump act1_bonding_rho_core_reveal

label act1_bonding_rho_core_reveal:
    rho "Listen. You're already crew—that's not in question. I just wanted you to know what that means to me. It means I'll fight for you. Bleed for you if it comes to it. And I hope... I hope you'll fight for us too."
    jump act1_bonding_rho_final_choice

label act1_bonding_rho_final_choice:
    "Rho's hand rests on the table between you—not reaching, just open. The weight of his words settles in the quiet galley. This is more than acceptance. This is {i}belonging.{/i}"
    menu:
        "I'm with you. All of you. No matter what.":
            $ game_state.set_flag("rho_bonded")
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_bonding_rho_full_commitment
        "I'll fight for us. But I won't lie—it scares me.":
            $ game_state.set_flag("rho_bonded")
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_bonding_rho_honest_commitment
        "I need time to understand what that means.":
            $ relationship_manager.process_reputation_affinity("rho", -3)
            jump act1_bonding_rho_need_time

label act1_bonding_rho_full_commitment:
    $ game_state.set_flag("rho_solidified")
    rho "{i}His grin splits wide, armor crinkling as he relaxes.{/i} That's what I needed to hear. Welcome home, Avyanna. For real this time."
    jump act1_bonding_rho_full_commitment_end

label act1_bonding_rho_full_commitment_end:
    "Rho stands, picking up his cannon with practiced ease. He pauses at the doorway, looking back. The weight of his seventy-three souls seems lighter, somehow. Shared."
    return

label act1_bonding_rho_honest_commitment:
    $ game_state.set_flag("rho_solidified")
    rho "Good. Fear means you understand the stakes. I'd be worried if you weren't scared. But you're here anyway—that's what courage looks like."
    jump act1_bonding_rho_honest_commitment_end

label act1_bonding_rho_honest_commitment_end:
    "Rho stands, picking up his cannon with practiced ease. He pauses at the doorway, looking back. The weight of his seventy-three souls seems lighter, somehow. Shared."
    return

label act1_bonding_rho_need_time:
    rho "{i}He nods slowly, understanding in his eyes.{/i} Fair enough. Door's open when you're ready. Just... don't take too long. This galaxy doesn't wait for anyone."
    jump act1_bonding_rho_need_time_end

label act1_bonding_rho_need_time_end:
    "Rho stands, picking up his cannon with practiced ease. He pauses at the doorway, looking back. The weight of his seventy-three souls seems lighter, somehow. Shared."
    return
