# Watermelons and Violin (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 25

* Event [Close Your Eyes](./mayadorm20.md) (Maya) is completed)



## Next events

* [Maya: FLAVOR BEAM!](./mayadorm25.md)

## Event properties

* Id: shrine25
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->shrine25

## Official wiki page

[Watermelons and Violin](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine25&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine25:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "It’s another hot day here at the end of Summer."
    "The shrine is uncrowded, as per usual on days like this."
    "A cool breeze sweeps through the grounds and provides temporary respite from the harsh rays of the sun."
    "Maya is nowhere to be found."
    "She’s probably hiding from me."
    "She seems to do that rather frequently, I’m finding."
    "It’s a little confusing given that I’ve never really gotten anything out of it other than seeing her in a cute outfit, but..."
    "There are plenty of girls in plenty of places- each with their own cute outfits."
    "Why am I gravitating to the one who’d sooner save a watermelon from falling off of a cliff than me?"
    "Sure, there aren’t many scenarios I can imagine where she’d be forced to choose between those two things-"
    "But we all know which one she’d pick if she was forced to."

    scene black
    with dissolve

    "I take a look around the shrine, checking all of her usual spots."
    "She’s not in any of them."
    "Wait. No."
    "She has to be somewhere."
    "Every time I think to myself, “Maybe she has the day off,” I wind up finding her in another peculiar place."
    "I just need to completely scan the area..."
    "………"
    "……"
    "…"

    scene mayaglow1
    with dissolve

    "After another five minutes or so, I spot her finding refuge in an old, otherwise unused booth of the shrine."
    "She doesn’t notice me approaching as she focuses on the world around her."
    "Dust particles, which had remained undisturbed for {s}God{/s} who knows how long, swim through the space around her and find their place among the air we breathe."
    "Did you know that the average human being consumes almost 10 lbs of dust every year?"
    "I wonder how many other things we unknowingly consume."
    "I wonder how our lives would change if we knew about them."

    s "Hey."

    scene mayaglow2
    with dissolve

    m "...Hi."
    s "I found you."
    m "Yes. It appears you did."
    m "I’m running out of safe places to take shelter."
    m "I might need to start tending to another shrine soon."
    s "Would you really go through the hassle of finding another shrine just to get away from me?"
    m "I wouldn’t need to find them. I know where they are."
    s "Oh. Well, could you tell me? I’d like to check them out."

    scene mayaglow3
    with dissolve

    m "Do you really think I’m going to fall for such an obvious ploy?"
    s "What ploy? Maybe I just...really like shrines?"
    m "The first time you came here, you said you didn’t even know why you’d shown up."
    m "I doubt that the time you’ve spent here has, in any way, sparked your interest in them."
    m "I don’t even think I’ve seen you pray yet."
    s "And you likely never will. There’s no point in praying."

    scene mayaglow4
    with dissolve

    m "A right and a wrong answer wrapped together in one sentence. How interesting."
    s "What do you mean by that?"
    m "Praying isn’t entirely pointless as long as the person doing it believes that something will happen in response."
    m "Of course, this doesn’t change the fact that anything that comes subsequently will be the result of coincidence rather than divine intervention-"
    m "But beliefs are beliefs nonetheless."
    s "So is that why you spend so much time here? To help people believe?"

    scene mayaglow2
    with dissolve

    m "Not at all. I couldn’t care less about what other people believe."
    m "I don’t even like shrines. "
    s "Then you should probably find a job that you enjoy. I’m sure there are plenty of girls who actually believe in god who would be happy to spend their afternoons sweeping up here."
    m "Probably. But that’s just not how things are supposed to go."
    m "Besides, I look cute in this dress."
    m "Can you honestly look at me and tell me I don’t belong here?"
    m "Actually, wait. Don’t answer that. I feel as if you’ll talk for hours on end about it."
    s "I like you more when you’re not being conceited."
    m "Then I will continue to praise myself so your disdain for me may grow as if it is a tree."

    if trinity1track == True:
        play sound "static.mp3"
        scene callous19
        with flash
        scene mayaglow2
        with flash
        stop sound

    "I’m not sure what it is about that last sentence, but it pisses me off for some reason."
    "It’s not uncommon for Maya to say things for the sole purpose of making me feel like shit, but that one was just different."
    "I wonder why?"

    scene mayaglow4
    with dissolve

    m "Are you excited for the cold?"
    m "You’ve always liked winter more than Summer."
    m "It’s one of the few things we have in common."
    s "More than anything, I think I’m just excited to see everyone in their winter clothes. "
    s "Summer clothes are nice and all, but they just don’t have the same appeal as a girl dressed in layers."
    m "You’re disgusting."
    s "How is it disgusting wanting to see a girl in {i}more{/i} clothes?"

    if bonus == True:
        m "It’s disgusting that you felt compelled to share your sexual attractions with me in response to a wholesome question."
    else:
        m "I don't know. It just is."

    m "What even are you?"
    s "I’m a normal [teenage]girl."

    scene mayaglow5
    with dissolve

    m "..."
    m "Why is everyone doing impressions of me lately?"
    m "It’s starting to get on my nerves."
    s "To be fair, you make it very easy."

    scene mayaglow6
    with dissolve

    m "Hah...Yes, I suppose I’ve become rather predictable over time."
    m "But that doesn’t excuse mocking someone."
    m "Please leave the shrine as penance for your actions here today."
    s "Nah, I want to stay here and talk more about the weather with you."

    scene mayaglow7
    with dissolve

    m "Wow, what an interesting topic for conversation."
    s "Weren’t {i}you{/i} the one who brought it up in the first place? I’m just following your lead."
    m "Being interesting hasn’t ever been one of my strong suits."
    s "That’s not true. You’re plenty interesting."
    s "Just in the “I have no idea what you’re talking about” way rather than the “What an exciting person to be around” sort of way."

    if bonus == True:
        m "Thank you for your wonderful, in-depth analysis of my character. Please include that in my recommendation letter for college."
        s "Jokes on you. You’re never going to make it to college if the world keeps resetting every few months."
    else:
        m "Thank you for your wonderful, in-depth analysis of my character. I look forward to reading more of your future fan theories."
        s "Joke's on you. I already have the whole game figured out."

    scene mayaglow8
    with dissolve

    if bonus == True:
        m "No. I suppose I won’t. "

    m "Perhaps I’ll finally find it in myself to ask for a class-transfer once the next cycle starts?"
    s "Oh, about that. There’s something I’ve been wondering."

    scene mayaglow9
    with dissolve

    m "You? Wondering something?"
    m "I’m absolutely shocked."

    scene mayaglow2
    with dissolve

    m "What is it?"
    s "How exactly is this whole switch to winter thing going to work?"
    s "There’s not much time left in the[school] year as-is, so it seems like winter is going to fall right around the same time that things start over."
    m "Correct."
    m "I'll be finalizing the switch during the next reset."
    s "You can change the weather as well?"
    m "Not exactly. It's complicated."
    s "Well...won’t everyone think it’s a little weird if it’s snowing in the middle of the[school] year?"

    scene mayaglow1
    with dissolve

    m "You really took your time asking that question, didn’t you?"
    m "You’re not wrong in being confused about it."
    m "While it’s true that most people would think snow in the middle of the[school] year is strange, something about the flow of time here prevents that from happening."
    m "It’s as if everyone’s perception of time itself resets along with the world."
    m "It’s just one more thing I don’t yet understand."
    s "That sounds...strangely convenient."

    scene mayaglow11
    with dissolve

    m "I can assure you that there is nothing convenient about this world at all."
    m "It’s filled with horrible things. Yourself included."
    s "Oh come on. I didn’t even say anything to warrant being insulted this time."
    m "Your existence itself is enough to warrant being insulted."
    s "Thanks. I love you too."

    scene mayaglow10
    with dissolve

    m "Anyway..."
    m "You needn’t concern yourself with something as trivial as how those around you will think of snow during the[school] year."
    m "There are many things that will happen in the future that are sure to confuse you."
    m "I am no exception to that. "
    m "The important thing is that you live each day as if you are meant to be here."
    m "Question everything, but accept that many things seem to come without answer."
    m "But most importantly, don’t be afraid."
    m "You, too, shall vanish one day."
    m "It’s absolutely imperative that you be ready for it at any given moment."
    s "…"

    "I hate hearing things like that."
    "I heard it on the beach, too."
    "It’s great that someone like Maya exists to shine light on the world I was reborn into-"
    "But each time I’m reminded that my existence is just as fleeting as a six-month Summer, I can’t help but be swallowed by dread."
    "It really could happen at any given moment."

    s "What are you going to do if that does happen?"

    scene mayaglow11
    with dissolve

    m "Hm?"
    m "Do you mean if it happens to {i}you{/i}? Or if it happens to me?"
    s "Both, I guess."
    s "How would your life change if this version of me were to vanish?"
    s "And how would it change if you were the one to vanish instead?"
    m "I don’t like that question. Ask a new one."
    s "What? Why?"
    m "It’s not easy to answer. It would take far too long."
    m "Let me ask you a question instead."
    m "What would {i}you{/i} do if this version of me vanished?"
    m "What if, after the next reset, there was a brand new Maya Makinami?"
    m "One who didn’t know too much about the world."
    m "One who didn’t know too much about you."
    m "Would you treat her the same way you treat everyone else?"

    if bonus == True:
        m "With lascivious glances and spontaneous visits to her dorm room in the middle of the night?"
        m "Would you view her as another piece of the puzzle? Another girl in the harem?"

    m "Or would you try to bring the old one back?"
    s "…"
    m "…"
    s "You’re right. This {i}is{/i} a hard question."

    "While I do like the idea of a Maya who doesn’t look at me with dead eyes every time I see her, would that {i}really{/i} be Maya?"
    "No. Of course not."
    "Even if she had all the same interests...watermelons and violin, those dead eyes are what I expect to see each and every time we meet."
    "Replacing them with brand new ones just wouldn’t feel right."

    scene mayaglow12
    with dissolve

    m "I’m glad you understand."
    m "You haven’t been here long, so I won’t fault you for believing that a world like this has its own unique set of benefits and positives."
    m "But the negatives that come with it are much worse."
    m "It’s hard enough living each day knowing that death could come at any moment."
    m "But a place like this will remind you of that with each and every passing second."
    m "Nothing lasts forever, even when it does."
    s "..."
    m "..."

    scene mayaglow2
    with dissolve

    m "Well, I suppose that’s enough sentimentality and exposition for the day."
    m "Please leave now."
    s "Wait, really? I thought we were about to have a breakthrough."
    m "We were not."
    s "But what about all of that stuff about how death could come at any moment? What if I disappear on the way home?"
    s "Wouldn't you be upset?"
    m "I have the worst luck out of anyone in the world, so I firmly believe you’ll be back here as soon as you possibly can be."
    s "Well {i}sorry{/i} that my continued living adds to your misfortune."
    m "Apology accepted. Goodbye now."
    s "…"
    m "…"
    s "...Fine."
    s "But I’m only leaving because I have other stuff to do."
    m "And to think you’ve called {i}me{/i} tsundere on multiple occasions..."

    scene black
    with dissolve2

    "The dust settles and the sun begins to disappear behind the clouds."
    "Maya retreats into another section of the shrine and I, just as always, must figure out what to do with the rest of my time today..."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine25 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine30:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
    if maya_love >= 20 and beachvacation16 == True and mayadorm15 == True and shrine20 == False:
        jump shrine20
    if maya_love >= 25 and mayadorm20 == True and shrine25 == False:
        jump shrine25
...
```