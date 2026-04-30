# No. 15 - starforge-renpy-demo

[Starforge Canticles](https://www.royalroad.com/fiction/149065/starforge-canticles)
is a serialized speculative-fiction novel I'm publishing chapter-by-chapter on
Royal Road. This repo is one game-adaptation path for it: Act 1 of the serial
rendered as a Ren'Py narrative demo with branching scenes, dialogue, combat
vignettes, and relationship-state systems.

Active development happens in a private workshop. This public copy is meant for
portfolio review and future iteration; unreleased later-act material is excluded.

## What this proves

- A published serial can be adapted into a playable narrative format.
- Branching scenes, relationship state, skill checks, and combat
  vignettes can coexist in a text-forward Ren'Py structure.
- The repo is curated rather than dumped: source is included, runtime junk is
  excluded, and validation is explicit.
- AI-assisted creative work can still keep clean release boundaries between
  public serial material and private workshop drafts.

## Run locally

Install or download Ren'Py 8.5.x, then open this folder as a Ren'Py project.

From the local workshop SDK used during cleanup:

```powershell
E:\claude_code\starforge-game\renpy-8.5.2-sdk\renpy.exe . lint
```

## Validate

```powershell
python -m pytest
python tools\validate_renpy.py game
```

## Cleanup boundary

Included:

- Act 1 `game/**/*.rpy` source
- game data JSON
- UI screens and Python systems
- validation tests

Excluded:

- Ren'Py SDK
- unreleased later-act source and endings
- `*.rpyc`, `*.rpyb`
- saves and persistent state
- cache directories
- `errors.txt`, `traceback.txt`, logs

## See also

Part of the Starforge cluster:

- [starforge-narrative-tools](https://github.com/AthenaTheOwl/starforge-narrative-tools) - public Act 1 corpus + conversion/validation tooling
- [starforge-rpg-prototype](https://github.com/AthenaTheOwl/starforge-rpg-prototype) - Act 1 Godot RPG prototype copy
