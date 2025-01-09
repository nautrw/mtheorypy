from dataclasses import dataclass

from notes import CIRCLE_OF_FIFTHS

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

    def get_signature(self):
        accidentals = self.sharps
        signature = []

        if self.sharps < 0:
            for i in range(-accidentals):
                signature.append(
                    f"{list(reversed(CIRCLE_OF_FIFTHS))[i]}b")
        else:
            for i in range(accidentals):
                signature.append(f"{CIRCLE_OF_FIFTHS[i]}#")

        return signature
