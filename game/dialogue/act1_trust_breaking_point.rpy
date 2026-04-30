## act1_trust_breaking_point.rpy — Auto-generated from act1_trust_breaking_point.json
## 34 dialogue nodes

label act1_trust_breaking_point:
    $ game_state.mark_dialogue_played("act1_trust_breaking_point")
    jump act1_trust_breaking_point_start

label act1_trust_breaking_point_start:
    "{i}The common area. Voices raised—not the careful sparring of Sparkle Doctrine, but something sharper. Raw.{/i}"
    jump act1_trust_breaking_point_elia_position

label act1_trust_breaking_point_elia_position:
    elia "We took the contract. We finish it. That's the floor."
    jump act1_trust_breaking_point_vesper_counter

label act1_trust_breaking_point_vesper_counter:
    vesper "{i}Jaw tight.{/i} The floor includes not walking into a trap. The client lied about the security. You saw the feeds."
    jump act1_trust_breaking_point_elia_dismissive

label act1_trust_breaking_point_elia_dismissive:
    elia "Security we can handle. We've handled worse."
    jump act1_trust_breaking_point_vesper_harder

label act1_trust_breaking_point_vesper_harder:
    vesper "{i}Colder.{/i} Handling it isn't the same as walking in blind. You're prioritizing completion over crew safety."
    jump act1_trust_breaking_point_rho_interjects

label act1_trust_breaking_point_rho_interjects:
    rho "{i}Grin gone.{/i} Hold up. Both of you. We're not doing this."
    jump act1_trust_breaking_point_elia_snaps

label act1_trust_breaking_point_elia_snaps:
    elia "{i}Turning on him.{/i} Doing what? Making a call? That's my job."
    jump act1_trust_breaking_point_rho_challenges

label act1_trust_breaking_point_rho_challenges:
    rho "Your job is {b}routing traffic{/b}, not making unilateral calls that risk everyone. Vesper's right—the client lied. That changes the contract."
    jump act1_trust_breaking_point_vesper_supports

label act1_trust_breaking_point_vesper_supports:
    vesper "{i}To Elia, voice like a blade.{/i} You taught me floors, not thrones. So why are you acting like a captain right now?"
    jump act1_trust_breaking_point_elia_stung

label act1_trust_breaking_point_elia_stung:
    elia "{i}Jaw working. The hit landed.{/i} That's not—"
    jump act1_trust_breaking_point_vesper_presses

label act1_trust_breaking_point_vesper_presses:
    vesper "It is. You're deciding for all of us. Without asking. Without explaining the math. {i}[Beat.]{/i} That's not the floor. That's a throne."
    jump act1_trust_breaking_point_player_choice

label act1_trust_breaking_point_player_choice:
    "{i}The tension is a live wire. Rho's hands are fists. Vesper's eyes are flat. Elia's blade hand twitches. This could break badly.{/i}"
    menu:
        "[Intervene] They need to hear each other. Step in.":
            $ game_state.set_flag("trust_intervention_attempted")
            jump act1_trust_breaking_point_intervene_check
        "[Let It Play Out] This is crew business. Stay quiet.":
            $ game_state.set_flag("trust_crisis_witnessed")
            jump act1_trust_breaking_point_play_out_resolution

label act1_trust_breaking_point_intervene_check:
    "{i}You step forward. Three pairs of eyes turn to you. This requires empathy—the ability to hold space for anger without flinching.{/i}"
    $ _sc_result = skill_check("empathy", 3, "avyanna")
    if _sc_result == "SUCCESS" or _sc_result == "CRITICAL_SUCCESS":
        jump act1_trust_breaking_point_intervene_success
    else:
        jump act1_trust_breaking_point_intervene_failure

label act1_trust_breaking_point_intervene_success:
    avyanna "{i}Voice steady.{/i} Elia. You're not wrong that we can handle security. Vesper's not wrong that we're walking in blind. But you're both angry about something else."
    jump act1_trust_breaking_point_intervene_elia_reaction

label act1_trust_breaking_point_intervene_elia_reaction:
    elia "{i}She stops. Blinks.{/i} What?"
    jump act1_trust_breaking_point_intervene_vesper_reaction

label act1_trust_breaking_point_intervene_vesper_reaction:
    avyanna "Vesper's scared you'll get hurt. Elia's scared of breaking the contract and losing crew trust. You're both right. You're both scared. {i}[Beat.]{/i} So say that instead."
    jump act1_trust_breaking_point_intervene_silence

label act1_trust_breaking_point_intervene_silence:
    "{i}Silence. Long enough to hurt. Then Elia exhales.{/i}"
    jump act1_trust_breaking_point_intervene_elia_concedes

label act1_trust_breaking_point_intervene_elia_concedes:
    elia "{i}Quieter.{/i} She's right. I was impatient. I wanted it done. I didn't explain the math."
    jump act1_trust_breaking_point_intervene_vesper_concedes

label act1_trust_breaking_point_intervene_vesper_concedes:
    vesper "{i}After a beat.{/i} And I should have said I was afraid instead of making it about procedure. {i}[She looks at you.]{/i} How did you—"
    jump act1_trust_breaking_point_intervene_avyanna_response

label act1_trust_breaking_point_intervene_avyanna_response:
    avyanna "{i}Shrugging.{/i} I'm good at watching. You taught me to speak up. So I did."
    jump act1_trust_breaking_point_intervene_resolution

label act1_trust_breaking_point_intervene_resolution:
    "{i}Rho laughs—surprised, relieved. The tension breaks. Not gone, but defused. You did that.{/i}"
    jump act1_trust_breaking_point_waffle_crisis_log

label act1_trust_breaking_point_intervene_failure:
    avyanna "{i}Voice uncertain.{/i} Maybe you should—I mean, you could try—"
    jump act1_trust_breaking_point_failure_elia_reaction

label act1_trust_breaking_point_failure_elia_reaction:
    elia "{i}Sharper than intended.{/i} Not now, Avyanna."
    jump act1_trust_breaking_point_failure_vesper_cold

label act1_trust_breaking_point_failure_vesper_cold:
    vesper "{i}Flat.{/i} This isn't your problem to solve. We'll handle it."
    jump act1_trust_breaking_point_failure_withdrawal

label act1_trust_breaking_point_failure_withdrawal:
    "{i}You step back, stung. The argument continues without you—louder, harder, until Rho forces a recess. It ends, eventually. But it leaves a mark.{/i}"
    jump act1_trust_breaking_point_waffle_crisis_log

label act1_trust_breaking_point_play_out_resolution:
    "{i}You watch. Silent. The argument escalates—Vesper's hands shake, Elia's blade hand drifts to her hilt, Rho steps between them—{/i}"
    jump act1_trust_breaking_point_play_out_rho

label act1_trust_breaking_point_play_out_rho:
    rho "{i}Voice hard.{/i} {b}Stop.{/b} Both of you. Right now."
    jump act1_trust_breaking_point_play_out_pause

label act1_trust_breaking_point_play_out_pause:
    "{i}They stop. Breathing hard. Rho looks between them.{/i}"
    jump act1_trust_breaking_point_play_out_rho_assessment

label act1_trust_breaking_point_play_out_rho_assessment:
    rho "You're both right. You're both scared. And you're both acting like this is about the contract when it's about trust. {i}[Beat.]{/i} So either say that, or take a break and come back when you can."
    jump act1_trust_breaking_point_play_out_break

label act1_trust_breaking_point_play_out_break:
    "{i}Elia leaves. Vesper sits, head in hands. Rho exhales. The crisis passes—unresolved, but not broken. You witnessed it. That matters too.{/i}"
    jump act1_trust_breaking_point_waffle_crisis_log

label act1_trust_breaking_point_waffle_crisis_log:
    waffle "{i}}{{WAFFLE.BAT// OBSERVATION: crew stress levels elevated | RECOMMENDATION: cooling period 2 hours minimum | NOTE: I am monitoring. I am here.}}{/i}}"
    jump act1_trust_breaking_point_bubbles_crisis_comfort

label act1_trust_breaking_point_bubbles_crisis_comfort:
    bubbles "{i}Quietly through the speakers, after the others have left:{/i} It's okay, Avyanna. Families fight. It doesn't mean they're broken."
    jump act1_trust_breaking_point_cinnamon_crisis_pragmatic

label act1_trust_breaking_point_cinnamon_crisis_pragmatic:
    cinnamon "Operational readiness unaffected. Crew conflict: temporary. Focus on the work."
    jump act1_trust_breaking_point_resolution_outcome

label act1_trust_breaking_point_resolution_outcome:
    "{i}Later, the crew will reconvene. They'll finish the conversation. But something shifted here—for better or worse.{/i}"
    menu:
        "[Continue]":
            $ game_state.set_flag("trust_crisis_resolved")
            $ game_state.set_flag("rep_crew_trust", game_state.get_flag("rep_crew_trust", 0) + 1)
            return
