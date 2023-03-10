# Closer to Me (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 40

* Event [Waiting for Anything](./sanadorm35.md) (Sana) is completed)



## Next events

None

## Event properties

* Id: bar40
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar40

## Official wiki page

[Closer to Me](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar40&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar40:
    scene barwalkhome1
    with fade
    play music "love.mp3"

    sa "Oh...Sensei."
    sa "Um...you have...pretty bad timing tonight..."

    "I show up at the bar a little later than normal to find Sana already prepared to leave."
    "I slide my phone out of my pocket to check the time and, even though it's late, it’s nowhere near closing time yet."
    "Well, actually, I guess closing time in a place like this is whenever the person running it wants it to be, so..."
    "I’m sure Sara has something to do with this."

    s "Leaving already?"
    s "Isn’t it a little too early?"
    sa "Normally...yes."
    sa "But we closed half an hour ago..."
    sar "You should learn to read signs, Sensei. "
    sar "Those big letters on the door that say “closed” mean we’re not open."
    s "I blame you for changing the hours so suddenly and throwing me off."
    s "What’s the reason you're closing so early tonight?"

    scene barwalkhome2
    with dissolve

    sa "I...don’t really know either, to be honest..."
    sa "I think my mom isn’t feeling well, but...that doesn’t mean I couldn’t look after the place myself..."
    sar "Don’t listen to her. I’m fine."
    sar "Just figured it would be good for the two of us to get some time off."
    sar "Ideally, Sana would have come upstairs to hang out with me, but she keeps talking about how tired she is."
    sa "The walk back is kind of long, so...if I can start heading back earlier I...probably should."

    scene barwalkhome3
    with dissolve

    sar "Yeah, yeah. Go home and sleep. "
    sar "I’ll just sit upstairs and do my best Haru-chan impression by watching movies and eating ice cream until I pass out."
    s "Better habit than drinking until you pass out, at least."
    sar "Is it really, though?"
    sa "Um...S-Sensei?"
    sa "You wouldn’t want to...maybe..."

    scene barwalkhome4
    with dissolve

    sa "W...Walk back with me...would you?"
    sar "He’s got no choice. We’re closed for the night."
    s "Wow. You’re not offering to keep the place open as a special favor to me?"
    s "You really aren’t feeling well, are-"
    sar "I said I’m fine."
    s "...Okay."
    sa "Um...is that a...no?"
    s "Not at all. Of course I’ll walk back with you."
    s "I came here to see you again, so it’s not like there’s anything else I have planned for tonight."

    scene barwalkhome5
    with dissolve

    sa "Really?..."
    sa "I...walk kind of slow since my legs are really small, so...I hope that’s not a bother..."
    s "I could always just carry you home instead if you want. "
    s "I can’t imagine you weigh more than a six pack of beer."

    scene barwalkhome6
    with dissolve

    sa "Uhh...n...no..."
    sa "You don’t have to carry me..."
    sa "And I...definitely weigh more than...a six pack of beer..."
    s "Jump into my arms and prove it."
    sa "…"
    sa "Maybe I should walk home alone after all?..."
    s "I’m kidding..."

    "I really wasn’t, though."

    if bonus == False:
        "I could really use a hug right now."

    scene barwalkhome7
    with dissolve

    sa "Hahah...y-yeah...I figured as much..."
    sa "But, umm...I guess we should head out so...my mom can start doing her...Haruka impression."
    sar "For real. I gave you both the green light to abandon little ole’ me and you’re still standing there talking."
    sar "Am I really that irresistible?"
    sa "{i}It certainly feels that way sometimes...{/i}"

    scene barwalkhome8
    with dissolve

    sa "A-Anyway...let’s start walking, Sensei..."
    sa "I know a...pretty quick way back, so...we’ll get there in no time."

    scene black
    with dissolve2

    "I follow Sana out of the bar, taking a look over my shoulder to see if Sara has changed expressions now that we’re finally leaving."
    "She had a pretty...interesting moment when I saw her in Sana’s room recently, so I wouldn’t be surprised if this somehow had something to do with that."
    "Perhaps more interesting, though, is how Sana has finally agreed to walk home with me."
    "I feel like I’ve offered this countless times in the past, so I figured the first time it actually happened would be the result of yet another one of my invites."
    "But, strangely enough, she’s the one who invited me."
    "Here’s hoping her “really small legs” don’t provide much of a hindrance to what I imagine will be a relatively peaceful walk back."
    "………"
    "……"
    "…"

    scene barwalkhome9
    with dissolve2

    "As expected, we don’t have the easiest time thinking up conversation topics as we wander down the streets toward the dorms."
    "I hate having to take the lead in situations like this. It’s exhausting. "
    "Putting two people together who struggle with that same exact thing turns what could be a sweet event in a romantic comedy into a night that will be easy to look back on and cringe."
    "{i}Why did it take so long for us to break the silence?{/i}"
    "{i}There were so many other things we could have talked about.{/i}"
    "Things like that."
    "Things you think but never say."
    "So, in layman’s terms- "
    "Most things."

    scene barwalkhome10
    with dissolve

    sa "How...tall do you feel right now?"
    s "Like a giant."
    s "I always forget how short you are until you’re standing right next to me."
    sa "It probably helps that I...don’t get to stand next to you all that often..."
    sa "I’m happy I...got to tonight, though..."
    s "I’m surprised you were feeling up to this all of a sudden."
    s "I feel like I’ve tried to do this with you a bunch of times now."

    scene barwalkhome11
    with dissolve

    sa "Y-Yeah...even though I’m happy, it...still feels really weird..."
    sa "Who would have thought that...someone who has so much trouble making friends would...wind up having a guy {i}your{/i} age as one?..."
    s "Are you calling me old, Sana?"

    scene barwalkhome12
    with dissolve

    if bonus == True:
        sa "Super old...old enough to be my dad, probably..."
    else:
        sa "Not...that old...but like...closer to my mom's age than mine..."
        sa "Like...you guys could be married..."

    s "I’m sure your mother would love that."

    scene barwalkhome13
    with dissolve

    sa "Yeah...she definitely would..."
    sa "I’m pretty sure...that might be what she’s trying to do..."
    sa "It would be nice if...she picked someone I didn’t know, though..."

    if bonus == True:
        s "First, you say I’m old. Now, you’re saying you wouldn’t want me as a father?"

    s "Sana, do you actually hate me?"

    if bonus == False:
        s "I know it's kind of random, but I am very sensitive and worried about what everyone thinks of me at all times."

    sa "What? No...of course not..."

    if bonus == False:
        sa "You're kind of like the weird dad I never wanted...but also not really?..."
        s "Okay. That is fine."

    sa "I just...can’t really ever think of you as...being that kind of person to me..."
    sa "But...then again...it’s not like I really...understand what that kind of person would feel like in the first place..."

    scene barwalkhome14
    with dissolve

    sa "You’re actually...kind of the closest thing I’ve ever had to...someone like that, Sensei."
    s "Already? I feel like we still barely even know each other."
    sa "Y...yeah...I know that..."
    sa "But all I really know about my dad is...what I’ve heard from my mom..."
    sa "And I think you’ve realized by now, but...she doesn’t really open up a lot..."
    s "Well, what kind of things {i}has{/i} she told you?"

    scene barwalkhome15
    with dissolve

    sa "Do you want...the good things or the bad things?..."
    s "Just a general synopsis would be fine, I guess."
    sa "Then..."
    sa "He wasn’t very loyal..."

    if bonus == True:
        sa "My mom has always been...kind of naive...and I think he was stringing her along..."
        sa "She said he always seemed nice to her in[school], but...he was also a lot older than her, so...he was probably just...good at manipulating her..."
        sa "It wasn’t until after I was born that...she found out he’d been seeing other girls..."
        s "I see."
    else:
        sa "He...never stood on the payload..."

    "And of course her father is the mirror image of me. Great."
    "I’m sure there’s no way that’s going to bite me in the ass eventually."

    sa "So...when I say you’re the closest thing I’ve had to someone like that...it’s not because I think we’re close yet..."
    sa "There’s just...not any competition..."
    sa "You win by default..."
    s "…"
    s "So, Sara really raised you by herself then, huh?"

    scene barwalkhome16
    with dissolve

    sa "Yeah but...not just me...My brother, too."
    sa "She raised both of us all by herself..."
    sa "It was probably...really hard..."
    sa "That’s why...I don’t like trying to get her to talk about the past..."

    scene barwalkhome13
    with dissolve

    sa "And when I brought up something that reminded her of my brother the other night..."
    sa "It made me feel like it was my fault she...started to break down..."
    s "I had a feeling it was something like that."
    sa "I had a feeling that...you had a feeling about that..."
    sa "I’m sorry for not saying goodbye, by the way..."
    sa "I just...don’t normally see my mom like that and...I needed to make sure she didn’t get any worse..."
    sa "It was my fault for bringing something nostalgic up anyway..."
    s "I don’t think you should blame yourself for that. Avoiding the past is impossible."

    scene barwalkhome17
    with dissolve

    sa "No...it’s really not..."
    sa "If there’s anything I’ve learned from my mom, it’s that...denial can be a really good tool sometimes..."
    sa "It’s hard for me since...I loved my brother a lot, but..."
    sa "Can you imagine how much harder it was for her?..."
    sa "She...made him...and watched him grow up..."
    sa "Which of these two things sounds easier, Sensei?..."
    sa "Learning to cope with...the person you love more than anything in the world suddenly going away-"
    sa "Or just...ignoring that it ever happened."
    s "The second one sounds easier, absolutely."
    sa "Right...so-"
    s "Something being easy doesn’t mean it’s the right thing to do, though."

    scene barwalkhome18
    with dissolve

    sa "Huh? What do you mean?"
    s "I mean that bottling things like that up can literally kill people."
    sa "But...so can grief."
    sa "No matter what we do, we’re going to...keep hurting."
    sa "A third of our family was taken away from us..."
    sa "All we can do is...help each other deal with that any way we can..."
    s "…"

    if sarasex == True:
        s "Didn’t you tell me when you were drunk that you wished Sara {i}would{/i} talk about it, though?"

        scene barwalkhome19
        with dissolve

        sa "..."
        sa "Things you do or say when...you’re drunk...don’t count..."
        s "That’s an incredibly dangerous thing for someone working in a bar to be saying."
        sa "Yes, but...it’s something I need to think or...everything will get even worse than it already is..."
        s "…"
        sa "…"

    scene barwalkhome20
    with dissolve

    sa "Oh no! I...I made this a really awkward walk all of a sudden!"
    sa "Wh-what were we talking about at first?"
    s "How I’m the closest you’ve ever had to a father figure."
    sa "Th-that’s awkward, too! Wh-wh-what was our last {i}normal{/i} conversation about? Let’s go back to that!"
    s "I think that was just about how tall I am."
    sa "So tall! The tallest!"
    s "Sana, calm down. It’s okay that things got awkward for a few minutes."
    s "If you’re embarrassed about it, just look at it as another exercise in public speaking."
    s "You were able to talk at length about something that makes you uncomfortable, and now I know more about you as a result."

    scene barwalkhome21
    with dissolve

    sa "Uh...uh-huh..."
    sa "But now it will probably be a little bit harder for me to...spend time with you when you could just...go hang out with Ayane instead and...avoid my awkwardness..."
    sa "At least when...she compares you to a dad, she...knows what she’s talking about..."
    s "Good point."

    if bonus == True:
        s "Maybe I should just adopt the two of you and get it over with?"
        sa "I think you’d...have to marry my mom to be able to adopt me..."
        s "I feel like there are several people who would be very unhappy with me if that were to happen."
        sa "And...one of them is right next to you..."
        sa "But it’s okay..."
        sa "Like I said...I don’t view you that way..."

    sa "I’m...perfectly fine if things just...stay like this..."
    sa "That would be...the easiest thing for everyone..."
    s "…"
    sa "…"
    s "You’re really fine with things never changing?"

    scene barwalkhome22
    with dissolve

    sa "…"
    sa "Actually..."
    sa "When I say this would be the easiest thing for everyone...I really just mean me..."
    sa "If you get any closer to Ayane...you’ll get further away from me."
    sa "If you get any closer to my mom...you’ll get further away from me."
    sa "And if..."
    sa "You get any closer to me..."
    s "…"
    sa "…"

    "Sana never finishes that thought but, through context clues and my unparalleled wisdom in the world of [teenage]girls, I’m able to ascertain what she means."
    "She’s afraid of her feelings for me growing."
    "{s}Growing like a tree.{/s}"
    "She’s afraid of what she’ll have to do and what she’ll have to go through if she, too, falls victim to my suspicious gravitational pull on all of these girls."
    "Take Ayane, Sara, and me and arrange us so we form a triangle."
    "Right now, Sana is in the middle of the triangle- and she wants to get out."
    "The only way to do that is by breaking one of the lines."
    "Breaking a line means the triangle would crumble."
    "So, just like her mother-"
    "She doesn’t try to change anything."
    "She stays exactly where she is and waits for everything else to resolve on its own."
    "It’s a horrible way to live."
    "A horrible, impassive way to live-"
    "That I, too, am guilty of in more ways than one."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar40 = True
    stop music fadeout 100.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}A short while later...{/i}"

    jump sanadorm40

label bar45:
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
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
    if sana_love >= 35 and utamaid5 == True and christmas7 == True and bar35 == False:
        jump bar35
    if sana_love >= 40 and sanadorm35 == True and bar40 == False:
        jump bar40
...
```