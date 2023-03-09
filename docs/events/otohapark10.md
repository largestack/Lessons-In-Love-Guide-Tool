# Pull the Plug
Otoha event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohapark10&go=Go)



## Event preconditions
✅Otoha love greater than or equal to 10

❌Event "[Main: Glued to the Sky](./christmastwo20.md)" is completed (event=christmastwo20)



## Next events
None

## Event properties
* ID: otohapark10
* Group: Otoha
* Triggered by label: otohapark
* Triggered by branch label: saturdaymorning

## Event code
File: \game\OtohaEvents.rpy
Code:
```python
...
label otohapark10:
    scene otohaparkten1
    with fade
    play music "samhain.mp3"

    "I head over to the park first thing in the morning, unsure of whether or not Otoha will be bogged down enough by the Rin situation to show up."
    "And, in the event that you just haven’t been paying attention to what’s in front of you for whatever reason, she has."
    "Or...does?"
    "Did?"
    "She’s here."
    "Albeit a bit more melancholic than I'm used to- but I guess that can be attributed to the early morning winter sun, still fighting its way through a layer of clouds much thicker than normal."

    o "..."

    "She doesn’t say anything. In fact, she probably hasn’t even noticed I’m here yet."
    "Granted, she’s one of the last people to ever notice my presence to begin with- but maybe this new version of her, temporary as it may be, will give me the chance to get closer."
    "I’m sure it sounds cynical, but that’s the great thing about fracturing relationships."
    "The more cracks, the more opportunities you have to fill them."
    "Here’s hoping I’ve learned enough from “fixing” others that I can start repairing this creature as well."

    s "Morning."

    scene otohaparkten2
    with dissolve

    o "Oh. Hey."
    o "How long have you been creepily standing there watching me for?"
    s "A couple minutes. No longer than the typical amount of time I use to stare at you intermittently throughout the school day."
    o "You live an extremely exciting life, don’t you?"
    s "I can sense sarcasm in that response, but I’ll have you know that my life is actually {i}very{/i} exciting. "
    s "I am a time traveler. Kind of."

    scene otohaparkten3
    with dissolve

    o "And I’m Christina Aguilera. Kind of."
    s "I have no idea who that is."
    o "I am not at all surprised by that."
    o "Anyway, are you here to see me? Or are you just passing by on the way to meet up with somebody else?"
    s "You mean somebody like {i}Rin?{/i}"

    scene otohaparkten4
    with dissolve

    o "Uhh...I guess? I was talking more or less about pretty much everyone."
    s "It sounds to me like you want to talk about Rin."
    o "How does it even remotely sound like that?"

    "I’ve gotta say, I think I’m doing a pretty good job of getting Otoha to open up so far."

    scene otohaparkten5
    with dissolve

    o "I guess you’re not wrong, though."

    "Oh. "
    "I was just joking when I said that last thing, but it looks like my backwards method actually worked for some strange reason."
    "Cool."

    o "Figured it was only a matter of time until {i}somebody{/i} tried talking to me about it after what went down at the Christmas party."
    s "There’s no way I’m the first one."
    o "First one other than Rin. Not even Nodoka or Futaba have asked about it."
    o "To be fair, though, Nodoka’s in the middle of another manic episode right now, so she’s not really in the condition to be asking {i}anything{/i} other than...I don’t know. Weird shit."
    s "Well, I’m here if you want to vent."

    scene otohaparkten6
    with dissolve

    o "The hell will venting even do, though? You pretty much already know everything that happened."
    o "Recapping it again is just going to make me feel like shit."
    s "Some people just like talking about what it is that bothers them."
    o "And you think I’m one of those people?"
    s "You were certainly one of those people at the beach. I distinctly remember that occasion on account of the giant banana."

    scene otohaparkten7
    with dissolve

    o "Oh yeah. I wonder how that banana is doing."
    s "Listen, I’m obviously not going to force you to talk to me if you don’t want to. I just get how frustrating it might be to feel like everyone’s against you without looking at the big picture."

    scene otohaparkten8
    with dissolve

    s "Everyone already knows that your parents suck. "
    s "And if I were in your shoes and everyone just conveniently decided to forget that detail when I needed them to remember it most, I’d be pretty pissed."
    o "Do I even have the right to get pissed right now, though?"
    s "Why wouldn’t you? Getting angry is one of the few things we’re allowed to do whenever we want."
    o "Not without consequences, though. And Rin’s already so heated that even a slight raise in {i}my{/i} blood pressure would cause the...thin ice we’re on to melt."
    s "Well, maybe you two aren’t meant to be together then?"

    scene otohaparkten9
    with dissolve

    o "Wow. This suddenly sounds a lot less like me venting and a lot {i}more{/i} like you being a fucking dick."
    o "Why would you say that?"
    s "Probably because I didn’t expect you to react like that."
    o "Of course I’m going to react like that. Even if we’re fighting or whatever right now, Rin’s still my girlfriend. "
    o "Just because things aren’t going perfect doesn’t mean I’m going to pull the plug. "
    s "Then what’s the plan? Because I’m pretty sure we both know she doesn’t want to be kept a secret forever."

    scene otohaparkten10
    with dissolve

    o "Yeah. She’s made that {i}very{/i} clear."
    o "I don’t know, man. I don’t really have a plan. I’m too busy trying to figure out how to make her stop being mad at me to plan out what I’m going to do when it comes to my parents."
    s "Can’t say sulking in a park is how I’d make my significant other stop being mad at me, but if that’s how you want to do things, be my guest."
    o "Well, what would you do then? Since you’re so smart, I mean. How would {i}you{/i} make {i}your{/i} significant other stop being pissed off at you?"
    s "Maybe...buy her flowers or something?"
    o "Uh-huh. But what would you {i}actually{/i} do? Because I refuse to believe you would ever buy anyone flowers."

    if bonus == True:
        s "My real answer is significantly more sexual and I don’t think you and Rin are at that level yet."
    else:
        s "My real answer involves investing in a series of food trucks, but I don’t think you and Rin are at that level yet."

    scene otohaparkten11
    with dissolve

    o "Even if we were, that is absolutely not something I would tell you about."
    s "That’s fine because I imagine Rin would call me and tell me all about it immediately after."

    if bonus == True:
        o "You know, that’s probably true and it feels extremely wrong to me."
    else:
        o "She {i}does{/i} love food trucks."

    s "That’s just the kind of relationship she and I have, I guess."

    scene otohaparkten12
    with dissolve

    o "Then help me, dude. It’s weird saying this, but you probably know her a lot better than I do. How can I fix this?"
    s "You-"

    if bonus == True:
        o "How can I fix this {i}without{/i} using any of your weird, sexual methods?"
    else:
        o "How can I fix this {i}without{/i} using any of your weird food trucks?"

    s "They aren’t weird. They are completely natural."
    s "But if you really want to know, the only thing I can imagine working is backpedaling on what you said at the party and actually introducing her to your parents."
    s "She said she’d be fine being introduced as a friend, didn’t she? Why not just do that?"

    scene otohaparkten13
    with dissolve

    o "Oh, come on. Do you honestly believe {i}Rin...Rin Rokuhara...{/i}would be able to convincingly act like she is not absolutely obsessed with me for even a fraction of a second?"
    s "That is a very good point."
    o "Yeah. I’m caught between like...six rocks and a lesbian right now. Which is why I’m going into like, stasis mode at this park. Because I can’t figure out what to do."
    o "Shit, dude. I haven’t even taken my guitar out of the case yet. "
    o "Barely anyone ever comes here anyway, so it’s not like it’s a really big deal, but still."
    s "Just climb over one of those rocks and go visit her at work or something. It might not make her immediately forgive you, but it will be a start."

    scene otohaparkten10
    with dissolve

    o "It’s a little too late for that now. I’ve got lessons today and don’t really have time to stop at the cafe."
    s "Then I guess your relationship is over and Rin is doomed to hate you forever."
    o "Welp. It was fun while it lasted. Back to dating my guitar, I guess."
    s "Unfortunate. Rin is much cuter than your guitar."

    scene otohaparkten14
    with dissolve

    o "She is. But at least I can bring the guitar home without my parents thinking I’m like, mentally challenged or something."
    s "Are they really that bad? "
    o "I mean...kinda? They’re not {i}bad,{/i} they’re just really fucking old fashioned and want me to be some, like...normal housewife or something when I get older."
    o "Which, of course, is {i}literally impossible{/i} if you’re dating a girl. You know, since there are {i}absolutely no{/i} successful same-sex couples out there."
    s "Here’s a genius idea. I’ll pretend to be your boyfriend as a cover. Then, you can bring Rin home and-"
    o "No."
    s "Wait, you need to let me finish."
    o "Fine. Go."
    s "Then, you can-"
    o "No."
    s "Your loss. It was a great idea, too."

    scene otohaparkten15
    with dissolve

    o "I don’t think there has ever been a great idea that starts with a teacher dating a student."
    s "Tell that to roughly half of your classmates and I’m sure you’ll quickly find that you have an outdated outlook on this topic."
    o "Or...that our class is just fucking weird."
    s "That is also a fair assessment. "

    scene otohaparkten16
    with dissolve

    o "Man, I have no idea how this even turned into as much of a thing as it has."
    o "I figured Rin would kind of understand that this might be an issue for us, but I guess that shit just...doesn’t even occur to you when you grow up with two moms. "
    s "Oh. And why haven’t you met {i}them{/i} exactly? Didn’t Rin say they wanted to meet you?"

    scene otohaparkten17
    with dissolve

    o "Yeah, but..."
    o "I don’t know. I kind of want to. But, at the same time, that makes everything seem so much more...serious? Is that the right word?"
    s "Do you not think things are serious with you two?"
    o "I {i}do{/i}. But it’s like...a different kind of serious."
    o "Like...I want to just enjoy liking each other and...being free and stuff right now. "
    o "If I met Rin’s parents and they liked me, some of that freedom would kind of vanish. "
    o "Because if we {i}do{/i} break up- and this isn’t me saying I want to, but if we {i}do{/i}, knowing them will make things like ten times harder."
    s "So...you think the expectations of her parents would be some kind of intangible jail cell for you?"
    o "That’s not really how I would word it, but...I guess?"

    if bonus == True:
        o "I want things to just be Rin and me and...our friends. I don’t want any adults involved."
        s "But I’m an adult."
    else:
        o "I want things to just be Rin and me and...our friends. I don’t want any food trucks involved."
        s "But I love food trucks."

    scene otohaparkten2
    with dissolve

    o "Yeah. Your point?"
    s "You’re always so mean to me."

    scene otohaparkten15
    with dissolve

    o "It’s all in good fun. I like you more than I let on."
    o "Besides, you barely count as an adult anyway since it seems like you just kind of stopped mentally maturing somewhere along the line."

    if bonus == True:
        s "Yes, because the girl who’s afraid of her parents finding out she wants to bone a girl knows all there is to know about mental maturity."
    else:
        s "Yes, because the girl who’s afraid of her parents finding out she wants to hug a girl knows all there is to know about mental maturity."

    scene otohaparkten18
    with dissolve

    if bonus == True:
        o "I don’t want to “bone” anybody! What bone would I even bone with?!"
    else:
        o "I'll catch on fire if I hug anyone! Stop forgetting that extremely important detail about my character!"

    scene otohaparkten10
    with dissolve

    s "All things considered, I mostly understand how you feel."
    s "I don’t think it’s wrong to want to create a world where things won’t get any more complicated than your relationship with one person- but that sort of thing isn’t realistic."
    s "And I think that you know, even if you won’t admit it, that there would just be a different problem soon enough if this thing with your parents never happened."
    o "I don’t know that. How could someone ever know that?"
    o "The only thing I {i}know{/i} is that they’re the problem right now. And that if it weren’t for them, Rin and I would still be just as happy as we were before the Christmas party."
    o "I want that back."
    o "I don’t like where we are now."
    s "Then go somewhere else. Do something about it. "
    s "How much of what you’ve told me today have you told her?"
    o "To be totally honest...not a lot."
    o "But she’s hard to talk to about stuff like this. I don’t want her to internalize it and think it’s all on her when, in all actuality, it’s my...indecisiveness that’s creating these problems."
    s "{i}Tell her that.{/i}"
    o "Yeah, because the whole, “It’s me, not you” thing always goes over so well in movies."
    s "This isn’t a movie, Otoha."
    o "Good, because this movie would fucking suck."

    scene black
    with dissolve2

    "Otoha doesn’t say anything that I didn’t already expect to hear when I approached her today."
    "And while there was minimal refilling of cracks or fixing of anything, I did manage to learn that at least she doesn’t dislike me as much as she lets on."
    "But of course that’s what I’d jump to since it’s the only detail pertaining to me I was able to siphon out of the entire conversation."
    "I’m not involved in this. It’s not my {i}place{/i} to be involved in this."
    "I’m simply observing what could be either the earliest stages of a potential fallout...or the first of many hurdles in a long and successful relationship."
    "Unfortunately, this world doesn’t have enough long and successful relationships."
    "In fact, I can’t put my finger on a single one- but that’s mostly due to the fact that my fingers belong closer to short term options than ones that will grow old beside me."
    "In that sense, I wish Otoha the best in her pursuit of eternal youth or eternal freedom or whatever it is that she wants to last forever."
    "My wishes fall on deaf ears, but that’s okay-"
    "Because those things might be closer than she’s willing to believe."
    "Those wishes might come true."

    scene otohaparkten19
    with dissolve2

    o "Okay, well...I need to start heading out. But thanks for dropping by and letting me vent."
    o "Didn’t really sound fun at first, but I guess it did kind of help."
    o "I’m gonna text Rin and see if she’s able to talk about this tonight. I probably should be filling her in on some of the stuff I said to you if I really do want this relationship to work out."
    s "I’m glad I was able to help in...whatever way I was able to help."

    scene otohaparkten20
    with dissolve

    o "Cool. So, uhh..."
    o "See you later, then."
    s "..."
    o "..."
    o "You’re not going to ask me for like...a goodbye hug or something, are you?"

    if bonus == True:
        s "I am not."
    else:
        s "I wouldn't {i}refuse{/i} one. But that's not why I'm not leaving."

    o "..."
    o "Then...why are you not leaving?"
    s "Because I’m going to come with you to your lesson."
    o "No. You’re not."
    s "Why not?"
    o "Because I don’t want you to be there."
    s "{i}You{/i} might not want me to be there, but I’m not so sure your vocal coach feels the same way."

    scene otohaparkten21
    with dissolve

    o "Why do you even want to come? It’s going to be totally boring and that basement is cold as shit."
    s "I don’t have anything else to do today. And also, Niki confessed to still being in love with me and I thought it might be nice to drop by unannounced and make her blush."
    s "Besides, it’ll also give you an opportunity to see how a real couple deals with their issues."

    scene otohaparkten22
    with dissolve

    o "Wait, are you two actually back together?"
    s "No. But we act like we are sometimes, and I think that should be good enough."

    scene otohaparkten23
    with dissolve

    o "Ugh...whatever. I know there’s no stopping you once you decide to actually do something, and I’m already running late."
    o "I’m warning you now, though- it really is going to be boring. And if you do anything to mess up the lesson, I’m never talking to you again."
    o "I need this, dude. It’s an amazing opportunity. Please don’t mess it up for me."
    s "Otoha, why would I ever mess {i}anything{/i} up for you?"
    o "That emphasis on {i}anything{/i} is really starting to make me worry, Sensei."

    scene black
    with dissolve2

    s "Don’t worry at all, Otoha."
    s "If there is anything I am good at, it is spending time with Niki without causing her to get flustered or angry at anyone."
    o "I swear to God..."

    $ renpy.end_replay()
    $ otohapark10 = True
    $ otoha_love += 1
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohaspecial10

label otohaspecial10:
...
```

## Code that triggers this event
File: \game\OtohaEvents.rpy
Code:
```python
...
label otohapark:
    if otoha_love >= 0 and otohadorm1 == True and saradate10 == True and otohapark1 == False:
        jump otohapark1
    if otoha_love >= 0 and otohapark1 == True and otohapark5 == False:
        jump otohapark5
    if otoha_love >= 10 and christmastwo20 == True and otohapark10 == False:
        jump otohapark10
...
```