# Love, Dorms, and Other Things
Kirin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirindorm10&go=Go)



## Event preconditions
✅Kirin love greater than or equal to 10

✅Event "[Main: What Was](./day271.md)" is completed (event=day271)

✅Day of week is not Wednesday

✅Event "[Uta: The VIP Treatment](./utadorm5.md)" is completed (event=utadorm5)

✅Event "[Io: Unnamed Wooden Robots](./iodorm5.md)" is completed (event=iodorm5)



## Next events
* [Kirin: Flickering Spotlight](./kirinsoccer15.md)
* [Noriko: Semi-Constructive Criticism](./norikodorm5.md)

## Event properties
* ID: kirindorm10
* Group: Kirin
* Triggered by label: kirindorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label kirindorm10:
    play sound "knock.mp3"

    "I knock on Kirin’s door and wait for her to answer."
    "It’s a little strange being able to do that after getting so used to just calling her every time I want to see her."
    "But the fact that she’s here now makes my life exponentially easier since this is already my second house."
    "Kirin and I are basically roommates now."
    "…"
    "Come to think of it, who {i}is{/i} her roommate?"
    "It has to be Noriko, right?"
    "Either that or she’s just living by herself in here- which would be extremely depressing."
    "But I guess if anyone was going to live alone out of the class it would be Kirin."
    "Or Yumi."
    "Or Maya."
    "…"
    "Actually, I have a lot of independently “functioning” girls in my class, now that I think about it."

    ki "Oh! Noriko, I think this is it. Could we be receiving our first ever visit from Sensei?"
    n "The first of many, dear Kirin. "
    n "Have you prepared the handcuffs?"

    if bonus == True:
        ki "I don’t believe handcuffs will be necessary. He seems like the type to willingly tie himself to the bed if it means getting to “hang out” with us."
        s "Stop accurately characterizing me from behind the door and let me in."
    else:
        s "Ooh! Are you guys fighting crime in there?!"
        n "We are pretending to!"
        ki "It is to prepare for when we are policewomen."
        s "I want to see!"

    ki "It’s open! Just walk in if you’re so impatient."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I turn the handle and, lo and behold, the door {i}was{/i} open after all."
    "I don’t know why I ever expect any less at this point."
    "And if this particular door isn’t locked now, I can’t imagine it ever will be in the future either. So that's cool, I guess."
    "Also, am I wrong for thinking that Dorm 10 seems like it could be a little more...intense than most of the others if these girls’ personalities mesh as well as I expect them to?"

    scene firstkirinnorikodorm1
    with dissolve

    ki "Welcome to our humble abode. May I take your coat?"

    if bonus == True:
        n "May I take your pants?"
        s "I'm already being stripped on my first trip here?"
    else:
        n "Please turn around so I may gently pat you down and confiscate any weapons you may have."
        n "Is there anything in your pockets that is going to poke me, stick me, or stab me?"

        "I start to cry because I am scared."

        n "Oh no. Have I made an error?"
        s "You did great. I am just a wimpy boy who didn't think it worked like this."
        n "That is fine. But I still need to pat you down."

    ki "Is that not how this normally goes?"
    ki "Sorry, just a little unfamiliar with the process."
    n "I just really like your pants."
    s "..."
    s "I take it you two have been getting along well?"

    scene firstkirinnorikodorm2
    with dissolve

    ki "Almost a little {i}too{/i} well."
    ki "It’s really convenient that we both happened to transfer in on the same day. "
    ki "Even if Noriko totally stole the spotlight and made my introduction seem super boring by comparison."
    n "The trick is to make everyone hate you on the first day so things can only go up from there."
    ki "And here I was thinking that getting people to dislike you should be more of a slow burn."

    scene firstkirinnorikodorm3
    with dissolve

    ki "So, what do you think? Pretty nice place, huh?"
    ki "We spent the whole day decorating it. And after seeing some of the other girls’ rooms, I think ours is among the best."
    n "By among the best she just means the best."
    ki "Yes. Yes, I do."
    ki "But after seeing the garbage dump that is Uta and Io’s room, it’s not like our competition is really all that strong."
    s "It’s a competition now?"
    ki "Everything is a competition, Sensei."
    ki "Love...dorms...pretty much every aspect of life becomes a battle when you put a bunch of like-minded girls in one place and tell them only one can survive."
    s "Who told you that only one of you is going to survive?"
    ki "I just can’t see this ending any other way."

    scene firstkirinnorikodorm4
    with dissolve

    "I step between Kirin and Noriko and begin to observe what I imagine is Kirin’s side of the room. "
    "I’m not exactly sure what I was expecting, but it’s definitely more well put together than I imagined it would be for someone who hasn’t had their own room, well, ever."
    "I wonder if all of those years of wanting to get out are what gave her the power to make this place...livable?"
    "Unlike the garbage dump that is Uta and Io's room."
    "I feel a little bad for adding to the insult, but...come on."
    "How could the two of them ever let that happen?"

    scene firstkirinnorikodorm5
    with fade

    ki "Does it live up to your expectations, Sensei?"
    s "I’m just glad you aren’t also a trainwreck."
    ki "I consider myself more of a calculated disaster."
    ki "The same appeal as a trainwreck where you don’t want to look away, but with significantly less shredded metal and all of that other morbid stuff."
    s "That is a strangely specific way to describe yourself."
    ki "That’s not my description. It’s Noriko’s. "
    s "Really?"
    s "I’m not one to judge how people get to know each other, but-"

    scene firstkirinnorikodorm6
    with dissolve

    s "Oh."
    s "You are very close."
    n "Am I?"
    s "You’re not actually blind, are you?"
    n "Blinded by your beauty, Sensei."
    s "First, please don’t call me beautiful."
    n "Noted."
    s "Second, are you sure it’s okay to be calling your new roommate a-"
    n "Calculated disaster? Yes."
    ki "Yeah, I really don’t care."
    ki "Noriko’s not “all there” herself, so the two of us can just put our minds together and create one socially acceptable human being. "

    scene firstkirinnorikodorm7
    with dissolve

    ki "Two for the price of one sounds pretty good, right?"
    s "Always."
    s "I just don’t want to leave this room thinking you’re on good terms just to find out that one of you killed the other one in their sleep the next day."
    n "Why does everyone always think I’m going to kill someone in their sleep?"
    ki "Probably the pocket knife and crazy eyes combo."
    n "Crazy eyes? Are my eyes crazy?"
    ki "Yeah, but they work for you. It’s cute. "
    n "Awwwww, Kirin~"

    scene firstkirinnorikodorm8
    with dissolve

    if bonus == True:
        ki "So, when did you want to fuck me?"
    else:
        ki "So, when did you want to hug me?"

    s "…"
    ki "…"
    s "Uhh..."
    ki "What’s up?"
    s "I don’t know if it’s safe for me to answer that question with Noriko directly behind me."
    s "You literally just mentioned her pocket knife and crazy eyes."
    ki "It’s fine. Noriko and I made a pact."
    s "A pact? What kind of pact?"

    scene firstkirinnorikodorm6
    with dissolve

    if bonus == True:
        n "Kirin gets to have your dick and I get to have your heart."
        n "And also your dick."
    else:
        n "Kirin gets to hug you and I get to also hug you."
        n "But I will hug you better."

    n "We laid ground rules when we moved in together."

    if bonus == True:
        n "I can’t say I’m fond of the prospect of you fucking my friend in my room, but I’ve already come to terms with you fucking my sister, so one more won’t hurt as long as there are no feelings involved."
        n "Also, there won’t be any issue at all since I’m sure you’ll only want me in due-time anyway."

    s "This dorm room is weird."
    ki "Hey! Eyes over here, Sensei."

    scene firstkirinnorikodorm9
    with dissolve

    ki "You stand on my side of the dorm, you talk to {i}me{/i}. Got it?"

    if bonus == True:
        s "Sorry. I’m just realizing this is the closest I’ve been to a threesome inside of the dorms and it's making it hard to focus."
        n "Oooooh! Everyone wins with a threesome! We can all live happily ever after~"
    else:
        s "Sorry. I just got a little excited when hugs were brought up."

    scene firstkirinnorikodorm10
    with dissolve

    s "So these, uhh...”ground rules” you two worked out-"
    ki "What about them?"
    s "Is there anything I need to know?"
    s "Like, who gets me on Thursdays, for instance?"
    ki "What, do you think Noriko and I are a divorced couple fighting for custody of our child or something? "
    ki "It’s nothing like that."

    if bonus == True:
        ki "We just need to be courteous to each other and not screw around while the other is in the room."
        s "That is going to make the threesome very difficult."
        n "Maybe we can set up like, a divider in the middle of the room and you can just walk to the other side after three or four thrusts?"
        ki "Not counting future threesomes, obviously. But it’s not like we’re just going to jump into that right away, you know?"
        s "I’m getting mixed signals here and I’m not sure what I should expect moving forward."
        n "Kirin wants to lose her virginity like any other dignified lady- bent over a vibrating bed in a love hotel."
    else:
        ki "We just need to be courteous and respectful to each other or the dorm will fall into disarray and tear us apart."
        n "The best way to stay on good terms is to respect each other's boundaries and maybe pat each other on the back every once in a while."

    scene firstkirinnorikodorm11
    with dissolve

    ki "Oh, that actually sounds pretty neat. Thanks, Noriko."
    n "I gotchoo, girl."

    if bonus == True:
        s "This is the first time I’ve ever heard someone call losing their virginity “neat.”"

    scene firstkirinnorikodorm12
    with dissolve

    ki "Sooooo, yeah. That’s basically the only major ground rule."

    if bonus == True:
        ki "Oh, and I also promised to never start feeling anything more than sexual attraction toward you but, let’s be real...me actually “liking” someone?"
        ki "That’s just not possible."
    else:
        ki "Oh, and I also can't enjoy the hugs. But like...let’s be real...me actually “enjoying” something?"
        ki "That’s just not possible."

    s "Are you sure about that?"

    if bonus == False:
        s "I am a very good hugger and you may wind up liking it more than you expect once I really start trying."

    scene firstkirinnorikodorm13
    with dissolve

    ki "Of course I’m sure about that. Why wouldn’t I be?"
    s "It just seemed like you might have been actually starting to, you know, {i}feel{/i} something the other day when you told me about transferring in."

    scene firstkirinnorikodorm14
    with dissolve

    if bonus == True:
        ki "That was just a weird day! All I feel is horny!"
    else:
        ki "That was just a weird day! All I feel is hungry!"

    n "Like, right now?"

    scene firstkirinnorikodorm15
    with dissolve

    ki "No! Not right now, Noriko! I meant in general!"

    if bonus == True:
        ki "I am a generally horny person who has no interest in actual romance!"
        n "Okaaaaay~ But you know what happens if you break the contract~"
        s "Wait, yeah, what happens if she breaks the contract?"
    else:
        ki "I am generally hungry!"
        n "You are on a diet, Kirin. Remember what you told me to do if you start breaking it."
        s "Wait, what happens if Kirin breaks her diet?"

    scene firstkirinnorikodorm16
    stop music

    n "I get to dissect her."
    s "…"
    n "…"
    s "…"
    n "…"
    s "…"
    n "…"

    scene firstkirinnorikodorm17
    with dissolve
    play music "sweetvermouth.mp3"

    ki "So, yeah. That’s how things stand."

    if bonus == True:
        ki "We can fuck each other, but we’re not allowed to feel anything on an emotional level or Noriko gets to cut me up."
        n "I believe the technical term is “friends with benefits.”"
        n "Meanwhile, I’m the “childhood friend slash imouto” type."
        n "So not only am I caring and adorable like a little sister, I have years worth of pent up sexual aggression and curiosity all aimed right at you!"
        ki "And obviously I can’t compete with that."
        s "…"
    else:
        ki "We can hug each other, but I am not allowed to enjoy it. It will be nothing but disgruntled, angsty hugs."
        s "I want to hug you right now from hearing that but I am afraid you would like it."
        s "It is so sad that you must live this way. How could Noriko do this to you?"

    scene firstkirinnorikodorm18
    with dissolve

    ki "It’s like...totally fine this way! I wouldn’t have agreed otherwise."
    ki "Now, can we just move onto something else?"
    ki "I feel like you’re trying to get me to second guess my instincts. And my instincts are exactly why I’ve managed to get as far as I have."
    s "And how far is that exactly?"

    scene black
    with dissolve

    "Kirin hops off of the bed and makes her way over to her desk, swiping a can off of it and taking a sip of some fruity-smelling energy drink."
    "There are several of the same exact cans strewn across the room, and it makes me question how much of tonight’s conversation has been sincere and..."
    "How much has been fueled by sugar and caffeine."

    scene firstkirinnorikodorm19
    with dissolve

    ki "Listen, I don’t know if you’re just trying to make me second guess myself, but I’m totally okay with things playing out like this."
    ki "It’s how it {i}should{/i} be and it’s exactly what I {i}want{/i}."

    if bonus == True:
        ki "If anything, I should be happy that I met Noriko so I don't wind up falling into that weird harem thing you’ve got going on."

    scene firstkirinnorikodorm20
    with dissolve

    n "And I should be happy I met Kirin because I am going to shatter your harem and make you love me and only me."

    scene firstkirinnorikodorm21
    with dissolve

    n "Also, she has a cute butt."
    ki "Uhh...thank you?"
    n "Squeeeeeeeze~"
    s "Do you two need some time alone?"

    scene firstkirinnorikodorm22

    ki "I have no idea."
    n "We do, but it doesn’t involve butts. "
    ki "I am mostly relieved, but also mildly disappointed to hear this news."

    if bonus == True:
        s "Same."

    n "I just want to talk to her a little more about our contract thingy and make sure we’re both okay with the terms and conditions."
    s "Ah. Well I should probably be heading back now anyway."

    if bonus == True:
        s "It’s getting late and becoming more apparent by the minute that there will be no threesome tonight."
    else:
        s "It's past my bedtime and I am a sleepy boy."

    n "Does that make you sad?"
    s "Sadder than you could ever imagine."
    n "I see, I see."

    scene firstkirinnorikodorm23
    with dissolve

    ki "Thanks for dropping by, though. "
    ki "I’m sure you’ll be here pretty often in the future, so...until next time, I guess?"
    s "Yup. Until next time it is."

    scene black
    with dissolve2

    "I say goodbye to the two of them and exit the dorm room, still slightly confused about the Kirin-Noriko character dynamic."
    "It {i}seems{/i} that they get along, but I can’t help but feel like Kirin may have prematurely agreed to something she wasn’t exactly 100%% behind."
    "Granted, she also seems like the type to easily trick herself into thinking she doesn’t want something she actually does-"
    "So I guess she’ll be fine no matter what happens."
    "I wish I was that good at manipulating my own thoughts."
    "But I guess it’s just as beneficial to be gifted enough to manipulate others."
    "…"
    "I’m looking forward to the time I’m going to spend in that room."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirindorm10 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kirindorm15:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label kirindorm:
    if kirin_love >= 10 and day271 == True and day != 3 and utadorm5 == True and iodorm5 == True and kirindorm10 == False:
        jump kirindorm10
...
```