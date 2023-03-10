# Bad Kitty (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Kadrillionbilliontrillion](./halloween14.md)

## Event preconditions

* Haruka lust greater than or equal to 10

* Event [Drunk Again](./harukadate1.md) (Haruka) is completed)



## Next events

* [Maki: Thank You For Your Business](./makidate15.md)

## Event properties

* Id: harukalust10
* Group: Haruka
* Triggered by label: halloween14
* Chain sources: halloween14
* Chain sources path: halloween14

## Official wiki page

[Bad Kitty](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukalust10&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label harukalust10:
    play sound "dooropen.mp3"
    scene harukamakithreesome1
    with dissolve
    play music "asobeatsex2.mp3"

    s "…"

    "I let myself into Haruka’s house after finding out through text that she had left the door open for me."

    if bonus == True:
        "Probably not the best idea given that someone else could have wandered in here and rightfully claimed my threesome, but the house seems undisturbed so I think I’m in the clear."

    s "Haruka? Maki? Where are you two?"
    h "WE’RE HIDING!~"
    s "Why?..."
    h "Because we’re [young]and full of life! It’s a game, nyaa~"
    s "{i}...Nyaa?{/i}"

    "Now, I’m not exactly familiar with Haruka’s house, but I {i}do{/i} know the way to the bedroom."
    "So here’s hoping the two of them have decided to hide in there and not some place weird like a laundry closet or something."

    maki "Are you coming or not?! We can’t hold this pose all night!"
    s "Pose? What are you two doing?"
    h "Come see for yourself, LOSER!"

    scene black
    with dissolve

    "Why does Haruka always have to call me a loser when she’s drunk?"

    if bonus == True:
        "Is that supposed to turn me on or something?"

    scene harukamakithreesome2
    with dissolve

    "I stop in front of Haruka’s bedroom door and can hear some hushed giggles escaping from the crack beneath it."

    s "Pretty sure I’ve found you. Can I have my reward now?"
    h "Who’s stopping you, LOSER?"
    s "Again with the loser thing. Why do you keep doing this?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    h "Probably because you’re a LOSER! Hehehe..."

    if bonus == True:
        jump catthreex
    else:
        s "I have had enough. I am leaving."
        h "Hahaha! Okay, LOSER!"

        "Haruka is so mean and it makes me sad."

        $ renpy.end_replay()

        "{i}Congratulations! You have completed the first ever Halloween update for Lessons in Love!{/i}"
        "{i}Christmas is right around the corner.{/i}"
        "{i}How crazy would it be if there were an event for that next?{/i}"
        "{i}Oh, and also-{/i}"

        $ haruka_lust += 1
        $ harukalust10 = True
        stop music fadeout 5.0

        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "………"
        "……"
        "…"

        jump advancetomon

label harukalust10skip:
    play sound "knock.mp3"

    "I bang on Haruka’s door, eager to get inside and see her and Maki drunk again."
    "I have to admit, I wasn’t expecting a call this random, especially on a Sunday night, but who knows what those two get up to during holidays?"
    "I mean, they’re definitely a lot closer than I expected them to be, so anything is possible I guess."

    h "Come in, Sensei! The door is open!"

    play sound "dooropen.mp3"

    "I open the door, ready to experience what I imagine will be the best night of my life."

    scene harukalusttenskip1
    with dissolve
    play music "normalday.mp3"

    h "Hey! Thanks for coming on such short notice. "
    h "I realize that Sunday night is a little late to be calling you to fix our pipes, but neither of us knew how so..."
    maki "You’re a real life saver. I can’t even remember the last time my pipes were fixed."
    s "Oh, uhh. Yeah. Why aren’t you wearing your costumes, though?"

    scene harukalusttenskip2
    with dissolve

    h "Hm? Why would we be wearing our costumes? The party was yesterday."
    s "Well, because-"
    s "Wait a second."

    scene harukalusttenskip3
    with dissolve

    s "…"
    h "Uhh, something wrong?"
    maki "Are they beyond repair?"
    s "What the fuck are these?"
    h "Those are the pipes we need you to fix, obviously. "
    s "…"
    maki "…"
    maki "Oooooooh."
    maki "Oof."
    maki "That’s embarrassing."
    h "What’s embarrassing? I don’t get it."
    maki "Just a misunderstanding. Poor guy."
    h "Wait, so are the pipes being fixed or not?"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene bedroom_night
    with dissolve
    play sound "dooropen.mp3"

    "I walk into my bedroom after an incredibly anti-climactic end to the weekend."
    "I will likely never forget this moment for as long as I live."
    "And I am now also forced to take every single innuendo I hear literally until proven otherwise."

    scene black
    with dissolve

    s "Ugh..."
    s "Halloween is the worst."

    "{i}Congratulations! You have completed the first ever Halloween update for Lessons in Love!{/i}"
    "{i}Christmas is right around the corner.{/i}"
    "{i}How crazy would it be if there were an event for that next?{/i}"

    stop music fadeout 5.0

    "........."
    "......"
    "..."

    jump advancetomon

label trinity3:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
play sound "phonebeep.wav"

    scene mollydrunk30
    with dissolve

    s "Hello?"
    mo "Tch! Stupid phones. Stealin ‘me teacher away from me."

    if bonus == True:
        h "HEY, PENIS MAN."
    else:
        h "HEY, HUGGY BOY."

    s "…"
    s "Hello, Haruka."
    h "I’M DRUNK~"
    s "Yes, I can tell. "
    h "Wanna come fix my pipes?"
    s "I’m kind of in the middle of-"
    h "Maki’s pipes too~"

    play sound "phonebeep.wav"

    "I hang up the phone and turn back to the girls, ready to disappoint them."

    s "Duty calls."

    scene mollydrunk31
    with dissolve

    c "Huh? Who was that?"
    f "Is something wrong, Sensei? Are you leaving already?"
    s "A friend of mine is having a bit of an emergency and needs my help as soon as possible."
    c "Is everything okay? Because we’re having a bit of an emergency here as well."
    mo "I can *hic* stand. T’aint no emergency here."
    mo "I’m *hic* fine on ‘me own ‘til ‘me legs give out."
    mo "Help 'yer friend..."

    scene mollydrunk32
    with hpunch

    mo "BUT KNOW T'IS, SIR."
    mo "EVEN IF YE' LEAVE ME HERE FOREVER-"
    mo "I WILL ALWAYS LOVE YOU!"
    c "…"
    f "…"

    scene mollydrunk33
    with dissolve

    mo "T’s wit’ all ‘ta starin’? I saw him first so he belongs ‘ta me!"
    c "You were actually one of the last people to see him."
    f "Sensei doesn’t believe in love in the first place."
    s "As much as I’d like to stay here and argue over Molly’s love for me, I really do need to get going."

    if bonus == True:
        "Like Hell am I going to miss the chance for a threesome with Haruka and Maki, even if this room is packed to the brim with other equally cute girls."
    else:
        s "My friends are in trouble and I must pretend to know things about plumbing."

    scene mollydrunk34
    with dissolve

    c "Well, I guess we’ll...see you in[school] tomorrow then?"
    mo "I ain’t comin’ to *hic*[school] tomorrow."
    mo "Or ever again! I quit! "
    s "I’ll see {i}all three{/i} of you tomorrow. Tell the others I said goodbye."
    f "I hope everything turns out okay. "
    f "We’ll take care of Molly, so don’t worry about that."
    s "I’m not worried at all. Thanks, girls."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I use my phone to ping the closest cab and patiently tap my foot as I wait for it to show up at the Amamiya estate."
    "Haruka and Maki were all over each other at the bar last night, so I’d be excited going over there even if it was just to watch."

    if bonus == True:
        "I just hope this doesn’t wind up being some cruel practical joke where I’m actually being summoned to fix pipes."

    "…"
    "Wait a minute."

    if bonus == True:
        "Am I really about to have a threesome with Maki when I just took her daughter’s virginity like an hour ago?"
        "I deserve some sort of award for this, I think."
    else:
        "Did I leave my wallet in the bathroom?"

    $ renpy.end_replay()
    $ halloween14 = True

    "………"
    "……"
    "…"

    if haruka_lust >= 10:
        jump harukalust10
...
```