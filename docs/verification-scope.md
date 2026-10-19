# Verification scope — October 18, 2026

The strict local gate passed with Ren'Py 8.5.2:

```powershell
python tools/check_release.py --clean --fail-on-generated --fail-on-renpy-lint-diagnostics --require-renpy --renpy E:\claude_code\starforge-game\renpy-8.5.2-sdk\renpy.exe
```

Evidence: 7 Python tests; static validation with 0 errors and 0 warnings;
65 routed story scenes and 4 routed combat scenes; native lint with no
blocking diagnostics. Generated engine files were cleaned by the gate.
The source, dialogue and encounter balance were unchanged.

Lint checks script validity. It does not exercise every menu, combat outcome,
save/load transition or visual layout. Human playthrough and a web export
remain separate proof obligations.

A useful AI Product Team task is a bounded regression proposal: select one
existing route, name its expected terminal state, then run it in the engine.
Keep the evaluator outside the agent's claim of success. Stop after one route
and report untested branches explicitly; a static route count is no substitute.
