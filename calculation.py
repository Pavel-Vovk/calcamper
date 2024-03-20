import math

class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def add(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def abs(self):
        return math.sqrt(self.re * self.re + self.im * self.im)

def polar_to_complex(magnitude, angle_degrees):
    angle_radians = (angle_degrees * math.pi) / 180
    return Complex(magnitude * math.cos(angle_radians), magnitude * math.sin(angle_radians))

def calculate_neutral_current(i1, i2, i3):
    phase1 = polar_to_complex(i1, 0)
    phase2 = polar_to_complex(i2, -120)
    phase3 = polar_to_complex(i3, 120)

    neutral = phase1.add(phase2).add(phase3)

    return neutral.abs()

def calculate_and_display():
    i1 = float(input("Введіть струм у фазі 1: "))
    i2 = float(input("Введіть струм у фазі 2: "))
    i3 = float(input("Введіть струм у фазі 3: "))

    neutral_current = calculate_neutral_current(i1, i2, i3)

    print(f"Ток на нейтралі: {neutral_current:.2f} A")

calculate_and_display()
