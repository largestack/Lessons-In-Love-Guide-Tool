# Everybody Loves Otoha
Otoha event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohafirsthall&go=Go)



## Event preconditions
✅Event "[Main: Adult Supervision](./day288.md)" is completed (event=day288)



## Next events
* [Nodoka: The Man Who Would Be King](./nodokadorm1.md)

## Event properties
* ID: otohafirsthall
* Group: Otoha
* Triggered by label: otohahall
* Triggered by branch label: dorm2monday

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label otohafirsthall:
    scene otohahall1
    with dissolve

    o "Oh, hey. What’s up?"
    o "You looking for somebody?"
    s "Yes. Her name is Otoha Okakura. Have you seen her anywhere?"

    scene otohahall2

    o "Cool name. Sounds like she’d be a really good singer."
    o "Want to look for her together?"
    s "No need. I’m pretty sure I just found her."
    o "What? Where?"
    s "Right in front of me..."

    scene otohahall3
    with dissolve

    o "Aww, shucks. You know what? Now that you mention it, that {i}is{/i} me."

    scene otohahall4
    with dissolve

    o "What do you need with {i}me{/i}, though? I didn’t like...break any rules or anything, did I?"
    s "Rules? I’m not even sure if these dorms have rules."
    s "And if they do, I’m definitely not the person you should be asking about them."
    s "I just came over to see how you were doing."

    scene otohahall2
    with dissolve

    o "I’m great. But like, what do you mean there aren’t any rules?"
    o "We’re [teenage]girls living in a dorm room without a permanent supervisor. Surely there have to be like...{i}some{/i} rules?"
    s "Just make up your own rules if you want them so much."
    o "I don’t {i}want{/i} them but like...it’s just weird that there {i}aren’t{/i} any."
    o "Like, what if I wanted to play my keyboard really loud at 2:00 AM. Wouldn’t I get in trouble?"
    s "Probably not. But I can’t imagine Nodoka or any of the other girls would like you very much after that."

    scene otohahall5
    with dissolve

    o "I’m pretty sure Nodoka doesn’t sleep, so she’d be fine with it."
    o "And it’s not like I’d do something like that anyway. I need peace and quiet after a certain point of the night or I just...can’t get anything done."

    scene otohahall6
    with dissolve

    o "This definitely isn’t me saying I want to go back or anything, but one of the things I liked about staying with my parents was that it was always quiet as soon as dinner was over."
    o "So I’d get to just...sit around and write whatever came to my mind."
    o "Here, it’s like...the complete opposite."
    o "I'm also literally {i}right{/i} next to Molly’s room and I’m pretty sure her volume knob is busted."
    s "I’m pretty sure most of her is busted."
    mo "I can hear you two, you know?!"

    scene otohahall7
    with dissolve

    o "Hey, Molly! If it makes you feel better, I think your Japanese is really good!"
    o "And you like, barely even have an accent, so...good job!"
    mo "I will...forgive these transgressions for now!"
    mo "But please wait until I am out of range if you’re going to use vicious mockery on me!"
    o "I don’t know what that is, but okay!"
    s "At least you seem to be getting along well."

    scene otohahall8
    with dissolve

    o "I’m like, weirdly good at making friends."
    o "I’ve gotten along with basically everybody here so far."
    s "Are you sure that's not just everyone having a crush on you by now?"

    scene otohahall9
    with dissolve

    o "Oh God, I hope not. I have no idea how I’d go about rejecting so many people at once."
    o "Should I like, send out a newsletter or something?"
    s "Yes. That is absolutely something you should do. I’ll give you my email address so you can copy me on it as well."

    scene otohahall10
    with dissolve

    o "Don’t tell me {i}you{/i} have a crush on me, too..."

    if bonus == True:
        s "Do you think it would be more likely or less likely that your parents would approve of you dating a man my age rather than someone {i}your{/i} age?"
        o "Is that even a question? They’d definitely prefer someone my age if they were forced to choose."
    else:
        s "Absolutely not. I have never once even thought of you that way."

    o "Rin would kill me if I ever dated you anyway. So, yeah. Sorry but..."
    o "Actually, just wait for the newsletter. That will explain everything."
    s "I’m pretty sure Rin would be a little more upset about you not dating {i}her{/i} than dating me, so she definitely won’t kill you."

    scene otohahall11
    with dissolve

    o "I don’t know about that, Sensei."
    o "I know I’ve only seen you two together a handful of times but...she’s different with you than she is with anybody else. Myself included."
    s "You know what? It probably wouldn’t be smart to carry on this conversation with Molly standing right behind us, so..."

    scene otohahall12
    with dissolve

    o "She started playing something on her phone, so I’m sure she’s not paying much attention. "
    o "But yeah, I agree. I feel weird talking about people when they’re not around anyway."
    s "Any suggestions for a new topic then?"
    o "Hmm...how about you tell me why you're suddenly so interested in {i}how I’m doing?{/i}"
    o "You’re not worried about me feeling homesick or something, are you?"
    s "No, but...are you?"

    scene otohahall13
    with dissolve

    o "I’m not."
    o "I...think I like it here."
    o "I had no idea that living with people similar to me could be so...exhilarating. "
    o "And even if it gets loud and I have a hard time focusing on my work...it’s fun. "
    o "Like there’s always some sort of...mystery behind every door."
    s "There is a mystery behind every door. Sometimes even more than one."
    s "Just make sure you knock on them before entering if you want to avoid ever walking in on something weird."

    scene otohahall12
    with dissolve

    if bonus == True:
        o "I’m...just going to hope that you’re talking about them getting changed or something and not anything involving you."
        s "You think whatever you want to think. I’m just giving you the proper warning."
        o "..."
        o "Okay, don’t take this the wrong way, but like..."
        o "How did you get hired as a teacher?"
        s "That’s a very good question, Otoha."
        o "…"
        s "…"
        o "Is there...an answer to it?"
        s "There’s no answer to why there aren’t any rules in the dorms, is there?"
        s "Acknowledge my role here the same way and I’m sure things will start making a lot more sense to you."
    else:
        o "Like what?"
        s "Every third Saturday of the month, if you wait until approximately 3:00 AM and very quietly walk into any of the dorms on the first floor, you will find that room's inhabitants sacrificing a lamb."

    o "This[school] is...weird."
    s "Very much so. But you must be weird too since you’re a part of it now."

    scene otohahall3
    with dissolve

    o "Pfft. Maybe so. No one’s perfect after all."
    o "I just hope you don’t lose sight of me amidst all the huge personalities on this floor."
    s "Wait a minute...You {i}want{/i} me to be worried about you, don’t you?"

    scene otohahall8
    with dissolve

    o "Hey, there are no rules up here. I need {i}someone{/i} to worry in case anyone tries to kidnap me in the middle of the night or something."
    s "I’m glad we never went with Plan B because that would have already happened by now."

    scene otohahall2
    with dissolve

    o "Wait, what?"

    scene black
    with dissolve

    s "Later, Otoha. It was nice talking to you."
    o "Hold on! What was Plan B?!"
    o "And...what was Plan A?!"
    o "What were you going to do to me?!"
    s "Enjoy the rest of your night. Hopefully no one comes to kidnap you."
    o "Sensei! This is making me feel really weird!"

    $ renpy.end_replay()
    $ otohafirsthall = True
    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadorm1:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label otohahall:
    if otohafirsthall == False:
        jump otohafirsthall
...
```