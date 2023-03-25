# Import Module
import datetime
import glob
from itertools import groupby
import re
from tkinter import *
import os
from tkinter import filedialog
import zipfile
import sys

def load_game_data(game_folder):
  """
  Loads all the game data along with savegame state.

  Args:
      game_folder (_type_): _description_
  
  Returns:
      (dict, dict, list, savegame, time): (Dictionary of all the parsed events, Dictionary of all the save data, character list)
  """
  # Load the root Lesson in Love folder
  file_script = os.path.join(game_folder, "game", "script.rpy")

  # Load the most recent save file
  save_folder = os.path.join(game_folder, "game", "saves")

  # Check if the folder exists
  save_file = None
  save_data = {}
  if os.path.exists(save_folder):
    # Enumerate the .save files, loading the most recent one
    save_files = [f for f in os.listdir(save_folder) if f.endswith(".save")]
    save_files.sort(key=lambda f: os.path.getmtime(os.path.join(save_folder, f)), reverse=True)
    if len(save_files) > 0:
      save_file = os.path.join(save_folder, save_files[0])
      print(f"Loading most recent save file: {save_file}...")

      # Unzip the save file in memory and load the log file
      with zipfile.ZipFile(save_file, "r") as zip:
        with zip.open("log") as f:
          save = f.read()

          # Basic parsing of all the values
          # Find all "store." entries
          index = 0
          while(True):
            index = save.find(b"store.", index)
            if index == -1:
              break
            
            # Format seems to be:
            # <byte: len of name> <name> <byte: variable type> (<value>)
            # Variable types:
            #   0x4b: Byte, 1 byte value
            #   0x4d: Word, 2 byte value
            #   0x88: Boolean true, no optional vale
            #   0x89: Boolean false, no optional vale

            length = save[index - 1]
            try:
              name = save[index:index + length].replace(b"store.", b"").decode("utf8")
            except:
              #print(f"Error decoding name: {save[index:index + length]}")
              next
            type = save[index + length]
            value = None
            if type == 0x88:
              value = True
            elif type == 0x89:
              value = False
            elif type == 0x4b:
              value = save[index + length + 1]
            elif type == 0x4d:
              value = save[index + length + 1] + save[index + length + 2] * 256
            else:
              pass

            save_data[name] = value

            index += 1
  
  if save_file == None:
    print("No save file found.")

  print(f"Loaded {len(save_data)} saved variables")

  # Load the character names
  characters = []
  with open(os.path.join(game_folder, "game", "newchecker.rpy"), "r", encoding="utf8") as f:
    script = f.read()

    character_section = script.split("#HAPPY (7 NON-MISSABLE/4 MISSABLE)")[-1].split("#NORIKO NUDES")[0]

    # Extract all character event names
    lines = character_section.split("\n")
    character = None
    for line in lines:
      line = line.strip()
      if line.startswith("#"):
        character = line.split(" ")[0][1:]
        characters.append(character.capitalize())

  print(f"Loaded {len(characters)} characters")
  print(f"Characters: {characters}")

  events = {}

  # Parse screens.rpy to load all the events
  with open(os.path.join(game_folder, "game", "screens.rpy"), "r", encoding="utf8") as f:
    script = f.read()

    lines = script.split("\n")
    current_event_group = None
    for i, line in enumerate(lines):
      if line == "\n":
        current_event_group = None
        continue

      line = line.strip()

      if "use game_menu(_(" in line and (" Events" in line or " SCENES" in line):
        current_event_group = line.split('"')[1].replace(" Events", "").capitalize()
      elif current_event_group:
        if line.startswith("textbutton _(\""):
          # Parse the name
          name = line.split('"')[1]
          name = name.replace("✓", "")
          # Regex remove regions within {} and () brackets
          name = re.sub(r"\(.*?\)", "", name)
          name = re.sub(r"\{.*?\}", "", name)
          name = name.strip()

          # Parse the event id
          id = None
          if i+2 < len(lines) and "action Replay" in lines[i+2]:
            id = lines[i+2].strip().split('"')[1]

          if id and id not in events and name != None:
              events[id] = {
                "id": id,
                "name": name,
                "group": current_event_group,
                "complete": None,
                "ready_to_trigger": None,
                "code": None,
                "event_code": None,
                "event_rpath": None,
                "trigger_code": None,
                "trigger_rpath": None,
                "trigger_code": None,
                "jump_to_file": None,
                "condition_text": None,
                "conditions": [],                
              }

  print(f"Loaded {len(events)} named events")
  # Print the number of events by group
  for group, event_set in groupby(sorted(events.values(), key=lambda e: e["group"]), key=lambda e: e["group"]):
    print(f"  {group}: {len(list(event_set))}")


  # Update the events on if they are complete or not
  for event, details in events.items():
    if event in save_data and save_data[event] == True:
      details["complete"] = True
    else:
      details["complete"] = False
    details["ready_to_trigger"] = False
    details["code"] = "no code found (this usually means it's part of an automatic event chain)"
    details["jump_to_file"] = []
    details["required_events"] = []

  # Parse all script files to requirements to the main and character events
  label_to_jumps = {}
  script_files = glob.glob(os.path.join(game_folder, "game", "*.rpy"), recursive=True)
  script_files.append(os.path.join(game_folder, "game", "scripts", "subscribestar", "inappropriatecontent.rpy"))
  for script_file in script_files:
    print(f"Processing {script_file}...")
    with open(script_file, "r", encoding="utf8") as f:
      script = f.read()
      lines = script.split("\n")

      label = None
      had_jump = True
      for i, line in enumerate(lines):
        # Create a map of jumps to the event label they are in
        # This is used to unwind the jump chains to find the actual event
        if line.startswith("label "):
          new_label = line.split(" ")[1].split(":")[0]
          if had_jump == False:
            if new_label in label_to_jumps:
              label_to_jumps[new_label].append(label)
              label_to_jumps[new_label] = list(set(label_to_jumps[new_label]))
            else:
              label_to_jumps[new_label] = [label]
          
          label = new_label
          had_jump = False

          if label in events:
            # Add code forwards until we hit another known label or 20K lines
            code = "..."
            for n in range(0, 20000):
              if i + n >= len(lines):
                break

              code = code + "\n" + lines[i + n]

              if n > 0 and lines[i + n].strip().startswith("label "):
                label_name = lines[i + n].strip().split(" ")[1].split(":")[0]
                if label_name in events:
                  break
            code = code.strip() + "\n..."
            
            events[label]["event_code"] = code
            events[label]["event_rpath"] = script_file.replace(game_folder, "")

        elif line.strip().startswith("jump "):
          had_jump = True
          target_label = line.strip().split(" ")[1]
          if target_label in label_to_jumps:
            label_to_jumps[target_label].append(label)
            label_to_jumps[target_label] = list(set(label_to_jumps[target_label]))
          else:
            label_to_jumps[target_label] = [label]

        line = line.strip()
        # Parse out the requirements to jumps to known events
        if line.startswith("jump "):
          event_name = line.split("jump ")[-1].split(" ")[0].split("#")[0].strip()
          if event_name in events:
            events[event_name]["jump_to_file"].append(script_file)

            # Add code backwards until we find a label
            trigger_code = "..."
            for n in range(0, 100):
              trigger_code = lines[i - n] + "\n" + trigger_code

              if lines[i - n].strip().startswith("label "):
                break
            trigger_code = "...\n" + trigger_code.strip()
            
            events[event_name]["trigger_code"] = trigger_code
            events[event_name]["trigger_rpath"] = script_file.replace(game_folder, "")
            
            # Find the preceding if statement to find the condition
            prefix = lines[i].split("jump")[0][0:-4] + "if"
            for n in range(0, 10):
              if lines[i - 1 - n].startswith(prefix):
                condition_statement = lines[i - 1 - n].split(prefix)[-1].strip()[0:-1]
                events[event_name]["condition_text"] = condition_statement
                events[event_name]["code"] = "\n".join([l.strip() for l in lines[i - 1 - n : i + 1]])

                # Parse the conditions, ignores complex conditions
                conditions = condition_statement.replace("(","").replace(")","").replace(" or ", " and ").split(" and ")
                if "conditions_text" in events[event_name]:
                  events[event_name]["conditions_text"].extend(conditions)
                else:
                  events[event_name]["conditions_text"] = conditions
                break
  
  # Remove label_to_jumps with more than two jumps
  # This is to remove the jump chains that are not actually events
  deletes = []
  for label, jumps in label_to_jumps.items():
    if len(jumps) > 3:
      deletes.append(label)
  for label in deletes:
    del label_to_jumps[label]

  # Identify branch label ids
  label_counts = {}
  for label, jumps in label_to_jumps.items():
    for jump in jumps:
      if jump in label_counts:
        label_counts[jump] += 1
      else:
        label_counts[jump] = 1

  label_branchers = set()
  for label, count in label_counts.items():
    if count > 5:
      label_branchers.add(label)

  def unwind_label(label, depth, target_set):
    # Unwinds the label unil a label in the target set is found.
    # Returns: (label, depth, [path]) or (None, None, [path]) if not found
    if depth > MAX_CHAIN_DEPTH:
      return (None, None, None)
    if label in target_set:
      return (label, depth, [label])
    
    if label in label_to_jumps:
      labels = label_to_jumps[label]
      
      best_label, best_depth, best_path = (None, None, None)

      # Return the least deep label
      for label in labels:
        result = unwind_label(label, depth + 1, target_set)
        if result != (None, None, None):
          if best_label == None or result[1] < best_depth:
            best_label, best_depth, best_path = result
      
      if best_label != None:
        return (best_label, best_depth, [label] + best_path)
    
    return (None, None, None)

  # Parse all script files to find the events that are triggered by other events
  # label_to_jumps = {label -> [jumping labels]}
  # Unwind the jump chains to find the first actual labelled event, and add it as a chain source
  MAX_CHAIN_DEPTH = 20
  for event_name, event in events.items():
    if event_name in label_to_jumps:
      event["triggered_by"] = label_to_jumps[event_name][0]
    
    # Unwind chain events
    chain_source_name = None
    chain_source_depth = None
    chain_source_path = None
    if event_name in label_to_jumps:
      for label in label_to_jumps[event_name]:
        new_chain_source_name, new_chain_source_depth, new_chain_source_path = unwind_label(label, 0, events)

        if new_chain_source_name is not None:
          if chain_source_name is None or new_chain_source_depth < chain_source_depth:
            chain_source_name = new_chain_source_name
            chain_source_depth = new_chain_source_depth
            chain_source_path = new_chain_source_path
      
    # Unwind branch events
    branch_source_name, branch_source_depth, branch_source_path = unwind_label(event_name, 0, label_branchers)

    # Select the shallowest chain or branch. Default to branch if both are the same depth.
    if chain_source_depth is not None and branch_source_depth is not None:
      if chain_source_depth < branch_source_depth:
        events[event_name]["chain_sources"] = chain_source_name
        events[event_name]["chain_sources_depth"] = chain_source_depth
        events[event_name]["chain_sources_path"] = chain_source_path
      else:
        events[event_name]["triggered_by_branch"] = branch_source_name
        events[event_name]["triggered_by_branch_depth"] = branch_source_depth
        events[event_name]["triggered_by_branch_path"] = branch_source_path
    elif chain_source_depth is not None:
      events[event_name]["chain_sources"] = chain_source_name
      events[event_name]["chain_sources_depth"] = chain_source_depth
      events[event_name]["chain_sources_path"] = chain_source_path
    elif branch_source_depth is not None:
      events[event_name]["triggered_by_branch"] = branch_source_name
      events[event_name]["triggered_by_branch_depth"] = branch_source_depth
      events[event_name]["triggered_by_branch_path"] = branch_source_path

  # Parse Phone.rpy getContacts() to get the call and invite over pre-requisites.
  # Add these as requirements to the events.
  invite_pre_reqs = {}
  call_pre_reqs = {}
  if os.path.exists(os.path.join(game_folder, "game", "Phone.rpy")):
    with open(os.path.join(game_folder, "game", "Phone.rpy"), "r", encoding="utf8") as f:
      phone_script = f.read()
      region = phone_script.split("contactsList = [")[1].split("]")[0]
      contacts = region.split("Contact(")
      for contact in contacts:
        contact = contact.split("\n")[0]
        tokens = contact.split(",")

        if len(tokens) >= 9:
          id_prefix = tokens[0].replace("\"","").strip()
          id_req_call = tokens[7].strip()
          id_req_invite = tokens[8].replace(")","").strip()

          if id_req_call not in ["True","False"]:
            call_pre_reqs[id_prefix] = id_req_call

          if id_req_invite not in ["True","False"]:
            invite_pre_reqs[id_prefix] = id_req_invite
  
  # Add the phone pre-requisites to the events
  for event_name, event in events.items():
    def get_call_name(id):
      if not(id.startswith("call") and (id.endswith("morning") or id.endswith("afternoon") or id.endswith("night"))):
        return None
      
      # Extract the name
      name = id[4:].replace("morning","").replace("afternoon","").replace("night","")
      return name

    def get_invite_name(id):
      if not(id.endswith("invite") or id[:-1].endswith("invite")):
        return None
      
      # Extract the name
      name = id.replace("invite","")
      while name[-1].isdigit():
        name = name[:-1]

      return name
    
    for id in [event_name, event["triggered_by"] if "triggered_by" in event else None]:
      if id is not None:
        # Add call pre-requisites
        name = get_call_name(id)
        
        if name is not None and name in call_pre_reqs:
          events[event_name]["call_pre_req"] = call_pre_reqs[name]
          if "conditions_text" not in event:
            event["conditions_text"] = []
          
          conditions = call_pre_reqs[name].replace("(","").replace(")","").replace(" or ", " and ").split(" and ")
          event["conditions_text"].extend(conditions)
        
        # Add invite pre-requisites
        name = get_invite_name(id)
        if name is not None and name in invite_pre_reqs:
          events[event_name]["invite_pre_req"] = invite_pre_reqs[name]
          if "conditions_text" not in event:
            event["conditions_text"] = []
          
          conditions = invite_pre_reqs[name].replace("(","").replace(")","").replace(" or ", " and ").split(" and ")
          event["conditions_text"].extend(conditions)


  # Add custom conditions. Used to add conditions that are not parsed in the game script.
  # These are mostly introductions of new characters.
  custom_conditions = {
    # "event_name": ["condition1", "condition2"],
    "iofirsthall": ["day247"],
    "utafirsthall": ["day247"],
    "yasufirsthall": ["day304"],
    "toukafirsthall": ["day304"],
    "toukastreets1": ["day304"],
    "ramen1": ["day154"],
    "tsuneyofirsthall": ["day154"],
    "otohafirsthall": ["day288"],
    "mollycafe1": ["day154"],
    "mollyfirsthall": ["day154"],
    "kirindate1": ["soccer20"],
    "kirinfirsthall": ["day271"],
    "nodokafirsthall": ["day288"],
    "norikofirsthall": ["day271"],
    "osakodojo1": ["osakodate1"],
    "harukafirstlust": ["harukadate1"],
    "harukalust10": ["harukadate1"],
  }
  for event_name, conditions in custom_conditions.items():
    if event_name in events:
      if "conditions_text" not in events[event_name]:
        events[event_name]["conditions_text"] = []
      events[event_name]["conditions_text"].extend(conditions)

  # Process the event condition status
  for event_name, event in events.items():
    if "conditions_text" in event:
      conditions = event["conditions_text"]

      if len(conditions) > 0:
        events[event_name]["ready_to_trigger"] = True

      # Dedupe conditions, keeping order
      conditions = list(dict.fromkeys(conditions))

      for condition in conditions:
        sections = re.split(r"([<>=!]+)", condition)
        variable = sections[0].strip()
        if len( sections ) == 3:
          comparison = sections[1].strip()
          value = sections[2].strip()
          if value == "True":
            value = True
          elif value == "False":
            value = False
          else:
            try:
              value = int(value)
            except:
              #print(f"WARNING: Unknown value: {value}")
              next
        elif len( sections ) == 1:
          comparison = "=="
          value = True
        else:
          print(f"ERROR: Unknown condition: {condition}")
          next
        
        # Add required events for this to occur
        if variable in events and variable != event_name:
          events[event_name]["required_events"].append(variable)
          # Add a post-requisite to the required event
          if "post_events" not in events[variable]:
            events[variable]["post_events"] = []
          events[variable]["post_events"].append(event_name)
        
        if variable not in save_data:
          # Default to 0 for int value, False for bool
          if isinstance(value, bool):
            comparison_value = False
          elif isinstance(value, int):
            comparison_value  = 0
        else:
          comparison_value = save_data[variable]

        # Determine if the condition is met
        satisfied = None
        if comparison == "==":
          satisfied = comparison_value == value
        elif comparison == "!=":
          satisfied = comparison_value != value
        elif comparison == ">":
          satisfied = comparison_value > value
        elif comparison == ">=":
          satisfied = comparison_value >= value
        elif comparison == "<":
          satisfied = comparison_value < value
        elif comparison == "<=":
          satisfied = comparison_value <= value
        else:
          print(f"ERROR: Unknown comparison: {comparison}")
          next
        
        events[event_name]["conditions"].append(
          {
            "variable": variable,
            "comparison": comparison,
            "value": value,
            "saved_value": comparison_value,
            "satisfied": satisfied
          }
        )

        if satisfied == False and variable != "day" and "_love" not in variable and "_lust" not in variable:
          events[event_name]["ready_to_trigger"] = False

  # Get timestamp of save_file
  if save_file is None:
    save_file_timestamp = "No save found"
  else:
    save_file_timestamp = os.path.getmtime(save_file)
    # Format it nicely
    save_file_timestamp = datetime.datetime.fromtimestamp(save_file_timestamp).strftime('%Y-%m-%d %H:%M:%S')

  return (events, save_data, characters, save_file, save_file_timestamp)


