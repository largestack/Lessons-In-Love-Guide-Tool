# Turn Off The Lights (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: specialclassroom
* Group: Happy scenes
* Triggered by label: inviteover
* Triggered by branch label: inviteover
* Triggered by path: inviteover->specialclassroom

## Official wiki page

[Turn Off The Lights](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=specialclassroom&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label specialclassroom:
    play sound "static.mp3"
    scene specialclassroom1
    with flash
    stop sound
    play music "holyplace.mp3"

    "I arrive in a special classroom situated somewhere underneath Heaven."
    "The room smells like someone left dirty laundry in it to fester in the summer sun for years on end."
    "The only problem is that no sun can reach this room."
    "Night is still hours away and yet everything is dark."
    "…"
    "I try to move my legs forward and escape from the room but, as has become customary in times like these, I can not."
    "I look down to inspect them to see if they’ve been pinned or nailed to the ground and discover that I have no form at all."
    "I am a shadow now."
    "But whose shadow am I?"

    play sound "static.mp3"
    scene specialclassroom2
    with flash
    stop sound

    "The same girl that always shows up when I am {s}lost{/s} happy appears before me."
    "Her hushed breaths sound more like atomic bombs due to how quiet it is in here. "

    s "Maya?..."
    q "…"
    q "あなたは誰?"
    q "だれ です か？"

    "I don’t understand a word she’s saying. "
    "I wish she would turn around so I could at least confirm that she is who I think she is."
    "Sometimes, Maya’s eyes go away in my dreams. "
    "They’re replaced with old TV static and memories of thousands of lives I have yet to live."
    "That must be why it terrifies me so much to gaze into them."

    if bonus == True:
        "That must be why it terrifies me to imagine receiving oral sex from her as she stares at me with empty spheres in place of gorgeous aquamarine beads."
        "I can feel myself becoming aroused at the thought of doing horrible things to her in my [niece]’s bed and need to remind myself that I am a shadow."
        "I will always be a shadow."
        "And shadows can not form erections the same way normal humans do."

    q "Please-"
    q "Come closer if you wish to speak in your language."

    "I click my heels together and-"

    if bonus == True:
        jump specialclassx
    else:
        scene black
        stop music
        "The event ends."
        "This is the wrong game."

        $ renpy.end_replay()

        $ specialclassroomtrack = True
        $ specialclassroom = False

        jump saturdaynight

label day110:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label inviteover:

    # Use the new phone UI when enabled
    if use_new_phone_ui == True:
        jump phone_night

    "Who should I invite over?"
    if specialclassroom == True and day >= 6:
        menu:
            "There is something buried underneath your feet":
                jump specialclassroom
...
```