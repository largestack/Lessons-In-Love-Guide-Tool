# Happy Hour
Chinami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate20&go=Go)



## Event preconditions
✅Chinami love greater than or equal to 20

✅Event "[Chinami: Pool Party](./chinamidate15.md)" is completed (event=chinamidate15)

✅chinaminumber equal to True (unknown variable)



## Next events
* [Main: Good Morning](./secondbeach1.md)

## Event properties
* ID: chinamidate20
* Group: Chinami
* Triggered by label: callchinamiafternoon
* Triggered by branch label: callafternoon

## Event code
File: \game\ChinamiEvents.rpy
Code:
```python
...
label chinamidate20:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "………"
    "……"

    play sound "phonebeep.wav"

    ch "Chinami hotline! Thank you for calling during happy hour!"
    s "It’s happy hour?"
    ch "Every hour is happy hour! Life is good! Buy giraffes!"
    s "But I still haven’t received the first ones I ordered."
    ch "Sorry. You need to call our customer support line if you want help with that. This is the giraffe center."

    "I sigh to myself and wonder for what feels like the millionth time why I’m calling one of my student’s little sisters."
    "I then hang up and dial the customer support number to follow up on the giraffe situation."
    "Just kidding."

    s "Where are you right now, Chinami? It sounds kind of loud."
    ch "Would you like a hint?"
    s "Sure. Why not?"
    ch "Arf! "
    s "Oh, you’re at the mall."
    s "Is Chika there?"
    ch "Of course big sis Chika is there. Did you think Chinami came here all by herself?"
    s "That’s...a good point. I’m not really sure why I asked that."
    ch "Well Chinami is glad you did! And she’s also glad you agreed to babysit her!"
    s "I-"
    ch "Bye bye, Papa! See you soon!"

    play sound "phonebeep.wav"

    s "…"

    "I slowly shove my phone back into my pocket and begin to head over to the bus station to hang out with a girl in a dog mask."
    "………"
    "……"
    "…"

    scene chinamimeetsalesbian1
    with dissolve
    play music "happyandplotting.mp3"

    s "…"
    ch "…"
    s "…"
    ch "…"
    ch "Arf!"
    s "I can’t imagine it’s very easy to drink that with a dog mask on."
    ch "Doggies can’t drink strawberry milk. They’ll get a tummy ache."
    s "Can you remind me why I spent money on buying you a drink you can not consume?"
    ch "Because you love Chinami."
    s "I do not love Chinami."
    ch "But you bought her strawberry milk and a cell phone."

    if bonus == True:
        s "Is that really how kids are judging love nowadays?"
    else:
        s "Is that really how wizards are judging love nowadays?"

    ch "Chinami doesn’t know. She’s not old enough to fall in love."

    "I quickly scan the mall to see how any onlookers might be viewing this...scene."
    "I immediately find that it’s not very good."

    s "Chinami, is there any way we could get you a less...conspicuous costume for when you come to the mall?"
    ch "Oh right. Chinami forgot you hate puppies."
    s "This is just kind of weird any way you look at it."

    if bonus == True:
        ch "Okay! Chinami understands that it would be normal for you to be seen with a little girl without a helmet on."
    else:
        ch "Okay! Chinami understands that it would be normal for you to be seen with a girl without a helmet on."

    ch "She’ll call her people and see what they can do."
    ch "But in the meantime-"
    ch "Arf!"

    "Again, I find myself leaning back in my chair and wondering how my life has gotten to this point."
    "I don’t have to wonder for very long, though, as I quickly remember that it was my idea to call her."
    "Could I have just left her at the clothing store with her sister? Absolutely."
    "Would it have been more socially acceptable for me to do that?"
    "Again, absolutely."

    if bonus == True:
        "Should I stop calling her altogether and begin hanging out with people that I couldn’t go to jail for just looking at?"
        "For a third time, absolutely."

    "But, no matter how many times I say “absolutely,” I have a hard time believing I’ll ever {i}really{/i} figure out how to stay away from this...demon slash CEO slash wizard slash dog."

    ch "Your eyebrows are being all...eyebrowy again."

    if bonus == True:
        s "I am a grown man sitting at a table with a little girl in a dog mask who is holding a box of strawberry milk for sheer aesthetic purposes."
    else:
        s "I want to die."

    ch "Arf!"
    s "I’m glad that you understand."
    o "What...the...fuck..."

    scene chinamimeetsalesbian2
    with dissolve

    if bonus == True:
        s "Oh, good. Now I’m a grown man sitting at a table with a little girl in a dog mask with aesthetic strawberry milk who has to explain to his students exactly what is happening."
        o "I mean...yeah?"
    else:
        s "I really do want to die."

    r "Um...Hi, puppy?"
    ch "Arf!"

    scene chinamimeetsalesbian3
    with dissolve

    o "Please tell me you’re not going to pretend she’s a real puppy."
    r "Otoha, I need you to think about this."
    r "If we just accept and agree that it {i}is{/i} a puppy, we can all move on and forget that this ever happened."
    s "I like Rin’s idea."
    ch "Arf!"

    scene chinamimeetsalesbian4
    with dissolve

    o "Did you kidnap her?"
    s "What? No. What would give you that idea?"
    o "The fact that you once made plans with Nodoka and Rin to kidnap me."
    s "Hey. Noriko was there too. "
    s "We all supported yuritopia and she needs to absorb some of the blame for me."

    scene chinamimeetsalesbian5
    with dissolve

    o "Yuri...topia?"
    r "Hahaha! Hahah...Noooo idea what Sensei’s talking about."
    ch "What’s a “yuritopia?”"

    scene chinamimeetsalesbian6
    with dissolve

    r "A magical world where all dreams come true."
    s "Not all dreams. Just yours."
    ch "Will Chinami’s dreams come true in yuritopia as well?"
    s "You still have several years left to figure that out, Chinami."
    ch "Chinami certainly hopes so!"

    scene chinamimeetsalesbian7
    with dissolve

    r "Chinami?..."
    r "That name sounds kind of familiar."
    s "Care to join us, Otoha?"

    if bonus == True:
        o "And be an accessory to whatever like, fifty felonies you’re committing right now? I'm good."
        s "I’m not doing anything wrong. I’m just babysitting."
    else:
        o "I'd rather eat a hedgehog."
        s "That is a strange alternative to this."

    ch "Arf!"
    o "Are teaching wages so bad that you need to pick up a second job just to keep yourself afloat?"
    s "They’re not great. That’s definitely true. But I’m doing this job for free."
    o "…"
    o "Yeah, I'm still good."
    r "Where in the world do I know that name from?"

    if bonus == True:
        s "Rin, pull up a seat with your girlfriend and hang out with us. Having two [teenage]girls with me {i}as well{/i} as Chinami might somehow make me look...less bad."
    else:
        s "Nowhere. Now tell your girlfriend to sit down."

    scene chinamimeetsalesbian8
    with dissolve

    r "G-Girlfriend?! "
    o "Come on, man. Why would you say that?"
    s "Because it will work. Watch."

    scene chinamimeetsalesbian9
    with dissolve

    r "Um...it doesn’t have to be for long...but...it probably {i}would{/i} help Sensei out a little..."
    o "You finally summoned up the courage to come here and {i}this{/i} is how you want to spend your time?"
    r "Like I said...it won’t be for long..."

    scene chinamimeetsalesbian10
    with dissolve

    o "How did you know that was going to work?"
    s "Honestly, it would have worked even if I left the girlfriend part out. I just like when Rin gets flustered."

    scene chinamimeetsalesbian11
    with dissolve

    o "You’re a real asshole sometimes, you know that?"
    s "No one knows that better than me, Otoha."

    scene black
    with dissolve2

    "Rin and Otoha grab chairs from a nearby table and join us at ours."
    "Of course, their attention isn’t even slightly focused on me."
    "Instead, it is focused on man’s best friend- a small girl in a dog costume. "

    scene chinamimeetsalesbian12
    with dissolve

    r "So...um...Chinami, right?"
    ch "Arf!"
    r "...What?"
    o "I think that means yes. I used to have a dog."
    r "Do you...come here often?"
    s "Rin, please don’t flirt with the puppy."

    scene chinamimeetsalesbian13
    with dissolve

    r "That’s not what I’m doing! I’ve just...never talked to a dog before! I don’t really know what to ask."
    ch "Chinami comes every once in a while!"
    ch "But she can’t come very much because she gets sick easily."
    o "Um..."
    o "Arf?"
    ch "Arf! Arf arf!"

    scene chinamimeetsalesbian14
    with dissolve

    o "Arf arf...arf arf?"
    ch "Arf! Arf arf!"
    r "Ohmygodohmygodohmygod."
    s "Otoha, would you mind explaining what you’re doing?"

    scene chinamimeetsalesbian15
    with dissolve

    o "I don’t know. Playing along I guess? "

    if bonus == True:
        o "Must be boring as hell having someone like you as a babysitter, so I’m just stepping in and trying to make things less lame."
    else:
        o "I'm just trying to like, make things less lame or whatever."

    s "You’re making things {i}less{/i} lame by barking at a girl in a dog costume?"

    scene chinamimeetsalesbian16
    with dissolve

    o "Hey! Don’t blame me for being good with kids. "
    r "Umm...I’m too embarrassed to bark at you like my not-girlfriend, Otoha, but...I’m happy to meet you Chinami."
    ch "Chinami is happy to meet you as well!"
    ch "Are you also friends with her big sisters?"

    stop music fadeout 10.0

    r "Big sisters? Do they go to our[school]?"
    s "Chinami, you probably shouldn’t be talking about that to-"
    ch "There’s big sis Chika and big sis Yumi! But only big sis Chika is related to Chinami by blood."

    scene chinamimeetsalesbian17
    with dissolve

    r "…"
    r "Oh..."
    r "{i}That’s{/i} where I’ve heard your name before."

    scene chinamimeetsalesbian18
    with dissolve

    o "..."
    ch "Did Chinami say something wrong?"
    r "No. You didn’t say anything wrong."

    scene chinamimeetsalesbian19
    with dissolve
    play music "gentle.mp3"

    r "It’s...uhh..."
    r "It's nice to meet you, Chinami. I’m Rin."
    r "I’m...going to take a wild guess and assume your sister’s never mentioned me before?"
    ch "Hmm..."
    ch "Chinami’s memory is very bad, so she isn’t sure."
    s "Rin, you know we can change the topic if this is weird for you, right?"
    o "Yeah..."
    o "That's...probably what we should do."
    r "I guess it doesn’t really matter if she mentioned me or not. We’re friends, though."
    r "Or...I think we’re friends? It’s a confusing...thing."
    r "But I’m really happy to finally meet you."
    ch "Chinami is confused."
    r "Why is Chinami confused?"
    ch "Because you’re saying you’re happy but your eyes are all teary."

    scene chinamimeetsalesbian20
    with dissolve

    r "Oh. "
    r "Huh. "
    r "I guess they are."
    r "And here I thought I was done crying over this."
    ch "So you’re {i}not{/i} happy? Chinami wants to confirm."
    ch "She isn't used to the complex emotions of [teenager]s."

    scene chinamimeetsalesbian21
    with dissolve

    r "Are {i}you{/i} happy, Chinami? Cause it would make me happy if you’re happy."
    ch "Chinami is super duper happy! She has two amazing sisters and an amazing new Papa who gets to babysit her at the mall."
    o "Oh, good. As if this couldn’t get any weirder."
    s "Strangely enough, I don’t really think this is as weird as the first time people saw me with her in full costume."

    scene chinamimeetsalesbian22
    with dissolve

    o "Weirder than {i}finally{/i} getting Rin to accept the end of her crush on that girl...{i}only{/i} to show up and bump into her little sister in a dog mask? Because that's pretty friggin' doubtful, man."
    ch "Crush?"
    ch "Chinami is sorry for asking, but aren’t you a girl?"
    r "Yes, Chinami. I’m a girl."
    ch "And you know Chinami’s sisters are girls too, right?"
    r "...Yup."
    ch "And you still liked her anyway?"
    ch "Are you allowed to do that?"
    r "Well..."
    r "I wasn't."
    r "But I guess it never really mattered since she didn’t like me the same way."
    ch "Chinami is very confused. She-"

    scene chinamimeetsalesbian23
    with hpunch

    ch "Wait!"
    ch "Chinami remembers something!"
    ch "But it’s very fuzzy. Like a puppy."
    r "What...is it?"
    ch "Big sis Chika did mention someone called Rin once!"

    scene chinamimeetsalesbian24
    with dissolve

    r "She did?..."
    r "Do you...remember what she said, by any chance?"
    ch "Umm..."
    ch "Chinami thinks..."
    ch "Chinami thinks she said you had very pretty eyes. And that she wanted hers to look more like yours."

    scene chinamimeetsalesbian25
    with dissolve

    r "..."
    r "That’s it?"
    ch "Chinami thinks so. She can’t remember any other Rins and big sis Yumi never talks about {i}anybody{/i}."

    scene chinamimeetsalesbian26
    with dissolve

    r "Heheh...hahahah!"
    r "Better than nothing, I guess!"
    o "Still not as weird as the first time?"
    s "I’m not sure. This has lasted a lot longer than that did."
    s "But I feel that this is probably weirder for {i}you{/i} than any of us since you're entirely unrelated to...pretty much all of it."
    ch "Chinami is so surprised! Until today, she didn’t know that girls could like other girls!"

    scene chinamimeetsalesbian27
    with dissolve

    o "I...uhh..."
    o "Yeah, I’m not gonna lie. I'm mad uncomfortable right now, so I think I’m gonna like...go walk around or something and...let you guys finish up on your own."
    r "I...can stop? "
    r "It just kinda happened out of nowhere and...I don’t want you to feel weird about me getting all emotional over it."

    scene chinamimeetsalesbian28
    with dissolve

    o "Don’t sweat it. When you’ve gotta cry, you’ve gotta cry. "
    o "But...again...this whole romance thing is just-"
    o "Well, to use Sensei’s words-"
    o "Entirely unrelated to me."
    o "Sooooooooyeah. I’m gonna go grab a milkshake or something and-"
    r "I’ll come with you. Don’t leave."
    o "Rin, you really don’t-"

    scene chinamimeetsalesbian29
    with dissolve

    r "Nope! I’m done here. "
    r "Not gonna waste a perfectly good opportunity to hang out with you getting upset over stuff that’s in the past."

    scene chinamimeetsalesbian30
    with dissolve

    r "Thanks for talking to me, Chinami."
    r "And please don’t say anything about this to either one of your sisters. I don’t really want to confront it again after it’s already over."
    ch "Chinami will do what you say!"
    ch "But she wants you to know that big sis Chika would never hurt you on purpose. She’s a very nice girl!"
    r "Yeah..."
    r "I know she is..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene chinamimeetsalesbian1
    with dissolve

    s "Just gonna go right back to jabbing your fake tongue against that straw, huh?"
    ch "Chinami feels like she wound up in a sticky situation just now! She’s parched!"
    s "All things considered, I think you handled it really well."
    ch "Chinami had no idea what to do when the girl with more red in her hair started barking at her! What is she, crazy?!"
    s "I can’t believe I’m about to say this...but don’t ever change, Chinami."
    ch "You want Chinami to stay little forever?"
    s "Okay. Maybe change a little bit. I wouldn’t want you stunting your growth for me."
    ch "Arf!"

    play sound "texttone.wav"

    "My phone suddenly goes off and I look down to see that Chika’s about to clock out for break and that my shift as “babysitter” is over."
    "I think I’ll wind up sticking around for a little while longer, though."
    "I’m in no rush to leave and-"
    "Honestly, having both Chosokabes around at once might be the exact medicine I need to counteract the overabundance of sadness and longing I just had to sit through."

    scene black
    with dissolve2

    ch "Chinami wants another strawberry milk! Go, Papa! Go!"
    s "…"

    "I text Chika, asking her to bring her sister a drink on the way over."

    $ renpy.end_replay()
    $ chinamidate20 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label chinamidate25:
...
```

## Code that triggers this event
File: \game\ChinamiEvents.rpy
Code:
```python
...
label callchinamiafternoon:
    if chinami_love >= 5 and chinamidate1 == True and day128 == True and chinamidate5 == False:
        jump chinamidate5
    if chinami_love >= 20 and chinamidate15 == True and chinamidate20 == False:
        jump chinamidate20
...
```