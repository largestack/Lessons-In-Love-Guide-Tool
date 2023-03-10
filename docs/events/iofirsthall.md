# Viva la Revolución (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Caterpillar](./day247.md) (Main) is completed)



## Next events

* [Io: Paperthin](./iodorm10.md)

## Event properties

* Id: iofirsthall
* Group: Io
* Triggered by label: iohall
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->iohall->iofirsthall

## Official wiki page

[Viva la Revolución](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iofirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iofirsthall:
    scene iohall1
    with dissolve

    i "Oh, Sensei. What’s up?"
    i "Not doing anything tonight?"
    s "Nope. Just thought I’d say hi since you’re sitting here on the floor for some reason."
    i "Just getting some fresh air. It’s kind of stuffy in the room at the moment."
    s "I don’t know if I’d call the air in the dorm “fresh” but you do you."
    i "Well, what else am I supposed to do? Go outside? It’s freezing out there."
    i "Let me borrow your jacket and I’ll go outside. You can hang out here and watch movies in my bed or something."
    i "We’ll just swap places for a little bit. Does that work for you?"
    s "I like my jacket and don’t particularly like movies, so no."

    scene iohall2
    with dissolve

    i "What kind of psychopath doesn’t like movies? What could possibly be the reasoning behind that?"
    s "I don’t know. Staying in one place for too long is just boring."
    i "Tell that to the weird bird on top of our vending machine. It hasn't moved since I got here."
    i "I could have sworn it was actually dead but I tried poking it the other day and I’m pretty sure it threatened to kill me."
    s "It didn’t...pull a knife out on you, did it?"

    scene iohall3
    with dissolve

    i "Uhh...no. It’s still just a bird after all. It wouldn’t be able to do something like that."
    s "Oh, Io...You sweet, summer child."
    i "What?...What did I do?"
    s "You will learn the true nature of that animal in time. For now, it may be best if you remain oblivious."

    scene iohall4
    with dissolve

    i "Oh...Uhh, okay."
    i "I still don’t really get it, but you got this really serious look as soon as I brought the bird up, so I’ll listen to you."
    s "Good."
    s "So anyway, how are things going over here? Hate being around the other girls as much as you expected to?"

    scene iohall5
    with dissolve

    i "If you mean the dorms in general and not[school], not really."
    i "I don’t have to talk to anybody over here. "
    i "Even when I’m just sitting in the hall, no one other than Uta really makes an effort to talk to me. So that’s cool."
    s "No, that’s just depressing. I figured they’d at least try."
    i "Ehh. Who knows? Maybe they have and I just haven’t noticed?"
    i "Either way, not really something I want to spend too much time thinking about."
    i "The dorm itself is really cool."
    i "Even though Uta takes up like 75%% of the room, it’s still cool having a place I can sort of turn into my own little thing."
    s "Don’t you have a room at the bathhouse?"
    i "I do, but it’s really just my aunt’s guest room that I wound up moving into and I feel kinda bad about sprucing it up. You know?"
    i "The dorm has a surprisingly small list of rules we need to adhere to, so once I found out I could do whatever I wanted, it made me a lot more comfortable."
    i "Only downside is that the showers here don’t get nearly hot enough so I still have to use the ones at work."

    if bonus == True:
        s "I have yet to use the showers here so I can not contribute to this conversation."
        i "Just get the blonde girl to bring you in there when she takes a shower one day."
        i "You guys already bathe together so I’m sure she won’t mind."
        s "I feel like there is a high likelihood of that actually happening one day, so I’ll let you know when it does."

        scene iohall6
        with dissolve

        i "Uhh...you don’t need to let me know whenever you get naked with some girl. I don’t have to keep tabs on that like Uta does."
        s "Finally, someone who understands."
    else:
        s "Your life is so hard."

    scene iohall7
    with dissolve

    if bonus == True:
        i "Hey, Sensei, do you know why this[school] has dorms in the first place?"
        i "It’s a public [high_school] so like, isn’t having dorms kind of...weird for somewhere like that?"
        i "Not to mention that your class has like, an entire building to itself."
    else:
        i "Also, why does our class get its own building?"

    i "Where even is the other dorm?"
    s "You’re asking me a bunch of questions I do not have the answer to right now."
    i "You didn’t learn all this stuff when you became a teacher?"
    i "Maybe it’s some sort of conspiracy or something?"

    scene iohall8
    with dissolve

    i "Oh man! Great idea!"
    i "Sensei, let’s start a revolution!"
    s "...What?"
    s "What are we revolting against?"

    if bonus == True:
        i "Kumon-mi High. We can secede and declare this dorm a republic. Then we won’t have to go to school {i}at all{/i} and can just hang out here every day."
        s "Yes, I’m sure everyone will love the idea of never going to college and spending the rest of their lives here."

        "Not like anyone is ever going to make it to college anyway."
        "They’re all caught in an infinite first year of [high_school]."
    else:
        i "[kumon_mi_high]. We can secede and declare this dorm a republic. Then we won’t have to go to[school] at all and can just hang out here every day."

    "You know, maybe this does call for a revolution after all?"
    "The dorm functioning as an independent entity sounds quite enticing."

    i "Who even needs college? "
    i "What’s the point of going into debt just so you can try out for a slightly better job in order to pay off all of it?"

    if bonus == True:
        s "That train of thought is too advanced for a girl your age. You need to slow down."

    scene iohall9
    with dissolve

    i "More people should just learn tradeskills."
    i "Sure, a lot of them are less {i}glamorous{/i}, but they’re literally {i}always{/i} needed and there are tons of programs much cheaper than colleges."

    if bonus == True:
        s "Is that what you’re planning on doing?"
        i "Idunno. I should focus on getting out of [high_school] first."
        s "Good call. Leave all that future-planning stuff to year three- a year you will definitely make it to."
        i "Saying it like that makes it sound like I’m going to drop out."
    else:
        s "Why are you in college then?"
        i "Because I'm a hypocrite. Duh."
        s "Oh, right."

    scene iohall7
    with dissolve

    i "I get that I haven’t shown a lot of interest in class yet, but I have no intention of leaving. Especially with you as my teacher."
    s "I had a feeling my methods would reach you."

    scene iohall9
    with dissolve

    i "Well your feeling was spot-on."
    i "It’s cool waking up and not dreading whatever is going to happen for the rest of the day immediately."
    i "It just sucks that I only have several months of that until it all goes away and I have to find my place in yet {i}another{/i} group of students."
    s "Just get held back and stay in my class."

    "Or do nothing at all and achieve the exact same result."

    scene iohall10
    with dissolve

    i "Heheh~ Gonna miss me when I’m gone?"
    i "Maybe I {i}will{/i} get held back and then run for class-rep next year so I can spend even more time with you."
    s "That sounds great as long as you can figure out how to communicate with others as well."
    i "For the last time, I’m actually pretty good at that. I can do it if I want to."
    s "Right. You just don’t {i}want{/i} to."

    scene iohall11
    with dissolve

    i "Precisely. So stop trying to get me to. Got it?"
    s "Yeah, yeah. I won’t make you do anything you don’t want to. "
    i "Good. Only someone horrible would force someone into doing something they’re not comfortable with."

    scene black
    with dissolve

    "Io and I talk for a little while longer before she decides she wants to go back into her room and head to sleep early."
    "Not having anything else to do and feeling a bit guilty about knocking on someone else’s door at this hour of the night, I decide to head home and go to sleep as well."

    if day == 5 or day == 6:
        "I have the day off tomorrow, so maybe I can squeeze in a little extra time in the morning if I’m able to wake up early enough?"

    else:
        "I have to go to work tomorrow, so crashing early will be advantageous in the long run."

    "I make my way down the steps of the dorm and into the cold once more, ready for the harsh winds of yet another winter night."
    "...Or at least that’s what I think until the wind actually hits my skin."
    "From that point on, it’s absolute Hell the whole way back."
    "I wasn't ready at all."

    $ renpy.end_replay()
    $ iofirsthall = True
    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
    if io_love >= 10 and iodorm5 == True and iofirsthall == True and iodorm10 == False:
        jump iodorm10
    if io_love >= 15 and bathhouse10 == True and day != 5 and iodorm15 == False:
        jump iodorm15
    if io_love >= 25 and bathhouse25 == True and day != 5 and iodorm25 == False:
        jump iodorm25
    elif io_love >= 5 and bathhouse5 == False:
        "I should probably get to know Io a little better before I see if she wants to hang out in her room."
        jump doorknock2
    else:
        jump iodormgen

label iodormgen:
    play sound "knock.mp3"

    s "Io, it's me."
    i "Come in, Sensei! Door is open!"

    scene iodormgen
    with fade

    "I walk into Io's room and, just as always, do not hesitate to comment on the condition of the place."
    "She gives me the same excuse as always, that it's really all Uta's fault, but she is undeniably an accomplice to this."
    "I understand the need for a place to do all of her crafts and whatnot, but isn't there somewhere like a woodshop in the[school] she could use?"
    "That would certainly beat trying to build anything in this extremely cramped space."
    "But, then again, she's proven thus far that she's not really the type to willingly spend any spare time somewhere like that."
    "And it's not like the clutter really affects me in any way since I'm not the one living here."
    "But I {i}would{/i} greatly appreciate it if she'd at least clear an area around the bed so I don't need to tap into my athletic capabilities each time I sit on it."

    scene black
    with dissolve

    "Io eventually convinces me to watch a movie with her and, lo and behold, I need to squeeze through the paperthin opening once more."
    "She sits close enough to me that our shoulders touch but makes no effort to go any further."
    "I'm still struggling to understand why she's so comfortable around {i}me{/i} of all people, but I benefit from this- so I will not question it out loud."
    "I'll just let her have her fun and humor her by pretending to watch whatever she puts on."
    "At the end of the day, I {i}did{/i} come here to see her. So letting her do what she wants is fine by me."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label iohall:
    if iofirsthall == False:
        jump iofirsthall
    else:
        jump iohallgen

label iohallgen:
    if chapthreeactive == True:
        scene iosummer2hallgen
        with dissolve
    else:
        scene iohall10
        with dissolve

    i "Hey, Sensei. What are you up to?"

    "I spend the night in the hallway with Io."
    "It isn't a particularly exciting time, but it's a time nonetheless."

    if bonus == True:
        "We talk more about potential non-college plans for her and I'm, once again, surprised by how much she seems to know about post-[high_school] life."

    scene black
    with dissolve

    "Eventually, it gets late and I decide to head back."
    "Io has some stuff she wants to do tonight anyway, so we mutually part ways and I quickly find myself on the way back home..."

    $ io_love += 1
    stop music fadeout 5.0

    "{i}Io's affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label utadorm5:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iohall:
    if iofirsthall == False:
        jump iofirsthall
...
```