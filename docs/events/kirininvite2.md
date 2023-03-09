# No Extortion Necessary
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirininvite2&go=Go)



## Event preconditions
✅Event "[Kirin: Too Much, All at Once](./kirininvite1.md)" is completed (event=kirininvite1)

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Main: Let Me Die in Spring](./day261.md)

## Event properties
* ID: kirininvite2
* Group: Kirin
* Triggered by label: kirininvite
* Triggered by branch label: inviteover

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirininvite2:
    play sound "phonebeep.wav"

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "Our last meeting didn’t exactly go anywhere on account of Ami’s plans being cut short, but I’ve already confirmed that she will {i}definitely{/i} be gone this time around."
    "Unless...of course, she decides to cut things short again."
    "But that’s a chance I’m willing to take if it means getting some alone time with Kirin."

    if bonus == True:
        "Based on some of the things she said last time, there’s a high probability that she’ll, once again, be too nervous to try anything, but-"

    play sound "phonebeep.wav"

    if bonus == True:
        ki "Heya! Can I come give you a blowjob?"
        jump kirinfirstbjx
    else:
        ki "Heya! I'm in Mexico right now."
        s "What? But I thought we weren't allowed to leave Kumon-mi."
        ki "We can in the Patreon version."
        s "Oh. Well, uhh...have fun?"
        ki "Will do! Talk to ya later, Sensei!"

        play sound "phonebeep.wav"
        scene black
        with dissolve

        "I'm unable to hang out with Kirin because she went to Mexico =/"
        "I'll just print out a picture of her face and tape it to one of my pillows and hang out with that instead."

        $ renpy.end_replay()
        $ kirininvite2 = True
        $ kirin_lust += 3
        stop music fadeout 8.0

        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinsoccer15:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
label kirininvite:
    if kirininvite1 == False:
        jump kirininvite1
    if kirininvite1 == True and kirininvite2 == False:
        jump kirininvite2
...
```