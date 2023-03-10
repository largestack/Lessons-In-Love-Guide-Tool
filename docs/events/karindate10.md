# If Only (Karin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Karin love greater than or equal to 10

* Event [NTR & Pregnancy](./mollycafe1.md) (Molly) is completed)

* karinnumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: karindate10
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon
* Triggered by path: callkarinafternoon->karindate10

## Official wiki page

[If Only](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate10&go=Go) for more details.

## Event code

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label karindate10:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene karinthirddate1
    with dissolve
    play music "retrospect.mp3" fadein 5.0

    "I show up at the park to find Karin dressed a bit differently than normal."
    "This is the first time she's worn her casual clothes to a meet-up, and I have to say they suit her really well."

    ka "…"
    s "…"

    "She stands nervously before me, saying nothing and just looking off to the side, waiting for me to take the lead."
    "Which I’m fine with, of course. It’s just a vast departure from how I’ve seen her act on the soccer field."

    if bonus == True:
        "But then again, the soccer field is filled with females and I have a penis."
        "So it goes."

    s "Are you not planning on running today?"

    scene karinthirddate2
    with dissolve

    ka "Oh, umm, I...went for a run earlier. So I thought that it would be fine to just...you know, {i}not{/i} run today."
    s "I’m not keeping you from hanging out with your friends, am I?"
    s "I know you and your sister are normally out and about, so sorry if you feel obligated to waste any of that time on me."

    scene karinthirddate3
    with dissolve

    ka "What?! N-No! It's not a waste at all!"
    ka "I’m totally free today. All day. And if you’re worried about me falling behind on practice or anything then-"
    s "Yeah, I’m definitely not worried about that. You practice more than anyone."

    scene karinthirddate4
    with dissolve

    ka "R-Right..."

    "Karin nervously fidgets with her hands behind her back, digging one of her sneakers into the ground and tracing a circle with it."
    "It’s a lopsided circle- one that would cause problems in art class."

    s "Is something wrong?"

    scene karinthirddate3
    with dissolve

    ka "Nothing is wrong! Everything is great! Super great!"
    ka "I’m not hiding anything behind my back!"
    s "I didn’t say you were hiding anything behind your back."
    ka "Good! Because I’m not!"
    s "I’m starting to think you are."

    scene karinthirddate5
    with hpunch

    ka "OKAYFINEHEREYOUGO!"
    s "…"
    ka "…"

    "Karin stretches her arms out and holds a bright pink bag several inches from my face."
    "It’s easy to see how much her hands are shaking due to how close she is. "
    "This is obviously the first time she’s ever given some sort of gift to a guy but...what is it exactly?"

    s "…"
    ka "…"
    s "What is this?"
    ka "…"

    scene karinthirddate6
    with dissolve

    ka "Cookies..."
    ka "I made...extra. And I thought you might want some."
    ka "But if not I’ll just throw them into the river."
    s "There’s no need to throw anything into the river, Karin..."

    scene karinthirddate4
    with dissolve

    "I take the bag from her and lightly shake it around a bit."
    "It feels like there’s a good amount in here. I highly doubt that she just happened to make {i}extra{/i}..."

    s "You made these specifically for me, didn’t you?"

    scene karinthirddate7
    with dissolve

    ka "N-No! I made them for...my mom and dad! "
    ka "But then I realized they were on a diet!"
    ka "And I suddenly had so many cookies and I thought to myself, “Who likes cookies?!”"
    ka "And then I thought of you!"
    ka "N-Not because I was thinking about {i}you{/i} but because...E-Everyone likes cookies!"

    scene karinthirddate8
    with dissolve

    ka "And that’s exactly what happened."
    s "Well, whatever the case, I’m very thankful for them. Can I have one now?"

    scene karinthirddate3
    with dissolve

    ka "Now?! No way! Wait until you get home!"
    ka "They’re probably bad anyway!"
    ka "In fact, give them back to me. The river isn’t far away and-"
    s "I’ll just eat them tonight...Thanks."

    scene karinthirddate9
    with dissolve

    ka "Hah...my heart feels like it’s going to explode and I didn’t even do any running today."
    s "I thought you said you went running earlier?"

    scene karinthirddate4
    with dissolve

    ka "O-Oh! Right! Yes! That is exactly why my heart must be beating so fast. Definitely not because of anything else. Nope. Nothing at all."
    ka "I mean, what would even be the cause of that?"
    s "...Do you really want me to say it?"

    scene karinthirddate10
    with dissolve

    ka "Please don’t..."
    ka "I beg you..."

    "I decide to give Karin a break and not explain to her that she might just be a {i}little{/i} bit infatuated with me for some indiscernible reason."
    "I’d be lying if I said I wasn’t impressed, though."

    if bonus == True:
        "Hell, I can’t even remember the last time any of the other girls gave me a non-sexual present."
        "Not to say that I wouldn’t accept something like that from Karin (I absolutely would) but cookies are still good."
    else:
        "No one ever gives me any presents and I admire her for being able to act on something that surely made her very nervous."

    "It must have been hard for her to give these to me."

    s "Okay, so, I won’t eat your cookies now. "

    scene karinthirddate1
    with dissolve

    ka "You can always...text me how they were later if you want to."

    if bonus == True:
        ka "I mean, it would obviously be a little weird for a grown man to text some random [teenager] but..."
    else:
        ka "I mean...obviously you'd never want to because you don't have unlimited texting, but..."

        "Why does she know that?"

    ka "You know...we’ve got phones so...we might as well use them, right? Hahahah..."
    s "Right..."
    s "But anyway, what did you want to do today if you’re not going to be running?"
    ka "I-I don’t know! "
    ka "If only there was...some sort of place that two people could go to kill time and...maybe eat dinner together..."

    "I feel like the last time I suggested something like that she ran away nearly crying."
    "Has she really changed her mind about that already?"

    ka "It’s very...unfortunate that a place like that doesn’t exist...right, Sensei?..."
    ka "I wonder what else there is to do?..."
    s "Karin."
    ka "...Yeah?"
    s "Are you pretending to not know what a restaurant is?"

    scene karinthirddate11
    with dissolve

    ka "I-Is it...working?..."
    s "If you want to go out to eat, just say it."
    s "There’s no point in trying to trick me into asking you out on a date."

    scene karinthirddate7
    with dissolve

    ka "MMMMMM! Don’t call it that!"
    ka "It’s embarrassing..."
    ka "It’s just...I mean...what else are we going to do?"
    ka "I didn’t bring my other clothes and...running without a sports bra on is kinda not something I want to do right now..."

    if bonus == True:
        "I can’t say I blame her. She’s rather...endowed for a girl her age."

    s "Well is there anywhere in particular you want to go? I still have some time before I have to leave tonight."

    scene karinthirddate10
    with dissolve

    ka "Oh...Umm, right...Of course you’d have stuff to do tonight. That’s fine..."
    ka "I’m sorry for expecting you to stay with me any longer. It’s obvious you’re busy and-"
    s "Hey, now. There’s no need to get all down on yourself. We can spend an entire day together sometime in the future."
    ka "That...really does make it sound like...you know."
    s "A date?"

    scene karinthirddate12
    with dissolve

    ka "NGH!"

    "Each time I insinuate something even slightly romantic or affectionate, Karin freezes up or cringes or does...anything else mildly comedic. "
    "With a sister like Kirin, I have no idea how she's able to act like this. It's the complete opposite personality."
    "Just what the hell is going on with that family?"

    s "Okay, okay. I’ll stop using the D-word."
    ka "D-WORD?! WHO SAID ANYTHING ABOUT THE D-WORD?!"
    s "Karin, I think you might be thinking of a different D-word now."
    ka "I’M NOT THINKING OF ANYTHING LIKE THAT. I DON’T EVEN KNOW ANY D-WORDS."
    ka "DOG? ARE YOU THINKING OF DOGS?"
    ka "DOGS ARE GREAT, AREN’T THEY, SENSEI?"
    ka "AM I YELLING AGAIN?!"
    s "Do you have an inhaler or something? It looks like you’re having a little trouble breathing."

    scene karinthirddate10
    with dissolve

    ka "Talking to you makes my chest hurt...I don’t like it."
    s "And yet you continue to hang out with me."
    ka "I even baked you cookies."
    s "I thought you baked those for your mom and dad?"
    ka "I did."
    s "But you just said-"
    ka "No I didn’t. "
    s "…"
    ka "…"
    s "Okay. Let’s just find somewhere nearby and get something to eat since you’ve apparently never been to a restaurant before."

    scene karinthirddate13
    with dissolve

    ka "Y-Yeah! Let’s d-d-d-d-do that! That sounds really f-f-f-f-f-f-f-f-"
    s "Just let me do the talking, okay?"

    scene black
    with dissolve2

    "Karin and I walk through the streets toward...well, anywhere."
    "She remains extremely tense the entire time."
    "And I mean extremely tense. It looks like every joint in her body has frozen up. "
    "But even though she’s struggling to maintain her composure, she follows gleefully alongside me and we eventually stop at a rather familiar place..."

    scene karinthirddate14
    with dissolve

    ka "…"
    s "…"
    ka "So umm...cafes...am I right?"
    s "Well, you are right in noticing that this is a cafe. Good job."
    s "I have to apologize in advance for something, though."

    scene karinthirddate15
    with dissolve

    ka "Apologize?! Did I do something wrong?!"
    ka "It’s too soon for us to go somewhere like this together, isn’t it?! "
    ka "I had no idea! I’m still really bad at this...I-I...I’ll do more research! I swear!"
    s "No, no. It’s nothing like that."
    s "There’s just one of my students here right now and I’m pretty sure that the two of us are going to be grilled in a matter of seconds."

    scene karinthirddate16
    with dissolve

    ka "For being seen together?..."
    s "Something like that..."

    scene karinthirddate17
    with dissolve

    ka "Oh...yeah. I’m sorry..."
    ka "Of course something like that would happen."

    "Frankly, I knew this was going to be a risk when the two of us came here. "
    "But I live for danger."
    "Just kidding. I live for cute girls. "
    "And I also want to see how Karin will act when she’s thrown into the fire."
    "Godspeed, co-captain."

    scene karinthirddate18
    with dissolve

    mo "Well, well, well...what do we have here?"
    mo "You bring a girl from our[school] into {i}my{/i} cafe? During {i}my{/i} shift?"
    mo "Is this some sort of test? What's your game here, Sir?"
    ka "Umm...Hey there. My name’s-"

    scene karinthirddate19
    with hpunch

    mo "SILENCE, WENCH!"
    ka "Oh. Uhh, okay. My bad..."

    scene karinthirddate20
    with dissolve

    mo "Sir. What is the meaning of this new character? How large is this pool of [young_girls] going to grow?!"
    mo "How do you expect to develop all of them?! Focus on the ones you have first!"
    mo "Can’t you see what Ireland has to offer?! Can’t you see me?!"
    s "Molly, this is Karin. She’s the co-captain of the[school] soccer team. "
    mo "This does not explain why you two are chatting over tea and crumpets."
    s "We haven’t even ordered anything yet."

    scene karinthirddate21
    with dissolve

    ka "We were just...practicing in the park and worked up an appetite."
    ka "Sensei recommended this place because of how much he likes it, so...I thought I’d give it a go too..."
    ka "Sorry if it seems like I’m intruding..."
    s "…"

    "How is Karin lying so naturally right now? I didn’t think she’d be the type to do something like that."
    "I don’t even need to think up an excuse now."
    "This is great."

    mo "Hmm...Well, at least you are polite."
    mo "But I have to say, I’m quite concerned by the size of your breasts. "
    ka "...I'm sorry?"
    mo "What are they? Double D’s? Triples?! Explain yourself!"
    ka "That’s...not something I’d like to discuss right now..."
    mo "Tch!"
    mo "You well-endowed women are all the same. Never wanting to discuss your sizes and leaving us flat girls to ROT in MISERY!"

    scene karinthirddate22
    with dissolve

    mo "YOU WILL BURN FOR YOUR SINS! BOTH OF YOU!"

    scene karinthirddate23
    with dissolve

    ka "…"
    s "…"
    ka "…"
    s "…"
    s "Yeah, so that’s what I was apologizing for."
    s "Molly doesn’t take too kindly to unexpected girls showing up and joining the harem."

    scene karinthirddate24
    with dissolve

    ka "Harem?!"
    s "That’s what she calls it at least. I think she wants to be recognized."
    ka "HAREM???????"
    s "...It was a joke."

    if bonus == True:
        "It wasn’t."
    else:
        s "As clear as it is than many of my students have feelings for me, I am simply not interested in any of them that way."

    scene karinthirddate25
    with dissolve

    ka "Phew..."
    ka "Hearing that made me a lot more...umm..."
    ka "Actually, never mind."
    ka "I never started that sentence."
    s "Agreed. You never started that sentence and we will do our best to avoid it coming up again in the future."
    s "So, are you ready to order?"

    scene karinthirddate26
    with dissolve

    ka "Oh! Almost! I just need a little more time to look at the menu if you don’t mind..."
    ka "I’m surprisingly picky when it comes to food. I still cut the crusts off of my sandwiches and everything."
    ka "I don’t know why I’m telling you this. Please stop me before I continue to embarrass myself."
    s "No, no. Please tell me more about how childish you are. It’s cute."

    scene karinthirddate27
    with dissolve

    ka "C!"
    ka "C-C-C-C-C-C-C-C!"

    scene black
    with dissolve2

    "Karin breaks again and takes a full five minutes to snap out of her cute-coma."
    "That’s what I’m going to call those moments from now on."
    "Is it really that hard for her to handle being complimented?"
    "You’d think that by now she’d at least be able to dodge the word or brush it off but...nope."
    "It is what it is, though."
    "The two of us wind up ordering coffee and a couple of sandwiches shortly after that."
    "They come on rolls, so Karin does not need to go through the trouble of removing the crust from hers."
    "Once we finish eating, we say our goodbyes and part ways in front of the cafe."
    "I think I can hear her squeal to herself in joy as she runs off toward home."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karindate10 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label karindate15:
...
```

## Code that triggers this event

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
    if karin_love >= 10 and mollycafe1 == True and karindate10 == False:
        jump karindate10
...
```