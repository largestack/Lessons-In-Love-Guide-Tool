# Lessons In Love Walkthrough Guide Tool

Would you like help with understanding what the next step in your Lessons in Love playthrough should be? This is the tool for you!

Lessons In Love Guide Tool looks at your most recent save game, and lets you know what events you can perform next and their requirements. End all the endless trial and error to find the next event to trigger!

Also see [the guide tool website here](http://largestack.github.io/Lessons-In-Love-Guide-Tool/) for a list of events and code corresponding to game events. You can go here if you are stuck on an event to see the code.

## Game version supported
This tool works for any game version, since it loads the events from the version of the game installed on your device.

## Installation - Windows
Download the [latest release](https://github.com/largestack/Lessons-In-Love-Guide-Tool/releases) executable here and run it.

## Installation - Linux or macOS
1. Download and extract the entire repo.
1. Install Python 3.7
1. Install the dependency packages:
* `pip install tkinter`
* `pip install webbrowser` (used to launch the event wiki pages)
4. From terminal run `python main.py` or `python3 main.py`.

## Using the tool

1. Run the tool.
1. On first run, it will ask you to select the base game folder.
1. It will automatically load the most recent save-game every time it loads.
1. You can also hit the "Reload" to load the most recent save game again. You can do this to refresh the guide tool while you play the game. Simply save your game, then hit "Reload" to update the guide.

<img src="./docs/images/UserInterface.png" width="70%" height="70%">

* **Suggested next events**: Click on these events to see what's required for the next suggested events.
* **Event group**: Browse events by character and main path.
* **Event**: The list of events for the selected event group.
* **Event prerequisites**: The requirements for the event to trigger.
* **Event raw details**: Some extra notes about the event.
