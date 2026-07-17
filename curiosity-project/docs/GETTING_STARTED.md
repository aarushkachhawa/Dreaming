# Getting Started with The Curiosity Project

## Overview

The Curiosity Project is an autonomous research system that explores one fascinating topic each night, creating beautifully-presented interactive explorations you can browse in the morning.

## Project Structure

```
curiosity-project/
├── frontend/                 # Next.js web app (the archive viewer)
├── backend/                  # Python generation logic
├── scripts/                  # Automation scripts
├── explorations/             # Generated exploration artifacts (JSON)
├── data/metadata/            # Metadata for listings and search
└── docs/                     # Documentation
```

## Quick Start

### 1. Setup Frontend Dependencies

```bash
cd curiosity-project/frontend
npm install
```

### 2. Start the Frontend Dev Server

```bash
npm run dev
```

The archive interface will be available at `http://localhost:3000`

### 3. Generate Explorations

From the `curiosity-project` directory:

```bash
# Generate the first exploration (already done)
python3 scripts/generate-first-exploration.py

# Generate a random exploration from the curated list
python3 scripts/nightly-generate.py
```

## What You'll See

### The Archive Interface

**Home page** (`/`):
- Grid of all explorations with dates and summaries
- Click on any card to read the full exploration
- Beautiful, dark theme optimized for late-night and morning reading

**Exploration detail** (`/exploration/[id]`):
- Full content and reasoning
- Multiple perspectives on the topic
- Connected ideas and open questions
- Backlink to browse more

## How It Works

### Generation Flow

1. **Topic selection** - Choose from curated list or emerging interests
2. **Research & reasoning** - Deep exploration of the topic
3. **Multi-perspective analysis** - View from different disciplines
4. **Artifact creation** - Generate beautiful presentation
5. **Archival** - Store for future discovery

### Storage

- **Full explorations**: `explorations/*.json` - Complete with content
- **Metadata**: `data/metadata/*.json` - Used for listing and search

Each exploration contains:
- `id` - Unique identifier based on date and topic
- `date` - When it was generated
- `title` - The exploration title
- `question` - The guiding question
- `summary` - One-line summary
- `content` - Full HTML content
- `tags` - Topic tags for discovery
- `perspectives` - Multiple ways to think about the topic
- `connections` - Related ideas
- `openQuestions` - Unanswered questions for further exploration

## Next Steps

### Running Nightly

Once automated scheduling is set up, the project runs autonomously each night:

```bash
python3 scripts/nightly-generate.py
```

Visit the archive the next morning to see what was explored.

### Customization

**Add new topics** in `scripts/nightly-generate.py`:
```python
CURIOSITY_TOPICS = [
    {
        "title": "Your Question",
        "question": "What do you want to understand?",
        "domain": "domain"
    },
    # ...
]
```

**Enhance explorations** by improving the content generation in `backend/generator.py`

**Customize the UI** by editing `frontend/styles/globals.css`

## Development

### Frontend Stack
- Next.js for the archive interface
- React for interactive components
- TypeScript for type safety
- CSS for beautiful, responsive design

### Backend Stack
- Python for generation logic
- JSON for data storage
- File-based (no database yet)

### Making Changes

```bash
# Edit frontend
cd frontend
npm run dev

# Edit backend/scripts
python3 scripts/your-script.py

# Check both work
npm run build  # in frontend
```

## Troubleshooting

**Port 3000 already in use?**
```bash
npm run dev -- -p 3001
```

**Explorations not showing?**
- Check that `explorations/*.json` files exist
- Check that `data/metadata/*.json` files exist
- Restart the dev server

**Python script errors?**
```bash
python3 -c "from backend.generator import ExplorationGenerator; print('OK')"
```

## Future Enhancements

- Integration with Claude API for richer content generation
- Semantic search and connection discovery
- User annotations and reflections
- Export to multiple formats
- Mobile-optimized interface
- Collaborative browsing
- Topic recommendations based on patterns

---

**Ready?** Start the frontend dev server and explore the first night's curiosity about emergence!
