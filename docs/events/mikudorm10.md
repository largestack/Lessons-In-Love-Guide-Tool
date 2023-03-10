# You and Me and the Night (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 10

* Event [Nightvision](./soccer10.md) (Miku) is completed)



## Next events

* [Main: Parasite](./day83.md)
* [Miku: Hormones Running Wild](./soccer15.md)
* [Miku: Moments Like This](./mikudorm15.md)

## Event properties

* Id: mikudorm10
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm
* Triggered by path: mikudorm->mikudorm10

## Official wiki page

[You and Me and the Night](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm10:
    play sound "knock.mp3"
    stop music fadeout 5.0

    "I hold my breath as I knock on Miku’s door."
    "I don't mean to, but I do."
    "I haven’t had a chance to talk to her one-on-one since the episode in the storage room and..."
    "In fact, approaching her at all has started to make me feel a bit uneasy."
    "I still don’t even understand what happened. That entire morning is just a blur to me, looking back on it now."
    "If something is actually wrong with Miku...I should at least try and figure out what it is...shouldn't I?"
    "I can't guarantee I'll be able to do something about it, but..."
    "I should at least {i}know.{/i}"

    s "..."

    play sound "knock.mp3"

    "I knock again."
    "I know she's in there."

    mi "Um..."
    mi "Hello?"
    s "It’s me. Can I come in?"
    mi "Sensei?...You're here?..."
    mi "But...why?"
    s "Why do you think? Just let me in."
    mi "I mean...are you sure you wanna?"

    "I can hear Miku speaking from right behind the door. I’m guessing she wasn’t expecting me to show up and talk about anything so soon after the incident."

    s "Did you think I was just going to start ignoring you or something?"
    mi "Maybe...I did kinda freak out on you, so..."
    s "Are you going to freak out on me if I come inside?"
    mi "Huh? Of course not. You haven’t done anythin’ wrong."
    s "Then let me in before someone in the hall catches onto our secret friendship."
    mi "I...uhh..."
    mi "Okay..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene mikupjs1
    with dissolve2
    play music "undersea.mp3"

    mi "..."
    s "Hey. How are you doing?"
    mi "You're not...gonna just pretend that none of that stuff in the storage room ever happened, are you?..."
    s "Maybe. Depends on what you think we should do."
    s "Did you want to talk about it? Because, as it stands, I am very confused."

    scene mikupjs2
    with dissolve

    mi "It’s not like I don’t wanna...I just don’t really know {i}how.{/i}"
    mi "There's a lotta...bad stuff about me that I don’t like bringin’ up...so I do my best to keep it locked away, I guess..."
    s "I’m not going to ask you to talk about anything you don’t want to talk about."
    s "If you want to just hang out and pretend it never even happened, that’s fine with me as well."

    scene mikupjs3
    with dissolve

    mi "Do you...really not hate me for yellin' at you like that?..."
    s "Even though I have no idea what caused it, I understand that you weren't yelling {i}at{/i} me. I just happened to be there."

    scene mikupjs4
    with dissolve

    mi "Oh man...that's such a relief..."
    mi "I was really worried that I mighta screwed everythin’ up just when we were startin' to get close."

    scene mikupjs5
    with dissolve

    mi "I, uhh...I ain't ever been friends with someone your age before."
    mi "So I was kinda worried you were gonna think I was just some immature loser or somethin’."
    s "Miku. Listen to me."

    scene mikupjs5r
    with dissolve

    mi "Y...Yeah?"
    s "..."
    mi "..."
    s "You {i}are{/i} an immature loser."

    scene mikupjs6
    with dissolve

    mi "Huh?! What is this, some kinda setup?!"
    mi "I let you in and you use it to just make fun of me?!"
    s "Of course not. You didn’t let me finish."
    s "I like you {i}because{/i} you’re an immature loser."
    mi "So you {i}are{/i} here to make fun of me?!"
    s "Again, no. There’s nothing wrong with being immature."
    s "You’re hyperactive and overly friendly....You’re enthusiastic about everything even though you have a hard time keeping up with certain topics."

    scene mikupjs3
    with dissolve

    s "You’re excitable and spontaneous and a bunch of other things that sound annoying in large doses but, somehow, none of them are."
    s "That’s exactly what I like about you."
    mi "Sensei..."
    s "But there is {i}nothing{/i} immature about whatever happened to you in the storage room."
    s "At all."
    mi "..."
    s "So it’s okay. You don’t need to worry about it."
    s "Some things are just beyond our control."

    scene mikupjs7
    with dissolve

    mi "How the heck are you able to say all this embarrassin’ stuff with a straight face?"
    mi "Especially when we still barely even know each other..."
    s "We were in the process of learning, though, weren't we?"
    mi "We were...but now that the cat's out of the bag and there's clearly some stuff that isn’t easy for me to talk about, you’d probably have an easier time cozyin’ up to Makoto."
    mi "At least when {i}she{/i} yells at you, you know it’s cuz’ you forgot your homework or somethin’."
    s "I don’t have homework. I’m the teacher."

    scene mikupjs5
    with dissolve

    mi "You know what I mean!"
    mi "I just don’t wanna make things all complicated for ya when you’ve already got a bajillion other girls comin’ to ya with their problems."
    mi "'Specially when I'm too much of a scaredy cat to even talk about mine."
    s "Like I said, I’m more than happy to pretend those problems don’t even exist. I do the same thing more often than not."

    scene mikupjs7r
    with dissolve

    mi "You...have problems like that too, Sensei?..."

    play sound "static.mp3"
    scene everythingg with flash
    scene happy7 with flash
    scene everythingg with flash
    scene happy7 with flash
    scene everythingg with flash
    scene happy7 with flash
    scene mikupjs7r2 with flash
    stop sound

    s "{s}You are the only one who's broken. I am simply here to fix you.{/s}"

    play sound "static.mp3"
    scene mikupjs7r with flash
    stop sound

    s "Everyone has problems. And I'd wager that most people run from them instead of confronting them head on."
    s "You're good at running, aren't you? Just try running faster if they keep catching up to you."
    mi "Try running...faster?..."
    s "That's not me trying to rush you, either."
    s "I just don't want you to break."
    mi "…"
    s "…"
    mi "Can I hug you?"
    s "Of course..."

    scene mikupjs8
    with fade

    "Miku wraps her arms around me softer than she did the last time we were at the soccer field."
    "I guess this is what it feels like to actually be embraced by her rather than used as some sort of makeshift weightlifting prop."
    "Call it the situation we've found ourselves in, but she seems much more fragile up close now that I can feel her."
    "The idea of snapping her in half is all I can think of- and the sensation of her growing body pressing against mine backs me into a corner."
    "For a moment, I even forget all of the other horrible things caught between us in the embrace."

    mi "Is this a weird time for me to ask ya to be our coach again?"
    s "Kind of, yeah."
    mi "Darn. I thought I might be able to play up the vulnerable thing and convince ya that way."
    s "I’ll agree sooner or later. You just need to keep bothering me about it."
    mi "I plan on it. A few of the girls could use some of those magic hands of yours. Myself included."

    scene mikupjs9
    with dissolve

    mi "Mm!~"

    "I squeeze Miku’s shoulders lightly and she quivers in response."

    mi "I...didn’t mean right now, you know?..."
    s "Why not? It felt good, didn't it?"
    mi "Heck yes it felt good...but I’m also in my PJ’s and...not in the right mindset to get a massage right now."
    s "You sure? It might help you relax a little."

    scene mikupjs10
    with dissolve

    mi "Save it for the field, coach."

    "I stop squeezing and immediately feel Miku's body relax and slope further into mine."
    "It's fascinating how delicate she seems despite the countless hours she spends conditioning her body."
    "I'm sure a lot of that is due to the immense size difference between us, but..."
    "Even if she were a foot taller...I somehow doubt it would change anything."
    "And even though she’s talking the same way she normally does and {i}acting{/i} the same way she normally does-"
    "She feels entirely new."
    "There’s much more to Miku that I’ve yet to learn. And I have no idea {i}when{/i} I will be able to learn it."
    "But if the things we don't know about each other give us an excuse to be together like this, I’m glad."
    "I'll remain in the dark for as long as it takes."

    mi "You doin' okay? Looks like ya got caught up in thought for a sec."
    mi "D’ya not like hugs or somethin’?"
    s "They’re okay I guess. I’m just trying to not move too quickly out of fear of snapping you in half."
    mi "I'd like to see you try. I'm a lot stronger than I look, Sensei."
    mi "I’ll arm wrestle ya right now, Sensei. You better watch out."
    s "I’m absolutely terrified, Miku."

    "Miku grabs my shirt and pulls herself closer with a bit more fervor this time."
    "I'm surprised by her willingness to do so on account of me being {i}very{/i} aware throughout this entire conversation that she's not wearing a bra-"
    "But I guess that sort of thing just doesn't pop into her mind the same way it does mine."
    "That's good."
    "It means there's still some hope left for her."

    mi "You know, Sensei...you might be twice my size, but I’ve got four times the willpower you do. And that's the X factor in helpin' anime characters win fights."
    s "Yeah, there is absolutely no way that is true. I should receive an award for the amount of willpower I have on display right now."
    mi "No way, Jose. Miku Maruyama's the real protagonist here and she's gonna take you down one day after a lengthy training arc."
    s "Why are we even fighting? Can't we just keep hanging out?"
    mi "You said you were gonna snap me. I've got a right to defend myself."
    s "If your method for defending yourself involves clutching my shirt and hugging me, you might want to start your training arc early."

    scene mikupjs8
    with dissolve

    mi "Nah. You’re in trouble as long as I’ve got a hold on you."
    s "And...how long do you intend to hold me, exactly?"
    mi "For as long as you'll let me."
    s "..."
    mi "..."

    scene black
    with dissolve2

    "Despite her final line before a bout of silence, Miku eventually lets go without me having to ask her to."
    "It's good that she does, too, because I wasn't sure how much longer I was going to be able to take that for without doing something I may regret."
    "As our bodies part, she takes a moment to collect herself and breathes in deeply- like she's getting ready for a fifty-yard dash."
    "But, instead of taking off down the hall in a sprint, she simply turns to me instead."

    scene mikupjs3
    with dissolve

    mi "I’m...sorry again for yellin’ at you, Sensei. If it makes ya feel any better, I'll let you yell stuff at me sometime."
    s "That won’t be necessary, but thanks."
    mi "You sure? I can take it. I swear."
    s "I’m not going to yell at you, Miku..."

    scene mikupjs7
    with dissolve

    mi "Fine...but if ya ever change your mind, you know where to find me!"
    mi "And if I’m not here, you can always...check the soccer field or...the streets or....anywhere else that’s good for runnin’."
    mi "Oh! And umm...speakin’ of which, we should totally go for a run together soon."
    mi "Just think about it! The wind in our faces! The sweat drippin’ from our pores!"
    mi "Just you and me and the night!"
    s "That sounds great other than the sweat part. And the wind part."
    s "And the running part."
    s "Actually, all of that sounds pretty bad."
    mi "Well, I’ll get ya into it! I swear!"
    mi "You’ll be trainin’ for the Hakone before ya even know it!"
    s "Whatever you say, Miku..."

    scene black
    with dissolve2

    "The two of us say our goodbyes and Miku jumps into my arms for another hug."
    "Part of me wants to hold her longer, but the time we've had is enough for today."
    "I still don’t understand the extent of whatever Miku’s issues are, so I want to be careful to not hurt her any more than she’s already hurting."
    "{i}If{/i} her pain is worth worrying over in the first place."
    "With the way she normally acts, it’s hard to tell."
    "I make my way back into the street and, for a moment, contemplate whether or not I want to try jogging."

    $ renpy.end_replay()
    $ mikudorm10 = True
    $ miku_love += 1
    stop music fadeout 8.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
...
```