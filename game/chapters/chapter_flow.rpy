## chapter_flow.rpy — Master chapter sequencer for Starforge Canticles: public Act 1 demo
##
## Orchestrates the released Act 1 chapters (0-20).
## Each chapter: title card -> story scenes (required) -> hub (optional) -> combat -> advance
## Story scenes come from prose_scenes/ (converted from prose markdown)

init python:
    import re as _re

    ## ─────────────────────────────────────────────────────────
    ## Chapter definitions: released Act 1 chapters
    ## ─────────────────────────────────────────────────────────

    CHAPTER_SEQUENCE = {
        # ═══════════════════════════════════════════════════════
        # ACT 1: FOUNDATIONS (Chapters 0-20)
        # ═══════════════════════════════════════════════════════
        0: {
            "title": "Floors, Not Thrones",
            "act": 1,
            "story_scenes": ["act1_00_prologue_floors_not_thrones"],
            "optional_scenes": [],
            "combat": "",
        },
        1: {
            "title": "Cinder Hours",
            "act": 1,
            "story_scenes": ["act1_01_cinder_hours"],
            "optional_scenes": [],
            "combat": "act1_tutorial",
        },
        2: {
            "title": "The Debt Clock",
            "act": 1,
            "story_scenes": ["act1_02_the_debt_clock"],
            "optional_scenes": [],
            "combat": "",
        },
        3: {
            "title": "The Thing in the Rock",
            "act": 1,
            "story_scenes": ["act1_03_the_thing_in_the_rock"],
            "optional_scenes": [],
            "combat": "",
        },
        4: {
            "title": "Contract: Glitter Vein",
            "act": 1,
            "story_scenes": ["act1_04_contract_glitter_vein"],
            "optional_scenes": [],
            "combat": "act1_glitter_vein",
        },
        5: {
            "title": "Flicker Day",
            "act": 1,
            "story_scenes": ["act1_05_flicker_day"],
            "optional_scenes": [],
            "combat": "",
        },
        6: {
            "title": "Minebreak",
            "act": 1,
            "story_scenes": ["act1_06_minebreak"],
            "optional_scenes": [],
            "combat": "",
        },
        7: {
            "title": "Exit Writ",
            "act": 1,
            "story_scenes": ["act1_07_exit_writ"],
            "optional_scenes": [],
            "combat": "",
        },
        8: {
            "title": "The Girl With the Shard",
            "act": 1,
            "story_scenes": ["act1_08_the_girl_with_the_shard"],
            "optional_scenes": [],
            "combat": "",
        },
        9: {
            "title": "A Name Given, Not Owned",
            "act": 1,
            "story_scenes": ["act1_09_a_name_given_not_owned"],
            "optional_scenes": [
                "act1_09a_medical_autonomy",
                "act1_09b_rowan_finds_vesper",
            ],
            "combat": "",
        },
        10: {
            "title": "First Watch",
            "act": 1,
            "story_scenes": ["act1_10_first_watch"],
            "optional_scenes": [
                "act1_10a_personal_property",
                "act1_10b_roster_roles_and_refusal",
            ],
            "combat": "",
        },
        11: {
            "title": "Shard Whispers",
            "act": 1,
            "story_scenes": ["act1_11_shard_whispers"],
            "optional_scenes": [
                "act1_11a_id_names_forms",
                "act1_11b_senna_small_good_thing",
            ],
            "combat": "",
        },
        12: {
            "title": "The Doctrine",
            "act": 1,
            "story_scenes": ["act1_12_the_doctrine"],
            "optional_scenes": [
                "act1_12a_crew_meal_dynamics",
                "act1_12b_ai_game_night_probability",
            ],
            "combat": "",
        },
        13: {
            "title": "Shipboard Physics",
            "act": 1,
            "story_scenes": ["act1_13_shipboard_physics"],
            "optional_scenes": [
                "act1_13a_starmap_hobby",
                "act1_13b_coffee_ritual",
                "act1_13c_asking_for_what_you_need",
                "act1_13d_choosing_rest",
                "act1_13e_water_is_not_a_test",
                "act1_13f_avyanna_yes_reflex",
                "act1_13g_rho_kenna_coffee",
            ],
            "combat": "",
        },
        14: {
            "title": "Dumb Reliability",
            "act": 1,
            "story_scenes": ["act1_14_dumb_reliability"],
            "optional_scenes": [
                "act1_14a_first_contract_debrief",
                "act1_14b_small_success_contract",
                "act1_14c_bridge_transit_ritual",
                "act1_14d_orin_teaches_bearing",
            ],
            "combat": "",
        },
        15: {
            "title": "Ghost Net Lesson",
            "act": 1,
            "story_scenes": ["act1_15_ghost_net_lesson"],
            "optional_scenes": [
                "act1_15a_guild_station_protocols",
                "act1_15b_first_purchase_decision",
                "act1_15c_station_micro_errand_paperwork_and_predators",
                "act1_15d_rival_crew_probe",
                "act1_15e_maren_blocks",
            ],
            "combat": "",
        },
        16: {
            "title": "Breach Hymn",
            "act": 1,
            "story_scenes": ["act1_16_breach_hymn"],
            "optional_scenes": [
                "act1_16a_jalen_navigation_lesson",
                "act1_16b_emergency_drill",
                "act1_16c_maintenance_pairing_day",
                "act1_16d_convoy_transit_comparison",
                "act1_16e_senna_math_is_power",
            ],
            "combat": "act1_breach_hymn",
        },
        17: {
            "title": "Rule of Locality",
            "act": 1,
            "story_scenes": ["act1_17_rule_of_locality"],
            "optional_scenes": [
                "act1_17a_assumption_lab",
                "act1_17b_complaint_posting",
                "act1_17c_reading_technical_manual",
                "act1_17d_library_glossary_of_lies",
                "act1_17e_nyx_and_halcyon_ward_lesson",
            ],
            "combat": "",
        },
        18: {
            "title": "Primordial Garden",
            "act": 1,
            "story_scenes": ["act1_18_primordial_garden"],
            "optional_scenes": [
                "act1_18a_cultural_context",
                "act1_18b_station_overwhelm_recovery",
                "act1_18c_grove_propagation_lesson",
            ],
            "combat": "",
        },
        19: {
            "title": "Contract: Station Justice",
            "act": 1,
            "story_scenes": ["act1_19_contract_station_justice"],
            "optional_scenes": [
                "act1_19a_contract_negotiation_witness",
                "act1_19b_teaching_consent_to_client",
                "act1_19c_receipt_practice",
            ],
            "combat": "act1_station_justice",
        },
        20: {
            "title": "The Receipt",
            "act": 1,
            "story_scenes": ["act1_20_the_receipt"],
            "optional_scenes": [
                "act1_20a_quiet_ship_night",
                "act1_20b_witnessing_crew_conflict",
                "act1_20c_archive_ritual",
                "act1_20d_aleena_pulls_elia_from_wreckage",
            ],
            "combat": "",
        },

        # ═══════════════════════════════════════════════════════
    }

    ## Act titles for title cards
    ACT_TITLES = {`r`n        1: "Act I: Foundations",`r`n    }

    ## Display names for optional scenes in the hub
    DIALOGUE_DISPLAY_NAMES = {
        "act1_09a_medical_autonomy": "Medical Autonomy (Nyx)",
        "act1_09b_rowan_finds_vesper": "Rowan Finds Vesper",
        "act1_10a_personal_property": "Personal Property",
        "act1_10b_roster_roles_and_refusal": "Roster, Roles & Refusal",
        "act1_11a_id_names_forms": "ID, Names & Forms",
        "act1_11b_senna_small_good_thing": "A Small Good Thing (Senna)",
        "act1_12a_crew_meal_dynamics": "Crew Dinner",
        "act1_12b_ai_game_night_probability": "AI Game Night",
        "act1_13a_starmap_hobby": "Starmap Hobby",
        "act1_13b_coffee_ritual": "Coffee Ritual",
        "act1_13c_asking_for_what_you_need": "Asking For What You Need",
        "act1_13d_choosing_rest": "Choosing Rest",
        "act1_13e_water_is_not_a_test": "Water Is Not a Test",
        "act1_13f_avyanna_yes_reflex": "The Yes Reflex",
        "act1_13g_rho_kenna_coffee": "Rho & Kenna: Coffee",
        "act1_14a_first_contract_debrief": "Contract Debrief",
        "act1_14d_orin_teaches_bearing": "Orin Teaches Bearing",
        "act1_16a_jalen_navigation_lesson": "Navigation Lesson (Jalen)",
        "act1_17e_nyx_and_halcyon_ward_lesson": "Ward Lesson (Nyx)",
        "act1_18c_grove_propagation_lesson": "Propagation (Grove)",
        "act1_20d_aleena_pulls_elia_from_wreckage": "Aleena & Elia",
    }

    ## Scene requirements (flag and relationship gating)
    DIALOGUE_REQUIREMENTS = {
        # Act 1 — story progression gates
        "act1_10_first_watch": {"flags": ["has_lagrange_name"]},
        "act1_11_shard_whispers": {"flags": ["completed_first_watch"]},
        "act1_12_the_doctrine": {"flags": ["ai_citizens_introduced"]},
        "act1_17e_nyx_and_halcyon_ward_lesson": {"flags": ["shard_symptoms_revealed"]},
        "act1_18c_grove_propagation_lesson": {"flags": ["bee_revealed"]},

        # Act 1 — flag-gated optional scenes
        "act1_09a_medical_autonomy": {"flags": ["has_lagrange_name"]},
        "act1_11a_id_names_forms": {"flags": ["has_lagrange_name"]},
        "act1_15b_first_purchase_decision": {"flags": ["spoke_up_first_time"]},

    }

    def get_act_for_chapter(chapter_num):
        """Return which act a chapter belongs to."""
        return CHAPTER_SEQUENCE.get(chapter_num, {}).get("act", 1)

    def is_dialogue_available(dialogue_id):
        """Check if a scene meets its flag and relationship requirements."""
        reqs = DIALOGUE_REQUIREMENTS.get(dialogue_id, {})
        if not reqs:
            return True
        for flag in reqs.get("flags", []):
            if not game_state.has_flag(flag):
                return False
        for char_id, required_tier in reqs.get("relationship", {}).items():
            if not relationship_manager.is_at_least(char_id, required_tier):
                return False
        return True

    def get_available_optional_scenes(chapter_num):
        """Return list of available optional scene IDs for a chapter."""
        chapter = CHAPTER_SEQUENCE.get(chapter_num, {})
        available = []
        for s_id in chapter.get("optional_scenes", []):
            if not game_state.has_played_dialogue(s_id) and is_dialogue_available(s_id):
                available.append(s_id)
        return available

    def get_dialogue_display_name(scene_id):
        """Return human-readable name for a scene."""
        if scene_id in DIALOGUE_DISPLAY_NAMES:
            return DIALOGUE_DISPLAY_NAMES[scene_id]
        name = scene_id
        for prefix in ("act1_",):
            if name.startswith(prefix):
                name = name[len(prefix):]
                break
        name = _re.sub(r'^\d+[a-z]*_', '', name)
        return name.replace("_", " ").title()

    def get_dialogue_lock_reason(dialogue_id):
        """Return why a dialogue is locked, or None if available."""
        reqs = DIALOGUE_REQUIREMENTS.get(dialogue_id, {})
        if not reqs:
            return None
        for char_id, required_tier in reqs.get("relationship", {}).items():
            if not relationship_manager.is_at_least(char_id, required_tier):
                current = relationship_manager.get_tier_name(char_id)
                return "Requires {} tier with {} (currently {})".format(
                    required_tier.title(), char_id.title(), current)
        for flag in reqs.get("flags", []):
            if not game_state.has_flag(flag):
                return "Locked"
        return None

    TOTAL_CHAPTERS = 21  # released Act 1: 0 through 20


## ═══════════════════════════════════════════════════════════
## Master chapter flow
## ═══════════════════════════════════════════════════════════

label chapter_flow:
    $ _chapter = 0
    $ _last_act = 0
    while _chapter < TOTAL_CHAPTERS:
        $ game_state.current_chapter = _chapter
        $ update_highest_chapter(_chapter)

        # Show act title card on act transitions
        $ _current_act = get_act_for_chapter(_chapter)
        if _current_act != _last_act:
            call show_act_title(_current_act)
            $ _last_act = _current_act

        call show_chapter_title(_chapter)
        call play_chapter(_chapter)
        call show_chapter_complete(_chapter)
        $ _chapter += 1

    call game1_complete
    return

## Show act title card
label show_act_title(act_num):
    scene black
    pause 0.5
    centered "{size=+12}[ACT_TITLES[act_num]]{/size}"
    pause 3.0
    scene black with slow_fade
    return

## Show chapter title card
label show_chapter_title(chapter_num):
    scene black
    pause 0.5
    if chapter_num == 0:
        centered "{size=+8}Prologue{/size}\n\n{size=+4}[CHAPTER_SEQUENCE[chapter_num]['title']]{/size}"
    else:
        centered "{size=+8}Chapter [chapter_num]{/size}\n\n{size=+4}[CHAPTER_SEQUENCE[chapter_num]['title']]{/size}"
    pause 2.0
    scene black with chapter_fade
    return

## Play a chapter's content
label play_chapter(chapter_num):
    $ _ch_data = CHAPTER_SEQUENCE[chapter_num]

    if is_ng_plus():
        $ game_state.set_flag("ng_plus_chapter_" + str(chapter_num))

    # Play required story scenes in sequence
    $ _story_list = list(_ch_data.get("story_scenes", []))
    while _story_list:
        $ _next_scene = _story_list.pop(0)
        if is_dialogue_available(_next_scene):
            call expression _next_scene
            $ game_state.mark_dialogue_played(_next_scene)
            pause 0.3
            with quick_dissolve

    # Show hub for optional scenes if any exist
    $ _optional = get_available_optional_scenes(chapter_num)
    if _optional:
        call chapter_hub(chapter_num)

    # Trigger combat if chapter has it
    $ _combat_id = _ch_data.get("combat", "")
    if _combat_id and not game_state.is_encounter_cleared(_combat_id):
        call expression "combat_" + _combat_id

    return

## Chapter hub — optional scene selection
label chapter_hub(chapter_num):
    $ _hub_done = False
    while not _hub_done:
        $ _available = get_available_optional_scenes(chapter_num)
        if not _available:
            $ _hub_done = True
        else:
            call screen hub_screen(chapter_num, _available)
            if _return == "advance":
                $ _hub_done = True
            elif _return and _return.startswith("play:"):
                $ _scene_to_play = _return[5:]
                call expression _scene_to_play
                $ game_state.mark_dialogue_played(_scene_to_play)
    return

## Chapter complete transition
label show_chapter_complete(chapter_num):
    $ game_state.set_flag("chapter_{}_complete".format(chapter_num))

    # Record story milestone memories at key chapters
    if chapter_num == 0:
        $ record_memory("prologue_boarding")
    elif chapter_num == 8:
        $ record_memory("girl_with_shard")
    elif chapter_num == 9:
        $ record_memory("naming_scene")
    elif chapter_num == 20:
        $ record_memory("the_receipt")

    scene black with slow_fade
    centered "{size=+4}Chapter Complete{/size}\n\n[CHAPTER_SEQUENCE[chapter_num]['title']]"
    pause 1.5
    return

## Act 1 demo complete
label game1_complete:
    scene black
    pause 1.0
    centered "{size=+12}End of Act 1 Demo{/size}\n\n{size=+6}Starforge Canticles{/size}"
    pause 3.0
    $ complete_playthrough()
    return
