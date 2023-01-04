# Import Module
from tkinter import messagebox
import webbrowser
from tkinter import *
import os
from tkinter import filedialog
import game_data
from tooltip import Tooltip

# Create the Tkinter UI
import tkinter as tk
import tkinter.font as tkFont


import tkinter as tk
import tkinter.ttk as ttk


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

class App:
  def __init__(self, root):
    #setting title
    root.title("Lessons in Love: Walkthrough guide")
    self.active_event = None

    #setting window size
    width=1236
    height=633
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_220=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_220["font"] = ft
    GLabel_220["fg"] = "#333333"
    GLabel_220["justify"] = "left"
    GLabel_220["text"] = "Suggested next events"
    GLabel_220.place(x=10,y=10,width=136,height=30)

    list_event_suggestions=tk.Listbox(root, exportselection=False)
    list_event_suggestions["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    list_event_suggestions["font"] = ft
    list_event_suggestions["fg"] = "#333333"
    list_event_suggestions.place(x=10,y=40,width=217,height=289)
    list_event_suggestions.bind("<<ListboxSelect>>", self.on_list_event_suggestions_select)
    self.list_event_suggestions = list_event_suggestions

    GLabel_221=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_221["font"] = ft
    GLabel_221["fg"] = "#333333"
    GLabel_221["justify"] = "left"
    GLabel_221["text"] = "Save game details\n(auto loads most recent)"
    GLabel_221.place(x=-30,y=330,width=236,height=40)

    text_save_details=tk.Text(root)
    text_save_details["borderwidth"] = "1px"
    ft = tkFont.Font(family="Consolas 10",size=10)
    text_save_details["font"] = ft
    text_save_details["fg"] = "#333333"
    text_save_details.insert(tk.END,"Save details go here")
    text_save_details.place(x=10,y=370,width=217,height=237)
    self.text_save_details = text_save_details

    
    list_event_groups=tk.Listbox(root, exportselection=False)
    list_event_groups["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    list_event_groups["font"] = ft
    list_event_groups["fg"] = "#333333"
    list_event_groups.place(x=230,y=40,width=247,height=588)
    self.list_event_groups = list_event_groups
    list_event_groups.bind("<<ListboxSelect>>", self.on_list_event_groups_select)

    GLabel_558=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_558["font"] = ft
    GLabel_558["fg"] = "#333333"
    GLabel_558["justify"] = "left"
    GLabel_558["text"] = "Event group"
    GLabel_558.place(x=240,y=10,width=70,height=25)

    list_events=tk.Listbox(root, exportselection=False)
    list_events["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    list_events["font"] = ft
    list_events["fg"] = "#333333"
    list_events.place(x=480,y=40,width=262,height=588)
    self.list_events = list_events
    list_events.bind("<<ListboxSelect>>", self.on_list_events_select)
    # Add a scrollbar to the listbox
    scrollbar = tk.Scrollbar(root, orient="vertical")
    scrollbar.config(command=list_events.yview)
    scrollbar.pack(side="right", fill="y")
    list_events.config(yscrollcommand=scrollbar.set)
    # Position the scrollbar next to it
    scrollbar.place(x=480+246, y=40, width=20, height=588)


    GLabel_939=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_939["font"] = ft
    GLabel_939["fg"] = "#333333"
    GLabel_939["justify"] = "left"
    GLabel_939["text"] = "Event"
    GLabel_939.place(x=490,y=10,width=70,height=25)

    GLabel_658=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_658["font"] = ft
    GLabel_658["fg"] = "#333333"
    GLabel_658["justify"] = "center"
    GLabel_658["text"] = "Event prerequisites (click on a row with event to jump to it)"
    GLabel_658.place(x=740,y=10,width=350,height=30)

    list_event_prereq_events=tk.Listbox(root, exportselection=False)
    list_event_prereq_events["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times',size=10)
    list_event_prereq_events["font"] = ft
    list_event_prereq_events["fg"] = "#333333"
    list_event_prereq_events.place(x=750,y=40,width=481,height=230)
    list_event_prereq_events.bind("<<ListboxSelect>>", self.on_list_event_prereq_events_select)
    self.list_event_prereq_events = list_event_prereq_events

    GLabel_650=tk.Label(root)
    ft = tkFont.Font(family='Times',size=10)
    GLabel_650["font"] = ft
    GLabel_650["fg"] = "#333333"
    GLabel_650["justify"] = "center"
    GLabel_650["text"] = "Event raw details"
    GLabel_650.place(x=740,y=270,width=128,height=30)

    text_event_details=tk.Text(root)
    text_event_details["borderwidth"] = "1px"
    ft = tkFont.Font(family="Consolas 10",size=10)
    text_event_details["font"] = ft
    text_event_details["fg"] = "#333333"
    text_event_details.insert(tk.END,"Event details go here")
    text_event_details.place(x=750,y=300,width=478,height=279)
    self.text_code_snippets = text_event_details
    # Add scroll bar
    scrollbar = tk.Scrollbar(root, orient="vertical", command=text_event_details.yview)

    button_event_wiki=tk.Button(root)
    button_event_wiki["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    button_event_wiki["font"] = ft
    button_event_wiki["fg"] = "#000000"
    button_event_wiki["justify"] = "center"
    button_event_wiki["text"] = "Open wiki for this event"
    button_event_wiki.place(x=890,y=590,width=137,height=30)
    button_event_wiki["command"] = self.button_event_wiki
    button_event_wiki_ttp = Tooltip(button_event_wiki, text="Opens this event on the official wiki.")

    button_refresh=tk.Button(root)
    button_refresh["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    button_refresh["font"] = ft
    button_refresh["fg"] = "#000000"
    button_refresh["justify"] = "center"
    button_refresh["text"] = "Reload"
    button_refresh.place(x=50,y=590,width=136,height=30)
    button_refresh["command"] = self.button_refresh
    button_refresh_ttp = Tooltip(button_refresh, text="Reloads everything from the most recent save file again.")

    button_back=tk.Button(root)
    button_back["bg"] = "#f0f0f0"
    ft = tkFont.Font(family='Times',size=10)
    button_back["font"] = ft
    button_back["fg"] = "#000000"
    button_back["justify"] = "center"
    button_back["text"] = "Back to previous event"
    button_back.place(x=1080,y=5,width=152,height=30)
    button_back["command"] = self.button_back
    button_back_ttp = Tooltip(button_back, text="Go back to the previous event that you were most recently viewing.")

    # Load the game folder if it exists
    game_folder = None
    if os.path.exists("game_folder.txt"):
      with open("game_folder.txt", "r") as f:
        game_folder = f.read()

    # Prompt the user to select the game folder
    if game_folder is None:
      game_folder = filedialog.askdirectory(title="Select the game folder")
    while not os.path.exists(os.path.join(game_folder, "game", "script.rpy")):
      print("Invalid game folder. Please select the root folder of the game.")
      game_folder = filedialog.askdirectory(title="Select the game folder")
    self.game_folder = game_folder

    self.refresh()

  def previous_event(self):
    if len(self.previous_events) > 1:
      self.previous_events.pop()
      self.select_event(self.previous_events.pop())

  def select_event(self, event, add_to_history=True):

    if event is None:
      self.active_event = event

      # Unselect list boxes
      self.list_event_suggestions.selection_clear(0, tk.END)
      self.list_event_groups.selection_clear(0, tk.END)
      self.list_events.selection_clear(0, tk.END)
      self.list_event_prereq_events.selection_clear(0, tk.END)

      # Update the event list box
      self.list_events.delete(0, tk.END)
      return

    # Update the event list box only if the group changed
    if self.active_event is None or event["group"] != self.active_event["group"]:
      self.list_events.delete(0, tk.END)

      # Populate the event list box from the new event group
      for e in self.group_to_events[event["group"]]:
        if e["complete"]:
          self.list_events.insert(tk.END, "✅" + e["name"])
        elif e["ready_to_trigger"]:
          self.list_events.insert(tk.END, "🔵" + e["name"])
        else:
          self.list_events.insert(tk.END, "❌" + e["name"])
      
    self.active_event = event

    # Unselect list boxes
    self.list_event_suggestions.selection_clear(0, tk.END)
    self.list_event_groups.selection_clear(0, tk.END)
    self.list_events.selection_clear(0, tk.END)
    self.list_event_prereq_events.selection_clear(0, tk.END)
    
    id = event["id"]
    
    if add_to_history:
      self.previous_events.append(self.active_event)
    
    # Select the event in the list boxes
    if id in self.event_suggestions:
      self.list_event_suggestions.selection_set(self.event_suggestions.index(id))
      self.list_event_suggestions.see(self.event_suggestions.index(id))
    if event["group"] in self.group_to_events.keys():
      self.list_event_groups.selection_set(list(self.group_to_events.keys()).index(event["group"]))
      self.list_event_groups.see(list(self.group_to_events.keys()).index(event["group"]))
    if event in self.group_to_events[event["group"]]:
      self.list_events.selection_set(self.group_to_events[event["group"]].index(event))
      self.list_events.see(self.group_to_events[event["group"]].index(event))

    # Update the event prereq events list box
    self.list_event_prereq_events.delete(0, tk.END)
    if "triggered_by_branch" in event and len(event["triggered_by_branch"]) > 0:
      self.list_event_prereq_events.insert(tk.END, "🔵 Triggered by '" + event["triggered_by_branch"] + "'")
    else:
      self.list_event_prereq_events.insert(tk.END, "❌ Triggered by 'unknown'")
    
    if "chain_sources" in event and len(event["chain_sources"]) > 0:
      name = event["chain_sources"]
      if name in self.events:
        name = self.events[name]["name"]

      self.list_event_prereq_events.insert(tk.END, "🔵 Part of chain event '" + name + "' (event=" + event["chain_sources"] + ")")
    
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
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is {day}')
          elif condition["comparison"] == "!=":
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is not {day}')
          elif condition["comparison"] == ">" and condition["value"] == 5:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend')
          elif condition["comparison"] == ">=" and condition["value"] == 6:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekend')
          elif condition["comparison"] == "<" and condition["value"] == 6:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday')
          elif condition["comparison"] == "<=" and condition["value"] == 5:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week is a weekday')
          elif condition["comparison"] == ">":
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is after {day}')
          elif condition["comparison"] == ">=":
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or after {day}')
          elif condition["comparison"] == "<":
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is before {day}')
          elif condition["comparison"] == "<=":
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is on or before {day}')
          else:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Day of week (Mon-Sun) is {condition["comparison"]} {day}')
        
        elif condition["variable"].endswith("_love"):
          # Convert to character name
          character = condition["variable"].replace("_love", "")
          character = character[0].upper() + character[1:]
          self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{character} love {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
        
        elif condition["variable"].endswith("_lust"):
          # Convert to character name
          character = condition["variable"].replace("_lust", "")
          character = character[0].upper() + character[1:]
          self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{character} lust {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
          
        elif condition["variable"] == event["id"]:
          # Ignore condition requiring the event to be completed
          pass

        elif condition["variable"] in self.events:
          # Requires an event to be in a certain state
          name = self.events[condition["variable"]]["name"]
          if condition["comparison"] == "==" and condition["value"] == True:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" is completed (event={condition["variable"]})')
          elif condition["comparison"] == "==" and condition["value"] == False:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" must not be completed (event={condition["variable"]})')
          elif condition["comparison"] == "!=" and condition["value"] == True:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" must not be completed (event={condition["variable"]})')
          elif condition["comparison"] == "!=" and condition["value"] == False:
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" is completed (event={condition["variable"]})')
          else:  
            self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Event "{name}" {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (event={condition["variable"]})')

        elif condition["variable"] == "totaldays":
          # Days since the start of the game
          self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}Days since the start of the game {comparison_symbol_to_text(condition["comparison"])} {condition["value"]}')
        
        else:
          # Unknown condition
          self.list_event_prereq_events.insert(tk.END, f'{"✅" if condition["satisfied"] else "❌"}{condition["variable"]} {comparison_symbol_to_text(condition["comparison"])} {condition["value"]} (unknown variable)')

    
    # Update the event details
    self.text_code_snippets.delete(1.0, tk.END)
    self.text_code_snippets.insert(tk.END,
      "event name:" + event["name"] +
      "\nevent id:" + event["id"] +
      "\nevent group:" + event["group"] +
      "\nevent chain:" + (event["chain_sources"] if "chain_sources" in event else "") +
      "\ntriggered by label:" + (event["triggered_by"] if "triggered_by" in event else "") +
      "\ntriggered by label branch:" + (event["triggered_by_branch"] if "triggered_by_branch" in event else "") +
      "\nevent trigger file:" + str(event["jump_to_file"]) +
      "\nevent trigger code:\n" + event["code"])
    # Add the condition logic
    if "conditions" in event:
      self.text_code_snippets.insert(tk.END, "\nconditions:")
      for condition in event["conditions"]:
        self.text_code_snippets.insert(tk.END, f'\n{"✅" if condition["satisfied"] else "❌"} {condition["variable"]} {condition["comparison"]} {condition["value"]}')

  def refresh(self):
    event_id_to_restore = self.active_event["id"] if self.active_event else None

    self.previous_events = []
    self.event_suggestions = []
    self.active_event = None
    self.select_event(None)

    # Load the game and save data
    (events, save_data, characters, save_file, save_file_timestamp) = game_data.load_game_data(self.game_folder)
    self.events = events
    self.save_data = save_data
    self.characters = sorted(characters)

    # Update the save game details panel
    self.text_save_details.delete(1.0, tk.END)
    self.text_save_details.insert(tk.END, f"Timestamp: {save_file_timestamp}\nFile: {save_file}\n")

    # Build a map from group to events
    self.group_to_events = {}
    for id, event in self.events.items():
      if event["group"] not in self.group_to_events:
        self.group_to_events[event["group"]] = []
      self.group_to_events[event["group"]].append(event)

    # Update the event groups list
    self.list_event_groups.delete(0, tk.END)
    for event_group in self.group_to_events.keys():
      self.list_event_groups.insert(tk.END, event_group)

    # Calculate the event suggestions
    self.list_event_suggestions.delete(0, tk.END)
    self.event_suggestions = self.get_event_suggestions()
    for event in self.event_suggestions:
      self.list_event_suggestions.insert(tk.END, f'{"🔵" if event["ready_to_trigger"] else "❌"} {event["group"]}: {event["name"]}')

    # Restore the selected event
    if event_id_to_restore:
      self.select_event(self.events[event_id_to_restore])

  def get_event_suggestions(self):
    # Calculates the next events to suggest based on the current state of the game
    # TODO: Implement

    event_suggestions = []

    # Add the next main event
    if "Main" in self.group_to_events:
      for i in range(len(self.group_to_events["Main"])-1, -1, -1):
        event = self.group_to_events["Main"][i - 1]
        if event["complete"]:
          event_suggestions.append(self.group_to_events["Main"][i])
          break
    
    # Add any ready_to_trigger character events after the two most-recently completed ones
    for character in self.characters:
      character = character.capitalize()
      if character not in self.group_to_events:
        continue

      # Unwind until we pass two completed events
      completed_events = 0
      for i in range(len(self.group_to_events[character])-1, -1, -1):
        event = self.group_to_events[character][i - 1]
        if event["complete"]:
          completed_events += 1
          if completed_events == 2:
            break
      
      # Walk forward until first ready_to_trigger event and has no event chain sources chain_sources
      for j in range(i, len(self.group_to_events[character])):
        event = self.group_to_events[character][j]
        if event["ready_to_trigger"] and ("chain_sources" not in event or len(event["chain_sources"]) == 0) and ("triggered_by_branch" in event and len(event["triggered_by_branch"]) > 0):
          event_suggestions.append(event)

          # Consider the next 3 events after this one if they are ready to trigger as well
          for k in range(j+1, min(j+4, len(self.group_to_events[character]))):
            event = self.group_to_events[character][k]
            if event["ready_to_trigger"]:
              event_suggestions.append(event)
            else:
              break
          break
    
    return event_suggestions

  def button_event_wiki(self):
    # Get the selected event name
    if self.active_event:
      # Open the webpage
      webbrowser.open(f'https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search={self.active_event["name"]}&go=Go')
    else:
      # Message box
      messagebox.showinfo("No event selected", "Please select an event to view the wiki page for it.")

  def button_refresh(self):
    self.refresh()


  def button_back(self):
    self.previous_event()


  def button_forward(self):
    print("command")

  def on_list_event_suggestions_select(self, value):
    # Get the selected event
    selection = self.list_event_suggestions.curselection()
    if len(selection) == 0:
      return
    event = self.event_suggestions[selection[0]]

    self.select_event(event)

  def on_list_event_groups_select(self, value):
    # Get the selected event group
    selection = self.list_event_groups.curselection()
    if len(selection) == 0:
      return
    event_group = self.list_event_groups.get(selection[0])

    # Select the last event in the group after the most recent completed one
    focused_event = self.group_to_events[event_group][0]
    for i in range(len(self.group_to_events[event_group]) - 1, -1, -1):
      event = self.group_to_events[event_group][i - 1]
      if event["complete"]:
        focused_event = self.group_to_events[event_group][i]
        break

    self.select_event(focused_event)
  
  def on_list_events_select(self, value):
    # Get the selected event
    selection = self.list_events.curselection()
    if len(selection) == 0:
      return
    event = self.group_to_events[self.active_event["group"]][selection[0]]

    # Select the event
    self.select_event(event)

  def on_list_event_prereq_events_select(self, value):
    # Parse a possible selected event from the selected row
    # Text is like "..... (event=EVENT_ID)"
    selection = self.list_event_prereq_events.curselection()
    if len(selection) == 0:
      return
    text = self.list_event_prereq_events.get(selection[0])
    if text.find("(event=") == -1:
      return

    # Get the event id
    event_id = text[text.find("(event=") + 7:]
    event_id = event_id[:event_id.find(")")]
    if event_id not in self.events:
      # Event not found
      print(f"ERROR: Referenced event not found: {event_id}")
      return
    
    # Select the event
    self.select_event(self.events[event_id])
      

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
