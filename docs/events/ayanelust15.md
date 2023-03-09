# What a Wonderful World
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanelust15&go=Go)


Part of event chain [Chaperone](./dormwar8.md)

## Event preconditions
✅Event "[Ayane: Prisoner](./ayanelust10.md)" is completed (event=ayanelust10)

✅Ayane lust greater than or equal to 15

✅Kirin lust greater than or equal to 15



## Next events
* [Ayane: Furlough](./ayanekirintalk.md)
* [Kirin: Made Out of Nothing](./kirinspecial30.md)

## Event properties
* ID: ayanelust15
* Group: Ayane
* Triggered by label: dormwar8

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label ayanelust15:
    play sound "knock.mp3"

    ay "Um...Sensei?"
    ay "You’re in there, right?"

    "Ayane shows up at my door because...well, she’s Ayane. And it’s my door."
    "Of course she’d be here."

    s "I am, but are you sure it’s a good idea to come visit me while there are people looking for you?"
    ay "…"
    s "Ayane?"
    ay "Can you just let me in?"

    scene black
    with dissolve

    "I turn around and head to the door to save both of us some time since she’s not really someone I can just turn away."
    "Besides, if she doesn’t want anyone to find her, it would be a lot safer in here than if she was aimlessly wandering around the halls."

    play sound "lock.mp3"

    "I unlock the door and pull it open."
    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene ayanekirinfuntime1
    with dissolve
    play music "asobeatsex8.mp3"

    ki "Surprise!"

    if bonus == True:
        jump ayanelust15x
    else:
        "Kirin and Ayane show up to play a game of Monopoly despite Ayane really not wanting to."
        "We wind up making our own rules and I am forced to choose which one of them is the winner."

        menu:
            "Ayane wins":
                s "Ayane is the Monopoly champion."
                ay "Yay!"

                $ ayanebjcontest = True
                $ dorm1warpoints += 1
            "Kirin wins":
                s "I think Kirin is better at Monopoly."
                ay "Aww. Darn it."

                $ kirinbjcontest = True
                $ dorm2warpoints += 1

        $ ayane_lust += 3
        $ kirin_lust += 3
        $ renpy.end_replay()
        $ ayanelust15 = True
        scene black with dissolve2
        stop music fadeout 7.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "………"
        "……"
        "…"

        jump dormwar9

label dojo35:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
if bonus == True:
        "I take a seat at the foot of the bed to conceal Tsuneyo’s (And probably Uta’s?) eyes from being seared by the sight of a growing erection."
        "I’m not worried about Noriko, obviously, since she has already felt it on multiple occasions now."
    else:
        "My legs are so weak. I should try running on the treadmill soon."

    scene warhotelarrival26
    with dissolve

    u "Hey, you haven’t seen Io by any chance, have you?"
    u "We walked back from the rap battle together, but she disappeared the second she realized there were people already waiting in our room."
    s "She’s missing as well? That makes three total since Ayane and Ami are MIA too."
    n "Kirin too, I guess. But she’s probably just out for a walk or something. She does that a lot."
    n "I’m sure they’ll all find their way back soon enough."
    s "Maybe Io just went back to the dorm or something? That seems like an Io thing to do."

    scene warhotelarrival27
    with dissolve

    u "Not without telling me, but...I guess I’ve kinda been on her case all day."
    u "She’s kinda like a pet snake that doesn’t like being handled or something."
    u "Give her too much attention and it’ll just make her mad. Then, next thing you know, you’ve gotta have someone suck the venom out of your wound and it becomes a whole thing."

    scene warhotelarrival28
    with dissolve

    t "Snake venom..."
    t "I still need to try that...and now I know where to get some."
    s "Tsuneyo, didn’t we decide that snake venom ramen was a bad idea?"
    t "Fuck you in the rude way and not the literal way that I have now discovered the meaning of."
    u "Io doesn’t have real venom, Tsunecchi. She’s a human girl, just like you and me."
    t "What does it mean to be human, Green Onion?"
    t "{i}What does it mean to be?...{/i}"
    s "…"
    s "Okay, well I’m probably going to head over to my room now."
    s "Today was exhausting enough and if I am going to continue to be a completely unbiased and awesome judge, I need to get some rest."

    scene warhotelarrival29
    with dissolve

    u "Good call, Sensei! Just keep doin’ what you’re doin’ since my girls are in the lead!"
    u "And hey, even if you do wanna be a {i}little{/i} biased, that’s okay. Just make sure it’s second floor bias and not first floor bias. You know?"
    n "Goodnight, Sensei."

    if bonus == True:
        n "I’d offer to come hang out in your room with you, but I should probably give you some space on account of that whole drug thing, shouldn’t I?"
        s "Probably. I still have to figure out how I feel about that."
        n "Wanna just drug me next and make it an eye for an eye?"
        s "I would much prefer you to be conscious during our time together."
        n "Are you suuuuuuure?"
        s "…"
        s "{i}Yes?{/i}"
        t "Perhaps if the venom was cut with something citric like...lemon?"

    scene black
    with dissolve2
    stop music fadeout 30.0

    "I exit the room of the second floor girls and follow the signs in the hall directing me toward my room."
    "I’m not sure why mine has to be on the opposite end of the hotel, but I guess things will be a lot quieter that way."
    "The girls were loud enough in both of their rooms that it was easy to hear what was going on in the other one through the walls."
    "But I guess it was like that at the inn I went to with Chika as well and that was also owned by the Tsukiokas."
    "Maybe cutting corners on thinner walls is just something they do to save money or something?"
    "Who knows? I’m no rich person or financial genius."

    scene warhotelarrival30
    with dissolve
    play sound "dooropen.mp3"

    "But I {i}will{/i} graciously accept and benefit from their kindness or naivete."
    "I’d never be able to afford three separate hotel rooms on my teacher’s salary."
    "And it’s not like I can really ask for a raise either since I’m...you know."
    "Really bad at my job."
    "But I guess there would be no reason for me to ever go out of my way and get something like this in the first place."
    "This is fun."
    "It is."
    "But it’s not something a normal class would do."
    "And it’s probably not something I should be letting them do."
    "But who cares?"
    "Their lives belong to them and them only."
    "And in letting them realize that, they’ve centered themselves around me."
    "Each one of them is a celestial body orbiting around my existence."
    "I am the center of the solar system."
    "I will take."
    "And I will take."
    "And I will take."
    "And I will grow."
    "If life is nothing but a strange string of coincidences and being in places at the right time, I will be everywhere at once so that nothing is coincidental at all."
    "Time is unlimited."
    "Until it’s not."
    "But, right now-"
    "It is."

    if ayanelust10 == True and ayane_lust >= 15 and kirin_lust >= 15:
        "Which makes moments like this okay."

        $ renpy.end_replay()
        $ dormwar8 = True
        jump ayanelust15
...
```