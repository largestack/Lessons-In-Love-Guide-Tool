# Like Fucking a Cloud
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day86&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 86

✅Futaba lust greater than or equal to 5

❌Day of week is Friday



## Next events
None

## Event properties
* ID: day86
* Group: Futaba
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day86:
    scene hall_day
    with dissolve
    play music "sweetvermouth.mp3"

    "I decide to leave the girls to their own devices in gym class today."
    "Are they going to be fine on their own? Probably not. But I put Makoto in charge so, at the very least, everyone will be mostly contained."
    "Well, everybody except Futaba, that is."
    "Which isn't to say that she became some sort of delinquent overnight. I mean, how could she when she never even showed up to the class?"
    "In fact, the main reason I decided to wander the halls is to find her."
    "I get that gym class can be taxing when you aren’t comfortable with your body, but it's not like running away is going to do anything to change that."
    "Especially when consistently running away is a thing that would probably get me in trouble if any of the other staff members found out it."
    "It's not like I don't want to help her, of course."
    "I just don't know how..."
    "Especially when I don't even know where she is."

    scene black
    with dissolve2

    "Now..."
    "Where would I go if I didn’t want to participate in class?"
    "………"
    "……"
    "…"

    scene futabanurse1
    with dissolve

    f "Ah...S...Sensei..."
    s "I knew it."
    f "What...are you doing in here?"
    f "Aren’t you supposed to be in gym?"
    s "Isn’t that what I should be asking you? Why are you in the nurse’s office?"
    s "And...why isn't the nurse here?"

    scene futabanurse2
    with dissolve

    f "The nurse...doesn't work on Fridays."

    if bonus == True:
        jump futabanursex
    else:
        s "Excuse me? But what if someone gets hurt?"
        f "I guess they just...die?"
        s "That is unacceptable. We are finding a new nurse right now."
        f "But where will we find one on such short notice?"
        s "Leave it to me, Futaba. If there is anything I know how to do, it is spontaneously track down medical professionals in the middle of the day."
        f "Such a specific skill."

        scene black
        with dissolve

        "Futaba and I wander through the hall and I am able to find a new[school] nurse that will not abandon her responsibilities every Friday."
        "I will be damned if there is anyone in this[school] who does not do their job."

        $ renpy.end_replay()

        scene black
        with dissolve2

        $ futaba_lust += 1
        $ day86 = True
        stop music fadeout 7.0

        "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
        "………"
        "……"
        "…"

        jump afterschoolevent

label specialclassroom:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
...
```