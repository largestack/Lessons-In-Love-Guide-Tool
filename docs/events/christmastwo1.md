# Three Amigos (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 455

* Event [The Gap in the Door](./chikadate45.md) (Chika) is completed)

* Event [See You Around](./yumispecial45.md) (Yumi) is completed)

* Event [Loxosceles Reclusa](./norikodorm25.md) (Noriko) is completed)

* Event [Dear You](./nikiinvite2.md) (Niki) is completed)

* Event [The Place She Falls Asleep At Night](./sarabar25p2.md) (Sara) is completed)

* Day of week is Thursday



## Next events

None

## Event properties

* Id: christmastwo1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->christmastwo1

## Official wiki page

[Three Amigos](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo1&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo1:
    scene wakanareturns1
    with fade
    play music "wewereangels.mp3"

    "And so another day comes to an end with absolutely nothing happening."
    "It’s almost as if becoming a teacher isn’t really as exciting as most people make it out to be."
    "Granted, I’m no stranger when it comes to traversing paths that most would find impassable."
    "Or at least I think that's the case."
    "I’m not the best when it comes to figuring out how the people around me feel but, then again, that’s something I’ve willed myself into doing simply because I like walking alone a little better."
    "I guess what I’m trying to get at here is that some days are good."
    "And others?"
    "Well-"
    "Saying they don’t matter is the nice way of putting it."
    "Today is one of those days- where I’m acutely aware of my state of being and how remarkably pointless it is from the perspective of some other person behind some other desk."

    if bonus == True:
        "But, at least there’s only one more day of this until the weekly cycle of self-induced apathy and student-induced orgasms starts over."

    "Thankfully, this weekend comes fully equipped with yet another get together that I’m positive won’t result in any sort of drama or rivalry between classmates."
    "After all, nothing bad ever happens as a result of those."
    "And nothing bad ever happens on Christmas. "
    "So, all things considered, I think I can count on making some memories that may or may not crush and/or consume the ones this mind used to hold. "
    "And, even more things considered- "
    "I wonder how much longer I can keep this up for."
    "{i}Welcome to the second Lessons in Love special Christmas update!{/i}"
    "{i}The next twenty-something events will play in succession.{/i}"
    "{i}Now, I know what you’re thinking.{/i}"
    "{i}Why is this chain of events starting on a Thursday? And why is it starting in an office completely devoid of all traces of Christmas spirit?{/i}"
    "{i}Well, unfortunately, I don’t have an answer for you.{/i}"
    "{i}But, you see- sometimes, it’s the average days that don’t carry any sort of weight that wind up completely changing everything we know when we look back on them.{/i}"
    "{i}And hey, maybe this random Thursday will be one of those days.{/i}"
    "{i}Or maybe I’m just bullshitting you and this really won’t matter at all when everything is said and done.{/i}"
    "{i}I guess we never really know until things are said and done, though, huh?{/i}"
    "{i}Anyway, I’ll leave you alone for now.{/i}"
    "{i}Please cherish this Christmas- for you never know how many of them you have left.{/i}"

    play sound "knock.mp3"

    "While I nodded, nearly napping, suddenly there came a tapping."

    s "Come in."

    play sound "dooropen.mp3"
    scene wakanareturns2
    with dissolve

    w "Pardon the intrusion."
    s "Woah. Hey."
    s "Can’t say I expected to see you today."
    w "Please hold your applause. I’m not returning to school until this coming Monday. I just came by to check on my office plants."
    w "Oh, and to do this."

    scene wakanareturns3
    with dissolve

    w "I am terribly sorry for the commotion I must have caused during your strange, winter beach trip. "
    w "I can’t imagine you dwelled too much on it seeing as you made no attempt to contact neither myself nor my significant other during my stay in the hospital-"
    w "But I don’t blame you at all on account of the position my actions must have put you in."
    w "It was a mistake. A bad one."
    w "And if there is anything I can do to prevent it from having a long-lasting effect on our friendship, please let me know. "
    s "So it is a friendship after all. "

    scene wakanareturns4
    with dissolve

    w "Well, yes. I thought that was obvious."
    s "You don’t have to apologize, Wakana. It’s fine."

    scene wakanareturns5
    with dissolve

    w "No, it’s not fine. And I do have to apologize."
    w "Even if {i}you{/i} don’t personally care, I’m sure some of your students may have been quite frightened by the event."
    w "I should never have placed anyone in that position, and not apologizing for it would weigh on me greater than the bulk of life itself."
    s "Can you stop assuming I don’t personally care just because I didn’t go out of my way to contact you?"

    scene wakanareturns6
    with dissolve

    w "I’d be willing to accept Miyamura as a token of your apology."
    s "I’m serious. What would I have even said if I {i}did{/i} contact you?"

    scene wakanareturns7
    with dissolve

    w "Hello, Wakana. Glad to hear you’re...still alive?"
    w "It’s not the most eloquent way of wording it, but you have experience in writing, so I’m sure you’d figure something out."

    scene wakanareturns8
    with dissolve

    w "I won’t be petty about it, though. It’s fine."
    s "You seemed pretty petty just a few seconds ago."
    w "Yeah, well, I want to fucking die. Not literally, though. "
    w "Osako has asked that I add that clause whenever I utter those words as she’s still understandably shaken up over the whole thing."
    s "Would you mind...explaining what happened, maybe? I still don’t really understand what went down."
    s "I didn’t even know you were on drugs until I woke up and heard that you were rushed to the hospital."

    scene wakanareturns9
    with dissolve

    w "I’m not {i}on drugs-{/i} and this may be hard to believe given the type of person that I’ve painted myself to be, but I wasn’t trying to kill myself either."
    w "I just took a little too much of my pain medication and it caused my body to temporarily shut down."
    s "That sounds like more than just a “little too much.”"

    scene wakanareturns10
    with dissolve

    w "Yeah, I'm aware. And I’ve spent essentially every conscious minute since then apologizing for it."
    w "If I could go back and just deal with it, I would. But that ship has sailed and carried us off to the middle of nowhere, and now I just want to go home."
    w "I have a problem. It is no fault of yours, nor is it any fault of Osako’s, but I need you to understand that it is not something I wanted or asked for."
    s "Hey, I was just being a little sarcastic. You don’t have to freak out."
    w "I’m not-"

    scene wakanareturns11
    with dissolve

    w "Ugh. "
    w "And now the {i}lack{/i} of medication is causing me to speak out of turn. "
    w "There’s truly no winning in this world, is there?"
    s "Nope, but there’s certainly losing. And you came pretty damn close to doing that at the beach."
    s "So just...be good or whatever and don’t almost kill yourself again and I’m sure everything will be just fine."

    scene wakanareturns12
    with dissolve

    w "...Yeah."

    if bonus == True:
        w "You know, if you didn’t spend virtually all of your free time committing heinous acts on high school girls, you might actually be a decent person."
        s "And if you didn’t spend all of your free time binding and gagging my karate instructor, you might find that you’re into the same sort of stuff that I am."
        s "Which isn’t me admitting anything, by the way."
        w "I’m sure."

    s "..."
    w "..."

    play sound "knock.mp3"
    scene wakanareturns13
    with dissolve

    w "{i}Ahem...{/i}"
    s "Oh, look. A conveniently timed knock that prevents this conversation from going somewhere unfavorable."
    ima "Yo, let me in! I have to tell you about a thing!"
    ima "Unless you’re helping some student with her problems or something! If that’s the case, I’m sorry and I will wait!"
    s "It’s fine. You can come in."

    play sound "dooropen.mp3"
    scene wakanareturns14
    with dissolve

    ima "What, am I not cool enough to get invited to your secret teacher meetings or something?"
    s "Sorry, but I think Wakana coming back means that you’re officially unemployed again."

    scene wakanareturns15
    with dissolve

    ima "What?! She’s back?! But I had a whole ‘nother month of cool shit planned!"
    w "Ahh. You must be the one who replaced me, then."

    scene wakanareturns16
    with dissolve

    ima "Imani Imai. You’re...Wakana Watabe, right?"
    w "Yes, but...what are we doing with our hands, exactly?"
    ima "Bonding. We’re friends now."
    w "We are?"

    scene wakanareturns17
    with dissolve

    ima "Yeah. All three of us are. We’re like those three amigos or whatever. Just instead of fighting people with swords and stuff, we fight them with {i}information.{/i}"
    s "I think you're thinking of the three musketeers."
    w "I take it you two have already gotten acquainted, then?"
    s "She just kind of showed up while Noriko was pouring her heart out to me in school the other day."
    w "Noriko?"
    s "The anarchist girl that you pawned off on me."
    w "Oh."
    w "She’s still fawning over you to that extent? I had assumed that was just a one time thing."
    s "She’s gotten...better."
    ima "You two married yet? Because I don’t remember getting a wedding invite."
    s "We are not, no. Nor are we going to be any time soon."

    scene wakanareturns18
    with dissolve

    ima "Are you going to come too? You seem pretty close to this guy since you came to his office before even dropping by your classroom."
    s "Wait, did you really come straight to my-"
    w "Miss...Imai, would you be willing to fill me in on what you’ve been teaching my class during my leave of absence?"
    s "Or just ignore me. That’s fine."
    ima "You can call me Imani, it’s cool. And they’re doing great, actually."
    ima "I will admit that I may have veered a {i}little{/i} far off the curriculum, but that’s kinda just how I do stuff."
    ima "So my bad if everyone is suddenly like, really knowledgeable about the Crusades and praying mantises and shit."
    w "Those...are certainly strange topics to specialize in."
    ima "You all good now, Wakana? You were in the hospital, right?"

    scene wakanareturns19
    with dissolve

    w "Well enough to return to school, I suppose."
    w "Which means that, come Monday, you’ll likely be moved to a temporary position or something along those lines."
    ima "You think?"

    scene wakanareturns20
    with dissolve

    w "Quite often. Though, I can’t say the thoughts are always colorful or jubilant."
    ima "And what do you think, Sensei? Where will I wind up?"
    ima "New school nurse? Vice principal? Janitor?"
    s "For your own safety, I hope you don’t wind up as the janitor."
    w "Our school has a strange history of losing members of the custodial staff to freak accidents or, on some occasions, manslaughter."

    scene wakanareturns21
    with dissolve

    ima "Well, damn. I thought Japanese schools were supposed to be safe. I didn’t realize I was walking into some kind of murder zone when I took this job."
    w "Where are you from, if you don’t mind me asking?"
    ima "Switzerland."
    w "I see."
    ima "Wales."
    w "..."
    ima "Alabama."
    w "..."
    ima "..."

    scene wakanareturns22
    with dissolve

    ima "Okay, fine. I moved here from Ghana right before the city was closed off."
    ima "I just thought it would be funny to name all of the whitest places I could think of since you don’t really have many teachers that look like me here."
    ima "And by {i}many{/i} I mean literally none. It’s just me."
    s "Is that something you’re not comfortable with?"

    scene wakanareturns23
    with dissolve

    ima "Oh, no. I’m totally cool with it. Just an awkward attempt at humor, I guess. I don’t know."
    ima "Even though I’ve been here for a few years now, I still don’t really have any friends. And I just thought it’d be kinda cool if like, you know, all three of us could hang out sometime or something."

    scene wakanareturns24
    with dissolve

    ima "But if you’d rather keep it professional or whatever, that’s fine too. You can just think I’m weird and I’ll go crawl in a hole and die."
    w "Hm."
    s "I mean...I’m fine with hanging out sometimes. Wakana is the one who’ll likely need convincing."

    scene wakanareturns25
    with dissolve

    ima "{i}Wakanaaaaaaa.{/i}"
    w "..."
    ima "{i}Wakanaaaaaaaaaaaaaaaaaaaaaa.{/i}"
    w "..."
    ima "{i}Wakana Wakana Wakanaaaaaa.{/i}"
    w "What are you doing?"

    scene wakanareturns26
    with dissolve

    ima "Will you pleeeeeease be my friend?"
    s "I don’t think that sort of thing will work on-"
    w "Sure."

    scene wakanareturns27
    with dissolve

    s "Oh."
    ima "Hell yeah! Teacher pals! Knowledge partners! Education...compadres!"
    w "Why do you think I’m so against the idea of socializing with my peers?"
    s "Because you spend roughly half of every day either talking about how you want to die or complaining about your students."

    scene wakanareturns28
    with dissolve

    w "But when do I ever complain about people who aren’t students?"
    s "You complain about me literally all the time."

    scene wakanareturns29
    with dissolve

    w "And yet I came here before even watering my plants."
    s "..."
    w "..."

    if bonus == True:
        ima "Wait, are you two fucking?"
    else:
        ima "Wait, are you two hug buds?!"

    scene wakanareturns30
    with dissolve

    w "Uhh...what?"

    if bonus == True:
        ima "Oh my God! Is {i}that{/i} what you were about to do before I knocked on the door?! Am I interrupting a sweet reunion bang sesh right now?!"
    else:
        ima "Oh my God! Is {i}that{/i} what you were about to do before I knocked on the door?!"

    scene wakanareturns31
    with dissolve

    if bonus == True:
        ima "Sorry. I’ll close my eyes. I’m sure it must have been hard after all of that time apart. Just forget I’m even here."
        ima "Have at thee!"
        s "Welp, you heard her Wakana. Let’s commence with our planned sexual intercourse now."
    else:
        ima "I have to close my eyes. I have a rare disease where if I ever see anyone hug, I die."

    w "Open your eyes. I’m dating a woman."

    scene wakanareturns32
    with dissolve

    ima "Oh, shit."

    if bonus == True:
        ima "And she’s okay with you banging your male coworker?"
    else:
        ima "What's her favorite breed of dog?"

    w "..."
    s "Is there something else you need, Imani?"

    scene wakanareturns33
    with dissolve

    ima "Maybe some ear plugs so I don’t hear anything when you two start going at it?"

    if bonus == True:
        s "Leaving the office would also suffice, you know."
    else:
        "How does she know I am such a loud hugger?"

    w "Please don’t insinuate that any of what she’s saying bears any ounce of truth whatsoever."
    ima "I can’t leave. What if someone saw me come in here after you two and they think {i}I’m{/i} a part of this secret tryst?"
    s "Wouldn’t leaving before us sort of quell that notion?"

    scene wakanareturns34
    with dissolve

    ima "Nooooo because then they’ll think I’m bad at stuff and that I couldn’t keep up with all of the action! I’m a part of this now!"

    if bonus == True:
        s "Well, either we have a threesome or we all leave this office together and just...go home since it’s already well past school hours."
    else:
        s "I am so confused and scared."

    scene wakanareturns35
    with dissolve

    ima "Hmmmmmmmmmm..."

    if bonus == True:
        w "I don’t believe Osako would take kindly to the idea of a threesome she isn’t involved in."
        s "Would she...take kindly to the idea of one she {i}is{/i} involved in?"
        w "Maybe? I’ve never asked."
    else:
        w "I am realizing now that I have never asked Osako about her favorite breed of dog. I have failed as a significant other."

    scene wakanareturns36
    with dissolve

    ima "Wait! But then what will happen to me?! Three plus one does not equal three! I know this because I am a teacher!"

    if bonus == True:
        w "In lieu of any sexual activities, I propose that the three of us simply leave here together and...find something else to do if we’re not yet done with this...reunion-slash-introduction."
    else:
        w "I do not have any idea what this strange, potentially intoxicated teacher is saying, but I propose that the three of us do a thing."

    scene wakanareturns37
    with dissolve

    w "Does that work for you?"
    s "I mean...I was kind of planning on just going home, but if you really want to keep hanging out, I guess I can do that instead."
    w "How kind of you, making time for your recently near-departed friend."

    if bonus == True:
        ima "I’m game! Hanging out normally sounds a lot less...sticky than a threesome, too."
        w "My only condition is that any and all discussions about {i}threesomes{/i} cease immediately, as I was already intending to visit Osako at the maid cafe."
        w "I’ve just added the two of you to the plan as well because...friendship."
    else:
        ima "I’m game! I love doing things!"

    scene wakanareturns38
    with dissolve

    ima "I’m gonna cry. It’s been years since I’ve gone out with coworkers."
    w "If you cry, I’m rescinding your invitation and cancelling our friendship indefinitely."
    ima "I’ll...{i}*sniff*{/i}"
    ima "I’ll do my best..."

    scene black
    with dissolve2

    "Somehow or another, I wind up getting dragged into a get together with Wakana and Imani."
    "Well, I guess dragged isn’t really an accurate term since I’m not really {i}against{/i} the idea of spending time with the two of them."

    if bonus == True:
        "I would have just much preferred the original idea since the new one doesn’t contain group sex."
        "But alas, those are thoughts I can not allow myself to be burdened with in the presence of someone who could eliminate me at the drop of a hat."

    stop music fadeout 10.0

    "Actually, now that she’s in my mind- I wonder how Osako’s doing with the whole Wakana situation."
    "I’d decided to stay out of her affairs so she could have time to figure things out with Wakana, but..."
    "Now that Wakana is doing, at least on a surface level, much better...I wonder if any of those worries I was, well, {i}worried{/i} about have vanished."
    "But just thinking that won’t help."
    "In fact, thinking rarely ever does anything to begin with."
    "I’ll just continue to go with the flow, hang out with a small group of coworkers like a normal functioning adult, and see how things play out from here."
    "Without any interference from me."

    $ renpy.end_replay()
    $ wakana_love += 1
    $ imani_love += 1
    $ christmastwo1 = True

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo2

label christmastwo2:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
    if totaldays >= 400 and day == 1 and halloweentwo13 == True and norikospecial20 == False:
        jump norikospecial20
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
    if totaldays >= 424 and kirindorm25 == True and day == 1 and chikaspecial40 == False:
        jump chikaspecial40
    if totaldays >= 455 and chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and day == 4 and christmastwo1 == False:
        jump christmastwo1
...
```