# Sweet Tooth
Karin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate20&go=Go)



## Event preconditions
✅Karin love greater than or equal to 20

✅Event "[Main: Permission Slip](./day355.md)" is completed (event=day355)

✅Event "[Karin: The Adventures of Karli & Steve](./karinsoccer20.md)" is completed (event=karinsoccer20)

✅karinnumber equal to True (unknown variable)



## Next events
* [Main: Good Morning](./secondbeach1.md)

## Event properties
* ID: karindate20
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon

## Event code
File: \game\KarinEvents.rpy
Code:
```python
...
label karindate20:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer. "
    "Soccer practice has already ended for the day, so she’s likely either on her way home right now or..."
    "I don’t know. Doing something else?"
    "It’s not like I have a tracking device on her or anything."
    "Though, if I separated everyone I know into two categories of “Would let me install a tracking device inside of them” and “Wouldn’t do that...”"
    "I think Karin would probably be in the first group."

    play sound "phonebeep.wav"
    with hpunch
    play music "justbehappy.mp3"

    ka "AAAAAAAHHHHHH!!!!!"
    s "…"
    ka "…"
    ka "Hi."
    s "What the fuck was that?"
    ka "I’m sorry...I’m just really frustrated right now. "
    ka "I didn’t hurt your ear, did I?"
    s "Did you say something? I can’t really hear you over the constant ringing in my ears."
    ka "Ah! Sensei, no! I didn’t mean to!"
    ka "Do you need medical attention? Should I come meet you somewhere?"
    ka "Where are you? I’ll bring my first aid kit and-"
    s "Karin, chill. I’m fine."
    s "Just a little surprised to hear you of all people yelling."
    ka "I know, I know...It’s just my stupid little sister."
    ka "Just kidding. She’s not stupid. I love her."
    ka "But really. It’s Kirin. She’s been getting on my nerves a lot lately and I don’t even have anyone to talk about it with since all of my friends are {i}also{/i} her friends."
    s "All of them?"
    ka "Well...all of the ones I’d normally complain about stuff to."
    s "Well...I’m available if you want to vent to me."

    if karinlied == False:
        ka "…"
        s "…"
        s "Karin?"
        ka "And you’ll keep anything I say hidden from her even though...you two are..."
        s "Sure. Just because I was honest about my relationship with her to you doesn’t mean we can’t talk anymore."
        ka "...Yeah."
        ka "Yeah, okay. That’s...fine."

    else:
        ka "Do you..."
        ka "Do you really mean that?"
        ka "You’re okay with me taking up a bunch of your time just to complain about stupid stuff that you’re in no way involved with?"
        s "{i}As long as I can be with you.{/i}"
        ka "S-Stop saying that! "
        ka "You said that at the locker room too and it made my heart go all GAAAAAAAAAHHH."
        ka "AAAAAAAAHHH I JUST WANNA YELL!"
        s "..."
        ka "..."

    ka "There’s um..."
    ka "There’s a new diner by my house if you’d want to maybe meet there?"
    s "That works for me. Just send me the address and I’ll start heading over."
    ka "Okay! Cool!"
    ka "I’ll...do that right now then!"
    s "Sweet."
    ka "Yeah! Really sweet!"
    s "Yup."
    ka "So...sweet..."
    s "…"
    ka "…"
    ka "Anyway, bye!"

    play sound "phonebeep.wav"

    "Karin awkwardly hangs up the phone and sends me the address of the diner we’re meeting at a few seconds later..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene karinangrybreakfast1
    with dissolve

    ka "I’m sorry for ordering so many sweets. I always crave sugar when I get angry."
    s "That is possibly the cutest reaction to getting angry I have ever heard."
    ka "I’m so angry I’m not even going to react to you using the C word at me."
    s "Wow. It must be really bad then, huh?"

    play sound "thump.mp3"
    scene karinangrybreakfast2
    with hpunch

    ka "I’m always so nice to her and she treats me like I’m the worst thing in the world!"
    ka "Like, I get that you’re automatically supposed to be jealous of me since I’m the older sibling, but cut me some gosh darn slack already!"

    scene karinangrybreakfast3
    with dissolve

    ka "I’m sorry for my language, too. You shouldn’t have had to hear that."
    s "I’m really seeing a brand new side of you today."
    ka "I’m sorry...I made you walk all the way over here and I’m just...jumping straight into things before you’ve even gotten to eat."
    s "Oh, don’t worry about that. I’m not really hungry."

    scene karinangrybreakfast4
    with dissolve

    ka "What? No. Tell me that’s not true. Please be hungry."
    ka "I don’t want to have to eat all of this by myself. I’ll get diabetes."
    s "Well you should have thought of that before your anger-induced sweet tooth kicked in."

    scene karinangrybreakfast5
    with dissolve

    ka "Maybe if I just...don’t have another cheat day until next winter it will be okay?..."
    s "So, what’s going on?"
    s "There had to be something in particular for you to get like this, right?"
    ka "Yeah, but..."
    ka "I might come off as a little needy or...annoying once I start explaining things."
    ka "Are you okay with that?"
    s "I wouldn’t have come if I wasn’t."
    ka "Then..."

    scene karinangrybreakfast6
    with dissolve

    ka "You know how you’re going to the beach soon, right?"
    s "In the middle of winter. Yes."
    ka "And you remember how I came with you last time?"
    s "In the middle of summer. Yes."
    ka "Yeah. Exactly."

    "Oh. Okay. I guess there won’t be any bigger reaction to the weird blurs in time with Karin."
    "Either that or she’s just so infuriated that it went completely over her head."

    ka "So...I had a lot of fun last time."
    ka "Even if Kirin ignored me for most of the trip, I got to hang out with Miku and...almost only killed one person with a baseball bat."
    s "Maya hasn’t been walking the same ever since."

    play sound "thump.mp3"
    scene karinangrybreakfast7
    with hpunch

    ka "She hasn’t?!"
    s "Karin, it was a joke. And please stop hitting the table like that. You’re going to break something."

    scene karinangrybreakfast4
    with dissolve

    ka "I’m sorry..."
    ka "But...I was asking her about it this morning because I thought it would be fun to tag along with you guys again...even if I’m not in your class..."
    ka "And she just kept saying all of this stuff about staying out of her personal life and that I wasn’t welcome there."
    ka "But I {i}know{/i} that isn’t true because Miku and Ami both invited me already."
    s "Then what’s the issue? Just show Kirin that you’re your own person and that you can do whatever you want."
    ka "That’s what I want to do, but..."
    ka "I also know that things aren’t really that great between us and that doing something like that after she asked me not to could just...make everything worse."

    scene karinangrybreakfast5
    with dissolve

    ka "So here I sit...in a diner, surrounded by a spread of food that could very well end my athletic career, complaining about it to her teacher."
    s "Don’t worry. I’m already used to all types of girls complaining about all sorts of things to me."
    s "At least you’re not asking me to kill anyone in order to save the world."
    ka "Yeah...I guess things could be worse if-"

    scene karinangrybreakfast8
    with dissolve

    ka "Wait? Killing someone to save the world?"
    ka "Is this really the level of problems the other girls you know have? Because if that’s true, I’m going to feel very immature about whining over something so small."
    s "It’s a long story. But either way, you shouldn’t feel small no matter what."
    s "You said there was no one else for you to talk to about this- and I don’t really think I’ll be able to {i}help{/i} in any way other than just listening, but..."
    s "I think it’s healthy for you to get mad."
    s "Maybe not the whole...binge eating thing that's going on here, but the anger alone."

    scene karinangrybreakfast5
    with dissolve

    ka "Ugh...I really hate getting angry, though."
    ka "Even when I was a baby, any time my parents disciplined me, I never screamed or cried or anything like that."
    ka "I just sat in my crib and silently sobbed to myself while they watched Jeopardy."
    s "Huh. Maybe your living situation isn’t as normal as I thought it was after all."

    scene karinangrybreakfast9
    with dissolve

    ka "It’s plenty normal. Really."
    ka "I just get overwhelmed really easily and don’t want anyone getting hurt because of me."
    ka "And sometimes...it feels like Kirin is trying to hurt me on purpose."
    ka "Like, what would it matter if I {i}did{/i} come to the beach? Why would {i}that{/i} bother her when she knows full well she’s met a bunch of people through me?"
    ka "Does it not go both ways? Am I not allowed to have a life of my own but she is? How is that fair?"
    s "It’s not."

    play sound "thump.mp3"
    scene karinangrybreakfast7
    with hpunch

    ka "Right?!"
    s "Karin, please."
    ka "I’ll replace it if I really do break the table! I just need this right now, Sensei!"
    ka "I’m so fed up with doing everything to try and get Kirin to like me only to have her be all like...“Grrr! I’m Kirin!”"
    s "Wonderful impression. I think you’ve found your next career if all of this food really does end your life as an athlete."

    scene karinangrybreakfast10
    with hpunch

    ka "AAAAAAAAHHHHHHH!"

    "I turn my gaze to the side to see if anyone is looking over this way and...of course, literally everyone is."

    ka "I’M SORRY TO EVERYONE JUST TRYING TO ENJOY THEIR MEALS BUT I AM VERY MAD AND HAVE AN UNGRATEFUL LITTLE SISTER!"
    s "Karin, it doesn’t work that-"
    s "Wait, why did everyone go back to eating their food like none of this ever happened?"

    if karinlied == False:
        scene karinangrybreakfast11
        with dissolve

        ka "Sensei...you {i}must{/i} understand her a little better than me, don’t you?"
        ka "Since you two are...you know..."
        s "The only thing I understand about Kirin is that she’s self destructive in pretty much every way imaginable."

        if bonus == True:
            "I also understand that she thoroughly enjoys giving blowjobs, but that isn’t something I feel the need to disclose to Karin."

        ka "She’s not supposed to be like that, though."
        ka "She’s supposed to come to me if she feels like she’s in trouble...or when things become too much for her to bear."
        ka "That’s what sisters are for. But if she won’t even come to me, then-"
        s "There’s a flaw in what you just said, though, Karin."
        ka "A flaw?..."
        ka "What flaw?"
        s "There is no way that people are “supposed to be.”"
        s "Kirin’s her own person who’s going to do things her own way."
        s "And it sucks that she’s apparently against you being {i}your{/i} own person, but isn’t a nonsensical decision like that something we should expect from her by now?"
        s "Just...keep telling her she’s a good girl or something and I’m sure she’ll soften up in time."
        ka "…"
        s "…"

        scene karinangrybreakfast12
        with dissolve

        ka "Is that...what you did?..."
        ka "To...get her to like you, I mean..."
        s "Surprisingly, I didn’t have to do {i}anything{/i} to get her to like me."
        s "She just came to me one day and that was that."
        ka "I wish I was that lucky..."
        s "If you were born a male, you probably would have been."
        ka "That’s not lucky at all. I’d look at myself in the mirror and immediately faint."
        s "I don’t know if your fear would exist if you were-"
        s "You know what, that doesn’t matter."
        s "What does matter is that you don’t let yourself get bogged down by the actions of a girl that literally no one, not even Kirin herself, understands."
        ka "…"
        ka "Yeah..."

    else:
        scene karinangrybreakfast5
        with dissolve

        ka "I just..."
        ka "I just want to understand her."
        ka "She’s supposed to come to me if she feels like she’s in trouble...or when things become too much for her to bear."
        ka "But instead, she just...pushes all of that anger onto the people around her and-"

        play sound "thump.mp3"
        scene karinangrybreakfast13
        with hpunch

        ka "Ah! That’s what I’m doing now!"
        ka "I’m Kirin Kanda! There is no more Karin!"
        s "Please remain Karin. One Kirin is more than enough for the world."
        s "Besides, I don’t really count venting like this as “pushing your anger onto other people.”"
        s "The key difference between you and Kirin is that you don’t actively want to make other people feel bad."

        scene karinangrybreakfast6
        with dissolve

        ka "And you think that she does?..."
        s "At the very least, I think she wants {i}you{/i} to feel bad. And all the evidence I really need for that is the dent you’ve put into our table."

        scene karinangrybreakfast14
        with dissolve

        ka "Oh my God, did I actually-"
        s "It was just a guess. I don’t know if the table is actually dented or not."
        s "But what I’m trying to get at is that you can’t let yourself get bogged down by the actions of a girl that literally no one, not even Kirin herself, understands."
        ka "…"
        ka "Yeah..."

    play sound "thump.mp3"
    scene karinangrybreakfast15
    with hpunch

    ka "Yeah!"
    ka "I’m not going to let Kirin decide what I can and can’t do!"
    ka "I’m my own person!"
    ka "I’m gonna go to the beach with my friends!"
    s "I’m very proud of-"

    scene karinangrybreakfast16
    with hpunch
    play sound "cheer1.mp3"

    s "...you?"

    "The rest of the diner erupts into a fit of applause and people leave their seats to start clapping for Karin."
    "And, in other news, Kumon-mi keeps getting weirder and weirder."

    ka "Heheh~"
    ka "Thank you very much everyone, but please hold your applause."

    stop sound fadeout 7.0
    scene karinangrybreakfast17
    with dissolve

    ka "Sensei...I’m sure I don’t have to say this...but thank you for letting me complain to you today."
    ka "It...definitely {i}is{/i} good that I was able to get all of this off my chest. Even if I’m about to put another fifty pounds on after all of the sugar you are about to watch me consume."
    s "Hey, consume away. It wouldn’t be the first time I’ve looked on in curiosity as a girl consumes sugary food."
    ka "…"
    ka "What?"
    s "Long story."
    ka "…"
    ka "What?"
    s "Anyway, how are you going to come to the beach if it’s not with Kirin?"

    scene karinangrybreakfast18
    with dissolve

    ka "Hmm...that’s a good question..."
    ka "I think Miku and Makoto were heading there with Kirin and {i}her{/i} roommate, so...I guess I’ll have to make the trip alone?"
    s "Would it be weird if you were to come with Ami and the rest of her group?"

    play sound "thump.mp3"
    scene karinangrybreakfast19
    with hpunch

    ka "With Ami?! The Ami who lives at your house?! "
    ka "Meaning that I would show up to your house really early in the morning to see you waking up and walking around in nothing but a T-shirt?!"
    s "Do you...think that’s just how I walk around the house when there are visitors there?"
    ka "I don’t know! Yes? No?"
    ka "Is it?!"
    s "Karin-"

    scene karinangrybreakfast20
    with dissolve

    ka "No! Don’t tell me! I don’t wanna know!"
    ka "I’ll just find out and maybe have to wash my eyes out with soap when I come to your house to tag along with Ami!"
    ka "Anyway, thanks for talking! Bye, Sensei!"
    s "Karin, hold on a-"

    scene karinangrybreakfast21
    with dissolve

    s "...second."
    s "…"
    s "…"
    s "…"

    scene karinangrybreakfast22
    with dissolve

    ka "…"
    s "Did you forget you ordered breakfast?"
    ka "Mhm..."
    s "Do you want to pretend you never walked out of the diner?"
    ka "…"
    ka "Mhm..."

    scene black
    with dissolve2

    "Karin winds up only eating around 30%% of what she ordered and stuffs the rest into an assortment of boxes to take home."
    "And I think she manages to get over her anger as well, as I can make out the sound of her whispering something about how Kirin will be excited to have pancakes when she gets home."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate20 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label karindate25:
...
```

## Code that triggers this event
File: \game\KarinEvents.rpy
Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
    if karin_love >= 15 and day264 == True and karinlied == True and karindate15 == False:
        jump karindate15
    if karin_love >= 20 and day355 == True and karinsoccer20 == True and karindate20 == False:
        jump karindate20
...
```