from dataclasses import dataclass

from scales import SCALES

# (Major, Minor)
KEYS = [
    (11, 8),  # Cb, Ab
    (6, 3),   # Gb, Eb
    (1, 10),  # Db, Bb
    (8, 5),   # Ab, F
    (3, 0),   # Eb, C
    (10, 7),  # Bb, G
    (5, 2),   # F, D
    (0, 9),   # C, A
    (7, 4),   # G, E
    (2, 11),  # D, B
    (9, 6),   # A, F#
    (4, 1),   # E, C#
    (11, 8),  # B, G#
    (6, 3),   # F#, D#
    (1, 10),  # C#, A#
]

BASE_SCALE = [0, 2, 4, 5, 7, 9, 11]

CIRCLE_OF_FIFTHS = [5, 0, 7, 2, 9, 4, 11]


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
                signature.append(list(reversed(CIRCLE_OF_FIFTHS))[i])
        else:
            for i in range(accidentals):
                signature.append(CIRCLE_OF_FIFTHS[i] + 1)

        return signature
