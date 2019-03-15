import math

width = float(input())
depth = float(input())
height = float(input())

volume_of_truck = width*depth*height

barrels_number = int(input())
count_of_barrels = 0

is_truck_full = False

for barrel in range(barrels_number):
    barrel_r = float(input())
    barrel_h = float(input())
    volume_of_barrel = math.pi * math.pow(barrel_r, 2) * barrel_h

    if volume_of_truck - volume_of_barrel >= 0:
        count_of_barrels += 1
        volume_of_truck = volume_of_truck - volume_of_barrel
    else:
        print(f'Truck is full. {count_of_barrels} on board!')
        is_truck_full = True
        break


if not is_truck_full:
    print(f'All barrels on board. Capacity left - {volume_of_truck:.2f}.')