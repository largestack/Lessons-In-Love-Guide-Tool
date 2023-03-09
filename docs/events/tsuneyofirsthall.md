# The Life of a Blue Whale
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyofirsthall&go=Go)



## Event preconditions
✅Event "[Main: Lifting the Curse](./day154.md)" is completed (event=day154)



## Next events
* [Tsuneyo: Drug Use & Jump-Rope](./tsuneyodorm5.md)
* [Kaori: The Best Ways to Rub a Cock](./kaoridate5.md)

## Event properties
* ID: tsuneyofirsthall
* Group: Tsuneyo
* Triggered by label: dorm2wednesday
* Triggered by branch label: dormwednesday

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyofirsthall:
    scene tsuneyohall1
    with dissolve

    s "Hey Tsuneyo. What are you doing?"
    t "…"
    s "…"

    "No response."
    "Is she looking at the board or something?"
    "I glance over Tsuneyo’s shoulder to see if there’s a flyer for...noodles or something, but everything up there seems to be normal."

    s "Hello? Earth to Tsuneyo."
    t "Do you ever just...think about whales?"
    s "…"
    t "…"
    s "Not really, no."

    scene tsuneyohall2
    with dissolve

    t "Did you know that the life expectancy of the blue whale is anywhere from 80-90 years?"
    t "Though, there are some cases in which whales have lived for much longer."
    s "Thank you for this information that I will likely never use again."

    scene tsuneyohall3
    with dissolve

    t "You’re welcome."
    s "So...what are you up to tonight?"
    t "Thinking about whales."
    s "I see that. What {i}else{/i} are you up to?"
    t "…"

    scene tsuneyohall4
    with dissolve

    t "Talking about whales?"
    s "What I’m asking is if you have any plans. "
    s "I don’t have anything to do, so I wanted to see if you’d be down to hang out for a bit."

    scene tsuneyohall3
    with dissolve

    t "In the hallway?"
    s "It doesn’t have to be the hallway. We could go to your room if you’d like."
    t "I think I’d prefer the hallway. "
    t "Being alone in a room with a boy is something I’m supposed to avoid."

    if tsuneyodorm5 == True:
        s "But I’ve been in your room before."
        t "Yes, because it would have been rude for me to deny you entry."
        t "Right now, we are already in the hallway. So I just won’t go back in my room."
        t "We can talk out here."

    else:
        s "Wait, so I’ll never be allowed in?"

        scene tsuneyohall4
        with dissolve

        t "You probably will."
        t "I tend to cave under pressure. "

    s "It's whatever. I'm fine with talking in the hallway, I guess."
    s "I just prefer a topic slightly more interesting than the amount of time whales live."
    t "I can probably manage that."

    scene tsuneyohall5
    with dissolve

    t "Have you met Noodles?"
    s "We literally named him together, Tsuneyo."

    scene tsuneyohall6
    with dissolve

    t "Ah-"

    scene tsuneyohall7
    with dissolve

    s "I’m surprised he’s still up there. How does a bird even get into the dorms?"
    t "Perhaps he is enrolled at the[school]?"
    s "How would a bird even enroll?"
    t "It’s crazy what you can do with a computer nowadays."

    scene tsuneyohall8
    with dissolve

    s "He literally does not have hands. He can’t type."
    s "Wait, he doesn’t know how to read either. This entire topic is flawed."
    t "I had no idea you hated birds so much."
    t "What did Noodles ever do to you?"
    s "I don’t hate birds. I just don’t think-"
    t "You just don’t think they should be allowed to attend[school] like the rest of us."
    s "No, that’s-"
    s "Actually. Yes, that’s right."

    scene tsuneyohall9
    with dissolve

    t "Noodles, attack."
    noodles "Caw!"
    s "Oh, he actually makes noise."
    t "That’s not all he can do."
    s "What is that supposed to-"

    scene tsuneyohall10
    with dissolve

    noodles "Caw!"
    s "What the fuck?"
    s "Where did it get such a small knife?"
    t "Do not ask questions you are afraid to hear the answers to."

    scene tsuneyohall9
    with dissolve

    s "You gave the bird a knife, didn’t you?"
    t "..."
    s "..."
    s "Tsuneyo."
    t "Well, I couldn’t just say no to him."
    s "He {i}asked{/i} you for one?"
    t "I thought maybe he wanted to learn how to prepare dinner for his family."
    s "He doesn’t have a family, though. He would have gone back to them already."

    scene tsuneyohall8
    with dissolve

    t "Perhaps he is just a horrible parent?"
    t "If birds are able to attend[school], it is also possible that they, too, struggle with certain family values from time to time."
    s "They...can’t attend[school], though. How did we get back to this?"

    scene tsuneyohall9
    with dissolve

    t "Noodles, attack."
    noodles "Caw!"
    s "Noodles, don’t attack."
    noodles "…"
    s "Why does he only respond to you?"

    scene tsuneyohall8
    with dissolve

    t "He is thankful that I provided him the tools he needs to prepare dinner for his family."
    s "If you’re going to go with that dinner excuse, you’re going to need to tell him to stop attacking me."
    s "Don’t force Noodles into a life of murder."

    "What is my life becoming?"

    if bonus == True:
        "Why am I arguing with a [teenage]girl about birds when there are several others I can think of off the top of my head that would have sex with me?"

    scene tsuneyohall10
    with dissolve

    noodles "Caw! {i}(Perhaps it’s because you’ve become too complacent with your current life and are just looking for that “chase” once again.)"
    noodles "Caw! Caw! {i}(Or perhaps you find comfort in knowing that there is someone with a fresh view of not only you, but of everything.)"
    noodles "Caaaaw! {i}(A worldview untainted by the evils of man. Just a girl with a passion for her craft and not a care in the world about romance.)"

    scene tsuneyohall11
    with dissolve

    noodles "Caw! {i}(Or perhaps you just want to return things to how they should be?){/i}"

    scene tsuneyohall8
    with dissolve

    s "Okay, I think it might be time for me to leave."
    t "Already? Why?"
    s "I’m beginning to think the bird is talking to me."
    t "But he is talking to you."
    t "I taught Noodles about existentialism."
    s "...How?"
    s "Why?"
    noodles "Caw!"
    t "If you are leaving, would you mind if I asked you a question first?"
    s "Sure, whatever. What is it?"
    t "It’s kind of personal, so I apologize if this crosses any lines."
    s "Just ask the question, Tsuneyo."

    scene tsuneyohall12
    with dissolve

    t "Okay. Well...here goes."

    "Tsuneyo begins to blush and bashfully looks away from me, clearly nervous about whatever she’s about to ask."

    t "Do you think you could..."
    t "…"
    t "Tell me what your favorite breed of whale is?"

    scene black
    with dissolve

    s "Nope. See you later, Tsuneyo."
    s "Have fun with your bird."
    t "But he is {i}our{/i} bird."
    t "You can’t just walk out on us like this."
    t "He hasn’t even started[school] yet."
    s "See you tomorrow."
    t "Get back here, you bastard."

    "..."
    "Well, that certainly was..."
    "One way to spend a Wednesday night."

    s "Tsuneyo is confusing..."
    s "…"
    s "And what the fuck was up with that bird?"

    "{i}Somewhere, off in the distance, the cawing of an existential bird rings out.{/i}"

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyofirsthall = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label tsuneyohall:
    if chapthreeactive == True:
        scene tsuneyosummer2hallgen1
        with dissolve
    elif christmas7 == False:
        scene tsuneyohall1
        with dissolve
    else:
        scene tsuneyohallwinter1
        with dissolve

    s "Hey, Tsuneyo."
    t "Ah-"

    if chapthreeactive == True:
        scene tsuneyosummer2hallgen2
        with dissolve
    elif christmas7 == False:
        scene tsuneyohall3
        with dissolve
    else:
        scene tsuneyohallwinter2
        with dissolve

    t "What's up, bro?"

    "Tsuneyo and I attempt to have a conversation in the hall to the best of our ability."
    "She tries her hand at speaking informally but, as always, fails dramatically."
    "Either way, we manage to keep the ball rolling for a few minutes and I can feel the...strange bond between the two of us growing stronger."

    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label mollyhall:
    if chapthreeactive == True:
        scene mollysummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene mollyhall1
        with dissolve
    else:
        scene mollyhallwinter1
        with dissolve

    mo "Evening, Sir! Have you perhaps come to join the Cult of Molly?"
    s "Maybe next time. I kind of just want to talk for now."
    mo "Suit yourself! Please think seriously before joining as all membership fees are non-refundable."
    s "...I have to pay?"
    mo "Aye."
    mo "{i}In blood...{/i}"

    "Molly and I hang out in the hallway for what feels like an hour or two but is probably only a few minutes."
    "She attempts to coerce a few ounces of blood out of me but, knowing that this is completely insane, I am able to refuse."
    "She sighs to herself and tells me that she'll get me eventually, and I wind up walking home while constantly looking over my shoulder."

    scene black
    with dissolve
    $ molly_love += 1
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label mollydorm5:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label dorm2wednesday:
    if chapthreeactive == True:
        scene summerdorm2wed
        with dissolve
    elif christmas7 == True and day271 == True and chapthreeactive == False:
        scene wedwinter2noriko
        with dissolve
    elif christmas7 == True and day271 == False and chapthreeactive == False:
        scene wedwinter2
        with dissolve
    elif christmas7 == False and chapthreeactive == False:
        scene dorm2_wednesday
        with dissolve

    if christmas7 == True and day271 == False:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"
    elif christmas7 == True and day271 == True:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo and Noriko aren't doing anything."
        "I could probably spend time with one of them if I want to."
        "What should I do?"
    else:
        "I walk up the stairs to the second floor of the dorms."
        "It looks like Tsuneyo isn't doing anything."
        "I could probably spend time with her if I want to."
        "What should I do?"

    menu wednesday2menu:
        "Knock on a door":
            jump doorknock2
        "Talk to Tsuneyo":
            if tsuneyofirsthall == False:
                jump tsuneyofirsthall
...
```