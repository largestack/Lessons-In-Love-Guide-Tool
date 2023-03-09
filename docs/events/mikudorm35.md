# Triple Whammy
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm35&go=Go)



## Event preconditions
✅Miku love greater than or equal to 35

✅Event "[Makoto: Something, Somewhere](./makotowinterbeach4.md)" is completed (event=makotowinterbeach4)

✅Day of week is not Thursday



## Next events
* [Miku: Speed of Light](./mikudorm40.md)

## Event properties
* ID: mikudorm35
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label mikudorm35:
    play sound "knock.mp3"
    stop music fadeout 30.0

    "I knock on Miku’s door and wait for her to answer, though I wouldn’t be surprised if she decides not to tonight."
    "The two of us haven’t really spent much time together ever since the...occurrence at the beach house, and I’m sure she’s feeling a little strange about it."
    "I know I would be in her position."

    if bonus == True:
        "Thankfully, I’ve never had the misfortune of being in the position {i}of{/i} a [teenage]girl and have much more experience either on top of or beneath them."

    "But I digress."
    "The volume of Miku's TV inside of the room is turned down, the same way it has been several times before when I’ve visited this place."
    "So, the chances are she’s either about to invite me in-"
    "Or peer through the door, see that it’s me, and then pretend to be asleep."

    play sound "knock.mp3"

    "I knock again to let her know I’m onto her."

    mi "Y-Yeah?"

    "She bites immediately."

    s "Hey. Are you free tonight?"
    mi "Um...yeah."
    mi "You wanna like...go out for a walk or somethin’?"
    s "I think I’d prefer to hang out in there."
    mi "You sure? It’s...supposed to be really nice out right now!"
    s "It’s freezing. I was literally just outside."
    mi "Yeah yeah but like, what if it...isn’t anymore?!"
    s "…"
    s "Just let me in, Miku."
    mi "Gaaaaah...fine! But only cause I feel bad for makin’ ya wait out in the hallway and stuff..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene mikupostbeach1
    with dissolve
    play music "behindabathroom.mp3"

    mi "Uhh..."
    mi "So...how about that weather?"
    s "Is that just going to be your go-to topic for avoiding awkward conversation tonight or are you suddenly interested in becoming a meteorologist?"
    mi "The heck do meteors have to do with the weather?"
    s "That’s-"
    s "Actually, never mind."
    s "Is there something you want to talk about?"
    mi "Well since we’re already on the topic of meteors-"
    s "Miku."

    scene mikupostbeach2
    with dissolve

    mi "Do we really have to talk about the thing that happened or can we just kinda...pretend it never did?"

    if bonus == False:
        "This must be about that one hug we had."

    s "Pretending it never happened means there will be less of a chance for it to happen again, so I’d like to avoid that if at all possible."
    mi "That’s...kinda why I think we {i}should{/i} avoid it. I can’t be thinkin’ about that kinda stuff with you, Sensei."
    s "Why not?"

    scene mikupostbeach3
    with dissolve

    mi "Cause you’re my friggin’ teacher, my soccer coach, and the guy my best friend obviously has the hots for!"
    mi "That’s a triple whammy, Sensei! I’ve gotta put myself on the bench for this one!"

    if bonus == True:
        s "Just take a seat on my lap instead. You’ve proven on two occasions now that you like it there."
    else:
        s "Are we allowed to hug on that bench?"

    scene mikupostbeach4
    with dissolve

    mi "Come on..."
    mi "I know I don’t act serious all that often cause like...I’m not good at actin’ like that...but I’m really trying right now."

    if bonus == True:
        mi "There are some things you just shouldn’t do and I’m pretty sure that bumpin’ uglies with a triple whammy is one of ‘em."
        mi "And I already have a hard enough time with feelin’ all weird around you, so hearin’ stuff about sittin’ on your lap makes it like a billion times harder."
    else:
        mi "And I already have a hard enough time with feelin’ all weird around you."

    s "You feel weird because you like me, Miku."

    scene mikupostbeach5
    with dissolve

    mi "Well, yeah! That much should be obvious after the beach!"
    mi "And even before that! "

    if bonus == True:
        mi "I started feelin’ that way about you a while ago...but it’s not like I ever saw myself hidin’ under the covers with you!"
        mi "I didn’t even know you were gonna be sleepin’ in that bed! The heck were ya thinkin’ gettin' all up in my space like that?!"
        s "That was actually Makoto’s idea, so we can probably just blame her for this entire ordeal."
        mi "Why the heck would Makoto let ya sleep next to me?!"
        s "Because I promised to keep my hands to myself."
        s "Which I actually did until...you know."

        scene mikupostbeach6
        with dissolve

        mi "Aaaahhhh! Whose idea was it to invent hormones anyway?! They just make everythin’ harder!"
        s "I don’t know how many times you want me to say it, but I really don’t mind doing things like that with you."

        scene mikupostbeach7
        with dissolve

        mi "Well yeah. Ya made that pretty obvious the first time you started puttin’ your hands where they don’t belong."
        mi "But I already told you, the two of us can’t do stuff like that."
        s "Sure we can. Especially since you’re already aware that you actually {i}like{/i} me and that it’s not {i}entirely{/i} hormones."
        mi "I know I friggin’ like you, Sensei. Stop makin’ me say it."
        s "Why? "
        mi "Because it just friggin’ reminds me of how long my best friend has liked you compared to me."
    else:
        mi "But...Makoto likes ya too."

    s "How long has Makoto liked me, Miku?"

    scene mikupostbeach8
    with dissolve

    mi "I don’t know! Months? Years?"
    s "But you two have only been my students for a few months, haven’t you?"
    mi "Course not! If that’s true then how come-"

    scene mikupostbeach9
    with dissolve

    mi "Wait, what the heck? "
    mi "Yeah. It’s only been a few months."
    mi "Why’s it feel like so much longer?"

    "It appears we are now two-for-two. "
    "First, Makoto started to catch on to how strange the flow of time has gotten with three semesters of memories packed into one-"
    "And now Miku is on that same exact train."
    "Pretty soon, everyone will be on board and the world will collapse."
    "Or at least that’s what I imagine Maya would say."
    "But this simply can’t go on forever."
    "Within a matter of time, someone is going to start piecing it together. And once they do, I’ll be able to talk about it without sounding like I’m absolutely insane."
    "For example, watch this-"

    s "Miku, what if I told you that the reason it feels like it’s been longer is because we’re stuck in a time loop?"
    mi "A time what now? Have you been drinkin’ or something?"

    "See?"
    "No one will believe me. "
    "Sometimes, you need to see the end of the world to accept that not everything is as it seems."
    "And I’m sure that same thing will apply to Miku, Makoto, and anyone else who begins to piece it all together."
    "Just like all of the girls I know, Kumon-mi is one big puzzle. "
    "So big that everyone has to work together to even fathom the chance of ever finishing it."
    "But that’s enough thinking for now."
    "There are more important things currently at stake."

    s "Why does it matter what Makoto wants if it directly contradicts what you want?"
    mi "It matters cause Makoto is my best friend and wants to do all sorts of cute girly stuff with you like...takin’ out a mortgage or adopting a parrot."
    s "You have a strange idea of what constitutes “girly.”"
    mi "I’m a friggin’ tomboy, Sensei. Go talk to Ami if ya want to know about girly stuff."

    if bonus == True:
        mi "Fact is, Makoto wants to do stuff with you and my mind keeps gettin’ wrapped around on stuff I want {i}you{/i} to do to me."
        s "So...you like me, but you’re more interested in the physical aspect of it rather than something like growing old together and buying a house?"
        mi "Kinda, yeah."
    else:
        mi "All I really know for sure is that Makoto wants to be the huggy girl, but I keep wantin' you to hug {i}me{/i} instead."

    s "This is the actual best news I’ve ever received."

    scene mikupostbeach10
    with dissolve

    mi "That’s not good news at all! I don’t know the first thing about that kinda stuff!"
    s "I mean...you definitely know at least {i}something{/i} now."

    scene mikupostbeach11
    with dissolve

    mi "…"
    s "…"
    mi "You’re really not makin’ this any easier on me, Sensei."
    s "Good. It’s not supposed to be easy."
    s "It’s good that you care so much about something that could hurt someone close to you."
    s "But it’s {i}not{/i} good how you’re giving up what you want in favor of that."
    s "I’m sure I don’t have to say this, but there are a lot more than just two people vying for my affection right now."

    scene mikupostbeach12
    with dissolve

    if bonus == True:
        mi "You’ve got half the friggin’ class ready to take off their skirts for ya."
        s "And I’m sure they’ll all come off in due time."
    else:
        mi "You’ve got half the friggin’ class ready to hug ya 'til you pop."
        s "That is so many hugs."

    s "I’m not looking to take out a mortgage with Makoto or...adopt a bird or whatever it was you said."
    s "I just want to spend time with all of you and, if we both happen to want to do a little extra with that time, I have no issues with it whatsoever."
    mi "But...I just keep thinkin’ of how all those girls would feel if they found out."

    if bonus == True:
        s "How would {i}you{/i} feel if you found out I was doing things with the other girls?"
    else:
        s "How would {i}you{/i} feel if you found out I was hugging the other girls?"

    mi "Weird."
    s "Don’t you already feel weird, though?"
    mi "I always feel weird when you’re around."
    s "Because you like me."

    scene mikupostbeach3
    with dissolve

    mi "Stop it with all that “like” business! I friggin’ know!"
    s "So what then? Are you just going to avoid how you feel forever?"

    scene mikupostbeach7
    with dissolve

    mi "No...I’ll just...wait until I feel different or somethin’."
    s "I doubt that’s going to happen any time soon."
    mi "Same here...but if Makoto ever finds out that I’m feelin’ stuff for the same guy she is...it’ll be a whole thing."
    s "And if she doesn’t find out?"
    mi "Then I can just...secretly feel bad, I guess."
    s "Great. Do that."

    scene mikupostbeach13
    with dissolve

    mi "I’m no genius but that really doesn’t sound like a good idea."
    s "It’s better to suffer in silence than it is to suffer in front of spectators."
    s "You’re already suffering. And that’s only going to get worse with time."
    s "So the best course of action would be to risk the chance of greater suffering in exchange for the guarantee of {i}no{/i} suffering now, wouldn’t it?"
    mi "I don’t know...that’s too many steps for me to follow."
    mi "I just don’t like hidin’ stuff from my friends. That’s all."
    s "You hide things all the time, don’t you?"

    scene mikupostbeach14
    with dissolve

    mi "Huh?"
    mi "What are ya talkin’ about?"
    s "I mean that I still don’t know anything about you."
    s "Or why you react in certain ways to certain things."
    mi "I..."
    mi "Telling you...wouldn’t help at all..."
    s "And I understand that."
    s "I guess what I’m saying is that if you’re already hiding things from people, one or two more won’t hurt."
    mi "Sensei...you’re sayin’ all this stuff that I can’t really keep up with..."
    s "I’m just channeling my skills in negotiation to help you cope with your feelings."

    if bonus == True:
        s "And also get your clothes off in the process."

    scene mikupostbeach15
    with dissolve

    if bonus == True:
        mi "But why me if there are a bunch of other girls who’d take ‘em off without all the extra steps?"
    else:
        mi "But why me when there are so many extra steps?!"

    mi "Seems like you’re workin’ hard but not smart when ya do it like that."
    s "Who knows? Maybe I just like tomboys?"

    scene mikupostbeach16
    with dissolve

    mi "You sure you don’t just like boys in general if you’re comin’ onto someone like me?"

    if bonus == True:
        s "You are very much not a boy, Miku. I have confirmed that."
        mi "My chest begs to differ."
        s "How about I be the judge of that?"
        mi "Not sure how I feel about ya invitin’ some little boy into the room to compare us side by side..."
        s "No invitations necessary. Just give in to my expert negotiation skills and take your shirt off."
    else:
        s "Hug me now or perish."

    scene mikupostbeach17
    with dissolve

    mi "Wow...uhh...didn’t think you’d be that direct..."

    if bonus == True:
        s "You were literally grinding up against me while I was asleep the other night. What I’m doing is significantly less direct than that."
        s "We’re still both in the wrong, though."
        mi "Well...at least we know we're in the wrong."
        s "Exactly. So what’s the harm in doing one more little thing?"
        s "It’s not like I’m asking you to have sex or something."
        mi "…"
        s "Unless..."
        mi "I don’t wanna have friggin’ sex, Sensei. The only position I know is the backwards cowboy."
        s "How did we come back to that?"
        mi "If I...do take off my shirt, though...what are you going to do?"
        mi "Cause I’ll feel weird if you just like...stand there and be all like, “Wow, Miku. You do look like a boy after all,” or somethin’."
        s "Well since you kicked me out the last time I tried touching you in here, there’s not really anything else I can do."
        mi "I don’t mind if you touch me...just...not down below."
        mi "That’s still a little too much..."
        s "So you're fine with hiding this from Makoto after all?"
        mi "I’m...tryin’ not to think of Makoto right now..."
        mi "To...put myself first or whatever you said..."
        s "So...we’re doing this?"
        mi "I’m not really doin’ anything. But if you wanna like...you know...judge them or something like you said..."
        s "…"
        mi "…"

        "An awkward silence fills the room as I come to terms with the fact that I just convinced a nervous girl to strip for me despite her great hesitation."
        "The moment does not last long."
    else:
        s "Here comes the hug, Miku."

    scene black
    with dissolve2

    if bonus == True:
        jump mikufreakdormx
    else:
        mi "GAAAAAAAAAH!"

        "Miku and I hug and it's super cool. But then Makoto shows up and gets really angry because I hugged another girl."

        jump endofmikudormfreak

label endofmikudormfreak:
    play sound "static.mp3"
    scene help with flash
    scene help5 with flash
    play sound "slap.mp3"
    scene mikupostbeach24 with hpunch

    if bonus == True:
        mak "Get out! Right now!"
        s "Wait, hold on. I really didn’t do any-"
        mak "I SAID GET OUT!"
        mi "MMMMMMMMMMMMMMMMM!!!!! MA...KOTO!!!!!!!!!"

        scene black

        "I leave the room and go home to my normal life and normal [niece]."
        "I try to jerk off when I get there but I can’t."
        "I fall asleep before eating."
        "I wake up in the middle of the night with a stomach ache and an apology text message from Makoto."
        "Life goes on."

        $ renpy.end_replay()
        $ miku_love += 1
        $ mikudorm35 = True
        stop music

        "{i}Miku’sssssssssssssssssssssssssssssss {s}affection{/s} dismay has increased to [[ERROR]!{/i}"
        "………"
        "……"
        "…"

        if day == 1:
            jump advancetotues
        if day == 2:
            jump advancetowed
        if day == 3:
            jump advancetothurs
        if day == 4:
            jump advancetofri
        if day == 5:
            jump advancetosat
        if day == 6:
            jump advancetosun
        if day == 7:
            jump advancetomon
    else:
        mak "YOU ARE SUPPOSED TO HUG ME!!! I AM THE HUG GIRL!!!"
        s "Ouchie."

        scene black

        "I go to the hospital and make them heal my face wound."
        "I am never talking to Makoto or Miku ever again."

        $ renpy.end_replay()
        $ miku_love += 1
        $ mikudorm35 = True
        stop music

        "{i}Your face hurts!{/i}"
        "………"
        "……"
        "…"

        if day == 1:
            jump advancetotues
        if day == 2:
            jump advancetowed
        if day == 3:
            jump advancetothurs
        if day == 4:
            jump advancetofri
        if day == 5:
            jump advancetosat
        if day == 6:
            jump advancetosun
        if day == 7:
            jump advancetomon

label mikudorm40:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
            if miku_love >= 15 and mikudorm10 == True and mikudorm15 == False:
                jump mikudorm15
            if miku_love >= 25 and soccer25 == True and mikudorm25 == False:
                jump mikudorm25
            if miku_love >= 30 and soccer30 == True and day != 4 and trinity3track == True and mikudorm30 == False:
                jump mikudorm30
            if miku_love >= 35 and makotowinterbeach4 == True and day != 4 and mikudorm35 == False:
                jump mikudorm35
...
```