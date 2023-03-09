# Three Words
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikaonsen3&go=Go)


Part of event chain [Bleed](./chikaonsen2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: chikaonsen3
* Group: Chika
* Triggered by label: chikaonsen2

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label chikaonsen3:
    scene chikavirgin1
    with dissolve
    play music "asobeatsex3.mp3"

    c "Uhh...where did that TV come from?"
    s "I asked the front desk if they had one and they brought it over."
    c "What happened to taking a bath?"
    s "I took one. I just didn’t realize how long you were going to be gone for."

    scene chikavirgin2
    with dissolve

    c "Yeah...sorry about that."
    c "That woman, Tsubasa. The one we met when we got here..."
    c "The two of us started talking for a little bit and time just sorta flew by without me realizing it."
    s "I see."
    s "Well I’m glad you’re back."
    c "Yeah. Me too."
    c "Whatcha watching?"
    s "This place only has basic cable, so it’s just some random baseball game."
    c "Cool, cool."
    c "Mind if I watch it with you?"
    s "I’m not really watching it. I was just figuring out how to pass the time."

    scene chikavirgin3
    with dissolve

    c "Oh, cool. Then you won’t mind if I do this."

    if bonus == True:
        jump chikavirginx
    else:
        scene black
        with dissolve

        "Chika walks in front of me and gives me a long, aggressive hug."
        "Unbeknownst to her, I do mind. She is interrupting my television program."
        "Anyway, we hug for a little while longer. And even though we have hugged many times before, this hug seems particularly important."

        $ renpy.end_replay()
        $ chika_virgin = False
        $ chikaonsen3 = True
        $ chika_love += 5
        stop music fadeout 10.0

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "………"
        "……"
        "…"

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
        else:
            "ERROR"

        "{i}[totaldays] days have passed...{/i}"

label chikaonsen4:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```