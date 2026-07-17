#!/usr/bin/env python3
"""
Curiosity exploration generator.
Each night, this creates a new exploration artifact.
"""

import json
import os
from datetime import datetime
import re
import hashlib

class ExplorationGenerator:
    def __init__(self, output_dir=None, metadata_dir=None):
        if output_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            output_dir = os.path.join(base_dir, "explorations")
        if metadata_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            metadata_dir = os.path.join(base_dir, "data", "metadata")

        self.output_dir = output_dir
        self.metadata_dir = metadata_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(metadata_dir, exist_ok=True)

    def generate_id(self, title):
        """Generate a unique ID from title and timestamp."""
        timestamp = datetime.now().strftime("%Y%m%d")
        hash_suffix = hashlib.md5(f"{title}{timestamp}".encode()).hexdigest()[:6]
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower())[:30]
        return f"{timestamp}-{slug}-{hash_suffix}"

    def save_exploration(self, exploration):
        """Save exploration to disk."""
        exploration_id = exploration['id']

        # Save full exploration
        exp_path = os.path.join(self.output_dir, f"{exploration_id}.json")
        with open(exp_path, 'w') as f:
            json.dump(exploration, f, indent=2)

        # Save metadata for listing
        metadata = {
            'id': exploration['id'],
            'date': exploration['date'],
            'title': exploration['title'],
            'question': exploration['question'],
            'summary': exploration['summary'],
            'tags': exploration['tags']
        }

        meta_path = os.path.join(self.metadata_dir, f"{exploration_id}.json")
        with open(meta_path, 'w') as f:
            json.dump(metadata, f, indent=2)

        return exploration_id

    def create_exploration(self, title, question, summary, content, tags,
                          perspectives=None, connections=None, open_questions=None):
        """Create and save a new exploration."""
        exploration_id = self.generate_id(title)

        exploration = {
            'id': exploration_id,
            'date': datetime.now().isoformat(),
            'title': title,
            'question': question,
            'summary': summary,
            'content': content,
            'tags': tags,
            'perspectives': perspectives or [],
            'connections': connections or [],
            'openQuestions': open_questions or []
        }

        saved_id = self.save_exploration(exploration)
        return saved_id

# Standalone generation script
if __name__ == "__main__":
    gen = ExplorationGenerator()
    print("Curiosity generator initialized.")
