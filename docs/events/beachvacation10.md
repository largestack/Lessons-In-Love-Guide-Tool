# Where Puppies Roam Free (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Wake Up Call](./amilust10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation10
* Group: Main
* Triggered by label: amilust10x
* Chain sources: amilust10
* Chain sources path: amilust10->amilust10

## Official wiki page

[Where Puppies Roam Free](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation10&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation10:
    if _in_replay:
        play music "normalday.mp3"

    scene beachbreakfast1
    with dissolve

    ay "...And so I say to the guy, “You {i}can’t{/i} kick me out! My father owns the place!”"
    ay "And so he’s all like, “Miss, that doesn’t mean you’re allowed to just free all of the animals! That will put them in danger!”"
    ay "So I grab him by the collar of his stupid shirt and I look him in the eyes and say..."

    scene beachbreakfast2
    with dissolve

    ay "My middle name is danger...and if you’ve got a problem with me freeing a few puppies, {i}I’ve got the nerve to show you why{/i}."

    scene beachbreakfast3
    with dissolve

    mak "But...that’s not your middle name. You don’t even have a middle name. You’re Japanese."
    mi "Hold the phone. Why would anyone get into trouble over freein’ some puppies? Puppies are supposed to be free! "

    scene beachbreakfast4
    with dissolve

    mak "I don’t think there’s anywhere in the world, let alone Japan, where puppies are {i}supposed{/i} to roam free."
    mak "The vast majority of dogs, other than wild ones like wolves I mean, are domesticated. "
    mak "So the chances of a normal puppy surviving alone in the wilderness is significantly lower than it would be should that puppy be in the care of a human."
    mi "...Why do ya gotta be so {i}real{/i} all the time?"
    mi "Why can’t ya just let my innocent heart think about some happy puppies floodin’ the streets of Kumon-mi?"
    mak "Because that would cause a multitude of problems that-"

    scene beachbreakfast5
    with dissolve

    ay "So anyway, how was your night, Karin? You went out jogging, didn’t you?"
    ay "I think most of us were probably asleep by the time you got back, right?"
    ka "Oh, uhh, yeah. It was nice. I kind of forgot how much harder it is to run in the sand, so that was a little bit of a wake up call."
    ay "You were able to find a spot in the room, though, right? I know it was kinda cramped in there. Especially with Molly sprawling out all over the place."
    ka "Yeah...I felt really bad for the one girl...Rin, I think?"
    ka "She was basically hugging her the entire night."

    scene beachbreakfast6
    with dissolve

    mi "Rin?! Imagine how I feel! I barely even know the girl and she was all up on me like I was her friggin’ body pillow!"
    mi "I felt like I was two steps away from gettin’ married with how close we were!"
    ki "You should have come slept next to me like I told you to in the first place."

    scene beachbreakfast7
    with dissolve

    mi "What, you mean right in front of the bathroom? Wouldn’t it be annoying havin’ people step over you to get in all night?"
    ki "I don’t even think I woke up at all. But I’m kind of a heavy sleeper so...yeah."

    scene beachbreakfast8
    with dissolve

    ka "I’m really thankful for that, by the way. Because I totally kicked you when I went in there to get dressed last night and you didn’t even move."
    ki "Gee. Thank you, beloved sister, for abusing me in my sleep. I’ll be sure to return the favor tonight."
    ka "I’ll be sure to not go to sleep until really late then."

    scene beachbreakfast9
    with dissolve

    mak "Oh, I've been meaning to ask...What’s it like having a little sister, Karin? "
    mak "I’ve always wanted one myself but my parents have always been pretty adamant about only having one child."
    ki "Yeah, Karin. What’s it like? Answer very carefully."

    scene beachbreakfast10
    with dissolve

    ka "Well..."
    ka "That’s kind of a hard question."
    ki "{i}Very carefully...{/i}"
    ka "Kirin and I don’t always get along. In fact, she was pretty unbearable when the two of us were little."
    ka "Being taller and older than her meant that she got a lot of my old clothes as I grew out of them, but that never stopped her from taking the ones I still used either..."

    scene beachbreakfast11
    with dissolve

    ka "Plus, I can’t even remember how many fights we’ve gotten into over other stupid stuff like where to go out to eat or what to name our cat."
    ki "I won the cat battle, in case anyone is wondering."
    ki "I’m clearly the superior sister."
    ka "Is that really what you think? That you won?"

    scene beachbreakfast12
    with dissolve

    ki "Uhh...well we went with the name {i}I{/i} chose, so yeah. That counts as a victory for me."
    ka "We went with {i}a{/i} name that you {i}agreed{/i} to. And you chose it out of a hat."
    ki "Whatever, still my name. You weren’t allowed to put anything in the hat anyway."
    ka "That’s just what Mom told you."
    ka "The {i}real{/i} truth is that I made up all of the names in the hat and just let you pick whichever one because I liked them all."

    scene beachbreakfast13
    with dissolve

    ki "You bitch!"
    ki "You two have been lying to me for years and letting me think I named the cat, when it’s really just been one long prank?!"
    ki "I don’t even want the cat anymore! Take it back to the pet store!"

    scene beachbreakfast14
    with dissolve

    ka "That pet store closed down like six years ago..."
    ka "And besides, you love Pancake. I don’t believe for a split second that you’d give him up that easily."

    scene beachbreakfast15
    with dissolve

    ki "Yeah well...fuck you, Karin."
    ka "I love you too!"
    mak "Your relationship seems a little more...complicated than I imagined it would be based on how often you two are together. "
    mak "I always figured having a little sister would be like always having someone to look after and...train, I guess."
    mak "Kind of like a mini-version of myself."

    scene beachbreakfast16
    with dissolve

    mi "Oh, heck no! I can barely deal with one of you!"
    mi "Ya have any idea how hard my life would be with {i}two{/i} Makoto’s? I’d never have time for soccer anymore."
    mak "True, but at least you’d be passing math."
    mi "What even is math?!"
    mak "It’s the subject with all of the numbers."
    mi "I know what it is! But like, what the heck {i}is{/i} it?! You know?!"
    mak "…"
    mak "No."

    scene beachbreakfast17
    with dissolve

    ka "Well, at the end of the day, I think it’s pretty safe to say that Kirin isn’t anything like me."
    ki "You’ve got that right..."
    ka "But honestly, I can’t imagine what life would be like without her."
    ka "Even if we fight all of the time and even if she stole like half of my clothes when we were growing up, thinking about doing all of that without her just seems pointless."
    ka "It sounds dumb, I’m sure, but I love her a lot. She means the world to me and, as her big sister, I’ll always have her back no matter what."

    scene beachbreakfast18
    with dissolve

    ki "Sis, what the fuck?! Why are you getting all sappy all of a sudden?!"
    ki "I haven’t even had breakfast yet! I don’t want to hear that!"
    ka "Don’t want to hear what? That I love you?"
    ki "Yes! You can’t just...say stuff like that in public! It’s embarrassing!"
    ka "I love you, Kirin!"
    ki "Ahhhhhhh!"

    scene beachbreakfast19
    with dissolve

    ay "Hey, Tsuneyo. Whatcha thinkin’ about over there?"
    ay "You’ve been pretty quiet all morning and I just want to make sure you’re not feeling left out or anything."
    ka "Yeah. We’re all friends here. Tell us what’s on your mind."
    t "…"
    ka "…"
    ay "…"

    if bonus == True:
        t "Masturbation."
    else:
        t "The Gaelic language."

    ka "…"
    ay "…"

    scene beachbreakfast20
    with dissolve

    ki "…"
    mi "…"
    mak "…"

    scene beachbreakfast21
    with dissolve

    t "Did I say something wrong?"
    ay "Well...no!"
    ay "I mean, I’m sure we all...everyone once in a while, but..."
    ay "Breakfast isn’t really the...best time to bring something like that up."
    t "It’s not?"
    ay "No...it’s just like..."
    ay "You know what? Maybe you should just go back to the inn alone for a little while if you really need to...do that."
    t "Do what?"
    ay "..."
    ay "Masturbate, obviously."
    t "But I don’t know how."
    ay "…"
    t "…"

    scene beachbreakfast22
    with dissolve

    ay "What?..."

    if bonus == True:
        t "I don’t know what masturbation is."
        t "I heard our teacher use the word yesterday and he told me it would be best to ask all of you about it."
    else:
        t "But I do not see what that has to do with Gaelic."
        t "Please teach me immediately, as the teacher refused to do so."

    scene beachbreakfast23
    with dissolve

    ki "Pfft..."
    mak "That son of a bitch."

    scene beachbreakfast24
    with dissolve

    ay "Would you...maybe mind explaining why Sensei would have told you to ask us about something like that?"
    t "He said that it was something that he probably shouldn’t teach me about and that one of you would show me."

    scene beachbreakfast23
    with dissolve

    mak "That son of a bitch..."
    ki "HAHAHAH! OH MY GOD!"

    scene beachbreakfast24
    with dissolve

    if bonus == True:
        ay "Well, uhh...I guess the easiest way to explain it would be that it’s like...sex that you do to yourself."
        ay "With like, your fingers or...toys or...the corner of the boy you admire’s desk."
        ay "Pretty much anything can get the job done if you try hard enough."
    else:
        ay "Well, uhh...I know it was brought over to Scotland from Ireland, but...my knowledge kind of stops there..."
        ay "Why not just ask Molly? I'm pretty sure she can speak it."

    ka "Is...anyone else getting dizzy?"
    t "I see."

    if bonus == True:
        t "So it is sex that you do to yourself."
    else:
        t "So the only way to find out is to go to one of the sources."

    ay "Exactly."
    t "Okay."
    ay "Great, so I guess we can just-"

    if bonus == True:
        t "What is sex?"
    else:
        t "But what if Scott does not want me on his land?"

    ay "…"
    t "…"

    play sound "thump.mp3"
    scene beachbreakfast25
    with hpunch

    ki "HAHAHAHAHAHAHAH!!!! AHHHHHH!!!!"
    mi "Ahh! Karin died! Someone call an ambulance!"
    mak "She’s not dead, Miku. She just...needs a minute to recover, I think."
    t "Is the tall girl with the beautiful abs going to be okay?"
    ay "Yeah...She’ll be fine. "
    ay "You’re the one I’m worried about."

    scene beachbreakfast26
    with dissolve

    t "I don’t understand."
    ay "I know you don’t..."
    ay "How about the two of us have a conversation in private later, okay?"

    if bonus == True:
        t "Are you going to teach me how to sex?"
        ay "Let’s just..."
        ay "Sure. Yeah. I’ll teach you how to sex."
    else:
        t "Do you know Scott?"
        ay "Sure. Yeah. I know Scott..."

    scene sky
    with dissolve2

    "…"

    s "So, what are you planning on doing today, Ami?"
    a "Me? I don’t know. More vacation stuff probably. "
    a "I know Ayane and some of the other girls are eating breakfast right now, but I can’t imagine they’re talking about anything exciting."
    s "Well let’s hope you didn’t miss anything fun."

    "Ami and I make it to the beach a short while later to find Karin passed out on her plate of breakfast."
    "I guess she must have had a long night."

    scene black
    with dissolve
    stop music fadeout 7.0

    "I decide to get some food from a nearby stall and scarf down an omelette before setting off to find something else to do this morning."

    $ renpy.end_replay()
    $ beachvacation10 = True

    "........."
    "......"
    "..."

label beachvacation11:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
label amilust10skipx:
    scene amibeachlust3
    with dissolve

    a "Get up..."
    a "…"
    s "…"
    a "…"
    s "…"

    play music "normalday.mp3"
    scene amibeachlust4
    with hpunch

    a "AHHHH!!! WHAT SORT OF SERIAL KILLER SLEEPS WITHOUT A BLANKET AND NO PANTS ON?!"
    a "IT’S TOO EARLY FOR THIS!"
    s "Zzzzzzzzzz..."

    scene amibeachlust7
    with dissolve

    a "Oh God...what am I supposed to do?"
    s "Mm...Ami?"

    "I open my eyes to find my [niece] standing in the doorway, caught in some sort of dilemma."
    "Probably due to the fact that I’m not wearing any pants and have a huge erection."

    scene amibeachlust5

    a "G-Good penis! I mean, good morning!"
    a "Um...I’m gonna go wait in the other room so just...get dressed and come out when you’re ready!"
    s "Yeah. I’ll be out in a second."

    "{i}Oh no! It looks like Ami wasn’t prepared to give you a morning blowjob!{/i}"
    "{i}If only her LUST was a little higher...This scene might have played out differently...{/i}"

    scene sky
    with dissolve2

    "Ami and I wind up walking to the beach together once my erection wears off."
    "She’s beet-red for the first few minutes, but the embarrassment eventually subsides as we make our way to where everyone else is..."

    "{i}Meanwhile...{/i}"

    $ renpy.end_replay()

    jump beachvacation10
...
```