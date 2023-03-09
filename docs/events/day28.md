# Ponytail
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day28&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 28



## Next events
None

## Event properties
* ID: day28
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day28:
    scene newponytail1
    with dissolve
    play music "10c.mp3"

    a "Sensei, can we please hurry up?!"
    a "Maya is all alone in the cafeteria and I'm worried about her cleaning the place out before I can get my lunch!"
    s "Well, you should have thought about that before nearly burning the classroom down."
    a "Come on! What kind of best friend would I even be if I let her put that many extra calories into her tiny body?!"
    s "The kind that, and forgive me for repeating myself, {i}nearly burned the classroom down a few minutes ago.{/i}"

    scene newponytail2
    with dissolve

    a "I already told you that was an accident!"
    a "None of this ever would have happened if they didn’t make those burner things so hard to use!"
    s "You literally just have to turn a knob. That's it."
    a "It’s a tough knob, okay?! You wouldn’t get it because you don’t have tiny girl fingers!"

    "As you may have heard, Ami nearly burned down the classroom today after getting into a fight with a Bunsen burner."
    "Sure, it may be my fault for allowing her to play with one unsupervised, but that’s beside the point."
    "The fact of the matter is, she now needs to help me clean up the remnants of the fire before the custodial staff shows up at the end of the day and I lose my job."

    scene newponytail3
    with dissolve

    a "Ugh...I know I shouldn’t be freaking out. It was my fault for not paying attention..."
    s "You're not trying to guilt me into letting you leave now, are you?"


    scene newponytail4
    with dissolve

    a "Me? Of course not...Why would I ever even try something as-"
    s "You can go to the cafeteria once we're done cleaning and not a second earlier."

    scene newponytail2
    with dissolve

    a "Ahhh! But who knows what could be happening to Maya within that time?!"
    s "Oh, come on. I'm sure she'll be fine..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Meanwhile...{/i}"

    scene lunch1
    with dissolve2

    y "…"
    m "…"
    y "…"
    m "…"

    scene lunch2
    with dissolve

    y "Why are you so fuckin’ weird?"
    m "I'm...sorry?"
    y "You heard me. Why are you so fuckin’ weird?"
    y "You’re always just...there. You know?"
    m "That...is an unfortunate side effect of my existence, yes."

    scene lunch3
    with dissolve

    "{i}Ahh...the[school] cafeteria...One of youth’s most dangerous battlefields.{/i}"
    "{i}If you're one of the lucky ones who have never had to spend a period like this alone, you can never truly comprehend what it means to be lonely!{/i}"
    "{i}The thing is, that girl with the ponytail right there? Well, a simple lunch alone means nothing to her.{/i}"
    "{i}For her, loneliness means something different.{/i}"
    "{i}Something much bigger.{/i}"
    "{i}But that’s something you're not ready to hear about yet!{/i}"

    scene lunch2
    with dissolve

    y "What’s your deal anyway?"
    m "My deal?"
    y "Yeah...you an ally? Or are you just another bitch who'll wind up on my shit list after we're done here today?"
    m "I'm not sure if I understand what type of {i}ally{/i} you're trying to equate me to."
    m "So, chances are, I am going to wind up on your list."
    y "So what you're telling me is you're a pussy?"

    scene lunch3r
    with dissolve

    m "I...don't think so? Maybe?"
    y "What I'm askin' is if you're one of those people who will try to keep yourself from gettin' fucked over and all that bullshit."
    y "I don't like hangin' around people who don't stand up for themselves, is all."
    m "But...what does that have to do with being an ally? What would standing up for myself make me an ally {i}of?{/i}"

    scene lunch3r2
    with dissolve

    y "You know..."
    y "You'd be an ally of...yourself. And shit."
    m "..."

    scene lunch6
    with dissolve

    m "I’m so confused..."
    y "Hey, Ponytail."
    m "That is not my name."
    y "Oh, please. Like I give a fuck what your actual name is."
    y "I’ve got a question for you."
    m "I will do my best to answer it in a way that will not compel you to hit me."

    scene lunch5
    with dissolve

    y "What do you think of our teacher? You hate his guts too, right?"
    y "You ain't like those other two girls you're always hangin' around. I can tell that much."
    m "You are correct. I am very much not like either one of them."
    m "In terms of our teacher- he is utterly revolting and thinking about him for extended periods of time makes me want to vomit."

    scene lunch8
    with dissolve

    y "Ha! I knew there was somebody else on the same page as me. Fuckin' finally."
    y "Was beginning to think everyone here was just trying to fuck him."
    m "Nope. Couldn't be me."
    y "I can’t fuckin' believe that guy sometimes, you know?"
    y "Like, it was barely a week ago that I caught him wandering the streets at night like some kind of...lost puppy."
    y "It was fuckin’ creepy, dude. He looked like he was gonna kill somebody. I’m lucky I escaped with my life."

    scene lunch9
    with dissolve

    m "That’s...certainly odd. Even by his standards- which only barely exist from what I've seen thus far."
    y "Yeah, it was {i}odd{/i} as shit. Real creep, that guy is. I can’t even believe-"

    scene lunch7
    with dissolve

    m "Wait, but what were you doing out that late?"
    y "What?"
    m "If you caught him wandering around in the middle of the night, wouldn't that make {i}you{/i} weird as well?"
    y "…"
    m "I'm just trying to understand your logic. Frankly, I know less about you than everyone else combined, so..."
    m "What if you're just weird too? Or something."
    y "…"
    m "…"

    scene lunch7r
    with dissolve

    y "You tryin’ to fuckin’ accuse me of something, Ponytail? You think I’m out late because I’m up to trouble, is that what this is?"
    m "That wasn't what I meant to imply. But-"

    scene lunch13
    with dissolve

    y "Save your fucking breath. No point explaining something that doesn’t {i}need{/i} any explaining."
    y "Shame. I was startin' to think you might be different in a {i}good{/i} way. Turns out you're just as pathetic as the rest of them."
    m "I think {i}pathetic{/i} might be a bit of a stretch."
    y "It ain't a stretch at all, Ponytail. You think I ain't seeing through that fuckin' dead-fish persona of yours? How you act all weird and quiet and shit just so you can get attention?"
    m "I feel like you are gravely misinterpreting my personality right now."
    y "Doubt it. Girls like you ain't got anything interesting about 'em at all. You're probably just some random ass Kumon-mi transplant trying to fit in in her own fucked up, ass backwards way."
    y "Yeah...where the fuck did you even come from anyway? I've lived here my whole life and I haven't even seen you until this year."
    m "This is a very hard conversation to keep up with so I am just going to eat my lunch if that is okay with you."
    y "The fuck was stopping you in the first place? Did I tell you not to eat?"

    scene lunch14
    with dissolve

    m "No, it's just..."
    m "…"
    y "…"
    m "…"
    y "The fuck are you waiting for?"

    scene lunch15
    with dissolve

    m "It just..."
    m "It feels weird with you staring at me."
    y "…"
    m "…"

    scene lunch16
    with dissolve

    y "Okay, that’s it. I’m getting out of here."
    y "For a second, I thought we might’ve had a chance to get along on account of our mutual hatred for the teacher...but you’re just too fuckin’ weird for me."
    m "Oh no. Please don't go. If you leave, who will watch me eat?"

    scene lunch17
    with dissolve

    y "Oh, get bent. Come talk to me if you ever decide to stop being a fuckin’ sketchball."
    m "Goodbye, Yumi. I apologize for being a sketchball."
    y "I said get bent, damn it!"

    scene lunch18
    with dissolve

    m "…"
    m "…"
    m "…"
    m "I forgot chopsticks."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene newponytail5
    with dissolve

    a "Ugh, finally done..."
    a "Who’d have ever thought cleaning up after a fire would be so difficult?"
    s "Probably...most people."
    a "Hopefully Maya didn’t gain 800lbs while I wasn’t there to supervise her..."
    s "You know, I wanted to say something before, but I don't think friends are supposed to be counting calories for one another."

    scene newponytail6
    with dissolve

    a "Most friends, probably not. But Maya is no normal friend, Sensei. The amount that girl is able to eat is one of the greatest mysteries of this world."
    a "She's even smaller than me, yet she can fit ten times as much in her mouth."
    s "Well, that's not a sentence I'm going to misinterpret at all. Thanks, Ami."
    a "Huh? I don't get it."
    s "And that's exactly what I like about you."

    scene newponytail7
    with dissolve

    a "I don't know what you mean by that, but it got you to say you like me so that's fine by me!"
    a "Now, come on! Maya should still be in the cafeteria and if we hurry, we might be able to save her from destroying her mysterious black hole of a body!"

    scene black
    with dissolve2

    "I follow Ami to the cafeteria and it's no surprise that I’m once again shrugged off by Maya as soon as we arrive."
    "Coincidentally, the cafeteria was also out of food when we got there."
    "In the end, Ami and I had to go the rest of the school day without eating..."

    $ renpy.end_replay()
    $ day28 = True
    stop music fadeout 3.0

    "………"
    "……"
    "…"

    jump afterschoolevent

label day30:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
...
```