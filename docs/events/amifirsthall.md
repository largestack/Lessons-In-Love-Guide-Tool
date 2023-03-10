# Uninvited (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: amifirsthall
* Group: Ami
* Triggered by label: dormfriday
* Triggered by branch label: dorms
* Triggered by path: dorms->dormfriday->amifirsthall

## Official wiki page

[Uninvited](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amifirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amifirsthall:
    scene amihall1
    with fade

    a "Ugh! How come I always end up on stupid bathroom duty?! Wasn't that my job last week too?!"
    s "Hey Ami. Am I interrupting something?"

    scene amihall2
    with dissolve

    a "Huh? Sensei?"
    a "When did you get here?"
    s "Just now. But if you have chores to do, I can just hang out with someone else instead."

    scene amihall3
    with dissolve

    a "I would sooner abandon all of my chores for the rest of eternity than let you spend your time with anyone else."
    s "Okay. That's not super controlling or anything."
    a "Of course it's not controlling, we're related. If you asked {i}me{/i} to never talk to anyone else, I'd do it in a heartbeat."
    s "That's...not really something to smile about, Ami. That's actually really depressing."

    scene amihall4
    with dissolve

    a "What's depressing is how you walked all the way through this hallway without shouting my name due to your uncontainable excitement to see me."
    s "I see you literally every morning."

    scene amihall4r
    with dissolve

    a "And yet you still need more."
    a "So, what are you {i}really{/i} doing here? Did I forget something at home?"
    s "I wouldn't know if you did. I came here straight from school."

    scene amihall4
    with dissolve

    a "You did? That's weird."
    s "Why is that weird?"
    a "Because even if you had to stay late for counseling stuff, it's pretty late to be showing up here. School ended hours ago."
    a "You haven't been sneaking around and doing anything you can't tell me about, have you?"
    s "It's not like I would tell you if I was. What I do with my free time is kind of up to me, isn't it?"

    scene amihall3
    with dissolve

    a "Nope!"

    "Is there somewhere I can go to trade in my niece for a different one?"

    scene amihall4r
    with dissolve

    a "I guess I can let you off the hook for tonight, though, since I already have plans."
    a "And no, I'm not talking about chores. The bathroom is stupid and it can die for all I care."
    s "What do these {i}plans{/i} of yours entail? And can I tag along?"

    scene amihall5
    with dissolve

    a "Me and Maya were going to go eat pizza and do karaoke or something like that."
    a "I'd invite you along, but...she kind of already made a no-Sensei rule, so...I'm not sure if I can make that happen."
    s "That's fair. If I were a teenage girl, I probably wouldn't invite me either."

    scene amihall6
    with dissolve

    a "Maybe you can come next time?"
    a "I'm not really sure what the problem is since me and Ayane are normally the only ones who sing anyway. Maya just hangs out on the bench and eats the whole time."
    s "You need to stop saying {i}me and blank.{/i} It's getting on my nerves."
    a "Please save your grammar lessons for when we're in school, Sensei."
    s "I can't. I use that time to sleep."

    scene amihall3
    with dissolve

    a "Then I guess I'll just have to talk this way forever!"
    s "That aside, how are you liking the dorms so far? This place seems like it has basically everything you could ever need."

    scene amihall7
    with dissolve

    a "{i}Almost{/i} everything."
    a "But I really like it here. It makes me feel like I'm in college."
    a "I obviously don't hang out here as much as the girls without other housing options, but all of the time I {i}do{/i} spend here is super fun!"
    s "Wait, there are girls without other housing options? What do you mean by that?"
    s "You're not implying that some of the girls in our class are homeless, are you?"

    scene amihall5
    with dissolve

    a "{i}Homeless{/i} probably isn't the right word...but there are definitely a few girls who wouldn't technically have anywhere else to go if the dorms just...blew up or something."
    a "Take Maya for example. She doesn’t have any family in Kumon-mi, so she’d probably be forced to come stay with us if something like that were to happen."
    s "What is she doing living here if her family isn’t anywhere nearby?"

    scene amihall4r
    with dissolve

    a "No clue. She just sorta showed up one day and we’ve been best friends ever since."
    a "I don't think we have to worry about a dorm explosion, though. I'm pretty sure nothing like that has ever happened before."
    a "Well...at least not here. But hey, I don't know everything."
    s "Huh..."
    s "Well, alright then."

    scene amihall8
    with dissolve
    play sound "dooropen.mp3"

    m "Okay. I’m ready to go."
    s "Hey, Maya. Nice to see you."

    scene amihall9
    with dissolve

    m "Yes, hello."

    scene amihall8
    with dissolve

    m "He isn’t coming, is he?"

    scene amihall10
    with dissolve

    a "He’s not...I already told him about your no-Sensei rule."
    s "I can't say I don't understand it."

    scene amihall11
    with dissolve

    m "Please stop talking to me."
    a "Well...I guess this means our time is up, huh?"
    s "Seems that way, Ami. Don't let Maya poison your mind about how horrible I am while I'm not around to stop her."
    m "I can assure you that it does not take poison for someone to understand just how deplorable you are."
    s "Have fun at karaoke, you two. I'll be looking forward to any videos I'm sent with Maya singing."
    m "And I am looking forward to the sound your phone will make when I snatch it out of your hands and toss it off of a bridge."
    a "Don't worry, Sensei. I won't let her do that."
    a "I'll talk to you later, okay?"
    s "Sounds good. Goodnight, Ami."
    a "Goodnight, Sensei."
    s "Goodnight, M-"
    m "No."

    scene amihall0
    with dissolve

    "Ami and Maya disappear down the hall and I'm suddenly left with nothing to do but head home."

    scene black
    with dissolve2

    "When I get outside, I realize that a great deal of time {i}has{/i} passed since school ended...which is strange, since I don't remember leaving much later than normal."
    "I guess it's easy to lose track of time when your mind is elsewhere, though."
    "Regardless, I accept the night and begin yet another walk across town in the sweltering heat."
    "Here's hoping that Ami's night winds up being a little more exciting than mine."

    $ renpy.end_replay()
    $ amifirsthall = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amihall:
    if chapthreeactive == True:
        scene amisummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene amihall3
        with dissolve
    else:
        scene amihallwinter1
        with dissolve

    a "Sensei! Did you miss me?"
    s "Of course. I keep having to make my own dinner on the weekends and it’s ruining my life."
    a "Then I guess I’ll have to cook you something extra special next time I’m home! Okay?"

    "Ami and I spend some time hanging out in the hallway while she waits for Maya to get back."
    "I’m glad that the two of them are so close, but it {i}is{/i} kind of lonely without her at times."
    "Either way, it’s good that she seems to be enjoying her [high_school] life."
    "Hopefully, the two of us can find some more time to spend together soon."

    scene black
    with dissolve

    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanafirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormfriday:

    if chapthreeactive == True:
        scene summerdorm1fri
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene friwinter
        with dissolve
    else:
        scene dorm_friday
        with dissolve

    play music "sweetvermouth.mp3" fadein 2.0

    "I decide to pay a visit to the dorms."
    "This might be a good time to hang out with one of the girls."
    "It looks like Sana and Ami aren’t doing anything."
    "I could probably spend time with one of them if I want to."
    "What should I do?"

    menu fridaymenu:
        "Knock on a door":
            jump doorknock
        "Talk to Sana":
            if sanafirsthall == False and firsttimebar == True:
                jump sanafirsthall
            else:
                jump sanahall
        "Talk to Ami":
            if amifirsthall == False:
                jump amifirsthall
...
```