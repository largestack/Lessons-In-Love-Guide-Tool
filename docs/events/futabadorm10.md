# Cutting Through Cocoons
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm10&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 10



## Next events
* [Futaba: Self-Insert](./library15.md)

## Event properties
* ID: futabadorm10
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm10:
    play sound "knock.mp3"

    "I knock on Futaba's door and wait for an answer."
    "Our last extended hang out session went pretty well apart from a poorly (Or expertly, based on who you ask) timed call from a certain niece of mine...so I'm sure this one will be just as good if not better."

    play sound "phonebeep.wav"

    "I turn my phone off just to be sure. Sorry, Ami."

    f "Umm...Sensei?"
    s "Hey. Good guess."
    f "Well...I already told you you're the only person who ever knocks..."
    s "Oh, sorry. I forgot about the {i}just come in{/i} rule."
    f "Uhh...wait a second, please! I...don't look...normal right now."
    s "..."
    s "Are you...secretly a werewolf or something?"
    f "Huh? No! Of course not. I just...ummm...hold on."

    "I hear some scuffling from behind the door as Futaba either attempts to reorganize things or make herself look like less of a werewolf."
    "I'll find out soon."

    f "Um...sorry...one more minute, please."
    s "Okay. But if I count to sixty and don't hear anything again, I'm opening the door."

    play sound "lock.mp3"

    f "No...you're not."

    "Damn it."

    "I spend the next minute or two standing beside the door, trying to look as normal as I possibly can while waiting for the person inside."
    "Needless to say, I do not look very normal."

    stop music fadeout 3.0

    "........."
    "......"
    "..."
    "Okay. What the hell is taking so long?"

    play sound "knock.mp3"

    s "Futaba, is everything okay in there? I'm starting to think the werewolf thing might actually be true."
    f "Ahh! I’m sorry, Sensei..."
    f "You can...come in now...but...again, I'm sorry..."

    "Sorry for what, exactly?"

    scene black
    with dissolve

    play sound "dooropen.mp3"

    "I open the door, unsure of what I'm going to see or why Futaba was so dead set on hiding it from me."

    scene futabadten1
    with dissolve2

    play music "love.mp3"

    "But all I see are two enormous breasts."

    f "Heeey..."
    f "Sorry you have to see me like this..."
    f "I was looking around for another pair of normal clothes, but everything is in the wash right now, so..."

    if bonus == True:
        "Why is she apologizing after blessing me with such a magnificent sight?"
        "It’s no secret that Futaba’s chest is the largest in the class, but like...come on."
        "This is just unfair."
        "How am I supposed to contain myself when she's over here basically spilling out of her pajamas?"

        s "You know there's no need to apologize for just being in your pajamas, right?"
        s "If anything, this shows that you’ve gotten comfortable around me."
    else:
        s "That is fine. My appearance here was unplanned and unannounced, so I will not belittle you for not being fully prepared and formally dressed."
        s "I will try to do better to make you more comfortable with my presence in the future."

    scene futabadten2
    with dissolve

    f "Of course I’m comfortable with you, Sensei...It’s just..."

    scene futabadten3
    with dissolve

    if bonus == True:
        f "You know...These pajamas are a little...{i}revealing...{/i}"
        f "So...I'm...sorry if I seem embarrassed or anything..."
        s "I mean, this is fifty times better than you seeing me in my pajamas. So I wouldn't worry too much about it."

        scene futabadten4
        with dissolve

        f "I doubt that. I really can't imagine what you wear to sleep being any worse than this."
        f "Unless it's...one of those really embarrassing one pieces, but...you don't really seem like the type to wear those."
        s "Oh, no. It's nothing like that."

        scene futabadten5
        with dissolve

        f "I figured. There's no way someone like you would-"
        s "I sleep naked."

        scene futabadten6
        with dissolve

        f "Ah."
        s "See what I mean?"
        s "Hearing that, don't you feel a little less self-conscious of how {i}revealing{/i} your pajamas are? Because, it probably goes without saying, but there's nothing quite as revealing as straight up nudity."

        scene futabadten7
        with dissolve

        f "No."
        f "No, I guess there's not."
        s "..."
        f "..."
        s "Futaba?"
        f "..."

        "Uh-oh. I think I might have broken her."

    "I take a step closer to Futaba and begin snapping my fingers in her face."

    if bonus == True:
        s "Hey, Futaba. Come back to life now. We don't have all night, you know."
        f "Naked..."
        f "Sensei...sleeps naked..."
        f "That's totally normal. That's a totally normal thing I know now."
        f "This is all completely normal. It's fine that he told me that. It's fine that-"
    else:
        f "...What are you doing?"
        s "Just showing you how quickly I can snap. Are you impressed?"

        "I snap really quickly. Futaba is impressed."

        f "Um..."

    "Sensing that the snapping isn’t having any effect, I poke one of her cheeks with my index finger and she is immediately shocked back to life."

    if bonus == True:
        scene futabadten8r
        with hpunch

        f "Ah! I’m so sorry. I must have zoned out for a second!"
        f "I think I may have...misheard you because it sounded to me like you said you sleep n-"
        f "N-"
        f "…"

        scene futabadten6
        with dissolve

        f "Ah."
        s "Futaba, come on."

        "I poke her cheek a second time."

    scene futabadten8r
    with hpunch

    if bonus == True:
        f "I’m so sorry! I have no idea what’s gotten into me!"
        s "I believe the scientific term for it would be {i}arousal.{/i}"
        jump futabapokex
    else:
        f "I am so confused! It feels like content is being removed in the strangest way possible right now!"
        s "I have no idea what you are talking about."

        scene black
        stop music

        f "Ahh! See?! The event is over already!"
        s "Yeah. There was a lot more inappropriate content in this one than I remember there being."
        s "This scene is probably getting nuked soon anyway, so it's not really a big deal."
        f "Oh...R-Right..."
        f "I...um...I guess...goodnight then?..."
        s "Yup! Night, Futaba."

        $ renpy.end_replay()
        $ futabadorm10 = True
        $ futaba_love += 1

        "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        if day >= 6:
            jump endofsat

label futabadorm15:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
...
```