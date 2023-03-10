# Coach (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 20

* Event [Hormones Running Wild](./soccer15.md) (Miku) is completed)



## Next events

* [Kirin: Partners in Crime](./kirindate1.md)

## Event properties

* Id: soccer20
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer20

## Official wiki page

[Coach](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer20&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer20:
    scene soccergirls0
    with dissolve
    play music "highspeedprinter.mp3"

    "I decide to spend yet another morning at the soccer field."
    "I feel like I’ve been doing that a lot lately."
    "It’s a little taxing coming all the way to[school] first thing in the morning, especially on the
    weekend, but I’ve managed to somehow get used to it on account of that whole ‘teaching’ thing I do."
    "Combine that with the fact that my trips here are normally pretty exhausting to begin with and it’s surprising that I’m still even showing up."
    "Who would have thought I’d get so hooked on hanging around a girls’ soccer team?"

    if bonus == True:
        "Sure, there are the skin tight shorts...the thigh-highs...the toned and developing muscles..."
        "…"
        "Actually, it does make sense that I keep coming here when I look at it that way."
    else:
        "It's just so rewarding seeing all of their hard work pay off."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene soccergirls1
    with dissolve

    "I spot the three girls I know the names of on a nearby...whatever this
    thing is and come to a full stop several feet away without them noticing."
    "I wait a moment to find out if they are talking about me (They aren’t) before
    deciding to call out and get myself involved in the conversation..."

    menu:
        "Hey, Karin":
            $ karin_love += 1
            $ hikarin = True

            s "Hey, Karin. What are you three up to today?"

            scene soccergirls2
            with dissolve

            ka "Ah-! W-W-What?! Who’s there?!"
            s "Open your eyes and find out..."

            scene soccergirls3
            with dissolve

            ka "Oh...Umm...Hey?..."
            ka "You kind of surprised me. I didn’t even hear you coming."
            mi "Heya, Sensei. Why’d ya call out to Karin? You know she has a heart attack whenever a boy shows up."
            s "That’s precisely why I called out to her instead of you or Kirin. I
            figured it would be funnier if Karin were to get all surprised and whatnot."
            s "And, of course, I was right."

            scene soccergirls4
            with dissolve

            ka "Am I...a plaything to you?! You can’t just toy with my condition like that!"
            s "It seems a little off to call it a condition, but I’ll try to keep that in mind
            the next time I sneak up on you."
            ka "There will be more times?!"
            s "Of course. I’ll have you warm up to me if it’s the last thing I do."

            scene soccergirls5
            with dissolve

            ka "Um...well..."
            ka "I guess if you're okay with waiting...I-"
            mi "Aaaaaanyway...I’m gonna interrupt this special moment to bring you an important announcement."
            s "Wait, what?"

        "Hey, Miku":
            $ miku_love += 1
            $ himiku = True

            s "Hey, Miku. What are you guys up to?"

            scene soccergirls6
            with dissolve

            mi "Oh, Sensei! We’re just hangin’ around on the giant blue step thingy, talkin’ about life and whatnot."
            s "Why is the soccer team having a discussion about life so early in the morning?"
            s "Shouldn’t you three be practicing for whatever fake-game you have coming up next?"

            scene soccergirls7
            with dissolve

            mi "Um...It sounds kinda rude when you call ‘em fake."
            s "Well, they are, aren’t they? They don’t count for anything."
            ka "We tend to use the word unofficial, Sensei..."

            scene soccergirls8
            with dissolve

            mi "Yeah, what Karin said. And besides, all games have a purpose! Even the fa- Erm, even the unofficial ones!"
            mi "If we don’t keep practicin’ we’ll be S-O-L when it comes time to actually play a real team."
            s "Just of out of curiosity, Miku, do you know what S-O-L stands for?"

            scene soccergirls9
            with dissolve

            mi "Uh..."
            mi "Of course I do~ Hahaha..."
            s "It stands for-"

        "Hey, Kirin":
            $ kirin_love += 1
            $ hikirin = True

            s "Hey, Kirin. What’s up?"

            scene soccergirls10
            with dissolve

            ki "Huh? What?"
            ki "Oh...Uhh, hey."
            ki "I saw you coming but I didn’t really think you were going to call out to {i}me{/i} over those two."
            mi "Yeah, what gives? Did you and Kirin become secret friends behind our backs or somethin’?"
            s "No. But we do have a sort of contract together now."

            scene soccergirls11
            with dissolve

            ki "Yeaaahhhh...I forgot about that...hahaha..."
            mi "A contract? What kind of contract?"
            ka "Are you two working on some sort of...new training regimen or something?"
            s "Well, that is {i}one{/i} way to put it."

            scene soccergirls12
            with dissolve

            ki "Dude."
            s "Sorry. Couldn’t help it."
            ka "I’m confused. What other sort of contract is there?"
            mi "Yeah, now I’m kinda curious too."

            scene soccergirls13
            with dissolve

            ki "Hey! Uhh, let’s just leave it alone for now, okay? Hahahah~"
            mi "You’re actin’ kinda weird today..."
            ki "Shut up. Besides, didn’t you have something you wanted to ask him?"
            mi "Something to ask- Oh!"

    scene soccergirls14
    with dissolve

    mi "Sensei! I hereby proclaim you the new coach of the soccer team!"
    s "Wait, what?"
    s "What just happened?"
    ka "Miku decided that if you showed up today, she was just
    going to make you the coach instead of waiting for you to agree to it."
    s "Can she do that?"

    scene soccergirls15
    with dissolve

    mi "There is no limit to my power! Mwahahahaha!"
    ki "She technically can’t, but are you really gonna say no to that face, Sensei?"
    s "What face? The one she has on now?"
    mi "Tremble before me, mortal!"
    s "Kirin, are you sure this is the face you’re talking about?"
    ki "What’s wrong? I think she’s cute when she turns into a supervillain."

    scene soccergirls16
    with dissolve

    mi "Jokin’ aside, I’m puttin’ my foot down, Sensei. You’ve kept me waitin’ for far too long."
    mi "We’ve all got achin’ muscles just beggin’ to be massaged by those magic hands of yours!"
    ka "…"

    scene soccergirls17
    with dissolve

    ka "Wait, what?!"

    scene soccergirls18
    with dissolve

    mi "Yeah! Haven’t you heard? Sensei is apparently a super good moose!"
    s "Masseuse, Miku. It’s masseuse. "
    s "Also, I’m just okay. I never said I was a god."
    ka "Wait, Miku! I know you said it would be good to have him around, but I’m pretty sure he’s not allowed to like, {i}touch{/i} us..."
    ki "I don’t mind~ My legs have been suuuuuper sore lately. I’m sure some {i}physical{/i} therapy will get all of those knots out in a jiff."

    if bonus == False:
        "She must be talking about a hug."

    mi "Why wouldn’t Sensei be allowed to touch us? The last coach did it all the time and you always talked about how great ya felt after."

    scene soccergirls19
    with dissolve

    ka "The last coach was a girl, though...She didn’t have any...{i}ulterior motives...{/i}"

    if bonus == True:
        s "I can hear you, you know..."
        mi "Hmm..."

        scene soccergirls20
        with dissolve

        "Miku pauses for a moment and stares deep into my soul."
        "She doesn’t believe the whole ‘ulterior motives’ thing, does she?"
        "…"
        "Wait a second. I {i}do{/i} have ulterior motives. Why am I getting so up in arms about this accusation?"

        mi "*Ahem* Sensei. Or shall I say...Coach!"
        s "Sensei is fine."
        mi "Coach! Do you have any ulterior motives when it comes to the [young]women of the soccer team?"

        scene soccergirls21
        with dissolve

        ki "Yeah, Sensei~ You weren’t planning on doing anything {i}naughty{/i} to us, were you?"

        "Kirin, I’m really going to need you to keep it together right now..."

        s "Of course not. I won’t touch anyone how they don’t want to be touched."
    else:
        s "Neither am I. I just want you all to become better at soccer."

    scene soccergirls22
    with dissolve

    ka "Hold on a second...I’m not entirely satisfied with that answer."

    if bonus == True:
        ka "What do you mean by how they want to be-"
    else:
        s "I'm being super duper serious, though."

    mi "Sounds good to me! You’re the moose here. You know what’ll work best."

    scene soccergirls23
    with dissolve

    ka "Miku! Don’t I get any sort of say in this? I’m second in command and a year older than you."

    scene soccergirls24
    with dissolve

    ki "You're also a year older than me and I’m still like three times more mature than you~"

    scene soccergirls25
    with dissolve

    ka "You still sleep with a teddy bear, Kirin! I don’t want to hear it!"
    ka "And if you’re more mature than me, how come your curfew is an hour earlier than mine?"

    scene soccergirls26
    with dissolve

    ki "Who cares about a stupid curfew? At least I don’t start crying any time a boy looks at me."
    mi "So, Sensei-Coach-Master-"
    s "Master has been added on now as well?"
    mi "As you can see, things can get a little dysfunctional around these here parts."
    mi "So what that means is, as our new coach, you’re gonna have to keep these two in check so they stop frickin’ fightin’ all the time."
    s "Are they really always like this?"
    mi "Well...not {i}all{/i} the time. But yeah, pretty often."

    if bonus == True:
        mi "I try to step in when I can but it’s not like a pipsqueak who’s just barely outgrown her trainin' bra can really do much to someone Karin’s size."
        mi "And Kirin’s kinda scary in her own way too. Like one of those feisty types that’ll pull ‘yer hair if ya mess with her."

        "Yeah, I definitely get that vibe from Kirin as well."
    else:
        s "That is sad. Sisters should love each other as often as they can because you never know when something bad might happen to one."
        s "Death comes far too soon for far too many people."
        mi "Got that right, Sensei!"

    s "And you’re really sure about me being the coach? I think I’ve told you before, but I really can’t be here every day."

    scene soccergirls27
    with dissolve

    mi "That’s totally fine! We can always do stuff later on if ya can’t make it to the field. "

    scene soccergirls26
    with dissolve

    mi "None of us really have anythin’ to do besides soccer and trainin’ and whatnot anyway. "
    mi "So if ya ever want to just do laps around the park or somethin’ like that, you can always let
    your good pal Miku know."

    scene soccergirls28
    with dissolve

    mi "Oh, actually! I’ve got an even better idea!"
    mi "How about you take down our phone numbers?!"

    scene soccergirls29
    with dissolve

    ki "I second that! Take mine first, Sensei!"

    scene soccergirls30
    with dissolve

    "Kirin pulls a smartphone out from the inside of her shirt and types out her contact info on it before holding it up for me to see."
    "I type the numbers down in my phone and click ‘save,’ still awaiting the next two numbers."

    "{i}Congratulations! You now have Kirin’s cell phone number!{/i}"

    mi "I can’t remember...do ya already have my number, Sensei?"
    mi "We’ve been together a lot and I’m kinda forgetful, so sorry if ya
    already have it and I’m bein’ weird. Hahahaha~"
    s "Nope, don’t think so. Here, you can type it in yourself."
    mi "Coolio!"

    scene soccergirls31
    with dissolve

    "Miku runs over and rapidly types her number into my phone."
    "I’m surprised she’s able to do it so quickly. I know she’s full of energy but I
    kind of figured that would all be saved for the field, not technology."

    "{i}Congratulations! You now have Miku’s cell phone number as well!{/i}"

    mi "Kirin and I are gonna go ahead!"
    mi "Good luck tryin’ to get Karin’s number, Sensei! She’s never given it to a boy before!"

    "Miku and Kirin start jogging toward where all of the other
    girls are playing and I’m suddenly left alone with Karin..."

    scene soccergirls32
    with dissolve

    ka "Mmh..."
    s "…"
    ka "Umm...I-"
    s "You don’t have to give me your number if you don’t want to, Karin."

    scene soccergirls33
    with dissolve

    ka "Huh?"

    if bonus == True:
        s "I don’t blame you for feeling weird around guys. Especially older ones like me."
        s "If anything, I think that most of the other girls are surprisingly forward."
        ka "Um-"
        s "Besides, even if you don’t want me to be your coach, I’ll do what I can to
        make sure it doesn’t bother you or anything like that."
        ka "Uhh-"
        s "I know you’ve been on the team for a while and I obviously wouldn’t want to be stepping on your toes, but-"
    else:
        s "I don't have unlimited texting anyway, so I'll barely ever be able to talk to you."

    scene soccergirls34
    with hpunch

    ka "T-T-T-Take my number too!"
    s "…"

    scene soccergirls35
    with dissolve

    ka "Mmmnnn..."
    s "Are you sure?"
    ka "…"

    "Karin quickly nods her head up and down in place of responding."
    "I hand her my cell and, with trembling fingers, she types her phone number in. "
    "Sure, she needs to backspace some of the digits a few times, but she gets it done in the end."

    "{i}Congratulations! You now have Karin’s cell phone number too!{/i}"

    if bonus == True:
        "{i}Wow! Three phone numbers in one day! It’s almost like you’re the protagonist of a porn game!{/i}"

    ka "…"
    s "…"
    ka "…"
    s "…"

    scene soccergirls34
    with dissolve

    ka "Okay bye!"

    scene soccergirls36
    with dissolve

    "With borderline-frightening speed, Karin joins the rest of her teammates and
    absolutely demolishes them in terms of speed as they make their way around the track."
    "Somehow, I don’t even think Miku would be able to keep up with her right now..."

    scene black
    with dissolve

    if hikarin == True:
        "{i}Karin’s affection has increased to [karin_love]!{/i}"

    if hikirin == True:
        "{i}Kirin’s affection has increased to [kirin_love]!{/i}"

    if himiku == True:
        "{i}Miku’s affection has increased to [miku_love]!{/i}"

    $ renpy.end_replay()
    $ soccer20 = True
    $ mikunumber = True
    $ karinnumber = True
    $ kirinnumber = True
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    jump saturdayafternoon

label soccer25:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
    if miku_love >= 5 and soccer5 == False:
        jump soccer5
    if miku_love >= 10 and soccer10 == False:
        jump soccer10
    if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
        scene soccerfield
        with dissolve
        "I show up at the soccer field to try and talk to Miku but she immediately runs off and starts talking to one of the other girls."
        "Am I...being avoided?"
        "I should probably try visiting her dorm sometime to figure out what's going on with her..."
        jump saturdayafternoon
    if miku_love >= 15 and day83 == True and mikudorm10 == True and soccer15 == False:
        jump soccer15
    if miku_love >= 20 and soccer15 == True and soccer20 == False:
        jump soccer20
...
```