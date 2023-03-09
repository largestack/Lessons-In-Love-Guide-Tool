# Something About Biting
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikadorm5&go=Go)



## Event preconditions
✅Chika love greater than or equal to 5

✅Day of week is not Monday

✅Day of week is not Wednesday

✅Event "[Chika: The Retail Machine](./firsttimemall.md)" is completed (event=firsttimemall)

✅Event "[Chika: A Dog that Does Math](./chikafirsthall.md)" is completed (event=chikafirsthall)



## Next events
* [Chika: Side Event](./chikadorm10.md)

## Event properties
* ID: chikadorm5
* Group: Chika
* Triggered by label: chikadorm
* Triggered by branch label: chikadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label chikadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "…"
    "I knock on the door and wait for Chika to answer."
    "In doing so, I'm also risking the possibility of Yumi answering and then promptly amputating one of my limbs, but that is a risk I am willing to take at this point in time."
    "Especially since I can't imagine a future in which I'm only allowed inside of {i}some{/i} of the dorm rooms and not all of them."
    "I'm counting on you, Chika. Please be here."

    c "Come in! Door's open!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I'm invited in with no hesitation, likely because Chika assumes I'm one of the girls."
    "But even though I'm aware of this, I decide against saying anything since my words would become just one more obstacle in what I'm already making out to be a great opportunity."
    "Here goes nothing, I guess."

    scene chikafirstdorm1
    with dissolve2

    c "Woah! You're certainly an unexpected visitor."
    s "Surprise."
    c "Surprise indeed. What's up? Did you need me for something?"
    s "Not anything in particular. Just wanted to see what you were up to and you just happened to not be in the hallway this time."

    scene chikafirstdorm2
    with dissolve

    c "Well, yeah...I just wish you would have told me in advance so I could like, prepare myself and stuff."
    s "Prepare yourself for what, exactly?"
    c "Umm...the...unfamiliar wave of emotions that comes from having a boy in my room for the first time?"
    s "Oh, right. You're anti-boy."

    scene chikafirstdorm3
    with dissolve

    c "I'm not {i}anti{/i}-boy, Sensei! I told you I'm just not super experienced when it comes to like, you know, dating and all that stuff."
    s "Well if it makes you feel any better, I am not here to date you."
    c "Why are you rejecting me before either of us has asked the other one out?!"
    s "Can I be in here or not? Because I can't really tell with the way you're acting right now."

    scene chikafirstdorm4
    with dissolve2

    c "Of course you can be in here..."
    c "Well, at least until Yumi gets back, I mean."
    c "It just feels a little sudden, you know? Like...I sleep in here."
    c "And if I hadn't finished cleaning like, five minutes before you showed up, you would have seen all of my clothes all over the floor and it would have totally ruined any opinion you have of me."
    s "You're right. My opinion of you hinges entirely on the frequency of your laundry routine."

    scene chikafirstdorm5
    with dissolve

    c "Why do I feel like every single thing I've added to this conversation so far has been me digging myself into an even deeper hole?"
    s "Because you're nervous. Relax. I'm just here to hang out."

    if mall10 == True:
        s "Unless you want to pick up where you left off in the dressing room the other day. I'd just want to wash my hands first and-"

        scene chikafirstdorm6
        with dissolve

        c "Ahhh!!!! No no no no no no! Stop right there! We don't talk about that anymore!"
        s "Why not? I figured you'd be a little more confident now that you're in your own room."
        s "Granted, confidence didn't really seem to be the issue at the mall and-"
        c "And nothing! Nothing happened at the mall! Unless...you {i}wanted{/i} something to happen at the mall! Which is a thing I still can't really wrap my head around!"
        c "I don't even like thumbs!"
        s "You should probably stop yelling, Chika."

        scene chikafirstdorm6r
        with dissolve

        c "Yeah. Yeah, okay. I'm good. Good and completely mature and not acting irrationally {i}at all{/i}."
        c "Just...a totally innocent girl hanging out with her totally unsuspecting teacher...all alone in...a bedroom and..."
        c "Oh boy..."

    else:
        scene chikafirstdorm4
        with dissolve

        c "Sensei, any girl in their right mind would be a little nervous right now. It's not just a {i}me{/i} thing."
        s "I just figured the whole age gap thing would-"
        c "That doesn't...really change anything for me. You're still a {i}guy{/i} and there's no way for like, a person to keep themself from falling for somebody even if everyone else thinks it's not the right person or whatever."
        c "The only thing that really changes is like, I guess how I'd act around that person? I don't know. It's hard to...put into words."
        c "Like, if I ever wound up liking somebody your age, I doubt I'd just up and tell them about it."
        s "What? Why not?"

        scene chikafirstdorm2
        with dissolve

        c "Well...isn't the older person supposed to make the first move in situations like that?"
        c "I just...kinda figured that's how that went."
        s "I don't really think there's a rulebook when it comes to that, Chika."
        c "Well...there should be. Because it would definitely make a lot of stuff a lot easier for me to understand right now."

    "It's times like this that really reinforce just how inexperienced Chika is when it comes to romance."
    "I’m sure that she'd be incredibly popular with guys if there were actually any around."
    "She’s already well-liked by pretty much all of the girls in the school...so I can only imagine how things would be with the opposite sex."

    s "Hey, Chika."

    scene chikafirstdorm7
    with dissolve

    c "Yeah? What's up?"
    s "Just out of curiosity, what sorts of guys {i}are{/i} you into?"

    scene chikafirstdorm7r
    with dissolve

    c "Wanna borrow my notebook so you can write it all down?"
    s "I think I'll be fine with just mental notes, thanks."
    c "Well, pay close attention then. Cause there's kind of a lot of stuff that I like and my soulmate would have like, at least 50%% of these qualities."
    s "I'd assume a {i}soulmate{/i} would have 100%% of them, but sure. Go ahead."
    c "I guess I’d like somebody...dependable."
    c "Somebody who could look after me if I got sick or...help me figure out how to pay bills or something like that."
    c "Someone who would take me shopping and be honest with me when I try something on and it doesn't look great."
    c "But...I’d also want them to be really down to earth and...sensitive and stuff too."

    if cafe15 == True:
        s "Them? Not him?"

        scene chikafirstdorm8
        with dissolve

        c "Huh? What do you mean?"
        s "I just haven't heard you specifically mention this person also having to come equipped with a penis yet."
        c "I mean...I don't know. I don't really think they do?"
        c "I don't think I'd be opposed to dating a girl if the right one came along. I've just kind of only been attracted to guys so far."

        "Huh."
        "I guess maybe there’s a little hope for Rin after all?"

    else:
        s "I see. I guess that makes sense for a girl your age."

    scene chikafirstdorm9
    with dissolve

    c "Now, hmm...let’s see..."
    c "What else do I like?..."
    c "Oh, well obviously, it would have to be someone I’m physically attracted to. So probably older and taller and stuff."
    c "I think glasses are kinda cute too. And muscles."
    s "I'm beginning to think you might be intentionally describing me here."

    scene chikafirstdorm6r
    with dissolve

    if bonus == True:
        c "{i}And someone who could be really gentle...but also a little wild at times...{/i}"
        s "Chika?"
        c "{i}Someone who likes biting...{/i}"
        c "{i}Someone who-{/i}"
        s "Chika."
    else:
        c "Someone like...Eddie Murphy."
        s "What?"

    scene chikafirstdorm10
    with dissolve

    c "Huh? What? Hi."
    c "How much did I say?"
    s "There was something about biting."
    c "No there wasn't."
    s "Oh. My bad. Must have been the wind."

    "Yeah, I'm pretty confident that this will be going somewhere in the near future."

    if mall10 == True:
        "Granted, I kind of figured that out the second my thumb went into her mouth, but now I'm {i}really{/i} sure."
    else:
        "{i}How{/i} near remains to be determined, but there is absolutely no way Chika is just dropping all of these hints on accident."
        "I don't know much about her yet, but I can tell she's smarter than that."

    scene chikafirstdorm7
    with dissolve

    c "Hey, do you wanna like, sit down or something?"
    c "I feel kinda bad just making you stand there like that when you probably walked all the way over here..."
    s "I'm getting pretty used to walking, so it's not a big deal. But yeah, we can sit."
    c "Cool! Is..."

    scene chikafirstdorm10r
    with dissolve

    c "Is the bed okay? Or would that be like, weird or something?"
    s "It wasn't going to be weird. But it might be now that you said that."
    c "Can we...pretend I didn't say that then? Cause the only other option is the couch and one of the cushions has a broken spring in it that makes weird noises and-"
    s "The bed is fine, Chika."
    c "Cool. Yeah. Bed it is, then."

    scene black
    with dissolve

    "Chika takes a moment to compose herself before leading me over to the bed and sitting down."
    "She turns the TV on for some reason, which I don't fully understand since she immediately mutes it, but I guess that doesn't matter right now."

    scene chikafirstdorm11
    with fade

    "Her blanket is one of those obnoxiously fluffy ones that air can’t get through, making it easy to surmise that she likely sleeps with minimal clothing on- a thought I shouldn't be having right now."
    "Actually, no. That is absolutely a thought I should be having right now."
    "This girl invited me onto her bed despite the obvious blooming attraction between us."
    "She wants me to think those things."
    "And I'm sure she'd be in the same exact position I'm in if I were the one to invite her over to my place instead."

    c "So! Now that we've talked about {i}my{/i} ideal partner...could you maybe tell me a little bit about yours?"
    s "Do {i}you{/i} need a notebook? Or will you also be employing the mental note strategy?"
    c "I think my memory will suffice."

    s "Then...let's see..."
    s "The quality that's most important to me would probably be..."

    menu:
        "Looks":
            s "Probably looks, despite how superficial I'm sure that sounds."
            s "I just can't imagine being with someone I'm not physically attracted to."

            scene chikafirstdorm12
            with dissolve

            c "No, yeah! I totally get that! I'm the same way!"
            c "Like, I don't think I'd say looks are the {i}most{/i} important quality, but they're definitely, like...super important. You know?"
            c "What, umm...what kinds of girls are you the most attracted to, if you don't mind me asking?"
            s "Tan, blonde ones who wear too much pink and decorate their walls with other, equally attractive girls."

            scene chikafirstdorm13
            with dissolve

            c "Hmm...I wonder if I know anybody like that?"
            s "If you do, could you maybe set me up? Preferably with one who doesn't mind me hanging out in her room all the time."

            scene chikafirstdorm13r
            with dissolve

            c "Yeah. I'm pretty sure I could find you somebody like that, Sensei."
            c "They're really sensitive, though, so you'd have to be super nice to them all the time."
            s "{i}Nice{/i} isn't really a strong point of mine, but I'll see what I can do."

        "Innocence":
            s "Innocence, I guess?"

            scene chikafirstdorm12r
            with dissolve

            c "Innocence? I’m innocent!"
            c "I have no idea why that's the most important quality to you, but I'm totally okay with it!"
            s "It certainly appears that way."

            scene chikafirstdorm11r
            with dissolve

            c "Oh, uhh...Sorry. I just..."
            c "Yeah."
            c "Innocence can mean like, a bunch of different things, though. So...what are you referring to exactly?"
            c "Cause you already know I don't have any experience with guys. But, at the same time, I'm not the same type of innocent as somebody like...I don't know. Sana."
            c "So do you mean like, experience innocent? Or...personality innocent? Cause I'm a little bit of both of those things, but...definitely more of the first one."
            s "Using Sana as the benchmark for the opposite end of the spectrum kind of insinuates that she has experience with men and that makes me feel very strange."

            scene chikafirstdorm13
            with dissolve

            c "Idunno. Maybe she does? Who are we to hold her back?"
            s "If you need an answer, I'm not really sure which of those two sides I lean towards."
            s "It's like asking me what the most important side of a coin is when they're both equally valuable."

            scene chikafirstdorm11
            with dissolve

            c "Right. Except tails is definitely the more important side and we all know it's true."

        "Sex" if bonus == True:
            s "...Sex, I guess?"

            scene chikafirstdorm14
            with dissolve

            c "...What? Really?"
            c "That's...the {i}most{/i} important thing to you? That's not even a quality. I thought we were talking about, like...personality traits."
            s "I guess calling it the most important quality isn't really accurate. But I don't think it's wrong to use it as a barometer to determine how potentially successful a relationship can be."
            c "That's just...such a..."
            c "Like, coming out and just admitting it like that takes balls."
            c "Obviously my word means like, literally nothing here since I've never even kissed anyone before, but...I don't know. I just feel like that's such a tiny part of what love is."
            s "Love wasn't really what you asked about, though."
            c "Huh?"
            s "You asked what I'd look for in a partner. Not every relationship needs to be about love, Chika."

            scene chikafirstdorm14r
            with dissolve

            c "I guess I...didn't really think of it like that."
            c "..."
            c "Huh."

        "Girls that really like hugs" if bonus == False:
            s "Honestly...I really like girls who aren’t afraid of putting themselves out there in hug form."

            scene chikafirstdorm14
            with dissolve

            c "Putting themselves out there in hug form?...What do you mean?"
            s "You know. Girls that just really like to hug."
            c "..."
            s "..."

    "The two of us sit in silence for a while as our gazes bounce back and forth from the depths of each other's eyes to the muted television."
    "They'll occasionally lock onto each other for short bursts of time that ultimately equate to nothing but slight nudges in the direction we both know we're heading."
    "And of course, I'm not the one to break the silence when its time is finally diminished."
    "I likely never will be, either."

    scene chikafirstdorm11
    with dissolve

    c "Oh! Umm, I’ve been meaning to ask you, but do you think that you might be able to help me study some time?"
    s "I {i}am{/i} your teacher, so I'm pretty sure I'm supposed to say yes."
    c "Okay, awesome! Cause like, I'm really into the whole {i}no tests{/i} thing, but I don't really want my mind to start, like...melting. You know?"
    s "I mean...I don't think I'd worry about it {i}melting,{/i} but yeah. I get it."
    s "Just let me know when and I'll do whatever it is I can."

    scene chikafirstdorm15
    with dissolve

    c "Thanks, Sensei."
    c "You know...when I first joined your class, I never would have even {i}imagined{/i} the two of us being able to talk like this."
    c "But...I really like it. And I like you, like...being here or whatever."
    c "I'm probably gonna start talking in circles if I don't cut myself off but, like...I guess what I'm trying to get at is that you..."
    c "You can come by whenever you want."
    c "Well, so long as Yumi's not here."
    s "That's good enough for me, Chika. I'll drop by as often as I can."
    c "Okay...cool."
    c "The door's always open."

    scene black
    with dissolve2

    "Chika walks me to the door and awkwardly wraps her arms around me for a few seconds before allowing me to leave."
    "I think about hugging her back, but get distracted by something on the wall."
    "I forget what that something is on the way home."

    $ renpy.end_replay()
    $ chikadorm5 = True
    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]! You can now
    spend time with her in her room!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikadorm10:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
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
...
```