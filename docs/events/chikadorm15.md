# A Castle for Everyone
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikadorm15&go=Go)



## Event preconditions
✅Chika love greater than or equal to 15

✅Event "[Chika: Side Event](./chikadorm10.md)" is completed (event=chikadorm10)

✅Day of week is not Wednesday

✅Day of week is not Monday



## Next events
* [Main: Scientific Research](./day79.md)
* [Main: On The Bright Side](./day126.md)
* [Chika: A Dog that Doesn't Do Math](./mall15.md)

## Event properties
* ID: chikadorm15
* Group: Chika
* Triggered by label: chikadorm
* Triggered by branch label: chikadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label chikadorm15:
    play sound "knock.mp3"

    s "Hey, Chika. Are you in there?"

    "I knock on Chika’s door and wait a moment before pressing my ear to it."
    "I can’t hear anything from inside the room and it’s not like her to just {i}not{/i} answer so I guess...maybe she’s out?"
    "That makes sense. I mean, she seems popular enough to be doing all kinds of-"

    c "Heya! Looking for me?"

    scene castleredux1
    with fade

    "Out of virtually nowhere, Chika shows up in the dorm and comes to a stop just several inches away from me."
    "She’s still dressed in her uniform, so it’s probably safe to assume she's just getting back from school now for...whatever reason would have kept her late."

    c "Whatcha doing? Dropping by to visit?"
    s "Yeah. Figured I’d stop by and see if you wanted to hang out since I didn't have anything else going on."

    c "Hmmm..."
    s "{i}Hmmm{/i} what?"
    c "Nothing. It's just that...well, I can’t hang out here right now."
    c "{i}However...{/i}if you want to go on a little field trip, we could spend some time together. It would just require a little extra leg work."
    s "Well, like I said, it's not like I have anything else going on right now."

    if day < 6:
        c "I’m surprised you even showed up as early as you did. I feel like school ended just a little while ago."
    else:
        c "I’m surprised you even showed up as early as you did. You're normally here a little later."

    scene castleredux2
    with dissolve

    c "Glad I caught you when I did, though! Was beginning to wonder when I’d see you again."
    s "The next[school] day is always a safe bet."

    scene castleredux1
    with dissolve

    c "Oh, shut up. You know what I mean."
    c "Lemme just run inside and grab my overnight bag really quick."
    s "Overnight bag? Are you not staying in the dorm tonight?"

    scene castleredux2
    with dissolve

    c "Nope! Stayin’ somewhere else."
    c "Somewhere I was {i}thinking{/i} would remain a secret a little while longer, but...oh well. I'm fine with you knowing."

    scene castleredux3
    with dissolve

    c "Besides, you’ve kinda already been there once before."

    "Once before?"
    "Then..."

    s "The second half of town?"

    scene castleredux4
    with dissolve

    c "The...what?"
    c "I mean, I've never heard it called that before, but I think so?"
    c "It's the same place I dragged you to the other night."
    s "Do you have family living there or something?"

    scene castleredux5
    with dissolve

    c "Well...yeah. But it's a liiiiittle more complicated than that..."
    c "Do you mind if I just fill you in on the way? We’re gonna need something to talk about anyway since it’s a pretty long walk, so..."
    s "Oh, right. Sure. Go grab your bag and I'll just wait out here, I guess."
    c "Gotcha. Want a bottle of water or anything? Yumi has like six million of them, so I’m sure she won’t notice if we snag a couple."
    s "I'll be fine. Just do what you need to do."

    scene castleredux2
    with dissolve

    c "Roger that! Be right back, then."

    scene black
    with dissolve2

    "Chika is in and out of her room in no time at all and the two of us begin our journey to the second half of town."
    "It kind of sucks that we won't get to be alone on account of her family being around, but-"
    "Hey...wait a second."
    "Why did I just casually agree to meeting Chika's family?"
    "This isn't like me at all."

    scene castleredux6
    with dissolve2

    s "Hey...Are you really okay with me meeting your family?"
    c "Hm? Why wouldn't I be?"
    s "Because I'm twice your age."
    c "You're also my teacher. We could always use that as an excuse. Nobody needs to know we hang out in dressing rooms together and stuff."
    c "Besides, she’s probably sleeping right now anyway."

    "Good. I've at least confirmed that Chika's mysterious family member is female- which makes sense given her dad walked out on her and most of the men here are missing anyway."
    "But I still feel a little better going in knowing I'm not going to have to deal with some guy who would very easily see through my motives in spending time with this girl."

    s "Why would {i}she{/i} be asleep right now? The sun hasn't even finished setting yet."

    scene castleredux7
    with dissolve

    c "Boredom, probably. It's not like there's really much to do in our apartment."
    s "Then why doesn't she leave?"
    c "That's...where it gets complicated."

    scene castleredux8
    with dissolve

    c "But that’s also why I’m staying there tonight! I’ve got some stuff I’ve gotta go over with her anyway."
    c "Yumi was supposed to handle it this time, but-"
    s "Woah, hold on. Yumi?"

    scene castleredux9
    with dissolve

    c "Yeah. What's wrong with Yumi?"
    s "Well...we're talking about a kid, right? That's at least what I'm starting to think based on all you've said."
    c "We are, yeah. Do you think Yumi is bad with kids or something?"
    s "I think Yumi is bad with everyone."

    scene castleredux6
    with dissolve
    stop music fadeout 20.0

    c "Sensei, Yumi might be rough around the edges, but she isn't some kind of...demon."
    c "Her family, on the other hand..."
    c "Well, I guess that doesn’t matter right now. You ready to meet my little sister?"
    s "Ready as I'll ever be."
    c "Great. Before we go in, though, I do wanna warn you of something."
    s "She doesn’t bite, does she?"
    c "She hasn't yet. But she also hasn't been exposed to very many people, so I guess it's not, like, totally impossible."
    s "Well, apart from the potential biting, what's the issue?"

    scene castleredux10
    with dissolve

    c "She's, uhh..."
    c "How do I say this?"

    scene castleredux11
    with dissolve

    c "She’s...not really the strongest little girl out there. So don’t do anything that’ll get her too riled up, okay?"
    s "What do you mean?"
    c "She’s just got...{i}really{/i} bad asthma and could have an attack if she over-exerts herself."
    c "And like, I obviously know how to handle that and everything, but it can get really scary for both of us and...I’m sure you wouldn’t really want to be around for that..."
    s "…"
    c "And, uhh, since we’re already on the topic, I guess I should also mention that she’s got a bit of a...compromised immune system as well."
    c "So if you even {i}think{/i} you might be sick, you should probably, like...just wait outside and let me figure something out."
    c "I obviously won’t make you wait out there for the rest of the day, but-"
    s "I’m not sick. Don’t worry. Let’s just head inside and take things slow if it's really that serious."

    scene castleredux12
    with dissolve

    c "…"
    c "Yeah."
    c "Thanks."
    c "It is..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    play sound "dooropen.mp3"

    c "I’m home!"

    scene hellochinami1
    with dissolve2
    play music "gentle.mp3" fadein 10.0

    c "{i}Remember, don’t do anything that might rile her up.{/i}"
    s "{i}How exciting of a person do you think I am, exactly?{/i}"

    "The sound of a book slamming shut breaks our conversation before it's even built."
    "It's followed by the sound of small feet, clapping against an old hardwood floor and steadily moving closer to the kitchen."
    "This is the symphony of a girl who will struggle to live in ways much different than you and I."

    scene hellochinami2
    with dissolve2

    "An angel descends from on high."

    an "Hello!"

    "The girl stares at me, expecting me to wave back."
    "I attempt to lift my hand, but it appears that my muscle memory has decided to clock out for the evening."
    "Both curious at my arrival and suspicious of who I am and why I’m here, she puts her hand down and looks at her sister."

    scene hellochinami3
    with dissolve

    an "{i}Who is he?{/i}"
    an "{i}Why were you two whispering?{/i}"
    an "{i}Does Chinami need to whisper, too?{/i}"
    c "It’s okay, Chinami. You don’t have to whisper. I was just telling him a secret."
    ch "{i}A secret about what? Can you tell me next?{/i}"
    c "It wouldn’t be a secret anymore if I told you."
    ch "Hmm..."

    scene hellochinami2r
    with dissolve

    "The girl looks at me again and, for the first time in a while, I can time the beating of my heart without having to press my hand against my chest."
    "All of the horrible things that fill this horrible part of town evaporate into thin air and rush out of the cracks in the window near the door."
    "I remember something."
    "Somewhere."
    "Somewhere just like this."

    ch "Hello, sir. My name is Chinami Chosokabe and I am an ancient, powerful 5000 year old Wizard."
    c "Ignore the wizard part, please. She says that to everyone."
    ch "What’s {i}your{/i} name?"
    c "Chinami, this is my teacher. So you need to be good and make sure you don't do anything to get me in trouble, okay?"

    scene hellochinami4
    with dissolve

    ch "Why would something Chinami does get her big sister in trouble?"
    c "Because that's just how the world works, Chinami."
    ch "Chinami has had enough of this world."

    scene hellochinami5
    with dissolve

    ch "Can you be Chinami's teacher, too? She's so bored all the time and has to read too many books!"
    c "No, Chinami. He’s {i}my{/i} teacher. You’re gonna have to keep putting up with Yumi and me until you’re ready to go to[school]."
    ch "But Chinami has no idea when that will be. She wants to learn now!"
    c "Then Chinami should get back to the worksheets big-sis Yumi printed out for her and-"

    scene hellochinami6
    with dissolve

    ch "Are you my big sister’s boyfriend?"
    ch "You don’t really look like a teacher."
    c "Ch-Chinami! That’s totally rude! You know I don't have a boyfriend! And that's not something you can just ask people you're meeting for the first time!"
    ch "Make sure you treat her super nice, okay?"
    ch "Big sis works super hard so that Chinami can go to[school] with the other girls someday."
    c "Chinami! He's not my boyfriend!"

    "A situation I felt prepared for just minutes ago has managed to throw me into a state of utter shock."
    "I don't think I've said a single thing since she's shown up and I can't even figure out why."
    "Is {i}this{/i} really the secret that Chika’s been so desperately keeping from everyone?"
    "I don't understand."

    s "Chinami, does anyone else take care of you? Or is it just your big sister?"

    scene hellochinami7
    with dissolve

    ch "Chinami has two big sisters! Chika and Yumi!"
    ch "And also the people who deliver Chinami food! They’re Chinami’s family, too!"
    c "She, uhh...likes to order from this one breakfast place in town since I’m not always here to cook in the morning..."
    s "Do you spend a lot of time alone, Chinami?"

    scene hellochinami8
    with dissolve

    "The girl shakes her head and looks directly into my eyes."

    ch "Chinami is never alone!"

    scene hellochinami9
    with dissolve

    "The girl runs out of the kitchen and into the bedroom."
    "Chika falls silent and looks away as if she knows what's about to happen and understands that it's going to hurt her."
    "But she presses on regardless, like a wild animal caught in barbed wire."
    "I can hear a few things being moved around on a countertop."
    "Seconds later, the footsteps return."
    "But they’re so light it’s as if they barely exist in the first place."

    scene hellochinami10
    with dissolve2

    "The girl runs back into the room with an old picture frame clutched in her tiny fingers."
    "I already know who lives inside."
    "Chika’s reaction and the suppressed sounds of desperate gasps are more than enough to give it away."

    ch "Chinami is never alone because Mommy is always right here!"
    c "Chinami...put Mom away...we can't just..drag Sensei into our problems..."
    s "..."
    c "Sensei...I’m sorry for crying...I told myself I wouldn't, but..."

    "I have no idea what to do in situations like these. And despite an overwhelming lack of knowledge of where I come from, I think it's safe to say that I've been that way forever."
    "But really, though- what is a person to do when spontaneously thrown into something as heavy as this?"
    "All I can do is let the weight of it crush me."

    ch "Isn’t she pretty?"

    "Despite being the youngest of all of us, Chinami is the one who takes the reins and begins to steer away the awkward silence that had since filled the rundown apartment."
    "Angels are real."

    s "She’s very pretty, Chinami."
    s "You both look a lot like her."

    scene hellochinami10r
    with dissolve

    c "{i}Sniff...Sniff...{/i}You...think so?"
    ch "Chinami thinks so too! She wants to look just like Mommy when she’s older."
    ch "And then she wants to marry a prince and live in a castle! "
    c "They...{i}sniff...{/i}don’t build castles anymore, Chinami..."
    ch "Then Chinami will have her prince build her one!"

    scene hellochinami11
    with dissolve

    ch "Just like {i}you’ll{/i} build a castle for Chinami’s big sister."
    c "I...uhh...don’t...really need a castle, Sensei..."
    c "I'm fine...right where I am, so...we can just...I don't know..."
    c "I don't know anything..."

    "I wonder what type of life I would have had to have led in order to build a castle for someone."
    "Most likely one that took place centuries ago...but still-"
    "Right now, I feel like castles are more than just colossal structures or set pieces in medieval movies."
    "Sometimes, a castle is just a place where you feel safe."
    "And even if Chinami never finds a fairy tale prince-"
    "I’m sure that someone will build her a castle some day."
    "And if {i}they{/i} don’t, I will."
    "I’ll build a castle for everyone."

    ch "…"
    c "…"
    s "…"
    ch "Chinami’s ancient wizard powers tell her that she should go into the bedroom now."
    ch "But she’ll see you again!"
    ch "She can tell you’re a good person."
    ch "Please continue to be nice to her big sister."

    scene hellochinami12
    with dissolve2

    "The angel flies away without realizing the aftershock her wings cause."

    c "Well, uhh...this is embarrassing."

    scene hellochinami13
    with dissolve

    c "Chinami tends to make, umm...{i}very strong{/i} first impressions...so I'm sorry if this was a little too much."
    s "Do I get bonus points for not riling her up?"

    scene hellochinami14
    with dissolve

    c "Hahah...You’ve been racking up a lot of those lately, haven't you?"
    c "Any idea of what you're going to cash them all in on?"
    s "..."
    c "..."

    scene black
    with dissolve2

    s "Maybe a castle."

    "I don’t hang around much longer after that."
    "As it turns out, tonight is Chinami's {i}homework night{/i}, so me being around would just serve as a distraction."
    "I feel a little weird knowing that I, a professional teacher, am now viewed as a distraction when it comes to education, but I guess I understand."
    "Before I leave, Chika tells me about how she and Yumi have been homeschooling Chinami for a couple years now."
    "Her immune system is bad enough to prevent her from going to[school] with the other kids her age."
    "And without enough money for treatment, if there even {i}is{/i} treatment, all she can really do is keep trying her best and hope to one day grow stronger..."
    "..."
    "I'll be rooting for her."
    "As hopeless as it may be."

    $ renpy.end_replay()
    $ chikadorm15 = True
    $ chika_love += 1
    stop music fadeout 6.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm5:
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
            if chika_love >= 10 and mall10 == True and chikadorm5 == True and chikadorm10 == False:
                jump chikadorm10
            if chika_love >= 15 and chikadorm10 == True and chikadorm15 == False and day != 3 and day != 1:
                jump chikadorm15
...
```