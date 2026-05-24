# Deterministic Orchestration

This repo is the Ren'Py adaptation proof. Its orchestration should use Ren'Py
tools for Ren'Py behavior and Python only for repo hygiene and static source
checks.

## Native Tooling

- `python -m pytest` checks the cleaned public copy and calls static validation.
- `python tools/validate_renpy.py game` checks labels, jumps, calls, speakers,
  and source-shape issues that can be found without launching the engine.
- `python tools/playtest_audit.py` checks routed Act 1 scene labels, combat
  labels, menu count, encounter enemy references, threat scores, and explicit
  dead-letter markers.
- `python tools/check_release.py` runs the deterministic local gate.
- `python tools/check_release.py --renpy <path-to-renpy>` adds Ren'Py lint.
- `python tools/check_release.py --clean --fail-on-generated --fail-on-renpy-lint-diagnostics --require-renpy --renpy <path-to-renpy>`
  is the full release gate for a machine with Ren'Py installed.
- `--clean` removes only known Ren'Py churn: root `errors.txt`, `log.txt`,
  `traceback.txt`; `game/cache`; `game/saves`; and generated `.rpyc`, `.rpyb`,
  or `.save` files under `game/`.

## Proof Gates

1. Public Act 1 Ren'Py source is present.
2. No runtime junk, saves, compiled Ren'Py files, logs, or later-workshop source
   are present.
3. Static Ren'Py validation reports zero errors.
4. Playtest path/dead-letter audit passes before Act 1 route-complete claims.
5. Ren'Py lint passes on a local machine with Ren'Py 8.5.x installed and emits
   no captured diagnostics under `--fail-on-renpy-lint-diagnostics`.
6. Manual smoke covers launch, one choice, one state/check branch, save/load,
   and return-to-menu before release.

## CI Ring

The GitHub Actions workflow runs `tools/check_release.py`, which covers the
Python, cleanup-boundary, and static gates. Ren'Py lint is intentionally a
release gate, because this cleaned public repo does not vendor the Ren'Py SDK.

## Release Rule

Do not treat Python tests as a substitute for Ren'Py lint or manual play. The
Python gate blocks obvious drift; the engine gate proves the project is still a
Ren'Py-playable demo.
