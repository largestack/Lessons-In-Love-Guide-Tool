# Schadenfreude (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 20

* Event [A Dog that Doesn't Do Math](./mall15.md) (Chika) is completed)



## Next events

* [Chika: True Power: Unleashed](./mall20.md)
* [Chika: Detention](./day139.md)

## Event properties

* Id: chikadorm20
* Group: Chika
* Triggered by label: chikadorm
* Triggered by branch label: chikadorm
* Triggered by path: chikadorm->chikadorm20

## Official wiki page

[Schadenfreude](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikadorm20&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label chikadorm20:
    play sound "knock.mp3"

    s "Chika. We’re hanging out tonight."

    "I knock on Chika’s door and wait for her to answer."
    "Not like it will make any difference, though, since I've already verbally confirmed that we will be hanging out."

    c "Who's there?~"
    s "The only male figure in your life."
    c "Dad?! You came back?!"
    s "Why did you have to make this weird?"
    c "Oh, stop. I know it's you, Sensei. Now, are you gonna come in or are you just gonna stand out there and look weird?"

    if day > 5:
        s "Look weird in front of who? No one’s out here."
        c "Correction: No one is out there {i}right now{/i}. You never know when someone is gonna show up."

    else:
        s "Well, no one’s said anything yet. So I’ll probably be fine out here for another few minutes."
        c "Are you really denying an invite into my room so you can continue to...what, {i}not{/i} look weird in front of the other girls?"
        s "It certainly looks that way right now."
        c "Sensei. Come on."

    s "Okay, fine. I’m coming in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene chikadormtwenty1
    with dissolve

    c "Geez, took you long enough."
    s "Yeah, hey."
    c "Did you miss me?"
    s "I guess."
    c "You {i}guess?{/i}"
    s "Am I being interrogated now?"
    c "Maybe~ I've just gotta make sure we're on the same wavelength before anything else happens tonight, and I {i}certainly{/i} missed you."

    scene chikadormtwenty2
    with dissolve

    c "But only because it's kinda tough going long periods of time without a babysitter."
    s "Yeah, so...about that- I don’t really think it was a great idea for me to walk around the mall with your little sister."

    scene chikadormtwenty3
    with dissolve

    c "Huh? Why? She didn’t bother you or anything, did she? I know that she can be a little much sometimes but she promised that-"
    s "I may or may not have run into Ami and Maya while I was with her."

    scene chikadormtwenty4
    with dissolve

    c "What? Oh my God, no way. How did you get out of {i}that?{/i} What did you tell them?"
    s "That she was a dog."
    c "…"
    s "It kind of hasn't shown up in discussion since then, and I'm hoping it will remain that way."
    c "…"

    scene chikadormtwenty5
    with dissolve

    c "Pfft-"
    s "Don’t you dare laugh at my misfortune, Chika."
    c "Sorry, sorry, sorry! It’s just...you really tried to pretend she was a normal dog? That was the best thing you could come up with?"
    s "What could anyone have possibly done in my situation that would have had a better outcome?"
    c "{i}That she was a dog...{/i}Oh my God. The look on your face when you said that-"
    s "Chika."

    scene chikadormtwenty6
    with dissolve

    c "Whaaaaat? I'm not laughing {i}at{/i} you, I'm laughing {i}with{/i} you."
    s "No, you are very much laughing at me."
    s "There’s a weird German word for having fun at someone else’s expense, you know. I don’t know how to say it or spell it, but it’s definitely a thing."

    scene chikadormtwenty2
    with dissolve

    c "Schadenfreude. It means pleasure derived from someone else’s misfortune."
    s "How were you able to say that extremely specific foreign word without even a moment's hesitation?"

    scene chikadormtwenty7
    with dissolve

    c "Who knows? Maybe I'm into that sort of thing?"

    if bonus == True:
        s "That would be quite the plot twist for a self-proclaimed {i}innocent{/i} girl."
        c "Hey, just because I haven’t actually {i}done{/i} anything doesn’t mean I don’t think of stuff like that. What if I’m some sort of, like...closet-dominatrix or something?"
        s "My opinion of you is rapidly changing tonight."

        scene chikadormtwenty8
        with dissolve

        c "Oh, please. We both know there’s only one perv in this room and it’s you."

        if chikatownfirst == True:
            s "Correct me if I’m wrong here, Chika, but wasn't it just the other day that {i}you{/i} decided it was time for us to start making out in the middle of the second half of town?"

            scene chikadormtwenty9
            with dissolve

            c "Who? Me? I’ve never kissed anyone before. I don't have any idea what you're talking about."
            s "Really? Because my memory of that night is a little different."
            c "R-Really? Well, uhh...what do you remember, then?..."
            s "Actually, now that I think about it, maybe that was someone else."

            scene chikadormtwenty10
            with dissolve

            c "Hey! Who else are you making out with behind my back?"
            s "Behind your back? But I thought there wasn’t anything going on between us?"

            scene chikadormtwenty9
            with dissolve

            c "Well, uhh...there's {i}technically{/i} not...but I think it should be pretty obvious that I-"

        else:
            s "Well, you’re not {i}wrong{/i}...But you’re the one not wearing any pants despite knowing that. And that kind of makes you a pervert by association."
            c "Okay, first off, what the hell is a pervert by association? That's not a thing."
            c "Second, how was I supposed to know you were coming over? I was just trying to get comfy."
            s "Please don’t let me get in the way of that, then. In fact, if you want to take even more clothes off to get comfier, I promise not to stop you."

            scene chikadormtwenty7
            with dissolve

            c "Suuuuure. So I just strip while you stand there and watch. How come I feel like that’s not exactly how things would go?"
            s "Probably because I'm a healthy, adult male who is heavily attracted to you."
            c "Oh yeah? Then how come-"
    else:
        s "Then I will have to resurrect your dead mother and inform her that her daughter is becoming a bad person."
        c "Wow. You say some pretty fucked up shit in the Patreon version."

    s "Chika."

    scene chikadormtwenty3
    with dissolve

    c "Huh? What? I wasn't finished talking."

    if bonus == True:
        s "Can we take this to the bed?"
    else:
        s "Can we platonically take this to the bed?"

    c "…"
    s "…"

    scene chikadormtwenty11
    with dissolve

    c "Huh?..."
    c "You mean, like...right now?"

    if bonus == True:
        s "Just to sit down, I mean."

        scene chikadormtwenty11r
        with dissolve

        c "Oh, what the hell?! You knew I wasn't going to interpret it that way, you big jerk!"
        c "I nearly had a heart attack just now!"
        s "Really? I guess that confirms you must be at least {i}somewhat{/i} perverted then, right?"
        s "I was making a totally wholesome request and you somehow twisted it into something inappropriate. Shame on you."
        c "I'm not a..."

        scene chikadormtwenty11rr
        with dissolve

        c "Ahh! Forget it!"
    else:
        s "Just to sit down. I spent too much time on the elliptical this morning and my leggies are sore."

    scene black
    with dissolve2

    "Chika sighs to herself and angrily moves over to the bed, hopping on and bringing herself closer to the wall."

    if bonus == True:
        "I catch a glimpse of what appears to be pink lace underwear as she adjusts herself and can’t help but think about how she’d react if I just went for it right now."
        "But I’m a good person."
        "I will not do that unless she invites me to do so."

        s "..."

        "{s}I will not do that unless she invites me to do so.{s}"

        c "Um...Sensei?"

    scene chikadormtwenty13
    with dissolve
    stop music fadeout 30.0

    c "Why are you looking at me like that all of a sudden?"
    s "Like what? This is how I always look at you."
    c "Nuh-uh. You keep, like...staring at my legs."
    c "It looked like you were...I don't know...maybe, like...thinking of something?"
    s "What would I be thinking of, Chika?"

    scene chikadormtwenty14
    with dissolve

    c "I don't know..."
    c "Stuff?"
    s "What kind of stuff?"
    c "Why do I have to be the one to say it?..."
    s "Because that's how this relationship has to work."
    s "You need to want it just as much as me."
    s "And if you don't, nothing will ever happen."
    c "..."
    s "But you want it to happen, don't you?"

    scene chikadormtwenty15
    with dissolve

    c "I'm..."
    c "I'm a little scared."
    s "Of what?"
    c "I've just...never done anything like this before."
    s "I-"
    c "We obviously both know we're on the bed cause, like...we want something to happen-"
    c "But...when you really think about what we want to happen...don't you also think it's something we should maybe, like...not want at all?"
    s "..."
    c "..."

    play music "asobeatsex7.mp3"

    s "No."

    scene black
    with dissolve2

    s "I don't think anything even close to that."

    "A moment of silence finds its way into the room, drowning out the volume of a live performance on TV that Chika must have been watching before letting me in."
    "It’s a strange thing when silence is powerful enough to kill off sound. And describing it to anyone who isn't swimming in the lakes of their own loneliness would prove problematic."
    "But me?"
    "I am an exceptional swimmer."
    "I can understand things like this that no one else can."
    "Was living and loving always this easy? "
    "And is it even okay to equate moments like this to words as strong as ‘love’ when it's something I've never understood at all?"
    "I don’t know."
    "But what I do know-"

    if bonus == True:
        c "Sensei..."
    else:
        c "We should hug."

    "What I do know is that now, in this moment-"
    "I want this girl."
    "I don’t know if I will forever."
    "But I want her now."
    "And that’s all that matters."

    if beachvacation16 == True:
        "Chika and Rin aren't going to end up together."
        "There was never a chance for them in the first place."
        "But what spells heartbreak for one opens doors for another."
        "I've done my duty in holding back thus far...but I was never going to keep that up forever."
        "What happens next is between Chika and me."
        "Rin has nothing to do with it anymore."

    "We move closer together."
    "........."
    "......"
    "..."

    if bonus == True:
        jump chikadorm20x
    else:
        "And then I hug her."

        $ renpy.end_replay()
        $ chika_love += 1
        $ chikadorm20 = True
        stop music fadeout 7.0

        "{i}Chika’s affection has increased to [chika_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikafingerreplay:
        play sound "knock.mp3"

        "..."

        c "Come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump chikafingerreplayx
        else:
            $ chika_lust += 1
            stop music fadeout 4.0

            "{i}Chika's lust has increased to [chika_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label chikahjreplay:
        play sound "knock.mp3"

        "..."

        c "Come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump chikahjreplayx
        else:
            $ chika_lust += 1
            stop music fadeout 4.0

            "{i}Chika's lust has increased to [chika_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label yumidorm20:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label chikadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if chika_love >= 5 and day == 1 and chikadorm5 == False:
                "I should probably wait until Yumi's not right there to hang out with Chika..."
                jump doorknock
            if chika_love >= 5 and day != 1 and day != 3 and firsttimemall == True and chikafirsthall == True and chikadorm5 == False:
                jump chikadorm5
            if chika_love >= 10 and mall10 == True and chikadorm5 == True and chikadorm10 == False:
                jump chikadorm10
            if chika_love >= 15 and chikadorm10 == True and chikadorm15 == False and day != 3 and day != 1:
                jump chikadorm15
            if chika_love >= 20 and mall15 == True and chikadorm20 == False:
                jump chikadorm20
...
```