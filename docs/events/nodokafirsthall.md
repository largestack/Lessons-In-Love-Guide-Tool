# Humbert Humbert
Nodoka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nodokafirsthall&go=Go)



## Event preconditions
✅Event "[Main: Adult Supervision](./day288.md)" is completed (event=day288)



## Next events
* [Nodoka: The Man Who Would Be King](./nodokadorm1.md)

## Event properties
* ID: nodokafirsthall
* Group: Nodoka
* Triggered by label: dorm2friday
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label nodokafirsthall:
    scene nodokahall1
    with dissolve

    no "Oh. Well, hello there."
    no "To what do I owe the pleasure, Sensei?"
    s "No pleasure involved, just here to kill some time."
    no "No pleasure involved? Not even a little bit?"
    s "I mean...if you want there to be pleasure..."

    scene nodokahall2
    with dissolve

    no "Of course I want there to be pleasure. "
    no "Why else would I have this word-coated rectangular object in my hands?"
    s "Weird way to say “book” but okay."
    no "What I mean to ask is why bother indulging yourself in anything if there is nothing to leech from it?"
    no "We are all but leeches, Sensei. Digging our tiny, jagged teeth into anything they’ll latch onto in search of the essence of life."
    s "Weird way to say “blood” but okay again."

    scene nodokahall3
    with dissolve

    no "Would you at least agree that words without experience are meaningless?"
    no "It’s something that appeared inside of this very rectangle and I’d be a liar if I were to say it didn’t provoke some impure thoughts in this old noggin of mine."
    s "You’re still in [high_school]. Your noggin is absolutely not “old.”"
    no "No, it is not."
    no "But that calls into question exactly why I am reading {i}this{/i} specific piece of literature despite having no experience in its subject matter."
    no "If words without experience are meaningless, shouldn’t {i}these{/i} words, which I have no experience {i}with{/i}, simply bounce off the walls of my brain without so much as leaving a minor bruise?"
    s "Can brains even bruise?"
    no "Probably? I can’t imagine it would feel very nice, though."
    s "What are you reading anyway?"

    scene nodokahall4
    with dissolve

    if bonus == True:
        no "“Lolita.” Are you familiar with it?"
    else:
        no "“Clifford the Big Red Dog.” Are you familiar with it?"

    s "Vaguely. I feel like I read that a long time ago but I’m kind of hazy on the details."
    no "I’m not surprised you’ve read it given your...demeanor so far."

    if bonus == True:
        no "I’m sure the title itself is enough to give you an inkling of what the subject matter is, though."
        no "Sexual conduct is one thing, but do you believe you’d ever be able to fall in love with someone so much younger than you, Sensei?"
        s "I prefer not discussing love whenever possible. It’s not exactly a cut and dry topic."
        s "Do you think you’d ever be able to love someone so much older?"

        scene nodokahall5
        with dissolve

        no "I also prefer not discussing love whenever possible. "
        no "It’s not exactly a cut and dry topic."
        no "I do yearn for the taboo, though. But I’m pretty sure the whole [incest] thing gave that away."
        s "Yeah, you’ve come across as kind of...freaky so far."
        no "{i}I{/i} do? Whatever do you mean?"
        no "I’m but an inexperienced, [adolescent] leech whose teeth aren’t sharp enough to latch onto anything."
        no "Perhaps I could try to take a bite out of you, Sensei? For practice."
        s "Like, right now?"
        no "Just a little nibble. Quickly, before Uta sees us."
        s "That book is really getting to you, huh?"
    else:
        s "Yeah. I really do present myself as a Clifford lover, don't I?"
        no "There's so much about you I can deduce just from that little factoid alone."

    scene nodokahall6
    with dissolve

    if bonus == True:
        no "It is. "
        no "I’m very easily fascinated by things most people aren’t able to experience in their own lives."
        no "Though, I suppose the idea of an illicit and inappropriate relationship may be a bit more common than I thought prior to attending [kumon_mi_high]."
        no "So, yes. I can’t help but feel my heart begin to race at the thought of something like that."
        s "Maybe I’ll give it another go soon. It’s been a while since I’ve read anything, to be honest."
        no "That’s a shame. Literature can be a portal to different worlds and different lives."
        no "Your time would likely be better spent on literature you’re not currently living through, though."

    s "Are you suggesting something about me, Nodoka?"

    if bonus == True:
        no "If not suggesting, then recommending...as you have more than a handful of {i}opportunities{/i} at your disposal."
        no "You’ve already confirmed some of your thoughts on the topic of manipulation. Surely you don’t only use that tactic for little, white lies."
        s "Is this your attempt at manipulating {i}me?{/i}"
    else:
        no "I'm not {i}not{/i} suggesting something about you, dog lover."
        s "Is this a manipulation tactic?"

    no "What would I possibly manipulate you into doing that you wouldn’t already do on your own?"
    s "Reading more books."

    scene nodokahall7
    with dissolve

    no "Ahh, yes. The consumption of knowledge has become more taboo than any illicit relationship out there."
    no "It’s certainly starting to feel like that, at least."

    scene nodokahall8
    with dissolve

    no "I’m surprised you’ve managed to go so long without diving into a word-maze, though."
    s "Jesus, Nodoka. Just use the word “book.”"
    no "Well now I’m just going to continue abstaining out of sheer spite."
    s "Of course you are..."
    no "Futaba tells me you used to be a writer, Sensei. "
    no "Why is it that you’ve given up on that? "
    s "At this point, my brain is so all over the place that I feel like anything I write would come out twisted and indiscernible."

    if bonus == True:
        no "So what? You should know better than anyone that the overflow of creative juices can lead to all sorts of amazing things."
        s "So can the overflow of {i}less{/i} creative juices."
        no "Please explain to me in detail exactly which juices you are referring to, Sensei."
        no "Quickly, before Uta hears us and has to call her parents."
        s "You know about the parent thing too?"
        no "I do. And your response has consequently confirmed that you’ve been involved in at least one sexual conversation with her."
        no "Nice."
        s "She’s an overly flirtatious part-time maid. It would be more surprising if I {i}didn’t{/i} find myself in a conversation like that with her at least once."
        no "Ooooooh and you like maids as well."
        no "We should go to the cafe together sometime and prey upon those innocent girls."
        no "Think of how many soft, slender necks we could dig our teeth into."
        s "My [niece] works at that cafe, Nodoka."
    else:
        no "Clifford's really gotten to you, huh?"
        s "Why is he so big? They never explain it."

    scene nodokahall9
    with dissolve

    no "Sensei...you’re {i}really{/i} trying to excite me now, aren’t you?"

    if bonus == True:
        s "I feel like you are very easily excited."
        no "But {i}not{/i} very easily satisfied."
        no "Remember that when the time comes for you to become my own Humbert Humbert."

        scene nodokahall10
        with dissolve

        no "Until then, though, I suppose I will continue to live inside of paper."
        s "Wait. I don’t remember much of “Lolita,” but I’m pretty sure I’m already that Humbert guy."
        no "We’re not at that part of the novel yet, Sensei."
        no "But perhaps, somewhere, some day, at a less miserable time, we may see each other again."
        no "Goodnight."
    else:
        s "What? No. I'm trying to open up to you about what the book series has done to me."

    scene nodokahall11
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        "Nodoka goes back into her room and leaves me standing in the hall, bewildered and mildly aroused."
        "That’s pretty much how half of our conversations end, though, so I’m not {i}too{/i} shocked by it."
    else:
        s "What the fuck. Don't just leave."
        no "{i}Can't hear you!{/i}"

        "I feel so alone all of a sudden."

    scene black
    with dissolve

    "Either way, I decide to simply go home and rest."

    if bonus == True:
        "But not until after knocking on her door several times to see if she was ready to skip further into our novel together."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokafirsthall = True
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohahall:
    if otohafirsthall == False:
        jump otohafirsthall
    else:
        jump otohahallgen

label otohahallgen:
    if chapthreeactive == True:
        scene otohasummer2hallgen
        with dissolve
    else:
        scene otohahall1
        with dissolve

    o "Yo!"
    o "What brings you over here, Sensei?"

    "I decide to {s}hang out with{/s} bother Otoha in the hall for a little while in an effort to quell some of my boredom."

    if bonus == True:
        "She obliges and humors me, constantly feeling the need to remind me that she is both way out of my league and way out of my age group."
        "Or both of those things."
        "In fact, yeah. Definitely both of those things."
    else:
        "She obliges and humors me, constantly feeling the need to remind me of her conservatorship and how large her parents are becoming."

    "But that doesn't change how we seem to enjoy talking to one another, even if we're talking through these two giant barriers positioned between us."

    scene black
    with dissolve

    "We don't hang around for long, as Otoha is supposed to be meeting up with Nodoka tonight, but we do make plans to hang out again soon."
    "Even if {i}making plans{/i} in this case means something more like...her agreeing to open the door if I randomly show up again."
    "But hey, you take what you can get."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohafirsthall:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label nodokahall:
    if nodokafirsthall == False:
        jump nodokafirsthall
...
```