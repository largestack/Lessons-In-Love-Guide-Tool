# First and Second
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dojo30&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 30

✅Event "[Ayane: Cold Air of an Encroaching Winter](./ayanedorm25.md)" is completed (event=ayanedorm25)



## Next events
* [Ayane: Crazier Things Have Happened](./ayanedorm30.md)

## Event properties
* ID: dojo30
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo30:
    scene ayanetoukadojo1
    with dissolve
    play music "sakuya4.mp3"

    "Ayane and I are resting for a bit after actually spending the afternoon training."
    "Given that we’ve been spending most of our recent days messing around and playing with her chicken (Which is apparently not allowed in the dojo), we figured it was about time to actually try."
    "That and the instructor has been getting on our case about taking things seriously or we’ll be removed from the class."
    "To be honest, I wouldn’t mind being kicked out since it would mean less time physically exerting myself...but Ayane likely would, so I’ve been bearing with it for her sake."
    "And yes, I can be nice like this every once in a while if I actually apply myself."

    ay "Sensei! Did you see my sweet dropkick earlier? I almost landed a hit on the instructor!"
    s "Yes. And I also saw you get scolded shortly after for using a pro-wrestling style dropkick in karate class."

    scene ayanetoukadojo2
    with dissolve

    ay "Hey, if it works, it works."
    s "It didn’t work, though."
    ay "Yeah, but neither does normal karate so I was trying to improvise."
    ay "It's not my fault Miss Osaka is some kind of martial arts goddess."
    s "I didn’t say that was your fault. I’m just saying you might want to start using, you know, {i}karate{/i} moves if you ever plan on getting better at karate."

    scene ayanetoukadojo3
    with dissolve

    ay "Guh. Maybe we should just take up pro-wrestling instead? Especially with all of those rumors floating around about the place being sold and stuff."
    s "Those are {i}still{/i} going around?"

    scene ayanetoukadojo4
    with dissolve

    ay "They haven’t even slowed down. "
    ay "I tried asking Miss Osaka about it the other day and even she wasn’t sure what was going on."
    ay "She doesn’t even know if she’ll be allowed to keep her job, so I told her I’d ask my dad about hiring her as my personal instructor if things really came to that."
    s "Is this really what you want to keep on doing? You're not going to, like...move on or something?"

    scene ayanetoukadojo1
    with dissolve

    ay "Do you remember the first time you showed up here, Sensei?"
    s "I am reminded every time the instructor makes fun of me for not paying my own membership."
    ay "There's no shame in having a sugar mama, Sensei."
    s "Yes there is and please don't call yourself that."
    ay "Anyway, it might sound a little silly...but I think it may have been fate that led you here."
    ay "So unless there’s some sign that descends from up above telling me that I should stop doing karate, I’m going to keep going."
    ay "Besides, even if I’m using American wrestling moves, I’ve definitely been feeling way better physically lately."

    if bonus == True:
        ay "My body’s actually in such good shape that pretty soon, I might be able to pull off some super crazy sex moves."
        s "I’m quite interested in finding out what sort of {i}super crazy sex moves{/i} derive from amateur karate lessons."
    else:
        ay "It is probably due to all of the steroids I am on."
        s "What?"

    scene ayanetoukadojo5
    with dissolve

    ay "They’d probably be easier for you to understand if you actually practiced every once in a while."
    s "What do you think I was doing today? I very clearly practiced."

    if bonus == True:
        ay "For three minutes, sure. After that, you just sat around and stared at all of the other girls’ butts."
        s "I was practicing my observational skills- one of the key fundamentals of karate."

        scene ayanetoukadojo6
        with dissolve

        ay "Well observe {i}me{/i} more next time instead of everybody else or I’ll be forced to become a martial arts master and eliminate all of them."
    else:
        ay "You call that practice, you little shit? Drop and give me twenty."
        s "But twenty is so many."

    scene ayanetoukadojo7
    with dissolve

    rlg "Pardon me, you two, but would either of you be willing to spare a moment of your time?"
    rlg "I’d like to ask you a few questions about this establishment, if you don’t mind."

    scene ayanetoukadojo8
    with dissolve

    ay "Hm? Who’s that?"
    s "No clue. She looks really...elegant, though."

    scene ayanetoukadojo9
    with dissolve

    ay "And I don’t?!"
    s "Not really. Her rich-girl aura is much stronger than yours. Especially considering you’re wearing a karate uniform."
    ay "It’s called a {i}Karategi{/i}, Sensei! Pay attention in class!"
    s "But there are just so many butts to look at."
    rlg "Umm...hello? Can you not see me?"
    rlg "Is there some sort of...karate code barring you from speaking with people dressed in normal attire?"

    scene ayanetoukadojo10
    with dissolve

    ay "Oh, no. Sorry."
    ay "You can come talk to us as long as you promise not to steal this man away from me."
    rlg "I have no intention of that whatsoever. He seems rather brutish in nature."
    s "You know, maybe it would be better if you two just spoke in private. I’m clearly not needed here."

    scene ayanetoukadojo11
    with dissolve

    ay "Oh, stop. You know I need you every minute of every day...Every day of every year. Every-"
    rlg "Every year of every decade."

    scene ayanetoukadojo12
    with dissolve

    ay "…"
    s "…"
    rlg "Oh, sincerest apologies. I thought we were playing a game."
    rlg "You’ll need to forgive me. I don’t typically converse with the middle class and may say some things that are quite hard for people of your kind to understand."
    ay "Middle class? But I’m not middle class at all."
    ay "I have the second largest house in Kumon-mi. We even have a room that's literally just a giant ball pit."
    s "What? Since when?"

    scene ayanetoukadojo13
    with dissolve

    rlg "The second largest..."
    rlg "Then that must mean-"

    scene ayanetoukadojo14
    with dissolve

    rlg "You wouldn’t happen to be Ayane Amamiya, would you?"
    ay "That's my name!"
    ay "But...who are you exactly? You've yet to introduce yourself."

    scene ayanetoukadojo15
    with dissolve

    rlg "Oh my, where are my manners?"
    to "My name is Touka Tsukioka- daughter of Tomonori Tsukioka and planned heir of the Tsukioka Foundation. It’s wonderful to finally meet you."
    ay "Nice to meet you too! Judging by your clothes, I’m guessing you’ve got an even bigger ball pit than I do."
    to "Ball...pit?"
    ay "It's like a swimming pool full of plastic balls."
    to "How wonderfuly creative. My family prefers to fill our pools with water. It had not occurred to me until today that there were other options available."
    ay "You don't get out much, do you?"

    scene ayanetoukadojo16
    with dissolve

    to "And you are? A butler perhaps?"
    ay "Oh, that’s my teacher. And future husband."

    scene ayanetoukadojo17
    with dissolve

    to "I beg your pardon?"
    ay "He's my future husband, I said. We're going to get married and have a disturbing amount of children one day."
    to "Future husband? This man?"
    to "You’ll have to forgive me if this is some sort of joke I’m not picking up on, but he seems rather...unfitting. Don’t you think?"
    s "That's fair. But also kind of rude."

    scene ayanetoukadojo18
    with dissolve

    ay "Woah- hold on a second. I don’t care {i}how{/i} rich you are, no one talks down to Sensei in front of me. And {i}definitely{/i} no one questions whether he and I are meant to be together."

    "I can think of at least eleven other girls who question that off the top of my head."

    to "Oh dear, I’m terribly sorry. I didn’t mean to offend."
    to "I just assumed you’d be getting married to someone of slightly higher status to propel your family’s name forward."
    to "But, perhaps...that’s just the way my family handles things? If so, I humbly ask for forgiveness."

    scene ayanetoukadojo19
    with dissolve

    ay "Uhh...it’s fine, just..."
    ay "What’s up? Why did you need to talk to us?"

    scene ayanetoukadojo20
    with dissolve

    to "Oh, yes. I was actually just looking to speak with some of the common folk who use this dojo about their feelings for it."
    to "You see, I’ve recently taken an interest in martial arts and have been looking into acquiring an establishment like this one for my own personal use."

    scene ayanetoukadojo21
    with dissolve

    to "Of course, it’s overwhelmingly clear that a large amount of work must be done in order to bring it up to my family's standards-"
    to "So hearing about the condition of the building from people who are here regularly would provide some much-needed peace of mind."
    ay "Wait...hold on...{i}You’re{/i} the one who’s planning on buying this place out?"
    s "I don't mean to brag, but I kind of saw that one coming."

    scene ayanetoukadojo22
    with dissolve

    ay "I didn’t! I thought she was just here to try out the class or something!"
    to "Oh, heavens no. I could never practice in a place like this given its current state. Especially not alongside people like this commoner here."
    to "I’m sure you understand that I mean no offense by that, yes?"
    s "I think you could probably use a little more practice when it comes to {i}not{/i} offending people."
    s "You’re not wrong, though."
    to "I seldom am."

    scene ayanetoukadojo23
    with dissolve

    ay "With all due respect, Touka...this place really means a lot to me and everyone else here."
    ay "Having this dojo taken from us would leave pretty much nowhere else to practice."
    to "I’m sure there is a...parking lot or vacant warehouse somewhere in the city that you can use if you truly want, correct?"
    ay "Doesn’t the same go for you? Do you even know karate?"
    to "Not yet, but my father is insistent on hiring the greatest instructor in Kumon-mi to tutor me directly."
    to "You know how fathers can be. Only the best for their daughters and whatnot."

    scene ayanetoukadojo24
    with dissolve

    ay "Only...the best for..."
    to "Miss Amamiya?...Did I say something wrong?"
    to "Is it because you don’t think you’ll be able to practice here anymore?"
    to "If it truly upsets you, I may be able to convince my father to let you train alongside me given our respective statuses in the city."
    to "Though...I unfortunately can not guarantee that the others will be able to join us as well."
    to "I’m sure you understand."
    ay "Not really..."
    ay "And I’m kind of starting to lose hope now, so..."
    ay "I think I’m going to go for a walk."
    s "Ayane-"

    scene ayanetoukadojo25
    with dissolve

    ay "Don’t...follow me, okay? I’ve gotta try and figure some stuff out..."
    ay "I’ll call you later."
    s "Uhh...sure. Okay."
    s "See you later, then."
    to "Miss Amamiya, I-"

    scene ayanetoukadojo26
    with dissolve

    "Ayane walks out of the dojo without even changing back into her normal clothes and suddenly I’m alone with a girl who has likely never been this close to someone as “middle-class” as me."

    to "Oh dear..."
    to "I had no idea that these circumstances would affect her so dramatically."
    s "You didn’t think that buying out the place she comes to every weekend would upset her?"

    scene ayanetoukadojo27
    with dissolve

    to "I did not know she came here in general."
    to "Miss Amamiya’s family is not one I know on a personal level, but I’ve heard my father speak of them on numerous occasions."
    to "Never in a million years did I think she’d be spending time somewhere so...{i}this{/i}."
    to "Perhaps her wealth is not as great as I’d been led to believe..."
    s "I think it’s more along the lines of Ayane wanting to feel like a normal girl. She definitely has money."
    s "I was at her house just recently and can testify that it was pretty remarkable."

    scene ayanetoukadojo28
    with dissolve

    to "They let you in?"
    s "...Yes. They let me in."
    to "Wow. It’s just one surprise after another today."
    s "Ayane was right. You don’t really get out much, do you?"

    scene ayanetoukadojo29
    with dissolve

    to "I actually go horseback riding rather frequently. And I’m part of a women’s golf organization as well."
    s "You’re just a walking rich-girl stereotype, aren’t you?"

    scene ayanetoukadojo30
    with dissolve

    to "Hahah! I suppose I am!"

    scene black
    with dissolve2

    "Touka gets off the ground (Which I’m sure was a real pain to sit on for someone of her status) and exits the dojo minutes later."
    "With Ayane still nowhere to be found, I make my way over to the instructor to figure out whether or not she knows anything..."
    "………"
    "……"
    "…"

    scene ayanetoukadojo31
    with dissolve

    kin "What now? Don’t you give me enough problems already?"
    s "No. I’m here to give you one more."
    kin "Of course you are. What do you need?"
    kin "Is this about the rich girl who just waltzed in here like she owned the place?"
    s "I mean...{i}isn’t she{/i} actually about to own the place, though?"

    scene ayanetoukadojo32
    with dissolve

    kin "Beats me. I'm more worried about keeping my job than anything else."
    kin "It's not like any of you take this seriously anyway. Why does it matter if someone else buys the place out?"
    s "Ayane takes it seriously."

    scene ayanetoukadojo33
    with dissolve

    kin "Then she should stop bringing guns in. We’re lucky she hasn’t gotten us closed down to begin with."
    s "I can't believe I'm asking this...but is there anything we can do?"

    scene ayanetoukadojo34
    with dissolve

    kin "If you’re really that worried, which I’m sure you aren’t considering you’ve spent maybe less than an hour actually doing anything since you signed up, why not talk to Ayane first?"
    s "I talk to Ayane all the time."
    kin "Not like that, you fucking idiot."
    kin "Ayane's crazy rich too, isn’t she? Maybe their families can start some sort of bidding war or something?"
    s "Maybe?...She didn’t seem to think her dad would be into the idea, though."
    kin "Don’t know until you try, right?"
    kin "It's not really my place to interfere. I'm just hoping this Tsukioka girl isn’t a pain in the ass."
    kin "Because based on first impressions alone, she really comes off as that “Don’t hit me” type and girls like that are the actual worst to teach."
    kin "Especially when their fathers step in and prevent you from doing things how you know they need to be done."
    kin "Really lucked out with Ayane not being like that, now that I think about it."
    kin "I guess she is kind of a good girl...even if she’s broken literally every single rule I set."
    s "Well, no matter what happens to the dojo, I hope things work out for you."
    kin "What? No you don't. You have never expressed an ounce of concern for me in my life."
    s "Then I will start right now."
    kin "Cool. Start by practicing."

    scene black
    with dissolve

    s "On second thought, it's getting late and I should probably start heading home."
    kin "Yeah, that's exactly what I thought..."

    "Obviously, I don't intend to actually go home. But as I exit the dojo, I {i}am{/i} hoping to find Ayane sulking on the steps or something."
    "Of course, she’s nowhere to be found- so I take a few laps around the block in an attempt to bump into her before giving up on it entirely and deciding to just...do something else for the rest of the day."
    "She'll call me if she needs me."
    "Maybe."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo30 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label ayaneinvite1:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
    if ayane_love >= 10 and ayanenew1 == True and ayanenew2 == False:
        jump ayanenew2
    if ayane_love >= 20 and ayanedorm15 == True and dojo20 == False:
        jump dojo20
    if ayane_love >= 25 and halloween14 == True and ayanedorm20 == True and dojo25 == False:
        jump dojo25
    if ayane_love >= 30 and ayanedorm25 == True and dojo30 == False:
        jump dojo30
...
```