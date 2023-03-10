# Third Wheel (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [A Woman's Heart](./saradate1.md) (Sara) is completed)



## Next events

* [Sara: A Mostly Empty Home](./sarainvite2.md)

## Event properties

* Id: sarainvite1
* Group: Sara
* Triggered by label: sarainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->sarainvite->sarainvite1

## Official wiki page

[Third Wheel](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sarainvite1&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarainvite1:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "I figure that the two of us know each other well enough at this point that it won’t really be weird for me to invite her over."
    "Sure, I don't really know what Ami will think about an older woman randomly showing up at the house, but I’m the one who’s paying the bills."
    "I’ll invite whoever I want over."
    "This is what it means to be an adult."

    if invitetip == False:
        call invitetip from _call_invitetip_2

    scene noonsky
    with dissolve
    play sound "phonebeep.wav"

    sar "Hellooo~ Sensei?"

    play music "normalday.mp3" fadein 10.0

    s "Hey. What are you doing tonight?"
    sar "Oh, you know. Just drinking half of my stock since no one else ever wants to show up."
    sar "Do you want to come over and keep me company?"
    s "Actually, I was wondering if {i}you{/i} wanted to come over for a change."
    sar "What, you mean like, to your place?"
    sar "Is that really okay?"
    s "Sure. I come to the bar all the time. I figure it’s about time for you to see where I live."
    sar "Oh my God! Yeah! Definitely!"
    sar "I-I’ll have Sana take over for me and I'll head right over."
    sar "I’m so excited. I was starting to think you were ashamed of me and didn’t want your [niece] knowing that we hang out and stuff."
    sar "Am I sleeping over? Do I need an overnight bag?"
    s "Hey, now. Slow down. "
    s "It’s one thing to invite you over, but I’m pretty sure Ami would kill both of us in the middle of the night if you stayed over your first time here."
    sar "Oooooh, right. Right. Okay!"
    sar "Can you send me the address? I’ll meet you over there as soon as I can."
    s "Sure thing. See you soon."

    play sound "phonebeep.wav"

    "I hang up the phone and quickly type out my address before sending it to Sara."
    "It will be her first time seeing the place and I’m pretty sure Ami will be around tonight."
    "All I can really hope is that the two of them manage to get along."

    scene black
    with dissolve

    "Sara, I’m obviously not worried about. "
    "She has a daughter, so she clearly knows (At least to some extent) how to deal with [young_girls]."
    "Ami, on the other hand..."
    "Well. I guess I’ll just have to wait and see."
    "………"
    "……"

    play sound "doorbell.mp3"
    "…"

    s "Come in."

    play sound "dooropen.mp3"

    "…"

    scene sarafirstinvite1
    with dissolve

    "I’m in the kitchen when Sara lets herself in."
    "She immediately comes to meet me at the counter and props herself up on it using her elbows."
    "She doesn’t say anything, just smiles at me and waits for me to talk."

    s "Uhh, welcome to my house, I guess."
    sar "Thank you so much for having me."
    sar "What are you making me for dinner?"
    s "...I'm sorry. What?"
    sar "You {i}are{/i} making me dinner, aren't you?"
    s "I...didn’t plan on it?"

    scene sarafirstinvite2
    with dissolve

    sar "You invited a girl over and aren’t going to make her dinner? I thought your manners were better than this."
    s "Trust me, you wouldn’t want me making you dinner in the first place. I can barely cook an egg."

    scene sarafirstinvite3
    with dissolve

    sar "It looks like the two of us would have to order out quite often if we ever moved in together."
    s "A - It’s way too early to be talking about moving in together."
    s "B - You can’t cook either?"

    scene sarafirstinvite4
    with dissolve

    sar "I can use a microwave pretty well."
    sar "Sana ate nothing but chicken nuggets until she was seven, so I’ve memorized the cooking times for like twenty different brands."
    s "I don’t know whether to be impressed or abhorred that you would allow your child to live off of nothing but microwaved chicken nuggets for so long."

    scene sarafirstinvite3
    with dissolve

    sar "Hey, she turned out okay, didn’t she?"
    sar "I have the cutest daughter in all of Kumon-mi. And she’s somehow still super tiny despite her diet."
    s "Well that’s obviously genetic. You’re pretty small yourself."

    if bonus == True:
        sar "I’m fun-size. Easier to lift up and have your way with."
        s "Are you already trying to seduce me? You’ve been here for five minutes."

        scene sarafirstinvite5
        with dissolve

        sar "Worried your [niece] will come home and catch us?"
        s "Kind of, yeah. She’ll be home any minute."
    else:
        s "Just like my accountant."

    scene sarafirstinvite6
    with dissolve

    sar "Oh, how is she going to feel about this, by the way?"
    sar "Won’t it be a little weird for her to come home and see you talking to some woman she’s never met before?"
    sar "I’m sure you at least warned her in advance, right?"
    s "Nahh. Ami is mature enough to handle being thrown into the fire every now and then."
    s "She’ll probably freeze at first, but I’m sure she’ll warm up to you in no time at all."

    scene sarafirstinvite7
    with dissolve

    sar "You really think so?"
    sar "Maybe I’ll have a second daughter before I know it?..."
    s "That...is not what I meant."

    play sound "lock.mp3"
    scene sarafirstinvite8
    with dissolve

    a "I’m home!"

    "The sound of the door unlocking quickly breaks up our conversation as we fix our eyes on the door."
    "The moment of truth approaches."

    sar "Oh God. That’s her, right? Do I look okay?"
    s "Why are you more focused on impressing my [niece] than me?"

    if bonus == True:
        sar "I already know you like me. I need to make her like me next and I’ll be basically guaranteed a spot in this family."
        s "Sara, that isn’t how families work."
    else:
        sar "I already know you like me. I need to make her like me next and I’ll be basically guaranteed a spot at her accounting firm."
        sar "You know, since the whole bar thing obviously isn't working out."

    play sound "dooropen.mp3"
    scene sarafirstinvite9
    with dissolve

    a "…"
    s "…"
    sar "…"
    a "…"
    s "Welcome home."
    sar "Hi! You must be Ami. Your [uncle]’s said so much about you."

    "No, I don’t think I have."

    a "…"
    s "How was[school]?"
    a "…"
    sar "…"
    a "I think I might have opened a door to the wrong dimension."
    a "I’m going to leave and come back in and I’m sure everything will go back to normal."

    play sound "dooropen.mp3"
    scene sarafirstinvite10
    with dissolve

    sar "That...didn’t go as I expected it to."
    s "It went exactly as I expected it to."

    a "I...I’m home!"

    play sound "dooropen.mp3"

    scene sarafirstinvite11
    with dissolve

    a "…"
    a "It...it's still here..."
    s "{i}It?{/i}"
    sar "Hi again~"
    s "Welcome home."
    a "What...what’s going on?"
    a "Why is there...a woman...in our house?..."
    s "I invited her over. She’s a friend of mine."

    scene sarafirstinvite12
    with dissolve

    sar "It’s nice to finally meet you, Ami! You’re very pretty."
    a "...Thank you."
    s "Good. Keep saying things like that. She loves compliments."

    if bonus == True:
        sar "You take care of your [uncle] too, don’t you? That’s very impressive for a girl your age."
    else:
        sar "You take care of your [uncle] too, don’t you? Accountants are really useful nowadays, aren't they?"

    sar "I wish my daughter would take care of me more."
    a "D...Daughter?..."
    s "Oh, right. This is Sana’s mom."

    scene sarafirstinvite13
    with dissolve

    a "S-Sana’s mom?!"
    a "Why is Sana’s mom in our kitchen?!"
    a "Is Sana here too?!"
    a "How many girls are you hiding from me?!"
    s "I’m not hiding any. Sana’s mom, {i}Sara{/i}, is right in front of you."
    sar "I hope I’m not intruding or anything."
    a "You are! Get out of my house!"

    scene sarafirstinvite14
    with dissolve

    sar "Wow...I had a feeling you two were close but I didn’t realize you were {i}this{/i} close."
    sar "It’s like she’s afraid of women."
    a "S...Sensei...what is this?..."
    sar "She even calls you Sensei?"
    sar "You haven’t brainwashed her, have you?"

    scene sarafirstinvite15
    with dissolve

    a "I...I’m not brainwashed! I just don’t want anyone stealing my [uncle] away from me!"
    sar "Aww...You really love him, don’t you?"

    if amifingered == True and bonus == True:
        "I think {i}love{/i} is a bit of an understatement, personally..."

    a "O-Of course I do! He’s my [uncle]! He’s all I have!"
    sar "Don’t worry, dear. I won’t steal him from you."
    sar "The two of us were just chatting and he wanted me to meet you."
    sar "In fact, when he invited me over, he specifically said, “I need to prove to you that my [niece] is the cutest girl in all of Kumon-mi.”"
    sar "Now, being the mother of a cute girl, I couldn’t help but dispute it. But now that I’ve seen you in person..."
    sar "I...I think I might have to agree."

    "In an incredibly risky and rather impressive move, Sara swoops in for the kill and appeals to Ami’s weakest point- validation."

    scene sarafirstinvite16
    with dissolve

    a "You..."
    a "You don’t mean that..."
    sar "No, no. I really do."
    a "...Well, thank you."
    a "But...you won’t say anything to Sana...right?..."
    a "I wouldn’t want her to feel bad..."
    a "She’s...really cute too..."
    sar "Of course not. I’ll keep my opinion to myself for the rest of eternity."
    sar "I just hope you can find it in your heart to forgive me for showing up unannounced..."

    scene sarafirstinvite17
    with dissolve

    a "Well...I guess it’s okay as long as I can supervise you two..."
    s "What? Why do we need a supervisor? We’re adults."

    scene sarafirstinvite18
    with dissolve

    a "I’m not a kid, you know! I’m old enough to know what two consenting adults do when they’re alone together!"
    sar "Unfortunately for me, I can’t imagine your [uncle] would ever consent to doing anything when his heart has already been taken by you."

    if bonus == True:
        "Okay. This is no longer risky. It’s reckless."
        "This is a dangerous can of worms you’re opening, Sara."

    scene sarafirstinvite19
    with dissolve

    a "S...Sensei..."
    a "You’d really...choose me over...someone as pretty as her?..."

    scene sarafirstinvite20
    with dissolve

    sar "{i}Did I do well? I did well, right?{/i}"
    s "…"

    scene black
    with dissolve

    "I sigh to myself and take a seat at the dining room table."
    "Sara follows suit and, after taking a minute to collect herself, Ami does as well..."

    scene sarafirstinvite21
    with dissolve

    sar "Thanks for not kicking me out, Ami. I really hope the two of us can get along."
    a "Um...this still feels a little weird for me..."
    a "It’s not exactly...common for someone Sensei’s age to join us at the dinner table."
    a "Especially when there is no dinner..."
    sar "I take it you do all of the cooking around here?"
    sar "I thought Sensei was going to cook dinner for us tonight. I was totally surprised when I found out he wasn’t."

    scene sarafirstinvite22
    with dissolve

    a "Sensei? My Sensei? Cooking dinner?"
    a "Never in a billion years. He needs me."
    s "I want to be offended by that but it’s really hard when it’s 100%% true."
    sar "Now...I don’t mean to impose, but maybe one day you and I could make dinner together, Ami?"
    s "Wait...but I thought you said you couldn’t-"

    scene sarafirstinvite23
    with dissolve

    a "T-Together?..."
    a "But...what about Sana? Shouldn’t you be making dinner with her instead?"
    s "Am I just being ignored now?"

    if bonus == True:
        "Sara seems to be taking this family-infiltration mission seriously. She’s not even acknowledging me anymore."
    else:
        "Sara seems to be taking this firm-infiltration mission seriously. She’s not even acknowledging me anymore."

    "And she’s almost completely won over Ami."
    "What is happening right now?"

    sar "What if Sana comes over as well?"
    sar "In fact, what if we leave Sensei out of it entirely and have a little girls’ night in? That sounds fun, doesn’t it?"
    sar "The blonde one can come too. Ayane, I think?"

    scene sarafirstinvite24
    with dissolve

    a "R-Really?! Just us girls?!"
    sar "Of course! No boys allowed."
    a "That means...I won’t have to worry about anyone stealing Sensei!"

    "Is Ami unaware that there are girls in other locations? One of them could easily {i}steal{/i} me if she’s not looking."

    a "Yes! Yes! I want to do that!"
    a "What was your name again?"
    a "I wasn’t paying attention the first time I heard it because I already decided I hated you. But I’ve changed my mind!"

    scene sarafirstinvite25
    with dissolve

    sar "It’s...Sara. Hahaha..."
    a "Sara...Sara...Okay. That’s easy to remember."
    a "I promise not to tell Sana that you think I’m cuter than her. That’ll be a secret between you and me."
    sar "Thanks. I really appreciate that..."

    scene black
    with dissolve

    "The two of them carry on their conversation and ignore me all the way until night falls."
    "I knew inviting Sara over would spark up some sort of confrontation with Ami, but I had no idea it would mean essentially locking me out of every discussion for the rest of the day."
    "But oh well."
    "I guess this just means it will be easier to invite Sara over in the future."
    "…"
    "Sara winds up calling a cab to drive her home once it gets dark out."
    "I offer to walk her back myself but she shrugs it off when she wants to stay on good terms with my [niece]."
    "It’s strange, though."
    "Even though the two of us didn’t get to spend much time actually {i}talking{/i} to one another, I still feel like I know Sara a lot better than I did before..."

    $ renpy.end_replay()
    $ sara_love += 3
    $ sarainvite1 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sarainvite2:
...
```

## Code that triggers this event

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarainvite:
    if sarainvite1 == False:
        jump sarainvite1
...
```