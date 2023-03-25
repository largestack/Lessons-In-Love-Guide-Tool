# Spontaneous Sentimentality (Touka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Horses or the Whispers of the Dead](./day304.md) (Main) is completed)



## Next events

* [Touka: Fish Out of Water](./toukadorm1.md)

## Event properties

* Id: toukafirsthall
* Group: Touka
* Triggered by label: toukahall
* Triggered by branch label: doorknock2
* Triggered by path: dorm2tuesday->toukahall->toukafirsthall

## Official wiki page

[Spontaneous Sentimentality](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukafirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label toukafirsthall:
    if _in_replay:
        play music "sweetvermouth.mp3"

    scene toukahall1
    with dissolve

    to "Good evening, Sensei. Do you have some sort of business in the girls’ dorm?"
    s "Hey. Nope. I’m just here to hang out."

    scene toukahall2
    with dissolve

    to "Hang out? Forgive me if I’m misunderstanding the full meaning of this popular common phrase, but wouldn’t that imply you are here for the express purpose of being around [young_girls]?"
    s "Yes. It would."
    to "I see."
    to "And forgive me if I am misunderstanding even more, but wouldn’t that imply that you have some rather unfavorable affinities for a man of your age?"

    if bonus == True:
        s "Again, yes. Yes it would."
    else:
        s "No. I just like hugs."

    to "I see."
    s "You’ll get used to it. I'm sure it will feel totally normal in no time at all."
    to "I..."
    to "I don’t think that it will."
    s "Either way, what are you up to tonight?"

    scene toukahall3
    with dissolve

    to "Well, I suppose I’m trying to understand exactly what I’m supposed to be doing here."
    to "It isn’t often that I have entire nights to myself and, somehow or another, I found myself feeling compelled to stand out in the hallway."
    to "Part of me wants to try greeting the dejected looking girl slouched up against the wall, but she does not seem to want to be bothered."
    s "I can tell you with absolute certainty that she definitely does not."
    s "But on the bright side, you have me now. And I am extremely exciting and only mildly suspicious."

    scene toukahall4
    with dissolve

    to "That sounds a lot like something a suspicious person would say."
    s "I don’t think so. A really suspicious person probably wouldn’t say anything. "
    s "They’d just stand there and stare at you, probably from around a corner or something."

    scene toukahall5
    with dissolve

    to "How bold of you to not utilize a corner at all and instead approach me with your suspicious behavior directly!"
    to "You are truly a man to be feared!"
    s "Again, you’ll get used to it and it will feel totally normal in no time at all."

    scene toukahall6
    with dissolve

    to "I somehow find the second utterance of that sentence even more disturbing than the first."
    to "So...go on. Out with it. What do you want or need from me tonight?"
    s "I already told you, I’m just here to hang out. I’m going to do that from time to time now that you live here."

    scene toukahall2
    with dissolve

    to "I understand that, but isn’t there some sort of objective you have in mind?"
    s "I mean, absolutely. But there is no way you are anywhere near ready for what that objective is."
    to "Well, now I’m rather curious. Can you not explain it?"
    s "Not without putting our future relationship in jeopardy. "
    to "I understand. If it will have some sort of effect on my time in both the dorms and [kumon_mi_high], I’d rather keep it at bay for the time being."
    to "It’s hard enough getting adjusted to life in a place like this."
    s "Yeah, I imagine this is basically the exact opposite of what you’re used to."

    scene toukahall3
    with dissolve

    to "I actually find it both endearing and mildly upsetting how so many girls are able to fit under one roof."
    to "I’ve yet to see the inside of anyone else’s room, but mine seems rather...small for two people."
    s "They’re all the same size. "

    scene toukahall7
    with dissolve

    to "And they expect us to live happily under these excruciatingly packed conditions?"
    s "Well, I don’t know if I’d say {i}happily,{/i} but yeah. "
    s "I guess it’s a lot easier if you don’t already have a bedroom that’s the size of this entire floor."
    to "Yes, I do suppose that having exactly that may be skewing my judgement in some way."
    s "Hold on a second...I was being sarcastic."
    s "You mean to tell me your bedroom is the size of this entire floor?"

    scene toukahall3
    with dissolve

    to "My first bedroom, absolutely. But my second and third are probably around the size of about...half?"
    s "What use could you have for three bedrooms?"

    scene toukahall7
    with dissolve

    to "Well, my first bedroom is where I keep all of my clothes and my...personal belongings. And the other two-"
    s "Why would you say “personal belongings” after a pause like that? That just makes it sound like you’re hiding something inappropriate."

    scene toukahall8
    with dissolve

    to "Th-That’s not what I meant at all! I just have several things that you would likely make fun of me for owning, so I would rather not disclose them at this point in time!"

    if toukastreets1 == True:
        s "That’s fine. I’m sure I’ll see whatever it is you’re hiding when I come over for that tea you promised me before."
        to "Absolutely not! As if I’d let {i}you{/i} of all people into my first bedroom!"

    else:
        s "That’s fine. It will just make finding out what you’re hiding from me all the more exciting when I finally get to see your “manor.”"
        to "You will do nothing of the sort! My first bedroom is still years and years away from accepting someone of the likes of you!"

    s "What about the second and third bedrooms, then?"

    scene toukahall9
    with dissolve

    to "Well...those are certainly closer to being within your reach than the first. But it would still be remarkably strange."
    to "I don’t think we’ve ever allowed anyone like you into the manor before, so we’d likely need to make special preparations of some sort."
    s "What sort of special preparations do you think “someone like me” would need, exactly?"

    scene toukahall10
    with dissolve

    to "Well, it’s...easy to get lost if you don’t understand where you’re going. So you would likely need a tour guide and-"
    s "You realize you could just show me around yourself, right?"

    scene toukahall11
    with dissolve

    to "Well...I would not mind that at all. But I feel as if my father and the house staff would be quite disappointed if they found me doing a job like that."
    s "Doing a job like that as opposed to?..."

    scene toukahall12
    with dissolve

    to "Studying to perfect both my academic and social skills."
    to "You know, those things I relocated to this side of the city to pursue only to be derailed by a rogue teacher."
    s "Hey, that’s me. I’m the rogue teacher."
    to "Yes. Yes you are."
    to "I do hope you’re proud of yourself, as you have somehow managed to make my otherwise simple and peaceful life into something out of a Saturday morning cartoon. "
    s "I’m surprised a girl of your “status” even knows what Saturday morning cartoons are."

    scene toukahall13
    with dissolve

    to "Did I say...cartoon?! I meant Saturday morning...golf program! "
    to "Those morning golfers...always causing a commotion for the...afternoon ones..."
    s "…"
    to "…"

    scene toukahall14
    with dissolve

    to "OKAY! GOODNIGHT!"
    s "Oh, come on. There’s no need to be embarrassed about not being seen as a proper lady for a minute or two."

    scene toukahall10
    with dissolve

    to "What in Heaven’s name are you saying, Sensei? Do you not realize who I am?"
    s "Of course I do, Tadako."

    scene toukahall15
    with dissolve

    to "Touka! Heir to the Tsukioka family’s fortune!"
    to "I can not risk losing yet another teacher due to my inability to maintain my composure and-"
    s "Yet another?"

    scene toukahall9
    with dissolve

    to "I...uhh..."
    to "{i}Hah...{/i}"
    to "How is it that you’re able to set me off so easily with nothing more than immature teasing?"
    s "Hold on, I’m curious about this apparent history of “losing teachers.”"
    to "Improper phrasing and spontaneous sentimentality. Please do not think much of it."

    scene toukahall7
    with dissolve

    to "I apologize for my sudden departure, but I just realized that I still have matters to attend to tonight."

    if toukastreets1 == True:
        to "But...if you’d still like to show me a little more about how things work on the outside world as we suggested before, you can always find me out and about early on the weekends."
    else:
        s "Sudden matters like what, exactly?"
        to "Matters you need not concern yourself with as they do not have anything to do with you, Sensei."
        s "Hold on, I-"

    scene toukahall16
    with dissolve

    to "I sincerely apologize, but I really can not talk any longer. "
    to "Goodnight, Sensei. Please do be careful on the way home. It is rather dark outside right now."

    scene black
    with dissolve

    "Touka disappears into her room and I’m left scratching my head in the hallway."
    "Io looks up at me from her spot on the floor and, without saying much of anything, exchanges a glance that essentially asks, “Why are you talking to {i}her{/i} of all people?”"
    "I shrug it off and ultimately hang out with Io instead for the next few minutes before finally deciding to head home."
    "I wonder what it is, if anything, that Touka so urgently needed to do tonight?"

    $ renpy.end_replay()
    $ toukafirsthall = True
    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasufirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label toukahall:
    if toukafirsthall == False:
        jump toukafirsthall
...
```