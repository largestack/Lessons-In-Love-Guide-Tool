# The Next Best Thing
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach5&go=Go)


Part of event chain [TPK](./secondbeach4.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach5
* Group: Main
* Triggered by label: secondbeach4

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach5:
    scene beachpartyyay1
    with dissolve2
    play music "oldweather.mp3"

    ay "Uhh...Tsuneyo? Are you sure you’re okay in there?"
    t "I no longer require a flotation device when in water below my shoulders."
    t "I will survive this event and, as the guardian says, “level up.”"
    a "I...think she means because of how cold it is."
    t "Please talk louder, Strawberry Leg Princess. I am unable to hear you from the middle of the ocean."

    scene beachpartyyay2
    with dissolve

    ay "How come Tsuneyo is always bringing up your legs, Ami?"
    a "I honestly don’t know."
    a "At first I thought it was flattering, but at this point it’s starting to get a little weird."
    ka "I...uhh..."
    a "You’re not going to compliment my legs as well...are you, Karin?"

    scene beachpartyyay3
    with dissolve

    ka "O-Of course not! I was just going to say...shouldn’t we maybe...{i}not{/i} let Tsuneyo stay in the water for that long? She’s going to get sick."
    ka "Also, you really do have nice legs."
    a "Eh. We’re probably all going to get sick after this weekend anyway. "
    a "Also, thank you."
    ay "I think we kind of all accepted that sickness might be a result of this whole swimsuits in winter thing."
    ay "But hey, if Tsuneyo is gonna be brave enough to hop in, I think we should too."

    scene beachpartyyay4
    with dissolve

    a "Ayane, didn’t you {i}just{/i} recover from being sick?"
    ay "I was sick with misery and loss! It’s nothing like having a cold."
    ka "No...What you had sounds much worse."

    scene beachpartyyay1
    with dissolve

    ay "Tsuneyo! On a scale of one to ten, how cold would you say the water is?!"
    t "Cold, but not too cold."
    a "The scale, Tsuneyo! Remember the scale!"
    t "What a rude way to tell someone to lose weight."
    ka "She means rate it on a-"
    ay "Save your breath, Karin. If Tsuneyo doesn’t understand something right away, there’s only one person who is able to teach her...and {i}she’s{/i} off practicing her stealth now."
    t "Fuck you in the insulting way and not the sexual one, bro."
    t "I am a strong independent noodle who needs no broth."
    t "The world is my soup bowl and I’m here to party."
    a "Maybe we really {i}should{/i} just swallow our pride and run in after all?"
    t "Cowards. You will never survive in the-"

    scene beachpartyyay5
    with dissolve

    t "Hm?"
    noodles "Caw."

    scene beachpartyyay6
    with dissolve

    t "Ah!"
    t "My son! You have decided to come to the beach!"
    t "If only your father had never abandoned us and was here to see this!"
    noodles "Caw :("

    scene beachpartyyay7
    with dissolve

    t "I shouldn’t. It would be far too dangerous."
    noodles "Caw. Caw caw caw. Caw caw caw?"

    scene beachpartyyay8
    with dissolve

    t "Can a simple chemical like bleach truly do something so impressive?"

    scene beachpartyyay9
    with dissolve

    a "That’s-"
    ka "What’s she talking to? I can’t really see."
    a "How did the dorm bird make it all the way to the beach?!"
    ay "Chickens always come home to roost, Ami."
    ay "And I guess sparrows, too."

    scene beachpartyyay10
    with dissolve

    ka "You guys have a dorm bird?! I want a dorm bird!"
    ka "Living at home sucks! I wanna go back a year!"
    a "No, Karin. No..."
    a "There’s something...special about that bird."
    a "He’s...up to something."
    ay "I think he’s just a bird, Ami."

    scene black
    with dissolve2

    "{i}Meanwhile, several feet behind them under a gazebo pavilion thing...{/i}"

    scene beachpartyyay11
    with dissolve

    r "I can do this. I can do this. I can do this. I can do this. I can do this. I can do this. I can do this. I can do this. I can do this. "
    r "Futaba, tell me I can do this."
    f "You can do this..."

    scene beachpartyyay12
    with dissolve

    r "Oh my god. I can’t do it and I’m gonna die."
    r "I’m gonna die and everyone’s gonna remember me as that girl who died from being too bisexual."
    f "You’re not going to die...you just need to calm down a little."

    scene beachpartyyay13
    with dissolve

    f "You have experience now, remember?"
    f "It won’t be your first confession this time, so I imagine you’ll be a little better at talking."
    r "You are putting way too much faith in my ability to make it through a sentence around a girl I wanna kiss."
    f "Maybe so. But also, you’ve been hanging out with Otoha a lot more than normal lately."
    f "Back when you confessed to Chika, you two had only just started hanging out."
    f "Don’t you think that has to be some sort of sign?"
    f "If someone you knew liked you and kept trying to hang out with you all the time, what would you do?"
    r "Height? Weight? Favorite band? Hair color? Do they like girls?"
    r "Wait, no. They obviously like girls if they like me."
    r "Unless they think I’m a boy-"

    scene beachpartyyay14
    with hpunch

    r "Oh God! What if Otoha thinks I’m a boy?!"
    f "I am...positive Otoha is well aware that you are a girl, Rin..."

    scene beachpartyyay15
    with dissolve

    f "Just stay confident...tell her how you feel...and be ready to accept whatever comes next."
    f "What...I would probably do if I was ever going to...confess like this, is plan out a reaction for both a good and a bad outcome beforehand."
    f "That way, I’d be ready to react no matter what happens and wouldn’t get blindsided by a surprise answer."
    f "And...given what you’re going to be asking her, I can’t really see how a...surprise answer would even happen."

    scene beachpartyyay16
    with dissolve

    r "Man...how come you’re so good with all of this romance stuff all of a sudden?"
    r "The Futaba from last year took all of her love tips straight out of medieval fantasy novels. "
    r "Now you’re out here talking like some seasoned mother who’s popped out five kids with a sixth on the way. "

    if bonus == True:
        r "And I’m your adopted daughter struggling with her sexual identity and spending way too long in the shower cause we’ve got one of those detachable hose thingies."
    else:
        r "And I’m your adopted daughter who keeps leaving the lights on and riding up the electricity bill."

    scene beachpartyyay17
    with dissolve

    f "Uhh...No, Rin. I’m talking like your best friend and number one support system."

    if bonus == True:
        f "Also, please leave your shower habits to yourself."
        r "Oh, come on. We all do it."

    scene beachpartyyay18
    with dissolve

    if bonus == True:
        f "It...It doesn’t matter what we do! What matters is that you don’t let yourself get distracted right now and figure out how and when you’re going to confess."
    else:
        f "Rin! Don’t let yourself get distracted right now and figure out how and when you’re going to confess."

    scene beachpartyyay19
    with dissolve

    r "Umm...Futaba?"
    f "Yes?"
    r "I really love you, you know. "

    if bonus == True:
        r "Like, not in a shower head kind of way. A sister kind of way."
        f "Thank you for clarifying. I love you in a non-shower head way as well."
        f "And Sensei is also just around the corner...probably. "
    else:
        f "I love you too, Rin."
        r "Wanna hug? I think it's hug time."
        f "Probably not with Sensei right around the corner...He always gets jealous when there is a hug he's not involved in..."

    r "Yeah...I already gave him the heads up about what’s gonna wind up happening this weekend."
    r "I am more than prepared to spend the coming days crying into both of you, so maybe us three should just get a room to ourselves?"
    r "Can you ask your parents for an advance on your allowance? I asked my mom for concert tickets last week, so I’m kinda in the no fly zone for a little while."
    f "I’m...pretty sure Touka’s family rented out the entire inn, so there will be more than enough places for you to cry."
    f "For now, though...let’s just hope that you won’t be crying at all."
    f "Now...tell me more about when you’re going to do it."

    scene black
    with dissolve2

    "{i}Meanwhile, yet again, even further along the beach.{/i}"
    "{i}But not that far.{/i}"
    "{i}Just...kinda...over there or something.{/i}"

    scene beachpartyyay20
    with dissolve2
    stop music fadeout 25.0

    mi "You plannin’ on swimmin’ at all, Sana? Or are you gonna be like me and just wear the swimsuit for show but not bother gettin’ your feet wet?"

    scene beachpartyyay21
    with dissolve

    sa "I’m...not really good at swimming."
    sa "And the ocean is kind of big, so...I’ll probably just stay here..."
    mi "Looks like it’s gonna be you and me then since Makoto’s still back at the room layin’ out futons and stuff."

    if bonus == True:
        mi "Did ya hear that Nodoka basically [molest]ed us? "
    else:
        mi "Did ya hear that Nodoka basically attacked us? "

    scene beachpartyyay22
    with dissolve

    sa "She...what?"
    sa "Are you okay?"
    mi "Uhhh, sorry. Probably not the best choice of words."

    if bonus == True:
        mi "Just kinda a light hearted strip search thingy. Didn’t actually touch any of the goods if ya know what I mean."
    else:
        mi "She only had finger guns instead of normal ones, so it wasn't a {i}real{/i} act of gun violence."

    mi "I should've cleared that up before scarin’ ya."

    scene beachpartyyay23
    with dissolve

    sa "Oh."
    sa "No...I’m sorry for...not understanding that right away..."
    sa "Nodoka is...a nice girl and...probably wouldn’t ever do anything like that."
    mi "Yeah..."
    sa "..."
    mi "Hey, everythin’ okay? You’re lookin’ a little under the weather. "

    scene beachpartyyay24
    with dissolve
    play music "starvingtodeathoutofreachofthesun.mp3"

    sa "Hm?"
    sa "No...I’m okay. Just a little tired."
    mi "You sure?"
    mi "I know we’re not really the closest, but I’ve still known ya since all the way back in middle[school]."
    mi "Us short girls gotta stick together, ya know? "
    mi "Not just for when we’re feelin’ sad and stuff, but for when we’ve gotta reach things that normal girls can reach. "

    scene beachpartyyay25
    with dissolve

    sa "Heheh..."
    sa "I guess we would make a...good team if we ever needed to...do something like that."
    mi "Well, if there’s anythin’ I’m good at, it’s bein’ part of a team."
    mi "Hey, you don’t have any interest in playin’ soccer, do you? Cause we could use another tiny girl or two. "
    mi "Work out those legs of yours and you’ll be the next Usain Bolt before ya even know it."
    sa "I...don’t know who that is...but I’m not really interested in soccer..."

    scene beachpartyyay26
    with dissolve

    sa "If you...um..."
    sa "If you ever want to...play video games or something, though..."
    mi "Heck yeah! I haven’t played games in like six trillion years cause Makoto’s always callin’ em poison for the mind."
    mi "That and the fact that I should...probably be usin’ my free time to study. "
    sa "Studying is boring, though..."

    scene beachpartyyay27
    with dissolve

    mi "Ya got that right. "
    mi "‘Sides...it’s not like we’ve got a teacher that really cares about that anymore anyway."
    mi "‘Two of us could probably ditch[school] for a week straight and come back with straight A’s if Makoto wasn’t there to bust into our rooms and spank us for bein’ absent."
    mi "Just kiddin’. Makoto’s never spanked me. "
    mi "But I’ve also never missed[school] for more than a day, so..."
    mi "Hey, if you wanna chime in, feel free. If not, I’ll probably just keep ramblin’ on about a bunch of random stuff until the sun goes down."
    sa "Heheh...no, it’s fine..."
    sa "It’s easier for me when other people talk anyway..."
    mi "Sounds good to me."
    mi "I was kinda here not too long ago anyway, so this whole beach trip thing is probably a little less excitin’ for me than it is for you and everybody you came with."

    scene beachpartyyay28
    with dissolve

    sa "You were here recently?"
    mi "Mhm! With Makoto and Sensei."
    mi "Pretty sure I’m allowed to tell you about that. I don’t think it was meant to be a secret or anythin’."
    mi "But if it was, you didn’t hear it from me."
    sa "Sensei was...there as well?"

    scene beachpartyyay29
    with dissolve

    mi "Yup! Think it was somethin’ Makoto wanted to do to make sure we had enough room for this trip or whatever."
    mi "Can’t actually remember the reason, but I {i}do{/i} remember the three of us were there and it was..."

    scene beachpartyyay30
    with dissolve

    mi "It was..."
    mi "Fun..."
    sa "…"
    mi "…"

    scene beachpartyyay31
    with dissolve

    sa "…"
    mi "…"

    "Two girls in a line on the beach."
    "Seen an undisclosed amount of time before breaking."
    "Could it be tomorrow? "
    "The next day?"
    "The day after that?"
    "A month from now?"
    "A year?"
    "Or perhaps the two of them are already broken."
    "And perhaps they’re not just staring off into the distance right now, but searching the shoreline for the remnants of things they may have lost."
    "Everyone loses something, you know."
    "I bet you’ve lost a fair deal yourself."
    "But how would you compare it to them?"
    "And {i}should{/i} you compare it in the first place?"
    "Two girls in a line on the beach, measuring around the same size as a professional basketball hoop when their heights are combined."
    "But the lack of physical verticality and concealed desire to snatch away the object of their respective best friends’ affection is not the only similarity they share."
    "They share a bond much deeper- "
    "One that very few will understand. "
    "One that very few {i}want{/i} to understand."
    "I will tell you now that they {i}were{/i} looking for the remnants of things they once lost in the sand."
    "Neither of them expected to find anything, of course."
    "I mean, why would they?"
    "But I, just as they do, struggle to think that anyone can walk around a place like this without incessantly gazing down at their feet in hopes of finding something that takes them back."
    "A seashell."
    "A coin with a specific year on it."
    "The sunglasses of a woman who was pulled in by the current."
    "Mementos and mementos and mementos!"
    "Each one left behind with a story of its own."
    "Every object in every place is more than it seems."
    "Just like every downtrodden, longing stare from a girl with A-cups is also more than it seems."
    "They connect."

    sa "Hey..."
    sa "How do you...feel about Sensei?"
    sa "Not...as a teacher, but-"
    mi "I want him to be with Makoto."

    scene beachpartyyay32
    with dissolve

    sa "With...Makoto?"
    mi "Yeah."
    mi "She’s liked him from the moment she met him."
    mi "And she’s my best friend, so I have to root for her."
    sa "…"
    mi "Makoto works harder than anybody and doesn’t have much to show for it other than good grades."
    mi "Her dad was a big part of her life, too...and now he’s up in space. So all she’s really got in terms of a guy figure to look up to is Sensei."
    mi "So I want him to look at her the same way she looks at him."
    mi "That way, everyone can be happy."
    sa "…"
    mi "I..."
    mi "Yeah."
    mi "I want him to end up with Makoto."
    sa "…"
    mi "…"

    scene beachpartyyay33
    with dissolve

    sa "I..."
    sa "I don’t want him to end up with anybody."
    mi "…"
    sa "…"
    mi "I guess that would be the next best thing for me too."

    scene black
    with dissolve2

    "The line remains unmoving on the beach, blending in with thousands more left there by nature or the pointy end of a stick gripped firmly by the slimy fingers of someone’s child."
    "Neither girl ever finds anything they’re looking for."
    "But, on the bright side-"
    "All of the other girls seem to have a good time."

    $ renpy.end_replay()
    $ secondbeach5 = True
    stop music fadeout 5.0

    "{i}There is something buried underneath your feet!{/i}"
    "{i}Could it be here?{/i}"
    "………"
    "……"
    "…"

    jump secondbeach6

label secondbeach6:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
if bonus == True:
        "Please don’t interpret that the wrong way."
    else:
        "Except it's not fun at all. It's really scary and I'm probably going to have bad dreams now."

    "I’m really just sitting here thinking about, as Otoha put it, the calm before the storm."
    "I know we only have one other experience to work off of, but it feels like a beach trip without some form of tragedy would be no beach trip at all."

    scene otohabananaboat16
    with dissolve

    mo "…"
    s "Molly?"

    "Right on cue."

    mo "G...Greetings, Supreme Overlord."
    s "How long have you been there for?"
    mo "I was...in the middle of leveling up my stealth when...I saw you and Otoha walking, so..."
    s "So you followed us?"
    mo "...Yeah."
    s "How much did you hear?"
    mo "Not much, Sir. I had to stand rather far away to conceal my presence. "
    mo "I had every intention of leaving you behind and returning to the inn to complete my quest, but..."
    mo "I...I think I’m leveled up high enough to skip out on the XP for a little while longer."
    s "Does this mean it’s {i}our{/i} turn to talk now?"
    mo "May I sit?"
    s "As long as you’re okay with the seat being a giant banana."

    scene otohabananaboat17
    with fade

    "Molly takes a seat on the banana boat and peers up at the sun through the leaves of the palm trees."
    "As if the idea of the calm before the storm was not enough the first time it was brought up, she had to show up now of all times and remind me of just how much is at stake this weekend."

    if bonus == True:
        "Perhaps {i}everyone{/i} will be damaged beyond repair and I’ll be around to pick up the pieces?"
        "…"
        "Why does the thought of that not excite me even half as much as it should?"

    s "Molly-"
    mo "I’m already prepared for it, Sir."
    s "Prepared for what?"
    mo "TPK."
    mo "A total party kill, rather."
    mo "The only issue is that this druid is currently in between groups and running a party of one."
    mo "It’s a lonely campaign."
    mo "But...I’ll be able to start again on a new character soon enough."
    s "…"

    scene otohabananaboat18
    with dissolve2

    mo "I know it’s coming."
    mo "And I know things do not look good for the main heroine."
    mo "But...that’s just the thing with main heroines, Sir. "
    mo "Sometimes, our happiness is pushed back to the very end."
    mo "Perhaps that’s what’s happening this time. "
    mo "Or..."
    mo "Or perhaps I’m no main heroine at all?"

    scene otohabananaboat19
    with dissolve

    mo "Either way...I’m prepared."
    mo "I {i}have{/i} to be prepared."
    mo "If Rin thinks Otoha is the one who can make her happy...I’ll just have to make someone else happy."
    mo "I’ll..."

    scene otohabananaboat20
    with dissolve

    mo "I’ll..."
    s "…"
    mo "Damn it..."
    s "Would it make you feel better if we hugged on a banana boat?"

    scene otohabananaboat21
    with dissolve

    mo "Hahah..."
    mo "Maybe for a moment..."
    mo "I do...have to be getting back to the Kendo Princess, though. "
    mo "She’s embarking on a quest of her own right now that...may or may not have its own set of difficulties."
    s "A quest of her own?"

    scene black
    with dissolve2
    stop music fadeout 5.0

    $ renpy.end_replay()
    $ secondbeach4 = True

    "{i}Meanwhile...further down the shore...{/i}"
    "………"
    "……"
    "…"

    jump secondbeach5
...
```