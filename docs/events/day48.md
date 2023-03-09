# Little Girl
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day48&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 48



## Next events
None

## Event properties
* ID: day48
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day48:
    scene bedroom_day
    with dissolve2

    "I wind up waking up without Ami's assistance, which is strange given that today is a[school] day...so I quickly begin going over possible explanations for this in my head."
    "Explanation 1: She was murdered."
    "Explanation 2: Today is some sort of national holiday that I am unaware of."
    "Explanation 3: She was murdered {i}and today is some sort of national holiday that I am unaware of."
    "I'm really hoping it's not that last one because it sounds like it would make arranging her funeral very difficult."

    play sound "dooropen.mp3"
    scene black
    with dissolve2

    "I walk out into the kitchen and prepare myself for whatever crime scene awaits."
    "However, what awaits is no crime scene at all..."

    scene amicouch1
    with dissolve2
    play music "love.mp3" fadein 3.0

    "It's simply the girl who didn't wake me up this morning, half-passed out with a huge blanket I have never seen before pulled over her body."

    a "I think...I might be dying..."

    if bonus == True:
        jump littlegirlx
    else:
        s "Say no more. I will save you."

        scene black
        with dissolve
        stop music fadeout 10.0

        a "Sensei?...Everything is going dark..."
        s "Stay with me, Ami."

        "I toss the blanket off of her and remove a scalpel from my pocket, carefully holding it against her trachea before making a small incision and reaching two of my fingers inside of it."

        s "What have you been hiding in here, Ami?"
        a "Ack! Mlemmaggahhhagggahhhhhahhhssssssssss!!!!!"

        "My fingers get kind of gross, but I have to save Ami because if I don't my taxes will never get filed on time."

        s "Wait, what is this?"

        "I feel something hard somewhere in her throat, but I have to make the incision larger to get it out."

        s "Hold still. This may hurt a bit."
        a "(Airplane noises)"

        "By now, my entire hand inside of her throat. But I have finally managed to get a good grip on whatever item she decided to hide inside of her."

        s "Ami...what is this?"
        a "Acckkkckkcipojfgoihdfoigjpoidsf[osadikfposjudfo~~~~!!!!!!!!!!!!!~~~~~~~~~~"

        play sound "alert.mp3"
        scene colorbars

        s "How did you manage to hide so many pretty colors inside of you"
        a "7"

        "One by one, I remove the colors from her body until there are none left."

        s "You are safe now."

        "I sew her throat back up, but make a few mistakes since I haven't taken a sewing class in many years."
        "Self-conscious about the job I did, I heat up a spoon over the stove and press it against the laceration, held together by red thread, and burn it closed."
        "The bleeding stops and Ami recovers."

        a "Sleep now."
        s "Yes, Ami."
        s "Sleep now."

        "Ami goes to sleep."
        "I did a good thing today."
        "God would be proud of me."

        scene bedroom_night
        with dissolve

        "Sensei sleep now too."

        scene black
        with dissolve

        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ day48 = True

        if day == 1:
            jump advancetotues
        if day == 2:
            jump advancetowed
        if day == 3:
            jump advancetothurs
        if day == 4:
            jump advancetofri
        else:
            jump advancetosat

label day50:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
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
...
```