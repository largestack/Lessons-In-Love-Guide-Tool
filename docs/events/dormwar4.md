# Alive & Active! All Out Athletics! (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Imouto Mode!](./dormwar3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar4
* Group: Main
* Triggered by label: dormwar3
* Chain sources: dormwar3
* Chain sources path: dormwar3

## Official wiki page

[Alive & Active! All Out Athletics!](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar4&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar4:
    scene sky
    with dissolve2
    play music "highspeedprinter.mp3"

    "It’s surprisingly tolerable outside today- which is great because the next part of the dorm war is apparently going to take place at the park."
    "It’s also apparently going to be a battle between Kirin and Miku, so I’m pretty sure I already know how it’s going to end."
    "Not to throw shade at Kirin or anything, of course. I mean, she’s about as athletic as someone who was born with a nice body and a poor work ethic can be."
    "But in order to take down Miku, she’ll need to either take performance enhancing drugs or rely on some sort of underhanded tactics to-"
    "Oh."
    "You know, maybe Kirin might win after all?"
    "Her roommate had no problem drugging me to gain an advantage in her competition. So maybe Kirin will drug Miku or something and win that way."
    "Thing is, if that actually happens, I’ll have to get as far away as possible as quickly as possible."
    "I’ve been able to fend off any suspicion from the general public as far as being seen with all of the girls goes, but I feel like it wouldn’t be that easy if one of them was unconscious in broad daylight."
    "Either way, there’s no turning back now."
    "Noriko, Ami and I make our way to the park, only for the two of them to abandon me shortly after and take a walk around the neighborhood themselves."
    "Sensing that the likelihood of either one of them murdering the other isn’t as high as you might expect it to be, I see no point in refusing and instead make my way over to the next two contestants."

    scene athleticstest1
    with dissolve

    ki "Uhh...so I know it’s nicer than normal out right now, but are you really sure wearing shorts is okay? "
    mi "Course I am! "
    ki "Aren’t you like...cold, though?..."
    mi "Maybe a little, but I’ll warm right up the second we kick things off!"
    mi "You wanted me to take this seriously, so I’m takin’ it seriously."
    mi "Figured you would too, but here you are in a friggin’ skirt. How ya plannin’ on takin’ me down when you ain’t even dressed for the job?"
    s "Good morning, you two."

    scene athleticstest2
    with dissolve

    mi "Mornin’, Sensei! Ready to watch Kirin get spanked?!"

    if bonus == True:
        s "Yes. And this competition just got a lot more interesting."
        ki "I feel kind of dumb for not suggesting that, actually. I’d probably have a pretty good chance of winning a test of spank endurance or whatever."
    else:
        s "Keep your hands off of her, Miku. Hitting your friends is bad."
        ki "I'm probs gonna lose anyway so it's not really a big deal."

    s "Don’t tell me you’ve already given up on victory for your {i}actual{/i} contest?"

    scene athleticstest3
    with dissolve

    ki "Nah. I mean, I know it’ll be tough. But I’m not going to just let Miku win as long as {i}you’re{/i} on the line."
    mi "And I’m not gonna let Kirin win cause I’m kinda scared about what that Noriko chick would do to ya if you guys slept in the same room!"
    s "After this morning, I am also mildly afraid of that."
    ki "Looks like you recovered pretty quickly, at least."
    s "Oh, good. So you knew what she was planning on doing."
    ki "In her defense, no one ever told her she couldn’t do that."
    s "Well, as long as you’re not planning on drugging Miku, I’m sure this contest will be a lot more...normal."

    scene athleticstest4
    with dissolve

    mi "Wait a sec! I feel like I’m missin’ an important detail here! What the heck happened this morning?"
    s "Don’t worry about it. "
    s "When are you two starting your thing? And how do I judge it?"

    scene athleticstest5
    with dissolve

    mi "Oh, you don’t have to judge this one. We called in a special guest judge cause we both know you’re not good with all that athletic stuff."
    s "I’ll have you know that I have at least one[school] year’s worth of soccer coaching experience."
    ki "I’m fine with you judging instead of the guest one, to be totally honest."
    s "Thank you for having faith in me, Kirin."
    ki "Oh, I don’t have any faith in you at all. I just don’t want my sister here."
    ka "It’s a little too late for that..."

    scene athleticstest6
    with fade

    ka "Um...good...good morning!"
    ka "I’m going to...help you with the contest thing..."
    ki "Hooraaaaay, Karin is here..."
    mi "Stop bein’ rude, Kirin. Yer gonna make the judge biased and have an even harder time gettin’ the W."

    if bonus == True:
        ki "The only letter I want to get is the D."
        mi "A...draw? Why would you want to tie?"

        scene athleticstest7
        with dissolve

        ka "Maybe she thinks you could both get a point that way?"
        mi "But that’s basically the same as neither of us gettin’ a point at all. I don’t get it."
        mi "Unless she meant getting a dog or somethin’. You guys getting a new puppy, Karin?"
        ka "I hope so. Though I don’t really know why Kirin would know about it and not me."
        ki "How the hell do you get to be their age and not pick up on things like that?"
        s "Just because you’ve been corrupted by the evils of life doesn’t mean they have to be too. Leave them alone."
    else:
        ki "The only letter I want to get is the T."
        s ">=("

    scene athleticstest8
    with dissolve

    mi "Anyway! Why don’t ya give Sensei a breakdown of how the athletics test is gonna go, Karin?"
    ka "Oh! R-Right!"
    ka "So, in order to keep things balanced, there will be three different sections of the test: Speed, strength, and endurance."
    ka "We’ll start off with a simple sprint around the park for the speed contest. "
    ka "After that, we’ll have Miku and Kirin arm wrestle to see which one of them is the “stronger” one. Though, I have to admit that method of testing strength isn’t entirely accurate."
    s "Why even do it that way, then?"
    ka "The captain...uhh, Uta? She was strangely adamant about it."

    "What is with Uta and arm wrestling?"

    ka "And, um...the final test will just be planking. The two of them will start at the same time and whoever falls first, loses."
    ka "Unless, of course, one of them wins the first two contests. If that happens, there’s no reason for the third."
    s "Seems simple enough. Though, with the way it’s structured, it doesn’t really seem like there’s a reason for either of us to be involved."
    ka "Right. Each contest should have a clear winner, but it’s up to us to make sure neither of them tries cheating."
    mi "No cheatin’ happenin’ here! I’m gonna win fair and square!"
    ki "Blah, blah, blah. At least have the dignity to beat me {i}before{/i} getting all braggy and whatnot."
    s "Does that mean you two are ready to go then?"

    scene athleticstest9
    with dissolve

    mi "Aye aye!"
    ki "Ready as I’ll ever be. Let’s just get the speed part over with so we can move on to the stuff I have a chance at."

    scene black
    with dissolve

    "Miku and Kirin take their places next to each other on the stone pathway and take off after Karin’s signal."
    "………"
    "……"
    "…"

    scene athleticstest10
    with dissolve

    mi "C’mon, Kirin! What kinda takeoff is that?!"
    mi "Need me to slow down and let ya catch up?!"
    ki "You really think mind games are going to work on me? I knew this part was over the second we started."
    ki "Just hurry up and beat me so I can take you down in the arm wrestling thing."

    scene athleticstest11
    with fade

    c "You know...I’m glad you came and everything, but it doesn’t really mean anything if you don’t actually {i}cooperate{/i}."
    y "The fuck you want me to do? Put on shorts and run around with those two fucking weirdos?"
    c "Something more than just stand around! All you have to do is engage with somebody and you’ll get us a point!"
    y "Oh, yeah. Let me just go out of my way and do something that will get Sensei in my room for the beach trip. Sounds like a blast."
    c "Are you even {i}coming{/i} to the beach this time? "
    y "Came last time, didn’t I?"
    c "For a couple hours, yeah."
    y "Then I’ll probably be there for a couple hours again. I ain’t fuckin’ {i}engaging{/i}, though. Just let the other girl win."

    scene athleticstest12
    with dissolve

    i "Yeah, I’m not really planning on “winning,” either. So you should probably just leave the two of us alone."
    y "Finally, someone who makes some fuckin’ sense."
    i "Sorry to interrupt, just wanted to say that."
    c "Isn’t you going out of your way to say that kind of what this competition is about in the first place?"
    i "I hope not, because I’m already regretting my decision to come over here and say that."
    i "Anyway, bye."

    scene athleticstest13
    with dissolve

    y "Welp, there ya have it. We both lose."
    c "Ugh...why is it so hard for you to just be a little social?"
    y "Why is it so hard for you to not be a bitch and just let me live my life?"
    c "…"
    y "…"

    scene black
    with dissolve

    "Miku winds up easily winning the first competition, but it’s not like Kirin really tried competing in any way. "
    "The two of them come back to Karin and me and sit down for a few minutes to catch their breath. "
    "But as soon as they’re feeling ready to go again, they sprawl out on the ground and get into position."

    if bonus == True:
        "Normally, that last sentence is a lot more exciting than it is in this context. But I guess there’s a time and a place for that, and a public park in the morning is not either of those things."

    scene athleticstest14
    with dissolve

    ka "Okay! You two know the rules, right?"
    ki "Karin, we’re arm wrestling. What kind of rules do you expect us to know?"
    ka "Well...tournament rules say that-"
    ka "Actually, if we’re going by tournament rules, you two wouldn’t be laying down and-"
    s "How about whoever wins, wins?"
    mi "Sounds good to me! I might be small, but these arms are rock hard and ready to annihilate a certain Kanda sister!"
    ki "Big words for someone who’s about to literally die."
    s "How would you even-"
    ki "Stay out of this, Sensei."
    s "Well, okay then."
    mi "Hey, you plannin’ on takin’ off those gloves? Might be a little hard to keep your grip...and I don’t want ya givin’ yourself even more of a disadvantage."
    ki "How about you just worry about your own strategy and not mine? Kaythanks~"
    mi "Suit yourself...just tryin’ to help."
    ka "Okay...are both of you ready?"
    mi "Heck yeah."
    ki "Bring it on..."
    ka "Then..."
    ka "In 3...2...1..."
    ka "Go!!!!!"

    scene athleticstest15
    with hpunch

    ki "{i}*Lick*{/i}"
    mi "Wha-"

    scene athleticstest16
    with hpunch

    ki "Yay! I win!"
    mi "What the heck was that?!"
    ki "What was what?"
    mi "Did you friggin’ lick me?!"
    ki "Yeah. Want me to do it again?"
    mi "No! Why would anyone ever want you to do somethin’ like that?!"
    ki "You sure? Seemed like you liked it."
    mi "How the heck does it seem like that?! Take this seriously or-"
    s "Round two goes to Kirin."

    scene athleticstest17
    with dissolve

    mi "Heck no it doesn’t! She cheated!"
    ki "There’s no rule that says I can’t lick my opponent."
    s "Karin?"
    ka "I mean...it’s certainly an unusual tactic, but...the rulebook online doesn’t say anything about licking."
    ki "See? Fair and square."
    mi "What does licking have to do with strength?! This competition is rigged!"
    ki "Looks like whoever takes the next round will be crowned the champion."
    mi "I want a do-over! I will not stand for this!"
    mi "Makoto! Come over here!"

    scene black
    with dissolve

    "Makoto doesn’t come over, as she’s currently in the process of discussing something with Uta."
    "In taking a look around, it actually seems like only around half of the class is here."
    "Ami and Noriko I already knew were gone, but Ayane and Maya seem to be absent as well."
    "Same with Futaba and Nodoka. "
    "Though I guess I shouldn’t expect everyone to be here for every single contest."
    "In fact, I didn’t even really want to be at this one."
    "At least not until Kirin started licking her classmates."

    scene athleticstest18
    with dissolve

    r "Soooo, uhh...this is where you’ve been hanging out lately?"
    o "You mean while you’re out making drinks for people? Yup."
    o "Not really as exciting as my old park, but it’s still kinda nice. "
    o "Sensei comes to keep me company sometimes."
    o "Well, when he’s not too busy hanging out at the cafe."

    scene athleticstest19
    with dissolve

    r "I mean...it’s not like he’s there {i}all{/i} the time, you know. Just...when he needs coffee and stuff...cause like..."
    r "We...sell coffee and stuff."
    o "Get out of here. Do you really?"
    r "And...pastries...and...cute girl."
    o "You...sell “cute girl?”"

    scene athleticstest20
    with dissolve

    r "Ah! No! I...I wish!"
    o "You wish?"
    r "No! I...talk with mouth again! Words bad! Bad talk!"
    r "No sell cute girl! Sell hot bean water!"
    o "Rin, chill. You don’t have to freak out around me. We’re cool."

    scene athleticstest21
    with dissolve

    r "Guh..."
    o "But hey! On another note, our contest is up next. "
    o "You nervous? "
    r "Extremely."
    o "Just to make sure, are we talking about the contest or are you still just nervous because of me?"

    scene athleticstest22
    with dissolve

    r "Oh, right. Contest."
    r "Uhh...I’m not really nervous about that, I don’t think. How about you?"
    o "Ehhh. Maybe about him being weird or saying weird stuff or whatever. But I should be fine."
    o "I’ve discovered that there’s something about him that almost everyone else sees that I just...don’t see yet or whatever. "
    o "But I guess you never know."
    o "Maybe you’ll surprise me and hold off longer than I can?"
    t "Emerald Guardian, is your mana low?"
    t "You are not talking as much as usual."

    scene athleticstest23
    with dissolve

    r "Yeah, now that she mentions it, you’ve been unusually quiet. Is something wrong?"
    mo "I’m okay."
    mo "Just tired."
    mo "Don’t mind me."
    r "Huh..."
    r "Well...let us know if we can do anything or whatever."
    o "Yeah. I don’t know you that well or anything but-"
    mo "I’m okay. "
    mo "Thanks."

    scene black
    with dissolve

    "It wasn’t long after the arm wrestling round that Kirin and Miku started the finale of their competition."
    "It’s rather unexciting to watch, though, as it consists of nothing more than the two of them laying there and balancing themselves on their forearms in an act of what I now know as “planking.”"
    "So...I guess we just wait to see if Kirin has any tricks up her sleeve for this round as well."

    scene athleticstest24
    with dissolve

    mi "What?! Why are ya just lookin’ at me like that?"
    ki "Like what? Am I not allowed to look at my friend?"
    mi "Not after just defilin’ my body!"
    ki "Oh, stop. If I was going to defile you, I’d do it in private. Not in front of a bunch of people. "
    ki "That whole licking thing was just strategy. "
    ki "Though, I will admit that you did taste a little better than I expected you to."

    scene athleticstest25
    with dissolve

    mi "Why was that a thing you expected at all?! Friends don’t lick friends! That’s the kinda stuff that couples do! Probably!"
    ki "Couples don’t really go around licking each other’s faces either, Miku."

    if bonus == True:
        ki "Though, many of them do lick each other in more exciting and interesting ways."
        ki "Want to hear about that? I'll teach you."
    else:
        ki "Hey, wanna hear my impression of the Seinfeld theme?"

    scene athleticstest26
    with dissolve

    mi "Nope! Not listenin’ to this! I know what you’re doin’!"
    mi "You’re playin’ mind games with me cause ya think it’ll get me to cave! But I ain’t cavin, ya hear me?!"
    mi "I won’t let any of your weird adult stuff influence me! I am Miku! Champion of justice and soccer! I will emerge victorious!"

    if bonus == True:
        ki "Hey, how much do you know about blowjobs?"
        ki "Have you ever given one before?"
    else:
        ki "(Mimics bass line)"

    mi "La la la la la la la la! Can’t hear you!"

    if bonus == True:
        ki "You know that some guys actually like it when you use your teeth?"
        ki "I didn’t believe it the first time, but then I-"
        ki "Well, let’s just say I figured out it was true."
        ki "Sorry for bringing that up so randomly. Just got to thinking about it since we were talking about licking and stuff."
        ka "Sensei, can you hear what they’re talking about down there?"
        s "No. But based on Kirin’s posture and Miku’s avoidance, I think it’s safe to make assumptions."
        ka "You don’t think Kirin might be making fun of her or something like that, do you?"
        ka "I know she can be rude at times, but she really likes Miku and-"
        s "I think it’s something else, Karin."
        ka "Something else?..."

    scene athleticstest27
    with dissolve

    if bonus == True:
        ki "Hey...have you ever had an orgasm before?"
    else:
        ki "Hey...have you ever tried skydiving before?"

    ki "You can tell me. I won’t say anything to anybody."
    mi "Die!"
    ki "Is that any way to talk to a friend who’s trying to open up to you?"

    if bonus == True:
        ki "Don’t you wanna hear about my first orgasm? We can compare stories and-"

    mi "Die! Die die die die die die die die!"
    ki "Just thinking about it is kind of making me want to get out of here and..."

    scene athleticstest28
    with dissolve

    ki "Wait..."
    ki "That's weird..."
    ki "My legs are starting to feel all..."

    scene athleticstest29
    with dissolve

    mi "Hehehe...seems to me like your plan may have backfired, Kirin."
    ki "What?! No! Impossible!"
    ki "This was supposed to make you fail! Not me!"
    mi "Mind games are an important part of sports, so I’m proud that ya pulled out a strategy like that."
    mi "Only thing is, sometimes, tryin’ to play mind games with people is a mind game itself."
    mi "And you, Kirin Kanda...are about to lose because of that."
    ki "No! Not like this! I refuse!"
    mi "And...for the record-"

    scene athleticstest30
    with dissolve

    mi "I {i}have{/i}."
    mi "Just once, though."
    ki "Wha-"
    ki "{i}You?{/i}"
    mi "Goodbye, Kirin."
    ki "But...you’re Miku...and..."
    ki "Oh no...I..."

    scene black
    with dissolve2

    ki "AAAAAAHHHHHHHH GOD FUCKING DAMNIT!"

    "………"
    "……"
    "…"

    scene athleticstest31
    with dissolve

    s "And so it appears that this contest goes to the first floor."
    mak "Ha. Of course it does."
    mak "This was perhaps the most one-sided competition of them all. Kirin was absolutely foolish for even thinking she could compete."
    s "Actually, Kirin wound up winning the second round. And almost the third."
    s "Apparently, Miku wound up saying some stuff that caused her to collapse during the planking part."

    scene athleticstest32
    with dissolve

    mak "Miku did? That’s odd."
    u "Oh well...guess I saw this one coming."

    scene athleticstest33
    with dissolve

    u "Luckily for us girls on floor two, you’re about to meet {i}our{/i} secret weapon."
    mak "Otoha is your secret weapon? You really think she’s going to beat Rin in the friend zone fight?"
    s "The what?"
    s "Excuse me, what is this next competition?"
    u "You’ll find out soon enough, Sensei."
    u "You’ll find out soon enough..."

    scene black
    with dissolve2
    stop music fadeout 12.0

    "Uta and Makoto turn away from me without saying anything else and I am left feeling extremely confused and mildly offended by whatever is about to happen next."
    "Everyone remaining in the park gathers their things and starts heading to the cafe as soon as Makoto blows a whistle she was just keeping in her pocket for some reason."
    "I imagine she just carries it everywhere because she is Makoto."
    "Either way, we move through the streets of Kumon-mi as a unit and eventually wind up in front of yet another familiar location."

    $ renpy.end_replay()
    $ dorm1warpoints += 1
    $ dormwar4 = True

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

label dormwar5:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
scene imoutomode25
            with dissolve

            a "Hah! Of course it is."
            a "True love always prevails. But don’t get so down about it, Noriko. I’ve been practicing for this contest since the moment Sensei took me in."
            n "But...I’ve also been kind of like a little sister to you for basically forever."
            n "What did I do wrong?"
            s "Noriko, you literally drugged me."

            scene imoutomode26
            with dissolve

            a "Yeah, there was no way you were going to win after making a move like that. "
            a "A real little sister thinks about her brother’s health before anything else."
            n "I wouldn’t have had to do that if I had gotten to go first! Just...waking him up was a part of my plan and I knew what I gave him was safe and...yeah."

            scene imoutomode27
            with dissolve

            n "This isn’t over, though! "
            n "Ami may have won the little sister contest, but it would have been completely different if we were fighting over who the better girlfriend would be!"
            s "Noriko, I wouldn’t want a girlfriend to drug me either."
            n "I’ll remember that!"

            scene black
            with dissolve

        "Noriko wins":
            $ imoutonoriko = True
            $ dorm2warpoints += 1

            s "The winner of the apparent little sister contest or whatever this was called...is Noriko."

            scene imoutomode28
            with dissolve

            a "What?"
            n "Hell yeah!"
            u "Hell yeah!"
            mak "Are...you fucking insane?"
            mak "Are you really just overlooking what she did?"
            a "…"
            s "No. What she did was inexcusable and it’s a miracle she won with that in mind."

            scene imoutomode29
            with dissolve

            n "Hey, what kind of victory speech is this? I want to be praised and stuff."
            a "…"
            s "The reason Noriko wins is that she just felt like a more authentic little sister to me."
            mak "{i}That{/i} was your idea of authentic? Roleplay like that is arguably the least authentic thing that exists."
            a "…"
            s "It was certainly...a thing. Though, I definitely enjoyed it."
            n "Same. I would have kept going if we weren’t stopped, too."
            a "…"
            s "The thing is, Ami’s portion of the contest was just more of...Ami being Ami."
            a "But..."
            a "But you love me..."
            s "Obviously. But to me, it was like you were just being my [niece] like always and slapping an “onii-chan” sticker on it."
            a "But...I had a whole backstory..."
            s "True, but Noriko actually felt like a different person."
            a "So...I lost because...I’m too good at being your [niece] to be seen as anything else?"
            s "If that’s how you want to rationalize it, sure."
            s "You were both great, though."

            scene imoutomode30
            with dissolve

            a "Well...it feels a little better when you put it like that...but I still don’t like this..."
            n "I wouldn’t worry, Ami. Sensei’s probably always looked at me like a little sister anyway, so my portion of the contest was probably just him living out some fantasy of his."
            s "You know, I can’t say there are any fantasies of mine that involve being drugged."
            n "I’m sure there will be at least {i}one{/i} after this morning, though."
            mak "Let’s just...stop talking about this contest altogether and move on..."
            mak "I absolutely can not be the only person extremely uncomfortable right now."
            a "For once, I actually agree with Makoto."
            a "Let’s just get dressed and...walk to the park..."

            scene black
            with dissolve

    "Makoto and Uta head out before the rest of us so they can relay the results of the match to their teams."
    "I’m ready before Ami and Noriko are, but I still decide to wait for them near the front door so we can all walk to the park together."
    "I’m sure it would be significantly more awkward if it were just the two of them, so I’m hoping my presence is able to quell some of the unease."
    "It’s not really easy to just choose between two girls you like, especially when you know how sensitive both of them are."
    "But it’s still just a game at the end of the day. And I’m sure that the result of this match won’t have any long lasting effects on their relationship."
    "Or my relationship with them, for that matter."
    "They’ll both continue to be head over heels in love with me-"
    "And I will continue to absorb their feelings until there is nothing left of them."

    $ renpy.end_replay()
    $ dormwar3 = True
    stop music fadeout 5.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    jump dormwar4
...
```