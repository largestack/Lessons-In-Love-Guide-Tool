# I Thought of You (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 20



## Next events

None

## Event properties

* Id: day20
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day20

## Official wiki page

[I Thought of You](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day20&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day20:
    scene daytwenty1
    with dissolve
    play music "10c.mp3"

    "It’s another average day in the classroom."
    "Or at least average by my standards. I'm sure the other classes are actually studying right now."
    "But ever since I took over and decided to just let the girls study on their own time, things have more or less just...been like this."
    "Even Makoto seems to be settling into this new routine. So apart from Yumi, who still only shows up once in a while, it appears that everybody seems to be enjoying themselves."

    if bonus == True:
        "The great part is that it doesn't seem classes are ever monitored here. So as long as I can submit everyone's grades on time, I should be able to dodge suspicion entirely."
        "All that's left to do now is...figure out how to submit everyone's grades."

    scene black
    with dissolve2

    "I sigh to myself and lean back in my chair, already excited for the day to come to an end so I can get out of here and actually do something fun with my time."

    s "..."

    "It is at that moment when I realize that all I have to do in order to make that happen is go to sleep."
    "And so that is precisely what I will do."
    "Goodnight, everyone."
    "Please don't cause any trouble while I am gone. And, in the event that I wake up without my memories, please ask Ami to once again escort me home."
    "........."
    "......"
    "..."
    "{i}Several minutes later...{/i}"

    scene daytwenty2
    with dissolve

    r "…"
    r "…"
    r "…"

    scene daytwenty3
    with hpunch

    c "Hey!"
    r "Ahh! Hand!"
    c "Something going on outside? You’ve been staring at the window for like ten minutes now."
    r "Uhhhh...air! That's where all the air is! And the...uhh...birds!"
    r "Anyway, good talk! Thank you!"

    scene daytwenty4
    with dissolve

    c "Did I scare you or something? I wasn't trying to sneak up on you like that."
    r "Huh? What? No? Scared? I've never been scared of anything in my life. Not even once."
    r "Do, umm...do you need something?"

    scene daytwenty5
    with dissolve

    c "Nah..."
    c "Just thought I'd come say hi since you seemed all lonely and stuff."
    c "I can leave if I'm bothering you, though. I put up with Yumi on a daily basis, so I know pretty well how much some people need their alone time or whatever."
    r "{i}I am never washing this cardigan again.{/i}"

    scene daytwenty5r
    with dissolve

    c "Hm? You say something just now?"
    r "Nope! Nothing at all! Just...thinking about...things. And stuff."

    scene daytwenty6
    with dissolve

    c "Well, speaking of {i}things and stuff,{/i} I was actually thinking about you this morning."
    r "You...of me?....Thinking? With brain?"
    c "Chika think of Rin with brain, yes."
    r "Why brain think?! Why?!"
    r "Surely your...free time is better spent on...being pretty. And...smelling nice."

    scene daytwenty6r
    with dissolve

    c "Oh, stop! We've known each other for how many years now? I'm allowed to think of you if I want to, dummy."
    r "{i}Relax, Rin. You fell asleep in class and this is all just a dream. But still, try not to say anything awkward.{/i}"
    c "Oh my god. You are like, totally hilarious."

    scene daytwenty6r2
    with dissolve

    r "So...umm...{i}why{/i} were you thinking of me, exactly? If that's...a thing I'm allowed to ask about."
    c "I just heard this band on my Discover Weekly this morning and they seemed like something you'd be into."
    c "I think I remember you having one of their shirts back in middle school and everything."
    c "You don't think it's weird, do you? That I remember that and stuff."
    r "No...No, that's not weird at all! I'm actually really flattered!"
    r "I...remember stuff about you from back then as well, so..."
    c "Do you? Like what?"
    r "Like...umm...that one week where you came to school with green hair because your hair didn't bleach correctly..."
    c "..."
    r "..."

    scene daytwenty6r3
    with dissolve

    c "That's what you remember most about me?! Why does your biggest middle school memory of me have to be one of the most embarrassing weeks of my life?!"
    r "I didn't think it was bad or anything! I actually thought you...kind of pulled it off."
    r "But...you also pull off, like...literally everything, so..."

    scene daytwenty7
    with dissolve

    c "God...that feels like, so long ago now. It's crazy to think it's only been a couple of years."
    c "How come we never hung out?"
    r "Because...you're popular and awesome and everyone likes you. And I'm just Rin."

    scene daytwenty9
    with dissolve

    c "Well, I think Rin is pretty great. And I'm not {i}that{/i} popular. The only reason I have so many followers is because I keep up with trends and stuff. It's really no big deal."
    c "Speaking of that, though, how do you like having the corner desk? It's probably really easy to hide your phone, right?"
    r "It is, yeah..."
    r "Not like we really {i}have{/i} to hide it anymore, though, with Sensei still in the throes of his midlife crisis."
    c "You really think that's what it is? Maybe he's just been kinda cool this whole time and we've just...never realized it."
    r "Well...whatever it is, it's definitely an improvement."

    scene daytwenty10
    with dissolve

    if rin_love > 4 and rinfirstvisit == False:
        r "He’s like...a totally different person lately."
        r "He's even been coming to the cafe lately and letting me try out new drinks on him."
        r "It just...came out of nowhere."
        c "Right?"
        jump restofrin

    if rin_love > 4 and rinfirstvisit == True:
        r "He’s like...a totally different person lately."
        r "This might sound kinda weird, but he even came into my room the other day. I wasn't expecting that at all."

        scene daytwenty10r
        with dissolve

        c "What? You let him into your room? But, like...what if he tried to...you know."

        if bonus == False:
            c "Hide a twig under your pillow?..."

        scene daytwenty5r
        with dissolve

        r "Sensei? No way. It wasn't like that at all."
        c "You sure? What if he's got a crush on you or something?"
        r "Not a chance. He's...way older than us. He was probably just...really bored or something."
        c "Older guys are into teenagers all the time, Rin. I don't think it's impossible, you know?"
        r "I told you, it's not like that. Besides, I'm like, last on the list of people who would be his type. I think."
        r "I actually don't really know. But there's no way he has a crush on me."


        scene daytwenty10
        with dissolve

        c "Whatever you say..."
        c "I do get what you mean by the whole {i}different person lately{/i} thing, though."
        jump restofrin

    else:
        r "He’s like...a totally different person lately."
        c "Right?"
        jump restofrin

label restofrin:
    c "It's like...not just {i}him{/i} either. It feels like the entire class has been different for the last couple weeks."
    c "It barely even feels like school anymore."

    scene daytwenty10r2
    with dissolve

    r "What, do you like...miss learning all of a sudden or something?"
    r "I always thought you hated studying."
    c "I don't {i}hate{/i} it! It's just boring."

    scene daytwenty10
    with dissolve

    c "I wonder if something happened to him. People don't just change like that overnight, do they?"
    r "I’m sure he’s fine. If anything was going on with him, I'm sure I'd hear about it from Ami anyway."

    scene daytwenty11
    with dissolve

    c "Well, let me know if you {i}do{/i} hear anything, since I'm just as curious about all this as you are."
    c "Also, hang out with me some time. If you're free, I mean."

    scene daytwenty11r
    with dissolve

    r "H...Hang out?! You and me?! Together?! In the same place?!"
    c "Yeah! It’ll be fun. Just come get me after class sometime. We’ll go shopping or get dinner or something."
    r "..."
    c "..."
    c "Is that...cool with you? Or should we just stay as like, school friends or something?"
    r "I'm sorry, I just...I wasn't expecting you to actually want to be around me."
    c "Well, I'll let you sleep on it. But, like I said, just come get me after school if you ever want to do something."
    c "As long as I don't have anything else going on, I'd be happy to chill with you."
    c "I should probs be heading back to my seat now, though. Need to do at least {i}some{/i} studying if I want to pass, you know?"
    c "But I'll see you around, Rin. It was nice chatting with you."
    r "Yeah..."
    r "Yeah it was...really nice..."

    scene daytwenty12
    with dissolve

    r "..."
    r "..."
    r "..."
    r "Futaba...was I hallucinating just now? Or did that really just happen?"
    f "Heheh...it really happened, Rin."
    r "I see..."
    f "How do you feel?"
    r "Dizzy. Very dizzy."
    r "I am going to sleep now. But if I start making weird noises or talking or something, please hit me."
    f "I will hit you with the biggest book I have..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ day20 = True
    stop music fadeout 5.0

    "........."
    "......"
    "..."

    jump afterschoolevent

label day21:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

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
...
```