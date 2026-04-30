## script.rpy — Entry point for Starforge Canticles
##
## This file defines the game start label and delegates to the chapter flow system.

label start:
    ## Initialize game state
    $ game_state = GameState()
    $ relationship_manager = RelationshipManager()
    $ party_manager = PartyManager()
    $ ending_tracker = EndingTracker()
    $ faction_reputation = FactionReputation()

    ## Check for NG+ and apply unlocks
    if persistent.playthrough_count and persistent.playthrough_count > 0:
        $ apply_ng_plus_unlocks()

    ## Hand off to chapter flow (public Act 1 demo only)
    call chapter_flow

    ## Act 1 demo complete - return to main menu
    scene black with fade

    if persistent.playthrough_count > 1:
        centered "{size=+10}Act 1 Demo Complete{/size}\n\nThe threads of fate twist anew.\nPlaythrough [persistent.playthrough_count] complete.\n\nNew memories stir beneath the old..."
    else:
        centered "{size=+10}Act 1 Demo Complete{/size}\n\nContinue reading Starforge Canticles on Royal Road."
    pause 3.0

    $ MainMenu(confirm=False)()

    return
