# Quick Start - The Curiosity Project

## Start in 3 Steps

### Step 1: Install Frontend Dependencies
```bash
cd curiosity-project/frontend
npm install
```

### Step 2: Start the Dev Server
```bash
npm run dev
```

You should see:
```
▲ Next.js 14.0.0
- Local:        http://localhost:3000
- Environments: .env.local

✓ Ready in 1.2s
```

### Step 3: Open Your Browser
Visit **http://localhost:3000**

You should see the Curiosity Project archive with one exploration: "Emergence: How Complexity Arises from Simplicity"

---

## Generate More Explorations

In a new terminal, from the `curiosity-project` directory:

```bash
python3 scripts/nightly-generate.py
```

Then refresh your browser to see the new exploration appear.

---

## What You're Looking At

**Home page:** Grid of all explorations, newest first. Each card shows:
- Date generated
- Exploration title
- The guiding question
- Summary
- Topic tags

**Click any card** to read the full exploration with:
- Complete reasoning and content
- Multiple perspectives from different viewpoints
- Connected ideas and themes
- Open questions for further exploration

---

## Architecture at a Glance

```
┌─────────────┐
│   Browser   │ http://localhost:3000
│  (Next.js)  │
└──────┬──────┘
       │ API calls
       ▼
┌──────────────────┐
│  API Routes      │ pages/api/explorations*.ts
│ (Read JSON)      │
└──────┬───────────┘
       │ filesystem
       ▼
┌──────────────────┐
│  JSON Files      │ explorations/*.json
│  (Storage)       │ data/metadata/*.json
└──────────────────┘
       ▲
       │ written by
┌──────┴───────────┐
│  Generator       │ backend/generator.py
│ (Python)         │
└──────────────────┘
```

---

## Nightly Automation (Setup Needed)

Once you set up the scheduled routine in Claude Code, it will automatically run `scripts/nightly-generate.py` each night, creating new explorations for you to discover in the morning.

---

## Project Files

- **docs/VISION.md** - Long-term direction and philosophy
- **docs/GETTING_STARTED.md** - Detailed setup guide
- **docs/PROJECT_STATUS.md** - Current state and roadmap
- **docs/NIGHTLY_ROUTINE.md** - How autonomous generation works

---

**Ready to explore?** Open http://localhost:3000 and dive into the first night's curiosity about emergence.

🌙✨
