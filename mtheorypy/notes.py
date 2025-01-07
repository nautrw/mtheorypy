from dataclasses import dataclass


@dataclass
class Note:
    number: int
    length: int
    octave: int


def get_note_name(note: Note, accidental: str = "#"):
    if note.number not in range(11):
        raise IndexError(f"note number out of bounds (0-11): {note.number}")

    if accidental not in ["#", "b"]:
        raise ValueError("argument `accidental` must be either `#` or `b`")

    sharp_notes = ["C", "C#", "D", "D#", "E",
                   "F", "F#", "G", "G#", "A", "A#", "B"]
    flat_notes = ["C", "Db", "D", "Eb", "E",
                  "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    if accidental == "#":
        return sharp_notes[note.number]
    else:
        return flat_notes[note.number]
