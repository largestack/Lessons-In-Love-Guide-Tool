# Backwards Spider Crawl (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 68

* Ayane lust greater than or equal to 5



## Next events

None

## Event properties

* Id: day68
* Group: Ayane
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day68

## Official wiki page

[Backwards Spider Crawl](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day68&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day68:
    scene gym
    with dissolve
    play music "normalday.mp3"

    "You know, if you came up to me and forced me to choose only one subject to be able to teach for the rest of my life-"
    "I would probably choose none of them."
    "Teaching sucks."
    "But, in the event that I'd, for some reason, be unable to forfeit the profession, I think I’d have to go with gym."
    "Sure, there are plenty of people who view physical education as the ground floor of this field but, when you really think about the day to day lives of people in that specific line of work, wouldn't you say they've got it pretty good?"
    "Look at me. I'm resigned to only one period per day in the gym and I'm ecstatic about the amount of form fitting clothing and exposed skin I get to see. Imagine I got to do this full time?"
    "I wonder if the impact would ever lessen."
    "Plus, if I was a gym teacher, I'd never have to actually worry about the whole {i}teaching{/i} part of the job and could just...make girls do squats all day or something."
    "I guess what I'm getting at is that this period is one of the few things keeping me attached to this job and-"

    ay "Sensei! Over here!"

    "And speaking of attachment, it looks like I'm going to be spending {i}today's{/i} physical education class with none other than Ayane Amamiya."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene ayanefirstlust1
    with dissolve

    s "What are you doing?"
    ay "What am {i}I{/i} doing? Just waiting for my favorite teacher in the whole wide world to realize that I'm all by myself so he feels inclined to spend time with me."
    s "Well, it worked. But if anyone asks, I guess just tell them you're not feeling well or something because there is no way this isn't going to stick out to the other girls."
    ay "Sensei! You would have me {i}lie{/i} to my friends? Just what kind of girl do you think I am?"
    s "The kind who had no problem designing her entire gym period around manipulating me into talking to her."

    scene ayanefirstlust1r
    with dissolve

    ay "Since when is carefully plotting my actions for the sole purpose of getting you to act in a certain way manipulation?!"
    s "That is quite literally what manipulation is."

    scene ayanefirstlust1r2
    with dissolve

    ay "Well, in {i}my{/i} book, we call that {i}love.{/i}"
    ay "Besides, I'm not really in the mood to run right now anyway."
    s "And why is that, Ayane?"

    if bonus == True:
        jump ayanefirstlustx
    else:
        scene black
        with dissolve

        ay "I really want a hug."
        s "Okay."

        "I quickly hug Ayane before anyone notices."

        $ renpy.end_replay()
        $ day68 = True
        $ ayane_lust += 1
        stop music fadeout 5.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "………"
        "……"
        "…"

        jump afterschoolevent

label day70:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
$ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
...
```