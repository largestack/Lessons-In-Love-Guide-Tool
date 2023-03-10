# Ten Steps Forward (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 35

* Event [Two Steps Back](./rindorm30.md) (Rin) is completed)



## Next events

* [Futaba: No, You](./library35.md)
* [Rin: I Died With You](./cafe35.md)
* [Haruka: Performance Review](./harukadate10.md)

## Event properties

* Id: rindorm35
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm35

## Official wiki page

[Ten Steps Forward](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm35&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm35:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "…"
    "I knock on Rin’s door and wait to hear if there’s a response. "
    "She was doing a lot better the last time I saw her, so I’m hoping that things have all but healed by now."
    "One of the good things about Rin is that she makes it very apparent whenever she’s down."
    "And I mean {i}very{/i} apparent. "
    "You’ve seen her. You know what I’m talking about."

    play sound "knock.mp3"

    "I knock again when there’s no response."

    s "Hey, are you in there?"
    s "I’m bored."
    r "Door’s open, Sensei."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Having received Rin’s blessing, I prepare myself for whatever lies within her room."
    "Which version of her will I see today?"

    scene ringlow1
    with dissolve
    play music "sleepystreets2.mp3"

    r "Yo."

    "Ah. I see I’ve stumbled upon the broken one once again."
    "I feel like it’s lasted a little longer this time, but at least she hasn’t slipped into another state of delirium."

    s "How are you feeling?"
    r "Me? Oh, you know...Tired. Sad. Hungry. Bored."
    s "Well hopefully I can make at least one of those go away."
    r "Did you bring food? I feel like the hunger issue would be the easiest to solve."
    s "I regret to inform you that I do not have any food."

    scene ringlow2
    with dissolve

    r "Damn. Back to the drawing board it is, then."
    s "We could always go out to eat if you want."
    r "What, you mean looking like this?"
    r "News flash but I look like a cross between a zombie and a serial killer."
    s "Serial killers aren’t normally this cute."
    r "They’re not normally this hungry either. What with all the bodies they eat and stuff."
    s "Not all serial killers eat their victims, Rin."
    r "No, but the best ones do."

    scene ringlow1
    with dissolve

    r "What would you do with your victims if you were a serial killer, Sensei?"
    s "What would I do?"
    r "Yeah. Like your signature. They’ve all got one."
    s "I...haven’t really thought about it before."
    r "If I ever started killing people, I think my trademark would be something involving tongues."
    s "I’m glad you’ve put so much thought into it."

    scene ringlow3
    with dissolve

    r "Think about it, though. The tongue has so many uses. It’s an underrated muscle."

    if bonus == True:
        r "You need it to speak...to taste. Plus, you can use it sexually. There’s no other part of your body that can do all three of those things."
    else:
        r "Oh! Know what else is underrated? The 1993 Disney classic, Cool Runnings."

    "Okay, maybe Rin {i}has{/i} slipped into delirium again."

    s "Are you sure you’re okay?"
    r "No. But I haven’t hurt myself today, so at least there’s that."
    s "Well...that’s definitely a start."

    scene ringlow2
    with dissolve

    r "Yeah...I’m getting there, though. I can feel it."
    r "Sometimes, I’m even able to make it a full hour without thinking about her if I try hard enough."
    s "Is she still texting you?"

    scene ringlow4
    with dissolve

    r "Yeah...I’ve been trying to keep my phone off as much as possible so I won’t have to deal with it, though."
    s "And you haven’t even thought about, you know, actually {i}talking{/i} to her?"
    r "Of course I’ve thought about it. But despite how I may seem to you, I’m not really one of those go-getter types."
    r "I’m actually a huge coward. "
    r "I don’t like facing my problems when it’s easier to just lock myself in my room and wait for them to go away."
    r "Downside is that those problems always have a way of catching up to you in the end. But it is what it is."
    r "I’ll just stay here all sad, hungry, tired, and bored or whatever."
    s "Until you have to come out, that is."

    if rinbetrayed == False:
        scene ringlow5
        with dissolve

        r "Oh, speaking of which."
        r "I’ve been thinking a little more about that...post-heartbreak trip and..."
        r "Well, I think it might be best if I do...explore a little."

        if bonus == True:
            s "...Are you coming onto me right now?"
            s "I know you’re normally into girls but, if you really want to-"
        else:
            s "I hope that wasn't a pass at me, young lady. We are destined to remain homies forever."

        scene ringlow6
        with dissolve

        if bonus == True:
            r "I meant like, physically explore."
            s "Oh, so purely sexual? Yeah, then-"

        r "Like purely {i}exploring{/i}. "
        r "I want to go somewhere with you. Futaba too, if she’s free."
        r "There’s a part of the city that I haven’t been to in a while. "

        if bonus == True:
            r "It’s a little closer to my old middle school than the [high_school], so there hasn’t been much reason for me to go over there as of late."
        else:
            r "It’s a little closer to my old high school than the [high_school], so there hasn’t been much reason for me to go over there as of late."

        r "But hey, change of pace and blah blah blah."
        s "You’re actually ready to start going out again?"

        scene ringlow1
        with dissolve

        r "Probably not. But I’ll do my best to make myself look normal again so I can survive in the outside world for a few hours."
        r "Besides, maybe I’ll find something out there that’ll help take my mind off of stuff a little better."
        r "Like...a new guitar or something."
        s "Sure. I’ll come out with you. Any idea when you’d want to go?"
        r "Haruka’s been pretty flexible with my hours lately, so how about we meet up at the cafe over the weekend?"
        r "Even when I’m not working, I tend to show up there to grab coffee."

        scene ringlow2
        with dissolve

        r "Though, I haven’t really had the motivation to do that lately..."
        s "Sure. That’s fine."

        "It looks like Rin and I will be going out on an excursion the next time I show up at the cafe in the morning."
        "From the sound of it, I think it might wind up taking all day. "
        "I should probably clear up my schedule and be ready for that in the near future..."

        $ rininvite = True

    else:
        scene ringlow1
        with dissolve

        r "Yeah...but I think I’ve figured out a way to do that."
        r "I’m going to...go out exploring soon. "
        r "Look for some things that might help me feel normal again. "
        r "Maybe...try out new guitars or something."
        s "You should bring Futaba along. The two of you might have some fun if you spend the day out doing...whatever girls do."
        r "It’s the same thing as whatever guys do, just cuter."
        s "Then yeah, that."

    s "By the way, what are you watching?"

    scene ringlow2
    with dissolve

    r "Hm? This? Just some music thingy. It helps calm me down."
    r "Most of the music I listen to is super angry and depressing, so hearing stuff like this is a big change of pace."
    s "What’s the point of listening to angry and depressing music anyway? I never understood that."

    scene ringlow1
    with dissolve

    r "It’s nice knowing that other people out there share the same level of misery as me."
    s "So...you’re basically cheering yourself up by hearing about how other peoples’ problems are worse than yours?"
    r "Kind of, yeah. But it’s a little more than that."
    r "It’s like...validation. Or something."
    r "Like, I’m still a [teenage]girl. We’re the prime demographic for overreacting and blowing things out of proportion."
    r "So I’m kind of designed to feel like this at times."
    r "But then again, so is everybody. You know?"
    r "Why listen to happy music when it’s probably just fake? "
    r "Real life is like, 90%% bullshit and 10%% actual good stuff. You know that, don’t you?"
    s "Yeah, it makes a lot more sense when you put it that way."
    s "I’m just having trouble understanding how sadness is somehow able to make sadness go away."

    scene ringlow7
    with dissolve

    r "It’s not really easy to explain...It just does. "
    r "But not all the time. Hence the chill lofi girl."
    s "Right..."
    s "Well, whatever works for you, I guess."

    scene ringlow8
    with dissolve

    r "Pro-tip, though...The next time you come to my room to try and cheer me up, bring a box of doughnuts or a cheeseburger. "
    r "Those have pretty much the same effect on me as an angsty pop punk album, but with more flavor and less ex-girlfriends."
    s "I don’t fully understand, but I’ll definitely stop somewhere and get you a cheeseburger the next time I have to go into damage-control mode."

    scene ringlow1
    with dissolve

    r "Heh...damage control is a good way of putting it."
    r "Between you and Futaba, I’ve barely had any time to feel sad at all."
    r "You guys are ruining my normal strategy of sitting on my bed and staring at the wall for hours on end."

    scene ringlow9
    with dissolve

    r "Now, if only you two knew a way to get me to stop dreaming..."
    s "What do you mean by-"

    play sound "knock.mp3"
    scene ringlow10

    "..."
    "A sudden knock on the door interrupts my train of thought as both Rin and I find ourselves staring at it."

    s "Expecting someone?"
    r "I don’t think so?..."
    r "Maybe Futaba saw you come in and she's just...being a good friend and making sure she’s not interrupting anything?"
    s "I don’t think Futaba believes that anything like that is going on between us..."
    r "Door’s open. You can come in."
    r "I’m not wearing pants, though. Hope that's cool."

    play sound "dooropen.mp3"
    scene ringlow11
    with dissolve

    r "Ah..."
    c "Excuse me..."

    scene ringlow12
    with fade

    c "Wait...what are you doing here?"
    s "Damage control."
    s "What are {i}you{/i} doing here?"

    scene ringlow13
    with dissolve

    c "I...still don’t really know. "
    c "It’s hard to say."

    scene ringlow14
    with dissolve

    c "Do you think you could leave the two of us alone for a little while?"
    c "There’s something I want to talk to Rin about."
    r "Wait...Sensei...don’t-"
    s "Yeah. I’ll let you two talk."

    scene ringlow15
    with fade

    r "{i}Wait a minute!{/i}"
    r "{i}I don’t want you to go!{/i}"
    r "{i}I’m not ready for this...{/i}"
    s "Then make yourself ready."
    s "You said it earlier. Problems always have a way of catching back up to you if all you do is hide from them."
    c "Sensei?..."
    s "I’m going. Don’t worry."
    r "{i}Please...don’t...{/i}"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Have a good night, you two."

    "Neither of them say another word to me as I make my way out of the room."
    "But I’ve overstayed my welcome anyway."
    "Rin’s been hiding from Chika ever since the beach, but has only just now run out of places to go."
    "I’m not sure what’s going to happen in there."
    "All I can hope is that something good comes of it..."

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    "{i}Meanwhile...{/i}"

    scene ringlow16
    with dissolve2

    r "…"
    c "Hey..."
    r "What...do you want?"
    c "Just to talk for a little while."
    c "You haven’t been answering my texts and I’ve been worried about you."
    r "But, why?..."

    scene ringlow17
    with dissolve

    c "Because you’re my friend..."
    c "And {i}look{/i} at you. This isn’t the Rin I know."
    c "The Rin I know is bubbly and full of life and would never look like this."

    scene ringlow18
    with dissolve

    r "That’s not true...I look like this all the time."
    r "I just always hid it from you because...yeah."
    c "If you think your feelings are something you need to dance around, you’re wrong."

    scene ringlow19
    with dissolve

    r "Huh?"
    c "I know that my reaction when you told me probably wasn’t the best...but it’s not like I thought it was weird."
    c "I just...I don’t know. It never occurred to me that you felt that way."
    c "And besides, I always kind of thought my first confession would have been from a boy, so...that was a bit of a shocker."

    scene ringlow20
    with dissolve

    r "I’m sorry..."
    c "Stop apologizing. You didn’t do anything wrong."
    c "I’ve felt like an asshole ever since you told me. I still can't believe I wasn’t able to say anything back then."

    scene ringlow21
    with dissolve

    c "But...I’m going to say something now."
    c "And I want you to pay very close attention because it’s really important."
    r "What...are you doing?"

    scene ringlow22
    with dissolve

    c "Rin Rokuhara."
    c "I can not be in a relationship with you."
    c "My heart belongs to someone else."
    c "But just because I don’t feel the same way about you doesn’t mean that the two of us need to stop spending time together."
    c "In fact, you are hereby obligated to spend time with me because you’re my friend and I love you."

    scene ringlow23
    with dissolve

    r "And...if I refuse?"
    c "I know where you live."
    c "And there’s no bathroom in here so I will literally sit outside of your room until you are forced to come out."
    r "This doesn’t seem very fair..."

    scene ringlow24
    with dissolve

    c "What’s not fair is how you haven’t even been giving me the time of day lately."
    c "I didn’t want to just show up here without giving you the proper heads up, but you really didn’t leave me any choice."
    r "I was embarrassed...leave me alone."

    scene ringlow23
    with dissolve

    c "No. I refuse."
    r "Chika..."
    r "You really don’t have to do this, you know..."
    r "I can only imagine how awkward it must be."
    c "It really doesn’t bother me. I swear."
    c "And I’ll try to be more conscious of it in the future."
    c "I’m sure there were a few things I said on our vacation that were easy to misinterpret, and I’m sorry for all of them."
    c "But again, just because I can’t accept your confession doesn’t mean I don’t still want to see you all the time."
    c "So please, for the love of God, stop ignoring me."

    scene ringlow25
    with dissolve

    c "Life goes on. I know that better than most."
    c "We’ll figure this out together. Got it?"
    r "...Mhm."
    r "Can you...maybe not touch me, though?"
    r "Like, I’m all for it, but yeah..."

    scene ringlow26
    with dissolve

    c "Oh, shoot! I wasn’t even thinking! I’m so sorry!"

    scene ringlow27
    with dissolve

    r "Heheh...hahahaha! It’s fine...it’s fine."
    r "Of course you’d react that way..."

    scene ringlow28
    with dissolve

    r "Thank you for properly rejecting me."
    r "I’m sorry for running off and not giving you the chance to in the first place."
    r "It may have been your first confession, but it was my first time confessing {i}to{/i} anyone. Soooo...that was pretty nerve-wracking."
    r "But...I’ll try my best to move on for both of our sakes..."
    r "Just don’t hate me if I can’t get over you, okay? It’s been...kind of a long time, so it’s sort of ingrained into me now."
    c "Of course...take all the time you need."
    c "I might not be the best person to actually talk to {i}about{/i} that with, but you’ve got Futaba and Sensei to air out your worries to whenever you want."
    r "I do...They’ve been a big help these last few days."
    c "They’re good people. And so are you."
    c "Just try not to let this get you down. You mean a lot to me."
    r "You mean a lot to me too."
    r "And not just because I’m in love with you."

    scene ringlow29
    with dissolve

    c "I know that, idiot..."
    c "I’ll get out of your hair now. I just...wanted to say that everything is going to be okay. That’s all."
    r "I see..."
    r "Thank you, Chika."
    r "I was nervous when you came in, but...this really did help."
    c "Then my job here is done."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    c "Have a good night, Rin!"
    c "Feel free to come knock on my door if you need anything."
    r "Mhm..."
    r "Goodnight, Chika..."

    stop music fadeout 5.0

    "{i}Life moves on!{/i}"
    "{i}Live every day as if it’s your last!{/i}"
    "{i}And if you can not find the will to live, steal it from someone who can!{/i}"
    "{i}Rin’s affection with Chika has increased to 1!{/i}"
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ rindorm35 = True

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabadorm30:
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
    if rin_love >= 30 and day != 2 and cafe30 == True and rindorm30 == False:
        jump rindorm30
    if rin_love >= 35 and rindorm30 == True and rindorm35 == False:
        jump rindorm35
...
```