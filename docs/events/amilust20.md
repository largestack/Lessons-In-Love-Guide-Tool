# Conscious or Not
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amilust20&go=Go)


Part of event chain [Anglerfish](./halloweentwo5.md)

## Event preconditions
✅Ami lust greater than or equal to 20



## Next events
None

## Event properties
* ID: amilust20
* Group: Ami
* Triggered by label: amilust20intro

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label amilust20:
    s "…"
    a "…"

    scene amilusttwenty23
    with dissolve

    if bonus == True:
        jump amilust20x
    else:
        a "Wanna hug?"
        s "Sure. Hugs are nice."

        scene black
        with dissolve

        "We hug."

        $ renpy.end_replay()
        $ amilust20 = True
        $ ami_lust += 3
        stop music fadeout 5.0

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "………"
        "……"
        "…"

        jump halloweentwo6

label halloweentwo6:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
scene amilusttwenty11
    with dissolve
    play sound "knock.mp3"

    a "Uhh...Noriko?"
    a "Is {i}this{/i} the one?..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty12
    with dissolve
    play sound "knock.mp3"

    a "Hello?...Anyone home?..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amilusttwenty13
    with dissolve
    play sound "knock.mp3"

    a "Noriko! Where the fuck are you and why does this house have so many identical bathrooms?!"
    s "Ami, this might be a strange question, but you’re sure these have all been {i}different{/i} bathrooms, right?"

    scene amilusttwenty14
    with dissolve

    a "What do you mean?"
    s "I just mean that...isn’t it possible we’ve been going in circles?"
    s "We’ve been walking around these halls for like ten minutes now and have seen like...twenty identical bathrooms."
    s "What if we’re just...circling back around to the same one over and over again?"

    scene amilusttwenty15
    with dissolve

    a "Hah...you’re right..."
    a "This is pointless."
    a "I think I understand now why you never try to do anything nice for anybody. This is exhausting and we haven’t even {i}found{/i} Noriko yet."
    s "I’m telling you, she’s probably fine. "
    s "Noriko’s strong and independent and...whatever. Even if she’s freaking out about me and her sister right now, she’ll calm down soon enough."

    scene amilusttwenty16
    with dissolve

    a "Wait, did something happen with you and Niki? Is that why she was crying?"
    s "Nope. I never said that."
    a "But I just-"
    s "Nope. Time to get back to the party."

    "If we can even find our way back at this point..."

    scene amilusttwenty17
    with dissolve
    play sound "knock.mp3"

    a "Norikoooooo, come onnnnnnnn..."
    s "Knocking on the same door more times isn’t going to just make her appear, Ami."
    a "I know that...but this is such a boring ending to what I thought was going to be a fun Halloween adventure."
    s "I agree. But at least you got to spend it with me. I’m sure that should hold you over for the rest of the night, right?"

    scene amilusttwenty18
    with dissolve

    a "Can you kiss my hand? It hurts from all of the knocking."
    s "I can not."
    a "Do you hate me now? Is that what’s happening here?"
    s "I do not."

    scene amilusttwenty19
    with dissolve

    a "Darn it..."

    "Ami stops knocking for a moment and rests her arm against the door of one of many identical bathroom stalls we’ve encountered tonight."
    "And given that she spends most of her free time either reading manga or watching TV with Ayane, it’s probably safe to say this is the most exercise she’s gotten in a while."

    if amifingered == True and bonus == True:
        "Well, non-sexual exercise, at least. "
        "But I feel like counting all of that stuff is a little unfair since she is known to get quite into it."

    scene amilusttwenty20
    with dissolve

    a "Um...Sensei?"
    s "Yeah? What’s up?"
    a "Do you..."
    a "Do you maybe want to..."

    if ami_lust >= 20:
        jump amilust20
...
```