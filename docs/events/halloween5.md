# Sexy Land (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Mysterious Abundance of Chickens](./halloween4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween5
* Group: Main
* Triggered by label: halloween4
* Chain sources: halloween4
* Chain sources path: halloween4

## Official wiki page

[Sexy Land](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween5&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween5:
    play sound "dooropen.mp3"

    s "I’m home. "

    "I open the door after a relatively long walk back from my semi-date with Kaori."
    "A date that may or may not have ended with me being closer to a chicken than probably ever before."
    "I’m thankful that I didn’t hit my head too hard, though. "
    "My day would really take a turn for the worse if I started seeing things that weren’t there or something along those lines."

    scene dolphinhome1
    with dissolve2

    s "Oh dear God no."

    play music "normalday.mp3"

    do "Welcome home."
    s "It talks, too?"
    do "...?"

    "Is it possible for a concussion to take this long in order to set in?"
    "Do concussions even cause people to hallucinate?"
    "What sort of medical condition would cause me to see a dolphin in the middle of my living room?"

    do "U-Umm...you look really pale all of a sudden..."
    do "Are you okay?..."
    do "Should I call Ami?..."
    s "Who are you and why do you know my [niece]?"

    scene dolphinhome2
    with dissolve

    "I approach the dolphin."
    "That is not a sentence I imagined I’d be saying today."
    "Or ever."

    do "S-Sensei?..."
    s "You’re no student of mine."
    s "Go back to the sea where you came from."
    do "The...sea?"
    do "..."
    do "Oh!"

    scene dolphinhome3
    with dissolve

    "The dolphin removes its head and I’m suddenly face to face with someone else I don’t know."
    "She looks kind of like Sana, but with one extra eye."

    sal "Um...sorry about that..."
    sal "It probably felt weird...coming home and seeing a dolphin in the living room."
    s "Do I know you?"

    scene dolphinhome4
    with dissolve

    sa "O-Of course you know me! I’m Sana!"
    sa "M-Maybe I should call Ami after all?"
    sa "If you don’t even recognize me, then..."
    s "Oh, Sana. Yeah, I know you."
    s "I’ve just never seen you with your hair not covering your face before."

    scene dolphinhome5
    with dissolve

    sa "Well, it’s...umm...really hot inside of this costume...so I kind of had to pull it back..."
    sa "I hope I don’t look too weird..."
    s "You’re wearing half of a dolphin’s body. Of course you look weird."
    sa "...That’s not what I meant."
    s "Why a dolphin, though? And did you really make this with stuff you bought from the mall?"

    scene dolphinhome6
    with dissolve

    sa "Of course not...I’m not talented enough to make something like this..."
    sa "I...couldn’t find anything I liked at the mall, so I got this from my mom."
    s "Would you mind explaining to me why your mom owns a dolphin suit?"
    sa "I think she got it from...Makoto’s mom..."
    s "I mean, I guess that makes slightly more sense given that we’re dealing with Maki, but I’d still like to know why she owns a thing like this."
    sa "So would I but...I’m not really in the...position to be asking any questions when I just...need a costume."
    sa "Are you...really not going to dress up, Sensei?"
    s "I’m not. I don’t really think something like that suits my personality."
    sa "But...you’re still coming to the party...right?"
    s "Right. I wouldn’t miss the chance to see everyone’s costumes even if it meant the death of me."

    scene dolphinhome7
    with dissolve

    sa "That’s...kind of weird..."
    s "What will be even weirder is if everyone else dresses like some sort of sea creature as well."
    ay "Never fear, Sensei! Behold, my wonderful non-sea-creature costume!"

    scene black
    with dissolve

    "Oh good, Ayane is here."
    "I was beginning to worry that Sana was just alone in my house for some reason."
    "I’m sure Ayane has some sort of slightly provocative costume that she’ll use in her favor to catch my-"

    scene dolphinhome8
    with dissolve

    ay "Mi'lady."
    s "..."
    s "What ever happened to normal costumes?"
    s "Why are two cute [teenage]girls in my house wearing a suit of armor and suit of...dolphin?"

    scene dolphinhome9
    with dissolve

    ay "What’s the matter, Sensei?"

    if bonus == True:
        ay "You weren’t expecting me to be wearing something more...risque, were you?"
        ay "And be careful how you respond. Sana is right next to us and still has virgin ears."
        ay "If we’re going to talk more about what you {i}wish{/i} I was wearing, perhaps we should take this to the bedroom?"

        scene dolphinhome10
        with dissolve

        sa "Umm...my ears aren’t-"
        s "Please tell me that at least Ami and Maya are wearing more...traditional Halloween costumes."
    else:
        ay "Do you hate dolphins, you fucking punk? Because I will hit you if you do."
        sa "..."
        s "Uhh... are Ami and Maya at least wearing more...traditional Halloween costumes?"

    scene dolphinhome11
    with dissolve

    ay "Oh, I don’t really know what Maya is going to be."
    ay "She said she had a plan and that she has everything she needs in the dorm."
    ay "Ami’s just going to be Sailor Moon."
    s "Sailor what?"

    scene dolphinhome12
    with dissolve

    ay "Sailor Moon. From that anime you used to watch with us when we were little."
    ay "That’s when Ami started putting her hair in twintails, remember?"
    ay "Because you always talked about how you thought Sailor Moon was cute and-"

    scene dolphinhome13
    with dissolve

    ay "Wait a minute. That means that she’s trying to get you to think she’s cute with her Halloween costume as well."
    ay "She knew I’d be at a disadvantage since you can’t gaze at my beautiful figure through this suit of armor and is using that against me."
    sa "But...I think...the suit of armor fits you, Ayane..."

    scene dolphinhome14
    with dissolve

    ay "Is that supposed to make me feel good?!"
    ay "Why do I look like I belong in a suit of armor?!"
    s "You could always just go as something else, you know."

    scene dolphinhome13
    with dissolve

    ay "I absolutely can not. Especially after Geoffrey went through the trouble of removing this suit from where it was mounted."
    ay "I owe it to him to follow through with my choice of costume. Even if it’s extremely hard and uncomfortable to walk around in."
    s "If it’s that uncomfortable, just take it off now."
    s "There’s no need to be walking around as a knight twenty-four hours before your party starts."
    s "Same thing with Sana and her dolphin costume."

    scene dolphinhome15
    with dissolve

    ay "That’s true. I suppose now that I’ve confirmed that it fits, there’s no reason for me to stay inside of it anymore."

    if bonus == True:
        ay "Besides, I don’t mind you seeing me in my underwear or anything like that."
        s "You’re...not wearing anything else under that besides your underwear?"
        s "Isn’t the metal...cold? Or uncomfortable?"
        ay "Extremely. I’d much prefer being in Sana’s costume right now."
        ay "She’s also in only her underwear beneath that, but probably much warmer than I am at the moment."
    else:
        ay "Thankfully, I am fully clothed beneath this."
        s "That sounds very hot. But like, temperature hot."
        s "I don't want it to sound like I'm insinuating anything."
        ay "Did you know that Sana is wearing a tuxedo beneath hers?"

    scene dolphinhome16
    with dissolve

    sa "Wh-why are you telling him something like that?!"

    if bonus == True:
        ay "What’s wrong? It’s not like he can see through clothes or anything."
        ay "And if he could, I’m sure he’d much prefer looking at you through your dress rather than through the mascot for Sexy Land."
    else:
        ay "What's wrong? A tuxedo sure beats being the mascot for Sexy Land."

    sa "What the heck is Sexy Land?!"
    ay "Hm? It's the name written over the costume's logo."
    ay "You really didn't notice?"

    scene dolphinhome17
    with dissolve

    sa "Wha-?!"
    sa "Why would someone make a dolphin the mascot for a place called S-S-S-Sexy Land?!"
    sa "This makes no sense!"

    if bonus == True:
        ay "I’ve actually heard that having sex with a dolphin is really close to what it feels like to have sex with a girl."
    else:
        ay "I’ve actually heard that hugging a dolphin is just like hugging a normal girl, except it is a dolphin so it is large and wet and doesn't feel anything like a normal girl."

    scene dolphinhome18
    with dissolve

    sa "WHY IS THAT A THING?!"
    sa "HOW DO THEY KNOW?!"

    if bonus == True:
        ay "Hey, I’m not saying it’s okay to have sex with dolphins."
        ay "I’m just saying that if a guy gets naked, closes his eyes and trips into a dolphin's vagina, he might not know right away."
    else:
        ay "Seems like a pretty reasonable thing to assume."

    sa "WHYAREYOUSTILLTALKINGABOUTTHIS?!"

    scene dolphinhome19
    with dissolve

    s "Maybe it would be good to lay off of Sana for a second."
    s "At least until she comes to terms with exactly what she’s wearing."
    ay "Sounds good to me."

    if bonus == True:
        ay "Would you have sex with a dolphin, Sensei?"
        s "…"
        ay "…"
        s "No?"
    else:
        ay "Would you hug a dolphin, Sensei?"
        s "I would hug anything and everything."

    s "Is that even a real question?"

    if brony == True and bonus == True:
        "I would have sex with a pony, though. But Ayane doesn't need to know that."

    ay "What if the dolphin looked like the girl of your dreams? So basically, what if it looked like me?"

    if bonus == True:
        s "I’m not going to have sex with a dolphin, Ayane."
        ay "Well, that's good."
    else:
        s "I already said yes, Ayane."

    sa "I’m...going to get changed..."

    scene dolphinhome20
    with dissolve
    play sound "dooropen.mp3"

    "Sana quickly vanishes into Ami’s room and presumably strips down to her underwear."
    "I try to fantasize about it, but I keep landing back on that dolphin fact instead."
    "There’s no way that’s true, is it?"

    scene dolphinhome21
    with dissolve

    ay "Oh my. It appears the two of us are suddenly alone."
    s "Just because everyone else is in Ami’s room doesn’t mean we’re {i}alone{/i}, Ayane."
    ay "It’s not everyone, it’s just Sana."
    ay "Ami and Maya went to the convenience store to get snacks for tonight."
    s "Tonight? But the party is tomorrow."
    ay "Oh, she didn’t tell you?"
    ay "We’re all sleeping over and watching horror movies and stuff tonight."

    if sanadorm30 == True:
        s "I’m sure Sana is thrilled about that. She loves horror movies."

        scene dolphinhome22
        with dissolve

        ay "How...do you know that?"
        ay "That's not something she normally tells anyone."
        ay "Are you two getting closer or something?"
        s "It’s just...come up in conversation before."
        ay "I see..."

        scene dolphinhome23
        with dissolve

        ay "Well, either way..."

    ay "Did you want to maybe...watch some with us or something?"
    ay "Maya will probably complain about there not being enough room for all of us on the couch, but I don’t mind sitting on the floor if I have to."
    ay "I just want you to be there so I can hold your hand when I get scared and stuff."
    s "Are you actually going to get scared from watching a horror movie?"
    s "I have a hard time believing that for some reason."
    ay "Of course not. But I can pretend I am so no one will get mad at me when I jump on you."
    s "Well, sorry to be the bearer of bad news, but I actually have plans tonight."

    scene dolphinhome22
    with dissolve

    ay "Plans?"
    ay "What...kind of plans?"
    s "A friend of mine is having a Halloween party at her bar."
    ay "Her...bar?"

    scene dolphinhome24
    with dissolve

    ay "Are you..."
    ay "Friends with Sana’s mom now?..."

    "...Right."
    "Of course Ayane would be a little surprised to hear that."
    "All this time, she’s been under the impression that her and the rest of the girls are the only ones in my life."
    "It’s probably a bit of a shock hearing that there are others she doesn’t know about."
    "But as long as I downplay the fact that I’ve spent enough time with Sara to warrant going to her place for a Halloween party, I’m sure I can console Ayane to at least...some extent."

    s "I am."
    s "Just friends, though. So don’t worry."
    ay "Of course I’m going to worry. She’s really pretty."
    ay "She’s like a grown-up Sana and Sana is already super cute."
    ay "You’re telling me I need to compete with a grown woman now, too?"
    s "You’re not competing with anyone."
    s "You’ll always have a special place in my life, Ayane. There’s not really anyone that could replace you."

    "That might sound like a lie, but that much is actually true."
    "Sure, she might interpret that as “There is no one else I’m romantically involved with,” but what I really mean is that she’s like..."
    "The closest someone can get to being family without actually being family."
    "She’s here almost every day and has obsessed over me longer than anyone."
    "Even Ami took a little while to start showing her true colors. Ayane's been head over heels since the beginning."
    "So of course she has a special place in my heart."

    scene dolphinhome25
    with dissolve

    ay "When you say it like that...I really can’t worry at all, can I?"
    ay "That would just make me needy."
    ay "Can I text you all night?"
    s "Sure, but that also kind of makes you needy."
    ay "Can I text you after the movie, then?"

    if bonus == True:
        ay "Or, better yet, can I “sleepwalk” into your room in the middle of the night and sleep there with you?"
    else:
        ay "Or, better yet, send you unsolictited and funny photoshopped pictures of Ami's face on a variety of sumo wrestlers?"

    s "You can do whatever you want. I figured that’s what you’ll wind up doing anyway, so I’m at least grateful for the warning."

    scene dolphinhome26
    with dissolve

    ay "Heheh! It’s settled then!"

    if bonus == True:
        ay "You have fun at your party and there will be a special serving of Ayane that you can have all to yourself once you get home!"
    else:
        ay "Be ready for some awesome sumo Ami action!"

    s "Thanks. I’m looking forward to it."

    scene black
    with dissolve2

    "Ami and Maya come home roughly twenty minutes later and immediately disappear into Ami’s room to finish her costume."
    "The sun is beginning to set, so I figure now is as good a time as any to start heading over to Sara’s."

    play sound "dooropen.mp3"

    "Without saying goodbye to anyone, I put my shoes back on and head out the door."
    "The first thing I notice when I step outside is the sudden lack of crying cicadas-"
    "And a breeze so cold I can feel my organs freeze."

    $ renpy.end_replay()
    $ sana_love += 1
    $ ayane_love += 1
    $ halloween5 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

label halloween6:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```