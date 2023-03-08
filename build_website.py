
from string import Template
from game_data import load_game_data

if __name__ == "__main__":
  # Load the template
  with open("index.template", "r") as f:
    template = Template(f.read())
    
  # Load the game data
  game_path = "D:\\Games\\Dult\\LessonsInLove0.28.0-0.28.0-pc-subscribestar"
  events, save_data, characters, save_file, save_file_timestamp = load_game_data(game_path)

  # Build the list of event names supported
  event_groups = {}
  for event in events.values():
    if event["group"] not in event_groups:
      event_groups[event["group"]] = []
    event_groups[event["group"]].append(event["name"])

  character_event_md = ""
  for character in characters:
    character_event_md += "### " + character + "\n"
    character_event_md += "  * " + "\n  * ".join(event_groups[character]) + "\n\n"
  
  main_event_md = "### Main Events\n"
  main_event_md += "  * " + "\n  * ".join(event_groups["Main"]) + "\n\n"
  

  
  # Replace the 'main_events' and 'character_events' in the template in utf format
  """with open("./website/index.md", "w") as f:
    f.write(template.substitute(
      main_events = main_event_md,
      character_events = character_event_md
    ))"""
  # Now with UTF format instead
  with open("./website/index.md", "w", encoding="utf-8") as f:
    f.write(template.substitute(
      main_events = main_event_md,
      character_events = character_event_md
    ))
  