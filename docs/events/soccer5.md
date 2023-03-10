# It's Always Sunny in Kumon-mi (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 5



## Next events

None

## Event properties

* Id: soccer5
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer5

## Official wiki page

[It's Always Sunny in Kumon-mi](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer5&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer5:
    scene sky
    with dissolve2
    play music "highspeedprinter.mp3" fadein 3.0

    "I kick some dirt up as I make my way across the soccer field first thing in the morning."
    "Why I've decided to take my chances on conversing with the most energetic creature I have ever encountered less than an hour after waking up? I have no idea."
    "But I'm here now, so...I guess that means I should be making the best of it."
    "That aside, I'm here relatively early today. So chances are I'll have some time to kill before Miku and the others shows up."
    "I'm not exactly excited to spend this surplus of time alone, but I guess it will give me some time to think over whether I want to actually {i}coach{/i} this team or not."
    "On one hand, doing that would probably mean waking up earlier a lot more often...and that doesn't sound fun at all."
    "But on the other hand, it may enable me to seduce a congregation of tomboys- and that sounds significantly more interesting."

    s "..."

    "You know, maybe it's good that I came a little early? At least now I can-"

    mi "Heya! Sensei! Over here!"

    "At least now I can forget I ever thought that and get locked into a conversation with Miku."

    scene soccerfive1
    with dissolve

    mi "Mornin', Sensei! Come to watch me practice again?"
    s "Looks that way. And for a second, I thought I may have beaten you here."

    scene soccerfive2
    with dissolve

    mi "Ha! You're gonna need a lot of practice if you ever expect to beat me here. Not even rain or snow can stop Miku Maruyama from bein' the first one to practice every morning."
    s "Well I'm glad that it's always sunny in Kumon-mi because I'm beginning to believe you might freeze to death if it wasn't."

    scene soccerfive3
    with dissolve

    mi "Hey, yeah. That is kinda weird, isn't it?"
    s "You tell me. I've only been here for [totaldays] days so it's not like it's {i}that{/i} weird for me just yet."
    mi "The heck is that supposed to mean? You some kinda alien or robot the government sent over?"
    mi "Oh! Or maybe you're not the real Sensei at all and this is one of those body swap thingies! Like in that one movie with all the lens flares!"
    s "I have absolutely no idea what you're talking about, but I feel like that second one has a chance to be true."

    scene soccerfive1
    with dissolve

    mi "Just don't let Makoto know. She likes the normal Sensei a lot and I don't know how she'd handle some country girl bein' the one inside of you all of a sudden."
    s "I'd much prefer to be inside of the country girl in that scenario."
    mi "You would be! That's how body swaps work. You'd be inside of her and she'd be inside of you."
    s "Well, that just sounds difficult and painful. But anyway, where is everybody else right now?"
    mi "Idunno. Probably still wakin' up or somethin'."
    s "You’re the captain, aren’t you? Shouldn’t they get here whenever you show up?"
    mi "I mean...I guess so? I ain't holdin' it against anybody if they don't wanna be as early as me, though."
    s "Here's hoping that doesn't come around to bite you in the ass one day."

    scene soccerfive4
    with dissolve

    mi "Ain't much to bite in the first place."
    s "..."
    mi "..."
    s "I can't tell if that silence means you want me to compliment your ass or not."

    scene soccerfive2
    with dissolve

    mi "Sensei, if there's anything I've learned from Netflix documentaries, is that it's probably best to never compliment a schoolgirl's butt."
    s "What an extremely specific thing to be the {i}one{/i} piece of information you leeched from documentaries."

    scene soccerfive5
    with dissolve

    mi "I kinda only pay attention for the first ten minutes or so anyway, so it ain't like that info has anywhere to go."
    mi "'Sides, my brain's filled to the brim with soccer stuff so there ain't even room for all that smart person mumbo jumbo."
    s "I'm sure you could be plenty smart if you applied yourself, Miku."

    scene soccerfive6
    with dissolve

    mi "Applied where?"
    s "Okay, nevermind."
    mi "I’m confused."
    s "You know what? Why don't we talk about something you do understand. Like...soccer."
    s "Why exactly do you want me to be your coach again?"
    mi "Because the last one got knocked up and we're gonna get disbanded if we don't find a new one."
    s "So...it doesn't have to be me. It can be anyone?"
    mi "Pretty much, yeah."
    s "You're not very good at selling things, Miku."

    scene soccerfive7
    with dissolve

    mi "Selling?! I gotta {i}pay{/i} you now?!"
    s "That...That would be {i}buying,{/i} wouldn't it?"
    mi "I don't friggin' know! I've been lost since you started talkin' about butts!"
    s "I will do my best to resist bringing them up in the future, but I will also inform you now that I will likely fail."
    mi "So...wait, are you gonna be the coach or not?"
    s "I'm still not sure. I don't know the first thing about soccer. Hell, I barely even remember all the names of my students. There's no way I can memorize the entire team."

    scene soccerfive1
    with dissolve

    mi "Really? I thought learnin’ names that quick was like a special ability all teachers were just born with."
    s "Well, first off, we aren’t born as-"
    s "Well...{i}most{/i} people aren't born as teachers."
    s "But even the ones that {i}are{/i} still have to practice memorizing names."
    mi "Really? Then...do you have any special talents at all, Sensei? It doesn't have to just be boring teaching stuff. Could be anything."

    if bonus == True:
        s "I...guess I'm good with my hands?"
    else:
        s "I am exceptional when it comes to braiding hair."

    scene soccerfive7
    with dissolve

    if bonus == True:
        mi "What do you mean? Like givin' massages or somethin’?"
        s "Sure. Why not?"
    else:
        mi "Woah! Ya must be really good with your hands, then!"
        s "I am okay, I suppose. I just like how hair feels against my skin."

    scene soccerfive8
    with dissolve

    mi "Well, that’s just one more reason for you to be coach, then!"

    if bonus == True:
        mi "Never underestimate the value of a good massage on an athlete’s muscles!"
        mi "Plus, think of all the girls you’d get to rub without ever seemin' like a weirdo!"
        s "There is no possible way things would work out that easily."
        mi "Sure it would! Silence 'em all with those magic hands of yours!"
        s "Can I just...give the massages without doing the coaching thing?"
    else:
        s "It is?"
        mi "Yeah! Lots'a girls on the team would love gettin' their hair braided!"
        s "But I am a human male and you are all human females. Someone could get the wrong idea."
        mi "Hmmmm..."

    scene soccerfive7
    with dissolve

    mi "That might be kinda hard explainin’ to everybody..."
    mi "Especially on account of most of ‘em not havin’ any experience with boys and stuff."
    s "Are you implying that you {i}do{/i} have experience with boys, Miku?"

    scene soccerfive9
    with dissolve

    mi "Huh?"
    mi "Me?"
    mi "The heck are you talkin’ about?"

    if bonus == True:
        mi "Have you {i}seen{/i} me? I’m built like a ten year old boy. "
        mi "Goin’ on a date with Miku Maruyama would be like...askin’ out your little brother."

        scene soccerfive1
        with dissolve

        mi "I don't care, though! I don’t really have time for stuff like that anyways. Gotta focus on soccer and stuff."
    else:
        mi "I don't got time for that kinda stuff when I'm so determined to become the best soccer player in all of Kumon-mi!"

    scene soccerfive2
    with dissolve

    if bonus == True:
        mi "Plus! My growth spurt should be comin’ any day now! Don’t be surprised if I wind up even bustier than Futaba this time next year!"

        "I am trying to picture that and I...can't really see how it would work."

        s "Maybe...aim for someone closer to Rin's size if you're going to have goals like that. I don't know if Futaba is at a level you'll ever be able to reach."
        s "She’s honestly kind of unreal for someone your age."

        scene soccerfive6r
        with dissolve

        mi "Right?! You could knock over an ice cream truck with those puppies!"
        s "But...why would you-"
    else:
        mi "Plus! I've still gotta get ripped so that if anyone ever pulls a sword out on the field, I'll be able to deflect it with my abs!"

    scene soccerfive1
    with dissolve

    mi "You just could, okay? And hey, why are you even here so early?"
    mi "We started talkin’ about body swaps and stuff right away so I never found out. You have some kinda...teacher meeting or something?"
    s "Maybe I was just really excited to see you?"
    mi "Yeah, I ain't buyin' that. What's the real reason?"
    s "No real reason, I guess. Thought about heading over to the cafe beforehand, but that...never happened."
    mi "The one Rin works at? Makoto loves that place."
    mi "She always gets this weird drink with caramel in the name."
    mi "It’s like a caramel marshmallow or something."
    s "I think that would be a...caramel macchiato?"
    s "I guess that drink fits her, though. Sweet and mildly complicated."

    scene soccerfive2
    with dissolve

    mi "And totally hot, right?"
    s "..."
    mi "{i}Right?{/i}"
    s "Miku, do you have a crush on Makoto?"

    scene soccerfive6r
    with dissolve

    mi "What?! No!"
    mi "She just told me she’d buy me lunch if I said nice stuff about her to you. I didn't mean to make it sound like I was tryin' to score with her!"
    s "Makoto is...paying you to 'talk her up' to me?"

    scene soccerfive2
    with dissolve

    mi "You bet! And for the low, low price of 500 yen, I can deliver a message for you as well!"
    s "Are you some sort of used car salesman now? Because I thought we figured out that selling things wasn't right for you."

    scene soccerfive4
    with dissolve

    mi "With my grades, I might have to be."
    mi "You don’t have to take any sort of fancy test to become a car salesman do you?"
    s "I don’t think so?..."
    s "But is that something you really want to do?"

    scene soccerfive5
    with dissolve

    mi "I don't know. I haven’t really thought about the future like that."
    s "You haven’t? I was under the impression you just wanted to be a soccer player or something."

    scene soccerfive1
    with dissolve

    mi "I mean, that’d be awesome, yeah. But even someone as good as me isn’t a sure shot to make the Olympic team..."
    mi "Or...any sort of professional team, for that matter."
    mi "I always hear people sayin’ stuff like “Miku! You need a backup plan! What if your leg snaps in half or your arm gets bitten off by a shark!”"
    mi "And I’m just over here like, “Sharks aren’t even real!”"
    mi "And then Makoto is all like “What are you talking about?! Of course they are!”"
    mi "And so I’m all like “You’re not my mom, Makoto! Gimme my 500 yen for tellin’ Sensei you’re a caramel marshmallow!”"
    s "Miku, I think you need to sleep more."

    scene soccerfive2
    with dissolve

    mi "Heheh...I’m just pullin’ your leg this time."
    mi "I’m sure I'll be fine with whatever happens to me after high school."

    scene soccerfive9r
    with dissolve

    mi "Yeah, I might not make it as a soccer player or used car salesman or whatever-"
    mi "But as long as I can find somethin’ that makes me happy, that’s all that matters, right?"
    s "..."
    mi "..."

    play sound "whistle.mp3"
    scene soccerfive11
    with dissolve

    mi "Oh! Here come the other girls!"
    mi "Hey! I'm over here with our future coach!"
    mi "Kirin! Make sure you wear your shin guards this time! If your sister kicks you in the leg again, don’t come cryin’ to me!"

    scene soccerfive1
    with dissolve

    mi "Sorry to break up our meeting, but I’ve gotta get to practicin’ for real now, Sensei."

    if bonus == True:
        mi "But it was fun talkin’ to you and stuff! Keep thinkin’ about that coachin’ offer if you ever want to rub some [teenage]legs!"
        mi "Or just drop by whenever you want to hang out! So long as I'm not practicin', I mean."
    else:
        s "I will miss you dearly and wish you the best of luck in your athletic journey."

    scene black
    with dissolve2

    "Miku gets up and sprints over to the rest of her team, jumping into the arms of a taller looking girl before I even have a chance to respond."
    "I wonder what she meant by finding ‘something that makes her happy...’"
    "I'm sure she's not the only person who hasn't been thinking that much about the future...but she should probably have at least {i}some{/i} sort of idea and-"

    s "..."

    "My thoughts of Miku's future are interrupted by a stampede of exposed thighs and form fitting spandex."

    $ renpy.end_replay()
    $ soccer5 = True
    $ miku_love += 1
    stop music fadeout 3.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label soccer10:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
    if miku_love >= 5 and soccer5 == False:
        jump soccer5
...
```