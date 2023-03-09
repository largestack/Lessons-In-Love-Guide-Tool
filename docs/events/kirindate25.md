# All That is Contaminated
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindate25&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 25

✅Event "[Kirin: Terms & Conditions](./kirindorm20.md)" is completed (event=kirindorm20)

✅Event "[Kirin: Full Blossom](./kirinlust5.md)" is completed (event=kirinlust5)

✅kirinnumber equal to True (unknown variable)



## Next events
* [Main: Good Morning](./secondbeach1.md)

## Event properties
* ID: kirindate25
* Group: Kirin
* Triggered by label: callkirinnight
* Triggered by branch label: callnight

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirindate25:
    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I tap on Kirin’s name in my phone and wait for her to answer."
    "It’s already dark out, but not dark enough that she’d be able to shrug off an invitation on account of it."
    "Not like she would anyway, though."
    "Kirin thrives in the dark."
    "But that’s probably only because she’s so weak in the light."
    "And most other places, if you want my honest opinion."

    if bonus == True:
        "As much as I appreciate the constant battering of sexual innuendos and near-pleas for me to take her away to somewhere else [[with my penis], it doesn’t exactly scream “strength.”"
    else:
        "As much as I appreciate the constant near-pleas for me to take her away to somewhere else, it doesn’t exactly scream “strength.”"

    "It screams, though."
    "But the noises are unintelligible and pained like a dying animal."
    "Probably a bird."

    play sound "phonebeep.wav"
    play music "thesleepingcity.mp3"

    ki "Hey. What’s up?"
    s "Not much. Just walking around. "
    s "Are you free?"
    ki "Are you looking to come over? Or are you looking to meet up somewhere?"

    if bonus == True:
        s "We don’t seem to have very good luck in your dorm, so we should probably just meet."
        ki "Are you grading luck entirely on our chances of fucking each other?"
        s "Is there any other way to grade luck?"
        ki "There is not."
    else:
        s "I don't know. Making decisions is hard. You choose."

    ki "Uhh..."
    ki "Hold on a sec."

    "Kirin puts the phone down and a few moments of silence pass by."

    if bonus == True:
        "I’m not sure what she’s doing right now, but I imagine it involves a lot of thinking."
        "Thinking about if tonight is actually the night...or if we’re just destined to “almost” have sex another hundred times or so before actually committing."
        "Fate can be cruel like that."

    ki "Okay. Yeah."
    ki "I’m gonna send you an address. Is it okay if we meet there?"
    s "What sort of address?"
    ki "What, do you need to know if you should bring your bowling shoes or something? Why does it matter?"
    s "Wait, do I actually need to bring bowling shoes?"
    ki "I’ll see you in an hour."
    ki "Bye."

    play sound "phonebeep.wav"

    "Kirin hangs up and immediately texts me an address quite far from where I am now."
    "It’s somewhere between the urban district and the old district and I’m a little curious about why we’d have to go all the way there to meet up."
    "But it is what it is, I guess."
    "It’s not like I had anything else to do tonight anyway..."

    scene black
    with dissolve

    "{i}One hour later...{/i}"
    "………"
    "……"
    "…"

    scene becomingapuzzlepiece1
    with dissolve2

    "I find Kirin leaned up against an unfamiliar building in an unfamiliar part of town, and I realize that it’s the most familiar place I could possibly find her."

    if bonus == True:
        jump kirindate25x
    else:
        s "So we {i}are{/i} bowling after all."
        ki "Yes."

        scene black
        with dissolve2

        "Kirin and I go bowling."
        "I am much better than her and she hates the experience."

        $ renpy.end_replay()
        $ kirin_love += 5
        $ kirindate25 = True
        stop music fadeout 10.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label kirinspecial25:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
label callkirinnight:
    if kirindate1 == False:
        play sound "phonebeep.wav"

        "I tap on Kirin's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        ki "Hihi~ How can I help you, Sensei?"
        s "Hey, Kirin. I was wondering if you'd want to meet up tonight?"
        ki "Tonight? You should have told me sooner. I already made plans with some friends."
        s "Damn. And you can't get out of them?"
        ki "Sensei, are you really asking me to bail on everyone {i}just{/i} so I can hang out with you?"
        s "Yes. Yes, I am."
        ki "Hmm...Well, I {i}do{/i} like you...But I don't know if I like you {i}that{/i} much."
        ki "How about you just call me a little earlier next time and I'll drop everything so we can hang? Cool?"
        s "Yeah, that's fine. Have fun with your friends tonight."
        ki "I will certainly try~"

        play sound "phonebeep.wav"

        "Looks like Kirin is busy tonight. I guess I'll have to call someone else."
        jump callnight
    if kirin_love >= 5 and kirindate1 == True and beachvacation16 == True and kirindate5 == False:
        jump kirindate5
    if kirin_love >= 25 and kirindorm20 == True and kirinlust5 == True and kirindate25 == False:
        jump kirindate25
...
```