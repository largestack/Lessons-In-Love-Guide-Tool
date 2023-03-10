# Slope Intercept Form (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 77



## Next events

* [Makoto: Declaration of War](./makotoinvite1.md)
* [Makoto: Studious Teen Virgin](./makotoinvite2.md)

## Event properties

* Id: day77
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day77

## Official wiki page

[Slope Intercept Form](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day77&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day77:
    scene amimak1
    with dissolve
    play music "phantomthief.mp3" fadein 4.0

    mak "...and that’s how you find slope-intercept form. Any questions?"
    a "Umm...could you please repeat...all of that?"

    scene amimak2
    with dissolve

    mak "Sensei, I have no idea what else I’m supposed to do. She’s just not retaining any information."

    scene amimak3
    with dissolve

    a "That’s just because you keep using big words and weird terms like ‘slope intercept form.’ Who the heck even knows what that is?!"

    scene amimak4
    with dissolve

    mak "Everyone! Or at least we’re supposed to!"
    mak "The next mandatory test is based almost entirely around this and, if you can’t even remember what it’s
    called, there is no way you’re going to pass."

    scene amimak5
    with dissolve

    a "Ahhhh! Why can’t all of our tests just be about how to be a good caretaker?!"
    mak "If you can’t even figure out slope intercept form, there’s no way you’re a good caretaker."

    scene amimak4
    with dissolve

    a "Those two things have absolutely nothing in common!"
    a "And besides, I’m a much better caretaker than you’ll ever be, Makoto!"
    mak "Take that back!"
    a "No!"
    mak "Yes!"
    a "No!"

    "So-"
    "I bet you’re probably wondering how I ended up in this position."
    "And, to be honest, I am too."
    "It all started with Ami coming up to me in class and asking for help with algebra."
    "I guess a boring thing like that must have caused Makoto’s geek-radar
    to go off because she immediately jumped up and volunteered to help coach Ami on the subject."
    "Of course, Ami wanted me around as well, so..."
    "Here we are. ‘Learning’ things."

    s "You two really don’t get along, do you?"

    scene amimak6
    with dissolve

    a "Makoto is just jealous because you spend more time with me than her."

    scene amimak7
    with dissolve

    mak "I-I am not! I’m just trying to help you so you don’t get held back!"
    a "See? She’s yelling at me to try and impress you but you’re not impressed at all, are you Sensei?"
    s "I’m...wait...what’s going on, exactly?"

    scene amimak8
    with dissolve

    if bonus == True:
        mak "Sensei! Tell her to focus or she’s never going to get into a good[school] and become a doctor."
    else:
        mak "Sensei! Tell her to focus or she's never going to get her doctorate!"

    scene amimak9
    with dissolve

    a "I don’t wanna be a doctor! I wanna be a housewife!"

    scene amimak10
    with dissolve

    mak "Who in their right mind would marry someone who doesn’t even know slope intercept form?!"
    a "None of your business!"
    a "I bet Sensei doesn’t even know the formula for that!"

    if bonus == True:
        "Please don’t drag me into this."
    else:
        "Does Ami really not know slope intercept form? She should have learned that years ago."

    mak "Preposterous! Of course he does!"
    a "No way! He doesn’t like boring stuff like that!"
    mak "It’s not boring just because it’s educational!"

    scene amimak11
    with dissolve

    mak "Sensei! What is the formula for slope intercept form?!"
    s "Uhh..."

    menu:
        "m = bx + y":
            s "Definitely ‘m = bx + y.’"

            scene amimak12
            with dissolve

            mak "Tch-!"
            a "Teehee~ Told you he doesn’t know!"
            a "Sensei isn’t interested in that kind of stuff!"
            mak "That’s simply not true! Of course he’s interested in that kind of stuff. He just had...a momentary memory lapse."
            mak "Things like that happen."
            a "Whatever you say, Makoto~"

        "y = mx + b":
            s "Easy. ‘y = mx + b.’"

            scene amimak13
            with dissolve

            a "Ah-!"
            mak "I expected nothing less from you, Sensei."
            a "Why do you know the answer to that?!"
            s "Hey, I might not be the best at showing it...or applying it...but I’m actually pretty smart."
            s "I’m offended you’d think otherwise, Ami."
            mak "If it’s any consolation, I’ve never judged you at all. I think you’re brilliant and wonderful and the best man I’ve ever met."

            scene amimak14
            with dissolve

            a "Hey! You watch it! I’m supposed to be the primary love interest
            and I’m not gonna let some smartypants glasses-wearer get in the way of that!"

            scene amimak10
            with dissolve

            mak "Who are you calling a smartypants glasses-wearer?!"
            a "The one who is a smartypants and is also wearing glasses!"

            "The two of them continue shouting at each other for another several minutes
            before I finally decide to step in..."

        "x = by + m":
            s "Definitely ‘x = by + m.’"

            scene amimak12
            with dissolve

            mak "Tch-!"
            a "Teehee~ Told you he doesn’t know!"
            a "Sensei isn’t interested in that kind of stuff!"
            mak "That’s simply not true! Of course he’s interested in that kind of stuff. He just had...a momentary memory lapse."
            mak "Things like that happen."
            a "Whatever you say, Makoto~"

    scene amimak15
    with dissolve

    s "Listen, you two. It doesn’t matter whether or not I know this formula. What matters is that both of {i}you{/i} do."
    s "I’d hate to see something as simple as this hold either of you back."

    if bonus == True:
        "And I’d also hate to get in trouble for having some of my students fail the standardized test."
        "Thank god that Makoto is able to tutor everyone on things that I can’t remember or never learned in the first place."
    else:
        s "Especially since you're both brilliant and talented and just all around wonderful people. I am thankful for the two of you every single day."

    mak "Well said, Sensei."
    mak "I mean, obviously you don’t have to worry about me. But those words are very wise when applied to everyone else."

    scene amimak16
    with dissolve

    a "Can't you just study with me instead, Sensei? Makoto is a mean teacher."

    scene amimak17
    with dissolve

    mak "I’m sorry, Ami...I just get frustrated whenever it seems like someone isn’t paying attention."
    a "So...you’re not gonna be a big meanie anymore?"
    mak "I...will do my best to not be a ‘big meanie...’"
    a "...Fine. I guess I can try a little harder, too."
    mak "So, can we finally move on with things?"
    a "Can you do one more thing for me, first?"
    mak "Of course. What do you need?"
    a "Can you admit that Sensei likes cute girls like me more than he likes nerdy ones like you?"
    mak "…"
    a "…"

    scene amimak18
    with dissolve

    mak "…"
    s "Hey, don’t look at me. I can’t control her."
    mak "She’s {i}your{/i} [niece]. Can’t you at least tell her to focus?"
    s "Uhh...I can try?"
    s "Ami, focus."

    scene amimak19
    with dissolve

    a "Yes, Sensei!~"
    mak "…"
    s "…"

    scene amimak20
    with dissolve

    mak "{i}Hah{/i}...how about we just take a break instead?"
    mak "We’ve been at this for an hour and haven’t really gotten anywhere, so maybe
    talking about something else for a little while might help?"

    scene amimak21
    with dissolve

    a "That works for me! I was getting tired of all the slopey stuff anyway."
    mak "It’s slope int- ahh, forget it. Let’s just talk about something the two of us have in common instead."
    a "Sure! Did you have anything in mind? The two of us have never really talked about stuff we have in common before."
    mak "That’s true. I don’t think I know much about you at all, Ami."
    mak "How about you tell me your top three interests and I’ll see if any of mine match up?"

    scene amimak22
    with dissolve

    a "Hmm...my top three interests...Okay. So, in no particular order-"
    a "Cats, rabbits, and Sensei."

    scene amimak23
    with dissolve

    mak "Your...[uncle] is in your top three interests?"

    if bonus == True:
        a "Of course. I love him and he loves me."
    else:
        a "Do you have a fucking problem with that Makoto? Do you want to throw hands? I'll fuck you up."

    mak "Isn’t that a little...uhh..."
    a "Hm? A little what?"
    mak "...Nothing."
    a "What are {i}your{/i} top three, Makoto? Do we have any of the same stuff?"

    scene amimak24
    with dissolve

    mak "Uhhh...well it’s kind of embarrassing to say this in front of him, but..."
    mak "I guess Sensei would be in my top three interests as well."
    mak "Of course, it’s just because of how much of a role model he’s been for me in terms of teaching and..."
    mak "Umm...yeah."

    scene amimak21
    with dissolve

    mak "So...I guess we could talk about that if you want."
    a "…"
    mak "…"
    a "…"
    mak "…"

    scene amimak25
    with dissolve

    a "…"
    mak "Ami?"
    a "I’m keeping an eye on you, Makoto..."
    mak "What? Did I...do something wrong?..."

    scene black
    with dissolve2

    "In the end, Ami never learned how slope intercept form works."
    "She wound up memorizing the formula, though, so hopefully she can just...figure it out come test-day."
    "As for the relationship between these two-"
    "Well...I’m starting to think it’s just destined to not ever work out..."

    $ renpy.end_replay()
    $ day77 = True
    stop music fadeout 4.0

    "………"
    "……"
    "…"

    jump afterschoolevent

label day79:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
...
```