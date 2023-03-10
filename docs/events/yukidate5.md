# Better Off Alone (Yuki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yuki love greater than or equal to 5

* Event [Walls Too Thick to Hear Through](./yumidorm30.md) (Yumi) is completed)

* Event [Rule #1](./yukidate1.md) (Yuki) is completed)

* yukinumber equal to True (unknown variable)



## Next events

* [Main: Operation: Firestarter](./day318.md)
* [Yuki: Opposite Directions](./yukidate10.md)

## Event properties

* Id: yukidate5
* Group: Yuki
* Triggered by label: callyukinight
* Triggered by branch label: callnight
* Triggered by path: callnight->callyukinight->yukidate5

## Official wiki page

[Better Off Alone](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yukidate5&go=Go) for more details.

## Event code

File: (install folder)\game\YukiEvents.rpy

Code:
```python
...
label yukidate5:
    play sound "phonebeep.wav"

    "I tap on Yuki’s name in my phone and wait for her to answer."
    "I don’t exactly call bearing great news or anything like that, but since Yumi seems adamant about keeping her distance, I should at least let Yuki know."
    "I’m sure she was expecting as much anyway."
    "I’m foolish for expecting anything else."

    play sound "phonebeep.wav"

    yu "Yo. Sup?"
    s "Hey. Are you doing anything tonight?"
    yu "Nope. If I answer, just assume I ain’t doin’ shit. "
    yu "Want to meet up at the usual spot?"
    s "Are you paying again?"
    yu "Ha. Not a chance."
    yu "That was a one-time only thing, pal. Don’t have enough to be buying dinner for you every time we meet."
    yu "Aren’t you a fuckin’ teacher anyway? Figured you’d be pretty much loaded or some shit."
    s "Teachers don’t make as much as you think they do."
    yu "That so? Sucks."
    yu "We’ll just buy our own shit then."
    yu "I’m close, so I’ll just wait for you there."
    s "Not going to offer to give me a ride again?"
    yu "And waste my gas on someone who ain’t even buyin’ me dinner? Nah. You’re walking."
    yu "See you soon."

    play sound "phonebeep.wav"

    "Yuki hangs up before I have the chance to retort and I quickly find myself shoving my hands back into my pockets and setting course for Tojo Ramen."
    "Tonight, I’m going to upset someone."

    scene black
    with dissolve
    stop music fadeout 5.0

    "Well, probably at least."
    "But I seem to inadvertently do that pretty often."
    "Does something like this still count as inadvertent if it’s a situation that I manufactured entirely on my own?"
    "Or do I need to rely on a term like “accident” and fall back on the hope that her own low expectations will act as a cushion for this poor turn of events?"
    "There is only one way to find out."
    "………"
    "……"
    "…"

    scene yukioutside1
    with dissolve2
    play music "thingsthathurt.mp3" fadein 5.0

    yu "Yo."

    "I turn the corner to find Yuki waiting outside of Tojo Ramen and make my way over to her."
    "I can smell cigarette smoke clinging to her jacket like her daughter clings to the hole inside of her heart."
    "A hole so big she can fit her fingers through it."
    "And, if she cares enough about her future, she might even have the chance to suture it back together."
    "Of course, there’s no chance it will ever work as well as the original version- the one that still had a mom."
    "But a heart is a heart."
    "Even if it’s ripped into pieces."

    s "Why are you out here? It’s freezing."
    yu "Is it?"
    yu "The cold never bothered me much, I guess."
    yu "But I imagine all those days of sleepin’ outside probably have somethin’ to do with that."
    yu "If you want to go in, we can. Just figured it’d be easier to talk out here."
    s "But Tsuneyo always has so much to add to the conversation."

    scene yukioutside2
    with dissolve

    yu "Hey, now. Leave the kid alone. She’s trying her best."
    yu "I didn’t even know she left this fuckin’ place until recently."
    s "Probably because she {i}didn’t{/i} leave this place until recently."
    yu "Then you should damn well know to cut her some slack. Unless you want to answer to me, of course."
    s "Are you threatening me now?"
    yu "I’ve got a history of lookin’ out for kids when I’m not too busy abandoning ‘em."
    s "Correct me if I’m wrong, but weren’t you in a biker gang?"
    yu "The fuck you think biker gangs do? Ride around and beat the shit out of people for no reason whatsoever?"
    s "…"
    s "Yeah. Pretty much."

    scene yukioutside3
    with dissolve

    yu "Yeah, well...you’re definitely not alone in thinkin’ that."
    yu "It’s a little more complicated, though."
    yu "Gangs for a lot of people are like families."
    yu "A place you can run away to and...start over, I guess."
    yu "Like a whole ass support group for people who fell on tough shit, lost their way, or just want to try something different."
    yu "People like me."
    s "Well that doesn’t sound intimidating at all."

    scene yukioutside2
    with dissolve

    yu "What, you scared of me or somethin’?"
    s "Not anymore now that I know you’re just a babysitter in a leather jacket."
    yu "Good. Means I don’t have to tell you about what happens to anyone that messes with people I care about."
    s "And now I’m back to being intimidated."

    scene yukioutside4
    with dissolve

    yu "Shit. Was {i}this{/i} close to havin’ somebody around who doesn’t think I’m some kinda scumbag."
    s "What about the rest of your...people? Or whatever gang members are called."
    yu "Most of ‘em are gone by now."
    s "Oh. "
    s "Well...I’m sorry to hear that."
    yu "Not {i}gone{/i} gone. Like they moved somewhere else and shit. Before the city closed up."
    yu "Not like I can follow after ‘em now."
    s "Why ever leave in the first place?"

    scene yukioutside5
    with dissolve

    yu "Good fucking question."
    yu "Answer is simple enough, though."
    yu "You ever meet someone who you think can turn your life around only to find out later that getting to know them made everything ten times worse?"
    s "I...don’t think so?"
    yu "Lucky."
    s "That’s what happened to you, I’m guessing?"
    yu "Yup."
    yu "Teenage girl. Poor as shit. Only one outfit to my fuckin’ name. Relyin’ on other girls in the gang just so I could eat a few nights a week."
    yu "Then along come these dudes who think they’re tough shit for walking up on some tiny ass runaway out by herself at night."
    yu "Cornered me. Pushed me to the ground. Fucked up my only shirt."
    yu "And then I bashed their fucking brains in with a loose pipe I pulled off the side of some building."
    s "The way this story began, I had the feeling that someone was going to come rescue you or something."

    scene yukioutside6
    with dissolve

    yu "Nope. The complete opposite, actually."
    yu "The guy I’m talking about, Yumi’s dad, was one of those fucking punks."
    yu "Granted, he never laid a finger on me. Just cowered in the corner while I fucked his stupid ass goons up."
    yu "But, after all that was done, he came up to me and started sayin’ all this shit about how he’d never seen a girl so strong before. "
    yu "Offered to buy me new clothes. Said he wouldn’t rat me out and shit and that all those guys were scum anyway."
    yu "Just...kept spittin’ out all these nice words that I couldn’t even process because I was still high off adrenaline."
    yu "In hindsight, he was probably just fuckin’ fearing for his life."
    yu "But when you’re a runaway without a penny to your name and some dude in nice clothes pulls out his wallet and starts offering to buy you shit, it’s hard to just fuckin’ walk. You know?"
    yu "Like, what if he was my ticket out?"
    s "So you...went home with some guy who was going to just sit there and watch a bunch of other guys do god knows what to you?"

    scene yukioutside7
    with dissolve

    yu "I was a fuckin’ naive [teenage]girl who’d never seen so much money before. "
    yu "Plus he was kind of cute, I guess."
    yu "So it was either take a chance on him, a dude I knew I could fuck up if he tried anything on me-"
    yu "Or wander back to my crew with my tits basically hangin’ out of my shirt without any idea of when I’d be gettin’ a new one."
    yu "Easy choice then and there. But {i}fuck{/i} if it's not the biggest regret of my life."
    s "And here I was thinking Yumi’s dad was some intimidating mob boss."

    scene yukioutside8
    with dissolve

    yu "Intimidating? That piece of shit? Not a chance."
    yu "There are some people who work for power and some people who are just born with it."
    yu "Which one do you think he is after hearing all that?"
    s "I’m pretty sure I can guess, but..."
    s "I’m still not really getting why you wound up staying with him if he was so horrible."

    scene yukioutside9
    with dissolve

    yu "What part of “he was fucking loaded” do you not understand?"
    yu "I could eat. Get high. Sleep in an actual futon. "
    yu "And, shit...I could even afford to dress nice when I wanted to."

    if bonus == True:
        yu "And all I had to do was suck his tiny fucking cock every once in a while in order to keep doing all that."
    else:
        yu "And all I had to do was read him bedtime stories and tell him everything was going to be okay in order to keep doing all that."
        s "That sounds nice."

    yu "Shit went on for years."

    if bonus == True:
        yu "Wasn’t a bad gig at all until he fuckin’ took advantage of me while I was high out of my mind one night."
        s "..."
        s "Is that..."
    else:
        yu "Wasn’t a bad gig at all until the stork came."
        s "So {i}that{/i} is how Yumi happened."

    scene yukioutside10
    with dissolve

    yu "Yup."
    yu "Was so fuckin’ out of it that it took me two months to even realize I was knocked up."
    yu "Guess you can probably figure out what happened after that."
    s "Does Yumi know all this?"

    scene yukioutside11
    with dissolve

    yu "No. And you’re not going to fucking repeat a word of it to her either, got it?"
    yu "It’s bad enough that she had to pop out of {i}me{/i}. You have any idea how much it would fuck her up to hear how it actually happened?"
    s "But something like that might completely change her outlook on-"
    yu "And what if it did?"
    yu "Think we’d be able to just start over after she finds out she was never planned?"
    yu "Think it will excuse all of the times I passed out while watching her?"
    yu "Will it excuse me leaving?"
    s "…"
    s "No."
    s "It won’t."

    scene yukioutside12
    with fade

    yu "She was such a cute fucking kid. And I fucking hate babies. They never shut the fuck up."
    yu "Do you want to know what her first word was?"
    s "I’m guessing “Mama?”"
    yu "What? No. Her first word was “Fuck.”"
    yu "Shit was hilarious."
    s "I am somehow not at all surprised by this."

    scene yukioutside13
    with dissolve

    yu "I’m assuming you talked to her about meeting up with me, right?"
    s "…"
    s "It didn’t exactly go well."
    yu "I didn’t think it would."
    yu "Thanks for trying, though. "

    if bonus == True:
        yu "Probably the first guy I’ve ever met who’s done something for me without trying to get into my pants."
        yu "But I’m still not convinced you’re not fucking my daughter. So you’re probably pretty satisfied in that area already."
        s "Uhh..."

    scene yukioutside14
    with dissolve

    yu "God, she’s so fucking pretty now."
    yu "She looks nothing like me either. Good for her."
    s "You have the same eyes at least."

    if bonus == True:
        yu "Yeah but her tits are like two sizes bigger than mine and she’s not even half my age. The fuck is that about?"
        s "I’m still slightly intimidated by you, so I’m going to try and refrain from commenting on your [teenage]daughter’s breasts."

        "That does not mean I won’t think about them, though."
        "They are...very nice."

    scene yukioutside15
    with dissolve

    yu "Whatever you two are doing together is fine. I don’t care."
    yu "Like I said, you seem like a good guy. And it’s not like I’m a good judge of character anyway."

    if bonus == True:
        yu "Just wear a fucking condom so she doesn’t also wind up pregnant before she’s ready."
        s "Okay, let’s talk about something else now."
        yu "Nah, fuck that. Not until you agree to the condom thing. "
        s "I agree to the “condom thing.” Now please stop talking about my entirely wholesome and not-at-all suspicious relationship with your daughter."

    yu "So, now what then? "
    yu "You done hangin’ out with me now that you know Yumi’s not gonna be involved?"
    s "I was actually thinking of asking you the same thing."
    s "You’re the one who wanted to check in on her and have made it very clear that our meetings aren’t dates. "
    s "I just figured you wanted to probe someone close to her for info without really getting in the way."
    yu "Well, yeah. That’s definitely true."
    yu "You’re alright, though. We can still chill if you want. "
    yu "Not like I ever have anything to fuckin’ do."
    s "No dates, though?"

    scene yukioutside16
    with dissolve

    yu "The fuck is it with you and all this dating shit? "

    if bonus == True:
        yu "There are like thirty different [teens] trying to jump your bones and you’re hitting on a recovering addict in her late 30’s. "
        s "I hit on virtually everyone. I’m sure you’ll get used to it."
        yu "We’ll see about that."
    else:
        s "I just want to feel loved."

    yu "I’m kind of staying out of the game for now, though."
    yu "As you’ve heard, my track record with men is kind of shit. "
    yu "I’m better off stayin’ a loner. And {i}you’re{/i} better off not gettin’ involved."
    yu "‘Specially since my daughter would kick your fucking ass if she found out we were together right now."
    s "I’m going to keep this hidden from her at all costs. Don’t you worry."
    yu "Appreciated."

    scene yukioutside17
    with dissolve

    yu "Oh, and sorry for dumping all of that shit on you tonight."
    yu "I realized halfway through that I was ventin’ to some dude who probably did not give two shits, but it’s been a long time since I’ve actually been able to say any of that."
    yu "Only other person in Kumon-mi who knows outside of the fuckin’ Yakuza is Tsu-chan."
    s "I can’t imagine Tsuneyo was very helpful in that regard."
    yu "She’s actually a really good listener. "
    yu "Io, on the other hand..."
    yu "Yeah, it’s probably better if she never hears any of that."

    if bonus == True:
        s "Is this that “protecting kids” setting of yours that you were talking about earlier?"

        scene yukioutside18
        with dissolve

        yu "It’s the best I can do since mine has already given up on me."
        yu "They’re all good girls."
        yu "Hurt any one of them and I will rip your fucking dick off."
        s "…"
        s "You and Yumi really do have a lot in common."

    scene black
    with dissolve2

    "Yuki and I head into Tojo Ramen and order a quick dinner."
    "It’s already really late by the time our food arrives, so we scarf it down, pay for ourselves and head on our way."
    "I’m not exactly sure what this means for the beginning of our relationship-"
    "And I’m even less sure of how (And if) Yumi will ever fit into it."
    "But at least I have one more person to talk to in the middle of the night now."

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate5 = True
    stop music fadeout 10.0

    "{i}Yuki’s affection has increased to [yuki_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yukidate10:
...
```

## Code that triggers this event

File: (install folder)\game\YukiEvents.rpy

Code:
```python
...
label callyukinight:
    if streets30 == False or ramen20 == False:
        "I should probably make sure I'm caught up with Yumi and Tsuneyo before giving Yuki a call."
        jump callnight

    if yuki_love >= 0 and streets30 == True and ramen20 == True and yukidate1 == False:
        jump yukidate1
    if yuki_love >= 5 and yumidorm30 == True and yukidate1 == True and yukidate5 == False:
        jump yukidate5
...
```