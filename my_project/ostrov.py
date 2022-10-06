def fly_by(lamps, drone):
    return "o" * len(drone) + lamps[len(drone)+1:]


print(fly_by( 'xx', 'T'))