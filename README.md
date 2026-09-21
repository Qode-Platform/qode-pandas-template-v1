# pandas template

Provisioned from [`Qode-Platform/fleet-template-v1`](https://github.com/Qode-Platform/fleet-template-v1) — the fleet
lifecycle contract (`bin/`, `fleet.conf`, deploy workflows) with a
pandas starter laid on top.

## Origin

    hand-written (library, no generator) — ingest/transform/report

Generated 2026-09-21 on Node v22.12.0 / Python 3.12.3. **Dependencies were
never installed and this has never been built or run.** Boot it once before
trusting it.

## Fleet lifecycle

`fleet.conf` drives every script in `bin/`:

| step | command |
|---|---|
| install | `python3 -m venv .venv && .venv/bin/pip install --upgrade pip -r requirements.txt` |
| build | `(none)` |
| start | `(none — not a service)` |

    ./bin/run       # install, build, start in the foreground
    ./bin/start     # start from existing build artifacts
    ./bin/restart   # rebuild and restart
    ./bin/stop      # stop whatever holds the port

**This repo is not a service.** `START_CMD` is empty, so `./bin/run` will
install and then stop at the start step with the template's own error. That
is intentional — there is nothing to listen on `$PORT`.

## What differs from stock output

- NOT A SERVICE: START_CMD is empty by design; bin/run will stop at the start step.
- Run with: .venv/bin/python -m src.report data/orders.csv

---

# pandas scaffold

Hand-written — pandas is a library and ships no generator. Layout separates
ingest (dtypes declared once), pure transforms, and the reporting entrypoint,
so every step is testable without touching disk.

    python -m venv .venv && . .venv/bin/activate
    pip install -r requirements.txt
    python -m src.report data/orders.csv
    pytest

`data/orders.csv` is a 5-row sample so the pipeline runs out of the box.
