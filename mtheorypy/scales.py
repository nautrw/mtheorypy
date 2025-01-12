from dataclasses import dataclass

from keys import Key

BASE_SCALE = [0, 2, 4, 5, 7, 9, 11]


@dataclass
class Scale(Key):
    def get_scales(self):
        self.validate()
        root = self.sharps % 12

        base_scale = []
        current_root = root
        for i in range(7):
            base_scale.append((current_root + BASE_SCALE[i]) % 12)
            current_root = (current_root + 12) % 12

        def modify(indices, flatten: bool = True):
            return [(v + (-1 if flatten else 1)) % 12 if i in indices
                    else v for i, v in enumerate(base_scale)]

        # TODO: ADD MORE MODES
        scales_dict = {
            "major": base_scale,
            "minor": modify([2, 5, 6]),
            "pentatonic": base_scale[:3] + base_scale[4:6],
            "dorian": modify([2, 6]),
            "phrygian": modify([1, 2, 5, 6])
        }

        return scales_dict
