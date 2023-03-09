# Reconciliation
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumispecial40&go=Go)


Part of event chain [A Thing of the Past](./yukidate10p2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: yumispecial40
* Group: Yumi
* Triggered by label: yukidate10p2

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label yumispecial40:
    scene familyreunion1
    with dissolve2

    y "The fuck are you smiling for? You think that just because I’ve decided to say a few words to you means I’m gonna just let you back into my life?"
    y "If it weren’t for you putting your filthy fucking hands all over the dude my best friend likes for...whatever fucking weird reason she likes him for, I would have just kept walking."

    scene familyreunion2
    with dissolve

    yu "Course you would have. Just like you did back at Tojo’s. "
    yu "I know it must be exhausting coming to terms with how I somehow managed to stay alive all these years, but would it kill you to at least {i}pretend{/i} to be happy to see me?"
    y "Would it kill {i}you{/i} to stop fucking trying to...reconcile with me or whatever the fuck this is? "
    yu "Reconcile? Your teacher the one helpin’ you learn big words like that?"
    y "Maybe. Just because {i}you{/i} decided to drop out of school doesn’t mean I’m going to follow in your footsteps."

    scene familyreunion3
    with dissolve

    yu "Good. I’m not sayin’ you should. "
    yu "I’m glad you’re actually out there makin’ an effort and shit. Damn impressive for someone constantly running from the shadow of her mother."
    y "Would be a hell of a lot easier if that “shadow” wasn’t behind nearly every fucking corner I round lately."
    y "How hard have you been trying to see me? I feel like I can’t go ten minutes without Sensei or...anyone else fuckin’ bringing you up. Why now?"
    y "If you’re looking for drug money, go to Dad. Not me. I won’t take shit from him. I’m tryin’ to make it on my own."
    yu "I don’t need drug money, Yumi. I’m clean now."
    y "Yeah? For how many hours?"

    scene familyreunion4
    with dissolve

    yu "…"
    y "Hey, how about we take a trip to the counter together? Maybe we can buy you a fucking cupcake or something to celebrate half a day sober!"
    y "It’ll be just like the old days...when we’d come down to places just like this so you could buy cigarettes or booze to keep yourself occupied while I tried to learn how to read."
    y "Doesn’t that sound fun, {i}Yuki?{/i}"

    scene familyreunion5
    with dissolve

    yu "You can still call me Mom, you know."
    y "Why would I?! Apart from the fuckin' ramen place, I can’t even remember the last time I saw you!"
    y "And half of the times I {i}do{/i} remember, you’re passed the fuck out with a needle sticking out of your arm!"
    y "Why the absolute {i}fuck{/i} would I call you “Mom?!” That’s a title you have to work for!"

    scene familyreunion6
    with dissolve

    yu "Well then let me fucking {i}work{/i} for it, Yumi! You really think I’ve been trying so hard to see how you’re doing just because I need drug money?!"
    yu "Why the fuck do you think I’m still in Kumon-mi in the first place?"
    y "Beats me. Probably got stuck inside before they closed the place off. "
    y "And knowing you, chances are you’ve burned all the bridges you need to keep yourself on your own two feet. Or what’s left of them, at least."
    yu "Yeah. I’m a shitty person, and an even worse mother. And I’ve done a lot of stuff that I wish I never did. But I’m still a fucking person."
    yu "I’m not asking for your help or forgiveness or any of that bullshit because I know full well that I don’t deserve it. Hell, I don’t even need to be a part of your life if you don’t want me to."
    yu "But to have my...entire existence be ignored by my own daughter is just-"

    scene familyreunion7
    with dissolve

    y "Just what?! Unfair?!"
    y "You know what’s unfair, Yuki?! Growing up without a mom! "
    y "At least if you would have fucking {i}died{/i} or something I could look back on you and try to dig up any of the “good” times we may have had!"
    y "But, nope!"

    scene familyreunion8
    with dissolve

    y "You were out...riding around on your little motorcycle...having a grand old time getting high and sucking dick for heroin while I was trying to figure out what it meant to be a normal girl."
    y "The only reason I’m as fucked up and “rough around the edges” as I am now is because of you, {i}Yuki.{/i} You did this to me."
    y "So when I ignore your existence, it’s probably safe to assume that I’m doing it to protect myself."
    y "Got it?"
    yu "...Yeah."
    yu "I got it."

    scene familyreunion9
    with dissolve

    yu "But I ain’t ever tried to dodge the blame for all that, Yumi. "
    yu "In fact, all the shit I’ve been tryin’ to do lately is to prove how {i}sorry{/i} I am. "
    y "I’m sorry, would you mind explaining to me how flirting with my fucking teacher in front of me is trying to prove how sorry you are? Because, to me, that just makes it look like you haven’t changed one bit."
    yu "It was a joke, I don’t know. I just wanted you to say something. I didn’t really care what it was."

    scene familyreunion10
    with dissolve

    y "Stop {i}wanting{/i} me to do anything and just go back to leaving me alone like you’ve done for the last...forever!"

    if yumiknows == True:
        y "I don’t want anything to do with you! And if you’re going to keep flirting with my friend’s boyfriend, do it in whatever fucking box you’re living in instead of in public!"
    else:
        y "I don’t want anything to do with you! And if you’re going to keep flirting with my teacher, do it in whatever fucking box you’re living in instead of in public!"

    yu "…"
    yu "Did you like your present at least?"
    yu "I know it probably seemed like a fuckin’ slap in the face gettin’ something so small after so much time away, but that was really all I could afford with the money I have."
    yu "I just wanted to do something for your birthday after missing the rest of ‘em."

    scene familyreunion11
    with dissolve

    y "I’m surprised you’ve got enough brain cells left to even remember my birthday."
    y "As for the “present,” I loved it. Made a real satisfying sound when I tossed it into some fucking rich girl’s pond."

    scene familyreunion12
    with dissolve

    yu "You...what?"
    s "I didn’t realize you were in the position to just be throwing away things that people give you-"
    y "Stay the fuck out of this, Sensei."
    y "As if I’d accept a fucking consolation prize from this piece of shit. "

    scene familyreunion13
    with dissolve

    yu "Heh."
    y "...What?"
    y "What reason could you possibly have to be laughing right now?"
    yu "No real reason."
    yu "You just remind me a lot of myself when I was your age."

    play sound "slap.mp3"
    scene familyreunion14 with hpunch

    y "Fuck you!"
    yu "…"

    "I looked away for a second, likely because even I get tired of staring at roadside car accidents, but even without looking, it’s easy to understand what just happened."
    "And I’m sure it’s the same thing that would have happened when Futaba was in the same exact scenario not too long ago."
    "The last thing Yumi wants is to resemble her mother."
    "But, if that’s the case, it would probably be good for her to stop hitting people since I’m pretty sure that was just Yuki’s thing for a...very long time."
    "That aside, I think the time has come for me to step in. "

    s "Yumi, that’s-"
    yu "Nah, let her go. It’s no big deal."

    scene familyreunion15
    with dissolve

    yu "She hits like a bitch anyway."
    y "Wha-"
    yu "You know, maybe you’re {i}not{/i} my daughter after all. {i}My{/i} daughter would take her gloves off before slapping someone. It softens the blow."

    scene familyreunion16
    with dissolve

    y "J-Just because your face is numb from being coked out of your mind doesn’t mean I hit like a bitch!"
    y "Now get the fuck out of here before I do it again!"

    if yumiknows == True:
        yu "I can’t. I’m still waiting for your “friend’s boyfriend” to choose what he wants for dinner since I owe him for helping me out."
    else:
        yu "I can’t. I’m still waiting for your teacher to choose what he wants for dinner since I owe him for helping me out."

    scene familyreunion17
    with dissolve

    if yumiknows == True:
        if bonus == True:
            y "Well maybe my {i}friend’s boyfriend{/i} should try to be a decent person for once in his life and {b}not stick his dick in my mother in exchange for a convenience store dinner!{/b}"
        else:
            y "Well maybe my {i}friend’s boyfriend{/i} should try to be a decent person for once in his life and {b}not just hug everyone in Kumon-mi!{/b}"
    else:
        if bonus == True:
            y "Well maybe my teacher should try to be a decent person for once in his life and {b}not stick his dick in my mother in exchange for a convenience store dinner!{/b}"
        else:
            y "Well maybe my teacher should try to be a decent person for once in his life and {b}not just hug everyone in Kumon-mi!{/b}"
            s "Hey! That hurts my feelings!"

    play sound "slap.mp3"
    scene familyreunion18 with hpunch

    y "-!"
    yu "Hey. You can talk as much shit to me as you want, but that is your {i}teacher.{/i} You treat him with respect. "
    s "Yuki, that’s really not-"

    scene familyreunion19
    with dissolve

    yu "Huh. You know, maybe there’s a right way to slap someone with gloves on after all?"
    s "…"
    y "…"

    "It’s clear that neither of these two have any interest in letting me interfere but, to be honest, I kind of expected as much."
    "Yumi’s already proven to be beyond reasoning with and Yuki is...well, {i}still{/i} not the best mother even when she’s trying to be."

    if bonus == True:
        "Her methods were definitely effective, though, as I don’t think I’ve ever seen Yumi this shell-shocked before- and I have literally forced my tongue down her throat."

    scene familyreunion20
    with dissolve

    yu "I haven’t heard an “I’m sorry, Sensei” yet."
    yu "He did nothing wrong. When you have a problem with someone, you don’t bring other people into it. Got it?"
    yu "I raised you better than that."
    y "I’m...sorry..."
    s "…"

    scene familyreunion21
    with dissolve

    y "And you didn’t raise me at all, so my bad for not knowing where to properly direct my anger."
    y "Hitting your daughter in public, though? That’s low."
    yu "What, and hitting your mother isn’t? Don’t dish it out if you can’t take it, Yumi."
    yu "You wanna act like an adult and grow up all by yourself? Fine. Go right ahead."
    yu "But don’t go around accusing everyone of being against you when they’re just trying to help. "
    yu "If you’re that afraid of winding up like me, that’s the very least you can do."
    y "…"
    yu "…"
    y "I fucking hate you."

    scene familyreunion22
    with dissolve

    yu "Good."
    yu "You should hate me."
    yu "If I were you, though, I’d go check and see if that present you tossed into the rich girl’s pond is still there. "
    yu "There were enough gift cards in that to feed you for a week, probably. Two if you be cheap about it."
    y "Please...just..."
    y "Just leave me alone..."

    scene familyreunion23
    with dissolve
    play sound "entrybell.mp3"

    "Yumi exits the convenience store in a hurry without buying anything- and I think it’s strange that my mind gravitates to {i}that{/i} aspect of this situation rather than anything else."
    "I guess watching her struggle to stay afloat has become so normal for me that I just chalk it up to a natural occurrence any time things go horribly for her."
    "I guess there are just some people born with horrible luck."
    "And I guess they just all happened to be born in close proximity to me."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene familyreunion24
    with dissolve

    yu "Well, that could have gone better."
    s "You know, when Yumi arrived, I could have sworn that you were going to ease up on the flirting rather than just entirely lean into it."
    yu "Not the best idea looking back on it, but I’ve got a history of making shit decisions in the heat of the moment."
    yu "You gonna follow her?"
    s "What would I do if I did?"
    yu "I don’t know. Teacher shit? Tell her everything’s gonna be okay and like, pat her on the back or somethin’?"

    scene familyreunion25
    with dissolve

    s "Cheering people up isn’t really one of my strong suits."
    yu "Same here, but I’m sure you’ve probably figured that out in the last few minutes."
    yu "We’ll take a rain check on dinner for now."
    yu "Go run after my piece of shit daughter and make her feel like {i}less{/i} of a piece of shit for popping out of me."
    yu "I’ll just go back to my {i}box{/i} and relapse or something since that’s clearly all I’m good for."
    s "Please don’t. You’re doing really well based on the zero experience I have of the drug-addicted version of you."

    scene familyreunion26
    with dissolve

    yu "I know. And I won’t. "
    yu "Gonna take more than that to knock me on my ass again."
    yu "But, uhh...thanks again for showin’ up or whatever. Sorry it couldn’t end on a better note."
    yu "Bad shit really tends to just follow me around at times."
    s "Yeah..."
    s "Same here."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yumispecial40 = True
    stop music fadeout 10.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "………"
    "……"
    "…"

    jump yumispecial40p2

label yumispecial40p2:
...
```

## Code that triggers this event
File: \game\YukiEvents.rpy
Code:
```python
...
s "...I’ll be the one to talk, I guess."
    s "Hi, Yumi."

    scene yukiconvenience15
    with dissolve

    y "Yeah. {i}Hi.{/i}"
    y "Would you mind explaining what you’re doing all the way in bumfuck nowhere with {i}her{/i}?"
    s "This is the most populated part of the city and you have weird criteria for what constitutes “bumfuck nowhere.”"
    s "As for why I’m with {i}her{/i}-"

    scene yukiconvenience16
    with dissolve

    yu "We’re on a date."

    "Oh no."

    s "{i}What are you doing?{/i}"
    yu "Hm? Flirting, obviously."
    y "You expect me to believe that {i}you two{/i} are on a date?"
    y "Even this guy, who’s one of the scummiest people I’ve ever met, would have to be drunk out of his fucking mind to even {i}consider{/i} going on a “date” with someone like you."

    scene yukiconvenience17
    with dissolve
    stop music fadeout 20.0

    yu "Maybe he just likes girls who are a little rougher around the edges? Don’t ask me, ask him."
    s "Don’t ask me. We are not on a date and I have no idea why she is doing this."
    yu "Oh, come on. You could have at least played along a {i}little{/i}."

    if bonus == True:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m screwing her mother when I {i}definitely am not.{/i}"
    else:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m hugging someone evil."

    scene yukiconvenience18
    with dissolve

    y "Great. Consider yourself lucky then for not catching one of the millions of STDs the world’s greatest mom over here is carrying."

    if bonus == False:
        "Oh no. Can you catch those from hugging?"

    s "Okay, Yuki was clearly in the wrong with pretending to date me, but-"
    yu "Nah, she’s right. Well, apart from the STD thing. I deserve whatever she throws at me. "
    yu "Besides, this is the first time she’s said anything to me in years. I’ll take what I can get."

    play music "undersea.mp3"

    if yumiknows == True:
        y "What you can {i}get{/i} is the fuck away from my teacher who, coincidentally, also happens to be {i}dating my best fucking friend.{/i}"

        scene yukiconvenience19
        with dissolve

        if bonus == True:
            yu "Wait, you never told me that."
            yu "I thought you were fucking Yumi?"
        else:
            yu "Wait, you never told me that."
            yu "I thought Yumi was you huggy buddy."
    else:
        y "What you can {i}get{/i} is the fuck away from my teacher, you dumb bitch."
        yu "{i}Just{/i} your teacher?"
        s "Yuki, no."
        y "Well, what else would he fucking be?"

        if bonus == True:
            yu "Beats me. I just thought you two were screwing or something."
        else:
            yu "I thought he was your hugging partner."

    scene yukiconvenience20
    with dissolve

    y "You thought fucking {i}what?{/i}"
    yu "Well...yeah. Because I’ve seen you two around together and...I don’t know. I just kinda figured there was some shit goin’ on."
    yu "Sensei always told me that wasn’t the case, but I kinda just figured that was because I’m your mom and that would make shit real awkward for him."
    y "Are you fucking kidding me?"
    yu "What? It’s a misunderstanding. It’s not a big deal."

    scene yukiconvenience21
    with dissolve

    yu "But, uhh...apart from that..."
    yu "You...got taller?"
    y "Yeah. It’s a little known fact, but most kids continue growing once their parents walk out on them."
    s "Okay, I’m just...gonna...go over there."

    scene black
    with dissolve

    "Yuki lets go of my collar and I quickly make my way over to the magazine rack to make it look like I’m...doing anything but being involved in this discussion."
    "And while I’d like to say it will only be a matter of time until one of the staff breaks things up (Which probably {i}should{/i} be my job), it looks like the only person working really doesn’t want to get involved."
    "And I don’t blame them. Neither Yuki nor Yumi look particularly friendly...especially when they’re at each other’s throats."

    $ renpy.end_replay()
    $ yukidate10p2 = True
    jump yumispecial40
...
```