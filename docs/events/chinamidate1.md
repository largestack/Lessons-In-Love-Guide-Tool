# 5,000 Year-Old Wizard (Chinami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chinami love greater than or equal to 0

* chinaminumber equal to True (unknown variable)



## Next events

* [Chinami: Chinami-Corp](./chinamidate5.md)

## Event properties

* Id: chinamidate1
* Group: Chinami
* Triggered by label: callchinamimorning
* Triggered by branch label: callchinamimorning
* Triggered by path: callchinamimorning->chinamidate1

## Official wiki page

[5,000 Year-Old Wizard](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate1&go=Go) for more details.

## Event code

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label chinamidate1:
    "Come to think of it, I haven’t really spoken to Chinami over the phone yet."
    "It would probably brighten her day to hear from someone, so maybe I’ll do that?"
    "Plus, it’s not like I have any qualms spending my free time chatting with a complete angel."
    "The only issue is whether or not she’s even awake yet. "
    "But, oh well. Won’t hurt to try I guess."

    play sound "phonebeep.wav"

    "I tap on Chinami’s name and wait to see if she answers."
    "………"
    "……"

    play sound "phonebeep.wav"

    c "Hello? Sensei?"
    s "Oh, uhh. Hey."
    c "Why are you calling Chinami so early in the morning?"
    c "In fact, why are you calling Chinami at all?..."
    s "Oh, you know. I just thought she’d be happy to actually get a call from someone..."
    s "I can’t imagine she’s gotten to use her phone for its intended purpose yet so...Yeah."
    c "It’s like 9:00 AM...It really couldn’t wait until later?"
    s "I’m a busy guy, Chika."
    c "Well...I guess that’s true."
    c "Chinami’s actually sleeping right now, but I’m really glad you called. I was actually just about to text you."
    s "Really? For what?"
    c "Well, Yumi was supposed to come over to watch her this morning since I have work, but she just told me that she’s not feeling well and doesn’t want to get Chinami sick."
    c "Soooo...I’m guessing you already know what I’m going to ask, right?"
    s "Right. You want me to dog-sit again."
    c "Hahahah~ Well she won’t be wearing her mask today, so it’s just normal Chinami-sitting."
    c "I know you said you’re busy, but I’ll be eternally grateful if you could at least hang out here for a few hours so she doesn't wake up alone."

    "Well...It’s not like I had anything else going on this morning."
    "Chika’s place is pretty far, but I guess I can probably make it there in around half an hour."

    s "Yeah...I’ll head over now. You owe me, though."
    c "Heheh~ Of course I do. I won’t forget this. Promise."

    play sound "phonebeep.wav"

    "Chika hangs up the phone and, after getting dressed, I begin to head over..."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene chinamifirstdate1
    with dissolve
    play music "happyandplotting.mp3"

    c "Hey~ Thank you so so so so much. Really."
    s "Don’t mention it. I’m free until the afternoon anyway."
    c "That’s totally fine. Like I’ve said before, she’s fine alone. I just feel bad leaving her that way."
    s "Is she still asleep?"

    scene chinamifirstdate2
    with dissolve

    c "Nah, she’s just sitting in front of the TV right now. I made breakfast before you got here, so you like, literally don’t need to do anything."

    if bonus == True:
        c "You can even just hang out in the kitchen if you want. I can’t imagine it’d be fun hanging out with someone so much younger than you anyway."
        s "I think you might be forgetting how much younger than me {i}you{/i} are, Chika. "

        scene chinamifirstdate3
        with dissolve

        c "Heheh~ I don’t count. You told me I’m mature for my age so I’m counting that as being on the same level as you."
        s "Do whatever you want. Not like that part matters to me anyway."
    else:
        s "I love clowns."

    scene chinamifirstdate4
    with dissolve

    c "Yeah, I think you made that pretty clear recently. "
    c "But yeah, just hang out here and do whatever for a few hours. You can leave whenever you want."
    s "When will you be back exactly?"
    c "Not until later tonight, so don’t worry about staying the whole time."

    scene chinamifirstdate3
    with dissolve

    c "You should know my schedule by now, Sensei. I’m at the mall every weekend."
    s "Well hurry up and get going then. I’ll be fine here."
    c "Yeah, yeah. I’m going. "

    scene chinamifirstdate4
    with dissolve

    c "Thanks again, though. Really."
    c "You’ve been doing way too much for me lately. I have no idea how I’m going to repay you."
    s "Figure that out later. Just go to work for now."
    c "Roger that."

    scene black
    with dissolve

    c "Chinami! Don’t annoy Sensei while I’m gone!"
    ch "Chinami will do her best!"
    ch "Have a nice day at work!"

    "Chika exits the apartment, locking the door behind her and leaving me alone with her little sister."
    "………"
    "……"
    "…"

    scene chinamifirstdate5
    with dissolve

    ch "Hello! Welcome to Chinami’s house!"
    ch "Did you wash your hands?"
    s "Yeah, your sister made me wash them as soon as I came in."
    ch "Because she doesn’t want Chinami to get sick."
    s "I don’t want Chinami to get sick either."
    ch "That’s good. "
    s "It sure is."
    ch "…"
    s "…"
    ch "…"
    s "…"
    ch "Now what?"
    s "What do you mean now what?"
    ch "Are you just going to sit there and stare at Chinami until her sister comes home?"
    s "I...I haven’t really thought of that."

    "Now that she mentions it, I have absolutely no idea what I’m even supposed to be doing right now."

    if bonus == True:
        "I know Chika said it was fine to just hang out and do whatever, but it {i}does{/i} feel kind of weird being alone with a girl this small...even if she is a 5000 year old wizard."
    else:
        s "I am so lost and scared."

    ch "You can stare at Chinami if you want. But she’s going to watch TV if that’s okay with you."
    s "Nothing’s even playing on the TV."
    ch "Big sis says that the TV won’t come back on until tomorrow, so Chinami is pretending that her favorite show is on instead."
    s "And what exactly is Chinami’s favorite show?"

    "Knowing her, I’m assuming it’s some early morning cartoon or-"

    scene chinamifirstdate6
    with dissolve

    ch "Game of Thrones."
    s "…"
    ch "…"
    s "I know I’m not the one who’s supposed to be raising you, but aren’t you a little too [young]for that?"
    ch "Chinami is a 5000 year old-"
    s "Wizard. I know. Does your sister know you watch it, though?"

    scene chinamifirstdate7
    with dissolve

    ch "Mhm! We watch it together on her laptop whenever she brings it home."

    "I can’t say I know much about this show...but from what I understand, it can get pretty gruesome and..."
    "Well, let’s just say I was unaware that Chinami had been exposed to those kinds of things yet."

    s "So, you’re just sitting on a cushion pretending you’re watching Game of Thrones."

    scene chinamifirstdate6
    with dissolve

    ch "Right. Chinami took a quiz on her phone that says she’s part of House Lannister."
    s "I have no idea what that means. What does that house do?"
    ch "They have a lot of money and like each other more than they’re supposed to I think."
    s "Having a lot of money is pretty much the exact opposite of you. You don’t have {i}any{/i} money, Chinami."
    ch "This is the sad truth."

    scene chinamifirstdate7
    with dissolve

    ch "But that’s okay. Because one day, Chinami is going to be rich."
    ch "And then she's going to buy a big house for her and big sis."

    scene chinamifirstdate5
    with dissolve

    ch "And you’ll get one too since you bought Chinami her first phone."
    s "Well thank you. But I already have a house."
    ch "That’s okay. You can have two houses. A Lannister always pays her debts."
    s "I’m assuming that’s a quote from the show, so I’m just going to say thanks."
    ch "You’re welcome!"

    scene chinamifirstdate8
    with dissolve

    ch "Now, watch pretend-TV with me while we wait for big sis to finish working."
    s "That’s going to be hours from now. We’re really going to stare at a blank TV the entire time?"
    ch "It’s not blank! There are dragons and zombie things and a few really funny looking old people."
    s "You’re not supposed to make fun of old people, Chinami."
    ch "Shh! This is the best part!"

    "Chinami ‘shushes’ me and I direct my attention (For reasons I don’t understand) to a blank TV screen."

    ch "…"
    s "…"
    ch "…"
    s "…"

    scene chinamifirstdate9
    with dissolve

    ch "This isn’t as fun as Chinami expected."
    s "I can’t say I was really expecting any more from this. "
    ch "Now what do we do?"
    s "I don’t know. It’s your house. You figure something out."

    scene chinamifirstdate10
    with dissolve

    ch "Wanna watch Chinami kill pigs? She’s really good at it."
    s "I’m a little worried about your enthusiasm for killing animals. You know there are other games you can play on your phone, right?"

    scene chinamifirstdate11
    with dissolve

    ch "Other games?"
    s "Yeah. Like, that one where you crush candy. Or that one with the farm."
    ch "Can Chinami destroy the animals on the farm?"
    s "That’s...not really the point of the game, but probably? I don’t really know."
    ch "You don’t seem to know as much as big sis when it comes to phones, Mr. Sensei."
    s "Just Sensei is fine, Chinami."
    ch "Okay, Just Sensei."
    s "…"
    ch "…"
    s "You did that on purpose, didn’t you?"
    ch "Chinami has no idea what you’re talking about. She’s just a little girl who is also an ancient wizard."
    s "I’m beginning to think you might be smarter than you let on, Chinami..."
    ch "Chinami is very confused right now."
    s "{i}Sure she is...{/i}"
    ch "…"
    s "…"
    ch "Are you and big sis getting married yet?"

    "This again? How does this keep coming up?"

    s "How many times do the two of us need to tell you that things aren’t like that between us?"
    ch "A few more, probably. Chinami’s memory isn’t very good."
    ch "But she thinks you should get married anyway."

    scene chinamifirstdate12
    with dissolve

    ch "If Sensei and big sis get married, Chinami will be alone less. "

    "…"

    s "Is that why you want us to get married? So I’ll come around more?"
    ch "Maybe. "
    s "You know I can just, come around more {i}without{/i} marrying her, right?"

    if bonus == True:
        ch "Chinami also wants a little sister."
        s "...Okay, that one is a little less doable. "
    else:
        ch "You dare defy me, mere mortal?"
        s "Excuse me?"

    scene chinamifirstdate11
    with dissolve

    if bonus == True:
        ch "Big sis said she’d have a baby if it’s with you, Sensei."
        s "I do not believe a word of that, Chinami. You’re deceiving me."
        ch "Chinami doesn’t know what that word means, but she’s telling the truth."
        s "Why would your sister even say that? Something’s not adding up here."
        ch "Chinami doesn’t even know where babies come from because you wouldn’t tell her. She has no reason to lie."
        s "Good. I have no intention of telling you something like that."
        ch "Okay. I’ll ask big sis."
        s "No. Definitely don’t do that either. She’ll think it was me who said something."
        ch "Then Chinami will ask big sis Yumi. She looks mature so she probably knows."
        s "..."
        s "Actually, yes. Do that. I’m sure Yumi will be willing to tell you all about it. She won’t get flustered even one bit."
    else:
        ch "I have lived for thousands of years and you will tell me what I demand you to tell me."
        s "Chinami, no."
        ch "Teach Chinami the secrets of life! What it means to be human!"
        ch "Only then will Chinami spare you destruction!"
        s "Okay, Chinami. I will do just that."

    scene chinamifirstdate13
    with dissolve

    ch "Hooray! Chinami will learn a new thing soon! And no thanks to her future daddy!"
    s "Marrying your sister wouldn’t even make me your daddy. I’d have to marry your mom."
    ch "…"
    s "…"

    scene chinamifirstdate14
    with dissolve

    ch "Hi, Mom. Can you do me a favor?"

    "Things suddenly become incredibly morbid and don’t mesh well with the background music. Such is life."

    ch "Can you marry Sensei? He is a nice man and he bought Chinami a phone."
    ch "Chinami wants to take care of a sister the way big sis takes care of Chinami."
    ch "Also Sensei has glasses and big sis says you always liked boys with glasses."
    s "Chinami..."
    ch "Shh...I’m talking to my mom. Watch pretend-TV, Sensei."
    s "...Fine."

    "I pretend to watch pretend-TV and fall into pretend-inception."
    "How did a trip to hang out with my student’s little sister turn into something so complicated?"

    scene chinamifirstdate15
    with dissolve

    ch "{i}Also, he has lots of money. He even paid for Yumi’s phone. I think he works for the government.{/i}"
    s "Chinami, what in the world are you whispering about over there? I think I just heard something about the government."
    ch "No words, Sensei. Chinami needs silence to reach her mom through the picture."
    s "...Whatever Chinami needs."

    scene black
    with dissolve

    "Chinami spends the next twenty minutes whispering to the picture of her mother while I sit next to her, pretending to not hear what she’s saying."

    if bonus == True:
        "It’s an incredibly uncomfortable morning, especially when you realize that she’s basically trying to get her mom to agree to have sex with me."
        "Now, let’s get one thing straight."
        "I am a man with very low morals."
        "But even I don’t think I’d stoop as low as having sex with the Chosokabes' mother."
        "If she were alive, that would be another story but-"
        "Wait a minute. What the fuck am I even saying right now?"

    "{i}The next few hours pass by without becoming any more comfortable.{/i}"
    "{i}But at least Chinami didn’t spend the day alone.{/i}"

    $ renpy.end_replay()
    $ chinami_love += 1
    $ chinamidate1 = True
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label chinamidate5:
...
```

## Code that triggers this event

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label callchinamimorning:
    if chinami_love >= 0 and chinamidate1 == False:
        jump chinamidate1
...
```