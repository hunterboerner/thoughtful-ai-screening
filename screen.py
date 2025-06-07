def sort(width, height, length, mass):
  bulky = width >= 150 or height >= 150 or length >= 150 or width * length * height >= 1_000_000
  heavy = mass >= 20

  if bulky and heavy:
    return "REJECTED"

  if bulky or heavy:
    return "SPECIAL"

  return "STANDARD"
