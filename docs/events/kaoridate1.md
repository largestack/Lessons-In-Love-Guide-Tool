# How to Date a Human (Kaori)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kaori love greater than or equal to 0

* kaorinumber equal to True (unknown variable)



## Next events

* [Main: The Value of Sharing](./halloween1.md)
* [Kaori: The Best Ways to Rub a Cock](./kaoridate5.md)

## Event properties

* Id: kaoridate1
* Group: Kaori
* Triggered by label: callkaorimorning
* Triggered by branch label: callkaorimorning
* Triggered by path: callkaorimorning->kaoridate1

## Official wiki page

[How to Date a Human](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kaoridate1&go=Go) for more details.

## Event code

File: (install folder)\game\KaoriEvents.rpy

Code:
```python
...
label kaoridate1:
    s "I wonder what Kaori is up to right now..."

    "I haven’t tried contacting Kaori ever since I got her phone number the other day, so
    I figure now is as good a time as any to get that ball rolling."
    "How that ball will end up when rolling in the direction of someone as...eccentric as her, I have no idea. But it’s at least worth a kick or two."

    play sound "phonebeep.wav"

    "I tap on Kaori’s name in my phone and wait for her to answer."
    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    k "Goodbye."
    s "Wait, what?"
    k "Did I make a mistake?"

    play music "lifeismostlygood.mp3"

    s "Yes, Kaori. That isn’t how you answer the phone."
    k "Apologies. I think I meant to say hello."
    k "This is the Hamburger Man, yes?"
    s "Correct. Do you not have me saved in your contacts or something?"
    k "There are no names in my contact list. Only the colors I expect people to like the most."
    s "You...saved my name as a color?"
    k "Yes."
    s "Well, what-"
    k "Actually no."
    k "For you, I wrote “clear.”"
    s "Clear isn’t a color..."
    k "I know."
    s "Okay, well-"
    k "What are you currently participating in, Hamburger Man?"
    s "Me? Nothing. I called because I was wondering if-"
    k "Let us go on what humans call a “date!”"

    "Woah, already?"
    "Kaori moves quick."

    s "Uhh, are you sure you’re okay with that? I kind of figured you’d want to at least talk more before-"
    k "Come to this address."

    play sound "phonebeep.wav"

    "I immediately receive a text from Kaori with nothing but numbers."

    s "Uh...Kaori?"
    k "Hamburger Man."
    s "I need the name of the street too."
    k "Do humans give names to streets the same way they award them to children for being born?"
    s "Kind of? Yeah. It's the name on the-"
    k "I remember now! Prepare for the beep!"

    play sound "phonebeep.wav"

    "The beep happens, I guess."
    "And, in other news, I have a full address now."

    k "Why is your body not in the same place as mine yet?"
    s "Probably because I can't teleport."
    k "That makes sense!"

    "I take another look at the address she texted me and realize that it isn’t too far from here."
    "I recognize the street name, but I’m not sure where I’ve seen it before."

    s "I'll head over in a few minutes, I just need to get dressed and-"
    k "I understand!"
    k "Hello!"

    play sound "phonebeep.wav"

    "…"
    "Aaaand, she’s gone."

    scene black
    with dissolve2

    "Shrugging off Kaori’s interesting end to our conversation, I get myself together and begin to head over to the address she sent me."
    "As soon as I set foot outside, I accept that there is absolutely no way this is a real date."
    "Even knowing that, though, I can't help but be a little intrigued by the prospect of getting to see what makes Kaori tick."
    "Here's hoping that she's a bit more...grounded today."
    "………"
    "……"
    "…"

    scene kaorifirstdate0
    with dissolve2

    s "So that's why the address looked familiar..."

    "I don't know why I even expected something else in the first place."
    "I stand in the lobby, waiting for Kaori to show up and explain why we’re here on her day off."
    "Or at least what I {i}hope{/i} is her day off."
    "A few customers busy eating their breakfast stare at me and make me feel slightly uncomfortable...but my “date” shows up seconds later to either quell that or make it ten times worse."

    scene kaorifirstdate1
    with dissolve

    k "You came!"
    s "I came. It would have been rude for me to tell you I’m coming and then just...not show up."
    k "Yes! That would have been a very bad thing!"
    k "But you are here! And now the human date can begin!"
    s "Just “date,” Kaori..."

    scene kaorifirstdate2
    with dissolve

    k "This language perplexes me."
    s "The trick is to just not add “human” before every single object."

    scene kaorifirstdate3
    with dissolve

    k "What does it mean to be “human?”"

    "Oh no. She’s turning into Maya."

    s "Let’s not worry about that for now. Would you mind explaining why we’re hanging out at the diner on your day off?"
    s "I figured you’d want to go somewhere else since you’re probably cooped up in here for an indeterminate amount of hours each week."
    k "Day off? What is this “day off” you speak of?"

    "Yup. Saw that coming."

    s "It...means a day that you’re not working."
    k "But I am working. That is why we’re at the diner."
    s "Kaori, why would you invite me here while you're working?"
    k "Is this not how a regular {i}date{/i} works?"
    s "Nope. A “date” is what you call it when two people who are romantically interested in one another go do stuff together."
    k "Oooooh...I see."

    scene kaorifirstdate4
    with dissolve

    k "Wait, what?!"
    k "What is this romantic interest you speak of?!"
    k "To think that I would make such a mistake in the heat of human mating season!"
    c1 "You can do it, Kaori!"
    c2 "We believe in you!"
    k "What are we supposed to do now?!"
    s "Relax. I kind of expected this was a misunderstanding."

    if kaoriprepared == True and bonus == True:
        k "Has the...time finally come to prepare my body?..."
        s "Kaori, why do you remember that? It was such a small part of that meeting."
        s "Besides, Rin would kill me if we were to do that while she's not here."
        k "How many humans must be present for the mating ritual to be successful?..."
        s "Just two. But there will be no mating ritual today."

    scene kaorifirstdate5
    with dissolve

    k "Okay...I will trust you, Hamburger Man."
    k "But only because you are one of the few people in this city that I know by name."
    s "But you don't-"

    scene kaorifirstdate6
    with dissolve

    k "Hamburger Man, would you like to consume hot meat with me for the breaking of my lunch?"
    s "Uhh...sure. Are you really going to take your lunch break this early, though? It’s not even 10:00 AM yet."

    scene kaorifirstdate7
    with dissolve

    k "You traversed many miles of harsh terrain in order to reach me and all {i}I{/i} did was misunderstand the meaning of the word “date.”"
    k "Now you must return home without having mated and it is all my fault."
    s "It wasn't even a two mile walk and I made like one turn. I will accept your apology for the mating thing, though."
    k "I will take my break early to spend time with the Hamburger Man. It is how I will correct my error."
    s "You really don't have to-"
    k "Please give me 300 seconds to tell the computer that I am hungry."

    "..."

    s "Sure. Go tell the computer, Kaori. I'll wait here."
    k "Thank you. I will return with slightly more freedom than I have right now."

    scene kaorifirstdate0
    with dissolve

    "Kaori disappears into the back room, leaving me once again uncomfortable and the center of attention."

    scene black
    with dissolve

    "I avert the gazes of various customers and take a seat at the closest booth, waiting for the Mistress of the Dark or whatever it is she calls herself to come back..."
    "………"
    "……"
    "…"

    scene kaorifirstdate8
    with dissolve

    "Kaori places a, you guessed it, hamburger in front of me and takes a seat on the opposite side of the table."
    "Honestly, if given the chance, I would have much preferred ordering something else this morning."
    "I love hamburgers, don’t get me wrong, but I love them significantly more when it isn’t 10:00 AM and I’m still trying to wake up."

    k "I am very glad that we are currently engaged in a real human date, Hamburger Man."
    s "Kaori, I already told you this isn't a real date. Please try to remember the meanings of things from now on as it will save both of us a great deal of time."

    scene kaorifirstdate9
    with dissolve

    k "But these customs and meanings are so hard to keep track of! I am just a girl with a spider tattoo and extra colors in my eyes, not a dictionary!"
    s "Wait, are those actually your real eyes?"

    scene kaorifirstdate10
    with dissolve

    k "Of course. Where would I procure fake ones?"
    s "I...have no idea. I was just under the impression those were colored contacts or something."
    k "Aren't contacts the names of the colors in your telephone?"
    s "Kaori, what planet were you born on?"

    scene kaorifirstdate11
    with dissolve

    k "I believe they told me it was some place called...Gunma?"
    s "Wait, who are {i}they?{/i}"
    s "Also, there's no way that's true. Gunma is in Japan."

    scene kaorifirstdate12
    with dissolve

    k "Hamburger Man! Don’t tell me you have forgotten where we are?"
    k "Do you require medical assistance? I am trained in CPR. Can you breathe? How many colors are there in the rainbow?"
    s "I don’t require medical assistance, Kaori. I just don’t understand how you’re still coming to terms with normal human behavior if you were born in Japan."
    s "It might sound crazy, but I was starting to think you were some sort of...alien or robot or something."

    scene kaorifirstdate13
    with dissolve

    k "That sounds very crazy. You are a crazy person. I am suddenly the normal person here."
    s "I still think I have a bit of an edge, all things considered."

    scene kaorifirstdate14
    with dissolve

    k "Wrong. You still have much to learn from me, grass-bug."
    s "It’s “grasshopper.”"
    k "I make the rules here, grass-bug. Not you."
    s "I’m actually kind of getting used to Hamburger Man, so if we can stick with that instead of grass-bug, it would be much appreciated."

    scene kaorifirstdate15
    with dissolve

    k "Good! Hamburger Man is a good name. And very fitting for someone who likes hot meat as much as yourself."
    k "However!"
    s "However what?"
    k "I like the new name too! So I hereby pronounce you..."
    k "Hamburger-bug!"
    s "Okay, that’s the worst nickname so far. Please don’t ever call me that again."
    k "Are we going to go on more “dates” in the future? Or do we need to “hang the outs” first? That is a term I learned recently!"
    s "Either you have the worst teacher in the world or you are gravely misremembering it."
    k "Please explain the process we must go through to become closer, Hamburger-bug Man! I must learn more things!"
    s "You know, I'm just going to go ahead and assume you {i}are{/i} romantically interested in me if you keep calling this a date."

    scene kaorifirstdate16
    with dissolve

    k "No! I am simply curious!"
    k "You have many interesting words and stories to share!"

    scene kaorifirstdate17
    with dissolve

    k "I do not have many colors in my phone..."
    k "Sometimes, when I think I’ve made what you would call a {i}friend...{/i}the friend just disappears."
    k "They all keep going away and I don’t understand why."
    k "What am I doing wrong, Hamburger-bug-burger-man-bug?"
    s "..."
    s "Kaori, can I ask you something? And don’t take this the wrong way."

    scene kaorifirstdate18
    with dissolve

    k "I will do my best."
    s "Do you...really talk like that on purpose? Or is it just a sort of...self-defense mechanism or something?"
    s "Like, you’re only talking that way because you want to stand out or seem unique in someone else’s eyes."
    s "Because if it’s anything like that, I want you to know that-"
    k "Talk like what? I don't understand."
    k "Is this about adding “human” to words again?"
    s "Uhh, well yeah. That’s...definitely part of it."
    k "What are the other parts? "
    k "I lack the type of education that you provide when you aren’t trafficking humans, but I am trying my best to learn."
    s "First off, please stop saying I’m a human trafficker."
    s "Second, the way you talk now is perfectly fine as long as you’re not intentionally trying to sound weird."
    s "Learning a language is tough. And I’m not sure how you got to the point you’re at now, but I’m glad to see you’re trying to get better."
    s "Just...keep practicing or something. A lot."

    scene kaorifirstdate19
    with dissolve

    k "Thank you Hamburger-bug! I really appreciate it."
    s "Please stop calling me that."
    k "I understand!"
    k "Since you have been a good person to me, I will give you a new name instead!"
    s "What is it this time? Grassburger? Hamhopper?"
    k "No! It is better!"
    k "You are now..."

    scene kaorifirstdate20
    with dissolve

    k "Friend!"

    scene black
    with dissolve2

    "Kaori and I talk for another twenty minutes before her break ends and she has to get back to work."
    "Not wanting to disturb her anymore, I pay the bill and take my leave."
    "Somehow, and I really don’t understand it- but I feel like I learned a lot about Kaori today."
    "That feeling drifts away the second I realize I could have probably talked her into giving me a discount, though."
    "Either way, I consider today's meeting a good first step in what I can now confirm is some sort of...friendship."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate1 = True
    stop music fadeout 5.0

    "{i}Kaori’s affection has increased to [kaori_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label kaoridate5:
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
...
```