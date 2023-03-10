# To Die, To Sleep (Kaori)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kaori love greater than or equal to 15

* Event [What Was](./day271.md) (Main) is completed)

* Event [Abyss](./yumicallnight35.md) (Yumi) is completed)

* kaorinumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: kaoridate15
* Group: Kaori
* Triggered by label: callkaorimorning
* Triggered by branch label: callkaorimorning
* Triggered by path: callkaorimorning->kaoridate15

## Official wiki page

[To Die, To Sleep](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate15&go=Go) for more details.

## Event code

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label kaoridate15:
    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer. "
    "She’s typically working around this time but somehow always manages to pick up, so I’m not all that worried."
    "Granted, she also somehow always manages to be in every single place at once, so I’m pretty sure that there are either duplicates of her roaming around or that she’s just 90%% magic."

    play sound "phonebeep.wav"
    play music "remember.mp3"

    k "Phone call!"
    s "Well that’s a new greeting."
    k "Good morning, Friend! To what do I owe the talking today?"
    s "Just seeing what my favorite waitress is up to. Are you at work right now?"
    k "I am always at work! "
    s "Cool. Do you have time to go on break for a little bit if I swing by?"
    k "The whole day is a break! I do not have work!"
    s "But...you just said-"
    k "Friend, I have been having many lightbulbs inside of my brain and all of them are going BZZZZ BZZZZ and I believe it means there is something we must do!"
    s "Please continue to explain."
    k "I would like to spend the day with you and show you the light bulbs!"
    s "If this winds up being something like you literally needing help changing a light bulb I am going to lose interest very quickly."
    k "Darn!"
    s "Was that really what it was?"
    k "I don’t like sleeping in the dark, so sometimes my light bulbs get tired and need to take a break for the rest of forever."
    s "Isn’t one of your nicknames literally the Mistress of the Dark?"
    k "Mistress of the Burger! Let’s hang the outs for an entire day! Just you and me!"
    k "And John!"
    k "And John’s friends!"
    s "John has friends now?"
    k "Not yet! But I will explain when we get there!"
    s "Get {i}where{/i}, Kaori?"
    k "There!"
    k "I will see you soon!"
    k "Phone call!"

    play sound "phonebeep.wav"

    s "…"
    s "Phone call."

    scene black
    with dissolve

    "I decide to stop ever complaining about how Kaori starts or ends calls because, at this point, what would complaining even do?"
    "Despite not telling me where she wants to meet...I have a pretty good feeling that it’s in that alleyway with all of the chickens we’ve visited before."
    "Especially since today is apparently going to involve procuring friends for her obnoxiously large pet."
    "So, either Kaori’s landlord is about to hate her for turning her place into a chicken coop...or she somehow lives on a secret farm somewhere in the middle of Kumon-mi."
    "Both of these things seem entirely plausible for someone like her."
    "But I should probably start getting a move on if I don’t want her to wind up overpaying for a chicken or-"

    s "…"

    "God, what has happened to my life?"
    "………"
    "……"
    "…"

    scene kaoribigdate1
    with dissolve

    "Just as I expected, Kaori wanted to meet in the chicken alley- a real place that exists in Kumon-mi."
    "Well, apparently it’s not exactly a chicken alley anymore since, according to Kaori, the previous owner of the chickens recently sold them to another restaurant manager a few blocks down."
    "So the two of us make our way down this wind tunnel of a shortcut in hope of being able to purchase-"

    s "Wait, how many more chickens did you plan on buying?"
    k "As many as I can fit in my arm feet!"
    s "Hands. And I can’t imagine that is very many."
    k "Then Friend can help carry chickens as well since his arm feet are bigger and stronger!"
    s "Hands. Please stop calling them arm feet."
    k "Friend, do you know that John misses you? "
    s "How would I possibly know something like that, Kaori?"
    k "Chicken-sense! Friend-sense!"
    k "Like how I feel every time I know you are nearby!"
    s "I’m having a hard time believing you can somehow sense my presence based on nothing but our friendship."
    k "Maybe my friendship muscles are just stronger than yours?"
    s "Those aren’t even a-"
    k "Don’t doubt my feelings for you, Chickenburger Friend Man!"
    s "These names are getting out of arm feet."

    scene kaoribigdate2
    with dissolve

    k "Arm feet!"
    s "Oh God damnit."

    scene kaoribigdate3
    with dissolve

    k "Th...Thank you for coming today!"
    k "I was worried you would have turned your leg machines into escape mode when I told you I wanted to be with you for the entire day."
    s "No need to thank me. I’m the one who called you, remember?"
    k "Of course! It’s much easier to remember things from this morning than things from a long time ago."
    s "That is how memory works in most cases, yes."
    k "Are you good at remembering things, Friend?"
    s "…"
    s "Not exactly."
    k "Me too!"
    k "Did you also get hurt when you were a mini human?"

    play sound "static.mp3"
    scene happy9 with flash
    scene kaoribigdate3 with flash
    stop sound

    s "Also? "
    k "Yes!"
    k "I have told you about the juice before, yes?"

    "Ahh. I guess she’s talking about her apparent familiarity with hospitals again."
    "Am I actually about to learn why Kaori acts and speaks the way she does?"

    s "Yes. You have told me about the juice."
    s "What happened to you that...led you to the juice, though?"

    "That is absolutely not how I imagined ever asking anyone about their past."

    scene kaoribigdate4
    with dissolve

    k "WHAPAM! BOOM! KCHHHHHH!!"
    s "…"

    "And that is absolutely not how I imagined anyone ever explaining it."

    k "And on that day...a baby spider hatched!"
    k "The Mistress of the Burger Dark escaped the clutches of evil robots and started her new life as a superhero who saves furry or fluffy or feathery creatures!"

    "Or she’s just delusional."

    k "WHAPSSSSHHHHHHH!!!"

    "She is definitely delusional."

    s "What are the sound effects for, Kaori?"

    scene kaoribigdate5
    with dissolve

    k "Sound effects?"
    s "Those...sounds you were making."
    k "Do you not know Latin, Friend?"
    s "No...And neither do you."
    k "“WHAPSSSSHHHHHHH!!!” is Latinspeak for “Life is good now!”"
    s "…"
    k "…"
    s "Are you sure it was okay for you to leave the hospital?"

    scene kaoribigdate6
    with dissolve

    k "Yes! My yoke is easy and my burden is light! "
    k "There is no reason to stay in one place when the juice is but juice and the animals are elsewhere!"
    k "And so I ask you, Friend of Friends, to help me acquire more of you!"

    scene kaoribigdate7
    with dissolve

    k "To multiply the friendship in the world by a kadrillionbilliontrillion and-"

    stop music fadeout 5.0
    scene kaoribigdate8
    with dissolve

    k "Huh?"
    s "What’s wrong?"
    k "There’s nothing in the cages."
    k "This is where I was told that John’s friends would be."
    k "Do non-Kaori humans normally take chickens inside to roam around during the morning? "
    s "…"
    s "No. That’s not normally a thing non-Kaori humans do."

    scene kaoribigdate9
    with dissolve

    k "Should we find four-legged foldable rectangles to sit on them in wait of our new friends’ arrival?"
    s "Are you absolutely sure this is the right place?"
    k "Yes! I checked the address the last chicken seller gave me many times!"
    k "It is why I am not carrying food items today!"
    s "Kaori..."

    scene kaoribigdate10
    with dissolve

    k "Why do you say my name with so much sadness?"
    s "I think that maybe we’re just..."
    s "A little too late."
    k "Too late?..."
    k "Did someone else purchase the friends before I could?"
    s "Either that or-"

    play sound "static.mp3"
    scene happy9 with flash
    scene kaoribigdate11
    with flash
    stop sound
    play music "contemplation.mp3"

    k "Or what?"
    s "…"
    k "If you know what happened, please tell me."
    k "Our day can not continue until I acquire at least one new companion."
    s "When you asked the previous owner of the chickens where they’d be, what did he tell you?"
    k "That I could see them if I went to this building."
    k "But I don’t see anything at all."
    s "He didn’t tell you you could buy them, though?"
    k "He said it wasn’t up to him since they were no longer in his possession."
    s "And they were sold to another restaurant?"
    k "Yes. Another one that will not hire me. The one we are behind right now."
    s "Then...they were probably used already."
    k "Used?"
    s "Killed."

    scene kaoribigdate12
    with dissolve2

    k "…"
    k "I see."
    s "…"
    k "…"
    s "…"
    k "…"
    s "…"
    k "…"
    s "…"
    k "…"

    scene kaoribigdate13
    with dissolve

    s "…"
    k "…"
    s "Are you okay?"
    k "Friend. Can I ask you a question?"
    s "Sure. Go ahead."

    scene kaoribigdate14
    with dissolve

    k "What happens when something dies?"
    s "…"
    s "That’s not an easy question to answer."
    k "Why not?"
    s "Because it’s not really something anyone knows."
    s "For us, the ones who haven’t died, life continues to move on...albeit a little bit slower than before."
    s "But for the ones that do die, they just...stop existing."
    s "Or get reborn or sent to heaven or some other afterlife. Different people will tell you different things."
    k "What will you tell me? I trust you more than anyone else I know."
    s "I would tell you not to worry too much about it. "
    k "Because you don’t want me to be sad?"
    s "Right."
    k "But I’m already sad."
    s "…"
    k "…"
    s "Do you like poetry, Kaori?"
    k "Poetry?"
    k "Like....knock knock poems?"
    s "Those are called jokes."
    s "Poems are weird combinations of words that exist to make people feel certain ways or think certain things."
    k "Like laughter?"
    s "Sometimes, yes."
    k "How is that different from a joke?"
    s "I...don’t know."
    s "I’m not really good when it comes to cheering people up, but there’s part of a poem that just popped into my head that...might explain death a little better than I can."
    s "The only thing is that you’re going to have to imagine I’m the one who died or it will be a little awkward and not make as much sense."

    scene kaoribigdate15
    with dissolve

    k "This poem makes me feel very bad!"
    s "The poem hasn’t even started..."
    s "If imagining me dead doesn’t help, just...imagine me as one of the chickens or something."
    k "Ahh! Zombie chicken!"
    s "…"
    s "Anyway, the poem goes like this."

    scene kaoribigdate16
    with dissolve

    s "Death is nothing at all. It does not count."
    s "I have only slipped away into the next room. Nothing has happened."
    s "Everything remains exactly as it was. I am I, and you are you-"
    s "And the old life that we lived so fondly together is untouched, unchanged. Whatever we were to each other, that we are still."
    s "...And then there’s a bunch of other shit, but you should be able to get the point."
    s "Basically, life’s going to be exactly the same and this is nothing but a hiccup, even if you get all depressed right now."
    s "Also, you should be thankful that I don’t think of you as an actual human being, because doing that with anyone else is not something I think I’d be able to live down."
    k "I had no idea Friend was so good with words! Did you write that?"
    s "No. I haven’t written anything in a very long time."

    scene kaoribigdate17
    with dissolve

    k "Well your poem did not make me feel better, but I am impressed by how smart you are to remember so many things!"
    s "Thanks. But this wasn’t really about trying to show you how smart I am."
    k "No no! This is a good thing!"
    k "You said you were bad at remembering, but you remembered all of those words!"
    k "Do you know any poems about chickens?"
    s "Are you sure that hearing about chickens will make you feel better when chickens are kind of the reason you’re upset in the first place?"
    k "I am not sad because of the chickens."
    k "I am sad because of how cruel human beings can be."
    k "But you have reminded me that not everyone is evil by confusing me with your strange knock knock joke."


    scene black
    with dissolve

    "Kaori turns around and begins to walk over to a strange table full of random objects several feet behind us."
    "I’m sure it’s something just used by the employees of one of these restaurants for their breaks or something along those lines, but I can’t help but feel like it’s eerily out of place."
    "She lifts up a stuffed rabbit and hugs it tightly before sitting down and starting to play with its ears."

    scene kaoribigdate18
    with dissolve

    k "When Mini-Kaori got hurt a long time ago, she learned that the people she used to live with got hurt a lot worse."
    k "So bad that they disappeared forever. Like one of my light bulbs."
    k "But Mini-Kaori didn’t remember those people when she woke up, so she didn’t feel any pain other than what was in her body."
    k "If losing friends I never became friends with is as painful as this, what should Mini-Kaori have felt when people she actually loved died?"
    s "Worse. Which is why I’m confused about your smile right now."
    k "If I don’t smile, my eye-water will come rushing out and Friend will need to squeeze me to make me feel better."
    s "I’m fine with squeezing you if you want to cry, you know."
    s "Just don’t expect another poem or any advice or something like that."
    k "If you squeeze me, you must squeeze this rabbit as well! He is a replacement friend to help me cope with the death of John number two through however many I could fit in my arm feet!"
    s "You know, I feel like this is a good opportunity to teach you about stealing being wrong, but whoever left all this stuff out here is basically asking for it to be stolen."

    scene kaoribigdate19
    with dissolve

    k "I am very sorry our fun day together had to begin with such despair. "
    k "Do you feel your shadow growing larger, Friend?"
    s "It’s...about the same?"

    scene kaoribigdate20
    with dissolve

    k "Then we should leave this place and go somewhere even more exciting!"
    s "Pretty much anywhere would be more exciting than a random alleyway several blocks away from one of your workplaces."
    k "Then take me to the most exciting place you know!"
    k "A place where normal female humans like me can have a good time with their normal male friends after suffering great loss!"
    s "…"
    k "A place with things I can consume because I have the hunger!"
    s "…"

    scene black
    with dissolve

    "The most exciting place I know, huh?"
    "..."
    "That can only mean one thing."

    $ renpy.end_replay()
    $ kaoridate15 = True
    $ kaori_love += 1
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "………"
    "……"
    "…"

label kaoridate15p2:
...
```

## Code that triggers this event

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label callkaorimorning:
    if kaori_love >= 0 and kaoridate1 == False:
        jump kaoridate1
    if kaori_love >= 10 and kaoridate5 == True and kaoridate10 == False:
        jump kaoridate10
    if kaori_love >= 15 and day271 == True and yumicallnight35 == True and kaoridate15 == False:
        jump kaoridate15
...
```