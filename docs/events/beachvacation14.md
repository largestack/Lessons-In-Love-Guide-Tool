# Prayer Position (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Smile Guide](./beachvacation13.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation14
* Group: Main
* Triggered by label: beachvacation13
* Chain sources: beachvacation13
* Chain sources path: beachvacation13

## Official wiki page

[Prayer Position](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation14&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation14:
    play music "blueair.mp3"

    "I can feel myself getting lost on the way to-"
    "…"
    "…"
    "…"
    "Where was I going again?"

    play sound "static.mp3"
    scene amibreak1
    with flash
    stop sound

    "Rin splits apart from me on the way to [[redacted] and I find myself crawling after a matter of minutes."
    "Or at least doing something that resembles crawling."
    "I lose control of my limbs because of how hard it is to move your body through sand and wind up finding solace leaning up against a tree."
    "The tree looked something like this."

    play sound "static.mp3"
    scene tree1
    with flash
    stop sound

    "Wait."
    "No."
    "That isn’t right. "
    "This tree was happier."

    play sound "static.mp3"
    scene tree2
    with flash
    stop sound

    "That’s better."
    "So the tree looks like this, but it feels just like any other tree."
    "It has the branches, leaves, the wide part at the bottom that I forget the name of-"
    "And roots."
    "The roots sprawl out underground like a labyrinth, stealing nutrients from wherever it can find them, which I imagine is pretty hard on a beach."
    "All that’s here is sand."
    "And stars."
    "And oh how beautiful the stars are tonight."
    "They make me forget, if even for a moment, how hard it is to move."
    "How hard it is to breathe."

    if bonus == True:
        "How hard it all is."
        "And no. Not a penis joke."
        "Lol. Come on. You really think I’d joke at a time like this?"

    play sound "static.mp3"
    scene tree3
    with flash
    stop sound

    "{s}WHO WOULD JOKE AT A TIME LIKE THIS?{/s}"
    "{s}THIS IS VACATION!{/s}"
    "{s}THE HAPPIEST POSSIBLE TIME{/s}"
    "So why is everything breaking?"

    av "Come to the shoreline."
    av "Reach for salvation."
    av "Reach for anything you can grab hold of."
    av "{s}Unless it’s me.{/s}"

    play sound "static.mp3"
    scene whygodwhy
    with flash
    scene whereareyou
    with flash
    scene whythesky
    with flash
    scene mayabeach1
    with flash
    stop sound

    "A GIRL STANDS {s}ALONE{/s} ON THE BEACH WITH HER HANDS CLASPED IN PRAYER POSITION."
    "But why would someone who despises {s}GOD{/s} praying so much be doing just that at a time like this?"

    m "[[redacted prayer. god is real.]"

    "I can’t understand a word coming out of the girl’s mouth."
    "It’s all foreign to me. "
    "I had no idea Maya spoke another language."
    "That’s what’s happening, right?"
    "She’s speaking another language!"
    "You’re so talented, Maya!"

    m "…"
    m "I can hear you breathing, you know."

    play sound "static.mp3"
    scene mayabeach2
    with flash
    stop sound

    m "Wait..."
    m "Are..."
    m "Are you okay?"
    s "Huh? It’s not like you to ask something like that."
    s "Are you actually worried about me for once?"

    scene mayabeach3
    with dissolve

    m "..."
    m "Not anymore."
    m "You just seemed different for a second."
    s "Yeah well...it hasn’t really been the best day."
    m "I see that. You look like you’ve been through a lot."

    if ayanelust10 == True:
        s "You don’t even know the half of it."
        m "You’d be surprised."
        s "Yeah, well-"
        m "How is Ayane?"
        s "..."

        "{i}Does{/i} she know the half of it?"

        s "Why do you ask that?"
        m "She didn’t look so great when she came back from the inn. I wonder what could have possibly happened in there?"

        if bonus == True:
            s "You weren’t in the room as well...were you?"
            m "Not this time."
            m "But I’m pretty sure I can guess what happened."
            s "I’d very much appreciate it if you didn’t guess."
            m "I’d very much appreciate not having to speak of something so utterly horrifying."
        else:
            s "Fucking Kirin ruined all of her sandcastles. I felt so bad."
            m "I thought s- Wait, what?"
            s "Stupid collegiate age females, ruining sand castles and stuff. So mean."
            m "..."

    else:
        s "I really have..."

    m "Is there anything not involving [teenage]girls on your mind that you'd like to discuss?"
    s "Wait, you actually want to talk to me?"

    scene mayabeach4
    with dissolve

    m "The stars are beautiful tonight."
    m "They’ve put me in a good mood."
    m "And I thought that maybe I might be able to stand a brief conversation with you."
    m "But if that’s too much to ask, I’d be happy to find something else to do."
    s "No way. I’ve gotta seize this opportunity while I have it."
    s "Something happened right before coming here that's still on my mind. I guess it does involve a [teenage]girl, though."
    m "Shocker."
    m "You made another girl cry, I’m guessing?"
    s "Well...yes. But probably not for the reasons you’re thinking."
    m "Does it really matter {i}how{/i} you made them cry? The point is that you did."
    m "Not everyone is made to be broken, you know. I’d be careful if I were you."
    s "Well, I mean...It’s not like I {i}really{/i} need to be careful, right?"

    scene mayabeach5
    with dissolve

    m "I try to give you a warning and that’s your response? "
    m "Maybe I {i}will{/i} find something else to do after all."
    s "No, I just meant that nothing’s really permanent. Right?"
    m "There are plenty of things that are permanent."
    m "I’m not sure what you’re getting at."
    s "I’m talking about your reset button or whatever it is."
    s "Can’t you just fix whatever you don’t like?"
    m "Clearly not if you’re still here."
    s "Okay, so you can’t get rid of people. But you can get rid of pain or memories or things like that, can’t you?"

    scene mayabeach6
    with dissolve

    m "I think you might be misunderstanding something."
    m "I’m not the one resetting anything."
    m "I’m just asking someone else to do it."
    m "And it’s not like I can do it whenever or however I want either. "
    m "There are some things that work and some things that don’t work."
    m "But why are you bringing that up now?"
    m "There are still several months left until we need to worry about that again."
    m "Just focus on enjoying your time here until that happens."
    s "I’m confused..."

    scene mayabeach7
    with dissolve

    m "You’re always confused. How did you even become a teacher?"
    s "Beats me. Could you maybe reset me into a different job whenever the next time rolls around?"
    m "You know you could always just quit if you don’t want to do it anymore...I wouldn’t complain."
    s "But think about how much good I’m doing for the other girls."

    scene mayabeach8
    with dissolve

    m "I’d rather not think about your relationships with any of the girls, to be honest."
    m "Quite frankly, I find it abhorrent. "

    if amilust10 == True and bonus == True:
        m "I can only imagine how poor Ami must have felt coming into your room to wake you up this morning."

        "To be fair, I think she felt pretty good..."
        "But again, why does Maya know something like that?"

        s "The way you say that makes it sound like you were waiting around for her."

        scene mayabeach7
        with dissolve

        m "Because I was, you idiot."
        m "I don’t know what she is to you, but to me, she’s my best friend."

        scene mayabeach8
        with dissolve

        m "And I’d never do something to betray her trust."
        m "Not even something as simple as eating breakfast without her."
        s "What a dedicated and wonderful friend you are..."

    else:
        m "But I suppose that all men are weak and impulsive at the end of the day."
        m "You’ll take advantage of every opportunity you see fit."
        m "..."
        s "..."

        if bonus == False:
            m "After all-"
            m "You {i}are{/i} the huggy boy..."
            s "..."
            m "..."

    scene mayabeach4
    with dissolve

    m "How do you feel about the stars, Sensei?"
    s "The stars? Why are you asking?"
    m "It’s a test of sorts, so answer honestly."
    s "Like...right now? Or in general?"
    m "In general."
    s "They’re...fine, I guess."
    m "Just fine?"
    s "I think so. I haven’t really thought much of it. You need to let me study if you’re going to give me random tests like this."
    m "No, it’s fine. You passed."
    m "Congratulations."
    s "What kind of test was that?..."

    scene mayabeach8
    with dissolve

    m "One that doesn’t matter much to you, but means everything to someone else."
    m "Do you believe in god, Sensei?"
    m "Some say that god is out there among the stars, watching over everything we do."
    m "Those people are wrong, of course. But it’s still a thing they say, regardless."

    scene mayabeach4
    with dissolve

    m "Do you find blind faith like that in accordance with how you live {i}your{/i} life?"
    m "Is there something that you inherently believe in despite the odds being stacked heavily against you?"
    m "Or are you the type to not believe anything unless you see it?"
    s "Is this another test?"
    m "Perhaps."
    s "Well I think I’m going to fail this one because there are a lot of things I’ve been seeing lately that I {i}still{/i} don’t believe."
    m "I see."

    scene mayabeach9
    with dissolve

    m "I was the same at one point."
    m "It took me a very long time to come up with the theories and outlooks I have now. Which is probably why they confuse you so greatly."
    s "Okay, save the backhanded insults for the classroom."

    scene mayabeach10
    with dissolve

    m "But the thing about the stars, especially on nights like this, is that they make all of those theories of mine almost float away in a sense."
    m "It makes me think, “If there are things this beautiful...anything is possible.”"
    m "It defies all logic. It defies all reason. But I still believe it while my head is raised."

    scene mayabeach11
    with dissolve

    m "Of course, those feelings go away as soon as I close my eyes."
    m "But for a brief moment in this seemingly infinite timeline, I doubt nothing."
    m "So with that in mind, does your opinion of the stars change?"
    m "Or do you still just think they’re fine?"
    s "..."
    m "..."
    s "Honestly, I still just think they’re fine."

    scene mayabeach12
    with dissolve

    m "Then you pass again. Two victories in one night."
    m "This must be a new record for you."
    m "It will never cease to amaze me how carelessly you carry on despite not having a single thing you love."
    s "Is that a compliment?"

    scene mayabeach13
    with dissolve

    m "Quite the opposite, actually. It’s repulsive."
    m "But still intriguing. "
    m "I wonder how long you’ll be able to carry that weight for?"
    s "What do you mean?"
    m "I mean that there’s only so much your mind is able to hold."
    m "Memories persist through resets. "
    m "Well, most of the time at least."
    m "Our physical forms may revert to the way they were months prior, so things like scars and even graver injuries can be wiped away."
    m "But the things we see and the things we hear do not."
    m "Tell me, did you find it strange that everything remained exactly the same when we met again in front of the bistro?"
    s "Yeah, but it’s not like you didn’t warn me beforehand. I just still don’t understand {i}why{/i}."
    m "That’s normal. Neither do I."
    s "Well, can’t you just ask whoever is resetting the world then?"
    m "You can ask anyone anything, but it doesn’t mean you’ll ever get an answer."

    scene mayabeach14
    with dissolve

    m "There are some things that people dedicate their entire lives to discovering."
    m "But you and I...and everyone else in the class-"
    m "We have a little more time than that."
    m "So what are we to do with it all?"
    m "Sit around and endlessly enjoy our youth?"
    m "How many years worth of memories can we fit into such short time periods without going absolutely insane?"
    m "It will all come tumbling down one day."
    m "You may have your questions, but I have mine too."
    m "So the next time you suggest that nothing is permanent, keep in mind that some things very much are."
    m "Some things are too permanent. "

    scene mayabeach15
    with dissolve

    m "That’s all I wanted to say."
    s "…"

    "As always, I’m not really sure what to say to Maya."
    "Until now, I’ve been trying not to think much about the whole ‘reset’ thing..."
    "But it seems like Maya has been thinking about it for quite a while."
    "I wonder how many times she’s reset by now?"

    scene black
    with dissolve2

    "And I wonder-"
    "How many more resets will there be until I’m gone?"
    "How easily can someone else steal back the body I stole myself?"
    "I close my eyes and cling to Maya’s words."
    "Some things are too permanent."
    "And I think about praying, for the first time in my life-"
    "That I am one of those things."

    $ renpy.end_replay()
    $ maya_love +=1
    $ beachvacation14 = True
    stop music fadeout 7.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    "{i}Somewhere else along the shoreline...{/i}"

label beachvacation15:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```