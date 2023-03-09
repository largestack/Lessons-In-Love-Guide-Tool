# Ahead of the Curve
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm20&go=Go)



## Event preconditions
✅Molly love greater than or equal to 20

✅Event "[Molly: The Legacy of Thaum Pt. II](./mollycafe20.md)" is completed (event=mollycafe20)



## Next events
* [Main: Operation: Firestarter](./day318.md)

## Event properties
* ID: mollydorm20
* Group: Molly
* Triggered by label: mollydorm
* Triggered by branch label: mollydorm

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label mollydorm20:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait for her to answer."
    "I can hear a slight rustling inside of the room, so if she’s not in there it’s either Tsuneyo or..."
    "An intruder."

    play sound "knock.mp3"
    stop music fadeout 35.0

    s "Okay, intruder. Get out of Molly’s room."

    "…"
    "Another few seconds go by without an answer, I begin to suspect that either Molly has her headphones on or is just knowingly avoiding me for some reason."
    "No one avoids me during my free time and gets away with it."
    "Especially not someone like Molly MacCormack."
    "If that actually {i}is{/i} her inside of the room and not Tsuneyo or an intruder."

    s "…"

    play sound "knock.mp3"

    s "Open up. I can hear you in there."

    "I press my ear against the door to confirm that I {i}did{/i} actually hear something moments ago...and I can’t really tell if I did or not."
    "It's definitely quiet now."
    "That doesn’t put an end to my curiosity, though."
    "Maybe I should try going in?"
    "What should I do?"

    menu:
        "Open the door":
            "Obviously I’m going to try and open the door."
        "Don’t not open the door":
            "Obviously I’m not going to not open the door."

    "There was always only one choice."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I push the door open, hoping that if it {i}is{/i} an intruder inside that they also happen to be wearing headphones for some mysterious reason."
    "That way, I’d be able to take them down before-"

    if bonus == True:
        jump mollymastx
    else:
        s "..."

        "Actually...on second thought, I'm kind of hungry."
        "Maybe I'll just go get some spaghetti instead."

        mo "I like Rin!"
        s "Woah. I was just leaving. Don't just shout plot stuff at me."
        mo "Rin doesn't like me! But I like her!"
        s "Ughhhhhh I just wanted spaghetti."

        "I spend the next few minutes trying to get away from Molly, but she is Molly so it is hard."
        "Eventually, she goes to sleep."
        "The spaghetti place is closed by the time I get there."
        "Darn it."

        $ renpy.end_replay()
        $ molly_love += 1
        $ mollydorm20 = True
        stop music fadeout 8.0

        "{i}Molly’s affection has increased to [molly_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label tsuneyodorm15:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label mollydorm:
    if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
        jump mollydorm5
    if molly_love >= 10 and mollydorm5 == True and mollycafe10 == True and mollydorm10 == False:
        jump mollydorm10
    if molly_love >= 15 and christmas7 == True and mollydorm15 == False:
        jump mollydorm15
    if molly_love >= 20 and mollycafe20 == True and mollydorm20 == False:
        jump mollydorm20
...
```