# sdk-python

The `sdk-python` entry in [`.github/signoff/products.yml`](../.github/signoff/products.yml) decides when this signoff applies, and most of its paths are outside this directory:

- `signoff:` paths (this directory, `scripts/swagger/`, `docs/swagger.yaml`) need your signoff before merge, even when nothing under `sdk-python/` changed.
- `queue-only:` paths (the root `Taskfile.yml`, `sdk-test.yml`) need none; the merge queue runs `task sdk-python:test` on them.
- Go changes reach the SDK only through the committed spec. The router's Go trees need `signoff/swagger-spec` instead (`task swagger-spec:signoff`), which fails until you commit the regenerated `docs/swagger.yaml`; committing it then requires this signoff.

## Signoff (mandatory)

- These changes need `signoff/sdk-python` before they can merge, and you are responsible for it: **when the PR is ready to merge, run `task sdk-python:signoff`** (or `task signoff`) from the repo root. It runs `task sdk-python:test` (regenerate the SDK, then the unit tests on Python 3.9–3.13 in parallel) on a clean tree, pushes, and posts `signoff/sdk-python` on the tested commit.
- While iterating, run the cheapest tests that cover the change. Generating the SDK is the expensive step (about a minute: Go, swagger, npx); after one generation, `sdk-python/scripts/signoff-tests.sh test <version> -k <name>` takes seconds. The full signoff takes a minute or two.
- If tests fail, rerun each failure once on its Python: `sdk-python/scripts/signoff-tests.sh test <version> -k <name>` (or the test node id). `pytest --lf` can't see the signoff's runs: they keep no cache and use per-version `.venv-py<version>` environments. A pass is a flake: record it on DX-790 and sign off again. Only a failure that reproduces means fix the code.
- Generation needs Go, uv and npx. The generated modules are gitignored; never commit them. A spec diff after a successful generation means `docs/swagger.yaml` is out of date: commit the regenerated spec.
- Before the first signoff: `git submodule update --init --recursive`, set `git config user.name`, and never run `gh signoff install` (it edits repository rulesets). Details: [git-workflow skill](../.agents/skills/git-workflow/SKILL.md#before-your-first-signoff).
