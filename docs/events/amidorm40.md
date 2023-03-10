# Heaven for Human Blood (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 40

* Event [The Big Sleep](./amidate35.md) (Ami) is completed)

* amidorm40miss equal to False (unknown variable)

* Event [Stop Looking For Answers](./shrine35.md) (Maya) is completed)

* Day of week is not Monday



## Next events

None

## Event properties

* Id: amidorm40
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm
* Triggered by path: amidorm->amidorm40

## Official wiki page

[Heaven for Human Blood](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm40&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm40:
    play sound "knock.mp3"

    "I knock on Ami’s door."

    play sound "static.mp3"
    scene 2 with flash
    scene 3 with flash
    scene happyroom with flash
    stop sound
    play music "amiasleep.mp3"

    "{s}I knock on Ami’s door.{/s}"

    play sound "static.mp3"
    scene ayhh11 with flash
    scene dorm with flash
    stop sound
    stop music

    a "Coming!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Ami arrives at the large wooden rectangle currently preventing me from entering her room."
    "Most people would refer to this as a “door” but I personally think doors are useless when you could always tear through the wall and force your way into places."
    "Unless those walls are made of metal."
    "In those cases, rare as they may be, tearing through anything will not work."
    "You must find special tools and cut."
    "Or saw."
    "Thankfully, I don’t need to do anything like this tonight."

    scene amihumanblood1
    with dissolve
    play music "normalday.mp3"

    a "Hi!"
    s "Hey. Where are your pants?"
    a "Who cares?"
    s "Good point. "

    if bonus == True:
        s "I’m not interrupting any “alone time,” am I?"
        a "It wouldn’t make much of a difference if you were."
        a "It's not like you haven't already caught me in the act before, right?"
        s "True. But, to be fair, the door {i}was{/i} locked. So it's not like that one time really counts or anything."

        scene amihumanblood2
        with dissolve

        a "Of course! Masturbating behind a locked door is basically the same thing as never masturbating at all!"
        s "Uhh...sure. That makes sense."

    scene amihumanblood3
    with dissolve

    if bonus == True:
        a "Besides...and this isn't me saying that any of that kind of stuff was gonna happen tonight...but I’m glad you showed up because that means we get to talk instead!"
        s "I obviously can’t speak for you, but I personally gain a lot more pleasure from...well, {i}pleasure{/i} than casual conversation."
    else:
        a "Anyway, I’m glad you showed up because that means we get to talk!"
        s "That sounds delightful. A little friendly conversation never hurt anybody."

    scene amihumanblood1
    with dissolve

    a "Who says it has to be casual? Maybe I want to talk about {s}wires{/s} what you ate for lunch today or {s}where we go when we die{/s} what you ate for lunch today?"
    s "That’s a good idea. Let’s talk about what I ate for lunch today."

    scene amihumanblood4
    with fade

    "I decide to talk to Ami about what I ate for lunch today."
    "The conversation falls flat when I realize I can’t remember if I even ate anything at all."
    "And that would be no good. Ten out of ten doctors agree that if you don’t eat things, you will likely die."
    "I don’t want to die yet."
    "If I die, how will I get to eat lunch tomorrow?"

    a "So, Sensei...I’ve been doing some thinking, and I think it would be good if we got a new house together."
    s "Oh, sure. Let me just buy a new house in the spur of the moment because you’ve been doing some thinking."

    scene amihumanblood5
    with dissolve

    a "Yay!"
    s "Ami, we’re not buying a new house."

    scene amihumanblood6
    with hpunch

    a "AAAaaAAAHAhAHAHAHAAAA!@!!!!!!!!"

    "Ami throws a temper tantrum as if she were a little girl."

    if bonus == True:
        "The only thing is that I can’t personally confirm if it’s the same type of tantrum she’d throw when she was {i}really{/i} little because her parents didn’t die until she was seven."
    else:
        "Thankfully, she is a grown woman, so it does not last long."

    scene amihumanblood4
    with dissolve

    a "Aren’t you going to ask the reason I wanted to buy a new house, Sensei?"
    s "I wasn’t planning on it since it definitely isn’t going to happen, but sure."
    a "Because I love you!"
    s "That is not a suitable reason for a purchase that large."
    a "But if we get a bigger house, there will be a larger number of square feet in which we can get our love all over each other."

    if bonus == True:
        s "We haven’t even gotten our love all over our current house yet."
        a "Well then hurry up and pour it all over me, [amimaster]."
        a "Fill buckets and buckets with your love juice and dump it right onto my adorable little head."
        a "We can even leave the front door open so if somebody shows up, they can catch us in the act and then probably cry because everyone thinks they love you for some reason."
    else:
        s "Ewwwwww gross."
        a "I want a whole bucket of love. Please provide one for me."

    s "Wow. You’re even more possessive than normal today."

    scene amihumanblood7
    with dissolve

    a "Do you really not want a new house, though? Even though our current one is filled with sad memories?"
    s "There are good memories too. {s}I just can’t remember most of them yet.{/s}"
    a "I guess. But doesn’t it get annoying having people just show up all the time when we want to be alone together?"

    play sound "knock.mp3"

    m "Ami, can you let me in? I forgot my key..."

    if bonus == True:
        a "See what I’m talking about? We’ve barely even gotten each other’s clothes off and Maya is already trying to come between us."
    else:
        a "See what I’m talking about? We’ve barely even started doing our taxes and Maya is already trying to come between us."

    s "Maya? I didn’t hear Maya."

    play sound "knock.mp3"

    m "Are you asleep or something? What’s going on?"
    s "Oh. I heard her that time."

    scene amihumanblood8
    with dissolve

    if bonus == True:
        a "Hold on, Maya! I’ll be there in a second! Just have to put my underwear back on!"
    else:
        a "Hold on, Maya! I’ll be there in a second! I just have to finish eating this watermelon!"
        m "Gasp!"

    s "Why would you say that? Now I’m either going to have to deal with her calling me disgusting again or hide under the bed until she leaves."

    scene amihumanblood4
    with dissolve

    a "Well that’s no good. Sometimes, Maya doesn’t leave the room for days. You could very well starve to death, [amimaster]."

    if bonus == True:
        a "And if you starve to death, how am I going to ride you cowgirl style anymore?"
    else:
        a "And if you starve to death, who is going to eat the breakfast I make?"

    play sound "knock.mp3"

    m "Okay, seriously...open the door."
    a "Hold on one second, Sensei. I have to go do something really quick."
    s "了解です。"

    scene black
    with dissolve

    if bonus == True:
        "Ami gets off the bed and I stare at her butt for a few seconds before she makes it to the door."
        "It’s a good butt. The kind that you want to grab and squeeze and then have her jump because you’re actually in a train and she’s never seen you before."
        "Lol."
    else:
        "Ami gets off the bed and I take my phone out to see if anyone has bought some of the stuff I listed on ebay yet."
        "No luck =/"

    scene amihumanblood9
    with dissolve

    a "Who’s there?"
    m "Are you kidding? It’s me. Open the door."
    a "Name and age, please."
    m "Maya Makinami, age- Wait, why am I identifying myself for you? Just let me in. I live here."
    a "Sorry, Maya. But I’m a little busy right now."
    a "Sensei and I haven’t gotten to be alone together as much as I want lately, and you’re kind of getting in the way with all of your knocking."
    m "Sensei is in there?"
    s "Hey, Maya. What did you eat for lunch today?"
    a "Don’t ask her that, Sensei. She obviously just ate a WATERMELON."

    scene amihumanblood10
    with dissolve

    a "Hahahahahahahahahahah!"
    s "Hahahahahahahahahahah!"
    a "Hahahahahahahahahahah!"
    s "Hahahahahahahahahahah!"
    m "…"

    play sound "knock.mp3"
    scene amihumanblood11
    with hpunch

    m "Open the fucking door."
    a "Woah! No one’s ever going to marry you if you have that kind of attitude, Maya."
    m "Ami, I’m not kidding."
    m "I don’t know what’s going through your head right now but-"

    scene amihumanblood12
    with dissolve

    a "Sensei, Maya doesn’t want us to be alone together..."

    if bonus == True:
        a "She thinks we’re up to something weird even though we’re related."
        a "I just want to sit on your lap like I’m a little girl again and talk about lunch, but she’s being meeeeaaaaaan~~~~~"
        s "Maybe we should just let her-"
    else:
        a "She thinks we’re up to something weird when all I want to do is help you with your taxes."
        s "Maybe we should just let her-"

    scene amihumanblood13
    with dissolve

    a "No."
    a "I don’t want to let her in."
    a "This is our time together."

    scene amihumanblood9
    with dissolve

    a "Maya, here’s an idea! How about you come back in half an hour or so? There’s something I need to talk to Sensei about."
    m "Why? What do you need to talk to him about?"
    a "Why do you care? You hate Sensei."
    m "Right. He’s horrible. But what do you need to talk to him about?"
    a "{i}Why do you care?{/i}"
    m "Because if it’s something involving me, I-"
    a "Why would it be something involving you?"
    a "You’re not secretly hiding some sort of relationship with my [uncle] from me, are you?"
    m "No! I just-"
    m "Can you just please open the door?..."

    scene amihumanblood14
    with dissolve

    a "What do you think? Should we open it?"

    menu:
        "DON’T OPEN THE DOOR":
            s "Of course not. We’re not done talking yet."
        "THE DOOR DOES NOT NEED TO BE OPENED":
            s "We don’t have to open it. Not if you haven’t said everything you want to say yet."
        "ALL OF THE GOOD THINGS ARE HERE":
            s "All of the good things are already in here. Opening the door would just let the bad things in."
        "STAY IN THE ROOM ALONE":
            s "We should stay in here without Maya. I don’t feel like talking about the stars."
        "MAYA IS A FUCKING NERD":
            s "Maya’s a fucking nerd. She can wait in the hall."
        "STAY WITH YOUR NIECE" if bonus == True:
            s "I would rather be with my [niece] alone. She’s the only one who understands me."
        "STAY WITH YOUR ACCOUNTANT" if bonus == False:
            s "I would rather be with my [niece] alone. She’s the only one who understands me."

    scene amihumanblood9
    with dissolve

    a "Well, there you have it. Please come back later after Sensei and I are done loving each other."
    a "As [niece] and [uncle], of course. We’d neeeeeeeeeeeeeeever be anything more than that."
    s "I am a respectable man with morals and-"

    play sound "knock.mp3"
    with hpunch

    m "OPEN THE FUCKING DOOR!"

    scene black
    with dissolve

    "Ami and I slowly back away from the wooden rectangle and Maya, who doesn’t appear to know that you can just cut your way into rooms, ultimately retreats."

    if bonus == True:
        "Either that or she goes silent and slopes downward in the hall to [masturbate] to the thought of an [incest]uous [uncle]/[niece] pairing."

        if day < 5:
            "The only thing is that there are other girls in the hallway today and, if any of them saw her touching herself out there, they’d probably say something."
            "Unless it’s Rin. If it’s Rin, she’ll probably offer to finger Maya herself."
            "And then she’ll probably convince herself she’s fallen in love with her too."
            "They’d make a cute couple. "
        else:
            "Thankfully, there’s no one else in the hall right now (At least to my knowledge), so she’d be able to get away with it."
    else:
        "Either that or she GOES TO BUY A WATERMELON! LOL!!!!!"

    scene amihumanblood4
    with dissolve

    a "So, now that we’ve gotten rid of Maya, there are a few more things I’d like to talk about."
    a "Are you in the right mindset yet, [amimaster]? Or do you need a little more time to regain your footing?"
    s "Right mindset? What do you mean? "
    s "I just got here, didn’t I?"
    a "Right. You knocked on the door and immediately came to sit on my bed with me. "
    a "Nothing happened in between those two things. And everything is completely okay now."
    a "{i}You’re{/i} completely okay now. Ami’s got you."
    s "…"
    s "You’re being kind of weird."

    "Ami sits up on the bed, fixing her posture but spreading her legs apart more."
    "She smells faintly of shampoo so I imagine she just took a shower."
    "And, on another note, I feel strangely out of place right now."
    "Have you ever found yourself in a situation where you think you’re there, but you’re not {i}really{/i} there?"
    "Like you can comprehend the things hanging around you, but all of them are swaying so rapidly that you can’t find it in yourself to burn them into your mind."
    "To etch them into the gray walls of your cerebral cortex and really start to understand exactly {i}what{/i} is happening and not just “what’s happening.”"
    "This is one of those times. "
    "So, I slap myself in the face and put myself back into serious mode, because I’m pretty sure Ami wants to have an actual conversation about something more than just relocating right now."

    a "We’re both being kind of weird."
    a "We do that sometimes."
    a "But we’ve seen and felt horrible things together, so we share a bond that not many other people do."
    a "It’s a bond that makes it okay for the two of us to “black out” at times."
    a "I think that’s how we used to describe it in the past, isn’t it?"
    a "If you remember the past at all, that is."
    a "Your memory has never been that good, [amimaster]."
    s "To be completely honest, I can’t even tell if it’s been getting better or worse lately."
    s "It’s like every time I start to remember something, there’s a brief flash and TV static."

    play sound "static.mp3"
    scene neg1 with flash
    scene amihumanblood4 with flash
    stop sound

    s "Like that."
    a "That’s completely normal. And it’s okay for you to feel that way."

    if bonus == True:
        a "Because, even if you start doing weird stuff, it’s not like I’ll ever say no to anything. "
        a "You could honestly pin me down and ravage me in the middle of[school] one day and I’d lay there and take it like the good girl I am."
        s "I don’t think that’s a thing that will be happening any time soon."
        a "Of course it won’t be happening any time soon. Or probably ever."
        a "There are too many people who would be hurt by it."

    scene amihumanblood15
    with dissolve

    a "You know, one of the many many many many many many many reasons I love you is because, even though you pretend not to, you really {i}do{/i} care about everyone."
    a "You’ve always been that way. It’s the same reason you decided to take in an orphaned girl when she had nowhere else to go."
    a "Even when you were just as sad as her and had broken into a million pieces of your own."
    a "And so we did what we had to do and finished each other’s puzzles. "
    a "You were what I needed you to be, and I was what you needed me to be."
    a "Everything else was just static."

    scene amihumanblood16
    with dissolve

    a "But once that static got louder...that’s when things started getting weird."
    s "I’m guessing that’s when you started realizing you were in love with me?"
    a "That’s not what I’m talking about."
    a "I’m talking about when you started going back to normal. "
    a "When you stopped being so sad all the time and started putting things back together without my help."

    if bonus == True:
        a "It was nice seeing you learn to walk again, but I missed having to be the little girl who would hold you up with her big hugs and her infectious smile."
    else:
        a "It was nice seeing you learn to walk again, but I missed hiding cans of soup everywhere and asking you to find them."
        s "I knew I didn't just randomly acquire that hobby one day. I knew there had to be a reason."

    a "I don’t want to say you were drifting away because we were still really close-"
    a "But I could tell there was something else there. Something that was preventing us from being closer."
    a "You started coming home a little later some nights."
    a "And then even later than that some other nights."

    if bonus == True:
        a "And it didn’t really occur to me until a couple years ago, but that wasn’t {i}just{/i} because of tutoring, was it?"
    else:
        a "Is it because you were in a bowling league, Sensei? Because I told you to never join of those. They are scams."

    s "I...honestly have no idea."

    scene amihumanblood4
    with dissolve

    a "How come you never really tutored anyone at our house, Sensei?"
    s "I already told you. I have no idea."

    if bonus == True:
        s "But if I had to take a guess, it’s because it would have been weird to invite girls of that age over to a middle-aged guy’s house without parental supervision."
        s "I can’t imagine any of those parents would be thrilled about that either."
        a "Are you sure you weren’t just trying to keep your “work” life and your personal life separate?"
        s "Again, I don’t know."
        a "You don’t know?"
        s "No. And why are you asking about {i}this{/i} right now? "
        s "What does what I did for work back then have to do with us?"
        s "This is hardly normal [uncle]/[niece] bonding, Ami."
        a "I guess it is a little random to talk about it out of nowhere like this, but I’ve been thinking really hard about some stuff lately."
        a "I’m sure it’s not true, but I keep thinking that maybe something happened with you while I wasn’t around that hurt you really bad."
        a "Because, somewhere along the line, you gave up on tutoring. And I never really understood why."
        s "Probably because it didn’t pay well enough to support taking care of you."
    else:
        s "Maybe it was because I didn't figure out how to operate a phone until later?"

    a "Would the answer really be that simple? Or would it be something a little more complicated?"
    s "Complicated?"
    a "Like Noriko, maybe?"
    s "I mean. Noriko is definitely complicated, but I don’t think I’d ever quit tutoring because of her."
    a "Maybe Maya then?"
    s "Maya is also complicated, but I don’t think I’d quit over tutoring her-"

    stop music

    a "But you never tutored Maya."
    s "..."
    s "Wait, what?"

    play sound "static.mp3"
    scene amibreak3 with flash
    scene amihumanblood17 with flash
    stop sound

    a "You never tutored Maya, Sensei. "
    a "She wasn't one of your students."

    if bonus == True:
        a "You didn’t meet her until I started bringing her home in middle[school]."
        s "…"
        a "Unless you were hiding her from me, that is."
        a "But why would you be hiding another girl my age from me when I could have become friends with them?"
        a "You had no problems with Ayane when I started bringing her home."
        a "Have you actually known Maya this whole time? "
        a "Have you just been pretending not to know her?"
        a "And if so, why?"
        a "I don’t understand. "
        s "I-"
    else:
        s "Oh. Silly me. I must be misremembering."

    "Now that I think about it, every time I’ve tried talking to Ami about Maya’s past, she’s seemed almost completely oblivious."
    "Ayane, too. "
    "Neither of them knew anything about her family. Just where she came from and when she showed up."

    a "You two don’t like each other. That much is very clear to me."
    a "So why, if you have known each other for that long, are you pretending not to?"

    play sound "static.mp3"
    scene amibreak3 with flash
    scene amihumanblood17 with flash
    stop sound

    a "Do you think that maybe someone is just playing a trick on you, [amimaster]?"
    a "Do you think that someone could be taking advantage of your bad memory to make you think things are real that aren’t actually real?"
    a "Do you know what {i}is{/i} real, though?"

    play sound "static.mp3"
    scene amibreak3 with flash
    scene amihumanblood17 with flash
    stop sound

    a "The past you have with me."
    a "Not the past of girls that you’d see during designated hours five or six days a week."
    a "The past you have with the girl who would bleach the maggots out of your room for you or sponge bathe you when you couldn’t bring yourself to get out of bed."
    a "That past is real."
    s "…"
    a "…"
    s "…"
    a "Tell me you see me."

    play sound "static.mp3"
    scene amibreak3 with flash
    scene amihumanblood17 with flash
    stop sound

    a "Tell me you see me, not the fake memories of someone else who thinks they love you."
    a "When you love someone, you don’t have to hide it."
    a "So either everything is fake...or you’ve been hiding something very bad from me for a very long time..."
    s "…"

    scene amihumanblood4
    play music "wewereangels.mp3"

    a "Or you’re just misremembering and talked about tutoring Maya on accident!"
    a "In fact, since your memory is so bad, I’m sure that’s exactly what happened."
    a "So I won’t annoy you about it any more. "
    a "At least not until something else slips out that makes me think, “Hmm...is my [uncle] less amazing than I thought he was?”"
    a "Because right now, I still think you’re the most amazing, most handsome person in the entire world."

    if bonus == True:
        a "With the biggest penis of all time."
        a "And I want to have cute [incest] babies with you and watch them live long, happy, healthy lives."
    else:
        s "Awwwwww. Someone is getting a raise soon."

    play sound "dooropen.mp3"
    scene amihumanblood8
    with dissolve

    a "Oh! Maya’s back!"

    scene amihumanblood18
    with fade

    a "Oh. And {i}you’re{/i} here, too."
    mak "Would you mind explaining why I had to use {i}my{/i} key to unlock your door when you’re clearly capable of opening it on your own?"
    mak "It’s fine to have fights with your roommates, but dragging me into them is just a waste of my time."
    m "What happened in here?"
    s "…"
    s "I’m not sure."

    scene amihumanblood19
    with dissolve

    if bonus == True:
        mak "Well, whatever it was, please keep a tighter leash on your [niece]."
        a "I would love that."
        mak "{i}Please.{/i}"
    else:
        mak "I smell soup. Has someone been hiding soup in here?"

    m "Ami..."
    a "Yes, Maya?"
    m "I already told you there’s nothing going on. You didn’t need to go this far to prove-"
    a "Hm? Sensei and I just talked about lunch and stuff. "
    a "I have no idea what you’re talking about."
    m "…"
    a "…"

    scene amihumanblood20
    with dissolve

    mak "I think it’s probably best if we leave the two of them to resolve this on their own."
    mak "You’re clearly involved in this somehow and-"
    a "Sensei isn’t involved at all. He was just spending time with his favorite girl in the world. "
    s "Makoto’s right, though. I definitely think I should start heading home for the night."
    a "I’m sad, but I understand. "
    a "I’ll see you in the morning, though. I bought chocolate chips for pancakes, too, so expect a really big breakfast!"
    s "That..."
    s "That sounds great..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"
    stop music fadeout 7.0

    "…"
    "What exactly happened tonight?"

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidorm40 = True

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

                    ###############################################
                    ######## SECRETSECRETSECRETSECRETSECRET########
                    ###############################################

label roomwithclocks:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
            if ami_love >= 15 and amidorm10 == True and mayadorm5 == True and amidorm15 == False:
                jump amidorm15
            if ami_love >= 20 and day != 1 and day != 5 and amisroom20 == True and amidorm20 == False:
                jump amidorm20
            if ami_love >= 25 and amidorm20 == True and day != 5 and amidorm25 == False:
                jump amidorm25
            if ami_love >= 40 and amidate35 == True and amidorm40miss == False and shrine35 == True and day != 1 and amidorm40 == False:
                jump amidorm40
...
```