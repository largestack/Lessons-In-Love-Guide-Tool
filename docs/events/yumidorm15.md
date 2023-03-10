# Worse Comes to Worst (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 15

* Event [Yumi Revitalization Project](./yumidorm10.md) (Yumi) is completed)

* Event [Nothing Was Missing, Except Me](./cafe20.md) (Rin) is completed)



## Next events

* [Yumi: Apples to Apples](./streets15.md)

## Event properties

* Id: yumidorm15
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm
* Triggered by path: yumidorm->yumidorm15

## Official wiki page

[Worse Comes to Worst](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm15&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm15:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on the door and make the executive decision to, once again, not say anything."
    "Yumi and I have been on better terms as of late, but it’s still inherently clear
    that she hates my guts."
    "Which is fine, don’t get me wrong. But it does make for
    slightly more boring narration during times like that."

    y "Yeah? What do you want?"
    s "I have a-"

    if bonus == True:
        y "Say one thing about a fuckin’ pizza delivery and I swear to God I’ll rip your nuts off."
    else:
        y "Say one thing about a fuckin’ pizza delivery and I swear to God I’ll tear your wig off."

        "{i}She knows too much.{/i}"

    s "Uhh..."
    s "Did somebody order...Chinese food?"
    y "..."
    y "Just fucking come in. The door’s open..."
    s "Deal. But only because you asked me to."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "…"
    "I turn the handle..."

    scene yumidormonefive1
    with dissolve
    play music "yumiska.mp3"

    "And Yumi’s theme song immediately starts playing in my head."

    s "Why does it have to be so loud, though?"

    scene yumidormonefive2
    with dissolve

    y "Huh? The fuck are you talking about? I don’t even have any music on."
    s "It’s the- Oh, never mind. What are you up to?"

    scene yumidormonefive1
    with dissolve

    y "Nothing."
    s "Cool, cool."
    y "…"
    s "This is the part where you ask me what I’m up to. Or how my day went. Or literally anything."
    y "…"
    s "Just ask me a god damn question, Yumi. I can’t carry every conversation."

    scene yumidormonefive3
    with dissolve

    y "Ugh...fine. Uhh..."
    y "I don't fuckin' know, man. Gimme a sec to think of one."
    s "Sure. You can have all the secs you want."

    scene yumidormonefive4
    with dissolve

    y "Okay, here's a good one- why are you so fucking annoying?"
    s "..."
    s "I kind of asked for that one, didn't I?"
    y "Yes. And also, fuck you."
    s "I really don’t appreciate insults at this stage of our relationship, Yumi."

    scene yumidormonefive2
    with dissolve

    y "What {i}stage{/i} do you think we’re at, douchebag?"
    y "All I did was sign some stupid paper that said you need to buy me free lunch."
    s "You’re leaving out the most important part of the contract...getting you a job
    so you don’t have to sell stolen TVs to people."

    scene yumidormonefive5
    with dissolve

    y "Was that really part of the deal? Can’t say I remember it if it was."
    s "Hey, if you don’t want to hold up your end of the bargain, I’m perfectly fine walking away from this."
    y "Cool. Walk away then."
    s "…"
    y "…"
    s "Okay, I kind of expected you to try and stop me there, but I guess not."

    scene yumidormonefive2
    with dissolve

    y "Yeah. You expect a lot of weird shit, don't you?"
    s "I mean...I don't know if I'd say {i}a lot{/i}."

    scene yumidormonefive5
    with dissolve

    y "Well...it’s whatever. You haven’t really done anything shitty today so I guess the least I can do is...humor you for a little while."

    scene yumidormonefive6
    with dissolve

    y "I’m guessing you came here to talk about that work thing?"
    s "Not specifically, but I guess we might as well since we’re already on the topic."
    s "Is there anywhere you’re interested in working, Yumi? Or maybe some job you’d like to try out?"

    scene yumidormonefive7
    with dissolve

    y "I get to choose?"
    s "Did you think I was going to just bring you to random places until one of them hired you?"
    y "Kinda, yeah. I didn’t think there’d be any actual effort involved on my part."
    s "You’re going to need to put effort into more than just choosing a place to apply to if you really want to earn money."
    s "Not that you were really putting any effort into that aspect of the search either, but yeah."

    scene yumidormonefive8
    with dissolve

    y "You're forgetting that I don't even fuckin' know {i}how{/i} to put this effort shit in! Aren't my options as a teenager like, fuckin' limited or whatever?"
    y "The fuck you want me to do? Walk around town and think of all the places that might be lookin' for someone my age?!"
    s "That is...exactly what I want you to do. Yeah."

    scene yumidormonefive5
    with dissolve

    y "Just...fucking choose a place, dude. I don’t really care. I told you I’m just in it for the free food."
    s "Then...how about something like a maid cafe?"

    scene yumidormonefive9
    with dissolve

    y "…"
    s "…"

    "Yumi elects to not say anything at all, filling the room with an awkwardly
    tense silence that would be sure to make me sweat if I wasn’t twice her size."

    y "The fuck did you just say to me?"
    s "I asked if you’d want to work somewhere like-"

    scene yumidormonefive10
    with hpunch

    y "I KNOW WHAT YOU FUCKING SAID!"
    s "Well, then why did you ask?"
    y "BECAUSE I’M NOT FUCKING OKAY WITH WORKING AT A MAID CAFE! LOOK AT ME!"
    y "DO I LOOK LIKE MAID CAFE MATERIAL?!"
    s "It sounds to me like someone doesn't understand both the allure and archetypical diversity of maid cafes."

    scene yumidormonefive11
    with dissolve

    y "Arca-what? Fuck does that even mean?"
    y "Like, can you actually imagine me dressing up in that kinda shit?"
    s "To be completely honest, I've been imagining it for a few minutes now."

    scene yumidormonefive10
    with dissolve

    y "WELL STOP! THAT’S NOT A THING ANYONE SHOULD EVER THINK OF."

    scene yumidormonefive8
    with dissolve

    y "Now give me a fucking real suggestion before I...rip up your God damn contract or whatever."

    "I think for a moment about places that might be hiring a part-timer..."
    "Somewhere that wouldn’t mind taking on someone like Yumi."
    "And before long-"
    "I realize that I have absolutely nothing."
    "Well, next to nothing."
    "The truth is that there {i}is{/i} one place I can think of, but I don't really have any idea if they're hiring or not."
    "I guess it wouldn't hurt as a suggestion, though, when the worst case scenario would just be the two of us going somewhere else."

    s "Okay...How about something like-"
    s "A cafe?"

    scene yumidormonefive7
    with dissolve

    y "A cafe?"
    s "A cafe."
    y "With or without maids?"
    s "Without. Even I know better than to suggest the same thing twice in a row."
    y "A cafe, huh?..."
    y "You mean like the one Headphones works at?"
    s "Headphones? Who is- oh. Rin."
    y "Yeah. Headphones."
    y "The one who’s always starin’ at Chika and shit."
    s "So I take it you've noticed that."

    scene yumidormonefive2
    with dissolve

    y "Fuck yeah I've noticed that. If it’s somethin’ she’s tryin’ to hide then she’s doin’ a piss-poor job. I barely even come to[school] and I noticed."
    s "That’s...relatively worrying. But yes, the one that Rin works at."
    s "She seems to like her job. And I can’t imagine being a barista is all that hard."

    scene yumidormonefive5
    with dissolve

    y "Don’t they have to memorize all those fuckin’ confusing-ass drinks, though?"
    y "My memory kinda sucks, not gonna lie. Can’t even remember what I ate for breakfast today."
    s "Probably nothing because you can’t afford breakfast."

    scene yumidormonefive9
    with dissolve

    y "Hey. Watch your fucking mouth, dick."
    y "Just because I don’t have money doesn’t mean you get to fuckin’ tease me about it."
    s "I’m not teasing you. Just trying to motivate you to turn things around."
    s "The sooner you get a job, the sooner you get to start buying things to improve your life."

    if day79 == True:
        s "For example, wouldn’t you feel good about yourself if you managed
        to save up enough to buy Chinami a present or something?"

        scene yumidormonefive12
        with dissolve

        y "Oh, give me a fuckin’ break...Do you really need to bring her into this? That shit ain’t fair."
        y "You’d have to be a heartless fuck to not have a weak spot for that little twerp."
        s "…"
        y "…"

        scene yumidormonefive13
        with dissolve

        y "Hey...the fuck you gettin’ all quiet for?"
        s "No reason. It’s just rare to see you actually show that you care about someone."

        scene yumidormonefive12
        with dissolve

        y "Yeah, well..."
        y "Fuck you."
        s "…"

    else:
        s "For example, wouldn’t it feel good buying a laptop or something like that?"

        scene yumidormonefive7
        with dissolve

        y "Actually...that {i}would{/i} be kinda sweet. I could watch all those badass American action movies I used to watch with my cousin when I was little."
        s "You watched action movies when you were little?"

        scene yumidormonefive13
        with dissolve

        y "There a problem with that, asshole? Action movies are cool as shit."
        s "I didn’t say they weren’t. I just think that might be the first thing I’ve learned about your past."

        scene yumidormonefive12
        with dissolve

        y "Well, have fun jotting it down in my page of the weird stalker journal you definitely have."
        s "How do you know about my journal?"
        y "Oh, fuck off."
        y "Unless you're not kidding and that shit is actually real."
        y "And if it is, please get the fuck out right now before I puke."
        s "Just forget I said anything."

    s "So, anyway, is the cafe okay? I never got a clear answer."

    scene yumidormonefive5
    with dissolve

    y "{i}Hah...{/i}"

    "Yumi lets out a sigh and thinks to herself for a moment."
    "I guess she’s decided to stop refuting everything I say and put some actual thought into something for once."
    "The truth is...I can’t imagine her actually working at the cafe. But it’s a good place to start."
    "Right now, I think a job where Yumi doesn’t have to deal with people is probably the best course of action. "
    "But, from what I remember, there aren’t a lot of jobs like that open to girls her age..."

    y "Uhh...I don’t know..."

    scene black
    with dissolve2

    "Yumi walks away from me and takes a seat on the bed, grabbing one
    of her pillows and pressing it up against her chest."

    scene yumidormonefive14
    with dissolve2

    y "I don’t..."
    y "I don't really think anyone's gonna wanna order from any place I’m workin’."
    y "And I wouldn’t want to fuck up business for that place when they haven't even been open for that long."
    y "Plus, I’m not friends with Headphones and I don't want her thinkin' that I'm like, intruding on her turf or some shit."
    s "Rin’s not like that. She’s pretty cool with everyone."

    scene yumidormonefive15
    with dissolve

    y "What, is she a part of your gross-ass harem too?"
    s "That is a...complicated question."

    if bonus == True:
        y "I have no idea what the hell that means but I’m just going to assume you’re fucking her too."
    else:
        y "I have no idea what the hell that means but I’m just going to assume you’re hugging her too."

    s "Yeah, you seem to assume that about everyone."
    y "Yup. Sometimes I think I’m the only one left with any ounce of self-respect."

    if bonus == True:
        s "You and I {i}have{/i} kissed, though..."

        scene yumidormonefive16
        with dissolve

        y "Not because I wanted to, you fucking [rapist]!"
    else:
        s "You and I {i}have{/i} hugged, though..."

        scene yumidormonefive16
        with dissolve

        y "Not because I wanted to, you fucking jerk!"

    s "Woah there. Calm down. Can we get back to the cafe thing?"
    y "I don’t know, can we?! Or are you just gonna start blurting out more unnecessary shit from the past that I’m still tryin’ to forget about?!"
    s "I think you should give it a shot."

    scene yumidormonefive17
    with dissolve

    if bonus == True:
        y "I hope you’re talkin’ about the cafe again and not making out with you."

        "I mean...not like I’d be opposed to the latter, but..."

        s "Yes, I mean the cafe. I say we go there sometime soon and give it a shot."

    s "Worse comes to worst, you don’t get hired and wind up with free lunch instead."
    y "What if I {i}do{/i} get hired, though?"
    y "Not saying I will, of course. I mean...just fucking look at me."
    y "But what if I {i}do{/i} get hired? I can’t be as friendly as Headphones. Or even half as nice. "
    y "I can’t even fuckin’ smile ninety-nine percent of the time. No one’s gonna
    want someone like that behind the counter."
    y "So I’ll just wind up without a job again soon enough."
    s "And so you think it’s better to give up before you even try?"
    y "…"

    "Yumi stays silent for a moment, likely pondering over the impact of my last sentence."
    "I’m not always the best when it comes to giving advice, but I’m pretty sure that I had the optimal response in this case."
    "The truth is, she’s got a point. There’s no way she can be as friendly as Rin. That’s not the type of person Yumi is."
    "But that doesn’t mean she shouldn’t try."
    "Life is all about facing your fears and trying to accomplish the un-accomplishable."
    "Or at least that's what it's supposed to be about."
    "For the rest of us, it's just..."
    "Trying to stay occupied, I guess?"
    "Filling a void?"
    "I don't know. This isn't really the time to get introspective."

    y "...Fine."
    y "I’ll come with you to the stupid cafe."
    y "But you still have to buy me lunch when I don’t get hired. Got it?"
    s "Got it. We can go wherever you want."

    scene yumidormonefive18
    with dissolve

    y "Wait...really? Anywhere?"
    y "You’re okay with spending that kind of money on me?"
    s "I mean, I wish you’d be a little nicer to me every once in a while, but yeah."

    scene yumidormonefive19
    with dissolve

    y "Um...cool. Okay. I guess if you’re okay with it then that’s fine."
    y "I’ll try not to get too much, though. I know how much it sucks when you wind up
    rackin’ up a bill you can’t afford."
    s "Just get whatever you want and don’t even worry about it."
    s "As long as you make a somewhat conscious effort at the cafe, I’ll be happy."
    y "…"
    s "…"
    y "Okay."
    y "But I still fucking hate you. Got it?"
    s "How could I possibly forget when you remind me every thirty seconds?"

    scene black
    with dissolve2

    "I don’t stick around much longer after that."
    "I would have, but I guess Yumi got her fill of me and wanted to be alone again."
    "Unfortunately for her, if this job-hunting thing is ever going to work out, she needs to force herself to accept my presence in at least slightly larger doses..."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ yumidorm15 = True
    stop music fadeout 4.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikadorm20:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
...
```