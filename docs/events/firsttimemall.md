# The Retail Machine (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 0



## Next events

* [Chika: Something About Biting](./chikadorm5.md)

## Event properties

* Id: firsttimemall
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall
* Triggered by path: mall->firsttimemall

## Official wiki page

[The Retail Machine](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimemall&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label firsttimemall:
    scene chikanewmall1
    with fade
    play music "mall.mp3"

    "I decide to spend my afternoon at the mall because-"
    "Well, I don’t really know. "
    "It’s probably safe to just chalk it up to some subconscious desire to hang around teenage girls, though, since that’s pretty much all there is to do with my life now."
    "Not like there are many other things I’d prefer doing in the first place, but you get the point."
    "Without an inkling of what to do as a middle-aged man in a shopping mall, I spend my time walking around in circles, hoping to bump into someone I know."
    "Unfortunately, this process repeats itself a good five times before I’m able to find any amount of success."

    scene black
    with dissolve2

    "That success comes in the form of one of the girls from my class, alone on a bench I’ve passed several times over now."
    "I doubt she’ll be happy to see me since the mall is like a...recreational sanctuary to girls her age, but that’s not something I’m going to dwell on when I’m getting desperate at this point."
    "Worse comes to worst, I simply walk away and the two of us forget I ever tried to talk to her in the first place."

    q "Sensei? Is that you?"

    scene chikanewmall2
    with dissolve

    s "Hey, Chika."
    c "Hey! It’s not often I see you outside of school. What brings you to the mall?"
    s "A mix of despondence, boredom, and lack of direction. You?"

    scene chikanewmall3
    with dissolve

    c "I work here. Just sat down for my break, actually."
    c "You’re welcome to join me if you want, but I doubt you’d-"
    s "Deal."

    scene chikanewmall4
    with dissolve

    c "Oh! Okay. Nevermind, then."
    c "I didn’t really think you’d want to spend your day off hanging out with somebody like, half your age."
    s "And I didn’t think you’d want to spend your break with someone old enough to be your father, but here we are."
    c "Oh, come on. You’re not {i}that{/i} old..."
    c "Are you?"
    s "I really wish I could tell you."
    c "Uhh...why can’t-"
    s "Anyway, which one of these stores do you work at? Maybe I can drop by sometime and like, support local business or whatever."

    scene chikanewmall5
    with dissolve

    c "If by “support local business” you mean pump some money into a major corporation, feel free to drop by. It’s the really fancy looking place at the east end of the mall."
    s "Does it have a weird, French name? Because I passed by a place like that earlier and couldn’t even bring myself to look inside again after catching a glimpse of the prices."
    c "Yup. That’s the one. I am but a humble slave to the retail machine that is {i}Les Vêtements{/i}."
    c "Gotta pay the bills somehow, though. You know?"
    s "Sure, but I can’t imagine someone your age has very many bills to worry about."

    scene chikanewmall6
    with dissolve

    c "Hahah...yeah..."

    scene chikanewmall7
    with dissolve

    c "But, uhh...yeah. That’s where I work. So if you ever want to drop by just to say hi or something, feel free. I won’t pressure you into buying anything since I know how crazy expensive it all is."
    s "I appreciate that. Here’s hoping the “retail machine” doesn’t eat you alive."
    c "Have you ever worked a job like that before, Sensei? "
    s "Me? No. "

    "Or at least I don’t think so?"
    "For all I know (which isn’t much on account of the whole “rebirth” thing), I could have worked in the same exact store as Chika when I was her age."
    "Without any experience to pull from, though, I’m probably better off just steering the topic toward something else."

    s "So about those bills you supposedly have to pay-"

    scene chikanewmall8
    with dissolve

    c "What? No. Why? How are we back to that?"
    s "I’m just curious, that’s all."

    "I’m not, really. I just don’t want to risk talking about myself before understanding a little more about...who I am or where I’m from or...anything like that."
    "And if making Chika slightly uncomfortable is the price to pay for saving face, I suppose she’ll just have to suffer."

    scene chikanewmall9
    with dissolve

    c "I’ve just got...other obligations, I guess. It’s not really something I want to get into right now."
    s "Other obligations? You mean like, a boyfriend?"

    scene chikanewmall10
    with dissolve

    c "Boyfriend?! No way. Nuh-uh. It’s nothing even remotely {i}close{/i} to that. I have literally never even held hands before."
    c "My obligations are like, way more boring."
    s "Well, I’m sorry to hear that."

    "But I’m not sorry I was able to confirm that Chika is, at this moment in time, completely and entirely single."

    s "I have a hard time believing you’re completely inexperienced, though. Like, based on how you look, I kind of just figured that-"

    scene chikanewmall11
    with dissolve

    c "What’s wrong with how I look?"
    s "What? Nothing. I was just trying to say you look a lot more...{i}mature{/i} than the other girls in class."

    scene chikanewmall7
    with dissolve

    c "Oh! Well, that’s totally fine then."
    c "I thought you were gonna lean into that whole “gyarus are slutty” stereotype thing for a sec and I was about to get really upset."
    s "That’s not where I was going. I just kind of figured that someone as attractive as you would be popular with the opposite sex."
    c "I don’t know. I guess I just never really- "

    scene chikanewmall12
    with dissolve

    c "Wait a second. What did you just call me?"
    s "Should I not have said that?"
    c "No, you should say it again. I want to confirm that I’m not going crazy and that those words actually did just come out of your mouth."
    s "I’m not being recorded, am I? Because this is starting to sound like a set-up."
    c "A set-up for what? If I didn’t want you around, do you really think I would have invited you to chill with me during my break?"
    s "This is our first time spending time together outside of school. I have no idea what sorts of strategies you employ."
    c "Sensei, just friggin’ say it already. It’s totally cool."
    s "Fine. I think you’re attractive. Are you happy now?"

    scene chikanewmall13
    with dissolve

    c "Duh! I’m obviously not gonna get upset by a compliment I basically forced out of you."
    s "To be fair, the first time was voluntary. "
    c "Well...thanks, Sensei. "

    scene chikanewmall14
    with dissolve

    c "Even if we’re like, way out of each other’s dating ranges, I’m totally flattered. And, just for the record, I think you’re pretty handsome too."

    "Well, {i}now{/i} we’re getting somewhere."

    s "Oh?"

    scene chikanewmall15
    with dissolve

    c "{i}Oh{/i} what? Don’t believe me? You want it in writing or something?"
    s "No, I think that would be just as risky as the whole recording thing."
    c "Do {i}you{/i} have someone back at home, Sensei? You asked me, so it’s only fair that I get to ask you as well."
    s "Me? No. I already have ten teenagers I have to keep track of and that’s more than enough for me."
    s "Also, I {i}quite literally{/i} have Ami back at home, but that’s a totally different sort of thing."

    "A thing that I should...probably start putting some more thought into since that is absolutely a bridge I’ll have to cross one day."

    c "I would {i}really{/i} hope so! Because I’m pretty sure that would be like, way illegal."
    s "This is not a thing we should be talking about at the mall."

    scene chikanewmall14
    with dissolve

    c "Probs not, but we’ve been crossing boundaries for a few minutes now, so it would probably be good to start backing things up a bit."
    s "Agreed. The big takeaway from today’s conversation is that we’re equally attracted to one another and that I’m going to be coming to the mall more often from now on."

    scene chikanewmall16
    with dissolve

    c "For real? You actually are? "
    s "Is there a problem with that?"
    c "Not at all. It’s just..."
    c "This is all kinda coming out of nowhere."
    c "Like, just a few days ago, I looked at you as a totally normal teacher. And now we’re, like...bantering and stuff, and..."
    c "I don’t know. Doesn’t this feel a little weird to you, Sensei? Like, why’d your whole outlook on teaching change all of a sudden?"
    s "Just...woke up a brand new person, I guess."

    scene chikanewmall15
    with dissolve

    c "Well, for what it’s worth...I like this person a lot more so far. "
    c "He’s a lot of fun to talk to if this...spontaneous meeting on a bench says anything about the kind of guy he normally is outside of school."
    c "Unfortunately, that’s kind of all the time I have to hang out today since I’ve gotta be getting back to work."
    c "But I’ll be looking forward to seeing you more from now on, Sensei. Both in {i}and{/i} out of school."
    s "I’ll be looking forward to that as well."
    s "See you around, Chika."

    scene black
    with dissolve2

    "“The kind of guy I normally am outside of school...”"
    "This can’t possibly be that, can it?"
    "I was able to contain myself today, but...wasn’t it only because I was dead set on doing that?"
    "Moving too quickly in the beginning tends to scare people away. It doesn’t take a genius to understand that."
    "In order to get closer, sometimes you need to lure a person into a false sense of security."
    "There’s no way that girl is truly {i}safe{/i} with me when I’ve already begun planting seeds in her garden."
    "Soon, the flowers will begin to bloom and the two of us will flourish."
    "But it will be all because I got a head start."
    "And because she left her gate unlocked."
    "I leave the mall and try to figure out what else to do with my day."


    $ renpy.end_replay()
    $ firsttimemall = True
    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdaynight

label mall2to4:
    play music "mall.mp3" fadein 2.0
    scene mall1
    with dissolve

    "I decide to kill some time at the mall again."
    "Chika is sitting on a bench when I get there and she quickly waves me
    over to come watch some video on her phone."
    "She goes on to talk about a few new pop-stars and makeup
    tutorials and I basically just sit there and absorb her words, understanding very little."
    "Despite the two of us having virtually nothing in common, I feel strangely comfortable with her..."

    scene black
    with dissolve

    $ chika_love += 1

    "{i}Chika’s affection has increased to [chika_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdaynight

label mall5:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
...
```