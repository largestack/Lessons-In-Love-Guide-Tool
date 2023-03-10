# An Extra Set of Arms (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 30

* Event [Scaredy Cat](./mikudorm25.md) (Miku) is completed)



## Next events

* [Miku: One. Two. Three.](./mikudorm30.md)

## Event properties

* Id: soccer30
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer30

## Official wiki page

[An Extra Set of Arms](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer30&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer30:
    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene mikudayrun1
    with dissolve
    play music "highspeedprinter.mp3"

    "I show up at the[school] much earlier than normal after deciding to skip my morning coffee."
    "Now that I’m here, however, I’m definitely regretting the decision."
    "Not only is this particular morning much colder than it should be for what is {i}technically{/i} still summer, but there’s no one anywhere to be found."
    "I guess it’s too early for even someone like Miku to show up and start...running around in circles or whatever it is she does when she’s the only one here."

    s "…"

    "A thought suddenly crosses my mind along with a strong gust of wind as I stand before an empty bench, too afraid to sit down and feel how cold it would be against me."
    "If winter is truly right around the corner, what is going to happen to soccer practice?"
    "Are all of the girls still going to show up every day when it starts dropping to freezing temperatures?"
    "Does Kumon-mi even get that cold?"

    scene mikudayrun2
    with dissolve

    mi "...?"

    "Out of nowhere, Miku comes running toward me from around the corner."
    "Her eyes widen when she realizes I’m here already, and I’m a bit curious as to why she’s wearing pants when she has practice this morning."
    "The hoodie I can understand, but I’m pretty sure pants aren’t the best for a sport that so-heavily involves lower body movement."

    scene mikudayrun3
    with dissolve

    mi "M-Morning, Sensei! "
    mi "What brings ya here so early? Also, isn’t it a little too cold to be wearin’ that same ole’ blazer?"
    mi "Where’s your winter jacket? Your scarf? Your gloves?"
    mi "Ya gotta be prepared or you’ll wind up catchin’ a cold and we’ll get a substitute teacher who actually {i}teaches{/i} us stuff."
    s "That sounds horrible."

    scene mikudayrun4
    with dissolve

    mi "It would be! I don’t even know if I remember how to write my own name."
    s "Please tell me you’re exaggerating."
    s "That seems like too much even for you."

    scene mikudayrun5
    with dissolve

    mi "Course I am. I practiced writin’ my name a bunch of times when I was little since I thought I’d be signin’ autographs and stuff once I got to college."

    if bonus == True:
        s "Still think you have a chance to make it there?"
        mi "Make it where? College or autographs?"
        s "Both?..."
        mi "Probably not, but I try not to think too much about that anymore."
        mi "Besides, now that it’s gettin’ all cold and stuff, I'm havin' a hard time focusin' anyway."
        s "I was actually just thinking, is anything about soccer practice going to change when winter rolls around?"

        scene mikudayrun6
        with dissolve

        mi "Mm...I don’t really know."
        mi "I’m a first-year so I haven’t ever seen how this[school] handles that sorta thing before."
        mi "But if it’s anythin’ like my middle[school] was, I don’t think much should change. Some girls will probably just bring hoodies or somethin’."
        s "Are they going to be bringing pants, too? "

        scene mikudayrun7
        with dissolve

        mi "Why do ya ask, Sensei? Afraid of missin’ out on some of that good ole exposed [teenager] skin?"
        s "That and the fact that you’re wearing pants right now. "
    else:
        s "Ahh, yes. College. The place we are at right now."
        s "Also, why are you wearing pants? They are going to hinder your athletic ability."

    scene mikudayrun8
    with dissolve

    mi "Oh. Well, ya see, there’s actually a good reason for that."

    if bonus == True:
        s "That reason wouldn’t happen to involve what went down in your dorm room recently, would it?"
        s "Are those pants your anti-Sensei barrier?"

        scene mikudayrun9
        with dissolve

        mi "What? Nononono. It’s nothin’ like that. "
        mi "Besides, there are much easier ways to prevent ya from gettin’ all handsy with me if I don’t want ya to."
        s "Sounds ominous. You don’t carry any weapons around, do you?"
    else:
        s "Is the reason because you are concealing a firearm?"

    scene mikudayrun10
    with dissolve

    mi "No weapons here, just the heart of a warrior! "
    mi "The real reason I’m not dressed in my jersey today is that we’re skippin’ practice on account of everybody bein' sick."
    mi "A bunch of the girls went out to some yakiniku place last night and all wound up with food poisoning. "
    s "So you’re here all by yourself? Why not just sleep in?"

    scene mikudayrun11
    with dissolve

    mi "I can’t sleep in or I’ll miss out on the exercise I need to prevent my body from going all wibbly-wobbly whenever I’m playin’ soccer."

    scene mikudayrun12
    with dissolve

    mi "And also I...thought I might run into ya here and stuff."
    s "So you woke up extra early on the weekend and came all the way to[school] in your normal clothes because you thought you might see me?"
    mi "Don’t forget about the exercise part. It’s not {i}just{/i} because of you. That’s just a little bonus I guess."

    "Adorable."

    s "Well, I’m glad I wound up coming here then. It will give the two of us a chance to talk about stuff."

    scene mikudayrun13
    with dissolve

    if bonus == True:
        mi "This isn’t gonna be one of those adult talks about the dangers of babymakin’, is it? Cause we got real close recently and I definitely ain’t ready for that."
        s "Okay well first, we did not come anywhere close to “babymaking.”"
    else:
        mi "Does it have somethin' to do with how Makoto's family still hasn't changed the name of their business to somethin' other than {i}DVD Store{/i} yet?"
        s "Firstly, yes. That is something they should do."

    s "Secondly, I mean more about just...discussing normal stuff."
    s "You said you wanted to get to know me better, and I don’t really know anything about you either other than that you play soccer and don’t like loud noises."

    scene mikudayrun14
    with dissolve

    mi "That’s pretty much all I’ve got. If you’re lookin’ for someone more unique, you’re probably better off with somebody like Kirin."

    if kirindate10 == True or ayanelust10 == True:
        "Well, she’s definitely right about Kirin being...unique."
        "I’m not quite sure if that’s a good thing yet, though."

    s "Well then it shouldn’t be a difficult conversation since I don’t have much interesting to say either."

    scene mikudayrun15
    with dissolve

    mi "Really? No crazy stories about what it’s like lookin’ after Ami?"
    s "I think it’s closer to Ami looking after me, to tell you the truth."

    "In all fairness, though, it’s not like I know anything about how things were beforehand."
    "That’s probably something I’ll need to hear from Ami or Ayane directly before I jump to any conclusions about how difficult things were."

    s "Do you want to go sit down somewhere, maybe?"
    s "I’m starting to feel a little odd just standing on this pathway talking about...whatever we’re talking about."
    mi "A whole lotta nothin’, if ya ask me. But yeah, we can go sit."

    scene mikudayrun16
    with dissolve

    mi "There’s a spot I ran past earlier that the sunlight can reach. We probably won’t freeze our butts off like we would on one of the benches either."
    mi "Nothin’ worse than a cold bench, ya know?"
    s "I mean, there are definitely worse things. But yeah, take me to your secret sunspot."
    mi "Heheh...it’s not a secret. It’s just a corner of the[school] building. "
    mi "Come with me and you’ll see!"

    scene black
    with dissolve2

    "Miku begins to walk alongside me and it feels rather...odd."
    "It’s never occurred to me before but I don’t normally see her walking. Like, ever."
    "Even on the rare occasions where we’ve gone out at night during one of my dorm-visits, it’s always centered around jogging."
    "It’s good knowing that Miku has a lower setting as well."
    "I like the high-velocity version, but a cold morning like this is definitely not ideal for the standard version of Miku, as far as I’m concerned."

    scene mikudayrun17
    with dissolve

    "The light filters through the clouds and spills onto us as we step into a sun-soaked sanctuary on the side of the[school]."
    "Miku leans up against the wall and I decide to take my place in front of her instead of off to her side."
    "Sure, my section is a little closer to the shade, but if we’re actually going to be {i}talking{/i} to each other for once, it might be helpful to see her face."
    "Not to mention, I like her face quite a bit. It’s a good face."

    mi "Sooooo...what did you want to talk about?"
    mi "I can go on and on about most stuff, but when it comes to this openin’ up kinda thing, I just sorta freeze up."
    s "Is that like, a confidence issue or something?"

    scene mikudayrun18
    with dissolve

    mi "Uhh...no. No, that’s not it at all."
    mi "Just that there’s some stuff that’s happened to me in the past that’s not really fun to talk about."
    mi "I told you that in my dorm a while ago, didn't I? After the first time ya saw me actin' all weird."
    mi "I don’t like feelin’ weak, so I try to push it away as much as I can. But there’s only so much I can push, ya know?"
    mi "I’m strong, but I’ve got tiny arms. Pushin’ stuff can be hard."

    "Oh, this is a good opportunity to be deep."

    s "You know Miku, I can-"

    scene mikudayrun19
    with dissolve

    mi "You can help me push things that are too heavy for me to push on my own. I know."
    s "What the hell? You stole my moment."

    scene mikudayrun20
    with dissolve

    mi "Yup! Makoto said the same thing when I brought up the arm thing before. And you’re really just the boy version of her."
    mi "Err, actually no. I {i}used{/i} to think you were like the boy version of her. But now you’re like...just a boy."
    mi "But you two still have glasses and talk the same so I guess you’re kinda still similar."
    s "Well it’s good knowing that I remind you of your best friend."
    mi "Yup!"

    scene mikudayrun21
    with dissolve

    if bonus == True:
        mi "Can’t say Makoto’s ever tried to put her fingers in me before, though, so that’s a thing we’ve gotta take into account now."
        s "So really, the only things Makoto and I have in common in your head are...glasses and the way we talk."
        mi "I coulda sworn there was more but I guess not."
    else:
        mi "Can’t say Makoto’s ever tried to hug me before, though...."
        s "That is so sad."

    scene mikudayrun22
    with dissolve

    mi "Do you have any cool stuff you want to tell me about {i}your{/i} past since I don’t wanna talk about mine, Sensei?"
    mi "Like I said the other day, I don’t know anything about you. Tell me some stuff."

    if bonus == True:
        mi "Like, when did ya realize you liked thighs so much?"
    else:
        mi "Like, when did ya realize you liked pretzel rods so much?"
        s "How did you know about that?"
        mi "Just tell me, idiot."

    s "Probably the first time I saw them but that’s not really something I can talk about at length."

    "At least not with Miku. I’m not trying to scare her off when we’re finally becoming closer."

    mi "That’s like me and soccer! "
    mi "The first time I ever saw a game, I was totally hooked!"

    if bonus == True:
        mi "Sure, soccer is a lot more innocent to get hooked on than a girl’s legs, but I can kinda understand more about your interests now."
    else:
        mi "Sure, soccer is a lot more normal to get hooked on than pretzel rods, but I can kinda understand more about your interests now."

    s "Can you really, though?"

    scene mikudayrun23
    with dissolve

    mi "Course I can! A hobby is a hobby is a hobby is a hobby!"
    s "I think you said “hobby” a few too many times there."

    scene mikudayrun24
    with dissolve

    mi "I don’t think so. Hobbies are important."
    mi "Ya never know when ya need somethin’ like that to help you get yer mind off of stuff."
    mi "One of the big reasons I’m as into soccer as I am is that it helps me push away all of that sad stuff I was hinting at earlier. "
    mi "Soccer makes it so I don’t need to ask people like you and Makoto for an extra set of arms when things get tough."
    mi "Just like in sports, sometimes you just need to push through."

    "Miku begins spewing out a bunch of positivity despite hiding something so big from me that she breaks down whenever she hears a loud noise."
    "Thankfully, there are no loud noises around in this quiet pre-winter morning, so she is able to maintain the illusion of happiness for the time being."
    "Of course, that illusion is bound to come crashing down at any minute and she’ll need to think up a brand new justification for why she’s disguising her past."
    "What the hell happened to her and why is it worth putting on airs to tuck away?"

    scene mikudayrun25
    with dissolve

    mi "Woah! Where’d that angry face come from?"
    mi "If I knew ya hated positive outlooks so much I would have just started cryin’ and punchin’ the wall or somethin’."
    s "Don’t punch the wall. It’s made of stone and you’ll hurt your hand."
    mi "Then snap the heck out of it and look at me normally again! "

    scene mikudayrun26
    with dissolve

    mi "If we’re gonna be spendin’ the mornin’ together, I wanna do it with smiles on our faces. None of that “I’m a bad-guy teacher! Rawr!” mumbo-jumbo."
    s "I have never once {i}rawr’ed{/i} at you, Miku."
    mi "Not yet! But you look like you’re about to! "

    scene mikudayrun27
    with dissolve

    mi "Oh! I know! Let’s talk about anime! Lemme tell ya all about this tournament arc thingy I watched with Makoto last night!"
    s "Makoto watches anime?"
    mi "Of course! Now, listen up-"

    scene black
    with dissolve

    "Miku goes on to talk about a bunch of things I have to pretend to be interested in in order to avoid bringing her down any more than my face from several minutes ago did."
    "The rest of the morning flies by and, before we know it, the sunspot consumes all of Kumon-mi and converts a temporary, cool sanctuary into another scorching nightmare."
    "But at least it’s a nightmare Miku is able to smile in."

    $ renpy.end_replay()
    $ soccer30 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label mikuwinterbeach1:
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
    if miku_love >= 10 and soccer10 == False:
        jump soccer10
    if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
        scene soccerfield
        with dissolve
        "I show up at the soccer field to try and talk to Miku but she immediately runs off and starts talking to one of the other girls."
        "Am I...being avoided?"
        "I should probably try visiting her dorm sometime to figure out what's going on with her..."
        jump saturdayafternoon
    if miku_love >= 15 and day83 == True and mikudorm10 == True and soccer15 == False:
        jump soccer15
    if miku_love >= 20 and soccer15 == True and soccer20 == False:
        jump soccer20
    if miku_love >= 25 and mikudorm15 == True and halloween14 == True and soccer25 == False:
        jump soccer25
    if miku_love >= 30 and mikudorm25 == True and soccer30 == False:
        jump soccer30
...
```