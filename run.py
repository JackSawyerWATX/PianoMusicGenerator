from PIL import Image
from music21 import stream, note, instrument

img = Image.open("SyntronicLabsStandup.png").convert("L")

s = stream.Stream()
s.append(instrument.Piano())

# Convert image data to list first, then slice
pixels = list(img.getdata())
for pixel in pixels[::500]:
  n = note.Note(60 + pixel//15)
  s.append(n)

# Export to MIDI file
s.write('midi', fp='output.mid')
print("✓ MIDI file saved as 'output.mid'")
print(f"✓ Generated {len(list(img.getdata())[::500])} notes from image")
