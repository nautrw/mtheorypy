from mtheorypy.keys import Key

BASE_SCALE = [0, 2, 4, 5, 7, 9, 11]


def get_base(root):
    base_scale = []
    current_root = root
    for i in range(7):
        base_scale.append((current_root + BASE_SCALE[i]) % 12)
        current_root = (current_root + 12) % 12

    return base_scale


def modify(base_scale, indices, flatten: bool = True):
    return [(v + (-1 if flatten else 1)) % 12 if i in indices
            else v for i, v in enumerate(base_scale)]


class Scale(Key):
    def __init__(self, sharps):
        super().__init__(sharps)
        self.root = self.sharps % 12
        self.major = get_base(self.root)
        self.minor = modify(self.major, [2, 5, 6])
        self.pentatonic = self.major[:3] + self.major[4:6]
        self.dorian = modify(self.major, [2, 6])
        self.phrygian = modify(self.major, [1, 2, 5, 6])
        self.lydian = modify(self.major, [3], False)
        self.myxolidian = modify(self.major, [6])
        self.locrian = modify(self.major, [1, 2, 4, 5, 6])
