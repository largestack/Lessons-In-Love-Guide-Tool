# One. Two. Three. (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [One. Two. Three.](./mikudorm30.md)

## Event preconditions

* Miku love greater than or equal to 30

* Event [An Extra Set of Arms](./soccer30.md) (Miku) is completed)

* Day of week is not Thursday

* trinity3track equal to True (unknown variable)



## Next events

* [Main: As Loud as a Whisper Can Be](./day214.md)
* [Makoto: Bluejay](./makotodorm25.md)
* [Miku: Loxonin](./soccer35.md)

## Event properties

* Id: mikudorm30
* Group: Miku
* Triggered by label: mikudorm30
* Chain sources: mikudorm30
* Chain sources path: mikudorm30

## Official wiki page

[One. Two. Three.](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm30&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm30:
    "I go to knock on Miku’s door and-"

    mak "Miku! Are you really planning on going out tonight? "
    mak "The weather forecast says it’s supposed to rain. You don’t even have an umbrella."

    "And I suddenly hear Makoto lecturing the girl I am here to see."

    mi "I’ll be fine! It never rains around here. And those weather thingies are always wrong anyway."
    mak "Well, that may be true, but-"
    mi "I said I’ll be fine! Just go back to yer borin’ ole’ books and let me get my night run in."
    mak "They’re not- ugh. Fine."
    mak "Just call me if you need anything and I can have my mom go pick you up."
    mi "Roger that! See ya in a few hours!"

    "The conversation comes to a stop and, before I know it-"

    play sound "dooropen.mp3"
    scene onetworedux1
    with fade

    mi "Sensei? What are you doin' over here?"
    s "Same thing I’m always doing over here. Trying to kill time."
    s "Where are you off to?"

    scene onetworedux2
    with dissolve

    mi "Wherever. Was in the mood to get my body movin’ so I was thinkin’ about hittin' up my normal route."
    mi "Wanna come with me? It’s the same one I took you to last time that you totally hated."
    s "So...you’re inviting me again despite knowing I hated it?"
    mi "Yup! You in?"
    s "…"
    s "Yeah, I guess so. Not like I had anything better to do."
    mi "Sure you don’t wanna go talk to Makoto instead? She could probably use the company."
    mi "Who the heck studies this late anyway? This is prime time for doin’ fun stuff!"
    s "You might be underestimating just how much fun Makoto has while studying."

    "To be fair, though, it’s highly plausible that she’ll use her time to do other...Makoto things instead."
    "I’ll leave her be for now and catch up with her some other time."

    s "You sure it’s going to be fine with the rain, though?"
    mi "Course I am. When was the last time you saw it rain here? Just doesn’t happen."
    mi "Startin’ to think there might be some kinda top secret barrier hoverin’ over the city preventin’ us from gettin' stuff like that."
    mi "Already got one surrounding us. Another on top wouldn't hurt."
    s "Interesting theory. A dome would definitely explain the extremely predictable weather pattern."

    scene onetworedux3
    with dissolve

    mi "You know it! Now get yer friggin' butt into gear and let’s get a move on, Sensei! The night waits for no one!"
    mi "Last one to the street has to buy the other a condo!"

    scene black
    with dissolve2

    "Miku bolts past me and like always, jumps down an entire flight of stairs on the way outside- leaving me all alone with an unanswered question."

    s "Why a condo?..."

    stop music fadeout 5.0

    "………"
    "……"
    "…"

    scene mikudarkrain1
    with dissolve
    play music "retrospect.mp3"

    "Miku and I spend the next thirty-minutes or so jogging to the same area she took me to the last time we went out at night."
    "Surprisingly enough, I didn’t completely hate myself the entire way here this time around."
    "Could it be that just being around Miku is enough to train my stamina without actually having to do anything?"
    "If so, I should probably hang around her a little more often."
    "It might add a few more years to my life."

    s "Hey. Mind explaining why we’re stopping in the middle of the road instead of some storefront porch or something?"

    scene mikudarkrain2
    with dissolve

    mi "Hm? Don’t see why it matters. Not like any cars are gonna come around here this time of night."
    mi "No one really drives over here anyway since a lot of these places are out of business."
    s "Is that why you normally come here to run instead of like, the park or something?"
    mi "There are a bunch of reasons I come here, but I guess that would be one of ‘em, yeah."
    mi "It’s also nice that the streetlights work. For some reason, the ones in the park get all...flickery sometimes and it gives me the friggin’ creeps."
    s "Do you get scared easily, Miku?"

    scene mikudarkrain3
    with dissolve

    mi "The heck do you think? Was one panic attack not enough for ya? Want me to flip out again?"
    s "I meant in general. From things that don’t involve loud noises."

    scene mikudarkrain4
    with dissolve

    mi "Umm...maybe? Maybe...not?"
    mi "Haven’t ever really thought about it before."
    mi "I just try to take things as they come. If ya spend yer entire life livin’ in fear, yer gonna wind up missin’ out on some pretty great things."
    mi "Like, for example, if I was scared of the dark, we wouldn’t have been able to come out here tonight."

    scene mikudarkrain5
    with dissolve

    if bonus == True:
        mi "Which means ya’d probably be back in the dorm room playin’ tonsil-hockey with Makoto while she tries to study or somethin’."
        mi "And I’d probably be at Karin’s house doin’ sit-ups and watchin’ shark documentaries on her fancy TV."
        s "That’s an interesting set of hypotheticals you swapped this out for. I’m not so sure about the tonsil-hockey part, though."

        "As a matter of fact...have I ever even kissed Makoto?"
        "..."
        "Huh."
        "I don’t think I have."
        "How the hell did we skip kissing on the way to sex?"
        "I suddenly feel even worse about taking her virginity than I did before. Which was still kind of bad."
        "Not {i}really{/i} bad, though."
        "She was asking for it."
        "Like, literally."
        "She asked probably a thousand times."
    else:
        mi "Which means ya’d probably be back in the dorm room playin' Jenga with Makoto."
        s "Makoto {i}does{/i} love wooden rectangle based games."

    scene mikudarkrain6
    with dissolve

    mi "It’s gonna be a real buzzkill havin’ to change up my route soon, ya know?"
    s "What? Why would you have to change your route?"
    mi "This place normally fills up with snow pretty quick in the winter."
    mi "Falls right through the cracks in the overhangs and sticks to the cement so hard that ya can’t even {i}think{/i} about runnin’ on it without fallin’ over and crackin’ yer skull."
    s "What are you going to do instead, then?"

    scene mikudarkrain7
    with dissolve

    mi "The track at[school], maybe?"
    s "As if you don’t already spend enough time there."
    mi "Well, it’s that or a treadmill at one of the other girls’ houses and I’m not a big fan of indoor exercise. Just doesn’t feel the same, ya know?"
    s "Not really. Exercise is exercise. I don’t think it matters whether you’re indoors or outdoors."
    mi "Take a look up and try sayin’ that again, why don’t ya?"
    s "…"

    scene nightsky
    with dissolve2

    "I take a look up and find exactly what I expect to find."
    "The same sky as always."
    "Why does everyone always expect me to think there’s something beautiful about it when it’s just a dark, expansive blanket of dead stars?"
    "First it was Maya...now it’s Miku."
    "These girls would be better off looking for beauty in things that are still living rather than things that died a long, long time ago."

    mi "Pretty cool, right? Can’t see that indoors, now can ya?"
    s "I mean, you could buy those stick-on stars that young girls normally attach to their ceilings and get something...kind of similar."
    mi "Oh! I always wanted those when I was little!"
    mi "Think Makoto would let me stick 'em to the ceiling of the dorm room?"
    s "Makoto? Absolutely not. There’s probably some sort of rule against it."

    scene mikudarkrain8
    with dissolve

    mi "Ugh...really? But we're allowed to hang up posters."
    s "Hey, don't ask me. Ask your walking rulebook of a roommate."
    mi "How'd a free spirited tomboy like me end up with such a strict best friend anyway? What kinda nonsense is that?"
    s "Chances are you just gravitated toward someone to keep you in check."
    s "That whole thing about opposites attracting isn’t as untrue as-"

    scene mikudarkrain9
    with dissolve

    mi "Oh, would ya look at the time? Break’s over, Sensei! Time to start runnin’ again!"
    s "Come on, that tangent wasn’t going to be nearly as boring as you expected it to be..."

    scene black
    with dissolve2

    mi "Get up! We’re not even halfway done yet!"
    mi "Ya can talk about yer borin’ life lessons while we do another lap!"
    s "Wait, we're not even halfway done? Just how long are you planning on going tonight?"
    mi "At least another hour! Now get a move on before I leave ya in the dust!"
    s "Ugh..."

    "Miku and I start jogging once again, back down the same streets we took on our first lap."
    "It’s clear that she has a defined route she likes to stick to, so I remain at her side just trying to keep up."
    "When we first did this, she had no problem lowering her pace to make sure I didn’t give up. But now it’s like she’s intentionally speeding up to try and...make me {i}improve{/i} or something."
    "I don’t want to improve, though."
    "Improving means that I’d need to run even more to ensure I don’t slip into bad shape again."
    "And, I know this might sound shocking, but I {i}hate{/i} running."
    "…"
    "Another fifteen minutes pass by and I can no longer keep up with Miku. "
    "She makes it to the end of each street long before I do and simply jogs in place, waiting for me to catch up."
    "Eventually, I go from feeling pretty good to feeling like I’m going to pass out if I take another step..."

    scene mikudarkrain10
    with dissolve

    mi "Come on, Sensei! Yer doin’ great!"
    mi "Just one more lap and we can head on home!"
    s "Can’t...make it...any...more...laps..."
    mi "Sure ya can! I believe in you! "
    mi "Deep breaths, ready?"
    mi "One..."
    mi "Two..."
    mi "Three..."

    stop music
    play sound "thunder.wav"
    scene mikudarkrain11

    mi "………………………………………………………………………………………………………"
    s "…"

    "Oh no."

    scene mikudarkrain12
    with dissolve2
    play music "rainloop.wav" fadein 3.0

    mi "Hah..."
    mi "Ahh..."
    mi "...S..."
    mi "...........S..."

    scene mikudarkrain13
    with dissolve2

    mi "...Sen...sei?"
    s "It’s just rain, Miku."
    mi "............huh?"
    s "It's just rain."

    "My instincts tell me to pull this girl to safety and hide her away from two different storms. "
    "The first of the two batters us with heavy raindrops and soaks us to the core."
    "I’m colder now than I’ve ever felt before."
    "The second storm is the one you probably assumed I was alluding to."
    "The one inside of her head, causing her legs to shake and her eyes to grow wide and fill with tears."

    mi "R...a...i...n...?"

    scene mikudarkrain14
    with dissolve2

    mi "Rain..."
    mi "It’s...raining..."
    mi "It’s...so...quiet..."
    mi "So..."
    mi "Why...am I..."
    s "…"

    scene mikudarkrain15
    with dissolve2

    mi "{i}Where{/i}...am I?..."

    play sound "static.mp3"
    scene help
    with flash
    scene help2
    with flash
    scene help3
    with flash
    scene help4
    with flash
    scene help5
    with flash
    stop sound
    play sound "thunder.wav"
    scene mikudarkrain16
    with flash

    mi "Where did everyone go?..."
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"

    scene black

    "{i}////////////////////////////////SCENE - BLACK{/i}"
    "///////////////////////////////////CONNECTING..."
    "///////////////////////////////////ONE NETWORK WITHIN REACH"
    "///////////////////////////////////WOULD YOU LIKE TO CONNECT TO “USER2” ?"

    menu:
        "Yes":
            "///////////////////////////////////CONNECTED TO “USER2”"

            s "Come with me."

            "I grab Miku’s hand and pull her under the first archway I can find to shelter her from the rain."
            "I’m not sure what is going on, but letting her just stand here in the middle of a downpour isn’t going to help in any way."

            mi "NO! DON'T TOUCH-"

            "I ignore Miku’s resistance and pull her with all of my strength."
            "She struggles for a minute or two, almost falling to the ground time and time again."
            "But she eventually gives in-"
            "Because she is so much weaker than me."

            play sound "static.mp3"
            scene mikudarkrain17
            with flash
            stop sound

            "The resistance finally ends and she locks herself around my arm."
            "I remain useless."
            "My body converts from a living, sentient organism to an inanimate object meant to provide solace to a girl who has slipped her tongue into the mouth of Hell."

            mi "Hah...hah...hah..."

            "I want to comfort her, but I cannot."
            "So I will wait."

            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"

            "It goes on forever."

            scene mikudarkrain17
            with dissolve2

            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "Hah...hah...hah..."
            s "…"
            mi "…"
            s "…"

            "Until it doesn't."

            scene mikudarkrain18
            with dissolve2

            mi "Sensei?..."
            s "Welcome back."
            mi "Did..."
            mi "Did I..."
            s "Don’t worry about it."
            mi "And..."
            mi "And you...{i}stayed{/i} with me?..."
            s "Obviously."

            scene mikudarkrain19
            with dissolve

            mi "Well, that’s friggin’ embarrassing..."
            s "It’s fine. "
            s "I’m here."
            s "The thunder only struck twice and the rain’s already started to slow down."
            mi "Yeah."

            scene mikudarkrain20
            with dissolve

            mi "Let’s...head back once it stops."
            s "Done running for the night?"
            mi "Yeah..."
            mi "Makoto’s not gonna be happy when I walk into the room soakin’ wet."
            s "Wanna stay at my place instead?"
            mi "No thanks. I don't wanna have to explain things to Ami and...I kinda need my body pillow to fall asleep."
            mi "Is it okay if...I hang on to you for now, though? I don’t think I can hold myself up on my own just yet."
            s "Of course..."

            scene black
            with dissolve2
            stop music fadeout 10.0

            "The rain stops within the next fifteen minutes."
            "The two of us remain under the archway of an unfamiliar store for five extra minutes just to make sure the storm doesn’t start up again."
            "When it doesn’t, we quietly and awkwardly make our way back to the dorm."
            "Before making the walk of shame back upstairs in her still-damp hoodie, Miku wraps her arms around me and gives me the single coldest hug I’ve ever had in my life."
            "It starts raining again halfway through my walk home."

            $ renpy.end_replay()
            $ mikudorm30 = True
            $ miku_love += 3

            "{i}Miku’s affection has increased to [miku_love]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        "No":
            "///////////////////////////////////PLEASE REFRESH YOUR MODEM AFTER ENSURING ALL WIRES ARE PROPERLY CONNECTED"
            "///////////////////////////////////THE SYSTEM WILL NOW ATTEMPT TO REFRESH ITSELF"
            "///////////////////////////////////..."
            "///////////////////////////////////..."
            "///////////////////////////////////..."
            play music "sweetvermouth.mp3"
            play sound "static.mp3"
            scene helpme
            with flash
            scene happy4
            with flash
            scene helpme
            with flash
            scene happy6
            with flash
            scene helpme
            with flash
            scene happy7
            with flash
            scene helpme
            with flash
            scene happy2
            with flash
            scene helpme
            with flash
            scene happy1
            with flash
            scene helpme
            with flash
            scene happy9
            with flash
            scene dorm
            with flash
            stop sound
            jump mikudorm30

label makotodorm20:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
mi "Hah...hah...hah..."
            s "…"
            mi "…"
            s "…"

            "Until it doesn't."

            scene mikudarkrain18
            with dissolve2

            mi "Sensei?..."
            s "Welcome back."
            mi "Did..."
            mi "Did I..."
            s "Don’t worry about it."
            mi "And..."
            mi "And you...{i}stayed{/i} with me?..."
            s "Obviously."

            scene mikudarkrain19
            with dissolve

            mi "Well, that’s friggin’ embarrassing..."
            s "It’s fine. "
            s "I’m here."
            s "The thunder only struck twice and the rain’s already started to slow down."
            mi "Yeah."

            scene mikudarkrain20
            with dissolve

            mi "Let’s...head back once it stops."
            s "Done running for the night?"
            mi "Yeah..."
            mi "Makoto’s not gonna be happy when I walk into the room soakin’ wet."
            s "Wanna stay at my place instead?"
            mi "No thanks. I don't wanna have to explain things to Ami and...I kinda need my body pillow to fall asleep."
            mi "Is it okay if...I hang on to you for now, though? I don’t think I can hold myself up on my own just yet."
            s "Of course..."

            scene black
            with dissolve2
            stop music fadeout 10.0

            "The rain stops within the next fifteen minutes."
            "The two of us remain under the archway of an unfamiliar store for five extra minutes just to make sure the storm doesn’t start up again."
            "When it doesn’t, we quietly and awkwardly make our way back to the dorm."
            "Before making the walk of shame back upstairs in her still-damp hoodie, Miku wraps her arms around me and gives me the single coldest hug I’ve ever had in my life."
            "It starts raining again halfway through my walk home."

            $ renpy.end_replay()
            $ mikudorm30 = True
            $ miku_love += 3

            "{i}Miku’s affection has increased to [miku_love]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        "No":
            "///////////////////////////////////PLEASE REFRESH YOUR MODEM AFTER ENSURING ALL WIRES ARE PROPERLY CONNECTED"
            "///////////////////////////////////THE SYSTEM WILL NOW ATTEMPT TO REFRESH ITSELF"
            "///////////////////////////////////..."
            "///////////////////////////////////..."
            "///////////////////////////////////..."
            play music "sweetvermouth.mp3"
            play sound "static.mp3"
            scene helpme
            with flash
            scene happy4
            with flash
            scene helpme
            with flash
            scene happy6
            with flash
            scene helpme
            with flash
            scene happy7
            with flash
            scene helpme
            with flash
            scene happy2
            with flash
            scene helpme
            with flash
            scene happy1
            with flash
            scene helpme
            with flash
            scene happy9
            with flash
            scene dorm
            with flash
            stop sound
            jump mikudorm30
...
```