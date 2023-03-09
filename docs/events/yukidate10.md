# Opposite Directions
Yuki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yukidate10&go=Go)



## Event preconditions
✅Yuki love greater than or equal to 10

✅Event "[Yuki: Better Off Alone](./yukidate5.md)" is completed (event=yukidate5)

✅Event "[Kirin: Temporary Bliss](./kirindorm25.md)" is completed (event=kirindorm25)

✅yukinumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: yukidate10
* Group: Yuki
* Triggered by label: callyukinight
* Triggered by branch label: callnight

## Event code
File: \game\YukiEvents.rpy
Code:
```python
...
label yukidate10:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I haven’t really spent any time with her since the Halloween party, and even then, I don’t know if what I did would really count as {i}spending time with her{/i} to begin with."
    "I just kind of showed up, revealed her long-lost and no longer comatose niece to her, and then went on my way."
    "But I guess that’s just how things go sometimes."
    "But hey, if anyone I know is able to roll with the punches, it’s probably Yuki. "
    "For all I know, she’s completely come to terms with that aspect of her life being flipped on its head- given that she spent years personally flipping everything else over on her own."

    play sound "phonebeep.wav"
    play music "recovery.mp3" fadein 3.0
    scene black
    with dissolve

    yu "Yo. Sorry, but I can’t really talk right now."
    s "What? Why?"
    yu "Uhh...because I have a job now?"
    yu "Can’t just fuckin’ eat noodles with you whenever you want anymore. Gotta pay bills and shit."
    s "What kind of bills do you even have?"
    yu "The fuck is that supposed to mean? Same kinda bills everyone else has to pay. Water...gas-"
    yu "I don’t know man, whatever comes in the mail. I can’t be bothered to keep track of all that shit."
    s "And here I was thinking you were still living on the streets. No offense."
    yu "How am I not supposed be offended by- wait, Kaori! I already went that way!"
    s "You’re with Kaori?"
    yu "Hm? Yeah. "
    yu "Sara was tired of bein’ cold and shit so she sent the two of us out here to pass out fliers. "
    s "And where is {i}here{/i} exactly?"
    yu "Urban district. Why? You gonna come help? "
    s "No. But I wouldn’t mind standing around and talking to you while you work."
    yu "Yeah, I’m sure that- wait. That actually might be a good idea."
    yu "Boss lady seems dead set on the whole idea of me bringin’ in new customers by bein’ the closest thing all these girls can get to an actual dude now, but...well, you’re {i}actually{/i} a dude."

    if bonus == True:
        yu "Could save me the effort of turning down a bunch of desperately horny women and actually getting rid of all these papers."
        s "I don’t know, Yuki. I’m not really that great at turning down desperately horny women."
        yu "Then maybe I can show you a thing or two."
        s "Maybe {i}I{/i} can show {i}you{/i} a thing or-"
    else:
        s "That's true. But only just barely."

    play sound "phonebeep.wav"

    s "...two."

    "Yuki hangs up on me (Likely on accident) and I’m suddenly faced with the question of whether or not I want to go all the way across Kumon-mi just to see her and her no-longer estranged niece."

    s "…"

    "I sigh to myself and accept that, at this point, I’ve pretty much already decided. "
    "It’s very rare that I make it this far into a conversation only to back out and, well...I guess it’s been getting a little warmer out lately anyway."
    "A trip to the urban district might not actually be all that bad with that in mind."

    if bonus == True:
        "Besides, maybe Yuki and I can...bond over the fact that we...both have nieces or something."
        "I don’t know."
        "I just need to keep myself occupied."
        "Nothing good ever comes from wandering around aimlessly. "
        "And if I can focus on something, I’m sure I’ll-"
    else:
        "I just hope I don't get a blister because that would make me sad."

    play sound "static.mp3"
    scene beforewefall5 with flash
    scene everythingg5 with flash
    scene dust3 with flash
    scene yukiflier1 with flash
    stop sound

    "Oh. Okay."
    "I guess I’m here now."

    yu "You fuckin’ run here or something? I feel like I just hung up on you like five minutes ago."
    s "I was just really excited to see you, I guess. "

    scene yukiflier2
    with dissolve

    yu "Yeah? Lucky me."
    yu "Want a flier? I’ve only got like two hundred more to get rid of, and Sara didn’t say shit about not givin’ ‘em out to people who have already been to the bar."
    s "That’s great, because if you can give one to me and every other customer you’ve ever had, you’ll only have around 195 left."

    scene yukiflier3
    with dissolve

    yu "Shit’s actually been pickin’ up lately, believe it or not."
    yu "Granted, I don’t really know how it was before I started goin’ there, but we’ve basically always got {i}somebody{/i} inside. "

    "That’s actually pretty surprising given how horrible the name of the place is."
    "And the fact that Sara is confident enough in it to put it on a flier makes it all the more surprising that-"

    s "…"
    yu "What? Somethin’ wrong with the flier?"
    s "Apart from the name of the bar? Yeah. "
    s "Did Sara design these?"

    scene yukiflier4
    with dissolve

    yu "Nope. She gave me complete creative control or whatever."
    s "Well...I’m glad that she trusts you."

    scene yukiflier5
    with dissolve

    yu "Wait, I didn’t spell anything wrong, did I? "
    yu "I ain’t really the best when it comes to writing and shit on account of the whole no education thing."
    s "No, it’s all fine. You just normally want to be a little more...polite or...precise when it comes to marketing, I think."
    s "And saying “You have drinks and shit” doesn’t really scream “You should come to this bar.”"
    s "All bars have drinks and shit. That’s the entire purpose of a bar."

    scene yukiflier6
    with dissolve

    if bonus == True:
        yu "Well, what the fuck else do you want me to put on here? “Come to Sakaki-bar-a: We’ve got a horny barmaid and her reclusive daughter?”"
    else:
        yu "Well, what the fuck else do you want me to put on here? “Come to Sakaki-bar-a for a chance to hug a barmaid?"

    s "You joke, but that would bring me in quicker than the other sign."

    scene yukiflier7
    with dissolve

    yu "Yeah, but you’re a fucking creep and normal people probably don’t think the same way as you."
    s "You remind me more and more of your daughter every time I talk to you."

    scene yukiflier8
    with dissolve

    yu "Oh, speaking of which...were you able to give my present to Yumi?"
    s "Oh, yeah. I guess I should have probably called you about that or something."
    s "I gave it to her at the Halloween party, but I didn’t really stick around to see what she thought of it. "
    s "In fact, I don’t even think I asked what it was you gave her."

    scene yukiflier9
    with dissolve

    yu "Nothing that impressive. Just a case for her phone and some gift cards and shit."
    yu "Figure that if you’re gonna be payin’ her phone bill, least I can do is get her something to protect it from breakin’ or...getting wet or whatever."
    s "…"
    yu "If she’s anything like me, she’ll break that shit quicker than you can cook a pot of rice."
    s "I’m going to ignore the irony of this analogy and just re-confirm that I did give Yumi the present."
    s "I am sure that whatever happened after that went entirely according to plan and that her phone is both dry and protected as we speak. "

    scene yukiflier10
    with dissolve

    yu "Heh. Look at us- both payin’ for her shit. It’s almost like I’m actually her mom again."
    s "True, but that would make me her dad and I don’t think any of us would particularly enjoy that sort of change in our relationship status."

    if bonus == True:
        yu "Hey, can’t be any worse than her last dad. Unless you’re plannin’ on makin’ me suck you off in exchange for a bed or some shit."
    else:
        yu "Hey, can’t be any worse than her last dad. Unless you’re plannin’ on makin’ me hug you in exchange for a bed or some shit."

    yu "But I’m starting to think you’re not that type of guy."
    s "I will continue working hard to prove to you that I’m not that type of person."
    s "Unless you’re offering. In that case, you can sleep in my bed whenever you like."
    yu "Noted. "
    s "Not going to use this opportunity to remind me that you’re too old for me or...not interested in that sort of thing, or whatever it is you always say?"

    scene yukiflier11
    with dissolve

    yu "Nah. You’ve heard that shit enough by now. No point in repeatin’ myself anymore. "
    yu "But hey, if any of that changes, I’ll make sure you’re the first to know."
    s "…"

    if bonus == True:
        "Did Yuki just openly admit that there’s actually a prospect of the two of us sleeping together eventually?"
        "Because even if those doors stay closed forever, the fact that I’m the first in line outside of them means that, if I time everything well enough, I might be able to squeeze my way in at the first sight of an opening."
        "I’ll mark this down as a victory and file it in a completely separate cabinet from the one where I keep the prospect of fucking her daughter."
        "Then, before I attempt to carry on the conversation like a normal human being, I chuckle to myself at the idea of a cabinet full of written documents full of different girls’ sexual characteristics and traits."
        "I wonder how many more loops it will take before Maya is forced to forge something like that instead of just her weird journal of my {i}original{/i} ten students."

        s "So, about us fucking-"
    else:
        "Did Yuki just openly admit that there’s actually a prospect of the two of us hugging?"
        "I should hurry up and ask her."

        s "So, about us hugging-"

    yu "Shove it, asshole. "

    "I appear to have failed at carrying on the conversation in a believable and normal way."

    scene yukiflier12
    with dissolve

    k "Tired-looking woman of familial relation to me! I have finished passing out the rectangular remains of annihilated natural wood pillars! What would you have me do next?"
    yu "That’s all, Kaori. You don’t have to stick around anymore. I’ve got this scrub keeping me company now."

    if bonus == True:
        s "If I’m a scrub, how come I’m at the top of your sex list?"
    else:
        s "=("

    scene yukiflier13
    with dissolve

    if bonus == True:
        yu "Oh, good. I say one nice thing to you and you’re already twisting it into a secret list of people I’m deciding whether or not to bone."

    k "Friend! If I had known your body would be in the same location as mine, I would have contacted you through my communication cube!"
    s "I could have sworn I’d heard you say “cell phone” before. "
    s "You’re not...getting {i}worse{/i} at talking...are you, Kaori?"

    scene yukiflier14
    with dissolve

    k "Friend has too many {i}other{/i} friends to make regular contact with me, so I have been taking it upon myself to do the studying of human vocabulary as my own person! Without his help!"
    k "To speak is to communicate! And to square is to cube! I am learning!"
    yu "Kaori, are you sure it was okay for you to be released from the hospital?"

    scene yukiflier15
    with dissolve

    k "There are some things that juice can not cure, Yukiburger! I shan’t return to the jungle of uncomfortable beds and fluorescent brightness tubes!"
    s "Yukiburger?"
    yu "She added the burger part to my name earlier today. I have no idea why. And she gets mad any time I try to tell her to take it out."
    k "Yukiburger! Are you confident that I can depart? Are all of the trees dead?"
    yu "Yup. All dead, Kaori. Thanks for helping out."
    yu "I’ll ask Sara to like...wire you the money or however the fuck she’s been paying you."

    scene yukiflier16
    with dissolve

    k "Wires are unreliable, Yukiburger. Money is far too large to fit inside of them."
    k "I will return to the Sara and collect my payment in the physical realm sometime before the end of the year."

    scene yukiflier17
    with dissolve

    k "But...until then, hello!"
    k "Press buttons and say goodbye to me soon, Friend! I miss you very much!"
    s "Will do, Kaori. Have a good night."

    scene yukiflier18
    with dissolve

    "Kaori runs off and disappears into some alleyway, probably on the hunt for more chickens or...other animals or something."
    "I don’t see much point in trying to figure out what she’s doing in her spare time."

    yu "You know, it’s starting to make sense why you decided against telling me my niece was still alive."
    s "Sure. Let’s just say that I was doing this for your own good and that it wasn’t just something that completely slipped my mind."

    scene yukiflier19
    with dissolve

    yu "For real, though. Is she like...{i}okay{/i} to function in the real world? Cause I ain’t one to really talk when it comes to shit like that, but I feel like even {i}I’ve{/i} got a leg up compared to her."
    s "She actually functions really well apart from frivolously spending roughly 90%% of her income on trying to free animals. "
    s "I’m pretty sure she’s simultaneously holding six thousand jobs- and you’re somehow only holding {i}one{/i}."
    s "So maybe you should be taking pointers from her, Yuki?"

    scene yukiflier20
    with dissolve

    yu "Hm. You know, when you put it like that, yeah. I guess maybe I could be taking some pointers from her?"
    s "I...wasn’t really being serious. Kaori is an enigma and I don’t think it would be a good idea for any of us to try and live our lives the same way she lives hers."

    scene yukiflier21
    with dissolve

    yu "I’m just glad she’s okay. "
    yu "If my daughter’s not gonna fuckin’ acknowledge my existence, I guess a niece doing it is like...the next best thing."
    yu "‘Sides, Kaori seems actually kind of excited to have someone she can call family. Even if she’s adding fucking “burger” onto the end of my name."
    s "Well hey, maybe one day, all {i}three{/i} of you can sit down and...do whatever it is the three of you did when you were younger."
    yu "Yeah. And maybe I’ll win the lottery and get elected prime minister of Japan as well."
    yu "Don’t feel the need to provide hope where there ain’t none, man. "
    yu "There’s some shit that stays broken forever once you’ve fucked it up...and no amount of glue or...tape, or...any other sticky shit can put it back together."
    yu "What really surprises me, though, is that Yumi doesn’t want to see her."
    yu "The two of them weren’t like...{i}inseparable{/i} or anything like that back then, but she’s one of the few people I’ve actually seen who was able to make her smile."
    yu "...heh. She had a real cute smile back then, too. The kind where there’d be like, missing teeth and shit. But in a “kid” sort of way. Not like a...gross sort of way."
    s "You have such a way with words sometimes."

    scene yukiflier22
    with dissolve

    yu "Right, right. Which is exactly why you had such an issue with what I decided to put on all of our fuckin’ fliers."
    s "Speaking of which, aren’t you supposed to be passing those out?"

    if bonus == True:
        yu "What, am I not allowed to take a fuckin’ break to hang out with the dude at the top of my secret sex list?"
    else:
        yu "Yeah, but I'm allergic to paper and holding them for so long is starting to make my throat close up."

    s "I {i}knew{/i} it. "
    yu "It was a joke, asshole. "
    yu "I don’t care if you’re Yumi’s new dad or...sugar daddy or whatever the fuck you are-"
    s "I believe it’s pronounced “teacher.”"
    yu "Sure, let’s go with that."
    yu "What I’m sayin’ is I don’t care what your role is. I’m just glad I’ve got someone like you to hang around who actually feels like a decently good person."
    yu "That shit’s hard to come by."
    s "I feel like you are, once again, gravely misinterpreting the kind of person I am."
    yu "Am I?"
    s "Absolutely. And this isn’t me just being a self-loathing piece of shit again- that’s what inner monologues are for."
    yu "Uh-huh. Right."
    s "What I’m saying is that you can’t really judge a person by just...how they act around you. You need to think about what’s underneath the surface as well."
    s "You barely know me. Have I been mostly kind to you? Sure. But what about how I treat other people? "
    s "What about how I treat Yumi?"
    yu "You mean when you’re paying her phone bill and taking her job hunting? Yeah, you sound like a real douche."
    s "No, Yuki...that’s not what I mean."

    if bonus == True:
        yu "Then...you mean like when you’re boning her?"
    else:
        yu "Then...you mean like when you’re hugging her?"

    s "You know what? I feel like getting into a philosophical debate right now probably isn’t the best thing for either one of us."
    s "Just know that I’m not as great as you think I am."
    yu "Oh, I don’t think you’re great at all."
    yu "I’m sure you’ve done plenty of shit that you regret- but we’ve all got stuff like that."
    yu "You think I look back on all of the mistakes I’ve made and just shrug them off because I’m like...above them now or something? Course not."
    yu "I think I’m the fuckin’ scum of the earth. And I’m sure you feel the same way about yourself most of the time."
    yu "But those thoughts are our own, man. You’ve gotta look at shit from the outside."
    yu "You obviously don’t think I’m fucking Satan. If you did, you wouldn’t be helping me out all the fuckin’ time."
    yu "So I can think whatever the fuck I want about you and you can’t do shit about it."
    yu "We can hate ourselves as much as we want inside of our heads, but until we go out there and show {i}every single person in the fucking world{/i} that we’re against them-"
    yu "There are going to be some people who are just...on our side for no reason whatsoever."
    s "…"
    yu "What? I’m older and more experienced than you. Don’t tell me you’re surprised to hear some words of wisdom out of me?"
    yu "Now, help me figure out what to do with the rest of these fliers. And don’t suggest that I just throw them out or whatever. The more customers Sakaki-bar-a gets, the more I get paid."
    s "Can we just go back to calling it “the bar” please? I get irrationally angry each time I remember the real name."
    yu "We can do whatever the fuck you want as soon as we finish handin’ these out. "
    yu "Here-"

    scene black
    with dissolve

    "Yuki hands me roughly half of her stack of fliers and the two of us set off in opposite directions to...distribute them, I guess."
    "I don’t really know how I allowed myself to get roped into this, but it is what it is."

    if sarasex == True and bonus == True:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks (And blowjobs) she’s given me."
    else:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks she’s given me."

    "I do my best to hand them out to people, but “my best” only survives for a matter of minutes before being brutally murdered in the form of me stashing my entire pile in a nearby shoe store."
    "But hey, my job was to get rid of all of my fliers without throwing them away, and that is precisely what I did."
    "I send Yuki a text to figure out where she is and whether or not she wants to continue hanging out after she’s done with “work.”"
    "Fortunately, she also found a shoe store to offload her fliers in, and the two of us reconvene at our original meeting spot and decide to head to a nearby convenience store for dinner."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate10 = True
    jump yukidate10p2

label yukidate10p2:
...
```

## Code that triggers this event
File: \game\YukiEvents.rpy
Code:
```python
...
label callyukinight:
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callnight

    if yuki_love >= 0 and streets30 == True and ramen20 == True and yukidate1 == False:
        jump yukidate1
    if yuki_love >= 5 and yumidorm30 == True and yukidate1 == True and yukidate5 == False:
        jump yukidate5
    if yuki_love >= 10 and yukidate5 == True and kirindorm25 == True and yukidate10 == False:
        jump yukidate10
...
```