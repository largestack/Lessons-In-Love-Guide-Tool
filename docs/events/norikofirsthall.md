# Sculpture (Noriko)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [What Was](./day271.md) (Main) is completed)



## Next events

* [Main: Annabel Lee](./day280.md)
* [Noriko: Nakayarakawayama](./convenience1.md)

## Event properties

* Id: norikofirsthall
* Group: Noriko
* Triggered by label: dorm2wednesday
* Triggered by branch label: dormwednesday
* Triggered by path: dormwednesday->dorm2wednesday->norikofirsthall

## Official wiki page

[Sculpture](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikofirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikofirsthall:
    scene norikohall1
    with dissolve

    n "Hey! What brings you over here today, Sensei?"
    n "If you’re just wandering around the halls looking for something to do, might I suggest hanging out with yours truly?"
    n "I heard from some of the others that you mope around here like some sort of lost puppy pretty often, and I would like to inform you that I am looking to adopt."
    s "I wasn’t looking to be adopted today, but I guess the two of us can hang out."
    n "If {i}you{/i} were looking to adopt as well, I would also like to make myself available as your dog. "

    if bonus == True:
        n "You can walk me around on a leash and everything. Ami would love it."
        s "I don’t think there’s anything in the world that Ami would hate more, actually."

        scene norikohall2
        with dissolve

        n "You’ve just gotta learn how to talk to her. Leave it to me, Sensei."
        s "If you say one word to her, I feel that the two of us may never see each other again."

        scene norikohall3
        with dissolve

        n "But I just got you back! That’s not fair! "
        s "You're right. Which is why I regret to inform you that I can not walk you around on a leash {i}in public{/i}."

        scene norikohall4
        with dissolve

        n "Oh, right. I forgot that the public part was the first link in the chain of events that lead to us being separated once more."
        n "I can live with that as long as one of us gets to leash the other in private some time."
    else:
        s "I hope you are ready to be put up for adoption. I do not want to take care of a pet."
        n "Wow, okay. Nevermind then."

    s "Noriko, can I ask you something?"

    scene norikohall5
    with dissolve

    n "You can ask me literally anything you want whenever you want."
    s "Have you really been waiting years for me to walk back into your life?"
    n "Well, I’m technically the one who walked back into yours. But yeah."
    s "Then...how did you get so into this leash thing? Has this {i}always{/i} been a dream of yours, or..."
    n "I have an overactive imagination that sometimes drifts into dangerous territory."
    n "If you’re worried that it’s something I’ve experienced and thus have developed an unhealthy craving for, you are mistaken."
    s "Interesting."
    n "How so?"
    s "I just normally have to work a little harder to get girls this invested in me."

    scene norikohall6
    with dissolve

    n "Hehe...yeah."
    n "I still remember how hard you had to work to get Niki to like you back in the day."
    n "But as soon as you did it was like, all she ever talked about."
    n "Which is probably why {i}I{/i} started feeling all tingly really early too."
    n "Well, that and you were super cute back then."
    n "Not to say that you’re not still cute, obviously. But now it’s more of a “mysterious older guy” cute and not “shirtless neighbor boy in the backyard” cute."
    s "Well thanks for not ever making a move back then, I guess."
    s "I can’t imagine that would have been good for my apparent previous relationship with a pop star."

    scene norikohall7
    with dissolve

    n "There’s no need to add “apparent” to that, Sensei. It definitely happened and it was a huge part of all of our lives."
    n "Even if you don’t remember it right now, I’m sure you will in time."
    n "And once you do, I’ll be there to squeeze you and let you cry on my shoulder until your eyes turn so red and puffy that they swell shut and need to be surgically reopened."
    s "I can’t foresee myself crying any time soon, but thanks for the offer regardless."

    scene norikohall8
    with dissolve

    n "Don’t mention it...I-"
    n "I know it’s probably really weird hearing someone bring up the past so much when you’ve already clearly moved past it, but..."
    n "There’s a life for you outside of this dorm, you know? Outside of the[school], too."
    n "And I make good enough money between my job and doing PA work for Nee-chan that I could {i}probably{/i} support the two of us if you wanted to just quit teaching altogether."

    scene norikohall9
    with dissolve

    n "But teaching has always been what you're good at."
    n "That’s why Maya and I turned out so darn smart."
    n "Obviously, there was a lot of work that still had to be done outside of that creepy old apartment of yours-"
    s "Wait, Maya?"

    scene norikohall10
    with dissolve

    n "Yeah. The same Maya that's in our class and wants to turn my spine into a coat rack."
    n "You don’t remember that either?"
    s "Not at all..."
    n "Well...how did you think the two of us knew each other, then?"
    s "I had no idea. She wouldn’t tell me anything about it. Just that you’re evil and going to ruin everything."
    n "How would I ruin anything at all? I’ve done literally nothing wrong since I’ve shown up here."
    s "True. But, to be fair, that hasn’t been very long."

    scene norikohall1
    with dissolve

    n "Well then, let me prove it to you."
    n "I didn’t wait all of these years to show up and get you to hate me or think I’m weird."
    n "And, if there’s anything you want to change, just let me know. "
    n "Turn me into a sculpture. "
    n "Make me your ideal girl."
    n "Want someone with darker hair? I’ll dye it. "
    n "Someone skinnier? I’ll lose weight."
    s "Please don’t lose any weight. You’re already extremely skinny."
    n "I can gain weight, too. Just say the word."
    s "Just...stay the way you are now."
    s "I’m not going to do something like ask you to change for me when I haven’t even identified any problems yet."
    s "Except for maybe the pocket knife thing."
    s "Actually, yeah. Get rid of your knife."
    n "Oh, the pocket knife stays. I need it to protect myself and conserve my chastity for you."
    s "Fine. But get a holster or something so you don’t wind up slicing your leg open again."
    n "Roger that. "
    n "Anything else?"
    s "Yes. Give me your number."

    scene norikohall2
    with dissolve

    n "Nice. That was smooth."

    if bonus == True:
        n "Are you going to text me at weird hours of the day asking for nudes? "
        s "Are you going to send them if I do?"
        n "Uhhhh yeah? Duh."
        n "Just don’t post them online or show them to anybody else."
        s "Who would I even show them to?"
        n "I don’t know. I heard you’re really close with that girl who wears the skull hairclip in our class and I get hardcore lesbian vibes from her."
        n "But, actually, she’s cute. You can show her if you want. "
        n "Just don’t let her know {i}I{/i} know because then it will be a whole thing and we might wind up fingering each other on a camping trip or something."
        s "Please invite me if that ever happens. I will never forgive you if you don't."
    else:
        s "Not as smooth as your...face."
        n "That was less smooth."
        s "I'm sorry. I am not used to flirting."

    s "Also, why haven't you given me your number yet?"
    n "I’m still waiting for you to give me your phone."
    n "I promise to not delete every single contact except for myself."
    s "That wasn’t a thing I was worried about until you said that."

    scene norikohall9
    with dissolve

    n "I was kidding, obviously."
    n "You don’t actually believe the stalker thing that Maya said in class, do you?"
    s "Let’s just say if I were to rank the girls by “likelihood to follow me home after[school],” you’d be near the top."
    s "And that’s pretty impressive given that we just met."
    n "Just {i}reunited{/i}. And yeah, I’m definitely going to follow you home from time to time."
    n "But I have zero qualms doing that alone {i}or{/i} as part of a group."
    n "Nothing would make me happier than just going out to karaoke with you, Ami, and that one blonde girl who thinks she loves you more than I do for some reason."

    if bonus == True:
        n "Except for maybe making out with you in said karaoke booth while Ami and the blonde girl sing Misfits songs."
    else:
        n "Except for maybe hugging you in said karaoke booth while Ami and the blonde girl sing Misfits songs."

    s "That fantasy seemed plausible up until the very end of it."
    n "Gimme your phone. "

    if bonus == True:
        n "Oh, and if I {i}do{/i} send you nudes, please send some back. "
        n "I know I said I have an overactive imagination, but visual aids still help a loooooot when I’m jilling myself off under the covers."
    else:
        n "I'm gonna order Domino's."

    s "I have no idea why Maya doesn’t like you. You’re perfect."

    scene black
    with dissolve

    "Noriko takes my phone and enters her contact information into it."
    "Not only does she slap a heart emoji next to her name, she inserts a puking emoji next to her sister’s name right above hers."
    "I figured the Kandas were going to be the only sibling war I found myself wrapped up in, but..."
    "It seems that this is very much not the case."
    "And even though my experience with the Nakayamas (Or at least the experiences I am consciously aware of right now) is brief-"
    "I imagine this war will be much more...intense than that of the other one..."

    $ renpy.end_replay()
    $ norikonumber = True
    $ noriko_love += 1
    $ norikofirsthall = True
    stop music fadeout 5.0

    "{i}Congratulations! You now have Noriko’s number!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirindorm10:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label dorm2wednesday:
    if chapthreeactive == True:
        scene summerdorm2wed
        with dissolve
    elif christmas7 == True and day271 == True and chapthreeactive == False:
        scene wedwinter2noriko
        with dissolve
    elif christmas7 == True and day271 == False and chapthreeactive == False:
        scene wedwinter2
        with dissolve
    elif christmas7 == False and chapthreeactive == False:
        scene dorm2_wednesday
        with dissolve

    if christmas7 == True and day271 == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
    elif christmas7 == True and day271 == True:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo and Noriko aren't doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
    else:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"

    menu wednesday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Tsuneyo":
            if tsuneyofirsthall == False:
                jump tsuneyofirsthall
            else:
                jump tsuneyohall
        "Talk to Noriko" if day271 == True:
            if norikofirsthall == False:
                jump norikofirsthall
...
```