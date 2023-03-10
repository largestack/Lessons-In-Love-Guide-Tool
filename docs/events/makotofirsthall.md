# Teacher's Pet (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Makoto: Completely Platonic](./makotodorm5.md)
* [Makoto: Bluejay](./makotodorm25.md)

## Event properties

* Id: makotofirsthall
* Group: Makoto
* Triggered by label: dormthursday
* Triggered by branch label: dormthursday
* Triggered by path: dormthursday->makotofirsthall

## Official wiki page

[Teacher's Pet](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotofirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label makotofirsthall:
    scene makhall1
    with dissolve

    s "Hey Makoto. What are you up to?"
    mak "Hey, Sensei...I was actually just about to go meet up with my mom for dinner, but..."
    mak "Now I'm curious as to what exactly you're doing here."
    mak "You do realize there doesn't have to be a rule specifically advising that males are not allowed in the girls' dorm to just...{i}know{/i} you shouldn't enter, correct?"
    s "And yet here I am."

    scene makhall2
    with dissolve

    mak "Though...it is rather strange that there {i}isn't{/i} a rule barring males from entry given that there are so many other strangely specific rules in the student handbook."
    s "Am I allowed to talk now or do you want to think about rules for a little while longer?"

    scene makhall3
    with dissolve

    mak "Apologies. Did you maybe...need something from me?"
    s "All I need from you is a good conversation, Makoto."
    mak "...I beg your pardon?"
    s "A conversation. It's the formal word for when two normal people talk to one another."
    mak "I'm so confused. Are you implying that you came all this way, breaking several unwritten rules in the process, to do something as simple as {i}talking?{/i}"
    s "There is no such thing as an unwritten rule. If it's not written down, it may as well not exist."
    mak "I have many issues with that statement, but for the sake of our {i}conversation{/i}, I will attempt to look past them."

    scene makhall4
    with dissolve

    mak "So, what would you like to talk about? I'm all ears for the next several minutes."
    s "Anything really. I kind of just wanted to hang out with you and kill some time before heading home."

    if day38 == False:
        scene makhall3
        with dissolve

        mak "Hang out? Like....me and you? Together?"
        mak "I had no idea that was something you were even interested in..."
        mak "Are you sure it's okay?"
        s "I can't see why it wouldn't be."
        mak "I am...sure you can, but..."

        scene makhall5
        with dissolve

        mak "I'd...love to regardless."
    else:
        scene makhall1
        with dissolve

        mak "Hang out? Like...right now?"
        s "Is that a problem? We've hung out before, haven't we?"

        scene makhall5
        with dissolve

        mak "Yes, it's just..."

    mak "I wish I knew you were planning on hanging out with me before I made plans with my mom."
    s "I can always come back some other time if you're busy. It's no big deal."

    scene makhall3
    with dissolve

    mak "Hmm...Well, I suppose it wouldn't hurt to spare a few minutes."
    s "Is your mom going to be okay with you being late?"
    mak "Honestly, I doubt she would have shown up on time anyway...so it's not really a big deal."

    scene makhall7
    with dissolve

    mak "And, in the event that she's actually on time for once, I can just tell her I was helping out the teacher."
    s "Great idea. Feel free to use me as an excuse whenever you want, Makoto."
    mak "To be perfectly honest, Sensei, I have been doing that all year. But I'm glad to know that my occasional tardiness is now teacher-approved."

    scene makhall1
    with dissolve

    mak "Oh, speaking of which...I don't think I've ever asked you why you decided to teach at a high school instead of a college or...night school or something."
    mak "Was there any reason behind that choice? How different is the salary of a high school teacher compared to that of a college professor?"
    mak "What sort of benefits are offered? And, in terms of job security-"
    s "Makoto, chill. That's way too many questions at once."

    scene makhall3
    with dissolve

    mak "Sorry...it's just-"
    mak "Well, you know how badly I want to be a teacher one day."

    "I guess I do now."

    mak "And I'm sure it might be premature to begin thinking about it now, but I've yet to decide on which level I want to teach at."
    mak "I think I'd be best off with college students, but...I also lack a formal college education right now, so I could be very, very wrong about that."
    s "Well, unfortunately, I don't think I'll be of much help to you right now."
    s "I have literally no idea how I wound up where I am and...honestly? I'm not sure if I ever will."

    scene makhall1
    with dissolve

    mak "What do you mean by that, exactly?"
    mak "Are you saying that...life is so unpredictable that even the most focused individuals can get hurled down an unexpected path entirely at random?"
    s "Sure, let's go with that."

    scene makhall8
    with dissolve

    mak "Hmm...I see."
    mak "I guess I never thought of it that way."
    mak "I suppose it would be best to just...not focus on that for now then."

    scene makhall9
    with dissolve

    mak "At the very least, it will give me a bit more time to focus on keeping a certain {i}someone{/i} in check."
    s "Good idea, Makoto. Miku needs all the help she can get."
    mak "..."
    mak "I..."
    mak "I was talking about you, Sensei..."

    scene black
    with dissolve2

    "Makoto and I talk for another few minutes before she decides it’s best to start heading over to wherever she's meeting her mom."
    "I think for a moment about what she would be like as a teacher, but ultimately get sucked into a fantasy I would prefer to not tell you about."
    "Either way, the night comes to an end. But not before the two of us manage to get a little bit closer..."

    $ renpy.end_replay()
    $ makotofirsthall = True
    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotohall:
    if chapthreeactive == True:
        scene makotosummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene makhall3
        with dissolve
    else:
        scene makotohallwinter
        with dissolve

    mak "Sensei! I’m glad you decided to drop by."
    mak "I actually have a few questions about what you think I could improve on as the class representative..."

    "Makoto and I talk about[school] for a few minutes before she has to leave for work."
    "It never ceases to amaze me how dedicated she is to improving herself even during her off-time."
    "If I was even half as productive as that, I’d probably be in an entirely different position right now."
    "It’s funny how {i}I’m{/i} the one being looked up to when she could probably teach this
    class even better than me."

    scene black
    with dissolve

    "The two of us talk for another few minutes before she decides it’s best to head out."
    "Being the gentleman I am, I walk her out of the dorm and make sure she’s in a nice
    area before the two of us separate."

    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanefirsthall:
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
            else:
                jump ayanehall
        "Talk to Makoto" if makotoblock == False:
            if makotofirsthall == False:
                jump makotofirsthall
...
```