## act1_deep_vesper.rpy — Auto-generated from act1_deep_vesper.json
## 155 dialogue nodes

label act1_deep_vesper:
    $ game_state.mark_dialogue_played("act1_deep_vesper")
    jump act1_deep_vesper_start

label act1_deep_vesper_start:
    if game_state.has_flag("first_watch_visited_vesper"):
        "Vesper sits alone in the observation deck, the viewport framing her silhouette against the void. She's cleaning Clarity — slow, methodical movements that suggest ritual more than maintenance.

She glances up as Avyanna enters. \"You again. Guess I'm predictable.\""
    elif game_state.has_flag("nyx_saw_shard"):
        "Vesper sits alone in the observation deck, star charts spread across the nav console like a paper battlefield. The viewport casts cold light across her hands. She's cleaning Clarity — slow, methodical — but her eyes keep drifting to the shard-burn scar on the bulkhead where Nyx's episode blew out a conduit last week.

She doesn't look up as Avyanna enters. But she speaks anyway. \"Close the door. This isn't a conversation for hallways.\""
    elif game_state.has_flag("bee_manifested"):
        "Vesper sits alone in the observation deck, star charts pinned to the console with magnetic clips. Bee's residual glow still hums faintly in the overhead wiring — that warm amber pulse that won't quite fade since the manifestation.

Vesper's cleaning Clarity. She pauses when she sees Avyanna, and something in her expression cracks — just a millimeter. \"Sit down. I need to tell you something I haven't told anyone in twelve years.\""
    else:
        "Vesper sits alone in the observation deck, the viewport framing her silhouette against the void. She's cleaning Clarity — slow, methodical movements that suggest ritual more than maintenance.

She doesn't look up as Avyanna enters."
    jump act1_deep_vesper_nav_deck_atmosphere

label act1_deep_vesper_nav_deck_atmosphere:
    "{i}The nav deck smells of gun oil and cold coffee. Star charts cover every flat surface — hand-annotated in Vesper's cramped handwriting, routes plotted in three colors of ink. Red for danger. Blue for safe passage. Black for routes she's lost people on. There are a lot of black lines.

The viewport throws blue-white starlight across the deck. It catches the oil on Vesper's fingers, the dark circles under her eyes, the way her hands move with mechanical precision even when the rest of her is still.{/i}"
    jump act1_deep_vesper_opening

label act1_deep_vesper_opening:
    vesper "The Sovereign Marches. You ever been?"
    jump act1_deep_vesper_opening_response

label act1_deep_vesper_opening_response:
    menu:
        "No. What's it like?":
            jump act1_deep_vesper_marches_description
        "Once. Hard place to forget.":
            jump act1_deep_vesper_marches_shared
        "{i}Shake your head. Wait for her to continue.{/i}":
            jump act1_deep_vesper_marches_silence

label act1_deep_vesper_marches_description:
    vesper "Dust. Ruins. Corporations strip-mining what's left of civilization. Most people don't make it past thirty. I made it out at seventeen."
    jump act1_deep_vesper_marches_context

label act1_deep_vesper_marches_shared:
    vesper "Then you know. The kind of place that teaches you to count bullets before you count friends."
    jump act1_deep_vesper_marches_context

label act1_deep_vesper_marches_silence:
    vesper "{i}She sets down Clarity's barrel assembly with careful precision.{/i}

Good instinct. Don't interrupt someone when they're working up to something."
    jump act1_deep_vesper_marches_context

label act1_deep_vesper_marches_context:
    vesper "Grew up in a salvage crew. My mother died when the refinery collapsed. My father sold my older brother to pay debts. I learned fast — {i}trust no one, carry your own weight, and always know the exits{/i}."
    jump act1_deep_vesper_marches_detail

label act1_deep_vesper_marches_detail:
    vesper "{i}She holds a barrel pin up to the starlight, checking for burrs. Her fingers are steady — the steadiness of someone who trained the tremors out of herself a long time ago.{/i}

I slept in a cargo pod for two years. Ate protein paste and whatever I could steal. Learned to strip a rifle before I learned to read. The Marches don't raise children. They forge tools or they grind bones."
    jump act1_deep_vesper_marches_detail_response

label act1_deep_vesper_marches_detail_response:
    menu:
        "How did you survive?":
            jump act1_deep_vesper_survival_instinct
        "That's no way to grow up.":
            jump act1_deep_vesper_no_childhood
        "{i}Let the silence hold.{/i}":
            jump act1_deep_vesper_silence_holds

label act1_deep_vesper_survival_instinct:
    vesper "I was fast. And mean. And I didn't care about anyone enough to slow down for them. That's the recipe, in the Marches. Empathy is a luxury. Compassion gets you killed."
    jump act1_deep_vesper_rowan_intro

label act1_deep_vesper_no_childhood:
    vesper "{i}She shrugs — one shoulder, economical.{/i}

No. It wasn't. But it was mine. And it made me useful. I'd rather be useful than happy. Happy doesn't stop bullets."
    jump act1_deep_vesper_rowan_intro

label act1_deep_vesper_silence_holds:
    "{i}Vesper glances at you. Something in your silence seems to steady her — the absence of pity, maybe. She sets down the barrel assembly and reaches for the receiver.{/i}"
    jump act1_deep_vesper_rowan_intro

label act1_deep_vesper_rowan_intro:
    vesper "Then I met Rowan Rook. Ex-corporate tactician, burned out and hiding in the wastes. He saw me steal rations from a convoy guard. Could've turned me in. Instead, he trained me."
    jump act1_deep_vesper_rowan_response

label act1_deep_vesper_rowan_response:
    menu:
        "Why would he do that?":
            jump act1_deep_vesper_why_train
        "What did he teach you?":
            jump act1_deep_vesper_what_taught
        "You said 'met.' Past tense.":
            jump act1_deep_vesper_past_tense_catch

label act1_deep_vesper_why_train:
    vesper "He said I reminded him of himself. Someone with potential rotting in a place that kills potential. So he taught me tactics, discipline, how to think instead of just survive."
    jump act1_deep_vesper_rowan_appearance

label act1_deep_vesper_what_taught:
    vesper "Everything. Sightlines. Threat assessment. How to read a battlefield like a book. How to keep people alive when the odds say they should die."
    jump act1_deep_vesper_rowan_appearance

label act1_deep_vesper_past_tense_catch:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Her jaw tightens. She doesn't look at you.{/i}

Yeah. Past tense."
    jump act1_deep_vesper_rowan_appearance

label act1_deep_vesper_rowan_appearance:
    vesper "{i}She sets the receiver down. Picks up a cloth. Wipes oil from her knuckles with slow deliberation.{/i}

He was tall. Taller than anyone in the crew. Had these hands — scarred across every knuckle, but gentle when they needed to be. He'd annotate star charts in green ink because he said black reminded him of corporate memos. Stupid detail to remember. But I remember it every time I pick up a pen."
    jump act1_deep_vesper_rowan_personality

label act1_deep_vesper_rowan_personality:
    vesper "He laughed too loud. Terrible cook — burned everything, even ration paste, which I didn't think was possible. But he could read a room faster than anyone I've met. Knew who was lying, who was scared, who was about to break. That's what made him good. Not the tactics. The {i}seeing{/i}."
    jump act1_deep_vesper_rowan_personality_response

label act1_deep_vesper_rowan_personality_response:
    menu:
        "Sounds like he saw you.":
            jump act1_deep_vesper_rowan_saw_her
        "You learned that from him. The seeing.":
            jump act1_deep_vesper_learned_seeing
        "How long were you together?":
            jump act1_deep_vesper_training_years

label act1_deep_vesper_rowan_saw_her:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Her hands still. For a moment she looks younger — the angles of her face softening into something almost fragile.{/i}

Yeah. He did. First person who ever did. And the last, for a long time."
    jump act1_deep_vesper_training_years

label act1_deep_vesper_learned_seeing:
    vesper "I tried. Don't know if I'm as good at it. He made it look easy — compassion without weakness, empathy without vulnerability. I just fake it and check my sightlines."
    jump act1_deep_vesper_training_years

label act1_deep_vesper_training_years:
    vesper "Three years. Best three years of my life. He turned me into something more than a survivor. He made me a {i}tactician{/i}. Then he got himself killed."
    jump act1_deep_vesper_killed_reaction

label act1_deep_vesper_killed_reaction:
    menu:
        "What happened?":
            jump act1_deep_vesper_what_happened
        "[Empathy DC 14] You blame yourself.":
            $ _sc_result = skill_check("empathy", 14, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_vesper_empathy_success
            else:
                jump act1_deep_vesper_empathy_failure
        "{i}Say nothing. Let her speak.{/i}":
            jump act1_deep_vesper_silence_space

label act1_deep_vesper_empathy_check:
    "[Rolling Empathy check...]"
    jump act1_deep_vesper_empathy_success

label act1_deep_vesper_empathy_success:
    $ game_state.set_flag("vesper_guilt_understood")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    avyanna "You blame yourself. I can see it in how you hold Clarity. Like you're carrying his weight."
    jump act1_deep_vesper_blame_confirmed

label act1_deep_vesper_empathy_failure:
    avyanna "It wasn't your fault. You know that, right?"
    jump act1_deep_vesper_empathy_failure_response

label act1_deep_vesper_empathy_failure_response:
    vesper "{i}She looks at you with something between pity and frustration.{/i}

You don't know enough to say that. But... thanks for trying."
    jump act1_deep_vesper_what_happened

label act1_deep_vesper_silence_space:
    vesper "{i}The silence stretches. When she speaks again, her voice is quieter.{/i}"
    jump act1_deep_vesper_what_happened

label act1_deep_vesper_blame_confirmed:
    vesper "{i}She stops cleaning the rifle. Her hands are very still.{/i}

Yeah. I do."
    jump act1_deep_vesper_blame_story

label act1_deep_vesper_blame_story:
    vesper "We were running extraction on a research facility. Corporate black site, experimental weapons. Rowan planned it — perfect op, clean exits, minimal risk. But I saw a secondary objective. Datacore with intel we could sell."
    jump act1_deep_vesper_blame_story_2

label act1_deep_vesper_blame_story_2:
    vesper "I pushed for it. Said we could handle both. He trusted my judgment. So we split the team."
    jump act1_deep_vesper_the_night_rowan_died

label act1_deep_vesper_the_night_rowan_died:
    vesper "{i}She picks up the cleaning rod. Puts it down. Picks it up again. Her jaw works like she's chewing on glass.{/i}

The facility was called Heron-7. Underground. Three levels. The lights were that corporate white — the kind that makes everything look like a morgue. I can still smell it. Recycled air and floor wax and fear."
    jump act1_deep_vesper_night_detail_2

label act1_deep_vesper_night_detail_2:
    vesper "My team hit the datacore on sublevel two. Clean breach, minimal contacts. I was feeling good about it. Feeling {i}smart{/i}. That's when the alarms went."
    jump act1_deep_vesper_night_detail_3

label act1_deep_vesper_night_detail_3:
    vesper "Not the facility alarms. Those, we'd killed. Corporate rapid-response. Someone on the inside had flagged us. My team got pinned in a server corridor — no cover, no exits, just racks of humming databanks and a kill-funnel doorway."
    jump act1_deep_vesper_night_detail_4

label act1_deep_vesper_night_detail_4:
    if game_state.has_flag("nyx_saw_shard"):
        vesper "{i}Her fingers trace the stock of Clarity. The same motion. Over and over.{/i}

You know that feeling when Nyx touched the shard? That moment where everything just... stops? Where the air goes thick and you know — you {i}know{/i} — something irreversible is happening? That's what it felt like when I heard Rowan's voice on the comm."
    else:
        vesper "{i}Her fingers trace the stock of Clarity. The same motion. Over and over.{/i}

I heard him on the comm. Calm. Always calm. He said, '{i}Vesper, hold position. I'm coming to you.{/i}' And I wanted to scream at him to stay, to not, to run. But I couldn't speak."
    jump act1_deep_vesper_night_detail_5

label act1_deep_vesper_night_detail_5:
    vesper "He came down the service corridor at a dead sprint. Forty meters of open ground with no cover. He was carrying a breaching charge he'd pulled from the primary objective. He blew the wall behind us — made an exit where there wasn't one."
    jump act1_deep_vesper_night_detail_6

label act1_deep_vesper_night_detail_6:
    vesper "Then he turned around and held the doorway."
    jump act1_deep_vesper_night_the_doorway

label act1_deep_vesper_night_the_doorway:
    vesper "{i}Her voice drops. Not to a whisper — to something harder. The voice of someone reciting a report they've memorized against their will.{/i}

He took the first round in the shoulder. Kept firing. Second round — thigh. He dropped to one knee. Kept firing. Third round, center mass. He..."
    jump act1_deep_vesper_night_the_doorway_2

label act1_deep_vesper_night_the_doorway_2:
    vesper "{i}She stops. Her knuckles are white around the cleaning rod. The starlight catches something wet on her cheek but she doesn't acknowledge it.{/i}

He looked back at me. Just once. And he smiled. That stupid, gentle, Rowan smile. Like he was forgiving me for something I hadn't even understood yet."
    jump act1_deep_vesper_night_the_doorway_3

label act1_deep_vesper_night_the_doorway_3:
    vesper "I dragged him through the breach. Half-carried him up two flights while the team covered us. He was trying to talk — giving tactical updates, can you believe that? Bleeding out and still calling positions. '{i}Three contacts, east stairwell. Watch your spacing.{/i}'"
    jump act1_deep_vesper_night_the_shuttle

label act1_deep_vesper_night_the_shuttle:
    vesper "We made the shuttle pad. Forty meters from extraction. He stopped walking. I pulled. He said, '{i}Vesper. It's okay. The math works.{/i}' And I said, '{i}Shut up, the math doesn't work, you're coming with me.{/i}'"
    jump act1_deep_vesper_night_the_shuttle_2

label act1_deep_vesper_night_the_shuttle_2:
    vesper "{i}Her voice breaks. She covers it with a cough, but it's too late. The mask slipped.{/i}

He died on the shuttle pad. Thirty-seven meters from the ramp. I counted later. I counted because that's what he taught me to do. Measure everything. Quantify the loss. As if numbers could make it make sense."
    jump act1_deep_vesper_night_aftermath_response

label act1_deep_vesper_night_aftermath_response:
    menu:
        "{i}Reach across the console. Take her hand.{/i}":
            jump act1_deep_vesper_take_her_hand
        "Thirty-seven meters. You've carried that number a long time.":
            jump act1_deep_vesper_carried_number
        "[Insight DC 16] The math works — he was telling you something.":
            $ _sc_result = skill_check("insight", 16, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_vesper_insight_math_success
            else:
                jump act1_deep_vesper_insight_math_failure
        "{i}Say nothing. Just be here.{/i}":
            jump act1_deep_vesper_just_be_here

label act1_deep_vesper_take_her_hand:
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    "{i}You reach across the star charts — across the black-inked routes and the red warnings and the cold coffee rings — and take her hand. She flinches. Then her fingers close around yours, tight enough to hurt.{/i}"
    jump act1_deep_vesper_split_consequence

label act1_deep_vesper_carried_number:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Twelve years. Thirty-seven meters. I dream about it sometimes. In the dream I'm faster. In the dream those thirty-seven meters don't exist. I step off the shuttle pad and he's right there."
    jump act1_deep_vesper_split_consequence

label act1_deep_vesper_insight_check_math:
    "[Rolling Insight check...]"
    jump act1_deep_vesper_insight_math_success

label act1_deep_vesper_insight_math_success:
    $ game_state.set_flag("vesper_rowan_math_understood")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    avyanna "'The math works.' He wasn't talking about the mission. He was telling you the trade was worth it. His life for the whole team's."
    jump act1_deep_vesper_math_realization

label act1_deep_vesper_insight_math_failure:
    avyanna "What did he mean? The math works?"
    jump act1_deep_vesper_math_she_explains

label act1_deep_vesper_math_she_explains:
    vesper "I don't know. I've turned it over for twelve years. Maybe he meant the mission. Maybe he meant... something else. I'll never know."
    jump act1_deep_vesper_split_consequence

label act1_deep_vesper_math_realization:
    $ game_state.set_flag("vesper_rowan_forgiveness")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She stares at you. Her mouth opens. Closes. Opens again.{/i}

I... I never... {i}Twelve years{/i} and I never read it that way. I thought he was delirious. Running numbers. But you're right. That's exactly what he'd say. One life for six. The math works.

{i}She presses her palm flat against the star charts, steadying herself.{/i}

God. That makes it worse. And better. Both. How is it both?"
    jump act1_deep_vesper_split_consequence

label act1_deep_vesper_just_be_here:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    "{i}You don't speak. You don't move. You let the nav deck hold the weight of her words — the hum of the ship's reactor, the creak of the hull, the distant pulse of stars through the viewport. Vesper's breathing evens out. She nods, once, like you've passed a test she didn't know she was giving.{/i}"
    jump act1_deep_vesper_split_consequence

label act1_deep_vesper_split_consequence:
    vesper "Security was heavier than intel suggested. My team got pinned. Rowan came back for us. Took three rounds holding the doorway so we could extract. Died before we made the shuttle."
    jump act1_deep_vesper_aftermath_response

label act1_deep_vesper_what_happened:
    vesper "Corporate black site extraction. I pushed for a secondary objective — datacore with valuable intel. Rowan trusted me. We split the team. Security was heavier than we thought."
    jump act1_deep_vesper_what_happened_2

label act1_deep_vesper_what_happened_2:
    vesper "My squad got pinned. He came back for us. Held the doorway while we extracted. Three rounds center mass. Dead before we reached the shuttle."
    jump act1_deep_vesper_aftermath_response

label act1_deep_vesper_aftermath_response:
    menu:
        "He made his choice. He chose to save you.":
            jump act1_deep_vesper_choice_argument
        "You carry that every day. I see it.":
            jump act1_deep_vesper_carry_weight
        "The intel — was it worth it?":
            jump act1_deep_vesper_intel_question
        "You were young. Learning. He knew that.":
            jump act1_deep_vesper_young_excuse

label act1_deep_vesper_choice_argument:
    vesper "He made his choice because I made {i}mine{/i}. Bad tactical assessment. Greed. Overconfidence. I killed him as sure as if I pulled the trigger."
    jump act1_deep_vesper_guilt_deepens

label act1_deep_vesper_carry_weight:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Every. Single. Day. Every tactical decision I make, I ask — {i}would this get someone killed?{/i} Every person I train, I ask — {i}am I giving them the skills to survive, or just more ways to die?{/i}"
    jump act1_deep_vesper_weight_acknowledged

label act1_deep_vesper_intel_question:
    vesper "{i}Her eyes go cold.{/i}

No. It was corrupted data. Worthless. I traded the best man I ever knew for {i}nothing{/i}."
    jump act1_deep_vesper_worthless_trade

label act1_deep_vesper_young_excuse:
    vesper "I was twenty. Old enough to know better. He trained me {i}specifically{/i} to know better. And I ignored everything he taught me."
    jump act1_deep_vesper_guilt_deepens

label act1_deep_vesper_guilt_deepens:
    vesper "I took over after he died. Led the crew. Made myself into what he was — tactician, planner, the one who keeps everyone alive. Because I {i}owe{/i} him that."
    jump act1_deep_vesper_after_rowan_died

label act1_deep_vesper_after_rowan_died:
    vesper "{i}She stands, walks to the viewport. The starlight turns her profile into something carved — all angles and tension. She presses her forehead against the glass.{/i}

The first three months, I didn't sleep. Not couldn't — {i}didn't{/i}. I'd sit at the nav console and chart routes until my eyes bled. Literally. Burst blood vessel. Elia had to sedate me."
    jump act1_deep_vesper_coping_mechanisms

label act1_deep_vesper_coping_mechanisms:
    vesper "I started drinking star charts. That's what Jalen calls it — when you memorize routes until they replace your dreams. Every corridor, every jump point, every exit strategy. If I couldn't sleep without seeing Heron-7, I'd fill my head with something else. Burn the nightmares out with data."
    jump act1_deep_vesper_coping_mechanisms_2

label act1_deep_vesper_coping_mechanisms_2:
    vesper "I stopped eating unless someone put food in front of me. Stopped talking unless it was operational. The crew thought I was being professional. I was being {i}dead{/i}. Walking dead. Going through the motions of a person while something inside me rotted."
    jump act1_deep_vesper_coping_response

label act1_deep_vesper_coping_response:
    menu:
        "What brought you back?":
            jump act1_deep_vesper_what_brought_back
        "[Empathy DC 12] You're still doing it. Right now.":
            $ _sc_result = skill_check("empathy", 12, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_vesper_still_doing_it_success
            else:
                jump act1_deep_vesper_still_doing_it_failure
        "But you survived.":
            jump act1_deep_vesper_survived_response

label act1_deep_vesper_what_brought_back:
    vesper "A kid. Station raid, six months after Heron-7. Civilian caught in the crossfire — couldn't have been more than twelve. I pulled her out. She looked up at me and said, '{i}Are you the one who keeps people alive?{/i}'

{i}She laughs, but it's thin.{/i}

I said yes. And I meant it. So I had to start being alive myself, to keep that promise."
    jump act1_deep_vesper_debt_response

label act1_deep_vesper_empathy_check_2:
    "[Rolling Empathy check...]"
    jump act1_deep_vesper_still_doing_it_success

label act1_deep_vesper_still_doing_it_success:
    $ game_state.set_flag("vesper_coping_seen")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    avyanna "You're still doing it. The star charts, the obsessive planning, the coffee instead of sleep. You never stopped coping. You just got better at hiding it."
    jump act1_deep_vesper_still_doing_it_response

label act1_deep_vesper_still_doing_it_failure:
    avyanna "At least you found a way through it."
    jump act1_deep_vesper_survived_response

label act1_deep_vesper_still_doing_it_response:
    vesper "{i}She turns from the viewport. In the starlight, her expression is stripped bare — no wit, no armor, no angles. Just a woman who's been running from a shuttle pad for twelve years.{/i}

Yeah. I am. And I don't know how to stop. Because stopping means feeling it. All of it. Every meter of those thirty-seven."
    jump act1_deep_vesper_debt_response

label act1_deep_vesper_survived_response:
    vesper "Survived. That's one word for it. Rowan would've called it something sharper. '{i}Existing isn't living, Vesper. Surviving isn't enough.{/i}' He said that to me once. Didn't understand it then. Starting to now."
    jump act1_deep_vesper_debt_response

label act1_deep_vesper_weight_acknowledged:
    vesper "That's why I'm meticulous. Why I triple-check exit vectors. Why I won't let anyone take unnecessary risks. Because I've seen what happens when you get {i}sloppy{/i}."
    jump act1_deep_vesper_methodology_choice

label act1_deep_vesper_worthless_trade:
    vesper "So yeah. I remember. Every time I plan an op, every time I calculate risk, every time I save someone's life — I remember the one life I {i}couldn't{/i} save."
    jump act1_deep_vesper_cant_save_response

label act1_deep_vesper_debt_response:
    menu:
        "You honor him by keeping others alive.":
            jump act1_deep_vesper_honor_path
        "You're punishing yourself. He wouldn't want that.":
            jump act1_deep_vesper_punishment_path
        "How many have you saved since then?":
            jump act1_deep_vesper_saved_count

label act1_deep_vesper_methodology_choice:
    menu:
        "That's not sloppy. That's {i}care{/i}.":
            jump act1_deep_vesper_care_recognition
        "But you can't control everything.":
            jump act1_deep_vesper_control_limits
        "Is that sustainable? Long-term?":
            jump act1_deep_vesper_sustainable_question

label act1_deep_vesper_cant_save_response:
    menu:
        "You've saved others since. That counts.":
            jump act1_deep_vesper_others_count
        "Like you've saved me. More than once.":
            jump act1_deep_vesper_saved_avyanna
        "One death doesn't erase a lifetime of good calls.":
            jump act1_deep_vesper_balance_argument

label act1_deep_vesper_honor_path:
    vesper "Maybe. Or maybe I'm just too stubborn to let anyone else die on my watch. Either way, it keeps people breathing."
    jump act1_deep_vesper_philosophy_accepted

label act1_deep_vesper_punishment_path:
    vesper "Maybe I am. But if punishing myself means twelve years of zero preventable casualties, I'll take that trade."
    jump act1_deep_vesper_philosophy_accepted

label act1_deep_vesper_saved_count:
    $ game_state.set_flag("vesper_shared_count")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}She's quiet for a long moment.{/i}

Forty-three. Forty-three people who should be dead, but aren't. Because I learned from my mistakes."
    jump act1_deep_vesper_count_reflection

label act1_deep_vesper_care_recognition:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Something shifts in her expression. Not quite vulnerability, but close.{/i}

Yeah. I guess it is."
    jump act1_deep_vesper_avyanna_echoes

label act1_deep_vesper_control_limits:
    vesper "No. I can't. But I can control {i}my{/i} decisions. My planning. My execution. That's enough."
    jump act1_deep_vesper_acceptance_path

label act1_deep_vesper_sustainable_question:
    vesper "Probably not. But I'll burn out before I let someone die because I didn't check the angles."
    jump act1_deep_vesper_burnout_response

label act1_deep_vesper_others_count:
    vesper "Forty-three, last count. Forty-three people breathing because I learned. But that doesn't balance the scale."
    jump act1_deep_vesper_scale_argument

label act1_deep_vesper_saved_avyanna:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}Her eyes meet yours. Something unguarded in them.{/i}

Yeah. Like I saved you. And I'd do it again. Every time."
    jump act1_deep_vesper_avyanna_echoes

label act1_deep_vesper_balance_argument:
    vesper "Tell that to Rowan. Oh wait — you can't. Because I got him killed."
    jump act1_deep_vesper_harsh_reality

label act1_deep_vesper_philosophy_accepted:
    vesper "Rowan used to say, '{i}Every plan is a promise you make to the people counting on you.{/i}' I keep my promises now."
    jump act1_deep_vesper_promise_response

label act1_deep_vesper_count_reflection:
    menu:
        "That's extraordinary.":
            jump act1_deep_vesper_extraordinary_response
        "But you still count the one you lost.":
            jump act1_deep_vesper_still_counting
        "He'd be proud of that.":
            jump act1_deep_vesper_proud_statement

label act1_deep_vesper_avyanna_echoes:
    vesper "{i}She sits back down. Picks up Clarity's barrel, then sets it down again — the first time you've seen her abandon the ritual mid-motion.{/i}

Can I tell you something that scares me?"
    jump act1_deep_vesper_avyanna_echoes_response

label act1_deep_vesper_avyanna_echoes_response:
    menu:
        "Of course.":
            jump act1_deep_vesper_vesper_fear_avyanna
        "I didn't think anything scared you.":
            jump act1_deep_vesper_vesper_fear_deflection
        "{i}Nod.{/i}":
            jump act1_deep_vesper_vesper_fear_avyanna

label act1_deep_vesper_vesper_fear_deflection:
    vesper "{i}A ghost of a smile.{/i}

Plenty of things scare me. I just shoot at most of them. This one I can't."
    jump act1_deep_vesper_vesper_fear_avyanna

label act1_deep_vesper_vesper_fear_avyanna:
    vesper "You remind me of him. Not in the obvious ways — you don't look like him, don't talk like him, don't move like him. But there's this... {i}thing{/i} you do. This hope. Like the universe is broken and you know it's broken and you're going to fix it anyway."
    jump act1_deep_vesper_vesper_fear_avyanna_2

label act1_deep_vesper_vesper_fear_avyanna_2:
    vesper "Rowan had that. That stubborn, impossible belief that people were worth saving. That the next mission would be the one that mattered. That you could be good in a galaxy that rewards cruelty."
    jump act1_deep_vesper_vesper_fear_avyanna_3

label act1_deep_vesper_vesper_fear_avyanna_3:
    if game_state.has_flag("bee_manifested"):
        vesper "{i}She looks up at the amber glow still pulsing in the wiring. Bee's residual warmth.{/i}

And I'm terrified. Because last time I followed someone with that kind of hope, I got them killed. And now here you are, with your impossible missions and your pet ghost-light and your absolute refusal to leave anyone behind. And I'm following you anyway. Because I can't help it. Because that hope is {i}contagious{/i} and I hate it and I need it."
    else:
        vesper "And I'm terrified. Because last time I followed someone with that kind of hope, I got them killed. And now here you are, pulling us into impossible missions, refusing to leave anyone behind. And I'm {i}following{/i} you. Again. Because that hope is contagious and I hate it and I need it and I don't know which feeling is stronger."
    jump act1_deep_vesper_vesper_fear_response

label act1_deep_vesper_vesper_fear_response:
    menu:
        "I'm not Rowan. And this isn't Heron-7.":
            jump act1_deep_vesper_not_rowan
        "Then help me be smarter than he was. Keep me honest.":
            jump act1_deep_vesper_keep_me_honest
        "[Insight DC 14] You're not afraid of losing me. You're afraid of caring again.":
            $ _sc_result = skill_check("insight", 14, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_deep_vesper_insight_caring_success
            else:
                jump act1_deep_vesper_insight_caring_failure
        "{i}Let her words sit. Don't rush to fix them.{/i}":
            jump act1_deep_vesper_let_it_sit

label act1_deep_vesper_not_rowan:
    vesper "I know. That's what makes it worse. Because if you were him, I'd know the pattern. I'd know the risks. You're something new. And I don't have a playbook for new."
    jump act1_deep_vesper_vulnerability_moment

label act1_deep_vesper_keep_me_honest:
    $ game_state.set_flag("vesper_tactical_bond")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She looks at you sharply — then something in her face unknots.{/i}

You mean that. You actually mean that. Rowan never asked for that. He just trusted his own judgment. You're asking me to check yours."
    jump act1_deep_vesper_vulnerability_moment

label act1_deep_vesper_insight_check_caring:
    "[Rolling Insight check...]"
    jump act1_deep_vesper_insight_caring_success

label act1_deep_vesper_insight_caring_success:
    $ game_state.set_flag("vesper_fear_named")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    avyanna "You're not afraid of losing me. You're afraid of what it means that you care. Because caring is what killed Rowan — not the bullets, not the bad intel. The fact that he cared enough to come back for you."
    jump act1_deep_vesper_fear_named_response

label act1_deep_vesper_insight_caring_failure:
    avyanna "You don't have to be afraid. Not with me."
    jump act1_deep_vesper_vulnerability_moment

label act1_deep_vesper_fear_named_response:
    vesper "{i}She makes a sound — half laugh, half something broken. She covers her mouth with her hand. When she lowers it, her eyes are bright and raw.{/i}

Damn you. Damn you for seeing that. I spent twelve years building walls and you just — {i}she gestures vaguely{/i} — walked through them like they weren't there."
    jump act1_deep_vesper_vulnerability_moment

label act1_deep_vesper_let_it_sit:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    "{i}The nav deck is quiet. The reactor hums. Stars turn slowly past the viewport. Vesper's breathing is ragged, and you let it be ragged. You don't fill the silence. You don't fix it. You witness it.

After a long moment, she exhales — long and shuddering — and nods.{/i}"
    jump act1_deep_vesper_vulnerability_moment

label act1_deep_vesper_vulnerability_moment:
    vesper "{i}She puts Clarity down. Not carefully — she just sets it aside, like it doesn't matter. Like the ritual can wait. She presses both palms flat on the star charts and leans forward, head bowed, breathing slowly.

When she looks up, the mask is gone. No wit. No edge. No angles. Just Vesper — tired, scared, stubbornly alive.{/i}"
    jump act1_deep_vesper_vulnerability_words

label act1_deep_vesper_vulnerability_words:
    vesper "I don't know how to do this. The... trusting. The hoping. I know how to plan ops and check sightlines and keep people alive through sheer force of paranoia. But this — {i}she gestures between you{/i} — this terrifies me more than any firefight."
    jump act1_deep_vesper_vulnerability_words_2

label act1_deep_vesper_vulnerability_words_2:
    vesper "Because firefights have rules. Exit strategies. Contingencies. People? People die in ways you can't plan for. They die thirty-seven meters from the shuttle. They die smiling. They die and you have to keep going because forty-three other people need you to keep going."
    jump act1_deep_vesper_vulnerability_choice

label act1_deep_vesper_vulnerability_choice:
    menu:
        "Then don't do it alone. That's not a weakness — it's a tactic.":
            jump act1_deep_vesper_tactic_reframe
        "I'm scared too. Every day. But I'd rather be scared with you watching my back.":
            jump act1_deep_vesper_scared_together
        "{i}Move to stand beside her at the viewport.{/i}":
            jump act1_deep_vesper_stand_beside
        "What would Rowan tell you right now?":
            jump act1_deep_vesper_rowan_ghost_advice

label act1_deep_vesper_tactic_reframe:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She laughs — a real laugh, startled out of her.{/i}

A tactic. Trust as a force multiplier. God, you even speak my language. Rowan would've liked you. He would've liked you a lot."
    jump act1_deep_vesper_emotional_resolution

label act1_deep_vesper_scared_together:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}Her throat works. She looks at you, and for a moment the twelve years between Heron-7 and now collapse into nothing.{/i}

Yeah. Yeah, okay. Scared together. That's... I can work with that. That's a plan I understand."
    jump act1_deep_vesper_emotional_resolution

label act1_deep_vesper_stand_beside:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    "{i}You move around the console and stand beside her at the viewport. Not touching. Just close enough that she can feel you there — a presence, a proof that the universe isn't entirely composed of empty shuttle pads and corrupted data.

The stars wheel past. Cold and distant and beautiful in the way that only things that don't care about you can be beautiful.

Vesper's shoulder touches yours. She doesn't pull away.{/i}"
    jump act1_deep_vesper_emotional_resolution

label act1_deep_vesper_rowan_ghost_advice:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She's quiet for so long you think she won't answer. Then:{/i}

He'd say, '{i}Stop using my death as an excuse to stop living.{/i}' He'd say it gently, because he was gentle. And then he'd say something about star charts and sunrises and how the void is just the space between lights.

{i}She wipes her eyes with the heel of her hand, efficient, like clearing a scope.{/i}

God, I miss him. I miss him every day. But I'm starting to think... maybe missing someone doesn't have to mean drowning in them."
    jump act1_deep_vesper_emotional_resolution

label act1_deep_vesper_emotional_resolution:
    vesper "Thanks. For listening. For... understanding. Most people don't ask. They just see the rifle and assume I'm fine."
    jump act1_deep_vesper_gratitude_response

label act1_deep_vesper_acceptance_path:
    vesper "That's all any of us can do. Control what we can. Make the best calls possible. Keep moving forward."
    jump act1_deep_vesper_forward_together

label act1_deep_vesper_burnout_response:
    menu:
        "Let me help carry that weight.":
            jump act1_deep_vesper_share_burden
        "You don't have to do this alone.":
            jump act1_deep_vesper_not_alone
        "That's not a plan. That's slow suicide.":
            jump act1_deep_vesper_harsh_truth

label act1_deep_vesper_scale_argument:
    menu:
        "Maybe it's not about balance. Maybe it's about growth.":
            jump act1_deep_vesper_growth_perspective
        "Forty-three lives. That's not nothing.":
            jump act1_deep_vesper_not_nothing
        "What would Rowan say?":
            jump act1_deep_vesper_rowan_wisdom

label act1_deep_vesper_harsh_reality:
    vesper "{i}The bitterness in her voice is sharp enough to cut.{/i}

Sorry. That was... I'm not good at this. Talking. Feelings. I usually just shoot things."
    jump act1_deep_vesper_deflection_response

label act1_deep_vesper_promise_response:
    menu:
        "And you've kept them. Forty-three times over.":
            jump act1_deep_vesper_promises_kept
        "He sounds like he was remarkable.":
            jump act1_deep_vesper_rowan_remarkable
        "That's a good philosophy.":
            jump act1_deep_vesper_good_philosophy

label act1_deep_vesper_extraordinary_response:
    vesper "It's necessary. This life — freelance ops, corporate raids, void stations falling apart — people die {i}easy{/i}. Keeping them alive is the hard part."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_still_counting:
    vesper "Always. He's the reason I count at all. The reminder that {i}one mistake{/i} is all it takes."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_proud_statement:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Her throat works. She looks away.{/i}

Maybe. I hope so. That's why I do it."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_gratitude_response:
    menu:
        "You're not just fine. You're human.":
            jump act1_deep_vesper_human_recognition
        "Anytime you need to talk, I'm here.":
            jump act1_deep_vesper_standing_offer
        "{i}Rest a hand on her shoulder.{/i}":
            jump act1_deep_vesper_physical_comfort

label act1_deep_vesper_forward_together:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Yeah. Together. That's... that's new for me. But good."
    jump act1_deep_vesper_closing_professional

label act1_deep_vesper_share_burden:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She looks at you for a long moment. Something shifts in her eyes.{/i}

Yeah. Okay. I'd like that."
    jump act1_deep_vesper_emotional_resolution

label act1_deep_vesper_not_alone:
    vesper "I know. You've proven that. More than once. I just... it's hard to trust that. After Rowan."
    jump act1_deep_vesper_trust_acknowledged

label act1_deep_vesper_harsh_truth:
    vesper "{i}She laughs — short, bitter.{/i}

Yeah. You're not wrong. But at least it's a suicide that saves people."
    jump act1_deep_vesper_deflection_response

label act1_deep_vesper_growth_perspective:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Growth. Huh. Never thought of it that way. Just thought of it as... penance."
    jump act1_deep_vesper_penance_to_growth

label act1_deep_vesper_not_nothing:
    vesper "No. It's not. But some days it feels like I'm running up a debt I'll never clear."
    jump act1_deep_vesper_debt_endless

label act1_deep_vesper_rowan_wisdom:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She's quiet. When she speaks, her voice is soft.{/i}

He'd say, '{i}Stop counting corpses and start counting sunrises.{/i}' He was better at hope than I am."
    jump act1_deep_vesper_rowan_wisdom_reflection

label act1_deep_vesper_deflection_response:
    menu:
        "You're doing fine. This takes courage.":
            jump act1_deep_vesper_courage_recognized
        "I'm glad you're talking to me.":
            jump act1_deep_vesper_glad_talking
        "Shooting things is easier. I get it.":
            jump act1_deep_vesper_shared_understanding

label act1_deep_vesper_promises_kept:
    $ game_state.set_flag("vesper_shared_rowan")
    vesper "Yeah. I have. And I'll keep keeping them. For him. For everyone."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_rowan_remarkable:
    vesper "He was. Best tactician I ever knew. Better person. The kind who believed people were worth saving, even when they proved him wrong."
    jump act1_deep_vesper_rowan_remarkable_detail

label act1_deep_vesper_rowan_remarkable_detail:
    vesper "He kept a journal. Wrote in it every night. I found it after — couldn't read it for three years. When I finally did, the last entry was about me. About how proud he was. How I was going to be better than him.

{i}She touches the breast pocket of her jacket. There's something flat and rectangular inside it.{/i}

I carry it. Every op. Every mission. Stupid, right? Sentimental. He'd have called it a tactical liability — extra weight, emotional compromise. But I carry it."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_good_philosophy:
    vesper "It kept me alive this long. Kept others alive too. That's enough."
    jump act1_deep_vesper_closing_professional

label act1_deep_vesper_closing_moment:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "{i}She reassembles Clarity with practiced efficiency. The conversation is over, but something has shifted. She's lighter, somehow.{/i}

Thanks. For listening. For not telling me it wasn't my fault. For just... being here."
    jump act1_deep_vesper_closing_vesper_thanks

label act1_deep_vesper_closing_vesper_thanks:
    if game_state.has_flag("vesper_rowan_forgiveness"):
        vesper "{i}She touches the journal in her pocket.{/i}

You said the math works. That he was choosing, not just dying. I'm going to sit with that for a while. Might change some things. Might change a lot of things.

{i}She almost smiles — a real one, fragile as spun glass.{/i}

Don't tell anyone I cried. I have a reputation."
    elif game_state.has_flag("vesper_fear_named"):
        vesper "You named the thing I couldn't name. The fear. Twelve years of carrying it around like shrapnel and you just — pulled it out. Still hurts. But cleaner now.

{i}She picks up Clarity again. This time the ritual feels different — less compulsion, more care.{/i}

Don't expect me to be nice about it. That's not who I am. But I'll be honest. That's more than most people get."
    else:
        vesper "I don't do this. Talk. Share. Whatever this is. But you made it... easier. Somehow.

{i}She slings Clarity across her back.{/i}

We speak of this to no one. Especially Jalen. He'll write a song about it and I'll have to shoot him."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_human_recognition:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}She almost smiles.{/i}

Human. Yeah. I forget that sometimes. Good to be reminded."
    jump act1_deep_vesper_final_words_warm

label act1_deep_vesper_standing_offer:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "I'll remember that. Not sure how often I'll take you up on it, but... I'll remember."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_physical_comfort:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She stiffens for a moment, then relaxes. Her hand comes up to briefly rest on yours.{/i}

Thanks. I needed this."
    jump act1_deep_vesper_final_words_warm

label act1_deep_vesper_closing_professional:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "{i}She stands, slinging Clarity across her back. The moment of vulnerability has passed, but not forgotten.{/i}

Good talk. We should do this again. Maybe without the emotional bloodletting."
    return

label act1_deep_vesper_trust_acknowledged:
    vesper "But I'm trying. That's something, right?"
    jump act1_deep_vesper_trying_response

label act1_deep_vesper_penance_to_growth:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Maybe it can be both. Penance that grows into something better. Something Rowan would recognize."
    jump act1_deep_vesper_closing_moment

label act1_deep_vesper_debt_endless:
    vesper "But that's my problem. Not yours. You've listened. That's more than most people do."
    jump act1_deep_vesper_closing_professional

label act1_deep_vesper_rowan_wisdom_reflection:
    menu:
        "Then let's try counting sunrises together.":
            jump act1_deep_vesper_sunrise_together
        "Maybe you can learn that from him too.":
            jump act1_deep_vesper_learn_hope
        "He sounds wise. You honor him by remembering.":
            jump act1_deep_vesper_honor_memory

label act1_deep_vesper_courage_recognized:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "Courage. Huh. Usually that involves getting shot at. But yeah. Thanks."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_glad_talking:
    $ game_state.set_flag("deep_vesper_complete")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Me too. More than I expected. You're... you're good at this. Listening. Understanding. Keep that."
    jump act1_deep_vesper_final_words_warm

label act1_deep_vesper_shared_understanding:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "{i}She actually smiles — small, but genuine.{/i}

Yeah. Clear objectives. Measurable outcomes. No emotions to navigate. But this... this was good too."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_trying_response:
    menu:
        "It's everything.":
            jump act1_deep_vesper_everything_affirm
        "It's a start. That's all we need.":
            jump act1_deep_vesper_start_affirm

label act1_deep_vesper_sunrise_together:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}Her expression softens. Something like hope flickers there.{/i}

Yeah. I'd like that. Together."
    jump act1_deep_vesper_final_words_warm

label act1_deep_vesper_learn_hope:
    $ game_state.set_flag("vesper_shared_rowan")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Maybe. It's harder than tactics. But... I'm willing to try."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_honor_memory:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "I try. Every day. Every decision. Every life I save. He's there."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_everything_affirm:
    $ game_state.set_flag("vesper_combat_synergy")
    $ relationship_manager.process_reputation_affinity("vesper", 2)
    vesper "{i}She nods slowly.{/i}

Okay. Then I'll keep trying. With you."
    jump act1_deep_vesper_final_words_warm

label act1_deep_vesper_start_affirm:
    $ game_state.set_flag("deep_vesper_complete")
    vesper "A start. Yeah. I can work with that."
    jump act1_deep_vesper_final_words

label act1_deep_vesper_final_words:
    vesper "Next time we're in the field, watch my six. I'll watch yours. That's what Rowan would do. What he {i}did{/i} do. We honor him by staying alive."
    jump act1_deep_vesper_final_scene

label act1_deep_vesper_final_words_warm:
    vesper "{i}She picks up Clarity, but this time there's warmth in her eyes.{/i}

Next time we're in the field, we keep each other alive. That's the promise. That's how we honor everyone we've lost. By making sure we don't lose anyone else."
    jump act1_deep_vesper_final_scene_warm

label act1_deep_vesper_final_scene:
    $ game_state.set_flag("deep_vesper_complete")
    "{i}Vesper turns back to the nav console. She picks up a pen — green ink, you notice — and begins annotating a route. Her handwriting is small, precise, certain.

The viewport fills with stars. Somewhere in the ship, the reactor hums its endless lullaby. The star charts flutter in the ventilation draft, black lines and red warnings and blue safe-passages rustling like paper wings.

She doesn't look up as you leave. But just before the door closes, you hear her voice — quiet, stripped of wit, stripped of armor:

\"Avyanna. Thanks.\"

The door seals. The corridor is silent. But something has changed — a weight redistributed, a burden shared, a promise made in starlight and gun oil and the space between two people who've learned that trust is the most dangerous weapon of all.{/i}"
    return

label act1_deep_vesper_final_scene_warm:
    $ game_state.set_flag("deep_vesper_complete")
    if game_state.has_flag("vesper_rowan_math_understood"):
        "{i}Vesper walks to the nav console and picks up a pen. Green ink. She stares at it for a moment, then uncaps it and begins to write — not route annotations, but something else. Something personal. The journal's breast-pocket silhouette is visible through her jacket.

She's writing to Rowan. You know it without asking.

You leave quietly. The door seals behind you, and the corridor is warm with reactor heat and Bee's residual amber glow. Somewhere behind that door, a woman is learning that the math was never about subtraction. It was about what you carry forward.

Thirty-seven meters. Forty-three lives. And one more person who finally, finally, doesn't have to count alone.{/i}"
    else:
        "{i}Vesper slings Clarity across her back and walks with you to the door. She pauses at the threshold — one hand on the frame, starlight catching the oil on her knuckles.

For a moment she looks like she might say something else. Something bigger. Instead, she reaches out and adjusts the collar of your jacket — a small, precise gesture, the kind of care she usually reserves for rifle maintenance.

\"Stay alive out there. That's an order.\"

The door closes. The corridor stretches ahead, quiet and warm with reactor heat. Behind you, through the bulkhead, you can hear Vesper humming — low and tuneless and unmistakably human.

She hasn't hummed in twelve years.{/i}"
    return
