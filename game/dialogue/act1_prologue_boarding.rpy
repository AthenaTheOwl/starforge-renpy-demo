## act1_prologue_boarding.rpy — Auto-generated from act1_prologue_boarding.json
## 85 dialogue nodes

label act1_prologue_boarding:
    $ game_state.mark_dialogue_played("act1_prologue_boarding")
    jump act1_prologue_boarding_start

label act1_prologue_boarding_start:
    "{i}The hull screams before the alarms do. Someone is cutting through the starboard cargo bay. Thermal lance. Military-grade.{/i}"
    jump act1_prologue_boarding_waffle_report

label act1_prologue_boarding_waffle_report:
    waffle "Unregistered vessel. Modified hauler. They've locked on. Cutting through starboard cargo. Five life signs — four moving in. One's still on their ship. Pilot, probably, or someone who knows better."
    jump act1_prologue_boarding_elia_weapons

label act1_prologue_boarding_elia_weapons:
    elia "Weapons?"
    jump act1_prologue_boarding_waffle_weapons

label act1_prologue_boarding_waffle_weapons:
    waffle "Standard pulse rifles, mostly. One plasma cutter doubling as close-range. And... one of them is doing something with the Lattice. Badly."
    jump act1_prologue_boarding_floor_check

label act1_prologue_boarding_floor_check:
    rho "Floor check. Who's calling pattern?"
    jump act1_prologue_boarding_elia_orders

label act1_prologue_boarding_elia_orders:
    elia "Routing traffic. Starboard cargo breach, four mobile hostiles plus ship-bound. Rho, junction funnel. Elisira, comms intercept. Nyx, Lattice interference on standby."
    jump act1_prologue_boarding_floor_holds

label act1_prologue_boarding_floor_holds:
    "{i}The response comes fast, overlapping, muscle memory. 'Floor holds.' — from every voice. No one asked permission. No one gave orders. The pattern just happened.{/i}"
    jump act1_prologue_boarding_elia_restraint

label act1_prologue_boarding_elia_restraint:
    elia "Don't kill anyone we don't have to."
    jump act1_prologue_boarding_rho_restraint

label act1_prologue_boarding_rho_restraint:
    rho "{i}Something in his shoulders tightens — the weight of a count that never stops.{/i} I know."
    jump act1_prologue_boarding_elisira_intel

label act1_prologue_boarding_elisira_intel:
    elisira "Their comms say the independent contractor vessel will be easy. That they've done this before. That the 'captain' won't be a problem."
    jump act1_prologue_boarding_elia_captain_reaction

label act1_prologue_boarding_elia_captain_reaction:
    elia "{i}Jaw tightening.{/i} They said captain?"
    jump act1_prologue_boarding_elisira_package

label act1_prologue_boarding_elisira_package:
    elisira "The pilot keeps asking about 'the package.' They're here for something specific. He mentioned docking fees. His kids. He's doing this because the alternative is worse."
    jump act1_prologue_boarding_elia_thought

label act1_prologue_boarding_elia_thought:
    "{i}(Always. It's always the same. The ones at the bottom eating the ones further down.){/i}"
    jump act1_prologue_boarding_cargo_bay_confrontation

label act1_prologue_boarding_cargo_bay_confrontation:
    elia "Gentlemen."
    jump act1_prologue_boarding_pirate_demand

label act1_prologue_boarding_pirate_demand:
    lead_pirate "Down on the ground. Hands visible. Now."
    jump act1_prologue_boarding_elia_refuses

label act1_prologue_boarding_elia_refuses:
    elia "I don't think I will. You've cut through my hull. That's going to need repair. You've also made assumptions about command structure that I find... philosophically distasteful."
    jump act1_prologue_boarding_elia_floors

label act1_prologue_boarding_elia_floors:
    elia "You came here expecting a captain. A throat to cut. Someone whose death makes the rest compliant. We don't have that. We have a ship full of people who work together. Floors, not thrones. No hierarchy for you to decapitate."
    jump act1_prologue_boarding_pirate_angry

label act1_prologue_boarding_pirate_angry:
    lead_pirate "Lady, I don't care about your —"
    jump act1_prologue_boarding_elia_moves

label act1_prologue_boarding_elia_moves:
    "{i}She moves. The blade doesn't hurry. It arrives at the necessary points in the necessary order.{/i}"
    jump act1_prologue_boarding_approach_choice

label act1_prologue_boarding_approach_choice:
    "{i}The raiders are down. The fight lasted seconds. Now comes the question: what happens to the survivors?{/i}"
    menu:
        "Restrain them. Patch their wounds. Turn them over to the Guild.":
            $ game_state.set_flag("prologue_nonlethal")
            $ game_state.set_flag("rep_guild", game_state.get_flag("rep_guild", 0) + 1)
            jump act1_prologue_boarding_nonlethal_resolution
        "Let Rho secure them. No need for gentleness — they attacked first.":
            $ game_state.set_flag("prologue_harsh")
            jump act1_prologue_boarding_harsh_resolution
        "Check on the pilot. The one with the kids who stayed on the ship.":
            $ game_state.set_flag("prologue_mercy")
            $ game_state.set_flag("rep_guild", game_state.get_flag("rep_guild", 0) + 1)
            jump act1_prologue_boarding_pilot_mercy

label act1_prologue_boarding_nonlethal_resolution:
    elia "Patch them up. File the waiver. Guild can sort the rest."
    jump act1_prologue_boarding_rho_nonlethal

label act1_prologue_boarding_rho_nonlethal:
    rho "{i}He lowers the cannon. Relief in his shoulders — one less number on the count.{/i} Zip ties and field dressings. Coming up."
    jump act1_prologue_boarding_bubbles_wrap

label act1_prologue_boarding_harsh_resolution:
    rho "{i}His jaw tightens.{/i} Secure. Not gentle, but secure. They'll live to regret it."
    jump act1_prologue_boarding_bubbles_wrap

label act1_prologue_boarding_pilot_mercy:
    elisira "The pilot's still on the ship. Heart rate elevated. He hasn't moved. He's waiting to find out if he's a widower's husband or an orphan-maker."
    jump act1_prologue_boarding_elia_pilot

label act1_prologue_boarding_elia_pilot:
    elia "Hail him. Tell him his crew's alive. Tell him to undock and go home. The debt that made him do this isn't going away because we broke his friends."
    jump act1_prologue_boarding_bubbles_wrap

label act1_prologue_boarding_bubbles_wrap:
    bubbles "{i}Through earpiece, voice like warm water over stones.{/i} Drones secured. Four hostiles accounted for. Hull breach sealed — temporary. Jalen will have opinions about the weld quality."
    jump act1_prologue_boarding_waffle_post_boarding

label act1_prologue_boarding_waffle_post_boarding:
    waffle "{i}}{{WAFFLE.BAT// DAMAGE_REPORT: hull breach sealed temporary | HOSTILE_COUNT: 4 neutralized, 1 departed | CREW_STATUS: all accounted for | MOOD: relieved}}{/i}}"
    jump act1_prologue_boarding_cinnamon_post_boarding

label act1_prologue_boarding_cinnamon_post_boarding:
    cinnamon "Structural integrity holding. Drill bay unaffected. Recommend permanent weld within six hours."
    jump act1_prologue_boarding_end_prologue

label act1_prologue_boarding_end_prologue:
    "{i}The boarding action is over. The coffee machine resumes its mechanical sulk, as if nothing happened. The Lumen Thief flies on.{/i}"
    jump act1_prologue_boarding_arrival_transition

label act1_prologue_boarding_arrival_transition:
    "{i}Hours earlier. Before the boarding. Before the blood and the blade. The memory rewinds to where it actually started — to a docking clamp engaging, to a hatch cycling open, to the first breath of recycled air that wasn't the Kennel's.{/i}"
    jump act1_prologue_boarding_arrival_sensory_1

label act1_prologue_boarding_arrival_sensory_1:
    "{i}The Lumen Thief smells like engine grease, coffee that's been on the burner too long, and something faintly botanical — herbs, maybe, growing somewhere under UV. The air recyclers hum a half-tone lower than the Kennel's. Your body notices before your mind does. The pitch is wrong. Everything is wrong.{/i}"
    jump act1_prologue_boarding_arrival_sensory_2

label act1_prologue_boarding_arrival_sensory_2:
    "{i}The corridor is narrow. Cables bundled along the ceiling with mismatched zip ties. A child's drawing taped to a bulkhead — stick figures under a yellow sun. Someone has written 'JALEN DO NOT TOUCH' on a panel in permanent marker. The ship is alive in ways the Kennel never was.{/i}"
    jump act1_prologue_boarding_arrival_disorientation

label act1_prologue_boarding_arrival_disorientation:
    "{i}Your legs don't trust the gravity. The Kennel ran point-eight-seven standard; this ship runs full G. Every step feels like pushing through shallow water. The shard at the base of your skull pulses once — a faint heat, like a match struck and snuffed — and you steady yourself against the wall.{/i}"
    jump act1_prologue_boarding_first_glimpse_jalen

label act1_prologue_boarding_first_glimpse_jalen:
    "{i}A man passes through the junction ahead, arms full of conduit piping, muttering calculations to himself. Tall. Broad. Hands stained with coolant. He glances at you — not unkindly, not warmly — the way you'd clock a new piece of equipment. Then he's gone, around the corner, still muttering.{/i}"
    jump act1_prologue_boarding_first_glimpse_vesper

label act1_prologue_boarding_first_glimpse_vesper:
    "{i}In the galley doorway, a young woman sits cross-legged on the floor, disassembling a drone component with surgical precision. Her eyes are somewhere else entirely — focused on a middle distance that doesn't exist in this room. She doesn't look up. The parts click together in her hands like they're teaching themselves.{/i}"
    jump act1_prologue_boarding_first_glimpse_nyx

label act1_prologue_boarding_first_glimpse_nyx:
    "{i}The med bay is open. Inside, someone is organizing vials by color, humming something atonal. Dark hair. Steady hands. A holographic anatomy chart rotates slowly beside her — not human anatomy. Something older. She notices you watching and offers a single, precise nod. Permission to exist in her space. Nothing more.{/i}"
    jump act1_prologue_boarding_first_glimpse_rho

label act1_prologue_boarding_first_glimpse_rho:
    "{i}The big one is in the cargo hold, doing pull-ups from a ceiling strut. Each rep is silent — controlled. A man that size should make noise. He drops, lands soft as a held breath, and picks up a cup of tea from the floor. Chamomile. He drinks it without irony.{/i}"
    jump act1_prologue_boarding_first_glimpse_elisira

label act1_prologue_boarding_first_glimpse_elisira:
    "{i}You hear her before you see her. A voice from the comms station, reciting intercepted transmissions in three languages simultaneously — not translating, experiencing. When she turns, her expression is a library deciding whether to let you in.{/i}"
    jump act1_prologue_boarding_elia_welcome

label act1_prologue_boarding_elia_welcome:
    elia "{i}She's waiting at the end of the corridor. Leaning against the bulkhead. Arms folded. Not a pose — a position. Load-bearing patience.{/i} You're Avyanna."
    jump act1_prologue_boarding_avyanna_confirm

label act1_prologue_boarding_avyanna_confirm:
    avyanna "Yes."
    jump act1_prologue_boarding_elia_practical_1

label act1_prologue_boarding_elia_practical_1:
    elia "Elia. I coordinate. The extraction package said you'd need medical attention, food, and somewhere horizontal. Medical's down the hall — Nyx runs it. Food's in the galley — help yourself, clean your plate. Bunk's this way."
    jump act1_prologue_boarding_elia_practical_2

label act1_prologue_boarding_elia_practical_2:
    elia "{i}She starts walking. Doesn't check if you follow. Trusts that you will, or doesn't care either way.{/i} Ground rules. Nobody enters your space without asking. Lock works from inside only. You eat when you're hungry, sleep when you can. Don't touch anything in the engine room without asking Jalen first. He bites."
    jump act1_prologue_boarding_elia_no_warmth

label act1_prologue_boarding_elia_no_warmth:
    elia "Questions can wait until you've slept. Most things can."
    jump act1_prologue_boarding_quarters_approach

label act1_prologue_boarding_quarters_approach:
    "{i}The bunk is small. A cot bolted to the wall. A shelf. A porthole the size of a dinner plate showing nothing but the slow wheel of stars. Someone has left a folded blanket — not standard issue, hand-knitted, one corner unraveling. The pillow smells like detergent, not disinfectant. That difference means everything.{/i}"
    jump act1_prologue_boarding_quarters_details

label act1_prologue_boarding_quarters_details:
    "{i}The walls are scratched. Previous occupants carved initials, tallied days, drew constellations. A small shelf holds three items left behind: a dead succulent in a chipped mug, a dog-eared paperback with the cover torn off, and a bolt that someone polished smooth as a worry stone.{/i}"
    jump act1_prologue_boarding_elia_leaves

label act1_prologue_boarding_elia_leaves:
    elia "{i}She pauses at the threshold.{/i} The lock is the button on the left. Green means open. Red means yours. Use red whenever you need to. Nobody will ask why."
    jump act1_prologue_boarding_elia_leaves_2

label act1_prologue_boarding_elia_leaves_2:
    "{i}She leaves. The door closes. You press the button. The light goes red. And for the first time in — how long? Years? — the locked door is keeping others out, not keeping you in.{/i}"
    jump act1_prologue_boarding_alone_processing_1

label act1_prologue_boarding_alone_processing_1:
    "{i}You sit on the cot. The springs protest. The blanket is rough under your fingers. Real. Not a simulation, not a test, not a Kennel trick where they let you feel safe before the next round of extraction. The shard hums at the base of your skull — a low, persistent warmth, the way an old wound aches before rain.{/i}"
    jump act1_prologue_boarding_alone_processing_2

label act1_prologue_boarding_alone_processing_2:
    "{i}The extraction. You remember it in fragments. Hands pulling you through a maintenance shaft. The taste of copper. Someone saying 'move, move, move' in a voice that expected to be obeyed. The Kennel alarms wailing behind you — that particular frequency they use to make your teeth hurt. And then the shuttle. And then nothing, for a while.{/i}"
    jump act1_prologue_boarding_alone_shard

label act1_prologue_boarding_alone_shard:
    "{i}The shard. They put it in you at the Kennel. Or it put itself in you. The doctors disagreed. You remember the surgery — the light, the restraints, the sound of the drill. You remember waking up different. You remember the word they used: 'compatible.' Like you were a port and it was a cable. Like compatibility was all that mattered.{/i}"
    jump act1_prologue_boarding_alone_free

label act1_prologue_boarding_alone_free:
    "{i}Free. The word sits in your chest like something swallowed wrong. You are on a ship full of strangers. You have no money, no identity papers, no contacts outside the people who extracted you. The shard is fused to your spine. You are free the way a falling object is free — no longer held, but not yet landed.{/i}"
    jump act1_prologue_boarding_attitude_choice

label act1_prologue_boarding_attitude_choice:
    "{i}You stare at the locked red light on the door. How does this feel?{/i}"
    menu:
        "Grateful. They didn't have to take you. Whatever comes next, this is better.":
            $ game_state.set_flag("prologue_attitude_grateful")
            jump act1_prologue_boarding_attitude_grateful
        "Wary. Kind strangers are the most dangerous kind. You've learned that.":
            $ game_state.set_flag("prologue_attitude_wary")
            jump act1_prologue_boarding_attitude_wary
        "Numb. You can't feel anything yet. Maybe later. Maybe never.":
            $ game_state.set_flag("prologue_attitude_numb")
            jump act1_prologue_boarding_attitude_numb

label act1_prologue_boarding_attitude_grateful:
    "{i}The gratitude is a physical thing — pressure behind your eyes, tightness in your throat. You press your palm against the blanket. Someone knitted this. Chose the yarn. Counted the stitches. That effort exists in the world, and now it's keeping you warm. You let yourself feel it. Just for a moment.{/i}"
    jump act1_prologue_boarding_bee_first_signal

label act1_prologue_boarding_attitude_wary:
    "{i}You check the lock twice. Map the room — one entrance, one porthole too small to crawl through, cot bolted down, shelf removable. The bolt on the shelf is heavy enough to swing. You note this and hate yourself for noting it. The Kennel taught you to think like this. The Kennel taught you everything wrong.{/i}"
    jump act1_prologue_boarding_bee_first_signal

label act1_prologue_boarding_attitude_numb:
    "{i}Nothing. The room is a room. The blanket is a blanket. Your hands are in your lap and they don't feel like yours. Somewhere behind the numbness there is a person who will have opinions about all of this, but she's not here right now. She left sometime during the extraction and hasn't come back yet.{/i}"
    jump act1_prologue_boarding_bee_first_signal

label act1_prologue_boarding_bee_first_signal:
    "{i}A flicker. Not visual — deeper. Like a word on the tip of your tongue, except the tongue is your spine and the word is in a language you've never heard. The shard pulses once, twice. A rhythm that almost sounds like —{/i}"
    jump act1_prologue_boarding_bee_proto_message

label act1_prologue_boarding_bee_proto_message:
    "{i}}{{BEE:: ...ledger... | STATUS: sub-threshold | DETAIL: signal below conscious parsing — catalogued as somatic noise}}{/i}}"
    jump act1_prologue_boarding_bee_dismissed

label act1_prologue_boarding_bee_dismissed:
    "{i}You rub the back of your neck. Stress. Extraction aftershock. The doctors at the Kennel said the shard would produce phantom signals during periods of elevated cortisol. They said a lot of things. Most of them were lies, but this one might be true. You let it go.{/i}"
    jump act1_prologue_boarding_crew_interaction_choice

label act1_prologue_boarding_crew_interaction_choice:
    "{i}A knock at the door. Soft. Then a voice — not Elia's. Someone checking in. You could answer, or not. But when you look at the door, you realize you want to. Even that small want feels like progress. Who is it?{/i}"
    menu:
        "It's Rho. You recognize the careful weight of his knock — deliberate, like he's afraid of breaking something.":
            $ game_state.set_flag("prologue_met_rho")
            jump act1_prologue_boarding_interact_rho
        "It's Elisira. Her voice carries even through the door — measured, warm at the edges.":
            $ game_state.set_flag("prologue_met_elisira")
            jump act1_prologue_boarding_interact_elisira
        "It's Jalen. You can hear him shifting his weight, impatient, something metal clinking in his hands.":
            $ game_state.set_flag("prologue_met_jalen")
            jump act1_prologue_boarding_interact_jalen

label act1_prologue_boarding_interact_rho:
    rho "{i}He fills the doorway. Holds out a thermos — battered, dented, clearly beloved.{/i} Chamomile. It's, uh. It helps. After adrenaline. Allegedly."
    jump act1_prologue_boarding_interact_rho_2

label act1_prologue_boarding_interact_rho_2:
    rho "{i}He doesn't come in. Doesn't lean on the frame. Gives you the full doorway to close if you want.{/i} I'm Rho. I carry heavy things and try not to break them. That's... basically the job description."
    jump act1_prologue_boarding_interact_rho_3

label act1_prologue_boarding_interact_rho_3:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    "{i}His hands are enormous. The thermos looked like a toy in them. But he held it like it was made of glass.{/i}"
    jump act1_prologue_boarding_interact_rho_response

label act1_prologue_boarding_interact_rho_response:
    avyanna "Thank you."
    jump act1_prologue_boarding_interact_rho_exit

label act1_prologue_boarding_interact_rho_exit:
    rho "{i}A nod. He turns to leave, then stops.{/i} The gravity's higher here than what you're used to. Drink water. Your joints will thank you in the morning. {i}And he's gone. Quiet as something that big has no right to be.{/i}"
    jump act1_prologue_boarding_ftl_approach

label act1_prologue_boarding_interact_elisira:
    elisira "{i}She stands at an angle — not directly in front of the door, but offset. Giving you sightlines. Deliberate.{/i} I brought you something to eat. Nothing complicated. Rice, protein, broth. The galley has more, but your stomach won't be ready for more."
    jump act1_prologue_boarding_interact_elisira_2

label act1_prologue_boarding_interact_elisira_2:
    elisira "I'm Elisira. I listen to things — signals, chatter, what people say between the things they say. You don't have to talk to me. But if you do, I'll hear you. That's not a promise. It's just what I am."
    jump act1_prologue_boarding_interact_elisira_3

label act1_prologue_boarding_interact_elisira_3:
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    "{i}Her eyes are steady. Not searching — receiving. You get the sense that she's already heard everything your body is broadcasting: the fear, the exhaustion, the razor-thin hope. She doesn't comment on any of it.{/i}"
    jump act1_prologue_boarding_interact_elisira_response

label act1_prologue_boarding_interact_elisira_response:
    avyanna "Thank you."
    jump act1_prologue_boarding_interact_elisira_exit

label act1_prologue_boarding_interact_elisira_exit:
    elisira "{i}She sets the tray on the floor inside the threshold — not reaching in, not crossing the line.{/i} Eat when you want. Leave the tray outside when you're done. Or don't. No one's counting. {i}A pause.{/i} Welcome aboard, Avyanna."
    jump act1_prologue_boarding_ftl_approach

label act1_prologue_boarding_interact_jalen:
    jalen "{i}He's holding a piece of conduit and looks mildly annoyed about everything in general.{/i} So you're the new one. Right. I'm Jalen. I keep this ship from becoming a very expensive coffin. Don't touch anything in the engine room. I'm not being dramatic — the plasma coils will actually kill you."
    jump act1_prologue_boarding_interact_jalen_2

label act1_prologue_boarding_interact_jalen_2:
    jalen "{i}He glances past you at the bunk.{/i} The heating vent rattles at oh-three-hundred. It's not broken — it's a pressure equalization thing. If it bothers you, stuff a sock in it. Left side."
    jump act1_prologue_boarding_interact_jalen_3

label act1_prologue_boarding_interact_jalen_3:
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    "{i}It's the most practical kindness you've received in years — someone telling you how to sleep better in a new place. He doesn't seem to realize he's being kind. He seems to think he's being efficient.{/i}"
    jump act1_prologue_boarding_interact_jalen_response

label act1_prologue_boarding_interact_jalen_response:
    avyanna "Thank you."
    jump act1_prologue_boarding_interact_jalen_exit

label act1_prologue_boarding_interact_jalen_exit:
    jalen "{i}He waves the conduit like a dismissal.{/i} Don't thank me. Thank whoever designed the pressure system on this heap. {i}He's already walking away, muttering about weld integrity.{/i}"
    jump act1_prologue_boarding_ftl_approach

label act1_prologue_boarding_ftl_approach:
    "{i}A tone sounds through the ship — three rising notes, almost musical. An announcement system that someone bothered to make pleasant.{/i}"
    jump act1_prologue_boarding_cinnamon_ftl_warning

label act1_prologue_boarding_cinnamon_ftl_warning:
    cinnamon "FTL transit in ninety seconds. Secure loose items. First-time passengers: the nausea is temporary. The sense of existential dislocation is also temporary but takes longer."
    jump act1_prologue_boarding_ftl_pre_jump

label act1_prologue_boarding_ftl_pre_jump:
    "{i}You don't know what to secure. You grip the edge of the cot. The engines change pitch — the hum deepens, drops below hearing, becomes a vibration in your molars, your sternum, the shard. Especially the shard. It resonates like a tuning fork struck against the universe's spine.{/i}"
    jump act1_prologue_boarding_ftl_jump

label act1_prologue_boarding_ftl_jump:
    "{i}The jump happens. It doesn't feel like acceleration. It feels like being turned inside out and put back — everything in the right place, but briefly aware of its own assembly. Your vision whites. Your ears ring. The stars in the porthole stretch into lines, then vanish, replaced by the churning non-color of FTL space. It looks like static. It looks like the inside of a thought.{/i}"
    jump act1_prologue_boarding_ftl_aftermath

label act1_prologue_boarding_ftl_aftermath:
    "{i}Your stomach lurches. Your fingers ache from gripping the cot. The shard flares — a bright, sharp heat — and for one instant you hear something. Not words. A frequency. A tone that sounds like geometry, like architecture, like a door being measured for a key. Then it's gone.{/i}"
    jump act1_prologue_boarding_bee_ftl_signal

label act1_prologue_boarding_bee_ftl_signal:
    "{i}}{{BEE:: ...transit-resonance... | STATUS: signal spike during FTL boundary crossing | DETAIL: harmonic match 0.03 above noise floor — still sub-threshold — still deniable}}{/i}}"
    jump act1_prologue_boarding_ftl_settle

label act1_prologue_boarding_ftl_settle:
    "{i}The nausea passes. The non-color outside the porthole settles into a slow, nauseating churn. You breathe. The ship breathes. Somewhere, the coffee machine gurgles its permanent complaint. Normal. This is normal here. You will learn what normal means.{/i}"
    jump act1_prologue_boarding_sleep_attempt

label act1_prologue_boarding_sleep_attempt:
    "{i}You lie down. The cot is too soft — the Kennel used slabs, said it was better for spinal alignment, said a lot of things about what was better for you. This mattress has a dip where someone else slept before you, and you fit into the shape they left. A stranger's ghost, cradling you.{/i}"
    jump act1_prologue_boarding_sleep_sounds

label act1_prologue_boarding_sleep_sounds:
    "{i}The ship speaks in its sleep. The heating vent ticks. The hull groans against FTL pressure. Footsteps pass your door — someone on a late watch, their stride unhurried. A murmur of voices from the galley. Laughter. The sound is so foreign it takes you a moment to identify it.{/i}"
    jump act1_prologue_boarding_sleep_shard

label act1_prologue_boarding_sleep_shard:
    "{i}The shard is warm. Not painful. Warm the way a hand on your shoulder would be warm, if anyone had touched you gently in the last three years. You close your eyes. Behind them, faint geometric patterns bloom and fade — the ghost of BEE's signal, or the ghost of a ghost. You are too tired to be afraid of it.{/i}"
    jump act1_prologue_boarding_sleep_final

label act1_prologue_boarding_sleep_final:
    "{i}Sleep comes. Not peacefully — it never does — but it comes. And in the space between waking and unconsciousness, in that liminal dark where the body finally lets go of its vigil, you feel something you haven't felt since before the Kennel. Not hope. Not yet. But the absence of the certainty that tomorrow will be worse. And that absence — that tiny, fragile void where despair used to be — is enough. For now. It's enough.{/i}"
    return
