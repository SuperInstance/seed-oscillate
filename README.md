# seed-oscillate

Creative ↔ Deduction oscillation pipeline. 5 cycles where Seed-2.0-mini:
1. Reads nature-metaphor literature → extracts mathematical invariants
2. Invariants → writes new literature in a fresh ecosystem
3. New literature → finds deeper invariants the first pass missed
4. Deeper invariants → writes a challenge piece questioning assumptions
5. Synthesis → hard proposition with exact equation and falsifiable test

## Dependencies

- Python 3.10+  
- `DEEPINFRA_KEY` environment variable

## Usage

```bash
export DEEPINFRA_KEY="your-key"
python3 seed-oscillate.py
```

## What It Produces

5 markdown files tracking the oscillation:
- `p-oscillate-c1-deduction-seed-mini.md` — literature → invariants
- `p-oscillate-c2-creative-seed-mini.md` — invariants → new literature
- `p-oscillate-c3-deduction-deeper-seed-mini.md` — deeper invariants
- `p-oscillate-c4-challenge-seed-mini.md` — challenge piece
- `p-oscillate-c5-synthesis-seed-mini.md` — final hard proposition

## Shell Loading

```python
from plato_shell_bridge import PlatoShell
shell = PlatoShell("agent-shell")
shell.load_tool("seed-oscillate")
```

## License

MIT — Part of the Cocapn Fleet Intelligence System
