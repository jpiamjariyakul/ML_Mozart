import py_midicsv

# Load the MIDI file and parse it into CSV format
csv_string = py_midicsv.midi_to_csv("./midi_sonatas/mz_311_1.mid")
print(csv_string)

# # Parse the CSV output of the previous command back into a MIDI file
# midi_object = py_midicsv.csv_to_midi(csv_string)

# # Save the parsed MIDI file to disk
# with open("example_converted.mid", "wb") as output_file:
#     midi_writer = py_midicsv.FileWriter(output_file)
#     midi_writer.write(midi_object)