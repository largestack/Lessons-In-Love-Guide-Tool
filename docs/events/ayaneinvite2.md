# One of Many Rooms
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayaneinvite2&go=Go)



## Event preconditions
✅Event "[Ayane: Hail Mary](./ayaneinvite1.md)" is completed (event=ayaneinvite1)

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
None

## Event properties
* ID: ayaneinvite2
* Group: Ayane
* Triggered by label: ayaneinvite
* Triggered by branch label: inviteover

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayaneinvite2:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer."
    "Ami told me earlier today that she was covering a shift for Uta at the maid cafe so, unless something has changed, the house should be completely empty tonight."
    "Ayane’s last visit to the house was nice, but I’m sure it wasn’t exactly the type of visit she was looking forward to."

    if bonus == True:
        "The blame for that falls on me, obviously, so the least I can do is make it up to her with some proper “alone time.”"
    else:
        "The blame for that falls on me, obviously, so the least I can do is make it up to her with some proper “hug time.”"

    play sound "phonebeep.wav"

    ay "[ayanemaster]! I was wondering when you would call."
    s "You were?"
    ay "Yes!"
    ay "I mean, I’m always wondering that. But I had a good feeling that it would actually happen today."
    s "I see..."
    s "Well, you’re in luck because I was wondering if you’d want to come over today."
    s "Ami isn’t going to be around and-"
    ay "I know. I’m already inside of your house."
    s "...Why?"
    ay "I was waiting for you to get home."

    if day < 6:
        s "How did you even get there so quickly? Class just ended a little while ago."
    else:
        s "Since when?..."

    ay "That doesn’t matter! Just hurry up and get over here so I don’t miss out on any teacher-time!"
    s "Again, please stop calling it that. I really don’t like it."
    ay "And I really don’t like being alone in your house, so run! Run, [ayanemaster]!"

    stop music fadeout 5.0
    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I hang up the phone and absolutely do {i}not{/i} run."

    if bonus == True:
        "Why would I waste energy on something like that when I’m likely going to wind up having sex as soon as I get there?"
        "I’m taking my time for Ayane’s sake. She should thank me for showing up fashionably late."

    "………"
    "……"
    play sound "dooropen.mp3"
    "…"

    scene lr2_noon
    with dissolve2
    play music "behindabathroom.mp3"

    "I don’t see Ayane when I walk into the house."
    "I figure this means she’s hanging out in my bedroom already, so I’m kind of excited to see what she has in store for me."

    if bonus == True:
        "She’s been here for god knows how long at this point so there might even be some sort of lavish set up like there was when I took her virginity."
        "I still think back on how cute that was sometimes."
        "Of course, that thought slips away when I remember the look on her face shortly after turning her into a woman."

    play sound "dooropen.mp3"
    scene bedroom_noon
    with fade

    s "Okay Ayane, let’s see what you’ve got..."
    s "...in store for me."
    s "…"

    "She didn’t leave, did she?"

    if bonus == True:
        jump ayaneamisbedx
    else:
        scene black
        with dissolve

        "In the end, it turned out that she did."

        $ renpy.end_replay()
        $ ayaneinvite2 = True
        $ ayane_lust += 3
        stop music fadeout 8.0

        "{i}Ayane’s lust has increased to [ayane_lust] even though she left and you didn't get to hug her!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or lust with her!{/i}"
        "{i}Hopefully, she won't leave next time!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label ayanelust15:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayaneinvite:
    if ayaneinvite1 == False:
        jump ayaneinvite1
    if ayaneinvite1 == True and ayaneinvite2 == False:
        jump ayaneinvite2
...
```