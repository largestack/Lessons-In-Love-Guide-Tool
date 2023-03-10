# Unidentical Twins (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: futabafirsthall
* Group: Futaba
* Triggered by label: dormtuesday
* Triggered by branch label: dorms
* Triggered by path: dorms->dormtuesday->futabafirsthall

## Official wiki page

[Unidentical Twins](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabafirsthall&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabafirsthall:
    scene futabahall1
    with dissolve

    s "Hey, Futaba. What are you up to tonight?"
    f "Hey, Sensei. I’m...not really doing anything."
    f "The plan was to spend tonight studying, but..."

    scene futabahall2
    with dissolve

    f "I guess I...don't really know if there's any rush in doing that on account of your...new methods?"
    f "I suppose there still are standardized tests coming up, though...so maybe I should?"

    scene futabahall1
    with dissolve

    f "Oh! You could...maybe help me study if you have a little free-"
    s "Pass."

    scene futabahall4
    with dissolve

    f "Oh."
    s "Yeah. It's nothing against studying. That's still an...important thing to do, I guess. I'd just prefer not spending my free time helping out with something like that."

    scene futabahall3
    with dissolve

    f "I guess I can't blame you since that's the same dilemma I'm facing right now. I'll just...hold off until Rin gets home and do it with her, I suppose."
    f "Studying alone isn't really fun anyway."
    s "To be fair, it's not very fun studying with other people either. But I commend you for keeping up with your studies despite having a teacher who actively talks you out of it."
    f "Well...I know you still have my best interests at heart. So I'm sure these new methods of yours will all make sense soon enough."
    s "Exactly. Just do everything I tell you to do and you'll graduate in no time at all."

    scene futabahall4
    with dissolve

    f "E...Everything? That...sounds a little...umm...how should I put this?"
    s "Controlling? I guess. I wasn't planning on commanding you to do anything weird, though."

    "That comes later."

    s "I just think it would be best for all of us if we spent more time relaxing and less time worrying about school."

    scene futabahall3
    with dissolve

    f "That...kind of sounds like you're trying to discourage me from studying altogether."
    s "Maybe not {i}altogether,{/i} but whenever I'm around."
    f "Umm...doesn't that sound a little risky, though?"
    s "I don’t think so. It's not like I'm going to be with you all hours of every day. Utilizing the time spent with your teacher to...get inspired or something will motivate you when you're alone."
    s "I read that in a book somewhere, so it is obviously true."

    scene futabahall1
    with dissolve

    f "Heheh...Well, if it's in a book, it {i}must{/i} be true."
    f "I do like talking to you a lot...so I suppose indulging in that a little more often is fine by me as long as you're okay with it."
    f "I just wish I had a little more time tonight to...do that."
    f "I don't think Rin will be gone for much longer, unfortunately."
    s "I won't take up too much of your time, don't worry. I just wanted to see how things were going over here."
    s "Are you enjoying dorm life? Sleeping properly? Do you have a key to the showers I could borrow?"

    scene futabahall4
    with dissolve

    f "W...What was that last part?"
    s "Are you sleeping properly?"
    f "Huh...maybe I'm not if I'm...hearing things like I thought I just heard."

    scene futabahall1
    with dissolve

    f "That aside, living with Rin is really fun. I can't really imagine having any other roommate."
    s "Yeah. She’s quite the character, isn’t she?"

    scene futabahall5
    with dissolve

    f "Mhm! I’ve known her for years too, so I’ve seen sides of her nobody else has seen."
    f "I don't think it would be an overstatement to say that the two of us are inseparable at this point."
    s "Huh. I knew you two were close, but I didn’t think you were {i}that{/i} close."

    scene futabahall6
    with dissolve

    f "Oh, yeah. We are. The two of us are more like sisters than friends, I think."
    s "Does that make you the older sister or the younger sister?"

    scene futabahall1
    with dissolve

    f "I...guess a little of both?"
    f "There are times where I have to look out for her...but there are plenty of times where she looks out for me as well."
    f "I'd say she's more like a twin sister than anything, but the two of us...don't really look anything alike, so..."
    s "Interesting. Well, I'm glad that the two of you can rely on each other. All I have is Ami and you can probably imagine how that is."

    scene futabahall5
    with dissolve

    f "Hahaha! Yeah, I can imagine that getting pretty exhausting from time to time..."

    scene futabahall1
    with dissolve

    f "Ami is a good girl, though...And so is Rin."
    f "You and I are lucky, Sensei...having people who care about us so much. Even if they can be a little too energetic at times."

    scene black
    with dissolve2

    "Futaba and I spend the next few minutes talking about school and how she's saving up her allowance money to find a new place closer to the urban district once she graduates."
    "Apparently, even though Futaba's parents live overseas, they still send her a check every month."
    "It must be great getting money for not doing anything."

    if bonus == True:
        "Though, I guess it's also pretty great getting paid to loiter in girls' dorms, so...I probably shouldn't be complaining."
    else:
        "Unfortunately, I am a hard working man who must earn money to live and pay for my CPA's services."

    "Eventually, Rin comes back home and I lose my role as the person keeping Futaba occupied for the night."
    "The two of them head back inside to start studying for tests and I-"
    "I go back home to someone who cares about me."

    $ renpy.end_replay()
    $ futabafirsthall = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabahall:
    if chapthreeactive == True:
        scene futabasummer2hallgen
        with dissolve
    elif christmas7 == False:
        scene futabahall6
        with dissolve
    else:
        scene futabahallwinter
        with dissolve

    f "Oh, Sensei! It’s nice to see you."
    f "What brings you to the dorm?"

    "Futaba and I spend some time talking about random subjects together."
    "She asks me for some advice regarding how to harness her creativity and I answer to the best of my ability."
    "Ami eventually texts me asking where I am and I decide to head back before she lights the house on fire."
    "Futaba laughs at this and says she understands, but it’s easy to tell that she feels a little upset."
    "Regardless, I bid her goodbye with a pat on the head and begin my trek home..."

    scene black
    with dissolve

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rinfirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label dormtuesday:
        if chapthreeactive == True and mikublock == False:
            scene summerdorm1tues
            with dissolve
        elif chapthreeactive == True and mikublock == True:
            scene dormtuesmikugone
            with dissolve
        elif christmas7 == True and chapthreeactive == False:
            scene tueswinter
            with dissolve
        else:
            scene dorm_tuesday
            with dissolve

        play music "sweetvermouth.mp3" fadein 2.0

        "I decide to pay a visit to the dorms."
        "What should I do?"

        menu tuesdaymenu:
            "Knock on a door":
                jump doorknock
            "Talk to Miku" if mikublock == False:
                if mikufirsthall == False:
                    jump mikufirsthall
                else:
                    jump mikuhall
            "Talk to Futaba":
                if futabafirsthall == False:
                    jump futabafirsthall
...
```