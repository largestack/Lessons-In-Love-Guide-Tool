# The Color of a Heart (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The WAP Man](./day295.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: Call Me By Your Name](./day297.md)

## Event properties

* Id: day295parttwo
* Group: Main
* Triggered by label: day295
* Chain sources: day295
* Chain sources path: day295

## Official wiki page

[The Color of a Heart](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day295parttwo&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label day295parttwo:
    scene nightskysepia
    with dissolve2
    play music "andlove.mp3" fadein 3.0

    "I notice a distinct lack of color on my walk home."
    "I don’t typically leave[school] this late, nor do I remember how exactly the time managed to go by as quickly as it did."
    "And yet, here I walk under dimly lit streetlights emitting a soft buzzing noise signalling that the end of their days approaches."
    "It reminds me of a noise I’ve heard recently, but can’t remember where or when."
    "I don’t look down as I walk."
    "I keep my eyes focused on the sky."
    "It’s unsafe, sure. But I’ve walked this path time and time again and have yet to truly get lost."
    "Or at least “lost” by the common definition of the word and not some more artistic way of describing it."
    "Actually, since we’re on the topic of art, there’s something I’d like you to look at."

    play sound "static.mp3"
    scene redstring with flash
    stop sound

    "Before you lies a line. "
    "And if you align that line alongside lines of lies you tell yourself so you can sleep at night-"
    "You have something red."
    "And red is an evil color."
    "Or so many would like you to think."
    "But I think red can be beautiful under the right circumstances."
    "A gift carefully wrapped underneath a Christmas tree."
    "A fledgling cardinal taking flight for the first time."
    "The color of a heart."
    "How can red be a bad color when things like all of these bring smiles to our faces?"
    "Tug the line."
    "Tug the line and cross it. "
    "Tie it around all of the things you love and pull them along, dragging them across rough terrain until their skin (If applicable) begins to wear away."

    play sound "static.mp3"
    scene redstring2 with flash
    stop sound

    "I feel arms {s}warp{/s} wrap* around me, the same way I’ve felt them countless times in the past."
    "My sinuses have become mostly clogged from the temperature of both the air and the snow dancing around me as I try to reopen my already opened eyes."

    play sound "static.mp3"
    scene clearnightsky with flash
    stop sound

    "I see a sky, but it isn’t the right one."
    "It’s not the sky I saw just moments ago."
    "And it forces me into a state of worry that I have somehow gotten lost in a more literal sense than I’d been alluding to before."
    "Why does everything have to hurt so much?"

    play sound "static.mp3"
    scene yasuwhite1
    with flash
    stop sound

    sg3 "Oh, how pitiful it is to lose yourself once again."
    sg3 "To find yourself trapped in a state of being that you can not influence and yet, somehow or another, pray to move your own limbs."
    sg3 "To think your own thoughts."

    play sound "static.mp3"
    scene yasuwhite2
    with flash
    stop sound

    sg3 "Oh, how pitiful you are to find yourself lost."
    sg3 "To wander so aimlessly through the dark in search of...what?"
    sg3 "Salvation?"
    sg3 "Is that why you are here?"
    sg3 "Has the time finally come for you to {b}BREATHE?!{/b}"

    play sound "static.mp3"
    scene yasuwhite3
    with flash
    stop sound

    sg3 "Why does everything have to hurt so much, you ask?"
    sg3 "Wouldn’t it be wonderful if the answer was something like, “So we can feel alive?”"
    sg3 "Oh, how glorious that would be."

    play sound "static.mp3"
    scene sky with flash
    scene noonsky with flash
    scene wintersky with flash
    scene nightsky with flash
    scene clearnightsky with flash
    scene yasuwhite4 with flash
    stop sound

    "I happen upon a girl in a white dress, standing still under the only living streetlight I can see."
    "She shouldn’t be out this late. "

    if bonus == True:
        "Bad things tend to happen to girls who stay out this late. Especially ones as cute as her."
        "Thoughts happen."
        "You don’t want to hear about them."
    else:
        "She should be doing her homework."

    sg3 "I’ve come out of hiding, Sensei."
    s "…"
    s "Have we met somewhere before?"
    sg3 "Have you forgotten me already? How sad."
    sg3 "I may have interrupted a private conversation you were having with a girl around my age several months ago."
    sg3 "She was wearing a dress not much different from mine at the time. A dress I can no longer wear."

    "The girl remains remarkably still, letting snow fall on top of her already snow-colored hair. Never blinking, even once."
    "I think for a moment about whether or not those with blue eyes see everything in a slightly bluer tint and then, in a matter of seconds, wind up slipping toward the idea of the color red once again."

    sg3 "Do you need me to remind you?"
    s "What, can you teleport us back in time or something?"
    sg3 "Let me close my eyes and try."

    scene yasuwhite5
    with dissolve

    "The girl actually closes her eyes and I think to myself that she must be messing with me."

    scene yasuwhite4
    with dissolve

    sg3 "I’m sorry, but it doesn’t appear that I have that power. "

    "Yup. Definitely messing with me."

    s "Forget that. What are you doing out here just...standing under a streetlight?"
    s "It’s the middle of the night and it’s freezing cold."
    sg3 "Are you worried about me?"
    s "Not particularly. It’s just weird."
    sg3 "Can you come closer? I would like to continue speaking with you, but my voice does not carry very well."
    s "…"

    "Something tells me that I have nothing to gain from obliging, but..."
    "There’s a morbid curiosity deep within me. A curiosity deeper than the thoughts of lines or lies, that moves my limbs without my consent."

    scene yasuwhite6
    with dissolve

    sg3 "Am I truly so forgettable? That’s no good at all."
    s "I remember you. You’re that crazy girl who showed up in the park when I was with Sana."
    sg3 "Sana..."
    sg3 "That is such a pretty name."
    sg3 "Almost as pretty as her brother’s."
    s "…"
    s "Do you...know his name?"
    sg3 "Perhaps."
    s "How?"
    sg3 "If I told you, would you run away?"
    s "There aren’t many things that can make me run away from a girl your size."
    s "But if you’re somehow communicating with my students’ dead relatives...yeah. I’d probably consider booking it."

    scene yasuwhite7
    with dissolve

    sg3 "Hahahahahah!!! Hahahahaha!"
    sg3 "An unexpected response! How delightful it is to see you stand as still as a cross instead of running away!"
    s "I take it you’re pretty used to people running away from you, huh?"

    play sound "static.mp3"
    scene yasuwhite8 with flash
    stop sound

    sg3 "Why does everything have to hurt so much?"
    s "Oh. Okay. I guess we're moving on, then."
    s "Do you like...need something, or?"

    scene yasuwhite9
    with dissolve

    sg3 "We all need something. "

    if bonus == True:
        sg3 "Water. Food. Sex. Sleep. "
    else:
        sg3 "Water. Food. Trying to drown fish and failing miserably. Sleep. "

    sg3 "Without these pillars of existence and the endless pursuit of true bliss, we are but puddles of unused potential slowly dripping into sewers through grates on the ground."

    if bonus == True:
        s "No offense, but you don’t really strike me as someone who revels in sex."
    else:
        s "No offense, but you don’t really strike me as a fish drowner."

    scene yasuwhite10
    with dissolve

    sg3 "Of course not. I'm as pure as the snow."

    if bonus == True:
        sg3 "My chastity is proof of a love much greater than I could ever have."
        sg3 "More pliable than flesh and more pure than water from the cleanest spring in all the land."
        sg3 "But I’m sure someone like you doesn’t need to hear that from a lowly messenger, do you?"
    else:
        sg3 "Besides, {i}do fish even real???????????{/i}"

    s "I have no idea what that is supposed to-"

    play sound "static.mp3"
    scene yasuwhite11
    with flash
    stop sound

    sg3 "You know exactly what that is supposed to mean. "
    sg3 "You can hear things too. You can see things."
    sg3 "I can see that you see things. And I am a seer, so what I see is real."
    sg3 "You can only feign ignorance for so long."
    s "I’m not feigning anything, I really haven’t-"

    play sound "static.mp3"
    scene yasuwhite6
    with flash
    stop sound

    sg3 "Then you must be either truly callous or truly dense. And I pray that it’s the latter for both of our sakes."

    "This girl is insane. "

    s "I really don’t care about whatever you pray for, but you should probably try and find a place to stay for the night."
    sg3 "And if I have nowhere to go, will you escort me to your stable like a lost, little lamb?"
    s "I mean, I don’t have a stable, but you can crash at my place if you want. "

    if bonus == True:
        s "I’m locking my door, though. You’re cute, but not cute enough for me to risk my life over."
        sg3 "I have no reason to hurt you. Nor anyone else."
    else:
        s "I’m locking my door, though. I sleepwalk sometimes and I don't want you to see me in my onesie."
        sg3 "I have no interest in onesies."

    sg3 "I exist solely to communicate. To spread the word of {s}GOD{/s} {s}god{/s} {s}GoD{/s} God and to bathe in his light."
    sg3 "Light that you have the pleasure to bathe in whenever you want, and yet you stray further into the dark and further away from the answer to everything."
    sg3 "You are special."
    sg3 "Much more special than someone like me."
    s "That's probably not something you should be saying to unfamiliar men in the middle of the night."
    sg3 "Nothing bad will ever happen to me, for I am blessed."
    sg3 "And, even if something bad {i}did{/i} happen, it would be for a reason. It would be for something larger."

    play sound "static.mp3"
    scene yasuwhite12
    with flash
    stop sound

    sg3 "Why do you continue to wait?!"
    sg3 "Why do you make {s}me{/s} him wait?!"
    sg3 "Why is there so much waiting?! Every hand on every clock is moving! They tick! They tock!"
    sg3 "Time marches on and yet you remain still!"
    sg3 "Still still still still still!"

    play sound "static.mp3"
    scene yasuwhite8
    with flash
    stop sound

    sg3 "Why does everything have to hurt so much?"
    s "…"
    s "You know, maybe we {i}should{/i} get you back to my...stable. You’re clearly delusional from the cold and-"

    scene yasuwhite10
    with dissolve

    sg3 "Stables are for animals, Sensei."
    sg3 "I am not the little lamb you think I am."
    sg3 "If anything, you are the lamb. And I am the shepherd, here to guide you to where you need to be."
    sg3 "If only you were willing to open your heart wide enough to be accepted there."
    s "Sorry, opening my heart isn’t really a strong suit of mine."
    s "I prefer to keep everything locked away. And, honestly, I’d prefer it if you would do the same. You’re kind of freaking me out."
    sg3 "The things I do with my body and mind are not of my own choice. I am but a vessel for the one so commonly mislabeled. "
    sg3 "A god not as old as the {i}others,{/i} but dying just the same."
    sg3 "If you were to find a dying animal on the side of the road ...a lamb, convulsing after being hit by a car. Coughing up blood..."
    sg3 "Would you ignore it? Or would you attempt to save it?"
    s "I’d probably convince myself I never saw it and just keep walking."

    play sound "static.mp3"
    scene yasuwhite13 with flash
    stop sound

    sg3 "Does that fulfill you? "
    sg3 "Does it not haunt you when you crawl into bed at night?"
    sg3 "It’s all real. Everything you see is real. Everything you feel is real. If it exists to you, it is real."
    sg3 "What else would it mean to be real in the first place?"
    s "I get that you’re a missionary or whatever, but comparing your god to a dying animal isn’t really all that convincing if you’re trying to convert me."

    play sound "static.mp3"
    scene yasuwhite14
    with flash
    stop sound

    sg3 "You can not convert someone who doesn’t believe in anything. "
    sg3 "You can only wait patiently and explain. "
    sg3 "Which is why my “dying animal” is the answer to all things."
    sg3 "It is a dying animal that will lay there, convulsing and coughing up blood until someone reaches out their hand."
    sg3 "Eternally writhing in pain for the sake of giving others a chance to be saved."

    scene yasuwhite9
    with dissolve

    sg3 "Which is precisely why everything needs to hurt so much."
    sg3 "I hurt because you hurt. You hurt because I hurt. He hurts because all of us hurt."
    sg3 "We are all but dying animals. So when we see someone else having a particularly hard time, we must offer our assistance."

    scene yasuwhite6
    with dissolve

    sg3 "I reach out my hand to you. Take it if you will. For I may not be able to show you the light myself, but I can take you somewhere brighter."
    sg3 "I know where the sanctuary is. And I can show you the moment you decide to open yourself up to something greater."
    sg3 "Come with me."
    sg3 "I can show you such beautiful things."
    sg3 "I ask for nothing in return. Nor could I if I wanted to."
    sg3 "I am only a vessel."

    "The wind begins to pick up and rapidly blow the strange girl’s hair around. "
    "It whips her in the face and turns her already rosy cheeks an even darker shade of red."
    "But she does not attempt to stop the pain that comes with her own body being turned into a weapon."
    "She just grips her necklace and looks deep into my eyes."
    "Deeper than I would ever want anyone to."

    s "What is your name?"
    sg3 "My name?"
    s "Yes. I’m not asking to be friends or anything, but it would probably be good to know in the event that we run into each other again."
    sg3 "We will run into each other many more times."
    sg3 "But I do not have a name. Nor do I need one."
    sg3 "There is no sense in having a name when I exist not for myself but-"
    s "For “the one so commonly mislabeled.” Right."
    s "Whatever. That’s fine, I guess."
    s "I really don’t want to spend the entire night listening to you ramble on about that, though, so I’m probably going to head out now."
    s "Are you sure you’re okay out here? You don’t need a place to stay or anything?"
    sg3 "I thank you for the offer, but I am fine as I am."
    sg3 "I have somewhere I need to be anyway."
    s "Suit yourself, then. "
    s "Any creepy parting words for me before I go?"

    scene yasuwhite15
    stop music

    sg3 "Yes."
    sg3 "You are surrounded by whispers."
    sg3 "Someone misses you very much."
    sg3 "Tick tock."

    scene yumis4

    "74 6f 20 77 68 61 74 20 64 6f 65 73 20 69 74 20 6d 65 61 6e 20 74 6f 20 62 65 20 63 61 6c 6c 6f 75 73 "

    $ renpy.end_replay()
    $ god_love += 1
    $ day295parttwo = True
    scene black

    "{i}Your affection with {s}GOD{/s} {s}god{/s} {s}GoD{/s} has increased to [god_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label day297:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
scene tsubasaofficevisit18
    with dissolve

    tb "I’d also like it to be known that it wasn’t just the presence of those two bright, [young]stars that forced my hand in making this decision. "
    s "What was it then? Because I was pretty confident my first impression was...not very good."

    scene tsubasaofficevisit19
    with dissolve

    tb "It was what this girl right here had to say about you during a lengthy conversation at the {i}petting zoo{/i} about the way you make her feel."
    tb "That told me everything I needed to know about you as a teacher."
    tb "And while your methods are certainly...unorthodox, I am going to assume that was simply due to the fact that it was a special occasion."

    scene tsubasaofficevisit20
    with dissolve

    tb "My daughter does not have a very easy time...opening up to people. "
    tb "She is a wonderful [young_girl]...and extremely dedicated when it comes to both the family business as well as her academic life."
    tb "But she has a history of being rather...uninspired when it comes to those who have been fortunate enough to teach her."
    tb "And so, in knowing that you are able to see your students as more than just minds to mold, I’ve decided to take a leap of faith and put her in your hands."

    scene tsubasaofficevisit21
    with dissolve

    tb "I can’t guarantee she’ll be entirely cooperative to begin with, but I can assure you that she is unreasonably kind at heart and wants nothing more than to fit in."
    s "…"

    if bonus == True:
        "You know, only I would be lucky enough to somehow gain the trust of the wealthiest woman in Kumon-mi by audibly deflowering a girl the same age as her daughter in the room right next door."

    s "I mean...if that’s what you think is best for her, she can definitely hang out."

    scene tsubasaofficevisit22
    with dissolve

    tb "{i}Hang out.{/i} I love that! It’s so informal that it’s as if you don’t view your students as students at all."
    s "Yes. That exact principle is the single largest pillar in my teaching strategy."
    mak "I mean...it’s certainly not {i}not{/i} working?"
    c "Yeah. Weirdly enough, having someone like Sensei around is the exact motivation I needed to really start putting myself back on track."
    c "And, if your daughter is anything at all like you, I’m sure that she and I will get along great."

    scene tsubasaofficevisit23
    with dissolve

    tb "That would mean so much to me, dear. Please make her feel at home if at all possible."
    c "Of course! Anything for you, Tsubasa!"

    "The gap between first and second place on Chika’s secret MILF ranking widens."

    mak "Well...I guess that’s that, then."
    mak "Miss Tsukioka just wanted to formally touch base with you and confirm that you were, indeed, the “WAP” man."
    tb "I have decided to embrace my poor usage of the “WAP” and convert it into a multifunctional tool for describing good people!"
    c "{i}Cooooooool.{/i}"

    scene tsubasaofficevisit24
    with dissolve

    tb "So, would this Friday work as her first day in your class?"
    tb "We’re still in the process of relocating her to a second, smaller house in the area so the commute will be less strenuous on her, but we should be finished within the next day or two."
    s "You’re...getting her her own house?"
    tb "Of course. It’s the very least we can do to reward her for all of this."
    tb "She was quite resistant to the idea at first, actually. But she eventually came around after seeing how many people were flocking to this[school]."
    s "That’s great and all, but she could just move into the dorms instead. She doesn’t need a whole house."
    tb "Ooooooh, I see. I see."
    tb "But, what is a “dorm” exactly?"
    s "It’s like...an apartment specifically designed for people attending[school]."
    tb "My, that sounds like it would be absolutely splendid once she’s ready for it."
    tb "But I do think we should at least wait to see if she’s able to seamlessly transition into the actual[school] first before making a commitment like that."
    s "Hey, whatever works for you. She’s your daughter. I’m just some guy that's going to be around her pretty frequently from now on."
    c "Not {i}too{/i} frequently, though. You’ve got...other obligations."
    mak "Precisely. Like your paperwork and spending time showing your glorified secretary how much you appreciate all she does for you."
    c "Yup. Exactly what I’m talking about. Definitely not anything else."

    if bonus == False:
        "She must be referring to hugs."

    tb "Oh my...I can feel the secondhand excitement bubbling up within me by the second."
    tb "Perhaps I should also transfer into this[school]?"

    scene tsubasaofficevisit25
    with dissolve

    c "Let’s just...focus on your daughter for right now instead..."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "The three girls leave the office moments later and I take a couple hours to {i}actually do some paperwork{/i} before heading out myself."
    "I figure it’s the least I can do to not only lessen some of the burden on Makoto, but to reward her for putting together this entire rich girl transfer operation."
    "I just hope the process for our final student goes just as smoothly..."

    $ renpy.end_replay()
    $ day295 = True

    "………"
    "……"
    "…"

    jump day295parttwo
...
```