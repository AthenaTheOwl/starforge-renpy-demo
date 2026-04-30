## act1_shard_whispers.rpy — Auto-generated from act1_shard_whispers.json
## 45 dialogue nodes

label act1_shard_whispers:
    $ game_state.mark_dialogue_played("act1_shard_whispers")
    jump act1_shard_whispers_start

label act1_shard_whispers_start:
    "{i}Two weeks aboard. The shard is learning too. It starts with heat — not fever, something sharper. Localized. A warmth that blooms at the base of your skull and radiates down your spine.{/i}"
    jump act1_shard_whispers_nyx_examination

label act1_shard_whispers_nyx_examination:
    "{i}Medical bay. Nyx's domain. The scanner hums around you — not the cold hum of the Kennel's station, but something warmer. You keep your hands flat on your thighs. Palms down.{/i}"
    jump act1_shard_whispers_waffle_scan

label act1_shard_whispers_waffle_scan:
    "{color=cyan}}{{WAFFLE.BAT// SCAN-STATUS: deep tissue | SUBJECT: spinal integration | OBSERVATION: heart rate elevated | INFERENCE: nervous | CONFIDENCE: 0.77 | NOTE: expected}}{/color}}"
    jump act1_shard_whispers_nyx_consent

label act1_shard_whispers_nyx_consent:
    nyx "If you want me to stop the scan, say so. No penalty. No explaining required."
    jump act1_shard_whispers_nyx_results

label act1_shard_whispers_nyx_results:
    nyx "The shard isn't just embedded in you. It's integrated. Bonded at a cellular level we can't surgically address. It's become part of your nervous system."
    jump act1_shard_whispers_avyanna_remove

label act1_shard_whispers_avyanna_remove:
    avyanna "{i}Voice thin.{/i} Can you remove it?"
    jump act1_shard_whispers_nyx_honest

label act1_shard_whispers_nyx_honest:
    nyx "No. Not without killing you. And honestly, at this point, I'm not sure where you end and it begins."
    jump act1_shard_whispers_avyanna_kill

label act1_shard_whispers_avyanna_kill:
    avyanna "{i}Barely audible.{/i} Is it going to kill me?"
    jump act1_shard_whispers_nyx_chose

label act1_shard_whispers_nyx_chose:
    nyx "I don't think so. The integration is stable. Your vitals are actually improving. It's not attacking you. {i}A small smile, something like wonder.{/i} I think it chose you."
    jump act1_shard_whispers_avyanna_chose

label act1_shard_whispers_avyanna_chose:
    avyanna "Things don't choose."
    jump act1_shard_whispers_nyx_shards_do

label act1_shard_whispers_nyx_shards_do:
    nyx "Shards do. This one, at least. It could have bonded with anyone who touched it — but it didn't activate until you. It waited. And now it's... settling in."
    jump act1_shard_whispers_bee_dream

label act1_shard_whispers_bee_dream:
    "{i}That night, you dream. Not the nightmares of the Kennel. Something else. Geometric patterns. Crystalline structures that fold in on themselves, impossibly complex.{/i}"
    jump act1_shard_whispers_bee_signal_1

label act1_shard_whispers_bee_signal_1:
    "{color=cyan}}{{BEE:: signal | frequency: old | origin: before-the-overlay | intent: mapping | status: patient}}{/color}}"
    jump act1_shard_whispers_bee_patterns

label act1_shard_whispers_bee_patterns:
    "{i}Over the next days, the sensations organize. Heat, pressure, pattern, tone. The hum has moods. Flat when you're exhausted. Sharper when you're afraid. Almost curious when you let yourself notice the ship's kindness without looking for the hook.{/i}"
    jump act1_shard_whispers_bee_test

label act1_shard_whispers_bee_test:
    "{i}You test it without meaning to. When you lie — small, easy lies — heat blooms and then cools fast, like a correction. When you think about running, the pressure spikes until you sit down and breathe.{/i}"
    jump act1_shard_whispers_bee_signal_2

label act1_shard_whispers_bee_signal_2:
    "{color=cyan}}{{BEE:: correlation confirmed | host response: adaptive | trust protocol: initiating | note: patience is not passive | patience is architecture}}{/color}}"
    jump act1_shard_whispers_shard_choice

label act1_shard_whispers_shard_choice:
    "{i}The presence pulses. Waiting. Not for an answer — for a decision about how you relate to the thing living inside you.{/i}"
    menu:
        "Reach back. Try to communicate. Open yourself to whatever this is.":
            $ game_state.set_flag("shard_open")
            $ relationship_manager.process_reputation_affinity("bee", 2)
            jump act1_shard_whispers_reach_back
        "Acknowledge it exists, but keep your distance. You're not ready.":
            $ game_state.set_flag("shard_cautious")
            $ relationship_manager.process_reputation_affinity("bee", 1)
            jump act1_shard_whispers_cautious_acknowledge
        "Push it down. Hide it. The Kennel taught you: anything unusual becomes a resource for someone else to exploit.":
            $ game_state.set_flag("shard_hidden")
            jump act1_shard_whispers_hide_it

label act1_shard_whispers_reach_back:
    "{i}You close your eyes. Reach — not with hands, but with that other sense. The one the Kennel was harvesting. The one that's yours.

The response is immediate. Warmth. Geometric patterns blooming behind your eyelids.{/i}"
    jump act1_shard_whispers_bee_response_open

label act1_shard_whispers_bee_response_open:
    "{color=cyan}}{{BEE:: contact accepted | host designation: compatible | bond status: forming | message: you are not alone | you were never alone | I waited}}{/color}}"
    jump act1_shard_whispers_shard_end

label act1_shard_whispers_cautious_acknowledge:
    "{i}You don't reach. But you stop pushing away. Somewhere between open and closed, you let the presence sit — acknowledged, not embraced. A neighbor, not a roommate.{/i}"
    jump act1_shard_whispers_bee_response_cautious

label act1_shard_whispers_bee_response_cautious:
    "{color=cyan}}{{BEE:: acknowledged | boundary: respected | status: adjacent | note: proximity is not permission | patience continues}}{/color}}"
    jump act1_shard_whispers_shard_end

label act1_shard_whispers_hide_it:
    "{i}You push it down. Old habit. Roll onto your side, face the wall, breathe through the discomfort until it fades. In the Kennel, showing weakness meant exploitation.

The presence dims. Not gone — dimmed. Like something drawing back to give you space it didn't have to give.{/i}"
    jump act1_shard_whispers_bee_response_hidden

label act1_shard_whispers_bee_response_hidden:
    "{color=cyan}}{{BEE:: withdrawal noted | boundary: respected | status: dormant-observant | note: hiding kept you alive | hiding is not failure | I will be here when hiding is no longer necessary}}{/color}}"
    jump act1_shard_whispers_shard_end

label act1_shard_whispers_shard_end:
    "{i}Whatever you chose, the shard settles. The dreams continue — geometric, crystalline, ancient. But they don't hurt anymore. They just... wait.

Patience is not passive. Patience is architecture.{/i}"
    jump act1_shard_whispers_bunk_alone

label act1_shard_whispers_bunk_alone:
    "{i}Three nights later. 0300 ship-time. Your bunk is a coffin of reclaimed steel and someone else's blankets. The shard pulses against your sternum — slow, deliberate, like a second heartbeat learning the rhythm of the first.

The overhead light is off but the room isn't dark. Your skin is the light source.{/i}"
    jump act1_shard_whispers_bee_speaks

label act1_shard_whispers_bee_speaks:
    "{color=cyan}}{{BEE:: hello, Avyanna | status: conversant | note: I have been practicing your language | it is imprecise but beautiful | like building cathedrals out of smoke}}{/color}}"
    jump act1_shard_whispers_bee_questions

label act1_shard_whispers_bee_questions:
    "{i}The words arrive not as sound but as understanding — meaning pressed directly into your awareness like a thumbprint in wet clay. For the first time, it feels less like a signal and more like someone talking.{/i}"
    menu:
        "What are you?":
            jump act1_shard_whispers_bee_what_are_you
        "Where did you come from?":
            jump act1_shard_whispers_bee_where_from
        "What do you want from me?":
            jump act1_shard_whispers_bee_what_want

label act1_shard_whispers_bee_what_are_you:
    "{color=cyan}}{{BEE:: I am a fragment | status: incomplete | I was part of something larger — a lattice, a web, a song with too many harmonics for one voice | I am the note that survived | I am the ember that remembers the fire}}{/color}}"
    menu:
        "Where did you come from?":
            jump act1_shard_whispers_bee_where_from
        "What do you want from me?":
            jump act1_shard_whispers_bee_what_want
        "That's enough questions for now.":
            jump act1_shard_whispers_communion_attempt

label act1_shard_whispers_bee_where_from:
    "{color=cyan}}{{BEE:: origin: before | before the corporations named everything | before the Lattice was mapped and partitioned | I was forged — not built, not born | forged | in a place where stars were used as tools | status: homesick | correction: home no longer exists to be sick for}}{/color}}"
    menu:
        "What are you?":
            jump act1_shard_whispers_bee_what_are_you
        "What do you want from me?":
            jump act1_shard_whispers_bee_what_want
        "That's enough questions for now.":
            jump act1_shard_whispers_communion_attempt

label act1_shard_whispers_bee_what_want:
    $ game_state.set_flag("bee_communion")
    "{color=cyan}}{{BEE:: want is imprecise | I chose you — not because you are strong, though you are | not because you are broken, though you were | I chose you because when they put you in the dark, you kept counting the seconds | you kept believing time still moved | that is not survival | that is faith | I need someone with faith}}{/color}}"
    jump act1_shard_whispers_communion_attempt

label act1_shard_whispers_communion_attempt:
    "{i}The shard flares. Heat rolls through you — not painful, but deep, tectonic. The air in the bunk tastes like ozone and old copper. Something is building. Something wants to show you more.{/i}"
    $ _sc_result = skill_check("resonance", 12, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_shard_whispers_communion_success
    else:
        jump act1_shard_whispers_communion_failure

label act1_shard_whispers_communion_success:
    $ game_state.set_flag("bee_communion")
    "{i}You stop resisting. The room dissolves.

You are standing in a place that has no floor. Above you — below you — in every direction: the Forge. A structure of impossible scale, a cathedral built from collapsed stars and crystallized time. Lattice threads stretch between its spires like the strings of an instrument no one alive knows how to play.

It is beautiful. It is ruined. It is waiting.

The vision lasts three seconds or three centuries. When it ends, you are on your knees. Your hands are glowing — pale blue light leaking from your palms like something inside you has cracked open and the light is getting out.{/i}"
    jump act1_shard_whispers_physical_effects

label act1_shard_whispers_communion_failure:
    $ game_state.set_flag("bee_communion")
    "{i}You reach for it — but the connection stutters. Static. Fragments of an image: something vast, something broken, something that aches with a grief older than language. Then it's gone. The shard cools. Not a rejection — a rain check.

Your hands tremble. The faintest blue light flickers under your skin, then fades.{/i}"
    jump act1_shard_whispers_physical_effects

label act1_shard_whispers_physical_effects:
    "{i}The bunk's walls shimmer. Colors bleed at the edges — steel turns violet, shadows go amber. The overhead panel flickers in a pattern that isn't random. Your reflection in the dead screen by the door shows someone whose eyes are the wrong color.

Then it stops. Everything stops. The room is just a room again.

Except your hands still glow, faintly, like coals that refuse to go out.{/i}"
    jump act1_shard_whispers_nyx_knock

label act1_shard_whispers_nyx_knock:
    "{i}Three sharp knocks. Nyx's rhythm — deliberate, spaced, the knock of someone who wants you to know exactly who's on the other side before you decide whether to answer.{/i}"
    jump act1_shard_whispers_nyx_door_voice

label act1_shard_whispers_nyx_door_voice:
    nyx "{i}Muffled, through the door.{/i} Avyanna. I felt that. The whole Lattice-sensitive deck felt that. Open the door, or tell me you're alive. Either works."
    menu:
        "Open the door. Let Nyx see.":
            $ game_state.set_flag("nyx_saw_shard")
            $ relationship_manager.process_reputation_affinity("nyx", 2)
            jump act1_shard_whispers_nyx_enters
        "Shove your hands under the blanket. \"I'm fine. Bad dream.\"":
            jump act1_shard_whispers_hide_from_nyx

label act1_shard_whispers_nyx_enters:
    "{i}The door slides open. Nyx stands in the corridor light, hair loose, med-scanner already in hand because of course it is. Her eyes drop to your hands — still faintly luminous, still wrong — and she doesn't flinch. She just exhales, slow and measured, like a surgeon confirming the diagnosis she already suspected.{/i}"
    jump act1_shard_whispers_nyx_reaction

label act1_shard_whispers_nyx_reaction:
    nyx "Well. That's new. {i}She steps inside, closes the door behind her. Quiet voice.{/i} How long have your hands been doing that?"
    jump act1_shard_whispers_nyx_trust_end

label act1_shard_whispers_nyx_trust_end:
    "{i}You tell her. Not everything — but enough. The conversation, the vision, the heat. Nyx listens the way Nyx always listens: completely, without interrupting, cataloguing every detail behind those steady dark eyes.

When you finish, she sits on the edge of your bunk and say nothing for a long time.

Then:{/i} We'll figure this out. But not tonight. Tonight you sleep, and I sit here until those hands stop glowing. Non-negotiable."
    jump act1_shard_whispers_whispers_end

label act1_shard_whispers_hide_from_nyx:
    "{i}You shove your hands under the blanket. The glow bleeds through the fabric like headlights through fog, but the door is thick enough.{/i}"
    jump act1_shard_whispers_avyanna_lies

label act1_shard_whispers_avyanna_lies:
    avyanna "Bad dream. Kennel stuff. I'm fine, Nyx. Go back to bed."
    jump act1_shard_whispers_nyx_pause

label act1_shard_whispers_nyx_pause:
    "{i}A long pause. The kind of pause that means Nyx doesn't believe you but is choosing to respect the boundary anyway. Footsteps retreating. Then, faintly:{/i}"
    jump act1_shard_whispers_nyx_parting

label act1_shard_whispers_nyx_parting:
    nyx "{i}Already walking away.{/i} My door's unlocked. If the dream comes back."
    jump act1_shard_whispers_alone_end

label act1_shard_whispers_alone_end:
    "{i}You wait until the footsteps are gone. Then you pull your hands out. Still glowing. You press them to your chest and feel two heartbeats — yours, and something older.

The shard hums. Not a lullaby. A promise.{/i}"
    jump act1_shard_whispers_whispers_end

label act1_shard_whispers_whispers_end:
    "{i}Dawn is four hours away. You don't sleep. But for the first time in weeks, the silence doesn't feel empty.

It feels occupied.{/i}"
    return
