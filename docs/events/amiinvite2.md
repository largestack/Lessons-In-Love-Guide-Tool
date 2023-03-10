# Rising to the Challenge (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Living](./amiinvite1.md) (Ami) is completed)

* amiinvite2miss equal to False (unknown variable)

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: amiinvite2
* Group: Ami
* Triggered by label: amiinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->amiinvite->amiinvite2

## Official wiki page

[Rising to the Challenge](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amiinvite2&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amiinvite2:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "………"
    "……"

    play sound "phonebeep.wav"

    a "Helloooo~ What’s up, [amimaster]?"
    s "Hey. Do you have some free time tonight?"
    a "I always have free time for you. Is there something you had in mind?"
    s "Why don’t we just hang out in my room and see where that takes us?"

    if bonus == True:
        a "So you want to have sex?"
        s "I mean, I don’t {i}not{/i} want to have sex."
    else:
        a "I bet it's toward a hug."
        s "Hugs are even better than elephants."

    a "Saying it that way is confusing. You should be more honest about what you want."
    s "I’m hanging up now, Ami."

    if bonus == True:
        a "Okay! I’ll go take a bath and get myself ready!"
    else:
        a "You're so weird!"

    a "Love you, [amimaster]!"

    play sound "phonebeep.wav"

    s "…"

    "Well, she definitely wasn’t holding anything back just now."

    scene black
    with dissolve2
    stop music fadeout 10.0

    if bonus == True:
        jump amithighx
    else:
        s "But neither was I..."
        s "I am prepared to hug."

        "I go home and hug Ami a few times."

        $ renpy.end_replay()
        $ amiinvite2 = True
        $ ami_lust += 1
        stop music fadeout 8.0

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "{i}You can now invite her over on nights and choose to raise either your affection or hug her!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amiinvite3:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amiinvite:
    if amiinvite1 == False:
        jump amiinvite1
    if amiinvite1 == True and amiinvite2 == False and amiinvite2miss == False:
        jump amiinvite2
...
```