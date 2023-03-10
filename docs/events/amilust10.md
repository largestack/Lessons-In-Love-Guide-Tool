# Wake Up Call (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Summer and Winter](./beachvacation9.md)

## Event preconditions

* Ami lust greater than or equal to 10



## Next events

None

## Event properties

* Id: amilust10
* Group: Ami
* Triggered by label: endofbeachvac9
* Chain sources: beachvacation9
* Chain sources path: beachvacation9->beachvacation9

## Official wiki page

[Wake Up Call](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amilust10&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label amilust10:
    scene amibeachlust1
    with dissolve2

    "{i}The next morning...{/i}"

    play sound "slidedoor.mp3"

    a "Ugh...Is he really going to spend the entire morning sleeping?"
    a "Sensei! Are you up?"
    s "…"
    a "Senseiiiii~"

    play sound "slidedoor.mp3"
    scene amibeachlust2
    with dissolve

    a "Sensei. It’s almost 10 AM. That means it’s time to..."

    if bonus == True:
        jump amilust10x
    else:
        a "..."
        a "Eh. Nevermind."

        scene black
        with dissolve

        "Ami leaves the room without doing anything because this is a family friendly game."

        $ renpy.end_replay()
        $ ami_lust += 1
        $ amilust10 = True

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "………"
        "……"
        "…"

label amilust10skip:
    scene amibeachlust1
    with dissolve2

    "{i}The next morning...{/i}"

    play sound "slidedoor.mp3"

    a "Ugh...Is he really going to spend the entire morning sleeping?"
    a "Sensei! Are you up?"
    s "…"
    a "Senseiiiii~"

    play sound "slidedoor.mp3"
    scene amibeachlust2
    with dissolve

    a "Sensei. It’s almost 10 AM. That means it’s time to..."

    if bonus == True:
        jump amilust10skipx
    else:
        a "..."
        a "Eh. Nevermind."

        scene black
        with dissolve

        "Ami leaves the room without doing anything because this is a family friendly game."

        $ renpy.end_replay()

        "………"
        "……"
        "…"

label beachvacation10:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label endofbeachvac9:
    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
    else:
        "ERROR"

    "{i}[totaldays] days have passed...{/i}"

    if ami_lust >= 10:
        jump amilust10
...
```