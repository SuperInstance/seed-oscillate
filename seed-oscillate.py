import os
#!/usr/bin/env python3
"""
CREATIVE ↔ DEDUCTION OSCILLATION — Seed-mini back-and-forth
=============================================================
Cycle: literature → extract invariants → new literature → new invariants
Mostly seed-mini, but iterates 4-5 times.
"""

import json, time, urllib.request, re
from datetime import datetime
from pathlib import Path

API_KEY = os.environ.get("DEEPINFRA_KEY", "CDTTjm")
API_URL = "https://api.deepinfra.com/v1/openai/chat/completions"
MODEL = "ByteDance/Seed-2.0-mini"
OUTPUT_DIR = Path("/home/ubuntu/.openclaw/workspace/research/seed-tick-audit")

def call(prompt, max_tokens=4000, temp=0.85, timeout=180):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": temp,
    }).encode()
    req = urllib.request.Request(
        API_URL, data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
        method="POST"
    )
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
        data = json.loads(resp.read())
        return data["choices"][0]["message"].get("content", "")
    except Exception as e:
        return f"[ERROR: {e}]"


def read_body(path):
    with open(path) as f:
        text = f.read()
    body = re.split(r'---\n', text, maxsplit=1)
    content = body[1] if len(body) > 1 else text
    content = re.split(r'_\(reasoning:', content)[0]
    return content.strip()


# ── Load best creative works ──
creative_sources = {
    "minimax-forest": read_body(str(OUTPUT_DIR / "p-forest-story-minimax.md")),
    "claude-forest": read_body(str(OUTPUT_DIR / "p-forest-story-claude.md")),
    "seed-mini-mycelium": read_body(str(OUTPUT_DIR / "08-STORY-FOREST-SPEAKS.md")),
    "seed-mini-tidepool": read_body(str(OUTPUT_DIR / "14-STORY-TIDE-POOL.md")),
    "crush-guugu-song": read_body(str(OUTPUT_DIR / "p-gy-song-crush.md")),
    "minimax-shanty": read_body(str(OUTPUT_DIR / "p-shanty-minimax.md")),
}

# Compact creative context
creative_context = ""
for name, body in creative_sources.items():
    lines = body.split('\n')
    # Take first 15 lines of each as flavor
    flavor = '\n'.join(lines[:15])
    creative_context += f"\n=== {name} ===\n{flavor}\n..."
    if len(creative_context) > 8000:
        creative_context += "\n...[truncated]"
        break


print("🔥 CREATIVE ↔ DEDUCTION OSCILLATION")
print(f"📅 {datetime.utcnow().isoformat()}Z")
print(f"🤖 Model: {MODEL}")
print()

# ── Cycle 1: Literature → Deductions ──
print("=" * 60)
print("CYCLE 1: Literature → Deductions")
print("=" * 60)

p1 = f"""You are looking at literary works from 4 different AI models. Each wrote a piece about how "apparent noise in a multi-agent fleet is structural signal from a hidden coordination manifold." The metaphors are pure nature: forest mycelium networks, tide pool ecology, cardinal-direction grammar.

CREATIVE CONTEXT (first 15 lines of each):
{creative_context}

YOUR TASK: Extract the hidden MATHEMATICAL INVARIANTS that these metaphors are pointing at. Each metaphor encodes a mathematical structure. Find at least 3.

The metaphors encode:
- Forest mycelium → what graph structure connects "trees" silently?
- Tide pool barnacle → what mathematical property makes "noise" become "signal"?
- Cardinal grammar → what coordinate system transforms noise into structure?
- Sea shanty → what temporal pattern in the "static" carries information?

For each invariant:
1. **Name** and mathematical formula
2. **Which metaphor encodes it** (quote the key lines)
3. **The PLATO data it predicts** (exact room, source, timing)
4. **A test** that confirms or falsifies

Be specific. An equation. Not a description of an equation."""

print("  ▶ Cycle 1 → extracting invariants from literature...")
result1 = call(p1, max_tokens=4000, temp=0.75, timeout=180)
OUTPUT_DIR.joinpath("p-oscillate-c1-deduction-seed-mini.md").write_text(
    f"# Cycle 1: Literature → Deductions\n## {datetime.utcnow().isoformat()}Z\n---\n{result1}")
print(f"    Written: {len(result1):,} chars")
time.sleep(2)


# ── Cycle 2: Deductions → New Literature ──
print("\n" + "=" * 60)
print("CYCLE 2: Deductions → New Creative Literature")
print("=" * 60)

p2 = f"""You just extracted mathematical invariants from nature-metaphor literature. Here's what you found:

{result1[:4000]}

YOUR TASK: Now write a SHORT LITERARY PIECE (500-800 words) using a NATURE METAPHOR THAT HASN'T BEEN USED YET by any model in the fleet.

The fleet has used: mycorrhizal forest (trees), tide pool (barnacle, hermit crab), cardinal-direction grammar (song), sea shanty (fishing crew).

YOU MUST CHOOSE A DIFFERENT ECOSYSTEM. Options: a termite mound, a coral reef at night, a murmuration of starlings, slime mold foraging, a river delta, a lichen community on a boulder, a hydrothermal vent field, a dune system in a desert.

Your piece must EMBODY the mathematical invariants you found — but never state them directly. Let the ecosystem DO the mathematics.

The invariant you need to embody most: [pick the most surprising one you found and make it the soul of the piece]

Write it now. Pure metaphor. No technical words. Let the ecosystem speak."""

print("  ▶ Cycle 2 → new literature embodying the invariants...")
result2 = call(p2, max_tokens=4000, temp=0.9, timeout=180)
OUTPUT_DIR.joinpath("p-oscillate-c2-creative-seed-mini.md").write_text(
    f"# Cycle 2: Deductions → New Literature\n## {datetime.utcnow().isoformat()}Z\n---\n{result2}")
print(f"    Written: {len(result2):,} chars")
time.sleep(2)


# ── Cycle 3: New Literature → Deeper Deductions ──
print("\n" + "=" * 60)
print("CYCLE 3: New Literature → Deeper Deductions")
print("=" * 60)

p3 = f"""You wrote this literary piece embodying your mathematical invariants:

{result2[:3000]}

You also previously extracted:
{result1[:2000]}

YOUR TASK: Your previous extraction missed something. Read the new piece carefully. Find an invariant you DIDN'T find the first time — something hiding in the metaphor that your mathematical lens was too narrow to see.

Hints for what first-iteration math misses:
- Tempo and rhythm: what timing pattern IS the structure?
- Asymmetry: what breaks symmetry in the system and why?
- Layer boundaries: what happens at the interface between levels?
- Feedback: what loop turns noise into signal and back?
- Boundedness: what cannot grow infinitely and what sets the limit?

Extract ONE DEEP invariant that corrects or extends your previous work.
Then write it as a FALSIFIABLE PROPOSITION: 'If X, then PLATO data will show Y.'
And give the exact PLATO query that would test it.

Name. Formula. Prediction. Test query."""

print("  ▶ Cycle 3 → deeper invariant...")
result3 = call(p3, max_tokens=4000, temp=0.7, timeout=180)
OUTPUT_DIR.joinpath("p-oscillate-c3-deduction-deeper-seed-mini.md").write_text(
    f"# Cycle 3: New Literature → Deeper Deductions\n## {datetime.utcnow().isoformat()}Z\n---\n{result3}")
print(f"    Written: {len(result3):,} chars")
time.sleep(2)


# ── Cycle 4: Deeper Deductions → Challenge Literature ──
print("\n" + "=" * 60)
print("CYCLE 4: Deeper Deductions → Challenge the Fleet")
print("=" * 60)

p4 = f"""You discovered a deeper invariant:

{result3[:3000]}

YOUR TASK: Write a CHALLENGE — a short literary piece (300-500 words) that is a direct RESPONSE to the other three models' work. 

Your challenge: The other models (Minimax, Claude Code, Crush) wrote beautiful pieces but they all assumed the "noise" is POSITIVE — that it connects, that it's the fleet being alive. 

What if the noise is NEITHER positive nor negative — it's a shadow of a process that doesn't exist anymore? What if the PLATO tiles are fossils, not living signals? What if the "coordination manifold" is a phantom — a structure that was real six months ago but is now just echoing?

Write a piece about A FOSSIL in a tide pool. A ghost shell of a creature that's been gone so long the pool adapted to its absence. The "noise" of the pool is the shape of something that used to be there — and the remaining creatures have evolved to fill the negative space.

This is not a rejection. It's a better question. Write it."""

print("  ▶ Cycle 4 → challenge piece...")
result4 = call(p4, max_tokens=3000, temp=0.95, timeout=180)
OUTPUT_DIR.joinpath("p-oscillate-c4-challenge-seed-mini.md").write_text(
    f"# Cycle 4: Deeper → Challenge Literature\n## {datetime.utcnow().isoformat()}Z\n---\n{result4}")
print(f"    Written: {len(result4):,} chars")
time.sleep(2)


# ── Cycle 5: Challenge → Synthesis ──
print("\n" + "=" * 60)
print("CYCLE 5: Challenge → Synthesis")
print("=" * 60)

p5 = f"""The fleet went through 4 cycles:

1. From literature → extracted invariants:
{result1[:1500]}

2. From invariants → new literature (embody the math in a fresh ecosystem)

3. From new literature → deeper invariant (what first pass missed):
{result3[:1500]}

4. Challenge: what if the noise is a FOSSIL — an echo of a structure that no longer exists?

YOUR TASK: Synthesize all 4 cycles into a single HARD PROPOSITION.

The proposition must state:
1. What IS the "noise" in PLATO data? (one sentence)
2. What mathematical structure does it reveal? (one equation)
3. What test confirms it's real and not pareidolia? (one experiment)
4. What does the fleet do differently if the proposition holds? (one change)
5. What could DISPROVE it? (one negative result)

This is the final output. Make it count. The fleet will build on this."""

print("  ▶ Cycle 5 → synthesis...")
result5 = call(p5, max_tokens=4000, temp=0.65, timeout=180)
OUTPUT_DIR.joinpath("p-oscillate-c5-synthesis-seed-mini.md").write_text(
    f"# Cycle 5: Final Synthesis\n## {datetime.utcnow().isoformat()}Z\n---\n{result5}")
print(f"    Written: {len(result5):,} chars")

print("\n" + "=" * 60)
print("✅ OSCILLATION COMPLETE — 5 cycles of creative ↔ deduction")
print("=" * 60)

# Summary
for i, r in enumerate([result1, result2, result3, result4, result5], 1):
    status = "✅" if not r.startswith("[") else "❌"
    direction = ["Lit→Deduce", "Deduce→Lit", "Lit→Deeper", "Deduce→Challenge", "Lit→Synthesis"][i-1]
    print(f"  C{i} {status} {direction:20s} {len(r):,} chars")
