# Partners in Crime
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindate1&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 0

✅Event "[Miku: Coach](./soccer20.md)" is completed (event=soccer20)



## Next events
* [Main: What's Done is Done](./beachvacation1.md)
* [Kirin: Long and Hard](./kirindate5.md)

## Event properties
* ID: kirindate1
* Group: Kirin
* Triggered by label: kirinafternoonhang
* Triggered by branch label: callafternoon

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirindate1:
    "I guess I’ll give Kirin a call."
    "I’ve sort of been sitting on her number ever since she gave it to me, and she seems...normal enough to hang out with."
    "Okay, well, maybe 'normal' isn’t the right word."
    "If anything, she’s actually kind of abnormal. "
    "But it’s the good kind of abnormal."

    if bonus == True:
        "The kind that makes me feel like she’ll be down to sleep with me after hanging out a few times."
        "And it’s not wrong for me to say that, either, since this was basically her idea."
        "I’m just a totally normal teacher who can’t help but do whatever’s possible to make his students happy."
        "And, uhh, other students, I guess. Because Kirin isn’t really my responsibility."
    else:
        "Like she's actually an evil spirit or something."
        "Wait, no. That's paranormal. Silly me."

    "What am I even talking about right now? I should just call her before she winds up doing something else."

    play sound "phonebeep.wav"

    "I press on Kirin’s name in my contact menu and wait for her to pick up."
    "…"

    play sound "phonebeep.wav"

    ki "Hihi~ Whatcha up to, Sensei? Bored on your day off?"
    s "I guess so. Just looking for something to do."
    ki "Cool, cool. "
    ki "Wanna come over?"

    "Woah. Already?"

    if bonus == True:
        s "Really? Your parents aren’t home?"
    else:
        s "Can I have chocolate milk if I do?"
        ki "Uhhhhh...sure?"
        s "Did your parents and or roommates specifically say it was okay for me to drink their chocolate milk? Because I need to know for sure before I make any plans."

    ki "Nope! They’re not here much anyway."
    s "And your sister?"
    ki "Mmm...I think she’s out with Miku? I can’t really remember."
    s "And she’s not planning on coming back any time soon?"
    ki "What’s with all the questions? Do you wanna come over or not?"
    s "Sure. Where do you live?"
    ki "Do you know where Pepper-Lunch is?"
    s "Pepper what?"

    stop music fadeout 10.0

    ki "Some old restaurant that’s popular with people your age. I used to work there ‘til I got
    fired for some stupid stuff."

    s "Getting fired at your age probably isn’t going to look good on future applications."
    ki "Ehh, it’s whatever. That job was super boring anyway."
    ki "Just look up the address of that place and meet me there in like...half an hour. Kay?"
    ki "I’ll walk you to my house and stuff."
    s "Sure thing. See you then."
    ki "Byeeee~"

    play sound "phonebeep.wav"

    "..."
    "After hanging up, I punch in the address to Pepper-Lunch in my phone and begin to make my way there..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    play music "justbehappy.mp3" fadein 7.0
    scene kirinfirstdate1
    with dissolve

    "I show up in front of the restaurant to find Kirin already waiting there."
    "I feel slightly bad for making her stand around and wait for me to show up, but then I
    remember she doesn’t live far from here and immediately get over it."
    "She’s probably only been here for a few minutes anyway."

    scene kirinfirstdate2
    with fade

    "Kirin pulls herself off of the wall and skips over to me as I approach her. "

    ki "Hey! Find the place okay?"
    s "It was easy enough."

    if day89 == True:
        s "I’ve been around here before, so I more or less knew where I was going."

    else:
        s "Maybe a little confusing at first, but once I figured out the streets were numbered it was fine."

    ki "Well I’m glad you made it. I felt like I was gonna die if I had to sit around the stupid house all day."
    s "Do you...not have any friends or something?"

    scene kirinfirstdate3
    with dissolve

    ki "Of course I have friends...What is that supposed to mean?"
    s "I don’t know. I just figured that if you did, you’d be hanging out with them instead of, you know, a teacher."

    scene kirinfirstdate4
    with dissolve

    ki "I was actually thinking about texting a few of ‘em, but then I saw your number show up and was like “ehh, screw it.”"
    ki "And now here we are, in front of the place that fired me for not showing up to one or two shifts."
    s "Not to take sides here, but I’m pretty sure that’s a good reason to fire someone."

    scene kirinfirstdate5
    with dissolve

    if bonus == True:
        ki "Right, right. Cause you know all about doing stuff that can get you fired, don’t you, Sensei?"
        s "Valid point, Kirin. And thank you for reminding me that you occasionally eavesdrop on what
        happens inside of my office."
        ki "Of course! You’re very welcome~"
    else:
        ki "Yeah. I learned from my mistakes and am attempting to become a better person."
        s "I'm very proud of you for being able to admit that, Kirin. That takes strength."

    scene kirinfirstdate6
    with dissolve

    ki "Are you, uhh, sure you’re ready to come over, though? I figured you’d be kinda hesitant after our talk in your office. "

    if bonus == True:
        s "Why would you think that? I literally agreed to help you ditch[school] in exchange for sex during that same conversation."

        scene kirinfirstdate7
        with dissolve

        ki "Well, yeah, but you didn’t seem as excited about it as I thought you’d be. I was kinda expecting you
        to like, push me down and just shove it in there or something."
        s "That's...kind of vulgar. I don't really think I'd go {i}that{/i} far."
        s "I’m obviously not the best when it comes to expressing emotions, but I can assure you I was very much excited."
        s "I especially liked the part where you showed me your underwear. That was cool and you should do it again."
    else:
        s "I know I didn't seem very enthused by the prospect of watching Seinfeld Season 3 back then, but I have thought more about it and am ready to give it a try."
        ki "Okay, but if you change your mind-"
        s "Just take me to your damn apartment, woman."

    scene kirinfirstdate5
    with dissolve

    ki "Bossing me around already? We’re not even alone yet, Sensei."
    s "So it’s okay to boss you around once we {i}are{/i}?"
    ki "Hehe~ Maybe not today. I’ve still gotta size you up and stuff."

    if bonus == True:
        s "…"
        s "Like, measure my penis?"
    else:
        s "Is there a height limit? Oh! Do you live on a rollercoaster?!"

    scene kirinfirstdate8
    with dissolve

    ki "What? No. It’s a phrase."
    ki "I meant like, I want to at least be alone with you for a little while and stuff to make sure you’re
    not like, a {i}total{/i} creep."
    s "Oh. I, uhh, think that might be a problem then. But I’ll do my best."

    scene kirinfirstdate6
    with dissolve

    ki "You don’t really have to do anything you normally wouldn’t. I mean like, we’ll be alone, so stuff might just happen naturally. "
    ki "That’s how this sort of thing goes, right?"

    if bonus == True:
        ki "A guy and a girl hang out alone. Hands wind up going where they’re not supposed to go. Blah blah blah, orgasms, so on and so forth."
        s "That...was a really weird sentence. But I think I know where you were going with it."
        s "It’s kind of weird to hear you talk like that, though."
        ki "Weird? Why? You barely even know me."

        "That’s...a good point."
        "I really don’t know Kirin at all. It’s just strange hearing girls her age without
        any sexual experience discussing orgasms so bluntly."
        "It’s like she’s another Ayane. And two Ayane’s in the same dimension sounds kind of intimidating."

        s "It’s just odd hearing stuff like that from someone other than Ayane."
    else:
        s "I just want to reiterate that I'm only here for chocolate milk."

    scene kirinfirstdate9
    with dissolve

    ki "Ohhhh. Is that so?..."
    s "…"
    s "Why do you look so pissed off now?"

    scene kirinfirstdate10
    with dissolve

    ki "I’m not pissed off."
    ki "Just...follow me."

    scene kirinfirstdate11
    with dissolve

    ki "I’ll show you where the apartment is..."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Kirin’s anger(?) winds up fading away just moments later."
    "She begins to tell me about the all of the different shops in the area- which ones
    have the best prices...which ones are open the latest."
    "From the sound of it, she’s lived in this same area her entire life."
    "I wonder what it is that turned her into who she is now?"
    "Or, at least, what she seems to be."
    "The whole thing about not knowing her is sticking in my head a lot more than I thought it would..."

    play sound "dooropen.mp3"
    scene kandahouse
    with dissolve

    ki "I’m home~"

    "Kirin calls out to absolutely no one and takes her shoes off, leaving them in the entryway."
    "She leads me into a relatively modern looking apartment teetering somewhere between upper middle
    class and high-end. "
    "I’d actually be rather impressed by the place if it wasn’t also the size of a large shoebox. "

    s "Does your entire family really live here?"
    ki "Hm? Yeah. What do you mean?"

    scene kirinfirstdate12
    with dissolve
    play music "love.mp3"

    "I join Kirin, who’s already taken a seat on the couch, and continue on with my train of thought."

    s "It just seems kind of small for four people. Do you and Karin share a room?"
    ki "Technically, yeah. I normally just sleep on the couch, though."
    s "You sleep on the couch in your own home?"
    ki "Yeah. Karin talks in her sleep sometimes and it gets really weird."
    s "She talks? About what?"

    scene kirinfirstdate13
    with dissolve

    ki "Sports stuff, I guess? Nothing interesting or sexy or anything like that."
    s "I see."

    scene kirinfirstdate14
    with dissolve

    ki "What? Boring answer? Did you think she might be saying stuff about you or something?"
    s "Not really, no. Was just hoping for something a little more entertaining."
    ki "Yeah. I can relate to that."
    ki "Life can get pretty boring sometimes, huh?"
    s "It’s not {i}that{/i} bad."
    ki "Says the guy with a harem of [high_school] girls."

    if bonus == True:
        s "Okay, so it’s not that bad {i}for me{/i}."
    else:
        s "Hey, I never wanted that. I just want to teach."

    s "What do you have to be bored of, though? Isn’t this like, the prime of your life?"

    scene kirinfirstdate15
    with dissolve

    ki "It’s supposed to be. I just feel like nothing ever happens around here anymore."
    ki "Yeah, the city’s closed off and stuff, but that’s not really what I’m talking about."
    ki "It’s like, everything I try doing I only do to be around other people. Nothing’s ever fun."

    if bonus == True:
        ki "And so a lot of the time I just wind up sitting at home reading or like, watching porn or whatever."
    else:
        ki "And so a lot of the time I just wind up sitting at home reading or like, donating money to charity or whatever."

    menu:
        "What kind of books do you like?":
            s "Interesting. You didn’t really strike me as a reader."

            scene kirinfirstdate16
            with dissolve

            ki "Is that an insult?"
            s "No, of course not. There’s nothing wrong with reading."
            ki "That’s not what your face says..."
            s "Well I can’t see my face, so I’m no help there...but what kind of books are you into?"

            scene kirinfirstdate15
            with dissolve

            ki "Hmm...Well, I don’t really read books. I guess just like, magazines or...whatever’s laying
            around the house."
            s "I see..."

        "Porn?!?!?! I LOVE porn!" if bonus == True:
            "I suddenly feel the urge to yell about my love for porn, but decide to suppress my desires and inquire normally."

            s "It’s not weird watching porn in the room with your sister?"

            scene kirinfirstdate17
            with dissolve

            ki "Well, she’s out all the time so it’s not like I’m never alone."
            ki "And I normally just use my phone anyway so I can hide under the blanket and..."
            s "…"
            s "Please go on."

            scene kirinfirstdate18
            with dissolve

            ki "…"
            ki "Naaaah. Not today..."

    "An awkward silence suddenly finds its way next to us on the couch, changing the air in the room for a brief moment in time."
    "I can’t tell if Kirin feels comfortable or uncomfortable. To me, she just seems weird."
    "Like she’s got some type of shell up that she’s trying to crack {i}and{/i} glue back together at the same time."

    ki "Hey."
    ki "Something’s been bugging me and I feel like I’m gonna get annoyed if I don’t ask you. Is that cool?"
    s "Sure. There aren’t many questions I have trouble answering. Sometimes, a window even pops up to help me choose."

    scene kirinfirstdate19
    with dissolve

    ki "A what now?"
    s "Nothing. Please just ask me your question."
    ki "Well, okay. But you have to be honest about it."
    s "Sure."
    ki "Okay, so, uhhh-"

    if bonus == True:
        jump kirinfirsthousex
    else:
        ki "How upset will you be if I tell you that one of my friends is actually borrowing my Seinfeld DVD right now?"

        stop music

        s "..."
        ki "You're really upset, aren't you?"
        s "Is that what you do to people, Kirin?"
        s "Invite people over just to cut them down?"
        ki "Not...normally?"
        s "So I'm special?? I'M THE ONE WHO GETS TO HURT?!"
        ki "..."

        scene black
        with dissolve

        s "I can't do this."
        ki "Wait. I have other DVDs. We can-"
        s "I'm going home to hug my accountant."
        s "Have fun dancing all by yourself."
        ki "Sigh. Looks like I'm donating to another charity..."

        play sound "seinfeld.mp3"
        $ renpy.pause(4, hard=True)

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirindate1 = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdaynight

label kirindate5:
...
```

## Code that triggers this event
File: \game\KirinEvents.rpy
Code:
```python
...
label kirinafternoonhang:
    if kirin_love >= 0 and kirindate1 == False:
        jump kirindate1
...
```