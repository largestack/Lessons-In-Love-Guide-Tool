# Scaredy Cat (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 25

* Event [Thighs On-Demand](./soccer25.md) (Miku) is completed)



## Next events

* [Miku: An Extra Set of Arms](./soccer30.md)

## Event properties

* Id: mikudorm25
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm
* Triggered by path: mikudorm->mikudorm25

## Official wiki page

[Scaredy Cat](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm25&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm25:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Miku’s door and wait for her to answer."
    "The volume on the TV is turned up so loud that I can make out almost every single word from all the way out here."

    s "Miku. Open the door."

    "…"

    s "She doesn’t hear me at all, does she?"

    play sound "knock.mp3"

    "I knock again, slightly harder this time, and hear the volume start to drop."

    mi "Hm? Somebody there?"
    s "Yes. Someone is here."
    s "Can I come in?"
    mi "Oh, Sensei! Sorry about that. Of course ya can come in."
    mi "If ya ever know I'm in here and I'm not answerin', just open the door anyway. I give ya full permission."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Great idea. I'm sure that won't ever backfire in the future."

    "I open the door and push my way inside as the voices of sports broadcasters are turned down to a near-whisper."

    scene mikuthighs1
    with dissolve
    play music "love.mp3"

    mi "Heya, Sensei. Come here to talk to me about animals?"
    s "...What?"
    mi "Am I right or am I wrong?"
    s "Why would you just...assume that's what I'm here to talk to you about?"
    mi "Just had this look on your face that made me think ya wanna talk about animals. I'm sure you know what I mean."
    s "Have you been drinking?"
    mi "Hey, it was worth a guess. You miss 100%% of the shots you never take."
    s "Were you even aiming at the goal?"

    scene mikuthighs2
    with dissolve

    mi "Nope. But sometimes I’ll get really lucky and make it in by just shootin' in the general direction of it."
    s "As your coach, who admittedly knows next to nothing about soccer, I recommend that you aim at the goal from now on."
    mi "Yeah, yeah. Now, you gonna tell me what you’re here for? Or are you just gonna stare at me while I work out all these knots?"

    "Miku lightly pushes down on her skin, kneading it in small circles and {i}stealing the job I was put on this earth to do.{/i}"

    s "Are you insulting me right now?"

    scene mikuthighs3
    with dissolve

    mi "Am I? Cause I sure as heck didn't mean to."
    s "You are stealing my rightful job as your coach by giving yourself a massage instead of allowing me to do it."
    mi "Well, it ain't like I'm gonna call you over here just so you can rub my legs and stuff."
    s "Then why do I even have a phone?"
    s "Am I not good enough for you? I thought we were friends."

    scene mikuthighs4
    with dissolve

    mi "Slow down, buddy! We {i}are{/i} friends! I just figured you'd have better stuff to be doin' right now!"

    scene mikuthighs5
    with dissolve

    mi "And I...also think Makoto might get a little jealous if you start massagin' me before her."
    s "I’ve massaged her plenty of times."

    "And by plenty I mean...once?"
    "Which obviously means it should be Miku's turn next."

    scene mikuthighs6
    with dissolve

    mi "Woah, really? Why the heck wouldn't she tell me about such a huge development like that?"
    s "I wouldn't call it a huge development since it's basically the same thing you did for me in the storage shed the other day."
    s "Just some completely wholesome, G-rated shoulder rubbing."

    if bonus == True:
        mi "Not even a little PG-13? Ya didn’t try to cop a feel or anythin’?"
        mi "Makoto’s boobs aren’t {i}big,{/i} but ya’d probably still have a heck of a time playin’ around with ‘em if ya wanted."
        mi "Meanwhile, I'm over here with about as much to offer in the chest department as a lunch-tray."
        s "Everyone likes lunch trays. They carry lunch and lunch is good."

        scene mikuthighs7
        with dissolve

        mi "Yeah, it's great. But I don’t see what that has to do with you gettin’ all touchy-feely with someone who looks like a prepubescent boy."
        s "Prepubescent is a pretty big word for you, Miku. "

        scene mikuthighs8
        with dissolve

        mi "And unfortunately one I know very well after countless Google searches about why I ain't growin' as fast as everybody else... "
        mi "Sometimes, I feel like only Ami understands me."
        s "What about Sana? Or Maya? Or...any of the other girls in the school who are struggling with the same {i}issue{/i} as you?"
        mi "You think {i}Maya{/i} cares about her boobs? She's too busy bein' all weird and smart and cool and stuff. Ami's the only other person actually beat up about it."
        s "Why are we even talking about breasts right now? I'm offering to massage your legs, not your chest."
        mi "Hey, I don't know how good your aim is. Maybe you'd mess up and start grabbin' at the wrong thing?"
        s "I would have to be blind to make a mistake that drastic."

        scene mikuthighs9
        with dissolve

        mi "I guess so. Especially since it would take sniper-precision to grab these mosquito bites in the first place."
        s "Are you really going to sit there continuously massaging your own thighs instead of letting someone with hands as large as {i}these{/i} take over?"

    "I present my hands toward Miku and begin to move my fingers in an incredibly creepy and suggestive manner."
    "I don’t mean to, it just kind of happens naturally."

    scene mikuthighs10
    with dissolve

    if bonus == True:
        mi "Uhh...yeah, they’re really heckin’ big. But why are ya movin’ em around like that?"
    else:
        mi "..."
        mi "I feel like we either just missed a decent chunk of dialogue or yer goin' friggin' crazy, Sensei."
        s "Lol."

    mi "This some weird kinda...Swiss massage technique or somethin’ they teach ya in college?"
    s "My instinct tells me to say yes to that, but I think it’s important that you know they don’t teach massage techniques in college."

    scene mikuthighs11
    with dissolve

    mi "I don’t know, Sensei..."
    mi "A few months ago, you probably coulda convinced me."

    if bonus == True:
        jump mikuthighsx
    else:
        scene black
        with dissolve

        mi "But unfortunately for you, I ain't gettin' convinced tonight."
        s "Can I at least have a hug."
        mi "What, like, from me?"
        s "Yeah."
        mi "Uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh yeah okay."

        "We hug =D"

        $ renpy.end_replay()
        $ miku_love += 1
        $ mikudorm25 = True
        stop music fadeout 5.0

        "{i}Miku’s affection has increased to [miku_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mikudorm30:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

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
            if miku_love >= 25 and soccer25 == True and mikudorm25 == False:
                jump mikudorm25
...
```