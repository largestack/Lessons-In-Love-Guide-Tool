# Swim Trip (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Still Young](./ayanedorm20.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: swimming
* Group: Happy scenes
* Triggered by label: ayanedorm20
* Chain sources: ayanedorm20
* Chain sources path: ayanedorm20

## Official wiki page

[Swim Trip](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=swimming&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label swimming:
    window hide
    scene 5
    $ renpy.pause(1, hard=True)
    scene 4
    $ renpy.pause(1, hard=True)
    scene 3
    $ renpy.pause(1, hard=True)
    scene 2
    $ renpy.pause(1, hard=True)
    scene 1
    $ renpy.pause(1, hard=True)
    scene 0
    $ renpy.pause(1, hard=True)
    scene neg1
    $ renpy.pause(1, hard=True)
    play sound "thisep.mp3"
    $ renpy.pause(5, hard=True)
    play sound "tvtrans.mp3"
    scene sitcom1
    with dissolve2
    $ renpy.pause(5, hard=True)

    play music "oldweather.mp3"

    s "…"
    a "…"
    s "…"
    a "…"
    s "…"
    a "…"

    play sound "dooropen.mp3"
    ay "I’m home!!"

    scene sitcom2
    with hpunch
    play sound "cheer1.mp3"

    ay "=D"

    scene sitcom3

    a "Ayane!"
    a "You made it!"
    a "Did bring thhee bathing suit)?"

    scene sitcom4

    ay "Yes! Are you ready to go swimming?!"

    scene sitcom5

    a "Yes! Swim!!"

    "So, I bet you’re wondering how I got mixed up in this situation."
    "And the true story is that it dates all the way back to when I was a child."
    "Some things transpired, and eventually the girl to my right’s parents were involved in a horrific car accident."
    "Now, she cooks me breakfast and fingers herself to the idea that one day I will love her even a fraction of how much she loves me."

    if bonus == True:
        "It can be kind of tough at times, but I’m pretty sure we’re going to have sex soon, so everything is okay."
    else:
        "It’s kind of tough at times, but now she does my taxes and everything is okay!"

    scene sitcom6
    stop sound

    a "Sensei! Take a look at Ayane’s swimsuit! Doesn’t it make you just want to eat her alive?"
    di "Cut! The line is “Doesn’t it make you want to eat her up?”"
    a "I know what the fucking line is."
    di "Then say-"
    a "Sensei! Take a look at Ayane’s swimsuit! Doesn’t it make you just want to eat her up?"
    s "…"

    if ayane_virgin == False and bonus == True:
        ay "Don’t mind him, Ami! He’s {i}already{/i} taken my virginity! I know he loves me DEEP down INSIDE!!!~!~~~"
        ay "{size=-15}imprettysureitmayhavecausedirreparabledamagetomeaswellsinceitstillfeelslikeit'sstuckinsidesometimes{/size}"

        scene sitcom5

        a "WhaaaaaaaaaaaaT?! That’s crazy!!! Me next!!"

    if ayane_virgin == True and bonus == True:
        ay "Swallow me whole, Sensei!"
        ay "Fuck me until I die!"

        scene sitcom5

        a "Ayane! Watch your language! "
        ay "Sorry Ami! LOL!!"

    play sound "dooropen.mp3"

    "..."

    scene sitcom7
    play sound "cheer1.mp3"

    m "Well, well, well. What do we have here?"
    m "A family gathering?"

    scene sitcom8

    ay "GUYS!! LOOK WHAT I CAN DO!!"

    scene sitcom9
    stop sound

    a "MAYA!!!!!!"
    s "…"
    m "Hi, Ami. Your eyes look absolutely marvelous today."
    a "I use them to see!"
    m "You're so very talented."
    a "Did you know that we are going to {b}SWIM{/b} today?"
    a "Hope brought clothes can wet!"
    m "I’m afraid I didn't bring my swimsuit, no."

    scene sitcom10

    m "How about you? Will you be joining them?"
    s "…"
    m "...I see."

    scene sitcom11
    play sound "laugh3.mp3"

    ay "Help! "

    scene sitcom9

    a "Maya! Remember the other day when we were discussing the things we like most about Sensei????"

    play sound "laugh1.mp3"

    m "If I recall correctly, my list was very short."
    s "…"
    a "Well, about that list, there’s something I’d like to add to it."
    m "Oh? And what’s that?"

    if bonus == True:
        a "His fingers feel like tiny people when they're inside of me!"
        a "We should have him put his fingers in both of us soon! It will be a good bondage experience!"
        di "Cut! Ami, come on! The word is {i}bonding.{/i}"
        a "Okay, seriously, who the fuck hired this guy?"
    else:
        a "The other day, when he was {b}hugging me in the dorm room{/b}, he was very gentle! You should have him try that on you some time!"

    m "I think I’ll have to pass on the {i}bondage{/i} experience, Ami. But thank you for the offer."

    scene sitcom12

    a "Suit yourself! But I know you secretly want the tiny people fingers inside of you as well."

    play sound "laugh2.mp3"

    a "We all do! That’s the whole point of Lessons in Love!"

    scene sitcom2
    play sound "cheer1.mp3"

    ay "I’m back!"
    ay "What did I miss?"

    scene sitcom13

    a "AYANEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE!"

    scene sitcom12
    stop sound

    ay "What?????????????????????????????"

    scene sitcom14

    a "I love you!"
    s "..."
    m "..."
    m "Do you have anything you'd like to add?"
    m "It’s not like you to just...sit there and observe."
    s "This isn't right."
    s "None of it is."
    s "Something is upside down."
    m "Oh? Could it be that you’re actually semi-conscious this time?"
    s "I feel no fear."
    s "I feel nothing."
    m "Is there something in particular you {i}want{/i} to feel?"

    if bonus == True:
        scene sitcom15
        play sound "cheer1.mp3"

        ay "He wants to feel me!"
        ay "Isn’t that...amf...right...Sensei?..."
        s "…"

        stop sound

        a "…"

        play sound "laugh3.mp3"

        a "Swim trip!"
        s "Are you sure you’re okay with watching this, 61 6d 20 69 20 6f 6b 61 79?"
        m "Who?"
        s "Isn’t that your name?"
        m "I think you might have me confused with someone else."
        m "Besides, this isn’t the worst thing I’ve seen. If anything, this is rather plain by comparison."
        m "You seem to be enjoying yourself, at least."

        play sound "laugh2.mp3"

        ay "SURRENDER YOURSELF TO MY TONGUE!~~~~~~"
        s "I don’t feel anything right now."
        ay "You’re just...*lick* saying that...because your [niece]...is right there..."
        a "…"

        scene sitcom16

        a "Cum in her mouth and I will kill you."
        m "So...is this really what a normal dream looks like to you?"
        s "Is that what this is?"
        s "A dream?"
        m "You would know the answer more than I would, wouldn’t you?"
        s "If I were dreaming, would you still be here talking to me?"
        m "You would know the answer more than I would, wouldn’t you?"
    else:
        scene colorbars
        play sound "cheer1.mp3"

        ay "He wants to feel the glorious colors of censorship!"
        a "There used to be real images here! Those images are no more!"
        ay "Noooooooooooooooooo."
        m "Is this what a normal dream looks like to you?"
        s "It's a little more colorful here...but I guess so?"

    scene sitcom17
    with dissolve
    play sound "laugh3.mp3"

    ay "Wait! No! I wasn’t finished!"
    ay "Sensei! Help!"

    scene sitcom18
    with dissolve

    s "Why do things like this keep happening?"
    m "You would know the answer more than I would, wouldn’t you?"
    s "Can't you say anything else?"
    m "Blame whoever wrote the script, not me. I'm just reading my lines."
    s "I think you know more than you let on."
    m "Are you implying that I understand this?"
    s "I don’t see what other reason there would be for you to keep showing up here."
    m "Showing up where? Your living room?"
    m "I come here almost every week."

    scene sitcom19

    a "Maya! Wanna sleep over tonight?! You can help me find Ayane!"
    m "I’ll think about it."
    m "Would you mind getting me a drink of water, Ami?"
    m "I’d like to have a word with Sensei."

    if bonus == True:
        a "Will you promise not to {b}TAKE A RIDE ON HIS GIANT COCK LIKE THE HORNY BITCH I KNOW YOU ARE????{/b}"
        m "Sure."
        a "Great! Then I will be right back!"
    else:
        a "Sure! {s}If you hug him I will tear you to pieces{/s} I’ll be right back!"

    scene sitcom20
    with dissolve
    scene sitcom21
    with dissolve

    m "…"
    s "…"
    m "Does this feel...familiar to you?"
    s "Does {i}what{/i} feel familiar?"
    m "Anything."
    m "What are you thinking at this exact moment?"
    s "Are you actually interested in what I think now?"

    scene sitcom22

    m "I'm not...entirely uninterested in your thoughts, you know."
    m "I just understand that the vast majority of them involve my friends with their clothes off."
    s "Does this feel familiar for {i}you{/i} in any way?"
    m "Perhaps it does. Perhaps it doesn’t."
    m "Not that it would matter even if it did."
    m "This will all reset momentarily and we’ll go back to doing whatever it is we do."
    s "Which is what?"
    m "…"
    s "…"
    m "Wait, perhaps?"
    s "…"

    "Wait?"
    "For what?"

    a "Maya! What flavor water do you want?!"
    play sound "laugh1.mp3"

    scene sitcom21

    m "…"
    s "…"

    if shrine10 == True:
        m "Please do not pursue me any further."
        m "It is in both of our best interests for things to stay the way they are now."

        scene sitcom22

        m "Live your new life the way you see fit. Leave me out of it."

    else:
        m "…"

        scene sitcom22

    m "I should probably get going."
    m "I have...things I need to take care of."

    scene sitcom23

    m "Enjoy your swim trip."
    m "Please bring something back for me."
    m "The watermelons they sell at the shack half a mile away from the beach are simply the best."

    scene sitcom24
    with dissolve

    s "…"

    "Am I supposed to bring back an entire watermelon for her?"

    scene black
    with dissolve2
    stop music

    "Ayane, Ami, and I went swimming that day and all of us drowned."
    "It wasn't any fun at all."
    "Our bodies were found three weeks later, bloated and unrecognizable."
    "Ami’s was found in two separate locations hundreds of miles apart."
    "Maya died from unrelated causes a week later."
    "Just kidding."
    "None of that ever happened."
    "We all lived happily ever after."

    window hide
    scene theend
    with dissolve2
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene specialmenu
    with flash
    play music "shiningstarvocals.mp3"
    stop sound
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene whereareyou
    with flash
    scene specialmenu
    with flash
    scene whereareyou
    with flash
    scene specialmenu
    with flash
    scene whereareyou
    with flash
    scene specialmenu
    with flash
    stop music
    stop sound
    scene black
    $ renpy.end_replay()
    $ swimming = False
    $ swimmingtrack = True
    jump saturdayafternoon

label howifeel:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
$ v11check()

    if ((totaldays >= 220) and (day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and
        (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and
        (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 14 or (amipoint + amimiss == 16)) and
        (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and
        (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2) and (day == 6)):
            jump day220
    if day == 6 and totaldays >= 370 and day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False:
        jump secondbeach1
    if totaldays >= 464 and christmastwo20 == True and day == 6 and mayafestival1 == False:
        jump mayafestival1
    if utamaid25p2 == True and day == 6 and iodorm25 == True and iospecial30 == False:
        jump iospecial30

    scene bedroom_day
    with dissolve2

    "{i}[totaldays] Days have passed...{/i}"

    if totaldays >= 24 and day24 == False:
        jump day24
    if totaldays >= 60 and day56 == True and aminew1 == True and aminew2 == False:
        jump aminew2
    if totaldays >= 80 and day72 == True and day80 == False:
        jump day80
    if totaldays >= 102 and day == 7 and day96 == True and mayadorm15 == True and letterttrack == True and howifeeltrack == True and day102 == False:
        jump day102
    if totaldays >= 174 and day154 == True and amidorm15 == True and futabadorm15 == True and day79 == True and makotonew3 == True and kirindate1 == True and ramen1 == True and mollydorm10 == True and rindorm25 == True and bar10 == True and day == 6 and beachvacation1 == False:
        jump beachvacation1
    else:
        "I wake up to sunlight pouring in through the window."

    "What should I do today?"

    menu satmorningmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Archery Range" if chapthreeactive == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Kirin":
                            jump kirinarchery
                        "Touka":
                            jump toukaarchery
                        "Uta":
                            jump utaarchery
                "Koi Cafe" if firsttimeamisroom == True:
                    if harukadate1 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Rin":
                                jump cafe
                            "Haruka":
                                if harukafirstlust == True:
                                    "What do I want to do?"
                                    menu:
                                        "Hang out":
                                            jump harukacafe
                                        "Quickie (Doggystyle)" if bonus == True:
                                            jump harukacafedogrep
                                        "Hug Really Quickly" if bonus == False:
                                            jump harukacafedogrep
                                else:
                                    jump harukacafe
                    else:
                        jump cafe
                "Library" if firsttimeamisroom == True:
                    jump library
                "Pool" if chapthreeactive == True:
                    jump mikupool
                "Soccer field" if firsttimeamisroom == True and chapthreeactive == False:
                    if soccer20 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Miku":
                                jump soccerfield
                            "Karin":
                                jump soccerfieldkarin
                            "Kirin":
                                jump soccerfieldkirin
                    else:
                        jump soccerfield
                "Ami's Room" if christmas7 == False:
                    jump amisroom
                "Maid Cafe" if christmas7 == True:
                    jump amimaidhub
                "Park" if day288 == True:
                    if otohadorm1 == False:
                        "I should make sure Otoha is settled into the dorm first before visiting her at the park."
                        jump satmorningmenu
                    else:
                        jump otohapark
                "Streets" if day304 == True and chapthreeactive == False:
                    jump toukastreets
                "New Hope Cathedral" if buckettoken == True and day == 7:
                    jump bucketscene
                "=D" if swimming == True:
                    jump swimming
...
```