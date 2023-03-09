# A Dog that Does Math
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikafirsthall&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Chika: Something About Biting](./chikadorm5.md)

## Event properties
* ID: chikafirsthall
* Group: Chika
* Triggered by label: dormwednesday
* Triggered by branch label: dormwednesday

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label chikafirsthall:
    scene chikahall1
    with dissolve

    c "Whaaaaaat? No friggin’ way! This can't be happening!"
    s "Hey Chika. What’s going on?"

    scene chikahall2
    with dissolve

    c "This can't be happening!"
    s "I heard that much. {i}What{/i} can't be happening, exactly?"
    c "So, this girl I work with at the mall just got a new puppy, and she taught it friggin' {i}math!{/i}"
    s "..."
    c "..."
    s "{i}Why?{/i}"

    scene chikahall3
    with dissolve

    c "I don't know, Sensei! Can't you at least be happy for her, though? This is like, a totally huge deal!"
    s "Happy for your friend? Or happy for the dog?"
    c "The dog, obviously!"
    c "Like, my friend is the one who posted the video online and it's gotten her like a trillion new followers, but the {i}dog{/i} is the real hero here! We all know that!"
    c "Here! Look for yourself. You aren't impressed enough."

    scene chikahall4
    with dissolve

    "Chika hands me her phone and, sure enough, there is a video of a dog doing math."

    c "That dog is going places, Sensei. It's even better at math than Ami."
    s "I...don't really understand what I'm watching here."
    c "What's not to understand? My friend asks the dog a basic math problem and then it just barks the correct amount of times."
    s "I guess what I'm {i}really{/i} not understanding is why someone would waste their time teaching something like that to an animal."

    scene chikahall5
    with dissolve

    c "Well...why do you teach people? I'm sure it's probably for the same reason."
    s "Your friend was reborn into a world where she was {i}already{/i} teaching?"
    c "I don't know, maybe. If Kanye West can win 23 Grammys, pretty much anything is possible."
    c "Wait, what are you even doing over here? I didn't think boys were allowed in the girls' dorm."
    s "I'm a special exception to that rule."
    c "Is it because Ami lives here? Are you here to teach her math?"
    c "Should I call my friend's dog?"
    s "I'd rather spend my time exclusively with humans, personally."

    scene chikahall6
    with dissolve

    c "Well, I'm a human! You can hang out with me! It's obviously not like I have anything else planned if I'm out in the hall watching TikTok."
    s "Well, I guess that's that then. But I'd kind of prefer to go into your room instead of staying out here where everyone else can hear us...talk about dogs or something."

    scene chikahall7
    with dissolve

    c "I mean...{i}I{/i} don’t have a problem with that...but I’m pretty sure Yumi would literally kill me if I ever let you see where she sleeps."
    s "Yumi seems like the type of person to kill you for even talking to me, so I'm glad you're at least doing that much."

    scene chikahall8
    with dissolve

    c "Yeah...she's really got it out for you for some reason."
    c "I guess even she accepts that I can't just {i}not{/i} talk to my teacher, though."
    s "So, if we can’t go inside, what do you want to do?"

    scene chikahall6
    with dissolve

    c "Oh! I know! How about you tell me a little more about yourself?"
    c "If we're gonna be doing that whole...informal teaching thing or whatever it was, shouldn't we like, know more about each other?"
    s "Well, what do you want to know, exactly?"
    c "I don't know. Anything, really. Like...what are you good at? What are your interests?"
    s "...huh."

    "You know...I'm not really sure."
    "I haven't really had time to get reacquainted with who {i}I{/i} am yet, but..."

    s "I think..."
    s "I think I've always been good at...writing?"

    scene chikahall9
    with dissolve

    c "A writer? Color me impressed."
    c "What kind of stuff do you write?"
    s "Nothing anymore. But I feel like-"

    play sound "static.mp3"
    scene whygodwhy with flash
    scene chikahall9 with flash
    stop sound

    s "Nothing anymore."

    scene chikahall6
    with dissolve

    c "Well, if you ever start up again, maybe you could show me something?"
    s "I'll...keep that in mind..."

    scene chikahall9
    with dissolve

    c "You okay, Sensei? You look kinda pale all of a-"

    play sound "knock.mp3"
    scene chikahall10
    with hpunch

    y "Chika? The fuck are you doing out there? You're bein' loud as shit."
    y "This about that fuckin' smart dog or whatever again? How many times are you gonna watch that shit?"

    scene chikahall11
    with dissolve

    c "As many as it takes, Yumi! He's a good boy and you know it!"
    y "Just keep it the fuck down, please. I'm tryin' to sleep."

    scene chikahall8
    with dissolve

    c "Sorry, Sensei. I should...probably be heading back in now anyway."
    c "But we should definitely do this again sometime."
    s "Sounds good to me."
    s "Just make sure you don't mention that I was here when you head back in or we might never be able to see each other again."

    scene chikahall12
    with dissolve

    c "My lips are sealed~"

    scene black
    with dissolve

    "Chika vanishes back into her dorm room and I’m left with nothing to do once again."
    "I guess I’ll just go home and hang out with Ami or something..."

    $ renpy.end_replay()
    $ chikafirsthall = True
    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikahall:
    if chapthreeactive == True:
        scene chikasummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene chikahall6
        with dissolve
    else:
        scene chikahallwinter
        with dissolve

    c "Sensei! Welcome back! Did you come all the way over here just to see me?"

    "Chika grabs the sleeve of my jacket and pulls me over to watch something on her phone."
    "We hang out for a little while until Yumi screams something from the inside of her room again."
    "Chika ignores her a good three or four times before finally giving in and apologizing for her friend’s behavior."
    "It would be nice to actually spend some time alone with her for once. I can feel the two of us getting closer."
    "I guess I’ll just have to keep at it until then..."

    scene black
    with dissolve

    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotofirsthall:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label dormwednesday:
    if chapthreeactive == True:
        scene summerdorm1wed
        with dissolve
    elif rinsad == True and chapthreeactive == False:
        scene wedwinterringone
        with dissolve
    elif cafe15 == True and rindorm20 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif beachvacation16 == True and rindorm35 == False and chapthreeactive == False:
        scene dorm_wednesday2
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene wedwinter
        with dissolve
    else:
        scene dorm_wednesday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "This might be a good time to hang out with one of the girls."

    if cafe15 == True and rindorm20 == False or rinsad == True:
        "It looks like Chika isn't doing anything."
        "I can probably spend time with her if I want to."
        "What should I do?"
        jump wednesdaymenu
    if beachvacation16 == True and rindorm35 == False or rinsad == True:
        "It looks like Chika isn't doing anything."
        "I can probably spend time with her if I want to."
        "What should I do?"
        jump wednesdaymenu
    else:
        "It looks like Chika and Rin aren’t doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
        jump wednesdaymenu

    menu wednesdaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Chika":
            if chikafirsthall == False:
                jump chikafirsthall
...
```