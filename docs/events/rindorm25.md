# Sock Fetish (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 25

* Event [Delirium](./rindorm20.md) (Rin) is completed)



## Next events

* [Main: What's Done is Done](./beachvacation1.md)

## Event properties

* Id: rindorm25
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm25

## Official wiki page

[Sock Fetish](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm25&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm25:
    play sound "knock.mp3"

    "I knock on the door, wondering what sort of wholesome activities Rin is up to tonight."

    r "Sensei, is that you? Listen, don’t come in. I’m harvesting the organs from a body I found in an alleyway a few weeks ago."
    s "That’s not wholesome at all. And there is no way those organs are still usable."
    r "Who said anything about using them? I'm just doing this for fun."
    s "I'm sure you are, Rin. Can I come in now?"
    r "Sure! As long as you don’t mind the scent of blood and decomposition and stuff!"
    r "Not everybody's built for that sorta thing, you know?"
    s "Nope. But I am going to open the door now."
    r "Sound good! See you in three seconds!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene sockredux1
    with dissolve

    r "Heya! I was just kidding. There’s no body in here."
    r "Well...technically, there are two bodies in here. But they’re both living and their organs aren’t really ripe for harvesting yet."
    s "Can we stop talking about organs now?"
    r "Sorry. Just got done watching some zombie movie with a friend from another class and I'm having a hard time getting out of gore mode."
    r "Anyway, what do {i}you{/i} want to talk about? I feel like it's been a hot minute since we've had a good talk."
    r "You wanna go somewhere? Or just hang around and chat or something?"
    s "Why would I have come all the way over here just to ask you to go somewhere else?"

    scene sockredux2
    with dissolve

    r "Probs cause you haven't unlocked my number yet and you do weird stuff all the time. For all I know, you could be here to try and sneak into my sock drawer or something."
    s "What would I do with your socks?"

    scene sockredux3
    with dissolve

    r "I don’t know, man. Maybe you’ve got a...sock fetish? I’m not gonna pry into your personal details."
    r "They’re in my top drawer. Take however many you need. I need to buy new ones anyway and this might finally be the push I've been looking for."
    s "Thanks, I’ll just-"
    s "Wait, why did I feel compelled to actually look just now?"

    scene sockredux1
    with dissolve

    r "Maybe you do have a creepy, perverted side after all?"

    if bonus == True:
        "While that is obviously true, I don’t think I'm ready to stoop to the level of raiding sock drawers yet."

        s "Let's remove socks from our list of potential conversation topics as well. I don't have any use for your...footwear."
        r "I didn’t think you did. I was kinda just messing around, but now I'm not so sure."
    else:
        s "Of course, not. I think I may have just wanted to subconsciously wear them since man socks make me self-conscious."

    scene black
    with dissolve

    "Rin hops onto her bed and pats the space beside her, gesturing me to come sit next to her despite her newfound skepticism of whether or not I am here for her socks."
    "I'm not."
    "I do sit beside her, though."

    scene rindormbed1
    with dissolve

    r "So! Whatcha wanna talk about?"
    s "I’ll just wait for you to come up with something since I am very much not the talkative one here."
    r "Gotcha. Then, do you want to hear about the latest development in my hopeless pursuit of a girl who probably doesn’t even like girls?"
    s "You are aware that I know her name, correct?"

    scene rindormbed2
    with dissolve

    r "Obviously. But every time I say her name, my heart starts going crazy and my knees get all wobbly and stuff and I don't want you taking advantage of me in my time of hormonal weakness."
    s "You really like her that much?"

    scene rindormbed3
    with dissolve

    r "I want to crawl inside of her and sleep there forever."
    s "…"
    r "…"
    s "…"

    scene rindormbed3r
    with dissolve

    r "Dude, I’m kidding."
    s "I’m sorry. I just feel like I never really know with you."

    scene rindormbed4
    with dissolve

    r "Yeah, that’s fair. I mean, I can't really blame you for thinking that way when my mind's been all over the place lately."
    r "And I can't imagine the whole thing with my cutting habit really helping you form a better opinion of me."
    s "I never said that..."

    scene rindormbed5
    with dissolve

    r "You don’t always have to {i}say{/i} something in order for people to understand how you feel, Sensei."
    r "Like, come on. I know that stuff is still in the back of your mind somewhere."
    s "You’re not trying to blame me for {i}worrying{/i} about you, are you?"
    r "Not at all. If anything, I’m {i}glad{/i} you’re worried about me. I need that sort of relationship in my life to keep me from getting all weird again."
    s "Well, I didn’t really plan on talking about this tonight, but since we’re already on the topic, how {i}is{/i} your arm?"

    scene rindormbed6
    with dissolve

    r "Totally fine! It's not like I'm trying to kill myself or anything like that."
    r "Just a little...wake up call, I guess."

    scene rindormbed7
    with dissolve

    r "Plus! You’d be surprised what some decent make-up skills and a healthy body can do! I healed up almost right away."
    s "Speaking of make-up skills, how exactly did we wind up talking about {i}this{/i} when you were seconds away from telling me the latest developments in the Chika saga?"

    scene rindormbed7r
    with dissolve

    r "Chika?! What?! Where?! What happened with Chika?!"
    r "Did she say something about me? What was it? Tell me right now!"
    s "{i}She{/i} hasn’t said anything about you. You just alluded to some sort of development before our conversation slipped into something way too dark for me right now."

    scene rindormbed8
    with dissolve

    r "Oh, right."
    r "Sorry for the random, depressing tangent. Let’s get to the good part before you lose interest and never talk to me again."
    r "You can’t freak out when you hear this, though. Got it? Cause it’s kind of a big deal."

    "A big deal? Rin hasn’t already confessed to her, has she?"
    "How could I have missed this?"

    scene rindormbed9
    with dissolve

    r "Okay, so..."
    r "The other day, I was walking home, just mindin’ my own business and listening to music."
    r "Then all of a sudden, out of friggin’ {i}nowhere{/i} she just rounds the corner and starts heading my way."
    r "So, me being me, I almost threw up due to shock."
    r "BUT...I managed to NOT throw up and was actually able to talk to her instead!"
    s "Okay...and what did you two talk about?"

    scene rindormbed10
    with dissolve

    r "Oh, you know. A little of this. A little of that."
    r "School...The weather...TV..."
    r "Mostly just normal high school stuff."

    scene rindormbed9
    with dissolve

    r "BUT! Then, something {i}amazing{/i} happened."
    s "Did you two make out?"

    scene rindormbed11
    with dissolve

    r "God, I wish..."

    scene rindormbed12
    with dissolve

    r "But no..."
    r "She DID say that I looked cute, though! Which is only like, a step away from making out I think."
    r "So...maybe next time if I'm lucky."
    s "…"

    scene rindormbed3
    with dissolve

    r "Come on! Aren’t you gonna say anything? That’s like, a super big deal. It means there’s a {i}chance{/i}!"
    s "Sorry, I think I may have set my expectations a little too high and it made the payoff very much not worth it."
    s "But either way, I'm happy for you."

    if chikatownfirst == True:
        s "I don’t know if I’d get my hopes up if I were you, though."
        s "You still don’t really know if she’s into girls."

        scene rindormbed13
        with dissolve

        r "Yeah, I know..."
        r "It’s a really weird spot to be in...not knowing if your crush is into the same sex as you."
        r "Like, no one other than you and maaaaybe Futaba knows about this side of me."
        s "Don’t call it a ‘side’ if it’s just who you are, Rin."

        scene rindormbed14
        with dissolve

        r "Thanks, Sensei...But it’s a little more complicated than that."
        r "Like...what if I {i}do{/i} tell her and she thinks it’s weird?"
        r "Or...or even worse-"
        r "What if she’s already into someone else?..."

        "My mind quickly travels back to when Chika and I kissed in the second half of town."
        "I still have no idea if I should tell Rin or not..."
        "But I can’t imagine right now being the best time either way."
        "Tearing her out of the first good mood she's been in since I found out about her darker, less lesbian secret would just be..."
        "Well, not a thing I'd want to do."
        "Basically, I don't want to be the reason she spirals out of control again."

    else:
        s "Hearing that is definitely a big deal. "
        s "Plus, even if she’s {i}not{/i} into girls, it at least means you’re kind of her type, right?"

        scene rindormbed5
        with dissolve

        r "Well...I don’t know if I’d go that far."
        r "Chika’s super into those really cutesy idol-type girls. And here I am wearing a t-shirt and basketball shorts."
        r "She’d probably take one look at me in this condition and think ‘Wow, if I were a lesbian, I totally wouldn’t want THAT girl’ or something."
        r "You know?"
        s "I don’t think I do."
        s "I like your basketball shorts, personally."
        r "Yeah, but you have a penis and it’s a reflex for you to say stuff like that when you’re in close proximity to girls."
        s "Attacking me when I am defenseless is rude."

        scene rindormbed7
        with dissolve

        r "Maybe! But it's the best time to strike!"

    "Rin pauses for a moment and sighs to herself-"

    scene rindormbed15
    with dissolve

    "And...I guess now she’s on my shoulder?"

    s "…"
    r "{i}Mm...{/i}"
    r "You know, I’m really glad I have someone like you to talk to, Sensei."
    r "It’s weird being able to chat about all of my secrets so openly without the fear of you walking away or whatever."

    scene rindormbed16
    with dissolve

    r "And sorry for suddenly using your shoulder as a headrest. It just felt like the right thing to do in the moment."
    r "If you’re uncomfortable, you can ask me to move."
    s "{i}I’m{/i} fine. If anything, I figured you would be the one uncomfortable."
    r "Why’s that?"
    s "Because you like Chika, not me."
    r "You don’t need to {i}like{/i} someone to lean on them, you know..."

    scene rindormbed17
    with dissolve

    r "Besides, it’s not like there's some kind of rule preventing you from liking two people at once, is there?"
    s "…"
    r "…"
    s "You’re not stalking {i}my{/i} Instagram, too, are you?"

    scene rindormbed18
    with dissolve

    r "Hey, you don’t even have an Instagram! I checked!"
    s "What did you even search for? You don’t know my name."
    r "I don’t need to know your name! I have my ways!"

    scene rindormbed19
    with dissolve

    r "This ain’t my first rodeo, dude. If I wanna find out more information about somebody, by golly I’m gonna do it."
    s "Please refrain from stalking me, if at all possible."
    r "I will do what I want and you won’t stop me!"

    scene black
    with dissolve

    "Rin's head does not leave my shoulder until it comes time for me to leave roughly an hour later."
    "Within that time, we manage to talk about all sorts of things."
    "But each and every one of them leads back to the one she really loves."
    "Or, at the very least-"
    "The one she {i}thinks{/i} she loves."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm25 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm30:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
    if rin_love >= 25 and rindorm20 == True and rindorm25 == False:
        jump rindorm25
...
```