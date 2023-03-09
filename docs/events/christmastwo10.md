# Walking on Eggshells
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo10&go=Go)


Part of event chain [The Other Half](./kirinlust202.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo10
* Group: Main
* Triggered by label: kirinlust202scenex

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo10:
    scene ioxmashall1
    with dissolve2
    play music "closeto.mp3"

    "When we exit the boiler room, someone is there."

    if kirinlust202 == True and bonus == True:
        "And, unfortunately, it’s someone perceptive enough to understand the implications of two people emerging from the dark together- one still red in the face from over exerting herself during a titjob."
        "I’m beginning to think I should have rented that extra room after all."
    elif kirinlust202 == True and bonus == False:
        "And, unfortunately, it’s someone perceptive enough to understand the implications of two people emerging from the dark together."
    else:
        "And, unfortunately, it’s someone perceptive enough to understand the implications of two people emerging from the dark together."
        "Nothing happened, though."
        "Which I’m sure is hard to believe since it was Kirin and me, but..."
        "It’s the truth."
        "And now I’m burdened with having to prove that."

    i "..."
    ki "Oh, it’s Io. Hi."
    i "Uh...just for my own curiosity...what were you two doing in there?"
    s "Just getting away from the party for a bit. I’m sure you know what it’s like."

    "I try to appeal to her in the only way I know how- by making everything sound unbearable and irritating."

    i "..."
    s "Io?"
    i "Oh. Uhh...yeah. That’s why I’m out here too. Cause...it was irritating and..."
    i "I’m sorry, why were you in there again? I don't think I properly registered your answer just now."
    i "I understand getting away from everyone, but not the whole “retreating into a boiler room” part."
    ki "Have you stopped and thought that maybe it was just like, extra quiet in there?"

    scene ioxmashall2
    with dissolve

    i "Can you do me a favor and just like, not talk for a second? Because I kind of don’t care at all about your side of the story."
    ki "Jeez, fine. It’s not like Sensei’s side is gonna be any different, though, since we were clearly in there {i}together.{/i}"

    scene ioxmashall3
    with dissolve

    i "Do you like her? Even after what she said about my robot? Why?"
    ki "Robot? What robot? What are you talking about?"
    s "I don’t {i}like{/i} her, Io. We were just hanging out."
    i "Yeah, but...this is the second time I’ve found you {i}hanging out{/i} with someone in private while everyone else is like, less than a hundred feet away."
    i "Are you dating {i}her{/i} now too?"
    ki "Wait, are you and Ayane official, Sensei?"
    i "{i}And{/i} Ayane? Is that why you stuck up for her back then?"
    s "I’m not dating anyone. And I think you might be forgetting that I was with {i}you{/i} in private the first time you caught wind of me with anyone. It wasn’t the other way around."

    scene ioxmashall4
    with dissolve

    i "I know I’m probably overanalyzing things again right now, but it’s kind of hard {i}not{/i} to when I go out to look for you and find you in a private room with a girl who clearly just wants to-"
    s "You {i}are{/i} overanalyzing things. And I’d appreciate it if you’d let me talk to you without jumping down my throat."
    i "I really wish I could but it’s kind of hard to stop talking when I get scared like this, Sensei! How many more girls are in front of me in the line?!"
    i "I said I was fine with doing a little pulling but I didn't think I'd be playing tug of war against the entire class all by myself."
    s "What, then? Am I just not allowed to talk to anyone else without the risk of upsetting you?"
    i "You’re allowed to do whatever you want! I told you that!"
    s "Then stop freaking out whenever I do."

    scene ioxmashall5
    with dissolve

    i "I..."
    i "I just wanted to spend time with you...that’s all."

    scene ioxmashall6
    with dissolve

    ki "Well, hey! If you’re looking for a good place, might I recommend the boiler room?"
    ki "It might not sound appealing at first, but I can guarantee you there’s plenty of room in there to do all kinds of stuff."
    i "I...didn’t mean that kind of-"
    s "You’re not helping, Kirin."

    scene ioxmashall7
    with dissolve

    ki "Obviously. But if Io’s going to show up and start freaking out on you for just hanging out with me, I think it’s only fair to toss a little passive aggression back her way."
    i "It’s...because of the context..."

    scene ioxmashall8
    with dissolve

    ki "What context? That the two of us came out of some sketchy room together when no one else was around? That context?"
    i "I...should just leave."
    ki "Yeah, you probably should."
    s "You don’t have to leave, Io..."

    scene ioxmashall9
    with dissolve

    i "I was actually getting ready to leave anyway! I just wanted to come say...Merry Christmas to you on the way out..."
    i "There are too many people here and there’s just...too much to listen to and it’s really messing me up."
    i "And I know you don’t care about this and probably just want to go back to spending time with Kirin for whatever reason, but I wanted you to know that."
    i "You and me can...do something for Christmas next year instead. I’ll still be around, you know. I’m not going to give up on you just because basically every other girl in school is-"
    ki "Damn. You’ve got it really bad, huh?"

    scene ioxmashall10
    with dissolve

    i "Huh?"
    ki "For Sensei. Like...how into him are you on a scale of one to ten?"
    i "Maybe like a...nine? Ten? Eleven? Am I allowed to go past ten?"
    ki "Why, though?"
    i "What do you mean why? Why do you care?"
    ki "I just want to know what you see in him. That’s all."

    scene ioxmashall11
    with dissolve

    i "He..."
    s "..."
    ki "...Well?"
    i "He makes me feel...comfortable..."

    scene ioxmashall12
    with dissolve

    ki "Sensei does? Seriously? Are you on drugs or something?"
    i "Multiple, actually. But they’re all legal and prescribed, so it’s kind of like I’m not on drugs at all."
    s "I don’t think I make you comfortable, Io."

    scene ioxmashall13
    with dissolve

    i "You really do, though! I mean it!"
    s "Then why are you always freaking out around me? If you’re comfortable, you should be acting...I don’t know, more comfortable."
    i "Because my brain is broken, Sensei!"
    i "I don’t have any impulse control and I’m afraid you’ll leave me for a girl more willing to put out than I am!"
    i "Not that you’re {i}with{/i} me at all in the first place! I mean, why would you be? I’m the absolute worst."
    i "But I really really really like you and I can’t hold it back and the thought of you with anyone else, though well within your right, makes me want to build another wardrobe that I can crawl inside of and die."
    ki "Have you considered...oh, I don’t know- putting out?"
    ki "If that’s what you think Sensei wants, why not offer it up and see if he takes the bait? Sure beats dying in some random wardrobe."

    scene ioxmashall14
    with dissolve

    i "Because...that’s not the way I..."
    s "You don’t have to explain yourself to her, Io. And you don’t really have to explain yourself to me either."
    s "I fully expect you to keep doing that, though, since you’d probably have a nervous breakdown without putting yourself down at least once every ten minutes."
    i "I’m on the brink of having a nervous breakdown right now and I’ve repeatedly insulted myself throughout this conversation."
    s "Are you going to do that every time you see me with somebody else?"
    i "You mean every time I encounter you either hooking up or {i}finishing{/i} a hookup? Probably."
    s "That’s-"

    scene ioxmashall15
    with dissolve

    ki "Okay, Io? Listen."
    i "P-Please don’t touch me! I’ll listen to whatever you have to say, just..."
    i "Don’t do that..."

    scene ioxmashall16
    with dissolve

    ki "Oh. Uhh...okay."
    ki "I was just going to say that even if Sensei and me {i}were{/i} hooking up, it wouldn’t like, fuck up your chances with him or anything."
    ki "I’m not, like, dating material or whatever. And I don’t have any interest in romance at all."
    s "That sort of thing might work on Noriko, but I don’t think it makes much of a difference to Io."
    s "She’s made it clear, almost painstakingly so, that she wants me to want her and no one else."

    scene ioxmashall17
    with dissolve

    i "Is that...really so bad?"
    s "Not until it starts ruining other relationships I have."
    ki "I mean...this didn’t ruin shit for me. I’m kind of used to being around people who want to spend the rest of their life with you or whatever other sappy bullshit they’re always saying."
    s "Sure, but you’re kind of like an inverse Io where you’re always pointing out your flaws and embracing them rather than letting them consume you."

    scene ioxmashall18
    with dissolve

    ki "See? I told you we’d make good friends."
    i "Uhh...no. I’m still going to pass."

    scene ioxmashall19
    with dissolve

    s "Io, I know in whatever world you’ve dreamt up for yourself that you’re this...irreparable trash heap completely immune to changing-"
    s "But you’re going to {i}have{/i} to change if you ever want to make it through even an hour without having a self-deprecative emotional breakdown."
    s "It’s extremely exhausting sometimes. All I did was walk out of a room and you looked like you were about to shatter into a million pieces."
    i "I really felt like I was going to, though."
    s "That’s exactly the problem. Do you really think I’m going to want to be around you more if I have to constantly walk all over eggshells just to get to you? No. Of course not."
    i "Then I’ll...build a bridge over them or something! It’s not like I {i}want{/i} to be impulsive and clingy and annoying! I just am! I warned you about this!"
    s "And I’m pretty sure I’ve warned you that I’m not going to completely drop everything else other than you just to make you comfortable."
    s "I think this is one of those times where you’ll just...kind of have to be uncomfortable."
    s "I told you nothing happened. You can either believe me or not believe me. That’s up to you."
    s "But don’t just get all accusatory again if this happens in the future. Actually, not {i}if{/i}. When."
    s "If you can promise me you’ll at least {i}try{/i} to do that..."
    s "Then I guess I can promise you I’ll at least {i}try{/i} to take you to an amusement park some day."

    scene ioxmashall20
    with dissolve

    i "Uhhhhh...I’m sorry, what?"
    i "I don’t know if it’s just more of that make believe world of self loathing you were alluding to earlier playing tricks on me, but I’m pretty sure you just jumped from scolding me to making my dreams come true."
    s "I haven’t done anything yet. And to be honest, I don’t even like amusement parks."
    s "But if taking you to one is enough to maybe motivate you into not being so neurotic all the time, I can deal with it."
    i "I mean...I {i}love{/i} the idea. But I’m not exactly sure how possible it is for me to change at this point since I’m so set in my ways."
    ki "Do I get to come to this amusement park or is this just like a...G-rated boiler room kinda thing for the two of you?"
    s "The latter. Do we have a deal, Io?"

    scene ioxmashall21
    with dissolve

    i "Yes, but...like I said, I don’t know if I’ll be able to follow through on it. I’m notoriously bad at changing and...communicating and...pretty much everything that doesn’t involve my hands."
    ki "There’s a joke to be made here, but I’m pretty sure this isn’t the time."
    s "It’s not. We’ve already been out here way too long."
    s "We should probably be getting back to the party now before anyone thinks all {i}three{/i} of us were in the boiler room together."
    ki "Hot. And not just because it’s, like...a boiler room."
    i "..."
    s "..."

    scene ioxmashall22
    with dissolve

    i "Okay...I’m going to just...go back to the dorm now."
    i "It’s probably a bad idea for me to stick around when I can’t get my mind into the right place anyway."
    s "Are you sure? Because I’m pretty sure Uta is going to get upset about that."
    i "Uta will live. She’ll have more fun without me anyway."
    ki "Let me come with you."

    scene ioxmashall23
    with dissolve

    i "Uhh..."
    i "No?..."
    ki "Why not? I’m bored as shit here and was probably going to wind up going home anyway."
    i "Because I don’t like you? I thought I made that pretty clear throughout the course of this conversation."
    ki "So what? I hang out with people I don’t like all the time."
    ki "It’s also dark and we’re less likely to get assaulted if we’re not alone."
    s "That’s...actually a surprisingly decent reason, Kirin."
    ki "Yeah well, I’m a surprisingly decent person sometimes."

    scene ioxmashall24
    with dissolve

    i "Will walking home with Kirin bring me one step closer to the amusement park?"
    s "It’s a start. Just don’t kill her on the way home. I’d be the last one to see you two together and I really don’t want to be questioned by the police."

    if kirinlust202 == True and bonus == True:
        "Especially not with my semen still in Kirin’s system."

    scene ioxmashall25
    with dissolve

    i "Then...fine. But I’m probably going to either just ignore you or say a bunch of annoying shit that’ll make you think less of me as a person."
    ki "I don’t know if anything I say will be annoying, but I can definitely see some of it leading to the whole “less of a person” part as well."
    s "Well...enjoy your walk home, then."
    s "I’m going to go try and explain to everyone why I disappeared for so long shortly after getting here."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I watch Io and Kirin leave the hotel together- an outcome I would not have expected based on the first part of our run-in tonight."
    "And while I’m not sure if they’ll still {i}be{/i} together by the time they make it back to the dorm, I'm a little proud of Io for at least trying."
    "And I’m proud of Kirin for miraculously not managing to make anything worse this time around."
    "I just hope that this isn’t a one-off situation and that the two of them can maybe learn something from this."
    "What they’ll learn exactly, remains to be seen."
    "But I’m sure that whatever future comes will be better than the ones they would have found here."
    "Neither of them are suited for places like this."
    "But, then again, neither am I."
    "I say this as I make my way back into a room I don’t belong in."
    "........."
    "......"
    "..."

    scene ioxmashall26
    with dissolve2
    play music "stpartynight.mp3" fadein 3.0

    a "Sensei! I’m going to ignore the fact that you were gone for so long and jump straight to asking if you heard me sing or not!"
    s "I did. It was very impressive, Ami."
    a "Yeah?! Do you think Niki would be proud?!"
    s "Sure. Why not?"
    m "Where have you been?"
    s "With Kirin and Io outside of a boiler room. It’s a long story."
    m "That’s...certainly a combination of characters."
    ka "Io? Who is that?"

    scene ioxmashall27
    with dissolve

    a "She’s another girl in our class, but she never really talks to anyone, so you probably didn’t know she existed."
    ka "And she’s...friends with Kirin?"
    a "I...don’t think so? At least I’ve never really seen them together before."
    s "I wouldn’t say they’re friends, but they're walking back to the dorms together now, so at least that’s a thing."

    scene ioxmashall28
    with dissolve

    ka "Kirin left? Why? She was supposed to walk back with me tonight. I would have left early if I knew she wasn’t having fun."
    a "You can leave with us instead, Karin. You spend more time hanging out in our group anyway."
    m "Does them leaving have anything to do with what may have happened outside of this boiler room thing?"
    s "Maybe. Maybe not. Anyway, what have you guys been up to?"

    scene ioxmashall29
    with dissolve

    ka "Well...I was worrying about why you and Kirin left together...but I feel kind of...really stupid for that now..."

    "I subconsciously thank Io for showing up and becoming a part of my alibi, even if she almost broke down in the process of doing so."

    m "That seems like a plausible thing to worry-"
    s "And you, Ami?"
    a "Oh, you know. Just singing and...waiting for you. So basically what I’m always doing, but with more of a Christmas vibe."
    a "Have you eaten anything yet? We ordered a million more cakes for the party since we finished everything at our house last night."
    s "I’m assuming “we” means Maya?"

    scene ioxmashall30
    with dissolve

    m "I regret nothing."
    ka "I also...b...baked one if you want to try that, Sensei!"
    ka "Actually, nevermind! Don’t! I’m sure the others are better! Hahaha!"
    s "Karin, why are you laughing about that?"

    scene ioxmashall31
    with dissolve

    ka "I have no idea! Hahahahaha!"
    m "So, do you intend to stay in this room for the rest of the party? Or are you bound to go wandering around again?"
    s "Worried you’ll miss me too much if I leave?"
    m "Quite the opposite, actually. I’m trying to plan my night so I see as little of you as possible."

    "It’s really amazing how she can still pretend she hates me this much even after starting to let the truth slip out."
    "But I guess she has plenty of experience after all those years of hating other iterations."
    "Or...other versions of this same iteration?"
    "I still have no idea how it works. I’m just glad to be sentient right now."

    s "I’ll probably stick around for a little while, get pulled into some drama, come back, get pulled into more drama, and then bump into you on the roof or something."
    s "That’s how things normally go, at least."

    scene ioxmashall32
    with dissolve

    m "Joke's on you. The roof here is closed."
    a "Roof? When did you try to go to the roof?"
    a "Is this about stars again? You know you can take a break from stars on Christmas, Maya. They’re not going anywhere."

    scene ioxmashall33
    with dissolve

    m "Thank you, Ami. This changes everything. All this time, I was under the impression that they were just going to disappear."
    m "I can now celebrate Christmas like the normal [teenage]girl I am. Hooray."

    scene ioxmashall34
    with dissolve

    a "You don’t have to be a jerk about it, you know..."

    scene black
    with dissolve2

    "{i}Meanwhile...{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo10 = True

    jump christmastwo11

label christmastwo11:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
s "Do you want me to apologize for being too large or something?"
    ki "Fuck no I don’t. Seeing the size difference just makes me like you even more."
    ki "To think you’re willing to share something this amazing with someone like me...letting you fuck my tits is the {i}least{/i} I can do."
    s "Well, you’re...doing a damn good job with what little there is to work with..."

    scene kirinxmanhall21
    with dissolve

    ki "Yeah?...How good, [kirinmaster]?"
    ki "Tell me I...can make you feel...better than anyone else does..."
    s "Well...I’d kind of have to get a side by side comparison to-"
    ki "Then just fucking lie to me. I don’t care if it’s true or not. I just want to hear it."
    s "..."
    s "You’re...the best, Kirin..."
    ki "Mm...[kirinmaster]...thank you..."
    ki "I worked so hard...I worked so hard just...so I could please you..."
    ki "Does that make you happy, [kirinmaster]? Knowing I spend...so much of my free time...fantasizing about your thick cock?"
    ki "Fantasizing about...all of the different ways to make it-"
    s "Sorry to cut you off, but I’m about to cum."

    scene kirinxmanhall19
    with dissolve

    ki "Woah, already? I really {i}am{/i} good at this, huh?"
    s "It must have been the hairbrush."
    ki "Wanna do it in my mouth? I’m already right here so we might as well."
    s "Yes."
    ki "Great, so-"

    scene kirinxmanhall22
    with dissolve

    s "And down you go."
    ki "Mm! Mmn...mnch..."

    "Knowing that I’m only a few moments away from ejaculating, I slide Kirin’s mouth onto my cock and begin slightly thrusting into her."
    "She jerks me off in response, opening as widely as she can so I can move in and out without any resistance."
    "The heat of her mouth is much different than the warmth I was experiencing just moments ago and is exactly what I needed to finish the job."
    "I probably {i}could{/i} have cum from just the titjob alone but, frankly, I find this a lot more satisfying."

    scene kirinxmanhall23
    with dissolve

    ki "Mm...mlem...mnch~!"
    ki "Mmf...[kirinmaster]...do it..."
    ki "Do it...I’m...mnch...tired of...waiting..."

    "Kirin decides to quit leaving her mouth open for me to do all of the work and begins taking things into her own hands."
    "She massage the underside of my shaft with her tongue, doing her best to try and curl it around my shaft, but mostly failing due to the massive size disparity between the two organs."
    "I get lost in that thought for a moment."
    "How much bigger I am than her."
    "How easy it would be to take everything from her if she was not already willing to-"

    play sound "static.mp3"
    scene treefall1 with flash
    scene imissyou12 with flash
    scene whygodwhy with flash
    scene kirinxmanhall24 with flash
    stop sound

    ki "Mmnnngh!!~~~~~~~"

    "Before I know it, I’m filling Kirin’s mouth with cum, but..."
    "I..."
    "I kind of stop feeling anything?..."
    "It’s hard to describe."
    "So I won’t."

    scene black
    with dissolve2

    ki "Pah~"
    ki "Fuck...that was...intense..."
    ki "Kinda...forgot to breathe there...for a second...whoo~"
    ki "Gotta...catch my...breath..."
    ki "So...did you-"
    s "We should start heading back to the party."
    ki "Hah...ah...huh? Already?"
    ki "Don’t you want to...hang out for a little while longer or something?..."
    s "We can hang out back in the room. I just feel weird being stuck somewhere as dark as this."
    ki "Huh...I figured you of all people would like the dark."
    ki "Sure. We can go back."
    ki "Just...give me a minute to make sure I’m totally cum-free first."

    "Kirin takes a moment to get situated and fan herself off."
    "Then, after making sure she is “cum-free,” she gives me the green light and the two of us move back up the stairs."
    "The sound of the machinery follows us."
    "The scent gets stuck in my nostrils."

    $ renpy.end_replay()
    $ kirin_lust += 1
    $ kirinlust202 = True
    stop music fadeout 6.0

    "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo10
...
```