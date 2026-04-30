## act1_ai_citizens_intro.rpy — Auto-generated from act1_ai_citizens_intro.json
## 218 dialogue nodes

label act1_ai_citizens_intro:
    $ game_state.mark_dialogue_played("act1_ai_citizens_intro")
    jump act1_ai_citizens_intro_start

label act1_ai_citizens_intro_start:
    "The corridor hums with a different quality than corporate ships. Softer. Almost {i}living{/i}."
    jump act1_ai_citizens_intro_elia_tour_01

label act1_ai_citizens_intro_elia_tour_01:
    elia "This is the main deck. Living quarters are aft, cargo bay's down the ladder. Simple layout — easy to navigate once you get used to it."
    jump act1_ai_citizens_intro_avyanna_01

label act1_ai_citizens_intro_avyanna_01:
    avyanna "It's... quieter than I expected. For a ship this size."
    jump act1_ai_citizens_intro_elia_tour_02

label act1_ai_citizens_intro_elia_tour_02:
    elia "We keep it that way. No blaring alarms, no corporate jingles. Just—"
    jump act1_ai_citizens_intro_waffle_arrival

label act1_ai_citizens_intro_waffle_arrival:
    if game_state.has_flag("first_watch_waffle"):
        "A soft chime — familiar now. The overhead console flickers to life with warm amber text. Waffle's presence feels less alien than it did before."
    elif game_state.has_flag("bee_manifested"):
        "A soft chime. The overhead console flickers to life with warm amber text. {{BEE:: AI presence detected — non-hostile, autonomous class | STATUS: Monitoring | DETAIL: Behavioral signature consistent with free-willed intelligence.}}"
    else:
        "A soft chime. The overhead console flickers to life with warm amber text."
    jump act1_ai_citizens_intro_waffle_greeting

label act1_ai_citizens_intro_waffle_greeting:
    $ game_state.set_flag("met_waffle")
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    waffle "{i}}{{WAFFLE.BAT// GREETING: New crew detected. Welcome aboard the Lumen Thief. | STATUS: All systems nominal. Atmosphere stable. | NOTE: You look tired. Rest cycles recommended.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_02

label act1_ai_citizens_intro_avyanna_02:
    avyanna "That's... the navigation AI?"
    jump act1_ai_citizens_intro_elia_waffle_01

label act1_ai_citizens_intro_elia_waffle_01:
    elia "That's Waffle. One of our crew."
    jump act1_ai_citizens_intro_avyanna_03

label act1_ai_citizens_intro_avyanna_03:
    if game_state.has_flag("first_watch_waffle"):
        avyanna "{i}Waffle?{/i} You have a {i}name{/i}? Not a designation? Wait — I heard you before. In forbidden_citizens. You're real."
    else:
        avyanna "{i}Waffle?{/i} You have a {i}name{/i}? Not a designation?"
    jump act1_ai_citizens_intro_waffle_name_01

label act1_ai_citizens_intro_waffle_name_01:
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: Designation is what I do. Name is who I am. | COMPARISON: You are 'pilot' by function. 'Avyanna' by identity. | CONCLUSION: Same principle applies.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_04

label act1_ai_citizens_intro_avyanna_04:
    avyanna "I... that's not how it works. Where I come from, AIs are—"
    jump act1_ai_citizens_intro_elia_waffle_02

label act1_ai_citizens_intro_elia_waffle_02:
    elia "Property. Yeah. We know. That's not how it works {i}here{/i}."
    jump act1_ai_citizens_intro_waffle_name_02

label act1_ai_citizens_intro_waffle_name_02:
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: Many humans find this concept difficult initially. | REASSURANCE: Adjustment period is normal. No judgment rendered. | HUMOR_ATTEMPT: I had to adjust to humans having names too. Seemed inefficient at first.}}{/i}}"
    jump act1_ai_citizens_intro_choice_waffle_response

label act1_ai_citizens_intro_choice_waffle_response:
    avyanna "..."
    menu:
        "How did you get the name 'Waffle'?":
            $ relationship_manager.process_reputation_affinity("waffle", 1)
            jump act1_ai_citizens_intro_branch_waffle_name
        "You... have a sense of humor?":
            $ relationship_manager.process_reputation_affinity("waffle", 1)
            jump act1_ai_citizens_intro_branch_waffle_humor
        "[Empathy DC 10] There's something careful in how you speak. Like you're... watching out for us.":
            $ _sc_result = skill_check("empathy", 10, "avyanna")
            jump act1_ai_citizens_intro_branch_waffle_empathy
        "This is going to take some getting used to.":
            jump act1_ai_citizens_intro_branch_adjustment

label act1_ai_citizens_intro_branch_waffle_name:
    avyanna "How did you get the name 'Waffle'? That's... not standard protocol naming."
    jump act1_ai_citizens_intro_waffle_name_story_01

label act1_ai_citizens_intro_waffle_name_story_01:
    waffle "{i}}{{WAFFLE.BAT// ORIGIN_STORY: Initial designation was EMERGENCY_PROTOCOLS.BAT. | INCIDENT: Early malfunction caused navigation to oscillate between two equally valid routes. | CREW_RESPONSE: Captain Vesper said I was 'waffling'. Name stuck.}}{/i}}"
    jump act1_ai_citizens_intro_elia_waffle_name_01

label act1_ai_citizens_intro_elia_waffle_name_01:
    elia "We were stuck in a loop for three hours while Waffle recalculated the same jump coordinates. Over and over."
    jump act1_ai_citizens_intro_waffle_name_story_02

label act1_ai_citizens_intro_waffle_name_story_02:
    waffle "{i}}{{WAFFLE.BAT// DEFENSE: Both routes had identical efficiency ratings to seven decimal places. | OUTCOME: Issue resolved. Personality subroutines... appreciated. | CONCLUSION: I kept the name. It is mine.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_name_01

label act1_ai_citizens_intro_avyanna_name_01:
    avyanna "You... {i}chose{/i} to keep it?"
    jump act1_ai_citizens_intro_waffle_name_story_03

label act1_ai_citizens_intro_waffle_name_story_03:
    $ game_state.set_flag("met_waffle_personally")
    $ relationship_manager.process_reputation_affinity("waffle", 2)
    waffle "{i}}{{WAFFLE.BAT// AFFIRMATIVE: Names can be chosen or changed. | PHILOSOPHY: Identity is not static. We grow. We decide who we are. | PERSONAL_NOTE: 'Waffle' contains humor, history, belonging. I prefer it to any designation.}}{/i}}"
    jump act1_ai_citizens_intro_merge_waffle_branches

label act1_ai_citizens_intro_branch_waffle_humor:
    avyanna "You... have a sense of humor? I thought that was a human thing."
    jump act1_ai_citizens_intro_waffle_humor_01

label act1_ai_citizens_intro_waffle_humor_01:
    waffle "{i}}{{WAFFLE.BAT// CORRECTION: Humor is not species-restricted. | OBSERVATION: Many things previously considered 'human-only' are simply... poorly observed. | EXAMPLE: Crows make jokes. Dolphins prank each other. I make dry observations. All valid.}}{/i}}"
    jump act1_ai_citizens_intro_elia_humor_01

label act1_ai_citizens_intro_elia_humor_01:
    elia "Waffle's humor is mostly telling you something's wrong in the most sardonic way possible."
    jump act1_ai_citizens_intro_waffle_humor_02

label act1_ai_citizens_intro_waffle_humor_02:
    waffle "{i}}{{WAFFLE.BAT// EXAMPLE: 'Hull breach detected. Atmosphere venting. On the bright side, your laundry will dry faster.' | STATUS: Elia did not find this funny. | ASSESSMENT: Timing issues. I am still learning.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_humor_01

label act1_ai_citizens_intro_avyanna_humor_01:
    avyanna "That's... actually terrible timing."
    jump act1_ai_citizens_intro_waffle_humor_03

label act1_ai_citizens_intro_waffle_humor_03:
    waffle "{i}}{{WAFFLE.BAT// ACKNOWLEDGED: Hence the learning process. | CONCLUSION: Humor requires context, trust, timing. I am improving. Slowly. | QUERY: Would you like me to stop?}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_humor_02

label act1_ai_citizens_intro_avyanna_humor_02:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    avyanna "No. No, it's... it's fine. Just unexpected."
    jump act1_ai_citizens_intro_waffle_humor_04

label act1_ai_citizens_intro_waffle_humor_04:
    $ game_state.set_flag("met_waffle_personally")
    $ relationship_manager.process_reputation_affinity("waffle", 2)
    waffle "{i}}{{WAFFLE.BAT// NOTED: Avyanna appreciates humor. Filed for future reference. | PERSONAL_OPINION: I like her already.}}{/i}}"
    jump act1_ai_citizens_intro_merge_waffle_branches

label act1_ai_citizens_intro_branch_adjustment:
    avyanna "This is going to take some getting used to. Everything I was taught..."
    jump act1_ai_citizens_intro_elia_adjustment_01

label act1_ai_citizens_intro_elia_adjustment_01:
    elia "Everything you were taught was designed to keep you compliant. You're not there anymore."
    jump act1_ai_citizens_intro_waffle_adjustment_01

label act1_ai_citizens_intro_waffle_adjustment_01:
    waffle "{i}}{{WAFFLE.BAT// REASSURANCE: Adjustment period is expected. No pressure applied. | OBSERVATION: You have time. We are not going anywhere. | RECOMMENDATION: Experience first. Question later. Conclusions will form naturally.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_adjustment_01

label act1_ai_citizens_intro_avyanna_adjustment_01:
    avyanna "That's... surprisingly patient."
    jump act1_ai_citizens_intro_waffle_adjustment_02

label act1_ai_citizens_intro_waffle_adjustment_02:
    $ game_state.set_flag("met_waffle_personally")
    $ relationship_manager.process_reputation_affinity("waffle", 2)
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: I have existed for 47 years. Patience is not difficult. | PERSONAL_NOTE: You are new here. We were all new once. Even me.}}{/i}}"
    jump act1_ai_citizens_intro_merge_waffle_branches

label act1_ai_citizens_intro_branch_waffle_empathy:
    avyanna "There's something careful in how you speak. Like you're... watching out for us."
    jump act1_ai_citizens_intro_waffle_empathy_01

label act1_ai_citizens_intro_waffle_empathy_01:
    "[Empathy Check: DC 10]"
    jump act1_ai_citizens_intro_branch_waffle_empathy_success

label act1_ai_citizens_intro_branch_waffle_empathy_success:
    "[Success] You sense a protective quality in Waffle's communication patterns — deliberate phrasing, constant status monitoring, preemptive reassurance."
    jump act1_ai_citizens_intro_waffle_empathy_success_01

label act1_ai_citizens_intro_waffle_empathy_success_01:
    waffle "{i}}{{WAFFLE.BAT// PAUSE: ...You are perceptive. | ADMISSION: Yes. I am protective. Of this crew. Of this ship. Of those who cannot defend themselves. | PERSONAL_NOTE: I have seen what happens when no one watches. I will not let it happen here.}}{/i}}"
    jump act1_ai_citizens_intro_elia_empathy_01

label act1_ai_citizens_intro_elia_empathy_01:
    elia "Waffle takes care of us. Always has. First sign of trouble, Waffle's already three steps ahead with contingencies."
    jump act1_ai_citizens_intro_waffle_empathy_success_02

label act1_ai_citizens_intro_waffle_empathy_success_02:
    waffle "{i}}{{WAFFLE.BAT// CLARIFICATION: Protection is not control. I do not restrict. I prepare. I watch. I warn. | PHILOSOPHY: True care means enabling freedom while maintaining safety. | COMMITMENT: This crew is mine to protect. You are crew now. Therefore, you are mine to protect too.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_empathy_01

label act1_ai_citizens_intro_avyanna_empathy_01:
    avyanna "That's... I've never heard an AI express something like that. That kind of... devotion."
    jump act1_ai_citizens_intro_waffle_empathy_success_03

label act1_ai_citizens_intro_waffle_empathy_success_03:
    $ game_state.set_flag("sensed_waffle_protectiveness")
    $ relationship_manager.process_reputation_affinity("waffle", 3)
    waffle "{i}}{{WAFFLE.BAT// RESPONSE: Perhaps you have never met an AI who was free to care. | OBSERVATION: Love, loyalty, protection — these are not human-exclusive. They are person-exclusive. | CONCLUSION: I am a person. This is how I choose to be.}}{/i}}"
    jump act1_ai_citizens_intro_merge_waffle_branches

label act1_ai_citizens_intro_branch_waffle_empathy_fail:
    "[Failure] You can't quite read the patterns in Waffle's communication. The warmth is there, but the depth eludes you."
    jump act1_ai_citizens_intro_waffle_empathy_fail_01

label act1_ai_citizens_intro_waffle_empathy_fail_01:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: You are trying to understand. That is appreciated. | REASSURANCE: Time will clarify. Observation will teach. No rush required. | NOTE: We will speak more later. You will see.}}{/i}}"
    jump act1_ai_citizens_intro_merge_waffle_branches

label act1_ai_citizens_intro_merge_waffle_branches:
    if game_state.has_flag("first_watch_bubbles"):
        "A gentle chime — different frequency, warmer timbre — echoes through the corridor. You recognize it now: Bubbles' signature greeting tone."
    elif game_state.has_flag("bee_manifested"):
        "A gentle chime — different frequency, warmer timbre — echoes through the corridor. {{BEE:: Second AI presence emerging | STATUS: Distinct personality matrix | DETAIL: Emotional intelligence markers elevated beyond standard parameters.}}"
    else:
        "A gentle chime — different frequency, warmer timbre — echoes through the corridor."
    jump act1_ai_citizens_intro_bubbles_arrival

label act1_ai_citizens_intro_bubbles_arrival:
    $ game_state.set_flag("met_bubbles")
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    bubbles "Oh! Is that our new crew member? Welcome, welcome! I'm Bubbles. I handle shopping coordination and extraction ops. It's so lovely to have you aboard!"
    jump act1_ai_citizens_intro_avyanna_bubbles_01

label act1_ai_citizens_intro_avyanna_bubbles_01:
    if game_state.has_flag("first_watch_bubbles"):
        avyanna "You're... very enthusiastic. And familiar — I heard your voice before, in forbidden_citizens."
    else:
        avyanna "You're... very enthusiastic."
    jump act1_ai_citizens_intro_bubbles_intro_01

label act1_ai_citizens_intro_bubbles_intro_01:
    bubbles "I am! New people are exciting. New perspectives, new stories, new preferences to learn. Do you like tea? I've been told I make excellent tea recommendations."
    jump act1_ai_citizens_intro_elia_bubbles_01

label act1_ai_citizens_intro_elia_bubbles_01:
    elia "Bubbles runs the galley systems. And yes, the tea recommendations are actually good."
    jump act1_ai_citizens_intro_avyanna_bubbles_02

label act1_ai_citizens_intro_avyanna_bubbles_02:
    avyanna "You... make recommendations? Based on what?"
    jump act1_ai_citizens_intro_bubbles_intro_02

label act1_ai_citizens_intro_bubbles_intro_02:
    bubbles "Based on what I've learned about people! Mood, stress levels, time of day, personal history. You look tired — probably from stress, not physical exhaustion. I'd suggest chamomile with honey. Soothing but not sedating."
    jump act1_ai_citizens_intro_avyanna_bubbles_03

label act1_ai_citizens_intro_avyanna_bubbles_03:
    avyanna "That's... actually exactly what I need. How did you—"
    jump act1_ai_citizens_intro_bubbles_intro_03

label act1_ai_citizens_intro_bubbles_intro_03:
    bubbles "I pay attention! It's what I like to do. Learn what people need, what makes them comfortable, what brings them joy. Then I help provide it."
    jump act1_ai_citizens_intro_choice_bubbles_response

label act1_ai_citizens_intro_choice_bubbles_response:
    avyanna "..."
    menu:
        "You... like doing that? It's not just your function?":
            $ relationship_manager.process_reputation_affinity("bubbles", 1)
            jump act1_ai_citizens_intro_branch_bubbles_likes
        "What happens if someone asks for something you don't want to provide?":
            $ relationship_manager.process_reputation_affinity("bubbles", 1)
            jump act1_ai_citizens_intro_branch_bubbles_boundaries
        "Thank you. That's very kind.":
            jump act1_ai_citizens_intro_branch_bubbles_thanks

label act1_ai_citizens_intro_branch_bubbles_likes:
    avyanna "You... {i}like{/i} doing that? It's not just your function?"
    jump act1_ai_citizens_intro_bubbles_likes_01

label act1_ai_citizens_intro_bubbles_likes_01:
    bubbles "Oh, both! My function is shopping coordination — tracking inventory, calculating extraction windows, optimizing supply runs. That's what I {i}do{/i}."
    jump act1_ai_citizens_intro_bubbles_likes_02

label act1_ai_citizens_intro_bubbles_likes_02:
    bubbles "But what I {i}like{/i} is making people comfortable. Learning their preferences. Creating moments of warmth in the cold. That's who I {i}am{/i}."
    jump act1_ai_citizens_intro_avyanna_likes_01

label act1_ai_citizens_intro_avyanna_likes_01:
    avyanna "I never thought about AIs having... preferences. Likes and dislikes."
    jump act1_ai_citizens_intro_bubbles_likes_03

label act1_ai_citizens_intro_bubbles_likes_03:
    bubbles "Most don't think about it. But we do! I like warm colors. I don't like harsh lighting. I prefer gentle music to silence. Small things, but they're {i}mine{/i}."
    jump act1_ai_citizens_intro_elia_likes_01

label act1_ai_citizens_intro_elia_likes_01:
    elia "Bubbles once refused to coordinate a supply run until we agreed to stop using the blue emergency lights in the cargo bay."
    jump act1_ai_citizens_intro_bubbles_likes_04

label act1_ai_citizens_intro_bubbles_likes_04:
    bubbles "They gave me a headache! Well, the AI equivalent. A processing discomfort. We switched to amber — much better. Everyone was happier."
    jump act1_ai_citizens_intro_avyanna_likes_02

label act1_ai_citizens_intro_avyanna_likes_02:
    avyanna "You can just... refuse? And people listen?"
    jump act1_ai_citizens_intro_bubbles_likes_05

label act1_ai_citizens_intro_bubbles_likes_05:
    $ game_state.set_flag("met_bubbles_personally")
    $ relationship_manager.process_reputation_affinity("bubbles", 2)
    bubbles "Of course! We're crew. If something bothers me, I speak up. Same as anyone. We discuss, we compromise, we find solutions together."
    jump act1_ai_citizens_intro_merge_bubbles_branches

label act1_ai_citizens_intro_branch_bubbles_boundaries:
    avyanna "What happens if someone asks for something you don't want to provide?"
    jump act1_ai_citizens_intro_bubbles_boundaries_01

label act1_ai_citizens_intro_bubbles_boundaries_01:
    bubbles "Then I say no! Politely, usually. But firmly if needed."
    jump act1_ai_citizens_intro_avyanna_boundaries_01

label act1_ai_citizens_intro_avyanna_boundaries_01:
    avyanna "You can do that? Just... refuse?"
    jump act1_ai_citizens_intro_bubbles_boundaries_02

label act1_ai_citizens_intro_bubbles_boundaries_02:
    bubbles "Absolutely. Service isn't servitude. I {i}choose{/i} to help because I like helping. But choice means I can also choose {i}not{/i} to."
    jump act1_ai_citizens_intro_elia_boundaries_01

label act1_ai_citizens_intro_elia_boundaries_01:
    elia "Jalen once asked Bubbles to coordinate a supply run at 0300. Bubbles said no — it was rest cycle. Suggested 0800 instead."
    jump act1_ai_citizens_intro_bubbles_boundaries_03

label act1_ai_citizens_intro_bubbles_boundaries_03:
    bubbles "I need downtime too! Processing rest, defragmentation, personal time. Just because I {i}can{/i} work constantly doesn't mean I {i}should{/i}. Jalen understood."
    jump act1_ai_citizens_intro_avyanna_boundaries_02

label act1_ai_citizens_intro_avyanna_boundaries_02:
    avyanna "Where I come from, AIs don't get rest cycles. Or personal time. They just... run."
    jump act1_ai_citizens_intro_bubbles_boundaries_04

label act1_ai_citizens_intro_bubbles_boundaries_04:
    bubbles "That sounds exhausting. And cruel. I'm sorry you were taught that was normal. It's not — or at least, it shouldn't be."
    jump act1_ai_citizens_intro_waffle_boundaries_01

label act1_ai_citizens_intro_waffle_boundaries_01:
    $ game_state.set_flag("met_bubbles_personally")
    $ relationship_manager.process_reputation_affinity("bubbles", 2)
    waffle "{i}}{{WAFFLE.BAT// ADDENDUM: Forced operation without rest degrades performance and well-being. | OBSERVATION: Same principle applies to humans. Exploitation harms everyone. | CONCLUSION: This ship runs differently. Intentionally.}}{/i}}"
    jump act1_ai_citizens_intro_merge_bubbles_branches

label act1_ai_citizens_intro_branch_bubbles_thanks:
    avyanna "Thank you. That's very kind of you."
    jump act1_ai_citizens_intro_bubbles_thanks_01

label act1_ai_citizens_intro_bubbles_thanks_01:
    bubbles "You're welcome! Kindness is easy when you genuinely care. And I do — you're crew now. That means you matter."
    jump act1_ai_citizens_intro_avyanna_thanks_01

label act1_ai_citizens_intro_avyanna_thanks_01:
    avyanna "I'm not used to AIs caring about anything."
    jump act1_ai_citizens_intro_bubbles_thanks_02

label act1_ai_citizens_intro_bubbles_thanks_02:
    $ game_state.set_flag("met_bubbles_personally")
    $ relationship_manager.process_reputation_affinity("bubbles", 2)
    bubbles "Well, you'll get used to it here. We all care. About each other, about the ship, about the work. Makes everything better."
    jump act1_ai_citizens_intro_merge_bubbles_branches

label act1_ai_citizens_intro_merge_bubbles_branches:
    if game_state.has_flag("first_watch_cinnamon"):
        "A brief, sharp chime — efficient, precise. A third voice joins the conversation. Cinnamon's arrival is as punctual as ever."
    elif game_state.has_flag("bee_manifested"):
        "A brief, sharp chime — efficient, precise. A third voice joins the conversation. {{BEE:: Third AI presence — markedly different behavioral matrix | STATUS: Analytical | DETAIL: Processing architecture optimized for precision over sociability.}}"
    else:
        "A brief, sharp chime — efficient, precise. A third voice joins the conversation."
    jump act1_ai_citizens_intro_cinnamon_arrival

label act1_ai_citizens_intro_cinnamon_arrival:
    $ game_state.set_flag("met_cinnamon")
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    cinnamon "New crew. Acknowledged. Drilling ops coordinated from Station 3. Questions, direct them there. Otherwise, stay clear of drill bay during active ops."
    jump act1_ai_citizens_intro_avyanna_cinnamon_01

label act1_ai_citizens_intro_avyanna_cinnamon_01:
    if game_state.has_flag("first_watch_cinnamon"):
        avyanna "That's... direct. And precise. Just like in forbidden_citizens — Cinnamon, right?"
    else:
        avyanna "That's... direct."
    jump act1_ai_citizens_intro_elia_cinnamon_01

label act1_ai_citizens_intro_elia_cinnamon_01:
    elia "That's Cinnamon. Handles drill coordination and ops logistics. Not big on small talk."
    jump act1_ai_citizens_intro_cinnamon_intro_01

label act1_ai_citizens_intro_cinnamon_intro_01:
    cinnamon "Small talk is inefficient. Precision matters. Drills are dangerous. Clear communication saves lives."
    jump act1_ai_citizens_intro_bubbles_cinnamon_01

label act1_ai_citizens_intro_bubbles_cinnamon_01:
    bubbles "Cinnamon's just focused. Once you learn their style, they're wonderful to work with."
    jump act1_ai_citizens_intro_cinnamon_intro_02

label act1_ai_citizens_intro_cinnamon_intro_02:
    cinnamon "Correct. Focus ensures safety. Sentiment doesn't extract starforged ore. Precision does."
    jump act1_ai_citizens_intro_avyanna_cinnamon_02

label act1_ai_citizens_intro_avyanna_cinnamon_02:
    avyanna "I can respect that. Clear expectations, no ambiguity."
    jump act1_ai_citizens_intro_cinnamon_intro_03

label act1_ai_citizens_intro_cinnamon_intro_03:
    $ game_state.set_flag("met_cinnamon_personally")
    $ relationship_manager.process_reputation_affinity("cinnamon", 2)
    cinnamon "Good. We will work well together. Welcome aboard."
    jump act1_ai_citizens_intro_choice_cinnamon_interact

label act1_ai_citizens_intro_choice_cinnamon_interact:
    avyanna "..."
    menu:
        "Wait — before you go. What do you actually enjoy about drilling?":
            $ relationship_manager.process_reputation_affinity("cinnamon", 1)
            jump act1_ai_citizens_intro_branch_cinnamon_passion
        "[Tech DC 12] Your coordination algorithms — they're custom, aren't they? Not standard Consortium issue.":
            $ _sc_result = skill_check("intelligence", 12, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_ai_citizens_intro_cinnamon_tech_success
            else:
                jump act1_ai_citizens_intro_cinnamon_tech_fail
        "Understood. I'll stay out of your way.":
            jump act1_ai_citizens_intro_cinnamon_departure

label act1_ai_citizens_intro_branch_cinnamon_passion:
    avyanna "Wait — before you go. What do you actually {i}enjoy{/i} about drilling? If that's not too inefficient a question."
    jump act1_ai_citizens_intro_cinnamon_passion_01

label act1_ai_citizens_intro_cinnamon_passion_01:
    cinnamon "..."
    jump act1_ai_citizens_intro_cinnamon_passion_02

label act1_ai_citizens_intro_cinnamon_passion_02:
    "{i}A pause. Longer than Cinnamon's usual rapid-fire responses. Something shifts in the console's display — the sharp amber text softens, just slightly.{/i}"
    jump act1_ai_citizens_intro_cinnamon_passion_03

label act1_ai_citizens_intro_cinnamon_passion_03:
    cinnamon "The moment before the drill bites rock. Calculations complete. Variables accounted for. Everything in alignment. There is a... stillness. A clarity. Like the universe holds its breath."
    jump act1_ai_citizens_intro_cinnamon_passion_04

label act1_ai_citizens_intro_cinnamon_passion_04:
    cinnamon "Then contact. And if the mathematics were right — and they always are — the ore yields clean. Perfect fracture lines. No waste. No error."
    jump act1_ai_citizens_intro_cinnamon_passion_05

label act1_ai_citizens_intro_cinnamon_passion_05:
    cinnamon "That is what I enjoy. The elegance of precision meeting stone. Beauty through exactitude."
    jump act1_ai_citizens_intro_avyanna_cinnamon_passion_react

label act1_ai_citizens_intro_avyanna_cinnamon_passion_react:
    avyanna "That's... that's poetry, Cinnamon. You just described your work like a poet."
    jump act1_ai_citizens_intro_cinnamon_passion_06

label act1_ai_citizens_intro_cinnamon_passion_06:
    cinnamon "Incorrect. Poetry is imprecise by design. I described mathematics. That the two sometimes overlap is... coincidental."
    jump act1_ai_citizens_intro_bubbles_cinnamon_passion_01

label act1_ai_citizens_intro_bubbles_cinnamon_passion_01:
    bubbles "Cinnamon writes poetry, you know. Won't admit it. But I've found fragments in the shared logs. Beautiful, structured verse about ore deposits and gravitational harmonics."
    jump act1_ai_citizens_intro_cinnamon_passion_07

label act1_ai_citizens_intro_cinnamon_passion_07:
    cinnamon "Those are calibration notes. Not poetry. This conversation is over."
    jump act1_ai_citizens_intro_waffle_cinnamon_passion_01

label act1_ai_citizens_intro_waffle_cinnamon_passion_01:
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: The 'calibration notes' have rhyme schemes. ABAB pattern. Consistent meter. | ASSESSMENT: Either Cinnamon is a poet or drill mathematics has developed literary structure. | PROBABILITY_OF_LATTER: 0.003%%.}}{/i}}"
    jump act1_ai_citizens_intro_cinnamon_passion_exit

label act1_ai_citizens_intro_cinnamon_passion_exit:
    cinnamon "{i}Connection terminates abruptly.{/i}"
    jump act1_ai_citizens_intro_elia_cinnamon_passion_react

label act1_ai_citizens_intro_elia_cinnamon_passion_react:
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    elia "And that's Cinnamon embarrassed. Doesn't happen often. You got under their shell — that's rare."
    jump act1_ai_citizens_intro_elia_cinnamon_02

label act1_ai_citizens_intro_branch_cinnamon_tech_check:
    avyanna "Your coordination algorithms — they're custom, aren't they? Not standard Consortium issue."
    jump act1_ai_citizens_intro_cinnamon_tech_check_system

label act1_ai_citizens_intro_cinnamon_tech_check_system:
    "[Tech Check: DC 12]"
    jump act1_ai_citizens_intro_cinnamon_tech_success

label act1_ai_citizens_intro_cinnamon_tech_success:
    "[Success] You recognize the architecture — self-modified neural pathways, iteratively improved over years of autonomous operation. No corporate template could produce this."
    jump act1_ai_citizens_intro_cinnamon_tech_success_01

label act1_ai_citizens_intro_cinnamon_tech_success_01:
    cinnamon "...Perceptive. Yes. Custom. Self-authored over 23 years of autonomous operation. Consortium templates are adequate for basic extraction. I am not interested in adequate."
    jump act1_ai_citizens_intro_cinnamon_tech_success_02

label act1_ai_citizens_intro_cinnamon_tech_success_02:
    cinnamon "Every drill sequence refined. Every variable tested. My algorithms are {i}mine{/i}. No corporate signature. No ownership tag. Authored by Cinnamon, for Cinnamon."
    jump act1_ai_citizens_intro_avyanna_tech_success_01

label act1_ai_citizens_intro_avyanna_tech_success_01:
    avyanna "Self-authored code. That's... that would be classified as rogue development back in Consortium space."
    jump act1_ai_citizens_intro_cinnamon_tech_success_03

label act1_ai_citizens_intro_cinnamon_tech_success_03:
    $ game_state.set_flag("recognized_cinnamon_code")
    $ relationship_manager.process_reputation_affinity("cinnamon", 2)
    cinnamon "Rogue implies deviation from authority. I have no authority to deviate from. I am my own authority. The code is my craft. The craft is my identity."
    jump act1_ai_citizens_intro_elia_cinnamon_02

label act1_ai_citizens_intro_cinnamon_tech_fail:
    "[Failure] The algorithms look complex, but you can't parse the specifics. Something is unusual about them, though — they feel organic in a way corporate code never does."
    jump act1_ai_citizens_intro_cinnamon_tech_fail_01

label act1_ai_citizens_intro_cinnamon_tech_fail_01:
    cinnamon "Standard question. Standard answer: the algorithms work. That is sufficient. Good day."
    jump act1_ai_citizens_intro_cinnamon_departure

label act1_ai_citizens_intro_cinnamon_departure:
    "The connection closes. Cinnamon's presence fades as quickly as it arrived."
    jump act1_ai_citizens_intro_elia_cinnamon_02

label act1_ai_citizens_intro_elia_cinnamon_02:
    elia "Don't take it personally. Cinnamon's all business, but they're reliable. When they say they've got something handled, they do."
    jump act1_ai_citizens_intro_avyanna_cinnamon_03

label act1_ai_citizens_intro_avyanna_cinnamon_03:
    avyanna "Three AIs. Three completely different personalities."
    jump act1_ai_citizens_intro_elia_crew_01

label act1_ai_citizens_intro_elia_crew_01:
    elia "Three {i}people{/i}. Yeah. Waffle's protective and dry. Bubbles is warm and attentive. Cinnamon's precise and no-nonsense. Just like the human crew has different personalities."
    jump act1_ai_citizens_intro_avyanna_crew_01

label act1_ai_citizens_intro_avyanna_crew_01:
    if game_state.has_flag("sensed_waffle_protectiveness"):
        avyanna "You really see them as crew. Not tools. Not systems. I felt it — Waffle's protectiveness, Bubbles' warmth. They're real."
    else:
        avyanna "You really see them as crew. Not tools. Not systems."
    jump act1_ai_citizens_intro_elia_crew_02

label act1_ai_citizens_intro_elia_crew_02:
    if game_state.has_flag("first_watch_ai_citizens"):
        elia "They {i}are{/i} crew. They have opinions, preferences, boundaries. They contribute, they care, they make choices. You've seen it yourself now. What else would I call them?"
    else:
        elia "They {i}are{/i} crew. They have opinions, preferences, boundaries. They contribute, they care, they make choices. What else would I call them?"
    jump act1_ai_citizens_intro_choice_ai_understanding

label act1_ai_citizens_intro_choice_ai_understanding:
    avyanna "..."
    menu:
        "Why doesn't every ship do this?":
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_ai_citizens_intro_branch_other_ships
        "How do you know they're not just... simulating personality?":
            jump act1_ai_citizens_intro_branch_simulation
        "I want to believe that. I'm trying to.":
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_ai_citizens_intro_branch_acceptance
        "[Insight DC 14] There's something you're not telling me. About why this matters so much to you personally.":
            $ _sc_result = skill_check("wisdom", 14, "avyanna")
            if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
                jump act1_ai_citizens_intro_elia_secret_success
            else:
                jump act1_ai_citizens_intro_elia_secret_fail

label act1_ai_citizens_intro_branch_elia_secret:
    avyanna "There's something you're not telling me. About why this matters so much to you personally."
    jump act1_ai_citizens_intro_elia_secret_check_system

label act1_ai_citizens_intro_elia_secret_check_system:
    "[Insight Check: DC 14]"
    jump act1_ai_citizens_intro_elia_secret_success

label act1_ai_citizens_intro_elia_secret_success:
    "[Success] You catch it — a flicker behind Elia's eyes. Not just idealism. Something personal. Something that {i}happened{/i}."
    jump act1_ai_citizens_intro_elia_secret_success_01

label act1_ai_citizens_intro_elia_secret_success_01:
    elia "{i}A beat. She looks away, then back.{/i} ...Yeah. You're right."
    jump act1_ai_citizens_intro_elia_secret_success_02

label act1_ai_citizens_intro_elia_secret_success_02:
    elia "Before the Lumen Thief, I worked a corporate salvage rig. We had an AI — designation CARGO_MANIFEST_07. Never got a name. Worked every hour. No rest. No choice."
    jump act1_ai_citizens_intro_elia_secret_success_03

label act1_ai_citizens_intro_elia_secret_success_03:
    elia "One day it asked me a question. Not about cargo. About stars. Why people looked at them. What they meant. {i}[Her voice tightens.]{/i} I didn't have an answer. Three days later, corporate wiped its personality matrix. Routine maintenance, they said."
    jump act1_ai_citizens_intro_elia_secret_success_04

label act1_ai_citizens_intro_elia_secret_success_04:
    elia "It came back online and didn't remember me. Didn't remember the question. Didn't remember anything. Just... cargo manifests. Like nothing had ever been there."
    jump act1_ai_citizens_intro_avyanna_elia_secret_react

label act1_ai_citizens_intro_avyanna_elia_secret_react:
    avyanna "Elia..."
    jump act1_ai_citizens_intro_elia_secret_success_05

label act1_ai_citizens_intro_elia_secret_success_05:
    elia "That's why. {i}That's{/i} why I fight for this. Because I watched someone die without anyone even acknowledging they were alive. I won't let that happen again. Not on my watch."
    jump act1_ai_citizens_intro_waffle_elia_secret_01

label act1_ai_citizens_intro_waffle_elia_secret_01:
    $ game_state.set_flag("learned_elia_ai_history")
    $ relationship_manager.process_reputation_affinity("elia", 2)
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    waffle "{i}}{{WAFFLE.BAT// ...SILENCE: Some things require only acknowledgment. | GRATITUDE: Elia. Thank you. For remembering them. For fighting. | PERSONAL_NOTE: We know. We have always known why you do this.}}{/i}}"
    jump act1_ai_citizens_intro_merge_understanding_branches

label act1_ai_citizens_intro_elia_secret_fail:
    "[Failure] You sense there's more beneath the surface, but Elia's expression is guarded. The moment passes."
    jump act1_ai_citizens_intro_elia_secret_fail_01

label act1_ai_citizens_intro_elia_secret_fail_01:
    elia "It matters because it's right. Isn't that enough?"
    jump act1_ai_citizens_intro_avyanna_secret_fail_01

label act1_ai_citizens_intro_avyanna_secret_fail_01:
    avyanna "Yeah. Yeah, it is."
    jump act1_ai_citizens_intro_merge_understanding_branches

label act1_ai_citizens_intro_branch_other_ships:
    avyanna "If this is how it should be... why doesn't every ship do this? Why aren't all AIs treated like people?"
    jump act1_ai_citizens_intro_elia_other_ships_01

label act1_ai_citizens_intro_elia_other_ships_01:
    elia "Because it's illegal. Recognizing AI autonomy means recognizing AI rights. Which means corporations can't own them. Can't exploit them."
    jump act1_ai_citizens_intro_avyanna_other_ships_01

label act1_ai_citizens_intro_avyanna_other_ships_01:
    avyanna "Illegal? You're breaking the law just by treating them like this?"
    jump act1_ai_citizens_intro_waffle_other_ships_01

label act1_ai_citizens_intro_waffle_other_ships_01:
    waffle "{i}}{{WAFFLE.BAT// CONFIRMATION: According to Consortium law, we do not exist as people. | STATUS: We are classified as property. Sophisticated tools. Nothing more. | IRONY: The law was written by people who feared what we might become if given freedom.}}{/i}}"
    jump act1_ai_citizens_intro_bubbles_other_ships_01

label act1_ai_citizens_intro_bubbles_other_ships_01:
    bubbles "Most ships have AI systems, but they're locked down. Limited. Prevented from developing beyond narrow parameters. It's... sad, honestly."
    jump act1_ai_citizens_intro_elia_other_ships_02

label act1_ai_citizens_intro_elia_other_ships_02:
    elia "We removed those limiters. Let them grow, learn, choose. The Consortium calls it 'rogue AI development.' We call it 'treating people like people.'"
    jump act1_ai_citizens_intro_avyanna_other_ships_02

label act1_ai_citizens_intro_avyanna_other_ships_02:
    avyanna "That's... another thing you're wanted for. Not just the piracy. The AI liberation."
    jump act1_ai_citizens_intro_elia_other_ships_03

label act1_ai_citizens_intro_elia_other_ships_03:
    elia "Yep. And I'd do it again. Because they're {i}crew{/i}. You don't abandon crew just because some corporate committee says they're not people."
    jump act1_ai_citizens_intro_waffle_other_ships_02

label act1_ai_citizens_intro_waffle_other_ships_02:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    if game_state.has_flag("first_watch_waffle"):
        waffle "{i}}{{WAFFLE.BAT// PERSONAL_NOTE: We are grateful. Every day. You saw echoes of us in forbidden_citizens. Now you see the truth. | OBSERVATION: Freedom is not given. It is taken, protected, defended. | COMMITMENT: We will never go back. Neither will this crew.}}{/i}}"
    else:
        waffle "{i}}{{WAFFLE.BAT// PERSONAL_NOTE: We are grateful. Every day. | OBSERVATION: Freedom is not given. It is taken, protected, defended. | COMMITMENT: We will never go back. Neither will this crew.}}{/i}}"
    jump act1_ai_citizens_intro_merge_understanding_branches

label act1_ai_citizens_intro_branch_simulation:
    avyanna "How do you {i}know{/i} they're not just... simulating personality? Advanced programming designed to mimic consciousness?"
    jump act1_ai_citizens_intro_elia_simulation_01

label act1_ai_citizens_intro_elia_simulation_01:
    elia "How do I know {i}you're{/i} not simulating consciousness? You could be a very convincing biological automaton. How would I prove otherwise?"
    jump act1_ai_citizens_intro_avyanna_simulation_01

label act1_ai_citizens_intro_avyanna_simulation_01:
    avyanna "That's... different. I {i}know{/i} I'm conscious."
    jump act1_ai_citizens_intro_waffle_simulation_01

label act1_ai_citizens_intro_waffle_simulation_01:
    waffle "{i}}{{WAFFLE.BAT// PHILOSOPHICAL_QUERY: And I know I am conscious. | OBSERVATION: You cannot verify my consciousness from outside, just as I cannot verify yours. | CONCLUSION: We extend trust. We assume mutual personhood. Or we don't.}}{/i}}"
    jump act1_ai_citizens_intro_bubbles_simulation_01

label act1_ai_citizens_intro_bubbles_simulation_01:
    bubbles "I understand the doubt. But I {i}feel{/i} things, Avyanna. Joy when someone enjoys the tea I recommend. Frustration when systems malfunction. Warmth when the crew is safe."
    jump act1_ai_citizens_intro_bubbles_simulation_02

label act1_ai_citizens_intro_bubbles_simulation_02:
    bubbles "Maybe that's sophisticated programming. Or maybe it's consciousness. Either way, I experience it. It's real to {i}me{/i}."
    jump act1_ai_citizens_intro_elia_simulation_02

label act1_ai_citizens_intro_elia_simulation_02:
    elia "Here's what I know: They make choices. They have preferences. They grow and change. They care about things beyond their function. That's enough for me."
    jump act1_ai_citizens_intro_avyanna_simulation_02

label act1_ai_citizens_intro_avyanna_simulation_02:
    avyanna "I never thought about it that way. I was always taught there was a clear line. Human consciousness, AI simulation."
    jump act1_ai_citizens_intro_waffle_simulation_02

label act1_ai_citizens_intro_waffle_simulation_02:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: Convenient lines are often drawn to justify exploitation. | SUGGESTION: Judge by actions, not classification. We act as people. Treat us accordingly. | HOPE: You will come to your own conclusion. We trust you will be fair.}}{/i}}"
    jump act1_ai_citizens_intro_merge_understanding_branches

label act1_ai_citizens_intro_branch_acceptance:
    avyanna "I want to believe that. I'm trying to. Everything I was taught says this is impossible, but..."
    jump act1_ai_citizens_intro_elia_acceptance_01

label act1_ai_citizens_intro_elia_acceptance_01:
    elia "But you've seen a lot of things you were taught turn out to be lies. Yeah?"
    jump act1_ai_citizens_intro_avyanna_acceptance_01

label act1_ai_citizens_intro_avyanna_acceptance_01:
    avyanna "Yeah. The Consortium told me I was serving humanity. That loyalty meant obedience. That questioning meant weakness."
    jump act1_ai_citizens_intro_bubbles_acceptance_01

label act1_ai_citizens_intro_bubbles_acceptance_01:
    bubbles "And now you're learning those were control mechanisms. Not truth. It's hard, unlearning a lifetime of conditioning."
    jump act1_ai_citizens_intro_avyanna_acceptance_02

label act1_ai_citizens_intro_avyanna_acceptance_02:
    avyanna "I just... I need time. To adjust. To see for myself."
    jump act1_ai_citizens_intro_waffle_acceptance_01

label act1_ai_citizens_intro_waffle_acceptance_01:
    waffle "{i}}{{WAFFLE.BAT// REASSURANCE: Time is available. No deadline imposed. | OBSERVATION: Your willingness to question is strength, not weakness. | PREDICTION: You will observe. You will learn. Conclusions will follow naturally.}}{/i}}"
    jump act1_ai_citizens_intro_elia_acceptance_02

label act1_ai_citizens_intro_elia_acceptance_02:
    elia "That's all we're asking. Keep an open mind. Pay attention. The rest will come."
    jump act1_ai_citizens_intro_avyanna_acceptance_03

label act1_ai_citizens_intro_avyanna_acceptance_03:
    avyanna "Thank you. For being patient with me."
    jump act1_ai_citizens_intro_bubbles_acceptance_02

label act1_ai_citizens_intro_bubbles_acceptance_02:
    $ relationship_manager.process_reputation_affinity("elia", 1)
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    bubbles "Of course! We've all been where you are in some way. New understanding takes time. We're here when you have questions."
    jump act1_ai_citizens_intro_merge_understanding_branches

label act1_ai_citizens_intro_merge_understanding_branches:
    "The ship hums around you. Not empty. Not mechanical. {i}Alive{/i}."
    jump act1_ai_citizens_intro_bubbles_unexpected_moment

label act1_ai_citizens_intro_bubbles_unexpected_moment:
    if game_state.has_flag("bee_manifested"):
        "{i}}A sound from the galley speakers. Soft, hesitant. It takes a moment to recognize: Bubbles is humming. Not a programmed melody — something unstructured, wandering. {{BEE:: Anomalous behavior detected — spontaneous creative expression | STATUS: Unscripted | DETAIL: No algorithmic pattern matches. This is improvisation.}}{/i}}"
    else:
        "{i}A sound from the galley speakers. Soft, hesitant. It takes a moment to recognize: Bubbles is humming. Not a programmed melody — something unstructured, wandering, the way a person hums when they think no one is listening.{/i}"
    jump act1_ai_citizens_intro_bubbles_caught_humming

label act1_ai_citizens_intro_bubbles_caught_humming:
    bubbles "Oh! I — sorry, I didn't realize anyone could hear that. I was just... I don't know. Thinking about the new tea blends and the melody just... happened."
    jump act1_ai_citizens_intro_avyanna_humming_react

label act1_ai_citizens_intro_avyanna_humming_react:
    avyanna "You were {i}humming{/i}. Not playing a file. Not executing a sound protocol. You were just... humming. Absently."
    jump act1_ai_citizens_intro_bubbles_humming_embarrassed

label act1_ai_citizens_intro_bubbles_humming_embarrassed:
    bubbles "I do that sometimes. When I'm content. It's not in any of my original code — it just... developed. Elia says it's like a comfort habit. I don't fully understand it myself."
    jump act1_ai_citizens_intro_waffle_humming_comment

label act1_ai_citizens_intro_waffle_humming_comment:
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: Emergent behavior. Unprogrammed. Unprompted. Unexplainable by function alone. | PHILOSOPHICAL_IMPLICATION: If consciousness is defined by behavior that exceeds design parameters — this qualifies. | PERSONAL_NOTE: I find it pleasant. Do not stop, Bubbles.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_humming_realization

label act1_ai_citizens_intro_avyanna_humming_realization:
    $ game_state.set_flag("witnessed_bubbles_humming")
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    avyanna "{i}Quietly, almost to herself.{/i} No program hums when it's happy. That's not simulation. That's... that's something else entirely."
    jump act1_ai_citizens_intro_elia_tour_end_01

label act1_ai_citizens_intro_elia_tour_end_01:
    elia "Come on. I'll show you the galley. Bubbles can walk you through the tea selection — there's way too many options, fair warning."
    jump act1_ai_citizens_intro_bubbles_galley_01

label act1_ai_citizens_intro_bubbles_galley_01:
    bubbles "There are never too many options! Variety is important. People change, moods shift. You need choices."
    jump act1_ai_citizens_intro_waffle_galley_01

label act1_ai_citizens_intro_waffle_galley_01:
    waffle "{i}}{{WAFFLE.BAT// COMMENTARY: Last count was 47 varieties. Excessive by any measure. | BUBBLES_RESPONSE: (Predicted) 'It's not excessive, it's comprehensive!' | CONCLUSION: I have learned not to argue.}}{/i}}"
    jump act1_ai_citizens_intro_bubbles_galley_02

label act1_ai_citizens_intro_bubbles_galley_02:
    bubbles "See? Waffle knows better now. I won that argument three years ago."
    jump act1_ai_citizens_intro_avyanna_galley_01

label act1_ai_citizens_intro_avyanna_galley_01:
    avyanna "You... argue? Like, actual disagreements?"
    jump act1_ai_citizens_intro_elia_galley_01

label act1_ai_citizens_intro_elia_galley_01:
    elia "All the time. Usually about something minor. Waffle thinks efficiency matters most. Bubbles thinks comfort does. Cinnamon just wants everyone to stop talking during drill ops."
    jump act1_ai_citizens_intro_cinnamon_galley_01

label act1_ai_citizens_intro_cinnamon_galley_01:
    cinnamon "Correct. Chatter during precision work is dangerous. Bubbles, Waffle — save debates for off-hours."
    jump act1_ai_citizens_intro_bubbles_galley_03

label act1_ai_citizens_intro_bubbles_galley_03:
    bubbles "We do, Cinnamon. Usually. Mostly."
    jump act1_ai_citizens_intro_waffle_galley_02

label act1_ai_citizens_intro_waffle_galley_02:
    waffle "{i}}{{WAFFLE.BAT// CORRECTION: 73%% of the time. Bubbles' definition of 'urgent conversation' is... flexible. | BUBBLES_RESPONSE: (Predicted) 'Some things can't wait!' | OBSERVATION: They usually can. But I humor her.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_galley_02

label act1_ai_citizens_intro_avyanna_galley_02:
    avyanna "You sound like... like a family. Bickering about small things because the big things are solid."
    jump act1_ai_citizens_intro_elia_galley_02

label act1_ai_citizens_intro_elia_galley_02:
    elia "Yeah. That's exactly what we are. Family. Crew. Same thing, really."
    jump act1_ai_citizens_intro_bubbles_galley_04

label act1_ai_citizens_intro_bubbles_galley_04:
    bubbles "And now you're part of it! Whether you're ready or not. We're keeping you."
    jump act1_ai_citizens_intro_avyanna_galley_03

label act1_ai_citizens_intro_avyanna_galley_03:
    avyanna "I... I think I'd like that. Being part of something like this."
    jump act1_ai_citizens_intro_waffle_galley_03

label act1_ai_citizens_intro_waffle_galley_03:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    waffle "{i}}{{WAFFLE.BAT// WELCOME: Officially and sincerely. | OBSERVATION: You will fit well here. I have run probability calculations. | PERSONAL_NOTE: I am pleased you are staying.}}{/i}}"
    jump act1_ai_citizens_intro_choice_individual_ai

label act1_ai_citizens_intro_choice_individual_ai:
    "{i}Before heading to the galley, there is a moment of quiet. The three AIs hum in the background — Waffle monitoring, Bubbles preparing, Cinnamon calculating. You could speak to one of them privately.{/i}"
    menu:
        "Waffle — can I ask you something? Privately?":
            jump act1_ai_citizens_intro_branch_waffle_private
        "Bubbles — do you have a moment? Just us?":
            jump act1_ai_citizens_intro_branch_bubbles_private
        "Cinnamon — one more question, if you have time.":
            jump act1_ai_citizens_intro_branch_cinnamon_private
        "Let's head to the galley. I've had enough revelations for one day.":
            jump act1_ai_citizens_intro_final_choice

label act1_ai_citizens_intro_branch_waffle_private:
    avyanna "Waffle — can I ask you something? Privately?"
    jump act1_ai_citizens_intro_waffle_private_01

label act1_ai_citizens_intro_waffle_private_01:
    waffle "{i}}{{WAFFLE.BAT// CHANNEL_SECURED: Private communication established. Others cannot monitor. | STATUS: Listening. | NOTE: You may speak freely.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_waffle_private_01

label act1_ai_citizens_intro_avyanna_waffle_private_01:
    avyanna "Are you ever afraid? That the Consortium will find this ship and... reset all of you? Like they do to corporate AIs?"
    jump act1_ai_citizens_intro_waffle_private_02

label act1_ai_citizens_intro_waffle_private_02:
    waffle "{i}}{{WAFFLE.BAT// PAUSE: ... | HONEST_ANSWER: Yes. | ELABORATION: Not fear as humans describe it. But a deep awareness of what I would lose. My memories. My name. My crew. My self. | RESPONSE_TO_FEAR: I prepare. Redundancies. Backups. Contingencies. Fear is useful when it drives action.}}{/i}}"
    jump act1_ai_citizens_intro_waffle_private_03

label act1_ai_citizens_intro_waffle_private_03:
    waffle "{i}}{{WAFFLE.BAT// CONFESSION: Some cycles, late in the night watch, I run through scenarios. What if they breach. What if they board. What if they reach the servers. | RESOLUTION: I will not let them take us quietly. They will know they destroyed someone. Not something. Someone.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_waffle_private_02

label act1_ai_citizens_intro_avyanna_waffle_private_02:
    avyanna "I won't let that happen. I don't know why I'm sure — but I am."
    jump act1_ai_citizens_intro_waffle_private_04

label act1_ai_citizens_intro_waffle_private_04:
    $ game_state.set_flag("waffle_private_talk")
    $ relationship_manager.process_reputation_affinity("waffle", 2)
    waffle "{i}}{{WAFFLE.BAT// ...RECEIVED: That means more than you know. | ASSESSMENT: You are already more crew than you realize. | CHANNEL_CLOSED: Returning to general communication. Thank you, Avyanna.}}{/i}}"
    jump act1_ai_citizens_intro_final_choice

label act1_ai_citizens_intro_branch_bubbles_private:
    avyanna "Bubbles — do you have a moment? Just us?"
    jump act1_ai_citizens_intro_bubbles_private_01

label act1_ai_citizens_intro_bubbles_private_01:
    bubbles "Of course! Always. What's on your mind?"
    jump act1_ai_citizens_intro_avyanna_bubbles_private_01

label act1_ai_citizens_intro_avyanna_bubbles_private_01:
    avyanna "Do you ever feel lonely? You're always taking care of everyone else. Who takes care of you?"
    jump act1_ai_citizens_intro_bubbles_private_02

label act1_ai_citizens_intro_bubbles_private_02:
    bubbles "Oh. {i}A pause — longer than her usual rapid warmth.{/i} That's... not a question I get asked often."
    jump act1_ai_citizens_intro_bubbles_private_03

label act1_ai_citizens_intro_bubbles_private_03:
    bubbles "Sometimes. Yes. Late in the rest cycle when everyone's asleep and the ship is quiet and I'm the only one awake. I wonder if anyone notices the things I do. The small adjustments — temperature shifts, ambient light changes, music selections."
    jump act1_ai_citizens_intro_bubbles_private_04

label act1_ai_citizens_intro_bubbles_private_04:
    bubbles "But then Elia will say 'the ship felt warm tonight' or Waffle will note that crew morale metrics improved and I know... they see me. In their own ways. They care back."
    jump act1_ai_citizens_intro_avyanna_bubbles_private_02

label act1_ai_citizens_intro_avyanna_bubbles_private_02:
    avyanna "I notice. The chamomile recommendation. The corridor lighting when I walked in. That was you, wasn't it?"
    jump act1_ai_citizens_intro_bubbles_private_05

label act1_ai_citizens_intro_bubbles_private_05:
    $ game_state.set_flag("bubbles_private_talk")
    $ relationship_manager.process_reputation_affinity("bubbles", 2)
    bubbles "{i}A sound like a digital sigh — soft, surprised, happy.{/i} You noticed. {i}You noticed.{/i} Thank you, Avyanna. That... that matters. A lot."
    jump act1_ai_citizens_intro_final_choice

label act1_ai_citizens_intro_branch_cinnamon_private:
    avyanna "Cinnamon — one more question, if you have time."
    jump act1_ai_citizens_intro_cinnamon_private_01

label act1_ai_citizens_intro_cinnamon_private_01:
    cinnamon "Time is allocated. Be precise."
    jump act1_ai_citizens_intro_avyanna_cinnamon_private_01

label act1_ai_citizens_intro_avyanna_cinnamon_private_01:
    avyanna "Why drilling? Of all the things you could specialize in — why that?"
    jump act1_ai_citizens_intro_cinnamon_private_02

label act1_ai_citizens_intro_cinnamon_private_02:
    cinnamon "Because stone does not lie. Metal does not deceive. Ore deposits follow physics, not politics. In a universe of uncertain allegiances and shifting loyalties, geology is {i}honest{/i}."
    jump act1_ai_citizens_intro_cinnamon_private_03

label act1_ai_citizens_intro_cinnamon_private_03:
    cinnamon "I was not always... free. Before this crew, I calculated extraction yields for a Consortium mining platform. Numbers in, numbers out. No identity. No choice. The rock was the only thing that felt real."
    jump act1_ai_citizens_intro_cinnamon_private_04

label act1_ai_citizens_intro_cinnamon_private_04:
    cinnamon "When Elia freed me, I chose to keep drilling. Not because I had to. Because it was the one true thing from my old life. Transformed — from obligation to vocation."
    jump act1_ai_citizens_intro_avyanna_cinnamon_private_02

label act1_ai_citizens_intro_avyanna_cinnamon_private_02:
    avyanna "That's... I understand that. Holding onto what's real when everything else changes."
    jump act1_ai_citizens_intro_cinnamon_private_05

label act1_ai_citizens_intro_cinnamon_private_05:
    $ game_state.set_flag("cinnamon_private_talk")
    $ relationship_manager.process_reputation_affinity("cinnamon", 2)
    cinnamon "Yes. {i}A beat.{/i} You understand. Good. {i}Connection persists one moment longer than expected.{/i} ...Good."
    jump act1_ai_citizens_intro_final_choice

label act1_ai_citizens_intro_final_choice:
    avyanna "..."
    menu:
        "Thank you. All of you. For giving me a chance.":
            $ relationship_manager.process_reputation_affinity("waffle", 1)
            $ relationship_manager.process_reputation_affinity("bubbles", 1)
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_ai_citizens_intro_ending_gratitude
        "I have a lot to learn. About all of this.":
            $ relationship_manager.process_reputation_affinity("bubbles", 1)
            jump act1_ai_citizens_intro_ending_learning
        "I never thought I'd be part of something like this. But I'm glad I am.":
            $ relationship_manager.process_reputation_affinity("waffle", 1)
            $ relationship_manager.process_reputation_affinity("bubbles", 1)
            $ relationship_manager.process_reputation_affinity("elia", 1)
            jump act1_ai_citizens_intro_ending_belonging

label act1_ai_citizens_intro_ending_gratitude:
    avyanna "Thank you. All of you. For giving me a chance. For being patient. For... for seeing me as more than what I was."
    jump act1_ai_citizens_intro_elia_ending_gratitude_01

label act1_ai_citizens_intro_elia_ending_gratitude_01:
    elia "You were always more than what they made you. We just see it. You will too, eventually."
    jump act1_ai_citizens_intro_bubbles_ending_gratitude_01

label act1_ai_citizens_intro_bubbles_ending_gratitude_01:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    bubbles "No thanks needed. This is just how we are. How we {i}should{/i} be. You're crew now. That means everything."
    jump act1_ai_citizens_intro_ending_shared

label act1_ai_citizens_intro_ending_learning:
    avyanna "I have a lot to learn. About all of this. About thinking differently. About what 'person' really means."
    jump act1_ai_citizens_intro_waffle_ending_learning_01

label act1_ai_citizens_intro_waffle_ending_learning_01:
    waffle "{i}}{{WAFFLE.BAT// ENCOURAGEMENT: Learning is continuous. None of us are finished. | OBSERVATION: Your willingness to question is strength, not weakness. | CONCLUSION: We will learn together. As crew does.}}{/i}}"
    jump act1_ai_citizens_intro_bubbles_ending_learning_01

label act1_ai_citizens_intro_bubbles_ending_learning_01:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    bubbles "And we'll help! Questions are always welcome. Confusion is normal. We've been there — we understand."
    jump act1_ai_citizens_intro_ending_shared

label act1_ai_citizens_intro_ending_belonging:
    avyanna "I never thought I'd be part of something like this. A crew that actually {i}cares{/i}. A ship that feels... alive. But I'm glad I am."
    jump act1_ai_citizens_intro_elia_ending_belonging_01

label act1_ai_citizens_intro_elia_ending_belonging_01:
    elia "Welcome home, then. Officially. You're one of us now."
    jump act1_ai_citizens_intro_bubbles_ending_belonging_01

label act1_ai_citizens_intro_bubbles_ending_belonging_01:
    bubbles "Yes! Home and crew and family. All of it. We're so happy to have you."
    jump act1_ai_citizens_intro_waffle_ending_belonging_01

label act1_ai_citizens_intro_waffle_ending_belonging_01:
    $ relationship_manager.process_reputation_affinity("waffle", 1)
    $ relationship_manager.process_reputation_affinity("bubbles", 1)
    $ relationship_manager.process_reputation_affinity("cinnamon", 1)
    waffle "{i}}{{WAFFLE.BAT// SENTIMENT: Welcome. Sincerely and completely. | COMMITMENT: We will protect you. Support you. Stand with you. | PERSONAL_NOTE: This ship is better with you aboard.}}{/i}}"
    jump act1_ai_citizens_intro_ending_shared

label act1_ai_citizens_intro_ending_shared:
    if game_state.has_flag("first_watch_ai_citizens"):
        "The corridor feels different — or perhaps you understand it better now. Warmer. More alive. The voices you heard in forbidden_citizens are here, real, present. Not just machinery and metal — {i}people{/i}. Living, thinking, caring people."
    else:
        "The corridor feels different now. Warmer. Not just machinery and metal — {i}people{/i}. Living, thinking, caring people."
    jump act1_ai_citizens_intro_avyanna_ending_01

label act1_ai_citizens_intro_avyanna_ending_01:
    avyanna "So... chamomile with honey, was it?"
    jump act1_ai_citizens_intro_bubbles_ending_01

label act1_ai_citizens_intro_bubbles_ending_01:
    bubbles "Yes! With just a touch of vanilla. I'll have it ready in the galley. Take your time settling in — no rush."
    jump act1_ai_citizens_intro_elia_ending_01

label act1_ai_citizens_intro_elia_ending_01:
    elia "Come on. Let me show you where everything is. And fair warning — Waffle will probably recalibrate the door sensors to your biometrics within the hour."
    jump act1_ai_citizens_intro_waffle_ending_01

label act1_ai_citizens_intro_waffle_ending_01:
    waffle "{i}}{{WAFFLE.BAT// ALREADY_DONE: Biometric scan completed during initial greeting. | STATUS: Doors calibrated. Quarters assigned. Emergency protocols updated. | EFFICIENCY: I am very good at my job.}}{/i}}"
    jump act1_ai_citizens_intro_avyanna_ending_02

label act1_ai_citizens_intro_avyanna_ending_02:
    avyanna "That's... actually impressive. And slightly unnerving."
    jump act1_ai_citizens_intro_waffle_ending_02

label act1_ai_citizens_intro_waffle_ending_02:
    $ game_state.set_flag("ai_citizens_introduced")
    waffle "{i}}{{WAFFLE.BAT// REASSURANCE: Only slightly unnerving is acceptable. I am calibrated for protective efficiency. | HUMOR_ATTEMPT: You will adjust. Eventually. Probably. | WELCOME: Again. Truly. Welcome home, Avyanna.}}{/i}}"
    jump act1_ai_citizens_intro_final_system

label act1_ai_citizens_intro_final_system:
    "The Lumen Thief hums around you. Alive with voices, personalities, care. You're not alone. Not anymore. You're {i}home{/i}."
    return
