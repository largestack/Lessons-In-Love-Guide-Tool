# Neon Heart (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Reconciliation](./yumispecial40.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Yumi: Unsung Heroes](./streets40.md)

## Event properties

* Id: yumispecial40p2
* Group: Yumi
* Triggered by label: yumispecial40
* Chain sources: yumispecial40
* Chain sources path: yumispecial40

## Official wiki page

[Neon Heart](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumispecial40p2&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label yumispecial40p2:
    scene clearnightsky with dissolve2
    play sound "entrybell.mp3"

    "I make my way out of the convenience store and try to spy on Yuki out of the corner of my eye- thinking that maybe she was just waiting for me to be gone to let her guard down and start crying or something."
    "Of course, I’m unable to see anything. "
    "Not just because she’s likely not robotic enough to cease functioning the second I’m out of her line of sight, but because mine is currently being flooded by an onslaught of street lights and neon."

    play music "sensei.mp3"

    "Yumi."
    "That’s what I should be thinking about right now- not whatever minor inconveniences I’m stuck dwelling on in an effort to make myself believe my problems are somehow bigger than hers."
    "After all, this is a rare opportunity for me to make a positive impact on someone’s life when they need it the most."
    "And oh, how excited I am to let that {s}slip{/i} fall through my fingers like the grains of sand I’m {i}still{/i} finding on my clothes and in my shoes all this time after the second beach trip."
    "If only I was able to bring something of value home with me rather than the useless remnants of something I never wanted to begin with."
    "Now, where did she run off to?"

    s "…"

    "I look around and see plenty of other people."
    "And if this were one of those Korean dramas Ami watches all the time, I’m sure the first person I’d ask would know exactly which direction the girl I’m looking for ran off in."
    "Unfortunately, real life is scarcely that convenient- and I expect tonight to be full of failed chances at locating her amidst growing waves of uncertainty regarding whether or not I even {i}should.{/i}"
    "What can I do?"
    "Or rather, what {i}will{/i} I do? "
    "Because those questions have two dramatically different answers, and the one that we’ll wind up observing together will likely be the one furthest from the right course of action."
    "Oh well."
    "I guess I’ll just shrug-"
    "Slide my hands into my pockets-"
    "And venture off in whatever general direction my gut points me in."
    "It’s led me to her plenty of times in the past."
    "Here’s hoping it doesn’t stop cooperating now."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene yumiwallpound1
    with dissolve2

    "Well, would you look at that?"
    "There were barely any failures at all on the way here."
    "In fact, I think this is only the third or fourth alleyway I’ve had the displeasure of searching. "
    "And here she is in all of her miserable glory- pounding away at a cement wall, still wearing the gloves her mother ridiculed her for not removing just a short while ago."
    "That’s good. "
    "It might be awkward for all of us if I have to rush Yumi back to the convenience store for bandages only to find Yuki there, still caught up in a daze about where her life is heading."

    s "…"
    y "{i}*Sniff*{/i}"
    y "Fuck!"
    y "Fuck! Fuck! Fuck!"
    s "…"

    scene yumiwallpound2
    with dissolve

    y "I know you’re there, asshole. "
    s "Damn. I was a little interested in seeing if you’d be able to take down that wall or not."
    s "What gave my presence away?"
    y "Probably the fact that my body instinctively tenses up any time you’re within ten feet of me."
    s "I’ll try and stay at least fifteen feet away the next time I have to chase you down an alley, then."
    s "How are your hands?"

    scene yumiwallpound3
    with dissolve

    y "I don’t know. Cold?"
    y "They hurt a little, I guess."
    y "Not like I have anything else I can fuckin’ take my anger out on around here, though."

    scene yumiwallpound4
    with dissolve

    y "And what the fuck were you doing with her?! I thought I told you to stop getting yourself involved with my fucking family!"
    s "I’m aware. I have a tendency to kind of just do what I want, though, so commands like that won’t ever really have any effect on me."
    y "You don’t fuckin’ say."
    s "Since you’re being so polite, I guess I can let you know, though."
    s "I was helping her pass out fliers for the bar she works at."
    s "Probably so she can save up enough money for another present you can throw into Ayane’s pond."

    scene yumiwallpound5
    with dissolve

    y "I don’t want her fucking {i}presents.{/i} I want my childhood back."
    y "Let me know when she figures out how to fit that into a fucking box and I’ll think about maybe {i}not{/i} dumping it into the nearest body of water."
    s "I’ll be sure to let you know."
    y "Yeah. Thanks."


    scene yumiwallpound6
    with dissolve

    s "So, how long are you planning on staying out here for?"
    s "In fact, why are you even all the way over here in the first place? We’re a long way from the dorms."
    y "So what? I’ve got legs. I know where the fuck I’m going."
    s "I’m pretty sure the last time I saw you over here, you were in the heat of trying to evade our constant run-ins with one another. Don’t tell me that’s what-"

    scene yumiwallpound7
    with dissolve

    y "I was looking for a job, okay?! "
    s "Without my help? I didn’t think you cared that much."
    y "Well, I do! And since nowhere near the fuckin’ dorms wants to hire me, it looks like I’ve got nowhere else to search but right smack dab in the heart of the fuckin’ city!"
    s "I really hope you weren’t planning on applying to that convenience store because I’m pretty sure you may have just ruined your chances."

    scene yumiwallpound8
    with dissolve

    y "Ha ha ha. You’re fucking hilarious. Now can you leave me alone for a few more minutes so I can finish crying?"
    y "Feel like that’s all I’ve been fuckin’ doing lately. "
    y "You know, it’s real weird how I went basically my whole life without crying until you started getting involved in it. Now, it’s like I can’t even do shit without realizing how fucked up and weak I am."
    s "You should be thankful you met me now, then. That sort of thing would catch up to you after a while."
    s "And the longer you kept it held in, the worse it would be when it finally boils over."

    scene yumiwallpound9
    with dissolve

    y "I’d sure as fuck be fine with takin’ my chances. Can’t see how it would be any worse than trying to beat a fucking cement wall to death."
    y "‘Sides, wouldn’t all that shit about not bottling things up make you a hypocrite or whatever?"

    if bonus == True:
        y "That is, assuming you’re still capable of feeling anything and you’re not some...mindless fuck-robot."
        s "You know, at this point, that’s starting to sound like a pretty accurate description."

        if yumiknows == True:
            y "Remember who it is you’re talking to, asshole. The second I have {i}any{/i} confirmation you’re sticking your dick in anyone other than Chika, I’m tearing it all down. "
            s "You could start by finishing that wall. A few hundred more punches and you’ll have likely made some sort of chip in it."
    else:
        y "That is, assuming you’re still capable of feeling anything and you’re not some...mindless hug-robot."
        s "Beep boop. Does not compute."

    scene yumiwallpound10
    with dissolve

    y "{i}*Sniff*{/i}"
    y "Why me, man?..."
    y "Why won’t everyone just leave me alone?..."
    s "…"
    y "…"

    "I highly doubt Yumi wants me to actually answer that question- which is good, because I’d have no answer for it if she did."
    "I can’t speak for anyone else, obviously, but why {i}do{/i} I keep bothering Yumi?"

    if bonus == True:
        "Is it {i}really{/i} just to have sex with her? "
        "Or is it more like I’m chasing after some sort of debt that I feel she’s owed after stealing her first kiss on a hill overlooking the homeless?"
    else:
        "Is it really just to hug her?"
        "Or is it more like I’m chasing after some sort of debt that I feel she’s owed after {i}actually{/i} hugging her?"

    "Or maybe it’s neither of those things? "
    "Or maybe it’s both?"
    "Maybe I’m just doing this because I feel like I’m supposed to?"

    if bonus == True:
        "Like neglecting her will, one way or another, cause my life to spiral out of control into a marathon of meaningless sex acts with all of her classmates."
    else:
        "Like neglecting her will, one way or another, allow me to hug more people on a more frequent basis."

    "That would have sounded wonderful several school years ago."
    "Actually, it sounds wonderful right now."
    "But, strangely enough, the presence of a girl who just wants me to leave her alone somehow brings a little balance to this thing of mine resembling a life."
    "And I’m talking about someone who {i}actually{/i} wants me to leave them alone."
    "Even that part of Maya’s personality has been beginning to show cracks as of late."
    "But here’s Yumi- equipped with more cracks than you’d get from throwing a frag grenade at a china cabinet."
    "And here’s me-"
    "Desperate to “fix” her."

    scene black
    with dissolve2

    "Yumi stands up and shakes her gloves off before bringing them to her eyes to wipe away her tears, because god forbid I actually {i}see{/i} them."
    "She stands still for a moment, torn between thoughts of running away again or actually talking to me."
    "If she does run, I won’t chase her this time. I know better than to go out of my way for someone twice in rapid succession."
    "But-"
    "If she wants to talk-"
    "I’ll do my best to soak up whatever overly-aggressive behavior or excuse she has for me this time around."
    "All while reminding myself that I can’t touch her, no matter how much I may want to."

    scene yumiwallpound11
    with dissolve2

    y "So...fliers? Really?"
    y "This why you can’t be bothered to actually teach? You’re too busy workin’ night jobs with allegedly recovering addicts?"
    s "Yes. I also fight crime by night, but you have to keep my secret identity to yourself or the two of us could be assassinated. "
    s "Also, you should be thankful that I don’t actually teach because, if I did, you would have failed a long, long time ago."

    if bonus == True:
        y "I’d be more interested in coming to school if I didn’t constantly feel like my teacher was imagining me naked."
        s "Don’t flatter yourself, Yumi. I have a whole twenty girls to imagine naked now. I only have so much time for you."
    else:
        s "Just kidding. I love teaching."
        s "And...I love {i}you.{/i}"

    scene yumiwallpound12
    with dissolve

    y "Ew! Gross! Fuck off! "
    y "See, this is exactly why I don’t show up! Because of you!"
    s "Why not ask for a transfer then?"
    y "To where? Everyone thinks I’m a fucking delinquent, dude. No one wants me."
    s "They don’t {i}think{/i} you’re a delinquent. You literally {i}are{/i} a delinquent. "
    y "Well, yeah. That’s why they all think it. But that’s beside the point!"
    y "I’m stuck in your stupid class, and unless you decide to throw me out of it, you’re stuck with me too."
    y "Just...only on days when I actually show up. The rest of the time, just pretend I don’t exist or some shit."
    s "You know I can’t do that, Yumi."

    scene yumiwallpound13
    with dissolve

    y "But...why?"
    y "All I do is cause problems and start shit with both you {i}and{/i} the other girls. "

    if bonus == True:
        y "I’ve got what’s basically a negative attendance record, shit grades when I {i}do{/i} take tests and, to top it all off, I’ve got mad fucking dirt on you from when you kissed me."
    else:
        y "I’ve got what’s basically a negative attendance record, shit grades when I {i}do{/i} take tests and, to top it all off, I’ve got mad fucking dirt on you from your attack hug."

    y "Granted, nobody will fucking believe me if I tell them, but all of that should be enough for you to want to stay the fuck away."
    s "…"
    y "…"
    y "What?"
    s "You just normally look a little...angrier when you say things like that."
    y "…"
    s "…"

    scene yumiwallpound14
    with dissolve

    y "I’m done being angry for today."
    y "It’s giving me a headache."
    y "I just want to go home and go to sleep."
    s "…"
    y "…"

    scene yumiwallpound15
    with dissolve

    y "What now?"
    y "Is my sudden vulnerable side making you question your morals again?"
    y "Are you going to make another horrible decision, Sensei?"
    s "…"

    scene yumiwallpound16
    with dissolve

    y "What if I close my eyes?"
    y "How about now?"
    y "Are you thinking about what you could get away with?..."
    y "What sort of horrible shit you could do to me?..."

    scene yumiwallpound17
    with dissolve

    y "And how fucking easy it would be to overpower me when I’m so fucking weak right now!"

    play sound "static.mp3"
    scene connect with flash
    scene frown with flash
    scene happy7 with flash
    scene yumiwallpound18 with flash
    stop sound

    "Something pulls me under so quickly that I can’t even get a glimpse at what it is."
    "But, if I had to take a guess, it would probably look something like me."
    "I don’t know whether or not I’m blacking out right now, and I fear that whenever I snap out of this, I might find myself in a similar place to somewhere I’ve been in the past."
    "I can only hope this isn’t true-"
    "But given the fact that Yumi’s already had a bad streak of luck today-"
    "And the {i}added{/i} fact that she’s been the target of these lapses in not just judgement but what seems like reality as a whole-"
    "Well-"
    "I can only imagine how things must be-"

    play sound "static.mp3"
    scene attempting with flash
    scene everythingg with flash
    scene frown with flash
    scene yumiwallpound19 with flash
    stop sound

    s "…"
    y "…"

    "When I open my eyes, it’s as if nothing has changed at all."
    "Yumi is still standing there with tears pooling up behind her eyelids- though, several have managed to escape down the length of her cheeks."

    if bonus == True:
        "And I’m still standing right next to her, caught somewhere between the early stages of forming an erection and the desire to slap her across the face and snap her out of whatever this is."
        "Two slaps in one night might be a bit too much for her, though."
        "And so I will use this moment as an excuse to reclaim several of the brownie points that I may have lost by being seen out in public with her least favorite person in the world."
    else:
        "And I’m still standing right next to her, ready to hug and ready to party."

    if yumiknows == True:
        s "I’m not going to kiss you, Yumi. Chika is my woman and I am her loyal, monogamist man."
    else:
        s "Nothing's going to happen, Yumi."
        s "I'm not going to hurt you."

    scene yumiwallpound20
    with dissolve

    y "Huh?..."
    y "Oh...Yeah. "
    y "Yeah. Okay."
    s "..."
    s "Don’t tell me you were hoping I {i}would{/i}...were you?"

    scene yumiwallpound21
    with dissolve

    if bonus == True:
        y "O-Obviously not! In fact, I’m surprised you were able to hold back given how fucking...perverted and...insatiable you are!"
    else:
        y "O-Obviously not! I hate you and...I hate your stupid hair cut!"

    s "Right."
    y "Right! And why are you just standing there fuckin’...staring at me, you creep! Back the fuck off!"
    s "You’re the one who walked up to me, Yumi. "

    scene yumiwallpound22
    with dissolve

    y "Jesus! When the fuck did it get so dark out here?! What time even is it right now?!"
    s "…"
    y "Listen, as much as I’d love to stay and chat, I’ve got shit to do and...and it’s a long walk home."
    s "…"
    y "…"
    s "We can walk together if you want?..."

    scene yumiwallpound23
    with dissolve

    y "…"
    s "…"

    scene yumiwallpound24
    with dissolve

    y "…"
    y "No..."
    y "No."
    y "I’ll make it on my own."

    scene black
    with dissolve2

    "Yumi leaves with that, and I’m forced to stand there in the alleyway and wait for her to fade away from my sight so as to not awkwardly walk behind her since we have to go in the same direction."
    "I’m not sure what really came over her with that “test” of hers a few minutes ago, but I’m thankful that it didn’t end in tragedy when nearly everything else tonight did."
    "I guess there’s nothing left to do now but...go home, then."

    play sound "phonebeep.wav"

    "I decide to send Yuki a text on my way out of the alley, confirming that her daughter is, at least as of several minutes ago, still alive and doing mostly okay."
    "Yuki doesn’t respond."
    "I catch a bus back home and go the rest of the night without saying or thinking anything else."

    $ renpy.end_replay()
    $ yumi_love += 2
    $ yumispecial40p2 = True
    stop music fadeout 7.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label streets40:
...
```

## Code that triggers this event

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
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
...
```