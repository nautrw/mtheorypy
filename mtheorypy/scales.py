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

        minor_scale = [v-1 if i in [2, 5, 6]
                       else v for i, v in enumerate(base_scale)]
        # TODO: ADD MORE MODES
        scales_dict = {
            "major": {
                "base": base_scale
            },
            "minor": {
                "base": minor_scale
            }
        }

        return scales_dict
