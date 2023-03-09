# The Gap in the Door
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikadate45&go=Go)



## Event preconditions
✅Chika love greater than or equal to 45

❌Event "[Chika: The Gap in the Curtain](./mall40p2.md)" is completed (event=mall40p2)

✅chikanumber equal to True (unknown variable)



## Next events
* [Main: Three Amigos](./christmastwo1.md)

## Event properties
* ID: chikadate45
* Group: Chika
* Triggered by label: callchikamorning
* Triggered by branch label: callmorning

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label chikadate45:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "And, since it’s still early in the day, I figure that meeting up with her now will give her the chance to {i}not{/i} have to monitor her instinct to always act like we’re the world’s cutest couple."
    "She’s been having to do a lot of that lately. And...let’s just say that I’ve been a little closer to feeling bad than I normally am after telling her to tone it down."
    "A break can be good for everyone."
    "Depending on the {i}type{/i} of break, of course. Because I’m pretty sure if I asked Chika to take a {i}real{/i} break, all hell would break loose."
    "But that’s enough iterations of the word “break” for the moment. "
    "Here’s hoping she’s awake, I guess."

    play sound "phonebeep.wav"

    c "Hey! Good morning!"
    s "Hey. You sure seem lively for someone who probably just woke up."
    c "Chinami wanted waffles, so I had to run over to the store to get stuff for them."
    s "Stop letting her control your life. If you don’t want to make waffles, don’t make waffles. It’s as simple as that."
    c "Do you...have something against waffles, Sensei?"
    s "I have something against eternal kindness. And waffles just appear to be the connection between that and you this morning."
    c "Do you want me to be meaner to Chinami or something?"
    ch "{i}Who wants to be mean to Chinami?! She wants to give them a piece of her mind!{/i}"
    c "Shush. Eat your waffles."
    ch "{i}Okay! I love you, big sister!{/i}"
    c "Do you hear that? {i}That’s{/i} who you want me to be mean to."
    s "I never said-"
    s "You know what, forget it. Are you busy this morning?"
    c "Nope!"
    s "Sweet."
    c "Mhm. I guess it is pretty sweet."
    s "..."
    c "..."
    s "This is the part where you’re supposed to invite me over."
    c "Is it? I wasn’t sure if that would be moving too quickly."
    s "..."
    c "Sensei! It was a joke! Of course you can come over."
    c "I’m not making you waffles unless you bring more ingredients, though."
    s "I think I’m okay without waffles. I’ll see you soon."
    c "We’ll be here!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and start getting ready to head to Chika’s place."
    "When I make it to the second half of town, I see a surprising amount of its inhabitants showing a bit more life than they normally do at this time of day."
    "Upon trying to come up with a reason for their sudden shift in behavior, I decide to go with the simple fact that the seasons are changing."
    "And that, soon enough, they’ll be wandering around in search of shade or shadows instead of fire. "
    "Good luck, old district. I wish you the best in your endless battle against death and nature. "
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene controversialscene1
    with dissolve2
    play music "love.mp3"

    "I step into the Chosokabe apartment to find absolutely no one."
    "Could it be that Chika was so torn up about me asking her to slow down that she took her sister and moved to some far away land?"
    "And, if that’s the case, why did she invite me here? Is this all just to inconvenience me?"
    "That bitch."

    play sound "water1.mp3"

    c "In here, Sensei!"
    s "The bathroom?..."
    c "Don’t worry! It’s safe to come in."

    if bonus == True:
        jump chinamibrx
    else:
        scene black
        with dissolve

        "I make my way into the bathroom and, to my great surprise, there are chickens again."

        s "Why does this keep happening?"
        ch "It's Chicken Day, Papa! Here! Take one!"

        "Chinami hands me a chicken."

        s "Thank you."

        "I accept the chicken."
        "We all dance around in circles for a little while before the chickens have to go home, then the event continues."

        jump restofchinamibr

label restofchinamibr:
    scene controversialscene14
    with dissolve2

    "Chinami jumps onto the bed next to me, wearing nothing but an oversized t-shirt, before gazing into my eyes with a look that essentially screams, “I am secretly evil.”"

    c "Chinami, come on. That’s my spot."
    ch "Chinami wants to know what your intentions are with her big sister."
    s "Chinami should mind her own fucking business."

    scene controversialscene15
    with dissolve

    ch "Did you just curse at Chinami?! You can’t do that!"
    ch "Go put all of your money in the swear jar!"
    s "Do you actually have one of those things?"
    c "Why else do you think Yumi is so poor?"

    scene controversialscene16
    with dissolve

    c "Oh crap. I can’t believe I just made that joke. I’m sorry, Yumi. If it makes you feel any better, I’m also poor."
    ch "While big sis Chika apologizes to the air, Chinami demands that you be nicer to her in the future."
    s "To you? Or to your sister?"
    ch "Yes."
    s "Oh."
    s "Well, uhh...okay."
    ch "Good."
    ch "Chinami will give back her sister’s spot now, but she’ll be watching you..."
    s "Sure, Chinami. And I’ll make sure to drop a coin in your swear jar the next time I have cash on me."

    scene black
    with dissolve2

    "Chinami gets off the bed and, within a matter of seconds, Chika stops apologizing to the spirit of Yumi for calling her poor and lays down beside me."
    "She rests her head on my lap and talks a little about how she really doesn’t want to go into work later because of the holiday rush, and I sit there the same way I always do and pretend to be interested."
    "Before long, though, the conversation begins to die down and more gaps begin to form- ones even larger than the half-open bathroom door that she and her sister emerged from just a short while ago."
    "But I guess there have been plenty of gaps forming between us as of late."
    "Gaps between what we want to do and what we have to do."
    "Gaps between what we {i}actually{/i} do and what we struggle to."
    "Gaps in our own personal mindsets as they sink further into a pit that will be near impossible to climb out of if neither one of us has climbing equipment."
    "Chika didn’t bring hers as she believed me to be some sort of experienced climber."
    "And I am."
    "But the truth is that I don’t even know how to use my equipment."
    "And, at this point, I don’t know if it’s even worth the effort to learn."

    scene controversialscene17
    with dissolve2

    "The biggest gap of all is one of consciousness as Chika passes out on my lap."
    "I don’t mean to, but somewhere along the line, I rest my hand on her head and begin stroking her hair."
    "It’s slightly damp, so I’m able to figure out that she took a bath before Chinami."
    "But, with that {i}and{/i} a trip to the store...just how early did she have to wake up?"

    scene controversialscene18
    with dissolve

    ch "..."
    s "..."
    s "Yes, Chinami?"
    ch "Nothing."
    ch "Chinami is just happy you’re here."

    scene controversialscene19
    with dissolve

    ch "Big sis hasn’t been sleeping much lately. But she was able to fall asleep on you right away."
    ch "She must really, really like you."
    s "..."
    s "Yeah. She must."

    scene controversialscene20
    with dissolve

    ch "Can Chinami tell you a secret?"
    s "Chinami is probably going to tell me anyway, so yeah."
    ch "Well, last night, Chinami woke up in the middle of the night because she was thirsty, but she never got out of bed."
    s "What a fascinating secret. Thank you, Chinami."
    ch "No, no. You don’t understand."
    ch "Chinami didn’t {i}want{/i} to get out of bed because her sister was crying."

    scene controversialscene21
    with dissolve

    ch "So she just pretended to stay asleep and hugged her instead."
    s "..."
    ch "..."
    ch "Did you two get into a fight?"
    s "..."
    s "Something like that."
    ch "Does this mean you’re going to stop coming over?"
    s "No, it doesn’t."

    "Not...now, at least."
    "I have no idea what’s going to happen in the future-"
    "Or what other gaps will form."

    ch "That’s good."

    scene controversialscene22
    with dissolve

    ch "Chinami likes when you’re here. And she doesn’t want to hear her sister cry anymore."
    s "Do you have to hear that often?"
    ch "Not really."
    ch "Not since Mommy died."
    ch "But Chinami thinks big sis Chika will stop crying as much if you tell her you love her."
    s "..."
    ch "Or give Chinami a little sister."
    s "Okay, stop that."
    ch "Chinami will convince you one day."
    s "If Chika had a baby, it wouldn’t even be your sister. It would be your [niece]."

    scene controversialscene23
    with dissolve

    if bonus == True:
        ch "Chinami would be an aunt?!"
        s "Yes. And you’re way too young to be an aunt."
    else:
        ch "What?! How does that work?!"
        s "It just does. Don't question it."

    ch "This is a really sticky situation!"
    s "That’s right. So, for everyone’s sake, please stop asking me to have a baby with your sister."

    scene controversialscene24
    with dissolve

    ch "Fine! But Chinami isn’t happy about it!"
    s "Chinami seems to very rarely be happy about anything I do."

    scene controversialscene25
    with dissolve

    ch "Then make it up to her by not letting big sis cry anymore."
    ch "Chinami can only do so much to cheer her up all alone. She needs your help."
    s "..."
    ch "..."
    s "I’ll see what I can do..."

    scene black
    with dissolve2

    "Chinami lays down beside her sister and falls asleep as well."
    "Next thing I know, I’m surrounded by two lightly breathing, unconscious blondes and unable to figure out a way to escape this situation."
    "Not that it’s a bad one, just...not how I imagined my morning going."
    "But, I guess there are more ways to ensure that these two get a good night’s sleep than just buying them a brand new bed."
    "Or...good morning’s sleep."

    s "..."

    "I’ll just hang around here until they wake up, I guess."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chinami_love += 1
    $ chikadate45 = True
    stop music fadeout 8.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "{i}Both sisters wake up a few hours later and you’re able to get on with the rest of your day...{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label chikalust25skip:
    scene poorgirldoggystyle1
    with dissolve

    c "So, now what? "
    c "We’ve got like forty-five minutes before we need to start heading over to the next contest. And I’m pretty sure the Tsukioka kitchen staff is setting up a buffet for everybody before that happens."
    c "If you don’t have anything else going on, want to head over there with me? "
    c "Or would you rather I walk ten steps behind you the whole way so no one gets any ideas about us dating? Which is a thing we are totally not doing."
    s "Chika-"
    c "Fine, fine. Twenty steps. But that’s my final offer."
    s "I think we can manage to walk to whatever fancy dining hall the Tsukiokas have without anyone thinking we are having sex."
    c "Sex? Me? Nuh-uh. Not until marriage, Sensei. But I {i}guess{/i} I can find the time to accompany you to the buffet."
    s "You {i}guess?{/i} You’re the one who invited me."
    c "Only because I feel bad that you’re all alone, obviously. It doesn’t have anything to do with that fact that I, the reigning Dorm Wars date champion, have barely gotten to spend time with you the last couple days."
    s "You do realize there is a new champion, right?"
    c "Sure, but...come on. We all know who the {i}real{/i} champion is."
    c "Hint, {i}it’s the one who lets you cum inside of her.{/i}"

    if datewarfutaba == True:
        "{i}That does not help narrow it down...{/i}"

    scene black
    with dissolve2

    "Chika and I exit whatever room I was kidnapped and tossed into and I am forced to follow her on account of having no idea where I am."
    "Sure, I’ve toured at least part of the place before, but when your house is so big that it requires a GPS to get around, it’s easy to find yourself being completely and utterly lost."

    c "Oh, we have to go left down the next hallway in order to make it to the dining hall?"
    s "How do you even remember that? This place is only half a step away from being a full-on maze."
    c "Hm? Did you not download the Tsukioka Manor app? There’s a whole map built in."

    "Oh. So I guess it actually {i}does{/i} require a GPS to get around."
    "Regardless, we make it to the dining hall after a five minute walk and spend the next half hour gorging ourselves on food we can not pronounce until it is finally time to leave..."

    $ yumi_love += 1
    $ nodoka_love += 1
    $ chikalust25skip = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo14

label chikalust25:
...
```

## Code that triggers this event
File: \game\ChikaEvents.rpy
Code:
```python
...
label callchikamorning:
    if onsenticket == True and streets30 == True and day == 6:
        jump chikaonsen1
    if chika_love >= 45 and mall40p2 == True and chikadate45 == False:
        jump chikadate45
...
```