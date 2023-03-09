# Disappointing Everyone
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas4&go=Go)


Part of event chain [Fuck Christmas](./christmas3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmas4
* Group: Main
* Triggered by label: christmas3

## Event code
File: \game\script.rpy
Code:
```python
...
label christmas4:
    if _in_replay:
        play music "christmasyay.mp3"

    if ayanelust10 == True:
        scene ayanekirinchristmas1
        with dissolve

        "A girl who had been filled with Christmas joy just moments ago stands beside an overpriced plasma-screen TV and ponders over how to get herself out of the [[very] uncomfortable situation she’s suddenly found herself in."
        "If we were to put things in Molly’s terms, which we might as well do since she is currently scouring the halls for a vending machine, it’s almost like there's some sort of dark entity lurking between them."
        "And no, the dark entity is not in reference to Ayane’s shadow which is {i}literally{/i} in between the two of them."
        "It’s a reference to how these girls, who may or may not have been “friends” up until recently, are now miles apart emotionally but only two or so feet between each other physically."

        if bonus == True:
            "Though, Ayane will gladly accept two feet over attached and half-nude alongside the man she’s grown to love in recent years."

        ki "Hey. I like your scarf."
        ay "…"
        ki "Did Sensei buy it for you? I saw Ami and Maya had similar ones as well."
        ay "I bought it for myself so I could match them."
        ay "Sensei bought the other two."
        ki "Really? That’s kinda sus."
        ki "Isn’t he supposed to be your boyfriend or whatever?"
        ay "He’s not my boyfriend. I just like him."
        ay "I’ve told you this how many times now?"

        scene ayanekirinchristmas2
        with dissolve

        if bonus == True:
            ki "Wait, you guys {i}still{/i} aren’t dating? Even after giving him your virginity? "
        else:
            ki "Wait, you guys {i}still{/i} aren’t dating? Even after hugging?"

        ki "What the hell is taking so long?"

        if bonus == True:
            ki "You should probably be more careful about who you give yourself to if that’s the case, though."
            ki "All guys care about is sex, so there’s always a chance he could just be using you or something like that."
            ki "He {i}was{/i} kinda crazy hard when he was screwing you, so it’s definitely possible."
            ki "Not like it matters to me or anything, but yeah."

        scene ayanekirinchristmas3
        with dissolve

        ay "What do you want, Kirin?..."
        ay "I obviously don’t want to talk to you, so it’s probably best if you mind your own fucking business."
        ay "Not like it matters to me or anything, but yeah."
        ki "Hey, now! No reason to get all toxic, Ayane. I’m just chatting with an old friend at a party."
        ki "That’s what friends do, isn’t it?"
        ay "Yup. And that’s how I’m sure tonight would have went if you never pulled that stunt at the beach."
        ay "Do you think that’s how friends are supposed to act with each other?"
        ay "I told you something in confidence and you used it against me."

        if bonus == True:
            ki "Hey, all I did was stumble across two people fucking each other. How is that pulling a stunt?"
            ki "You started it. Just try not getting horny at a moment’s notice and things like that won’t happen."
        else:
            ki "Is this about the fucking sandcastles again? Give me a break."

        ay "Kirin...leave me alone."
        ki "Hmmm, all these negative feelings must be why I wasn’t invited to your Halloween party."

        scene ayanekirinchristmas4
        with dissolve

        if bonus == True:
            ki "{i}You’d think after sharing a dick, the two of us would have become closer. Am I right?{/i}"
            ki "{i}Like, how many other girls here can say you grinded on their hand? We’re kind of super close, whether you like it or not.{/i}"

        ay "{i}Please...go away...{/i}"
        ki "But everyone else here is so boring."

        scene ayanekirinchristmas5
        with dissolve

        if bonus == True:
            ki "Wanna see if Sensei has some free time to take us downstairs and-"
        else:
            ki "Wanna see how many marshmallows we can fit in our mouths or something?"

        scene ayanekirinchristmas6
        with dissolve

        ka "Kirin! They have pancakes here!"
        ki "...Yeah? And?"
        ka "You love pancakes! And these ones are really good!"

        scene ayanekirinchristmas7
        with dissolve

        ki "Didn’t you just fucking eat before we came here?! Shouldn’t you be watching your weight?"
        ka "No way! It’s Christmas! "
        ka "Here, come eat some!"

        scene ayanekirinchristmas8
        with hpunch

        ki "I DON’T WANT ANY FUCKING PANCAKES, KARIN! LEAVE ME ALONE!"

    else:
        scene ayanekirinchristmas9
        with dissolve

        "Two girls meet beside an overpriced plasma-screen TV and greet each other in kind because that’s what friends do. "
        "They greet each other."
        "Hello. How are you doing?"
        "Have you been enjoying the weather lately?"
        "These are not things they actually say, but moreso just examples of things that you, a real human being, can say if you ever find yourself in front of a plasma-screen TV with a person you’re kind of cool with."
        "But these two, being several steps beyond conversing about the weather, decide to talk about the one thing they have in common more than anything else-"
        "Their love for Christmas."

        ki "Hey! Long time, no see."
        ki "Was starting to think I’d go the whole winter break without running into you."
        ay "You have my number, you know? You could always ask me to hang out when I’m not doing anything."
        ki "True, true. But I figured with it being the holiday season and all, you’d probably be spending a little more time with you-know-who."

        scene ayanekirinchristmas10
        with dissolve

        ay "No...not much more time than normal."
        ay "He’s got a lot of other girls who are important to him, so it’s not like he can {i}only{/i} spend time with me, whether I want him to or not."

        if bonus == True:
            ki "You sure you’re okay with that? Guys tend to only think about what they can stick their dick inside, don’t they?"
        else:
            ki "You sure you’re okay with that? Guys tend to only think about free golf lessons, don't they?"

        scene ayanekirinchristmas11
        with dissolve

        ay "Sensei isn’t like that. He’s kind and compassionate and actually cares about everyone. "
        ay "You should try actually getting to know him sometime. "
        ay "I’m sure he seems like just another guy, but he really is a special person."

        scene ayanekirinchristmas12
        with dissolve

        ki "I already know him pretty well...But how come you’re gettin’ all sappy all of a sudden?..."
        ki "That’s not really like you."

        scene ayanekirinchristmas13
        with dissolve

        ay "Because it’s Christmas!"
        ay "We’re supposed to be saying sappy stuff to each other and spreading around all of the Christmas joy!"
        ki "Umm...well, I mean, I like Christmas too...but I’m not really a fan of all that sentimental stuff."
        ki "I kind of just like being able to eat disgusting amounts of chicken without anyone judging me."

        scene ayanekirinchristmas14
        with dissolve

        ki "But...I guess it {i}is{/i} kind of nice getting attention and stuff too."
        ki "My grandma normally comes over around this time of year and always gives me money and stuff."
        ki "Not like you’d care, though, little miss black-card."
        ay "See? This is exactly the kind of stuff we’re supposed to be talking about- the things that make us happy. "
        ay "My mom always liked Western Christmases when I was growing up, but this was back before the bubble wrap thing."
        ay "So we’d always wake up early in the morning and open the few presents we were able to get for each other and then spend the entire day together."

        scene ayanekirinchristmas15
        with dissolve

        ay "Things aren’t like that anymore."
        ay "But at least now I have other special people to spend the day with. "
        ay "And even if it’s not a “traditional” Christmas in the sense I’m used to, it’s something I wouldn't mind becoming tradition."
        ay "As long as I can continue to be around Sen...{i}everyone{/i}, I’m sure there will be plenty of Christmas memories to be made that are just as good as the old ones."
        ki "…"
        ay "…"

        if bonus == True:
            ki "You got laid last night didn’t you?"
        else:
            ki "You made a bone necklace last night, didn’t you?"

        scene ayanekirinchristmas16
        with dissolve

        ay "Wha-?! "
        ay "Kirin!"
        ki "What?"

        if bonus == True:
            ki "You smell like you got laid."
        else:
            ki "You smell like bones."

        ay "What does that have to do with Christmas?!"

        if bonus == True:
            ki "Idunno. You were talkin’ about making new memories and stuff so I kinda just figured you meant you were getting Christmas-style boned all night."

            scene ayanekirinchristmas17
            with dissolve

            ay "What would doing it...Christmas-style even entail?..."
            ki "I don’t know. Maybe you were dressed like an elf? Could mean anything."
            ki "Didn’t you sleep over at Ami’s place, though?"
            ki "Did you really fuck her [uncle] while she was around? That’s kind of sick, Ayane."
            ki "You’re even bolder than I thought you were."
            ay "N-Nothing like that happened! I slept in the bed with Ami and Maya. You can ask either of them..."
            ki "Hmm...well, either way, I hope you get to make some {i}Christmas memories{/i} soon, if you catch my drift."
        else:
            ki "Idunno."
            ki "Listen you can make bone necklaces whenever and wherever you want."

        scene ayanekirinchristmas18
        with dissolve

        ki "Just make sure the coast is clear if you do. Wouldn’t want Ami or somebody catchin’ you in the act, now would you?"
        ay "I...have no idea what you’re talking about..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene ayanekirinchristmas19
    with dissolve

    s "Hey. Why are you guys sitting on a bed with two swans kissing behind you?"
    a "We were actually just talking about that."
    m "Please don’t draw any more attention to it. It’s a hurdle Ami and I have overcome as best friends."
    s "I will not draw any attention to it as long as Maya helps me with something."

    scene ayanekirinchristmas20
    with dissolve

    a "Maya? What do you need her help with?"
    m "Yeah, what? Why am I suddenly involved?"
    m "All we did was walk here together. You don’t think this means we’re close now, do you?"
    m "Go ask Ayane. I’m sure she’s willing to help."
    a "Probably {i}too{/i} willing. Ask me instead."
    s "Fine, then. Ami, who did I have for Secret Santa?"

    scene ayanekirinchristmas21
    with dissolve

    a "You didn’t get your Secret Santa a present?!"
    a "How could you do this?! You’re literally ruining Christmas for the rest of our lives!"
    s "That’s a little dramatic, don’t you think?"
    a "Not at all!"
    a "And why would Maya even know who you have? That’s something you’re supposed to keep track of yourself so the surprise isn’t ruined."
    m "She’s right."
    m "There’s no way for me to know who you’d have. You never told me."
    m "You’re probably just misremembering something."
    s "Wait, really? I could have sworn I {i}told you{/i}."

    scene ayanekirinchristmas22
    with dissolve

    m "Again, I have no idea."
    m "The only way to find out is by waiting until the end of the night and then disappointing someone."
    m "But I’m sure you’re already used to disappointing everyone, so that won’t come with much difficulty for you."
    s "You always know exactly what to say to cheer me up, don’t you?"
    m "Of course. Just like you always know exactly how to annoy me."

    scene ayanekirinchristmas23
    with dissolve

    a "Listening to you two is kind of like listening to a pair of divorced senior citizens."

    if bonus == True:
        m "No it isn’t because that implies that the two of us would have had to have been romantically involved at some point."
        s "Yeah, and I’d never divorce Maya. Even if all she does is insult me. That’s just part of her charm."
    else:
        m "Great. Now I'm just sad. Thanks, Ami."
        s "Don't frown, Maya. I'll always be here as your friend."

    scene ayanekirinchristmas24
    with dissolve

    m "Why are you still here? Shouldn’t you be out buying a generic present for whoever your Secret Santa is?"
    a "Yeah, if you didn’t get anything, you’re either going to need to go buy something right now or just give something you have on you to your Santa person."
    s "I didn’t even think of that..."

    "A generic gift might just be crazy enough to work as long as I can find something...serviceable."
    "I’m dealing with a bunch of [teenage]girls here. Buying a generic present is probably as easy as buying a bottle of perfume or something along those lines."
    "But...perfume can be kind of expensive."
    "Let’s see what I have in my pockets."

    scene ayanekirinchristmas25
    with dissolve

    m "Now what?..."
    m "What are you doing?"
    a "You’re not looking through your pockets to see if there’s anything you could give someone, are you?"
    s "Leave me alone. I have my methods."
    m "You’re not just disgusting. You’re a complete idiot."
    s "Do you think...700 Yen would be a good present?"
    a "…"
    m "…"
    a "No."
    a "Our limit was 2,000 Yen."
    s "Yeah but that’s just a limit. You can go under that as long as the present has some sort of emotional value."
    m "And I’m sure the coins you just pulled out of your pockets and picked lint off of are just teeming with emotional value."
    s "You have no idea how much these coins mean to me, Maya."
    m "They mean literally nothing. You’re trying to pass them off as presents."
    m "You probably didn’t even know you had them until thirty seconds ago."
    s "Fine. I’ll go buy an actual present. "
    s "But I won’t be happy about it."
    a "You’re never really happy about anything, so that’s probably fine."
    s "…"
    s "I’ll be back."
    a "Okay, but don’t get lost. It’s kind of a big hotel."
    m "No, it’s fine. You can get lost. "
    m "You will not be missed."
    s "I’ll definitely be back..."

    scene black
    with dissolve2

    "I make my way to the door, hoping I’m able to find a gift shop or something similar downstairs."
    "Of course, though, I’m met with another five-foot obstacle as soon as I get to the door."

    scene ayanekirinchristmas26
    with dissolve

    mo "Is everything okay, Sir? You appear to be in a rush."
    mo "If you are low on mana, I’ve just placed an entire satchel worth of potions on the-"
    s "Molly, I’m in a hurry. "
    mo "A hurry for what? What’s going on?"
    s "Something big. And serious."
    mo "Big?...Serious?"
    s "Just...come with me. I’ll show you."

    if bonus == True:
        scene ayanekirinchristmas27
        with dissolve

        mo "H-Hold on a second, Sir! You need to show me something {i}big{/i} and {i}serious{/i} right now?!"
        mo "Do you have any idea how something like that sounds to a girl who’s played as much eroge as me?!"
        s "Are you coming or not? I really don’t have time to deal with your ramblings right now."

        scene ayanekirinchristmas28
        with dissolve

        mo "I-If you’re going to p-p-pressure me, the least you can do is hear my concerns!"
        mo "I’m not ready for this to go where it’s going in my head!"

    scene black
    with dissolve

    "I grab Molly by the wrist and pull her out of the hotel room."
    "Someone like her finding out I forgot my Secret Santa present probably won’t be as demeaning as someone like Makoto or even Chika finding out."
    "If anything, I feel like Molly might actually be a good person to help me pick something out."

    mo "S-Sir! Your strength level far surpasses mine! "
    mo "My wrist is being critically injured and all of the medkits are upstairs!"

    "........."
    "......"
    "..."

    scene ayanekirinchristmas29
    with dissolve

    if bonus == True:
        mo "I never thought my first time would be in a hotel gift shop on Christmas day."
        mo "Is this even legal?"
        s "If you still think this is something sexual after coming all the way here, you’re even more hopeless than I am."
    else:
        mo "Are we really about to hug in a hotel gift shop?"
        mo "Is that even allowed?"
        s "Surprisingly, we are not here to hug."

    mo "Well then what is it? What is this confounded side-quest that has pulled me from the main story chain once more?"
    s "I forgot a...key item. Or something."
    mo "A key item? But the only key items required for tonight’s mission are-"

    scene ayanekirinchristmas30
    with dissolve

    mo "You forgot to buy a present!"
    s "Wow, you picked up on that faster than I thought."

    scene ayanekirinchristmas31
    with dissolve

    mo "This is even more serious than I imagined..."

    if bonus == True:
        s "Up until five seconds ago, you thought we were about to have sex."
        mo "Sex is temporary. Christmas is forever."
    else:
        s "Up until five seconds ago, you thought we were about to hug."
        mo "Hugs are temporary. Christmas is forever."

    s "No it’s not. It’s 24 hours long. "

    scene ayanekirinchristmas32
    with dissolve

    mo "Well...who are you shopping for exactly?"
    s "I...don’t know."
    mo "So you’re trying to farm an item for a quest before you even pick it up? How can you be sure you’ll get the right one?"
    s "I can't. That’s exactly why I need your help. "
    s "I need you to help me choose something that any girl in class would like so that, when I find out who I’m supposed to give this to, it will go over well."

    scene ayanekirinchristmas33
    with dissolve

    mo "Hmm...I see. I see."
    mo "Luckily for you- I, Molly MacCormack, am an expert when it comes to winning the hearts of [teenage]girls."
    mo "I’ll have you know I’ve fully completed nearly every VN CG gallery on my computer, so it’s safe to say I’m kind of an expert when it comes to things like this."
    mo "What [teenage]girls want more than material goods is an {i}experience{/i}, Sir."
    s "Cool. What {i}experience{/i} can I buy with 2,000 Yen?"
    mo "Heheh~ You can thank me later, as you won’t even need that much."
    mo "And perhaps...you won’t even need to thank me at all."
    mo "Perhaps the experience itself will be fated to be my own."
    s "And it won’t ruin the surprise if the present winds up being for you?"
    mo "Not at all. For this particular experience is sure to move the heart of any [teenage]girl. "
    mo "And I thank you for giving out an opportunity to make this [young_girl]’s dreams come true, Sir!"
    s "Sure, Molly. Just point out whatever thing you want me to buy and we can get back upstairs."

    scene ayanekirinchristmas34
    with fade

    mo "It would be my pleasure..."

    scene black
    with dissolve2

    "Molly immediately hoists a white bottle into the air as if it’s some sort of sacred sword or whatever it is warriors typically hold up in fantasy movies."
    "I initially think she’s trying to buy alcohol but it looks like it’s...just an empty bottle?"
    "Maybe it's just a weirdly shaped...vase or something?"
    "Is that a thing girls like?"
    "Either way, it’s not like I have time to debate this right now, so I’ll just have to trust her judgement and see how things play out."
    "At least I know she’ll appreciate the strange bottle if I wind up having to give it to her."

    $ renpy.end_replay()
    $ christmas4 = True
    $ molly_love += 1
    stop music fadeout 10.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

label christmas5:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```