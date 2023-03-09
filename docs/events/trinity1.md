# Trinity Pt. I: Stations of the Cross
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=trinity1&go=Go)



## Event preconditions
❌trinity equal to True (unknown variable)



## Next events
None

## Event properties
* ID: trinity1
* Group: Happy scenes
* Triggered by label: doorknock
* Triggered by branch label: doorknock

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label trinity1:
    stop music

    "I don’t want to go home."
    "Let me see what my [niece] is doing instead."

    play sound "knock.mp3"
    "…"
    play sound "knock.mp3"
    "…"
    play sound "knock.mp3"
    "…"
    play sound "static.mp3"
    scene callous1
    with flash
    stop sound
    play music "sweetervermouth.mp3"

    s "AMI! COME OUT OF YOUR ROOM!"
    a "Huh?..."
    a "Umm, one second! "
    a "I’m just getting changed!"

    if bonus == True:
        "Ami takes her clothes off behind the door, tracing her fingers lightly along her developing chest and wondering if I am going to touch her tonight."
        "These thoughts have been brought to you in part by Sensei™, your friendly neighborhood teacher and Ami’s [uncle]."
    else:
        s "Make sure you wear something purple. It will protect you."

    play sound "static.mp3"
    scene callous2
    with flash
    stop sound

    a "Help me."
    s "You look pretty today."
    a "I love you so much."

    if bonus == True:
        play sound "static.mp3"
        scene callous3
        with flash
        stop sound

        "Ami begins to contort her body into interesting and endearing shapes and sizes."
        "I choose my favorite one (It’s the one you’re looking at now) and my affection with her increases by 5 because I saw her naked again."

        play sound "static.mp3"
        scene callous4
        with flash
        stop sound

        "A familiar girl shows up shortly after and begins to trail her long, slender finger along my [niece]'s belly toward her pubic area."
        "I attempt to switch places with her through the means of telekinesis, but it does not work as that is not an ability I possess. "
    else:
        play sound "static.mp3"
        scene ayhh5
        with flash
        stop sound

        "Ami begins to contort her body into interesting and endearing shapes and sizes."
        "I choose my favorite one (It’s the one you’re looking at now) and my affection with her increases by 5 because I got to sneak in a quick hug during her transformation."

        play sound "static.mp3"
        scene colorbars
        with flash
        stop sound

        "A familiar girl shows up shortly after and begins to filter Ami's body into a vat of acid that melts her down into a series of interesting colors."
        "But then the colors fade and we get to have a normal conversation."

    play sound "static.mp3"
    scene callous5
    with flash
    stop sound

    m "Hello there!"
    a "Yes! Hello!"
    m "Welcome to the happiest day of your life!"
    a "Happy, indeed! Praise be!"
    m "Praise be!"
    s "Hey. What are you two up to tonight?"
    m "Tonight, we’re taking you on a tour!"
    s "A tour? But I’ve already familiarized myself with the local customs and locales of Kumon-mi."
    s "What else could there possibly be to learnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn?"

    play sound "static.mp3"
    scene callous6
    with flash
    stop sound

    m "Ah! A wonderful question!"
    a "Wonderful, indeed!"
    a "Tell him where we’re going, Maya!"
    m "We’re going..."
    m "ON A LUXURIOUS JAMAICAN CRUISE!"
    m "Feast your eyes on the wonderful sights of places like Discovery Bay, Fort Charles, and Noel Coward’s Firefly House!"
    a "No, no! It’s best to tell him the truth!"
    a "We’re not going to Jamaica until the SECOND beach update, silly!"

    scene callous7

    m "Oh right?! How could I forget something like that?"
    m "HAHAHAHAHAHAHAHAHAHAH!!!!"

    scene callous8

    a "HAHAHAHAHAHAHAHAHAHAH!!!!"
    m "{s}sssssssssssssssssssssssssssssssssssssssssssssssssss{/s}"
    a "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    "Ami and Maya cry out."
    "The walls begin to shake."
    "I begin to cry."

    scene callous5

    a "Oh gee. Would you look at that?"
    a "It appears my [uncle] has gotten rather {i}excited{/i} following our introduction."
    m "It appears he has!"

    if bonus == True:
        m "Why don’t you suck his cock then, you fucking whore?"
        a "HAHAHAHAHAH! We don’t have time for that!"
        a "Besides, the other girls would see us!"
        s "But there are no other girls around. It should be fine if you do it quickly."
    else:
        s "I am a good boy. The only thing I am excited for is walking elderly women across the street."

    play sound "static.mp3"
    scene callous2
    with flash
    stop sound
    stop music

    a "They’re all around us."

    play sound "static.mp3"
    scene callous9
    with flash
    stop sound

    "The room fills up with wonderful things."
    "Some of them look at me, some of them don’t."
    "Such is the way of life."

    s "And such is the petri dish."

    "I begin to say things I don’t understand. "
    "My tongue stings when I speak them."
    "It’s almost like spitting acid."
    "I hope I don’t get any on my [niece] and burn her skin off."

    play sound "static.mp3"
    scene callous10
    with flash
    stop sound
    play music "contemplation.mp3"

    a "Do you love me, Sensei?"
    a "Tell me the truth."

    if amifingered == True:
        s "Of course I love you..."

    else:
        a "I’ve done everything I can to make you recognize me, and yet you still only see me as a [niece]."

        if bonus == True:
            a "What else do I need to do to get you to touch me?"
            a "I don’t care that we’re related. I want to be with you forever."
        else:
            a "Why don't you hug me the same way you hug the other girls?"

        a "You’re my entire world. "
        a "So why?..."
        a "Why are you so insistent on breaking me?..."

    "Ami tries to reach out and touch me, but she’s unable to move her arms."
    "I know that feeling all too well."
    "There have been plenty of times where I’ve felt suffocated by the world around me."
    "Sometimes, it even seems like I’m strapped to a chair."
    "I hope that’s not something she ever has the displeasure of feeling in her life."

    play sound "static.mp3"
    scene callous11
    with flash
    stop sound

    a "How much can you see in the dark, Sensei?"
    a "Because...me?"
    a "I have nightvision. "
    a "I can see everything."
    a "I can see the way you {i}feel{/i} about everything."
    a "About everyone."
    a "And, honestly-"
    a "It’s really scary."

    scene callous12
    with dissolve

    a "Sometimes, I like to close my eyes and pretend that we’re actually husband and wife."

    if bonus == True:
        a "I’ll go into your room and kiss you before you wake up."
        a "Sometimes, I’ll even rub your penis to try and get you hard so that you’ll come into my room and ask for help when you wake up."
    else:
        a "I’ll go into your room and hug you before you wake up."
        a "Sometimes, I’ll even put a pickle in your mouth and run around in circles singing songs about the old days."

    scene callous13
    with dissolve

    a "I’d do anything for you. "
    a "I’d even rewrite the world."
    a "But, sadly...that’s not something I have the power to do."

    scene callous14
    with dissolve

    a "That’s something only God can do."
    a "And since you don’t believe in God, it looks like I can never get the world I truly want, doesn’t it?"
    s "And what kind of world is that, Ami?"
    a "A world..."
    a "Where..."

    play sound "static.mp3"
    scene callous15
    with flash
    stop sound

    a "Where things like {i}this{/i} don’t happen."
    a "With so many wonderful things cuddled up beside you."
    a "Is it too much to ask to be included among them?"

    if amifingered == True:
        "I look up to tell Ami that she is included among them, but she’s already gone."

    else:
        "I want to tell Ami that I do care about her...just in a different way."
        "But when I look up, I find that she’s dissolved into a puddle of...something."
        "Her body drips down onto me, soaking my jacket and causing a mild burning sensation as it finds its way through the fabric."

    "Meanwhile, everyone else I know stares at me."
    "Well, almost everyone. "
    "I notice a few faces among them missing."

    play sound "static.mp3"
    scene callous16
    with flash
    stop sound

    m "…"
    s "…"

    "A new girl stands before me."
    "Her name is Maya."
    "I know her."
    "She is my [niece]’s best friend."

    m "What are you doing here this late?..."
    m "It’s nearly 3 AM."
    s "Wait...is it?"
    s "I feel like it was barely dark just a few minutes ago."
    m "No...It’s been dark for hours. "
    s "Well then why are you still awake?"

    scene callous17
    with dissolve

    m "I felt the urge to go for a walk all of a sudden."
    m "I've never been good at sleeping."
    s "A walk at 3 AM? Are you insane?"

    scene callous18
    with dissolve

    m "You’re the one just creepily standing around in a girls’ dormitory in the middle of the night."
    m "Please don’t accuse {i}me{/i} of being the insane one."
    s "Can you at least tell me where you’re going so if you’re murdered, I can give the police some info?"

    scene callous17

    m "You should probably just come with me, to be honest."
    m "As much as I hate inviting you places, where I'm going is on the way to your house and it would probably be best if you didn’t spend the rest of the night just standing here."
    m "You’re lucky it was me who found you and not anyone else."

    scene black
    with dissolve2

    m "Come."
    m "It’s not far from here."

    "Maya grabs my wrist and forces me to follow her."
    "She lets go shortly after. I’m pretty sure she just wanted to make sure my legs weren’t frozen in place or something along those lines."

    scene nightsky
    with dissolve

    "I forget where I am halfway through the trip."
    "I forget that I’m anywhere to begin with."
    "I just focus on the stars and let the sound of the footsteps of the girl in front of me guide the way."
    "………"
    "……"
    "…"

    m "Okay."
    m "This is as far as I come."

    scene callous19
    with dissolve2

    "We come to a stop in front of a tree positioned in the middle of three spotlights."
    "It’s not a particularly interesting tree or anything like that, so I’m a little confused as to why it’s been so carefully illuminated."

    s "What is this?"
    m "A tree, idiot."
    s "No, like...what {i}is{/i} this?"
    m "What do you mean?"
    s "I mean why would you decide to come here of all places in the middle of the night?"

    play sound "static.mp3"
    scene callous20
    with flash
    stop sound

    m "Why does anyone decide anything?"
    m "You know better than me that, sometimes, people decide to act out things without any logic or reason behind them."
    m "Is visiting a strange tree truly peculiar enough to warrant asking that question?"
    s "Kind of. I think."
    s "I don’t really know."
    s "You’re weird."

    scene callous21
    with dissolve

    m "There is no beauty without some strangeness in its proportion."
    s "Edgar Allan Poe."
    m "Correct."
    m "Some of the most beautiful things in life also happen to be the strangest."
    s "Is this you trying to get me to call you beautiful? Because I normally get in trouble for that."

    scene callous20
    with dissolve

    m "Absolutely not. Anything but that."

    scene black
    with dissolve2

    "Maya moves over toward a snow-white cat basking in what little warmth one of the spotlights has to offer."
    "It isn’t until just then that I realize it’s begun to snow."
    "When did it become this cold?"

    scene callous22
    with dissolve2

    m "You’re hungry, aren’t you?"
    m "I’m sorry, but I don’t have any food for you."
    m "The strange man over there may be willing to lend you money so you can go out and buy dinner, though."
    s "Hey...You do realize it’s snowing, don’t you?"
    m "Obviously. I’m not an idiot."
    s "You don’t think that’s strange?"
    m "Of course it’s strange. But so is the fact that there is a tree positioned between three spotlights next to an abandoned[school] building."
    s "Abandoned[school] building? Is that where we are right now?"
    m "That’s one thing you could call it."
    m "But it’s many other things as well."
    s "I’m not sure if I follow."
    m "Are you familiar with the stations of the cross?"
    s "Uhh, not really..."
    m "Well, the easiest way to summarize it would be that there are three gods, but also only one god."
    s "How is that easy? That doesn’t make any sense at all."
    m "Welcome to religion."
    m "The idea is that the cross is made up of three parts: The father, the son, and the holy spirit."
    m "But those three things are of one body and make up who the Christians call “God.”"
    m "So, when you pray, you’re praying to not only one but three Gods. But also one. It’s odd."
    s "Yeah, this is one of the many reasons I don’t get involved with religion."
    m "I can understand why. A person with your limited mental capacity wouldn’t be able to grasp such a confusing concept."
    s "You say that as if it’s something {i}you{/i} can actually grasp."
    m "You can not grasp what isn’t real."
    m "Three gods is far too many. "
    m "Two gods is also too many."
    m "And so is one."
    m "I wish they’d all just go away."

    "There’s a faint sadness in her voice that leaves with the wind as it sweeps through the courtyard."

    scene black
    with dissolve2

    "The snow-white cat darts away in fear as soon as the branches of the tree beside us start to rustle."
    "Maya does not frown or chase after it."
    "She simply stands up and walks over to me."
    "Then she closes her eyes."
    "And says this-"

    m "God is dead."
    m "So we’ll never have to worry about three all at once."
    m "But, if for some strange reason, one day we do-"
    m "I hope that you will choose the least callous of them."

    "………"
    "……"
    "…"

    stop music

    "//ERROR"
    "//GOD IS NOT DEAD"
    "//GOD IS ALIVE AND WELL"
    "//HE RISES"
    "//SLEEPS AMONG US"

    if bonus == True:
        "//RAPES THE ONES WE LOVE"
    else:
        "//CONSENSUALLY HUGS THE ONES WE LOVE"

    "//WE MUST WATCH AS OUR DREAMS ARE DESECRATED"
    "//PRAISE BE"

    $ renpy.end_replay()
    $ trinity2 = True
    $ trinity = False
    $ trinity1track = True
    $ god_love += 1

    "{i}Your affection with God has increased to [god_love]!{/i}"
    "{i}It will change nothing!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
jump doorknock
                            else:
                                r "Uhhhhh...Look down here?"
                                s "Huh? Oh, damn. My bad."
                                jump rinhall
                        else:
                            play sound "knock.mp3"

                            s "Hey Rin, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock


                    "Futaba (Current Affection - [futaba_love])":
                        if futaba_love >= 5 and day != 2:
                            jump futabadorm
                        if day == 2:
                            play sound "knock.mp3"
                            s "Hey Futaba, are you in there?"
                            f "Umm...Sensei?...I'm right next to you..."
                            s "Huh? Oh, right. Sorry."
                            jump futabahall
                        else:
                            play sound "knock.mp3"

                            s "Hey Futaba, are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock

                    "Go Back":
                        jump doorknock
        "Room 5 (Ami & Maya)":
            if roomwithclocks == True:
                jump roomwithclocks
            if ticktock == True:
                jump ticktock
            else:
                "Who do I want to talk to?"
                menu:
                    "Ami (Current Affection - [ami_love])":
                        if ami_love >= 5 and day != 5:
                            jump amidorm
                        if day == 5:
                            play sound "knock.mp3"

                            s "Hey, Ami. Are you in there?"
                            a "Huh? Sensei? I'm right over here."
                            a "Do you not recognize the back of your own [niece]'s head?..."
                            s "Woah. What are you doing there?"

                            jump amihall
                        else:
                            play sound "knock.mp3"

                            s "Hey, Ami. Are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock
                    "Maya (Current Affection - [maya_love])":
                        if maya_love >= 5 and day != 1:
                            jump mayadorm
                        if day == 1:
                            play sound "knock.mp3"

                            s "Hey, Maya. Are you in there?"
                            m "..."
                            s "..."
                            m "Is this really happening?"
                            s "Huh? Oh, hey. I didn't see you there."
                            jump mayahall
                        else:
                            play sound "knock.mp3"

                            s "Hey, Maya. Are you in there?"
                            "..."
                            "There's no answer."
                            jump doorknock

                    "Go Back":
                        jump doorknock
        "Go Back":
            if day == 1:
                jump mondaymenu
            if day == 2:
                jump tuesdaymenu
            if day == 3:
                jump wednesdaymenu
            if day == 4:
                jump thursdaymenu
            if day == 5:
                jump fridaymenu
            else:
                jump weekendmenu
        "Go Home":
            if lettert == True:
                jump lettert
            if trinity == True:
                jump trinity1
...
```