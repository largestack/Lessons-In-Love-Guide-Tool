# The Other Half
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinlust202&go=Go)


Part of event chain [Fear of Missing Out](./christmastwo9.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: kirinlust202
* Group: Kirin
* Triggered by label: christmastwo9

## Event code
File: \game\KirinEvents.rpy
Code:
```python
...
label kirinlust202:
    scene kirinxmanhall1
    with dissolve2
    play music "justlights.mp3"

    "The sound of the party does not relent even a bit despite how far away Kirin and I move from it."
    "I’m still not sure where she’s taking me but, knowing her, I imagine it’ll be somewhere quieter."
    "For someone with an alleged fear of missing out, she sure does isolate herself a lot."
    "Whether that’s intentional or not, I don’t know."
    "But it’s a part of her that, like many others, I’ll have to accept even when I don’t completely understand the rationale."
    "If there even is any rationale, that is."
    "I know {i}I’ve{/i} been known to do things I don’t fully understand from time to time."
    "But I can take solace in the fact that, at least so far, Kirin has not been on the receiving end of any of them."
    "And that’s in contrast to the irrefutable fact that she’d just convince herself she wanted it if any of that ever {i}did{/i} happen."
    "I’ll never understand her, but that’s okay."
    "Because she’ll never understand herself."

    if bonus == True:
        "Or at least not until she starts doing a little growing up in a way that doesn’t include having meaningless, casual sex with an older man."

        ki "So, wanna go have meaningless casual sex in the boiler room?"
    else:
        "Or at least not until she starts doing a little growing up."

        ki "Boy am I glad I never have to grow up."

    "See what I mean? Eternal youth."

    if bonus == False:
        ki "Let's go hug somewhere really dark and damp."

    s "Are you sure that’s what you really want right now?"

    scene kirinxmanhall2
    with dissolve

    ki "As opposed to what? Holding your hand and crying into your shoulder because some girl I don’t give two shits about said something mildly hurtful to me?"
    s "You seemed a little more than “mildly hurt” a few minutes ago."
    ki "I’m just a good actor, that’s all. "
    s "That would certainly be a convenient excuse."
    ki "It’s no {i}excuse.{/i} It’s true. "
    ki "I just don’t really see the need to act anymore in general."
    ki "If people want to look down on me, they can. It’s not like I think I’m some kind of angel or anything."

    scene kirinxmanhall3
    with dissolve

    ki "That’s why I wear these earrings, you know? Irony."
    s "You know, I kind of forget that Cupid is even an angel sometimes. In my head, he’s just some half naked baby who sunk an arrow into every single girl in class the moment I showed up."

    scene kirinxmanhall4
    with dissolve

    ki "Well, if he didn’t do it, I would have wound up just shooting myself eventually."
    ki "In the good way, of course. Not the super depressing way. Even if that might be the only thing I can imagine making an impact on my parents from time to time."
    s "The whole “holding hands and crying” thing is beginning to sound like a much stronger possibility the further we get down this hallway."
    ki "Sorry, but that’s getting a little closer to the line I already promised Noriko I wouldn’t cross."
    s "I didn’t realize promises actually meant anything to you."
    ki "They don’t."
    s "Then why-"
    ki "Because that’s just how it is, okay?"
    ki "Stop trying to figure me out and just be with me when I want you to be with me."

    if bonus == True:
        ki "You swallow up all of my angst and fury, and I’ll swallow up all of your cum in dark rooms where no one can find us. "
        ki "It’s just one more trade in a relationship completely built out of them."
        s "It doesn’t have to be, though."
    else:
        s "{size=-20}I just don’t want you missing out on more than, well, you’ve already missed.{/size}"

    scene kirinxmanhall5
    with dissolve

    ki "Uhh...what was that?"
    s "I just don’t want you missing out on more than, well, you’ve already missed."
    ki "But...I’m not missing out on anything. I’m getting exactly what I want out of you, and I’m {i}pretty{/i} sure you’re getting exactly what you want out of me."
    s "I am."

    if bonus == True:
        s "I can’t imagine I’ll ever love you. And having meaningless sex with you in...boiler rooms or whatever sounds like a great deal when all I have to do is absorb some of your feelings from time to time."

    scene kirinxmanhall6
    with dissolve

    s "But you’re allowed to want more."
    s "And if you think you’re just settling for what you deserve all the time, just...{i}take{/i} more."
    s "Stop manufacturing situations where everything goes wrong all the time and obviously a few more things will start to go right."
    ki "..."
    s "We’ve all got our reasons and whatnot. Yours just annoy me because there’s no drive to...grow."
    ki "Grow into what, exactly?"
    s "I don’t know. Something a little more valuable."
    s "Cry into my shoulder if you want. We’re going to be alone, aren’t we?"
    s "No one will ever know it happened."
    ki "You will, though."

    scene kirinxmanhall7
    with dissolve

    s "So what?"
    ki "I don’t know. I just don’t want to cry in front of you for some reason. There’s no double meaning to it."
    s "I’ve spent enough time with you to know that there is always a double meaning, Kirin."
    ki "And I’ve spent enough time with you to know that you don’t care about that."
    s "You-"
    ki "You can keep telling yourself I’m some sort of...temperamental brat who’s just forcing herself to be the antithesis of everything she admires in the real world-"
    ki "But that’s only, like...half true."
    s "What’s the other half then? "
    ki "H-"
    s "And don’t say hormones."

    scene kirinxmanhall8
    with dissolve

    ki "...ow are you doing today?"
    s "..."

    scene kirinxmanhall9
    with dissolve

    ki "Hah..."
    ki "Will you think I’m broody if I say there {i}is{/i} no other half?"
    s "Kind of, yeah."
    ki "Well, I’m saying it."
    ki "And since there’s nothing I can really do to fill that void myself, I’ll keep trying out things other people have in hopes that {i}something{/i} will slide into place."
    ki "Just like a puzzle piece."
    s "I feel like we’ve been here before."
    ki "So do I."
    ki "Just in a different sort of way."

    scene black
    with dissolve2

    if kirin_lust >= 20 and bonus == True:
        jump kirinlust202scenex
    elif kirin_lust >= 20 and bonus == False:
        "Kirin and I make our way into a boiler room, but standing in the center is famous Jewish comedian Jerry Seinfeld."

        seinfeld "What's the deal with airline food?"
        ki "Merry Christmas, Sensei."
        s "Kirin why"
        ki "One day, you will understand."
        s "Nooooooooooooooooooooooooooooo!"

        "Jerry Seinfeld tells what I think are supposed to be jokes for a little while before falling through a grate in the floor and disappearing forever."
        "Kirin is very upset about this but I don't really care."

        $ renpy.end_replay()
        $ kirin_lust += 1
        $ kirinlust202 = True
        stop music fadeout 6.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo10

    else:
        "Kirin and I make our way into a boiler room that she had come across while navigating the halls by herself earlier."
        "She tells me that Noriko wasn’t able to come because she had to help out at her parent’s restaurant or something like that, but that she’s still dropping by to give me a present later."
        "Her voice cracks a little while telling me this- and I can’t figure out whether there’s any meaning to it or not."
        "I’ll just assume there isn’t-"
        "Because that’s what she’d want me to do in the first place."

        $ renpy.end_replay()
        $ kirin_love += 1
        $ kirinlust202skip = True
        stop music fadeout 5.0

        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
        "........."
        "......"
        "..."

        jump christmastwo10

label kirinlust30intro:
    scene thevaliumscene1
    with dissolve2

    ki "How are you feeling?"
    mi "You ever just think about phones?"
    ki "Well, I guess that answers that question."
    mi "No, seriously. I can just, like...press this glass in the right spots and then suddenly know more about bees. "
    mi "Who comes up with this stuff?"
    ki "I can’t tell if you’re so overtired that you’re acting high or if you’re just...you know, literally high."

    scene thevaliumscene2
    with dissolve

    mi "I wanna take a nap."
    mi "I can barely even remember what happened during the costume thing."

    scene thevaliumscene3
    with dissolve

    ki "Yeah. Well, Io did say that short term memory loss can be a side effect. But hey, at least you’re not puking your brains out all over the carpet."
    mi "Where’d Sensei go? I wanna talk to him again now that I don’t have to keep sayin’ all those weird buzzwords anymore. "
    ki "He followed a dolphin outside last I saw."
    mi "A dolphin? Maybe I really am high."
    ki "I’m sure he’ll be back soon. It’s not like him to stay away from an entire room full of girls trying to get into his pants."
    mi "I ain’t been followin’ the tally, but I hope my team wins...I miss the good old days when there were only ten of us fightin’ over Sensei’s pants."

    scene thevaliumscene4
    with dissolve

    ki "Are you officially a part of that fight now?"
    mi "Dunno what you’re talkin’ about."
    ki "I’m asking if you have feelings for him or not. Like, real feelings. Not just pubescent curiosities."
    mi "Pubescial what now?"
    ki "When you see him...how does it make your heart feel? Is it like when you’re playing soccer? Watching a horror movie? Or is it more like...I don’t know. When you’re watching porn or something?"
    mi "Maki says I can’t watch that stuff."
    mi "But if I had to compare it to somethin’..."

    scene thevaliumscene5
    with dissolve

    mi "I’d say it’s closest to wakin’ up from a really nice dream."
    mi "Ain’t so much racin’ as it is feelin’ comfortable. "
    mi "All's I know is that I ain’t ever felt this way ‘bout anyone before. And that I get now why Makoto’s liked him for so long."
    ki "..."
    mi "..."
    ki "Do you think I’ll ever feel that way about someone?"
    ki "That sounds nice...comfort, I mean. Being able to just be with somebody without being tempted to {i}do things{/i} with that person."
    mi "..."
    ki "I don’t know. Maybe I really am just a thirsty bitch at the end of the day. But I can’t help but feel a little jealous when other people know what they want."
    mi "..."
    ki "..."

    scene thevaliumscene6
    with dissolve

    ki "Hey. Wake up."
    mi "Huh? Were you sayin’ somethin’ just now?"
    ki "..."
    mi "..."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        scene thevaliumscene7
        with dissolve

        ki "When Sensei {i}does{/i} come back..."
        ki "Maybe we should see if he wants to hang out with just {i}us{/i} instead of the rest of the girls? "
        ki "That way...you’d get what you want in finally getting to spend time with him..."
        ki "And I could..."
        ki "I could keep an eye on you...and make sure you don’t pass out or anything."
        mi "I think that sounds nice. But Sensei’s not gonna wanna be with me when we’ve got people like Futaba walkin’ around with her bodonhonkaroos takin’ up half the room."

        scene thevaliumscene8
        with dissolve

        ki "He chose you over Uta, you know. And Uta’s got some pretty nice bodonhonakroos for a girl of her size. "
        mi "Don’t remind me."
        ki "All I’m saying is...if this is the last night you get to be {i}that{/i} version of yourself, why not play it up instead of retreating back to your comfort zone?"
        ki "Sensei clearly likes this Miku. Why take her away?"
        mi "Cause at this point, I don’t know if {i}any{/i} Miku is going to be able to stay awake."

        scene thevaliumscene9
        with dissolve

        ki "Then we’ve just gotta do something fun!"
        ki "You snapped out of it for a second when you won the contest, didn’t you?"
        mi "Did I? I don’t remember."
        ki "You did. Which tells me that, in order to stay awake, you just need a little {i}more{/i} stuff to excite you! And what better way of getting that blood pumping than relying on your new crush?"
        mi "You think he’ll carry me? Cause I ain’t sure if I can walk if we’re goin’ anywhere."
        ki "Oh, yes. I’m quite sure he’d be happy to carry you."
        mi "Then sign me the heck up, Kirin."
        ki "I will. Don’t you worry."
        ki "In fact, don’t worry about anything at all if you’re not feeling up to it. Save that energy for later and leave all of the talking to me. I’ll make sure he comes along."
        mi "Think you can handle it? Sensei ain’t that easy to convince."
        ki "That just tells me you don’t know {i}how{/i} to convince him yet."

        scene black
        with dissolve2

        ki "But again, don’t worry."
        ki "I’ll teach you."

        "........."
        "......"
        "..."

    else:
        scene thevaliumscene10
        with dissolve

        ki "Hah...This is what I get for opening myself up for a second."
        mi "Kirin, you’ve been open for business since the day I met you."
        ki "Not like that, Miku."

        scene black
        with dissolve2

        ki "Let’s just hurry up and get you back to the hotel before anyone realizes that you’re drugged up."
        mi "Kaaaay...I’m gonna sleep like a rock, so I’m trustin’ you to not do anythin’ weird to me."
        ki "Does taking your makeup off count as weird? Because I wouldn’t be able to live with myself if I let you fall asleep with all of that on."
        mi "Just don’t touch my ears. I’m weak there."
        ki "Well, now I {i}have{/i} to..."

        "........."
        "......"
        "..."

    "I make my way back into the bar after miraculously avoiding what was sure to be my hardest decision of the weekend."
    "This means that, fortunately no one had their heart broken or felt betrayed by me tonight."
    "This also means that, unfortunately, my chances of getting laid on Christmas have greatly decreased."
    "But if there is anything I know about my likelihood of getting laid, it is that it’s never 0%%."
    "And that’s good enough for me."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        scene thevaliumscene11
        with dissolve2

        ki "Hey. What are you doing right now?"
        s "I was-"
        ki "Wrong. You’re hanging out with us."
        s "Okay, I guess I’m hanging out with you. But let it be known that the others are going to approach me and take me away after another few lines of dialogue because that’s just how it works."
        ki "Then we’ve just gotta beat them to the punch and get out of here before they have a chance to do that."
        s "Out of here?"

        scene thevaliumscene12
        with dissolve

        ki "Yeah. Miku and I were just talking about how sad we are that we haven’t gotten to spend much time with you this weekend. "
        mi "We were?"
        ki "{i}Yup.{/i} And we thought that maybe the three of us could head back to the hotel early and have a little fun together."

        scene thevaliumscene13
        with dissolve

        ki "What that means, only time will tell!"
        ki "You do like having {i}fun...{/i}don’t you, Sensei?"
        s "Uhh..."
        ki "...Sensei?"
        s "Are you on board with this, Miku?"
        mi "Teach, please. I’m on board with like, literally whatevs. If bestie says let’s go have fun, Miku’s gonna go have fun."
        s "You realize the contest is over right? You don’t have to stay in character anymore."

        scene thevaliumscene14
        with dissolve

        ki "She loves this character! Right, Miku?"
        mi "Huh? Oh. Oh, yeah. It’s great. I love not understanding what I’m saying."

        scene thevaliumscene11
        with dissolve

        ki "See? She’s all about it."
        s "Kirin-"
        ki "Sensei, come on! Before I change my mind! Who knows how many lines of dialogue we have left?!"
        mi "Sensei, can you carry me?"
        s "Carry you? Why would-"
        ki "Contest reward! A little bonus since Miku floored you with her amazing costume and above-average roleplaying skills."
        mi "I also can’t feel my legs."
        ki "Gyaru really do say some {i}crazy{/i} things now, huh?"
        s "This seems a little sketchy to me."
        ki "That’s just because you’re still in work mode! Come relax with us! This top is so tight that it's cutting off my circulation anyway. And I’m sure Miku feels the same way about her fishnets."
        mi "Yeah. And they ain’t even caught any fish."

    else:
        scene thevaliumscene15
        with dissolve

        ki "Hey. How much do you love me?"
        s "Zero."
        ki "Good. But how much do you love Miku?"
        s "I don’t know. Slightly more than zero?"
        ki "Great, because we need your help with something."
        s "I am assuming it’s something that’s going to take me away from the party?"
        ki "And you would be correct in assuming that, yes. "
        s "Yeah. That’s how most parties seem to end for me nowadays."
        s "What is it? What do you need help with?"
        ki "Io gave Miku a Valium and now Miku is about to pass out. "
        s "This sounds like a job for Makoto. "
        ki "Sensei, come on. Do you really want to bother Makoto with this after all she’s been through lately? I can handle it."
        ki "I just need your help carrying her back to the hotel. Or at least the Uber that will take us to the hotel. But you know what I mean."
        s "Wait, why did Miku take some of Io’s medication in the first place?"
        mi "I can’t remember. But I’m sure glad I did. "
        mi "You ever just think of phones before, Sensei?"
        s "Why did you let this happen?"
        ki "Doesn’t matter. Are you in or not?"
        s "..."
        ki "..."
        mi "Phones are like...they put all of the knowledge in the world inside a little box that you have to put {i}another{/i} little box on top of to protect it."
        s "Yeah, I should probably help."

    scene thevaliumscene16
    with fade

    ki "Okay then! On that note, let’s go wait outside. It’s way too stuffy in here and I need some fresh air anyway."
    s "I should probably at least say bye to-"
    ki "And risk getting stopped? No way. We have to do this now."
    s "I really don’t think another two minutes will-"
    mi "Ugh...pathetic. Aren’t you supposed to be a {i}man?{/i} Why don’t you just act like one?"
    s "By submitting to everything Kirin wants from me?"
    mi "Obvs by escorting these...two lovely ladies back to the hotel, loser. I can’t believe I had to spell it out for you. Hilarious."
    ki "So? Are we good? Can we go?"
    s "Yeah...fine. Whatever. Just lead the way."

    scene thevaliumscene17
    with dissolve

    ki "{i}Thank you, Sensei! You’re so- Miku, watch your foot. There’s a drop- okay. You’re on the ground now.{/i}"
    mi "{i}Ugh...can you believe the construction around here? It’s like...so outdated. {/i}"
    mak "..."
    f "..."

    scene thevaliumscene18
    with dissolve

    futamak "Hah..."

    scene thevaliumscene19
    with dissolve

    mak "Ah..."
    f "..."

    scene thevaliumscene20
    with dissolve

    mak "..."
    f "..."
    mak "You too?"
    f "Yeah..."
    mak "I see..."
    f "..."
    mak "..."
    f "Maybe...nothing will happen?..."
    mak "Yeah..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    mak "And maybe the sky will fall."

    if kirin_lust >= 30 and miku_lust >= 10 and mikucostumewin == True:
        jump kirinlust30
    else:
        "Nothing else happens when we return to the hotel."
        "But something almost does."
        "Instead of rushing Miku back to the girls’ room to make sure she gets her rest, Kirin suggests that we all go hang out in mine for a little while instead."
        "And for some reason, I don’t decline."
        "But halfway there, she changes her mind."
        "It doesn’t make me feel any better about myself."
        "But it {i}does{/i} make me feel better."
        "I collapse onto the bed and hide myself beneath the covers."
        "Before the darkness whisks me away, though..."
        "I think about what could have been."
        "And mourn the idea of any body but mine beneath these covers as well."
        "Sleep comes shortly after I do."
        "You’ll never guess who I thought of."

        $ renpy.end_replay()
        $ kirinlust30skip = True

        jump dormwartwo19

label kirinlust30:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
s "Well, you can’t say I didn’t try."

    ima "That girl’s gonna cause some problems for us, isn’t she?"
    mak "No...She’s normally fine in school. I just pushed her a little too far."
    no "And, on that note, I need another glass of wine. But when I return...more genomics."

    scene black
    with dissolve2

    "Kirin waits for me near the door and the two of us walk out together."
    "I can feel the irritation essentially pouring out of her, so I really do hope that wherever the two of us wind up going is somewhere that can kind of...absorb it, I guess."

    if bonus == True:
        "Or maybe I can just fuck it out of her. "
        "That sounds like a better idea."

    "........."
    "......"
    "..."

    if karinlied == True:
        scene imaniandgirls30
        with dissolve2

        ka "..."
        ka "..."
        ka "..."

        scene imaniandgirls31
        with dissolve

        ay "Okay! I managed to pry the microphone out of Ami’s hands {i}and{/i} got a second one just for you."
        ay "I hope you’re good at Spanish, cause-"
        ka "Did you see that just now?"

        scene imaniandgirls32
        with dissolve

        ay "See what? What’s wrong?"
        ka "Sensei and...my sister. Walking out together. Where do you think they’re going?"

        if ayanelust15 == False:
            ay "Sensei and Kirin? I don’t know. Maybe they’re just taking a walk or something?"
            ka "A walk..."
            ay "Do you...want to follow them or something? I can just give these back, you know. Despacito is forever, so we can sing whenever we want."
            ka "I..."
            ka "..."

            scene imaniandgirls33
            with dissolve

            ka "No..."
            ka "No. I’m probably just being weird. I’m sure it’s nothing."
            ka "Yeah. I’m definitely weird."
            ay "..."
            ka "..."

            scene imaniandgirls34
            with dissolve

            ka "Wait...Spanish?"

        else:
            scene imaniandgirls35
            with dissolve

            ay "Sensei and...Kirin?..."
            ka "Yeah..."
            ka "They just...left."
            ka "They walked right past me..."
            ka "Isn’t that kind of weird?..."
            ay "..."

            scene imaniandgirls36
            with dissolve

            ka "Ayane?"
            ay "Let’s just..."
            ay "Sing..."

    scene black
    with dissolve2
    stop music fadeout 10

    $ renpy.end_replay()
    $ christmastwo9 = True
    $ kirin_love += 1
    $ imani_love += 1
    $ nodoka_love += 1
    $ makoto_love += 1

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    jump kirinlust202
...
```