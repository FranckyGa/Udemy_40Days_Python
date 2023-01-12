def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet":feet, "inches": inches}          #use dictionary as output to be able to use these numbers later


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
