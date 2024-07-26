from resources import Entry
from typing import List
import os


class EntryManager:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.entries: List[Entry] = []

    def save(self):
        for entry in self.entries:
            entry.save(self.data_path)

    def load(self):
        for item in os.listdir(self.data_path):
            if item.endswith('.json'):
                self.entries.append(Entry.load(os.path.join(self.data_path, item)))

    def add_entry(self, title: str):
        self.entries.append(Entry(title))
