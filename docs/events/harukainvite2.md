# Roses (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Shades of Green](./harukainvite1.md) (Haruka) is completed)

* harukaskipped equal to False (unknown variable)

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: harukainvite2
* Group: Haruka
* Triggered by label: harukainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->harukainvite->harukainvite2

## Official wiki page

[Roses](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukainvite2&go=Go) for more details.

## Event code

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label harukainvite2:
    play sound "phonebeep.wav"

    "I tap on Haruka’s name in my phone and wait for her to answer."
    "Ami isn’t going to be around today, but I feel like there’s a good chance Haruka will still refuse to come over on the off chance that that changes- and understandably so. "
    "The two of them meshed together just about as well as peanut butter and arsenic, so a refusal may very well be in the cards."
    "She’ll likely invite me to her house instead...but if the two of us are ever going to get anywhere, serious or not serious, some bridges need to be burned."
    "And yes, the bridge in this case has only existed for a combined total of three hours if you count all of the time she’s spent in my home."
    "But I want that number to grow."
    "And I’m also tired of riding the bus."
    "It smells bad and the seats are uncomfortable."

    play sound "phonebeep.wav"

    h "Hey, [harukamaster]. What’s up?"
    h "You busy tonight?"
    s "I am not. That’s actually why I’m calling."
    h "Cool beans. Can I come hang out at your place?"
    s "Wait, really? Even after how things went with Ami last time?"
    h "Oh, I’m not worried about her today."
    s "Why not?"
    h "Because she’s with Rin, Molly, and a few other girls I don’t know the names of right now. "
    h "They were all hanging out at one of the tables in the back of the cafe when I left."
    h "I’m actually still in the car now, so I can start heading over if that's okay with you."
    s "Yeah, that’s fine. I should be home soon anyway."
    h "Sweet! Gonna hang up now since talking on the phone and driving is illegal. Byeeee!"

    play sound "phonebeep.wav"

    "Haruka hangs up and I quicken my pace so I can make it home before she gets there."
    "I’d feel a little bad having her stuck in her car while I’m still walking and-"

    s "Wait."
    s "I could have asked her to pick me up..."

    scene black
    with dissolve2
    "………"
    "……"
    play sound "dooropen.mp3"
    "…"

    scene harukasecondinvite1
    with dissolve2
    play music "acoustic.mp3"

    h "Hey! Thanks for having me over again."
    h "And thanks for not immediately bringing up my chest the second I walked through the door."
    s "I learned my lesson last time. "
    h "You should teach Molly. She still does it at least five times every day."
    s "That’s it? I figured it would be more."

    scene harukasecondinvite2
    with dissolve

    h "Yeah, it’s actually a surprisingly low amount when you consider the type of person she is."
    h "But I was more or less the same when I was her age, so I get it."
    s "I can not imagine you being anything like that girl."

    scene harukasecondinvite3
    with dissolve

    h "I definitely wasn’t as...outgoing as her."
    h "But I was definitely on the geekier side and spent pretty much all of [high_school] being jealous of other, prettier girls."
    h "Also, my “assets” didn’t really grow in until later, so I didn’t have any of that same envy I  get from my employees and...apparently now your [niece]."
    s "Well, I’m glad you turned out the way you did."
    s "I’m probably biased since I see you pretty often, but I think you’re alright."

    scene harukasecondinvite4
    with dissolve

    h "Hey, cool. I think you’re alright too. What are the chances of that?"
    s "We have so much in common."
    h "We’re both adults."
    s "We both look after [teenage]girls for at least six hours every day."
    h "We both drink black coffee and wear...black shirts in the winter."
    s "We’re both moderately attractive."
    h "And great kissers."

    if harukasex == True and bonus == True:
        s "And we’ve both [masturbate]d to Rin at least one time."
        h "A lot more than once. Not gonna lie."
        s "Same."
        h "That girl can get it."
        s "I fully support you in your endeavors, Haruka."
        h "And I in yours, [harukamaster]."
        h "Though, you’ve got a much better shot at it than I do. Even {i}with{/i} the whole “preferring girls” thing."
        h "Not like I’m actively pursuing it or anything. I’m fine with living vicariously through you as long as you’re not stingy on the details."
        s "I will do my very best for the sake of your masturbation habits."
        h "Thanks. They’ve gotten pretty out of control over the last couple years."
        s "Well hey, at least you’ve got me now, right?"
        s "No point in masturbating if you can just give me a call and-"

        scene harukasecondinvite5
        with dissolve

        h "…"
        s "…"
        h "…"
        s "Haruka?"

        scene harukasecondinvite6
        with dissolve

        h "Oh, sorry. Right."
        h "Um, hey..."
        h "We’re still only just friends, right?"
        s "What do you mean?"
        h "Like, when you say that “I’ve got you,” you don’t mean I literally {i}have{/i} you."
        h "You’re messing around with a bunch of girls. And that’s totally chill."
        h "But like..."
        h "All you’re doing for me is...occasionally filling a void that...I have a hard time filling on my own."
        h "And we could stop doing it at any time and both be totally fine with it."
        s "I mean, yeah. That’s technically correct."
        h "Cool. Because I’m...definitely not interested in anything more than that."
        h "I like hanging out with you and...I have fun flirting, but..."

        scene harukasecondinvite7
        with dissolve

        h "I can’t help but feel really shitty about myself any time we actually...talk about what we do together."

        "Ahh..."
        "She’s still in denial."
        "In denial that I’m able to make her feel ways the man she “loves” can’t and was likely {i}never{/i} able to."
        "I’ve seen the way she falls apart beneath me."
        "In front of me."
        "On top of me."
        "But even though I’ve watched her break in so many ways, she still thinks she’s put together perfectly."
        "An uncracked porcelain doll."
        "How precious."

        s "There’s no need to talk about it at all then."
        h "Right."

        scene harukasecondinvite8
        with dissolve

        s "And it’s not like there’s any chance things will ever progress because-"
        h "Can we go in your room?"
        s "…"
        s "What, like, right now?"
        s "Isn’t this a weird time?"
        h "No. I’m starting to think about stuff and I need to get my mind off of it or I’m probably going to cry."
        h "I don’t want to cry here. I’d feel like shit."
        h "Just...help me take my mind off of things."

        scene black
        with dissolve2

        "Of course, we all know that the “things” Haruka wants to get her mind off of are how her husband is likely dead and about how, any minute now, she’ll be filled with another man’s seed."
        "And, if this were a different world- one where it was okay to replace old flowers with new ones after the initial inhabitants rot to death-"
        "That seed would form roots."
        "The roots would {s}turn to wires{/s} sink deep into the soil."
        "And bloom into a beautiful, sick rose."
        "I close my eyes and wish for God to exist so he can watch me pluck yet another fruit before it’s fully ripe."

        jump harukainvite2sex
    if harukasex == True and bonus == False:
        s "And exceptional huggers."
        h "Oh snap. Does this mean what I think it means?"
        s "That it's time to watch Wheel of Fortune and eat Chinese food?"
        h "You always say just what I want to hear."
        s "Let's put on weird hats and stare at people as they walk down the street."
        h "Yessssssssssssssss, I brought my grandmother's bonnet in hopes that this would happen."
        s "Can I be the one to wear it this time."
        h "Is my name Stephanie?"
        s "No."
        s "Oh."
        s "Damn it."

        scene black
        with dissolve

        "Haruka and I put on our weird hats but no one ever walks down the street."
        "Probably because no one actually exists and that this is all just some sort of illusion planted in my brain by the government."
        "Does Haruka even real?"
        "Who knows?"
        "Certainly not this guy."

        $ renpy.end_replay()
        $ harukainvite2 = True
        $ haruka_lust += 3
        $ harukasex = True
        stop music fadeout 8.0

        "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or lust with her!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

    else:
        s "I mean, I agree...But it's kind of weird for you to randomly bring that up again."

        scene harukasecondinvite9
        with dissolve

        h "Oh my god! I really didn’t mean to say that out loud..."
        s "Freaking out will just make it more awkward. It’s not really a big deal."

        scene harukasecondinvite10
        with dissolve

        h "Right. Because, when you’re married, it’s totally fine to just get drunk and make out with guys you barely even know."

        "And, of course, now it's awkward."

        s "I wouldn’t say you barely know me. You-"
        h "I don’t even know your first name."
        h "And the only reason I know your surname is because one of my employees told me."

        scene harukasecondinvite11
        with dissolve

        h "So don’t act like that was just some little thing. It was so much bigger than that."
        s "You were drunk. It happens."

        scene harukasecondinvite12
        with dissolve

        h "I fucking know that! But it shouldn’t!"
        h "I’m so fucking...{i}alone{/i} every day that I couldn’t help but jump on the first guy who showed me some sort of affection!"

        "Why is this happening?"

        h "Do you think I {i}want{/i} to feel this way about you?! Of course not!"
        h "But even now, I’m saying things that any sane, married woman would never say because I’m scared of what will happen if the guy I married never comes back!"

        if bonus == False:
            "Haruka stop, it was just a hug."
        else:
            h "And now, instead of thinking of my {i}husband{/i} fucking me any time I lay in bed and give into how pathetic I am, I’m thinking of you!"
            s "…"
            h "…"

        scene harukasecondinvite13
        with dissolve

        h "I’m sorry...that was totally random and uncalled for."
        h "I’m just...really...I don’t know..."
        h "I keep trying to bottle up what happened back then and...how you were nice enough to not take advantage of me..."
        h "But there’s an ugly part of me that..."
        h "May have wished you did..."

        if bonus == False:
            s "Sorry, Haruka. I only do consensual hugs."

        scene harukasecondinvite14
        with dissolve

        h "Why?..."
        h "Why’d he have to leave, [harukamaster]?"
        h "I miss him so much..."
        h "I miss not feeling like I’m the worst person in the world..."
        h "Being able to fall asleep at night..."
        h "And then waking up next to someone special to me..."
        h "I just want everything to go back to normal."
        s "…"
        h "…"
        s "What exactly do you want me to say to that?"
        h "…"

        scene harukasecondinvite15
        with dissolve

        h "Who knows?"
        h "I’m clearly an indecisive {i}bitch{/i} who can’t even sort her own feelings out."
        h "You really expect me to know what I want to hear from you?"
        h "I don’t know. Maybe I just needed to vent or something."
        s "Is venting enough?"

        if bonus == True:
            h "Probably not. But what else am I supposed to do? {i}Fuck{/i} you and just commit to being a horrible person?"
        else:
            h "Probably not. But what else am I supposed to do? {i}Hug{/i} you and just commit to being a horrible person?"

        h "Give up hope altogether and choose a physical connection over an emotional one I’ve had for years?"
        s "If that’s what makes you happy."
        h "What will make me happy is my husband coming back."
        s "You know I can’t do anything about that."
        h "Obviously."
        h "There’s nothing you can do that will fix everything and there’s nothing I can do to successfully cope."
        h "So what’s even the point? I lose no matter what."
        h "I just want to go home and sleep now that I’ve ruined any chance of you ever inviting me over again."
        h "Stupid Haruka. Stupid random emotional breakdowns."

        if bonus == True:
            h "Stupid sex drive. Stupid husband."

        h "Everything is stupid."
        s "…"

        "There are two options I have here."
        "And they’re ones that I’m familiar with since I’ve made this same choice in the past."
        "But now, it falls on me to decide things once and for all."
        "If I decide right now to leave Haruka and her marriage alone, I’ll be leaving things that way for good."
        "But..."

        if bonus == True:
            "If I’m okay with destroying everything she’s built over the years for an opportunity to sleep with her-"
        else:
            "If I’m okay with destroying everything she’s built over the years for an opportunity to hug her-"

        "I can tap into her vulnerability right now-"

        if bonus == True:
            "And be inside of her within the hour..."
        else:
            "And do the hug thing."

        menu:
            "Be a gentleman again":
                s "..."
                "I can’t do it."
                "Not when she’s still this torn."
                "If I’m going to be a homewrecker, I at least need the woman to be fully on board."
                "I honestly couldn’t care less about Haruka’s husband."
                "But, to some extent, I care about Haruka."

                if bonus == True:
                    "And there’s no way I’d be able to hold an erection if I know she’s miserable the entire time."
                else:
                    "And I am too kind to hug another man's wife."

                s "Maybe we shouldn’t hang out today after all."

                scene harukasecondinvite16
                with dissolve

                h "Hahaha...Yeah, I kind of deserve to be kicked out after that meltdown."
                h "I’m sorry. I’m clearly not in the right state of mind today."
                h "You’re a really good friend, Sensei."

                if bonus == True:
                    h "There are a lot of other guys who would have tried to take advantage of me after something like that, but..."
                    h "You were somehow able to resist."

                h "I really get why Rin likes you so much."
                h "You can be a great guy when you want to."
                s "The catch is that I don’t normally want to, so consider yourself lucky."
                h "I do. Really."
                h "And if there’s ever anything I can do for you that isn’t...you know..."
                s "Unfaithful and horrible?"
                h "Yeah. If there’s anything like that, just let me know."
                h "But, for now...I’m gonna head home."
                h "It obviously doesn’t have to be right away, but...I {i}do{/i} hope you’ll invite me back sometime."
                h "As friends..."

                scene black
                with dissolve2

                "{i}Interesting!{/i}"
                "{i}It seems that you’ve chosen a path that doesn’t make you feel bad about yourself.{/i}"
                "{i}Why?{/i}"
                "{i}You know that nothing is real, don’t you?{/i}"
                "{i}Now, you’re locked out of Haruka’s romance route.{/i}"
                "{i}What if her husband IS dead, huh? Then what?{/i}"

                if bonus == True:
                    "{i}You gonna fuck her on the rebound?{/i}"
                    "{i}Maybe shoot for a hot blowie in the bathroom of the cafe?{/i}"

                "{i}You’re strange.{/i}"
                "{i}You make strange choices.{/i}"
                "{i}I don’t like you very much.{/i}"

                $ renpy.end_replay()
                $ harukainvite2 = True
                $ harukaskipped = True
                stop music fadeout 5.0

                "{i}Haruka’s lust stays exactly the same because you have morals!{/i}"

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday

            "Fuck another man’s wife" if bonus == True:
                jump harukawhyx
            "Do the hug thing" if bonus == False:
                s "Haruka."
                s "I hope you are prepared."
                h "Prepared for what?"
                s "My birthday party next week."
                h "You're having a birthday party? Why didn't I find out until right now."
                s "Because it was a surprise."
                h "...For me?"
                s "Yeah."
                h "Why?"
                s "Ugh. This is why I didn't want to invite you."
                h "Wtf man?"
                s "Anyway, let's get this hug thing out of the way."
                h "Oh thank God. It's been so long that I was thinking I might never hug again."

                scene black
                with dissolve

                s "They don't call me {i}the hugger{/i} for nothing."
                h "Who calls you that?"
                s "The swim team. It's a long story."
                h "You should tell it to me sometime."

                "Haruka and I hug."
                "If her husband knew about it, he'd probably get really ticked off at me."
                "Take that, husband."

                h "Why are you sticking your tongue out?"
                s "Shut up."

                $ renpy.end_replay()
                $ harukainvite2 = True
                $ haruka_lust += 3
                $ harukasex = True
                stop music fadeout 8.0

                "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
                "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
                "………"
                "……"
                "…"

                if day >= 6:
                    jump endofsat
                else:
                    jump endofweekday

label harukadate20:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label harukainvite:
    if harukainvite1 == False:
        jump harukainvite1
    if harukainvite1 == True and harukaskipped == False and harukainvite2 == False:
        jump harukainvite2
...
```