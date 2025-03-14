import math

# angles = [0, math.pi / 6, math.pi / 4, math.pi / 3, math.pi / 2, math.pi, math.pi * 3 / 2, math.pi * 2]
angles = [0, 30, 45, 60, 90, 180, 270, 360]

for angle in angles:
    print(f'{angle}: ')
    # sin = math.sin(angle) #if in radian for ex.: math.pi / 6
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))
    tg = math.tan(math.radians(angle))
    ctg = None if tg == 0.0 else 1 / tg
    print(f'sin(): {sin}')
    print(f'cos(): {cos}')
    print(f'tg(): {tg}')
    print(f'ctg(): {ctg}')
    print('-------------')
