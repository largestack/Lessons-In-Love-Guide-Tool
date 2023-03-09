# Fish Out of Water
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukadorm1&go=Go)



## Event preconditions
✅Touka love greater than or equal to 1

✅Day of week is not Thursday

✅Event "[Touka: Spontaneous Sentimentality](./toukafirsthall.md)" is completed (event=toukafirsthall)



## Next events
* [Touka: A Brief Moment in Time](./toukastreets5.md)

## Event properties
* ID: toukadorm1
* Group: Touka
* Triggered by label: toukadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label toukadorm1:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"

    "I knock on Touka’s door and wait for her to answer."
    "I’ve already made it known that I routinely drop by everyone’s rooms and, tonight, the lucky recipient of my highly demanded company is her."
    "Which is not to say I imagine she wants it or anything."
    "In fact, I’m sure a good portion of this visit will just involve her complaining about her roommate."
    "But her complaints can only last so long. And I am determined to make this room yet another home away from home for me."

    to "H...Hello?"
    to "Who goes there?"
    s "I go here. It’s me."
    to "Sensei?"
    to "If I let you inside, may I proceed to angrily vent at you in a rather unladylike manner?"

    if bonus == True:
        s "That directly depends on how much clothing you are wearing."
        to "I am wearing all of my clothes. And I greatly appreciate you asking to be sure you don’t walk in on me looking anything less than appropriate."
        s "Yes. That is exactly why I was asking. I am a good guy."
        to "You...have your moments."
    else:
        s "Yes. I am always here to help."

    play sound "lock.mp3"

    to "You may enter, Sensei. But please do not make a mess of the place. The maid just left for the night."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "...Maid?"

    "Touka unlocks the door before letting me in and I can’t help but think of how far the two of us have come in just the short time we’ve known each other."

    scene toukafirstdorm1
    with dissolve

    s "This is nice."
    s "I feel like it was just the other day you were trying to get me fired. "
    s "Now look at us, bonding in your bedroom."
    to "Please don’t steer this conversation into a strange direction or I absolutely {i}will{/i} have you fired."
    to "You are only here today because I wanted someone to complain to and have an admittedly hard time bonding with those beneath me."
    s "What happened to not placing yourself above others?"

    scene toukafirstdorm2
    with dissolve

    to "I meant the first floor, which is directly beneath this one."
    s "Typical Touka, always thinking she’s on a higher level than everyone around her."

    scene toukafirstdorm3
    with dissolve

    to "Stop it! I’m referring to the actual vertical distance between the second floor and the first!"
    to "I invited you in to get rid of my bad feelings and you’ve gone and created even more of them! Apologize!"
    s "I’m sorry, Tsukiko."

    scene toukafirstdorm4
    with dissolve

    to "Why do I bother continuing to let you talk to me when I could have you assassinated in a matter of minutes?"
    s "Wait, what?"

    scene toukafirstdorm5
    with dissolve

    to "Anyway, I’m glad you showed up when you did. I was beginning to feel rather uncomfortable."
    to "Please direct your attention to the left hand side of the room."
    s "Hold on, what was that about having me assassinated?"
    s "That's not a thing you can just ignore."
    to "I have no idea what you are talking about."
    s "That’s-"
    s "Wait, what’s happening on the left hand side of the room?"

    scene toukafirstdorm6
    stop music
    $ renpy.pause(10, hard=True)

    play music "sweetvermouth.mp3"

    s "Uhh..."
    s "What is she doing?"
    to "I have no idea. She has been sitting there ever since we got back home and will not speak a word to me."

    scene toukafirstdorm7
    with dissolve

    to "Am I going to die tonight?"
    s "Probably not."
    s "Have you two been getting along any better?"

    scene toukafirstdorm8
    with dissolve

    to "Does it look like we have been getting along any better?"
    s "It doesn’t look like you {i}haven’t{/i}."
    s "Is this what you wanted to vent about?"

    scene toukafirstdorm9
    with dissolve

    to "I suppose so. Though I will admit that it is infinitely better than hearing her whisper to her dry erase board at 3:00 in the morning."
    to "She gave up on turning the lights off too, so that is a plus."
    s "Yeah. Huge improvement, I’m sure."
    to "It will probably be best if we just pretend she is not there and carry on with the conversation topic I chose for us upon your arrival."
    s "Sure. And that topic is?"

    scene toukafirstdorm10
    with dissolve

    to "You, of course."
    s "Did you really invite me into your room so you could vent about me {i}to{/i} me?"
    to "Well I can not vent to Yasu while she is pretending to be a chair."
    s "Right. And everyone else is below you."
    to "In terms of physical verticality, yes. They are."
    s "And the rest of the girls on this floor?"

    scene toukafirstdorm11
    with dissolve

    to "I attempted to have a conversation with the green-haired girl and it...did not go very well."
    to "So I returned to my room to simply wait for the day to end so I can try again tomorrow."
    s "Unfortunately, you picked the one girl on this entire floor that just doesn’t want to talk to anyone."
    s "I’m sure it wasn’t personal."
    to "Well it certainly {i}felt{/i} personal."
    to "I have realized as of late that I am no stranger to accidentally offending people, but I didn’t know that simply saying hello was enough to warrant such unbecoming glares."
    s "Yeah, she does that. Just move on and try someone else."
    s "Even though they’re both {i}below{/i} you, Ayane and Chika don’t seem to have a problem talking to you."
    to "No, they do not. But they are also always doing things and I am never doing anything."
    to "Alas, I remain alone in a half filled room talking to my teacher because I am too fearful to show my face in the hall again."
    s "I’m sure you’ll get over it in a second when you remember you called me in here to complain about me."

    scene toukafirstdorm12
    with dissolve

    to "Oh, right! Thank you kindly for reminding me!"
    to "You are a bad man!"
    s "You’re welcome and I know."
    s "What did I do this time?"
    to "Knowingly invited me to live in a room with a crazy person!"
    s "You’re still going on about that? Whatever happened to bonding over horses and dead people?"
    to "I showed Yasu a picture of my favorite horse when we returned to the dorm that night and she proceeded to maniacally laugh for five whole minutes!"
    to "I still do not understand why!"
    s "Maybe it was a funny looking horse?"
    to "It’s a beautiful black Misaki and cost my family an absolute fortune!"

    if brony == True:
        if bonus == True:
            s "Damn. That's not even the kind that I'd want to have sex with."
            to "What?!"
            s "Nothing."
        else:
            s "Hot."
            to "What?!"
            s "Nothing."

    s "I have no idea what that means but, I’m sure it was funny looking if it made Yasu laugh for five minutes."

    scene toukafirstdorm13
    with dissolve

    to "Sensei...You probably do not understand this as you don’t sleep in the same room as her, but Yasu is very much not a run of the mill commoner."
    s "You really don’t have to live with her to figure that out."
    to "Then why would you subject {i}me{/i}, of all people, to the brutal test of willpower that is befriending her?"
    s "If you don’t like it, why not just go stay in the spare house your parents bought you when you transferred[school]s?"

    scene toukafirstdorm14
    with dissolve

    to "Because...sleeping in a house alone is scary..."
    s "Oh, right. You’ve been coddled forever, so of course you wouldn’t be used to something like that."

    scene toukafirstdorm15
    with dissolve

    to "Can you stop implying that all of these flaws of mine are the result of selfishness or conceit and instead acknowledge that I might just be genuinely confused?"
    to "I am a fish out of water here and expect special treatment {i}not{/i} because I see myself as a superior being, but because I {i}need{/i} it."
    to "So yes, I apologize dearly, but I am very mad at you as the man who is now at least partially responsible for the woman I will ultimately become one day."

    if bonus == True:
        "Unfortunately for Touka, that day will never come."
        "But I suppose that I have been a little harsh to her ever since she arrived when she clearly {i}is{/i} trying."

    s "Fine, yeah. I get it. You’re abnormal."
    s "But if you’re going to vent in an “unladylike manner” like you said before, you should avoid saying things like “I apologize dearly” and just really lay into me."

    scene toukafirstdorm16
    with dissolve

    to "Lay into you?"
    to "As in...threaten your job and your well being as I’ve been doing in[school]?"
    s "No. Like say actual mean things to me about the kind of person you think I am."

    scene toukafirstdorm17
    with dissolve

    if bonus == True:
        to "Wait...you are not some sort of...masochist, are you?"
        to "Do you enjoy when powerful women say mean things to you? My mother has told me about those types of men before."
        to "I don’t think I’m comfortable-"
        s "First off, I’m not a masochist."
        s "Second, what could have possibly compelled your mother to tell you about things like that?"

        scene toukafirstdorm18
        with dissolve

        to "It was part of a twelve hour briefing I was given on things I may encounter in what my father referred to as “the wilderness.”"
        to "According to my mother and the presentation the family put together, there are these things called “fetishes” that somehow provide pleasure to...certain types of people."
        to "Could it be that...this whole time...you’ve been provoking me for your own satisfaction?"
        s "I..."
        s "I don’t think so, but...you know, at this point, I wouldn’t be surprised if there was some element of truth to that."

        scene toukafirstdorm19
        with dissolve

        to "This causes a great deal of stress for me as I will no longer be able to belittle you without the fear of you becoming...excited."
        to "I find myself belittling you quite often, so please suppress your desires until after we are married."

        scene toukafirstdorm20
        with dissolve

        to "N-Not that I would ever consider marrying a masochistic commoner like you!"
        s "Careful, Touka. Yelling at me like that might have some...adverse effects."
    else:
        s "I probably deserve it anyway."
        s "I am a bad man."
        to "What have you done now?"
        s "I stole a piece of Ami's gum while she was asleep this morning."
        to "Sensei, how could you?"
        s "I am a bad, bad boy."
        to "I do not know what to say."
        s "You can show me the rest of the room. Just hide any gum first if you know what is good for you."

    scene toukafirstdorm21
    with dissolve

    to "Oh...right."
    to "Apologies..."
    to "I...umm..."
    to "Please follow me for the rest of the tour."

    scene black
    with dissolve

    "Touka somehow switches into tour guide mode, probably being desperate for a topic change and realizing that she hasn’t shown me around since I entered."
    "Not like there’s much to show me anyway, but-"

    scene toukafirstdorm22
    with dissolve

    s "Wait, hold on. Why do you have a love hotel bed?"

    scene toukafirstdorm23
    with dissolve

    to "What is a love hotel?! It sounds romantic!"
    s "It’s a hotel made for the express purpose of having sex."
    s "This is the exact type of bed they use."
    to "..."

    scene toukafirstdorm24
    with dissolve

    to "You are lying to get a rise out of me again, aren’t you?"
    to "This is the same type of bed I have been using since I was little."
    to "My mother would never knowingly allow me to sleep in something that...filthy!"
    s "Knowingly, no. But your mother hasn’t seemed to be the most...worldly person so far either."
    to "Nonsense, she is fluent in seven languages. That is plenty worldly."
    to "This is just one more trick out of the many you’ve had the pleasure of playing on me thus far."
    s "Does the bed ever vibrate?"

    scene toukafirstdorm25
    with dissolve

    to "Yes, but...that just means it is set to...sleep mode."
    s "Touka, it’s a bed. It is literally always in sleep mode."

    if bonus == True:
        s "The vibrating is for sex stuff."
    else:
        s "The vibrating is for other stuff."

    scene toukafirstdorm26
    with dissolve

    to "No, it is not! I’m not falling for that! It is a high quality, imported bed with...rapid sleep mode technology!"
    s "There’s a rapid sleep mode now?"
    to "For when sleeping just isn’t fast enough!"

    scene toukafirstdorm27
    with dissolve

    to "You wouldn’t know because you can’t afford one."

    if bonus == True:
        s "Sure I can. In fact, for just 3,000 yen, I can rent one downtown and-"
    else:
        s "That was a low blow, you big jerk."

    scene toukafirstdorm28
    with dissolve

    to "Yasu! Are you done being a chair yet?! I am cornered by an intimidating man and require your assistance!"
    s "How is Yasu going to help? She has the constitution of a decrepit old woman."
    to "Mother?! Yumi?!"
    s "{i}Yumi?{/i}"

    scene toukafirstdorm29
    with dissolve

    to "I ran out of people I rely on and inadvertently began to list people I find intimidating."
    to "If you hadn’t stopped me, I would have likely called out for your assistance next."
    s "Wait, does that mean you find Yumi more intimidating than me?"

    scene toukafirstdorm30
    with dissolve

    to "Yumi has not sworn to protect me and guide me through life while you have. She is clearly more intimidating to me than you are."
    s "If you think {i}she’s{/i} intimidating, you should see her mother."
    to "Will she be attending the next parent teacher conference?"
    s "I don't really do those. And even if I did, no. She would definitely not be there."

    scene toukafirstdorm31
    with dissolve

    to "If you do not hold parent teacher conferences, how are my mother and I to know if my performance is adequate or not?"
    s "What performance? All you do in class is sit around."
    to "That isn’t true. Your assistant actually just gave me a batch of personalized worksheets meant to help with my studies as your methods have not...clicked for me just yet."
    s "Makoto did that?"
    to "Yes, Makoto. That was her name."
    to "I was under the assumption it was a thing she did for everyone, what with being your assistant and all."
    s "I honestly had no idea."
    to "Well...regardless, how will you be informing my mother and myself of my progress?"
    to "Do we need to arrange for a personal meeting or something of that nature?"
    s "How about I just...send you an email with a thumbs up or something?"

    scene toukafirstdorm32
    with dissolve

    to "An...email?..."
    to "That’s hardly sufficient, Sensei..."
    to "Your methods sound less and less rational every time you speak about them."
    s "Yeah, well...you sleep in a love hotel bed, so there’s not a lot about you that screams “rational” either."

    scene toukafirstdorm28
    with hpunch

    to "FOR THE LAST TIME, IT’S A NORMAL BED! AND IT’S VERY COMFORTABLE!"

    if kirin_virgin == False and bonus == True:
        s "Just don’t let Kirin see it or she might get a little excited."
        to "I CAN’T EVEN REMEMBER WHICH GIRL THAT IS! THERE ARE SO MANY OF THEM!"
        s "If you want, I can go see if she can come over here to confirm-"

    elif kirin_virgin == True and bonus == True:
        s "Is it? Maybe I’ll scrounge up a spare 3,000 yen and go check one out after-"

    else:
        s "Yeah, it looks it."

    to "OH, WOULD YOU LOOK AT THE TIME? I HAVE A...ZOOM CALL WITH MY CROCHET INSTRUCTOR, SO IT IS TIME FOR YOU TO LEAVE!"
    ya "Crochet? Can I try, Touka?"

    scene toukafirstdorm33
    with dissolve

    to "Oh, Yasu! How nice of you to finally join the conversation! Did you enjoy being a chair?!"
    ya "I felt God’s hands on my shoulders. They were so light and-"
    to "Wonderful! Let us crochet together, then!"
    to "Goodnight, Sensei!"

    scene black
    with dissolve2

    "Touka quickly pushes me out of the room...and is surprisingly quite strong."
    "Of course, I don’t bother fighting back because A: she is a girl. And B: she is a girl."
    "So I accept defeat for the time being, having just satiated my lust for awkward rich girl content, and begin my walk home through a suddenly heavy snowfall."
    "Or, at least I start my walk home."
    "Touka wound up sending a driver to pick me up just two or three blocks along."
    "I have no idea why she did that or how it managed to get here so quickly, but I accept the ride and find myself back at home within a matter of minutes."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm1 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukafirsthall:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label toukadorm:
    if touka_love >= 1 and day != 4 and toukafirsthall == True and toukadorm1 == False:
        jump toukadorm1
...
```