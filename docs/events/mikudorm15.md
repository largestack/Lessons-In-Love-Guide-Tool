# Moments Like This
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm15&go=Go)



## Event preconditions
✅Miku love greater than or equal to 15

✅Event "[Miku: You and Me and the Night](./mikudorm10.md)" is completed (event=mikudorm10)



## Next events
* [Miku: Thighs On-Demand](./soccer25.md)

## Event properties
* ID: mikudorm15
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label mikudorm15:
    play sound "knock.mp3"

    s "Hey, Miku. What are you doing right now?"

    "I knock on Miku's door and, almost instantly after doing so, hear the sound of a dresser drawer slamming shut."

    mi "Sensei? Is that you bangin’ out there?"
    mi "Gimme one sec! I’m gettin’ dressed!"
    s "Do you...need help?"

    play sound "dooropen.mp3"
    scene momentsredux1
    with fade

    mi "Nope! All done!"
    s "I see you are just as quick at getting changed as you are at...literally everything else."
    mi "You know it! Just had to put my hoodie on and stuff."
    mi "What brings ya over here tonight? Bored of sittin’ at home or somethin’?"
    s "Something like that. Figured I'd drop by and see if you want to hang out."

    scene momentsredux2
    with dissolve

    mi "Well, I was just about to go for a jog, but I'd be happy to take ya along if ya want!"
    s "There is absolutely no way I can keep up with you."

    "Despite my body {i}appearing{/i} to be in great shape, it is very much {i}not.{/i}"
    "In fact, even the thought of running is making me tired. Tagging along with Miku would just slow her down."

    mi "So, what’ll it be? You gonna run around with me?"
    mi "I’ll buy ya a drink if you say yes!"
    s "I’m not going to make you buy me a drink, Miku."

    stop music fadeout 15.0

    mi "Why the heck not?! It’s just a drink! It'll giva ya one of those, uhh...incentive thingies to come out with me. Did I use that word right?"
    s "More or less. But why do you even want me to come? Won't I get in the way?"

    scene momentsredux3
    with dissolve

    mi "You think I care about that? I don't mind slowin' down to match your pace at all. I just think it sounds fun bein' out at night with somebody."
    s "..."
    mi "Pleeeeeeease?"
    s "Okay, fine. But I'm buying my own drink."

    scene momentsredux4
    with dissolve

    mi "Heck yeah, let's go! Nobody in our class ever wants to jog with me! This is great!"

    scene black
    with dissolve2

    "Miku immediately jolts down the hall, playfully punching me in the arm as she passes."
    "Sighing to myself and bracing for what is going to be a much more exhausting night than I anticipated, I follow after her..."
    "………"
    "……"
    "…"

    scene momentsredux5
    with dissolve2

    play music "retrospect.mp3" fadein 5.0

    mi "Okay! You ready to do this, Sensei?"
    s "As ready as I’ll ever be..."

    "Miku begins to stretch herself out before taking off and I make a half-hearted attempt to do the same."
    "Her hoodie lifts up each time she bends backwards and I catch a glimpse of her stomach."
    "The moonlight bounces off of it and into my eyes as if to remind me that now is the worst possible time to be thinking of things that may give me an erection."

    mi "So, what we’re gonna do is this..."
    mi "You run wherever the heck you want and I’ll jog right next to ya. Kay?"
    s "Wait, really? Isn't there, like...a path you normally take or something?"
    s "I don’t want to accidentally run into a dead-end and mess up your pace."

    scene momentsredux6
    with dissolve

    mi "Oh! Good thinkin’!"
    mi "Then, how about...you just try your best to stick next to me and I'll slow down whenever I have to?"
    mi "We don't gotta worry about any dead ends if we stick to my normal route."
    mi "And if ya ever feel your legs gettin’ tired or somethin', you can just reach over and tap my shoulder."
    mi "Slowin’ down for one night won’t do much harm since I do this pretty much every night."
    s "And I'm assuming it's too late for me to back out?"

    scene momentsredux5
    with dissolve

    mi "You got that right. You're stuck with me 'til we're out of breath, Sensei."

    "Little does Miku know, there are plenty of things we could be doing within the safety of her room that would cause us to run out of breath."
    "But I guess a little sacrifice like this won't kill me every now and then."
    "She seems excited, so...the least I can do is try to be excited with her and fail miserably."

    scene momentsredux7
    with dissolve

    mi "Okay! You ready to go? All stretched out?"
    s "Let's just get this over with..."

    scene black
    with dissolve

    "Miku moves to my side and gets into that position track team members take right before they begin a race."
    "I’m not sure if there’s a name for it or not...but whatever it’s called, it’s certainly intimidating."

    s "You’re not gonna start sprinting right out of the gate, are you?"
    mi "‘Course not! It just feels cool when you start like this!"
    mi "You should try it! Come on! Just bend your knees like this and-"

    "Miku, still hunched over and ready to take off, starts pushing against the backs of my knees, trying to force me into the potentially unnamed track position as well."
    "Not wanting to fall, I oblige and crouch down- very likely looking like an idiot."

    mi "Okay! On three...Ready?"
    s "..."

    "I take a deep breath and stare at the empty street before me."
    "There's no one here but us."

    s "..."

    menu:
        "I'm ready":
            scene nightsky
            with dissolve2
            s "Let’s do this."

    mi "That’s the spirit! Okay-"
    mi "3..."
    mi "2..."
    mi "1..."

    with hpunch

    mi "GO!"

    "And just like that, we’re off."
    "Well...{i}off{/i} probably isn't the best word to use since we start with a light jog as I try to remember how running works."
    "I can't remember the last time I did anything this physical, so it's a little hard at first...but seeing just how much I'm slowing down Miku motivates me to go a little faster."
    "Slowly but surely, I begin to pick up the pace."
    "And within a few minutes, I reach what is {i}probably{/i} my top speed..."
    "………"
    "……"
    "…"

    scene momentsredux8
    with dissolve

    mi "You’re doin’ great, Sensei! Much better than I thought you'd be!"
    s "Is that...some kind of...joke?"
    mi "No way! I really mean it!"
    mi "Sure, you're runnin’ out of breath and your face is gettin’ kinda red, but you’re still goin’ strong! I’m proud!"

    "It’s true that I’ve been able to {i}mostly{/i} keep up with Miku so far, but..."
    "Well, let’s just say I’m feeling like I could pass out at any moment."
    "I’m not sure if I’ll ever do this again, but I’m definitely glad that I didn’t make myself look like a {i}complete{/i} idiot tonight..."

    scene momentsredux9
    with dissolve

    mi "Oh! Turn left up here! This path is a lot easier for beginners. Just a bunch of really long streets and stuff."
    s "How...can you...still talk in...complete sentences?..."

    scene momentsredux8
    with dissolve

    mi "Cause I’m having fun!"

    scene black
    with dissolve2

    "Miku instinctively picks up the pace as the two of us round the corner, but she slows down once again when she realizes I can’t keep up."
    "At least she was telling the truth about this route being a series of really long streets."
    "I can’t even see the ends of them."
    "It’s almost like they go on forever."
    "………"
    "……"
    "…"

    mi "Okay! Let’s stop here for now. You look like you could use a break..."

    scene mikusweat1
    with dissolve2

    mi "You were totally great tonight, Sensei! I’m super surprised!"
    mi "You didn’t ask to stop even once!"

    scene mikusweat2
    with dissolve

    s "You know I'm never going to do this again, right?"
    mi "Yeah, I kinda figured."
    s "Are you okay, though? You’re looking awfully...flushed right now."

    scene mikusweat3
    with dissolve

    mi "Mhm! I’m totally fine. I always get kinda red when I do stuff like this."
    mi "That’s just how my body works, I guess."
    mi "But I could totally run another three or four miles if ya want!"
    s "I don't."

    scene mikusweat4
    with dissolve

    mi "Heheh...I figured. And I ain't tryin’ to break your legs tonight, so we can just hang out here until ya catch your breath."
    s "Sounds good to me. I'll probably be good to again...maybe sometime next year?"

    scene mikusweat5
    with dissolve

    mi "That’s fine..."
    mi "I wouldn’t mind hangin’ out with you for another year or so."
    mi "Maybe even longer."
    mi "Sure, Makoto might miss me, but..."
    mi "I don't know."
    mi "I kinda wish...moments like this would last forever."
    mi "It’s not often I get this hyped up outside of the soccer field."
    mi "Is that weird?"
    mi "All we did was some light jogging and it feels like my heart is about to explode."
    mi "I don’t get it..."
    mi "Is..."
    mi "Is that goin' on with yours as well, Sensei?"
    s "..."
    mi "..."

    scene mikusweat5r
    with dissolve

    s "Sure..."

    "Of course my heart is beating fast, but not for the same reasons Miku's is."
    "She's accustomed to running long distances- and her heart has been conditioned for this type of beating."
    "What it is not conditioned for is the onslaught of emotions flooding into her each time the two of us are alone."
    "But me?"
    "I am the inverse."
    "My heart is not capable of shrugging off the immense physical strain brought on by running for miles."
    "But it {i}is{/i} capable of shrugging off everything else."

    scene mikusweat6
    with dissolve

    mi "…"
    s "…"
    mi "Umm...Silence is kinda weird, so I’m gonna keep talkin’, okay?"
    s "Sure. If that's what you want to do, do it."
    mi "Got it...So, like-"
    mi "Uhh..."
    mi "I guess...thanks for hangin’ out with me and stuff tonight?"
    mi "I’m sure you wanted to stay inside instead, but I’m glad I got to give you a little taste of my world."
    mi "It's probably obvious to you by now, but I’ve always loved running."
    mi "It’s like..."

    scene mikusweat7
    with dissolve

    mi "Okay, so this is gonna sound dumb-"
    mi "But it’s almost like it's the only time I ever feel {i}alive{/i} you know?"
    mi "Every other moment is kinda like...I’m just waitin’ for somethin’ to happen."
    mi "And it seems like lotsa things have been happenin’ lately."
    mi "I’m like...actually excited to get out of bed again! And not just to go to soccer practice and see my friends, but..."
    mi "I guess the easiest way to say this is that a lot of the way I've been feelin' lately is thanks to you, Sensei."
    s "I’ve barely even done anything. I’m just following you around and letting you be yourself."

    scene mikusweat8
    with dissolve

    mi "Yeah, well..."
    mi "Maybe that’s all I needed?"
    s "…"

    "The two of us sit there, catching our breath and watching cars pass us by for a good twenty minutes or so."
    "Scattered moments of awkward silence are dropped into the mixture every so often, turning this outing into a strange concoction of melancholic contemplation and..."
    "And a sensation I may be confusing for nostalgia."
    "This feels...familiar for some reason."

    scene nightsky
    with dissolve2

    "I wonder how many nights I spent in my past life sitting on the sides of roads with sweat dripping down my face?"
    "I wonder what I did at all?"
    "This wasn't what I was like, was it?"
    "And, if it was, why does the idea of doing something like this now not ring out to me like a bell in a far off tower?"

    s "..."

    "Something pops into my head."
    "It's a poem."

    if firsttimelibrary == True:
        "And it’s one you might recognize from Futaba’s textbook."
        "It goes-"
        "‘There are days we live as if death were nowhere in the background-’"
        "‘From joy to joy; from wing to wing-’"
        "‘From blossom to blossom, to impossible blossom, to sweet impossible blossom...’"

    else:
        "That poem goes-"
        "‘There are days we live as if death were nowhere in the background-’"
        "‘From joy to joy; from wing to wing-’"
        "‘From blossom to blossom, to impossible blossom, to sweet impossible blossom...’"

    "Something...somewhere inside of me tells me I used to believe poems were just strings of random words...tied haphazardly together to create something that sounded nice but meant nothing."
    "But now?"
    "Now, I believe the opposite."
    "Now-"
    "Poems all sound horrible to me."
    "Now-"
    "Now, they just hurt."

    scene black
    with dissolve2

    "Miku and I went home shortly after that."
    "She hugged me on the steps of the dorm."
    "She did not invite me inside."

    $ renpy.end_replay()
    $ miku_love += 1
    $ mikudorm15 = True
    stop music fadeout 7.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotohjreplay:
        play sound "knock.mp3"

        "..."

        mak "Come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump makotohjreplayx
        else:
            $ makoto_lust += 1
            stop music fadeout 4.0

            "{i}Makoto's lust has increased to [makoto_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label makotofingerreplay:
        play sound "knock.mp3"
        "..."

        mak "Yes? Who is it?"
        s "The most loyal customer of the Miyamura family business."

        "I can hear a heavy sigh from inside of the room..."

        mak "You may enter, Sensei..."
        mak "Just please refrain from saying anything else about my family's shop within earshot of others..."

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump makotofingerreplayx
        else:
            $ makoto_lust += 1
            stop music fadeout 4.0

            "{i}Makoto's lust has increased to [makoto_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label makotobjreplay:
        play sound "knock.mp3"
        "..."

        "I knock on Makoto's door and wait for her to answer."
        "I can hear some shuffling around before she finally comes closer and cracks it open just enough to speak out of."

        mak "What do you want?"
        s "What do you think I want?"
        mak "You knock differently when you have ulterior motives."
        s "Are you implying I have ulterior motives?"
        mak "Are you implying you don't?"
        s "Can you just let me in? You know you want to do this too."
        mak "I know no such thing! Good day, Sens-"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump makotobjreplayx
        else:
            $ makoto_lust += 1
            stop music fadeout 4.0

            "{i}Makoto's lust has increased to [makoto_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label makotomissreplay:
        play sound "knock.mp3"
        "..."

        mak "Come in!"

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump makotomissreplayx
        else:
            $ makoto_lust += 1
            stop music fadeout 4.0

            "{i}Makoto's lust has increased to [makoto_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label mikudormfingeranim:
    play sound "knock.mp3"

    "..."

    mi "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I walk into Miku's room to find her laying on the bed and watching some action movie."
    "She pats the space beside her, sliding over to make room for me...but what I'm interested in tonight is a {i}different{/i} form of entertainment."
    "I climb onto the bed and bring myself closer to her, wrapping one of my arms around her and pulling her close."
    "She's small enough that it feels like I'm moving nothing at all- and within seconds, she returns the embrace."
    "Her tiny arms struggle to fully reach around my body, prompting her to climb onto my lap for a better shot of enveloping me."
    "But the incomplete embrace quickly transitions to kissing."
    "Which then transitions to the aggressive rocking of her hips."

    image mikudormfingeranim1 movie = Movie(play="subscribestar/images2/mikudormfingeranim1.webm")
    image mikudormfingeranim2 movie = Movie(play="subscribestar/images2/mikudormfingeranim2.webm")

    show mikudormfingeranim1 movie
    with dissolve

    "Which then transitions to this."

    mi "Ahh...ahhh...[mikumaster]...ain't this a little random?..."
    s "Do you have a problem with random, Miku?"
    mi "Not if...random always feels as good as this..."

    "Miku's pussy is as tight as ever as I struggle to fit even a full finger inside. But despite that, I can feel her arousal rapidly increasing."
    "Her face turns a bright shade of a red almost instantly as her breathing becomes labored and heavy."
    "She presses her back as deep into the mattress as it will go, trying to come to terms with the pleasure as she grinds against my hand."

    mi "How'd you...get so good at this anyway?..."
    mi "I've been tryin' to do it myself lately and...mnf...it never feels...even close to how good it feels when you do it..."
    s "Why try at all when you can just call me?"
    mi "You...tellin' me I can...call you up whenever I want and...get ya to do this to me?..."
    mi "You have any idea how many calls that'd be, [mikumaster]? You'd run outta minutes in just one week."
    s "You like it that much, huh?"
    mi "It's...friggin' amazing...I ain't ever felt as good as I do when I'm with you, [mikumaster]..."
    s "Good. Let's keep things that way."
    mi "Wha...what do you mean?..."
    s "Just that you're mine to pleasure whenever I want...and that no one else is ever allowed to touch you."
    mi "Who would even...do that anyway?...Makoto?..."
    s "That's...not really the point..."
    mi "I don't want anybody but you to touch me like this, [mikumaster]..."
    mi "You're the only person...who can see me this way..."

    show mikudormfingeranim2 movie
    with dissolve
    hide mikudormfingeranim1 movie

    mi "Ngh! [mikumaster]! It's...hard to hold back when you...go that fast!"
    s "Say it again. That I'm the only person who can see you this way."
    mi "It's just...frick...it's just you...that can...do this to me!"
    mi "Mngh...oh man...oh man...startin'...to lose focus..."
    s "Your tight little tomboy pussy can't get enough of me, huh?"
    mi "Mmf...mmmf! I can't tell if...that's an insult or...a compliment!"
    s "It means I'm enjoying this just as much as you are, Miku."
    mi "Y...Yeah?...So you're about to...explode too?!"
    s "Are you going to cum?"
    mi "I...ngh..."
    mi "I don't even...I {i}can't{/i} even..."
    mi "Ngh...crap..."
    mi "[mikumaster]...I can't...take it...anymore!"

    with sexfade
    with sexfade
    scene mikudormfingercum
    with cumflash
    with hpunch

    mi "AAAAAaAAAaaaaaaaaaAAAAAHHHHHHHH!!!!!!!~~~~~~~"

    "Miku's body convulses violently as she tries and fails to muffle the sounds of her screaming."
    "Her hips shake as she rides out the pleasure of her orgasm and, within seconds, it becomes clear that I have broken her and that we must stop here for today."

    scene black
    with dissolve2

    mi "Hah...hah...hah...water..."
    mi "Need...water..."
    s "Do you have any in here?"
    mi "The...vending machine...but...but no money..."
    s "Ah."
    s "Well, I've got nothing on me either. So don't go dying due to dehydration while I'm on my way home. Got it?"
    mi "Guh..."
    mi "I'll...see you in school if...I don't die tonight...[mikumaster]"

    "I exit Miku's room feeling both accomplished and refreshed."

    $ miku_lust += 1
    stop music fadeout 4.0

    "{i}Miku's lust has increased to [miku_lust]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudorm25:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
            if miku_love >= 15 and mikudorm10 == True and mikudorm15 == False:
                jump mikudorm15
...
```