# Morals vs. Orgasms
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinfirsthall&go=Go)



## Event preconditions
✅Event "[Main: What Was](./day271.md)" is completed (event=day271)



## Next events
None

## Event properties
* ID: kirinfirsthall
* Group: Kirin
* Triggered by label: dorm2thursday
* Triggered by branch label: dormthursday

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label kirinfirsthall:
    scene kirinhall1
    with dissolve

    ki "Yo. "
    ki "Please tell me you’re here for me. I’m bored as shit."
    ki "I was actually just about to text you begging you to come over."
    s "I am here for you, Kirin."
    ki "Thank fucking God."
    ki "Noriko’s been blasting music for like two hours and I’m about to pour liquid cement into my ears."
    s "I take it things aren’t going well in there?"
    ki "Oh, things are actually really great. Just kind of annoying at times. "
    ki "But it’s not like I can tell her to chill when it’s her room, too. She can do whatever she wants."
    ki "I’m sure there will be plenty of times where {i}she’ll{/i} get mad at me, so learning how to deal with that is a pretty logical first course of action."
    ki "Whatever the case, it sure beats staying at home. "
    s "Ramping up to complain about your sister again?"

    scene kirinhall2
    with dissolve

    ki "What do you mean, “ramping up?”"
    ki "You make it sound like that’s a thing I do all the time."
    s "I mean...not {i}all{/i} the time."
    s "You’ve definitely made me aware of how much you hate living at home before, though."
    s "But despite that, you still waited until you were put in my class to move into the dorms."
    s "Why didn't you just bite the bullet and move into the other building?"

    scene kirinhall3
    with dissolve

    ki "Are you {i}trying{/i} to be a dick to me right now, or is this just happening on accident?"
    ki "All I did was talk to you and now it’s like you’re fucking profiling me or something."
    s "I didn’t mean it like that. "
    s "I’m obviously glad you’re here. I wouldn’t have come to see you if I wasn’t."
    s "I just...also like your sister and wouldn’t feel right if I didn’t at least try to stand up for her."

    scene kirinhall4
    with dissolve

    ki "Well...yeah...that makes sense."
    ki "Sorry for being so on edge or whatever. I shouldn’t have exploded like that."
    ki "It’s just weird, you know?"
    ki "Even though I love it here, it’s still a huge frickin’ transition going from your parents’ house to living with some girl you literally just met."

    scene kirinhall5
    with dissolve

    ki "Buuuuut...that’s enough emotional Kirin for now. Help me take my mind off of that stuff, Sensei."
    ki "I’m sure you didn’t just come over here to hear me complain."
    s "If you want to complain, it’s fine-"
    ki "I {i}said{/i}...I’m sure you didn’t come all the way here to hear me complain."
    ki "Take my fucking mind off stuff. "
    s "…"
    s "You can be really intimidating when you’re in a bad mood, Kirin."

    scene kirinhall6
    with dissolve

    ki "You just need to learn how to deal with me. Don’t call me intimidating just because you haven’t figured it out yet."

    if kirinpatgasm == True:
        s "Will more headpats do the trick? Because you seemed to {i}really{/i} like those."

        scene kirinhall7
        with dissolve

        ki "Wha-?! No?! That won’t do the trick at all! "
        ki "I didn’t even like them that much!"
        s "I distinctly remember you liking them so much that you started pleasuring yourself."
        ki "Shut up!"
        s "I had to wash my sheets and everything."

        scene kirinhall8
        with dissolve

        ki "OH MY GOD, STOP!"

    else:
        s "Well, here’s hoping I’m actually able to do that one day."
        ki "If there’s anyone who can right now, it’s definitely you."
        s "Because I’m the first boy you’ve ever had feelings for?"

        scene kirinhall9
        with dissolve

        if bonus == True:
            ki "There’s a difference between “having feelings” and “wanting to feel you inside of me.”"
            s "Please don’t turn me on in the hallway."
            ki "I’d turn you on in the room but Noriko’s music would kill the mood for me."
            ki "You’re just going to have to hang in there, Sensei~"
            s "Yeah, yeah..."
        else:
            ki "There’s a difference between “having feelings” and just wanting to hug somebody a whole bunch, you big jerk."

    s "Anyway, have you been getting acclimated to life here apart from all of the Noriko stuff?"
    s "It must be a lot easier getting to[school] now, right?"

    scene kirinhall10
    with dissolve

    ki "I guess so, yeah."
    ki "Like, my parents’ house is far enough away for them to send buses and whatnot, but Karin and I never really took them."
    s "Is it because Karin thinks it’s best to get exercise early in the morning to...set your body up for the rest of the day or something?"
    ki "I don’t know, probably. That sounds like a thing she would say."
    ki "I just don’t really like buses. Or trains, really."
    ki "Or any small space with a lot of people, I guess."
    ki "People suck. Why would I ever want to be surrounded by them? "
    ki "It also means that there’s probably someone in that group who’s going to think {i}I{/i} suck as well."

    if bonus == True:
        s "You do suck. And you’re quite good at it."

        scene kirinhall11
        with dissolve

        ki "Yay. Blowjob compliment."
        ki "My parents would be so proud."
    else:
        s "But you're so awesome and talented and your hair smells so nice."

    scene kirinhall10
    with dissolve

    ki "But really, though. Fuck everybody."

    if bonus == True:
        s "I mean, if-"
        ki "Stop making sex jokes whenever I use a word that could also be considered suggestive."
        s "But that’s like, half of my strategy for keeping a conversation going."
        ki "Are you sure it’s not half of your strategy for grooming [teenage]girls into thinking sex is cool and casual and that it would be totally fine to have it with you?"
        s "That does sound more in-line with how I think, yes."
    else:
        s "Your attitude could use a little adjusting, though."
        s "I thought growing platonically closer to you might fix that, but..."

    scene kirinhall1
    with dissolve

    ki "Well, hey. It’s definitely working, so it’s not like I can really bash you for it."
    s "Right. You can just call me out on it and make me question my morals."

    if bonus == True:
        ki "What morals?"
        s "See? Now I have to pretend to have them because you think I don’t."
        ki "Who needs morals when orgasms exist? Just do whatever you want as long as both parties consent."
        ki "Doesn’t matter if it’s teacher and student. Husband and mistress-"
        s "Uncle and niece."
    else:
        ki "Not only does our platonic relationship have nothing to do with your morals, the moral compass you {i}do{/i} have is infallible and unbreaking."
        ki "I truly do wish more people could be like you."
        s "Thanks, Kirin."
        ki "No problem, boy'o. Now brace yourself because I'm gonna hit you with a random question."

    scene kirinhall12
    with dissolve

    ki "…"
    s "…"
    ki "Do you..."

    if bonus == True:
        ki "Do you want to fuck Ami?"
    else:
        ki "Do you want to hug Ami?"

    if amifingered == True and bonus == True:
        s "I have no idea what you’re talking about."
        ki "But..."
        ki "But you just said-"
        s "Well, it’s been fun, Kirin. But it’s probably time for me to start heading back."
        ki "I’m..."
        ki "I’m gonna...go ahead and forget I heard that."
        s "Again, no idea what you’re talking about."

    else:
        if bonus == True:
            s "No, of course not."
            s "But I can’t help but feel like it’s not the other way around sometimes."
            ki "Did like, something happen?"
            ki "Does she sneak into your room at night?"
            ki "Maybe you should install a camera?"

            scene kirinhall1
            with dissolve

            ki "Oh! You should have me sleep over and we can see if she hangs out outside of the door and touches herself to the sounds of us sixty-nining. "
            s "But how would we even see if-"
            ki "Doesn’t matter. Can I sleep over tonight?"
            s "I..."
            ki "...?"
            s "Maybe some other time. I'd like both of us to live to see tomorrow."
        else:
            s "Of course I want hug Ami. I want to hug everyone. And Ami is so soft and cute."
            s "It's like hugging a large strawberry."
            ki "What kind of fruit do I remind you of, Sensei?"
            s "Maybe a...............................cantaloupe."

    scene black
    with dissolve

    "Kirin sighs and presses her back up against her door."
    "We talk for a short while after that, but the conversation loses steam and we ultimately wind up a little bored further down the line."
    "I think about inviting her out to walk around town or something, but it’s already getting really late and it would make more sense at this point to just go home."
    "In the end, we exchange goodbyes and head our separate ways."
    "I can hear another sigh from Kirin bleed into the sounds of rock music contaminating the hall once she opens the door."
    "Here’s hoping she can get some sleep tonight."

    $ renpy.end_replay()
    $ kirinfirsthall = True
    $ kirin_love += 1
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikofirsthall:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label dorm2thursday:
    if chapthreeactive == True:
        scene summerdorm2thurs
        with dissolve
    elif day304 == True and chapthreeactive == False:
        scene thurswinter2yasu
        with dissolve
    elif day304 == False and day271 == True and chapthreeactive == False:
        scene thurswinter2
        with dissolve
    else:
        scene dorm2
        with dissolve

    if day304 == True:
        "It looks like Kirin and Yasu aren't doing anything today."
        "I can probably talk to one of them if I want to."
        "What should I do?"
        jump thursday2menu
    elif day304 == False and day271 == True:
        "It looks like Kirin isn't doing anything today."
        "I can probably spend some time with her if I want to."
        "What should I do?"
        jump thursday2menu
    else:
        "What should I do?"
        jump thursday2menu

    menu thursday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Kirin" if day271 == True:
            if kirinfirsthall == False:
                jump kirinfirsthall
...
```