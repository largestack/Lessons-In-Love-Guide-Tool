# It Comes to Claim Us All
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanesanabeach3&go=Go)


Part of event chain [Ad Meliora](./ayanesanabeach2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: ayanesanabeach3
* Group: Sana
* Triggered by label: ayanesanabeach2

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label ayanesanabeach3:
    play sound "static.mp3"
    scene pos1 with flash
    scene pos2 with flash
    scene pos3 with flash
    scene pos4 with flash
    scene pos5 with flash
    scene theridehome1 with flash
    stop sound
    play music "meanttobe.mp3"

    ay "Did you really play that game the entire day? Your battery didn’t, like...die or anything?"
    sa "I brought...a charger and...there was an outlet in the bathroom..."
    ay "Okay, but...don’t your eyes hurt?"
    sa "I can barely even...see anymore..."

    "I wind up in the back of Ayane’s limo again with no recollection of how I got here. But such things are no longer of much concern to me."
    "The day went by like a flash of lightning, and it is I who now feel the burn of electricity as it courses through my veins and reminds me that places like this are my least favorite in all of the world."
    "I think about becoming a circuit and grounding these memories so that the two girls unfortunate enough to accompany me in this vehicle make it out alive..."
    "But my lack of knowledge in terms of electricity prevents me from doing anything but sitting still and waiting for the car ride to come to an end."

    if ayanesanabeach2 == True:
        "I can tell that part of the day has disappeared. And an ever-powerful loneliness that sprouts from the ground as a result of that wraps around my ankles in an attempt to pull me under."
        "Something is missing, but not completely gone. "
        "It sits among us, watching on as the seer it is. Studying our every move and taking bets on what comes next."
        "I sink further into my seat, hoping to fall through the floor and have the tires of this vehicle kiss the back of my head and join me forever with the asphalt."
        "It is there where I can feel as if I belong again."

    else:
        "I think for a moment about whether or not anything valuable was missed in this recurring slip into the dark. I think for another about anything I may have potentially fractured in doing so."
        "But judging by the faces on the girls before me, I assure myself that nothing was fractured at all."
        "Either that or the two of them have grown so used to me destroying everything in my path that the smallest of breaks do not even register anymore."
        "Part of me feels like I have been here before."
        "Like I have thought these same thoughts under different circumstances. "
        "Perhaps a different body."
        "But they dissipate the moment the passenger side tires come into contact with a small pothole- and any thoughts that may have led any{i}where{/i} disappear like one more layer of cement."

    scene theridehome2
    with dissolve

    ay "Sensei, you wouldn’t mind seeing Sana back to the dorm, would you? Molly will be starting on our Halloween costumes soon, so I need to head back home for a little while to grab some supplies."
    sa "I don’t...need a babysitter, you know..."

    scene theridehome3
    with dissolve

    ay "Of course I know. But you {i}do{/i} need to take your eyes off of that screen for at least a few minutes today. You’re making Sensei feel lonely."
    s "If Sana doesn’t want me to go with her, that’s fine. I can just head home and she can keep playing her game."

    scene theridehome4
    with dissolve

    sa "No, it’s...fine...Ayane is right..."
    sa "I’ve been...too much of a loner all day and...that isn’t fair to either one of you..."
    sa "I just got a little...carried away, I guess...but...but I’m not tired, so..."
    sa "So if you don’t...want to go home yet..."

    scene theridehome5
    with dissolve

    ay "Then, it’s settled! Sensei will accompany Sana back to the dorm and I will go home to my bathrobe-wearing, smooth-jazz and whiskey-obsessed father!"
    s "That is a very interesting combination of traits."

    scene theridehome6
    with dissolve

    ay "You know, I thought so too. But the more I looked into it, the more I realized that all three of those things go hand in hand...and hand. Since there are three."
    sa "Um...are...are you sure you want to come over, though?..."
    sa "It’s...already really late and...I know Ami doesn’t like it when you’re...um...more than...five feet away from her..."
    s "I’ll come. I feel a sudden need to make up for lost time anyway."

    ay "Yeah, where did you go after you left me? I thought you were going to look for Sana, but she said she never even saw you."
    s "I..."

    scene black
    with dissolve2

    s "I really wish I knew."
    "........."
    "......"
    play sound "dooropen.mp3"
    "..."

    scene theridehome7
    with dissolve2

    sa "Um...sorry again for...not spending any time with you guys today..."
    sa "I...uhh...you know..."
    sa "New video game..."
    s "It’s not like you’re obligated to spend time with me or anything. There’s no need to apologize."
    sa "I’m apologizing less for...not spending time with you and...more for just...being rude..."
    sa "To Ayane too...She invited me to the beach and...I didn’t even...do anything...beach-related..."
    s "You wore a swimsuit which, honestly, is more than I would have expected out of you. So you’re in the clear."

    scene theridehome8
    with dissolve

    sa "I...uhh...kind of wish I didn’t, though..."
    s "If you’re only thinking that because I got to see more of your skin than ever before, you should take solace in the fact that it was only for a few seconds before you disappeared."

    scene theridehome9
    with dissolve

    sa "I guess that makes...two of us, then..."
    sa "We both...got to disappear while...Ayane stayed as noticeable as ever..."
    s "I have a history of disappearing, though. You’re normally more of a “fade into the background” type of person. We’re very clearly not on the same level."
    sa "We...found each other in the end, though..."
    sa "Now we just have to...figure out what to do without...being awkward..."
    s "I feel like every single time we’ve hung out in here, things have been kind of awkward. I say we just embrace it and accept that’s how things will always be between the two of us."

    scene theridehome10
    with dissolve

    sa "...Always?"
    s "Sana?"

    scene theridehome11
    with dissolve

    sa "Oh! S...Sorry, I...was just...thinking out loud..."
    sa "Do you, um...do you want to watch a...movie or something?..."
    s "Ahh, yes. What better way to give your eyes a break from staring at a screen all day than to just...stare at a different kind of screen?"

    scene theridehome12
    with dissolve

    sa "Don’t worry...only 50%% of my eyes...will suffer irreparable damage..."
    s "The benefits of being a cyclops."
    sa "Hehe..."
    sa "It’s much different from...having four eyes, I bet..."
    s "Are you actually making fun of me for wearing glasses right now?"
    sa "No...I like your glasses...they...they make you look...kind of sophisticated...like a real teacher..."
    sa "But, um...we should...probably...stop just...staring at each other and...actually watch a movie if...if you’re not going to spend the night..."
    s "Do you {i}want{/i} me to spend the night?"

    scene theridehome13
    with dissolve

    sa "I want..."
    sa "..."
    sa "To not answer that question..."

    scene black
    with dissolve2

    "Something feels different about the air in here."
    "It’s thicker."
    "Hotter."
    "And the way it fills my lungs makes it feel like an aphrodisiac."

    scene theridehome14
    with dissolve2

    "I wonder if Sana ever steals glances at me while I’m looking away. And I wonder if her mind races to the same place mine does when I do the same for her."
    "I wonder where it would go now if I were to take a sledgehammer to one of the only “pure” relationships I have maintained up until this point in exchange for just one more notch in my belt."
    "Would it be worth it if it etched a notch into hers?"
    "Would she follow in her mother’s footsteps? Crumble beneath the touch of an older man?"
    "Carry the burden he places in her for a whole nine months...grow to love it and refuse to let it go when its time finally comes?"
    "Or would she rather drown herself in the semen of the status quo? Refusing to accept that the entire world is passing her by while she sits idly and pretends it’s all screeched to a halt."
    "This is bad."
    "We’re half an hour into whatever it is we’re watching and I haven’t even been able to focus long enough to discern the title of the film. "
    "Does she feel the same?"
    "Is she comfortable?"
    "If so, why?"
    "How?"
    "Why can’t {i}I{/i} be comfortable?"
    "Why can’t I keep things the way they are? "
    "Why must all of my relationships end with sweat and cum? Drenched sheets and the flood of regret that never ceases pouring in once the dam bursts?"

    play sound "static.mp3"
    scene theridehome15 with flash
    stop sound

    "Forty five minutes and counting."
    "Sana has stopped moving. "
    "I think she’s waiting for me to do something."
    "My dick has been pressed up against my jeans and damp, pre-cum soaked spot for so long that I’m worried I may develop some sort of blister."
    "But thinking this does not quell the sexual rage stirring within me."

    play sound "static.mp3"
    scene theridehome16 with flash
    stop sound

    "Forty seven. "
    "She moves again."
    "Her shoulder bumps against mine. "
    "Is she trying to hint at something?"
    "How many more minutes should I wait before bumping into hers as well?"

    play sound "static.mp3"
    scene theridehome17
    with flash
    stop sound

    "Forty eight."
    "Forty nine."
    "Fifty."
    "I can’t take it anymore."

    menu:
        "Put your arm around her" if sarasex == True:
            $ chariotarm = True
            play sound "static.mp3"
            scene theridehome19 with flash
            stop sound

            "I reach out and rest my hand on her side, just inches from her lower back."
            "She does not move or twitch or react at all."
            "My touch is either entirely welcome or entirely unnoticed."
            "I can’t tell which one I prefer."

            play sound "static.mp3"
            scene theridehome20
            with flash
            stop sound

            sa "Huh?"
            sa "..."
            s "..."
            sa "Sen-"

            play sound "static.mp3"
            scene theridehome21 with flash
            stop sound

            "She moves closer of her own volition, bringing one of her {i}own{/i} hands to my thigh and softly stroking it."
            "If she moves any further upward, she’ll realize how I feel."
            "The last fifty- no. Fifty one minutes now will have not been for nothing."
            "We’ll cement ourselves as more than who we are when we have tried our hardest to remain alone in the dark. Unnoticed."
            "But we shan’t be blamed for the seeking of light when we’ve all but forgotten how it feels on our skin."

            play sound "static.mp3"
            scene theridehome22 with flash
            stop sound

            sa "Ah?..."
            s "Did you feel something?"

            scene theridehome23
            with dissolve

            sa "Did I..."
            sa "What?..."

            play sound "static.mp3"
            scene theridehome24 with flash
            stop sound

            "I pull her closer."
            "Her skin is hot. Scorching. "
            "I can tell she feels the same way I do. Perhaps even moreso. But, despite that, the tiny hand on my thigh stops moving."
            "She’s scared. Nervous. And I understand that. "
            "It’s her first time being this close to anyone."
            "Which means that it is up to me to take the initiative...even more than I have done thus far."

            play sound "static.mp3"
            scene theridehome25 with flash
            stop sound

            "I lean in closer."
            "The thickness of her hair and the massive differential in our height prevents me from being able to look into her eyes and drink in her fear."
            "But, in just several seconds, I will be drinking in her spit instead."
            "I wonder what this one will taste like."
            "I wonder how she’ll react to the sensation of my tongue twisting around hers."
            "Will she like it?"
            "Hate it?"
            "Will she beg me to stop?"
            "Beg me for more?"
            "Will we end up beneath the covers or simply remain on top of them?"
            "How does she want it?"
            "Does she swallow?"
            "Does she squirt?"
            "Has she even started growing hair yet? "
            "She’s small for her age, so there might be nothing there."
            "Will I like that?"
            "Hate it?"
            "What happens next?"

            play sound "static.mp3"
            scene theridehome26
            with flash
            stop sound

            sa "Mmf?!"
            s "You’re so cute when you’re turned on."

            scene theridehome27
            with dissolve2

            sa "...mm?"

            play sound "static.mp3"
            scene theridehome28
            with flash
            stop sound

            "Sana takes my thumb into her mouth, fellating it with an impressive amount of skill and confidence for a girl  who’s yet to ever taste a cock."
            "Her tongue slides beneath it as her hands pull me deeper into her mouth, desperate to show me what she’s capable of doing."
            "My head parts from hers slightly so I can get a better look at her face, but I’m still unable to see her eyes."
            "And while I want to tear my thumb from her mouth and replace it with my tongue, I worry about how the taste of myself could potentially ruin this long overdue experience."

            sa "Mmf..."
            sa "Mmnch~"
            sa "Amff..."
            s "..."

            play sound "static.mp3"
            scene theridehome29 with flash
            stop sound

            sa "Mmf...mm........mm?..."
            s "Good girl, Sana..."
            s "Just like that..."

            scene theridehome30
            with dissolve2

            sa "Mm?..."
            s "You must really want it, huh?"
            s "All you had to do was ask, you know."
            sa "Shen...shei?..."

            play sound "static.mp3"
            scene theridehome31 with flash
            stop sound

            "I lift her chin to kiss her."
            "And for a brief moment-"
            "I am finally able to see her eyes."

            play sound "static.mp3"
            scene theridehome32 with flash
            stop sound

            "It’s only a brief moment, though."
            "It’s gone quicker than a flash of lightning."

            sa "Stop stop stop stop stop stop stop! What are you doing?!"
            s "I..."
            s "Weren’t you-"
            sa "Okay, uhh...uhh..."
            sa "You...you have to leave. Right now."
            s "Right now?"
            sa "Right now."
            s "If I misunderstood something, you-"
            sa "Just...go. Please."
            sa "This is...this is happening...way too fast...and..."
            sa "I don’t even...remember how we..."
            sa "How this..."
            sa "What...happened..."
            s "It..."
            s "It kind of just did..."

            scene theridehome33
            with dissolve2

            sa "Sensei...I can’t do this..."
            sa "I need you to go."
            s "..."
            sa "I need you to {i}please{/i} go. "
            sa "We can...we can forget this ever happened..."
            s "Will you be able to?"
            sa "What?"
            s "Isn’t this what you want?"
            sa "Sensei..."
            sa "Please leave..."
            sa "{i}Please...{/i}"
            s "..."
            sa "..."

            scene black
            with dissolve2

            s "Okay."

            "........."
            "......"
            "..."

            scene clearnightsky
            with dissolve2

            "It feels cold when I step outside, though I think it’s just the result of elevated body heat."
            "Did I make a mistake?"
            "Everything seemed to be going fine until Sana just...changed her mind."

            s "..."

            "But..."
            "Was that even Sana at all?"
            "And if not...what would that mean?"
            "What was that look she gave me right before we were about to kiss?"
            "How did it stop me dead in my tracks?"
            "And why do I..."
            "Why do I want to see even more of it?"

            scene black
            with dissolve2

            "You’re probably tired of hearing this by now- "
            "But I slide my hands into my pockets and begin to head home."
            "I can’t even text Sana to apologize as, for some reason, I {i}still{/i} don’t have her phone number."
            "Maybe she’s just afraid of letting me in."
            "But she needs someone to protect her."
            "She needs someone to fix her."
            "And I’ve been successful so far."
            "Which means that this can’t be the end."
            "I won’t {i}let{/i} it be the end."
            "..."
            "But I’m not even sure it’s up to me anymore."
            "..."
            "And I’m not sure if it’s up to {i}her{/i} either."
            "..."
            "I hope she’s doing okay right now."

            play sound "static.mp3"
            scene pos1 with flash
            scene pos2 with flash
            scene pos3 with flash
            scene pos4 with flash
            scene pos5 with flash
            scene theridehome34 with flash
            stop sound

            sa "MMM! MMM! MMM! MMM! MMM!!!!!!"

            scene theridehome35
            with dissolve

            sa "HNGH.......MM!.....MMMFFF!!!!"
            sa "MMF.....AAMFH....MNNGHH!!!.........MMM!!!"

            play sound "static.mp3"
            scene theridehome36 with flash
            stop sound

            sa "AAAAH!!...NGAHHH!!!!!"
            sa "WHY...AM I SO......AHHH!!!"

            scene theridehome37
            with dissolve

            sa "Sensei...Sensei...Sensei!!! "
            sa "How did we........"
            sa "Why......can’t I........"
            sa "Oh fuck......ooooh...fuck..."

            scene theridehome38
            with dissolve

            sa "AAAAAH! RIGHT THERE! RIGHT THERE! RIGHT THERE!"
            sa "HARDER!....HARDER!!!..."
            sa "SEN.......SEI!!!!"

            with sexfade
            with sexfade
            scene theridehome39 with cumflash
            with hpunch

            sa "MMF.......MNGHH......MMMMMMMMMM!!!!!!!!!!!!!!!!"

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ ayanesanabeach3 = True
            $ sana_love += 5

            "........."
            "......"
            "..."

            jump ayanesanabeach4

        "{b}LEAVE! DON’T DO IT! PLEASE!{/b}":
            play sound "static.mp3"
            scene pos1 with flash
            scene pos2 with flash
            scene pos3 with flash
            scene pos4 with flash
            scene pos5 with flash
            scene theridehome18 with flash
            stop sound

            "The movie comes to an end..."
            "And I feel as if I have kept something alive."
            "But the sensation in doing so is not one of bliss."
            "It feels more like staring at the body of a loved one caught in a coma."
            "Like I’m prolonging an inevitability that I refuse to accept because drowning in the semen of the status quo is something I, too, indulge in from time to time."
            "Do not cheer for me. Do not admire this desperate bout of indecisiveness- for even if this is an improvement, it is something someone {i}normal{/i} would not be forced to face."
            "The man who breaks everything should not be lauded when he comes into contact with an object that somehow remains intact."
            "This girl, this {i}object{/i}, she-"

            sa "I think..."
            sa "You should head home, Sensei..."
            sa "It’s getting late..."
            s "..."
            sa "But this..."
            sa "Was nice..."
            sa "It was really nice..."
            s "..."

            play sound "static.mp3"
            scene bedroom_night with flash
            stop sound

            "I left Sana’s room and wound up in my own."
            "Was it the right decision?"
            "What could I have taken if I had only reached out?"
            "Would I still be there right now? Spending the night in that small bed of hers while one much larger and more familiar sits directly beside us?"
            "There is no way of knowing."

            scene black
            with dissolve2

            "All I can do is trust my gut."
            "I just wish it would stop feeling like it’s wrapping around itself."

            $ renpy.end_replay()
            $ sana_love += 10
            $ ayanesanabeach3 = True
            $ ayanesanabeach4skip = True
            stop music fadeout 10.0

            "{i}Sana’s affection has increased by 10!{/i}"
            "{i}You dream of her and only her.{/i}"
            "{i}But you’re unsure if you’ll ever dream that way again.{/i}"
            "........."
            "......"
            "..."

            if day == 1:
                jump advancetotues
            if day == 2:
                jump advancetowed
            if day == 3:
                jump advancetothurs
            if day == 4:
                jump advancetofri
            if day == 5:
                jump advancetosat
            if day == 6:
                jump advancetosun
            if day == 7:
                jump advancetomon

label ayanesanabeach4:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
with dissolve2

    q "And yet you have found yourself in {i}this{/i} timeline...where everything is bad and good all at once."
    q "Where time moves both backward and forward simultaneously...just like {i}Ayane{/i} said."
    s "If that was even her speaking. I’m not sure who I can trust anymore knowing that you can just...become other people."
    q "Thankfully, that’s a worry you won’t have to live with for long since you will {i}probably{/i} forget me again after tonight."
    q "I’ll never turn into {i}her,{/i} though."
    q "And I know it’s pointless to say this since I literally {i}just{/i} told you you're going to forget, but...try and remember that."
    s "Why won't you turn into Ayane? "
    q "..."
    s "..."

    scene sanaatthebeach26
    with dissolve

    q "Don’t wanna. "
    q "Don’t like feeling what she feels."
    q "Also, don’t make it sound like doing what I did tonight is some sort of hobby for me. I normally just try on their clothes. Very rarely do I feel the need to step in and start playing charades. "
    s "Maybe...don’t do that at all anymore."
    q "Going to have a hard time looking at Sana now that you know how she really feels about you? Or is that something you’ve known all along?"

    scene sanaatthebeach27
    with dissolve

    s "I won’t know anything for sure until {i}she{/i} tells me. Hearing her feelings fall out of someone else’s throat just isn’t enough."
    q "But you have your suspicions, of course."
    s "Of course."
    s "Everyone loves me."
    s "They have to."
    q "Do they?"
    s "The world was made for me."
    q "Was it?"
    s "Yes."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach28 with flash
    stop sound

    q "Is that what you really believe? Or is that what you {i}want{/i} to believe?"
    s "It’s the only thing that makes sense."
    q "You talk to birds. You are no authority on what does and doesn’t make sense."
    s "Are you?"

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach29 with flash
    stop sound

    q "No."
    q "In many respects, I’m just as lost as you are. "
    q "I just got a little lucky and skipped living through the whole “infinite high school” thing."
    s "You get used to it. I’m not really complaining. "
    q "Why would you? Your life is great."
    s "And yours isn’t?"
    q "..."
    s "..."
    q "It will be."
    q "Some day."

    play sound "static.mp3"
    scene happy1 with flash
    scene sanaatthebeach30 with flash
    stop sound

    s "I hope that day comes soon."
    s "You’re kind of annoying and I feel like you can definitely tell me more than what you actually have, but..."
    s "I don’t hate you or anything."
    q "I’m glad."
    q "I don’t hate you either."
    s "..."
    q "..."
    q "I think we have to say goodbye now."
    s "I see..."
    s "I’m not going to remember you...right?"
    q "Probably not."
    s "Then, for the sake of ending this extremely weird conversation on a good note...can you tell me your name?"
    q "..."
    s "..."
    q "Why don’t you give me one?"
    s "{i}Give{/i} you one?"
    s "I have no idea where I’d even start. "
    s "I don’t know anything about you other than the fact that you have nice eyes and...occasionally  someone {i}else’s{/i} eyes instead."
    q "Would you like a suggestion?"
    s "It would certainly be appreciated."
    q "Then..."

    scene black
    with dissolve2

    q "Name me after your favorite flower."

    stop music
    $ renpy.end_replay()
    $ ayanesanabeach2 = True

    scene youdiditlol
    $ renpy.pause(7, hard=True)

    jump ayanesanabeach3
...
```