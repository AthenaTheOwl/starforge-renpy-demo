# starforge-renpy-demo

2,414 labels, 264 menus, and 14 fights — the biggest of which, the mine breach, hits with 508 HP and 188 attack. That's Act 1 of a serialized novel turned into something you can actually click through.

## What it does

[Starforge Canticles](https://www.royalroad.com/fiction/149065/starforge-canticles) is a speculative-fiction serial I publish chapter-by-chapter on Royal Road. This repo is one adaptation path for it: Act 1 rebuilt as a Ren'Py narrative game — branching scenes, dialogue, skill checks, relationship state, and combat vignettes, all in a text-forward engine.

The prose came first. The game is the prose wired up so it can fork: 65 routed story scenes and 4 routed combat scenes, 14 named encounters tuned from a husk echo you can swat (70 HP) up to the mine breach that will end a careless run (508 HP). Same source as the [Twine demo](https://github.com/AthenaTheOwl/starforge-twine-demo) and the [Godot prototype](https://github.com/AthenaTheOwl/starforge-rpg-prototype) — same Act 1, different playable shape each time.

Active development lives in a private workshop. This public copy is the curated cut: Act 1 source is in, the SDK and runtime junk are out, and the cleanup boundary is enforced by a script, not a promise. Unreleased later-act material — endings included — stays sealed.

## Try it

No engine needed for this part. The playtest audit walks every label, counts the routes, and checks no scene drops into a dead letter:

```powershell
python tools\playtest_audit.py
```

```
Ren'Py playtest audit
- labels: 2414
- routed story scenes: 65
- routed combat scenes: 4
- menus: 264
- encounters: 14
- dead-letter marker hits: 0
- lowest encounter threat: act1_husk_echo hp=70 atk=16
- highest encounter threat: act1_mine_breach hp=508 atk=188
playtest audit passed
```

Zero dead-letter hits means every branch lands somewhere a player can reach. The encounter line at the bottom is the difficulty spread, smallest fight to largest.

## Run it locally

Install or download Ren'Py 8.5.x and open this folder as a Ren'Py project. To lint it from the local workshop SDK used during cleanup:

```powershell
E:\claude_code\starforge-game\renpy-8.5.2-sdk\renpy.exe . lint
```

## Browser build (needs the Ren'Py web toolchain)

This repo is engine source, not a browser-ready bundle. A browser-playable build is feasible, but only through Ren'Py's own Emscripten-based web export (`renpyweb` / "Web" platform in the launcher), which requires the full Ren'Py SDK. There is no checked-in HTML5 export and producing one cannot be faked without that toolchain, so this repo is documented as run-locally rather than one-click deployable.

To produce the web build on a machine with the SDK:

1. Open this folder as a project in the Ren'Py launcher (8.5.x).
2. Install the web support module when prompted (Build > Web).
3. Choose **Build > Build Web Application**. Ren'Py emits a `web/` directory containing `index.html` plus the packaged game.
4. That `web/` directory is then a static bundle you can host on any static host (Vercel, Netlify, GitHub Pages, itch.io).

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

`tools/check_release.py` is the one entry point that runs the whole gate in order: cleanup, static source validation, path/dead-letter audit, then Ren'Py's own engine lint. `--clean` strips known Ren'Py generated artifacts before and after the native lint run, and `--fail-on-renpy-lint-diagnostics` treats any captured lint diagnostic as release-blocking. See `docs/deterministic-orchestration.md` for the proof gates.

## Cleanup boundary

The script decides what ships. Included:

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

Part of the Starforge cluster — one prose source, several playable shapes:

- [starforge-narrative-tools](https://github.com/AthenaTheOwl/starforge-narrative-tools) — public Act 1 corpus + conversion/validation tooling
- [starforge-rpg-prototype](https://github.com/AthenaTheOwl/starforge-rpg-prototype) — Act 1 Godot RPG prototype copy
- [starforge-twine-demo](https://github.com/AthenaTheOwl/starforge-twine-demo) — single-HTML Twine/SugarCube demo
- [starforge-choicescript-demo](https://github.com/AthenaTheOwl/starforge-choicescript-demo) — stat-forward ChoiceScript demo

## License

MIT. See [LICENSE](LICENSE).
