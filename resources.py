class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.entries = entries
        self.parent = parent

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for e in self.entries:
            e.print_entries(indent + 1)

    def json(self):
        return {
            'title': self.title,
            'entries': [entry.json() for entry in self.entries]
        }

    @classmethod
    def from_json(cls, value):
        new_entry = cls(value['title'])
        for entry in value.get('entries', []):
            new_entry.add_entry(cls.from_json(entry))
        return new_entry


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(f'{indentation}{value}')
