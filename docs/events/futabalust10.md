# Selfless (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Christmas Miracle](./christmas6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: futabalust10
* Group: Futaba
* Triggered by label: futabalust10intro
* Chain sources: christmas6
* Chain sources path: christmas6->christmas6

## Official wiki page

[Selfless](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabalust10&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label futabalust10:
    scene futabalustten5
    with dissolve
    stop music fadeout 20.0

    if bonus == True:
        jump futabalust10x
    else:
        scene black
        with dissolve

        "Futaba tells me all about how her mother was killed in a raid by the fire nation in an attempt to uncover the last water bender in her village."
        "Now Futaba has to help some kid with a weird tattoo save the world or something. I don't really know."
        "But she's clearly got a lot more important shit to deal with than hanging out with me, so I decide to leave her alone for the rest of the night."

        $ renpy.end_replay()
        $ futabalust10 = True
        $ futaba_lust += 1

        "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
        "………"
        "……"
        "…"

        jump christmas7

label christmas7:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label futabalust10intro:
    scene futabalustten1
    with dissolve

    f "Umm...Hi, Sensei."
    f "Is there a reason you’ve decided to hang out here instead of going downstairs with everyone else?"
    s "Wouldn’t the same go for you? "
    s "Go enjoy your youth or whatever it is someone in my position is supposed to say right now."
    f "Maybe in a bit. Things have been pretty...hectic in here tonight and I’m trying to avoid getting a headache."
    s "I get that. Molly’s little game sure shook things up a bit."

    scene futabalustten2
    with dissolve

    f "And of course I’m going to be the one who has to hear about it for the next month."
    s "A month? I don’t think it will take Rin that long to get over something as trivial as a little kiss."

    scene futabalustten3
    with dissolve

    f "Sensei! A girl’s first kiss is important!"
    f "It probably sounds silly to you, but a lot of people really care about that stuff."
    s "Are you one of those people, Futaba?"

    scene futabalustten4
    with dissolve

    f "I {i}was{/i}. "

    if bonus == True:
        f "Now we do naughty stuff all the time and I’m starting to think I’ll go the rest of my life without ever being kissed by anyone."
        s "Did I really corrupt you this much without ever kissing you?"
    else:
        f "But everything changed when the fire nation attacked..."
        s "=("

    if futaba_lust < 10:
        scene futabalustten5
        with dissolve

        if bonus == True:
            f "Some might say you haven’t corrupted me enough."
            f "I’m sure in some alternate timeline, my lust for you would be even higher and we’d wind up doing something pretty risky while everyone else was downstairs."
            s "Does that mean that isn’t going to happen in this particular timeline?"
            f "Mhm."
            f "Well, not today at least."
            f "But we can still hang out and talk for a little while before heading down."
            f "I’m curious to hear about whatever it is Yumi wrote in that notebook for you."

            scene black
            with dissolve2

            "Just as she suggests, Futaba and I spend the next five or ten minutes talking about the gifts we received tonight."
            "It turns out that Maya’s exchange with her wasn’t exactly lengthy and that she just handed her a gift card on her way out the door, but Futaba apparently doesn’t care for presents much anyway."
            "She talks about how she much prefers buying things for herself so she can be sure she’ll like something- and it’s really just the thought that counts at the end of the day."
            "And while some people might think giving someone a gift card has no thought to it at all, 100%% of the people in this room disagree- and that’s more than enough for me."
            "…"
            "Eventually, the two of us decide to head back downstairs to meet up with everyone else."
            "To avoid suspicion, I go to exit the room first while Futaba runs into the bathroom to adjust her makeup."
            "But, just as I reach for the handle, it opens on its own and someone rather peculiar steps in."
        else:
            scene black
            with dissolve

            "Futaba tells me all about how her mother was killed in a raid by the fire nation in an attempt to uncover the last water bender in her village."
            "Now Futaba has to help some kid with a weird tattoo save the world or something. I don't really know."
            "But she's clearly got a lot more important shit to deal with than hanging out with me, so I decide to leave her alone for the rest of the night."

        stop music fadeout 5.0

        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ futabalust10miss = True
        jump christmas7

    else:
        jump futabalust10
...
```