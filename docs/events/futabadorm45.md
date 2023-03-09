# Hall of Mirrors
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm45&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 45

✅Day of week is not Wednesday

❌Day of week is a weekday

✅Event "[Futaba: Without Running Away](./library40part2.md)" is completed (event=library40part2)



## Next events
* [Sana: Sweet Vermouth](./bar45.md)

## Event properties
* ID: futabadorm45
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm45:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm

    play sound "knock.mp3"

    "I knock on Futaba’s door and wait for her to answer. "

    r "Come in!"

    "Rin answers instead."
    "Is this just how things are going to be from now on?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene futabagymtwo1
    with dissolve

    r "Yo! What’s up, Sensei?"
    s "Hey. Do you know where Futaba is?"
    r "Yes sir. I’m actually on my way to meet her now."
    r "She’s at the gym with Nodoka and, if the texts I’m receiving are true, the scary but also hot blonde lady from the last time."
    s "Yumi’s mom."

    scene futabagymtwo2
    with dissolve

    r "Wait, what? Are you for real?"
    s "Yes. And before you go saying anything about it to Yumi, please be advised that they are not on good terms with one another."
    r "I mean...I don’t really talk to Yumi anyway. But I’ll keep that in mind."
    r "Also, we shouldn’t tell Nodoka about it because she has the hots for her and kind of hates Yumi, so yeah."
    s "I’ve come to learn that Nodoka has the hots for virtually every single older woman she has met."
    r "I feel that."
    s "Well, I guess I’ll just...head home then."

    scene futabagymtwo3
    with dissolve

    r "You’re not gonna come hang out at the gym with us?"
    s "Am I “allowed” yet?"
    s "Futaba seemed pretty adamant about me not coming."

    scene futabagymtwo4
    with dissolve

    r "Futaba’s been doing great lately, so I’m sure she won’t mind. "
    r "You’ve got the Rin stamp of approval for tonight and tonight only, Sensei!"
    s "Okay, but if I get yelled at, you’re taking the blame."
    r "Roger that! "

    scene nightsky
    with fade
    stop music fadeout 10.0

    "Rin and I exit the dorm and begin to make our way over to the gym."
    "As it turns out, Futaba’s been spending more time there than both her and Nodoka combined ever since the place opened."
    "Which is impressive, don’t get me wrong...but it sounds slightly worrying for someone who doesn’t have much of a history with exercise."
    "I’m in pretty good physical shape and even I can’t fathom being able to handle prolonged exposure to...treadmills or...other exercise things."
    "See? I don’t even know the names of the things. That’s how bad I would be in the gym."
    "Either way, I’m glad Futaba seems to be doing well on at least an...attendance level."
    "I just hope that she’s not overworking herself."

    scene black
    with dissolve

    "………"
    "……"
    "…"
    "…"
    "……"
    "………"

    play sound "static.mp3"
    scene futabagymtwo5 with flash
    stop sound
    play music "pianomelancholy3.mp3"

    "There are 357 chances to go back locked inside the Palace of Versailles’ Hall of Mirrors."
    "I wonder how many of them the two of us could stand in front of without feeling out of place."
    "I mean, we are not mirrors of course. "
    "So unless they wanted to retitle it the “Hall of Mirrors & People,” which seems unlikely at this point in time, we’d basically be screwed."
    "But that’s okay!"
    "There are mirrors everywhere!"
    "Everywhere we go, we can remind ourselves of the things we either love to see or hate to see!"
    "Or tolerate seeing!"
    "We even have them built into our phones now!"
    "We are everywhere, all at once."
    "And though many of us hate being followed by ourselves or, as Futaba so artistically mentioned the other day, our {i}shadows{/i}, the rest of us can live peacefully."
    "Unfortunately, however, there are people who would go mad in a room with that many mirrors."
    "Are you among them?"
    "Do you enjoy looking at yourself?"
    "If not, what {i}do{/i} you enjoy looking at?"
    "Is it something portable?"
    "Something you could hold in front of your face, so that when you’re forced to stare at your reflection over and over and over again, you won’t want to destroy what you see on the other side?"
    "Personally-"
    "I’d like to destroy anything and everything."
    "I’d like to destroy all of it so I could rebuild it all again."
    "Especially that stupid fucking Hall of Mirrors because 357 is an idiotic number and should have been rounded up to 360 or something."
    "I think 365 would be better, though."
    "That way, you could stare into a new mirror every single day of the year-"
    "And still look absolutely hideous."
    "Except for leap years, obviously."
    "On leap years, you’d get an extra day to do whatever you want."

    "A day where mirrors or pictures don’t exist."
    "Where everything in the world is entirely up to perception and can not be visually checked by others."
    "It would all be exactly as we want it to be, and we’d never have to face the truth of what it {i}actually{/i} is."
    "Do you understand?"
    "…"
    "No?"
    "Well, fuck you then."
    "74 68 69 73 20 69 73 20 6e 6f 74 20 77 68 61 74 20 79 6f 75 20 74 68 69 6e 6b 20 69 74 20 69 73"

    play sound "static.mp3"
    scene futabagymtwo6 with flash
    stop sound

    r "Futaba?..."
    f "AAAAAAAAAAAAAHHHHHHHHHHHHH!!!!!!"

    play sound "static.mp3"
    scene futabagymtwo7
    with flash
    stop sound

    s "What’s going on?"
    yu "Fuck if I know. All I did was say hi and she started freaking the fuck out."
    yu "She ain’t on drugs or some shit, is she? Not really sure how to handle this."
    f "I’m fine! Just...Just give me a minute!"
    no "Take as much time as you need. No one’s rushing you."
    s "She’s not on drugs. Seeing you probably just...surprised her."

    scene futabagymtwo8
    with dissolve

    yu "Shit, dude! I ain’t {i}that{/i} intimidating, am I?"
    f "Sensei...please go home!"
    r "Futaba..."
    s "It’s not that. She’s probably just...feeling reminded of something she didn’t want to be reminded of."
    no "We’re going to need a better explanation than that if we’re going to be able to understand..."
    yu "Yeah. The fuck is that supposed to mean?"
    yu "I’ve never even said a word to the fuckin’ girl. The hell would she be reminded of?"
    s "Your daughter."

    scene futabagymtwo9
    with dissolve

    f "I told you to go home!"
    s "Which I would happily do if you weren’t having a nervous breakdown."
    f "I’m just stressed! It’s not a breakdown! "
    no "Her daughter?"
    yu "Yumi? She do something to this girl?"

    scene futabagymtwo10
    with dissolve

    no "Yumi?..."
    yu "The fuck did she do that would make a girl break down like that out of fuckin’ nowhere?"
    f "You are making everything worse! Go home!"
    no "You’re...Yumi’s mom?"
    yu "In name only at this point. Hasn’t said a word to me in years."
    s "Yeah, that kind of...has a lot to do with what happened."
    s "You were brought up and Yumi kind of exploded on Futaba here."
    s "Which, by itself probably would have been okay, but she’s been tormenting her for the entire[school] year."

    scene futabagymtwo11
    with dissolve

    f "Do you think this is helping?"

    play sound "static.mp3"
    scene futabagymtwo12 with flash
    scene futabagymtwo11 with flash
    stop sound

    s "I don’t know. But there’s not really anything else I can do."
    s "It’s not like Yumi’s going to stop on her own. And you’re already freaking out, so there’s no harm in just airing out all of the dirty laundry while we’re still in the thick of things."
    no "I’m going to be sick."
    yu "The fuck you mean “tormenting” her? How’d I even come up in the first place?"
    s "You just...did. It wasn’t really a calculated decision or anything."
    yu "And that alone was enough to make her blow up?"
    s "Yes. But, like I said, this has been going on for a while and-"

    scene futabagymtwo13
    with dissolve

    yu "Hey...uhh...Futaba, was it?"
    yu "I’m not really that good at this...apology shit...but I’m sorry for whatever my fucking shithead daughter said to you."
    f "You...don’t have to..."
    yu "Nah, I kinda do. Even if she doesn’t talk to me, I’m a lot of the reason she wound up the way she did."
    yu "So I’m not askin’ you to forgive her or try to be her friend or any of that shit...I just want you to know that she’s a prick and that...she’ll just do shit like that sometimes."
    yu "It runs in the family, I guess."
    f "Oh...uhh...okay..."
    s "Great. So, now that everything is back to normal-"

    scene black
    with dissolve

    "Futaba gets off of the workout bench thing (Still have no idea what the proper name is) and immediately approaches me."
    "Yuki and Nodoka quickly back off and I’m suddenly dealing with this on my own..."

    scene futabagymtwo14
    with dissolve

    f "Back to normal?"
    f "It wasn’t enough to come to the one place you {i}know{/i} I’m not comfortable with you seeing me in...You had to tell Yumi’s mom about what happened as well? Even when I told you not to?"
    f "And then once you’re done you say everything is “back to normal?”"
    f "Are you kidding?"
    s "I-"

    scene futabagymtwo15
    with dissolve

    r "I...deserve some of the blame too."
    r "He was going to go home and...I invited him to come hang out here with us."
    f "Even though you knew I didn’t want him here?"
    r "Yeah..."
    r "I just thought you’d been doing a great job lately and...that you might change your mind if he was actually here."

    scene futabagymtwo16
    with dissolve

    f "Well...that still doesn’t change anything."
    f "Sensei should have known better."
    f "But apparently Sensei cares more about {i}observing{/i} my issues than he does actually helping me with them now."
    s "I really didn’t mean any harm."
    f "Yes you did..."
    s "Futaba-"
    f "No. Don’t say another word."
    f "Just because I opened up to you about my...disorder doesn’t mean I want you neck deep in all of my problems, Sensei."
    f "Stop getting involved in every single aspect of my life and let me do what I need to do to get better."
    f "Now, go home. I don’t want you here."
    r "Sorry again, Futaba..."
    f "I’ll deal with you later, Rin. I just want to get back to working out and...forget this whole freakout even happened."
    s "…"
    f "…"

    scene black
    with dissolve2

    "I somehow manage to bite my tongue (Something I’m not very good at) and head home."
    "I wish I had more to say about why I just...kept going despite being told to stop-"
    "But I guess it really just comes down to something I already know about myself."
    "I’m the worst."
    "I don’t need any fancy words or poetic prose to showcase that."
    "Just a few actions that seem small to me, but gigantic to someone else."

    scene bedroom_night
    with dissolve2

    if bonus == True:
        "I lie in my bed after microwaving the dinner Ami left out for me, unsure of whether or not I want to go to sleep now or spend the next hour or two browsing the Internet for porn."
        "What I’d prefer is to wallow in self-pity and beat myself up over getting involved in something I shouldn’t have bothered with-"
        "But that just doesn’t seem possible right now."
        "I don’t feel anything."
        "I’m too busy thinking of mirrors."
    else:
        "I lay in my bed after microwaving the TV dinner Ami left out for me, happy that she was able to find one where none of the corn spilled into the brownie."

    play sound "knock.mp3"

    a "Umm...Sensei?"
    s "Yeah? What’s up?"
    a "Uhh...Futaba is here to see you?"
    s "Wait, really?"
    a "Yeah...I invited her in but, she says it will only take a second and that she’d rather stay outside."
    s "…"

    "Huh."

    scene black
    with dissolve

    "I get off the bed and head to the front door."
    "Ami tries to follow me to see what's going on, but I wave her off and she heads into her room as I make my way outside..."

    scene futabagymtwo17
    with dissolve2

    s "Hey."
    f "Hi..."
    f "So...umm..."
    f "I wanted to...apologize for how I acted before."

    "Weakling."

    f "I know you wouldn’t do anything to purposely hurt me and...I’m sorry for telling you not to get involved when...I’m sure you were just trying to help."
    f "I’ve just been...overworking myself lately and...so many things happening at once got to me."
    s "It’s fine."
    s "I’m just a little surprised since I figured I was going to have to be the one to apologize to you."

    scene futabagymtwo18
    with dissolve

    f "I mean...that...would be kind of nice..."
    f "Since you sort of...did exactly what I told you not to do...twice."
    s "The first one should be excused because it was Rin who invited me. Just assume I was going there to hang out with her."
    f "Nice try, but...she already told me that you asked for me when you showed up at the dorm."
    s "Then she has betrayed both of us today and can not be trusted any longer."

    scene futabagymtwo19
    with dissolve

    f "Heheh...if that’s true, then the only person I can still trust is Nodoka. And she’s...still a little shaken up by discovering her latest crush is Yumi’s mom."
    s "She’ll get over it the second another older woman walks by."

    scene futabagymtwo18
    with dissolve

    f "Probably..."
    f "But...yeah..."
    f "I just wanted you to know that...I didn’t {i}entirely{/i} mean everything I said to you at the gym tonight."
    f "Yes, I do wish you’d be less involved in...certain aspects of my life..."
    f "But that thing about how you care more about observing my issues than helping me was...uncalled for."
    s "Well, thanks."
    s "But next time, wait a little longer before coming to apologize. "
    s "There’s no point in saying anything mean to anyone if you’re just going to backtrack as soon as it happens."
    f "I...think you’re overestimating how mean I want to be..."
    f "You should know by now that...that isn’t the kind of person I am."
    s "That’s right."
    s "You’re the kind of person who walks across town to apologize for something {i}I{/i} did when you could have just called or sent me a text."

    scene futabagymtwo20
    with dissolve

    f "Well...I also wanted to...see you, so..."
    f "I’ll go home now, though."
    s "Do you want me to walk you back?"

    scene futabagymtwo21
    with dissolve

    f "No...it’s okay. I’ll probably stop at the convenience store for coffee along the way or something..."
    s "It’s like...10:00 PM."
    f "Yeah, but...I’m suddenly in the mood to...try writing something."
    s "Ahh, yes. Overworking yourself mentally because overworking yourself {i}physically{/i} wasn’t quite enough."
    f "Exactly. "
    f "But at least I know...you and everyone else will wind up swooping in to save the day or something if I...work too hard again."
    f "So...yeah."
    f "I’m sorry again and...goodnight, Sensei."
    s "Goodnight, Futaba."

    scene black
    with dissolve2

    "Sometimes, people apologize just so they can hold onto things they’re afraid of losing."
    "I feel like tonight was one of those nights."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabadorm45 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rindorm50:
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
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
            if futaba_love >= 15 and futabanew2 == True and futabanew3 == False:
                jump futabanew3
            if futaba_love >= 15 and futabanew3 == True and futabadorm15 == False:
                jump futabadorm15
            if futaba_love >= 25 and day > 5 and bookdate == True and futabadorm25 == False:
                jump futabadorm25
            if futaba_love >= 30 and library30 == True and day != 3 and futabadorm30 == False:
                jump futabadorm30
            if futaba_love >= 35 and library35 == True and futabadorm35 == False:
                jump futabadorm35
            if futaba_love >= 40 and day != 3 and dormwar17 == True and futabadorm40 == False:
                jump futabadorm40
            if futaba_love >= 45 and day != 3 and day < 6 and library40part2 == True and futabadorm45 == False:
                jump futabadorm45
...
```