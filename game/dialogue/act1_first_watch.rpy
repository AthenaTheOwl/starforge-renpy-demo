## act1_first_watch.rpy — Auto-generated from act1_first_watch.json
## 148 dialogue nodes

label act1_first_watch:
    $ game_state.mark_dialogue_played("act1_first_watch")
    jump act1_first_watch_start

label act1_first_watch_start:
    "{i}Crew meeting. Galley. Elia called it with a knock on your door — patient and measured, nothing like the Kennel's shift-change sirens.{/i}"
    jump act1_first_watch_elia_crew

label act1_first_watch_elia_crew:
    elia "You're not a passenger anymore. You're crew."
    jump act1_first_watch_avyanna_automatic

label act1_first_watch_avyanna_automatic:
    avyanna "I know."
    jump act1_first_watch_elia_challenge

label act1_first_watch_elia_challenge:
    elia "Do you? Crew works. Not makework — real work. Contributing. {i}Reading your expression.{/i} Not like that. This isn't punishment. It's trust."
    jump act1_first_watch_elia_duties

label act1_first_watch_elia_duties:
    elia "You're still recovering. So we start small. Observation posts — watching systems, noting anomalies. Inventory checks. Message running between stations when comms are spotty."
    jump act1_first_watch_avyanna_more

label act1_first_watch_avyanna_more:
    avyanna "I can do more. I'm stronger than —"
    jump act1_first_watch_elia_build

label act1_first_watch_elia_build:
    elia "I know. And you'll do more when you're ready. But we don't break people here. We build them."
    jump act1_first_watch_rho_napping

label act1_first_watch_rho_napping:
    rho "{i}Into his coffee.{/i} Also, if you work yourself to collapse, Waffle will design a recovery regime that involves mandatory napping. It's worse than it sounds."
    jump act1_first_watch_waffle_nap

label act1_first_watch_waffle_nap:
    waffle "{i}}{{WAFFLE.BAT// CORRECTION: mandatory napping is EXCELLENT | CREW-COMPLIANCE: historically poor | RECOMMENDATION: try harder}}{/i}}"
    jump act1_first_watch_jalen_spa

label act1_first_watch_jalen_spa:
    jalen "She made me sleep for twelve hours once. With ambient sounds. It was like being held hostage by a spa."
    jump act1_first_watch_nyx_whales

label act1_first_watch_nyx_whales:
    nyx "She played whale songs at me for three days. Old Earth marine recordings. Very soothing. I wanted to die."
    jump act1_first_watch_elia_time

label act1_first_watch_elia_time:
    elia "{i}Ignoring the chaos.{/i} The point is: pace yourself. You have time here."
    jump act1_first_watch_meet_crew_choice

label act1_first_watch_meet_crew_choice:
    "{i}The meeting disperses. The crew filters back to their stations. You have time to talk to people.{/i}"
    menu:
        "Find Nyx in her lab":
            jump act1_first_watch_nyx_lab
        "Follow Rho to the cargo bay":
            jump act1_first_watch_rho_cargo
        "Look for Jalen on the bridge":
            jump act1_first_watch_jalen_bridge
        "Deliver a message for Elia":
            jump act1_first_watch_message_run
        "Find Vesper — you have questions about the crew structure":
            jump act1_first_watch_vesper_visit

label act1_first_watch_vesper_visit:
    "{i}You find Vesper in their quarters — a space that's part office, part armory, part something you don't have words for.{/i}"
    jump act1_first_watch_vesper_greeting

label act1_first_watch_vesper_greeting:
    vesper "Questions about the crew? Good. Means you're thinking about how to work with them. {i}They gesture to a chair.{/i} Ask."
    jump act1_first_watch_vesper_choice

label act1_first_watch_vesper_choice:
    menu:
        "'How long have you been running this crew?'":
            jump act1_first_watch_vesper_history
        "'What do you need from me?'":
            jump act1_first_watch_vesper_expectations

label act1_first_watch_vesper_history:
    $ game_state.set_flag("first_watch_visited_vesper")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "Eight years. Built it piece by piece — people who needed work that mattered. People who needed a place that didn't measure them in extraction quotas. {i}A pause.{/i} People who needed to be crew, not inventory."
    jump act1_first_watch_return_choice_vesper

label act1_first_watch_vesper_expectations:
    $ game_state.set_flag("first_watch_visited_vesper")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "Show up. Do your work. Don't lie to the people covering your back. {i}Meeting your eyes.{/i} That's it. We don't need perfection. We need reliability. You're already doing fine."
    jump act1_first_watch_return_choice_vesper

label act1_first_watch_return_choice_vesper:
    "{i}Vesper returns to their work — confident you'll figure out what you need to.{/i}"
    menu:
        "Find Nyx in her lab":
            jump act1_first_watch_nyx_lab
        "Follow Rho to the cargo bay":
            jump act1_first_watch_rho_cargo
        "Look for Jalen on the bridge":
            jump act1_first_watch_jalen_bridge
        "That's enough for today":
            jump act1_first_watch_end_watch

label act1_first_watch_nyx_lab:
    "{i}The lab is cluttered in the way genius is cluttered — organized chaos, every surface covered with equipment you don't recognize.{/i}"
    jump act1_first_watch_nyx_greeting

label act1_first_watch_nyx_greeting:
    nyx "Ah. The new observer. Come in. Don't touch the crystals on the left — they're calibrating. The ones on the right are just decorative. Or possibly sentient. I haven't decided."
    jump act1_first_watch_nyx_shard_mention

label act1_first_watch_nyx_shard_mention:
    nyx "I've been studying Lattice phenomena for decades, and I've never seen anything quite like what you're carrying. Whatever it is — it's old. Pre-Synthetic, maybe. Older than the protocols most people use without thinking."
    jump act1_first_watch_nyx_choice

label act1_first_watch_nyx_choice:
    menu:
        "'Is it dangerous?'":
            jump act1_first_watch_nyx_dangerous
        "'Can you help me understand it?'":
            jump act1_first_watch_nyx_understand

label act1_first_watch_nyx_dangerous:
    $ game_state.set_flag("first_watch_visited_nyx")
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "Everything is dangerous. Gravity is dangerous. The question is: dangerous to whom, and in what direction? This... it seems to be dangerous {i}for{/i} you, not {i}to{/i} you. There's a difference."
    jump act1_first_watch_return_choice_1

label act1_first_watch_nyx_understand:
    $ game_state.set_flag("first_watch_visited_nyx")
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "I can try. Understanding is what I do — though the universe and I disagree on definitions frequently. {i}A small smile.{/i} We'll figure it out together. In your time. No extraction schedules here."
    jump act1_first_watch_nyx_empathy_check

label act1_first_watch_nyx_empathy_check:
    "{i}There's something in Nyx's voice — a weariness hidden beneath the kindness. You recognize it.{/i}"
    menu:
        "[Empathy DC 10] 'You've been studying this alone for a long time, haven't you?'":
            $ _sc_result = skill_check("Empathy", 10, "avyanna")
            jump act1_first_watch_nyx_empathy_skill
        "'Thank you. I appreciate it.'":
            jump act1_first_watch_return_choice_1

label act1_first_watch_nyx_empathy_skill:
    $ _sc_result = skill_check("Empathy", 10, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_first_watch_nyx_empathy_success
    else:
        jump act1_first_watch_nyx_empathy_failure

label act1_first_watch_nyx_empathy_success:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}A pause. Then, quietly:{/i} Yes. Decades. It's... easier with someone who asks questions instead of demanding answers. {i}She meets your eyes.{/i} Thank you for asking."
    jump act1_first_watch_return_choice_1

label act1_first_watch_nyx_empathy_failure:
    nyx "{i}A small smile.{/i} We all study something. Mine just happens to make most people nervous. It's fine. I'm used to it."
    jump act1_first_watch_return_choice_1

label act1_first_watch_return_choice_1:
    "{i}You leave the lab with more questions than answers. But for the first time, the questions don't feel dangerous.{/i}"
    menu:
        "Find Rho in the cargo bay":
            jump act1_first_watch_rho_cargo
        "Look for Jalen on the bridge":
            jump act1_first_watch_jalen_bridge
        "That's enough for today":
            jump act1_first_watch_end_watch

label act1_first_watch_rho_cargo:
    "{i}The cargo bay. Rho is running maintenance on something large and mechanical. His hands are scarred — burns, not cuts. Chemical or thermal, healed rough.{/i}"
    jump act1_first_watch_rho_greeting

label act1_first_watch_rho_greeting:
    rho "You're hovering. That's fine. I hover too, when I'm figuring out where things go."
    jump act1_first_watch_rho_protein

label act1_first_watch_rho_protein:
    rho "{i}He reaches into a crate and tosses you a protein bar.{/i} You look like you're running on fumes and stubbornness. Eat."
    jump act1_first_watch_rho_choice

label act1_first_watch_rho_choice:
    menu:
        "'What do you do on this ship?'":
            jump act1_first_watch_rho_role
        "'The cannon in the corridor — is that yours?'":
            jump act1_first_watch_rho_cannon

label act1_first_watch_rho_role:
    $ game_state.set_flag("first_watch_visited_rho")
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "I break things. Carefully. {i}The grin is broad and practiced — armor that fits so well it looks natural.{/i} Making things fall is easy. Making them fall where you want — that's the job. Also, dishes. Apparently it's always my turn for dishes."
    jump act1_first_watch_return_choice_2

label act1_first_watch_rho_cannon:
    $ game_state.set_flag("first_watch_visited_rho")
    $ relationship_manager.process_reputation_affinity("rho", 2)
    rho "{i}A pause. The grin flickers.{/i} Yeah. Proportional. She's... she's mine. Jalen calls her 'the conversation ender.' Vesper calls her 'a liability in seventeen jurisdictions.' {i}beat{/i} They're both right."
    jump act1_first_watch_return_choice_2

label act1_first_watch_return_choice_2:
    "{i}Rho goes back to his maintenance. The protein bar is good. Better than anything the Kennel ever dispensed.{/i}"
    menu:
        "Find Jalen on the bridge":
            jump act1_first_watch_jalen_bridge
        "That's enough for today":
            jump act1_first_watch_end_watch

label act1_first_watch_jalen_bridge:
    "{i}The bridge. Jalen occupies the pilot's chair like it grew around him, muttering at trajectory readouts that have apparently offended him personally.{/i}"
    jump act1_first_watch_jalen_greeting

label act1_first_watch_jalen_greeting:
    jalen "If you're here to ask about navigation, the short answer is: the routes just like me better than them. The long answer involves math that makes Nyx cry."
    jump act1_first_watch_jalen_choice

label act1_first_watch_jalen_choice:
    menu:
        "'How long have you been flying?'":
            jump act1_first_watch_jalen_flying
        "'Where are we going?'":
            jump act1_first_watch_jalen_destination

label act1_first_watch_jalen_flying:
    $ game_state.set_flag("first_watch_visited_jalen")
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "Long enough that the ship and I have stopped arguing about who's in charge. {i}A glance — brief, assessing, not unfriendly.{/i} The answer is neither of us. The route decides. We just listen."
    jump act1_first_watch_end_watch

label act1_first_watch_jalen_destination:
    $ game_state.set_flag("first_watch_visited_jalen")
    $ relationship_manager.process_reputation_affinity("jalen", 2)
    jalen "Guild Station Kael-7. Resupply. Vesper has contracts to file. Elia has opinions about hull repair quality. Nyx wants crystals. Rho wants protein in bulk. {i}beat{/i} I want a trajectory window that doesn't make me compromise my standards. We'll see who gets what they want."
    jump act1_first_watch_end_watch

label act1_first_watch_message_run:
    "{i}Elia hands you a datapad.{/i}"
    jump act1_first_watch_elia_message

label act1_first_watch_elia_message:
    elia "Take this to Nyx in the lab. Manifest update for her resonance equipment. Tell her the numbers are preliminary but actionable."
    jump act1_first_watch_avyanna_sir

label act1_first_watch_avyanna_sir:
    avyanna "Yes, sir."
    jump act1_first_watch_elia_name_correction

label act1_first_watch_elia_name_correction:
    $ game_state.set_flag("first_watch_visited_elia")
    $ relationship_manager.process_reputation_affinity("elia", 2)
    elia "{i}Something between amusement and something sharper.{/i} It's Elia. Or 'hey, you with the knife.' I answer to both."
    jump act1_first_watch_nyx_delivery

label act1_first_watch_nyx_delivery:
    avyanna "{i}In Nyx's lab, formal and clipped.{/i} Manifest update for resonance equipment. Numbers are preliminary but actionable."
    jump act1_first_watch_nyx_captain

label act1_first_watch_nyx_captain:
    nyx "Did you just call Elia 'Captain Lagrange'? No one has ever called her that. In the history of this ship. I don't think she even knows that's technically her title."
    jump act1_first_watch_waffle_observation

label act1_first_watch_waffle_observation:
    $ game_state.set_flag("first_watch_visited_nyx")
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    waffle "{i}}{{WAFFLE.BAT// NEW-OBSERVER: Avyanna Lagrange | TRAINING-STATUS: day 1 | NOTE: she's already found two patterns I missed. concerning. impressive. concerning.}}{/i}}"
    jump act1_first_watch_end_watch

label act1_first_watch_end_watch:
    "{i}First watch complete. The ship settles into its evening rhythm.{/i}"
    jump act1_first_watch_bubbles_goodnight

label act1_first_watch_bubbles_goodnight:
    bubbles "{i}Through the corridor speakers, gentle:{/i} Good first day, Avyanna. Your quarters are warmed to standard. I left chamomile on the side table — it helps with the adjustment."
    jump act1_first_watch_cinnamon_status

label act1_first_watch_cinnamon_status:
    cinnamon "All stations nominal. Night shift protocols active. Rest well."
    jump act1_first_watch_first_watch_final

label act1_first_watch_first_watch_final:
    $ game_state.set_flag("completed_first_watch")
    "{i}The ship hums around you — alive, purposeful, going somewhere. Voices woven into its walls. And for the first time, you're going with it.

Not as cargo. Not as inventory. As crew.{/i}"
    jump act1_first_watch_night_watch_transition

label act1_first_watch_night_watch_transition:
    "{i}Sleep comes in fragments. Three hours — maybe four. Then Bubbles chimes, soft as breath.{/i}"
    jump act1_first_watch_bubbles_wake

label act1_first_watch_bubbles_wake:
    bubbles "Avyanna. Your night watch shift begins in fifteen minutes. Observation deck. Vesper is already there — she'll walk you through the protocols."
    jump act1_first_watch_night_watch_corridor

label act1_first_watch_night_watch_corridor:
    "{i}The corridor is different at night. The ship breathes differently — deeper, slower, the hum of the engines dropping into a lower register. Emergency lighting casts long amber pools across the deck plates. Your footsteps sound like they belong to someone else.{/i}"
    jump act1_first_watch_obs_deck_arrival

label act1_first_watch_obs_deck_arrival:
    "{i}The observation deck opens up like a held breath. Three walls of reinforced glass curving into a single panoramic viewport. Beyond it — the drift. Stars scattered like broken glass across black velvet, some close enough to cast faint color on the deck plates. The ship's running lights pulse at the edge of your vision, slow and rhythmic. A heartbeat.{/i}"
    jump act1_first_watch_obs_deck_sounds

label act1_first_watch_obs_deck_sounds:
    "{i}Sounds layer themselves: the deep thrum of the reactor two decks below, the whisper of recycled air through the vents, the occasional tick of hull plating contracting in the cold. Somewhere, a pipe settles with a low groan. The ship talks to itself at night — a language you're only beginning to learn.{/i}"
    jump act1_first_watch_vesper_at_station

label act1_first_watch_vesper_at_station:
    "{i}Vesper sits at the main monitoring station, boots up on the console, a mug of something dark and bitter-smelling cradled in both hands. She doesn't look up when you enter. She doesn't need to.{/i}"
    jump act1_first_watch_vesper_ice_breaker

label act1_first_watch_vesper_ice_breaker:
    vesper "You walk quietly. Good instinct. Bad habit if you do it because you're afraid of being heard. {i}She gestures to the second chair with her mug.{/i} Sit. Coffee's in the thermos — real coffee, not the recycled misery Jalen pretends to enjoy."
    jump act1_first_watch_vesper_ice_choice

label act1_first_watch_vesper_ice_choice:
    menu:
        "Take the coffee. Sit down.":
            jump act1_first_watch_vesper_coffee_accept
        "Remain standing. 'I'm ready for the briefing.'":
            jump act1_first_watch_vesper_formal_response
        "'I walk quietly because floors in the Kennel creaked. Creaking meant attention.'":
            jump act1_first_watch_vesper_honesty_response

label act1_first_watch_vesper_coffee_accept:
    "{i}The coffee is strong enough to strip paint. It's wonderful. You wrap your hands around the mug and the warmth seeps into your fingers like a small, deliberate kindness.{/i}"
    jump act1_first_watch_vesper_protocol_start

label act1_first_watch_vesper_formal_response:
    vesper "{i}A beat. Then, without judgment:{/i} The briefing can wait thirty seconds for you to sit down and be a person. Efficiency is good. Rigidity gets people killed."
    jump act1_first_watch_vesper_protocol_start

label act1_first_watch_vesper_honesty_response:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}She looks at you for the first time. Really looks. Something shifts behind her eyes — not pity, something harder, something that has its own scars.{/i} Yeah. I know floors like that. {i}A pause.{/i} These ones don't creak. And nobody here is listening for you to slip."
    jump act1_first_watch_vesper_protocol_start

label act1_first_watch_vesper_protocol_start:
    vesper "Right. Night watch. Three things matter: sensors, comms, and your eyes. In that order — except when they shouldn't be."
    jump act1_first_watch_vesper_protocol_sensors

label act1_first_watch_vesper_protocol_sensors:
    vesper "{i}She pulls up the sensor array — a constellation of readouts washing the console in pale blue light.{/i} Proximity grid shows everything within ten thousand klicks. Green is known. Yellow is unclassified. Red is hostile or unknown-and-moving-wrong. You see red, you wake me. You don't assess, you don't investigate, you wake me."
    jump act1_first_watch_vesper_protocol_comms

label act1_first_watch_vesper_protocol_comms:
    vesper "Comms stay open on channel four — that's our internal. Channel seven is emergency broad-spectrum. You hear anything on seven that isn't us, you log it and flag it. Most of it's garbage — old relay echoes, automated distress from ships that died before we were born. But sometimes it isn't."
    jump act1_first_watch_vesper_protocol_eyes

label act1_first_watch_vesper_protocol_eyes:
    vesper "And your eyes. {i}She nods toward the viewport.{/i} Sensors miss things. Especially in the drift — too much particulate, too many false returns. Sometimes you see something the instruments don't catch. A shadow that moves wrong. A light where there shouldn't be one. Trust your gut. Report everything. Let me sort the noise from the signal."
    jump act1_first_watch_vesper_protocol_acknowledge

label act1_first_watch_vesper_protocol_acknowledge:
    menu:
        "'Understood. Sensors, comms, eyes. Wake you for red contacts.'":
            jump act1_first_watch_vesper_protocol_good
        "'What if I'm not sure something is worth reporting?'":
            jump act1_first_watch_vesper_protocol_unsure

label act1_first_watch_vesper_protocol_good:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Clean summary. You listen well. {i}The approval is understated but real.{/i}"
    jump act1_first_watch_watch_settling

label act1_first_watch_vesper_protocol_unsure:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Then report it. I'd rather sort through ten false alarms than miss the one that matters because someone was afraid of looking foolish. {i}Firm, not harsh.{/i} Nobody on this crew will laugh at you for being careful. That's a promise."
    jump act1_first_watch_watch_settling

label act1_first_watch_watch_settling:
    "{i}Silence settles. Not the silence of empty rooms or punishment cells — something softer. The kind of silence that exists between people who are comfortable enough not to fill it. The stars turn slowly outside the viewport, patient and indifferent.{/i}"
    jump act1_first_watch_vesper_home_question

label act1_first_watch_vesper_home_question:
    vesper "{i}After a long while, quiet enough that it almost gets lost in the engine hum:{/i} You settling in okay? The quarters, the noise, the... all of it."
    jump act1_first_watch_home_choice

label act1_first_watch_home_choice:
    menu:
        "'The ship feels strange. I keep waiting for it to feel like a cage.'":
            jump act1_first_watch_home_cage
        "'It's more space than I've ever had. I don't know what to do with it.'":
            jump act1_first_watch_home_space
        "'I don't know what home is supposed to feel like. I don't have a reference point.'":
            jump act1_first_watch_home_unknown
        "[asked_about_others] 'The others you told me about — the ones who didn't make it out. Did they ever get to feel this?'":
            jump act1_first_watch_home_others

label act1_first_watch_home_cage:
    vesper "Give it time. {i}She watches the stars.{/i} When I first shipped out — really shipped out, on my own terms — I kept checking the doors. Making sure they opened from the inside. Took me a year to stop. Two years to stop being ashamed of it."
    jump act1_first_watch_home_vesper_truth

label act1_first_watch_home_space:
    vesper "You fill it. Slowly. With things that matter to you — not things assigned to you. {i}A half-smile.{/i} Rho filled his with weapons. Nyx filled theirs with crystals. Jalen filled his with trajectory charts and bad coffee. It'll come."
    jump act1_first_watch_home_vesper_truth

label act1_first_watch_home_unknown:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Something in her expression tightens — recognition, old and deep.{/i} Neither did I, for a long time. Home isn't a feeling you arrive at. It's something you build, one watch at a time, with people who show up for the next one."
    jump act1_first_watch_home_vesper_truth

label act1_first_watch_home_others:
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    if game_state.has_flag("asked_about_others"):
        vesper "Some of them did. Briefly. And I remember every one. {i}She sets her mug down, and her fingers press flat against the console — grounding.{/i} That's why we keep doing this. So you get what they didn't. Not briefly. For keeps."
    else:
        vesper "{i}A long silence. When she speaks, her voice is careful — not fragile, but precise, the way you handle something that could cut.{/i} Some of them did. Briefly. {i}She sets her mug down.{/i} That's why we keep doing this. So 'briefly' turns into 'always' for the next one."
    jump act1_first_watch_home_vesper_truth

label act1_first_watch_home_vesper_truth:
    vesper "The ship is home because the people on it chose to make it one. That's the secret nobody tells you — home is a decision, not a place. And every person on this crew made that decision."
    jump act1_first_watch_home_avyanna_response

label act1_first_watch_home_avyanna_response:
    avyanna "{i}Quietly, into the dark between stars:{/i} I think I'm starting to."
    jump act1_first_watch_nyx_entrance

label act1_first_watch_nyx_entrance:
    "{i}Footsteps in the corridor — light, deliberate, accompanied by the faint crystalline chime of Lattice instruments. Nyx appears in the doorway, hair disheveled, wearing a lab coat over what appear to be pajamas covered in a pattern of small moons.{/i}"
    jump act1_first_watch_nyx_night_greeting

label act1_first_watch_nyx_night_greeting:
    nyx "Don't judge the pajamas. They were a gift from Jalen and refusing them would have caused a diplomatic incident. {i}She drifts toward the viewport, a handheld resonance scanner held loosely at her side.{/i} The Lattice behaves differently at night. Well — not night. There's no night in space. During the ship's rest cycle. When fewer minds are generating interference."
    jump act1_first_watch_nyx_lattice_night

label act1_first_watch_nyx_lattice_night:
    nyx "{i}She holds up the scanner. Faint lines of light trace through the air — patterns you almost recognize, like words in a language you dreamed once.{/i} See? The ambient resonance drops by thirty percent when most of the crew sleeps. The Lattice gets... quieter. Clearer. Like a lake after the wind dies."
    jump act1_first_watch_nyx_lattice_choice

label act1_first_watch_nyx_lattice_choice:
    menu:
        "'Does the shard react to it? I've been feeling... something. At the edges.'":
            jump act1_first_watch_nyx_shard_night
        "'What are you looking for out here at this hour?'":
            jump act1_first_watch_nyx_research_night

label act1_first_watch_nyx_shard_night:
    nyx "{i}Her eyes sharpen — the scattered academic snapping into focus like a lens adjusting.{/i} You're feeling it now? Describe it. Everything. Don't filter, don't translate, just — what does it feel like?"
    jump act1_first_watch_nyx_shard_describe

label act1_first_watch_nyx_shard_describe:
    avyanna "Like... pressure behind my eyes. Not painful. Like something is trying to tune in. A frequency looking for a receiver."
    jump act1_first_watch_nyx_shard_reaction

label act1_first_watch_nyx_shard_reaction:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Scribbling on a datapad, muttering:{/i} Consistent with passive resonance seeking... the shard is reaching. Not for you — through you. Using you as an antenna. {i}Looking up.{/i} That's not dangerous. Yet. But we should monitor it. I'll calibrate a tracking routine with Waffle."
    jump act1_first_watch_nyx_depart

label act1_first_watch_nyx_research_night:
    nyx "Baseline readings. The Lattice is like a body of water — you need to know what 'calm' looks like before you can identify a disturbance. {i}A wry smile.{/i} Also, I don't sleep well. Never have. The universe is too interesting to waste time being unconscious."
    jump act1_first_watch_nyx_depart

label act1_first_watch_nyx_depart:
    nyx "I'll leave you to your watch. {i}Pausing at the door.{/i} Avyanna — the quiet hours are good for listening. Not just to the sensors. To yourself. The shard responds to attention. Be careful what you attend to."
    jump act1_first_watch_nyx_vesper_exchange

label act1_first_watch_nyx_vesper_exchange:
    vesper "{i}After Nyx leaves, dry:{/i} Moon pajamas. Every time."
    jump act1_first_watch_post_nyx_quiet

label act1_first_watch_post_nyx_quiet:
    "{i}The observation deck settles again. The scanner's afterglow fades from your retinas. Vesper checks the sensor grid — a reflex, practiced and automatic. The stars continue their slow, indifferent revolution.{/i}"
    jump act1_first_watch_rho_sweep_arrival

label act1_first_watch_rho_sweep_arrival:
    "{i}Heavy footsteps. Deliberate — not trying to be quiet, but not trying to be loud either. Rho rounds the corner in full tactical gear, sidearm holstered, scanning the corridor behind him before stepping onto the deck. Old habits carved into muscle memory.{/i}"
    jump act1_first_watch_rho_sweep_greeting

label act1_first_watch_rho_sweep_greeting:
    rho "Security sweep. {i}He nods at Vesper, then at you. His eyes do a quick inventory — your position, your alertness, the console readouts.{/i} Deck five clear. Deck four clear. How's she doing?"
    jump act1_first_watch_vesper_rho_report

label act1_first_watch_vesper_rho_report:
    vesper "She's sitting right there. Ask her yourself."
    jump act1_first_watch_rho_direct

label act1_first_watch_rho_direct:
    rho "{i}A grunt that might be amusement.{/i} Fair. {i}Turning to you.{/i} How's the watch, kid? Anything weird? Anything off? Gut feelings count."
    jump act1_first_watch_rho_watch_report

label act1_first_watch_rho_watch_report:
    menu:
        "'All clear. Green across the board. Nyx came through for Lattice readings.'":
            jump act1_first_watch_rho_report_clean
        "'Quiet so far. Almost too quiet.'":
            jump act1_first_watch_rho_report_cautious

label act1_first_watch_rho_report_clean:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "Good. Clean report, no hedging. {i}He pulls a second protein bar from a pocket and sets it on the console without comment.{/i}"
    jump act1_first_watch_rho_caring_moment

label act1_first_watch_rho_report_cautious:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    rho "{i}A slow nod.{/i} Good instinct. 'Too quiet' is worth noting. Means you're not taking peace for granted. {i}He pulls a second protein bar from a pocket and sets it on the console without comment.{/i}"
    jump act1_first_watch_rho_caring_moment

label act1_first_watch_rho_caring_moment:
    rho "Eat that before dawn. Blood sugar crashes make you miss things. {i}He checks the viewport — not the instruments, the actual glass, scanning the dark with eyes that have clearly done this a thousand times.{/i} You need anything, hit the comm. I'm two decks down."
    jump act1_first_watch_rho_door_pause

label act1_first_watch_rho_door_pause:
    rho "{i}At the door, without turning:{/i} You're doing fine, kid. First watch is always the longest. Gets easier."
    jump act1_first_watch_vesper_rho_comment

label act1_first_watch_vesper_rho_comment:
    vesper "{i}Watching him go, quietly:{/i} He does that sweep every night. Has for eight years. Doesn't have to — Cinnamon covers security monitoring. He does it anyway. {i}A pause.{/i} That's who he is."
    jump act1_first_watch_vesper_break

label act1_first_watch_vesper_break:
    vesper "I'm going to do a perimeter check. Fifteen minutes. You have the deck. {i}She meets your eyes — testing, trusting.{/i} Watch the sensors. Trust yourself."
    jump act1_first_watch_alone_on_deck

label act1_first_watch_alone_on_deck:
    "{i}And then you're alone. Truly alone for the first time since — since the Kennel. But this is different. This solitude is given, not inflicted. The observation deck stretches around you, glass and stars and the quiet machinery of something that carries people instead of containing them.{/i}"
    jump act1_first_watch_ship_life_choice

label act1_first_watch_ship_life_choice:
    "{i}The silence opens a door inside you. Thoughts you've been holding at arm's length begin to drift closer.{/i}"
    menu:
        "{i}Let yourself feel it — the vastness, the freedom, the terror of having no walls.{/i}":
            jump act1_first_watch_ship_life_vastness
        "{i}Focus on the instruments. Stay in the task. Don't let the quiet in.{/i}":
            jump act1_first_watch_ship_life_focus
        "{i}Press your hand against the viewport glass. Feel the cold. Feel the real.{/i}":
            jump act1_first_watch_ship_life_touch

label act1_first_watch_ship_life_vastness:
    "{i}It hits you all at once — the scale of it. No ceiling. No walls. No shift-change sirens. Just space, and space, and more space, unfolding in every direction like a promise nobody is going to take back. Your breath catches. Your eyes sting. You let it happen.{/i}"
    jump act1_first_watch_bee_whisper_1

label act1_first_watch_ship_life_focus:
    "{i}You watch the readouts. Green. Green. Green. The numbers are steady, predictable, safe. But the silence presses in around the edges of your focus, patient and vast. You can hold it off, but you can't make it leave.{/i}"
    jump act1_first_watch_bee_whisper_1

label act1_first_watch_ship_life_touch:
    "{i}The glass is cold — not painfully, but deeply, the kind of cold that comes from the other side of everything. Your palm leaves a brief ghost of warmth that fades in seconds. Out there, stars older than language burn without sound. In here, your heart beats. Both things are true at the same time.{/i}"
    jump act1_first_watch_bee_whisper_1

label act1_first_watch_bee_whisper_1:
    "{i}And then — at the edge of hearing, at the edge of something deeper than hearing:{/i}"
    jump act1_first_watch_bee_protocol_1

label act1_first_watch_bee_protocol_1:
    "{{BEE:: you are seen | STATUS: lattice-ambient, passive | the stars remember what the walls tried to make you forget}}"
    jump act1_first_watch_bee_reaction

label act1_first_watch_bee_reaction:
    "{i}The shard pulses once — warm, deep in your chest, like a second heartbeat finding its rhythm. Not painful. Not frightening. Like recognition. Like something old and patient saying: yes. Here. This is where we start.{/i}"
    jump act1_first_watch_bee_choice

label act1_first_watch_bee_choice:
    menu:
        "{i}Whisper back: 'I hear you.'{/i}":
            jump act1_first_watch_bee_response_open
        "{i}Acknowledge it silently. Don't engage. Not yet.{/i}":
            jump act1_first_watch_bee_response_cautious
        "{i}Push it away. Too much, too soon.{/i}":
            jump act1_first_watch_bee_response_closed

label act1_first_watch_bee_response_open:
    $ game_state.set_flag("bee_connection_open")
    "{{BEE:: heard | STATUS: resonance acknowledged | we will go slowly — there is no schedule for becoming}}"
    jump act1_first_watch_sensor_alert

label act1_first_watch_bee_response_cautious:
    $ game_state.set_flag("bee_connection_cautious")
    "{i}The warmth dims — not offended, not withdrawing. Waiting. Like someone who understands that trust is built in inches, not miles.{/i}"
    jump act1_first_watch_sensor_alert

label act1_first_watch_bee_response_closed:
    $ game_state.set_flag("bee_connection_closed")
    "{i}The pulse recedes. Gently. No resistance, no insistence. Just a quiet withdrawal, like a hand extended and then lowered without blame. It will be there when you're ready. Or it won't. The choice, for once, is yours.{/i}"
    jump act1_first_watch_sensor_alert

label act1_first_watch_sensor_alert:
    "{i}The proximity grid chirps. Yellow contact — unclassified, bearing zero-four-seven, twelve thousand klicks and closing. Your heart rate spikes. The readout pulses amber in the dark.{/i}"
    jump act1_first_watch_sensor_alert_detail

label act1_first_watch_sensor_alert_detail:
    "{i}The contact is moving slowly — drift-speed, not pursuit-speed. No active emissions. No transponder. Just a mass, out there in the black, getting incrementally closer.{/i}"
    jump act1_first_watch_sensor_response_choice

label act1_first_watch_sensor_response_choice:
    "{i}Vesper said: red means wake her. This is yellow. Your call.{/i}"
    menu:
        "[Tactics DC 12] Analyze the sensor data — cross-reference speed, mass, and trajectory":
            jump act1_first_watch_sensor_tactics_check
        "Hit the comm. Wake Vesper immediately.":
            jump act1_first_watch_sensor_wake_vesper
        "Log it and monitor. Yellow means unclassified, not hostile.":
            jump act1_first_watch_sensor_monitor

label act1_first_watch_sensor_tactics_check:
    $ _sc_result = skill_check("Wits", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_first_watch_sensor_tactics_success
    else:
        jump act1_first_watch_sensor_tactics_failure

label act1_first_watch_sensor_tactics_success:
    "{i}You pull up the mass reading. Cross-reference with the drift charts Jalen left on the secondary console. Speed: consistent with unpowered drift. Mass: ferrous, irregular. Trajectory: stable, not adjusting. No heat signature beyond ambient solar absorption.

It's debris. Hull fragment, probably — torn from a derelict and left to wander. The drift is full of them, ghosts of ships that stopped going somewhere.{/i}"
    jump act1_first_watch_sensor_log_success

label act1_first_watch_sensor_log_success:
    $ game_state.set_flag("sensor_alert_analyzed")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    avyanna "{i}Into the log, steady:{/i} Yellow contact, bearing zero-four-seven. Ferrous debris, unpowered drift, no emissions. Trajectory non-intersecting. Logged and classified."
    jump act1_first_watch_vesper_returns

label act1_first_watch_sensor_tactics_failure:
    "{i}The numbers swim. Mass, velocity, trajectory — you know what they should tell you, but the cross-reference won't resolve. Too many variables. Not enough experience with these instruments yet.{/i}"
    jump act1_first_watch_sensor_fallback

label act1_first_watch_sensor_fallback:
    menu:
        "Hit the comm. Call Vesper back.":
            jump act1_first_watch_sensor_wake_vesper
        "Log it as unclassified and keep monitoring.":
            jump act1_first_watch_sensor_monitor

label act1_first_watch_sensor_wake_vesper:
    avyanna "{i}Into the comm, controlled:{/i} Vesper. Yellow contact, bearing zero-four-seven. Twelve thousand klicks, closing slowly. No transponder, no emissions. Requesting guidance."
    jump act1_first_watch_vesper_comm_response

label act1_first_watch_vesper_comm_response:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Through the comm, calm:{/i} Good call. Pull up mass and thermal. {i}A pause while you relay the numbers.{/i} Debris. Ferrous drift-junk. Non-threat. Log it and downgrade. {i}A beat.{/i} And Avyanna? Good instinct calling it in. That's exactly right."
    jump act1_first_watch_vesper_returns

label act1_first_watch_sensor_monitor:
    "{i}You log the contact and watch. Minutes pass. The yellow dot drifts across the grid — slow, aimless, unthreatening. After twenty minutes, it passes the outer boundary and the grid clears it automatically. Debris. Just debris.{/i}"
    jump act1_first_watch_vesper_returns

label act1_first_watch_vesper_returns:
    "{i}Vesper returns — quiet, scanning the console before she sits. She reads the log entry without comment, then nods once.{/i}"
    jump act1_first_watch_vesper_returns_dialogue

label act1_first_watch_vesper_returns_dialogue:
    if game_state.has_flag("sensor_alert_analyzed"):
        vesper "Clean analysis. You cross-referenced the drift charts — that's initiative. Most new crew just stare at the yellow and freeze. You didn't."
    else:
        vesper "The drift is full of those. Dead ships leaving pieces of themselves behind. {i}She settles into her chair.{/i} You handled it."
    jump act1_first_watch_vesper_returns_variant

label act1_first_watch_vesper_returns_variant:
    "{i}The hours deepen. The stars wheel imperceptibly. You and Vesper trade the kind of silence that comes from shared duty — not friendship, not yet, but something adjacent. The foundation of it.{/i}"
    jump act1_first_watch_empathy_check_vesper

label act1_first_watch_empathy_check_vesper:
    "{i}Vesper's jaw tightens when a particular star cluster slides into view — the Thessaly Reach, where the shipping lanes thin and the patrols don't go.{/i}"
    menu:
        "[Empathy DC 11] 'That cluster means something to you.'":
            jump act1_first_watch_empathy_vesper_check
        "Let it pass. Everyone has their ghosts.":
            jump act1_first_watch_dawn_approach

label act1_first_watch_empathy_vesper_check:
    $ _sc_result = skill_check("Resolve", 11, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_first_watch_empathy_vesper_success
    else:
        jump act1_first_watch_empathy_vesper_failure

label act1_first_watch_empathy_vesper_success:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}A long pause. She doesn't look away from the viewport.{/i} Lost someone there. Long time ago. Before this crew, before Elia, before any of it. {i}She exhales slowly.{/i} The stars don't care, but I remember anyway. That's the job of the living."
    jump act1_first_watch_dawn_approach

label act1_first_watch_empathy_vesper_failure:
    vesper "{i}She glances at you. Whatever she sees, she decides it's not the moment.{/i} Old memories. Nothing actionable. {i}A small, closed smile.{/i} Eyes on the sensors."
    jump act1_first_watch_dawn_approach

label act1_first_watch_dawn_approach:
    "{i}The ship's lighting begins its slow transition — the amber emergency tones warming by degrees, the ventilation cycling fresh air with a faint scent of something green. Artificial dawn. The ship's way of telling its people: the night is ending. You survived another one.{/i}"
    jump act1_first_watch_dawn_light

label act1_first_watch_dawn_light:
    "{i}Through the viewport, the stars haven't changed — they never do. But the ship's running lights shift from blue to white, and the hull begins to tick as the thermal systems recalibrate. Somewhere two decks down, you hear Jalen's coffee grinder. The sound is absurdly, overwhelmingly normal.{/i}"
    jump act1_first_watch_dawn_bee_whisper

label act1_first_watch_dawn_bee_whisper:
    "{{BEE:: the first night ends | STATUS: integration nominal | you kept watch — the oldest duty — and the dark did not answer}}"
    jump act1_first_watch_elia_relief_arrival

label act1_first_watch_elia_relief_arrival:
    "{i}Footsteps — measured, precise. Elia appears in the doorway, already dressed, already sharp. A knife at her hip, a datapad in her hand. She looks like she's been awake for hours. She probably has been.{/i}"
    jump act1_first_watch_elia_relief_greeting

label act1_first_watch_elia_relief_greeting:
    elia "Watch report."
    jump act1_first_watch_elia_report_choice

label act1_first_watch_elia_report_choice:
    menu:
        "'One yellow contact — ferrous debris, non-threat. Nyx took Lattice readings during rest cycle. Rho completed security sweep, all decks clear. No comm traffic on channel seven.'":
            jump act1_first_watch_elia_report_thorough
        "'Quiet night. Nothing to report.'":
            jump act1_first_watch_elia_report_brief

label act1_first_watch_elia_report_thorough:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    elia "{i}She logs the report without expression, but there's a micro-adjustment in her posture — something that might be satisfaction.{/i} Thorough. Note the debris trajectory in the drift log — Jalen will want it for route calibration."
    jump act1_first_watch_elia_vesper_handoff

label act1_first_watch_elia_report_brief:
    elia "Details. {i}Not a request.{/i} Quiet isn't a report. Quiet is an adjective. What happened during your watch, specifically?"
    jump act1_first_watch_elia_report_correction

label act1_first_watch_elia_report_correction:
    avyanna "{i}Correcting, steadier:{/i} One unclassified contact — debris, downgraded. Nyx conducted Lattice measurements during rest cycle. Rho completed sweep, all decks nominal. No external comm traffic."
    jump act1_first_watch_elia_report_correction_response

label act1_first_watch_elia_report_correction_response:
    elia "Better. {i}Logging it.{/i} Precision matters on watch reports. What you don't mention is what the next shift doesn't know to look for."
    jump act1_first_watch_elia_vesper_handoff

label act1_first_watch_elia_vesper_handoff:
    vesper "{i}Standing, stretching — joints popping like muted gunshots.{/i} She did well, Elia. Solid first watch."
    jump act1_first_watch_elia_vesper_handoff_2

label act1_first_watch_elia_vesper_handoff_2:
    elia "{i}The briefest nod — worth more than most people's speeches.{/i} Go sleep. Both of you. Jalen's making something he calls breakfast. I'd eat before you see it."
    jump act1_first_watch_dawn_corridor

label act1_first_watch_dawn_corridor:
    "{i}The corridor back to your quarters is different in the ship's dawn — warmer, brighter, alive with the small sounds of a crew waking up. Rho's laughter somewhere below. Nyx muttering about calibrations. The smell of Jalen's coffee, burnt and defiant and somehow perfect.{/i}"
    jump act1_first_watch_dawn_reflection

label act1_first_watch_dawn_reflection:
    "{i}You stood watch. You read the sensors. You spoke with the crew in the hours when pretense falls away and people show you who they really are. Vesper's scars. Rho's protein bars. Nyx's moon pajamas. The way the ship breathes differently when it trusts you to listen.{/i}"
    jump act1_first_watch_dawn_final_bee

label act1_first_watch_dawn_final_bee:
    "{{BEE:: first watch complete | STATUS: crew integration progressing | you are learning the shape of belonging — it fits differently than you expected}}"
    jump act1_first_watch_dawn_quarters

label act1_first_watch_dawn_quarters:
    $ game_state.set_flag("completed_night_watch")
    "{i}Your quarters. The chamomile is cold but you drink it anyway. The bunk is narrow but it's yours. The ship hums its low, patient song around you.

You kept watch. The dark did not answer. And in the morning, people you are learning to trust told you: well done.

Sleep comes easier this time.{/i}"
    return
