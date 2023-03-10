# Clouds (Kaori)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Sad Girl Special](./kaoridate15p2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Futaba: Shadowplay](./library40.md)
* [Wakana: Soup, or Another Year With You](./wakanadate5.md)

## Event properties

* Id: kaoridate15p3
* Group: Kaori
* Triggered by label: kaoridate15p2
* Chain sources: kaoridate15p2
* Chain sources path: kaoridate15p2

## Official wiki page

[Clouds](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate15p3&go=Go) for more details.

## Event code

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label kaoridate15p3:
    scene nightsky
    with dissolve4
    play music "sanctuary.mp3"

    "It’s funny how you can gradually drift from one place to somewhere on the complete opposite side of the {s}world{/s} town without ever realizing it until it’s time to go home."
    "Well, I suppose that “funny” isn’t the right word to describe that phenomenon."
    "And I suppose that “phenomenon” isn’t the right word to describe the act of simply walking."
    "But let’s say for a moment that neither Kaori nor myself walked anywhere and only happened upon places like the chicken alley and the maid cafe by wishing ourselves there."
    "If I could, I’d like to wish myself back home to avoid having to deal with the now miles we must traverse on account of Kaori not wanting to ride a bus."
    "Or, as she referred to it- a motorized wheely mega-car."
    "Regardless, our journey begins at a time when everything has already quieted down, leaving myself and one of many surprisingly loud girls I know to find things to converse about."
    "We talk about animals and machinery and the prospect of mechanized animals that you don’t have to feed."
    "Pets who would go on to live forever, completely avoiding the sometimes immediate need to console others as they come face to face with death when they least expect it."
    "These strange, fictional creatures we come up with sound quite nice."
    "And it ultimately leads me to the idea of a world in which I could just replace {i}everyone{/i} and {i}everything{/i} with a mechanized version."
    "That way, I’d never have to worry about doing something that breaks them."
    "Because I could always take them to a repair shop or something along those lines if they wound up going haywire."
    "Or, if I read the control manual really hard and paid close attention to how the machines operated, I could learn how to shut them off and do as I pleased with them whenever I wanted."
    "This is not a specific thing that Kaori and I talk about, but one of many things that pop into my mind as we round corner after corner, likely getting lost along the way."
    "Neither of us have any idea where we’re going."
    "Kaori says she does, but she’s also the same girl who refers to hands as “arm feet” and chickens as “friends.”"
    "She’s just as broken as I am. "
    "But what isn’t broken around here?"
    "I feel what I think at first to be raindrop land on my head, only to realize seconds after that it was melted snow disembarking from the gutter of a closed fish market."
    "I run my hand through my hair and bid goodbye to the droplet as it attempts to rejoin the water cycle."
    "And then a strange girl begins to say more strange things."

    scene kaorijourney1
    with dissolve

    k "Friend! Now that the sun has fallen asleep, we can begin to ask each other more interesting questions!"
    k "Like what colors we think whales are or how far we think we could throw a leg-hand-ball!"
    s "Football. And are those really your ideas of “more interesting questions?”"
    k "I want to know everything there is to know about you! I am just choosing the most interesting topics first."
    s "Why not choose something we’d be able to keep talking about after I answer?"
    k "Hmm..."
    k "Okay!"
    k "Describe to me your ideal world!"

    scene kaorijourney2
    with dissolve

    s "Huh. That’s actually a pretty good one. Why not ask things like that more often?"
    k "Long conversations make the skin flaps that cover my eyes feel heavy and, before long, I have to open my mouth really wide to lighten them."
    k "It is a strange process that I do not yet understand, but is almost always almost successful!"
    s "Almost always almost successful?"
    k "It works occasionally."
    k "Now, please proceed to tell me about the things you would do to this world if only you could."
    s "…"

    "I think about whether or not I should come clean about my newfound desire to replace everyone with machines and then decide against it because-"
    "In a sense, breaking can be beautiful too."
    "It doesn’t make me {i}happy{/i} to see people in bad conditions, but it does make everything around me feel kind of like Kaori’s eye flaps after she opens her mouth really wide."
    "It all gets lighter."
    "Everything stops falling and floats instead."
    "And so I decide to speak from the heart about the world I would create if only I could."

    s "I think the world we live in now is fine."
    s "Miserable, but fine."
    s "Weirdly enough, I think a world without misery would be even more miserable. So I’m perfectly content with where we are now."
    k "There is nothing at all you would change?"
    k "You would not turn the clouds into candy or put a smile on the sun?"
    s "Those are just visual changes. They wouldn’t really affect our day-to-day lives in any way."
    k "Raining candy would affect my daily life in many ways!"
    k "My teeth would become very bad and it would eventually become much harder to grind up food with them."
    s "Either way, I don’t really know what else I would change. "

    "Besides the machine thing, but I’ve already decided against telling her that."

    play sound "static.mp3"
    scene happy9 with flash
    scene kaorijourney3 with flash
    stop sound

    k "Liar."
    s "...I’m sorry?"

    scene kaorijourney4
    with dissolve

    k "There are many things you would change. "
    k "I know this for sure because you never smile."
    k "Who would want to live on a giant floating ball where they are incapable of contorting their facial muscles into the most important look there is?"
    s "I don’t know."
    s "Someone who’s already given up, I guess."

    scene kaorijourney5
    with dissolve

    k "Never give up, Friendburger Man!"
    k "If this world can not make you smile, all you have to do is create a new one!"
    k "Put a bunch of your favorite things into a box and shake it really hard! "
    k "What comes out will probably be really small because your arm feet can’t hold a box as big as the world."
    k "But if you close your eyes, you can pretend to jump into it and then smile once you get there!"
    k "Every day is special. But the days where your facial muscles are working properly are even more special than that."
    s "Your positivity can be really overwhelming at times, Kaori."
    k "Does it make you sad? "
    s "Not really."
    k "You appear to have caught the sadness."
    s "I have not “caught the sadness.”"
    k "It must have possessed you when it left my body in the maid realm."
    s "It’ll come back. There’s plenty more misery to be experienced in your life, I’m sure."
    k "The raspberry child told me the secret to expelling it, so everything will be kay-okay from now on."
    s "A-Okay. And sure, if that’s what you want to believe, go ahead and believe it."
    s "I’ll probably wind up being there when things get bad again, so I’ll do whatever it is I can to help as long as it’s not a major inconvenience."

    scene kaorijourney6
    with dissolve

    k "I hereby name you...Sadburger Friend Man!"
    s "I feel like I’ve doubled my nickname count today."
    k "You are a very sad burger."
    k "But since you attempted to give happiness back to me, I will now share some of it with you!"

    scene kaorijourney7
    with dissolve

    k "Would you like to see my apartment, Friend-Sad-Man-Burger-Chan?"
    k "I have heard that human males get very excited when they enter the domain of the opposite sex."
    s "I mean...I’m fine with that. But are you sure you are?"
    k "Yes! I have already informed you that John misses you! And he will be very excited to have company!"
    k "The cock will perk right up!"
    s "It already kind of is."
    k "Then the things I heard were true! Isn’t that excellent?"

    "Kaori...really does make it difficult to wallow in self-pity when she’s around."
    "Not that what I was feeling is self-pity or anything."
    "I’d probably call it something more like a melancholic longing or a...resigned exhaustion."
    "Some combination of words I’m sure she wouldn’t be able to grasp considering that it wasn’t until today that she really came to terms with how dark this place can be at times."

    play sound "static.mp3"
    scene happy9 with flash
    scene kaorijourney3 with flash
    stop sound

    k "You should stop thinking so much."

    scene kaorijourney7
    with dissolve

    s "What? "
    k "It’s no fun carrying on a talk-marathon by myself and your brain keeps going BZZZ BZZZ from the sadness cloud inside of it."
    s "The cloud normally hangs {i}over{/i} a person’s head, not inside of it."
    k "The sky is naked tonight and there are no clouds anywhere! So you must have eaten them!"
    s "…"
    s "We have to be getting close to your place by now, right?"
    k "Are your lower arm tubes also tired from all the stepping?"
    s "No, it’s just getting a little hard to keep up with a conversation that is half about my ideal world and half about noises inside of my brain."
    k "Then wish for a world where there are no noises in your brain!"
    s "That’s not really the problem here."

    scene kaorijourney8
    with dissolve

    k "Then what is, Friend?"
    k "How can I make the clouds disappear?"
    k "Ask and it shall be given."
    s "…"
    s "All I ask is that I don’t randomly wake up somewhere else one day and have to start over."
    k "You can ask for more, Friend."
    s "I’m selfish enough as is."
    k "If you are selfish, why did you tell me knock knock poems and buy me a chicken sandwich?"
    k "Is that a thing a selfish person would do?"
    s "It’s definitely not a thing {i}I{/i} would normally do. "
    s "I just have a bit of a soft spot for you, I guess."
    k "Can you tell me where the spot is so I do not accidentally touch it?"
    k "There is one part of me that the coated juice people say I can not let anyone touch no matter what."
    k "I do not want your insides to turn to mush."
    s "It’s a phrase. It means that I give you special treatment."

    scene kaorijourney9
    with dissolve

    k "Yes! That is what friendship is!"
    k "We give each other special treatment and help each other defeat sadness clouds!"
    k "Since you made my clouds go away, I, too, will destroy the BZZZ BZZZ inside of you."
    s "And what if the “BZZZ BZZZ” comes back tomorrow when you’re not around? "
    s "Are you going to quit work and become my personal the[rapist] or something?"
    k "Do not worry about tomorrow, for tomorrow will bring its own worries. Today’s trouble is enough for today."
    s "…"
    k "…"
    s "You’re so fucking weird, Kaori."

    scene kaorijourney10
    with dissolve2

    y "…"
    y "…"
    y "…"

    scene kaorijourney11
    with dissolve

    y "…"
    y "…"
    y "…"

    scene black
    with dissolve2

    "Kaori and I have to walk for what I believe is another hour until we finally make it to her apartment."
    "She remains insistent on “cheering me up” the entire way back but, to be completely honest, I feel exactly the same as I always do."
    "I imagine she just feels indebted to me after spending the day with her and using roughly half of it to push her over the hill that is death-"
    "But inviting me back to her place alone is more than enough to repay that debt."
    "I’m just hoping she may have heard a little more about what normally happens {i}after{/i} inviting someone in, though."
    "………"
    "……"
    "…"

    scene kaorijourney12
    with dissolve

    k "This is the building that I go to sleep in!"
    k "I would first like to show you the door. "
    k "Please look at the door."
    s "Okay...done."
    k "This concludes the outside portion of the tour!"
    k "I will now show you the inside of the sleep building."
    k "Please follow me, Friend-Burger-Sad-Burger-Chan-Burger."

    scene black
    with dissolve
    play sound "lock.mp3"

    s "You added “burger” way too many times. You’re just messing with me at this point..."

    play sound "dooropen.mp3"
    scene kaorijourney13
    with dissolve

    "I set foot inside of the “sleep building” and am immediately greeted by a rather small one bedroom flat with a half kitchen also serving as the entryway."
    "And, of course, Kaori’s best friend is there to say hello."

    john "BACAWK! (Ayo whaaaaaat? Man the fuck you doin’ walkin’ up in here like this?)"
    s "Hey, John. Long time, no see."
    john "BACAWK! (Yo take yo’ god damn shoes off, man. The hell you thinkin’?)"
    s "Oh. Sorry about that."

    "I kick my shoes off behind me as Kaori makes her way into the living room slash bedroom as well."

    scene kaorijourney14
    with dissolve

    k "Friend, why do you remove your foot protectors?"
    s "Because...that’s the polite thing to do."
    k "Do you intend to stay very long?"
    s "Are we...going somewhere else or something?"
    k "No. But now that you have seen my apartment, does this not mean that the final out has been hung and that the day is complete?"
    s "Did you think inviting me in just meant showing me where you lived and then...nothing else?"
    john "BACAWK (Oof. That’s rough, man.)"
    s "Stay out of this, John."

    scene kaorijourney15
    with dissolve

    k "I have never had another human in my room before. I do not know the rules."
    s "There aren’t really “rules.” I just figured I’d at least get to stay in here and talk for a while longer or something."
    k "But I must take off all of my clothing and lay in the water for at least an hour before I close my eyes and go into the sleep!"
    s "…"
    s "Can I watch?"

    scene kaorijourney16
    with dissolve

    john "…"

    "John doesn’t say anything but I know he’s judging me."

    k "Wh-wh-wh-wh-wh-wh-wh..."
    s "...Wh?"

    scene kaorijourney17
    with dissolve

    k "WHPSHHHHH!!!!"
    s "…"
    s "Was that Latin for “Get out?”"
    k "Mhm!"
    k "I’m sorry, Friend, but I unprepared my body to make room for more energy on the way home from Strawberry World!"
    s "That is absolutely not the name of the maid cafe."

    "Actually...what {i}is{/i} the name of the maid cafe?"

    scene kaorijourney18
    with dissolve

    k "I apologize for not properly understanding this time-honored tradition."
    k "But I...do not want to show you the things that you want to see just yet..."
    k "Will rubbing the co- Will rubbing John make you feel any better?"
    john "BACAWK! (I’m game if you are, man.)"
    s "Uhh..."
    s "Actually...I’ll just head out. My place isn’t all that far from here anyway."
    k "Despite the ending and my horrible mistake, I was happy to spend so much time with you today, Friend."
    k "I hope your clouds are gone."
    s "Yeah..."
    s "They’re gone."
    s "Goodnight, Kaori. "

    scene kaorijourney19
    with dissolve

    k "{i}Best{/i}night, Friend. It is better than good."
    s "Sure..."
    s "Bestnight it is, then."

    scene black
    with dissolve

    "I exit Kaori’s apartment and find myself arriving back at my porch in no time at all."
    "I don’t want to say that today was smooth sailing the whole way through or anything like that."
    "In fact, the water was pretty harsh all day long."
    "But, some way or another, we managed to avoid crashing into any rogue waves and came out with a bond much stronger than before."
    "I mean, I know where Kaori lives now."
    "And it looked exceedingly {i}normal{/i} apart from the giant chicken, so that in itself was a huge surprise."
    "I just hope that I can actually spend more than thirty seconds in there some day."
    "For now, though...it makes sense."
    "{i}She{/i} might not make sense, but the situation does."
    "And I should probably learn a little more about her before I expect her to start “properly upholding any time honored traditions” with me..."

    $ renpy.end_replay()
    $ kaori_love += 3
    $ kaoridate15p3 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label kaoridate20:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```