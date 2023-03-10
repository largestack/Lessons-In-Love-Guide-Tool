# Unpaid Promotion (Molly)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Molly love greater than or equal to 15

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Molly: The Legacy of Thaum Pt. II](./mollycafe20.md)
* [Noriko: Mouthjob](./convenience5.md)

## Event properties

* Id: mollydorm15
* Group: Molly
* Triggered by label: mollydorm
* Triggered by branch label: mollydorm
* Triggered by path: mollydorm->mollydorm15

## Official wiki page

[Unpaid Promotion](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm15&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm15:
    play sound "knock.mp3"
    stop music fadeout 60.0

    s "Hey, Molly. Are you home right now?"
    mo "Is that you, Sensei?"
    mo "I’m having a hard time hearing over how much fun I’m having!"

    if bonus == True:
        s "…"
        s "Are you like, masturbating or something?"
        mo "Even better!"
        s "{i}Than masturbating?{/i}"

    mo "Why don’t you come on in and take a look?!"
    s "…"
    s "I mean...okay, I guess."
    s "You’re kind of weirding me out, though."

    scene black
    with dissolve2

    "{i}Hi, guys! It’s me, Selebus.{/i}"
    "{i}Before we go into Molly’s room, I just want to let you all know about this awesome game I've been playing called Raid: Shadow Legends.{/i}"
    "{i}You see, I’ve never been much of a mobile gamer, but forget EVERYTHING you know about mobile games because Raid: Shadow Legends is the single most ambitious mobile game of the year.{/i}"
    "{i}But I’m sure you’ve heard that a thousand times before, right?{/i}"
    "{i}And that’s probably because with over 300,000 reviews and a nearly five star rating on all app stores, EVERYONE can agree that Raid: Shadow Legends is worth the hype!{/i}"
    "{i}So, without wasting any more of your time talking about Raid: Shadow Legends, I’ll let you get back to the game.{/i}"
    "{i}Lessons in Love, I mean. Not Raid: Shadow Legends.{/i}"
    "{i}But of course, the chances of anyone reading this are slim to none since Raid: Shadow Legends is the most innovative, awesome game of all time.{/i}"
    "{i}There’s literally no reason to play other games anymore!{/i}"
    "{i}But I guess if you really want to keep playing Lessons in Love instead of Raid: Shadow Legends, I should let you finish opening the door.{/i}"
    "{i}Before I go, though-{/i}"
    "{i}Just kidding. I won’t rant anymore.{/i}"
    "{i}Enjoy Molly’s next dorm event.{/i}"

    "………"
    "……"
    "…"

    scene mollyraid1
    with dissolve
    play music "rapid.mp3"

    "I walk into Molly’s room to find her sitting on her chair, absorbed in some game on her phone- the same way she always is."
    "But something about the air in the room this time makes me feel like she might be playing the most innovative action RPG on mobile platforms, Raid: Shadow Legends."

    mo "Oh! Hey, Sensei!"
    mo "As much as I’d love to put the phone down I’m just...kind of in the middle of something here."
    s "I can see that. You really look like you’re enjoying yourself right now."
    mo "Oh, but I am! I’m having more fun than I’ve ever had at any point in my life!"
    mo "In fact, I’m questioning whether or not I should keep coming to[school] or if I should just sit at home and play this game until I turn into dust!"
    s "What game are you playing, Molly?"

    scene mollyraid2
    with dissolve

    mo "I’m playing Raid: Shadow Legends! It’s only the most unique, action packed game of the last six million years!"
    mo "Filled with ultra realistic graphics and detailed character designs, Raid: Shadow Legends looks more like a console game than a game you play on your phone!"
    s "I was actually thinking that you were playing Raid: Shadow Legends the second I walked in here. "
    s "I mean, it’s the only logical explanation for the look of childish excitement and passion in your eyes."
    mo "Sensei! I had no idea you also played Raid: Shadow Legends!"
    mo "If you’re a new player, make sure you use the code MayaIsANerd to start with 50,000 extra silver!"
    mo "You’ll also gain access to a special tournament with special in-game prizes!"
    mo "But hurry up! Because the community behind Raid: Shadow Legends is growing fast and you never know when they’ll make this totally free game pay to win!"
    s "But Molly-"
    mo "Yes, Sensei?"
    s "I thought the developers of Raid: Shadow Legends were so confident in their game that they would NEVER resort to something like that."
    mo "That’s a good point, Sensei! The drops and rewards you receive from even being a free to play Raid: Shadow Legends member make coming back to the game every day so much more exciting!"
    mo "And with the best graphics in mobile games today, that excitement just keeps growing."
    mo "I mean, how else would Raid: Shadow Legends have gained over ten million subscribers in the last six months?"
    mo "And not only that, but it has over fifteen million downloads in that same exact time frame!"
    mo "That means half of the users who play Raid: Shadow Legends like it SO much that they delete it just to download it again!"
    s "Two copies of Raid: Shadow Legends? Doesn’t that seem a little excessive to you?"
    mo "Not at all, Sensei. In fact, before starting Raid: Shadow Legends, I kept hearing a bunch of things about it."
    mo "So, I decided to throw some hours at it and, I’ve gotta say, it really is just as good as the 300,000 reviews on the app store make it out to be."
    mo "In fact, even the app store itself agrees! That’s why Google Play nominated it for an award for being one of its top RPGs!"
    s "What I like most about Raid: Shadow Legends is that it’s got a really cool story mode, active PVP arenas, dungeons, and sixteen different factions."
    mo "Those are all great features, but what {i}really{/i} makes the game for me is that it has hundreds of heroes for you to collect and customize, with more being released every month!"
    s "Yeah. If I remember correctly, you gain rewards like armor, currency, and characters like Arbiter for just learning how to play the game."
    mo "And what better time to learn than now with login rewards every single day for the first 90 days! Have you ever heard of an offer that good?"
    s "Wow. Maybe you {i}should{/i} drop out of[school], Molly."
    mo "I mean, it {i}would{/i} give me a lot more time to take place in the new, highly anticipated Faction Wars system."
    s "Did you just say FACTION WARS?"
    mo "That’s right! {i}Faction Wars{/i} is an all new game mode that pits faction against faction in a fight for honor and glory."
    mo "It’s up to you, the player, to form a team of champions in order to enter the crypts and take down the powerful demonic leaders inside of them!"
    mo "The better you perform on each stage will net you huge rewards, with some even being brand new heroes!"
    s "Holy fuck. You should drop out {i}immediately{/i}."

    scene mollyraid3
    with dissolve

    mo "You really think so? But what will I do about money?"
    s "Who needs money when you can succeed even as a free to play player in Raid: Shadow Legends."
    s "All you need to do is log on and you’re already profiting."
    s "It’s fucking insanity, Molly."

    scene mollyraid4
    with dissolve

    mo "I...I can’t believe it..."
    mo "It’s like...everything I’ve wanted is finally within my reach, Sensei."
    mo "Will you...drop out with me?"
    s "Yes. And do you want to know why?"
    mo "Because in Raid: Shadow Legends, you can join a clan with your friends and everyone’s contributions to clan boss fights add up and help you take down the biggest, baddest enemies in the game?"
    s "{i}Exactly.{/i}"
    mo "But...but what about all of the other girls? I don’t think any of them play Raid: Shadow Legends."
    s "FUCK those girls. We don’t need them."
    s "They’re missing out on the most innovative mobile game of the last seventeen millennia."
    mo "It’s crazy to think that Raid: Shadow Legends has also been clinically tested and is now a proven cure for type 2 diabetes."

    if bonus == True:
        s "After the first time {i}I{/i} played Raid: Shadow Legends, my penis grew six more inches and I can now hold an erection for two whole hours."
    else:
        s "After the first time {i}I{/i} played Raid: Shadow Legends, I started liking cilantro. And I've {i}never{/i} liked cilantro."

    s "Can I ask you a question though, Molly?"

    if bonus == True:
        mo "Is it about Raid: Shadow Legends or your penis?"
    else:
        mo "Is it about why the sky is blue?"

    s "It’s about why you’re crying."
    mo "Oh. I’ve just never seen graphics this realistic before. "
    mo "Sometimes, I forget the heroes aren’t actual tiny people living inside of my phone that leave behind families when they die."
    s "That may be true, but boy do I have news for you."
    s "The next update coming to Raid: Shadow Legends lets you resurrect one person from your {i}real{/i} life as long as you enter the code “HOPE.”"
    mo "I could bring my mom back!"
    s "You could. I’ve already decided who {i}I’ll{/i} be resurrecting."
    mo "Is it Ami’s mo-"
    s "It’s the person I killed on the way over here for not liking Raid: Shadow Legends."
    s "I don’t want to go to jail."
    mo "Because you’re afraid you won’t survive?"
    s "No. Because I wouldn’t be able to play Raid: Shadow Legends anymore."
    mo "You’re right! That’s even worse!"
    mo "But at least Raid: Shadow Legends is easy enough to understand that you’d be able to come back after years of not playing and pick up right where you left off."
    mo "And with new characters being added every nineteen seconds, there will probably be eighty-seven-trillion by the time your sentence is over."
    s "I’m going to need more storage space on my phone..."
    mo "Just buy more phones! Because, let’s face it, are you even {i}playing{/i} Raid: Shadow Legends if you’re only using {i}one{/i} phone?"
    s "Way ahead of you, Molly. I just ordered nine more so every one of my fingers can be playing a copy of Raid: Shadow Legends at the same time."

    scene mollyraid5
    with dissolve

    mo "Wow! I wish I had that many fingers!"
    s "You {i}do{/i} have that many fingers, Molly."
    mo "Oh! Whoops! "
    mo "I guess I’ve just been playing Raid: Shadow Legends for so long that I’ve forgotten basic human concepts like the amount of fingers on a hand or how to make your lungs pump air throughout your body."
    s "But Molly-"
    mo "Yes, Sensei?"
    s "Your body is supposed to regulate breathing automatically. You shouldn’t have to focus on manually doing it."
    mo "Oh."
    mo "Well then we should probably call an ambulance because I can’t breathe at all!"
    s "Hahah! Looks like your body might like Raid: Shadow Legends a little too much as well!"

    scene mollyraid6
    with dissolve

    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"
    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"
    mo "Hahahahahahahahahah!"
    s "Hahahahahahahahaha!"

    play sound "thump.mp3"
    scene mollyraid7
    with hpunch

    "Molly falls backward on her chair due to asphyxiation and loses valuable time playing Raid: Shadow Legends, the most innovative and awesome RPG to ever exist."
    "With over nine trillion players (That’s more people than there are on Earth! Even aliens play!) Raid: Shadow Legends truly has something for everyone."
    "Play for thirteen hours every day and you’ll even see improvements in the following areas:"

    if bonus == True:
        "Sex life."
    else:
        "Height."

    "Ability to talk to old people."
    "Appreciation for the color orange."
    "Football."
    "Handball."
    "Other sports involving balls."
    "Finding sales at grocery stores."

    if bonus == True:
        "Sex Life Pt. II: Return of the Sex."
    else:
        "Height, but a second time."

    "And even resurrecting Irish transfer students who forgot how to breathe."

    s "Molly! Come back to me!"

    scene mollyraid8
    with dissolve

    mo "Hello!"
    mo "Thank you, Sir!"
    mo "I can now confirm that Heaven does not exist!"
    mo "It was nothing but pure darkness! "
    mo "I am scarred for life!"
    s "Hahahahahahaha!"
    mo "Hahahahahahaha!"

    stop music fadeout 10.0
    scene black
    with dissolve2

    "………"
    "……"
    "…"
    "{i}We now return to your regularly scheduled Molly event...{/i}"

    scene mollyraid9
    with dissolve
    play music "sweetvermouth.mp3"

    mo "Oh. Hello, Sir."
    mo "It’s nice seeing you for the first time tonight right now."
    s "Yes, neither of us have actually interacted tonight until this very moment."
    mo "And anything that took place over the last five minutes never actually happened."
    s "Exactly, Molly MacCormack."
    mo "Precisely, Sir."
    s "…"
    mo "…"
    s "Okay, well that was a fun hang out session."
    s "We should do this again sometime."
    mo "Yes. Yes we should."
    mo "Goodnight, Sir."
    s "Goodnight, Molly."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Molly and I only hang out for a few seconds before we decide to split apart for the night."
    "I walk down the stairs, sliding my phone out of my pocket as I do so."
    "And navigate to the app store-"

    stop music fadeout 5.0
    "………"
    "……"
    "…"
    play music "rapid.mp3"
    "To download Raid: Shadow Legends! Now available on all mobile platforms!"

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm15 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm20:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm:
    if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
        jump mollydorm5
    if molly_love >= 10 and mollydorm5 == True and mollycafe10 == True and mollydorm10 == False:
        jump mollydorm10
    if molly_love >= 15 and christmas7 == True and mollydorm15 == False:
        jump mollydorm15
...
```