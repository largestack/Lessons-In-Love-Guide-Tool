# Under the World Tree (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 35

* Event [Lesbian Stuff](./day333part2.md) (Main) is completed)



## Next events

* [Ayane: Crash of Thunder](./ayanedorm35.md)

## Event properties

* Id: dojo35
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo
* Triggered by path: dojo->dojo35

## Official wiki page

[Under the World Tree](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dojo35&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label dojo35:
    scene ayanedojothreefive1
    with dissolve
    play music "sakuya4.mp3"

    "I make my way through a crowd of girls practicing roundhouse kicks or something."
    "Actually, I can't even tell what kind of kick it is."
    "I feel like I should probably pay more attention in this class if I’m going to start calling moves and techniques by their proper names."
    "Anyway-"
    "I make my way through a crowd of girls doing indiscernible karate kick things and find Ayane pressed up against a wall in the back half of the dojo."
    "The sun must be feeling particularly feisty today as it leaps in through the window and reminds us that, even in winter, it is a giant, vicious ball of fire."

    ay "So...you came after all..."

    "Wind blows in through the window and misses Ayane’s hair by an inch or two."
    "I decide to mention it anyway, though, because I feel like I’m going to have to set the stage for what I imagine will be another roleplaying session."

    os "Amamiya! Are you doing anything today or are you just going to sit there?!"
    ay "Do you know what day today is, Sensei?"

    if day == 6:
        s "Saturday."
        ay "Not just Saturday."
        ay "It’s the anniversary of our fated first encounter under the world tree."
    else:
        s "Sunday."
        ay "Not just Sunday."
        ay "It’s the anniversary of our fated first encounter under the world tree."

    s "There’s a world tree now?"

    scene ayanedojothreefive2
    with dissolve

    ay "Oh, right...you lost your memories after retreating to the mountains and overworking yourself to the point of amnesia."

    "No, I was just reincarnated."
    "Probably."

    ay "But that’s fine...I’m already shouldering some of the world’s greatest secrets."
    ay "One more will not do me in."

    scene ayanedojothreefive3
    with dissolve

    ay "Just know...this is an important day for both of us."
    ay "And the fact that I must live through it each and every year on my own is tearing me up inside."
    s "Are you crying?"
    ay "Yes, but only in character. I’m fine otherwise."
    s "You’re a surprisingly good actress."

    scene ayanedojothreefive4
    with dissolve

    ay "Thank you!"
    ay "Ami and I used to have fake battles in her bedroom while you were out doing Sensei stuff, so I got a lot of practice in then."

    scene ayanedojothreefive5
    with dissolve

    os "At least give me a fucking answer, come on!"
    os "What happened to the two of you who were fighting to keep this place open?"
    os "Was it really all so you could just sit around and stare at each other all day?"
    ay "Sitting around and staring at Sensei is far more important to me than karate lessons."
    ay "Besides, I’m not feeling well today."

    scene ayanedojothreefive6
    with fade

    os "Again?"
    os "This is like the third weekend in a row."
    ay "On the bright side, I still showed up to see your beautiful face!"
    os "Flattery won’t earn you a belt, Ayane."
    os "If you want to get serious about this like you said, you’re going to have to actually start putting in the time."
    ay "I know, I know. And I will soon, I promise."
    os "Also, what the hell is with that posture? At least sit up straight if you’re going to be taking {i}another{/i} day off."

    scene ayanedojothreefive7
    with dissolve

    ay "No can do, Sensei...I have to sit this way or I won’t look cool. It’s half the reason my monologue succeeded."
    s "I know Osako is the instructor, but please don’t call her “Sensei.” It is needlessly confusing for me."

    scene ayanedojothreefive8
    with dissolve

    os "Are {i}you{/i} the reason she’s sitting out over and over again? Because I have no problem kicking you out of here for doing...literally nothing at any point ever."
    s "I’ll take you on right now, Osako."

    if bonus == True:
        s "I have to fight naked, though. It’s part of Arakawa family tradition."
        ay "Ahh yes, {i}crouching sausage style.{/i} One I’m all too familiar with."

    scene ayanedojothreefive9
    with dissolve

    if bonus == True:
        os "Yeah...I bet you are."
        ay "Hahah...hah..."
    else:
        os "I would rather fight Ayane. She is smaller than me and I want to see how many bones of hers I can break."
        ay "I must become stronger."

    s "Ayane will start practicing again next session. Just take it easy on her today."
    s "She’s still getting over how I lost my memory when I went into the mountains to-"

    scene ayanedojothreefive10
    with dissolve

    os "Leave and never come back."
    s "I’m sorry, who are you again? I lost my memory and can’t seem to remember your-"
    os "I’m the woman who is going to end your life."
    s "At least give your girlfriend that sweet release first. She’s been asking for it ever since I met her."

    scene ayanedojothreefive11
    with dissolve

    os "Wha- Never mention Wakana and “sweet release” in the same sentence again or I really {i}will{/i} end your life!"

    if bonus == True:
        s "Don’t worry. I only fantasize about you two on occasion. It doesn’t happen every night."
        os "Don’t fantasize about us ever!"
        s "I can’t help it. That’s just the way I am, unfortunately."
    else:
        s "I apologize for offending you. I did not mean it."

    scene ayanedojothreefive12
    with dissolve

    os "Whatever. Just don’t be expecting another invite out anytime soon."
    s "But we had so much fun."
    os "Fuck off. Goodbye."

    scene ayanedojothreefive13
    with dissolve

    "Osako storms off and-"

    ay "Did you go out with our karate instructor recently?"

    "And Ayane wastes no time getting to the interrogation that was sure to spring up as a result of that."

    s "It was just a spur of the moment thing."
    s "She and Wakana were leaving[school] together and they invited Maya and me to come get coffee with them."

    scene ayanedojothreefive14
    with dissolve

    ay "Maya was there too? But wouldn’t that make it kind of like a...double date?"
    s "With anyone other than Maya, sure. She only came because she was hungry."

    scene ayanedojothreefive15
    with dissolve

    ay "Well...okay. That does check out."
    ay "She’s kind of an abyss when it comes to food."
    s "That aside, though...what’s going on with you?"

    scene ayanedojothreefive16
    with dissolve

    ay "With me? What do you mean?"
    ay "Didn’t I already tell you that I’m grieving over having to spend our anniversary alone?"
    s "Were you grieving the apparent last several times you’ve sat out training as well?"
    ay "I’ve just been tired."
    s "That’s been happening a lot lately, though."
    s "You didn’t show up to the end of the dorm war. And you passed out extremely early the last time you slept over my place with Ami."

    scene ayanedojothreefive17
    with dissolve

    ay "What are you getting at, exactly?"
    s "I just want to know if everything is okay."
    ay "You’re worried about me?"
    s "I mean, I didn’t want to come out and say it. But yeah. Of course."
    s "One or two times would be fine. In fact, it {i}was{/i} fine. But this whole karate thing on top of that is just a pretty big red flag for me to think something’s actually going on."

    scene ayanedojothreefive18
    with dissolve

    ay "Well...thank you for your concern. But I haven’t really figured out a good way to talk about it yet."
    ay "You already know that I’m pretty bad when it comes to stuff like this, so I guess I’ve just been coasting on secret girl powers to get by."
    s "Secret...what now?"

    scene ayanedojothreefive19
    with dissolve

    ay "A hidden technique every girl is born with!"
    ay "The option to get out of stuff by blaming it on not feeling well!"
    ay "Want to get out of gym class? Say you’re on your period! Don’t want to go hang out with your friends? Period again!"

    if bonus == True:
        "My mind immediately jumps to the several times girls have dodged having sex with me for reasons related to that and I suddenly lose trust in everyone."
        "Nowhere is safe anymore."

    s "That’s evil."

    scene ayanedojothreefive20
    with dissolve

    ay "It’s not evil. It’s just a way for us to take advantage of our cuteness and gain some kind of benefit in the process."
    s "Yeah, well, I’m pretty sure people are going to catch on if you’ve been blaming your lack of participation on your period for several months straight."

    scene ayanedojothreefive21
    with dissolve

    ay "Uhh...well, all I said is that I wasn’t feeling well. So it was kind of a gray area."
    ay "But you’re right. I should stop trying to get the world to revolve around me and only take advantage of secret girl powers once a week at most."
    s "You know, that wasn’t really the lesson I was trying to teach you, but I’m glad that you at least got something out of it."

    scene ayanedojothreefive20
    with dissolve

    ay "Since I can’t turn back on using my power today, though, does this mean you’ll hang out with me and protect me if Osako tries to roundhouse kick my head off?"

    "A-ha. So it {i}was{/i} called a roundhouse kick."

    s "Sure."
    s "I’m pretty sure everyone in the dojo already assumes that you and I are-"
    ay "In love?"

    if bonus == True:
        s "In{i}volved{/i}."
    else:
        s "No. That we are friends."

    ay "Call it love. I want to hear you say you love me."
    s "Why?"
    ay "Because you barely ever say “love” and I could really use the pick me up right about now."
    s "…"
    ay "…"
    ay "I can wait all day. I hope you know this."
    s "Fine. Whatever. I love you."

    scene ayanedojothreefive22
    with dissolve

    ay "Heheh~! I love you too!"
    ay "Now come sit next to me and let me rest my head on you so I don’t have to hold this weird sitting pose thingy anymore."

    scene black
    with dissolve

    "Ayane straightens herself out and slides over a few inches so that she’s not in direct sunlight anymore."
    "I take my place beside her and, before I can even open my mouth, she cuddles up against me in complete disregard for the stigma surrounding public displays of affection."

    scene ayanedojothreefive23
    with dissolve

    if bonus == True:
        ay "Hello, sir. Could I interest you in a horny blonde girl who wants to jerk you off in the bathroom right now?"
        s "What happened to not feeling well?"
        ay "Teacher time is the cure for everything."
        s "For the last time-"

        scene ayanedojothreefive24
        with dissolve

        ay "I’m kidding."
        ay "Well, mostly."
        ay "To be honest, I’d be okay with doing anything with you whenever you want. Wherever you want."
        ay "But right now isn’t the time."
        ay "Unless you want it to be, I mean."
        s "…"
        ay "…"
        ay "Cause if you want it to be-"
        s "I’m fine right now, Ayane."
        s "Osako is already keeping an eye on us. I’m pretty sure if we both went to the bathroom at the same time, she’d understand exactly what’s going on."
        ay "True, but I already told you I saw her making out with Ms. Watabe once. So maybe we could make it one of those “eye for an eye” thingies?"
        s "You seem pretty desperate right now."
        ay "Hormones are evil."
        ay "As soon as we touched heads, I started thinking about kissing. And then kissing made me think about touching. And then touching led to sex. And then sex led to more kissing."
        ay "Now I’m going round and round and round and round and I’m going to have to change my underwear soon."

    s "…"
    ay "…"
    s "…"
    ay "…"

    scene ayanedojothreefive25
    with dissolve

    ay "What can I do to make you want me more?"
    s "What do you mean exactly?"
    ay "I mean that...pretty soon I..."
    ay "I might want a lot more attention than I’m currently getting."
    ay "So I’m...looking for tips, I guess."

    if bonus == True:
        s "And I’m assuming that’s why you jumped straight to the horny talk?"

        scene ayanedojothreefive26
        with dissolve

        ay "Oh, no. That was just me making casual conversation."
        ay "If sex drive was all it took to convince you to be with me more, we’d be on our honeymoon in Hawaii right now."
        ay "I don't know if you've realized this, but I love your penis almost as much as I love you."
        s "I can’t just give you tips on how to steal my attention away from the others, Ayane. It doesn’t really work that way."
        ay "I know, but...let’s pretend it {i}does{/i} work that way for a second."
        ay "You’re in a room with all twenty of us and you can only choose one to spend the rest of forever with."
        s "This hypothetical situation is already flawed because Yumi would not show up for that."
        ay "Okay, so you’re in a room with nineteen of us and Yumi isn’t there."
        s "Io probably wouldn’t show up either."
        ay "So there are eighteen girls in the room and-"
        s "And if Io wasn’t there, Uta would probably be out looking for her and-"

        scene ayanedojothreefive27
        with dissolve

        ay "Can I just finish, please?"
        s "Sorry, go ahead."
        ay "If you were in a room with...pretty much every girl you know and had to choose only one of them..."
        ay "Is there anything I could do to stand out a little more?"
        s "You’re not going to just ask me who I would pick?"
        ay "Of course not. I’m afraid of what I’d hear."
        ay "I know you love me...and {i}everyone{/i} knows I love you..but I feel like there might still be more I can do to show it or..."
        s "You do more than enough."
        s "Don’t even waste your time thinking about that. There’s no point to it."
        ay "There kind of is, though..."
        ay "Like...I get that some of the other girls might {i}want{/i} you, but..."
        s "But you {i}need{/i} me?"

        scene ayanedojothreefive28
        with dissolve

        ay "Yeah."
        ay "Pretty...{i}pretty{/i} badly..."
        s "Don’t you think you should be giving yourself a little more credit?"
        s "You’re independent and smart and...can do basically anything you set your mind to."
        ay "This isn’t about {i}me{/i}."
        s "Well, if it’s about me-"

    scene ayanedojothreefive29
    with dissolve

    ay "A-Actually! Let’s just change the topic completely."

    if bonus == True:
        ay "This isn’t really the best place to get all serious and...and I think things were going in a weird direction anyway."
        ay "This is...exactly why I don’t really like talking about this kind of stuff unless I have to..."
        s "…"
        ay "…"
        s "…"
        ay "Soooooo...could I interest you in a horny blonde girl who wants to jerk you off in the bathroom right now?"
        s "You already used that line."

        scene ayanedojothreefive30
        with dissolve

        ay "And you’ve already used {i}me{/i}, but it hasn’t made you any less “excited” whenever we do it."
        ay "Some stuff is made to be reused, Sensei."
        ay "Just look at your clothes. You wear the same thing every day and I don’t love you any less for it."
        s "I have two completely different outfits, thank you very much."

        scene ayanedojothreefive31
        with dissolve

        ay "And they’re both adorable!"
        ay "But if we’re not going to complain about reusing our clothes or our bodies, don’t you think it’d be okay to reuse some lines?"
        ay "Like, if that wasn’t the case, we would have only been able to exchange “I love you’s” one time and that would not be nearly enough for my gigantic, Sensei shaped heart."
        s "If there is anything even remotely resembling me inside of you, we should rush you to the hospital immediately. That is entirely abnormal and you require immediate surgery."
        ay "Nope! It being shaped that way lets me fit more of you inside of me than it would normally and-"

        scene ayanedojothreefive32
        with dissolve

        ay "Heh."
        ay "{i}Fit more of you inside of me.{/i}"
        ay "I wasn’t even trying to make that one dirty. It just happened on its own."
        s "…"
        ay "…"
        s "You have a problem."
        ay "I do."
        ay "A big Sensei shaped problem."
        ay "But I wouldn’t trade it for the world."
    else:
        s "I would like to talk about the destruction of the Amazon rainforest and how horrible it is."
        ay "Yes. That is precisely what I wanted to talk about as well."

    scene black
    with dissolve2

    "The rest of the afternoon proceeds normally."
    "There are no more immediate or sudden tonal jumps in conversation and Ayane and I manage to make it through yet another lesson without exerting any energy whatsoever."
    "However-"

    stop music

    "I couldn’t shake the idea of there being something looming in the background."

    if bonus == False:
        "I must save the Amazon rainforest."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo35 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label ayanespecial1:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
    if ayane_love >= 10 and ayanenew1 == True and ayanenew2 == False:
        jump ayanenew2
    if ayane_love >= 20 and ayanedorm15 == True and dojo20 == False:
        jump dojo20
    if ayane_love >= 25 and halloween14 == True and ayanedorm20 == True and dojo25 == False:
        jump dojo25
    if ayane_love >= 30 and ayanedorm25 == True and dojo30 == False:
        jump dojo30
    if ayane_love >= 35 and day333part2 == True and dojo35 == False:
        jump dojo35
...
```