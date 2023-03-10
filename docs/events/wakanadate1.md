# To the River (Wakana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* wakananumber equal to True (unknown variable)



## Next events

* [Wakana: Soup, or Another Year With You](./wakanadate5.md)

## Event properties

* Id: wakanadate1
* Group: Wakana
* Triggered by label: callwakanamorning
* Triggered by branch label: callmorning
* Triggered by path: callmorning->callwakanamorning->wakanadate1

## Official wiki page

[To the River](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=wakanadate1&go=Go) for more details.

## Event code

File: (install folder)\game\WakanaEvents.rpy

Code:
```python
...
label wakanadate1:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer."
    "I don’t really understand how things got to this point...but here we are."
    "Granted, I doubt she’ll answer in the first place. But at least it’s worth a shot."
    "Worse comes to worst, I can always just...go find someone else inherently sad to spend time with."
    "That sure sounds like a lot of fun."

    play sound "phonebeep.wav"

    w "I want to fucking die."
    s "I had a feeling you were going to answer the phone like that."
    w "Oh. It’s you."
    s "So, that wasn’t a personalized greeting and is just the way you answer the phone for everyone?"
    w "What do you want?"
    w "Do you have any idea what time it is?"
    s "Early. Let’s hang out."
    w "Okay."
    s "Now, before you say no, let me give you a list of the pros when it comes to spending time with me. I-"
    w "I said okay."
    w "Are you truly this incapable of simply listening to someone when they speak?"
    s "Wait, really? I don’t even have to convince you?"
    w "I’m in my office. Come here."
    s "Your office? Like, at[school]?"
    w "Correct. Now, goodbye. "
    s "But-"

    play sound "phonebeep.wav"

    s "…"

    "Why is Wakana at[school] on the weekend?"
    "And why this early?"
    "Am I really going to spend the little free time I have going back to the same place I’m forced to “teach” five days out of every week?"
    "…"

    scene black
    with dissolve

    "Of course I am- because there is an attractive girl there who wants to see me."
    "Or, at the very least, is {i}okay{/i} with seeing me."
    "And also has a girlfriend who could break my arm in five seconds if she wanted to."

    s "…"

    "I should probably be careful with what I say to Wakana this morning."
    "………"
    "……"
    "…"

    scene wakanafirstvisit1
    with dissolve2
    play music "sleepystreets2.mp3"

    s "Hey, Wakana. You’re looking awfully beautiful this morning."

    "I fail immediately."

    w "Thank you. I appreciate that."
    s "I'm sorry. I know I-"
    w "I said...{i}I appreciate that{/i}."
    s "Wait, you do?"
    w "Do you believe me to be so dead inside that I’m incapable of receiving a compliment?"
    s "Kind of, yeah."

    scene wakanafirstvisit2
    with dissolve

    w "Fair enough."
    w "Any more than that would have been entirely unprofessional and unwarranted, though."
    w "Especially given that my significant other could snap your arm like a toothpick in less than ten seconds."
    s "Less than five, actually. I already confirmed this in my thoughts a little bit earlier."
    w "How exciting."
    w "Anyway, thank you for coming here to do my bidding."
    s "Your...what?"
    w "My bidding."

    if bonus == True:
        s "Is this a sexual thing?"
    else:
        s "Like...on a horse race?"

    w "You’ve been spending too much time with that Nagasawa girl. "

    if bonus == False:
        s "You are confusing her with Touka. Touka is the one who likes horses."
        w "The only student who matters to me is Miyamura."

    s "Hey, your favorite student of mine is no saint either."

    scene wakanafirstvisit3
    with dissolve

    w "You leave Miyamura out of this. She’s as pure as the whitest snow."
    s "Wakana, she works in a porn shop."

    scene wakanafirstvisit4
    with dissolve

    w "Nonsense. The girl her age who works at the local porn shop does not wear glasses. They are entirely different people."
    s "I didn’t realize you were a customer there."

    if bonus == True:
        w "I’m in a lesbian relationship with a girl who likes being handcuffed. Of course I am a customer there."
        w "Now, can we please move this conversation away from territory that should remain completely unknown to one another as coworkers?"
        w "I only agreed to seeing you today as I’m behind on grading papers and need your assistance."
        s "That is something you should have probably informed me of beforehand."
        w "And risk you not coming to help? Absolutely not."
    else:
        w "I walked in once on accident."

    scene wakanafirstvisit5
    with dissolve

    w "Now, take these and make yourself useful."
    s "You know, maybe the reason you always want to die is because you spend so much time-"
    w "Doing my job?"
    s "Being anti-fun."
    w "I don’t have time for fun. I’m responsible for the education of a multitude of [young_girls] who may or may not wind up turning into more Nodoka Nagasawas as they get older."
    w "For the sake of our future generations, I must repeatedly kill myself on a daily basis."
    w "This is the road I must take. "
    s "Some might even say the {i}road less traveled by.{/i}"

    scene wakanafirstvisit6
    with dissolve

    w "Don’t try to appeal to me through overrated literary references. Frost was a hack."
    w "Why spend so much time writing about {i}nature{/i} of all things when essentially every other topic known to man is both far more interesting and far more...not fucking stupid."

    if bonus == True:
        w "The outside world is nothing but a hellish landscape even in the coldest of winters and I will not sit idly by as you quote a man who would probably fuck a tree if given the opportunity."
        s "You...feel pretty strongly about this, don’t you?"
    else:
        w "The outside world is nothing but a hellish landscape even in the coldest of winters and I will not sit idly by as you quote a man who would probably hug a tree if given the opportunity."
        s "I would also hug a tree, but I am the huggy boy so-"

    w "Are you going to help me grade these tests or not?"

    scene wakanafirstvisit7
    with dissolve

    s "This is a pretty nice office you’ve got here, Wakana."
    w "Oh my fucking god. Why do you even work here?"
    s "I think it’s a little smaller than mine overall, though."

    scene wakanafirstvisit8
    with dissolve

    if bonus == True:
        w "Yes. It’s almost as if the Japanese work force values male employees more than it does female ones- even when said males aimlessly wander the halls, sodomizing students with their eyes all day long."
        s "Hey. Don’t lump all males in with me. I’m a special exception."
        w "You sure are."
    else:
        w "Yes. It’s almost as if the Japanese work force values male employees more than it does female ones."
        s "We should work together to change that one day."
        w "I'll add it to my to-do list."

    s "Really, though. You should stop being so serious all the time."

    scene wakanafirstvisit9
    with dissolve

    w "I think you may be misinterpreting how much “time” we have left. "
    w "Every day, we slip further and further into a pit of despair that even the most seasoned of climbers will one day struggle to find their way out of."
    s "So you’re trying to get out by just subjecting yourself to {i}more{/i} despair?"
    s "What’s the strategy here?"
    w "The strategy is that you mind your own fucking business."
    s "Oh, I know- why don't we talk a little more about poetry?"
    w "You? The person who quoted the fucking “Road Not Taken?” "
    w "What’s next? Plums?"
    s "I just want to spend some time with a Wakana Watabe who isn’t killing herself over a job she doesn’t even like."

    scene wakanafirstvisit10
    with dissolve

    w "It’s not as if I don’t {i}like{/i} it. I just...don’t like it?"
    s "Deep."
    w "What I mean to say is that it’s as if there’s no true payoff anymore."
    w "You’re not a teacher, so you likely won’t understand, but the most satisfying part of this job is watching the flowers you've cultivated finally being plucked and stuck into vases all over Japan."
    w "The sense of accomplishment in knowing that you were able to impact the lives of others in some form."
    w "And...for some reason-"
    w "It feels as if that “payoff” is further away than ever before."
    s "…"

    "From out of Wakana’s mouth crawls an invisible spider in the form of a thought."
    "It quickly makes its way over to me and sinks its fangs into my skin, injecting me with the question of what effect the distortion of time has in scenarios like this."
    "If Wakana’s memories carry over from one reset to the next, the same way everyone else’s seem to-"
    "And her outlook on her profession is centered entirely around the relief that is provided once a[school] year comes to an end-"
    "Wouldn’t something like this put her into limbo?"
    "Endlessly chasing after a goal that’s impossible to obtain, yet clinging onto the belief that it’s just around the corner."

    scene wakanafirstvisit11
    with dissolve

    w "What’s this? {i}You{/i}, of all people, turning silent?"
    w "Don’t tell me that...you were able to understand what I was saying after all?"
    s "Do you have a favorite poet, Wakana?"

    scene wakanafirstvisit12
    with dissolve

    w "You’re still going on about that?"
    w "Just help me grade my fucking tests so we can get out of this place."
    s "I just want to know what sorts of things inspire {i}you{/i}- a person who, somehow or another, still gets up in the morning to try and inspire others."

    scene wakanafirstvisit13
    with dissolve

    w "Hah..."
    w "You can probably tell just by looking at me. "

    scene wakanafirstvisit14
    with dissolve

    w "{i}But when within thy wave she looks-\nWhich glistens then, and trembles-{/i}"
    w "{i}Why, then, the prettiest of brooks\nHer worshipper resembles;{/i}"
    w "{i}For in his heart, as in thy stream,\nHer image deeply lies-{/i}"
    w "{i}His heart which trembles at the beam\nOf her soul-searching eyes.{/i}"
    s "Edgar Allen Poe."

    scene wakanafirstvisit15
    with dissolve

    w "Did you actually know that one? Or was it just my choice of clothing after all?"
    s "I knew it."
    s "Just because I vehemently refuse to do my job doesn’t mean I’m not actually smart."
    w "Do you believe there to be a correlation between one’s level of intellect and how many lines of poetry they’ve memorized?"
    s "Not really. But I know stuff and knowing stuff makes me cool."

    scene wakanafirstvisit16
    with dissolve

    w "Hm."
    s "Are you impressed? Have I finally convinced you to take a break from doing your job on your day off?"
    w "Absolutely not."
    w "Though, I suppose it wouldn’t hurt to spare five minutes or so."

    scene black
    with dissolve

    "Wakana makes her way over to a bookshelf on the side of the room and drags her finger across a number of what appear to be anthologies."
    "She eventually stops on one and removes it from the shelf, leaning up against it and popping the book open as if she’s already memorized where a certain poem is located."
    "Either that or she’s just reading a random poem she opened to- but I'd like to believe that there was at least some level of tact or calculation to it."

    scene wakanafirstvisit17
    with dissolve

    w "{i}She walks in beauty, like the night\nOf cloudless climes and starry skies;{/i}"
    w "{i}And all that’s best of dark and bright\nMeet in her aspect and her eyes;{/i}"
    w "{i}Thus mellowed to that tender light\nWhich heaven to gaudy day denies.{/i}"
    s "That’s not Poe. Isn’t that-"

    scene wakanafirstvisit18
    with dissolve

    w "Lord Byron. "
    w "You asked me for a favorite poet, to which the answer was Poe."
    w "But if I were to choose a favorite poem, it would be this one."
    s "Why this one?"
    w "The answer is quite embarrassing, so I’d rather not say."
    s "Why even read it in the first place then? We're supposed to be using this opportunity to deepen our relationship."
    w "Why, I believe we just did."
    w "Now-"
    w "Back to work."

    scene black
    with dissolve

    "As quickly as she had found the book and thus the poem, she slides it back into place and makes her way over to her desk."
    "Without even drawing a breath, she once again holds out a file containing a bunch of tests and...expects me to know what to do with them."

    scene wakanafirstvisit5
    with dissolve

    w "Playtime is over. Either help me or get out."
    s "You are an entirely unexciting friend to have, Wakana."
    w "And you are proving to be an entirely useless one."
    w "Though, I can’t say I’m at all surprised."
    w "Even if you do have surprisingly decent taste in poetry apart from that fucking Robert Frost guy."
    s "What in the world did Robert Frost do to you to make you hate him so much?"
    w "Existed. "
    w "Now, take these fucking tests. My arm is getting tired."

    scene black
    with dissolve2

    "Surprisingly enough, I {i}do{/i} take the tests from Wakana."
    "However, I’m only able to grade three of them before getting bored and deciding to head home."
    "I also just mindlessly marked a few of them off instead of actually paying attention to them, so I apologize in advance to anyone who may have failed because of me."
    "But I’d also like to thank those people for allowing me to get a little closer to Wakana- something I didn’t really ever think I’d be able to do."

    $ renpy.end_replay()
    $ wakanadate1 = True
    $ wakana_love += 1
    stop music fadeout 5.0

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label wakanadate5:
...
```

## Code that triggers this event

File: (install folder)\game\WakanaEvents.rpy

Code:
```python
...
label callwakanamorning:
    if wakanadate1 == False:
        jump wakanadate1
...
```