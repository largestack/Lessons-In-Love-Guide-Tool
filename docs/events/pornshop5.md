# Watching Porn Alone
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=pornshop5&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 5



## Next events
None

## Event properties
* ID: pornshop5
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label pornshop5:
    scene pornshop
    with dissolve
    play music "citylife.mp3" fadein 3.0

    "Another night means another chance to embarrass Makoto, so I obviously decide to put these late hours to good use and terrorize my class representative."
    "Prepared to ruin her night, I walk through the doors and find the store entirely empty apart from my favorite employee and a large variety of sex toys."
    "I follow the sound of boxes being moved around and make my way across the store to find Makoto unloading a package of vibrantly colored dildos."
    "And honestly, seeing that is more than enough for me to deem tonight a success- but of course, I'm not going to leave here until I'm able to push her buttons a bit."

    scene pornfive1
    with fade

    mak "Correct me if I'm wrong, but I thought we agreed that you'd stop coming here."
    s "You're wrong. I'd never agree to such a thing."
    mak "And I'm assuming it wouldn't help if I explained how much I’d appreciate it if you just...let my work life be separate from my school one?"
    s "It would not. I want to know everything about you- from your blue eyes to the blue dildo protruding from the box near your feet."
    mak "I just don't understand why you keep coming here when I've already made it exceedingly apparent that I won't be selling you anything."
    s "Who says I’m here to buy anything?"

    scene pornfive2
    with dissolve

    mak "So you really do just find enjoyment in tormenting me, I see."
    s "To be fair, I thought that would have been obvious the second I returned."
    s "You just look so determined and professional while you’re here that it's just...really motivating."
    s "So thank you, Makoto. Thank you for your service."

    scene pornfive3
    with dissolve

    mak "You do realize that there are tons of places outside of school I'd be happy to see you in, correct?"

    if day38 == True:
        s "Like the park? Because we never did that again after the first time and that just makes me assume you prefer this."
        mak "I prefer...literally anything other than this."

        scene pornfive4
        with dissolve

        mak "Also, do you really expect me to believe that you want to use what little free time you have at the park with me?"
        s "Why not? I'm a lot more than just some insatiable porn addict, you know."
        mak "With how often you’ve been stopping by lately, I’m beginning to question that."
    else:
        s "Oh yeah? Like where?"

        scene pornfive4
        with dissolve

        mak "Um...well, there are places like the mall...or the movie theater..."
        mak "Or anywhere that doesn't reek of lubricant."

        scene pornfive3
        with dissolve

        mak "Just...you know...places we could hang out. Places where you could get to know the me that doesn't spend her nights stocking the shelves of a porn shop."

    s "Oh, speaking of which, I forgot to tell you about that DVD you let me have the first time I came by."

    scene pornfive6
    with dissolve

    mak "Why is that a thing you have to tell me about? Can't you just keep it to yourself?"
    s "No. You paid for it, so I obviously have to tell you about it now."
    mak "That is absolutely not a thing you have to do."

    if bonus == True:
        "Thankfully, I brought back the store’s copy of ‘After School Service: Student Council Punishment Games’ to see if maybe they
        have a trade-in policy of some sort."
        "Though, knowing Makoto, I doubt I’ll be able to actually trade it in even if they do."
    else:
        s "Napoleon Dynamite"
        s "I would like my money back."
        mak "But you didn't even pay for it."
        s "I know. But I deserve to be properly compensated for even holding something as horrible as this."

    s "But I will anyway. Here, look."

    "I remove the DVD (That I very conveniently happened to be carrying) from the inside of my blazer and show it to Makoto."

    if bonus == True:
        "The cover itself is boring, but there is an image of a girl who looks strikingly similar to her on the back jacking off two guys at once."
        "I could have done without the second guy, but it was a pretty solid DVD regardless."
    else:
        s "How could anyone possibly find this funny?"

    scene pornfive7
    with dissolve

    mak "Wha?!"
    mak "What the Hell do you think you’re showing me?!"

    if bonus == True:
        s "Just some girl who looks like you having the time of her life."
        mak "There are plenty of people out there who look like me! That doesn't make it okay to just...show me them {i}having the times of their lives.{/i}"
        mak "Now put that thing away before I call security."
        s "You don’t even have security."
        mak "Well....put it away anyway!"
    else:
        s "A very bad movie."
        s "Please. Remove it from my hands."
        mak "No! There are no takebacks here! Especially for shoplifted things!"

    s "I was kind of hoping I'd be able to trade it in for something else."

    scene pornfive8
    with dissolve

    mak "What kind of store do you think this is?"
    s "Not a very good one, apparently."
    s "…"
    mak "…"

    scene pornfive2
    with dissolve

    if bonus == True:
        mak "Hah...I don’t think I’m ever going to get over how you were secretly a pervert this whole time."
        mak "I swear, I never would have thought you were {i}that{/i} type of person in the beginning of the year."
        mak "You were so...professional. And serious."
    else:
        mak "Hah...I've been telling my mom for years that we should stop calling this place a DVD store and call it what it actually is."
        s "An adult-centered multimedia distribution center?"
        mak "Sure. Let's go with that."
        s "Life sure likes to throw us curveballs, doesn't it?"
        mak "Sure does..."

    scene pornfive8r
    with dissolve

    mak "And now you’re watching things like..."

    if bonus == True:
        "Makoto takes a quick glance at the DVD, doing her best to avoid locking eyes with her pornographic doppelganger."

        scene pornfive7
        with dissolve

        mak "S-Student Council Punishment Games?! We have like six million films here and you went and grabbed {i}that?!{/i}"
        s "It was actually pretty good. We should watch it together sometime."
        mak "Together?! Absolutely not! There's no way I could watch something like that with you hovering over me like some sort of...hungry jackal!"
        mak "I have a hard enough time just watching stuff like that on my own."
        s "And...what exactly is difficult about watching porn alone?"

        scene pornfive9
        with dissolve

        mak "Well, I just...I don't know...There's...not enough time?"
        mak "I’m barely ever alone to begin with...and when I actually {i}am,{/i} I'm normally studying instead..."
        mak "And these aren't exactly the types of movies I want to watch with my mom or Miku around..."
        s "You mean you and Miku don’t watch porn together?"

        scene pornfive5
        with dissolve

        mak "I don't think Miku's watched a single porn video in her life. She still closes her eyes any time she walks through the store."
        s "Maybe I should invite her to our viewing party as well?"
    else:
        s "Don't look at it Makoto. It will burn your eyes."
        mak "I can feel my soul being ripped from my body."
        s "Damn you, Pedro."

    scene pornfive5r
    with dissolve

    mak "Or maybe you should put that DVD back on one of the shelves and leave so I can finish closing the store?!"
    s "Aren’t you supposed to be open for another few hours? You can't keep closing early just because I'm bothering you."
    mak "If we don't have any actual customers, I can do whatever I-"
    s "I’m a customer. Hold on, let me get something."
    mak "I already told you that I don't intend to sell you-"
    s "It's not for me, it's for you. I'm getting you a present."

    scene pornfive9r
    with dissolve

    mak "A...present?"
    mak "But...what would you even-"

    if bonus == True:
        jump makotodildograbx
    else:
        scene black
        with dissolve

        s "Makoto, here. It is a brand new desk for you to study at because I know how much you like education."
        mak "How did you even get that into the store without me noticing?"
        s "That does not matter."
        s "Quick, sit down at the desk and show me how you study."
        mak "I am floored. This is such a generous gift."

        "I take a picture of Makoto enjoying her new desk and she gets very embarrassed because liking knowledge is something only a loser would do."

        $ renpy.end_replay()
        $ pornshop5 = True
        $ makoto_love += 1
        stop music fadeout 5.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label pornshop10:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
label pornshop:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump satnightmenu
    if makoto_love >= 0 and firsttimepornshop == False:
        jump firsttimepornshop
    if makoto_love >= 5 and pornshop5 == False:
        jump pornshop5
...
```