# Paperthin (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 10

* Event [Unnamed Wooden Robots](./iodorm5.md) (Io) is completed)

* Event [Viva la Revolución](./iofirsthall.md) (Io) is completed)



## Next events

* [Main: Annabel Lee](./day280.md)
* [Main: Operation: Firestarter](./day318.md)

## Event properties

* Id: iodorm10
* Group: Io
* Triggered by label: iodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->iodorm->iodorm10

## Official wiki page

[Paperthin](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iodorm10&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm10:
    play sound "knock.mp3"
    stop music fadeout 20.0

    "I knock on Io’s door and wait for her to answer."
    "I’m sure I’ll need to knock again or announce my presence at some point to circumnavigate her antisocial tendencies but-"
    "I see no harm in testing the waters each time I arrive."
    "It’s only a matter of time until that shell of hers crumbles and she winds up greeting anyone who knocks."
    "If anyone knocks."
    "There’s no reason anyone would want to at this point, is there?"
    "No one but me, that is."

    if bonus == True:
        "And it’s not like it’s flattering receiving a visit from me given that my end goal with all of these girls is exactly the same."
        "To sneak inside of them- in more ways than one."
        "Into their minds. Into their hearts."
        "Into their sheets. "
        "Their pants."
        "Their bodies. "
        "And to leave minimal trace behind so my efforts aren’t thwarted somewhere along the line I’m actively trying to erase."
        "If you think that’s so horrible-"
        "Then just look away."
        "It’s that easy."
    else:
        "And it’s not like it’s flattering receiving a visit from me when all I'm really interested in is hugging and Hot Pockets."

    s "…"

    play sound "knock.mp3"

    s "Io, it’s me."
    i "{i}Hah...{/i}"
    i "Say that after the first knock from now on."
    i "Come on in, Sensei."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I probably {i}should{/i} just say I’m here after the first knock, shouldn’t I?"
    "If my goal is so impure, is the pause to see if she’s grown as a person really all that necessary?"
    "Time is precious."
    "Or at least it used to be."
    "But I could still save so much of it by giving up on her."

    scene iodormten1
    with dissolve
    play music "io.mp3"

    i "Welcome back. "

    "So why won't I do that?"

    s "Hey. Any plans for tonight?"
    i "Not until now. "
    i "Was thinking about taking a trip to the convenience store but my shoes are still soaking wet from walking home in the snow."
    s "You only have one pair?"
    i "I only need one pair."
    s "Clearly not if shoes are currently your only barrier from fulfilling your nightly goal."

    scene iodormten2
    with dissolve

    i "Okay, sorry. I {i}usually{/i} only need one pair."
    i "But it’s not like the inability to go on a little walk is something that’s going to ruin my life."

    scene iodormten3
    with dissolve

    i "Especially now that you’re here."
    i "You’re a little bit more fun than a trek through frozen rain. "
    i "Just a little, though."
    s "Thanks. I also like you more than I like snow, if that means anything to you."
    i "It does."
    i "I have a tendency to think everyone likes everything more than me by default until proven otherwise."
    s "Well I’m not really in the mood to list all of the things you’re better than, so we should probably just change the topic now."

    scene iodormten2
    with dissolve

    i "Hahah...Probably."

    scene iodormten4
    with dissolve

    i "So, what do you want to do?"
    i "You came all the way here with just your regular blazer on. Aren’t you cold?"
    i "I’d offer you a jacket or something but I’m pretty sure that nothing I have would fit you."
    i "We can get under the kotatsu if you want?"
    i "It doesn’t turn on since I’m still trying to fix it, but it’s got a blanket and blankets are cool."
    i "Well, warm. They’re not cool at all. You know what I mean."
    s "There’s the bed, too. "
    i "Yes. There’s the bed, too. "
    i "If you can reach it, that is."
    i "You’re gonna have to climb over some stuff to get there so I figured a spot on the floor might be easier for you."
    s "Are you doubting my agility, Io Ichimonji?"

    scene iodormten5
    with dissolve

    i "Woah. Breaking out my last name? You must be really serious right now."

    if bonus == True:
        s "Never underestimate my willpower to get into bed with a cute girl."
    else:
        s "Nah. Just trying to look cool around a cute girl since I get nervous really easily and am very shy."

    scene iodormten6
    with dissolve

    i "Ooooh I’ve moved from “bathhouse attendant” to “cute girl” in your book. What a momentous occasion. "
    s "You’ve held both titles since I met you."
    i "{i}I’m flattered you feel that way, Sensei, but I’m sure it’s just your craving for body heat that is causing you to say such things.{/i}"
    i "{i}So I’m sorry but I must reject you. I hope we can stay friends, though.{/i}"
    s "And with that, you’ve earned the title of “Uta impressionist” as well."

    scene iodormten7
    with dissolve

    i "Nihihi~ Pretty good, right? I spend so much time with her that it’s basically second nature at this point."

    scene iodormten8
    with dissolve

    i "Come on. We can sit on the bed."
    i "As long as you can get to it, I mean~"

    scene black
    with dissolve

    "Io manages to slip between a table and a minifridge without bumping into either of them and hops onto her mattress."
    "I am slightly less successful but still manage to make it through without breaking anything, so this is a victory in my book."
    "………"
    "……"
    "…"

    scene iodormten9
    with dissolve

    i "Congratulations on passing through the barrier."
    s "I’m impressed you were able to make it through without even touching anything."
    i "I’m like five feet tall and paperthin. Plus I’ve done it a bunch of times before."
    i "Muscle memory really helps out with small things like that."
    i "Also, it’s not weird if I sit this close to you, is it?"
    i "You’re not getting nervous, are you?"
    s "Not at all."
    s "Are you?"
    i "Not at all."
    i "I'm just chilling."
    i "Wanna watch a movie or something? I’ve got a bunch."
    s "I already told you I’m not into movies."
    i "Yeah, but I’m obviously gonna try to change your mind when they’re another big hobby of mine. "
    s "You have too many hobbies."
    i "You don’t have enough hobbies. "
    i "Take something up so we can have a reason to hang out more."
    s "I was unaware that we needed a reason to hang out more."
    i "Less of a reason and more of an excuse so that no one will start thinking anything is going on between us."
    i "If we’re both in like...the golf club or something, nobody will think we’re up to anything if we hang out somewhere after[school]."

    if bonus == True:
        s "At this point, I think it’s pretty safe to assume that anyone and everyone thinks I’m up to something at any given point."
        s "Being around me probably just opens you up to more pressure like that."
    else:
        s "I don't think anyone would expect that at all since I am the huggy boy, but I don't blame you for wanting to avoid any pressure on that end."

    scene iodormten10
    with dissolve

    i "I don’t care about pressure but..."
    i "Is that really what everyone thinks of you?"
    i "That you’re up to something?"
    s "…"
    i "You’re not, though. Right?"
    i "And even if you were, isn’t it a little obsessive of them to not let you do what you want to do? "

    if bonus == True:
        i "You’re an adult. You don’t have to care about what a bunch of [teenage]girls think. They-"
        s "They’re toxic, yes. I already know how you feel."
        s "You’ve mentioned it a few times now."
    else:
        s "Is this the part where you call them all toxic again?"

    scene iodormten11
    with dissolve

    i "...Yeah."
    i "…"
    s "…"
    i "You know, Sensei..."
    i "I’ve got a lot going on and I’m by no means perfect-"
    i "But I’d never do something like judge you for hanging out with whoever you want to hang out with."
    i "That’s your prerogative."
    s "..."
    i "..."
    s "That’s not true and you know it."

    scene iodormten12
    with dissolve

    i "...Huh?"
    s "It’s human nature to get jealous of things you don’t have- or things you want."
    s "It’s clear you want to spend as much time with me as possible, so you’d obviously judge me if I just abandoned you for other girls."
    i "…"

    scene iodormten13
    with dissolve

    i "Yeah, you’re probably right."
    i "I don’t think I’d ever say anything about it, though."
    s "That’s because you’re a coward."
    i "I know."
    s "And you’re weak."
    i "Uh-huh..."
    s "And you have stupid hair."

    scene iodormten14
    with dissolve

    i "Okay, now you’re just being mean."

    scene iodormten15
    with fade

    "Io moves closer to me and rests her head on my shoulder- something people don’t normally do after you insult them."
    "Granted, I was just kidding for the most part. But it’s still a strange reaction either way."

    i "You can keep making fun of me if you want. I don’t mind."
    s "Sure but-"
    i "This is okay, right? Even though I’m a weak coward with stupid hair?"
    s "There’s nothing cowardly about making a move like this on your teacher."
    i "You’re right. I’m actually kind of awesome, aren’t I?"
    s "You’re definitely unique, if not anything else."

    scene iodormten16
    with dissolve

    i "That’s far from a compliment, Sensei."
    i "Being unique can be a death sentence sometimes."
    i "Also, you don’t actually think my hair is stupid, do you?"
    i "It’s like, one of the three things I like about myself."
    s "What are the other two?"
    i "My eyes and how I can still get out of bed in the morning."
    s "That last one is a little more real than I was expecting, but I get it."
    i "Do you have three things you like about yourself, Sensei?"
    s "I’m not even sure I have {i}one{/i}."

    scene iodormten17
    with dissolve

    i "And you call {i}me{/i} a coward. That’s the most cowardly thing I’ve ever heard."
    i "Everyone has {i}something{/i} they like about themselves. Even if it’s something small like how you look in a particular photo or how your voice sounds when you sing in the shower."
    i "There’s gotta be something in there."
    i "I’ve already found plenty of stuff I like about you."
    s "Name one."
    i "Your shoulder’s really comfortable. And warm."
    i "And I like how you still come talk to me despite me being overbearing and annoyingly sensitive."
    s "Yeah. You’re kind of hard to talk to at times."
    i "True. But at least I'm more interesting than the rest of the girls in class, right?"
    i "I mean, why else would you be here tonight instead of with any of them?"
    i "Not to mention, I haven’t even seen you with that one blonde girl again since the two of you showed up at the bathhouse."

    scene iodormten18
    with dissolve

    i "Are you bored of her now that you have me?"
    i "I’ve gotta say, I kind of get it."
    i "She seemed a little too plain anyway."
    i "Pretty, but plain."
    i "Obviously, I’m sure there’s a lot more to it than that."
    i "But even the fact that you’re letting me rest my head on your shoulder like this-"
    s "What are you doing?"

    scene iodormten19
    with dissolve

    i "Hm?"
    i "What do you mean?"
    i "Aren’t we bonding?"
    i "Did I say something wrong?"
    s "This is your idea of bonding?"
    s "Talking down about people you’ve never even spoken with?"
    i "..."
    s "That blonde girl's name is Ayane and she’s far from plain."
    s "She’s actually one of the most unique people I’ve ever met."

    scene iodormten20
    with dissolve

    i "Wait, I wasn’t trying to talk down on her. I was just..."
    s "Just what?"
    i "I...I was just trying to make you think I was...more interesting."
    s "There are ways to do that without making everyone else seem small."
    s "You’re underestimating how much you’ve impressed me so far."
    s "Don’t ruin all of that by belittling people you know nothing about."

    scene iodormten21
    with dissolve2

    i "..."
    s "..."

    "The caterpillar squirms once more."

    i "I'm..."
    i "I’m sorry."
    s "There’s no sense in apologizing to me."
    s "Just think more about what you’re saying before you actually say it."
    s "You’re smart. Bad with people, maybe, but really...really smart."
    i "Sensei..."
    s "You’re better than this. That’s all I’m saying."

    scene iodormten22
    with dissolve2

    i "Well..."
    i "Why are you here, then?"
    i "If there are other interesting people who don’t do things like talk down on everyone around them, why come {i}here{/i}?"
    i "I just...thought there was a reason for it. That’s all."
    s "I’m here because I wanted to be here."
    s "Don’t overthink it or try to turn it into some sort of equation that needs to be solved."
    s "Not everything happens for a reason. Sometimes things just...happen."

    scene iodormten23
    with dissolve

    i "…"
    i "Sometimes...things just happen..."
    i "..."
    i "I messed up big time, didn’t I?"

    scene iodormten24
    with dissolve2

    s "Yeah."
    s "But you’re still learning."
    s "Just don’t be a bitch and everything will work out fine."
    i "I like the head patting thing but not so much the being called a bitch part."
    i "I guess I deserve it, though."
    i "Either way, please don’t stop. That feels really nice."

    scene iodormten25
    with dissolve

    "I leave my hand on Io’s head for reasons beyond my comprehension...but I feel like a good portion of them are simply due to how cute she is."
    "Frankly, though...I’m actually kind of mad right now."
    "It’s one thing to not associate with any of the other girls- a thing I can understand and respect."
    "But to do something like demean them behind their backs without even attempting to understand where they come from-"
    "Isn’t that exactly why Io dislikes girls in the first place?"
    "Because they start unnecessary drama?"
    "Is she really this desperate for affection?"

    i "Mn..."

    "Or is it something else?"
    "Something I don’t understand yet."

    scene black
    with dissolve2

    "I don’t stay much longer after that, but not because I don’t want to."
    "Io actually asks me to leave so she can get a head start on some new thing she wants to build."
    "I try asking what she plans on making, but she hurries me out of the room in suspiciously quick fashion."
    "It is what it is, though."
    "I’m not interested in dampening her creative process when she seems weirdly motivated all of a sudden."
    "I just hope that whatever it is she makes doesn’t wind up collecting dust on her shelf for the rest of eternity."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm10 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label iodorm15:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
    if io_love >= 10 and iodorm5 == True and iofirsthall == True and iodorm10 == False:
        jump iodorm10
...
```