from dataclasses import dataclass

# (Major, Minor)
KEYS = [
    ("Cb", "Ab"),
    ("Gb", "Eb"),
    ("Db", "Bb"),
    ("Ab", "F"),
    ("Eb", "C"),
    ("Bb", "G"),
    ("F", "D"),
    ("C", "A"),
    ("G", "E"),
    ("D", "B"),
    ("A", "F#"),
    ("E", "C#"),
    ("B", "G#"),
    ("F#", "D#"),
    ("C#", "A#"),
]

BASE_SCALE = ["C", "D", "E", "F", "G", "A", "B"]


@dataclass
class Key:
    sharps: int

    def get_name(self) -> tuple:
        return KEYS[self.sharps + 7]
