# The Hole That Swallowed Everything
Yasu event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yasufirsthall&go=Go)



## Event preconditions
✅Event "[Main: Horses or the Whispers of the Dead](./day304.md)" is completed (event=day304)



## Next events
* [Yasu: Repentance](./yasudorm10.md)

## Event properties
* ID: yasufirsthall
* Group: Yasu
* Triggered by label: yasuhall
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label yasufirsthall:
    if _in_replay:
        play music "sweetvermouth.mp3"

    scene yasuhall1
    with dissolve

    s "Hey, Yasu. Having fun spending your free time just...standing in the middle of the hall?"
    ya "I’m not sure if I would call it fun, but Touka will not let me into the room right now. "
    ya "If you have any suggestions for a better way to spend my time, I would be happy to hear them."
    s "Well, I wouldn’t mind talking to you for a little bit. I’m sure it will keep the both of us at least mildly...entertained?"
    ya "I entertain you?"
    s "I think you go a little beyond that, but saying “entertain” is probably the easiest way to describe it."
    ya "Do I remind you of the snow on the ground? The wind in the trees?"
    s "No. You remind me of a girl who likely needs professional help but will not receive any."
    ya "What a strangely specific type of girl."
    ya "Is that what you would call your “type?”"
    s "Are you hitting on me right now?"
    ya "Romance is out of the question until my wings grow in, Sensei. For now, I am just trying to evaluate you."
    ya "It will come in handy soon."
    s "Why?..."

    scene yasuhall2
    with dissolve

    ya "Because soon, you’ll finally be ready to see where I’ve been hiding all this time."
    ya "Where I found solace when the world would not have me. "
    s "..."
    s "Is that just a really convoluted way of saying that you prefer cold weather over the heat?"

    scene yasuhall3
    with dissolve

    ya "I both love and hate the summer at the same time."
    ya "It’s quite complicated. I can’t really talk about it here."
    s "Why? You’re not going to tell me a top secret organization is conducting a surveillance mission on you or something, right?"
    ya "That’s something a crazy person would say."
    s "So you {i}are{/i} going to tell me that..."

    scene yasuhall4
    with dissolve

    ya "If we talk too loudly about things we’re not allowed to talk about yet, the floor will open up and swallow us."
    s "Yeah, that’s not a thing that happens."

    scene yasuhall1
    with dissolve

    ya "Are you sure?"
    s "...Yes?"
    ya "But I saw it with my own eyes, Sensei. The reckoning."
    ya "The hole that swallowed everything."
    s "The...hole that-"
    s "Wait, you’re not talking about Kumon-mi Academy, are you?"

    scene yasuhall5
    with dissolve

    ya "{i}Slip.{/i}"
    s "...Is that a yes or a no?"
    ya "It’s an answer. "
    ya "One I can share with you the moment you open your eyes."
    ya "When will you be ready to open your eyes?"
    s "I really wish you’d stop asking me that while I’m looking directly at you."
    ya "When will you be ready to be saved, Sensei?"
    ya "When will you be ready to be cleansed?"
    s "Cleansed of what, exactly?"

    scene yasuhall6
    with dissolve

    ya "All of the filth this world has to offer."
    ya "Let us wash it all away together."

    if bonus == True:
        s "You know, I’m normally the type to jump at an opportunity to shower with a cute girl, but I have a feeling I might not ever make it back if I accept this offer right now."
        ya "Make it back to where? It’s not as if this place is of any value to either of us."
    else:
        s "I will buy you a hose for Christmas."

    ya "It’s so much harder to feel the ground tremble from up on the second floor."

    if bonus == False:
        s "Okay Yasu."

    ya "Even if you lay down and press your cheek against the carpet of this very hall, you’d be lucky to feel anything at all."
    s "Please don’t put your face on the carpet here. I don’t think it’s vacuumed very often."

    scene yasuhall7
    with dissolve

    ya "Will agreeing to your demands bring you closer to the desire for salvation?"
    s "No, but it will keep you from getting dirty."
    ya "That which is white can never be dirty."
    s "That is very much not true, Yasu."
    s "In fact, I’d say it’s the complete opposite. "
    s "That’s a nice dress and you wouldn’t want it to get ruined."

    scene yasuhall8
    with dissolve

    ya "Nice?..."
    ya "Sensei..."
    ya "This dress is hideous. "
    ya "I want to tear it off right now."

    if bonus == True:
        s "You know, I tried giving you a compliment and being a nice guy, but then you went and said that. And now I’m stuck questioning my morals like I always am."
    else:
        s "Please don't. I don't want to see that."

    scene yasuhall9
    with dissolve

    ya "The funny thing about morals is that they are focused on what is right and what is wrong."

    if bonus == True:
        s "Yes. That is absolutely hilarious."
    else:
        s "Oh, okay. I guess we're talking about morals now."

    ya "But when we are nothing more than subjects for who we believe created us, aren’t morals rather silly?"
    ya "If I think something is right and you think something is wrong, but we are both virtuous in our beliefs, which one of us is truly right?"
    s "That’s a good point. If everything is subjective then-"

    play sound "static.mp3"
    scene yasuhall10
    with flash
    stop sound

    ya "BZZZT! Wrong answer!"

    play sound "static.mp3"
    scene yasuhall5
    with flash
    stop sound

    ya "My answer is the truly right one! Yours will only make the pain worse!"
    ya "The solution is to follow my lead! To see the things I see as right as virtuous in your own, {s}tainted{/s} purified eyes."
    ya "Does your vision ever get cloudy, Sensei?"
    ya "Tell me all of the horrible things you see, and I will swallow them whole."

    scene yasuhall11
    with dissolve

    if bonus == True:
        ya "I will swallow anything and everything that you ask of me."
    else:
        ya "(Airplane noises)"

    s "…"
    ya "…"

    scene yasuhall12
    with dissolve

    ki "Same."
    s "Thanks, Kirin. I had a feeling you were going to chime in there."

    if bonus == True:
        ki "That girl is fucking weird, Sensei. Come hang out with me and Noriko instead."
        s "Maybe some other time..."
    else:
        ki "I love airplanes."

    ya "Are you ready?"

    if bonus == True:
        s "For...the swallowing?"
    else:
        s "For what?"

    ya "For the {i}sanctuary.{/i}"
    ya "For the place that can not be swallowed by the hole that swallows everything. "
    ya "A place where we can cleanse ourselves together...and hide when the heat becomes too much for our pitiful bodies to bear."
    ya "A place where God does not live, but very much likes to visit when the time is right."
    ya "I want to show you that place, Sensei."
    s "It sounds a lot like you’re inviting me to a church right now."
    ya "..."
    s "..."

    scene yasuhall13
    with dissolve

    ya "..."
    s "..."
    s "You actually {i}are{/i} inviting me to a church aren’t you?"

    scene yasuhall14
    with dissolve

    ya "I’d be very happy if you came."
    ya "I just want to help you."
    s "I don’t think so, Yasu. I’m not really a religious person."

    scene yasuhall8
    with dissolve

    ya "Then why do you reek of a {i}shrine?{/i}"
    s "First off, rude."
    s "Second, shrines don’t have a scent."

    scene yasuhall7
    with dissolve

    ya "But gods do. And I am very very very very very very very very very very {i}very{/i} good when it comes to sniffing out things like that, Sensei."
    s "I wouldn’t mind showing up to hang out with you I guess, but..."
    s "Wait, hold on. This is a bad idea. I shouldn’t be going to see you in a place like a church where there are other people around."

    scene yasuhall3
    with dissolve

    ya "There is only me. "
    ya "It’s a special place that only the chosen can enter."
    s "Then how the hell will I get in? I haven’t been chosen at all."
    ya "I’m choosing you right now."
    ya "Come, wash away your sins with me."
    ya "I will not ask you to pray and will not stop you if you want to leave."
    ya "All I ask is that you come."
    s "…"
    ya "…"
    s "Ugh, fine. Whatever. But I’m literally only doing this because you’re cute."

    scene yasuhall6
    with dissolve

    ya "Hehehehehehehahahahahahehhahahaha!!!"
    ya "No romance, Sensei! Not without God’s approval!"

    "What the fuck did I just get myself into?"

    scene black
    with dissolve

    "Yasu takes one of her gloves off and removes an old newspaper clipping that she had been carrying around in there for some reason."
    "She places it into my hands and then clasps them together, bringing herself to her toes to try and whisper into my ear."
    "I crouch down a bit to help her."

    ya "{i}Praise be.{/i}"
    s "…"
    s "That’s it? That’s all you wanted to whisper?"
    ya "Goodnight, Sensei. The time has come again for me to pray."
    ya "The answer to all of your troubles can be found on that sheet of paper."

    "Yasu disappears back into her room and I..."
    "Well, I...go home."

    $ renpy.end_replay()
    $ yasufirsthall = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "{i}Congratulations! You may now visit New Hope Cathedral!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukadorm5:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label yasuhall:
    if yasufirsthall == False:
        jump yasufirsthall
...
```