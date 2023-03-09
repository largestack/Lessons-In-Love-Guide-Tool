# Something, Somewhere
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotowinterbeach4&go=Go)


Part of event chain [To Sleep, Perchance to Dream](./mikuwinterbeach1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Miku: Triple Whammy](./mikudorm35.md)
* [Main: The WAP Man](./day295.md)
* [Yasu: Repentance](./yasudorm10.md)

## Event properties
* ID: makotowinterbeach4
* Group: Makoto
* Triggered by label: mikuwinterbeach1

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotowinterbeach4:
    scene wintersky
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Morning comes before any of us want it to. "
    "But I suppose that’s just how vacations always end."
    "Even if those vacations happen to last no longer than a day. "
    "We pack our things and head for the bus stop."
    "It arrives roughly seven minutes later."
    "Makoto sits next to me once we board. "
    "Miku sits in the row across from us despite how our current bench could easily fit three people."
    "She doesn’t say much all morning."

    if bonus == True:
        "Neither does Makoto, but Makoto’s silence seems to be on account of being tired and not impulsively dry humping her teacher to climax last night."

    "The bus drives slightly over the speed limit, making the clouds work mildly harder to keep up with us."
    "On the way home, I notice the mangled corpse of a tanuki decaying along the side of the road."
    "No one else notices it. "
    "And if they do, they elect to remain silent instead of pointing out the beautiful yet grotesque concept of life spawning from death."
    "I focus on the yellowish mound of wriggling larvae on top of the corpse, trying desperately to live and not become the breakfast of a touring bird."
    "As the bus moves further away, I spot a buzzard."
    "I accept that death comes for everyone and everything."

    scene black
    with dissolve

    if bonus == True:
        "And then I close my eyes to the sensation of a glove-covered hand landing on one of my thighs."
        "Not sexually, but to provide comfort."
        "Or to attempt to provide comfort."
        "Or to attempt to be sexual but provide comfort instead."
        "Essentially, there is a hand on my thigh."
        "I don’t know what it means."
        "I don’t know what anything means."
    else:
        "........."
        "......"
        "..."

    scene makotocomeshome1
    with dissolve2

    "Miku winds up getting off the bus several stops before Makoto and I."
    "I expected Makoto to get off as well, but it appears that one night alone was not enough to clear her mind of the things she’d locked away in it."
    "She requires, at the very least, one more morning in order to do that."
    "And with Ami at work and not able to run interference between the two of us, it makes complete sense to invite her over and see what happens next."
    "I doubt it will be anything exciting."

    if bonus == True:
        "And, on the off chance it is, I don’t even have any condoms."

    "Today is already off to a bad start."
    "But I suppose it’s time to see how much worse it is going to get."

    mak "I obviously can’t speak for you, but {i}I{/i} had a good time yesterday."
    mak "And you managed to make it through the entire night without [molesting] me, so I’d be lying if I said I wasn’t a little impressed."

    if bonus == True:
        s "{s}I made your best friend cum.{/s} Yeah, I’m impressed with myself as well."
        s "Do I get a reward?"
    else:
        s "Does this mean I get an ice pop?"

    scene makotocomeshome2
    with dissolve

    mak "Do you want one?"
    s "Obviously. When do I ever {i}not{/i} want one?"
    mak "Then...how about I tell you a secret?"
    s "…"
    s "Why do I feel like this secret isn’t going to be the type of reward I’m looking for?"

    scene makotocomeshome3
    with dissolve

    mak "Because despite our obvious progress, I still feel a shadow lurking somewhere in the background."
    mak "And I’m afraid that as soon as I go back to my dorm, the shadow will fuse with you and turn you back into the same guy who gets off on picking on me."
    s "It’s my shadow. It’s already fused with me."
    mak "I suppose that’s true. But sometimes, when the light is angled just perfectly, it moves really far away. "
    mak "And, forgive my inadequacy when it comes to poetry, but I would very much like to be that light this morning."
    s "…"
    s "Is everything okay? You’re acting a little...unusual right now."
    mak "Is that genuine concern or do you just feel obligated to say that?"
    s "A little of both."
    mak "I see."
    mak "Everything is okay."
    s "Good. Because-"
    mak" But only because I force everything to be okay."
    s "Oh."
    s "Is this where the secret comes into play?"
    mak "This is where the secret comes into play."

    scene makotocomeshome4
    with dissolve

    "Makoto takes a deep breath and closes her eyes for a moment."
    "If this were a normal morning, she’d be breathing in the scent of french toast or an omelette made with an ungodly amount of meat in it."
    "But, as I walked out on the girl who would normally make those things in favor of spending time with Makoto yesterday, there is no scent at all."
    "She breathes in plain air."
    "It fills her lungs and I watch as her chest expands and contracts."
    "She remains silent for a moment before confessing something to me."

    mak "I’ve been having some pretty strange dreams lately, Sensei."
    mak "They come out of nowhere. Sometimes, when I’m not even sleeping."
    "I've heard this before."
    mak "I very rarely make it out of those dreams."
    mak "They’re always the kind that end with you on the brink of death. When the moment death comes is the moment that wakes you."

    scene makotocomeshome5
    with dissolve

    mak "You know the kind of dreams I’m talking about, right?"
    s "Of course. That phenomenon of waking up just as you’re about to die in a dream isn’t exactly uncommon."
    mak "I know. It’s a direct result of the combination of REM sleep with the flood of adrenaline that comes from being inserted into a stressful or terrifying situation."
    mak "But a more interesting phenomenon is when every single journey through REM sleep yields the same exact dream."
    mak "It turns something so obviously fake into something that feels just as real as waking up and starting your morning routine."
    mak "For me, that routine is brewing a pot of coffee, taking a shower, straightening out my uniform, and then texting my mother to say good morning."
    mak "But lately, that routine has started to become weighed down by the excruciatingly dark undertones of myself and a blanket of stars not at all dissimilar from what we saw on the beach last night."
    s "Well, yes. The night sky is dark by nature. I wouldn’t exactly say that’s a dark undertone, though."
    mak "By itself, no. But when you start having the same dream over and over and over again, you start having time to analyze different aspects of it."
    mak "The dream is not just of the sky itself but of me as I swim through it."
    mak "The only issue is, you can’t swim through the sky. And so logic dictates that I would have to be falling."
    s "Or flying, since it’s a dream and logic doesn’t influence dreams."
    mak "To say it doesn’t influence them is a bit of a reach, don’t you think?"
    mak "Pretty much everything we see is tied to logic in one way or another. Things very rarely happen without reason."
    mak "And so, as someone who spends far too much time bathing in this aspect of human thought, it’s easy for me to understand what’s happening in those dreams of mine."
    s "Which is?"

    scene makotocomeshome6
    with dissolve

    mak "I’m jumping, idiot."
    mak "I’m having recurring dreams about jumping off of something, somewhere. "
    mak "And I believe that the reason for this is that there has been something dark growing inside of me for a very long time."
    mak "My own shadow, I suppose."
    mak "Just mine compels me to think about things like jumping out of a moving car on the highway or taking a few extra painkillers just to see what would happen."
    s "That...definitely sounds a little worse than what my apparent shadow makes me do."
    mak "Worse, sure. But I’m stronger than you and would never let something like that overtake me the same way you let {i}yours{/i} overtake {i}you{/i}."
    mak "No matter how many times I have that dream, I’ll never try to reenact it."
    mak "I’m smart. I have a bright future ahead of me. I have a wonderful best friend. And I like to think I’m at least decently attractive."
    s "You’re very attractive, Makoto."

    scene makotocomeshome7
    with dissolve

    if bonus == True:
        mak "You’re only saying that because it’s directly linked to the possibility of us having more sex in the future."
    else:
        mak "You’re only saying that because you want another ice pop."

    s "Well, yeah. But also because it’s true."
    s "But why spend time thinking about all of those things when, comparatively, your situation isn’t all that bad?"

    scene makotocomeshome8
    with dissolve

    mak "I’ve explained something like that to you in the past, haven’t I?"
    mak "What was my reasoning back then?"
    s "I think it was something like “That's just the way it is.”"
    mak "Then that’s my reasoning this time, too."
    mak "Not everyone has complete control over their emotions the way you do, Sensei."
    mak "There are some people out there who would laugh in the face of all that I go through if it happened to them."
    mak "But the amount of effort I put into hiding that part of me really only makes me more tired at the end of the day."
    mak "Mix that with an onslaught of dreams that feel more like memories of horrible things and you have one unhappy Makoto."
    mak "And, it might not always work, but the best medicine for an unhappy Makoto is someone who can constantly remind her that her troubles are nothing but troubles."
    mak "And most troubles go away with time."
    mak "Dreams, too."

    scene makotocomeshome9
    with dissolve

    mak "I don’t want to die, Sensei."
    mak "And it’s not that I don’t want to die. I don’t want to think about dying. And, at this point, it’s become almost an inevitability."
    mak "I’ll never give into something just because of an inevitability, though. So I guess that's one area where I could be considered an idiot."
    mak "But the fact that part of me is there at all is just..."
    s "Scary."
    mak "Not even that."
    mak "It’s just...exhausting."
    mak "I’m so tired."
    s "Well then wake up, loser."

    scene makotocomeshome10
    with dissolve

    mak "Oh, would you look at that. I’m perfectly fine, now."
    mak "Thank you so much for listening to me, Sensei."
    s "Any time, Makoto."
    s "You know that a big part of why I say things like this to you is because I think you can handle it, right?"
    mak "Obviously, but even I have limits."
    mak "And so I figured coming out and trying to properly explain more about the things I’m feeling to you would help."
    mak "The issue with that is that even though I can try to explain those things, I feel like I can’t even come close to properly doing them justice."
    mak "All of those dreams and all of those things that I see, even though I {i}know{/i} they’re dreams, still feel like more."

    scene makotocomeshome11
    with dissolve

    mak "I know I’ve already compared them to memories, but...even that word doesn’t really apply."
    mak "But I’m sure that this combined with everything else I’ve forced onto you over the last 24 hours doesn’t exactly allude to my expected stability, does it?"
    s "Oh, I’ve already given up on expecting stability from you."

    scene makotocomeshome12
    with dissolve

    mak "Is that an insult?"
    s "More of an evaluation."
    s "You have depression, right?"
    mak "Probably. Over 10%% of all people are expected to have some sort of mental disorder. It would make sense if that was the reason behind all of this."
    s "That number definitely seems higher than 10%% based on all of the people I find myself associating with on a daily basis."

    scene makotocomeshome13
    with dissolve

    mak "We really don’t have the most...stable class, do we?"
    s "Not even close."
    s "But what I’m saying is that you don’t really need to worry about how you look to me or anyone else."
    s "Like, if you ever want to show up to[school] some time and skip out on doing my work for me, just tell me."
    mak "And if I ask to just...{i}always{/i} skip out on your work?"
    s "Well that would just be irresponsible if you want me to keep teaching."
    mak "Right...that would be completely irresponsible of {i}me...{/i}"
    s "There you go. Now you’re starting to get it."
    mak "What I’m confused about, though, is that if you don’t expect stability from me...what do you expect?"
    mak "Because all this time I’ve been citing myself as the cool, calm, collected one."
    s "I expect literally nothing from you."
    mak "Well that's just plain rude."

    if bonus == True:
        s "You’re a fucking [teenager], Makoto. Stop being an adult and just chill for once."

    s "Do you want to sit behind my desk from now on? Will that make you feel better?"

    scene makotocomeshome14
    with dissolve

    mak "Can I?!"
    s "…"
    s "Does that...really make you that excited?"
    mak "Forgive the pun but, depressingly so!"

    scene makotocomeshome15
    with dissolve

    mak "And...since we’re already on the topic of things that would make me feel better..."
    mak "Could I ask you to...maybe be a little more honest with me from now on?"
    s "Honest about what, exactly?"
    mak "Honest about the things that I already know you’re doing but you’ve yet to come out and admit to."

    if bonus == True:
        s "Oh...{i}those{/i} things."
        mak "Sensei...I don’t need to know {i}who{/i} else you have a more...{i}adult{/i} relationship with, but I’d at least gain some solace in knowing that you trust me enough to not blurt it out to anyone else."
        s "And here I was thinking I was doing you a service by {i}not{/i} telling you things I expect will upset you."
        mak "I never promised to not get upset. I just said that it would provide some solace."
        mak "And wallowing in sadness is exponentially easier than wallowing in uncertainty."
        s "Uncertainty? But I thought you “already knew?”"
    else:
        s "..."
        mak "..."
        s "..."
        mak "..."
        s "Okay, fine. {i}I{/i} am the one who has been hiding the various soups."
        mak "Why would you do this?"
        s "I just had so many of them. It got out of control."

    scene makotocomeshome16
    with dissolve

    mak "Nothing is truly certain unless you see it with your own eyes or hear it with your own ears."

    if bonus == False:
        s "Does soup make a sound?"

    mak "And even then, there’s the possibility of what you see or hear being an object of delusion."
    mak "So nothing is ever certain as a whole."
    mak "But there are some things that are a lot easier to accept once they’re out in the open."
    mak "So...I won’t say something like “I’ll be happy with just knowing” because that would make me a liar."
    mak "But I’d probably be able to fall asleep a little better."
    mak "And that would be a...good start."
    s "…"
    mak "…"

    if bonus == True:
        "Oh, fuck it."
        "Makoto’s been racking up losses left and right. "
        "It won’t kill me to hand her a single victory when I can’t imagine she’d be one to let anyone know about it."
        "After all, who would she even tell?"

        s "Your...suspicions are correct."
        s "There are others."
    else:
        s "I already told you I did it. What else you do want to know?"

    scene makotocomeshome17
    with dissolve

    mak "Can I...ask you how many or would that be pushing it?"
    s "That would be pushing it."
    s "Accept your victory and move on with whatever solace that was able to provide."
    mak "It feels out of place to say it in this context...but thank you."
    mak "Thank you for trusting me and thank you for not viewing me as a wicked witch."
    mak "And again, thank you for not [molesting] me in the middle of the night."
    mak "I realize that was probably the hardest for you out of all of those things."
    s "Is there any chance for a...second reward?"
    mak "…"
    s "…"
    mak "Right now? Seriously?"

    if bonus == True:
        mak "No. Get out of here, you pervert."
        s "But...this is my house."
        mak "Fine. {i}I’ll{/i} get out, then."
    else:
        s "Ice pop! Ice pop! Ice pop!"
        mak "...Fine."

    scene black
    with dissolve2

    if bonus == True:
        s "Wait. I was only kidding. You don’t have to-"
        mak "I do. I skipped my entire morning ritual anyway, so I have to catch up on all of that."
        mak "I’m really happy we got to spend so much time together this weekend, though."
        mak "Because even if...I know there are other girls now-"
        mak "At least there weren’t for one night."

        play sound "dooropen.mp3"

        "…"
        "Except there were."

    $ renpy.end_replay()
    $ makoto_love += 5
    $ makotowinterbeach4 = True
    $ makotobeachticket = False
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label makotonew1:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
mi "Mnh...mnh...mm..."
    s "Does that feel good?"
    mi "Mngh...mm...mhm...ye...yeah..."
    s "Are you going to cum?"
    mi "Hah...hah...I..."
    mi "I don’t know..."
    mi "I...I never..."
    mi "I...wouldn’t...ngh...know..."

    "I take a second to properly angle myself and begin to prod at her hole through my pants."
    "She likes this a lot."
    "Her squeaks get louder. Almost to the point where they’re difficult to conceal."
    "But she won’t last much longer at this rate."
    "In fact, any minute, she’ll-"

    scene mikusleeping13
    with dissolve

    mi "Sensei...I..."
    mi "It feels...really good..."
    mi "I...don’t think I...can stay quiet..."
    s "You have to."
    s "Unless you want your best friend to watch you cum."
    mi "I...don’t even know if I-"

    scene mikusleeping14
    with dissolve

    "Miku spreads her legs a little further apart and I begin to roughly grind up against her."
    "I move as hard as I can without shaking the bed."
    "She’s overcome with so many feelings by this point that it doesn’t take her long to have what I believe is likely her first orgasm ever."

    scene mikusleeping15
    with dissolve

    mi "Mngh...mmm...mnn..."
    mi "Sensei...I’m...so sorry...but I..."
    mi "I..."

    with sexfade
    with sexfade
    scene mikusleeping14
    with cumflash
    with hpunch

    mi "{i}MNGHHH!!!!{/i}"

    "Miku covers her mouth with full force as she convulses and vibrates against my cock."
    "Of course, I never had the opportunity to finish as well but, to be honest, I don’t really mind considering this is the only pair of sweatpants I brought."
    "Now...if she were willing to finish me off some other way..."

    scene mikusleeping16
    with dissolve

    mi "Oh no...that..."
    mi "We...I..."
    s "...?"
    mi "Please...please please please..."
    mi "Don’t tell Makoto..."
    s "Of course I'm not going to tell Makoto."
    s "Though, there’s still the matter of me-"
    mi "I..."
    mi "I can’t..."
    mi "I’m sorry for waking you up, but..."
    mi "I..."
    mi "I think I’m gonna go sleep in the other room..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "Miku grabs the same bag we emptied out for pills earlier and brings it with her to the living room, closing the door gently behind her."
    "I turn to face Makoto and find that she’s still sound asleep- a character trait that I will be happy to take advantage of again in the future."
    "If there is a future, of course."
    "I mean, Miku just managed to climax from dry humping me, so the idea of things just ending here would be rather depressing."
    "I keep my eyes closed, hoping for another miraculous dream-induced boning session but with the class rep this time."
    "Unfortunately, I doubt she’d let me put it in either on account of me wasting my only three condoms on an analogy before ever making it to this room."
    "I guess I just...lose this time."
    "There’s nothing else to it."
    "But at least I have some new memories for the mental spank bank that I can take advantage of tomorrow."
    "For now, though-"
    "I should probably get some rest..."

    $ renpy.end_replay()
    $ mikuwinterbeach1 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    jump makotowinterbeach4
...
```