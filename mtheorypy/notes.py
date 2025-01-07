from __future__ import annotations

from dataclasses import dataclass

SHARP_NOTES = ["C", "C#", "D", "D#", "E",
               "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_NOTES = ["C", "Db", "D", "Eb", "E",
              "F", "Gb", "G", "Ab", "A", "Bb", "B"]


@dataclass
class Note:
    number: int
    length: int
    octave: int

    def get_name(self, accidental: str = "#") -> str:
        if self.number not in range(11):
            raise IndexError(
                f"note number out of bounds (0-11): {self.number}")

        if accidental not in ["#", "b"]:
            raise ValueError("argument `accidental` must be either `#` or `b`")

        if accidental == "#":
            return SHARP_NOTES[self.number]
        else:
            return FLAT_NOTES[self.number]

    def is_enharmonic(self, target_note: Note) -> bool:
        return self.number == target_note.number
