# A Dog that Doesn't Do Math
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mall15&go=Go)



## Event preconditions
✅Chika love greater than or equal to 15

✅Event "[Chika: A Castle for Everyone](./chikadorm15.md)" is completed (event=chikadorm15)

✅Event "[Main: Scientific Research](./day79.md)" is completed (event=day79)



## Next events
* [Chika: Schadenfreude](./chikadorm20.md)

## Event properties
* ID: mall15
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label mall15:
    scene mall1
    with dissolve
    play music "mall.mp3"

    "I show up at the mall around the same time I always do and immediately take note of Chika not being on what I will now just refer to as {i}our{/i} bench."
    "Being an adult who's able to pick up on context clues, I understand that her absence means she’s working right now and I begin to ponder over whether or not today is the day I have been waiting for."
    "It's been a while since Chika has modeled anything for me and we've definitely grown closer since then. So either we're at the lingerie stage {i}now{/i} or we will be soon."
    "Either way, I must do my duty and find out."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene whyissheadog1
    with dissolve

    s "Chika, are you around? I was thinking that today we-"

    scene whyissheadog2
    with dissolve2

    s "…"
    q "…"
    s "…"
    q "…"
    s "…"
    q "…"
    s "Okay, nevermind. I’ll come back later."

    scene black
    with dissolve

    "Not knowing how to handle the situation I have somehow found myself in, I immediately turn around and head for the door."
    "Of course, the small hand of the strange...helmeted figure reaches out and grabs my wrist."
    "Her grip obviously isn’t strong enough to prevent me from leaving since she is only a fraction of my size...but I’m pretty sure I know who this is anyway and that there isn't any {i}real{/i} reason to run."

    scene whyissheadog2
    with dissolve

    chd "Woof!"
    s "Hello, Chinami."
    chd "Woof!"
    s "Would you mind explaining to me why you’re dressed like that? And...out in public?"
    chd "Big sis made Chinami put on her special mall clothes so she could be safe at work!"
    s "You’re not...covering your sister’s shift, are you? Because I don't think you're old enough to work here."
    chd "Chinami is a 5000 year old wizard! She is more than old enough to work!"
    chd "But no! Chinami didn’t want to be alone today and big-sis Yumi couldn’t come over."
    s "Yeah, you’re probably better off without Yumi anyway."
    chd "Woof!"
    s "Chinami, would you mind telling me where your sister is?"
    c "I’m coming! Hold on one sec!"
    chd "…"
    s "…"

    "This stare-down is making me incredibly uncomfortable."

    c "Chinami, go be a good girl and go...organize the underwear or something."
    chd "Okay! But Chinami needs to be sure she'll be fairly compensated!"

    scene whyissheadog1
    with dissolve

    "What exactly would be {i}fair{/i} compensation for child labor?..."

    scene whyissheadog3
    with dissolve

    c "That kid, I swear."
    s "She’s not a kid. She’s an ancient wizard. Be careful."

    scene whyissheadog4
    with dissolve

    c "Right, right. My bad."

    scene whyissheadog5
    with dissolve

    c "So, whatcha up to today, Sensei? Come to spend some time with your favorite student?"
    s "It certainly appears that way."
    c "Well, sorry to break your heart, but I’m kinda slammed right now. I’ve even resorted to having Chinami help since I can't handle all of this on my own."
    s "I’m pretty sure that's against the law, but whatever."
    c "I mean, it at least got her out of my hair for a little while...but you're right. I should probably figure something else out instead."
    c "It's just kinda hard since I can't really afford a-"

    scene whyissheadog6
    with dissolve

    c "Wait a second..."
    s "..."
    c "..."
    s "Please, no."
    c "I just got like, a totally awesome idea."
    s "No you didn't."
    c "Do you think that maybe {i}you{/i} could watch her?"
    s "No."

    scene whyissheadog7
    with dissolve

    c "Pleeeeeeease, Sensei? I’ll make it up to youuuuu~"
    s "How?"
    c "I don't know. Is there anything you want? What if I like, buy you lunch or something?"

    if bonus == True:
        s "I demand an expedited lingerie modeling session."
    else:
        s "Clown costume????"

    c "You’re still going on about that? That was like, forever ago."
    s "There are some promises you can’t back down from, Chika."
    c "This is a weird time to start dropping inspirational quotes."
    s "It's also a weird time for me to become a babysitter."

    scene whyissheadog8
    with dissolve

    c "How about this! Either you watch my sister or I call security and tell them some old guy is harassing me."
    s "This is blackmail."
    c "I guess maybe it is a little, yeah."
    s "You’ve been hanging out with Yumi too much."

    scene whyissheadog9
    with dissolve

    c "Kinda unavoidable when we sleep in the same room."
    s "Fine. I’ll do it. You’re going to have to explain the dog thing, though."

    scene whyissheadog8
    with dissolve

    c "I’m sure it’s not far off from whatever you're thinking. "
    c "Chinami doesn’t like wearing face-masks because they make her look funny. But, for some reason, she’s totally cool with a giant dog helmet."
    c "And she has to wear gloves to prevent herself from touching anything with germs. And the scarf thingy-"

    scene whyissheadog3
    with dissolve

    c "Well...that I don’t really have an answer for. I think she just likes it."

    scene whyissheadog9
    with dissolve

    c "She’s still super cute, though, right? And the way she’s all like “woof!” Oh my god. I wanna die."
    s "You might want to keep an eye on her in case she walks up to any other customers, though."

    scene whyissheadog6
    with dissolve

    c "Who, Chinami? She wouldn’t do something like that. She never talks to strangers."
    s "Are you sure about that?"
    c "Mhm. Why do you ask?"
    s "Because she’s trying to pet a customer’s dog right now."

    scene whyissheadog10
    with dissolve

    c "What?! Chinami! Stop that right now!"
    c "Just because you're in dog form doesn't mean you can play with...{i}other{/i} dogs!"

    scene black
    with dissolve

    "Chika runs over and snatches her sister away right before she comes into contact with a small dog hanging out of a wealthy-looking woman’s purse."
    "Feeling the need to get her out of here in order to avoid any other possible issues, Chika pawns Chinami off on me and sends the two of us out to go...walk around the mall or something."
    "………"
    "……"
    "…"

    scene whyissheadog11
    with dissolve

    s "What has my life become?"
    chd "Woof!"

    "Chinami’s tiny hands wrap around mine as the two of us walk through the mall."

    if bonus == True:
        "I’m sure everyone around thinks she’s my daughter-"
        "Or...at least, I {i}hope{/i} everyone around thinks she’s my daughter. It would be extremely problematic for them to think anything else at this point."
        "I'm sure the dog mask isn’t doing us any favors, either."
    else:
        "I wonder if this is what owning a dog is like."

    chd "Are you going to be Chinami’s new daddy?"

    if bonus == False:
        "I don't think this is what owning a dog is like."

    scene whyissheadog12
    with dissolve

    s "…"
    chd "…"
    s "No."
    chd "Why not? You and my big sister are in love, aren’t you?"
    s "No."
    chd "You’re not?"
    s "No, Chinami. I’m just her teacher."
    chd "Chinami doesn’t know much about teachers since Chinami is home-schooled. Do all teachers visit you at work?"
    s "..."
    s "No."
    chd "Then why are you visiting Big Sis? Do you need to buy new clothes?"
    chd "You look like you need to buy new clothes."
    s "I...Yeah, sure. Let’s go with that."
    chd "Do you have lots of money?"
    s "I have an adequate amount of money."
    chd "Will you buy Chinami a cell phone?"
    s "What are you going to do with a cell phone, Chinami?"
    chd "Chinami likes the game where you shoot birds at pigs and make them blow up."
    s "Then, no. I'm not going to buy Chinami a phone."
    chd "Do you actually hate Chinami?"
    s "No. I just don’t think your sister would be happy if I bought you a phone."

    scene whyissheadog13
    with dissolve

    chd "Why not? Are cell phones expensive?"
    chd "Chinami has 500 yen at home that she found at the beach."
    s "That’s nowhere near enough."
    chd "Okay. Chinami will save up more."
    chd "Thank you for telling her."
    s "... "
    chd "..."
    chd "Can Chinami ask you a question?"
    s "What is it, Chinami?"

    if bonus == True:
        chd "Where do babies come from?"
    else:
        chd "Why do you like clowns so much?"

    s "Ask something else, Chinami."
    chd "Okay. Chinami has another question anyway."
    s "What is it this-"

    scene whyissheadog13r
    stop music

    chd "Where do people go when they die?"
    s "..."
    chd "..."
    s "..."
    chd "..."

    scene whyissheadog12
    play music "mall.mp3"

    s "How about I just ask you some questions instead?"
    chd "Okay! Chinami thinks that sounds fun."

    "I can’t see through the dog helmet, but I can tell that there is a demon inside."

    s "Are...dogs your favorite animal, Chinami?"
    chd "Yes! Chinami wants a dog but she’s not allowed to have one cause dogs can get people sick."
    s "Can they? I thought that was just a myth."
    chd "Chinami doesn't know because she is home-schooled. She just believes whatever her big sisters tell her."
    chd "But if you want to teach Chinami all about animals, she’ll pay close attention."
    chd "She is currently very interested in giraffes!"
    s "I can barely even teach my students math. I don’t really think I’m qualified to teach you about what diseases animals carry."
    chd "You can teach Chinami math, then! And you can teach big-sis Yumi, too!"
    s "I’d love to if she would actually show up to class every once in a while."
    chd "Oh. Chinami forgot Yumi goes to[school] again."
    s "Don’t worry, Chinami. I forget that too sometimes."
    chd "Can Chinami ask another question?"
    s "That depends. Is it going to be something else incredibly difficult to answer given the nature of our relationship?"
    chd "Woof!"
    s "..."
    s "What’s your question, Chinami?"
    chd "Who are the girls in front of us?"
    s "Girls? What g-"

    scene whyissheadog14
    with fade

    a "…"
    m "…"
    chd "…"
    s "I can explain."
    a "Um...what?"
    chd "Woof!"
    s "…"
    s "This is a dog."
    chd "Woof!"
    a "Oh. Okay. Yes. That makes perfect sense."
    a "Sensei...wants to get me a present and...is looking at dogs..."
    m "That's-"
    a "It is clearly a dog, Maya. Just look at it."
    m "…"
    s "Nothing to see here."

    scene whyissheadog14r
    with dissolve

    m "What the actual fuck?..."
    a "Let’s go, Maya. Staying here and getting to know the dog will spoil the surprise."
    s "That’s a good idea. Hurry along, Ami. Forget what you saw here."
    a "I will. I'm sorry for bothering you on your day off, Sensei. I’ll see you later."

    scene whyissheadog15
    with fade

    if bonus == True:
        m "Do you need me to call the police?"
        s "Maya, come on. There is a perfectly reasonable explanation for this."
        chd "Woof!"
        m "…"
        s "…"
        m "Run."
        m "Run as far away as you can."
    else:
        m "Whatever you do, don't talk about clowns."
        m "I know from previous timelines that he really likes them."
        chd "Woof!"

    scene whyissheadog16
    with fade

    a "..."

    "Maya leaves, but Ami appears to be having some difficulty regaining control of her legs."

    a "..."
    s "..."
    a "You know...the more I look at her-"
    s "Forget what you saw here, Ami."
    chd "Woof!"
    a "..."
    s "..."

    scene whyissheadog17
    with dissolve

    a "My head hurts..."
    s "Okay. We’re heading back to your sister’s store now whether she likes it or not."
    chd "Chinami agrees! She feels like that could have gone better!"

    scene black
    with dissolve2

    "Thankfully, by the time we get back to the boutique, Chika’s already caught up on restocking the store and is able to take Chinami back without issue."
    "Myself, on the other hand..."
    "Well, it looks like I might have some explaining to do later..."

    $ renpy.end_replay()
    $ chika_love += 1
    $ mall15 = True
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label mall20:
...
```

## Code that triggers this event
File: \game\ChikaEvents.rpy
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
...
```