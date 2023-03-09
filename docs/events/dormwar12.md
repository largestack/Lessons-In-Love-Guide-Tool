# Us
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar12&go=Go)


Part of event chain [The Legacy of Thaum Pt. Z: Alentha Amastacia](./dormwar11.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar12
* Group: Main
* Triggered by label: dormwar11

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar12:
    scene datewar1
    with dissolve
    play music "maidcafe.mp3"

    u "Hi, everyone! Uta Ushibori here!"
    u "It’s a bright and sunny morning, but that doesn’t mean it isn’t cold!"
    u "And, in case you’re wondering where I am right now, I’d be happy to tell you!"
    u "You see, the building right behind me is the {i}exact{/i} location where today’s {i}second{/i} contest is going to be held!"
    u "That’s right! This is the outside of the Chosokabe apartment! And joining me today is my very special guest, the first floor’s own...Yumi Yamaguchi!"
    y "The fuck is going on right now? Who are you even talking to?"

    scene datewar2
    with dissolve

    u "So, Yumi...any insight on today’s competition? "
    u "It seems that you know Chika better than anybody else in the class, so we’re hoping you can shine some light on a few of her strategies or...tactics she might be using to defeat Touka today."
    y "Am I getting paid for this shit?"
    u "You’re being paid in exposure! It’s a completely valid form of currency that everyone accepts and appreciates without question! Trust me!"

    scene datewar3
    with dissolve

    y "Hah...whatever. What was the question again?"
    u "Actually, let me ask you this instead..."
    u "No disrespect to Chika, but this is a very low income area and isn't exactly an ideal location for a date."
    u "Are you at all worried about the effect of Touka’s money on the outcome of this competition?"

    scene datewar4
    with dissolve

    y "Uhh...not really. No."
    y "In fact, if there’s anything I know about Chika, it’s that she’ll use all of the bein’ poor shit to her advantage."
    u "How can one use their {i}lack{/i} of money to their advantage?"

    if bonus == True:
        y "You know...just make herself look all pitiful and shit so our pervert teacher will feel bad and choose her to be a white knight or whatever."
    else:
        y "You know...just make herself look all pitiful and shit so the huggy boy will feel bad or something."

    scene datewar5
    with dissolve

    u "I see, I see! Leave it to the Queen of Hearts to know both her opponent {i}and{/i} her man!"
    y "The queen of...wha?"

    scene datewar6
    with dissolve

    u "It’s the nickname we’ve given to Chika! Not only because of her heart hairpin thingy, but because she seems to know the most about love and stuff out of all of the girls!"
    y "Chika doesn’t know shit. She just watches a bunch of those sappy movies with her little sister. Not really experience."
    u "Do you think {i}you{/i} could do any better, Yumi?"

    scene datewar7
    with dissolve

    y "I think you better get the fuck away from my house before I beat the shit out of you."
    u "Well, there you have it! I’m Uta Ushibori with the...news thing! Back to you guys in the studio!"
    u "Stay tuned for full coverage of all date-related stuff, as Makoto Miyamura will be holding an interview with none other than Tsubasa Tsukioka in just two short hours!"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Uhh...hello?"

    "I knock on Chika’s door and wait for her to answer."
    "I could have sworn I saw Uta on the way here, but now that I look around again, I don't see anyone at all."

    if bonus == True:
        "So I’m starting to doubt that this is even part of the dorm war and that Chika just wants to have sex or something."
    else:
        "So I’m starting to doubt that this is even part of the dorm war and that Chika just wants to hug."

    "Either way, fine by me."
    "I just hope that Yumi is watching Chinami or something because...I’m not really sure how I’d explain something like that to her."

    c "Sensei, is that you? You can come on in!"

    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene datewar8
    with dissolve
    play music "kimitoakinobouken.mp3"

    c "Hey! Perfect timing!"
    c "I just finished making breakfast."
    c "Well...I guess, it’s not really breakfast. But like, it’s kind of that weird period after breakfast but before lunch."
    s "I believe that is called “brunch.”"
    s "What’s going on here?"

    scene datewar9
    with dissolve

    c "What do you mean?"
    s "I mean that this obviously isn’t part of the contest, so I want to know if you’re planning something or-"

    scene datewar10
    with dissolve

    ch "Papa!"
    c "Not yet, Chinami."
    ch "Nevermind!"

    scene datewar9
    with dissolve

    s "Well, I guess {i}that{/i} won’t be happening. "

    scene datewar11
    with dissolve

    c "This {i}is{/i} part of the competition. But that doesn’t mean it isn’t something I've been wanting to do anyway."
    c "It’s just...I don’t have much money, so I can’t take you on some lavish or exciting date or anything like that."
    c "All I can really give you is...me. And who I am and...what I am and...all of that kind of stuff."
    s "So...the competition is who can take me on a better date?"

    scene datewar12
    with dissolve

    c "Lucky me, right? "
    c "I kind of had to like, semi-blackmail Makoto to get this competition approved, but that’s beside the point. "
    s "Wait, what?"

    scene datewar13
    with dissolve

    c "Don’t worry about it."
    c "The point is...even though I don’t always have free time...and I can’t really afford the kind of stuff I’m sure you’ll be seeing later-"
    c "I want you to see that I...I can still make the most of our time together and...what little there is of it."
    c "So..."
    c "Chinami! Now!"

    scene datewar14
    with dissolve

    ch "Papa!"
    s "What is happening?"

    scene datewar15
    with dissolve

    ch "If you would please follow Chinami, she would like to show you to your table for the afternoon."
    ch "Today’s main course is a timeless Chosokabe favorite- instant curry made with love!"
    ch "The mild kind because Chinami can’t have spicy food."
    s "What-"
    ch "Silence, Papa! Big Sis worked very hard all morning making sure Chinami wouldn’t mess this up, and so she must stick to the plan!"

    scene datewar16
    with dissolve

    c "We should probably listen to her before she kicks us out."
    s "Yeah...I guess we should."
    ch "This way, please."

    scene black
    with dissolve

    "Chinami ushers us through the bedroom and out onto the balcony. "
    "There’s a table I haven’t seen before pressed up against the corner, overlooking my least favorite part of the city."
    "But, somehow or another, it doesn’t make me uneasy. "
    "In fact, I feel more at home here than I’ve felt in quite a while."
    "And I’m sure that a large portion of that is because the Chosokabe family dynamic is infectious, but that’s beside the point."
    "It’s not much. "
    "But what it is works well."

    scene datewar17
    with dissolve

    c "It’s not too cold out, is it?"
    c "I checked the weather like six hundred times last night making sure it wasn’t going to rain, and it’s like a whole ten degrees colder than it was supposed to be."
    c "Is that fine? Or do you want to go back inside and maybe like...improv this part of the date?"
    s "It’s fine, don’t worry about it."
    s "Also, has this table always been here?"
    c "Why do you ask?"
    s "It’s just strange that we haven’t done something like this before."
    c "It’s new, actually."
    c "Well, not {i}new{/i}. But we got it today."
    c "After I left your room this morning, I came back home with Yumi and the two of us walked around town looking for people who might be throwing away an old table and chairs."
    c "We had to make a couple trips to carry everything back but, as you can see, we got it done in the end."
    s "You did that just for today?"
    c "And for the future."
    c "I obviously don’t want this to be the only time the two of us can kind of...separate ourselves from how busy or...unfortunate life can be at times."
    c "So if I need to get a little dirty and barter with some creepy old people to make that happen, I’m fine with it."
    c "You do so much for me. The least I can do is make you feel like you belong."
    s "…"
    c "…"

    scene datewar18
    with fade

    "I sit down at the table and have a hard time finding anything to say in response to all of that."
    "Just this morning, I was making my relationship with Chika sound like some one-sided affair for no reason other than...not hurting Io’s feelings or something. "
    "Why did I do that again?"

    play sound "static.mp3"
    scene goodmorningio22
    with flash
    scene datewar18
    with flash
    stop sound

    "Oh."
    "Right."
    "Because I’m pathetic."
    "Because I can't be satisfied by just one beautiful girl."
    "I need all of them."

    if bonus == True:
        "Perhaps in another life, I’d take Chika’s hand."
        "The two of us would leave this scavenged table together and I’d march back over to the diner, dragging her by the wrist, and introduce her to everyone as my girlfriend."
        "She would graduate years later and we’d begin to grow old together."
        "We’d get married."
        "Maybe have a child or two."
        "We’d get sick."
        "Die."
        "And then go to sleep one final time, in plots right next to one another."
    else:
        "I am the huggy boy."
        "I must hug the whole world."

    c "I-"

    if bonus == True:
        s "I love you."
    else:
        s "I'm the huggy boy."

    scene datewar19
    with dissolve

    c "H-Hey..."
    c "Wh-what’s this all of a sudden?"
    c "It’s...embarrassing when you just come out and say it out of nowhere like that."
    s "It’s what you were about to do, isn’t it?"
    c "Well..."

    if bonus == True:
        c "Maybe..."
    else:
        c "I was going to say I'm the huggy girl, but..."

    "Perhaps in another life, the three words she loves more than the world itself would not carry so much weight."
    "Perhaps in another life, I would be able to say them and mean them."
    "Or perhaps I wouldn’t."
    "It’s not really something that someone like me could ever know."
    "There’s no way to know anything in this world. Not when it continues to spin as quickly and change as rapidly as it does every single day."
    "But, for a brief moment in time, the spinning stops."
    "The changing stops."
    "And, in a time where I least expect it-"
    "Chika and I exist. "
    "Not just as people. Not just as a couple."
    "But as us."
    "I am me. She is her."
    "We are us."
    "That is all."

    s "…"
    c "…"

    "O, world."
    "Why must I destroy everything I touch?"

    s "You’re going to win this competition."

    scene datewar20
    with dissolve

    c "I mean...{i}obviously.{/i}"
    c "But we’ve barely even started, and to say that before Touka even goes..."
    c "Why now?"
    s "Because you deserve it."
    s "And I don’t deserve you."

    "It’s funny how the moments we least expect are the ones that always change us."
    "Which is not to say that I’ve changed."
    "I will hurt this girl more times than she can bear."
    "I will ruin everything."
    "I will destroy her world."
    "But I will not have wanted any of it."
    "I do not change."
    "But a part of me does."
    "Or did."
    "I don’t know."
    "But such is the art of never knowing."
    "Something that resembles love digs its jagged fingernails into my beating heart and sinks its teeth in once it's inside."
    "It’s not much."
    "But it’s enough for me to say it to her without feeling like a complete liar."
    "For the kind of love that Chika both has and wants is the kind that exists to be traded between two entities."
    "And that kind of love does not exist to me."
    "Nothing exists to me."
    "I wish it did."

    scene datewar21
    with dissolve

    ch "Chinami has returned!"
    ch "Please help yourselves to-"

    play sound "glass.mp3"
    scene datewar22
    with hpunch

    ch "…"
    s "…"
    c "…"
    ch "Chinami is in trouble, isn’t she?"

    scene black
    with dissolve2

    "Chika laughs it off and helps her sister clean up the mess."
    "It’s a horrible date."
    "I enjoy every second of it."

    $ renpy.end_replay()
    $ dormwar12 = True
    $ dorm1warpoints += 1
    stop music fadeout 8.0

    "………"
    "……"
    "…"

    jump dormwar13

label dormwar13:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
f "Time to die, {i}monk{/i}..."
    mo "I...I have 10 HP..."

    scene wienerfight45
    with dissolve

    f "Then..."

    play sound "dice.wav"
    scene wienerfight46
    with dissolve

    f "…"
    f "Shit."
    sa "Wait...you still have...savage attacker...so you can reroll the damage dice..."

    scene wienerfight47
    with dissolve

    f "R-Right! I’ve never been so thankful for a reroll before!"
    f "Here...here goes nothing!"

    play sound "dice.wav"
    scene wienerfight48
    with dissolve

    sa "…"
    f "…"
    mo "............?!?!?!?!?!?!?!?!"
    r "Hey guys, how’s the game going? Did anyone- "
    r "Oh shit, Futaba rolled my lucky number."
    mo "MWAHAHAHAHAHA! ALENTHA LIVES ANOTHER DAY!"

    scene black
    with dissolve2

    "{i}Roughly five minutes later...{/i}"

    scene wienerfight49
    with dissolve

    mo "I did it, Sir! I defeated Zagull Throat Spear!"
    mo "It got really close at the end, but I-"
    s "That’s nice, Molly. Congratulations."

    scene wienerfight50
    with dissolve

    mo "Don’t...Don't you want to hear about my epic tale of bravery and strength? And how I overcame adversity in the face of danger through willpower and-"
    s "I wouldn’t really understand any of it, to be completely honest. So there’s really no point."
    mo "Oh..."
    mo "Well...okay."
    mo "I won, though. So...I guess I’ll just text Uta and tell her."
    f "Things...are really not looking good for the first floor, are they?"
    s "There’s always...whatever other competitions are being held today, I guess."
    f "Right..."
    f "There are still four more, so we could {i}technically{/i} come back if we...just keep winning until the competition is over."
    f "But the next contest could probably go either way, so..."
    s "What’s the next contest?"
    mo "It’s the Chika versus Touka battle, but we’re not allowed to tell you any more than that."

    play sound "texttone.wav"
    scene black
    with dissolve

    "My phone begins to go off in my pocket and-"
    "Wait, I went to sleep without a charger. How is it alive again?"
    "Either way, I answer the phone and step away from Molly and Futaba."

    s "Hello?"
    c "Hihi~"
    c "Is the Molly and Futaba thing over yet?"
    s "It just ended. Molly won."
    c "Damnit. The second floor has a pretty big lead then, huh?"
    s "They’re ahead, but it’s not impossible to come back, I guess."
    c "Course it’s not! Especially since my contest starts right now!"
    c "How long will it take you to get to my house from there?"
    s "Your house? Uhh...like thirty minutes, probably?"
    c "Perfect! Head over right now and ring the bell when you get here. Got it?"
    s "Got it. But what is-"
    c "Love you! Bye!"

    play sound "phonebeep.wav"

    "Chika hangs up and...I apparently have to go to her house for whatever the next contest is."
    "I slide my magical phone back into my pocket and say goodbye to everyone."
    "None of the girls follow me for the first time in two days and..."
    "Well, I guess I just...go to Chika’s house."

    $ renpy.end_replay()
    $ dorm2warpoints += 1
    $ dormwar11 = True
    stop music fadeout 5.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    jump dormwar12
...
```