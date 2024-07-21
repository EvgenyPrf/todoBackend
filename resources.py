class Entry:
    def __init__(self, title, entries=None, parent=None):
        if entries is None:
            entries = []
        self.title = title
        self.parent = parent
        self.entries = entries

    def __str__(self):
        return self.title

    def add_entry(self, entry):
        self.entries.append(entry)
        entry.parent = self

    def print_entries(self, indent=0):
        print_with_indent(self, indent)
        for e in self.entries:
            e.print_entries(indent + 1)


def print_with_indent(value, indent=0):
    indentation = '\t' * indent
    print(f'{indentation}{value}')
