from dataclasses import dataclass


@dataclass
class Note:
    number: int
    length: int
    octave: int
