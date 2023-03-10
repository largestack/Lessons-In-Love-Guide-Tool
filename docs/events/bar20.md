# Scouting Mission (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 20

* Event [Girl-Talk](./day65.md) (Main) is completed)

* Event [Carry Me Home](./bar15.md) (Sana) is completed)

* Event [The Queen of Spiders](./amisroom5.md) (Ami) is completed)



## Next events

* [Main: Human Trafficking](./day114.md)
* [Sana: Nice Weather We're Having](./sanadorm20.md)

## Event properties

* Id: bar20
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar20

## Official wiki page

[Scouting Mission](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar20&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar20:
    scene scoutredux1
    with dissolve
    play music "calmbar.mp3"

    "I walk into the bar and immediately put my head down as Sara and Sana are locked in a mildly heated argument behind the counter."
    "I worry for a moment that something like this could potentially drive customers away, but then I remember where I am and decide it's best to not worry at all."
    "I am a little offended, however, seeing as my presence has not put a stop to whatever debate those two are having."
    "Granted, I'm probably not even viewed as a customer anymore to them."

    if sarasex == True and bonus == True:
        "Now, I’m just a dude who shows up, has a beer or two, and then proceeds to either lecture or have sex with one of them."
    else:
        "Now I’m just a dude who shows up every once in a while to give public speaking
        lessons to one of them."
        "If you can even call our talks ‘lessons’ I mean..."

    scene scoutredux2
    with dissolve

    sa "Um...h-hi..."
    sa "You didn’t...hear anything just now did you?"
    s "Hey, Sana. "
    s "I didn't hear what it was about, but I could definitely tell it was some sort of argument."
    s "Is everything okay?"
    sa "Mhm...Everything is fine...I...umm..."
    sa "I don’t have to work tonight..."
    s "Sara’s going to take care of the bar on her own?"
    sa "I...guess so..."
    sa "I have...an...umm...important mission to take care of..."
    s "A mission this late?"

    scene scoutredux3
    with dissolve

    sa "And, um...it's...a mission for you too, actually..."
    s "Wait, what? Why? I just wanted to relax. Why do I have a mission now?"
    sa "Because that's just...how things worked out..."
    s "Well, can you tell me what it is? Or are you just going to stay cryptic about it?"

    scene scoutredux4
    with dissolve

    sa "I-I’ll tell you! I just need to go get dressed first!"
    sa "Please...wait a moment! My clothes are...upstairs..."

    scene scoutredux1
    with dissolve

    s "…"

    "Sana quickly dashes past me and up the stairs to her mother’s apartment."
    "It’s quiet enough in here that even the faint tapping of her footsteps manages to bring life to this dying bar."

    scene scoutredux5
    with fade

    sar "Hiya, stranger~"
    s "What the hell was that all about?"
    sar "Are you talking about our argument? Or about the mission?"
    s "Both, I guess?"
    sar "Well, the two of them are connected, so I'll just go ahead explain the whole thing to you."
    sar "This ‘mission’ involves checking out another bar in the area that’s been doing...admittedly better than this one."
    sar "Like, much better."
    sar "Like it's not even close."
    s "So it’s a...scouting mission?"

    scene scoutredux6
    with dissolve

    sar "Yeah, exactly! You two are going to go check out that bar and see what {i}they’re{/i} doing that we’re not."
    sar "Not sure if you’ve realized this, but my livelihood kinda depends on this place."
    sar "Unless a certain someone wants to start taking care of me, of course."
    s "I'm good, thanks."

    scene scoutredux7
    with dissolve

    sar "At least pretend to think about it, jerk!"
    s "That aside, are you sure it’s okay to send Sana to a rival bar?"

    if bonus == False:
        s "Doesn’t she look a little...young, but not so young that you would mistake her for someone who is not old enough to consent and can live entirely independently?"
    else:
        s "Doesn’t she look a little young? I can’t imagine there’s any place that would actually serve her."

    scene scoutredux8
    with dissolve

    sar "That’s exactly what we were arguing about! I was supposed to go with you instead!"
    sar "The two of {i}us{/i} going to a bar together would make a lot more sense than you going with my daughter! {i}And{/i} it would give us the chance to get to know one another better!"
    s "This wasn’t a scouting mission at all, was it? You just wanted to get drunk with me."

    scene scoutredux6
    with dissolve

    sar "I mean...that's not {i}all{/i} I wanted to do."
    s "That sentence makes the idea of you allowing your daughter to go in your place significantly more disturbing."

    scene scoutredux8
    with dissolve

    sar "It’s not like I {i}wanted{/i} to! She just seemed weirdly devoted to not letting me follow you out tonight for some reason!"
    s "That’s...interesting."

    scene scoutredux9
    with dissolve

    sar "{i}I{/i} think she's just jealous."
    s "I think it’s less jealousy and more feeling weird about the situation."
    s "Wouldn’t you feel odd if your teacher in [high_school] started dating your mom?"
    sar "Well, yeah. It would have been weird if we were {i}both{/i} dating him."
    s "I'm sorry, what?"

    scene scoutredux10
    with dissolve

    sar "Oh, it's not really a big deal."
    sar "It was one of those secret relationship things. No one ever found out about it."
    sar "Well, at least...not right away..."
    sar "But it was inevitable that someone eventually would and-"

    scene scoutredux5
    with dissolve

    sar "Wait, why are we even talking about this? That's definitely not something I want to discuss with you yet."
    sar "If only we were able to go out for drinks..."
    s "…"

    "Sara pauses for a moment and reflects on her past, but the reflection doesn't last long as the same faint tapping of footsteps from earlier makes its way back down the stairs."

    s "I’ll see you later, Sara. I’ll be sure to let you know how your rival bar is."
    sar "Be good to my daughter. Don't let her drink {i}too{/i} much."
    s "..."
    sar "It was a joke. You can laugh."

    scene scoutredux2r
    with fade

    sa "Um...I’m sorry it took me so long...I couldn’t find my socks..."
    s "It’s fine. I got the details from your mom. Do you know where this place is?"
    sa "Mhm...It’s not that far from here..."
    sa "You can just...follow me..."

    scene black
    with dissolve2

    "Sana and I exit the bar."
    "I turn around to look at Sara as we make our way through the door-"
    "But the smile she wore just moments ago has vanished."
    "And all I can do is imagine why."
    "………"
    "……"
    "…"

    scene sanabartwenty1
    with dissolve

    sa "…"
    s "…"

    "Sana and I take a seat at a table after being led over by a hostess around her mother’s age."
    "Right off the bat, you can tell this place has a much...{i}warmer{/i} atmosphere."
    "In fact, I don't even know if I'd call this place a {i}bar{/i} considering everyone seems to be eating as well."
    "I pick up a menu to confirm my suspicions and don't see the word {i}bar{/i} anywhere, so I ascertain that Sara's source of intel is just as bad as her management skills and toss away my gameplan for the night."
    "Sorry, Sara. Your mission was inherently flawed."

    sa "Um..."
    s "What’s up?"
    sa "Nothing’s up...I just...wanted to say...thanks for coming with me..."
    sa "I’ve never gone to another bar before..."
    s "You know this isn't a bar, right?"
    sa "..."
    s "Sana, it's clearly a full service restaurant. There are waiters and everything."
    sa "But...my mom said-"
    s "Your mom says a lot of things and it would probably be best to disregard most of them."
    sa "Well...either way...thank you..."

    scene sanabartwenty2
    with dissolve

    sa "I guess it’s...pretty easy to see why this place is better...right?"
    sa "It’s...really nice in here..."
    sa "I bet our...waitress will be really nice too..."

    "A moment of silence passes by as Sana begins to observe the layout of the place."

    scene sanabartwenty2r
    with dissolve

    "But unfortunately, before she's able to take in all of it, someone unexpected shows up."

    scene sanabartwenty3
    with dissolve

    k "…"
    s "…"

    if bonus == True:
        k "You brought a {i}child{/i}?"
    else:
        k "You brought a {i}health inspector{/i}?"

    scene sanabartwenty4
    with dissolve

    if bonus == True:
        sa "Ch...Child? No...I’m-"
    else:
        sa "My secret identity has been discovered."

    s "Sana, I’ll handle this."
    s "Talking to her is beyond your current skill level, I’m afraid."

    scene sanabartwenty5
    with dissolve

    sa "Wh-What?..."
    k "Explain yourself, Hamburger Man."
    sa "Um...do you...know this girl, Sensei?"
    s "I do. Her name is Kaori, but she also goes by the Mistress of the Queen of the Spider Dark or something."
    sa "The...what?..."
    k "Hamburger Man, I can not provide dizzy drinks to this undersized human."

    if bonus == True:
        s "That’s fine because this is a restaurant and not a bar. Not everyone has to drink."
        k "All of the other human customers order the dizzy drinks. I can not make special exceptions just because this human is not fully grown."

    scene sanabartwenty4
    with dissolve

    sa "Um...would I be able to...maybe have a glass of water?"
    sa "Does...that count as a..."

    scene sanabartwenty6
    with hpunch

    sa "OKAY NEVER MIND! SORRY I ASKED!"
    k "You are a strange creature. Perhaps...{i}a cyclops?{/i}...How do you know the Hamburger Man?"
    k "Tell me immediately, miniature human cyclops girl!"
    sa "I D-D-D-DON’T KNOW ANY HAMBURGER MAN! I SAID I’M SORRY! PLEASE DON'T HURT ME!"
    s "Kaori, it’s probably best to leave her alone until I progress further into her story."

    scene sanabartwenty7
    with dissolve

    k "What is this ‘story’ you speak of? Can it fit in a box?"
    k "Do {i}I{/i} have a story? What color is it?"
    s "Everyone has a story. Yours just hasn’t started yet."
    k "…"
    s "…"
    k "…"
    s "…"
    k "Order something now, please."
    s "I’ll have a-"
    k "No hamburgers."
    s "But I-"
    k "Absolutely no hamburgers, Hamburger Man. You will become one if you continue to live purely off of them."
    s "…"
    k "…"
    s "Just get me whatever dish you recommend. And a beer."
    k "Understood."
    k "Or, as I have learned to say from the cooking-man in the shiny back room, “heard.”"

    if bonus == True:
        k "I will retrieve your items now. Please do not allow your human daughter to consume any dizzy drinks in the meantime."
    else:
        k "I will retrieve your items now. Please do not allow the health inspector to look under the table."
        s "What? Why not?"

    scene sanabartwenty8
    with dissolve

    "Kaori leaves as quickly as she appeared and I’m alone with my human daughter again."

    sa "..."
    s "It’s okay, Sana. She’s gone now."

    scene sanabartwenty9
    with dissolve

    sa "Who was she?! {i}What{/i} was she?! Why did she talk like that?!"
    s "There are many questions in life that I am unable to answer. This is one of those questions."
    sa "Why do you know her? Are you...secretly a...weird person?"

    "Yes."
    "Probably not in...whatever way Sana is insinuating, but saying my habits are {i}not{/i} weird would be flat out lying."

    s "She’s just a waitress at some diner I’ve been to. And also at some bistro near the[school]."
    s "And...also here now I guess?..."

    "Just how many jobs does this girl have?"

    sa "People...{i}hired{/i} her? But...she’s so scary..."
    s "You’re not talking about the tattoo, are you? I don’t think it’s that bad."
    sa "She has a...tattoo?...I didn’t even see it...I had my eyes closed the whole time..."
    s "Yeah, she’s got a huge spider on her chest. Which makes it even stranger to me why so many places are hiring her."
    sa "Maybe she’s...in the Yakuza?..."
    s "Yeah...I don’t really think Kaori is the Yakuza type."

    scene sanabartwenty10
    with dissolve

    if bonus == True:
        sa "Um...you don’t...also think I’m...a {i}child{/i}...do you?"
        s "Of course not. I mean, obviously you’re younger than me. But you’re
        old enough to make your own decisions."
        s "Kind of like you did tonight."
    else:
        sa "Um...about me being a...health inspector..."
        s "Don't worry, Sana. I have strong feelings when it comes to health inspectors."

    scene sanabartwenty11
    with dissolve

    sa "Huh?...What do you mean by that?"

    if bonus == True:
        s "Like how you didn’t want me spending time alone with your mom and decided to volunteer yourself instead."
    else:
        s "I will tell you if you tell me why you didn’t want me spending time alone with your mom tonight."

    scene sanabartwenty12
    with dissolve

    sa "She...She told you that?!"
    s "Was she not supposed to?"
    sa "I...didn’t mean anything weird by it! I swear! I’ve just been meaning to visit this place for a while now!"
    sa "I hear the...water is really good!"
    sa "I’m totally not afraid of you being alone with my mom! Why would I be?!"
    s "Sana, I'm going to need you to calm down. People are starting to look over-"

    scene sanabartwenty13
    with dissolve

    sa "YOU TWO CAN BE ALONE WHENEVER YOU WANT AND I CAN’T STOP YOU!"
    s "Sana...please just-"
    sa "YOU ARE...BOTH ADULTS!"
    sa "YOUCANMAKEYOUROWNDECISIONS!"
    s "Sana, you really need to-"

    scene sanabartwenty14
    with dissolve

    k "..."
    s "..."
    k "...!"
    s "..."
    s "Okay, fine. We’re leaving."
    s "Sorry for causing a disturbance."
    k "I will remember this moment for all eternity."
    s "I’m sure you will. Come on, Sana."
    sa "I’MSOSORRY!"

    scene black
    with dissolve2

    "Sana and I exit the rival {i}bar{/i} and begin to make our way back to Sara’s."
    "Not wanting to explain the situation, I drop Sana off at the entrance and immediately begin to make my way home."
    "Here's hoping nothing like this ever happens again."
    "And here's to that hope being nothing short of a pipe dream."

    $ renpy.end_replay()
    $ bar20 = True
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar25:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

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
...
```