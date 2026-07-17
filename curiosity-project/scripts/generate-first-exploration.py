#!/usr/bin/env python3
"""
Generate the first exploration: Emergence
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from generator import ExplorationGenerator

def create_emergence_exploration():
    gen = ExplorationGenerator()

    content = """
    <p>Emergence is perhaps one of the most profound phenomena in nature: the appearance of complex, organized, intelligent-seeming behavior from simple rules applied locally. A murmuration of starlings exhibits breathtaking coordinated movement, yet each bird only follows three simple rules relative to its neighbors. Consciousness might emerge from billions of neurons firing according to electrochemical laws. Markets exhibit boom and bust cycles that no individual trader intends.</p>

    <h2>The Core Paradox</h2>
    <p>How can intelligence, beauty, and complexity emerge from simple rules? This is not metaphorical—it's deeply literal. A single ant is dumb. The colony is brilliant. No central planner coordinates the hive. Each bee follows local rules: "Dance if you found nectar. Follow dances you see. Come home when loaded."</p>

    <p>From this emerges: optimal route-finding, dynamic load-balancing, crisis response, collective memory spanning generations of individual organisms.</p>

    <h2>Why This Matters</h2>
    <p>Emergence explains how the universe got from dead matter to living things, from individual cells to ecosystems, from simple brains to consciousness. It's the bridge between the physics we understand (local rules) and the complexity we observe (global patterns).</p>

    <p>But there's something almost troubling about it: if emergence is everywhere, what room is left for traditional causation? If wholes arise from parts, can we predict wholes from parts? The answer seems to be: sometimes spectacularly yes, often surprisedly no.</p>

    <h2>Where Emergence Breaks Down</h2>
    <p>Not every system with simple local rules produces meaningful emergence. Some produce only noise. The difference between "organized emergence" and "chaotic noise" is still not fully understood. Why does this set of local rules produce a symphony and that one produces static?</p>

    <p>This is where emergence borders on magic—and where we find the deepest unsolved problems in complexity theory.</p>
    """

    perspectives = [
        {
            "title": "Physics Perspective",
            "description": "Phase transitions and symmetry breaking explain emergence at scales from particle physics to cosmology. Order arises naturally when systems reach critical thresholds."
        },
        {
            "title": "Biology Perspective",
            "description": "Life itself is emergence: DNA → proteins → cells → organisms → ecosystems. Each level has properties that couldn't be predicted from the previous level alone."
        },
        {
            "title": "Computer Science Perspective",
            "description": "Artificial life and agent-based models show emergence is computable. Simple CA rules produce Turing-complete systems. But predicting emergent behavior remains hard."
        },
        {
            "title": "Philosophy Perspective",
            "description": "Does emergence resolve the mind-body problem? If consciousness emerges from neurons, is it 'real' or 'just' physical? The debate hinges on what emergence actually means."
        }
    ]

    connections = [
        "Self-organization in complex systems",
        "Phase transitions and critical phenomena",
        "Information theory and entropy",
        "Evolution and natural selection",
        "Chaos theory and sensitivity to initial conditions",
        "Artificial life and agent-based modeling",
        "Consciousness and the hard problem of qualia"
    ]

    open_questions = [
        "Can we predict emergent behavior from first principles, or is emergence fundamentally unpredictable?",
        "What distinguishes creative emergence from destructive chaos?",
        "Does consciousness emerge from neural activity, or does it require something more?",
        "Are there universal laws of emergence that work across all domains?",
        "Can we harness emergence to solve problems no algorithm can crack?"
    ]

    gen.create_exploration(
        title="Emergence: How Complexity Arises from Simplicity",
        question="If all we have are simple local rules, where does complexity come from?",
        summary="A deep dive into how simple rules interact to create complex, intelligent-seeming behavior—from ant colonies to human consciousness.",
        content=content,
        tags=["complexity", "systems-thinking", "philosophy", "emergence", "ai"],
        perspectives=perspectives,
        connections=connections,
        open_questions=open_questions
    )

    print("✨ First exploration created: Emergence")
    print("Navigate to http://localhost:3000 to explore")

if __name__ == "__main__":
    create_emergence_exploration()
