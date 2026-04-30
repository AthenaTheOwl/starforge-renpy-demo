## act1_elia_rescue.rpy — Auto-generated from act1_elia_rescue.json
## 58 dialogue nodes

label act1_elia_rescue:
    $ game_state.mark_dialogue_played("act1_elia_rescue")
    jump act1_elia_rescue_start

label act1_elia_rescue_start:
    "The explosion tears through the eastern wing like a fist through wet paper. Emergency lighting floods the corridor in arterial red.

A figure rounds the corner at a dead sprint—armored, blade in each hand, moving with the precision of someone who has done this exact thing many times before.

She skids to a stop when she sees you."
    jump act1_elia_rescue_elia_first_words

label act1_elia_rescue_elia_first_words:
    elia "\"You. You're from the extraction list.\" Her eyes scan you—not with pity, with assessment. \"Can you walk? Can you run? I need one of those answers to be yes.\""
    menu:
        "\"I can run. Who are you?\"":
            jump act1_elia_rescue_elia_explains_quick
        "\"Why should I trust you?\"":
            jump act1_elia_rescue_elia_trust
        "[Say nothing. Just nod.]":
            jump act1_elia_rescue_elia_approves_silence

label act1_elia_rescue_elia_explains_quick:
    elia "\"Elia. I'm here to get you out. The rest of the introductions can wait until we're not standing in an active kill zone.\"

She sheathes one blade—Mourning, though you don't know its name yet—and extends her hand.

\"Move with me. Stay behind me. If I tell you to drop, you drop. Clear?\""
    menu:
        "\"Clear.\"":
            jump act1_elia_rescue_quick_followup
        "\"There are others in the extraction wing—\"":
            jump act1_elia_rescue_elia_others

label act1_elia_rescue_quick_followup:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "\"Good. Short answers. I like you already.\"

She turns and starts moving before the sentence is finished. The corridor ahead is a mess of burst pipes and sparking cable."
    jump act1_elia_rescue_quick_followup_2

label act1_elia_rescue_quick_followup_2:
    avyanna "{i}She moves like the building is hers. Like the fire and the wreckage are furniture she's rearranging.{/i}"
    menu:
        "\"You've done this before.\"":
            jump act1_elia_rescue_quick_followup_3
        "[Match her pace. Don't slow her down.]":
            jump act1_elia_rescue_quick_followup_silent

label act1_elia_rescue_quick_followup_3:
    elia "\"Fourteen extractions in two years.\" She says it the way someone else would say 'I take cream in my coffee.' \"You're number fifteen. Don't make me regret the streak.\""
    jump act1_elia_rescue_move_out

label act1_elia_rescue_quick_followup_silent:
    "You keep pace. Elia glances back once—just once—and whatever she sees makes the corner of her mouth twitch. Not a smile. Approval."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_elia_trust:
    elia "Something flickers across her face—not impatience, recognition. Like she's heard that question before, from someone who had every right to ask it.

\"You shouldn't. I'm armed, I'm in your facility, and I just blew a hole in your east wall.\" A beat. \"But I'm also the only person in this building who isn't here to harvest you. So.\""
    menu:
        "\"...Fair enough. Let's go.\"":
            jump act1_elia_rescue_trust_followup
        "\"How do you know about the extractions?\"":
            jump act1_elia_rescue_elia_knowledge

label act1_elia_rescue_trust_followup:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    "You fall in behind her. The decision sits in your chest like a swallowed stone—heavy, but solid."
    jump act1_elia_rescue_trust_followup_2

label act1_elia_rescue_trust_followup_2:
    elia "\"For what it's worth—\" She pauses at a junction, listens, takes the left fork. \"—most people I extract take longer to decide. The ones who freeze are the ones I lose.\""
    menu:
        "\"I've been frozen long enough.\"":
            jump act1_elia_rescue_trust_followup_3
        "\"Maybe I'm just tired of standing still.\"":
            jump act1_elia_rescue_trust_followup_3

label act1_elia_rescue_trust_followup_3:
    elia "She doesn't respond to that. But the way her grip shifts on Mourning's hilt—looser, easier—says she heard you."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_elia_approves_silence:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "She studies your silence for exactly one second. Then nods—not pity, not condescension. Respect.

\"Good. Quiet is useful where we're going.\""
    jump act1_elia_rescue_silence_followup

label act1_elia_rescue_silence_followup:
    "She turns toward the west corridor, both blades drawn now, and moves. She doesn't check if you're following.

{i}She doesn't need to. You're already moving.{/i}"
    jump act1_elia_rescue_silence_followup_2

label act1_elia_rescue_silence_followup_2:
    elia "Over her shoulder, without breaking stride: \"If you can fight, stay at my flank. If you can't, stay behind me and keep low. Tap my shoulder twice if you see something I don't.\""
    menu:
        "[Move to her flank.]":
            jump act1_elia_rescue_silence_followup_3
        "[Fall in behind her. Keep low.]":
            jump act1_elia_rescue_silence_followup_4

label act1_elia_rescue_silence_followup_3:
    "You move to her left side. Elia glances at your positioning—you've left her blade arm free without being told.

\"Huh,\" she says. Nothing else. But she adjusts her pace to match yours."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_silence_followup_4:
    "You keep behind her. In the red emergency light, her silhouette is all edges—blades, armor plates, the sharp line of her jaw. A weapon in the shape of a person, cutting a path through the smoke."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_elia_others:
    $ game_state.set_flag("asked_about_others")
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "She pauses. You see something shift behind her eyes—a calculation that costs her.

\"I know. Elisira's team is handling the east wing. We have—\" she checks something on her wrist, \"—four minutes before corporate security locks this sector down.\"

Her jaw tightens. \"We get who we can get. That's the mission. I'm sorry it's not better than that.\""
    jump act1_elia_rescue_others_followup

label act1_elia_rescue_others_followup:
    avyanna "{i}Four minutes. For all of them. The number sits wrong, like a bone set at the wrong angle.{/i}"
    menu:
        "\"Then we'd better not waste any of those minutes.\"":
            jump act1_elia_rescue_move_out
        "\"If Elisira's team fails—\"":
            jump act1_elia_rescue_others_followup_2

label act1_elia_rescue_others_followup_2:
    elia "\"Then we come back.\" She says it like a fact, not a promise. Like gravity. \"We always come back.\"

She's already moving again. The conversation is over."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_elia_knowledge:
    $ game_state.set_flag("learned_elia_watched")
    elia "\"Because we've been watching this place for eight months.\" Her voice is flat—the flatness of someone holding back anger. \"Site K-9. 'The Kennel.' Cute name for a place that bleeds people dry on a schedule.\"

She meets your eyes. \"We know what they're doing to you. All of you. That's why we're here.\"

The alarms change pitch. Running out of time."
    jump act1_elia_rescue_knowledge_followup

label act1_elia_rescue_knowledge_followup:
    avyanna "{i}Eight months. They watched for eight months. The math on that—how many extraction cycles, how many people they couldn't reach in time—{/i}"
    menu:
        "\"Eight months is a long time to watch.\"":
            jump act1_elia_rescue_knowledge_followup_2
        "[Let it go. Focus on surviving the next four minutes.]":
            jump act1_elia_rescue_move_out

label act1_elia_rescue_knowledge_followup_2:
    elia "Her jaw works. For a half-second, the professional mask cracks and you see something underneath—not guilt, exactly. The scar tissue where guilt used to be.

\"Yeah. It was.\"

She turns away. End of discussion."
    jump act1_elia_rescue_move_out

label act1_elia_rescue_move_out:
    "You move. Elia leads—blade-first through the smoke-choked corridors, stepping over debris with the casual ease of someone navigating their living room.

Behind you, the extraction wing groans and buckles."
    jump act1_elia_rescue_corridor_bodies

label act1_elia_rescue_corridor_bodies:
    "The first body is a technician. Lab coat, face-down, one hand still reaching for a keycard on the floor. Elia steps over him without looking down.

The second is a guard. His sidearm is still holstered.

{i}You step over them both. You don't look down either. Later, you'll wonder when you learned to do that.{/i}"
    jump act1_elia_rescue_corridor_locked_door

label act1_elia_rescue_corridor_locked_door:
    "A blast door blocks the corridor—Loss-of-Containment protocol, sealed magnetically. The emergency display reads: {b}SECTOR 7-W — LOCKDOWN ACTIVE — AUTHORIZATION REQUIRED{/b}

Elia doesn't slow down."
    jump act1_elia_rescue_elia_cuts_door

label act1_elia_rescue_elia_cuts_door:
    "She draws Mourning—the longer blade, the one that seems to drink the emergency lighting rather than reflect it. She drives it into the seam of the blast door at a precise angle, and the metal {i}screams{/i}.

Not melts. Not breaks. Screams. Like the door knows what's cutting it.

Three seconds. A vertical cut, a horizontal cut, a kick. The section falls inward with a clang that echoes down the corridor behind you."
    jump act1_elia_rescue_corridor_reaction

label act1_elia_rescue_corridor_reaction:
    avyanna "{i}That blade cut through six inches of reinforced steel like it was drywall. File that under 'reasons to keep her in front of you.'{/i}"
    menu:
        "\"What is that blade?\"":
            jump act1_elia_rescue_mourning_question
        "[Step through the gap. Keep moving.]":
            jump act1_elia_rescue_ceiling_collapse

label act1_elia_rescue_mourning_question:
    elia "\"Mourning.\" She says the name like it's a person she has complicated feelings about. \"Old weapon. Older than me, older than this facility. She cuts what needs cutting.\"

A pause. Then, quieter: \"Don't touch her. She's... particular.\""
    jump act1_elia_rescue_ceiling_collapse

label act1_elia_rescue_ceiling_collapse:
    "The corridor beyond the door is worse. Ceiling panels hanging like broken teeth, sparking cables writhing on the floor. You're halfway through when the groan comes—deep, structural, the sound of a building deciding to give up.

\"DOWN!\"

Elia's arm hits your chest like a steel bar. You drop. A section of ceiling the size of a dining table crashes into the space where your head was half a second ago."
    jump act1_elia_rescue_ceiling_aftermath

label act1_elia_rescue_ceiling_aftermath:
    "Dust. Silence. Then Elia's voice, close to your ear.

\"You're fine. Move.\"

She hauls you upright and shoves you forward through the gap between the fallen debris and the wall. There's maybe eighteen inches of clearance. You fit. Barely."
    jump act1_elia_rescue_lattice_hum

label act1_elia_rescue_lattice_hum:
    "And then—

Something in your chest {i}hums{/i}.

Not your heart. Deeper than that. In the place where the Lattice sits—the thing they put in you, the thing they never explained—something stirs. Like a wire vibrating at a frequency you can feel in your teeth."
    jump act1_elia_rescue_lattice_hum_2

label act1_elia_rescue_lattice_hum_2:
    avyanna "{i}It's warm. It shouldn't be warm. Every time they ran the extraction cycle it was cold—surgical cold, the cold of something being taken. This is different. This is the cold in reverse.{/i}"
    jump act1_elia_rescue_lattice_hum_3

label act1_elia_rescue_lattice_hum_3:
    elia "Elia freezes. Turns. Stares at your chest like she can see through your sternum.

\"Your Lattice just—\" She cuts herself off. Recalculates. \"Later. We deal with that later. Move.\""
    jump act1_elia_rescue_security_approach

label act1_elia_rescue_security_approach:
    "You hear them before you see them. Boot-falls, synchronized. The sharp click of safeties disengaging.

The corridor opens into a junction—and there they are. Four corporate security officers in full tactical gear, positioned behind a makeshift barricade of overturned desks and filing cabinets. Rifles trained on the corridor you just came through.

The lead officer—sergeant's stripes, visor up—raises a fist. His team holds."
    jump act1_elia_rescue_security_standoff

label act1_elia_rescue_security_standoff:
    security_sergeant "\"That's far enough. Subjects are to remain in containment during a Loss-of-Containment event.\" He reads the words like he's reciting a manual. Then his eyes find Elia's blades. \"Drop the weapons. Get on the ground. Both of you.\""
    jump act1_elia_rescue_security_elia_response

label act1_elia_rescue_security_elia_response:
    elia "Elia's posture doesn't change. But something in the air does—a shift in pressure, a tightening, like the moment before a dog bite.

\"Four of you,\" she says, conversational. \"Two blades. I like those odds fine, but your people don't need to die in this hallway tonight.\"

She glances at you sideways. A question in the look."
    menu:
        "[Watch silently. Let Elia handle it.]":
            jump act1_elia_rescue_security_elia_handles
        "[Create a distraction — knock over a pipe, draw their attention.]":
            jump act1_elia_rescue_security_distraction
        "\"Sergeant. The east wing is gone. Your command structure is gone. Who are you holding this line for?\"":
            $ _sc_result = skill_check("persuasion", 10, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_elia_rescue_security_talked_down
            else:
                jump act1_elia_rescue_security_talk_fail

label act1_elia_rescue_security_elia_handles:
    "You stay still. Elia moves.

It's not a fight. A fight implies two sides with a chance. This is a demonstration.

Mourning takes the barricade apart in one sweep. Her second blade—the short one, the fast one—disarms the sergeant before he finishes raising his rifle. Two of the others bolt. The fourth drops his weapon and puts his hands up.

Elapsed time: four seconds."
    jump act1_elia_rescue_security_aftermath

label act1_elia_rescue_security_distraction:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    "You grab a length of dangling pipe and wrench it free. Sparks spray across the junction. The sergeant flinches right—

—and Elia is already moving left.

Mourning catches the barricade at its weakest point. The whole thing folds inward. By the time the guards recover from the shower of sparks, Elia is inside their perimeter. The sergeant's rifle is on the floor. His team is backing up.

Four seconds. Maybe five."
    jump act1_elia_rescue_security_aftermath

label act1_elia_rescue_security_talked_down:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    security_sergeant "The sergeant's jaw works. You see it—the exact moment the math stops adding up for him. The east wing is rubble. His earpiece is static. The woman in front of him just cut through a blast door with a sword.

\"...Stand down.\" He lowers his rifle. His team follows. \"We were never here. Neither were you.\""
    jump act1_elia_rescue_security_aftermath_clean

label act1_elia_rescue_security_talk_fail:
    security_sergeant "\"Nice try.\" The sergeant's finger moves to his trigger. \"On the ground. Now—\"

He doesn't finish the sentence. Elia was waiting for him to stop listening to you and start reaching for his weapon. That half-second of distraction was enough."
    jump act1_elia_rescue_security_talk_fail_2

label act1_elia_rescue_security_talk_fail_2:
    "Mourning takes his rifle in half. The short blade pins the next guard's weapon to the barricade. The other two run.

Elia straightens up. Doesn't even look winded."
    jump act1_elia_rescue_security_aftermath

label act1_elia_rescue_security_aftermath:
    elia "\"Amateurs.\" She flicks something off Mourning's edge—not blood, just dust. \"Corporate security. They train for containment breaches, not for someone who wants to be here.\"

She starts moving again. The exit is close—you can smell outside air threading through the smoke."
    jump act1_elia_rescue_extraction_approach

label act1_elia_rescue_security_aftermath_clean:
    elia "She stares at you as the guards file out through a side corridor. The look on her face is new—not assessment this time. Reassessment.

\"You just talked down four armed guards in a burning building.\" A beat. \"I was ready to cut through them.\"

She sheathes her blades. \"Your way was better.\""
    jump act1_elia_rescue_extraction_approach

label act1_elia_rescue_extraction_approach:
    "The corridor ends at a loading dock—massive freight doors, half-open, letting in a gust of cold night air that tastes like freedom and engine exhaust.

A shuttle sits on the landing pad, engines idling. Its running lights cut blue lines through the smoke pouring out of Site K-9's corpse.

And there, positioned behind a concrete pylon with a rifle that looks like it was built for a vehicle, is a woman with silver-white hair and eyes that track your approach with preternatural calm."
    jump act1_elia_rescue_elisira_introduction

label act1_elia_rescue_elisira_introduction:
    elisira "\"Elia.\" Her voice is precise, clipped, the accent from somewhere old-world. She doesn't lower the rifle—it stays trained on the corridor behind you. \"You're forty seconds behind schedule.\"

\"Ran into a door.\" Elia's voice carries the ghost of a smirk. \"And some guards.\"

\"The door, I heard. The guards?\" A flicker of something in those pale eyes. \"Still breathing?\""
    jump act1_elia_rescue_elisira_exchange

label act1_elia_rescue_elisira_exchange:
    elia "\"All breathing. Ask the new one—\" She tilts her head toward you. \"—they had opinions about that.\"

Elisira's gaze shifts to you. It's not like Elia's assessment—less blade, more telescope. She's reading you at a distance you can feel."
    menu:
        "\"Elisira, right? Elia mentioned your team in the east wing.\"":
            jump act1_elia_rescue_elisira_east_wing
        "[Nod. Hold her gaze.]":
            jump act1_elia_rescue_elisira_nod
        "\"Thank you. For covering the exit.\"":
            jump act1_elia_rescue_elisira_thanks

label act1_elia_rescue_elisira_east_wing:
    elisira "\"Three extracted. Two couldn't be moved.\" She says it clean and factual, the way a surgeon describes an operation. But her trigger finger tightens on the rifle stock, just barely. \"We'll go back for them.\"

She turns to Elia. \"The shuttle won't wait. Get them aboard.\""
    jump act1_elia_rescue_board_shuttle

label act1_elia_rescue_elisira_nod:
    elisira "She returns the nod. Exact, measured. Like she's filed you under a category and will revisit the classification later.

\"Shuttle. Now. Both of you.\" She's already sweeping the corridor behind you through her scope. \"We have company inbound from the north tower. Sixty seconds.\""
    jump act1_elia_rescue_board_shuttle

label act1_elia_rescue_elisira_thanks:
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    elisira "Something shifts in her expression. Not softness—Elisira doesn't do soft. But the hard edges rearrange into something that might be warmth, viewed from very far away.

\"You're welcome.\" Two words, and she means both of them. \"Now get on the shuttle before I have to shoot someone to keep this exit open.\""
    jump act1_elia_rescue_board_shuttle

label act1_elia_rescue_board_shuttle:
    "The shuttle interior is stripped—no seats, just cargo straps bolted to the walls and a med-kit someone has already torn open. Two other people are huddled near the back—other extractions, you realize. They look exactly as hollow-eyed as you feel.

Elia drops into the co-pilot seat. Elisira swings aboard last, the rifle still trained on the loading dock until the ramp closes.

\"Go,\" Elisira says."
    jump act1_elia_rescue_liftoff

label act1_elia_rescue_liftoff:
    "The shuttle lurches upward. Through the narrow viewport, you watch Site K-9 shrink—first the loading dock, then the east wing (burning), then the whole compound. From above, it looks small. A concrete scar on a dark hillside, trailing smoke like a wound that won't clot."
    jump act1_elia_rescue_liftoff_look_back

label act1_elia_rescue_liftoff_look_back:
    avyanna "{i}You spent eleven months in that building. Eleven months of extraction cycles and fluorescent lighting and the taste of copper in the back of your throat every morning.{/i}"
    menu:
        "[Look back. Watch it burn.]":
            jump act1_elia_rescue_look_back_yes
        "[Don't look back. Face forward.]":
            jump act1_elia_rescue_look_back_no

label act1_elia_rescue_look_back_yes:
    "You press your hand against the viewport glass and watch Site K-9 burn. The east wing collapses in on itself—a slow, almost graceful implosion, sending a column of ash into the night sky.

{i}Good.{/i}

The thought surprises you. Not its presence—its certainty."
    jump act1_elia_rescue_bee_first_message

label act1_elia_rescue_look_back_no:
    "You turn your back to the viewport. Sit against the hull. Close your eyes.

Behind your eyelids, the red emergency lighting still pulses. It will for a while. But the shuttle is climbing, and the air pressure is changing, and every second puts more distance between you and the place that tried to take you apart.

{i}Don't look back. There's nothing there you need.{/i}"
    jump act1_elia_rescue_bee_first_message

label act1_elia_rescue_bee_first_message:
    "And then—in the space behind your sternum, where the Lattice hums its new warm frequency—something speaks.

Not words, exactly. Not yet. A pattern. A shape that wants to be language.

{{BEE:: first breath | initialization | the old pattern is broken — you are no longer a closed system}}

{{BEE:: freedom trajectory | confirmed | new variables detected — recalculating}}

{{BEE:: welcome to the outside | status: unprecedented | recommendation: survive}}"
    jump act1_elia_rescue_bee_reaction

label act1_elia_rescue_bee_reaction:
    avyanna "{i}Something just spoke inside your chest. Something that lives in the Lattice. Something that was sleeping—or waiting—or both.

It doesn't feel like the extraction cycles. It doesn't feel like anything they did to you.

It feels like yours.{/i}"
    jump act1_elia_rescue_elia_final

label act1_elia_rescue_elia_final:
    $ game_state.set_flag("elia_rescued")
    elia "Elia is watching you from the co-pilot seat. She saw your face change.

\"It's starting, isn't it.\" Not a question. \"The Lattice.\"

She leans back. Crosses her arms. The professional mask is still on, but the eyes behind it are tired—the tiredness of someone who has had this conversation before.

\"We'll explain everything. When we land, when you're safe, when you've eaten something that isn't nutrient paste. Everything.\"

A beat.

\"For now—welcome out.\""
    jump act1_elia_rescue_final_narration

label act1_elia_rescue_final_narration:
    $ game_state.set_flag("left_site_k9")
    "The shuttle climbs through low cloud cover, and Site K-9 vanishes.

Below, the fire still burns. Behind you, the old life collapses in on itself. Ahead, the dark, and whatever waits in it.

The Lattice hums. BEE:: hums with it. And Elia—the woman with the blade called Mourning, who cut through a building to find you—sits in the co-pilot seat with her eyes half-closed, already planning the next extraction.

{i}You are free. You do not yet know what that means.{/i}"
    return
