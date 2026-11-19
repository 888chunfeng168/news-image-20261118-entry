# World News — Wednesday 18 November 2026, in one image

Entry for make.fun competition **news-image-20261118**: "Sum up 18 November's
world news in one image" ($250 prize pool, top 50 entries share it).

## The image

`entry.png` (1024×1024, PNG) is a news poster of the day's world news,
researched from reporting by Reuters, AP, AFP and Al Jazeera:

- **Top story** — Xi Jinping and Vladimir Putin meet in Shenzhen, a day
  before the first-ever Trump–Xi–Putin trilateral summit.
- **Gulf on edge** — the US sinks five Iranian tankers; Iran fires on a US
  base in Kuwait as Gulf shipping comes under attack.
- **Ukraine** — Kerch Bridge struck for a second night; Moscow and Kyiv
  agree their biggest POW swap.
- **US politics** — Mary Peltola flips the Alaska Senate seat; Democrats
  take a projected 56–44 Senate majority.
- **Climate** — COP31 climate talks in Antalya enter their decisive phase.
- **Tech** — Nvidia chief Jensen Huang resigns; the board will not
  reinstate him.
- **Weather** — Cyclone Akvan bears down on India's east coast.
- **Also** — MS Dhoni retires from the IPL, Robert Pattinson is named the
  new James Bond, civil-rights leader Jesse Jackson dies at 84.

## How it is built

`draw.py` draws the poster with Pillow (deterministic: same input, same
bytes; no network, no clock, no randomness). `main.py` (Python 3.13,
standard library only) is the entrypoint: it copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`).

```sh
python3 draw.py          # regenerate entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # test the entrypoint
```

## License

MIT. See `LICENSE`.
