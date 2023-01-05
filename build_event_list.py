"""
This script builds a list of events from the game data. It is used
to build a fixed list of events that is used to filter the events
to. This is done to fix this tool to specific game versions as per
request by the game developers. They'd like this tool not to give
away event paths for no public versions of the game yet to let
people discover them manually.
"""
from game_data import load_game_data

# Load the game data
game_path = "D:\\Games\\Dult\\LessonsInLove0.27.0-0.27.0-pc-subscribestar"
events, save_data, characters, save_file, save_file_timestamp = load_game_data(game_path)

# Build the list of events
event_ids = []
for event in events.values():
    event_ids.append(event["id"])

# Output the list as a python list format
with(open("event_ids.py", "w")) as f:
  # Write the event ids in chunks of 100 characters per line
  f.write("VALID_EVENTS = set([\n  ")
  length = 0
  for i in range(0, len(event_ids)):
    if length > 100:
      f.write("\n  ")
      length = 0
    f.write("\"" + event_ids[i] + "\", ")
    length += len(event_ids[i]) + 3
  f.write("\n])\n")

