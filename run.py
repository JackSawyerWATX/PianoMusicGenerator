from PIL import Image
from music21 import stream, note

img = Image.open("SyntronicLabsStandup.png").convert("L")

s = stream.Stream()

# Convert image data to list first, then slice
pixels = list(img.getdata())
for pixel in pixels[::500]:
  n = note.Note(60 + pixel//15)
  s.append(n)

s.show('text')