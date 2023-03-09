# Residual Sadness
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotodorm20&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 20

✅Day of week is not Tuesday

✅Event "[Maki: Beautiful Porn Salesman](./makidate1.md)" is completed (event=makidate1)

✅Event "[Makoto: Aftermath](./pornshop20.md)" is completed (event=pornshop20)



## Next events
* [Makoto: Service Charge](./pornshop25.md)

## Event properties
* ID: makotodorm20
* Group: Makoto
* Triggered by label: makotodorm
* Triggered by branch label: makotodorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm20:
    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Makoto, are you around right now?"
    mak "I am! Do you need something, Sensei?"
    s "Yes. Attention."
    mak "Request denied. Please come back later."
    s "What's that? You want me to come in now?"
    mak "Why speak at all if you're not going to listen to what the other person is going to say?"
    s "Good question. We can talk more about it when I'm inside of your room."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    mak "What the- I could have sworn I locked that door."

    "I push my way into Makoto’s room and leave my shoes at the door."
    "I expect to find her sitting at her laptop, reading about...leaves or some other boring stuff she’s probably into but, to my surprise, she’s laid out on the couch just...relaxing."
    "I didn't realize she knew how to do that."

    scene makotocouch1
    with dissolve2
    play music "love.mp3"

    mak "Welp, it looks like my plans for the night have been drastically altered."
    s "Your plans for the night are already weird. Shouldn't you be studying or something right now?"
    mak "Probably. But I've decided to take the night off."

    if bonus == True:
        s "I kind of figured you'd have your laptop on and your pants off right now if that were the case."
    else:
        s "Good. You deserve it."

    scene makotocouch2
    with dissolve

    mak "Congratulations. If you were going for the “Quickest time between entering the room and pissing off Makoto” award, you’ve just destroyed the previous record."

    if bonus == True:
        s "Thanks, but I’m sure I’ll find a way to beat it again in the future."
        mak "I’m sure you will as well."

        scene makotocouch3
        with dissolve

        mak "So what’s up? I don’t want to have sex tonight."
        s "I haven’t even asked for that yet."
        mak "‘Yet’ implies that you were planning on asking."
        s "Well, I never really {i}plan{/i} on asking for things like that. They just kind of naturally happen."
        mak "I can’t tell if you’re being serious or if you’re mocking me for having to ask you to fuck me eight million times before you finally did."
        s "I think it was a few million more than that. You seemed pretty desperate at a few points."
    else:
        s "I was just trying to be nice."
        mak "Oh. Sorry. I must have misheard you."

    scene makotocouch4
    with dissolve

    mak "I'm going to courteously forget the fact that you just said that and extend a formal invitation for you to relax with me as well, Sensei."
    mak "You may not {i}work{/i} as much as you used to, but you still deserve a night off every now and again."
    s "A night off from what? My entire life is pretty much just one big vacation at one point."
    mak "Hmm..."

    if bonus == True:
        mak "Then maybe you can take the night off from being a perverted bastard?"
        mak "Think you can be this close to a girl in leggings without getting abrasive?"
    else:
        mak "But hey, if I can sit on the couch without being swallowed by it, I'm sure you can too."
        s "Is it alive?"
        mak "Is that a problem?"

    s "Probably not, but I will try if that’s what you truly desire."
    s "You sure you’re going to be okay not studying, though? If you’re feeling shaky or cold, it might be a sign of withdrawal."
    s "It might be better if you at least study a {i}little{/i} bit so we don’t need to rush you to the hospital."

    scene makotocouch5
    with dissolve

    mak "Stop treating my thirst for knowledge like it’s some sort of drug addiction. "

    if bonus == True:
        mak "You don’t see me trying to get you to wean off pornography little by little."
        s "That’s right. You’ve been trying to get me to quit cold turkey since day one and all it's done is make my desires stronger."
        mak "Oh, I’m well aware. You can't even make eye contact with me in the shop without undressing me in your mind."
        s "Makoto, something you should know about me is that I am constantly undressing {i}everyone{/i} in my mind and it doesn't really make a difference where I am when it's happening."
    else:
        s "I was addicted to drugs once. It was a horrible experience."

    scene makotocouch6
    with dissolve

    mak "Okay, time to change the conversation topic."
    mak "I thought telling you I had no intention of doing anything uncouth tonight would have been a good enough cue for you to abandon your affinity for all things sexual, but I can see now that is not the case."
    s "Sorry. I'm probably just confused about what to do since we don’t have normal conversations all that often."

    scene makotocouch7
    with dissolve

    mak "I think our conversation in the park the other night was relatively normal."

    if bonus == True:
        mak "At least until we got to the part where Ayane’s butler found me in a groggy state of delirium after you shredded my insides with your monster-cock."
        s "I have no regrets."
        mak "Neither do I. I’m sure younger Makoto didn’t envision losing her virginity like that, but I’m honestly still kind of high off of the fact that it happened."
        s "And yet you don’t want to have sex tonight."
        mak "Does that disappoint you?"
        s "A little."

        scene makotocouch8
        with dissolve

        mak "Well, I doubt you'll derive any sexual pleasure from it, but if you'd like to sit next to me and let me rest my legs on you, I think I’d be up for that. "
        s "Great idea. I think it would be a little better if you took your clothes off and put your legs {i}around{/i} me instead, though."

        scene makotocouch9
        with dissolve

        mak "And I think it would be a little better if you were to jump off a bridge."
        s "Fine. Be abstinent for the night, then. Just move over so I can sit down if that's going to be the case."
        mak "Move me yourself. You're a big, strong man, aren't you?"
    else:
        s "What conversation? That was cut out in this version."
        mak "Was it really? I liked that one a lot. It was really important to me."
        s "Becuase of how important our hug was that one time, right?"
        mak "Something like that."

    scene black
    with dissolve2

    if bonus == True:
        "I sigh to myself and pull Makoto’s legs up high enough for me to get underneath them."
        "She bends very easily despite me lifting them a bit higher than necessary and it makes me question whether or not she’s actually really flexible."
        "I'll have to find out when she goes back to desire, as she so aptly described earlier, {i}having her insides shredded by my monster cock.{/i} "
        "........."
        "......"
        "..."
    else:
        "The screen fades to black and the shot changes."

    scene makotocouch10
    with dissolve

    if bonus == True:
        mak "Wow! You’re touching my shoulder and not my chest. It’s almost like you actually care about me or something."
        s "I do actually care about you, though."
        mak "Do you?"
        s "Of course."
    else:
        mak "Wow! You’re touching me and not just hugging me. It’s almost like you actually care or something."
        s "I do actually care, though."
        mak "Do you?"
        s "Of course."

    scene makotocouch11
    with dissolve

    mak "I bet I care about you more."

    if bonus == True:
        "That’s probably a safe bet."
        "Makoto’s had a thing for me since long before I was {i}me.{/i}"
        "I can't even begin to imagine how many others took advantage of that."
    else:
        s "Don't turn our affection for one another into a competition, Makoto. It is mean."
        mak "You are right and I apologize. I just think there needs to be some sort of technical measurement for things like that."

    s "Probably. There’s not really a good way to measure something like that, though, so arguing about it can only get you so far."
    mak "Spoken like a true...guy who doesn’t care as much about a girl as the girl cares about him."
    s "Creative title, Makoto."

    scene makotocouch12
    with dissolve

    mak "I do what I can."
    s "You certainly-"
    mak "Can I be your girlfriend?"

    if bonus == True:
        s "…"
        mak "…"
        s "Makoto-"
    else:
        s "No. I do not see you that way, but I do not want to hurt your feelings. It is probably best for us to remain the way we-"

    scene makotocouch13
    with dissolve

    mak "Just kidding."

    if bonus == False:
        s "Oh."

    scene makotocouch10
    with dissolve

    mak "I know you can’t say yes to that."
    mak "I looked into it more and there are actually seven different rules prohibiting that type of relationship between a teacher and a student anyway."
    mak "But, if one of us were to just...stop coming to[school], we could probably pull it off."
    s "I’m sure your parents would love that."
    mak "My parents have probably the weirdest relationship I’ve ever heard of, so I wouldn’t take any of their thoughts on {i}us{/i} that seriously."

    if harukalust10 == False:
        "Now that she mentions it, I do remember Makoto’s mom saying something about her marriage being an open one before."

    else:
        "She’s got a point."

        if bonus == True:
            "Maki didn’t even have a second thought about the threesome with Haruka. "
            "Is her husband really okay with things like that?"

    s "How so?"
    s "I don’t really know much about your parents other than the whole...porn business thing."

    if bonus == True:
        mak "To be fair, the porn business thing should have been a big enough tip-off for you to realize something’s a little abnormal."
        mak "My parents have an open relationship, so it was never uncommon for more people to start getting involved."
        mak "And I don’t mean involved with {i}me{/i} or anything. Mom and Dad actually tried really hard to make things as normal as possible for me."
        mak "But when you grow up reading love stories and hearing all of these tales about soulmates, it’s kind of hard to understand the concept of being with...multiple people."
        s "Is their relationship really {i}that{/i} open? "
    else:
        mak "They do that thing where they hug other people sometimes. It makes me feel all weird and stuff."

    s "How often did they see other people?"

    scene makotocouch14
    with dissolve

    mak "Believe it or not, it was never really my mom who went off with others."
    mak "Like, yeah it happened every now and then, but it was my dad who really took advantage of the open relationship thing."
    mak "Sometimes, he’d disappear for days at a time and I’d need to pretend that I didn’t understand why."

    scene makotocouch15
    with dissolve

    mak "But then he’d come back and, suddenly, everything would be normal again."
    mak "We’d all laugh and dine together like nothing ever happened."
    mak "It all felt so fake."
    mak "I think it was especially hard on me since I always liked my dad a little more than my mom."
    mak "If you cut out his tendency to disappear, he really was the ideal father."
    mak "You know how in some families, one parent always says no to stuff and the other always says yes?"
    s "Was Maki really the type to deny you things? She seems really...laid back."
    mak "Oh, no. She was the one who said yes to everything."
    mak "It was my dad who always said no."
    s "…"
    s "I’m having a hard time figuring out why that would make you like him more."

    scene makotocouch16
    with dissolve

    mak "Because he was responsible, obviously."
    mak "I was, by no means, a normal little girl."
    mak "I think I even asked for an encyclopedia for my birthday one year."
    mak "So having a father who would say no to so many things helped me mature to a certain extent."
    mak "It really ingrained the idea of this world not being mine into my head."

    scene makotocouch17
    with dissolve

    mak "What were your parents like, Sensei?"
    mak "Did you learn anything valuable from them?"
    s "…"

    "My parents?"
    "…"
    "I-"
    "I don’t know."
    "I can’t even remember their faces."
    "But I guess that just means they were never really important to me to begin with."

    s "Not really. "
    mak "Hmm...I guess that explains why you’re such a manipulative degenerate then."
    s "You’re also a bit of a degenerate and you had at least one really solid parent while growing up."
    mak "Yeah. One really solid parent who’s probably had his way with a trillion women. "
    s "There aren’t even a trillion people on Earth."
    mak "If there were, I’m sure he would have had his way with all of them."
    s "So...you dislike him now or something?"
    s "I’m having a hard time gauging your feelings for your father, to tell you the truth."
    mak "Of course not. I love him more than anything."
    mak "It eats away at me inside not being able to see him while he’s up there in space doing...whatever the hell it is they're in space for."

    scene makotocouch17r
    with dissolve

    mak "And it kind of sucks that...in order to make myself feel a little better about him being gone, I need to pretend he’s with someone other than my mom."
    mak "You'd think that seeing him disappear over and over again throughout my life would have prepared me for this, but...{i}nope.{/i}"
    mak "It's not fair. How come {i}he{/i} had to leave but someone like {i}you{/i} got to stay?"
    mak "No offense, of course...I just..."

    scene makotocouch18
    with dissolve

    mak "I just want him to come home, you know?"
    mak "Also, I wouldn’t have to work as much if he were back in Kumon-mi and I could spend less time being harassed by you and more time doing things like this."
    s "At least you’re still able to joke about it. "
    s "Some people can’t even do that much."

    scene makotocouch19
    with dissolve

    mak "I’m a special case."
    mak "But don’t think for one second that I’m invincible. "
    mak "It hurts a lot."
    mak "More than you could imagine."
    mak "And I know it’s dumb to say that when my problems are infinitesimal compared to others..."
    mak "But it {i}does{/i} hurt...really...really bad..."

    scene makotocouch20
    with dissolve

    mak "But forgive me for losing my composure just now. I know I shouldn't be burdening you with that after suggesting you take the night off with me."
    s "I don’t care at all."
    s "Are you going to be okay, though?"
    s "I’m having a hard time believing this is something that you’re just thinking up now."
    s "In fact, I know enough about you to assume that you’re only taking a “break” tonight because this has really been bothering you, hasn’t it?"
    mak "…"
    s "…"

    scene makotocouch21
    with dissolve

    mak "Nope."
    s "Makoto."

    scene makotocouch22
    with dissolve

    mak "Okay. Maybe a little bit."

    if bonus == True:
        mak "But that doesn’t have anything to do with why I don’t want to have sex tonight, if that’s what you were wondering."
        s "Well, I wasn’t. But I kind of am now."
        mak "Let's just say that I'm a lot happier having you hold me tonight."
        mak "Weirdly enough, having you nearby basically {i}always{/i} makes me feel a little better."
        mak "Even if you’re one of the worst people I’ve ever met."
        s "Hey now. You’re supposed to admire me, remember?"
        mak "I do admire you. I think about you all the time."
        mak "It’s actually kind of unhealthy."
        mak "But also, you kind of suck. You do know that, right?"
        s "Oh, absolutely. "
        s "But I’m glad that doesn’t ruin your opinion of me for whatever reason."
        mak "Yeah...I’m glad too."

    play sound "dooropen.mp3"
    scene makotocouch23
    with dissolve

    mi "I’m hooooooooooome!"
    mak "Oh. Miku’s back."

    scene makotocouch24
    with dissolve

    mak "Welcome home."
    mi "...And now I’m leaving again!"
    mi "Goodbye!"

    play sound "dooropen.mp3"
    scene makotocouch25
    with dissolve

    "Miku bolts out of the room as quickly as she arrived and I am suddenly a barrier preventing her from using her own dorm."

    mak "Well, I'm sure that was awkward for her."
    s "We don’t need to worry about her saying anything, do we?"

    scene makotocouch26
    with dissolve

    if bonus == True:
        mak "What would she even say? We’re not doing anything wrong."
        s "We definitely look a little closer than teacher and student, though."
        mak "We {i}are{/i} closer than teacher and student."
        mak "As long as we have our clothes on, I doubt Miku will think anything of it."
        s "If you say so..."
    else:
        mak "You mean like an inappropriate joke or a reference to something that makes the two of us uncomfortable?"
        s "Yes. I do not like being around such conduct."
        mak "I think we will be safe."

    scene black
    with dissolve2

    "Despite being basically told that Miku is a non-issue, I still feel a little strange about sticking around while she’s likely just...waiting in the hallway."
    "Frankly, I wouldn’t mind if Miku came in as well, but..."
    "Well, I can only assume that she would be a bit uncomfortable in that sort of environment."
    "So, after another few minutes of letting Makoto rest her legs on me while waiting for her residual sadness to subside, I get off the couch, put my shoes back on, and head home."
    "I apologize to Miku for stealing her room on the way out."
    "It's her turn to comfort Makoto now."

    $ renpy.end_replay()
    $ makotodorm20 = True
    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label makotodorm25:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if makoto_love >= 5 and firsttimepornshop == True and makotofirsthall == True and makotodorm5 == False:
                jump makotodorm5
            if makoto_love >= 20 and day != 2 and makidate1 == True and pornshop20 == True and makotodorm20 == False:
                jump makotodorm20
...
```