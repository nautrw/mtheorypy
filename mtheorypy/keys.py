from dataclasses import dataclass

from notes import CIRCLE_OF_FIFTHS

# (Major, Minor)
KEYS = [
    (11, 8),  # Cb to Ab
    (6, 3),   # Gb to Eb
    (1, 10),  # Db to Bb
    (8, 5),   # Ab to F
    (3, 0),   # Eb to C
    (10, 7),  # Bb to G
    (5, 2),   # F to D
    (0, 9),   # C to A
    (7, 4),   # G to E
    (2, 11),  # D to B
    (9, 6),   # A to F#
    (4, 1),   # E to C#
    (11, 8),  # B to G#
    (6, 3),   # F# to D#
    (1, 10),  # C# to A#
]

BASE_SCALE = [0, 2, 4, 5, 7, 9, 11]


@dataclass
class Key:
    sharps: int

    def validate(self) -> None:
        if self.sharps not in range(-7, 8):
            raise IndexError(
                f'number of sharps out of bounds (-7 to 7): {self.sharps}')

    def get_names(self) -> tuple:
        self.validate()
        return KEYS[self.sharps + 7]

    def get_signature(self):
        self.validate()
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


key = Key(-2)
print(key.get_names())
