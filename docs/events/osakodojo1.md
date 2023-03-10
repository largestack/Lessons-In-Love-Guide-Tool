# Floating Forever, Unfulfilled (Osako)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Osako love greater than or equal to 1

* Event [Pressure Point](./osakodate1.md) (Osako) is completed)



## Next events

* [Main: Good Morning](./secondbeach1.md)

## Event properties

* Id: osakodojo1
* Group: Osako
* Triggered by label: osakodojo
* Triggered by branch label: saturdayafternoon
* Triggered by path: saturdayafternoon->osakodojo->osakodojo1

## Official wiki page

[Floating Forever, Unfulfilled](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=osakodojo1&go=Go) for more details.

## Event code

File: (install folder)\game\OsakoEvents.rpy

Code:
```python
...
label osakodojo1:
    scene osakokicksyourass1
    with dissolve2
    play music "rapid.mp3"

    "So, it appears that today is the day I die."
    "I knew that visiting Osako at the dojo would be a bad idea after her parting words to me the night of her anniversary were that she was going to activate one of my apparently fatal pressure points."
    "But, of course, I’ve always been bad when it comes to warnings. "
    "And even worse when it comes to staying away from cute girls."
    "And now, apparently girls who don’t even like men to begin with."
    "So yeah, no idea how I wound up in this mess if not for taking too many directions from my penis."

    s "I’ll give you one last chance to step down, Osako. "
    s "I am bigger than you. That must be good for something."

    scene osakokicksyourass2
    with dissolve

    os "Is this why you never want to actually practice? Because you’re scared?"
    os "Or are you just feeling a little vulnerable because Ayane isn’t here to protect you today?"

    scene osakokicksyourass1
    with dissolve

    s "I don’t need Ayane’s protection. I’m just saying that any rational person would look at this matchup and assume that {i}I{/i} am going to win."

    scene osakokicksyourass2
    with dissolve

    os "I’ll admit that you’re in surprisingly good shape for someone who despises any amount of physical activity."
    s "That’s not true. I love-"
    os "Don’t say it."
    s "Damn it."
    os "Listen, dude. You can talk all the smack you want, but if you think for a second that I am not going to knock you on your ass, you are sorely mistaken."
    s "In that case, is it too late to back out?"

    scene osakokicksyourass3
    with dissolve

    os "Yup. The least you can do in exchange for taking up a spot on the roster is letting me kick your ass once or twice every few months."
    s "No worries, I’ll just quit the dojo instead then. Thanks for all of your hard work up until now."
    os "You can’t quit. Your story with Ayane hasn’t finished yet. "
    os "Aren’t you guys trying to like, take back Kumon-mi or something?"
    s "Why do you know about that? And why can I hear the background music for it right now?"
    s "You’re not...part of the Amamiya army, are you?"

    scene osakokicksyourass4
    with dissolve

    os "The what?"

    "She must be a spy."
    "Or, even worse...an assassin sent by Ayane to take me down and reclaim the land that her family is owed or...something."

    scene osakokicksyourass5
    with dissolve

    s "Pretend you’re not a part of this all you like. I know that you’re with {i}them{/i}."
    os "Wait, are you actually into that whole roleplaying thing after all?"
    os "This whole time I thought you were just playing along to make Ayane happy."
    s "That’s precisely what I {i}wanted{/i} you to think."

    scene osakokicksyourass6
    with hpunch

    s "Because that means you’ve let your guard down!"

    scene osakokicksyourass4
    with dissolve

    os "…"
    s "…"
    os "Do you..."
    os "Do you expect me to also become a part of this now?"

    scene osakokicksyourass1
    with dissolve

    s "I expect you..."

    scene osakokicksyourass6
    with hpunch

    s "To die!"

    scene black
    with dissolve

    "I gather every last bit of energy in my body and charge at Osako with an ultimate attack."
    "One that’s sure to-"

    s "Wait...impossible!"

    play sound "static.mp3"
    scene osakokicksyourass7 with flash
    stop sound

    os "You know, I was going to say something like “Try and hit me if you can,” but you just went right ahead and attacked me without even getting the signal."
    os "You’re pretty ballsy for a complete wuss, huh?"
    s "Let go of my hand."
    os "And then what? Let you attack me?"
    s "You interrupted my strongest move."

    scene osakokicksyourass8
    with dissolve

    os "If {i}this{/i} is your strongest attack, you really should start paying a little more attention to my lessons."
    os "There’s a lot I can teach you if you actually open up your mind, you know."
    os "For example, do you want to know how I was able to predict the exact motion of your fist before it even reached its halfway point?"
    s "Is it because I’m a complete novice?"
    os "That’s definitely part of it!"
    os "In fact, for the sake of today’s exercise, we can even say that’s {i}all{/i} of it."
    os "While competitive karate does exist and is pretty fucking awesome, it doesn’t take away from the fact that it’s still an art of self defense at its core."
    os "If someone attacks you on the street, it’s probably safe to assume that they aren’t a trained fighter who knows how to counter things like this."
    os "So as long as you’re able to predict their actions before they make them, you have the upper hand."
    s "Cool. Can I have my hand back now? I want to try hitting you again."
    os "No. Because now it’s {i}my{/i} turn to hit you."
    os "But since I’m so nice, I’ll let you know how I’m going to attack and {i}where{/i} so you can try and block it."
    s "As if I’d fall for that. You’ll just attack whatever place you tell me {i}not{/i} to protect."
    s "I know your games, assassin. "
    os "No, no. Really. I mean it."
    os "I’m going to push back on your fist and then attack you from above with a kick."
    s "What? But how are you going to attack me from above when-"

    scene osakokicksyourass9
    with dissolve

    os "HA!"
    s "Wait, what?"

    scene osakokicksyourass10
    with hpunch

    "Osako connects with the side of my neck and I can instantly feel my body beginning to go limp."

    s "Was that..."

    scene osakokicksyourass11
    with dissolve

    os "One of seven ways I know how to kill you in one blow."
    os "Tell me how the ground tastes, would you?"
    s "I..."

    scene black
    with dissolve
    play sound "thump.mp3"

    "I hit the ground without even getting a chance to reach out and break my fall with my hands."
    "My body is no longer capable of moving."
    "I really am going to die today, aren’t I?"

    scene osakokicksyourass12
    with dissolve2

    s "Ngh..."
    s "Even though you told me...exactly where I’d be attacked...I couldn’t do anything about it..."

    scene osakokicksyourass13
    with dissolve

    os "Couldn’t? Or {i}didn’t{/i}?"

    if bonus == True:
        os "Because it seemed like you were too busy admiring how flexible I am to block where I told you to block."
        s "So many...possible positions..."
    else:
        os "Because it seemed like you were too busy thinking about hugs or something to block where I told you to block."
        s "They are just so warm"

    scene osakokicksyourass14
    with dissolve

    os "Hah...really, man. All you need to do is just listen to me and you can {i}actually{/i} become better at this. "
    os "I’m trying to actually help you out with your technique right now, and I can’t do that if you’re down there on the floor."
    s "It doesn’t look like you’re helping me."
    os "I told you what to do and you didn’t do it. Don’t go blaming me for your inadequacy or disinterest."
    os "Now get back up and fight me like a real man or I’ll have to show you where your other six pressure points are."
    s "I...don’t think I can move my body."

    scene osakokicksyourass13
    with dissolve

    os "Sure you can. I didn’t kick you {i}that{/i} hard. "
    s "No...I really-"

    scene osakokicksyourass15
    with dissolve

    s "Ngh-"
    os "Blah blah blah. I’m a weak little bitch who can’t even take one kick from a girl."
    s "Just...put me out of my misery already..."
    os "Are you Wakana now?"
    s "If I say yes...can we make out?..."

    scene osakokicksyourass16
    with hpunch

    s "Ngh!"
    os "You think I’d ever kiss someone as weak as you?"
    s "There is no way...Wakana is stronger than I am..."

    if bonus == True:
        os "True. But Wakana is a beautiful woman and you’re just some perverted lowlife. "
    else:
        os "True. But Wakana is a beautiful woman and you’re just the huggy boy. "

    s "Why is your...foot stronger than my entire body?"
    os "Hm? "
    os "Oh. I used to kickbox before starting karate, so I’ve always considered anything involving legwork my speciality."
    os "How else would I have been able to sink my heel into one of your pressure points without even trying?"
    s "Can I...have my head back now?..."
    os "That depends. Are you going to try and kiss me?"
    s "Not if it means experiencing this level of pain again."
    os "Then sure."
    os "I’ll even go get you a drink as a personal thank you for actually making an effort today."
    os "Even if that effort was entirely worthless."
    s "You are...much scarier than I thought you were..."

    scene black
    with dissolve2

    "Osako removes her foot from my head and I can slowly but surely feel the world begin to solidify beneath me."
    "My legs, which had been as gelatinous as the soup I made with Wakana nights before, stop wobbling and, before long, I’m able to get them to stand upright again."
    "I take another minute or so to fully regain consciousness and manage to open my eyes once I see Osako coming my way with a bottle of water."

    scene osakokicksyourass17
    with dissolve

    os "Uhh...why did you flinch? I’m just bringing you a drink."
    s "I think it was a reflex."
    s "This might just be how I have to act around you from now on."
    os "Oh, stop. I used that same kick on Ayane and she got up in like fifteen seconds."

    if bonus == True:
        "Yes but she also cried the first time I put my penis inside of her, so I know deep down that I’m stronger."

    scene black
    with dissolve2
    stop music fadeout 13.0

    "I take the bottle of water from Osako and quickly rehydrate myself."
    "Not because I want to continue training, but because if I don’t, I’ll likely pass out and be stomped on once more."
    "And while there are plenty of people out there who I am sure would love such a thing...I am very much not one of them."
    "Osako follows me to the side of the room and leans up against the wall beside me, sparing my life for at least another several minutes."
    "Or at least that’s what I {i}would{/i} think..."
    "If she wasn’t an Amamiya family assassin."

    scene osakokicksyourass18
    with dissolve

    s "…"
    os "…"
    s "…"
    os "…"
    os "What?"

    scene osakokicksyourass19
    with dissolve
    play music "sakuya4.mp3"

    s "Hah..."
    s "Nothing."
    s "I can see now why Touka’s family wanted to hire you personally."
    os "That’s not something you could possibly know after like, one tenth of a sparring match."
    os "If I was actually trying, you really would be dead right now."
    os "Like, that’s not even a joke."

    scene osakokicksyourass20
    with dissolve

    s "Why subject yourself to {i}this{/i} then?"
    s "Everyone here has little to no experience at all. Don’t you ever get bored having to teach people that are so...below you?"
    os "Don’t you?"
    os "Wakana says you’re pretty smart."
    os "You even recognized that Lord Byron poem I memorized for her when I confessed. "
    s "First off, Wakana specifically made a point of how recognizing things like that doesn’t make you smart."
    s "And secondly, that is adorable."

    scene osakokicksyourass21
    with dissolve

    os "Isn’t it?"
    os "A lot of people are surprised to hear that I’m actually into a lot of gothic stuff as well and that I’m not just dating Wakana because of that whole “opposites attract” thing."
    os "Like yeah, that applies to our personalities and styles, but we share a ton of the same interests and-"

    scene osakokicksyourass22
    with dissolve

    os "And now I’m going to start ranting about her again because I love her so much."
    s "…"
    os "…"
    s "You never answered the question."

    scene osakokicksyourass23
    with dissolve

    os "Was there a question? I zoned out when we started talking about Wakana."
    s "I asked you why you bothered teaching here since you’re so much better than everyone."

    scene osakokicksyourass24
    with dissolve

    os "Ahh, right. Right."
    os "I don’t know, really. "
    os "There aren’t enough advanced martial artists in Kumon-mi for me to make a living off of instructing them, so I guess I just followed where the money was."
    os "It’s not like this was my first choice or anything. I had much bigger plans. "
    os "Just...can’t really do anything about them anymore."
    s "What kind of plans are you talking about?"

    scene osakokicksyourass25
    with dissolve

    os "Competitions...getting better myself instead of helping others get better."
    os "Always wanted to try doing something on a national level because I’m definitely good enough."
    os "But now that no one’s allowed to leave Kumon-mi, that path just...isn’t possible anymore."
    os "And it doesn’t seem like it’s going to be opening back up anytime soon, so..."

    scene osakokicksyourass26
    with dissolve

    os "…"
    os "So I’ll very likely be a little too old to compete whenever it {i}does{/i}."
    s "Even if it’s a few years, I doubt it would matter-"
    os "It matters."
    os "The most important resource for pretty much all athletes is our age."
    os "Every year counts. And when your “prime” is limited to such a small window of your life, everything you do winds up getting centered around that."
    os "Then, once it’s gone, it’s all downhill and you’ve just gotta...figure out other shit to do."
    os "So even if it is only a few years, each one of those years will matter."

    scene osakokicksyourass27
    with dissolve

    os "Or {i}would{/i} matter...since chances are that’s not happening and that I’ll be stuck teaching beginners until I can’t move my body anymore."
    s "…"
    os "…"

    "I wonder if it’s okay to provide someone false hope even when you know things aren’t going to work out for them?"
    "Obviously, Osako has no idea that time is being reset every few months and that she’ll likely remain in the same limbo her significant other is caught up in-"
    "But I wonder if it’s okay to pretend that’s not the case."
    "To throw a few scripted words of false sincerity at her in hopes that she’s naive enough to eat them up."
    "I guess it’s worth a shot, right?"

    s "I wouldn’t give up just yet."
    s "For all we know, the city could open back up tomorrow and you could board the first flight to...wherever they do karate stuff."

    scene osakokicksyourass28
    with dissolve

    os "Yeah..."
    os "Maybe that will happen."
    os "Or maybe it won’t."
    os "I shouldn’t dwell on it either way."
    os "If things do make a turn for the better, that’s definitely the path I’ll wind up walking."
    os "But for now...I’m happy just walking beside my girlfriend and supporting her."
    s "..."
    os "..."
    s "Are you about to start talking about Wakana again?"
    os "God, she’s so fucking cute. I can’t stand it."

    scene black
    with dissolve2

    "It’s rather unfortunate that I’ll never get to see Osako kicking someone to death on live television."
    "But it {i}is{/i} fortunate that I’ll get to spend more time with her."
    "An unlimited amount of it, too."
    "Who would have thought that someone who’s been {i}this{/i} close to me ever since I arrived in Kumon-mi would suddenly become an actual character in {i}my{/i} story?"
    "And I in hers. "
    "We all have our own dreams...goals...desires..."
    "And most of them will float forever, unfulfilled."
    "But some of us are fortunate enough to learn this beforehand."
    "To create new goals that we can accomplish within shorter amounts of time."
    "And use that manipulation of the laws of the universe to survive or grow."
    "Then, sooner or later-"
    "We’ll have everything we’ve ever wanted."
    "The fortunate ones, I mean."
    "Everyone else?"
    "Well-"
    "Maybe they’ll be rewritten into someone with a little better luck?"

    $ renpy.end_replay()
    $ osako_love += 1
    $ osakodojo1 = True
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label osakodate15:
...
```

## Code that triggers this event

File: (install folder)\game\OsakoEvents.rpy

Code:
```python
...
label osakodojo:
    if osako_love >= 1 and osakodojo1 == False:
        jump osakodojo1
...
```