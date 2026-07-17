#!/usr/bin/env python3
"""
Nightly exploration generator - called by Claude Code's scheduled agent.
This is the entry point for autonomous nightly curiosity generation.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'backend'))

from generator import ExplorationGenerator
from datetime import datetime
import random

# Curated list of fascinating topics to explore
CURIOSITY_TOPICS = [
    {
        "title": "The Hard Problem of Consciousness",
        "question": "Why does subjective experience seem irreducible to physical description?",
        "domain": "philosophy"
    },
    {
        "title": "Quantum Entanglement and Locality",
        "question": "How do particles remain connected across infinite distance?",
        "domain": "physics"
    },
    {
        "title": "The Origin of Life",
        "question": "How did self-replicating chemistry emerge from non-living chemistry?",
        "domain": "biology"
    },
    {
        "title": "Language Evolution",
        "question": "How did the capacity for symbolic communication arise in humans?",
        "domain": "linguistics"
    },
    {
        "title": "Why Mathematics Works",
        "question": "Why does abstract mathematics describe physical reality so accurately?",
        "domain": "mathematics"
    },
    {
        "title": "Creativity and Novelty",
        "question": "What allows minds to generate genuinely new ideas rather than combinations?",
        "domain": "psychology"
    },
    {
        "title": "Time's Arrow",
        "question": "Why does time flow in one direction while physical laws are reversible?",
        "domain": "physics"
    },
    {
        "title": "Artificial General Intelligence",
        "question": "What's missing in current AI systems for human-like reasoning?",
        "domain": "ai"
    },
    {
        "title": "Beauty in Mathematics",
        "question": "Is mathematical beauty a guide to truth or subjective preference?",
        "domain": "mathematics"
    },
    {
        "title": "Free Will and Determinism",
        "question": "Can genuine choice exist in a determined or probabilistic universe?",
        "domain": "philosophy"
    }
]

def select_topic():
    """Select a topic for tonight's exploration."""
    return random.choice(CURIOSITY_TOPICS)

def generate_stub_exploration(topic):
    """Generate a basic exploration scaffold."""
    gen = ExplorationGenerator()

    content = f"""
    <p>Tonight's exploration focuses on a fundamental question in {topic['domain']}: {topic['question']}</p>

    <h2>The Core Question</h2>
    <p>{topic['question']}</p>

    <p>This is a placeholder exploration. The full research and multi-perspective analysis would be generated here through deep reasoning about the topic.</p>

    <h2>What We Might Explore</h2>
    <ul>
        <li>Historical context and how thinking has evolved</li>
        <li>Current scientific or philosophical understanding</li>
        <li>Multiple perspectives from different disciplines</li>
        <li>Open questions and unsolved mysteries</li>
        <li>Connections to other areas of knowledge</li>
    </ul>
    """

    perspectives = [
        {
            "title": "Scientific Perspective",
            "description": "What does empirical investigation tell us?"
        },
        {
            "title": "Philosophical Perspective",
            "description": "How do we reason about the conceptual foundations?"
        },
        {
            "title": "Historical Perspective",
            "description": "How has thinking about this evolved over time?"
        }
    ]

    connections = [
        "Historical context",
        "Related unsolved problems",
        "Interdisciplinary connections",
        "Technological implications"
    ]

    open_questions = [
        f"What is the current state of understanding around this question?",
        f"What evidence would resolve this question?",
        f"How does this connect to other fundamental questions?"
    ]

    return gen.create_exploration(
        title=topic['title'],
        question=topic['question'],
        summary=f"An exploration of {topic['title'].lower()}",
        content=content,
        tags=[topic['domain'], "exploration", "research"],
        perspectives=perspectives,
        connections=connections,
        open_questions=open_questions
    )

def main():
    print(f"🌙 Curiosity Project - Nightly Generation")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Select a topic for tonight
    topic = select_topic()
    print(f"✨ Tonight's curiosity: {topic['title']}")
    print(f"❓ {topic['question']}")
    print()

    # Generate the exploration
    exploration_id = generate_stub_exploration(topic)
    print(f"✅ Exploration generated: {exploration_id}")
    print()

    print("Morning awaits! Check the archive at http://localhost:3000")

if __name__ == "__main__":
    main()
