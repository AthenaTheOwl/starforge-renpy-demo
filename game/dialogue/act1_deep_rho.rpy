## act1_deep_rho.rpy — Auto-generated from act1_deep_rho.json
## 118 dialogue nodes

label act1_deep_rho:
    $ game_state.mark_dialogue_played("act1_deep_rho")
    jump act1_deep_rho_start

label act1_deep_rho_start:
    "The armory is cold, lit only by emergency strips along the floor. Rho sits on an ammunition crate, his rotary cannon disassembled on the workbench beside him. He's cleaning the barrel with methodical precision. He doesn't look up when you enter, but his voice carries across the metal chamber."
    jump act1_deep_rho_rho_opening

label act1_deep_rho_rho_opening:
    rho "Can't sleep either?"
    jump act1_deep_rho_avyanna_approaches

label act1_deep_rho_avyanna_approaches:
    "You step closer. In the dim light, you can see the wear on his hands—scars from burns, cuts, a lifetime of handling weapons that bite back. The cannon's barrel gleams, freshly oiled. He still doesn't look at you."
    jump act1_deep_rho_rho_continues

label act1_deep_rho_rho_continues:
    rho "One hundred and twelve."
    jump act1_deep_rho_avyanna_confused

label act1_deep_rho_avyanna_confused:
    "You wait. Rho fits a barrel segment back into place with a click."
    menu:
        "One hundred and twelve what?":
            jump act1_deep_rho_ask_count
        "You don't have to tell me.":
            jump act1_deep_rho_offer_out
        "[Stay silent. Wait for him.]":
            jump act1_deep_rho_patient_silence

label act1_deep_rho_ask_count:
    rho "Lives. People I've killed. I keep count. Always have. Some people forget. I don't."
    jump act1_deep_rho_count_explanation

label act1_deep_rho_offer_out:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He looks up at you for the first time. His eyes are dark, tired.{/i} I know. But I need to. Been carrying this for years. Gets heavy."
    jump act1_deep_rho_count_explanation

label act1_deep_rho_patient_silence:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}He glances at you, something like gratitude in his expression.{/i} One hundred and twelve lives. That's my count. Every person I've put down since I started carrying a gun."
    jump act1_deep_rho_count_explanation

label act1_deep_rho_count_explanation:
    rho "Forty-seven before the Lumen Thief. Sixty-five after. Raiders, enforcers, cultists, husks. Doesn't matter. They were all people once. Most of them still were when I pulled the trigger."
    jump act1_deep_rho_rho_barrel_work

label act1_deep_rho_rho_barrel_work:
    "He sets down the barrel segment and picks up the firing mechanism, turning it over in his hands. His voice stays level, matter-of-fact."
    jump act1_deep_rho_militia_prompt

label act1_deep_rho_militia_prompt:
    rho "First one I ever killed, I was nineteen. Frontier Militia, Third Resettlement Company. Border garrison on Yael's Reach."
    jump act1_deep_rho_militia_prompt_choices

label act1_deep_rho_militia_prompt_choices:
    "{i}He sets the firing mechanism down. His fingers rest flat on the workbench, still. The emergency strips hum beneath the silence.{/i}"
    menu:
        "Frontier Militia? I thought they disbanded decades ago.":
            jump act1_deep_rho_militia_history
        "What was it like out there?":
            jump act1_deep_rho_militia_life
        "[Say nothing. Let him find his own way into it.]":
            jump act1_deep_rho_militia_life

label act1_deep_rho_militia_history:
    rho "Disbanded. Absorbed. Sold off. Depends who you ask. Officially, Central Command folded us into the Reclamation Authority. Unofficially, they auctioned our contracts to the highest bidder and called it restructuring."
    jump act1_deep_rho_militia_life

label act1_deep_rho_militia_life:
    rho "Yael's Reach was nothing. Rock, ice, a settlement of three hundred people trying to scratch something out of frozen soil. We were there to keep the raiders off their backs. Sixteen of us. One squad. That was the whole garrison."
    jump act1_deep_rho_militia_squad

label act1_deep_rho_militia_squad:
    rho "Marcus Teague ran point. Best soldier I ever knew—not because he was fast or deadly, but because he thought about it. Every engagement, every round fired. He made you think about it too."
    jump act1_deep_rho_militia_squad_2

label act1_deep_rho_militia_squad_2:
    rho "Senna Voss handled demolitions. Could rig a charge in the dark, by feel, in under ten seconds. Laughed too loud. Ate too fast. Slept like the dead. {i}He pauses.{/i} Turns out that was prophetic."
    jump act1_deep_rho_militia_squad_3

label act1_deep_rho_militia_squad_3:
    "{i}Rho's hands move to the barrel again, tracing the rifling grooves with one scarred thumb. The motion is automatic—something his body does while his mind is elsewhere.{/i}"
    jump act1_deep_rho_militia_squad_4

label act1_deep_rho_militia_squad_4:
    if game_state.has_flag("rho_mentioned_past"):
        rho "I told you I had people once. Polk, Darien, Asha, Greer, Kotto, Lenn—all sixteen names. I run the roll call in my head some nights. Nobody answers."
    else:
        rho "Polk, Darien, Asha, Greer, Kotto, Lenn. I could name all sixteen. I still do, some nights. Roll call in my head. Nobody answers."
    jump act1_deep_rho_militia_camaraderie

label act1_deep_rho_militia_camaraderie:
    rho "But back then? We were good. Tight. Greer cooked. Badly, but he cooked. Kotto played cards and cheated, and we let him because he lost anyway. Asha sang old colony songs when she was on watch. Off-key. Didn't matter."
    jump act1_deep_rho_militia_camaraderie_2

label act1_deep_rho_militia_camaraderie_2:
    rho "That's what people don't understand about squads. It's not the fighting that binds you. It's the waiting. The boredom. The meals, the bad jokes, the knowing someone's got your flank without asking."
    jump act1_deep_rho_militia_camaraderie_choice

label act1_deep_rho_militia_camaraderie_choice:
    "{i}Something softens in his voice—not warmth, exactly. An echo of warmth. A place where warmth used to live.{/i}"
    menu:
        "Sounds like a family.":
            jump act1_deep_rho_militia_family
        "How long did it last?":
            jump act1_deep_rho_militia_end_prompt
        "I had people like that once, too.":
            jump act1_deep_rho_player_shared_loss_early

label act1_deep_rho_militia_family:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "Don't use that word. {i}His jaw tightens.{/i} Family is blood. What we had was choice. Every morning, we chose to stand next to each other. That's harder. That's rarer."
    jump act1_deep_rho_militia_end_prompt

label act1_deep_rho_player_shared_loss_early:
    $ game_state.set_flag("player_shared_loss_with_rho")
    $ relationship_manager.process_reputation_affinity("rho", 1)
    "{i}Rho looks at you—a quick, measuring glance. He nods, just once, an acknowledgment without words. He doesn't ask. He knows what that sentence costs.{/i}"
    jump act1_deep_rho_militia_end_prompt

label act1_deep_rho_militia_end_prompt:
    rho "Three years on Yael's Reach. Three years keeping those people safe. Then Central Command sent new orders."
    jump act1_deep_rho_betrayal_begins

label act1_deep_rho_betrayal_begins:
    "{i}His hands stop moving. The cloth he's been using to clean the barrel goes still, pressed flat against steel. The silence in the armory thickens.{/i}"
    jump act1_deep_rho_betrayal_orders

label act1_deep_rho_betrayal_orders:
    rho "Redeployment. Effective immediately. Some mining installation on Caldera Nix. Corpo-owned—Meridian Extraction. They'd bought a security contract from Command. We were the product."
    jump act1_deep_rho_betrayal_orders_2

label act1_deep_rho_betrayal_orders_2:
    rho "Marcus pushed back. Sent three formal objections up the chain. Said the intelligence was bad, the extraction zone was hot, the timeline was suicide. Command said acknowledged. Command said proceed."
    jump act1_deep_rho_betrayal_orders_3

label act1_deep_rho_betrayal_orders_3:
    rho "Acknowledged. Proceed. {i}He repeats the words like a liturgy.{/i} Two words. That's all it took to kill eight people."
    jump act1_deep_rho_betrayal_detail

label act1_deep_rho_betrayal_detail:
    "{i}Rho reaches for the cannon's rotary assembly, begins fitting the barrels back into the housing. Each one clicks into place with mechanical precision—the sound of something being rebuilt that was once broken apart.{/i}"
    jump act1_deep_rho_betrayal_mission

label act1_deep_rho_betrayal_mission:
    rho "Caldera Nix was a meat grinder. Meridian knew. Command knew. The miners had unionized, armed themselves with surplus military hardware. Meridian wanted them cleared out, but didn't want corpo fingerprints on the bodies. So they bought militia hands instead."
    jump act1_deep_rho_betrayal_mission_2

label act1_deep_rho_betrayal_mission_2:
    rho "We went in expecting a security sweep. Found fortified positions, crew-served weapons, people fighting for their homes. {i}He exhales slowly.{/i} Sound familiar? We'd been those people. On Yael's Reach, we were the garrison keeping settlers safe. On Caldera Nix, we were the threat."
    jump act1_deep_rho_betrayal_choice

label act1_deep_rho_betrayal_choice:
    "{i}The last barrel slots home. Rho stares at the partially assembled weapon, his reflection fractured across six polished tubes.{/i}"
    menu:
        "You were used.":
            jump act1_deep_rho_betrayal_used
        "Did Marcus follow the order?":
            jump act1_deep_rho_betrayal_marcus
        "What did you do?":
            jump act1_deep_rho_betrayal_rho_action

label act1_deep_rho_betrayal_used:
    rho "Weapon. Tool. Asset. Pick your word. They all mean the same thing—expendable."
    jump act1_deep_rho_betrayal_marcus

label act1_deep_rho_betrayal_marcus:
    rho "Marcus tried to negotiate. Walked into the mine with his hands up, helmet off. Said we didn't have to do this. The miners' leader—woman named Korr—she listened. They were close to a deal."
    jump act1_deep_rho_betrayal_marcus_2

label act1_deep_rho_betrayal_marcus_2:
    rho "Then Meridian's oversight team detonated the charges they'd pre-planted in the south shaft. Buried six miners alive. Made it look like we'd done it. After that, there was no talking."
    jump act1_deep_rho_betrayal_rho_action

label act1_deep_rho_betrayal_rho_action:
    rho "Twelve hours of fighting in tunnels. Close quarters. You can't use a rotary cannon in a tunnel—not without killing everyone, including your own. So I carried a sidearm and a combat blade. Made it personal."
    jump act1_deep_rho_betrayal_losses

label act1_deep_rho_betrayal_losses:
    rho "Kotto went first. Took a shotgun blast through a doorway. Asha dragged him back, but there was nothing left to save. Greer caught a ricochet—fragment through the neck. Bled out while Senna held pressure."
    jump act1_deep_rho_betrayal_losses_2

label act1_deep_rho_betrayal_losses_2:
    rho "Polk and Darien died holding a junction so the rest of us could pull back. We heard them on comms for four minutes. Then we didn't."
    jump act1_deep_rho_betrayal_losses_3

label act1_deep_rho_betrayal_losses_3:
    "{i}Rho's voice hasn't changed—still level, still controlled. But his hands have gone white-knuckled around the cannon housing. The metal groans faintly under his grip.{/i}"
    jump act1_deep_rho_betrayal_marcus_death

label act1_deep_rho_betrayal_marcus_death:
    rho "Marcus took a plasma bolt in the last push. Stepped in front of Lenn. Didn't hesitate. Didn't flinch. Just—moved. Like it was the most natural thing in the world."
    jump act1_deep_rho_betrayal_marcus_death_2

label act1_deep_rho_betrayal_marcus_death_2:
    rho "{i}He sets the cannon down carefully, like something fragile.{/i} He looked at me. Right at me. Didn't say anything. Didn't have to. I knew what he was saying. {i}Keep them alive.{/i}"
    jump act1_deep_rho_betrayal_senna

label act1_deep_rho_betrayal_senna:
    rho "Senna died setting charges to collapse the tunnel behind us. Bought us ninety seconds. She was laughing when the ceiling came down. I still hear it."
    jump act1_deep_rho_aftermath_begin

label act1_deep_rho_aftermath_begin:
    "{i}The armory's emergency strips flicker once—a brief stutter of light that makes the shadows jump. Rho doesn't notice, or doesn't care.{/i}"
    jump act1_deep_rho_aftermath_survivors

label act1_deep_rho_aftermath_survivors:
    rho "Eight of us walked into Caldera Nix as a squad. Eight walked out as strangers. We couldn't look at each other. Couldn't speak. Lenn deserted that night. Took a shuttle and vanished. Don't blame her."
    jump act1_deep_rho_aftermath_scatter

label act1_deep_rho_aftermath_scatter:
    rho "The rest scattered over the next month. Some went freelance. Some crawled into bottles. Ferris ate his sidearm on a station platform in front of fifty people. Nobody stopped him. Nobody even looked up."
    jump act1_deep_rho_aftermath_rho

label act1_deep_rho_aftermath_rho:
    rho "I filed my discharge papers. Command marked me as 'voluntary separation, no benefits.' Three years of service. Eight dead friends. And I walked away with a duffel bag and a cannon they forgot to requisition back."
    jump act1_deep_rho_aftermath_rho_choice

label act1_deep_rho_aftermath_rho_choice:
    "{i}He taps the cannon—two knuckle-raps against the housing, almost affectionate.{/i}"
    menu:
        "That's Proportional. The cannon Command forgot.":
            jump act1_deep_rho_proportional_reveal
        "What did you do after?":
            jump act1_deep_rho_drifting
        "You survived. That has to count for something.":
            jump act1_deep_rho_survival_response

label act1_deep_rho_proportional_reveal:
    rho "Proportional. {i}The ghost of something crosses his face—not quite a smile.{/i} Marcus named it. Said the recoil was proportional to the stupidity of whoever we were pointing it at."
    jump act1_deep_rho_proportional_meaning

label act1_deep_rho_survival_response:
    rho "{i}He shakes his head slowly.{/i} Surviving isn't counting. Surviving is just... still being here. The counting comes later, when you decide what to do with the time they gave you."
    jump act1_deep_rho_drifting

label act1_deep_rho_drifting:
    rho "Drifted for two years. Freelance security. Cargo guard. Whatever kept me moving. Didn't stay anywhere long enough to learn names. Names make it harder."
    jump act1_deep_rho_drifting_2

label act1_deep_rho_drifting_2:
    rho "The count went up. Forty, forty-five, forty-seven. Pirates mostly. Raider crews. People who shot first. I told myself that made it different. {i}He pauses.{/i} It didn't."
    jump act1_deep_rho_proportional_transition

label act1_deep_rho_proportional_transition:
    "{i}Rho lifts Proportional's barrel assembly, sights down its length with one eye closed. The weapon is enormous—meant for suppression platforms, not infantry carry. The fact that he handles it at all speaks to something beyond training.{/i}"
    jump act1_deep_rho_proportional_meaning

label act1_deep_rho_proportional_meaning:
    rho "People think I carry this thing out of sentiment. Big man, big gun, simple story. They're wrong."
    jump act1_deep_rho_proportional_meaning_2

label act1_deep_rho_proportional_meaning_2:
    rho "Proportional is the last piece of Third Resettlement Company that still exists. Every scratch on this housing is a firefight. Every dent is a story. Marcus's handwriting is still on the maintenance log inside the stock plate."
    jump act1_deep_rho_proportional_meaning_3

label act1_deep_rho_proportional_meaning_3:
    rho "I clean it every night because that's what we did. Squad ritual. End of shift, maintain your weapon. Senna always finished first. Kotto always finished last. Marcus inspected every piece himself."
    jump act1_deep_rho_proportional_meaning_4

label act1_deep_rho_proportional_meaning_4:
    if game_state.has_flag("rho_shared_burden"):
        rho "So I clean it. Not sentiment. Remembrance. As long as I maintain this weapon, Third Company still has one soldier doing the nightly check. {i}He glances at you.{/i} Maybe two, now."
    else:
        rho "So I clean it. Not sentiment. Remembrance. As long as I maintain this weapon, Third Company still has one soldier doing the nightly check. As long as I carry it, they're still here."
    jump act1_deep_rho_rho_weight

label act1_deep_rho_rho_weight:
    if game_state.has_flag("dinner_watched_rho"):
        rho "You watched me at dinner. Saw me staring at nothing. This is what I see. One hundred and twelve faces. Some nights they're all I can see."
    else:
        rho "People think heavy weapons means you don't see the details. They're wrong. I see everything. The way they fall. The moment they realize. I carry every one of them."
    menu:
        "Why do you keep count?":
            jump act1_deep_rho_why_count
        "That's a hell of a burden.":
            jump act1_deep_rho_acknowledge_burden
        "They would have killed us.":
            jump act1_deep_rho_justify_kills

label act1_deep_rho_why_count:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "Because forgetting would be easy. Too easy. If I stop counting, I stop being human. I become the weapon. And I've seen what that does to people."
    jump act1_deep_rho_weapon_talk

label act1_deep_rho_acknowledge_burden:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}He nods slowly.{/i} Yeah. But someone has to carry it. Better me than Vesper. Better me than Jalen. They've got enough weight."
    jump act1_deep_rho_weapon_talk

label act1_deep_rho_justify_kills:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "Most of them, yeah. But does that make it easier? Does that make me sleep better? {i}He shakes his head.{/i} No. It just means I'm still alive to keep counting."
    jump act1_deep_rho_weapon_talk

label act1_deep_rho_weapon_talk:
    rho "This cannon. You know why I keep it with me? Why I clean it myself, every night?"
    jump act1_deep_rho_cannon_pause

label act1_deep_rho_cannon_pause:
    "He runs his hand along the firing mechanism, almost tender."
    jump act1_deep_rho_cannon_revelation

label act1_deep_rho_cannon_revelation:
    rho "Because it's the one thing that's never lied to me. It doesn't pretend to be anything but what it is. Doesn't make promises it can't keep. When I pull this trigger, I know exactly what happens."
    jump act1_deep_rho_cannon_continues

label act1_deep_rho_cannon_continues:
    rho "Command lied. Told us we were liberators, heroes. Sent us to die for corpo contracts. My old squad—half of them died believing the lies. The other half died when they realized the truth."
    jump act1_deep_rho_loss_revelation

label act1_deep_rho_loss_revelation:
    rho "I couldn't protect them. Couldn't save Marcus when he took a plasma bolt meant for me. Couldn't save Senna when the ceiling collapsed. Couldn't save {i}any{/i} of them."
    jump act1_deep_rho_finding_crew_transition

label act1_deep_rho_finding_crew_transition:
    "{i}He exhales—a long, controlled breath, the kind a man uses to hold himself together. His hands find Proportional's stock and grip it, knuckles white, steadying himself on the only anchor he trusts.{/i}"
    menu:
        "How did you end up on the Lumen Thief?":
            jump act1_deep_rho_finding_crew
        "I lost people too. Not the same way, but—I understand the weight.":
            jump act1_deep_rho_player_loss_share
        "[Let the silence hold. He'll continue when he's ready.]":
            jump act1_deep_rho_finding_crew

label act1_deep_rho_player_loss_share:
    $ game_state.set_flag("player_shared_loss_with_rho")
    $ relationship_manager.process_reputation_affinity("rho", 1)
    "{i}Rho goes still. He doesn't look at you, but something shifts in the set of his shoulders—a tension releasing, barely perceptible. He nods. Once.{/i}"
    jump act1_deep_rho_player_loss_response

label act1_deep_rho_player_loss_response:
    rho "I know. {i}Two words, but they carry everything—recognition, respect, the understanding that some things don't need elaboration.{/i} I know you do."
    jump act1_deep_rho_finding_crew

label act1_deep_rho_finding_crew:
    rho "Docked at Venn Station for a resupply. Broke. Out of contracts. Hadn't spoken to another person in eleven days. Walked into a bar and Nyx was there, arguing with a dock foreman twice her size about fuel prices."
    jump act1_deep_rho_finding_crew_2

label act1_deep_rho_finding_crew_2:
    rho "She was losing the argument. Badly. But she didn't back down. Didn't bluff, didn't threaten. Just kept talking. Kept pushing. Foreman eventually dropped his price out of sheer exhaustion."
    jump act1_deep_rho_finding_crew_3

label act1_deep_rho_finding_crew_3:
    rho "{i}Something that might be amusement crosses his face.{/i} She saw me watching. Walked over. Said, 'You look like you need a job and a meal, in that order.' She was right about both."
    jump act1_deep_rho_finding_crew_4

label act1_deep_rho_finding_crew_4:
    rho "First job was a cargo run. Simple. Legal, even. Halfway through, we got hit by raiders. Three ships. Nyx didn't panic. Vesper didn't panic. Jalen—he was already aboard by then—he just started prepping the guns like it was Tuesday."
    jump act1_deep_rho_finding_crew_5

label act1_deep_rho_finding_crew_5:
    rho "Nobody gave me orders. Nobody told me where to stand. Nyx just looked at me and said, 'You know what to do.' And I did. Proportional did the rest."
    jump act1_deep_rho_why_stayed

label act1_deep_rho_why_stayed:
    "{i}He sets the firing mechanism back into its housing. The assembly is almost complete now—Proportional taking shape under his hands like a ritual nearing its conclusion.{/i}"
    jump act1_deep_rho_why_stayed_2

label act1_deep_rho_why_stayed_2:
    rho "After the fight, Nyx didn't debrief me. Didn't file a report. She poured two drinks and asked if I wanted to stay. Not 'we need your gun.' Not 'you're useful.' Just—'do you want to stay?'"
    jump act1_deep_rho_why_stayed_3

label act1_deep_rho_why_stayed_3:
    rho "Nobody had asked me what I wanted in years. I forgot people did that."
    jump act1_deep_rho_loyalty_philosophy

label act1_deep_rho_loyalty_philosophy:
    rho "Loyalty. {i}He says the word like he's testing a blade's edge.{/i} Command used that word. Said it a lot. Loyalty to the service. Loyalty to the mission. Means nothing when the people saying it are selling your blood by the liter."
    jump act1_deep_rho_loyalty_philosophy_2

label act1_deep_rho_loyalty_philosophy_2:
    rho "Real loyalty isn't given. It's earned. Slowly. Through a hundred small moments where someone could have lied and didn't. Could have left and stayed. Could have looked away and chose to see."
    jump act1_deep_rho_loyalty_philosophy_3

label act1_deep_rho_loyalty_philosophy_3:
    if game_state.has_flag("elisira_conflict_resolved"):
        rho "Nyx earned it. Vesper earned it. Jalen earned it every time he pulled someone out of fire instead of returning it. Elisira and I don't always agree, but she showed up when it mattered. That's enough."
    else:
        rho "Nyx earned it. Vesper earned it. Jalen earned it every time he pulled someone out of fire instead of returning it. Even Elisira—she's difficult, but she's honest about it. I respect that."
    jump act1_deep_rho_empathy_check

label act1_deep_rho_empathy_check:
    "His hands have stopped moving. The firing mechanism rests in his lap, forgotten. His shoulders carry a weight that has nothing to do with armor."
    menu:
        "[Empathy DC 12] You carry their weight because you loved them.":
            $ _sc_result = skill_check("empathy", 12, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_rho_empathy_success
            else:
                jump act1_deep_rho_empathy_fail_soft
        "You can't protect everyone.":
            jump act1_deep_rho_empathy_fail
        "What would they want you to do?":
            jump act1_deep_rho_empathy_neutral
        "Maybe the guilt isn't yours to carry. Command gave the order.":
            jump act1_deep_rho_challenge_guilt

label act1_deep_rho_empathy_roll:
    "{i}The words land in the silence between you.{/i}"
    jump act1_deep_rho_empathy_success

label act1_deep_rho_challenge_guilt:
    rho "{i}His jaw tightens.{/i} Command pulled the trigger on the contract. I pulled the trigger on the gun. Both of us killed them. Blaming command doesn't wash the blood off my hands. It just gives it somewhere else to drip."
    jump act1_deep_rho_challenge_guilt_2

label act1_deep_rho_challenge_guilt_2:
    "{i}He looks at you, and there's something hard in his eyes—not anger, but a refusal to be absolved.{/i}"
    menu:
        "There's a difference between guilt and responsibility. You know the difference.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_deep_rho_challenge_guilt_insight
        "Fair enough. I won't try to take it from you.":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_deep_rho_challenge_guilt_respect

label act1_deep_rho_challenge_guilt_insight:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He's quiet for a long time. When he speaks, the hardness is gone.{/i} Responsibility. Yeah. Maybe that's the word I've been looking for. Guilt is a cage. Responsibility is a direction."
    jump act1_deep_rho_core_question

label act1_deep_rho_challenge_guilt_respect:
    rho "{i}He nods, and something in him eases—not because you agreed, but because you stopped pushing.{/i} Good. Don't try. It's mine. But... thanks for seeing it clearly."
    jump act1_deep_rho_core_question

label act1_deep_rho_empathy_success:
    $ game_state.set_flag("rho_shared_burden")
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}His breath catches. He looks at you—really looks—and something breaks behind his eyes.{/i} Yeah. Yeah, I did. And that's why it hurts. Because they mattered. Because losing them {i}meant something.{/i}"
    jump act1_deep_rho_empathy_success_continue

label act1_deep_rho_empathy_fail_soft:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He looks at you, then away. The moment passes—whatever door might have opened stays closed, but not locked.{/i} Maybe. Maybe that's part of it."
    jump act1_deep_rho_core_question

label act1_deep_rho_empathy_success_continue:
    rho "I never... I never said that out loud before. That I loved them. That it still hurts. {i}He closes his eyes.{/i} Thank you. For understanding that."
    jump act1_deep_rho_core_question

label act1_deep_rho_empathy_fail:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "I know. Doesn't make it easier. Doesn't make the weight lighter. Just means I keep carrying it."
    jump act1_deep_rho_core_question

label act1_deep_rho_empathy_neutral:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He considers this.{/i} Marcus would tell me to stop being a damn martyr. Senna would laugh and say I'm too stubborn to die anyway. Maybe they'd be right."
    jump act1_deep_rho_core_question

label act1_deep_rho_core_question:
    rho "So why do I stay here? Why do I keep doing this? One hundred and twelve lives, Avyanna. What makes one hundred and thirteen worth it?"
    jump act1_deep_rho_core_pause

label act1_deep_rho_core_pause:
    "The question hangs between you. This is the heart of it—the reason he's telling you all of this."
    menu:
        "Because the Lumen Thief is different. This crew is worth it.":
            jump act1_deep_rho_crew_worth
        "Because you still have people to protect.":
            jump act1_deep_rho_protection_worth
        "Because you're looking for redemption.":
            jump act1_deep_rho_redemption_worth
        "I don't know. Maybe you shouldn't.":
            jump act1_deep_rho_challenge_worth

label act1_deep_rho_crew_worth:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}He nods slowly.{/i} Nyx doesn't trade lives. Vesper sees people, not assets. Jalen fights like every life matters—even the enemy's. That's rare out here. That's worth protecting."
    jump act1_deep_rho_why_matters

label act1_deep_rho_protection_worth:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "Yeah. And you're one of them now. That's not small. That's everything. Every person I protect—every person who makes it home—that's why I keep counting. Because they matter."
    jump act1_deep_rho_why_matters

label act1_deep_rho_redemption_worth:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He shakes his head.{/i} Not redemption. Can't redeem one hundred and twelve lives. But maybe... maybe I can make them mean something. Make sure they weren't wasted on lies."
    jump act1_deep_rho_why_matters

label act1_deep_rho_challenge_worth:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}His eyes narrow, then soften.{/i} You're asking if I've thought about stopping. Yeah. Every day. But then I remember—if I stop, who protects them? Who carries the weight so they don't have to?"
    jump act1_deep_rho_why_matters

label act1_deep_rho_why_matters:
    rho "I stay because this crew needs someone willing to do the hard thing. Someone who'll stand between them and the void and say 'not today.' That's me. That's what I'm good at."
    jump act1_deep_rho_cannon_matters

label act1_deep_rho_cannon_matters:
    if game_state.has_flag("trust_intervention_attempted"):
        rho "You tried to save someone back in the ruins. Tried to pull them back from the edge. That's who you are. {i}He taps the cannon.{/i} This is who I am. We both protect people. Just different methods."
    else:
        rho "And this cannon—this ugly, brutal, honest piece of metal—it's the tool I use to keep them safe. It doesn't lie. It doesn't pretend. When I fire it, I know exactly what I'm choosing."
    jump act1_deep_rho_rho_question

label act1_deep_rho_rho_question:
    rho "Here's what I need to know, Avyanna. Really know. When it comes down to it—when the count goes to one hundred and thirteen, one hundred and twenty, one hundred and fifty—can you stand next to someone like me?"
    jump act1_deep_rho_rho_question_clarify

label act1_deep_rho_rho_question_clarify:
    rho "Can you fight beside someone who counts their kills? Who carries the weight of every trigger pull? Because that's who I am. And I need to know if that changes how you see me."
    menu:
        "You're not defined by your kill count. You're defined by who you protect.":
            $ game_state.set_flag("deep_rho_complete")
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_deep_rho_accept_burden
        "I see someone who refuses to forget. That takes courage.":
            $ game_state.set_flag("deep_rho_complete")
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_deep_rho_accept_memory
        "I see a weapon trying to be human. I respect the struggle.":
            $ game_state.set_flag("deep_rho_complete")
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_deep_rho_accept_struggle
        "I see someone carrying too much. Let me help.":
            $ game_state.set_flag("deep_rho_complete")
            $ relationship_manager.process_reputation_affinity("rho", 2)
            jump act1_deep_rho_offer_help

label act1_deep_rho_accept_burden:
    rho "{i}His shoulders drop—not in defeat, but in relief.{/i} That's... that's what I needed to hear. Not that the count doesn't matter. But that it's not {i}all{/i} that matters."
    jump act1_deep_rho_path_split

label act1_deep_rho_accept_memory:
    rho "{i}He meets your eyes, and for the first time tonight, there's something like peace there.{/i} Courage. Never thought of it that way. Maybe you're right. Maybe remembering is its own kind of bravery."
    jump act1_deep_rho_path_split

label act1_deep_rho_accept_struggle:
    rho "{i}He laughs—short, dry, unexpected.{/i} Weapon trying to be human. Yeah. That's about right. Some days I'm not sure which side is winning. But I keep trying."
    jump act1_deep_rho_path_split

label act1_deep_rho_offer_help:
    $ game_state.set_flag("rho_combat_coordination")
    rho "{i}He stares at you for a long moment. Then he nods.{/i} Yeah. Yeah, okay. I've been carrying this alone for too long. If you're offering... I'll take the help."
    jump act1_deep_rho_path_split_help

label act1_deep_rho_path_split:
    "Rho picks up the firing mechanism again, slots it back into the cannon assembly. His movements are steadier now, less mechanical. He's still carrying the weight—but maybe it's lighter."
    menu:
        "What happens when you reach two hundred?":
            jump act1_deep_rho_future_count
        "Do you ever see them? The ones you've lost?":
            jump act1_deep_rho_haunted_question
        "How do I make sure I'm worth protecting?":
            jump act1_deep_rho_worth_question

label act1_deep_rho_path_split_help:
    "Rho picks up the firing mechanism again, slots it back into the cannon assembly. His movements are steadier now, less mechanical. He's still carrying the weight—but you're carrying it with him."
    menu:
        "We'll carry the count together.":
            jump act1_deep_rho_shared_burden_path
        "In combat, I'll watch your back. Always.":
            jump act1_deep_rho_combat_coordination_path
        "When it gets heavy, you tell me. Deal?":
            jump act1_deep_rho_check_in_path

label act1_deep_rho_future_count:
    rho "I keep counting. Keep remembering. Keep making sure each one matters. And I keep protecting the people who make it worth carrying."
    jump act1_deep_rho_peace_ending

label act1_deep_rho_haunted_question:
    rho "Marcus and Senna? Every night. Sometimes in dreams. Sometimes when I'm awake. They're not angry. They just... watch. Making sure I don't waste what they gave me."
    jump act1_deep_rho_peace_ending

label act1_deep_rho_worth_question:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}He looks at you, surprised.{/i} You already are. You asked. You listened. You didn't run. That's more than most people do. That's enough."
    jump act1_deep_rho_peace_ending

label act1_deep_rho_shared_burden_path:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}He extends his hand—scarred, calloused, steady.{/i} Together, then. One hundred and twelve becomes our count. Not just mine. I can live with that."
    jump act1_deep_rho_bonded_ending

label act1_deep_rho_combat_coordination_path:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "Yeah. And I'll watch yours. We move as a unit from now on. I fire, you position. You engage, I suppress. That's how we keep each other alive."
    jump act1_deep_rho_bonded_ending

label act1_deep_rho_check_in_path:
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}He nods slowly, something like gratitude crossing his face.{/i} Deal. I'm not good at asking for help. But for you, I'll try. That's... that's a promise."
    jump act1_deep_rho_bonded_ending

label act1_deep_rho_peace_ending:
    "Rho finishes reassembling the cannon. He lifts it, testing the weight, the balance. When he sets it down, he meets your eyes."
    jump act1_deep_rho_peace_final

label act1_deep_rho_peace_final:
    rho "Thank you. For listening. For not judging. For seeing the human under the weapon. That's rare. That's valuable. {i}He stands.{/i} I'll remember this. Add it to the count—but the good kind. The kind that makes carrying the rest easier."
    jump act1_deep_rho_peace_departure

label act1_deep_rho_peace_departure:
    "He picks up the cannon, settles it against his shoulder with practiced ease. At the doorway, he pauses. When he looks back, the weight is still there—but it's different now. Acknowledged. Shared, in some small way. He nods once, then disappears into the corridor. The armory is quiet. One hundred and twelve souls rest a little easier tonight."
    return

label act1_deep_rho_bonded_ending:
    "Rho finishes reassembling the cannon. He lifts it, testing the weight, the balance. When he sets it down, something has changed. The weapon looks the same. Rho looks lighter."
    jump act1_deep_rho_bonded_final

label act1_deep_rho_bonded_final:
    rho "You know what the best part is? I don't have to explain anymore. You just {i}get it.{/i} That's... {i}He shakes his head, almost smiling.{/i} That's everything, Avyanna. Thank you."
    jump act1_deep_rho_bonded_departure

label act1_deep_rho_bonded_departure:
    "He picks up the cannon, settles it against his shoulder with practiced ease. At the doorway, he pauses. When he looks back, there's warmth in his eyes—the kind that comes from being truly seen. One hundred and twelve souls. Two people carrying them. The weight hasn't changed. But the burden is lighter. He nods once, a warrior's salute. Then he's gone. The armory feels less cold."
    return
