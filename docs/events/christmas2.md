# Patent-Pending (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Snow-Covered Footprints](./christmas1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmas2
* Group: Main
* Triggered by label: christmas1
* Chain sources: christmas1
* Chain sources path: christmas1

## Official wiki page

[Patent-Pending](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas2&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label christmas2:
    q "Psst..."
    s "…"
    q "…"
    q "Psssssst..."
    q "[ayanemaster]..."
    q "Wake up..."
    s "…"

    if bonus == True:
        jump christmas2x
    else:
        "Unfortunately, I am too tired and remain asleep."
        "I am sorry, mysterious voice."
        "Thankfully, I can't imagine that missing out on whatever this is would impact story in any way."
        "I'm sure it was something completely random and not at all necessary for progression."

        $ renpy.end_replay()
        $ christmas2 = True
        $ ayane_lust += 1
        stop music fadeout 5.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day = 7
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date

label christmas3:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```