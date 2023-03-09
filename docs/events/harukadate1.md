# Drunk Again
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukadate1&go=Go)



## Event preconditions
✅Haruka love greater than or equal to 0

✅Event "[Main: Milk, Eggs, and Water](./day89.md)" is completed (event=day89)



## Next events
* [Main: The Value of Sharing](./halloween1.md)
* [Haruka: Invisible Worm](./harukadate5.md)
* [Haruka: The Need to be Hurt](./harukafirstlust.md)
* [Haruka: Bad Kitty](./harukalust10.md)

## Event properties
* ID: harukadate1
* Group: Haruka
* Triggered by label: callharukanighthang
* Triggered by branch label: callharukanighthang

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukadate1:
    "Maybe I’ll see what Haruka is up to?"
    "Now that I think about it, the two of us haven’t really hung out except for that one time she gave me a ride home."
    "And even then it was more along the lines of just...getting to her house and leaving a few minutes later."
    "Besides, she wouldn’t have given me her number if she didn’t want to actually talk, right?"

    play sound "phonebeep.wav"

    "Not knowing what else to do, I tap on Haruka’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    h "Hello?"
    s "Hey, it’s-"
    h "I know who it is. I've had your name in my phone since I asked you to check on Rin for me."
    s "And you haven't bothered calling? Do you even like me?"
    h "Hey, you haven't called either!"
    h "Is everything okay, though? Is this about Rin again? Because she seemed fine earlier today and-"
    s "Everything is fine. I was just wondering what you were doing tonight."
    h "Tonight? I was going to hang out at Sara’s bar."
    h "Do you...want to come or something?"
    s "Sure. If you guys are cool with having me."
    h "I'm sure we are, but let me check anyway! Hold on a sec."

    "A moment of silence passes by as Haruka does...whatever."

    h "Sara says you're free to come so long as you spend a lot of money."
    s "What if I just come, spend a normal amount of money, and keep you company?"
    h "Hmm...well, I {i}do{/i} seem like the loneliest person at the bar..."
    s "You’re probably the only customer at the bar in general."
    h "Also correct. So, are you going to come over now, or?..."
    s "Yeah, I’m on my way. Don't get too drunk without me."
    h "What's that? You want me to get super drunk without you? I mean...I wasn't going to but, if you insist-"
    s "Haruka-"
    h "Byeeeeee~!"

    play sound "phonebeep.wav"

    s "..."

    "Well, Haruka seems a bit...livelier than normal today."
    "I just hope that she doesn't {i}actually{/i} wind up getting too drunk while I'm on my way over since dealing with her {i}and{/i} Sara that way sounds...hard."

    s "..."

    "Maybe I'll try walking a little faster than normal..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play music "calmbar.mp3"

    "I take a moment to straighten out my clothes before making my way inside."
    "I'm sure no one cares, but it is one of the exceedingly rare opportunities I have to be alone with people actually close to my age and I should at least look the part of a mature human being."
    "Even if my companions for the evening will see me as one giant blur..."

    scene harukabar1
    with dissolve2

    h "Heeeeey! You made it! I’m not alone anymore!"
    sar "I’ve been here with you the entire time..."
    s "Hey, you two. What’s up?"

    "I take a seat next to Haruka, whose face has already gone full-blush from drinking."
    "Sara is busy wiping down the counter in front of us and, surprisingly enough, doesn't seem drunk at all."
    "Which I guess means this will, at least for the time being, be a decently lopsided conversation in which we counteract...however Haruka is when she's drunk."

    h "How was your walk, man? See anything {i}cool{/i} along the way?"
    h "Maybe like a...{i}huge stick{/i} or something?"
    s "..."

    "I immediately understand how Haruka is when she's drunk."

    s "It was a normal walk. I didn’t see anything particularly notable."
    h "Cool, cool. Normal walk. Got it."
    sar "Great icebreaker, Haru-chan."

    scene harukabar2
    with dissolve

    sar "So...you two are friends? Or..."
    h "Don’t talk to her, man. She's drunk."

    scene harukabar3
    with dissolve

    sar "I haven’t even had anything to drink yet..."
    s "Yeah, Haruka. I’ve seen Sara drunk and she-"
    h "Shhhh...You and me are talking right now. She’s just a bartender. It’s my turn to have you."

    scene harukabar4
    with dissolve

    sar "I...probably should have cut her off after five, huh?"
    s "Haruka, you had five beers in the time it took me to get here?"
    s "I called you like fifteen minutes ago."
    h "Five? That’s it? Pfft. Gimme five more. I got this."

    if bonus == True:
        h "Sara’s the one who gets drunk off five beers. I can go all night, if you know what I mean."

        scene harukabar5
        with dissolve

        h "Oh, wait! I didn’t mean it {i}like that{/i}. Hahahahah!"
        h "You’re so naughty, Sensei!"
        s "I didn’t even say anything..."

        scene harukabar6
        with dissolve

        h "Oh, you didn’t? Does that mean I'm...{i}imagining things?...{/i}"
        sar "{i}I’m so sorry...{/i}"
    else:
        sar "Pspspspspspspsppspsssss"

    "Sara whispers across the table as if to say something along the lines of “I had a feeling this might happen” or “I could have prevented this.”"
    "But the truth is, I really don’t mind."
    "Would I have minded if she was a {i}less{/i} horny drunk? Possibly. But this seems like a pretty great turn of events for me."
    "Besides, Haruka works hard enough as-is. It’s probably nice for her to take a load off like this every once in a while."

    s "Can I get a beer, Sara?"

    scene harukabar7
    with dissolve

    sar "Oh, shoot! I forgot to even ask."
    sar "I’ll be right back. I just need to grab some from upstairs since Haru-chan finished everything down here."
    s "And...why exactly do you keep the beer in your apartment instead of in the bar?"

    scene harukabar8
    with dissolve

    sar "Cause it's a lot less fun drinking myself to sleep if I have to keep walking downstairs."

    if bonus == True:
        sar "Now hang out for just a sec and don’t take advantage of my friend while I’m gone."
    else:
        sar "Now hang out for just a sec, and don't even think about hugging while I am away."

    scene harukabar9
    with dissolve

    "Sara disappears upstairs and, moments later, I can hear her footsteps as she moves through her apartment."
    "It makes me realize exactly how old this place must be if I can hear something like that even with the...jazzy piano music playing in the background."

    if sarasex == True:
        "…"

        h "Heheh~"
        s "What?"
        h "Hah...heheheh..."
        s "What’s so funny?"

        scene harukabar10
        with dissolve

        h "Heheheh..."
        s "Haruka, explain your-"

        scene harukabar11
        with dissolve

        if bonus == True:
            h "You two had {i}sex{/i} with each other~"
            s "…"
            h "…"
            s "Yes. That is a thing that happened."
            h "You put your penis inside of my friend."
            s "That would be how sex works, yes."
            h "Did it feel good?"
            s "It normally does."
            h "You gonna do it again?"
            s "Why do you ask, Haruka?"
            h "I don’t knooooow...curiosity?"
            s "Are you looking for an invitation?"

            scene harukabar12
            with dissolve

            h "Maybe you can just film it and send it to me so I can watch it at home?"
            s "I’ll bring it up to Sara next time."

            scene harukabar13
            with dissolve

            h "Dude, I was kidding!"
            h "I tooooootally don’t wanna watch you fuck my friend. That's like...{i}so{/i} gross..."
            sar "Who’s watching what now?"

            scene harukabar14
            with dissolve

            "Sara shows back up out of virtually nowhere and winks at me. There’s not a doubt in my mind that she at least heard the tail end of that."
            "In other news, though, I think I need to buy a video camera."
        else:
            h "Dogs."
            s "What?"
            h "You ever just think of silly they are?"
            s "Not really, no."
            sar "I am returning now!"

        scene harukabar15
        with dissolve

        h "Shhh. Don’t tell her what we talked about. {i}It’s a secret.{/i}"

        if bonus == True:
            s "Is it {i}really{/i} a secret if Sara already told you about us?"
            sar "Hm? What about us? What did I tell you, Haru-chan?"
        else:
            s "Are you...not allowed to talk about dogs for some reason?"

        h "Look! You’re gonna get me in trouble!"
        s "I’m not going to do anything that you weren’t going to do yourself."

    else:
        scene harukabar16
        with dissolve

        h "…"
        s "…"

        "I can’t help but notice Haruka stare off into the distance as soon as Sara disappears."
        "She grows rather quiet compared to how she was just moments ago and it’s...actually kind of confusing."
        "I'm assuming that something is bothering her, but it wouldn't be right for me to just-"

        h "She’s so pretty, isn’t she?"

        "Okay. I guess I'm going to find out after all."

        s "Sara?"
        h "Mhm."
        s "I mean...Yeah. She’s attractive. Why?"

        "Haruka lets out a heavy sigh, eyes still locked on where her friend stood just moments ago."

        if bonus == True:
            h "Why didn’t you have sex with her?"
            s "What?"
            h "Didn’t you turn her down when she was basically throwing herself at you? Why?"
            s "Not to be rude, but how does that involve you?"

            scene harukabar17
            with dissolve

            h "It doesn’t...but it’s confusing."
            h "Sara seemed pretty popular when we were in[school]. She was the kind of girl that everybody just, like...{i}knew.{/i} I was honestly really jealous of her."
            h "I never even had a boyfriend until I turned 18. And even then..."
            s "…"
            h "…"

            scene harukabar18
            with dissolve

            h "Heheh...actually...it’s not like any of {i}my{/i} story involves {i}you{/i}. So I’ll just stop there..."
        else:
            h "I'm just tired of her being pretty!"
            h "I am also tired of her pretending she has to be placed only to immediately come back!"

        scene harukabar19
        with dissolve

        sar "Okay! Supermom has returned!"
        sar "Did you two get along well while I was upstairs? Is anyone pregnant yet?"

        scene harukabar20
        with dissolve

        h "Yeah. We’re having twins. We need your help choosing names."

        scene harukabar21
        with dissolve

        sar "How about...Sana and Sara?"
        s "That...wouldn't bother you? Because it probably-"

    s "Hey. Wait a second."
    s "Where is my beer?"

    scene harukabar22
    with dissolve

    sar "In the cooler, silly. It needs to get cold."
    s "How can you provide such horrible customer service with a smile on your face?"

    if sarasex == False:
        scene harukabar23
        with dissolve

        if bonus == True:
            sar "{size=-10}Maybe I'm still a little mad that {i}somebody{/i} rejected me in my time of need?{/size}"
        else:
            sar "{size=-10}I am going to poison your beverage.{/size}"

        s "What?"

        scene harukabar22
        with dissolve

        sar "Hm? I didn’t say anything."

    else:
        sar "Apologies, sir. But you’re just going to have to deal with it. Please don’t cause a scene in front of my other customers."

        "Right. Forgot about all of her {i}customers{/i}."

    s "Fine. Whatever. I’ll just have some of Haruka’s."

    "I go to reach for Haruka’s beer and-"

    scene harukabar24
    with dissolve

    h "Nuh-uh! No you won’t! This one’s all mine. You’re gonna have to wait for your own."
    s "But that’s your sixth one and I'm stuck at zero for the foreseeable future. "
    h "So?"
    s "So that’s plenty. You’re not planning on driving home, are you?"
    h "I didn't even bring my car. I’m gonna sleep here tonight~"

    scene harukabar25
    with dissolve

    s "You are?"
    sar "{i}You are?{/i}"
    sar "Isn't this a thing I should have known about?"
    h "I just decided right now. "
    h "This is the first time I’ve been with {i}two{/i} friends in forever and I want to drink and have more fun."

    scene harukabar26
    with dissolve

    sar "Aww...Haru-chan is actually being cute and not just horny and lonely for once! What a rare and wonderful sight."
    sar "I’m in. Let’s all get drunk and talk about our feelings!"
    h "Yay!~"
    s "Feelings? What are those?"

    scene black
    with dissolve2

    "Sara runs upstairs for more alcohol and, like you may have guessed, the three of us spend the next couple hours getting drunk and talking about our “feelings.”"
    "Well, those two talk. I just sit there, sipping on warm beer and waiting for one of them to get drunk enough to pass out."
    "With a six-beer head start, the winner is Haruka."
    "Sara, who is in no condition to help when the time comes for us to start wrapping things up, stumbles her way up the stairs and presumably into her bed shortly after."
    "And I-"

    scene harukabar27
    with dissolve2

    "I wind up dealing with this."

    s "Haruka."
    s "..."
    s "Haruka..."
    h "Mmm..."

    "Haruka’s been passed out for around twenty minutes at this point."
    "Knowing that the bar is closed and that no one is around to really...{i}capitalize{/i} on this situation, I likely {i}could{/i} just leave her here without any consequences..."
    "But something about my involvement causes me to feel the slightest bit guilty."
    "And so I will continue to shake her shoulder until she wakes up."

    s "Haruka. Live."
    s "You can’t die here. It would be far too depressing."
    h "Mmm..."

    "I suddenly feel her body begin to move against my hand as she attempts to pull herself off of the counter..."

    scene harukabar28
    with dissolve

    h "Huh?..."
    h "What?..."
    h "What happened?..."
    s "You got drunk."
    h "I did?..."
    s "Very drunk, actually. Sara’s not doing so well right now either."
    s "In fact, she-"

    stop music

    h "Shut up."
    s "..."
    s "What?"

    play sound "static.mp3"
    scene harukabar29
    with flash
    stop sound

    h "I said shut up."
    s "…"
    h "…"
    s "Okay."

    play sound "static.mp3"
    scene harukabar30
    with flash
    stop sound
    play music "pianomelancholy3.mp3"

    h "Mmnh~!"
    h "Mmm...ngh...mnh~ Angh~ mmf~ Mmf!"

    "Haruka’s tongue violently assaults my own as if to make up for all of the time she's missed with the man she actually loves."
    "Or is pretending to love, based on how passionately she's currently gulping down my saliva."
    "The aggression behind just this single kiss is terrifying and, I know it sounds strange, but it feels like she's essentially trying to suffocate me."
    "I instinctively reach for one of her breasts and attempt to wrap my hand around it, not being able to cover it all due to the sheer size."
    "She leans into me, keeping her eyes closed to remain lost in whatever fantasy she'll use to justify this when the time comes to do so."
    "In between her gasps, I feel the lustful hesitance to reach downward and put an end to her loneliness right here and now."
    "I think about helping her, but not for long."
    "If I forget about breathing for even a second, she is sure to end me."

    h "Mmm...ngh...chu...mf...mlem...ngh...hah...ahm..."
    h "Mmm...mmm~ MMM!"
    h "Hm...mm...nnh..."
    h "..."
    h "..."
    h "Mmnch...mmm!"
    h "..."
    h "..."
    h "Mmh..."
    h "..."
    h "..."
    h "..."
    h "..."

    play sound "static.mp3"
    scene harukabar31
    with flash
    stop sound
    stop music

    h "Oh my god."
    h "Oh my god..."
    h "Oh god oh god oh god..."
    h "I-"
    h "I have to go."
    h "I’m so sorry."

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "Haruka pushes me away and nearly falls out of the chair as she tries to climb out."
    "She’s still too drunk to run, so she awkwardly stumbles away, grabbing on to everything she can in a desperate attempt to reach the stairs."
    "I don’t call out to her."
    "I get too caught up in watching her struggle."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate1 = True

    "{i}Haruka’s affection increased by {s}1{/s} more than she wants it to.{/i}"
    "………"
    "……"
    "…"

    if day > 5:
        jump endofsat
    else:
        jump endofweekday

label harukadate5:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label callharukanighthang:
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callnight
    if haruka_love >= 0 and day89 == True and harukadate1 == False:
        jump harukadate1
...
```