import json
import os

from app.config.settings import settings


class Memory:
    def __init__(self):
        self.file = settings.MEMORY_FILE
        self.data = {}

        self.load()

    def load(self):
        if os.path.exists(self.file):
            with open(self.file, "r") as f:
                self.data = json.load(f)
        else:
            self.save()

    def save(self):
        os.makedirs("data", exist_ok=True)

        with open(self.file, "w") as f:
            json.dump(self.data, f, indent=4)

    def remember(self, category, key, value):
        if category not in self.data:
            self.data[category] = {}

        self.data[category][key] = value

        self.save()

    def recall(self, category):
        return self.data.get(category, {})


memory = Memory()
