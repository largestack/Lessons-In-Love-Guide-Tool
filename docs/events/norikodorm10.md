# Kind Of, Yes. Kind Of, No.
Noriko event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikodorm10&go=Go)



## Event preconditions
✅Noriko love greater than or equal to 10

✅Event "[Noriko: Mouthjob](./convenience5.md)" is completed (event=convenience5)

✅Event "[Kirin: Terms & Conditions](./kirindorm20.md)" is completed (event=kirindorm20)



## Next events
* [Noriko: New Shoes](./norikoinvite1.md)
* [Noriko: Beginnings. Endings. Things in Between.](./norikoinvite2.md)

## Event properties
* ID: norikodorm10
* Group: Noriko
* Triggered by label: norikodorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label norikodorm10:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Noriko’s door and wait for her to answer."
    "I already know she works late most nights, so I won’t be surprised if she’s out."
    "But, since my luck always seems to be at least mildly good, I think the chances of us being able to spend some time alone together tonight are pretty solid."

    n "Come in!"

    "And so it appears that my mildly good luck prevails once more."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "wewereangels.mp3"

    "I push open the door to find that the typically fruity smell of the room has vanished. "
    "Today it’s something more like...laundry detergent."

    if bonus == True:
        jump norikounderx
    else:
        s "Oh, wow. You're doing laundry."
        n "Yup! Mind lending me a hand, Sensei?"
        s "Sure thing, buddy."

        "I help Noriko folder her laundry and then go immediately home."
        "I find 500 yen in one of her pockets and keep it to myself to invest it in Shiba Inu."
        "I am going to be rich."

        $ renpy.end_replay()
        $ noriko_love += 1
        $ norikodorm10 = True
        stop music fadeout 5.0

        "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label norikodorm25:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
    if noriko_love >= 10 and convenience5 == True and kirindorm20 == True and norikodorm10 == False:
        jump norikodorm10
...
```