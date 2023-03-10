# True Power: Unleashed (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 20

* Event [Schadenfreude](./chikadorm20.md) (Chika) is completed)



## Next events

* [Chika: Detention](./day139.md)

## Event properties

* Id: mall20
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall
* Triggered by path: mall->mall20

## Official wiki page

[True Power: Unleashed](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mall20&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall20:
    scene mall2
    with dissolve
    play music "mall.mp3"

    "I show up at the mall around the usual time and head directly over to Chika’s store when I notice she’s not on her normal bench."
    "The only issue is...she’s not at the store either."
    "Instead, some random girl around the same age as me is. Chika’s manager, maybe?"
    "Either way, I'm forced to look around the store for a few minutes so that it doesn't seem like I'm just some random guy who came in looking for a specific [teenage]girl."
    "And {i}now{/i} I’m forced to look around the mall to find Chika...if she’s even here."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene mall1
    with dissolve

    s "Huh...No Chika anywhere to be found. "
    s "Maybe she’s just off today?"

    "Chika having the day off is a thought that never even crossed my mind. "
    "I mean, she’s been here virtually every weekend since I woke up in Kumon-mi."
    "But I guess that even scripted events sometimes-"

    c "Okay, Chinami. Remember what I told you?"
    s "Hm?"

    scene chinamisphone1
    with fade

    chd "No talking to strangers!"
    c "Good girl. And what else?"
    chd "No microtransactions!"
    s "What’s going on here?"

    scene chinamisphone2
    with dissolve

    c "Hm? What do you-"

    scene chinamisphone3
    with dissolve

    c "Oh, Sensei! I didn’t expect to see you here so late in the day."
    s "Late in the day? It’s basically the same time it always is when I show up."
    c "That’s not true. It’s like, almost thirty minutes later."
    s "That’s only because I’ve been scouring the place looking for you."

    scene chinamisphone4
    with dissolve

    c "Oh, crap! I totally forgot to tell you I have the day off today."
    s "If you have the day off, what are you doing at the mall?"
    chd "Chinami is getting a phone!"

    scene chinamisphone5
    with dissolve

    c "Yup. Just like she said, I caved and I’m letting her get a phone."
    c "She’s been having to stay at home alone a lot more lately and I figured it would be good for her to be able to keep in touch with me at all times of the day."
    c "Especially since our house-phone was just deactivated and stuff."
    s "Deactivated? Why?"

    scene chinamisphone6
    with dissolve

    c "Money, obviously."
    c "Adults have so many bills that it’s kinda hard to keep up with all of ‘em."
    c "So when I missed the payment for the landline I figured I could just add Chinami to my cell-plan."

    "I figured it was something along those lines. I honestly feel a little foolish for even asking."
    "It makes sense that she’s not able to keep up with all of her bills just working part-time at a boutique in the mall."
    "Hell, it would probably be hard no matter how many hours she worked here every week."

    s "How much is it to add Chinami to your plan?"

    scene chinamisphone7
    with dissolve

    c "I looked it up online and I think it was somewhere around another 4,000 yen. And I imagine that will go up a bit after convenience fees or whatever."
    s "And you’re able to afford that?"

    scene chinamisphone6
    with dissolve

    c "I don’t really have a choice. It’s either fork over another 4,000 yen or leave my sister high and dry in the event of an emergency."
    s "…"
    c "...What? Why are you looking at me like that?"

    "I think it’s time to activate good-person mode for the week."
    "I figure I might as well get my one good deed out of the way while I have the chance to."

    s "Chika."
    c "Sensei."
    s "Let me pay your phone bill from now on."

    scene chinamisphone8
    with dissolve

    c "What?! Absolutely not. There’s no way I could let you do something like that."
    s "Why not? I make significantly more money than you."
    c "Well, duh. You’re a teacher and I’m a [teenage]girl working at the mall."
    c "But that doesn’t mean you should be friggin’ payin’ my bills for me and stuff."
    s "Just think of it as an early Christmas present or something."
    c "What kind of crazy Christmas present is a whole friggin’ phone plan?"
    chd "Chinami likes this idea! "

    scene chinamisphone9
    with dissolve

    c "Chinami, you stay out of this. This is between me and Sensei."
    chd "Woof!"

    scene chinamisphone10
    with dissolve

    "Chinami barks and sends Chika into emotional overload as she shows a rare moment of defeat, taking a deep breath as she closes her eyes."

    c "Listen...I’m flattered that you would even offer something like that...But this is {i}my{/i} problem."
    c "And besides, I’m already paying for half of Yumi’s bill as well. She’s on my plan, too."
    c "Yeah, an extra 4,000 yen a month is kind of rough for me, but I’ll figure something out."
    s "Why are you even trying to argue this? I’ve already made my decision."

    scene chinamisphone11
    with dissolve

    c "Your decision sucks. And it’ll make me feel like, a trillion times worse about everything."
    c "There’s literally nothing I’d be able to do to pay you back."
    s "You don’t need to pay me back. I wouldn’t be offering this if I didn’t want to do it."

    "Plus...there’s absolutely no way I could put Chinami in a situation like that. "
    "If she’s going to be alone, I’d be a lot more comfortable knowing she has a reliable service plan."

    scene chinamisphone12
    with dissolve

    c "Sensei...It’s fine. Really. I’ll figure it out."
    s "I’ve already figured it out. I’ll pay for you, Chinami, {i}and{/i} Yumi."
    s "I’m already paying for Ami’s bill. A few more won’t make much of a difference to me, but it’s a world of difference to you."
    s "Use that money to buy more food or something. You guys deserve it."

    scene chinamisphone13
    with dissolve

    c "Stop trying to be so cool in front of my little sister."
    s "I’m trying to be cool in front of you, too, you know."
    c "I already think you’re really cool, though."
    s "But I bet you think I’m even cooler now, right?"
    c "I don’t know. What do you think?"
    chd "Chinami thinks she doesn’t care who pays! She just wants a phone!"
    c "Quiet, Chinami. "
    chd "Woof!"

    scene chinamisphone14
    with dissolve

    c "You’re really okay with doing something like this for me?"
    s "Of course."
    c "And you’re not gonna try and extort me for something or whatever, right?"
    s "Uhh...That wasn’t something I was planning on, no."
    c "And Yumi, too?"
    s "Yumi, too."
    s "It would probably be best not to tell her about it, though."
    s "I feel like she’d throw her phone into the river if she found out I was the one paying for it."

    scene chinamisphone15
    with dissolve

    c "That’s sad because it’s true. "
    s "It really is..."

    scene chinamisphone16
    with dissolve

    c "Heheh..."
    c "Chinami, can you cover your ears for a second?"

    scene chinamisphone17
    with dissolve

    chd "Chinami isn’t sure if this will do anything, but she will listen to her sister!"
    c "Good girl, Chinami. "
    chd "Woof!"
    c "Sensei. Can you come here for a sec?"

    scene chinamisphone18
    with dissolve

    s "What’s up?"
    c "Are you really sure you’re okay with this?"
    s "Of course."
    c "And you don’t expect anything in return?"
    s "Nope. Just doing my good deed for the week. "
    c "I think a deed this good counts for the whole year."
    s "That’s even better. It means I can go back to being an asshole again after this."
    c "Hahaha, yeah, I guess it does."
    s "So, I’m assuming the store right behind you is the one where-"

    scene chinamisphone19
    with dissolve

    c "Oh! Umm, one more thing."
    s "What is it?"

    scene chinamisphone20
    with dissolve

    c "Are we like, allowed to kiss in public yet? Or is that still a no-go? "
    c "Cause I kinda wanna squeeze the life out of you right now and stuff."

    "I take a quick look around the mall to find that it’s actually rather busy today."

    if bonus == True:
        "And apart from Chika being my student, there’s still a considerable age gap between us."
        "I can’t imagine something like kissing her in broad daylight {i}not{/i} attracting attention to us, so..."

    s "I don’t think we should just yet..."

    scene chinamisphone21
    with dissolve

    c "Yeeeeah, I figured as much."

    if bonus == True:
        c "I’ll just have to make it up to you some other time then, huh?"
        s "The whole sticking your tongue out thing makes that seem pretty suggestive, Chika."

    scene chinamisphone22
    with dissolve

    if bonus == True:
        c "Oh? Does it?"
        c "Maybe I should be a little more careful with my expressions then?"
        c "I wouldn’t want you thinking I’m {i}suggesting{/i} something."

    chd "Chinami’s arms are getting tired. Can we buy her a phone now?"
    c "…"
    s "…"
    s "Let’s continue this some other time."
    c "Heheh...sure~"

    scene black
    with dissolve

    "The three of us enter the cell-phone store and let Chinami pick out whichever phone she wants."
    "Fortunately, she winds up choosing an older model that isn’t extremely expensive, and after signing a few forms, she’s ready to go."
    "Chika hugs me from behind at the checkout counter while the clerk is distracted filling things out and whispers her thanks to me once again."
    "…"

    scene chinamisphone23
    with dissolve

    chd "At last! Chinami’s true power can now be unleashed!"

    "Chinami holds the key to her true power (IE: A cell phone) above her head and screams loud enough for the entire mall to hear."
    "She’s so happy that neither of us have the heart to tell her to stop, though."

    c "Remember to take good care of that, Chinami. Sensei bought it for you, so you need to be super careful to not break it."

    scene chinamisphone24
    with dissolve

    chd "Chinami will be very careful. She will protect this phone with her life."
    c "Good girl, now thank Sensei or I’m going to take it away."
    chd "Thank you Sensei! Chinami will never forget this moment! Not even when you become her new daddy!"

    scene chinamisphone25
    with dissolve

    c "Hey, Chinami! No one is becoming anyone’s new daddy!"
    chd "What is Chinami’s phone number? She wants to make her first friend."

    scene chinamisphone26
    with dissolve

    c "Hm? You can’t give your number to Sensei, Chinami. He’s-"
    s "I don’t mind."

    scene chinamisphone27
    with dissolve

    c "Wait, what? I don’t even have your number yet and you’re going to give it to my little sister? She doesn’t even know how to use a phone yet."
    chd "Lies. Chinami has destroyed many pigs in the bird-game. She is a master of the phone."
    s "Give me your number then. And besides, wouldn’t it be good for me to have Chinami’s number in case there’s ever some sort of emergency?"
    c "Well, yeah but...It still seems kind of weird. "
    s "It’s not weird at all, I promise."

    scene chinamisphone28
    with dissolve

    c "Well...if you insist...I guess there's no fighting it."
    c "I’m more than happy to give you my number, at the very least..."

    scene black
    with dissolve

    "Chika walks over to me and swipes my phone out of my hand, entering hers and Chinami’s phone numbers into it with lightning-quick speed."
    "I expected no less from the cell-phone goddess of Kumon-mi."
    "Chika hands my phone back to me and I find that she’s added a heart next to it and..."
    "And a dog emoji next to Chinami’s..."

    $ renpy.end_replay()
    $ chikanumber = True
    $ chinaminumber = True
    $ chika_love += 1
    $ mall20 = True
    stop music fadeout 7.0

    "{i}Congratulations! You now have the phone numbers of the Chosokabe sisters!{/i}"
    "{i}Feel free to call them after[school] and on weekends to see what they’re up to!{/i}"
    "{i}Chika's affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label chikainvite1:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
    if chika_love >= 5 and mall5 == False:
        jump mall5
    if chika_love >= 10 and mall10 == False:
        jump mall10
    if chika_love >= 15 and chikadorm15 == True and day79 == True and mall15 == False:
        jump mall15
    if chika_love >= 20 and chikadorm20 == True and mall20 == False:
        jump mall20
...
```