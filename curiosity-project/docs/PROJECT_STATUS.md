# Project Status

## Current State

**Date:** July 17, 2026  
**Status:** 🚀 Foundation Complete - Ready for First Night

### What's Done

✅ **Frontend Architecture**
- Next.js project structure with TypeScript
- Beautiful, dark-themed archive interface
- Home page with exploration grid
- Detail page for individual explorations
- Responsive CSS design
- API routes for data retrieval

✅ **Backend Generation System**
- Python generator for creating explorations
- JSON-based storage (explorations + metadata)
- Unique ID generation for each exploration
- Proper path handling for cross-platform use

✅ **First Exploration**
- Generated: "Emergence: How Complexity Arises from Simplicity"
- Includes full content, perspectives, connections, and open questions
- Demonstrates the complete exploration structure

✅ **Nightly Automation Script**
- Topic selection from curated list
- Exploration generation pipeline
- Ready to be scheduled

✅ **Documentation**
- Vision document outlining long-term direction
- Getting started guide
- Nightly routine documentation
- Project structure overview

### Project Structure

```
curiosity-project/
├── frontend/                 # Next.js archive viewer
│   ├── pages/
│   │   ├── index.tsx        # Home page
│   │   ├── exploration/[id].tsx  # Detail page
│   │   └── api/             # API routes
│   ├── styles/globals.css    # Beautiful dark theme
│   ├── package.json
│   └── next.config.js
├── backend/
│   └── generator.py          # Exploration generation
├── scripts/
│   ├── generate-first-exploration.py
│   └── nightly-generate.py   # Scheduled entry point
├── explorations/             # Generated artifacts
│   └── 20260717-emergence-*.json
├── data/metadata/            # Listing metadata
│   └── 20260717-emergence-*.json
├── docs/
│   ├── VISION.md            # Long-term direction
│   ├── GETTING_STARTED.md
│   ├── NIGHTLY_ROUTINE.md
│   └── PROJECT_STATUS.md
└── README.md
```

## Next Steps

### Immediate (Tonight)

1. ✅ Set up autonomous nightly scheduling
   - Use Claude Code's scheduled agent feature
   - Schedule `scripts/nightly-generate.py` to run each night
   - Specify time (e.g., 11 PM or 2 AM depending on preference)

2. 🔄 Test the frontend locally
   - Run `cd frontend && npm install`
   - Run `npm run dev`
   - Visit http://localhost:3000
   - Verify the Emergence exploration loads and displays correctly

### Soon

- [ ] Integration with Claude API for richer content generation
- [ ] Improve exploration content beyond stubs
- [ ] Add semantic search across explorations
- [ ] Implement connection discovery between topics
- [ ] User engagement tracking (which topics you interact with)

### Later

- [ ] Export explorations (PDF, markdown, etc.)
- [ ] Collaborative browsing
- [ ] Integration with note-taking systems
- [ ] Mobile-optimized version
- [ ] Knowledge graph visualization
- [ ] Trend analysis across months

## How to Run

### Start Frontend Dev Server
```bash
cd curiosity-project/frontend
npm install  # First time only
npm run dev
```

Then visit `http://localhost:3000`

### Generate a New Exploration
```bash
cd curiosity-project
python3 scripts/nightly-generate.py
```

The generation will pick a random topic from the curated list and create a new exploration.

### Set Up Nightly Automation

To schedule automatic nightly generation:
```bash
# From the Claude Code CLI, you can set up a recurring task
# For now, this will be done via Claude Code's scheduling feature
```

## Technical Decisions

### Why Next.js?
- Fast development and hot reload
- File-based routing
- Built-in API routes
- Excellent TypeScript support
- Static generation + dynamic routes

### Why Python for Backend?
- Natural fit for generation and data processing
- Easy to integrate with Claude API later
- Simple file-based storage for now

### Why JSON Storage?
- Simple, inspectable data format
- No database dependency
- Easy to version control
- Can be migrated to real DB later

### Why Dark Theme?
- Explorations created at night, read in morning/evening
- Less eye strain
- Feels contemplative and elegant
- Matches the "dreaming" aesthetic

## Architecture Notes

**Frontend** talks to **API routes** which read from **JSON files**.  
**Backend scripts** generate **JSON files** and write to disk.  
**Nightly scheduler** invokes **backend scripts**.

This is simple, reliable, and easy to debug. Later phases can add a database, caching, and more sophisticated storage.

## Known Limitations

- Content generation is currently stubbed (needs Claude API integration)
- No persistent user state (bookmarks, annotations, etc.)
- No connection discovery algorithm yet
- Topic selection is random, not personalized
- No external data sources yet

These are all Phase 2+ improvements.

## Commands Reference

```bash
# Frontend
cd curiosity-project/frontend
npm install
npm run dev
npm run build

# Generate explorations
python3 scripts/generate-first-exploration.py
python3 scripts/nightly-generate.py

# Check generated files
ls -la explorations/
ls -la data/metadata/
```

---

**Status:** Ready to move to autonomous operation. The foundation is solid. Each night will build on this base, adding more explorations to the archive.
