# Hiding in Plain Sight (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Gamer Girl Grindfest](./dormwartwo4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo5
* Group: Main
* Triggered by label: dormwartwo4
* Chain sources: dormwartwo4
* Chain sources path: dormwartwo4

## Official wiki page

[Hiding in Plain Sight](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo5&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo5:
    scene datewarfutaba1
    with dissolve2

    ay "Hello and welcome back to yet another Dorm Wars interview with yours truly, Ayane Amamiya! Reporting in from the front of Couch Potato Arcade! "
    ay "Folks, in just a few moments now, we’ll be going live to the middle of the entertainment district where my favorite teacher {i}and{/i} yours embarks on a date with Futaba Fukuyama that’ll go down in history!"
    ay "Joining me today is her self-proclaimed best friend, Nodoka Nagasawa, who’s fresh out of the hospital bed and ready to continue fighting for the girl she loves so much!"
    no "Fortunately, there was no hospital involved. But yes, I am here to tell the world of the glories of my best friend, be it self-proclaimed or not."

    scene datewarfutaba2
    with dissolve

    ay "Nodoka, our last look at the official Dorm Wars online poll brought to you by the Produce Delivery Administration has Noriko Nakayama leading by a whopping 13 points."
    ay "Do you worry that these early results may foreshadow the ending to this competition? "
    ay "Or do you believe Futaba will be able to show everyone that polls are just polls and that the real winner of every election is someone chosen by a small group of overly powerful people?"
    no "I’m afraid I don’t have much time to spend online, so this is the first I’m hearing of any “polls.”"
    no "But what I {i}will{/i} say is that writing off my dearest Futaba is never a good idea."
    no "What she lacks in confidence, she makes up for in both reliability and persistence. And I believe that, today, we will see a side of her we’ve seldom seen before."

    scene datewarfutaba3
    with dissolve

    no "I’d also like to add that, should any late-thirties to early-forties woman be looking for someone young and full of energy to perform heinous sex acts on them, I am always available."
    ay "Thanks, Nodoka. That was a completely relevant and necessary comment that I’m sure all of our viewers really appreciated."
    no "Hooray for love and hooray for Team Futaba...even if siding with her gets me exiled from my floor."

    scene datewarfutaba4
    with dissolve

    ima "Hah...hah...hah..."
    ay "Oh! And here’s everyone’s favorite student teacher, Imani Imai, showing up almost an entire hour after the Dorm Wars began! "
    ay "Imani, is there anything you have to say for yourself?"
    ima "Fell asleep...on the subway..."
    ima "Had to run...two miles..."
    ima "Gonna die..."
    ay "Well, better late than never! As long as you-"

    scene datewarfutaba5
    with dissolve
    stop music fadeout 15.0

    ay "Wait! I’ve just received word that the eagle has landed! "

    scene black
    with dissolve2

    ay "Sensei’s made contact with his first target of the night, Futaba Fukuyama! And she’s...no! It can’t be! She’s still wearing her costume?!"
    ay "A cosplay date in the big city?! "
    ay "Is Futaba coming out swinging despite almost always taking a more indirect approach to love?!"
    ay "Find out soon, folks! Right here on...whatever the name of our television station is!"
    ay "We’ll be providing updates all weekend long! So make sure you tune in for our next interview with...I don’t know! Whoever we decide to interview next!"
    ay "So, until next time..."
    ay "Sayonara!"

    "........."
    "......"
    "..."

    scene datewarfutaba6
    with dissolve2
    play music "anewyou.mp3"

    s "Hey, sorry I’m- woah."

    scene datewarfutaba7
    with dissolve

    f "Oh, Sensei! It’s fine. I wasn’t waiting very long."
    f "I take it that was a...{i}good{/i} “woah?”"
    s "Yeah. This is just the first time I’ve gotten a good look at your costume up close and it certainly emphasizes your...uhh..."

    scene datewarfutaba8
    with dissolve

    f "Eyes?"
    s "Yes. That is exactly what I was referring to."
    f "I know what you were {i}actually{/i} referring to. But it probably isn’t something we should talk about in public."
    s "To be honest, I’m surprised you’re out in public {i}at all{/i} dressed like that. I figured your...self-consciousness would be rearing its ugly head again."

    scene datewarfutaba9
    with dissolve

    f "Ah...yeah. I’m sure that’s what anyone would expect. And I {i}definitely{/i} haven’t been doing myself any favors in that department lately, so..."

    scene datewarfutaba10
    with dissolve

    f "B...But, weirdly enough, I’m actually {i}more{/i} confident being in places like this where there are tons of people rather than only having a few handfuls passing by every now and then."
    f "It’s kind of like...with so many people around, the chances of anyone looking at {i}me{/i} go way down. So I feel a little better whenever I remember that. "
    f "Plus there are normally a bunch of other cosplayers around here for all of the themed cafes and...yeah. I’m just trying to...blend in by...{i}not{/i} blending in?"
    s "Well, anyone {i}not{/i} looking at you right now is an idiot when you’re clearly the most attractive person within at least a ten block radius."

    scene datewarfutaba11
    with dissolve

    f "Ha! I...expected you to say something like that, but it didn’t make it any less surprising. "

    scene datewarfutaba7
    with dissolve

    f "In any case, I’m...glad you’re not put off by being out with me while I’m dressed like this. "
    f "I felt like...if I was going to win today, I needed to challenge myself and...that meant doing something a little...unorthodox."
    s "That determined to win, huh?"

    scene datewarfutaba12
    with dissolve

    f "Failure isn’t an option today. And this costume gives me a load of extra confidence, so you better watch out."

    scene datewarfutaba13
    with dissolve

    f "I did have a sword to go along with it, but there are apparently rules against carrying things like that in public, so...I have to go pick it up from the police box later."
    s "I leave you alone for one morning and the police come after you. I’d expect this from your competitor, but you? Futaba, come on."

    scene datewarfutaba10
    with dissolve

    f "Let’s not talk about my competitor for now, okay? It’s just the two of us this morning and...I want it to stay that way."
    s "Of course. So, where to next? Any plans? Or are we just going to walk around and show everyone how attractive you are for the rest of the day?"

    scene sky
    with dissolve2

    f "I have a plan! In fact, I have several plans. And none of them involve me showing this side of myself to anyone else."
    f "Things like this..."
    f "Things like this are all for you. But before you respond, I want you to understand how embarrassing it was to say that and I’d prefer if you didn’t draw any attention to-"
    s "Say it again."
    f "Ugh! Sensei!"

    "Futaba and I start walking down the streets of the entertainment district, but I don’t bother asking where we’re heading as I’m sure that I’ll figure out a way to enjoy whatever it is without any prior knowledge."
    "I can’t recall any instance of the two of us going out and doing something that {i}I{/i} want to do, which I’m pretty sure is what today is about but, then again, there aren’t many things I {i}want{/i} to do to begin with."
    "Just being with her is enough to make the morning worthwhile. "
    "Especially when I can glance down at her chest any time there’s a lull in conver-"

    f "Eyes up here, Sensei."
    s "You don’t own me."
    f "Heheh...that may be true."
    f "But for the next few hours, let’s pretend it’s not."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene datewarfutaba14
    with dissolve2

    "To escape the heat (And also because Futaba probably planned it) we wind up climbing a narrow staircase into a small cafe overlooking some of the less scenic parts of the entertainment district."
    "There are no other customers, so it looks like we’ll have the place to ourselves for at least a little while."
    "This {i}would{/i} be cool, but I haven’t seen any employees yet either, so I’m beginning to question exactly what this place is and if Futaba, of all people, is going to be the one to defy all expectations and murder me."
    "And, to be fair, I probably deserve it considering that she and Makoto seem like the two most willing to accept the fact that I am also having sex with their friends."

    s "I regret nothing."
    f "Hm? What’s this about regrets?"
    s "My bad. Just talking to myself. "
    s "Where’d you hear about this place anyway? I don’t recall even seeing a sign for a cafe outside."

    scene datewarfutaba15
    with dissolve

    f "There used to be. I guess they either took it down or it was stolen or something. "
    f "I was actually a little worried that this place might be closed when I didn’t see anything outside, but I’m glad that worrying was for nothing."
    s "You’ve been here before, then?"

    scene datewarfutaba16
    with dissolve

    f "Mhm. With my parents, a {i}long{/i} time ago."
    f "I was a lot more into anime and manga when I was little, so they’d take me to the entertainment district to go shopping whenever they were able to find the time."
    f "It didn’t happen often given their schedules. But any time it did, we’d come here at the end of the day and eat dessert together before heading back home."
    s "And you’re not worried taking {i}me{/i} here will sever the...nostalgic connection you have with this place?"
    f "It’s {i}because{/i} it’s you that I took you here. Today’s a special day too, you know? And I’m just as excited to be out with you as I was to be out with my parents back then."

    scene datewarfutaba15
    with dissolve

    f "I just hope the management and menu haven't changed. The woman who used to run the place was always so nice to me when I was growing up."
    s "And {i}I{/i} hope that anyone at all works here because, as of right now, I’m not so sure."
    f "It’s not, uhh..."
    f "It’s not cliche...taking you to a cafe on a date, right? I’m just realizing now how...typical this must seem."
    s "Maybe if you weren’t dressed as some sort of scantily clad warrior or something, it would be. But I’m pretty sure you could take me anywhere right now and it wouldn’t be “typical.”"

    scene datewarfutaba17
    with dissolve

    f "That’s fair. I got so absorbed in the moment that I kind of forgot I was even wearing this."
    f "I promise we’ll do something more fun afterward. I just wanted to share something that was important to me with you and...I don’t get many chances to come here, so..."
    s "Careful. You’ve been pretty confident so far today and it would be a shame to start doubting yourself before anyone else even gets to see that."

    scene datewarfutaba14
    with dissolve

    f "You’re right. Which means this is the part where I’d normally say sorry. But I’m not going to do that today since I know you actually want to be here with me right now."
    s "And to think that a contest is what got you to realize that and not my countless attempts at positive reinforcement through affectionate affirmation."

    scene datewarfutaba18
    with dissolve

    f "There are other helpful factors at play, of course. Like the fact that I’m no longer a virgin."
    s "Are you sure that’s a topic you want to bring up in a cafe so directly linked to a bond you have with your parents?"

    scene datewarfutaba17
    with dissolve

    f "Okay, you just made stuff weird, so I’m going to use this opportunity to run to the restroom and wash my hands. But if a waitress or...anyone shows up, I’ll have a blueberry parfait and a cafe au lait."
    s "Ugh. Saying those words will take away some of my masculinity points."
    f "I’m sure it’ll be fine. You have plenty more to spare."

    scene datewarfutaba19
    with dissolve

    f "Oh, and I’m paying today! So you can feel free to order whatever you’d like! "
    s "You really don’t have-"

    if cheater == True:
        scene datewarfutaba20
        play sound "seek.mp3"

        s" ...to?"

        "WORDS HAPPEN."
        "MISS A THING."

        play sound "static.mp3"
        scene ayhh8 with flash
        scene ayhh2 with flash
        scene ayhh7 with flash
        scene datewarfutaba24 with flash
        stop sound

    else:
        q "Heeeeylo there! Sorry for the wait! What can I do for you?"

        scene datewarfutaba21
        with fade

        s "Oh, hi. I’ll take- woah. You are extremely attractive and I was not prepared for that."
        q "Sorry, we’re fresh out of “You are extremely attractive and I was not prepared for that” on account of you being on a date."
        q "But if you’re looking for veal a la mode or mantis juice, I can hop back into the kitchen and start getting that ready for you."
        s "Uhh...how about a blueberry parfait and...a cafe au lait?"

        scene datewarfutaba22
        with dissolve

        q "Yikes. By my calculations, you just incurred a net loss of roughly fifty masculinity points. May I recommend a nice hot plate of grilled weta to shove some of those points back into you?"
        s "I have no idea what that is and it sounds weird, but sure. And to drink, I’ll have-"

        scene datewarfutaba23
        with dissolve

        q "Goat urine?!"
        s "What? No. That’s-"
        q "Sorry. All orders are non-refundable. Now, if you could please close your eyes, I can start preparing your meal."
        s "Why do you need me to close my eyes? What kind of cafe even is this? Why are there no signs? Why is the only employee I’ve encountered peddling piss? Why is-"
        q "Not everything has an answer, you know! And not everything has to! So it’s probably best to just never ask questions at all and accept everything you’re given!"
        q "And if it sounds like I’m saying that reluctantly, I’m not! Please! Just do what you’re told!"
        q "Now close your gosh darn eyes before I sew them shut."

        scene black
        with dissolve

        s "Fine. But only because-"
        f "Sensei?"

        scene datewarfutaba24
        with dissolve2

    s "Huh?"
    f "Were you up late? You just nodded off out of nowhere."
    f "I’m not boring you, am I? Because the main objective of today is for you to have fun and-"
    s "Oh, no. I’m fine."
    s "Probably just exhausted from all of the walking or something."

    scene datewarfutaba25
    with dissolve

    f "Well, I hate to be the bearer of bad news, but we’ve got a lot more walking to do after this."
    f "I’ve got you for another three hours before your date with Noriko begins, and I plan on using every second."

    scene black
    with dissolve2

    "The next two and a half hours go by without me ever falling asleep again."
    "We move all over the entertainment district, visiting a variety of locations Futaba handpicked to make sure I enjoy every minute of the date."
    "One of those locations was a love hotel- in which we had sex three times, costume and all. So it’s clear to see just how tailor-made this date was to fit my interests."

    scene datewarfutaba26
    with dissolve2

    "But now, we’ve got half an hour left before the date comes to a close and nothing to spend it on."
    "And with me being very bad when it comes to suggesting...well, anything, I go ahead and shoot off the only thing I can think of to pass the rest of that time."

    s "Love hotel round two?"
    f "Sure. But only if you’re okay with me being paralyzed for life as my lower body can not handle anymore of you."

    scene datewarfutaba27
    with dissolve

    s "Maybe not, then. Even if the rest of the date was great, I think ending it in a hospital would lead to {i}that{/i} being the only part of it I remember."
    f "Well...the only other idea I have is all about me. And I wouldn’t want to subject you to coming along with me to another bookstore when-"
    s "Sure. Let’s do that."

    scene datewarfutaba28
    with dissolve

    f "Sensei, you don’t have to humor me. I know you don’t normally have {i}fun{/i} in places like that. And having such an anticlimactic end to one of the best days in a long time would be-"
    s "Not anticlimactic at all. The idea of a date where only one person enjoys themselves is intrinsically flawed  when the whole idea of things like this is for {i}both{/i} people to have fun."
    s "So go ahead and lead me toward the books and I will do my best to not talk about how bored I will be."
    f "I mean...you kind of just did. But...if there’s really nothing else you can think of...I do remember where the store is located. And it’s not that far from here."
    f "But are you sure you’re okay with-"
    s "Stop trying to talk me out of this and just run to your precious books already."
    f "Sensei-"
    s "I’m serious. Go. Be free."
    f "No, I-"
    s "As free as the wind blows."

    scene datewarfutaba29
    with hpunch

    f "I’m trying to tell you I can’t run! You were too mean to my vagina and it’s taking all I have to even walk!"
    s "Oh."
    s "I get it now."

    scene datewarfutaba30
    with dissolve

    rando "Nice."
    s "I do what I can."
    f "Oh God...I forgot there were other people around..."
    rando "Hey, wait a second. How old is-"

    scene black
    with dissolve

    s "Futaba, run."
    f "I just told you I can’t!"

    "........."
    "......"
    "..."

    scene datewarfutaba31
    with dissolve2

    f "Hah...this is really not how I thought today was going to end. And after the rest of it went so well..."
    s "This place looks familiar."

    scene datewarfutaba32
    with dissolve

    f "It’s a new branch of that other bookstore I’ve dragged you to before. And if what I’ve heard is true, their romance section is twice as large."
    s "Just think of how many elves you’ll be able to fuck."

    scene datewarfutaba33
    with dissolve

    f "I bet an elf would be gentler with my body than you are."
    s "Wow. That was a low blow. I’m really self-conscious about how great I am at sex, you know. Finding a girl who can handle that is-"
    bg "You two need to leave."

    scene datewarfutaba34
    with dissolve
    stop music fadeout 15.0

    f "What?! But we haven’t even gotten to read more book yet! I have to read more book! More book is...wait, why is it spelled like that?"
    s "Let’s just go, Futaba. It’s clear we’re not needed here."

    scene black
    with dissolve2

    f "But...my elves!"
    bg "Hah...I should have just sold tacos like my cousin."

    "And so our date comes to an end with the two of us getting kicked out of a bookstore."
    "But not before stopping at one more love hotel and paralyzing Futaba for life."

    $ renpy.end_replay()
    $ dormwartwo5 = True
    $ futaba_love += 5

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo6

label dormwartwo6:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
scene gamerbattle28
    with dissolve2

    mo "This game has to be bugged. Fatally bugged. That’s why I’ve never heard of it before."
    mo "This is our fourth time trying and we still can’t figure out how to get these damn boards off of the windows. Who even designed this nonsense?"
    sa "We’ll get it soon...we just...have to keep trying..."
    sa "That’s the key to games like this..."
    sa "Sometimes you...have to...bash your head against the wall...over and over...until you find something different...something that...unlocks the rest of the pieces in the puzzle..."
    mo "Yeah, that just sounds like bad game design."
    sa "I think...it’s kind of fun...and...really rewarding...once you finally break the pattern and-"

    scene gamerbattle29
    with dissolve

    mo "Wait! That book in the top right corner of the shelf! The one that’s jutting out a little. Click on that. Our next clue could have something to do with-"

    scene gamerbattle30
    with dissolve

    sa "It...it fell down! And...there’s a key inside!"
    mo "A-ha! So it {i}is{/i} possible after all!"

    scene black
    with dissolve2

    mo "Try the key on that door in the back of the house, Sana. That’s the only one we haven’t tried yet."
    sa "It’s...no. It’s not doing anything..."
    mo "Tch...we’ll just have to try something else then."

    "Sana and Molly wind up playing their weird, unnamed arcade game for another thirty minutes- paying no attention to anything happening off of the screen they’ve glued their eyes to."
    "And while their “contest” manages to devolve into two friends playing the same game for fun instead of competition, there {i}is{/i} a winner as it winds up becoming more of a test of endurance than anything else."
    "And when it comes to endurance and the depressing act of refusing to detach yourself from the virtual world at any point, there is only one person that will ever come out on top..."

    scene gamerbattle31
    with dissolve

    sar "It’s okay, Sana. I can just not eat next week. You did your best."
    sa "I’m not upset...I...actually had a lot of fun..."
    mo "As did I, Sana. We should do this again under better circumstances...on a day where I am not destined to win. Though, I very likely will as I am just that good."
    h "Fuck yeah, Molly. All of that time being a horrible employee has finally earned me money in a really roundabout way!"
    h "This is the part where I feel like I’m supposed to say I’m proud of you but, seriously, I’m going to have to start taking your phone away when you clock in."
    s "Congratulations, Molly. I now understand why I had to be here for this."

    scene gamerbattle32
    with dissolve

    mo "To experience firsthand one more example of how great I am as the girl who may potentially be the {i}only{/i} undefeated Dorm Wars competitor by the end of tomorrow night?!"
    s "Sure. Let’s go with that."
    mo "Thank you, Sir! I’m glad that I was able to share this experience with you even if you had no idea what was happening at any point and were nearly killed by a dolphin."
    s "Yeah, the dolphin disappeared a little while ago and I’ve been on edge ever since, so...I’m just going to-"

    "A faint tapping on my shoulder reminds me of how fleeting life is."
    "So...if I turn around and come face to face with my demise, there’s something I want you to know."

    scene black
    with dissolve2

    "And that something is this:"
    "Being around dolphins is exhausting."
    "That is all."

    scene gamerbattle33
    with dissolve

    s "Oh. It’s just you."
    u "..."
    s "..."
    s "Right. You have to stay in character."
    s "I’m assuming that letter is for me?"
    u "Do not speak...You’ll give away our location...And it is finally gone..."
    s "..."
    u "..."
    s "I understand entirely. Give me the note."

    scene black
    with dissolve2

    "I snatch the card out of Uta’s hand and turn it over to find that my next “mission” is walking approximately half a mile away from the arcade- a thing I’m definitely excited to do in the midst of summer."
    "And while that may sound like a complaint (Because it {i}is{/i} one), I’m not {i}entirely{/i} distraught as it appears that this “mission” involves kicking off the date war right away."
    "Considering that this is likely going to take several hours, I nod to the rest of the girls and say my goodbyes."
    "Unfortunately, all of them know where I am headed due to the Dorm War schedule being public knowledge, so all that happens in saying goodbye is me managing to make everyone jealous before disappearing."
    "But hey, at least {i}one{/i} person is having a good day so far."

    $ renpy.end_replay()
    $ dormwartwo4 = True
    $ dorm2war2points += 1
    $ molly_love += 1
    $ sana_love += 1

    "{i}Molly MacCormack has defeated Sana Sakakibara!{/i}"
    "{i}First Floor: 0\nSecond Floor: 1{/i}"
    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    play sound "phonebeep.wav"
    "{i}You have received two new picture messages from Imani Imai and Miku Maruyama!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo5
...
```