# Self-Medication
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar30&go=Go)



## Event preconditions
✅Sana love greater than or equal to 30

✅Event "[Sana: The Girl in the Black Dress](./sanadorm25.md)" is completed (event=sanadorm25)

✅Event "[Main: Girl Talk Pt. II](./day120.md)" is completed (event=day120)



## Next events
* [Sana: Tortoises and the Concept of Friendship](./sanadorm30.md)

## Event properties
* ID: bar30
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label bar30:
    scene sanadrunkagain1
    with fade
    play music "calmbar.mp3"

    sa "Hey...*hic* you..."
    sa "Whatchadoin’here?"

    "I arrive at the bar to find an unexpectedly inebriated Sana."

    if bonus == True:
        "Typically, things like drinking in your own workplace are frowned upon, especially for a [high_school]er..."
    else:
        "Typically, things like drinking in your own workplace are frowned upon, especially for a college student..."

    "But I guess given the nature of this establishment, it’s not too unusual."
    "I’m sure her mother was doing the exact same thing at her age."

    scene sanadrunkagain2
    with dissolve

    sar "Sensei! How dare you get my daughter drunk while I wasn’t watching!"
    s "Wait, what? I literally just got here."

    scene sanadrunkagain3

    sar "I know that, silly. I’m just messing with you."
    sar "We closed early tonight because Sana wasn’t feeling great."
    sar "Sooooo I gave her the only medicine that’s ever worked for me."
    s "You medicated your daughter with alcohol?"

    scene sanadrunkagain2

    sar "Well it worked, didn’t it? Look at her! She’s just peachy!"

    scene sanadrunkagain4
    with dissolve

    sa "Hey...ya ever think’ that...there’s more to life than just...all the things you do in life?"
    s "What does that even mean?"
    sa "Itmeanseverything."

    scene sanadrunkagain3
    with dissolve

    s "Are you positive that all she’s had is alcohol? She seems a little too far gone for that to be true."
    sar "She just needs to build up her tolerance. She might be my daughter but it’s not like she was born with an iron stomach."
    s "Is it even your stomach that processes alcohol?"
    sar "Beats me. You’re the teacher here."

    scene sanadrunkagain4
    with dissolve

    sa "Sensei...I’vebeendoin’somethinking..."
    sa "And I think...it’s about time I...cameouttamyshell..."
    sa "*Hic* ya know? Sometimes ya just gotta get out there and do the thing."
    s "What “thing” are you trying to do exactly, Sana? "
    sa "Idunno...issa...thing Rin says all the time..."
    sa "I’m just...doing what the Romans do..."

    scene sanadrunkagain2
    with dissolve

    sar "And on that note, I’m going to head upstairs."
    s "Wait, really?"
    s "I was under the impression you’d be joining us."
    sar "Not tonight, I’m afraid. There’s a glass of wine and a romance novel waiting for me in my bedroom."
    s "Why is there already a glass of wine poured in your bedroom?"

    scene sanadrunkagain5
    with dissolve

    sar "Stop asking questions and comfort my daughter."
    sar "She’s been down all day and I think you’re the one she needs to see."
    sar "I love her, but I’m not exactly the best when it comes to cheering people up. Hence alcohol."

    scene sanadrunkagain4
    with dissolve

    sa "Yeah...*hic* stay and...talk to me...Sensei..."
    sa "We’ll be all alone...we can do...{i}whateverwewant{/i}..."
    sar "Remember Sensei, even if girls say that while they’re drunk, they don’t necessarily mean it."
    s "You’re one to talk, Sara."
    sar "Heheh~ I sure am."
    sar "Have a good night, you two!"

    "I can hear Sara’s footsteps trail up the stairs and stop in the room above us."
    "I can even hear the bed squeak as she hops onto it."

    if sarasex == True and bonus == True:
        "That’s...mildly concerning for a number of reasons."

    else:
        "I feel like that would be cause for concern if the two of us were to ever...you know."

    scene sanadrunkagain1
    with dissolve

    sa "Hehehe...now I’ve gotcha...alltomyself..."
    s "How much have you had to drink, exactly?"
    sa "A million..."
    s "I think we need to get you into an ambulance if that’s the case."

    scene sanadrunkagain6
    with dissolve

    sa "I’m just kidding...I’m drunk but not...a million drunk."
    s "Wow, you really had me going there for a second. I sincerely believed you were a million drunk."
    sa "Heheh~ It’s all that...role playing experience from...vacation."
    s "Well, whatever you do, please don’t cut me in half like that mushroom monster or whatever it was."
    sa "You don’t have to worry...Orc Sana is much stronger than normal Sana..."
    sa "Normal Sana probably couldn’t even hold a battle axe..."

    "Sana sprawls out further so her leg doesn’t wind up falling off of the table."
    "She looks very different from how she normally is. And no, it's not because she’s drunk."
    "Well, I'm sure that's part of it."
    "But it’s the first time I’ve seen her in an actual relaxed position. "
    "It’s like she’s lounging around her bedroom right now."
    "Which, to be fair, is at least partially true since her mother is right upstairs."
    "But still."

    sa "Aren’t you...gonna ask me what was bothering me, Sensei?"
    sa "My mom just told ya I was down and you haven’t even...asked me why yet..."
    sa "If I was Ayane, you probably would’ve asked right away...right?"
    s "I was getting there."
    s "You’re still not great at conversation yet, so you haven’t realized that there are some steps involved when you want to get someone to open up."

    scene sanadrunkagain7
    with dissolve

    sa "What kind of steps?..."

    if bonus == True:
        s "Small talk. Prodding."
        sa "Prodding sounds lewd...Is that really one of the steps?..."
        s "Not that kind of prodding. That comes later."
    else:
        s "You know like when you're playing Monopoly and you have to go backwards?"
        sa "Not...really..."
        s "Oh. Well, shit."

    s "But yeah...what’s bothering you exactly?"
    sa "Woah...I’m glad you asked without...me having to force you to..."
    s "Sana..."

    scene sanadrunkagain8
    with dissolve

    sa "Remember that girl from the other night?"
    s "What, you mean the creepy, white-haired one?"
    sa "Yeah, that’s the one."
    sa "She said some strange things, didn’t she?"
    s "Pretty much everything she said was strange."
    sa "She said you saw God..."
    sa "Is that true, Sensei?"
    s "Not to my knowledge. I’m pretty sure I’d remember something like that."

    scene sanadrunkagain6
    with dissolve

    sa "Would you?"
    sa "Maybe God has like...crazy mind control powers or something...like in a movie."
    sa "He’s God, so he can do whatever he wants, right?"
    s "Is that why you’re feeling down? You’re thinking about God?"

    scene sanadrunkagain9
    with dissolve

    sa "Nah...It’s nothing that interesting..."
    sa "It’s something else she said that’s been bugging me."

    "I think back to the other things the white-haired girl said during our very brief but extraordinarily creepy meeting."
    "The ones that stick out among them are...something about the path I walk...seeing the end of the world and..."
    "That someone Sana knows is happy."

    s "Who was the girl talking about when she looked at you?"
    sa "Could be anyone...she was...kind of weird..."
    sa "But, if I had to take a guess-"
    sa "Probably my brother."
    s "You have a brother?"

    scene sanadrunkagain10
    with dissolve

    sa "You don’t pay much attention...do you?"
    sa "I told you that the first time you came to the bar...and you never even asked about it."

    scene sanadrunkagain6
    with dissolve

    sa "How long have you been coming here now?..."
    sa "Long enough to start asking me more personal questions...right?"

    "I try to think back to my first meeting with Sana at the bar, but it seems so long ago now."
    "But somewhere, buried deep beneath almost every other memory I’ve made with her, there is {i}something{/i}."

    s "That’s his uniform, isn’t it?"

    scene sanadrunkagain8
    with dissolve

    sa "Was..."
    sa "He’s gone now."
    sa "Which is probably why...that crazy girl’s words went straight to my head..."
    sa "Chances are she was just...off her medication like you said..but what if she wasn’t?"
    sa "What if she can...talk to the dead...or something?"
    sa "Sooo, yeah...That’s what I’ve been thinking about."
    s "And I’m guessing that’s also why you couldn’t bring your mom into it?"

    scene sanadrunkagain11
    with dissolve

    sa "Sensei..."
    sa "It’s really hard, you know?..."
    sa "She changes the subject any time it comes up..."
    sa "We’ve never even really talked about it before..."

    scene sanadrunkagain12
    with dissolve

    sa "You’d think me wearing his clothes to work every day would at least start a conversation with her but...nope."

    scene sanadrunkagain13
    with dissolve

    sa "Who knows, though? Maybe I’m just crazy and he never existed in the first place..."
    sa "Maybe it’s all just a dream."
    s "…"
    sa "…"

    scene sanadrunkagain14
    with fade

    sa "Um...A-Anyway! H-How about we talk about something...fun instead?"
    sa "I...don’t want to be one of those people who just...rambles on and on about her feelings when she’s drunk so..."
    sa "Maybe we could play the question game again?..."
    sa "Makoto’s mom isn’t here to interrupt us this time so...we can ask whatever we want..."

    scene sanadrunkagain15
    with dissolve

    if bonus == True:
        sa "I’d...still prefer nothing perverted, though..."
        sa "Even if we’re closer than we were before...you’re still my teacher and...there’s the thing with Ayane too and..."
        sa "And my mom is right upstairs."
        s "Okay. Well, here’s a question..."
    else:
        sa "We should probably...not bring up my secret identity, though..."
        s "As a health inspector?"
        sa "Y-Yeah..."
        sa "I know I'm...not like Ayane or my mom, but..."

    s "Why does everyone you associate with like me so much? It's odd."

    scene sanadrunkagain16
    with dissolve

    sa "Right?! "
    sa "I have no idea!"
    sa "Do you have any idea how weird that is for me?!"
    s "It’s weirder for me. I don’t even think I’ve done anything to warrant that sort of admiration."
    sa "You really haven’t!"
    s "…"
    s "You could have at least tried to pretend that wasn’t true."

    scene sanadrunkagain17
    with dissolve

    sa "Sorry...I’m drunk and...don’t have control over myself right now..."
    sa "You know I think you’re cool..."
    sa "I’m sure everyone else sees you the same way..."
    sa "Also, umm, this might sound a little weird...but I think you have really pretty eyes as well..."
    sa "It’s even...kind of hard to look at them sometimes."
    s "Thanks Sana. I think you have a really pretty eye as well."

    scene sanadrunkagain18
    with dissolve

    sa "The second one actually has special powers..."
    sa "The reason I was holding my hair back for most of this conversation was to...hypnotize you..."
    s "Into doing what, exactly?"
    sa "Into being a normal teacher again. One that can help me with history..."
    sa "And also one that doesn’t think my mom is cute."
    s "Okay, come on, though. We both know your mom is cute."

    scene sanadrunkagain19
    with dissolve

    sa "Ugh! Don't remind me! It's annoying!"
    sa "She’s pure evil, I tell you! She’d do anything to be the center of attention!"
    s "…"
    sa "I’m gonna go get another drink!"

    scene sanadrunkagain20
    with dissolve

    sa "Do you want anything?!"
    s "...I’ll have a beer."
    sa "Okay!"

    "Sana storms off toward the bar and throws open the doors of the cooler, grabbing a drink for both herself and me."
    "I’m surprised she had such a...passionate reaction to my mention of Sara this time."
    "Maybe it’s just the alcohol, but I feel like she’d typically get embarrassed and down on herself instead of walking away in a fit of rage."
    "The dynamic between those two is confusing."

    scene sanadrunkagain21
    with dissolve

    sa "…"

    "Sana returns moments later with two cans- one for me and one for her."

    sa "…"

    "She also doesn’t say a single word and elects to just stare at me instead."

    s "...What?"
    sa "You realize...that if I finish this beer...I may not be able to walk."
    s "Then why drink it?..."
    sa "I...do not give you permission to carry me upstairs again."
    sa "I am still dealing with the embarrassment from the last time that happened."
    s "So...just leave you on the couch?"
    sa "It’s a good couch. "
    s "Sure, whatever. Just don’t look at me like that anymore. It’s weird."
    sa "You’re weird."
    s "Okay, Sana."
    sa "…"
    s "…"

    scene sanadrunkagain22
    with dissolve

    sa "Heheh..."
    sa "I’m glad you came tonight, Sensei..."
    sa "I’m already feeling a little better..."

    scene sanadrunkagain23
    with dissolve

    sa "Maybe my mom’s method of medicating...works after all?..."
    s "Yeah, let’s not have you fall down the path to alcoholism at such a [young]age."

    scene black
    with dissolve2

    "Sana does, in fact, finish the beer."
    "And her legs do, in fact, give out."
    "I walk up the stairs into Sara’s apartment to find her already passed out."
    "So much for her romance novel, I guess."
    "I take a spare pillow and blanket from a couch in the living room and bring them downstairs, setting Sana up with them before I leave."
    "…"
    "It was another interesting night at the bar, if not anything else."
    "Hopefully, this time I can find it within myself to not forget such an important detail about her life."
    "But, for some reason, I already feel like something along those lines won’t happen again."
    "It’s safe to say that Sana’s become pretty important to me."
    "Sure, she might be more like a daughter than anything else at this moment, but-"
    "But I’m sure that still has room to change..."
    "I mean, who knows?"
    "This is Kumon-mi, after all."
    "Anything can happen here."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar30 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar35:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
...
```