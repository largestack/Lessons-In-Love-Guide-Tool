# I See You
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets10&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 10

✅Event "[Main: This Town Has Two Halves](./day44.md)" is completed (event=day44)



## Next events
* [Main: Contractions](./day85.md)
* [Yumi: Fuck The Police](./yumidorm5.md)

## Event properties
* ID: streets10
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label streets10:
    scene iseeyouredux1
    play music "streetnoise.mp3" fadein 5.0

    "Another weekend means another chance to wander the streets."
    "And with Yumi running out of places to hide, I find myself in yet another section of the city."
    "The problem is that I’ve been here for a little over an hour now and haven’t bumped into her."
    "So, the current strategy is to stand in one place and wait for {i}her{/i} to show up this time."
    "Sure, I’ll probably look a little suspicious to anyone that stares out of their window for an extended period of time, but it’ll all be worth it soon enough..."
    "Or not."
    "Either way, it's not like I have anything else to do."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Roughly 17 minutes later...{/i}"

    scene iseeyoureduxexhaust
    with dissolve2

    y "You’ve gotta be kidding me..."
    s "Oh, hey. Fancy meeting you here. What are you up to?"
    y "Why are you just...standing there? You look suspicious as fuck."
    s "Funny you should say that, I was actually just thinking the same thing."
    y "So...you knew you looked like a fucking creep and decided to continue standing around anyway?..."
    y "You hit your head or some shit this morning?"
    s "No. But now that we’re together, I think that we should hang out."

    scene iseeyoureduxeyesclosed
    with dissolve

    y "Nope. See ya."

    "Yumi goes to leave and I instinctively reach out and grab her wrist to prevent her from escaping."

    scene iseeyoureduxangry
    with dissolve

    y "Dude! Get your fucking grimy ass hands off of me! God knows where they’ve been!"

    if bonus == True:
        s "Don’t worry, they haven't been anywhere unattractive."
        y "The fuck does that even mean?!"
        y "Just fucking...let go!"
        y "There are people watching, asshole!"

        "It’s true."
        "Not the asshole part-"
        "Okay, {i}kind of{/i} the asshole part- but mainly that a few passersby are stopping and staring as I restrain a [teenage]girl by the arm."
        "Wanting to avoid further misunderstanding (If you can even call this a misunderstanding), I decide to let go."
    else:
        s "Sure thing, Yumi. I apologize for making you uncomfortable."

    scene iseeyoureduxlookingaway
    with dissolve

    y "Thanks...I guess."
    y "Not really sure why I'm thankin' you in the first place when this shit was literally all because of you, but..."
    y "Why do you even wanna hang out with me anyway?"
    y "We don’t like each other, remember?"
    s "That’s not true. I like you. Kind of."

    scene iseeyoureduxnormal
    with dissolve
    stop sound fadeout 8.0

    if bonus == True:
        y "My bad. What I meant to say is that I don’t like you and you just want to fuck me."
        s "I never said that."
    else:
        y "My bad. What I meant to say is that I don’t like you and you just want to hug me."
        s "I want to hug everyone."

    scene iseeyoureduxangry
    with dissolve

    if bonus == True:
        y "Well, you sure as Hell have fucking thought it!"
        s "..."

        "I mean-"

        y "Just...keep your fucking hands away from me or you’ll wind up with a...back-alley vasectomy or some shit."
        s "That’s...actually terrifying."
    else:
        y "And I just want to punch old people."
        s "You're so crazy."

    scene iseeyoureduxnormal
    with dissolve

    y "Yup. So, am I free to go now or are you still going to fucking stalk me?"
    s "I’m probably going to stalk you, so coming with me would make this significantly easier for the both of us."

    scene iseeyoureduxexhaust
    with dissolve

    y "Why the fuck do you have to be so...grossly honest all the time?..."

    scene black
    with dissolve2

    "Yumi begrudgingly starts walking alongside me down the street."
    "The second we make it to an intersection, she points out a small children’s park across the street and gestures that we should probably talk over there..."
    "........."
    "......"
    "..."

    scene grass1
    with dissolve2
    play music "blueair.mp3" fadein 5.0

    y "…"
    s "…"
    y "So are you gonna say anything or are we just gonna sit here in silence like fucking weirdos?"
    s "Depends, I guess. What would you rather do?"
    y "I’d rather keep walkin’ around by myself like I was planning."
    s "Is that really all you do for fun? Walk around by yourself?"

    scene grass2
    with dissolve

    y "No...I’ve got friends. They’re just at work and shit right now."
    s "Right, right. Friends..."
    s "You and Chika are pretty close, aren’t you?"
    y "Yeah. So? "
    s "Uhh, nothing. Just trying to make conversation."
    y "{i}That{/i} is what you want to talk about?..."

    "…"

    s "What’s that supposed to mean?"

    "Yumi pauses for a moment and begins to pull some grass out of the ground."

    y "Hey, I’ve got a great idea."

    scene grass3
    with dissolve

    if bonus == True:
        y "Instead of talking about that, how about we talk about the time you basically [rape]d me on the other side of town?"
    else:
        y "Instead of talking about that, how about we talk about the time you [rape]ged me on the other side of town?"

    y "That’s a thing I’d like to stop pretending didn’t happen."
    y "Do you have any idea how fucking weird it feels having you {i}still{/i} follow me around after that?"
    y "Do you think I’m easy or something?"
    y "Is it because I act up in[school]?"
    y "Is that what this is?"
    s "Yumi, I-"

    scene grass4
    with dissolve

    y "Shut the fuck up! I’m not done talking!"
    s "…"

    if bonus == True:
        y "I’m not like your secret-slut girlfriend Makoto, okay?!"
    else:
        y "I’m not like Makoto, alright?!"

    y "Or that fatass Futaba who’s clearly willing to just give herself to anyone desperate enough to take her!"
    y "And despite whatever it is you think about me, I have fucking feelings! And they're fucking hurt, okay?!"
    y "So never pull that shit again!"
    y "Got it?!"
    s "…"
    y "…"
    s "Got it..."

    scene grass5
    with dissolve

    y "Ugh...god damnit. Now I’m all fucking teary and shit."
    y "Forget this too. That’s part of the deal."

    "Despite how much I want to apologize, I can’t find it in myself to utter the words."

    if bonus == True:
        "I remember kissing Yumi but...it’s such a hazy memory that it almost doesn’t even feel real."
    else:
        "I remember hugging Yumi but...it’s such a hazy memory that it almost doesn’t even feel real."

    "But it’s clearly real to her."
    "That should be enough for me, right?"
    "That should be enough for me, right?"
    "That should be enough for me, right?"
    "That ssssshould be enough for me, right?"
    "Thaaaaatttts sghoiodudllld be enougyh forororo me rightttttttt>>>>>?????????"

    stop music
    scene grass6
    $ renpy.pause(2.5, hard=True)
    play sound "yayhappyyay.mp3"
    $ renpy.pause(19, hard=True)

    six "Tell me you see me."

    play music "sweetvermouth.mp3"

    if bonus == True:
        "Welcome to Lessons in Love, an adult dating simulation game!"
        "In Lessons in Love, you can use {i}Affection points{/i} to have sex with [young_girls]!"
        "If you play your cards right, some of them may even let you {s}remove their body parts{/s} cum inside!"
    else:
        "Welcome to Lessons in Love! A happy, all-ages video game that was definitely not censored in any way!"

    "The dorms are only accessible at night because, during the day, they don’t exist."
    "Do you exist?"
    "I do!"
    "Isn’t it wonderful to live?"
    "61 20 77 6f 72 6c 64 20 69 6e 20 77 68 69 63 68 20 77 65 20 6c 6f 76 65"

    play sound "static.mp3"
    scene grass7
    with flash
    stop sound
    stop music

    y "Tell me you see me."
    s "...What?"
    y "You zoned out and have been staring into space for like five minutes..."
    y "I was starting to think you went blind or some shit."
    s "Oh, no. I can see."
    s "I must have just dozed off for a second."
    s "I’m sorry for doing something like that at such a shitty time. I know you were being sincere."

    scene grass8
    with dissolve

    y "Yeah, whatever. I didn’t want to explode like that. "
    y "Just...don’t ever fucking take advantage of me again. I mean it."
    s "I won’t. Don’t worry."
    y "…"
    s "Can I ask {i}you{/i} a question now?..."
    y "...Yeah. What?"
    s "Do you really hate me? Or do you just pretend to hate me because you actually like me?"
    y "…"
    s "…"

    scene grass9
    with dissolve
    play music "yumiska.mp3"

    y "Yeah, I definitely fucking hate you."
    s "Oh."

    if bonus == True:
        y "In fact, after you forced yourself on me, I went home and made myself throw up like nine times."
    else:
        y "In fact, after you hugged me, I went home and made myself throw up like nine times."
        s "That seems like an overreaction."

    y "Chika even suggested bringing me to the hospital because I wouldn’t stop."
    y "I still have nightmares about it. It was the worst thing that’s ever happened to me, and I’ve seen people get curbstomped."

    if bonus == True:
        s "I mean, my memory of that kiss is kind of foggy, but I could have sworn you were kissing me back for most of it."
        y "As if. Like I’d ever actually kiss a fucking...perverted rapist like you."
        y "In fact, I’ve had enough of this weird ass conversation. Now, all I want to do is go home and make myself throw up {i}again{/i} for even remembering it."
        s "Yumi-"
        y "No. You've taken up enough of my time. Now, go force yourself on somebody else, dickwad. I'm done here."

    scene grass10
    with dissolve

    "Yumi gets up off the ground and shakes some grass and dirt off of her skirt."
    "She flips me off with an intense amount of vigor before turning around and heading back in the direction we originally came from."

    scene black
    with dissolve2

    "Instead of getting up and following her, I collapse onto the ground and close my eyes."
    "I can feel insects beginning to crawl on me in response, but I’m too tired to do anything about it."
    "I'm not sure where this sudden fatigue came from, but I would be lying if I said it was not a worthy opponent."
    "..."
    "I let it consume me and ultimately pass out."
    "I wake up with bites all over the nape of my neck."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ streets10 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has somehow increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label streets15:
...
```

## Code that triggers this event
File: \game\YumiEvents.rpy
Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
    if yumi_love >= 10 and day44 == True and streets10 == False:
        jump streets10
...
```