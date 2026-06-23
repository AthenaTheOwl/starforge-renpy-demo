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

## Browser build (needs the Ren'Py web toolchain)

This repo is engine source, not a browser-ready bundle. A browser-playable
build is feasible, but only through Ren'Py's own Emscripten-based web export
(`renpyweb` / "Web" platform in the launcher), which requires the full Ren'Py
SDK. There is no checked-in HTML5 export and producing one cannot be faked
without that toolchain, so this repo is documented as run-locally rather than
one-click deployable.

To produce the web build on a machine with the SDK:

1. Open this folder as a project in the Ren'Py launcher (8.5.x).
2. Install the web support module when prompted (Build > Web).
3. Choose **Build > Build Web Application**. Ren'Py emits a `web/` directory
   containing `index.html` plus the packaged game.
4. That `web/` directory is then a static bundle you can host on any static
   host (Vercel, Netlify, GitHub Pages, itch.io).

Until that export exists, play it locally via the Ren'Py SDK as described above.

## Validate

```powershell
python -m pytest
python tools\validate_renpy.py game
python tools\playtest_audit.py
python tools\check_release.py
```

For the full native release gate on a machine with Ren'Py installed:

```powershell
python tools\check_release.py --clean --fail-on-generated --fail-on-renpy-lint-diagnostics --require-renpy --renpy E:\claude_code\starforge-game\renpy-8.5.2-sdk\renpy.exe
```

`tools/check_release.py` is the deterministic orchestration entry point for
this repo. Python checks cover cleanup, static source validation, and
path/dead-letter audit; Ren'Py lint remains the engine-native gate. The
`--clean` flag explicitly removes known Ren'Py generated artifacts before and
after the native lint run, and
`--fail-on-renpy-lint-diagnostics` treats captured lint diagnostics as
release-blocking. See `docs/deterministic-orchestration.md` for the proof gates.

## Cleanup boundary

Included:

- Act 1 `game/**/*.rpy` source
- game data JSON
- UI screens and Python systems
- validation tests
- deterministic playtest/path audit

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
- [starforge-twine-demo](https://github.com/AthenaTheOwl/starforge-twine-demo) - single-HTML Twine/SugarCube demo
- [starforge-choicescript-demo](https://github.com/AthenaTheOwl/starforge-choicescript-demo) - stat-forward ChoiceScript demo
