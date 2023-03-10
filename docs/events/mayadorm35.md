# A Place That Can Only Exist in Our Minds (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 35

* Event [What it Means to Be Destroyed](./mayadorm30.md) (Maya) is completed)

* Day of week is a weekend

* Event [Like it's Any Other Day](./nikidate5.md) (Niki) is completed)



## Next events

* [Maya: Stop Looking For Answers](./shrine35.md)
* [Makoto: Condoms in the Sand](./makotowinterbeach1.md)

## Event properties

* Id: mayadorm35
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm
* Triggered by path: mayadorm->mayadorm35

## Official wiki page

[A Place That Can Only Exist in Our Minds](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm35&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm35:
    play sound "knock.mp3"
    stop music fadeout 20.0

    "I knock on Maya’s door, awaiting whatever sort of excuse she’s going to throw at me tonight that will keep me from coming inside."
    "I’ve just accepted it at this point."
    "There are some people out there who won’t let you know anything about them unless they absolutely have to."
    "People like me."
    "Sure, a lot of that is because I can’t remember much of my story."
    "But, even if I did-"
    "I don’t think I’d want to share it with anyone."
    "My thoughts and my experiences are mine and mine alone."
    "Just like Maya’s are hers and hers alone."
    "And the two of us are destined to forever remain that way. "
    "Detached from not only each other but the entire world around us."
    "Floating freely toward a place that can only exist in our minds."

    m "What do you want?"
    s "To see you."

    "I blurt out something smooth."

    m "Ew."

    "It’s not very effective."

    s "Can I come in?"
    m "…"
    s "Maya?"
    s "You normally reject me right away."
    s "Does this mean I’m actually allowed in tonight?"
    m "Is there anyone in the hall right now?"
    s "Right now? No. It’s totally empty."
    m "…"
    m "Fine."
    m "You may enter."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Blowing up in class...pleading for help at[school]...letting me into her room-"
    "Maya is changing."
    "Whether that change is good or bad is yet to be determined."

    scene imissyou1
    with dissolve
    play music "beginningoftheend.mp3"

    m "Please make this quick. I’m very tired."
    s "Well then you probably shouldn't have invited me in."
    m "If I didn’t, you would have just stood out there knocking until I caved."
    m "This was the easiest way to put an end to that."
    m "So go on, get to tonight’s helping of witty banter and be on your way."
    s "Wow. Now I’m feeling really pressured all of a sudden. "
    s "I’m not sure if I can come up with something witty enough for you off the top of my head."

    "A light in Ami’s side of the room begins to flicker."
    "It makes that soft, sad electrical noise you hear from some devices in the moments leading up to their deaths."
    "Any moment now, that light is sure to burn out."
    "I wonder what else will burn out tonight?"

    scene imissyou2
    with dissolve

    m "Why do you keep coming here when you know I don’t want you to?"
    s "Who knows? Maybe I’ve just been worried about you lately."
    m "You do realize that you wouldn’t have to worry at all if you’d just listen to me, right?"
    s "I don’t necessarily have a problem with worrying. "
    s "It’s nice being reminded that I’m not just some mindless affection robot wandering from dorm to dorm in exchange for more love points or something."
    m "Well I, for one, think it’s exhausting having to worry so much about everything."
    m "Which is why I’ve resigned myself to bed already while everyone else is out having fun."
    s "Are you sure that’s you being tired and not just you being a loser?"

    scene imissyou3
    with dissolve

    m "Yes. I’m extremely sure."
    m "Will that be all?"
    s "It will not."
    m "Then what else do you want?"
    s "To see you smile."

    "I try to be smooth again."

    m "Ew."

    "It’s not very effective."

    m "What reason would I possibly have to smile right now?"
    m "Things are happening that I can’t predict. People are showing up that I’ve never seen before."
    m "And to top it all off, I’m expected to just casually converse with the root of all of my problems in a dimly lit bedroom when all I want to do is sleep."
    s "Would you prefer I go talk to your friend Noriko instead?"

    scene imissyou4
    with dissolve

    m "Wait! "
    m "No..."
    m "I’m...just..."
    m "Stressed..."
    m "If staying here and annoying me keeps you away from her...fine. Whatever."
    m "I’ll stay awake all night if that’s what it takes."
    s "I feel like I should be happy for finally finding the key to spending more time with you..."
    s "But really I just feel even more worried than I did before."
    m "Yes. Good. Worry about me if that’s what you need to do."
    m "Just..."
    s "…"
    s "Just what?"

    scene imissyou5
    with dissolve

    m "Hah..."
    m "I don’t know. I don’t like being seen like this."
    s "Really? I think you look cute in your pajamas."
    m "I’m not talking about that...I’m talking about the way I’m acting, idiot."
    m "People who so freely express themselves are strange. I don’t know how they do it."
    s "What are you trying to express, exactly?"

    scene imissyou6
    with dissolve

    m "…"
    m "Urgency?"
    s "Urgency in what way?"
    m "Whichever way keeps you here the longest."
    s "Correct me if I’m wrong, but isn’t it normally the other way around?"
    m "There is nothing normal about anything anymore."
    s "Well what’s the reason for the sudden attachment then?"
    s "Why wait until someone you despise shows up to start saying things like that when I’ve been trying to get closer to you since I first came to the shrine?"
    m "…"
    s "…"
    m "Let’s sit down."
    m "We’re about to start a conversation that would be much easier if we’re both comfortable."
    s "…"

    scene black
    with dissolve2

    "Maya turns away from me and takes a seat on her bed."
    "I expected her to use the kotatsu since it would help her keep her distance from me-"
    "But I guess that sometimes even stray cats want attention."
    "Hopefully, this particular stray guides me toward what it is she’s looking for tonight."
    "I can only keep coming back to her for so long when there are so many other cats I also have to take care of."

    scene imissyou7
    with dissolve

    "Maya looks at me with a tinge of desperation that I don’t know what to make of."
    "Like she wants to say something, but fears that doing so would break the world or kill all of us or whatever other sort of catastrophic things could happen due to...time stuff."
    "Maybe one day I’ll actually understand how any of this works."

    m "…"
    s "…"
    s "Are you uncomfortable?"
    m "I’m not."
    s "You definitely look like you are."
    m "Okay, I am. But not for the reasons you’re thinking of."
    m "It’s true that you’re entirely too close right now, but what {i}really{/i} makes me uncomfortable is figuring out how I am supposed to tell you this."
    s "…"
    m "…"

    "I remain silent and let her discomfort course through her veins and infect the rest of her tiny body."
    "There’s no need for me to talk during a time like this. Which works out wonderfully because-"

    play sound "static.mp3"
    scene whygodwhy with flash
    scene imissyou7 with flash
    stop sound

    "Because..."
    "What was I thinking just now?"

    m "You..."
    m "Are not who I thought you were at first."
    m "Well, you still might be. But there’s a high likelihood you’re not."
    s "Who did you think I was at first?"
    m "Not you."
    s "…"
    s "That doesn’t help."

    scene imissyou8
    with dissolve

    m "Hah...the fact that you still pretend to be so dense during times like this is even further proving my thoughts correct."
    m "And...this is hard to do since I can’t reveal too much without the fear of-"

    play sound "static.mp3"
    scene whygodwhy with flash
    scene imissyou9 with flash
    stop sound

    s "…"
    m "…"
    m "Sensei?"
    s "…"
    s "Without the fear of what?"
    m "Are you..."
    m "Seeing things, perhaps?..."
    s "I’m totally fine."
    m "You’re not even looking at me anymore."
    s "If I look at you, something bad will happen."
    m "…"
    s "…"

    scene imissyou10
    with dissolve2

    m "Who says it has to be bad?"
    s "…"
    m "What will happen if you look at me?"
    s "…"
    m "You {i}are{/i} seeing things, aren’t you?"
    m "Do you..."
    m "Do you see them when you’re with {i}her{/i} as well?"
    m "Shouldn’t that be telling you something?"
    m "This is exactly what I was trying to say to you just a minute ago..."
    m "You...might just be {i}you{/i}."
    m "And all of those things that..."
    m "All of those things that you’re seeing..."
    m "You..."
    m "Might be..."
    m "{s}sssssssssssssssssssssss{/s}"
    m "{s}kkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    scene black
    stop music
    $ renpy.pause(10, hard=True)

    "There was a time,"
    "And this was many years ago,"
    "That I picked a baby bird out of a nest."
    "And squeezed until its eyes escaped its head."
    "I didn’t have to squeeze very hard."
    "For this bird was young."
    "And its eyes weak."
    "They had seen so little-"
    "That it was like removing the seeds from a pomegranate."
    "I’m so sorry."

    play sound "static.mp3"
    scene ayhh1 with flash
    scene ayhh2 with flash
    scene ayhh4 with flash
    scene ayhh7 with flash
    scene ayhh8 with flash
    scene ayhh9 with flash
    scene ayhh10 with flash
    scene ayhh12 with flash
    scene ayhh15 with flash
    scene ayhh16 with flash
    scene black with flash
    stop sound
    play music "painisreal.mp3"

    "There was a time,"
    "A very happy time,"
    "That a bird existed."
    "It had so many eyes."
    "They were all beautiful."

    play sound "static.mp3"
    scene whyme with flash
    scene imissyou11 with flash
    stop sound

    m "Sensei! Hey!"
    m "Keep your eyes open!"

    "A bird lays its nest on top of me."
    "Instead of wings, it has tiny hands."
    "Its eyes are beautiful and filled with tears."
    "I didn't realize birds could cry."

    m "This is exactly what I was talking about! "
    m "The more you remember, the harder it will be!"
    m "Look at me!"
    m "Sensei!"

    if bonus == True:
        play sound "static.mp3"
        scene imissyou12
        with flash
        scene imissyou11
        with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown
        with flash
        scene imissyou11
        with flash
        stop sound

    "I open my eyes for the very first time and imprint on what appears before me."
    "Maya Makinami. Occupation: Student.\nHobbies: Violin, manga, unnecessarily long daytime naps.\nStatus: Broken beyond repair."

    m "I told you to stay away from her, didn’t I?!"
    m "This is what happens when you don’t listen to me!"
    m "What do you want?! What can I do?!"

    scene imissyou13
    with dissolve2

    m "Wait...hey...here's an idea..."

    if bonus == True:
        m "Do you want me instead?..."
        m "Will that be enough to keep you away from her?..."
        m "Cause I’ll do it..."
        m "I’ll do it right now..."
        m "I know exactly what it is you like, Sensei..."
        s "Don’t."
    else:
        m "Why don't I rub your tummy and call you a good boy"
        m "Will that be enough to keep you away from her?..."
        s "Hmmmmmmmm..."
        m "Cause I’ll do it..."
        m "I’ll do it right now..."
        s "Actually...don't."

    scene imissyou14
    with dissolve

    m "Don’t?..."
    m "But...why?..."
    s "Don’t do things you..."

    if bonus == True:
        play sound "static.mp3"
        scene imissyou12
        with flash
        scene imissyou14
        with flash
        stop sound
    else:
        play sound "static.mp3"
        scene imissyou12
        with flash
        scene imissyou11
        with flash
        stop sound

    m "I’m not doing something I don’t want to do!"

    if bonus == True:
        m "If you want to learn more about your past, do what I suggested the other night! Rely on sensations!"
        m "You feel something, don’t you?!"
        m "Do you remember?"
        m "Do you remember how far back we go?"
        m "Why you left that fucking crazy psycho bitch?"

        scene imissyou15
        with dissolve

        m "Why don’t I just {i}help{/i} you remember?"
        m "You don’t have to do anything, Sensei."
        m "Just lay there on your back and let me do all the-"
        s "I am no orniphile."
        s "Unhand me, bird woman."
    else:
        m "I really do think you're a good boy!"
        m "You're just a little misguided!"
        s "I am no orniphile."
        s "Unhand me, bird woman."

    scene imissyou16
    with dissolve

    m "Wha-"
    m "Orniphile?..."
    m "It’s me, Maya. I’m not a..."

    scene imissyou17
    with dissolve2

    if bonus == True:
        m "…"
        m "Huh?..."
        m "It’s...not even hard?..."
        m "But...by now it...would always..."
    else:
        m "Wait...where did you get this shirt? It's so soft."

    scene imissyou18
    with dissolve2

    "A strange sensation sweeps over my lower body."
    "I think this creature might be trying to remind me of something."
    "Like what it means to love."
    "Or perhaps something easier, like how humans can fly."
    "The bird begins to weep and cry out, but I’m not well-versed in the noises these creatures make, so it could very well be something like a mating call."
    "It would certainly make sense at this point given the nature of our meeting."
    "Why did I come here again?"
    "Birdwatching, perhaps?"
    "Or was it something else?"

    play sound "static.mp3"
    scene tree3 with flash
    scene imissyou19 with flash
    stop sound

    m "STOP FUCKING AROUND!"
    s "…"
    s "Maya?"

    scene imissyou20
    with dissolve

    m "That’s right. It’s me, Maya."

    if bonus == True:
        m "Let’s have sex."
        s "What happened? Weren’t we just talking about-"
        m "Let’s have sex."
        s "What? No. Tell me what’s going on."
    else:
        m "Bring it in, buddy. Gimme a big hug."
        s "But you hate hugs."
        m "I said hug me, you fucking doofus."
        s "What? No. Tell me what’s going on."

    scene imissyou19
    with dissolve

    m "I can’t! Not if you’re going to zone out like that!"
    m "I already told you too much!"
    m "Which {i}really{/i} pisses me off by the way since Noriko can apparently tell you {b}EVERYTHING{/b} without you hallucinating {i}her{/i} as a fucking animal!"
    s "Maya...I think you might want to get some rest."
    s "I don’t know what’s going on with you, but you’re clearly exhausted."

    scene imissyou20
    with dissolve

    m "Hahah..."
    m "Hahahahahahah! Exhausted!"
    m "Yup!"
    m "I’m so exhausted!"
    m "I haven’t been this tired in a LONG FUCKING TIME!"
    m "GOODNIGHT, SENSEI. TIME TO GO TO SLEEP AND RETURN TO BEING A NORMAL TEENAGE GIRL IN THE MORNING."
    m "THANKS FOR DROPPING BY TO REMIND ME OF HOW HORRIBLE THIS WORLD CAN BE!"

    scene black
    with dissolve2

    "Maya climbs off me and sits perfectly straight up."
    "It’s the same seiza position I’ve seen her take at the shrine time and time again."
    "She doesn’t say another word, which is fine because it’s not like I had any idea what to say to her after all of that in the first place."
    "It’s like one second, the two of us were talking about-"

    if bonus == True:
        play sound "static.mp3"
        scene whereareyou with flash
        scene black with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown with flash
        scene black with flash
        stop sound

    "It’s like one second, we were just talking and...she somehow wound up on top of me."
    "…"
    "I really hope this doesn’t make things awkward between the two of us...but I can’t imagine there’s any way it won’t."
    "It’s so strange, though."
    "It all happened so quickly."
    "So quickly that I can’t even remember how it happened."
    "I return home to find Ami already fast asleep."
    "Now miles apart, Maya and I return to being detached from one another."
    "Detached from the entire world around us."
    "But that’s okay."
    "Because we’re both still floating freely toward a place that can only exist in our minds."
    "I hope that place is as beautiful as her when she cries."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayadorm35 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amidorm40:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
        if maya_love >= 20 and shrine20 == True and yumidorm10 == True and mayadorm20 == False:
            jump mayadorm20
        if maya_love >= 25 and shrine25 == True and mayadorm25 == False:
            jump mayadorm25
        if maya_love >= 30 and mayadorm25 == True and norikoinvite2 == True and mayadorm30 == False:
            jump mayadorm30
        if maya_love >= 35 and mayadorm30 == True and day > 5 and nikidate5 == True and mayadorm35 == False:
            jump mayadorm35
...
```