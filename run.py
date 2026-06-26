from typing import List, cast
from PIL import Image
from music21 import stream, note, instrument

img = Image.open("SyntronicLabsStandup.png").convert("L")

s = stream.Stream()
s.append(instrument.Piano())

# Convert image data to list first, then slice
pixels: List[int] = cast(List[int], list(img.getdata()))
for pixel in pixels[::500]:
  n = note.Note(60 + pixel//15)
  s.append(n)

# Export to MIDI file
s.write('midi', fp='output.mid')
print("✓ MIDI file saved as 'output.mid'")
print(f"✓ Generated {len(pixels[::500])} notes from image")
