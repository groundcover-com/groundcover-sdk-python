# sdk-python

The `sdk-python` entry in [`.github/signoff/products.yml`](../.github/signoff/products.yml) decides when this signoff applies, and most of its paths are outside this directory:

- `signoff:` paths (this directory, `scripts/swagger/`, `docs/swagger.yaml`, `cmd/router` and the router API packages the spec is scanned from, the `pkg/migration` gitlink) need your signoff before you push, even when nothing under `sdk-python/` changed.
- `queue-only:` paths (`go.mod`, `go.sum`, `sdk-test.yml`) need none; the merge queue runs `task sdk-python:test` on them.

## Push only through the signoff task (mandatory)

- **Push with `task sdk-python:signoff`** (or `task signoff`) from the repo root, never a bare `git push`. It runs `task sdk-python:test` (regenerate the SDK, then the unit tests on Python 3.9–3.13 in parallel) on a clean tree, pushes, and posts `signoff/sdk-python` on the tested commit.
- If tests fail, rerun each failure once on its Python: `sdk-python/scripts/signoff-tests.sh test <version> -k <name>` (or the test node id). `pytest --lf` can't see the signoff's runs: they keep no cache and use per-version `.venv-py<version>` environments. A pass is a flake: record it on DX-790 and sign off again. Only a failure that reproduces means fix the code.
- Don't run other signoffs at the same time: `generate.sh` uses fixed `/tmp` paths (DX-790).
- Generation needs Go, uv and npx. The generated modules are gitignored; never commit them. A spec diff after a successful generation means `docs/swagger.yaml` is out of date: commit the regenerated spec.
- Before the first signoff: `git submodule update --init --recursive`, set `git config user.name`, and never run `gh signoff install` (it edits repository rulesets). Details: [git-workflow skill](../.agents/skills/git-workflow/SKILL.md#before-your-first-signoff).
