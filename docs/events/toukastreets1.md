# Trial Period
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukastreets1&go=Go)



## Event preconditions
✅Touka love greater than or equal to 0

✅Event "[Main: Horses or the Whispers of the Dead](./day304.md)" is completed (event=day304)



## Next events
None

## Event properties
* ID: toukastreets1
* Group: Touka
* Triggered by label: toukastreets
* Triggered by branch label: saturdaymorning

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukastreets1:
    scene sky
    with dissolve
    play music "marshmallow.mp3"

    "I decide to mix things up for a change and start aimlessly walking around the city as soon as I wake up."
    "Now, I’m sure you’re thinking that aimlessly walking around is kind of just my thing. "
    "But the whole “mixing it up” part lies in the fact that I normally can’t do that until I’ve at least let the day’s misery sink in."
    "But here I am, on a surprisingly sunny morning in the middle of winter, successfully avoiding that exact misery."
    "And hey, I don’t even think I’ll wind up running into Yumi this time around since I’m pretty sure she’s incapable of waking up this early."
    "I have absolutely nothing to base that on other than that she’s just Yumi."
    "But I’m pretty sure that alone is enough."

    to "Accept my money, blasted peasant drink dispenser!"

    scene toukavending1
    with dissolve

    "Oh, it appears I’ve run into the exact opposite of Yumi."
    "Not so much in attitude since both of them seem to vehemently dislike me on at least a surface level-"
    "And also not so much in terms of adaptability or socializing with their peers..."
    "Actually, now that I think about it, Touka and Yumi might have more in common than they realize."
    "Just one of them is poor and one of them is rich. So yeah."
    "But despite being rich, Touka seems to be fighting with a “peasant drink dispenser” or, as you and I would call it, a vending machine."
    "I should probably call out to her and see what the issue is..."

    s "Having trouble there?"

    scene toukavending2
    with dissolve

    to "Back away, heathen! This is my battle!"
    s "Well okay then. See you later."

    scene toukavending3
    with dissolve

    to "Wait! Stay."
    to "I need your help and I did not realize it was you who was approaching."
    to "What are you doing out and about so early?"
    s "I’d ask you the same thing."
    s "Actually, why are you walking around in general? Don’t you have a chauffeur to bring you to...random vending machines or whatever?"

    scene toukavending4
    with dissolve

    to "I do...but in an attempt to become one with society, Mother has asked that I explore the area and attempt to blend in."
    s "Well you’re doing a great job by yelling at a large appliance. Keep it up."

    scene toukavending5
    with dissolve

    to "How do I make it like my money?! It seems fundamentally simple, but it’s actually very confusing!"
    s "It’s really not. It’s probably just a bad bill or-"

    "Wait."
    "Touka is extremely out of touch with modern society."
    "This obviously means that I must take advantage of her."

    s "Did you say the chant?"

    scene toukavending6
    with dissolve

    to "I’m sorry, the what?"
    s "The chant. "
    s "These vending machines are voice activated and you need to talk to them or they won’t accept your money."
    to "Voice activated? But they look so outdated compared to the high-tech ones we have in our game room."
    s "I guess they’re a little- wait, you have vending machines in your house?"
    to "There are machines at the dorm as well. Are they not a standard appliance in commoner households?"
    s "They-"

    scene toukavending7
    with dissolve

    to "Wait! Before you answer that, please teach me the chant!"
    to "This is the furthest I’ve walked since my family's last vacation to Kyoto and I am beginning to become dehydrated!"
    s "Hmm...I wonder how it went again."
    s "Perhaps there’s something that could jog my memory."

    scene toukavending8
    with dissolve

    to "Are you...attempting to have me bribe you?"
    to "I may be extremely well off, but even I’m not willing to just hand out money if that’s what you’re implying."
    s "I also accept personal favors."

    scene toukavending2
    with dissolve

    to "Just tell me the chant, Sensei!"
    s "Fine, fine."
    s "First, you need to raise your right hand in the air as if you’re about to cast a spell on the machine."

    scene toukavending6
    with dissolve

    to "There is a visual element to this as well?"
    s "Yeah. These machines also double as security cameras, so they can see everything you do."
    to "How utterly terrifying. But I suppose if that is what must be done..."

    "I don’t know if I’m more impressed by Touka’s gullibility or my own ability to come up with such a fluid lie without even thinking."
    "Either way, this is awesome."

    scene toukavending9
    with dissolve

    to "Okay! I am now in position!"
    to "Will this do?"
    s "Yup. Perfect. "
    s "Now all you need to do is politely ask the machine to accept your money."
    s "If you want, you can just repeat after me."
    to "If you’d be so inclined, I would very much appreciate it."
    s "Then-"
    s "Hear my call, peasant drink dispenser."
    to "Hear my call, peasant drink dispenser!"
    s "I, Touma Tsukiyama of the Tsukiyama family-"
    to "I, {b}Touka Tsukioka{/b} of the Tsukioka family-"
    s "Ask for nourishment-"
    to "Ask for nourishment-"

    if bonus == True:
        s "And surrender my rights and my body to the man beside me."
        to "And surrender my-"
    else:
        s "And promise to call my teacher every night before he goes to sleep and tell him he is a good boy."
        to "And promise to-"

    scene toukavending10
    with hpunch

    to "WHAT DO YOU THINK YOU’RE MAKING ME SAY?!"

    "So close."

    scene toukavending11
    with dissolve

    to "Mmm..."
    s "Wait, are you crying?"
    to "I trusted you and you took advantage of me."
    s "I was just messing with you. There’s no reason to cry."
    s "Here, give me the money."

    scene toukavending12
    with hpunch

    to "AND NOW I AM BEING ROBBED! "
    to "MOTHER! HELP!"
    s "I’m not robbing you...I just want to see if there’s a problem with your money."

    scene toukavending13
    with dissolve

    to "Do you promise not to take it and run away?"
    to "On most days, my above average athletic ability would allow me to catch up with you, but my dehydration has made me very weak and I do not think I would be able to today."
    s "I’m not going to run away with one bill. I am not that poor, Touka."
    s "Also, what would it even matter if I did? You’re made of money."
    to "It’s the principle of it. I refuse to fail even during times like this. Tsukiokas always come out on top."
    s "Just give me the note, Touka."

    scene toukavending12
    with dissolve

    to "Fine! But only because you used the right name this time!"

    scene toukavending14
    with dissolve

    "Touka hands me the note she’s trying to use and, just as I suspected, it’s in too bad of shape for the machine to take it."
    "It’s actually so bad that I’m a little surprised someone of her status would even be carrying it."

    to "Is my money broken?"
    s "Where did you get this?"
    to "The tiny, yet surprisingly endowed girl in our class gave it to me when I bumped into her and asked her where I could purchase a drink just moments ago."
    s "Uta? I mean, it makes sense that her money would be in this condition, but why not just use your own?"
    to "I left my coin purse in my room out of fear that I may be attacked during my first ever walk among “the people.”"
    s "Why even leave your room if you’re so afraid of things like that?"

    scene toukavending15
    with dissolve

    to "The constant pressure to blend in and the strive for both your and my mother’s approval as a normal girl!"
    s "Wow. That was a surprisingly honest answer."

    scene toukavending16
    with dissolve

    to "I utterly despise lying and found no reason to in this situation."
    to "Just tell me my money is expired and I will be on my way. "
    s "…"
    to "…"
    s "{i}Hah...{/i}"
    s "Move over."

    scene toukavending17
    with dissolve

    to "I beg your pardon? Why should I have to give up my spot when I arrived first and-"

    scene black
    with dissolve

    to "Hey! What do you think you’re doing!"
    to "Help! I am being attacked!"

    "I move Touka aside and slip some of the coins in my pocket into the machine."

    s "What do you want?"
    to "Wait...are you-"
    to "..."
    to "Just a water is-"
    s "Green tea? Got it."
    to "Why even ask me if you’re just going to do whatever you please?!"

    "………"
    "……"
    "…"

    scene toukavending18
    with dissolve

    s "…"
    to "{i}Sip...{/i}"
    s "This is normally the part where you say “Thank you.”"
    to "…"
    to "{i}Sip...{/i}"
    s "Well fuck you then."

    scene toukavending19
    with dissolve

    to "Oh, stop. There’s no need for such hostility. I’m extremely thankful."
    to "I just believed that there may have been some sort of ulterior motive for a moment, so I was protecting myself."
    to "Without you, I would be significantly less hydrated. You have affected me greatly."
    to "Even if you directly ignored my plea for water in place of this...boxed tea beverage."
    s "Have you never had boxed tea before?"

    scene toukavending20
    with dissolve

    to "I have not. Our family has a tea master who lives at the manor, and he would abhor the idea of me drinking something like this."
    to "It is not nearly as bad as it looks, though. So I would like to thank you once more for making a choice that only appeared bad at first."
    s "You’re...welcome?"

    scene toukavending21
    with dissolve

    to "I...would not reject the idea of you coming to the manor to experience a proper tea ceremony, if that would at all repay you for your graciousness today."
    s "Well thank you for not rejecting it."
    s "That’s not really an invitation, though."
    to "R-Right! It is not."
    s "…"
    to "…"
    s "…"
    to "…"

    scene toukavending22
    with dissolve

    to "{i}Sip...{/i}"
    s "You feel pretty awkward right now, don’t you?"

    scene toukavending23
    with dissolve

    to "Do you not?"
    to "I’ve received plenty of private lessons from teachers in the past, but I have never sat with any of them so casually in public."
    to "Being seen out here makes me feel as if I’m...exposed. And having a...man beside me-"
    to "It feels rather immoral, does it not?"
    s "Not really. I spend most of my days surrounded by [teenage]girls, so I’m pretty used to it."
    to "Yes, but that’s on[school] grounds. It’s entirely different."
    s "Not always. You’ve literally seen me at the dojo with Ayane before."

    scene toukavending24
    with dissolve

    if bonus == True:
        to "Well...yes! But after hearing the things she has said about her...feelings for you, I have come to terms with your relationship being...different."
    else:
        to "Well...yes! But...she appears to like you as more than just a sparring partner..."

    s "…"
    s "I don’t know what she told you, but you’d probably be better off not believing it."

    scene toukavending25
    with dissolve

    to "I will do just that, but...it does not exactly remedy my discomfort."
    to "I realize that I’m likely just being reserved based on my own personal experiences and stigmas, but I can not exactly help it just yet."
    to "With your help, though...I can see myself getting at least partially better."
    s "I wouldn’t count on me too much. "
    s "Just keep being a weird rich girl and I’ll probably keep bumping into you out of a mix of coincidence and curiosity."

    scene toukavending26
    with dissolve

    to "Forgive me if I am misunderstanding, but the latter half of that made it sound as if you are interested in me."
    s "I am. "

    scene toukavending27
    with dissolve

    to "You are?"
    s "Sure. "
    s "You’re weird. It’s funny."
    to "I’m...funny?"
    s "That’s not exactly what I said, but okay. "
    to "I...I see."
    to "Well then...if we happen to bump into each other again on our respective morning walks...I wouldn’t mind doing more things like this."
    to "Since we are both curious about each others’ lifestyles, of course. Not because we’re interested in each other as {i}people{/i}."
    s "I don’t really need to know much about your lifestyle, but I wouldn’t mind showing you a little more about how “commoners” live."
    s "You should be aware that I’m probably going to mess with you a lot, though."

    scene toukavending28
    with dissolve

    to "Why?! What have I done to deserve this?!"
    s "Nothing in particular, but that’s just how things are going to be for a while."
    s "I show you the ropes. You say something unintentionally funny. I tease you about it."
    s "Everyone wins."
    to "This really doesn’t sound like an ideal student-teacher relationship to me..."
    s "The “ideal” part comes later. We’re still in the beginning phase."

    scene toukavending29
    with dissolve

    to "So...you are only acting this way toward me for the time being and will eventually become more of a traditional role model? "
    s "Sure. That’s one way to put it."

    "An incredibly wrong way to put it, but still one way."

    to "I see. So this would be what you would call a...trial period?"
    s "Call it whatever makes you comfortable. "

    scene toukavending30
    with dissolve

    to "A trial period it is, then..."
    to "Though, I have a lot more to learn than just figuring out how to operate various drink machines."
    to "So, if you’re willing to continue guiding me when it is convenient for you to do so...I’d be inclined to accept."
    to "I can’t say I’ll be particularly {i}happy{/i} about it since your methods are still rather confusing to me..."
    to "But I suppose that nothing has gotten {i}dramatically{/i} worse since I’ve started learning under you just yet."
    s "I’m sure it will. That’s normally how things go."
    s "But life without problems is no life at all."

    scene toukavending31
    with dissolve

    to "I suppose that much I’d have to agree with."
    to "The true hardships have yet to come. And I must be prepared for them when they do."
    to "Right now, I’m nothing more than a girl with a fortunate background. A background I must learn to live up to."
    to "And to do that...I require your assistance."

    scene toukavending32
    with dissolve

    to "Not right now, though, since I have plans with my mother and my sister to play shuffleboard on the yacht this afternoon."
    s "I don’t think that’s really something I can assist with, so that’s fair."
    s "I should probably be heading out anyway. I didn’t really expect to spend the entire morning re-educating a princess."

    scene toukavending33
    with dissolve

    to "Would it be too much to ask for you to not call me that?..."
    to "That word bothers me even more than your compulsion to keep addressing me by different names."
    s "Uhh...sure. I didn’t really mean it as an insult."
    to "Well, thank you for understanding then..."

    scene black
    with dissolve2

    "I get off the bench and move away from Touka."
    "I turn back after a few seconds to see if she’s leaving as well, but she remains still-"
    "Sipping on her box of peasant liquid (Which I’m sure is what she’s calling it in her head) and staring off into the distance..."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukastreets1 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label toukastreets5:
...
```

## Code that triggers this event
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukastreets:
    if touka_love >= 0 and toukastreets1 == False:
        jump toukastreets1
...
```