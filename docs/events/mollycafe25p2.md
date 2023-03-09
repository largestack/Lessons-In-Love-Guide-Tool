# Tír na nÓg
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe25p2&go=Go)


Part of event chain [Resurrection Sickness](./mollycafe25.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: mollycafe25p2
* Group: Molly
* Triggered by label: mollycafe25

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe25p2:
    if _in_replay:
        play music "molly.mp3"

    scene nightsky
    with dissolve2

    "Molly and I walk relatively close together for the duration of the trip or...side quest or...whatever you want to call it."
    "I’m not too worried about whatever rewards it will yield considering that, if this were some sort of role playing game, I would either be the final boss or an overpowered hero character."
    "Someone who everyone else either aspires to be or inherently fears."
    "Or somewhere in between, but carrying over the best sides from both ends of the spectrum and packing them neatly into one tiny box known as “me.”"
    "Of course, it would be no game at all if there weren’t other people I met along the way."
    "Tonight, my companion is a [young_girl] who was not even born in this section of the world."
    "And while I can’t imagine her being of much use in terms of defeating enemies, she brings with her an aura that, more often than not, manages to bleed into and inspire others."
    "Or annoy them."
    "The effects are random, of course. And sometimes the aura is so clearly disadvantageous that, before you know it, you’re attempting to compensate for what she lacks."
    "If that doesn’t sound like a party member you’d take on your journey, you can chalk it up to the fact that I am no game designer."
    "I don’t know what is good or what is bad."
    "I’m just naming the things I see before me and attempting to connect them to a bigger picture and kill the silence that has consumed the air where her aura so typically lies."
    "The wind picks up as we wander into the park Otoha plays in."
    "We walk past her bench and I resist the urge to draw comparisons between her and the girl she “lost” to."
    "If Molly even considers it a loss in the first place and not just some...obstacle on the way to her next game."
    "That’s right."
    "I’m sure this will all blow over just as quickly as it began."
    "Kind of like the wind."

    scene mollywind1
    with dissolve2

    mo "Arise, spirits of the night! And to arms, my fae companions! "
    mo "I draw on your power in this time of need, for the world has begun to spin once more and left me behind."

    scene mollywind2
    with dissolve

    mo "Ahh, yes! It spins even now..."
    mo "And as the ground beneath my feet trembles...and the oceans swell with the pulsating, overinflated abdomens of gods of yore...I can feel it."
    mo "Silence, friends. For you may feel it too."
    mo "And though that feeling may cause you quite the fright, ‘tis fine! For as my guide is the light that brings you vibrance, your presence is the light that guides me home!"

    scene mollywind3
    with dissolve

    mo "Help me, dearest friends...for I have seen thou when no one else did."
    mo "And I have felt thou in the same winds that blow through these lands tonight and chills my bones to their core."
    mo "Be here for me, as I have been there for you."

    scene mollywind4
    with dissolve

    mo "And please, if you truly do exist at all- grant me your strength."
    s "…"
    mo "…"
    s "If you don’t really know if whatever you’re talking to exists or not, why talk to them or...{i}it{/i} at all?"

    scene mollywind5
    with dissolve

    mo "I wish I had an answer for that, Sir."
    mo "You see, I’ve spent most of my life talking to things that aren’t really there in the hopes that...if they {i}are{/i}, they’ll know I believed in them."
    s "Why?"
    mo "Because magic, Sir. Duh."
    mo "Imagine how amazing life would be if you could manipulate the elements or...fate...or...pull power out of the ether and convert it into anything you wished for."
    mo "I think that would be spectacular. "
    mo "So if there is anything out there that {i}has{/i} that power, all I wish is to see it."
    mo "And maybe channel a fair bit of it into myself for personal use, but only if those gifting it would be willing."
    mo "Wouldn’t want to ask for too much, of course."
    s "Well, I hope that whatever you’re talking to exists as well, since that was kind of the reason we came out here in the first place."

    scene mollywind6
    with dissolve

    mo "Would you like to try as well, Sir? Communicating with the fae, I mean."
    s "Yelling at trees in the middle of the night? I’m okay."
    s "I don’t even know what a fae is."
    mo "‘Tis not just {i}one{/i} thing, Sir. The fae encompass all fairies."
    mo "Aos Sí...Clurichaun...Púca.  "
    s "Those are words, alright."
    mo "Not just words, Sir. Legends."
    mo "And not just legends either. They’re characters in tales from not just Ireland, but all over the world."
    mo "Every country you can think of has their own myths...their own creatures that people believe exist, but just can’t gather enough proof for."
    mo "If such a thing exists all across the globe, I don’t think it’s fair to dismiss them without giving them a little more time."
    mo "They could always just be shy."
    s "So...all of these {i}allegedly{/i} made-up creatures from all over the world can also be known as the fae?"

    scene mollywind7
    with dissolve

    mo "For the sake of helping you understand, sure. We can summarize it like that for now."
    s "Wow. Look at you actually {i}helping{/i} me understand this time instead of just saying a bunch of things and expecting me to learn them right off the bat."

    scene mollywind8
    with dissolve

    mo "I’ve tried to help you many times, Sir! You’re just always very quick to tell me you don’t care."
    s "Probably because I don’t."
    mo "See? You just did it again."
    s "I know what I did. "
    s "But I don’t really {i}have{/i} to care about all the same stuff as you, do I?"
    s "If I had any interests, I wouldn’t expect you to jump all over them and...be excited to talk about stuff you know nothing about."

    scene mollywind9
    with dissolve

    mo "No...I understand. I am not looking for sympathy. I’ve been getting enough of that from the Kendo Princess lately. "
    mo "I..."
    mo "I need to get better at not...forcing myself onto others."
    mo "I just get excited easily. ‘Tis all, Sir. "
    mo "I swear it."
    s "It doesn’t really matter to me. I’m still here, aren’t I?"

    scene mollywind10
    with dissolve

    mo "Surprisingly, yes. You even allowed me to come to my power spot and everything."
    s "Well...are you feeling any more powerful?"
    mo "Not particularly. It did help being able to talk to all of my friends, though. Mythical-slash-mystical or not. "
    s "Great. Are we done here then?"

    scene mollywind11
    with dissolve

    mo "Aaaaaaaactually..."
    s "…"
    mo "Can we sit down for a little while? "
    mo "It’s a nice night and...I know I’ll start thinking once I get home."
    s "You? Thinking? That sounds dangerous."
    mo "Haha...hah..."
    s "Sure, Molly. We can sit. "
    s "But, I’d prefer if it didn’t take up too much time since it’s only getting colder and windier as the night goes on."
    mo "Understood, Sir. I will do my best to annoy you for less time than normal. "

    scene black
    with dissolve2

    "Molly runs forward and chooses a different bench than the one right beside me, probably because she is difficult, and immediately begins looking up at the sky again."
    "I’m not sure if it’s some sort of reflex for her or if she’s just doing it for momentary comfort, but I see no sense in stopping it because at least it’s bringing a smile to her face."

    scene mollywind12
    with dissolve2

    "Instead of talking, I decide to stare at her for a little while- wondering how she’s managing to keep things together even though I know she’s being torn up inside."
    "In the midst of mentally listing those possibilities, a funny thought pops into my head."
    "What if these fae or whatever...do exist?"
    "And what if they’re just...inside of her?"

    s "…"

    "Then I kick myself in the mental balls for being so corny, even if it was only in the form of an inner monologue."
    "The more realistic answer would be that she’s already dealt with one of the worst things a person can go through in losing her mother."
    "Does that have some sort of correlation to experiencing heartbreak? Probably not."
    "But at least she’s been hurt before."
    "It’s always easier when you’re hurt multiple times."

    s "…"
    mo "My foresight is telling me that you’re planning on asking me something."
    s "Your foresight is pretty damn good then because I haven’t even planned on that yet."

    scene mollywind13
    with dissolve

    mo "What is it, Sir? Do you want to learn more about the fae?"
    mo "Which kind? Leprechauns? Changelings?"
    s "Actually..."
    s "Why not tell me more about your family?"

    scene mollywind14
    with dissolve

    mo "My family?"
    s "More specifically-"

    scene mollywind15
    with dissolve

    mo "Ah."
    mo "I think our brain waves may have connected just now, for I was thinking the same thing when I was staring up at the sky."
    s "But I haven’t even told you what I was thinking about yet."
    mo "Then I will tell {i}you{/i} what I was thinking and we can pretend it was the same if it actually was not."
    mo "Tír na nÓg."
    s "…"
    s "Nope. Can’t even pretend that’s what I was thinking since I have no idea what it means."
    mo "Tír na nÓg- or the Land of the Young, is a magical land not far off the Isle, where no one can die...and where everyone remains eternally young."
    mo "Many believe that the reason the fae will not grace us with their presence is because they reside there, Sir."
    mo "One of those people was my mother."

    "Oh."
    "So I guess Molly might actually have foresight after all."
    "Either that or I’m just...incredibly easy to read."

    mo "I don’t have many memories of her, to tell you the truth."
    mo "But I do remember a large collection of storybooks and fairytales that she would read to me before she died."
    mo "I wish I remembered more about {i}her{/i} specifically...but I think that leaving all of those books behind was just...her way of communicating."
    mo "I wasn’t left with nothing like many other children who lose their parents are. "
    mo "I still have my father...and mountains of magical myths my mother may have memorized..."
    mo "I have pictures of her too. And old clothes I hope to be able to wear one day."
    mo "She was beautiful."
    mo "Not like me."
    s "Hey, now. "
    s "I doubt she’d be happy to hear you saying that about yourself."

    scene mollywind16
    with dissolve

    mo "No...It’s true, Sir."
    mo "And I’ve known it to be true for quite some time. "
    mo "If I was...prettier or...cooler like someone like Chika or Otoha, you and I wouldn’t be on this bench right now."
    mo "I’d have won."
    mo "But I made the executive decision to put all of my stat points into categories that didn’t matter as much as aesthetics to some people."
    mo "Which is fine. We all have different things we look for in partners."
    mo "I just wish it wasn’t too late to change where I allotted those points, is all."
    s "It’s not, though."

    scene mollywind17
    with dissolve

    mo "But, Sir...you {i}have{/i} to say that."
    mo "You’re the protagonist."
    mo "It’s your job to make us feel loved or wanted. "
    mo "We can’t just change who we are now after spending so many years figuring it out."
    s "These are the exact years you’re supposed to be {i}using{/i} to figure it out, though."
    s "Even if Rin {i}doesn’t{/i} think you’re pretty, which I don’t think is the case, there are plenty of people who do."
    s "And it might sound kind of weird, but a lot of people are really attracted to foreigners in Japan."

    scene mollywind18
    with dissolve

    mo "Well, {i}that{/i} was mildly racist. "
    s "I didn’t mean it in a bad way."

    scene mollywind19
    with dissolve

    mo "{i}*Sniff*{/i} No, it’s fine. I know you meant no harm."
    mo "I’m sure I’m overreacting. It’s just hard not to think certain things when you share literally {i}every{/i} interest with the person you like and they still won’t give you a shot."
    s "Some people just want something different from them, I guess."
    mo "Otoha isn’t that far off from Rin, Sensei."
    s "Okay, sure. But we shouldn’t be using Rin as the basis for {i}anything{/i} when she is about as composed as..."
    s "I can’t even think of a comparison. She’s a wreck."

    scene mollywind20
    with dissolve

    mo "A wreck I’ll never get to have or hold."

    if bonus == True:
        mo "Or get all hot and bothered with while playing h-games."

    s "No. But you {i}have{/i} kissed her before, which is more than a lot of people can say."

    if rinbetrayed == False:
        "Not including me, of course. I’m in that same boat. But Molly doesn't need to know that."

    mo "I don’t think it’s fair to count what happened on Christmas as a real kiss, Sir."
    mo "I've done some more thinking on the matter and, as far as I’m concerned, I still haven’t had my first."
    s "Really? Not even going to pretend you had your first with the girl you like just to make yourself feel better?"

    scene mollywind21
    with dissolve

    mo "The only thing that makes me feel better is gaming, Sir! And anime! That is all I need!"
    s "That’s so depressing."
    mo "Maybe! But this is the person I am! "
    mo "This is Molly MacCormack!"
    mo "And...if you don’t like that...Go dtachtfadh an diabhal thú!"
    s "Yeah. Gothafababable and dhtafghdadadad."

    scene mollywind22
    with dissolve

    mo "Pfft!"
    mo "Thank you for trying, Sir. I felt quite similar when I was learning Japanese. "
    s "I did my best. "
    s "But, on another note, I am done sitting on this bench. It is fucking cold."

    scene mollywind23
    with dissolve

    mo "Then...off to the original side quest we go!"
    mo "There were no physical rewards for this one, but I do believe we have increased our social link!"
    s "Yeah. And we’ve grown a little closer as well."

    scene mollywind24
    with dissolve

    mo "Oh, Sir...You still have so much to learn..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25p2 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump mollydorm25
...
```

## Code that triggers this event
File: \game\MollyEvents.rpy
Code:
```python
...
scene mollycleaning20
    with dissolve

    mo "As a...one time favor to me for...not making your life as difficult as you expected me to tonight."
    s "…"
    mo "And also if you’d walk me home after we’re done."
    s "So a two time favor."
    mo "One time consisting of two things."
    mo "Maybe a third when we get back to the dorm. Who knows?"

    if bonus == True:
        s "Can you do {i}me{/i} a favor when we get back to the dorm?"
        mo "Is this favor you have in mind a lewd one?"
        s "Is it {i}allowed{/i} to be a lewd one?"
        mo "Is my name Molly Medb MacCormack?"
        s "...Maybe?"
        mo "Wrong! It is Molly Moyra MacCormack!"
        mo "Why do you not know this?!"
        s "It wasn’t in your character profile."
    else:
        s "My father never taught me how to do any handyman-type things, so if you need a lock replaced or something, you should probably just ask Io."

    mo "Silence! Chairs! Go go go!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I sigh to myself and somehow let Molly bully me into helping out in some way."
    "I really don’t care as much as I made it seem, though."
    "It’s not like this place has {i}that{/i} many chairs...and the ones they do have are relatively light."
    "As such, I’m able to finish the task in several minutes and proceed to wait by the counter (That lives to see another day) for Molly to finish her portion of the work."
    "She does what I imagine is a half-assed job and finishes up in about twenty minutes before changing back into her winter clothes and beckoning me outside."
    "………"
    "……"
    "…"

    scene mollycleaning21
    with dissolve
    play music "molly.mp3"

    mo "Alas, the stars have retreated back into their caves in the depths of the night sky...preserving their light for the end of days as it steadily approaches."
    s "There are no caves in the sky, Molly."
    mo "Of course I know that, Sir."
    mo "I just mean that there’s a clear amount of light pollution here. It’s not like it was at the beach."

    scene mollycleaning22
    with dissolve

    s "Ah. I guess not."
    s "I wouldn’t really expect any less in a city, though."
    mo "You don’t have to expect something before being disappointed, Sir. Sometimes, you can just...be disappointed."
    mo "I like the stars. I wish the sky always looked the way it did when we were there."
    s "Don’t let Maya hear that. She’ll probably quiz you on them."
    mo "I’d fail a quiz miserably. I just like looking at them."
    s "... "
    s "They’re okay, I guess."
    mo "So, do you intend to venture forth on a side quest back to the dorm with me? Or is this where our party disbands and heads its separate ways?"
    s "My answer to this question hinges on how long you plan on talking about stars for."
    mo "I was already done, Sir. I was simply pointing out how I wish there were more."
    s "Then yeah. I can come back to the dorm with you."
    mo "Excellent. I’ll see to it that you obtain a rather desirable quest reward as a result."

    if bonus == True:
        s "Lewd or not lewd?"
        mo "Not lewd, of course."
        s "That doesn’t sound very desirable to me."
    else:
        s "Can you teach me how to tie my shoes? My father never taught me that either."
        mo "Of course, Sir. If that is what will make you happy."
        s "Yay!"

    scene mollycleaning23
    with dissolve

    mo "Sir, I realize this may be annoying, but would we be able to stop somewhere along the way?"
    s "Where did you have in mind?"
    mo "A nearby leyline I like to draw power from when my stocks begin to run low."
    s "Based on what I know about Mollyspeak...I’m going to assume that means a convenience store."

    scene mollycleaning24
    with dissolve

    mo "It appears you still have much to learn then, as that answer is rather far from the truth."
    mo "Come. Let us pick up yet another side quest and see if that one yields any worthy rewards as well!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump mollycafe25p2
...
```