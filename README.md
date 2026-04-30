# No. 15 - starforge-renpy-demo

A curated exhibit from Starforge, an in-progress narrative game project. This
repo is the Act 1-only cleaned Ren'Py source copy: released narrative scenes,
dialogue files, combat vignettes, state systems, and UI screens without SDK
files, saves, logs, or compiled runtime artifacts.

The story itself is published as
[Starforge Canticles on Royal Road](https://www.royalroad.com/fiction/149065/starforge-canticles).
This repo shows one in-progress game adaptation path for the published portion
of that public serial.

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
- [starforge-renpy-demo](https://github.com/AthenaTheOwl/starforge-renpy-demo) - Act 1 Ren'Py narrative demo copy
- [starforge-rpg-prototype](https://github.com/AthenaTheOwl/starforge-rpg-prototype) - Act 1 Godot RPG prototype copy
