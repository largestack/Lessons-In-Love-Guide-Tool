# Wicked Witch of Kumon-mi (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Samhain](./halloween10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween11
* Group: Main
* Triggered by label: halloween10
* Chain sources: halloween10
* Chain sources path: halloween10

## Official wiki page

[Wicked Witch of Kumon-mi](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween11&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween11:
    scene makotohalloween1
    with dissolve2
    play music "letsfuckingo.mp3"

    "It isn’t long before I wind up finding her."
    "I mean, after all, the party is in one giant room and she’s the only one with a huge hat."
    "So, considering my eyes function the way a normal person’s eyes do-"
    "Yeah."

    mak "Well, you sure took your time."
    mak "Where’d you go with the two new girls? "
    s "We were in the yard being overly-sentimental for a little while. I’m back to normal now, though."
    s "Well, technically, they’re the ones who were being overly-sentimental."
    s "I just kind of stood there and let them cry."
    mak "You’re such a nice *hic* guy. You know that?"
    s "..."
    mak "...?"
    s "Are you drunk?"
    mak "Are {i}you{/i} drunk?"
    s "No. No, I am not."
    mak "Do you {i}wanna{/i} be drunk?"
    s "Probably not. I’ll wind up saying or doing things that could get me into a lot of trouble with this particular group."
    s "When did you even start drinking? How long was I gone?"
    mak "Long enough for me to start drinking, obviously."
    s "Well, good for you."
    s "It’s nice to see you letting loose instead of bossing everyone around."
    s "You deserve this."
    mak "That’s right. You know what else I deserve, though?"
    s "What, Makoto?"

    scene makotohalloween2
    with dissolve

    if bonus == True:
        jump makotovirginx
    else:
        mak "A hug."
        s "I thought you'd never ask."
        scene black
        with dissolve2

        "Makoto and I hug, but this particular hug is more special than all of the other hugs since it's the one she's been begging for since I found out she thought I was awesome."
        "The important hug happens in a room that no one else knows about."
        "We have to pull a specific book off a shelf to even get in. It's kind of crazy and makes me feel like a spy or something."
        "I should hug Makoto more frequently from this point on."

        $ renpy.end_replay()
        $ makoto_virgin = False
        $ makoto_love += 5
        $ halloween11  = True
        stop music fadeout 6.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "………"
        "……"
        "…"
        "{i}While that was happening...{/i}"

        jump halloween12

label halloween12:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```