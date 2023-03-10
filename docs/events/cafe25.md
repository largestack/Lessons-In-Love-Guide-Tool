# Good Day, Humans (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 25

* Event [Delirium](./rindorm20.md) (Rin) is completed)

* Event [The Queen of Spiders](./amisroom5.md) (Ami) is completed)

* Event [Girl-Talk](./day65.md) (Main) is completed)



## Next events

* [Main: The Value of Sharing](./halloween1.md)

## Event properties

* Id: cafe25
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe
* Triggered by path: cafe->cafe25

## Official wiki page

[Good Day, Humans](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe25&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe25:
    scene gooddayredux1
    with dissolve
    play music "cafe.mp3"

    "Another morning at the cafe means another chance to be poisoned by an overly creative and mildly intimidating barista."
    "But upon entering, I realize that Rin isn’t behind the counter."
    "In fact, {i}no one{/i} is behind the counter."
    "No one is in the cafe at all..."
    "What exactly is going on here?"

    r "Hey, {i}loser.{/i} Can’t you read?"

    scene gooddayredux2
    with dissolve

    s "What's going on? Where is everyone? Also, don't call me a loser."
    r "I'll call you whatever I want to call you, loser. And what, was the big sign on the door saying we're closed today not enough to tip you off?"
    s "Why are you closed? It's just a random weekend."
    s "Also, why are you here if you're closed? And why are you wearing your casual clothes?"
    r "Damn, Sensei. Didn't realize we were gonna be playing twenty questions today. You know you can just ask me what color my underwear is, right? You don't have to beat around the bush."
    s "Wait, I can?"

    scene gooddayredux3
    with dissolve

    r "No. But I thought I'd be a good friend and give you some hope since I can't give you any coffee today."
    s "What good is hope if you're just going to take it away immediately?"
    r "I don't know, homie. Ask the Rin floatin' around in your fantasies later. She'll probs know better than I do."
    s "...Homie?"
    r "Sorry. I meant to say Sensei. I mix those two words up all the time."
    s "I feel like that would be mildly problematic if you had literally anyone else as a teacher."
    r "Well, I guess I'm lucky I ended up with you then, huh?"
    s "I guess so..."
    s "For real, though. Why are you closed?"

    scene gooddayredux4
    with dissolve

    r "Repairs or something, I think. Wasn't really informed of the full details."
    r "All I know is that Haruka needed somebody to come in and tidy stuff up before the repair people came and I just happened to have some extra time on my hands this morning."

    scene gooddayredux3
    with dissolve

    r "Lucky for you, I've got even {i}more{/i} spare time now since I've already finished up everything that needed to be done."
    s "Do you mean we're actually going to spend the morning together with you {i}not{/i} in that funny visor?"

    scene gooddayredux5
    with dissolve

    r "Woah, there! What did my visor ever do to you? You can't just talk crap on it like that."
    s "I blame the lack of caffeine. So, in a roundabout sort of way, it's actually your fault I said that."

    scene gooddayredux6
    with dissolve

    r "Well, I don't follow that logic at all. But if you want coffee, we can get some on the way. There are plenty of cafes between here and the urban district."
    s "What? We're going all the way over there?"

    scene gooddayredux2
    with dissolve
    stop music fadeout 10.0

    r "Hell yeah, man. I wanna walk around the city."
    r "I haven’t been getting out much lately and I need some exercise before my limbs fall off or stop working or something."
    s "Neither of those things happen due to lack of exercise but sure, I guess I’ll walk around with you."
    r "Neat! Well, I'm ready whenever you are."
    r "Oh, and the answer was black, by the way."
    s "The answer to- oh."

    scene gooddayredux3
    with dissolve

    r "You're welcome, homie."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene gooddayredux7
    with dissolve2
    play music "justbehappy.mp3" fadein 4.0

    "Rin and I spend some time walking around the more...{i}metropolitan{/i} section of Kumon-mi."
    "It's not one I venture too often, so I wind up sticking close to her as she leads us...well, wherever she's in the mood to lead us, I guess."
    "So far, that has equated to nothing but anime stores where she proceeded to freak out about the prices of things before getting upset and leaving."
    "This has happened five times now and I still do not have any coffee."

    scene gooddayredux8
    with dissolve

    r "Who shoved a stick up your butt, Mr. Crankypants?"
    s "..."
    s "Excuse me?"
    r "You've barely said anything since we left the cafe. Am I {i}boring{/i} you, Sensei?"
    r "Or are you just a little embarrassed to be walking around with a moderately cute girl?"
    s "I'd rank you several levels above moderate, Rin."
    r "Why, that's the nicest thing anyone has ever said to me. Thank you, Sensei."
    s "You're welcome. Can I get coffee now?"

    scene gooddayredux9
    with dissolve

    r "Oh, crap! I totally forgot!"
    r "Why didn’t you say anything sooner?!"
    r "I even dragged you into that one anime store that you were totally uninterested in!"
    s "It was five."
    r "Five?! Why did you let me carry on for so long?!"

    scene gooddayredux10
    with dissolve

    r "You need to be more open about your needs, Sensei."
    r "If this relationship is ever going to work, we're going to have to keep each other in check."
    s "Using the word {i}relationship{/i} makes it sound like we're more than just friends, you know."

    scene gooddayredux11
    with dissolve

    r "But...we are, aren't we?"

    "Rin pauses for a moment as her face begins to redden and her eyes get locked on mine."
    "I know this face. She’s about to confess her-"

    scene gooddayredux12
    with dissolve

    r "Homies."
    s "…"
    r "…"
    s "Why do you keep saying that all of a sudden?"
    r "What?! You said we're just friends, but we're so much more than that! Homies are like...four steps above friends."
    r "But I guess you probs wouldn't know that since you're such a friggin' boomer."
    s "Why am I being bullied today? All I wanted was coffee."
    r "And all I want is a cute gyaru girlfriend with fishnets and a cell phone addiction."
    r "I guess we can't always get what we want, though, can we?..."

    scene gooddayredux8
    with dissolve

    r "Buuuuut...since I’m the greatest and coolest homie in the entire world, we can stop for coffee at the next cafe we see."
    r "And I just so happen to know a pretty good place right around the corner and-"

    scene gooddayredux13
    with hpunch

    r "Ah-!"

    "Rin suddenly stops walking when something catches her attention."

    r "Holy shit."
    r "Holy shit. Holy shit. Holy shit."
    s "What? What's wrong?"
    r "We..."
    r "We have been graced by the presence of an angel..."

    scene omgkaori1
    with fade

    "Rin lunges forward toward the {i}angel{/i} who is none other than the Queen of Spiders herself- Kaori."
    "I'm surprised to see this sort of reaction out of her, though."
    "I get that Rin is {i}incredibly{/i} attracted to girls, but the way she's acting toward Kaori makes it seem like-"

    r "Oh my god! No friggin’ way! Kaori?! Is that really you?!"
    k "H-How do you know my name?! Who are you?!"
    k "Identify yourself!"
    s "Uhh...what’s going on here, exactly?"

    scene omgkaori2
    with dissolve

    k "Hamburger Man! Help! I am under attack!"

    scene omgkaori3
    with dissolve

    r "...Hamburger Man?"
    s "It’s better to not ask."
    s "How are you doing, Kaori?"
    k "Horrible! I require immediate assistance and will pay you in meat for the favors you will perform today!"
    s "And what exactly do you need immediate assistance with? You’re not actually under attack."

    scene omgkaori4
    with dissolve

    k "I’m...not under attack?"
    s "Of course not. Rin's just a mildly annoying, extraordinarily horny teenager."
    r "It's true. I really am."
    s "Rin, would you mind explaining how you know Kaori? Because she...definitely does not seem like she knows you."
    s "Was she your waitress before or something?"

    scene omgkaori5
    with dissolve

    r "Waitress? Are you kidding? She’s like, a totally famous Instagram model!"
    k "A...what?"
    k "What is this ‘instant gram’ you speak of, extraordinarily aroused girl? Explain yourself."

    scene omgkaori6
    with dissolve

    r "Sensei, remind me to show you her page later! She takes tons of super cute pictures of all kinds of stuff."
    s "I'm good. Not really big on social media."

    scene omgkaori7
    with dissolve

    k "Media can talk?!"
    r "You sure? There's a bunch of risque underwear pics on there that you'll be missing out on..."

    if bonus == True:
        s "My interest in this conversation has suddenly skyrocketed."
    else:
        s "Keep them away. I want no part of this."

    k "What does that strange word mean? {i}Risque?{/i}"
    s "It means sexy."
    k "Sexy?! Tell me it is not so, Hamburger Man!"
    s "Rin, how risque are these photos exactly?"
    k "Why do you not show more concern for my well-being when I am in a clear state of crisis?!"
    r "There aren't like, nudes or anything. Just some closeups of her tattoo and a bunch of pictures of her trying on different types of underwear."
    k "This can not be true! I do not even know what an instant gram is! "
    k "The only pictures I have inserted into the digital world have been for the sake of personal documentation of my journey through this planet!"

    scene omgkaori9
    with dissolve

    r "Wait...I kinda feel like you’re being serious right now."
    r "You haven’t actually been...posting all of those pictures on accident, have you?"
    s "Are we really not going to question why she’s been taking pictures in her underwear for ‘personal documentation?’"

    scene omgkaori10
    with dissolve

    k "Whose team are you on, Hamburger Man?!"

    if bonus == True:
        s "I’m on the team that wants to see those pictures."
    else:
        s "Whichever team is closest to the parking lot. I get embarrassed after playing sports and like running away as soon as games end."

    k "Those pictures are not to be seen by the prying eyes of a human male such as yourself!"

    scene omgkaori11
    with dissolve

    if bonus == True:
        k "Even if you are a prime mating specimen who I am extraordinarily attracted to!"
    else:
        k "Even if you are extraordinarily attractive!"

    r "Ah-"
    s "…"
    k "…"
    r "…"
    k "What?! What is the reason for this sudden silence?!"
    k "I am not yet familiar with human conversation! Is openly discussing mating rituals not acceptable behavior?!"

    scene omgkaori12
    with dissolve

    if bonus == True:
        r "Sensei...I think Kaori wants to...{i}mate with you...{/i}"
    else:
        r "Sensei...I think Kaori has a crush on you..."

    k "I...I said no such thing!"

    scene omgkaori13
    with dissolve

    r "Can I...maybe...watch?"
    k "You may watch nothing! You are already aroused enough! Any more will result in spontaneous combustion!"

    if bonus == True:
        s "I don't mind if you watch, Rin. Kaori and I are ready to mate whenever."
    else:
        s "I also do not understand what she wants to watch. You can not {i}see{/i} people have feelings."

    scene omgkaori15
    with dissolve

    if bonus == True:
        k "I will not mate with you, Hamburger Man! I have yet to even discover what the instant gram is!"
    else:
        k "I do not have feelings!"

    k "Too much remains undone! My body is simply not prepared!"
    r "Kaori...wants you...to prepare her body..."

    scene omgkaori17
    with dissolve

    k "You should be referred to as the extraordinarily dishonest girl instead! The lies drip from your mouth like water from a leaky faucet!"
    r "Sensei...what will you do?"

    menu:
        "Prepare Kaori’s body":

            $ kaoriprepared = True

            s "I suppose I’ll have to do what must be d-"

            scene omgkaori18
            with dissolve

            k "You will do no such thing!"

        "Don’t do that thing":

            $ kaoriprepared = False

            s "I’m not sure if she’s ready yet, Rin..."
            r "Maybe...{i}I{/i} can help her get ready then?..."

            scene omgkaori19
            with dissolve

            k "Do not come near me, heathen!"

    scene omgkaori20
    with dissolve

    k "Why must so many confusing things happen today of all days?!"

    scene omgkaori21
    with dissolve

    r "Is something wrong, Kaori? Are you having a bad day?"
    k "The worst day. The woman at the pet store would not provide me a furry companion to nurture and call my own!"
    r "Why not? Did you not have enough money or something?"
    k "I have many of the moneys! And yet each attempted transaction was refused!"
    k "There is no justice in this world!"
    s "Just find an animal outside. There are plenty of them just...wandering around."

    scene omgkaori22
    with dissolve

    k "But they are so fast and I am so average-speed. I simply can not keep up."
    s "I...really don't know what else to tell you, Kaori."

    scene omgkaori23
    with dissolve

    k "Of course you do, Hamburger Man..."
    k "And yet you conceal your vast amounts of human knowledge from me."
    s "I..."
    s "What?"
    k "I do not trust you."

    if bonus == True:
        k "And I will not mate with you."

    k "And I will now leave."
    k "Good day, humans."

    scene omgkaori24
    with dissolve

    r "…"
    s "…"
    r "She’s...{i}different{/i} from how I expected her to be."
    s "Yes, Rin."
    s "Yes she is."

    scene black
    with dissolve2

    "Shortly after that, we obtained my normal human coffee and-"
    "Oh, god damn it."
    "Now even I’m beginning to sound like Kaori."
    "We bought coffee and then I walked Rin back to the dorm."
    "The end."

    $ renpy.end_replay()
    $ cafe25 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label cafe30:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
...
```