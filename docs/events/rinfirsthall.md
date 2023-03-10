# Locked Out (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: rinfirsthall
* Group: Rin
* Triggered by label: dormwednesday
* Triggered by branch label: dormwednesday
* Triggered by path: dormwednesday->rinfirsthall

## Official wiki page

[Locked Out](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rinfirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rinfirsthall:
    scene rinhall1
    with dissolve

    s "Hey, Rin. What’s up?"
    r "…"
    s "{i}Ahem.{/i}"
    s "Hey, Rin. What's up?"
    r "…"
    s "…"
    s "Wow, look at all of this free hair dye and assorted skull accessories."

    scene rinhall2
    with dissolve

    r "Huh? What? Hair dye? Where?"
    s "I'm sorry to disappoint you but there's no free stuff. I just didn't know what else to say to get your attention."

    scene rinhall3
    with dissolve

    r "Oh! Yeah...sorry about that. I didn’t realize you were there and must've...zoned out or something."
    s "It’s fine, don't worry about it. What were you looking at, though?"

    scene rinhall4
    with dissolve

    r "Hm? What do you mean?"
    s "You just seemed pretty focused on something while you were ignoring my existence."

    scene rinhall5
    with dissolve

    r "Me? Nooo...That doesn't sound like me at all."
    r "I was probably just...thinking about how...awesome it is that my teacher is always keeping such a close eye on me!"

    scene rinhall6
    with dissolve

    r "You must really care about my future, huh?"
    s "I don't...{i}not{/i} care about your future?"
    r "Cool! But now that we're done talking about me, what are you doing over here?"
    r "Apart from closely monitoring my well being, I mean."
    s "Just trying to kill some time. Figured I’d drop by, say hello, and snap you out of whatever sort of trance you were caught in."

    scene rinhall7
    with dissolve

    r "Well...hello, then!"
    r "I’d offer to let you in so we can chill in my room, but I’m kinda locked out right now so I guess we're both SOL."
    s "You locked yourself out of your own room? How did you manage to pull that off?"

    scene rinhall6
    with dissolve

    r "To be fair, my problem could easily be solved by just going back to school, but...I think I'm having more fun just hanging out in the hallway."
    s "Yeah, you seemed to be having a real blast before I showed up."
    r "Maybe staring off into space is one of my hobbies? You don't see me belittling you for spending your free time sneaking into girls' dorms."
    s "I'll have you know that security is essentially non-existent here and that I was able to get inside with virtually no sneaking whatsoever."
    r "Well, I sure hope security for the shower room is a little bit tighter!"
    s "If you really need your keys, I can walk with you back to school. It's not like I have anything else going on right now."

    scene rinhall8
    with dissolve

    r "Nah, it's fine. The gates are probably locked by now anyway and I don't wanna have to make you hop them with me."
    r "Unless you've got a key, of course. But you don't really look like the type of guy the school would trust a key with."
    s "I feel like I'm supposed to be offended by this but, to be honest, I don't really feel anything."

    scene rinhall8r
    with dissolve

    r "Mood."
    r "Thanks for offering, though, Sensei."
    r "If Futaba wasn't already on her way back, I'd probably take you up on your offer. Quickest way to solve this remains to be just...sitting around and waiting."

    scene rinhall7
    with dissolve

    r "Just wish there was a little more to actually {i}do{/i} in the hallway, though. Options are {i}pretty{/i} limited here, as I'm sure you've noticed."
    s "You could always talk to Chika. She’s standing right there."

    scene rinhall9
    with dissolve

    r "Ooooooh...woooooow! It appears she is!"
    r "And to think that I am just noticing that for the first time right now..."
    s "…"
    r "…"
    s "You're acting weird."

    scene rinhall10
    with dissolve

    r "No! {i}You're{/i} acting weird! I'm acting like a completely normal teenage girl who just happens to enjoy yelling during her free time!"
    s "Do you...want {i}me{/i} to invite Chika to join us?"

    scene rinhall2
    with dissolve

    r "What? No. Chika's always just..."

    scene rinhall10r
    with dissolve

    r "Chika's always just on her phone and stuff..."
    r "We'd probably be better off if we just, like...left her alone or-"

    play sound "texttone.wav"
    scene rinhall10r2
    with dissolve

    r "Ah- I think that's Futaba."
    s "Almost back with your key to salvation?"
    r "No, just the key to our room."
    r "Either that or she's about to be eaten by wolves and is simply saying goodbye and thanks for everything."
    s "For everyone's sake, I'm going to hope it's the former."

    scene rinhall3
    with dissolve

    r "Same. You should probably head out now, though. I don't want Futaba getting jealous thinking that I'm out here trying to cozy up to you when {i}you're{/i} the one stalking {i}me.{/i}"
    s "I can assure you that I am very much not stalking you, nor do I ever intend to."

    scene rinhall2
    with dissolve

    r "Not even a little? That's actually kind of offensive."
    r "I am hurt and appalled and think you should at least {i}think{/i} about stalking me occasionally."
    s "I will...add it to my list of things to do. Later, Rin."

    scene rinhall6
    with dissolve

    r "Later, Sensei."
    r "Bring popcorn next time, okay?"

    scene black
    with dissolve2

    "I exit the dorm and make my way back into the street without any interest in ever purchasing Rin popcorn."
    "What I {i}do{/i} have an interest in, though...is why she got so weird as soon as I mentioned Chika."
    "Granted, she was already weird before that, but..."
    "I can't help but feel like there might be a little more to her lurking somewhere beneath the surface."

    $ renpy.end_replay()
    $ rinfirsthall = True
    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rinhall:
    if chapthreeactive == True:
        scene rinsummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene rinhall7
        with dissolve
    else:
        scene rinhallwinter
        with dissolve

    r "Oh, hey Sensei! Want to hang out for a little while?"

    "I sit down next to Rin and we spend the next hour or so talking about nothing."

    if bonus == True:
        "It’s a little odd how she consistently treats me more like someone her age than a full-grown adult."
        "But it’s nice. It feels different hanging out with her compared to the other girls."
        "Then again, that's probably just due to the fact that she's entirely unlike virtually all of them."
        "Not in bad way, though. Just...in a {i}Rin{/i} way."

    scene black
    with dissolve

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikafirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormwednesday:
    if chapthreeactive == True:
        scene summerdorm1wed
        with dissolve
    elif rinsad == True and chapthreeactive == False:
        scene wedwinterringone
        with dissolve
    elif cafe15 == True and rindorm20 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif beachvacation16 == True and rindorm35 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene wedwinter
        with dissolve
    else:
        scene dorm_wednesday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "This might be a good time to hang out with one of the girls."

    if cafe15 == True and rindorm20 == False or rinsad == True:
        "It looks like Chika isn't doing anything."
        "I can probably spend time with her if I want to."
        "What should I do?"
        jump wednesdaymenu
    if beachvacation16 == True and rindorm35 == False or rinsad == True:
        "It looks like Chika isn't doing anything."
        "I can probably spend time with her if I want to."
        "What should I do?"
        jump wednesdaymenu
    else:
        "It looks like Chika and Rin aren’t doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
        jump wednesdaymenu

    menu wednesdaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Chika":
            if chikafirsthall == False:
                jump chikafirsthall
            else:
                jump chikahall
        "Talk to Rin":
            if cafe15 == True and rindorm20 == False or rinsad == True:
                "Rin isn't around today for some reason..."
                "I'll just knock on someone's door instead."
                jump doorknock
            elif beachvacation16 == True and rindorm35 == False or rinsad == True:
                "Rin isn't around today for some reason..."
                "I'll just knock on someone's door instead."
                jump doorknock
            if rinfirsthall == False:
                jump rinfirsthall
...
```