# Stronger I Become (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 91

* Event [One to Seven](./day63.md) (Main) is completed)

* Event [Girl-Talk](./day65.md) (Main) is completed)



## Next events

* [Main: Girl Talk Pt. II](./day120.md)

## Event properties

* Id: day91
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day91

## Official wiki page

[Stronger I Become](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day91&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day91:
    scene daynineone1
    with dissolve
    play music "sweetvermouth.mp3"

    "With just a few days left until the testing period finally begins, the girls are
    hard at work and studying diligently."

    ay "Sensei! Come look at my sword!"
    ay "It’s sharp enough to cut three bodies in one strike!"
    s "I’m sure it is, Ayane. I can see it from here. It’s very nice."
    ay "I will use this blade to defend our children."
    s "I’m sure you will."

    "Okay, so maybe not everyone is studying diligently."
    "In fact, only Makoto is. But that’s basically how things are in here now."
    "I’m not too worried, though. I mean, everyone seems confident enough to pass at least most of the subjects."
    "I’m not sure how grading for these things go, but I’m sure you don’t have to pass {i}every{/i} subject, right?..."
    "Oh well. They’ll be fine. It would be incredibly disruptive to the plot if they weren’t."

    scene daynineone2
    with dissolve

    sa "…"

    "Sana suddenly raises her hand and I can hear her ellipses from the back of the room."
    "It’s not like her to command my attention in class...I wonder if something is wrong?"

    scene daynineone3
    with fade

    s "Hey, Sana. Do you need something?"
    sa "Um...Not particularly..."
    sa "You just...seemed bored...so I thought I’d wave you over and..."
    sa "Um..."
    s "You wanted to see if I wanted to talk, right?"
    sa "R-right..."
    sa "I’m still...not really friends with anyone else and..."

    scene daynineone4
    with dissolve

    sa "And Ayane has a sword for some reason..."
    s "Are you surprised by this?"
    sa "I think I should be, but...no..."
    s "Sword aside, don’t you think maybe it might be time to branch out a little and...you know, maybe
    make some friends?"

    scene daynineone5
    with dissolve

    sa "W-What?! You mean...like...right now?..."
    sa "With everyone watching?..."
    s "No one is even looking at you."

    scene daynineone6
    with dissolve

    sa "What else is new?..."
    s "Sana...even if people {i}were{/i} looking at you, it shouldn’t change anything."
    s "The key to becoming social is just learning how to ignore everybody and adapt to conversation
    without putting any actual thought into it."

    scene daynineone7
    with dissolve

    sa "Please...don’t try to sabotage me, Sensei...I have a hard enough time as is..."
    s "Well, how about this? I’ll make the first move for you."

    scene daynineone5
    with dissolve

    sa "Wait...what? First move? What are you going to do?..."
    s "Something I should have done a long time ago..."

    scene daynineone6
    with dissolve

    sa "I don’t like the sound of this..."
    s "It’s okay. Just think about all of our training."

    scene daynineone7
    with dissolve

    sa "You’ve...barely even taught me anything..."

    scene daynineone8
    with dissolve

    s "Hey, Rin."

    scene daynineone9
    with dissolve

    r "Hm? Sensei? What’s up?"
    s "Not much. How are you doing?"

    "Sana suddenly begins to tug on my sleeve."

    sa "Um...S-Sensei..."

    scene daynineone10
    with dissolve

    r "Uhh...I mean, I’m pretty good I guess. Just looking outside the window and stuff."
    s "Awesome. But what if I told you that there were more exciting things to do than
    look out of the window?"

    scene daynineone11
    with dissolve

    r "I’d...agree? I just don’t know what else to do instead."
    r "Futaba is reading and stuff and she doesn’t like being bothered in the middle of that."
    sa "Uh...umm..."

    "The tugging grows stronger."

    s "Well how about you talk to Sana, then?"

    scene daynineone12
    with dissolve

    r "I mean, sure. I’d love to."
    r "She’s just always so quiet that I didn’t think she really wanted to talk to anybody."

    scene daynineone13
    with dissolve

    sa "Um...I would...love to talk!"
    s "See? That wasn’t so hard, was it?"
    s "Just talk to Rin the same way you talk to me and everything will be fine."

    scene daynineone14
    with dissolve

    sa "Will you...stay and make sure I do everything right?"
    s "Nope. Your mission begins now."
    s "Have fun!"
    sa "What?!"

    scene daynineone15
    with dissolve

    sa "Ah-!"
    r "Cool! Mission text!"

    scene daynineone16
    with dissolve

    sa "Uh...umm...ahh..."
    r "Hey, Sana! What’s up?"
    sa "Um...nothing! Wh-What’s...up...with you?"
    r "Oh, you know. Just hangin’ around the classroom, doing classroom stuff. Same old, same old."
    r "The two of us haven’t really talked before, have we?"

    "I stand several steps back and watch as Sana begins her first ever conversation with the
    girl who has sat literally right next to her for the entire year."
    "In order to get a good look, though, I need to stand right next to Ayane."
    "Which of course means I need to continuously swat her hand away from me every three seconds."

    scene daynineone17
    with dissolve

    sa "Um...no...we haven’t..."
    sa "I’ve always...wanted to, but..."
    r "…"
    sa "…"
    r "It’s okay. Take your time."
    r "I get nervous around new people, too. Don’t worry about it."
    r "Besides, it’s not like I’m going anywhere. We’re still in[school] for another
    like, three hours or something."

    scene daynineone18
    with dissolve

    sa "R-Right! Th...thanks..."
    r "Of course! So, is there anything you’d like to talk about?"
    r "You play games and stuff, right?"

    "As expected, Rin takes the lead in the conversation and begins to steer Sana back into her comfort zone."
    "I think back to the other day when I was hanging out with Sara and Haruka."
    "I remember thinking then that it was weird these two had never gotten to know each other."
    "And, given Sana’s current skill level when it comes to public speaking, Rin is probably a great option for a first non-Ayane friend."

    scene daynineone19
    with dissolve

    sa "Y-Yes! I love games! Do you...um..."
    sa "Do you play anything, Rin?..."

    "Great job, Sana- already calling her by her name."
    "It’s a small detail, but a very important one in the world of socialization. Using someone’s
    name helps assure them that you’re paying attention."
    "I’m sure Rin doesn’t care about (Or even notice) things like that, but I’m still proud regardless."

    ay "Senseiiiii~"
    s "Ayane, stop touching me."
    ay "{i}Boo...{/i}"
    r "Of course!"

    scene daynineone20
    with dissolve

    r "Let’s see...I don’t really have as much time to play stuff as I used to, but I
    really like online multiplayer stuff mostly."
    sa "So like...MMO’s? Or do you like shooters more?..."

    scene daynineone21
    with dissolve

    r "Shooters. The more they bleed, the stronger I become..."

    scene daynineone22
    with dissolve

    sa "H-huh?..."
    sa "Is this...what bullying is?..."
    sa "Are you...trying to intimidate me?..."

    scene daynineone23
    with dissolve

    r "What?! No! Of course not! That was just a joke!"
    r "I like shooters, yeah, but I don’t actually become stronger by consuming peoples’ blood or anything."
    r "I was just playing around. I’m not bullying you at all."
    r "In fact, I think you’re super cute and like, I’ve kinda wanted to be your
    friend since the year started and stuff."

    scene daynineone24
    with dissolve

    sa "Huh?...You’ve..."
    sa "Really?"
    r "Of course! You’ve just always seemed kinda...distant."
    r "Oh, and I also want to try on that one dress you wear around the dorm all
    the time, but there’s no way in hell it would ever fit me."

    scene daynineone25
    with dissolve

    sa "Um...well...if it’s not a bother...I..."
    sa "I wouldn’t mind being your...friend..."

    scene daynineone18
    with dissolve

    r "Really? Awesome! That’s great news!"
    r "Maybe the two of us could hang out sometime then!"
    r "You’re literally in the room connected to mine, so it’s not like you don’t know where to find me."

    scene daynineone19
    with dissolve

    sa "I’d...love to! Thank you so much!"
    r "Dude, you don’t have to thank me."
    r "Like I said, you’re super cute and I’ve wanted to be your friend
    for a while. Just let me know whenever you want to chill, okay?"
    sa "Okay! Thank you!"
    sa "Oh, I mean, umm..."

    scene daynineone26
    with dissolve

    r "Hey! We did it!"
    sa "Where are these letters coming from?..."

    scene daynineone27
    with fade

    "I wait a minute before returning to Sana’s desk to congratulate her on a job well done."

    sa "Sensei! Did you...did you see what happened?!"
    sa "I made a friend!"

    "Sana is loud enough that Rin can hear her, but instead of jumping into
    the conversation, she just glances over and winks at me."

    s "I did. You were great, Sana. Like I’ve been saying, it’s not that hard to-"
    sa "No, it was totally hard! I almost cried!"
    sa "But I didn’t! I pulled through!"
    sa "And now I have a new friend!"
    s "That’s right! Now you just need to befriend the rest of the class and
    your main quest-line will finally be complete."

    scene daynineone28
    with dissolve

    sa "Wait...I have to be friends with {i}everyone{/i}?..."
    s "That’s right. Keep working hard, Sana."
    sa "But...I was barely even able to make one..."

    scene black
    with dissolve

    "I head back to my seat without giving Sana an opportunity to argue why she doesn’t
    need to become friends with everyone in class."
    "And the fact is, she doesn’t."
    "It’s rare that anyone in any class is ever friends with {i}everyone{/i}."
    "But in Sana’s case, I think it’s a good idea."
    "Or, at least it’s one of the only ways I can think of getting her to open up more for now..."
    "Oh well."
    "We’ll just have to see how things go from here on out."

    $ renpy.end_replay()
    $ sana_love += 1
    $ day91 = True
    stop music fadeout 3.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label day96:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
$ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
    if totaldays >= 89 and day65 == True and day89 == False:
        jump day89
    if totaldays >= 91 and day63 == True and day65 == True and day91 == False:
        jump day91
...
```