# Enigmatology (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin love greater than or equal to 20

* Event [Flickering Spotlight](./kirinsoccer15.md) (Kirin) is completed)



## Next events

* [Kirin: Bye Bye, Boner](./kirindorm15.md)

## Event properties

* Id: kirinsoccer20
* Group: Kirin
* Triggered by label: soccerfieldkirin
* Triggered by branch label: soccerfieldkirin
* Triggered by path: soccerfieldkirin->kirinsoccer20

## Official wiki page

[Enigmatology](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinsoccer20&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirinsoccer20:
    scene kirinthinking1
    with fade
    play music "behindabathroom.mp3"

    "So begins another day beside a calculated disaster."
    "I wasn’t particularly fond of that title when I first heard it in Kirin’s dorm room, but after putting a bit more thought into it, I think it works quite well."
    "In a sense, I’m also a calculated disaster of sorts."
    "And no, that is not another excuse for me to be self-deprecating. I already have plenty of those."
    "It’s a fair evaluation based on my tendency to change or mold myself to fit the ideals of those around me."
    "But I’ve never been fond of changing, so the transformation is always a bit incomplete."
    "Imagine you buy sixteen puzzles, all with at least one or more pieces missing. (It was a really shitty puzzle store.)"
    "And you have a friend who makes puzzles for a living."
    "An enigmatologist, if you will. "
    "The enigmatologist says to you-"
    "“I can likely craft you the missing piece based on a description of it, but there is a chance the size will be slightly off without the proper schematics.”"
    "Of course, that problem could be easily remedied if you’d just bring him the puzzle so he can figure out exactly what it is that’s needed."
    "But you’re a fucking lazy dick and don’t want to be bothered making a second trip."
    "So you have him guess and ultimately wind up with a piece that is slightly off."
    "But you still take it from him and just mash it into the puzzle anyway, not caring if it causes the rest to snap or break or whatever it is that happens when you try to solve a puzzle with brute force."
    "And everything comes falling down."
    "Everything but me, that is."
    "For I am both the enigmatologist as well as the one who was too lazy to ever provide the schematics."
    "I am both the cause of all problems as well as their respective solution."
    "A makeshift god who can provide temporary solace, but never truly guide someone toward salvation."
    "And as long as puzzles with missing pieces exist, I will continue to ruin them."
    "Because an enigmatologist does not just create puzzles, they solve them as well."
    "And if all of the puzzles in all of the world are solved, what is left for me to do?"
    "Break puzzles to make new puzzles."
    "Fuck it. Take every puzzle you bought from that shitty store and dump the contents into a giant bowl."
    "Maybe even a well."
    "Create the ultimate puzzle."
    "Solve it."
    "Become God."
    "Thank you for once again listening to my incessant ramblings about all that is broken and how to both fix and unfix it."

    ki "So...I’m thinking about quitting the team."
    s "Is this about the sit-ups again?"
    ki "Nah."

    if bonus == True:
        ki "Frankly, I was a little more disappointed that Miku wouldn’t let you into the showers with us despite clearly wanting it."
        s "So Miku’s prudence is the reason you’re thinking of quitting?"
    else:
        s "Is it about canola oil again?"

    scene kirinthinking2
    with dissolve

    ki "Nah."
    ki "I’m just thinking it might be time to move onto something I’m a little better at."
    ki "Like, I’ve been playing soccer for pretty much my entire life and have always been a middle-of-the-road player at best."
    ki "I still think it’s fun and everything, but it gets kind of annoying at times."
    ki "Like, you try so hard to improve...only to watch everyone else get better without putting in even half of the effort."
    s "I don’t really think it’s fair to say that they’re putting in less effort when, more often than not, it’s the two of {i}us{/i} up here rather than them."

    scene kirinthinking3
    with dissolve

    ki "Who says that I don’t spend every waking moment outside of practice practicing?"
    s "I think you might have the wrong idea of what “practice” and “outside of practice” are supposed to consist of."
    ki "Maybe I just like practicing alone better?"
    s "Because you’re self-conscious?"

    scene kirinthinking4
    with dissolve

    ki "What’s wrong with being a little self-conscious?"
    ki "I’m a [teenage]girl surrounded by other [teenage]girls who are naturally better at almost everything than me."
    ki "Of course I’m going to be self-conscious."
    ki "Do you think that makes me weak, Sensei?"
    s "No. I think it makes you human."
    s "Which is a good thing because I’ve definitely questioned that about you on several occasions."

    scene kirinthinking5
    with dissolve

    ki "What else would I be if not a human?"
    s "A puzzle."
    ki "Like a jigsaw puzzle or...a crossword puzzle?"
    s "Whichever one is harder for the average person to solve, I guess."
    ki "Probably a jigsaw puzzle, then. Those can get kind of intense once you start adding a bunch of pieces."
    ki "But I guess crossword puzzles can also get intense once you start adding crazy words like-"
    s "Enigmatology?"

    scene kirinthinking6
    with dissolve

    ki "Yeah. Whatever that is."
    ki "How is anyone supposed to guess a word that they’ve never even heard before?"
    ki "I mean, I guess it’s easier now since we all have access to the Internet, but still. That’s way too much work."

    scene kirinthinking7
    with dissolve

    ki "See that girl with the crazy thighs over there? The one with the ball in her hands?"
    s "That is your sister, Karin. I am quite familiar with her."
    ki "Yeah, whatsherface. "
    ki "She and I actually used to team up and put jigsaw puzzles together when we were little. Like, way before we were even in elementary school."
    ki "Neither of us were particularly good at them on account of being stupid little kids but, just like with soccer, she got better and I lagged behind."
    ki "Now, this club is pretty much the only thing the two of us ever do together."
    ki "So you can probably guess how that makes me feel."
    s "Not really any point in guessing when you’re already making it extremely apparent."

    scene kirinthinking8
    with dissolve

    ki "Hey, when a puzzle gets too hard, what do you do?"
    ki "Do you give up?"
    ki "Or do you keep working at it no matter how tough it gets?"
    s "No clue. But I’ll let you know how I feel the next time something like that happens to me."
    ki "Bummer."
    ki "I was hoping to find out what you’re planning on doing with me."
    ki "You know, since I’m just as much of a puzzle as I am a human being to you."
    ki "Once you’ve got all the outer pieces put together, are you really going to go through all of the effort to finish the rest?"
    ki "Or are you just going to call it quits and move onto another?"
    ki "I mean, we all know the outer part of the puzzle is the most fun. So why bother doing the rest when there are puzzles literally everywhere?"
    s "What would the equivalent of that be if we’re counting you entirely as a person and not an object?"

    scene kirinthinking9
    with dissolve

    if bonus == True:
        ki "I guess it would be just...getting close enough to fuck me, proceeding to {i}actually{/i} fuck me, and then running off to fuck somebody else when you realize I’m not worth fucking anymore."
        ki "Or something."
        s "So it all comes back to sex."
        ki "It all comes back to sex."
        ki "I mean, that’s how our relationship started, wasn’t it?"
        ki "A promise that you could have what you want from me as long as I can have what I want from you."
        ki "Luckily, we both want the same thing now."
        ki "Who’s to say either one of us will want to finish the rest of the puzzle once the outline is done?"
        ki "Sure, I guess there’s some momentary satisfaction once you actually {i}solve{/i} a puzzle. "
        ki "But after that, you just break it apart and put it back in the box or use that weird puzzle glue to hang it on the wall or the fridge."
        s "I don’t think you’d look particularly nice hanging on my wall."
        ki "I don’t even think you’d {i}fit{/i} on my wall."
        ki "Hell, I’m not even sure if you’ll fit in {i}me{/i}."
        s "So it all comes back to sex."
        ki "It all comes back to sex."
    else:
        ki "Beats me. You're the teacher, you come up with the comparisons."
        ki "I'm just here to gaze off into the distance and reflect on all of the horrible decisions I have made in my life."

    scene kirinthinking10
    with fade

    "Kirin looks away from me, watching the rest of the girls practice."
    "I can’t say for certain, as I still haven’t completed her outline, but I’m pretty sure she’s hoping that one of them looks over at her right now."
    "That someone smiles and coaxes her into coming down and practicing with them instead of abandoning her atop this stage filled with athletic bags and traffic cones."
    "At the same time, though, Kirin abandoned {i}them{/i}."
    "They’ve abandoned each other, so it wouldn’t make any sense for one of them to reach out."
    "It’s just an unfortunate yet realistic progression of one’s interests and confidence dwindling with the passage of time."
    "Time is the worst."

    ki "Maybe I’ll just find something to do with Noriko."
    ki "She’s fun to be around. And she’s yet to make me feel insignificant, so that’s pretty sweet."
    s "You two are still getting along?"

    scene kirinthinking11
    with dissolve

    ki "We’re kind of like two sides of the same coin."
    ki "We’ve got our differences and will probably never have the same exact mindset as one another, but we’re still out to do the same thing at the end of the day."

    if bonus == True:
        s "Is that “thing” having sex with me?"
    else:
        s "Saving the whales."

    scene kirinthinking12
    with dissolve

    if bonus == True:
        ki "I was talking more about filling a void in our hearts, but I guess the sex thing is also true."
    else:
        ki "I was talking more about filling a void in our hearts, but I guess the whales work too."

    s "Am I just a tool to you?"

    scene kirinthinking13
    with dissolve

    ki "You’re kind of a tool in general."
    s "I did not come here to be insulted."
    ki "A useful tool. Like a hammer or a...chainsaw."

    if bonus == True:
        s "Or a vibrator."
        ki "I guess it’s your turn to turn everything sexual now?"
        s "You did it twice in a row earlier, so now I have to catch up."
        s "From this point on, it’s anyone’s game."
    else:
        s "Or a whale catching net."

    scene kirinthinking14
    with dissolve

    ki "That aside, things have definitely started to look up a bit since Noriko and I moved in together."

    if bonus == True:
        ki "I always knew getting out of my parents’ house would be great for me, but combining that with a cool, new roommate and a teacher I actually like-"
        s "So it all comes back to sex..."
        ki "Stop fucking saying that when I’m trying to hand you a puzzle piece."
        s "Oh, we’re working together now?"
        s "I just thought we were solving our own puzzles in the same room as one another."

        scene kirinthinking15
        with dissolve

        ki "Doesn’t mean we can’t check in on each other’s progress every now and then."
        ki "Basically, I’m just saying that life is changing for me."
        ki "Still have no clue if it’s a good change or a bad one, but it’s definitely something. And I’ve been dying for {i}something{/i} for years."
    else:
        ki "My wardrobe has expanded to nearly three times its original size, even if most of the clothes are gaudy and unwearable now."
        s "I think Noriko's clothes are pretty neat."

    scene kirinthinking16
    with dissolve

    ki "Thanks a lot for being such a horrible person. I was starting to think other people like me didn’t exist."

    if bonus == False:
        "That was uncalled for based on just my outlook on fashion, but I will go along with her judgement regardless."

    s "Oh, we’re everywhere. You just need to figure out how to identify us."

    if bonus == True:
        ki "I found out how to identify {i}you{/i} pretty easily. Just had to lift my skirt and offer up my v-card. "
        ki "Pretty sweet deal in exchange for being able to feel my heart beat again, don’t you think?"
    else:
        ki "I found out how to identify {i}you{/i} pretty easily. Just had to flash my Seinfeld DVD and I had you hooked."
        ki "God, that show makes me feel like such a real New Yorker."

    s "Hopefully I’ll be able to feel that someday too."

    if bonus == True:
        ki "My heart or yours? Cause you can touch my chest pretty much any time you want. Just not sure if this is the best place for it and all."
        s "I meant mine. But I will gladly grope you in front of any amount of girls."
        ki "Grope away, good sir."

    scene black
    with dissolve

    if bonus == True:
        "I reach out for Kirin’s chest."
        "She closes her eyes and-"

        mi "S-Sensei! The heck are you doing over there?!"
        s "Trying to feel whole again."
        ki "Help! I’m being assaulted!"
        s "You fucking traitor."
        ki "Miku! Come save me!"
        mi "Sensei! Start doin’ ‘yer job and put all those friggin’ traffic cones back into the storage room!"
        s "Why did you even bring them onto the stage if you weren’t going to use them?"
        ki "{i}Ahh...Sensei...{/i}"
        s "And why is Kirin making these noises?"
        mi "Because you’re grabbin’ her friggin’ boob! Girls react to stuff like that!"
        s "This is a thing I absolutely did not know as it is my first time ever touching a woman and has definitely never happened before this moment in time."
        mi "I don’t care how many times it’s happened, I-"
        mi "Well, actually...I think I kinda do care."
        mi "But just let her go and do ‘yer job!"

        "I [[reluctantly] listen to Miku and stop groping Kirin."
        "She winks at me before adjusting her bra and skipping over to Miku in the middle of the gym."
        "I wonder if she’s actually going to follow through with quitting the team or if that was just another one of many of her momentary lapses in judgement."
        "But I guess there’s no way of knowing without waiting to see how things play out."
        "Until then, I will keep solving puzzles."
        "Or creating them."
        "Or all of the above."
    else:
        "For the next ten minutes, Kirin and I play rock, paper, scissors."
        "There is no specific reason why. We just get bored and run out of stuff to talk about."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinsoccer20 = True
    stop music fadeout 5.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label kirindate25:
...
```

## Code that triggers this event

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label soccerfieldkirin:
    if kirin_lust >= 5 and christmas7 == True and kirinlust5 == False:
        jump kirinlust5
    if kirin_love >= 15 and kirindorm10 == True and kirinsoccer15 == False:
        jump kirinsoccer15
    if kirin_love >= 20 and kirinsoccer15 == True and kirinsoccer20 == False:
        jump kirinsoccer20
...
```