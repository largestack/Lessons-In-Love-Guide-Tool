
from string import Template
from game_data import load_game_data

def comparison_symbol_to_text(comparison_symbol):
  if comparison_symbol == ">":
    return "greater than"
  elif comparison_symbol == ">=":
    return "greater than or equal to"
  elif comparison_symbol == "<":
    return "less than"
  elif comparison_symbol == "<=":
    return "less than or equal to"
  elif comparison_symbol == "==":
    return "equal to"
  elif comparison_symbol == "!=":
    return "not equal to"
  else:
    raise Exception("Invalid comparison symbol: " + comparison_symbol)

if __name__ == "__main__":
  # Load the main template
  with open("index.template", "r") as f:
    template = Template(f.read())
  
  # Load the event template
  with open("event.template", "r") as f:
    event_template = Template(f.read())
    
  # Load the game data
  game_path = "D:\\Games\\Dult\\LessonsInLove0.28.0-0.28.0-pc-subscribestar"
  events, save_data, characters, save_file, save_file_timestamp = load_game_data(game_path)

  # Create the event pages
  for id, event in events.items():
    with open("./docs/events/" + id + ".md", "w", encoding="utf-8") as f:
      # Build the event properties
      event_properties = []
      if "id" in event and event["id"]:
        event_properties.append(f"ID: {event['id']}")
      if "group" in event and event["group"]:
        event_properties.append(f"Group: {event['group']}")
      if "triggered_by" in event and event["triggered_by"]:
        event_properties.append(f"Triggered by label: {event['triggered_by']}")
      if "triggered_by_branch" in event and event["triggered_by_branch"]:
        event_properties.append(f"Triggered by branch label: {event['triggered_by_branch']}")
      
      if len(event_properties) > 0:
        event_properties = "* " + "\n* ".join(event_properties)
      else:
        event_properties = ""
      
      # Build the event conditions
      event_conditions = ""
      if "conditions" in event and len(event["conditions"]) > 0:
        for condition in event["conditions"]:
          if condition["variable"] == "day":
            # Convert to day of week text
            map = {
              1: "Monday",
              2: "Tuesday",
              3: "Wednesday",
              4: "Thursday",
              5: "Friday",
              6: "Saturday",
              7: "Sunday",
            }
            day = map[int(condition["value"])]
            if condition["comparison"] == "==":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is {day}\n\n'
            elif condition["comparison"] == "!=":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is not {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is not {day}\n\n'
            elif condition["comparison"] == ">" and condition["value"] == 5:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend\n\n'
            elif condition["comparison"] == ">=" and condition["value"] == 6:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend\n\n'
            elif condition["comparison"] == "<" and condition["value"] == 6:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday\n\n'
            elif condition["comparison"] == "<=" and condition["value"] == 5:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday\n\n'
            elif condition["comparison"] == ">":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is after {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is after {day}\n\n'
            elif condition["comparison"] == ">=":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or after {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or after {day}\n\n'
            elif condition["comparison"] == "<":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is before {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is before {day}\n\n'
            elif condition["comparison"] == "<=":
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or before {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or before {day}\n\n'
            else:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is {condition["comparison"]} {day}')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is {condition["comparison"]} {day}\n\n'
          
          elif condition["variable"].endswith("_love"):
            # Convert to character name
            character = condition["variable"].replace("_love", "")
            character = character[0].upper() + character[1:]
            #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{character} love {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
            event_conditions += f'{"✅" if condition["satisfied"] else "❌"}{character} love {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
          
          elif condition["variable"].endswith("_lust"):
            # Convert to character name
            character = condition["variable"].replace("_lust", "")
            character = character[0].upper() + character[1:]
            #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{character} lust {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
            event_conditions += f'{"✅" if condition["satisfied"] else "❌"}{character} lust {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
            
          elif condition["variable"] == event["id"]:
            # Ignore condition requiring itself to be completed
            pass

          elif condition["variable"] in events:
            # Requires an event to be in a certain state
            name = events[condition["variable"]]["name"]
            group = events[condition["variable"]]["group"]
            link = f"[{group}: {name}](./{condition['variable']}.md)"
            if condition["comparison"] == "==" and condition["value"] == True:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" is completed (event={condition["variable"]})')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Event "{link}" is completed (event={condition["variable"]})\n\n'
            elif condition["comparison"] == "==" and condition["value"] == False:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" must not be completed (event={condition["variable"]})')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Event "{link}" must not be completed (event={condition["variable"]})\n\n'
            elif condition["comparison"] == "!=" and condition["value"] == True:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" must not be completed (event={condition["variable"]})')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Event "{link}" must not be completed (event={condition["variable"]})\n\n'
            elif condition["comparison"] == "!=" and condition["value"] == False:
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" is completed (event={condition["variable"]})')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Event "{link}" is completed (event={condition["variable"]})\n\n'
            else:  
              #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (event={condition["variable"]})')
              event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Event "{link}" {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (event={condition["variable"]})\n\n'

          elif condition["variable"] == "totaldays":
            # Days since the start of the game
            #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Days since the start of the game {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
            event_conditions += f'{"✅" if condition["satisfied"] else "❌"}Days since the start of the game {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
          
          else:
            # Unknown condition
            #self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{condition["variable"]} {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (unknown variable)')
            event_conditions += f'{"✅" if condition["satisfied"] else "❌"}{condition["variable"]} {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (unknown variable)\n\n'
      
      if event_conditions == "":
        event_conditions = "No event conditions found, it is likely part of an event chain."

      event_chain = ""
      if "chain_sources" in event and event["chain_sources"]:
        event_chain = f"\nPart of event chain [{events[event['chain_sources']]['name']}](./{event['chain_sources']}.md)"

      # Build the post-event list from 'post_events'
      post_events = []
      if "post_events" in event:
        for post_event in event["post_events"]:
          post_events.append(f"[{events[post_event]['group']}: {events[post_event]['name']}](./{post_event}.md)")
      if len(post_events) > 0:
        post_events = "* " + "\n* ".join(post_events)
      else:
        post_events = "None"

      f.write(event_template.substitute(
        id = id,
        name = event["name"],
        group = event["group"],
        event_rpath = event["event_rpath"],
        event_code = event["event_code"],
        trigger_rpath = event["trigger_rpath"],
        trigger_code = event["trigger_code"],
        event_chain = event_chain,
        event_properties = event_properties.strip(),
        event_conditions = event_conditions,
        post_events = post_events,
      ))

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
  

  # Build the index page
  with open("./docs/index.md", "w", encoding="utf-8") as f:
    f.write(template.substitute(
      main_events = main_event_md,
      character_events = character_event_md
    ))

  
  