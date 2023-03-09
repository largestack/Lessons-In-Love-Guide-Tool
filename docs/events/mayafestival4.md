# Everlasting Mercy
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayafestival4&go=Go)


Part of event chain [As The Sun Disappears](./mayafestival3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Kaori: Såsom i en Spegel](./kaoridate20.md)

## Event properties
* ID: mayafestival4
* Group: Maya
* Triggered by label: mayafestival3

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label mayafestival4:
    play music "ihaveto.mp3"
    scene hanabi1
    with dissolve4

    "When was the last time you felt alive?"
    "Because in this moment, I feel more alive than I have in a very, very long time."
    "Something about how small everything looks from all the way over in this unknown part of the world makes even breathing exciting."
    "I time my inhalations to match the explosions in the sky. "
    "My lungs hate me for it, but my heart has hated me for much longer."
    "Pretty soon, every last organ in my body will give up on me."
    "I’ll be left decaying in a bed somewhere, wondering why I didn’t take more time to appreciate moments like this."
    "I hope that wherever that bed is, there’s a window."
    "And I hope that the view from it will be even half as nice as this one."
    "I wonder if she ever saw anything like this."
    "I wonder if she’d appreciate it as much as I do."

    m "I feel bad for the people living directly underneath all this."
    m "It’s nice from up here, but I can’t say I’d be very happy if there were fireworks above my house periodically throughout the year."
    s "I’m surprised they’re even doing something like this over here. "
    s "It looks like they’re being lit off in that forest over there. "
    m "Do you have a sudden interest in fire prevention or something?"
    m "There’s nowhere else to light them off around here. "
    m "It’s not as if they can be set off over a lake or river when the closest bodies of water are miles away."
    s "Oh well. Sucks for everyone trying to get some sleep right now, I guess."
    m "It certainly does. We’ll just have to continue enjoying this at the expense of everyone below us."
    s "I’ve gotta say, this seems like a pretty high budget affair for a part of Kumon-mi no one really travels to."
    m "Fireworks are relatively inexpensive. And, from what I understand, all of the lanterns and stalls were put together by the people still living here."
    s "And the six thousand vendors we bought food from?"
    m "Individually funded, I assume. I’m sure there were some vendors from the other districts too."
    s "Does this district have a name?"
    m "If it does, I don’t want to know it."
    s "Why does everything always have to be a mystery with you?"
    m "Because the only thing worse than being stuck in one place for all eternity is being stuck in one place and knowing everything about it."
    m "Missing details give me more to think about."
    s "No wonder why you’ve been smiling so much lately."
    m "Yes, it’s quite nice being able to do that in between the incessant bouts of emotional turmoil and mental strain."
    s "At least you can relax now."
    m "How unfortunate that an entire village must suffer for it."

    scene hanabi2
    with dissolve2

    "The fireworks don’t let up. But, in between the bursts of light, we can still hear the chatter from the festival below."
    "It seems that the later it gets, the more people show up."
    "And while plenty of them seem focused on tonight’s display, there are plenty others who don’t."
    "There’s even a surprising amount of men here- something I haven’t been able to say in...I guess what would be the equivalent of about a year in recycled time."
    "Maybe two?"
    "I’ve stopped keeping track of how long it takes for anything to happen here."
    "There’s just no point to it when you know that all clocks have stopped rotating in any meaningful way."
    "Surprisingly enough, I don’t hate the voices from below."
    "It’s hard to put it into words, but even this wide array of loud, intrusive noises feels incredibly quiet atop this hill."
    "Occasionally, a gust of wind will attack us from behind in an attempt to distract us from gazing too long at something neither of us deserve to see, but we pay it no mind- for we’ve already spent all we have."
    "That’s right."
    "Neither one of us has anything left to spare."

    m "Can I interrupt this moment to be cliche once again?"
    s "Sure. Just don’t put your hand in front of my face when you raise it up to the sky to measure stars or whatever. I’m actually enjoying watching these."
    m "I won’t."
    m "It’s just that, as the resident astronomy expert of our make-believe manga, I’m obligated to tell you the story of Altair and Vega at least once before the series concludes."
    s "That’s fine. You’ve gone the entire day without talking about the stars."
    s "I yield the floor to you now as a reward for your good behavior."
    m "Vega- or Alpha Lyra, which is the fifth brightest star in the entire sky...was said to be some sort of celestial princess according to Chinese mythology."
    m "Under the impression she’d be alone for all eternity, Vega began to lose hope and grew depressed."
    m "But, one day, a random mortal by the name of Altair showed up and Vega thought, “You know what? Fuck it. I’m lonely and this is the best I can find.”"
    s "I feel like every other iteration of this story I’ve heard has started off a little more romantic."
    m "Yeah, well, sometimes it doesn’t really work that way."
    m "Anyway, as Vega and Altair began to spend more time together, the two of them gradually started to fall in love- even though she was significantly better than him in every way."
    m "Vega promised Altair that, no matter what happened, the two of them would always be together. And since she was a goddess of the sky, Altair knew she meant business."
    m "But when Vega’s father found out about this, he got extremely pissed off."
    m "It was one thing for Altair to be mortal- but hearing that his daughter promised a seemingly eternal life in the heavens to her lover...saying Vega’s father was infuriated would be a bit of an understatement."
    m "In a fit of passive aggressive rage, he used his power to grant Vega’s wish- but in the worst way possible."
    m "The two of them were placed into the sky as stars, but separated by the Milky Way."
    m "They were {i}together{/i} in a technical sense, but as far apart as possible."
    m "But every year, on the seventh night of the seventh moon, a bridge would form across the Milky Way...and Altair would cross over to meet his lover."
    m "One night every year, the two of them could be together."
    m "But once the night would come to an end-"
    s "You don’t have to tell me how the story ends. I already know it."
    s "Besides, it’s too sad anyway."

    if bonus == True:
        s "Here’s hoping that Altair and Vega can stay together this year and have tons of white-hot, celestial star sex with each other."
    else:
        s "Here’s hoping that Altair can get Vega hugnant."

    m "You’re disgusting."
    s "You’re a nerd."

    scene hanabi3
    with dissolve2

    m "..."
    s "..."
    s "Does-"
    m "Don’t talk. You’ll just ruin everything."
    s "Fair enough."

    "Maya rests her head upon my shoulder. And while I can’t see her face, I can feel the smile count increase by one."
    "We meet on the other side of a bridge of magpies and, for just one night, detach ourselves from the rules that govern us every other day of the year."
    "Or at least that’s what we would do if we were stars."
    "But neither one of us is anywhere near bright enough to come close to one of those."
    "And even if, by some strange twist of fate, we were placed in the night sky along those same lights Maya dedicates at least ten hours a week to staring at-"
    "Even if that were to happen, I doubt the Milky Way could keep me from her."
    "I like annoying her far too much to let something like that get in the way."
    "The two of us may share some connections to those literal star-crossed lovers, Altair and Vega-"
    "But we’re our own creatures."
    "And there’s a high likelihood that there are {i}other{/i} creatures looking up at {i}us{/i} from somewhere underneath-"
    "And that they’ll hand down stories about us for generations and generations, despite how depressing or unfortunate they may be."
    "Hopefully, the stars can hear their story one day."

    s "..."
    m "..."
    m "Why did you tense up just now?"
    s "I just had some really immature, star-related thought that you would probably think is cute."
    m "Don’t share it. You and {i}cute{/i} don’t belong in the same room together."

    if bonus == True:
        s "I guess that defeats any chance of us ending up at a love hotel tonight, then."
    else:
        s "I guess that defeats any chance of us ending up in my bedroom playing with my Pokemon cards after this, then."

    m "As if that chance ever existed in the first place."
    s "I feel like it did."
    s "Or does."
    s "I feel like-"
    m "Shut up and watch the fireworks."
    m "The grand finale is close."
    m "I can feel it."
    s "..."
    m "..."
    s "Okay."

    if bonus == True:
        scene hanabi4
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi3
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi4
        with dissolve2
        $ renpy.pause(2, hard=True)
        scene hanabi3
        with dissolve2
        $ renpy.pause(2, hard=True)
        stop music
        play sound "static.mp3"
        scene magpie with flash
        scene black with flash
        scene magpie with flash
        scene black with flash
        scene magpie with flash
        scene black with flash
        scene black
        with flash
        stop sound
        $ renpy.pause(10, hard=True)
        play sound "static.mp3"
        scene smile with flash
        scene hanabi5 with flash
        stop sound
        play music "undoitall.mp3"

        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."
        "..."

        "The sky!"
        "An egg, an egg- what’s in an egg?"
        "A chicken?"
        "A duck?"
        "Another white egg?"
        "Maya’s hands find their way to mine."
        "They fuse together into one larger hand."
        "////////////////ADD HAND"

        scene hanabi6
        with pixellate

        "////////////////HAND SUCCESSFULLY ADDED"

        m "I had a dream that I was flying."
        m "You were there, but it wasn’t actually you."
        m "We were on the roof. The same room. At different times. The same place."
        m "The sky turned black and I felt a bubble begin to form underneath my forearm."
        m "You approached me and helped me pop it."

        play sound "static.mp3"
        scene hanabi7
        with flash
        stop sound

        m "From out of the bubble oozed a thick, yellow liquid."
        m "You lapped it up like a cat and told me that we would be better for it."
        m "I never forgot the sensation of that bubble popping. Or the tip of your tongue as it explored the inside of my arm."

        play sound "static.mp3"
        scene hanabi8
        with flash
        stop sound

        "I knew right then that it was egg time."
        "The hard-ish but not that hard white oval in my hand, reminiscent of holding a half-complete baseball- where the insides are all messed up and confusing when unwound."
        "Have you ever egg before?"
        "I would not recommend it unless you are ready."
        "Sometimes, people think they can egg when they can’t."
        "Then, before you know it-"

        play sound "static.mp3"
        scene hanabi9
        with flash
        stop sound

        "Squid!"
        "But why squid?"
        "This is second time squid show up in special Maya event chain! Not understand!"
        "Me teach."

        play sound "static.mp3"
        scene hanabi10 with flash
        stop sound

        "Everything in the waters that has fins and scales, whether in the seas or in the rivers, you may eat."
        "But anything in the seas or the rivers that has not fins and scales, of the swarming creatures in the waters and of the living creatures that are in the waters, is detestable to you."
        "You shall regard them as detestable; you shall not eat any of their flesh, and you shall detest their carcasses."
        "Everything in the waters that has not fins and scales is detestable to you."
        "This is my word."
        "Egg is okay, though."

        play sound "static.mp3"
        scene hanabi1 with flash
        stop sound

        m "Oh, I forgot."
        m "I got something for you."
        s "For me?"

        play sound "static.mp3"
        scene hanabi11 with flash
        stop sound

        m "Yes."
        m "I figured that it would be best to uphold this tradition as well, given my hesitancy when it comes to accepting change."
        s "What is it?"

        play sound "static.mp3"
        scene hanabi11x
        with flash
        stop sound

        m "A box."
        m "I don't have it with me."
        m "In fact, it's not really a present at all. I just need your help carrying it."
        s "Am I at least allowed to know what’s in it this time?"

        play sound "static.mp3"
        scene hanabi12
        with flash
        stop sound

        m "Only if you can open it."
        m "In the event that you can’t-"
        a "Sensei?"
        s "..."
        m "Wait, are you okay? You feel...ten degrees colder all of a sudden."
        a "Is...everything okay?"
        s "Everything is okay."

        play sound "static.mp3"
        scene hanabi4 with flash
        stop sound

        s "Everything is okay."
        m "I see..."
        m "Then, if you’re okay with it-"

        play sound "static.mp3"
        scene hanabi13 with flash
        stop sound

        m "I’d like to stop by both my dorm room and the school once we’re done here."
        m "It’s a little cold to be wearing a yukata anyway."
        m "I figured it would stay warm for a little longer."
        te "What’s wrong?"
        te "We won’t have time to play if you don’t hurry up and help me finish here."
        s "Yes. It {i}is{/i} too cold for a yukata."
        te "Yukata? What are you talking about?"
        s "I-"

        play sound "static.mp3"
        scene hanabi4
        with flash
        stop sound

        av "Do you ever feel yourself coming unglued?"
        av "How much skin comes off as you peel yourself to freedom?"

        play sound "static.mp3"
        scene hanabi14
        with flash
        stop sound

        ay "One very large banana!"

        play sound "static.mp3"
        scene hanabi15
        with flash
        stop sound

        c "Come on! Take the picture already!"
        mi "We ain’t got all day, Sensei!"
        mak "Yeah, Sensei!"
        r "Y-Yeah, Sensei! What are you waiting for?!"
        f "What are you waiting for?"
        y "What the fuck are you waiting for?"
        m "What the fuck are you waiting for?"

        play sound "static.mp3"
        scene hanabi16
        with flash
        stop sound

        s "Huh?"
        m "What are you waiting for?"
        m "You’ve been holding that box and staring into space for about a minute now."
        s "Weren’t..."
        s "Weren't we just at the festival?"
        m "If by {i}just{/i} you mean like two hours ago, yes."

        scene hanabi17
        with dissolve

        m "Wait..."
        m "Is it happening again?"
        s "Is what-"
        m "Are you blacking out?"
        m "Dreaming?"
        m "What’s going on? I can’t help you if I don’t know what it is- and you’ve seemed fine this whole time."
        s "I..."
        s "I don’t feel fine."

        scene hanabi18
        with dissolve

        m "I’d like to assume it’s just because you’re tired, but something tells me that would be far too convenient."
        m "Do you want to, like...lay down? Or go home?"
        m "We don’t have to do this tonight. There’s still time."
        s "No. We can do it now."
        s "You wanted to spend the whole day with me, so..."
        m "Yeah, but it’s already the {i}next{/i} day, {i}so...{/i}"
        s "I’ll be fine. If I’m able to hold a conversation with you now, the worst of it is probably over."

        scene hanabi19
        with dissolve

        m "Well, good. Because I hate having to carry that thing on my own."
        s "Yeah..."
        s "You carry enough as it is."

        scene black
        with dissolve2

        "I carry a box."
        "I have a sudden craving for eggs."

        stop music

        "////////////////MAYA EVENT COMPLETE"
        "////////////////THERE ARE NO MORE MAYA EVENTS IN CHAPTER 2"
    else:
        scene black
        stop music

        "THE EVENT IS OVER."
        "THERE WAS NEVER ANYTHING ELSE HERE."

    $ renpy.end_replay()
    $ maya_love += 25
    $ mayafestival4 = True

    "{i}Maya’s affection has increased by 25!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
        jump saturdaymorning
    else:
        "ERROR ADVANCING TO SUNDAY"
...
```

## Code that triggers this event
File: \game\MayaEvents.rpy
Code:
```python
...
m "Well, I don’t want to risk severing that."
    s "What if severing that connection repairs everything, though?"
    m "What if it doesn’t?"
    m "Besides, there’s absolutely no way this world is convenient enough to just “get repaired” by something as inconsequential as me not sweeping a staircase for several hours each weekend."
    m "The shortened version is that I do not want to risk this world dramatically changing- even with how much I’ve grown to abhor the mundane aspects of it."
    m "If all I’m faced with is a minor inconvenience two days out of every week, I will face it head-on....over and over again until I can no longer stand up straight."
    s "You’re doing all of that for me?"
    m "No, you narcissistic asshole. I’m doing it for everyone. "
    m "I suppose your sliver of the pie chart is a little larger than the others, though. Why that is, I will never understand."
    s "I understand."

    scene mayanightwalk17
    with dissolve

    m "Don’t say it a-"
    s "Because you’re in love with me."
    m "...gain."
    s "{i}Why{/i} you’re in love with me is still far beyond my comprehension, though."
    m "That is literally the exact thing I was saying."
    s "Does {i}that{/i} count as a confession?"
    m "Do you feel your brain liquefying?"
    s "I don’t think so."
    m "Then no. Probably not."
    s "Maybe we can avoid the whole blackout thing if you just think up really creative ways to say it instead of being blunt about it."
    m "Or maybe we can keep doing exactly what we’ve been doing since you “woke up” and maintaining a healthy distance that doesn’t spiral into a never ending pool of regret for both of us?"
    m "I think that sounds fun. Let’s go with that option."
    s "You’re going to break one day and you know it."

    scene mayanightwalk18
    with dissolve

    m "I have no idea what you’re talking about."
    s "You really-"
    m "Stop it. Please."
    m "I’ve heard it enough today."
    s "..."
    m "..."

    scene mayanightwalk19
    with dissolve

    s "Sure."
    s "Did you want to maybe start heading back soon, though?"
    s "As much as I appreciate and understand your love for shrines now, I highly doubt you want to spend the entire night at one."
    m "Back home or back to the festival?"

    scene mayanightwalk20
    with dissolve

    s "Is the festival still going? It seems pretty late."
    m "It should be. We’re quite a way from the main area, but I imagine we would have still heard the fireworks if they were set off."
    m "We missed the ones on Christmas, so I’d like to see these if you’re okay with it."
    s "Why wouldn’t I be okay with it?"
    m "Sorry, you might be fine with it {i}now.{/i} But who knows what would happen if another pink-haired girl were to show up out of nowhere and profess her love to you while we’re on the way?"
    s "I’d have to tell her I’m already on a date tonight."
    m "This isn’t a date."
    s "..."
    m "What? It’s not."
    s "Sure, Maya."

    scene mayanightwalk21
    with dissolve

    m "It’s not!"
    s "Uh-huh. Whatever you say."
    s "I'm going to start heading over now."

    scene mayanightwalk22
    with dissolve
    stop music fadeout 8.0

    m "It’s not a date!"
    s "Can’t hear you. Walking away."
    m "I mean it!"

    scene mayanightwalk23
    with dissolve

    m "..."
    m "..."
    m "..."

    scene mayanightwalk24
    with dissolve

    m "Hah..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ mayafestival3 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival4
...
```