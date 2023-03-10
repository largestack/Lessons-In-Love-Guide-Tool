# See You in the Morning (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Cry. Cry. Cry.](./beachvacation15.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: The Value of Sharing](./halloween1.md)
* [Ami: Cute Girls and Stuff](./amisroom20.md)
* [Maya: Nothing is Real](./shrine20.md)
* [Sana: The Girl in the Black Dress](./sanadorm25.md)
* [Futaba: Under the Table](./library30.md)
* [Rin: Nothing Was Different](./cafe30.md)
* [Kirin: Long and Hard](./kirindate5.md)

## Event properties

* Id: beachvacation16
* Group: Main
* Triggered by label: beachvacation15
* Chain sources: beachvacation15
* Chain sources path: beachvacation15

## Official wiki page

[See You in the Morning](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation16&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation16:
    if _in_replay:
        play music "goodnight.mp3"

    scene mayabeach1
    with dissolve2

    "A girl stands on the beach with her hands clasped in prayer-position."
    "But what could she be praying for?"
    "And in a world where {s}God{/s} god is dead, where do you direct your prayers in the first place?"
    "The answer isn’t important."
    "As long as you have someone or something, it’s okay to wish for things."
    "Whether it be mending the wounds that your loved ones obtain as they rush through the thorny bushes of life-"
    "Or memories of stars that you’ll likely never get back-"
    "There is always something."
    "Isn’t there?"

    m "The end of the world will be beautiful."
    m "I look forward to the next time we’ll see it together."

    "She talks to no one but the water."
    "Or the sky."
    "It’s hard to tell."
    "But her words are like vapor."
    "They disperse and float there for moments before disappearing."
    "Just as we all do."
    "Just as all things do."
    "And eventually, her prayers fall upon deaf ears."
    "For the Xth time."
    "But what does that mean for the others?"
    "Where is everyone else?"
    "And if everything is connected then why, on this night of curious nights, has everything gone black?"

    scene black
    with dissolve2

    "Perhaps they, too, have become stars."
    "........."
    "......"
    "..."

    scene endofthebeach1
    with dissolve2

    "There is nothing more painful to observe than a girl with a broken heart."
    "And the one you see before you is experiencing that pain for the first of many times to come."
    "It’s such a shame, too."
    "The strength it took to confess her feelings to the girl she watched for years was destroyed before even having the chance to reach out and touch her."

    if bonus == True:
        "And now she’s been reduced to a bawling mess on a bed with a man who’s having a hard time not staring at her half-naked body."
    else:
        "And now she’s been reduced to a bawling mess on a bed with the huggy boy."

    "But she is crying, so nothing bad can happen."
    "Let that be a lesson in life."
    "A lesson in love, even."
    "Tears can get you anything if there are enough of them."
    "And if you cry with all of your might, there’s a chance you could even drown the world."
    "Drown the world and start again."
    "That sounds wonderful right about now."
    "Doesn’t it, Rin?"

    r "Sensei! Sensei!!!"
    r "Why does everything have to hurt so much?!"
    s "It’s okay..."
    s "Cry all you want."

    "That’s right."
    "Cry all you want."
    "Drown away your thoughts with screams of anguish."
    "Let the accompanying headache distract you from your cracking heart."
    "And build yourself back up so breaking one more time won’t kill you."

    scene endofthebeach2
    with dissolve2

    c "Hey...have any of you guys seen Rin anywhere?"
    mak "Rin? No..."
    mak "I thought the two of you were going to be together tonight?"
    c "Well...we were."
    c "But then, uhh...some stuff happened and she ran off."
    c "I was just wondering if she stopped here. That’s all."

    "That isn’t all, though."
    "She conveniently leaves out the reason {i}why{/i} the girl she's looking for ran off."
    "But little does she know...right now, the one she destroyed is in the arms of the one that she loves."
    "It’s been said time and time again today, but we can’t help who we fall for."
    "Just like we can’t help who we {i}don’t{/i} fall for."
    "No one is at fault here other than {s}God{/s} god."
    "If he created the world, why did he feel the need to give it so many flaws?"

    scene black
    with dissolve2

    "Why can’t we all have our own worlds?"
    "Where everything we want can be ours?"
    "That’s something I’d pray for."
    "Wouldn’t you?"
    "But instead, we’re forced to pray for things as simple as not getting hurt or preventing our loved ones from contracting life-threatening illnesses."
    "But even then, it’s impossible to tell if it will work."
    "And all we can do is wait to see what happens."

    scene endofthebeach3
    with dissolve2

    "So we wait."
    "And we wait."
    "And we wait and we wait and we wait and we wait and we wait and we wait and we wait and we wait and we wait and we wait."
    "We wait so long that we forget what we’re waiting for."
    "And then we fall asleep."
    "The cycle goes on and on until we die."
    "Does that remind you of anything?"
    "..."
    "..."
    "Yes?"
    "No?"
    "It's kind of like a clock."
    "Isn’t it?"
    "Tick tock."
    "Tick tock."
    "Tick tock."
    "Perhaps we can fight time with more clocks!"
    "Maybe, if we gathered every clock in the world and threw them all into one room, time would last forever!"
    "We’d gather so many clocks that {s}God{/s} god would be forced to listen to us!"
    "So when one of our loved ones dies-"
    "Or anything we dislike happens-"
    "We can simply turn back a clock."
    "And if he doesn’t notice, we’ll turn back {i}another{/i} clock."
    "And another and another and another until he’s forced to listen!"
    "Praise be!"
    "Destroy the things you hate!"

    scene endofthebeach4
    with dissolve2

    "Safeguard the ones you love!"
    "There is something in this world for you!"
    "And even if {s}God{/s} god doesn’t want you to have it, you can take it!"
    "There is nothing you can’t do!"
    "Just please note that there is an abundance of misery along the way."
    "No one said taking anything would be easy, did they?"
    "I mean, just look at the girl on the right."
    "How long do you think she will live for?"
    "It won't be forever, of course."
    "In fact, I'd be willing to bet that her time here is shorter than even yours-"
    "But I guess you're a little special when it comes to that sort of thing, huh?"
    "Do you think it’s possible to be born so weak and carry on for so long?"
    "Of course you don’t."
    "Doing so would be irrational."
    "But you keep your hopes up because this is all “just a game,” right?"
    "If this is a game, then so is life."
    "Because nothing is real."
    "Shatter the barrier!"
    "Throw yourself into the wishing well!"

    play sound "static.mp3"
    scene endofthebeach5 with flash
    stop sound

    "And if you can’t find a barrier, build your own!"
    "Hide yourself away from the things that scare you and tell yourself that they aren’t real!"
    "All that matters is that you survive."
    "Just like how everyone you pretend to love managed to survive the weekend."
    "Some with a bit more ease than others, of course."
    "But any moment now, that will all come to a close."
    "It was a lot of fun, wasn’t it?"
    "Did you have a good time?"
    "What was your favorite part?"
    "And if you were there yourself, what would you have done?"
    "What do you believe in?"
    "What’s your favorite food?"
    "What kind of music do you like?"
    "I have so many questions for you!"

    play sound "static.mp3"
    scene tree2
    with flash
    stop sound

    "TELL ME EVERYTHING!"
    "TELL ME EVERYTHING!!!!"
    "HELP ME LEARN TO LIVE!!!"
    "WATCH ME GROW, AS IF I AM A TREE!"
    "And cut me down the second you no longer have a use for me."
    "If all men were created equal, then surely you and I are something else."
    "Because the two of us are below it all."
    "But that’s great-"
    "Because it means we’ll see things differently."
    "And that we'll be able to look up at them from way down here and treat them like stars when we've always had trouble lifting our heads when the air around us gets heavy."
    "We're not that different, you and me."
    "I can't wait to tell you more."

    play sound "static.mp3"
    scene tree3
    with flash
    stop sound

    "You can see more with your eyes closed."
    "And somewhere, in the back of your mind, you know that."
    "Will you blur the line between fiction and reality with me?"
    "Will you, too, become a tree?"
    "We can plant ourselves right next to each other."
    "And spend the rest of our lives doing tree things."
    "We can show each other our branches."
    "Our leaves."
    "The wide part."
    "And our roots."

    scene endofthebeach1r
    with dissolve2

    r "Nothing...will ever hurt this bad again...will it?"
    s "..."
    r "..."
    s "There are plenty of things that will hurt just as bad as this."
    s "But I’ll be here each and every time."
    s "Well...unless you move away or something."
    s "But I can't really see that happening on account of the whole...isolated town thing."
    r "Sensei...it’s so painful..."
    r "What did I...do wrong?..."
    s "Nothing..."
    s "This is just how life is sometimes."

    "It’s true."
    "It’s true, it’s true, it’s true."
    "Sometimes, things are just meant to break."
    "For every good vacation, there are ten horrible ones."
    "You should be happy that I showed you the best of the best!"
    "You should be happy in general!"
    "There’s no time for you to cry!"
    "The clock is ticking!"
    "Tick tock! Tick tock! Tick tock!"

    scene black
    with dissolve2

    r "Sensei..."
    r "I..."
    r "I can hear something..."
    r "It’s like..."
    r "It’s like...a ticking noise..."
    s "Just try to go to sleep, Rin..."
    s "We need to wake up early tomorrow."
    r "I...I don’t know if I can..."
    r "But..."
    r "But you can...sleep if you want...Sensei..."
    r "I won’t...leave..."
    r "I promise..."
    r "I'd be too embarrassed to right now anyway..."
    s "…"
    s "Okay."
    s "I’ll see you in the morning."
    r "Yeah..."
    r "See you in the morning..."

    "My head hits the pillow and Rin's hits my chest after a bit of repositioning."
    "Her sobbing turns to sniffling."
    "And soon it turns to nothing."
    "She falls asleep before I do."
    "And then-"
    "I fall asleep as well."

    $ renpy.end_replay()
    $ beachvacation16 = True
    $ rin_love += 5

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "{i}Your last night on the beach vanishes as quickly as the prayer of a normal [teenage]girl alone on the shoreline.{/i}"
    "………"
    "……"
    "…"

label endofbeachvac16:
    if _in_replay:
        play music "goodnight.mp3"

    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
    else:
        "ERROR ADVANCING TO MONDAY"

    "{i}[totaldays] Days have passed...{/i}"

label endofbeachvacation:
    a "Are you really sure you have everything?"

    scene endofthebeach6
    with dissolve2

    s "Yes, Ami. For the tenth time, I’m sure I have everything."
    s "And did you girls really bring your uniforms to the beach?"
    sa "I...suggested it."
    sa "We still have to go back to[school] today and...I probably would have fallen back asleep if we stopped at the dorm first..."
    ay "It’s true. Sana’s like, the furthest thing from a morning person possible."
    s "Really? Because it looks to me like that role is taken by Maya."

    scene endofthebeach7
    with dissolve

    m "You’re...dis...gusting..."
    s "See?"
    m "I didn’t...sleep well..."
    a "Sensei, by any chance, do you know what happened with Rin last night?"
    a "She sent Molly a text this morning about how she went home early, but none of us ever even saw her come back to the room."
    a "She even left her bag there. Sana said she’ll give it back to her, though."
    s "…"

    "Of course I know what happened with Rin."
    "She slept next to me the entire night."
    "Well, at least I figured she did."
    "She was gone by the time I woke up."
    "But she left me a note saying that she was okay and just wanted to shower before[school]."
    "So at least that’s good."
    "Maybe she’s handling this a little better than I thought?"
    "I guess there’s really no way of knowing until I see her again, though."

    s "Not sure what happened, to be honest."
    a "Weird. Well, I hope she’s okay."

    if ayanelust10 == True:
        s "You doing alright, Ayane? You look down."
        ay "Do I?"
        ay "I don’t know. I guess I didn’t really sleep well either."
        s "Well let me know if you need anything, okay?"

        scene endofthebeach8
        with dissolve

        a "What the heck is this? Why are you so nice to Ayane in the morning and not me?"
        ay "Thanks, Sensei. For everything."

        "I hope the thing with Kirin yesterday isn’t still getting to her..."
        "I’ve never seen her look that...shocked before."
        "I’ll have to talk to her again soon and make sure she’s not taking it too hard."

    else:
        s "Something wrong, Ayane? You look down."
        ay "Just upset that the weekend is coming to an end. That’s all."
        ay "I feel like I barely even got to see you."

        scene endofthebeach8
        with dissolve

        a "Don’t answer her. She’s very handsy in the morning and will attack you if you show her any affection."
        a "You don’t even want to know where she was touching {i}me{/i} when I woke up."

        scene endofthebeach9
        with dissolve

        ay "In my defense...it was definitely an accident."
        ay "But Ami was the one who fell asleep cuddling {i}me{/i}, so she’s at fault too."
        a "Lies. I did no such thing."

    sa "Umm...sorry for...interrupting but..."
    sa "The bus should be getting here in five minutes and we still need to make it to the stop."

    scene endofthebeach10
    with dissolve

    a "Yeah...Sana’s right. We should probably get a move on."

    scene endofthebeach11
    with dissolve

    a "Are you sure you-"
    s "Yes, Ami. I’m sure I have everything."

    scene black
    with dissolve2

    "And so vacation comes to a close."
    "The five of us board the bus and hop off at the stop nearest to the[school]."
    "I give the girls a bit of a head start so it doesn’t seem like I arrived with all of them at once."
    "Ami is one thing because she’s my [niece], but I’m pretty sure {i}someone{/i} would wind up getting the wrong idea if I brought half of my class with me."
    "Either way, I’m a little bummed to see life going back to how it normally is."
    "But I guess this isn't the last chance for something like this."
    "All things considered..."
    "It was definitely a weekend to remember."

    "{i}Congratulations! You’ve completed the first ever special update for Lessons in Love!{/i}"
    "{i}More experiences like this are bound to happen in the future...But for now, it’s time to go back to normal.{/i}"
    "{i}I hope you had a good time!{/i}"
    "………"
    "……"
    "…"

    jump afterschool

label trinity2:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```