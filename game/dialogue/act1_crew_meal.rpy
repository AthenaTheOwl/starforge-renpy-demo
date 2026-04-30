## act1_crew_meal.rpy — Auto-generated from act1_crew_meal.json
## 149 dialogue nodes

label act1_crew_meal:
    $ game_state.mark_dialogue_played("act1_crew_meal")
    jump act1_crew_meal_start

label act1_crew_meal_start:
    "{i}Dinner on the Lumen Thief. The galley smells like something Rho is calling 'stew' that probably started life as three different meals. It's not beautiful. But it's hot and it's food and no one has to eat alone.{/i}"
    jump act1_crew_meal_setting_detail

label act1_crew_meal_setting_detail:
    "{i}The galley is small — built for function, not ambiance. A battered metal table dominates the center, bolted to the deck. Mismatched chairs and a crate someone welded armrests onto. Overhead lights flicker at a frequency that's almost warm. Condensation beads on the porthole. Outside, the drift of stars is so slow it looks like stillness.{/i}"
    jump act1_crew_meal_seating_arrangement

label act1_crew_meal_seating_arrangement:
    "{i}Vesper sits at the head — not by demand, just gravity. Elia is to their left, back to the wall, sightlines on both doors. Elisira sits beside Elia, close enough their elbows brush. Jalen has claimed the far corner, datapad propped against a condiment jar. Rho is still at the stove, conducting. Nyx sits nearest the corridor, as though keeping one foot in an exit. The only open chair is between Rho's empty seat and Nyx.{/i}"
    jump act1_crew_meal_rho_serves

label act1_crew_meal_rho_serves:
    rho "Fair warning: I added spice. Jalen said the last batch was bland."
    jump act1_crew_meal_jalen_bland

label act1_crew_meal_jalen_bland:
    jalen "{i}Not looking up from his datapad.{/i} I said it tasted like warm disappointment."
    jump act1_crew_meal_rho_same

label act1_crew_meal_rho_same:
    rho "Same thing."
    jump act1_crew_meal_rho_menu_detail

label act1_crew_meal_rho_menu_detail:
    "{i}Rho ladles stew into dented bowls — something thick and brick-red with chunks of reconstituted protein and tubers that might once have been potatoes. A basket of flatbread, dense and dark, gets dropped in the center. A jar of pickled something no one can identify. And coffee. Always coffee — the one luxury this crew treats as non-negotiable.{/i}"
    jump act1_crew_meal_vesper_death

label act1_crew_meal_vesper_death:
    vesper "{i}Accepting a bowl.{/i} If this kills me, promote Elia to engineer."
    jump act1_crew_meal_elia_decline

label act1_crew_meal_elia_decline:
    elia "I don't want the job."
    jump act1_crew_meal_elisira_taste

label act1_crew_meal_elisira_taste:
    elisira "{i}Dipping flatbread into the stew, deliberate.{/i} It's better than last time. You let it simmer longer."
    jump act1_crew_meal_rho_noticed

label act1_crew_meal_rho_noticed:
    rho "{i}Pleased someone noticed.{/i} Two extra hours. Secret's patience."
    jump act1_crew_meal_jalen_patience_quip

label act1_crew_meal_jalen_patience_quip:
    jalen "The secret to your cooking is not cooking it. Noted."
    jump act1_crew_meal_nyx_taste

label act1_crew_meal_nyx_taste:
    nyx "{i}Tasting the stew.{/i} It's... functional."
    jump act1_crew_meal_rho_victory

label act1_crew_meal_rho_victory:
    rho "{i}Grinning.{/i} I'll take it."
    jump act1_crew_meal_avyanna_taste

label act1_crew_meal_avyanna_taste:
    "{i}You take a cautious bite. It's good. Better than good. Better than anything you ate in the mine, where food was fuel and nothing else.{/i}"
    jump act1_crew_meal_dinner_observation

label act1_crew_meal_dinner_observation:
    "{i}As the crew settles into their meal, you have a moment to observe. Who do you watch?{/i}"
    menu:
        "Watch Vesper — the way they hold command without demanding it":
            $ game_state.set_flag("dinner_watched_vesper")
            $ relationship_manager.process_reputation_affinity("vesper", 1)
            jump act1_crew_meal_watch_vesper
        "Watch Nyx — the quiet way she tracks everyone's comfort":
            $ game_state.set_flag("dinner_watched_nyx")
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_crew_meal_watch_nyx
        "Watch Rho — the practiced grin and careful hands":
            $ game_state.set_flag("dinner_watched_rho")
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_crew_meal_watch_rho
        "Watch Jalen — how he tracks everything while pretending not to care":
            $ game_state.set_flag("dinner_watched_jalen")
            $ relationship_manager.process_reputation_affinity("jalen", 1)
            jump act1_crew_meal_watch_jalen
        "Watch Elia — sharp eyes that miss nothing":
            $ game_state.set_flag("dinner_watched_elia")
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_crew_meal_watch_elia

label act1_crew_meal_watch_vesper:
    "{i}Vesper doesn't command. They curate. Every question deliberate. Every silence intentional. This is someone who leads by making space for others to be competent.{/i}"
    jump act1_crew_meal_rho_asks

label act1_crew_meal_watch_nyx:
    "{i}Nyx watches the room like she's solving an equation. Not cold — attentive. She notices when Jalen's coffee runs low, when Rho's smile gets tight. Care disguised as observation.{/i}"
    jump act1_crew_meal_rho_asks

label act1_crew_meal_watch_rho:
    "{i}Rho moves with the ease of someone who's practiced being comfortable. But you see the way he tracks the exits. The way his hands stay ready. A demolitions expert who knows exactly how fragile everything is.{/i}"
    jump act1_crew_meal_rho_asks

label act1_crew_meal_watch_jalen:
    "{i}Jalen's datapad is a shield. But his eyes move — tracking trajectories, probabilities, crew morale. He cares more than he wants anyone to know. Especially himself.{/i}"
    jump act1_crew_meal_rho_asks

label act1_crew_meal_watch_elia:
    "{i}Elia reads the room in threat vectors and weak points. Not paranoid — professional. They're the blade that keeps everyone safe. And they carry that weight like it's lighter than it is.{/i}"
    jump act1_crew_meal_rho_asks

label act1_crew_meal_rho_asks:
    rho "You like it?"
    jump act1_crew_meal_avyanna_likes

label act1_crew_meal_avyanna_likes:
    avyanna "Yes. It's... it's really good."
    jump act1_crew_meal_jalen_standards

label act1_crew_meal_jalen_standards:
    jalen "{i}Finally looking up.{/i} Some people have low standards."
    jump act1_crew_meal_rho_bread

label act1_crew_meal_rho_bread:
    rho "{i}Throwing a piece of bread at them.{/i} Heretic."
    jump act1_crew_meal_table_hub

label act1_crew_meal_table_hub:
    "{i}The table splits into overlapping conversations — voices layering over one another the way they do when people are comfortable. You could lean into any of them.{/i}"
    menu:
        "Listen to Vesper — they seem about to tell a story":
            jump act1_crew_meal_vesper_story_setup
        "Tune into Rho and Jalen — they're arguing about something":
            jump act1_crew_meal_rho_jalen_argument
        "Turn to Nyx — she's being quieter than usual":
            jump act1_crew_meal_nyx_drawing_out
        "Watch Elisira and Elia — something unspoken passes between them":
            jump act1_crew_meal_elisira_elia_exchange

label act1_crew_meal_vesper_story_setup:
    rho "Vesper. Tell the one about Calyx Station."
    jump act1_crew_meal_vesper_story_protest

label act1_crew_meal_vesper_story_protest:
    vesper "{i}Leaning back, cradling their coffee.{/i} That story gets worse every time I tell it."
    jump act1_crew_meal_rho_story_insist

label act1_crew_meal_rho_story_insist:
    rho "That's because you keep adding details. Tell the real version. For the new crew member."
    jump act1_crew_meal_vesper_story_begin

label act1_crew_meal_vesper_story_begin:
    vesper "Fine. So. We had a contract — simple extraction. Walk in, grab the cargo, walk out. The client neglected to mention the cargo was alive."
    jump act1_crew_meal_jalen_story_interject

label act1_crew_meal_jalen_story_interject:
    jalen "It was a cat."
    jump act1_crew_meal_vesper_story_cat

label act1_crew_meal_vesper_story_cat:
    vesper "{i}Holding up a hand.{/i} It was a genetically modified cat the size of a small dog, with bioluminescent fur and a very specific dietary requirement that no one told us about. Which is how Rho ended up in the ventilation system at three in the morning, covered in synthetic fish paste, trying to lure a glowing cat out of the reactor housing."
    jump act1_crew_meal_table_laughs

label act1_crew_meal_table_laughs:
    "{i}The table erupts. Even Jalen's mouth twitches. Rho is shaking his head but grinning. Nyx covers her mouth with one hand.{/i}"
    jump act1_crew_meal_rho_defense

label act1_crew_meal_rho_defense:
    rho "It liked me! Eventually. After I lost most of a shirt and all of my dignity."
    jump act1_crew_meal_vesper_story_turn

label act1_crew_meal_vesper_story_turn:
    vesper "{i}The smile fades slowly, like light through closing shutters.{/i} The client was a girl. Maybe twelve. The cat was hers — only thing left from before the Compact relocated her family. She'd hidden it in the station's service tunnels for six months. Feeding it scraps. Keeping it alive."
    jump act1_crew_meal_vesper_story_wistful

label act1_crew_meal_vesper_story_wistful:
    vesper "{i}Quiet now.{/i} We didn't charge her. Delivered the cat to her aunt's ship two sectors out. She cried when she held it. Not sad crying. The other kind. The kind that means something broke and then unbroken itself."
    jump act1_crew_meal_vesper_story_silence

label act1_crew_meal_vesper_story_silence:
    "{i}A beat of silence around the table. The kind that isn't empty — it's full. The hum of the ship fills it like a held breath.{/i}"
    jump act1_crew_meal_vesper_story_response

label act1_crew_meal_vesper_story_response:
    menu:
        "'That's why you do this. Not the contracts. This.'":
            $ relationship_manager.process_reputation_affinity("vesper", 1)
            jump act1_crew_meal_vesper_story_affirm
        "'What happened to the girl?'":
            jump act1_crew_meal_vesper_story_girl
        "Say nothing. Let the moment breathe.":
            jump act1_crew_meal_vesper_story_breathe

label act1_crew_meal_vesper_story_affirm:
    vesper "{i}A look that's harder to read than a redacted file.{/i} Some days. Other days it's just work. But that one... that one I kept."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_vesper_story_girl:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "Last I heard, she'd gotten into a trade school on Meridian. Doing well. {i}A pause.{/i} I check. Not often. But I check."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_vesper_story_breathe:
    rho "{i}Quietly, into his bowl.{/i} That cat bit me eleven times. Worth every one."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_rho_jalen_argument:
    rho "I'm telling you — you load the top rack first. Gravity does the work."
    jump act1_crew_meal_jalen_argument_counter

label act1_crew_meal_jalen_argument_counter:
    jalen "We're in artificial gravity. There is no 'gravity does the work.' You load bottom rack first for structural stability. This is basic physics."
    jump act1_crew_meal_rho_argument_escalate

label act1_crew_meal_rho_argument_escalate:
    rho "It's a dishwasher, Jalen. Not a load-bearing wall."
    jump act1_crew_meal_jalen_argument_principle

label act1_crew_meal_jalen_argument_principle:
    jalen "The principle is the same. Structural integrity matters at every scale. You wouldn't stack charges top-down."
    jump act1_crew_meal_rho_argument_charges

label act1_crew_meal_rho_argument_charges:
    rho "{i}Offended.{/i} Don't bring my charges into this. My charges are art. Dishwashing is... dishwashing."
    jump act1_crew_meal_rho_jalen_argument_choice

label act1_crew_meal_rho_jalen_argument_choice:
    "{i}They're both looking at you now, as though you're a tiebreaker they didn't ask for but will absolutely use.{/i}"
    menu:
        "[Tech DC 8] 'The rack geometry is designed for bottom-first loading. Jalen's right.'":
            $ _sc_result = skill_check("Tech", 8, "avyanna")
            jump act1_crew_meal_tech_dishwasher_check
        "'Rho cooked. Rho's method. That's the rule.'":
            $ relationship_manager.process_reputation_affinity("rho", 1)
            jump act1_crew_meal_rho_jalen_side_rho
        "'I'm not getting between a demolitions expert and a data analyst over dishes.'":
            jump act1_crew_meal_rho_jalen_dodge

label act1_crew_meal_tech_dishwasher_check:
    $ _sc_result = skill_check("Tech", 8, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_tech_dishwasher_success
    else:
        jump act1_crew_meal_tech_dishwasher_failure

label act1_crew_meal_tech_dishwasher_success:
    $ game_state.set_flag("dinner_tech_insight")
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    jalen "{i}Vindicated.{/i} Thank you. Someone on this ship understands engineering."
    jump act1_crew_meal_rho_jalen_resolved

label act1_crew_meal_tech_dishwasher_failure:
    rho "{i}Squinting.{/i} That didn't sound confident. I'm sticking with my method."
    jump act1_crew_meal_rho_jalen_resolved

label act1_crew_meal_rho_jalen_side_rho:
    rho "{i}Triumphant.{/i} The new crew member has spoken. Cook's law."
    jump act1_crew_meal_jalen_grudging

label act1_crew_meal_jalen_grudging:
    jalen "{i}Returning to his datapad.{/i} Cook's law isn't real. But I'll allow it. This time."
    jump act1_crew_meal_rho_jalen_resolved

label act1_crew_meal_rho_jalen_dodge:
    rho "{i}Laughing.{/i} Smart. Very smart. Self-preservation instincts are excellent."
    jump act1_crew_meal_jalen_dodge_agree

label act1_crew_meal_jalen_dodge_agree:
    jalen "First sensible thing anyone's said tonight."
    jump act1_crew_meal_rho_jalen_resolved

label act1_crew_meal_rho_jalen_resolved:
    "{i}Rho flicks a crumb at Jalen. Jalen catches it without looking. They've done this a thousand times. The argument was never about dishes.{/i}"
    jump act1_crew_meal_conversation_return

label act1_crew_meal_nyx_drawing_out:
    "{i}Nyx is eating slowly, methodically, gaze drifting between the others like she's cataloguing something. Her bowl is barely touched. When you turn toward her, she notices immediately.{/i}"
    jump act1_crew_meal_nyx_drawing_choice

label act1_crew_meal_nyx_drawing_choice:
    menu:
        "[Empathy DC 10] 'You're not eating. You okay?'":
            $ _sc_result = skill_check("Empathy", 10, "avyanna")
            jump act1_crew_meal_nyx_empathy_check
        "'What do you see? When you watch them like that.'":
            jump act1_crew_meal_nyx_observation_answer
        "Just sit with her. No words. Shared quiet.":
            $ relationship_manager.process_reputation_affinity("nyx", 1)
            jump act1_crew_meal_nyx_shared_quiet

label act1_crew_meal_nyx_empathy_check:
    $ _sc_result = skill_check("Empathy", 10, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_nyx_empathy_success
    else:
        jump act1_crew_meal_nyx_empathy_failure

label act1_crew_meal_nyx_empathy_success:
    $ game_state.set_flag("dinner_nyx_opened_up")
    $ relationship_manager.process_reputation_affinity("nyx", 2)
    nyx "{i}A flicker of surprise — quickly hidden.{/i} I'm... not used to eating with people. In the lab it was trays and silence and data. This is louder. I'm calibrating."
    jump act1_crew_meal_nyx_empathy_followup

label act1_crew_meal_nyx_empathy_followup:
    avyanna "I get that. The mine was the same. Eating was just... refueling. This is different."
    jump act1_crew_meal_nyx_empathy_bond

label act1_crew_meal_nyx_empathy_bond:
    nyx "{i}The smallest nod. Almost imperceptible.{/i} Different. Yes. Not bad different. Just... new variables."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_nyx_empathy_failure:
    nyx "{i}A polite deflection.{/i} I'm fine. Just thinking. Eat your stew."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_nyx_observation_answer:
    nyx "{i}Considering the question seriously.{/i} Rho uses humor as load-bearing structure. Remove it and he'd collapse. Jalen pretends information is a substitute for connection. Elia and Elisira communicate in a frequency the rest of us can't hear. And Vesper... Vesper is always calculating cost."
    jump act1_crew_meal_nyx_observation_you

label act1_crew_meal_nyx_observation_you:
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    nyx "{i}Meeting your eyes.{/i} And you're trying to figure out if this is real. If people can just... eat together. Without an angle."
    jump act1_crew_meal_nyx_observation_response

label act1_crew_meal_nyx_observation_response:
    menu:
        "'Is it? Real?'":
            jump act1_crew_meal_nyx_its_real
        "'You see a lot.'":
            jump act1_crew_meal_nyx_sees_a_lot

label act1_crew_meal_nyx_its_real:
    nyx "{i}A pause long enough to mean something.{/i} As real as anything gets out here. Which is more than you'd think."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_nyx_sees_a_lot:
    nyx "Seeing is easy. Knowing what to do with what you see — that's the hard part. I'm still working on it."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_nyx_shared_quiet:
    "{i}You don't say anything. Neither does Nyx. You eat in parallel silence — the comfortable kind that doesn't need filling. After a minute, Nyx's shoulders drop a fraction of an inch. She takes a real bite of stew.{/i}"
    jump act1_crew_meal_conversation_return

label act1_crew_meal_elisira_elia_exchange:
    "{i}Elisira murmurs something to Elia. Too low to catch. Elia's jaw tightens — barely, a millimeter — and then relaxes. Elisira's hand finds Elia's under the table. Brief. Then gone.{/i}"
    jump act1_crew_meal_elisira_elia_insight_choice

label act1_crew_meal_elisira_elia_insight_choice:
    menu:
        "[Insight DC 12] Try to read what passed between them":
            $ _sc_result = skill_check("Insight", 12, "avyanna")
            jump act1_crew_meal_insight_elisira_elia_check
        "Look away. Some things aren't yours to see.":
            jump act1_crew_meal_elisira_elia_respect_privacy

label act1_crew_meal_insight_elisira_elia_check:
    $ _sc_result = skill_check("Insight", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_insight_elisira_elia_success
    else:
        jump act1_crew_meal_insight_elisira_elia_failure

label act1_crew_meal_insight_elisira_elia_success:
    $ game_state.set_flag("dinner_elisira_elia_insight")
    $ relationship_manager.process_reputation_affinity("elisira", 1)
    $ relationship_manager.process_reputation_affinity("elia", 1)
    "{i}You catch fragments. Elisira said a name — someone from before. Elia's tension wasn't anger. It was grief, swallowed quickly, like medicine. Elisira's touch wasn't comfort. It was an anchor. 'I'm here. That was then.' They've had this conversation in gestures so many times it's become its own language.{/i}"
    jump act1_crew_meal_elisira_notices

label act1_crew_meal_elisira_notices:
    elisira "{i}Catching your eye. Not hostile — assessing.{/i} You're perceptive. That's useful. Just remember — perceptive people have a responsibility to be kind with what they see."
    jump act1_crew_meal_conversation_return

label act1_crew_meal_insight_elisira_elia_failure:
    "{i}You catch the motion but not the meaning. Whatever passed between them is in a dialect you haven't learned yet. Elisira glances at you — neutral, unreadable — then returns to her stew.{/i}"
    jump act1_crew_meal_conversation_return

label act1_crew_meal_elisira_elia_respect_privacy:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    "{i}You look away. Not everything is data. Not everything is yours. Elia notices your deliberate aversion and, after a moment, gives you the smallest nod. Acknowledgment. Maybe respect.{/i}"
    jump act1_crew_meal_conversation_return

label act1_crew_meal_conversation_return:
    "{i}The conversations weave and overlap. There's still time before the meal winds down.{/i}"
    menu:
        "Join another conversation at the table":
            jump act1_crew_meal_table_hub_second
        "This is enough. Just enjoy the moment.":
            jump act1_crew_meal_business_talk

label act1_crew_meal_table_hub_second:
    "{i}Who do you turn to?{/i}"
    menu:
        "Vesper is telling a story about a glowing cat":
            jump act1_crew_meal_vesper_story_setup
        "Rho and Jalen are debating dishwasher physics":
            jump act1_crew_meal_rho_jalen_argument
        "Nyx is unusually quiet in the corner":
            jump act1_crew_meal_nyx_drawing_out
        "Elisira and Elia — that look between them":
            jump act1_crew_meal_elisira_elia_exchange
        "Enough circulating. Settle in.":
            jump act1_crew_meal_business_talk

label act1_crew_meal_business_talk:
    "{i}Conversation flows. Business and dinner coexist without tension.{/i}"
    jump act1_crew_meal_bubbles_dinner_check

label act1_crew_meal_bubbles_dinner_check:
    bubbles "{i}Through the galley speakers, warm and attentive:{/i} Everyone hydrated? I'm tracking low fluid intake across three crew members today. You know who you are."
    jump act1_crew_meal_jalen_called_out

label act1_crew_meal_jalen_called_out:
    jalen "{i}Without looking up.{/i} I had coffee."
    jump act1_crew_meal_bubbles_coffee_water

label act1_crew_meal_bubbles_coffee_water:
    bubbles "Coffee is not water, Jalen. We've had this conversation. Seventeen times."
    jump act1_crew_meal_waffle_dinner_interject

label act1_crew_meal_waffle_dinner_interject:
    waffle "{i}}{{WAFFLE.BAT// CORRECTION: eighteen times | JALEN_COMPLIANCE_RATE: 11%% | RECOMMENDATION: give up}}{/i}}"
    jump act1_crew_meal_souffle_comment

label act1_crew_meal_souffle_comment:
    souffle "{i}The ship's tertiary AI chimes through the overhead speaker — a voice like velvet over static.{/i} For the record, I've been monitoring galley temperature. It's dropped 1.3 degrees since you all sat down. Body heat distribution suggests everyone is comfortable. I adjusted the ventilation to maintain it. {i}A pause.{/i} You're welcome."
    jump act1_crew_meal_rho_souffle_react

label act1_crew_meal_rho_souffle_react:
    rho "{i}Pointing at the ceiling.{/i} See? The ship likes my cooking. The ship has taste."
    jump act1_crew_meal_souffle_correction

label act1_crew_meal_souffle_correction:
    souffle "I adjusted for comfort, not endorsement. My taste protocols are reserved for music selection and interior lighting. Though I will note the stew's aroma profile is... within acceptable parameters."
    jump act1_crew_meal_cinnamon_dinner_brief

label act1_crew_meal_cinnamon_dinner_brief:
    cinnamon "Drill maintenance complete. Bay sealed. No interruptions during meal period."
    jump act1_crew_meal_vesper_recon

label act1_crew_meal_vesper_recon:
    vesper "Status on the new client's recon?"
    jump act1_crew_meal_elia_entry

label act1_crew_meal_elia_entry:
    elia "Two potential entry points. Both viable. Full report by tomorrow."
    jump act1_crew_meal_jalen_patrols

label act1_crew_meal_jalen_patrols:
    jalen "Station Kael-7 is reporting increased Compact patrol activity. Thirty percent more ships than usual. No official reason given."
    jump act1_crew_meal_vesper_flag

label act1_crew_meal_vesper_flag:
    vesper "{i}Thoughtful.{/i} Flag it. If it goes above fifty percent, we reroute. I'm not interested in Compact attention."
    jump act1_crew_meal_tactical_input_choice

label act1_crew_meal_tactical_input_choice:
    "{i}You've seen patrol patterns before. In the mine, you learned to read the guards' rotations. This feels similar.{/i}"
    menu:
        "[Insight DC 10] 'Thirty percent suggests redeployment, not increased vigilance. They're moving assets, not hunting.'":
            $ _sc_result = skill_check("Insight", 10, "avyanna")
            jump act1_crew_meal_tactics_check
        "[Empathy DC 10] 'The lack of official reason is the pattern. They don't explain when they're scared.'":
            $ _sc_result = skill_check("Empathy", 10, "avyanna")
            jump act1_crew_meal_empathy_check
        "Stay silent. You're still learning.":
            jump act1_crew_meal_dishes_argument

label act1_crew_meal_tactics_check:
    $ _sc_result = skill_check("Tactics", 10, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_tactics_success
    else:
        jump act1_crew_meal_tactics_failure

label act1_crew_meal_tactics_success:
    $ game_state.set_flag("dinner_tactical_insight")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}Looking at you with sharp attention.{/i} Exactly. Redeployment implies something worth deploying toward. {i}To Jalen.{/i} Pull fleet movement reports for adjacent sectors. If they're repositioning, I want to know where."
    jump act1_crew_meal_elia_impressed

label act1_crew_meal_tactics_failure:
    vesper "{i}Polite but neutral.{/i} Possible. We'll keep monitoring. Good instinct to think about it."
    jump act1_crew_meal_dishes_argument

label act1_crew_meal_empathy_check:
    $ _sc_result = skill_check("Empathy", 10, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_empathy_success
    else:
        jump act1_crew_meal_empathy_failure

label act1_crew_meal_empathy_success:
    $ game_state.set_flag("dinner_tactical_insight")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    vesper "{i}A slow nod.{/i} Fear makes patterns invisible to the people creating them. {i}To the table.{/i} The Compact doesn't move without reason. We find out what they're scared of before it finds us."
    jump act1_crew_meal_elia_impressed

label act1_crew_meal_empathy_failure:
    vesper "{i}Thoughtful.{/i} Maybe. Or they're just bureaucratic. Hard to tell with the Compact."
    jump act1_crew_meal_dishes_argument

label act1_crew_meal_elia_impressed:
    elia "{i}A rare approving glance.{/i} Keep talking like that. We need tactical minds."
    jump act1_crew_meal_dishes_argument

label act1_crew_meal_dishes_argument:
    elia "Your turn for dishes."
    jump act1_crew_meal_rho_cooked

label act1_crew_meal_rho_cooked:
    rho "I cooked!"
    jump act1_crew_meal_elia_assembly

label act1_crew_meal_elia_assembly:
    elia "You made stew. That's not cooking. That's assembly."
    jump act1_crew_meal_rho_backup

label act1_crew_meal_rho_backup:
    rho "{i}To the table.{/i} Someone back me up here."
    jump act1_crew_meal_vesper_rotation

label act1_crew_meal_vesper_rotation:
    vesper "You're on dish rotation. Elia's correct."
    jump act1_crew_meal_jalen_appreciated

label act1_crew_meal_jalen_appreciated:
    jalen "{i}Without looking up.{/i} You're appreciated exactly the correct amount."
    jump act1_crew_meal_player_toast_opportunity

label act1_crew_meal_player_toast_opportunity:
    "{i}A lull settles. Rho refills coffee. Bowls are scraped clean. The ship hums its low constant note. It feels like a moment that could hold something.{/i}"
    menu:
        "Raise your mug. 'To the Lumen Thief. And her crew.'":
            $ game_state.set_flag("dinner_toasted")
            jump act1_crew_meal_toast_crew
        "Tell a story from the mine — something small, something human":
            jump act1_crew_meal_player_story_mine
        "Ask: 'How did you all find each other?'":
            jump act1_crew_meal_ask_origin
        "Just listen. The silence is enough.":
            jump act1_crew_meal_nyx_quiet

label act1_crew_meal_toast_crew:
    "{i}You raise your mug. Dented metal, still warm. The words come out rough, unrehearsed.{/i}"
    jump act1_crew_meal_toast_words

label act1_crew_meal_toast_words:
    avyanna "To the Lumen Thief. And her crew. I don't know what I did to end up here, but... I'm glad I did."
    jump act1_crew_meal_toast_reaction

label act1_crew_meal_toast_reaction:
    "{i}A beat. Then Rho lifts his mug. Then Vesper. Then, one by one, they all do — even Jalen, who raises his coffee cup without looking up from the datapad, which is its own kind of ceremony.{/i}"
    jump act1_crew_meal_vesper_toast_response

label act1_crew_meal_vesper_toast_response:
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    $ relationship_manager.process_reputation_affinity("rho", 1)
    vesper "{i}Quiet. Genuine.{/i} To the crew."
    jump act1_crew_meal_nyx_quiet

label act1_crew_meal_player_story_mine:
    "{i}The table goes quiet. Not because you demanded it — because they gave it. Freely.{/i}"
    jump act1_crew_meal_player_story_choice

label act1_crew_meal_player_story_choice:
    menu:
        "Tell them about the old miner who sang while he worked — same song, every shift, for twelve years":
            jump act1_crew_meal_mine_story_singer
        "Tell them about the time you stole extra rations to feed someone too sick to work":
            jump act1_crew_meal_mine_story_rations
        "Tell them about the stars you could see from Shaft 7 — one crack in the rock, one sliver of sky":
            jump act1_crew_meal_mine_story_stars

label act1_crew_meal_mine_story_singer:
    avyanna "There was this man in Shaft 4. Kaed. He sang the same song every shift. Twelve years. Nobody knew the words. I don't think he did either, by the end. But the rhythm — it kept us moving. When he died, the shaft went quiet. And the next shift... someone else started humming it."
    jump act1_crew_meal_mine_story_reaction

label act1_crew_meal_mine_story_rations:
    $ game_state.set_flag("dinner_story_rations")
    avyanna "I stole rations once. For a woman named Sera. She was too sick to make quota, and if you didn't make quota, you didn't eat. I hid bread in my sleeve for a week. She never knew it was me. {i}A pause.{/i} She got better. Made quota again. That was enough."
    jump act1_crew_meal_mine_story_reaction

label act1_crew_meal_mine_story_stars:
    avyanna "Shaft 7 had a crack. Just a fracture in the rock — maybe a meter long. But at the right angle, at the right time, you could see stars through it. One thin line of sky. I used to press my face against the stone and just... look. {i}A beat.{/i} I didn't know the names of any of them. I do now."
    jump act1_crew_meal_mine_story_reaction

label act1_crew_meal_mine_story_reaction:
    "{i}No one speaks for a moment. Rho's grin is gone — replaced by something unguarded. Nyx's hands are still. Even Jalen's datapad has gone dark.{/i}"
    jump act1_crew_meal_rho_story_response

label act1_crew_meal_rho_story_response:
    $ relationship_manager.process_reputation_affinity("rho", 1)
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    rho "{i}Quietly.{/i} Thanks. For telling us that."
    jump act1_crew_meal_nyx_quiet

label act1_crew_meal_ask_origin:
    "{i}The question lands like a stone in still water. Glances exchanged — quick, coded.{/i}"
    jump act1_crew_meal_vesper_origin

label act1_crew_meal_vesper_origin:
    vesper "{i}Choosing words like a surgeon choosing instruments.{/i} Separately. Badly. In ways none of us planned. {i}A glance around the table.{/i} Rho was the second. Jalen was the third. Elia and Elisira came as a pair. Nyx was last, before you."
    jump act1_crew_meal_rho_origin_joke

label act1_crew_meal_rho_origin_joke:
    rho "I blew up the wrong building and Vesper hired me because, and I quote, 'anyone who can make that big a mistake and survive has useful instincts.'"
    jump act1_crew_meal_vesper_origin_correction

label act1_crew_meal_vesper_origin_correction:
    vesper "I said you had 'chaotic competence.' There's a difference."
    jump act1_crew_meal_jalen_origin

label act1_crew_meal_jalen_origin:
    jalen "{i}Not volunteering his own story. The datapad glows.{/i} We all had reasons to leave wherever we were. This ship was better than the alternative. For all of us."
    jump act1_crew_meal_nyx_quiet

label act1_crew_meal_nyx_quiet:
    if game_state.has_flag("dinner_watched_nyx"):
        nyx "You've been watching. I noticed. {i}Gentle.{/i} That's not criticism. Observation is how we learn. You're doing fine."
    elif game_state.has_flag("dinner_tactical_insight"):
        nyx "Good observation earlier. About the Compact patrols. {i}Gentle.{/i} You're thinking like crew already. That's faster than most."
    elif game_state.has_flag("dinner_toasted"):
        nyx "That toast. {i}Gentle.{/i} It meant something. To them. To me. You should know that."
    else:
        nyx "You're quiet tonight. More than usual. {i}Gentle.{/i} That wasn't criticism. Just observation. You're allowed to be quiet."
    jump act1_crew_meal_meal_choice

label act1_crew_meal_meal_choice:
    menu:
        "'I'm just listening. Learning how this works.'":
            jump act1_crew_meal_nyx_strategy
        "'Can I help with dishes? I know it's not my turn, but...'":
            jump act1_crew_meal_rho_grace
        "Just smile. The first real one in weeks.":
            jump act1_crew_meal_smile_end

label act1_crew_meal_nyx_strategy:
    nyx "Good strategy. You'll figure out when you want to talk. No pressure."
    jump act1_crew_meal_tone_shift

label act1_crew_meal_rho_grace:
    rho "{i}Waving you off.{/i} You're still new. Grace period. First month on crew, you're exempt from chores. Your job is learning to exist here without constant survival math."
    jump act1_crew_meal_vesper_explains

label act1_crew_meal_vesper_explains:
    vesper "Lets you acclimate without added pressure. You'll contribute plenty. Right now, just be here."
    jump act1_crew_meal_tone_shift

label act1_crew_meal_smile_end:
    "{i}You smile. Small. Involuntary. Rho notices and grins back. Jalen nods without comment. The presence behind your eyes pulses — warm, approving, curious about this thing called 'belonging.'{/i}"
    jump act1_crew_meal_tone_shift

label act1_crew_meal_tone_shift:
    "{i}The meal is winding. Bowls are empty, coffee is dregs. The warmth of the galley has that fragile quality — like a candle flame in a room with too many doors.{/i}"
    jump act1_crew_meal_jalen_tone_shift

label act1_crew_meal_jalen_tone_shift:
    jalen "{i}Setting down the datapad. The first time all evening.{/i} There's something else. The Kael-7 patrols... they correlate with a Writ-Bound sighting report. Unconfirmed, but the source is solid."
    jump act1_crew_meal_table_silence

label act1_crew_meal_table_silence:
    "{i}The table goes still. Not quiet — still. The kind of stillness that has weight. Rho stops smiling. Elia's hand moves to her belt, instinctive, then back. Elisira's eyes find Vesper's.{/i}"
    jump act1_crew_meal_vesper_writ_response

label act1_crew_meal_vesper_writ_response:
    vesper "{i}Very calm. The kind of calm that is itself a warning.{/i} How solid?"
    jump act1_crew_meal_jalen_writ_detail

label act1_crew_meal_jalen_writ_detail:
    jalen "Seven out of ten. The reporter has been reliable before. Never cried wolf on Writ-Bound specifically."
    jump act1_crew_meal_elia_writ_response

label act1_crew_meal_elia_writ_response:
    elia "{i}Flat. Professional.{/i} Then we assume it's real until proven otherwise. What's our exposure?"
    jump act1_crew_meal_jalen_exposure

label act1_crew_meal_jalen_exposure:
    jalen "Two jumps from our planned route. If they're moving toward Kael-7, our window narrows. If they're moving away, we're fine."
    jump act1_crew_meal_danger_response_choice

label act1_crew_meal_danger_response_choice:
    "{i}The warmth of dinner hasn't left the room. But something else has entered it. The meal and the mission, occupying the same air.{/i}"
    menu:
        "[Perception DC 12] 'Two jumps means a day's warning at minimum. Enough to adjust.'":
            $ _sc_result = skill_check("Perception", 12, "avyanna")
            jump act1_crew_meal_tactics_danger_check
        "[Insight DC 12] Watch the crew's reactions — read what they're not saying":
            $ _sc_result = skill_check("Insight", 12, "avyanna")
            jump act1_crew_meal_insight_danger_check
        "'What are Writ-Bound?'":
            jump act1_crew_meal_writ_bound_explain
        "Stay quiet. You don't know enough to speak.":
            jump act1_crew_meal_elia_brings_back

label act1_crew_meal_tactics_danger_check:
    $ _sc_result = skill_check("Tactics", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_tactics_danger_success
    else:
        jump act1_crew_meal_tactics_danger_failure

label act1_crew_meal_tactics_danger_success:
    $ game_state.set_flag("dinner_writ_bound_tactics")
    $ relationship_manager.process_reputation_affinity("vesper", 1)
    $ relationship_manager.process_reputation_affinity("jalen", 1)
    vesper "{i}A nod — slower this time, weighted.{/i} Correct. A day's buffer is workable. Jalen, set up an alert threshold. If Writ-Bound signatures enter single-jump range, I want to know immediately."
    jump act1_crew_meal_elia_brings_back

label act1_crew_meal_tactics_danger_failure:
    jalen "{i}Measured.{/i} Two jumps is variable. Depends on their drive configuration. Could be a day. Could be six hours. Don't assume comfort margins."
    jump act1_crew_meal_elia_brings_back

label act1_crew_meal_insight_danger_check:
    $ _sc_result = skill_check("Insight", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_crew_meal_insight_danger_success
    else:
        jump act1_crew_meal_insight_danger_failure

label act1_crew_meal_insight_danger_success:
    $ game_state.set_flag("dinner_read_crew_fear")
    $ relationship_manager.process_reputation_affinity("nyx", 1)
    "{i}Rho's fear is in his hands — they've gone still, the demolitions expert's instinct to hold steady when the ground shifts. Jalen's fear is in his voice — too flat, too precise. Nyx isn't afraid. She's calculating. And Vesper... Vesper is already three moves ahead, and doesn't like what they see.{/i}"
    jump act1_crew_meal_elia_brings_back

label act1_crew_meal_insight_danger_failure:
    "{i}The crew's reactions are guarded. Whatever Writ-Bound means to them, they've practiced not showing it.{/i}"
    jump act1_crew_meal_elia_brings_back

label act1_crew_meal_writ_bound_explain:
    vesper "{i}Choosing each word.{/i} Writ-Bound are... Compact enforcement taken to its theological conclusion. Augmented. Indoctrinated. They don't patrol — they hunt. And their definition of 'heresy' is broader than the Compact's official line. If they're near Kael-7, it means someone drew attention."
    jump act1_crew_meal_nyx_writ_addition

label act1_crew_meal_nyx_writ_addition:
    nyx "{i}Very quiet.{/i} They don't negotiate. They don't take prisoners. And they have technology that shouldn't exist. {i}A beat.{/i} I've seen their work. In a lab. What was left."
    jump act1_crew_meal_elia_brings_back

label act1_crew_meal_elia_brings_back:
    "{i}The silence stretches. The ship hums. Someone's bowl scrapes against the table — too loud in the quiet.{/i}"
    jump act1_crew_meal_elia_anchor

label act1_crew_meal_elia_anchor:
    elia "{i}Setting both hands flat on the table. Deliberate. An anchor.{/i} We eat. We rest. Tomorrow we plan. That's how this works. The danger will still be there in the morning. It doesn't get our evening too."
    jump act1_crew_meal_elia_anchor_reaction

label act1_crew_meal_elia_anchor_reaction:
    "{i}The words land. Not like an order — like a door closing gently on a cold wind. Rho exhales. Jalen picks up the datapad, then sets it down again. Deliberately. Nyx's shoulders ease.{/i}"
    jump act1_crew_meal_elisira_anchor_support

label act1_crew_meal_elisira_anchor_support:
    elisira "{i}Pouring the last of the coffee.{/i} Elia's right. Tomorrow's problems belong to tomorrow's crew. Tonight we're just people who had a meal together. That matters more than any of you want to admit."
    jump act1_crew_meal_vesper_final_word

label act1_crew_meal_vesper_final_word:
    vesper "{i}Standing. Pushing in their chair — the small formality that means 'meeting adjourned.'{/i} Agreed. Early start tomorrow. Get some rest. All of you."
    jump act1_crew_meal_meal_end

label act1_crew_meal_meal_end:
    "{i}Rho washes dishes. Jalen dries. Nyx disappears to her lab. Elia and Elisira sit close, speaking in low voices about tomorrow's work.

And you sit at the table, in a chair that's comfortable, with a full stomach, in a room full of people who aren't keeping score.

This is what dinner is supposed to be. You're only just learning that.{/i}"
    return
