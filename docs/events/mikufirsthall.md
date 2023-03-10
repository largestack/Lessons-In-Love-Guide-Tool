# Behind Closed Doors (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: mikufirsthall
* Group: Miku
* Triggered by label: dormtuesday
* Triggered by branch label: dorms
* Triggered by path: dorms->dormtuesday->mikufirsthall

## Official wiki page

[Behind Closed Doors](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikufirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikufirsthall:
    scene mikuhall1
    with dissolve

    mi "Sensei?! The heck are you doin' over here? You get a day pass to come hang out with us girls in the dorm or somethin'?"
    s "Nope. Just abusing my power as the lone male authority figure at school and hanging out in places I probably shouldn't be allowed in."
    mi "Well, as long as ya don't start sneakin' into the locker room, you're still A-Okay in my book!"
    mi "Not sure what kinda fun you're expectin' to have in a place like this, though. All the {i}real{/i} action is goin' on behind closed doors."
    s "I kind of need to go through the halls in order to get into any of the rooms, but I'll keep your advice in mind, Miku."

    scene mikuhall2
    with dissolve

    mi "Wait, how come you're talkin' to me, though? The girl with the biggest knockers in school is right behind ya. Probably knows more about {i}action{/i} than me, too."
    s "Who knows? Maybe I just have a thing for tomboys."

    scene mikuhall3
    with dissolve

    mi "It ain't nice playin' with a girl's heart like that, Sensei. Don't gotta pity me just cause I can't compete with the rest of the girls in looks."
    mi "Likin' tomboys is one thing, but I ain't really got any other good qualities at all when ya start gettin' down to it. Just soccer and..."
    mi "See, I got nothin'. It's literally just soccer."
    s "I'm sure you have tons of other good qualities. I just can't imagine I'll be learning about them in the hallway when, as you said, all the real action is behind closed doors."

    scene mikuhall1
    with dissolve

    mi "Hey, that woulda made a great segue thingy if you were tryin' to get into my room right now!"
    s "That...is exactly what I was doing, Miku."

    scene mikuhall4
    with dissolve

    mi "Wait, for real?! Why?!"
    s "Maybe I just {i}really{/i} have a thing for tomboys?"
    mi "Must be a pretty huge thing if you're gonna start tryin' to pick me up in the hallway!"
    s "It's pretty big, yeah."

    scene mikuhall3
    with dissolve

    mi "Umm....well I don't really know what to say, Sensei."
    mi "I like ya and all, but...I don't know if I'm really ready to take whatever steps you're tryin' to make here."
    mi "B-Besides! I'm already way behind schedule for my nightly run and...I've gotta get started on that as soon as we're done talkin'."
    s "You're planning on going out this late at night? Isn't that dangerous?"

    scene mikuhall1
    with dissolve

    mi "Dangerous? Nah. I can outrun any criminal who tries to start somethin' with me."
    mi "Chances are nobody will do that, though, since most people just confuse me for a boy on account of my...uhh...everything."
    s "I am both glad to hear that you'll be safe and saddened to hear about the whole {i}mistaken for a boy{/i} thing."
    mi "I ain't too beat up about it. Been dealin' with it forever, pretty much."
    s "If it's any consolation, you'll always be a girl to me."

    scene mikuhall3
    with dissolve

    mi "Man, where's all this comin' from, Sensei?! You been readin' one of those books about flirtin' or something lately?"
    s "I don't know if I'd consider calling you a girl {i}flirting...{/i}"
    mi "You would if you were me! I never hear that kinda stuff from anybody other than Makoto and-"

    scene mikuhall4
    with dissolve

    mi "Wait a sec! Makoto didn't put ya up to this, did she?!"
    mi "She's yelled at me three times this month for leavin' on my runs without pepper spray and she hired {i}you{/i} as an agent to come stop me with your sudden tomboy fetish!"
    s "That's-"

    scene mikuhall5
    with dissolve

    mi "Darn it, Makoto! I already told ya that the pepper spray doesn't fit into my stupid, undersized pockets!"
    mi "Why even put pockets on girl pants in the first place if ya can't friggin' fit anything in 'em?!"
    s "..."

    scene mikuhall6
    with dissolve

    mi "You got a problem, Sensei?"
    s "Nope. Just admiring your abundance of energy even as the day comes to an end."

    scene mikuhall1
    with dissolve

    mi "Why just admire when you can see it first hand? Come runnin' with me!"
    mi "I'll show ya my route and we can even stop by Makoto's place so I can yell at her for hirin' an assassin."
    s "As fun as it sounds to watch you yell at Makoto, I think I'm going to pass."
    s "Running's not really my thing."
    s "Nor is...any athletic activity, now that I think about it."
    mi "Well, suit yourself! But I can't really hang around here much longer."
    mi "Feel free to drop by again, though! Some of the other girls might be opposed to you hangin' out around here, but I think it's pretty great!"

    scene mikuhall7
    with dissolve

    mi "Just make sure ya barricade whatever doors ya wind up behind if you're lookin' for privacy since Makoto's got a key to all of 'em."

    scene mikuhall0
    with dissolve

    mi "Later, Sensei! Nice talkin' to you!"

    scene black
    with dissolve2

    "Miku gets off the ground and sprints down the hall, jumping down a flight of stairs and landing on a small platform before the next."
    "The sound echoes throughout the dorm and seems to startle even her as she needs to take a moment to collect herself after landing."
    "I turn around to see if Futaba is still here as well but, after realizing she must have gone back into her room, I decide it's probably best to just head home for the night."
    "At least I got to talk to Miku for a bit, though..."

    $ renpy.end_replay()
    $ miku_love += 1
    $ mikufirsthall = True

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikuhall:
    if chapthreeactive == True:
        scene mikusummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene mikuhall1
        with dissolve
    else:
        scene mikuhallwinter
        with dissolve

    mi "Hey again, Sensei! Did ya come to visit me?"
    mi "Let me tell you about this crazy thing I saw on the way to[school] the other day!"

    "Miku rants on and on about the eventful morning she had and I’m barely even able to get a word in."
    "We talk for a little while before she tells me she needs to leave for some late-night workout she has planned."
    "Before I know it, I’m back on my own and a little worn out."
    "I'm by no means an athlete, but hanging out with her is exercise all on its own and I'm glad I'm at least somewhat able to keep up."

    scene black
    with dissolve

    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabafirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormtuesday:
        if chapthreeactive == True and mikublock == False:
            scene summerdorm1tues
            with dissolve
        elif chapthreeactive == True and mikublock == True:
            scene dormtuesmikugone
            with dissolve
        elif christmas7 == True and chapthreeactive == False:
            scene tueswinter
            with dissolve
        else:
            scene dorm_tuesday
            with dissolve

        play music "sweetvermouth.mp3" fadein 2.0

        "I decide to pay a visit to the dorms."
        "What should I do?"

        menu tuesdaymenu:
            "Knock on a door":
                jump doorknock
            "Talk to Miku" if mikublock == False:
                if mikufirsthall == False:
                    jump mikufirsthall
...
```