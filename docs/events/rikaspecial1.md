# Metronome In Love
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rikaspecial1&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 541

❌Event "[Rin: Hot Boy Summer](./rindorm55p2.md)" is completed (event=rindorm55p2)

❌Event "[Sana: Black Sandy Beaches](./bar55.md)" is completed (event=bar55)

❌Day of week is Wednesday



## Next events
* [Main: Grief Seed](./day543.md)

## Event properties
* ID: rikaspecial1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\chap3.rpy
Code:
```python
...
label rikaspecial1:

    scene rikacomesearly1
    with fade
    play music "10c.mp3"

    s "Are you two going to explain why you’re here? Or are you just going to keep staring at me without saying anything?"
    r "..."
    n "..."

    "So, I guess this is my life now."
    "Rin and Noriko wasted no time at all coming here, following me straight from the classroom as soon as the final bell rang."
    "It has been roughly three minutes of silence since they closed the door, meaning neither one of them has said a word yet."
    "I give it three more minutes before I need to sacrifice one of them as a show of strength to send the other one running away."

    n "..."
    r "..."

    "But which one should it be?"

    menu:
        "Sacrifice Noriko":
            s "I’m sorry, Noriko. But you are going to have to die."

            scene rikacomesearly2
            with dissolve

            r "Tch! Damn it!"
            n "Pay up, Rin. A deal’s a deal- and I win even if it means I am going to be sacrificed. "
            r "If there is anything I have learned from killing hookers in Grand Theft Auto, it’s that you always get your money back once they die."
            s "I feel like I am missing a lot of context right now."

        "Sacrifice Rin":
            s "I’m sorry, Rin. But I need to sacrifice you."

            scene rikacomesearly3
            with dissolve

            n "Hah...damn it."
            r "Hell yeah! Thanks so much, Sensei! I’m now 500 yen richer thanks to you!"
            s "You’re...what?"

    scene rikacomesearly4
    with dissolve

    n "We made a bet to see whose name you’d say first. I’m not sure we would have if we knew it was going to result in one of us dying, but hey. A bet’s a bet."
    s "What an exciting and productive use of your time. I completely understand why you came directly to my office after school now and not to...whichever room the light music club practices in."
    r "Noriko and I are taking the day off. No practice for us, Sensei."
    n "Well...it’s less “taking the day off” and more “giving Otoha some time alone with Sana.”"
    r "Non-sexual time, of course. I made sure to check. You never know what kind of tricks Sana might be hiding up her sleeves."
    s "And why exactly does Otoha need time alone with Sana?"
    n "Sana’s still really weak when it comes to drums and Otoha has a fair bit of experience, so we’re dedicating today to some one-on-one training."
    r "But mostly because we’d probably just get in the way and Otoha needs to focus when she’s doing stuff like that."
    r "Also, it’s not {i}really{/i} one-on-one since Chika is there..but still."
    s "Interesting that Chika stayed behind if the two of you decided to abstain. Seems like she’s a lot closer to you two than either of them."

    scene rikacomesearly5
    with dissolve

    r "We’re really only “abstaining” because we’ve already been yelled at once- the {i}last{/i} time Otoha tried to help Sana."
    r "Us being here is what’s safest for everyone right now."
    n "Just hope Chika doesn’t wind up getting on her nerves. I’m not sure how Otoha feels about someone just looming in the background, but that would make {i}me{/i} feel weird as hell if I was the one tutoring."

    scene rikacomesearly6
    with dissolve

    r "Chika will be totally fine. She’s good at reading people. "
    r "Well...not good enough to realize when someone she’s close to has a crush on her. But, hey. Same. "
    s "I’d be worried about Sana if anything. She doesn’t exactly shine in social situations. Let alone social situations with girls she hasn’t spoken to much."

    scene rikacomesearly7
    with dissolve

    r "Oh, stop. Otoha’s a great teacher and I’m sure that Sana is completely fine."

    scene rikacomesearly8
    with fade

    "{i}She was not fine.{/i}"

    o "Sana, chill. It’s fine to play a little slower when you’re just starting out. "
    o "Just focus on keeping a steady rhythm going and add speed once you’re more comfortable with how everything feels. "
    o "If you keep trying to act like Travis Barker, you’re gonna burn yourself out and never want to play again."
    sa "Travis...who?..."
    o "Just...some guy who plays too fast. Don’t worry about it. "
    o "Fact is, you’re really not bad. A lot better than I expected you to be at least. It’s clear you’ve got some understanding of music and, in time, I’m sure you’ll be solid."
    o "Just gotta...not work yourself too hard for the time being."

    scene rikacomesearly9
    with dissolve

    sa "I’m sorry...I know I’m the one...holding everyone up..."
    o "You’re the only one without any experience. If you {i}weren’t{/i} holding us up, it would mean that we suck."

    scene rikacomesearly10
    with dissolve

    c "Maybe she should try playing along with a song instead of your metronome thingy? Music’s supposed to be, like, something you {i}feel.{/i} Right?"
    c "I obviously can’t speak for Sana, but I can’t bring myself to get excited hearing “click...click...click” over and over."
    o "Well, it’s a good thing you’re not the one playing then."

    scene rikacomesearly11
    with dissolve

    c "Jeez. Hostile much? I’m just trying to help. "
    c "And the article I pulled up says a lot of drummers have a ton of success early on by just learning to play along with songs they like."

    play sound "slidedoor.mp3"
    scene rikacomesearly12
    with dissolve

    o "Oh, okay. It {i}must{/i} be true if you found an article. "
    ri "Umm..."
    o "I’m sure there are plenty of people who benefit from that method, but it’s a lot better to drill the basics into your head rather than just bypassing the training period and hoping to pick them up along the way."
    ri "S...Sorry to interrupt, but would any of you happen to know where...Rin Rokuhara is?"

    scene rikacomesearly13
    with dissolve

    o "Huh?"
    c "Rin? I can text her and find out. You a new teacher or something?"

    scene rikacomesearly14
    with dissolve

    ri "Uhh...not quite..."
    c "Wait..."
    c "Aren't you her mom?!"
    c "Because you look crazy familiar and I’m like, 99%% sure I saw you drop her off at middle school a few times."
    o "Rin’s...mom? You’re here? At school? Right now?"
    ri "Hahah...Guilty as charged..."

    scene rikacomesearly15
    with fade

    o "Uhh...okay. Hi."
    o "I’m...Otoha Okakura. "
    o "Rin’s...girlfriend. "
    o "It’s...really nice to finally meet you."

    scene rikacomesearly16
    with dissolve

    ri "Oh, shit!"
    c "And I’m Chika Chosokabe. Rin’s friend."

    scene rikacomesearly17
    with dissolve

    ri "Oh...{i}shit.{/i}"
    o "..."
    c "..."
    c "Welp, I can see that I’m not needed here. But it was nice meeting you!"

    scene rikacomesearly18
    with dissolve

    ri "I’m sorry, I...I probably should have realized that you and Rin would be in the same club. She’s going to kill me if she finds out I met you like this."
    o "Rin is? No way. She’s been gung-ho about getting me to meet you and your partner for months now. "

    scene rikacomesearly19
    with dissolve

    ri "Ahh, yes...the partner I still have."
    o "{i}I{/i} should be the one apologizing for delaying things for so long. I just...well, you see, {i}my{/i} parents aren’t as “progressive” as you two and-"

    scene rikacomesearly20
    with dissolve

    o "And..."
    o "Mrs...Rokuhara?..."
    ri "Not now, not now, not now! Any time but now!"

    scene rikacomesearly21
    with fade

    n "...and that’s exactly why soy-based protein is extremely good for you so long as you work out a proper diet!"
    s "Stop trying to convert me, Noriko. I get enough of that out of Yasu."
    n "There’s a difference between conversion and education, Sensei. "
    n "All I’m doing is providing information that {i}you{/i} can use to make your {i}own{/i} decision. I’d never judge you for having a different opinion than me."
    s "That’s weird because your sister judges me for having literally any opinion at all."
    n "Yeah, that’s just her archetype. I’m the exact opposite. I would {i}never{/i} be mean to you because I’m worried it would impede the amount of time I am able to spend in your presence."
    s "Stop liking me so much. It’s scary."
    n "Never."

    scene rikacomesearly22
    with dissolve

    s "How are you doing over there, Rin? You went silent after Noriko started talking about vegetarianism and just never recovered."
    r "Chika’s being weird. I think something is going on in the club room."
    n "Are Otoha and Sana making out? Is {i}that{/i} why Otoha was so insistent on-"

    scene rikacomesearly23
    with hpunch

    r "OH, FUCK! "
    r "I HAVE TO GO!"

    play sound "doorslam.mp3"
    scene rikacomesearly24
    with hpunch

    n "..."
    s "Wow. Maybe they actually {i}were{/i} making out."
    n "Poor Rin. Just can’t catch a break."

    scene rikacomesearly25
    with dissolve

    n "Anyway...it’s just the two of us now...I sure hope no one takes advantage of me..."
    s "We both know you’d pull back the second I try."

    scene rikacomesearly26
    with dissolve

    n "Probably. But you can take solace in knowing that I’d kick myself for it while rubbing one out later."
    n "But, undying desire to be with you under only the most perfect of circumstances aside, what do you wanna talk about now that we’re alone?"
    n "Halloween’s coming up. You going to dress up this year?"
    s "Do I really look like the type of person to dress up for Halloween?"
    n "You look like the type of person {i}I{/i} want to dress up for Halloween."
    s "I’m a little more interested in what you’ll be wearing. Going to raid your sister’s closet and then beg for me to finger you again?"

    scene rikacomesearly27
    with dissolve

    n "Hey, that’s mean. I was going through some shit back then. Granted, I’m going through some shit right now as well. But I was going through shit back then too."

    scene rikacomesearly28
    with dissolve

    n "But no. I’m hoping to make it through the entire holiday this year without trying to force something to happen between us. Which allows me to perfectly segue into the reason for all of that- my darling sister."
    s "What about her?"
    n "How are things with you two?"
    s "What do you mean?"
    n "You know exactly what I mean. I want to know if you guys are in love again yet. "
    s "I’m sure Niki will waste no time at all in telling you if we are."
    n "She already talks about you all the time. The only side I don’t fully understand is yours. "
    n "Are you, like...waiting for something? Because I could have sworn her letters would have been the nail in your coffin."
    s "I don’t want to talk about this with you, Noriko."
    n "Is it because I’m around the same age she was when she used to give you blowjobs under the blanket on our living room couch?"
    s "It’s because the only relationship I want to talk about with you is the one that {i}we{/i} have."
    s "Not the one I have with some other Nakayama who apparently used to give me blowjobs under the blanket on your living room couch."
    n "Sounds like they were pretty bad blowjobs if you can’t even remember. I promise to work a little harder and make mine memorable once I’m done with all of this self-sacrificing."
    s "Uh-huh. And when will that be?"
    n "Sometime after Halloween, hopefully."

    scene black
    with dissolve2

    n "I’ve been feeling really {i}hot{/i} lately...and I'm not sure how much longer I can keep it all in."

    "........."
    "......"
    "..."

    scene rikacomesearly29
    with dissolve2

    r "..."
    ri "..."
    r "Mom."
    ri "Heeeeeey, Rin. Nice to...be in the same...building as you...for the first time today..."
    r "What do you think you’re doing?"
    ri "Oh, you know...a little crying...a little...more crying..."
    r "And the suit?"
    ri "..."
    r "That {i}interview{/i} you had..."
    r "Where was it?"
    ri "..."

    scene rikacomesearly30
    with dissolve

    ri "L-Look at it this way! If your club goes any longer without an advisor, it might get shut down! And it’s better off having somebody who knows what they’re talking about than some random person, right?!"
    r "Mom! How am I supposed to have a fun and exciting high school life if {i}you’re{/i} there too?! You’re 43 years old!"

    scene rikacomesearly31
    with hpunch

    ri "Stop spreading misinformation! I’m 42 and you know it! "
    r "You’ve still lived my entire life more than twice! You don’t need to live it a third time! Let me have this!"
    o "Rin...why didn’t you tell me?"

    scene rikacomesearly32
    with dissolve

    r "Oh..."
    r "So..."
    r "I guess you found out."
    o "Yeah. And now I feel like an asshole for making your mom cry within five minutes of meeting her."
    ri "It’s my fault. I should have stayed in the dorm. Oh, and by dorm, I mean a different dorm. Not the one you guys live in since I am 42 and living there would be wrong."
    o "Is she actually 42?"
    r "She’s 43."

    scene rikacomesearly33
    with dissolve

    ri "That’s it! You’re grounded! Go to our room!"
    r "Phpbhpbhpbt!"
    o "Rin, seriously. What’s going on?"

    scene rikacomesearly34
    with dissolve

    r "I really wasn’t trying to hide anything from you, Otoha..."
    r "I didn’t even know until super recently, so...this is all pretty messed up for me as well. I haven’t even finished wrapping my head around everything yet."
    o "Do you...wanna like...like, talk about it or something?"
    r "Yeah, but...not with my mom here."

    scene rikacomesearly35
    with dissolve

    o "Maybe...after practice then? "
    o "I still have to teach Sana how to-"
    ri "No. Go talk now. Waiting on things never helps. "
    ri "Oh, and neither do flowers apparently, so don’t go buying each other roses or something. It’ll just make you look like a loser whose only redeeming factor is how good she is at- nope. Shouldn’t say that."
    ri "Anyway, I’m still unemployed technically, but I know my way around instruments. "
    ri "I’ll hang out here while you two go do cutesy girlfriend stuff. Love is stupid. I hate this."
    r "Can we...talk later too? Please?"
    r "I still have...a lot of questions..."

    scene rikacomesearly36
    with dissolve

    ri "Yeah. We’ll talk tonight."
    ri "I’ll pick up a pizza on the way home."
    r "Pepperoni, please."
    ri "Are there even other toppings?"

    scene black
    with dissolve2
    stop music fadeout 15.0

    $ renpy.end_replay()
    $ rikaspecial1 = True

    "........."
    "......"
    "..."

    jump rinspecial55

label day543:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
    if totaldays >= 500 and chapthree8 == True and church15 == True and yasuspecial15 == False:
        jump yasuspecial15
    if totaldays >= 514 and yasudorm20 == True and nodokadorm15 == True and day == 4 and nodokaspecial15p1 == False:
        jump nodokaspecial15p1
    if totaldays >= 522 and sadgirls7 == True and day == 5 and sadgirls8 == False:
        jump sadgirls8
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
    if totaldays >= 540 and imanispecial1 == True and day == 2 and ayanespecial40 == False:
        jump ayanespecial40
    if totaldays >= 541 and rindorm55p2 == True and bar55 == True and day == 3 and rikaspecial1 == False:
        jump rikaspecial1
...
```