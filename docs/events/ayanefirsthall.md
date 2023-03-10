# Spy on Me (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: ayanefirsthall
* Group: Ayane
* Triggered by label: dormthursday
* Triggered by branch label: dormthursday
* Triggered by path: dormthursday->ayanefirsthall

## Official wiki page

[Spy on Me](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanefirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanefirsthall:
    scene ayanehall1
    with fade

    ay "Oh? What's this?"
    s "Take a wild guess, Ayane."
    ay "Did you come all the way over here to propose to me in the middle of the hallway?"
    s "Yes. I was brainstorming the most romantic places to do it and I just kept landing on “dorm hallway.”"

    scene ayanehall2
    with dissolve

    ay "Wha...Sensei..."
    ay "Do you really mean that?..."
    s "No? Absolutely not. On what planet would that actually be true?"

    scene ayanehall3
    with dissolve

    ay "I was kind of hoping it would be Earth..."
    s "No, Ayane. But, while I'm not here to propose to you, I am here to hang out."
    s "So I suggest you stop pounding on your door for a second and, I don't know, pay more attention to me or something."

    scene ayanehall4
    with dissolve

    ay "Sensei, you know there's no one in the world I'd rather pay attention to than you. But I promised Sana I'd wake her up around this time and it's already like, ten minutes after the time she gave me."
    s "Why not just go inside? It's your room, isn't it?"
    ay "It is. But I think that in an effort to sleep longer, Sana's subconscious may have forced her out of bed to lock the deadbolt on the door and now I can't get in."
    ay "Which, of course, means that I must repeatedly knock until my mission is complete."

    scene ayanehall4r
    with dissolve

    mak "Ayane, you know I have a key that controls both locks on the door, right? I can let you in if-"
    ay "I'm sorry, Makoto. But this is something I must handle on my own."
    mak "Uh...I guess if that's what you think is best..."

    scene ayanehall1
    with dissolve

    ay "Oh! I know! After Sana wakes up, what if all three of us did something together?"
    s "Something like what, exactly? Because I was kind of hoping to be alone with you."

    scene ayanehall5
    with dissolve

    ay "Oh?"
    s "I mean, that's not how I meant it. But I enjoy that face, so you are free to interpret it that way and act in accordance to whatever you believe I want."
    ay "Oh, I know what you want."
    mak "I am still right here-"
    ay "Can it, Makoto. This is a moment between me, Sensei, and possibly Sana if we can get her to wake up."
    s "I'm sorry, what was that last part?"
    ay "It's her room as well, Sensei. We can try to ignore her if we want, but chances are she's going to notice once things really start to get going."
    s "Maybe I should be the one to knock instead? I'm stronger."

    scene ayanehall5r
    with dissolve

    if bonus == True:
        ay "Sensei! I was obviously kidding! Sana is a sweet, delicate flower and I could never let you defile her innocence like that!"
        s "I'm going to go talk to Makoto instead."
        mak "Oh, no. I've tried to interject twice now and it's exceedingly clear that I am not a welcome participant in this conversation."
        ay "You're not going anywhere, Sensei! Apologize for your lewd fantasies about my sleeping roommate!"
        s "I was literally just playing off of your suggestion. I am a human being and, when tempted with certain things, I am going to act in a human way."
    else:
        ay "Sensei! You're underestimating just how much Sana loves street corn!"

    scene ayanehall6
    with dissolve

    if bonus == True:
        ay "I know...I know..."
        ay "It only makes sense that you'd want {i}both{/i} of us at once since we are equally adorable and loving and kind and soft and-"
        s "The point, Ayane. Get to it."
        ay "Sorry. I think what I'm trying to say is that as much as I understand the...need for more than one partner, I was kind of hoping you'd think otherwise."
        ay "I know {i}I'd{/i} be happy with only you, but...you're a guy, so..."
        s "You know that not all guys are interested in just...racking up their body count, right? There are plenty of men who are happy with only having one partner."

        "I'm just not one of them."
        "It would sure make things a lot easier if I was, though."
    else:
        ay "I swear, sometimes it's like you don't even remember your place in this video game."
        s "Sorry, Ayane."

    scene ayanehall1
    with dissolve

    ay "Really? Then I can keep you all to myself and it will be completely justified?!"

    if bonus == True:
        s "I mean...I'd prefer if you didn't treat me like property {i}when we are literally just acquaintances.{/i}"

        "I look over at Makoto to-"

        mak "I already told you, I want no part of this. I'm not even listening anymore."

        "That's just what she wants me to think."
    else:
        s "Wait, what? Did I just miss a line of dialogue or something?"

    scene ayanehall4r
    with dissolve

    ay "Alas...reduced from future wife to mere acquaintance in one, brief conversation."
    s "Stop assigning yourself roles you never earned."

    scene ayanehall1
    with dissolve

    ay "Anyway, I’m glad you dropped by, Sensei. I just wish it was under more fun circumstances and that I could actually get inside of my room."

    if bonus == True:
        ay "But hey! Now you know where I sleep in case you ever want to come spy on me at night."
        ay "Remember, though. If you {i}do{/i} decide to do that, do it on a night Sana is working."
        ay "I don't even want to imagine the sort of panic attack she'd have if some mysterious man showed up in the middle of the night and started taking pictures of me."
        s "It would be more concerning if that was a situation she wasn't fazed by."
        ay "Well, it wouldn't be the first time something like that has happened."
        s "Wait, what?"
        ay "You don't know my life."
        s "{i}What?{/i}"

        scene ayanehall4r
        with dissolve

        ay "I guess we’ll just have to reschedule our “alone time” for another day, though."
        ay "I swear, at this rate, Sana won't be putting {i}any{/i} work into our science fair project and I'm going to have to win all on my own yet again."
        s "Science fair project?"

        scene ayanehall6r
        with dissolve

        ay "Mhm! For the science fair you were supposed to tell us about but then forgot to."
        mak "I took care of it for you, Sensei. You're welcome."
        s "I thought you weren't listening?"
        mak "I'm not."
        ay "The only issue is that what Sana and I are working on is top secret and the government could send assassins after us if they knew anything about it."
        s "Uhh..."
        s "I'm assuming that means you can't give me any details?"
    else:
        ay "I was kind of busy anyway."
        s "With the street corn?"
        ay "No. Something else."
        s "What?"

    scene ayanehall7
    with dissolve

    ay "All I can tell you is that it’s supposed to bring the dead back to life."
    s "..."
    ay "..."
    s "What?"

    scene ayanehall0
    with dissolve
    play sound "dooropen.mp3"

    "..."
    s "What?"

    scene black
    with dissolve

    "..."
    "{i}What?{/i}"

    stop music fadeout 3.0

    $ renpy.end_replay()
    $ ayanefirsthall = True
    $ ayane_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanehall:
    if chapthreeactive == True:
        scene ayanesummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene ayanehall1
        with dissolve
    else:
        scene ayanehallwinter
        with dissolve

    ay "Sensei! You missed me didn’t you? Tell me you missed me!"

    "Unfortunately, Sana is home right now so the two of us aren’t able to be alone together."
    "Instead, we talk for a bit about karate and how much Ayane hates her dad."
    "Apparently, he invented the unpoppable version of bubble wrap and it made her family rich."

    if bonus == True:
        "She promises to show me the mansion eventually, but I can’t imagine it would be easy to explain why she brought home someone twice her age, teacher or not."

    "Eventually, she heads back inside to hang out with Sana and I’m left on my own..."

    scene black
    with dissolve

    $ ayane_love += 1

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amifirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormthursday:
    if chapthreeactive == True and makotoblock == False:
        scene summerdorm1thurs
        with dissolve
    elif chapthreeactive == True and makotoblock == True:
        scene dormthursmakotogone
        with dissolve
    elif makotodorm25 == True and hoorayanotherreset == False and chapthreeactive == False:
        scene dorm_thursday2
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene thurswinter
        with dissolve
    else:
        scene dorm_thursday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "What should I do?"

    menu thursdaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Ayane":
            if ayanefirsthall == False:
                jump ayanefirsthall
...
```