
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
  

def get_event_conditions_markdown(event):
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
          event_conditions += f'* Day of week is {day}\n\n'
        elif condition["comparison"] == "!=":
          event_conditions += f'* Day of week is not {day}\n\n'
        elif condition["comparison"] == ">" and condition["value"] == 5:
          event_conditions += f'* Day of week is a weekend\n\n'
        elif condition["comparison"] == ">=" and condition["value"] == 6:
          event_conditions += f'* Day of week is a weekend\n\n'
        elif condition["comparison"] == "<" and condition["value"] == 6:
          event_conditions += f'* Day of week is a weekday\n\n'
        elif condition["comparison"] == "<=" and condition["value"] == 5:
          event_conditions += f'* Day of week is a weekday\n\n'
        elif condition["comparison"] == ">":
          event_conditions += f'* Day of week (Mon-Sun) is after {day}\n\n'
        elif condition["comparison"] == ">=":
          event_conditions += f'* Day of week (Mon-Sun) is on or after {day}\n\n'
        elif condition["comparison"] == "<":
          event_conditions += f'* Day of week (Mon-Sun) is before {day}\n\n'
        elif condition["comparison"] == "<=":
          event_conditions += f'* Day of week (Mon-Sun) is on or before {day}\n\n'
        else:
          event_conditions += f'* Day of week (Mon-Sun) is {condition["comparison"]} {day}\n\n'
      
      elif condition["variable"].endswith("_love"):
        # Convert to character name
        character = condition["variable"].replace("_love", "")
        character = character[0].upper() + character[1:]
        event_conditions += f'* {character} love {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
      
      elif condition["variable"].endswith("_lust"):
        # Convert to character name
        character = condition["variable"].replace("_lust", "")
        character = character[0].upper() + character[1:]
        event_conditions += f'* {character} lust {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
        
      elif condition["variable"] == event["id"]:
        # Ignore condition requiring itself to be completed
        pass

      elif condition["variable"] in events:
        # Requires an event to be in a certain state
        name = events[condition["variable"]]["name"]
        group = events[condition["variable"]]["group"]
        link = f"[{name}](./{condition['variable']}.md) ({group})"
        if condition["comparison"] == "==" and condition["value"] == True:
          event_conditions += f'* Event {link} is completed)\n\n'
        elif condition["comparison"] == "==" and condition["value"] == False:
          event_conditions += f'* Event {link} must not be completed)\n\n'
        elif condition["comparison"] == "!=" and condition["value"] == True:
          event_conditions += f'* Event {link} must not be completed)\n\n'
        elif condition["comparison"] == "!=" and condition["value"] == False:
          event_conditions += f'* Event {link} is completed)\n\n'
        else:  
          event_conditions += f'* Event {link} {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (event={condition["variable"]})\n\n'

      elif condition["variable"] == "totaldays":
        # Days since the start of the game
        event_conditions += f'* Days since the start of the game {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}\n\n'
      
      else:
        # Unknown condition
        event_conditions += f'* {condition["variable"]} {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (unknown variable)\n\n'
  
  if event_conditions == "":
    event_conditions = "No event conditions found, it is likely part of an event chain."
  
  return event_conditions

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
        event_properties.append(f"Id: {event['id']}")
      if "group" in event and event["group"]:
        event_properties.append(f"Group: {event['group']}")
      if "triggered_by" in event and event["triggered_by"]:
        event_properties.append(f"Triggered by label: {event['triggered_by']}")
      if "triggered_by_branch" in event and event["triggered_by_branch"]:
        event_properties.append(f"Triggered by branch label: {event['triggered_by_branch']}")
      if "triggered_by_branch_path" in event and event["triggered_by_branch_path"]:
        path = list(reversed(event["triggered_by_branch_path"][0:-1]))
        path.append(event["id"])
        path = "->".join(path)
        event_properties.append(f"Triggered by path: {path}")
      if "chain_sources" in event and event["chain_sources"]:
        event_properties.append(f"Chain sources: {event['chain_sources']}")
      if "chain_sources_path" in event and event["chain_sources_path"]:
        event_properties.append(f"Chain sources path: {'->'.join(reversed(event['chain_sources_path']))}")
      
      if len(event_properties) > 0:
        event_properties = "* " + "\n* ".join(event_properties)
      else:
        event_properties = ""
      
      event_conditions = get_event_conditions_markdown(event)

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

  # Build the list of events by group
  events_by_group = {}
  for event in events.values():
    if event["group"] not in events_by_group:
      events_by_group[event["group"]] = []
    events_by_group[event["group"]].append(event)
  
  # Build the markdown lists by group
  event_tables_by_group_md = {}
  for group in events_by_group:
    event_tables_by_group_md[group] = f"## {group}\n\n"

    # Build the simplified table of events
    table = "| Event | Prerequisites | Next Events |\n"
    table += "| --- | --- | --- |\n"
    for event in events_by_group[group]:
      event_prereq = get_event_conditions_markdown(event)
      event_prereq = event_prereq.replace("\n\n", "\n")
      event_prereq = event_prereq.replace("\n", "<br>")
      event_prereq = event_prereq.replace("* ", "")

      event_chain = ""
      if "chain_sources" in event and event["chain_sources"]:
        event_chain = f"Part of event chain [{events[event['chain_sources']]['name']}](./events/{event['chain_sources']}.md)"
      if "No event conditions found" in event_prereq:
        event_prereq = event_chain
      else:
        event_prereq += f"<br>{event_chain}"

      post_events = ""
      if "post_events" in event:
        for post_event in event["post_events"]:
          post_events += f"[{events[post_event]['name']}](./{post_event}.md) ({events[post_event]['group']})<br>"

      table += f"| [{event['name']}](./events/{event['id']}.md) | {event_prereq} | {post_events} |\n"
    
    event_tables_by_group_md[group] += table + "\n"
  
  event_tables = ""
  groups = list(event_tables_by_group_md.keys())
  groups.sort()
  groups.remove("Main")
  groups.remove("Happy scenes")

  # Add an link to each group anchor with markdown
  event_tables += "Main events:\n\n"
  for group in ["Main", "Happy scenes"]:
    event_tables += f"* [{group}](#{group.lower().replace(' ', '-')})\n"
  
  # Add an link to each group anchor with markdown
  event_tables += "\nCharacters:\n\n"
  for group in groups:
    event_tables += f"* [{group}](#{group.lower().replace(' ', '-')})\n"

  for group in ["Main", "Happy scenes"] + groups:
    event_tables += event_tables_by_group_md[group]

  # Build the index page
  with open("./docs/index.md", "w", encoding="utf-8") as f:
    f.write(template.substitute(
      event_tables = event_tables,
    ))

  
  