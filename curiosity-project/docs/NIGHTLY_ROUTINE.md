# Nightly Curiosity Generation

This document describes how the autonomous nightly generation works.

## How It Works

Each night, the Curiosity Project automatically:

1. **Selects a topic** - Based on recent trends, emerging interests, or random selection from a curated list
2. **Researches and explores** - Deep analysis from multiple perspectives
3. **Generates an artifact** - Creates an interactive exploration with insights
4. **Archives it** - Stores metadata and full content for retrieval
5. **Updates indices** - Makes it discoverable in the archive

## Triggering Generation

### Manual Generation

Run directly:
```bash
cd curiosity-project
python3 scripts/generate-first-exploration.py
python3 scripts/generate-random-exploration.py
```

### Automated Nightly Generation

The system will run automatically each night via Claude Code's scheduled agent feature.

The scheduler will execute: `scripts/nightly-generate.py`

## Adding New Explorations

To create a new exploration programmatically:

```python
from backend.generator import ExplorationGenerator

gen = ExplorationGenerator()
gen.create_exploration(
    title="Your Question Here",
    question="What specific question are we exploring?",
    summary="One sentence summary of the exploration",
    content="<p>Full HTML content</p>",
    tags=["tag1", "tag2"],
    perspectives=[...],
    connections=[...],
    open_questions=[...]
)
```

## Topic Selection Strategy

Topics are selected from several sources:

1. **Curated curiosities** - Pre-selected interesting questions
2. **Semantic drift** - Connections between previous explorations
3. **Random interesting domains** - Physics, philosophy, biology, technology, art
4. **User feedback** - If you've mentioned something interesting
5. **Emergent patterns** - Topics that connect multiple previous explorations

## Storage Structure

```
explorations/
├── 20260717-emergence-how-complexity-arise-5c4044.json    # Full exploration
├── 20260718-quantum-entanglement-weirdness-a3f9b2.json
└── ...

data/metadata/
├── 20260717-emergence-how-complexity-arise-5c4044.json    # Metadata only (for listing)
└── ...
```

## Monitoring

Check the exploration archive each morning to see:
- What was explored overnight
- New connections discovered
- Emerging themes across explorations
- Open questions for future investigation

## Future Enhancements

- [ ] Learning from user interactions (which topics you engage with most)
- [ ] Cross-exploration connection discovery
- [ ] Collaborative browsing/annotation
- [ ] Export explorations in different formats
- [ ] Topic trend analysis
- [ ] Integration with knowledge graphs
