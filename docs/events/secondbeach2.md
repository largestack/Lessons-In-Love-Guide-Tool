# Egg Tossing (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Good Morning](./secondbeach1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach2
* Group: Main
* Triggered by label: secondbeach1
* Chain sources: secondbeach1
* Chain sources path: secondbeach1

## Official wiki page

[Egg Tossing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach2&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach2:
    scene secondbeachintro1
    with dissolve2
    play music "shiningstarinstrumental.mp3"

    "Ami and the others wind up [[reluctantly] parting ways with me once we make it to the beach to unpack their things and figure out whether or not it’s safe to get changed into their swimsuits."
    "But, judging by the fact that it is freezing out and everyone else I’ve encountered is dressed in their winter clothes, this seems highly unlikely."
    "Oh, and also Karin had to go get into a fight with her sister or something."
    "I don’t know, I’m not really trying to get involved."
    "Kirin’s the angry one and I doubt she’d be able to ever hurt her older sister on a more than emotional level, so I’m not worried about anyone getting injured."
    "What I am worried about, though..."

    s "Are you guys just going to let Yasu...talk to Yumi?"
    to "She’s been quite well behaved as of late, so I have decided to loosen her leash and allow her wildest dreams to run free for a moment or two."
    ya "Oh, how I wish I could don such dark clothing at this time of year! "
    ya "How do you stand so still with feet yet unsinged by the gaze of what lurks below?! "
    c "I think it’s going pretty well."
    s "You two are bad friends."

    scene secondbeachintro2
    with dissolve

    y "The fuck am I supposed to do about this? She’s clearly off her meds, right?"
    s "I’ve been wondering that ever since I met her."
    s "I think she might just be permanently off of them."
    y "Do we need to like, call somebody or some shit?"
    s "That depends on if you’re okay with using your phone now that you know I pay for it."

    scene secondbeachintro3
    with dissolve

    y "Of course I’m okay with using it! It’s not like I have much of a fuckin’ choice, is it?!"
    to "Sensei, you pay for the class bully’s phone bill?"
    to "I feel as if this may be enabling her to a certain extent. "
    c "He pays for mine and my sister’s as well. "

    if bonus == True:
        c "Sensei gets a lot of shit for being a perv and stuff, but he’s actually a really nice guy who’d never hurt anyone or anything."
    else:
        c "You know, a lot of people don't realize it, but Sensei really is a generous guy and a great teacher."
        s "=D"

    s "..."
    to "At the very least, you should have her perform some sort of service in exchange for such a cumbersome weight on your depressingly thin- {i}ahem...{/i}"
    to "On your exceedingly standard commoner wallet."
    s "Good idea, Touka. "
    s "Yumi, can you-"
    y "Fuck off! No!"
    s "I don’t think she wants to provide any sort of service."

    if bonus == True:
        "Which is extremely depressing as I had a good amount of them lined up for her."
        "I doubt she’d fit into Ami’s maid outfit, though, so I should probably take some time to-"
    else:
        "Which is extremely depressing as I've been procrastinating trimming my hedges for {i}weeks{/i} now."

    y "Yo! Quit fuckin’ thinkin’ about whatever weird shit it is you’re thinkin’ about and tell me what to do about this...thing!"
    ya "Yes, Yumi! I am just a {i}thing!{/i} "
    ya "Unworthy to be even called a human if I’m still so weak that the threads of his choosing play hell upon my skin!"
    ya "Praise be!"
    s "So anyway, welcome to the beach, I guess."

    scene secondbeachintro4
    with dissolve

    c "Welcome to you as well, Sensei! You’re gonna be the busy one this weekend, so I hope you’re savoring this moment as much as I am."
    s "As true as I expect that statement to be, I’d like to know why you think I’m going to be busy."
    c "Because Makoto started asking everyone where you were the second she showed up."
    to "She’s been searching for you quite thoroughly, might I add."
    to "I do believe I even saw her check the men’s washroom for you. It must be incredibly urgent."
    s "Nah. Makoto’s just secretly a boy and really self conscious about it."

    scene secondbeachintro5
    with dissolve

    to "Oh my. How insensitive of me to assume such a thing about him. "
    s "It’s okay. I won’t say anything."
    c "…"
    s "…"
    s "What? Why are you looking at me like that?"
    c "Stop taking advantage of Touka’s...gullibility and clear this up before it becomes a dramatic and awkward misunderstanding."
    s "But it would have been so funny."
    c "And mean to Makoto. She like, {i}just{/i} cleared up the whole thing about the fake relationship with a janitor you told everyone about."
    s "I didn’t tell {i}everyone{/i}. Just a select few people."
    s "It’s not my fault you girls can’t keep secrets to yourselves."

    scene secondbeachintro6
    with dissolve

    c "Oh, we certainly can."
    s "And on that note, I will now confirm that Makoto is a girl."

    if bonus == True:
        s "Don’t ask me how I know how, though. "
    else:
        s "Though, if she wants to identify as a different gender, that is okay and won't change who she is as a person."

    to "I am quite confused right now."
    s "Yeah. I think you’ll find yourself getting even more confused about certain things as the weekend goes on. "
    s "The beach trip is normally a pretty exciting string of events for us that resolves a lot of ongoing issues while introducing several more."

    scene secondbeachintro7
    with dissolve

    to "How incredibly specific."
    to "Are you willing to confirm this, Chika? I have learned this morning to distrust every bit of information this man provides me."
    c "Haha...hah..."
    s "You’re just going to have to take my word for this one, Touka."

    scene secondbeachintro8
    with dissolve

    c "A-Anyway! Must be kind of weird for your first trip to the beach to be such a cold one, right?!"
    s "You’ve never been to the beach before, Touka?"

    scene secondbeachintro9
    with dissolve

    to "Not one even half as...quaint as this one."
    s "I’m going to go out on a limb here and assume your family owns a private beach?"
    to "A private island, actually. I’ve been taking competitive swimming lessons since I was a little girl and am quite confident when it comes to watersports."
    s "Ha."
    to "…"
    to "Ha?"
    s "Don’t worry about it."
    to "The lower middle class certainly has the strangest sense of humor."

    scene secondbeachintro10
    with dissolve

    to "But yes, Chika. It is quite strange to be coming to a place like this in the middle of what is one of the coldest winters in Kumon-mi’s recorded history."
    to "I’m not yet entirely accustomed to the traditions of most of you girls, but I’d like to express my concern for your well-being if you truly do intend to swim in this weather."
    c "I’m probably not going to bother."
    c "I brought my swimsuit, but...yeah. Not really trying to catch a cold."
    to "That is fine. I’m sure there are plenty of other ways for us to enjoy ourselves."
    s "You're at least going to try them on, though...right?"

    scene secondbeachintro11
    with dissolve

    to "Hm? What reason would there be to wear our swimsuits in weather like this? That doesn’t make any sense at all."
    s "But..."
    s "But it’s the beach trip..."

    if bonus == True:
        to "Sensei, you are making it sound as if your enjoyment of this small vacation hinges entirely upon whether or not the majority of us are dressed down."
        s "Yes."
    else:
        s "I think not wearing a swimsuit is against the rules and I don't want any of us getting in trouble."

    y "Uh. My shift with this...thing is over. "
    y "Anyone wanna take control so I can go fuckin’...walk around or some shit?"
    ya "Let us walk together! To the highest of highs! The ends of the earth! "
    ya "Let us bare it all before he who-"

    scene secondbeachintro12
    with dissolve

    to "Yasu!"

    scene secondbeachintro13
    with dissolve

    ya "…"
    ya "Yes, Touka?"
    to "If you do not stop terrorizing that girl this instant, you are going to end up with a black eye and medical bill so extravagant that even I would not be able to handle it."

    scene secondbeachintro14
    with dissolve

    to "Just kidding. That was elevated high class humor in which I say things that are untrue and then laugh when I reveal that they actually {i}are{/i} true."
    to "Oh, I crack myself up."
    y "And on that note, I’m outta here."
    y "Peace."
    s "Mind if I tag along?"
    y "…"
    s "...?"
    y "Is that a fuckin’ joke? Course I mind."
    y "Get the fuck away from me, knob goblin."

    scene secondbeachintro15
    with dissolve

    c "Don’t be gone too long, okay? I’d like to at least spend {i}some{/i} time with you before the end of the weekend. "
    s "I’m sure you will, Chika."
    s "{i}I’m sure you will...{/i}"
    to "You are quite bad at whispering, Sensei. I can hear you loud and clear."
    s "I..."
    s "Yeah."
    s "Anyway. Let’s go, Yumi."
    y "The fuck do you mean, “Let’s go, Yumi?!” That’s not a thing you say!"
    s "Let’s-"
    y "No! I’m going somewhere {i}alone{/i}! Fuck off!"

    scene black
    with dissolve2

    "Yumi and I make plans to go somewhere a little more private and-"

    y "Jesus Christ, can’t I get a moment to myself around here?!"
    s "Of course not. That completely defeats the purpose of this entire trip."

    scene secondbeachintro16
    with dissolve

    "I walk down what feels like the length of the entire shoreline with Yumi, but is realistically only around half a mile."
    "And I technically wasn’t walking {i}with{/i} her. I was walking behind her."
    "But hey, she’s finally slowed down and is now actually looking at me, so that’s a good place to start."

    if bonus == True:
        y "The fuck are you still following {i}me{/i} for when you’ve got an entire yacht full of girls trying to suck your dick?"
    else:
        y "The fuck are you still following {i}me{/i} for when you’ve got an entire yacht full of girls ready to hug as soon as you say the word?"

    s "Touka has the yacht. I’m just a lowly middle class citizen trying to coax a loner into having fun this weekend."

    scene secondbeachintro17
    with dissolve

    y "Oh! Well, in that case, sure! Wanna go get a popsicle and watch the sunrise together?"
    s "Sure, Yumi. That sounds delightful."

    scene secondbeachintro18
    with hpunch

    y "No it doesn’t and you fucking know it!"
    y "I don’t even like the beach! I’m only here because Chinami kept fuckin’ bitchin’ at me to take a vacation or some shit!"
    y "Ain’t a fuckin’ vacation if I’m gonna have to deal with you, though!"
    s "I mean, you should have known something like this was going to happen as soon as you agreed to come."


    scene secondbeachintro19
    with dissolve

    y "Ugh...At least you’re not fuckin’ zoned out this time."
    y "And I guess it’s {i}technically{/i} easier talkin’ to you than it is that fuckin’ religious cult girl."
    s "I want to take that as a compliment, but Yasu is extraordinarily hard to talk to."

    scene secondbeachintro20
    with dissolve

    y "Right? The fuck’s her deal?"
    s "Yasu aside, can I take Chinami’s apparent forcing of you to come here as confirmation that you won’t be leaving after just a few hours again?"

    scene secondbeachintro21
    with dissolve

    y "I’ll be here the whole fuckin’ weekend."
    y "No idea how the fuck I’m gonna sleep in a room full of those other girls, but I managed during the dorm war thing, so I guess I’ll just fuckin’ chill in a corner or some shit."

    if dormwarfloor1win == True:
        s "Don’t forget that I’m going to be sleeping in there, too."

        scene secondbeachintro22
        with dissolve

        y "The fuck you mean you’ll be there too?!"
        s "That was the prize for the dorm war, remember? And you guys won."
        y "That was real?!"
        s "Did you think the grand prize was just a joke?"
        y "I was sure as fuck hoping it was! I can’t sleep in the same room as you!"

        if bonus == True:
            s "If you’re worried about me assaulting you again, I think I’d sooner do it {i}here{/i} than in a room full of a bunch of witnesses."
        else:
            s "If you’re worried about another surprise hug, I think I’d sooner do it {i}here{/i} than in a room full of a bunch of witnesses."

        scene secondbeachintro23
        with dissolve

        y "Fuck you. "
        y "We’re not at the level for you to joke about shit like that...and we probably never will be."
        y "I’m finally starting to feel less...scared or whatever the fuck you wanna call it around you, and it’s not gonna help if you keep pullin’ that shit."

    scene secondbeachintro24
    with dissolve

    y "But, uhh..."
    y "Shit, how do I say this?"
    y "Even though I want you to stay away from me now..."
    y "There..."
    y "There...is kinda somethin’ I’ve been meaning to ask you."
    s "Oh my god."
    y "What? The fuck do you mean “Oh my god?”"
    s "I mean you’re actually going to talk to me for once."
    s "This is a big moment."

    scene secondbeachintro18
    with hpunch

    y "You know what?! Nevermind! I don’t need to ask you shit!"

    if bonus == True:
        y "Now run the fuck off and go hang out on your blowjob yacht with the rich girl and her culty ass friend!"
    else:
        y "Now run the fuck off and go hang out on your hug yacht with the rich girl and her culty ass friend!"

    s "Yumi-"
    y "No! Fuck you!"
    s "Yumi-"
    y "Shut up!"

    menu:
        "Pry":
            stop music
            play sound "static.mp3"
            scene yumis1 with flash
            scene yumis2 with flash
            scene yumis3 with flash
            scene yumis4 with flash
            scene yumis5 with flash
            scene secondbeachintro25 with flash
            stop sound
            play music "blueair.mp3"

            s "…"
            y "…"
            s "Did-"
            y "Nothing happened."
            y "You just said some shit about how I {i}had{/i} to tell you and then stomped over to this fuckin’ log thing."
            y "But...you had that weird look thing again, so...yeah."
        "Leave her alone":
            stop music
            play sound "static.mp3"
            scene yumis1 with flash
            scene yumis2 with flash
            scene yumis3 with flash
            scene yumis4 with flash
            scene yumis5 with flash
            scene secondbeachintro25 with flash
            stop sound
            play music "blueair.mp3"

            s "…"
            y "…"
            s "Did-"
            y "Nothing happened."
            y "You just started walkin’ away and...I guess I kinda maybe...chased after you or something."
            y "But not cause I wanted to."
            y "Cause you had that...weird look again."
            y "The one that always happens when...yeah."

    s "I see."
    s "Thanks, I guess."
    y "It’s whatever."
    s "So-"
    s "Are you going to tell me or not?"
    y "Tell you what? Don’t know what you’re talkin’ about."
    s "The thing you said you wanted to ask me."
    y "Fuck."
    y "Was hopin’ your wack ass memory or whatever would have left that part out when your brain started goin’ haywire."
    s "You don’t have to, you know."
    s "I really couldn’t care less about whether or not you want me getting involved in your problems."
    y "Why? Cause you’re just gonna involve yourself anyway?"
    s "No. Because I doubt I can really do anything to fix them."
    s "I’m just curious and want to know because it’s interesting to me."
    y "Well thanks for bein’ fuckin’ honest at least."

    "Time goes by."
    "I’m not sure how much, but it’s not a lot."
    "The wind picks up and the sun refuses to rise."
    "It tries to, but it’s currently stuck behind layers and layers of clouds."
    "I begin to manually blink as my body’s auto-pilot function and the glass panes in front of my eyes do not do enough to protect me from sand or other foreign objects."
    "Then, a crack in Yumi’s tough outer shell makes its presence known."
    "An outpouring of light leaks out of her."

    y "How about tomorrow?"
    s "What about tomorrow?"

    scene secondbeachintro26
    with dissolve

    y "That I fuckin’...tell you or whatever."
    y "I don’t normally do this shit, so I’ve gotta like...figure out how."

    "I resist the urge to joke about whether or not it’s a confession of love because, let’s face it, even this much is kind of a breakthrough for Yumi."
    "One wrong move can turn that crack in her shell into the shape of a spiderweb."
    "Then, before long, everything will shatter and all of the light will escape at once."
    "And sure, I know that would make things a lot brighter for at least a short period of time."
    "But the slow drip of light particles seeping out otherwise is significantly more appealing to me than any sudden burst of sunshine."

    s "Whatever works for you."
    s "It’s not like I have anywhere else to be."
    y "Unfortunately for both of us, neither do I."
    y "Can’t say I like bein’ stuck with you of all people."
    s "I’m still better than Yasu."

    if bonus == True:
        y "‘Least Yasu won’t try to stick her tongue down my throat."
        s "I thought we weren't supposed to joke about that?"
        y "{i}You’re{/i} not supposed to joke about that."
        y "I can do whatever the fuck I want."
    else:
        y "Literally everyone is better than that freak and her fucking...airplane noises or whatever."
        s "(Airplane noises)"
        y "Nevermind. Maybe some people aren't any better at all."

    "More time goes by."

    scene secondbeachintro27
    with dissolve

    "Yumi leaves."
    "I don’t chase after her this time."
    "I figure that it’s a good move in letting her believe that she “can do whatever the fuck she wants” when I know for a fact that is false."
    "The only person who can do everything they want is me."
    "And, I guess to some extent- Maya."
    "But she’s too wrapped up in Maya things to exert any form of effort on that front."
    "Basically, those of us with an unlimited amount of time and the knowledge of such a gift may do whatever it is we desire."
    "Yumi may {i}try{/i} to do whatever she wants, but she’s closer to that of an unsuspecting mother bird than a fledgling cuckoo."
    "She’s far too busy ignoring the things she knows in her heart to be true to make an effort to push anything else aside for her own well-being."
    "And yet she pushes everything aside anyway."
    "But why?"
    "…"
    "Oh, right."
    "Because that’s all she ever learned how to do."
    "…"
    "If only I could teach her how to be more like me."
    "To toss other eggs outside of the nest."
    "And thrive in an environment you simply don’t belong in."

    scene black
    stop music

    "I have no time for such troubling thoughts."
    "I should be having fun."

    scene secondbeachintro28
    play music "justbehappy.mp3"

    "I arrive at fun."

    u "Sensei! Good timing!"
    u "Me and Io just got here and have no idea where the heck this resort thingy is supposed to be."
    s "It’s not really a “resort thingy.” It’s just kind of a small beach inn that we rented out a few rooms for."
    s "And by “we” I mean Ayane and probably Touka."
    s "As much as I like this, I absolutely would not pay for it."
    i "Do you have your own room, Sensei? Or are you going to be sleeping with the girls the whole weekend?"
    s "If I have my own room, are you going to sneak into it in the middle of the night again?"

    scene secondbeachintro29
    with dissolve

    i "Mhm. So be careful when you get out of bed so you don’t wind up breaking my leg again. It just healed."

    if bonus == True:
        u "Yeah yeah yeah. Keep it in your friggin’ pants."
    else:
        u "Yeah yeah yeah. Get a room."
        s "That...is what we're talking about, though."

    scene secondbeachintro30
    with dissolve

    u "Now take us to the heckin’ beach resort inn thingy so I can eat my breakfast and listen to whatever it is Makoto’s tryin’ to tell me about."
    s "Is she looking for you too?"
    u "She’s been textin’ me all morning about a stupid schedule thing."
    u "Apparently managin’ {i}one{/i} stinkin’ dorm war was enough for her to make me the supreme leader of the second floor. Now I’m in charge of friggin’ everybody."
    u "Ya have any idea how hard it was gettin’ Io to agree to this? Your girl is tired, Sensei. So friggin’ tired."

    scene secondbeachintro31
    with dissolve

    s "Well, whatever you did, I’m glad."
    s "I was just thinking about how I need to have more fun, and there’s certainly never a dull moment with either of you two around."
    i "You know what would be really fun? If we all-"
    u "No amusement park, Io. One step at a time."
    i "…"
    s "…"
    i "Nevermind."

    scene black
    with dissolve2

    "I scan the beach to see if anyone else is around and quickly find that either everyone is already here or we were just way earlier than I thought we were today."
    "Either way, I'm unable to find anyone and wind up showing Uta and Io the way to the inn."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ secondbeach2 = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach3

label secondbeach3:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
with dissolve

    a "Can’t you just eat it here if it's that big of a deal?"
    m "Here? Instead of on the beach? Are you insane?"
    m "Everyone knows that the beach is the best place to enjoy a watermelon. I don’t mind waiting at all if that’s a feasible option."
    m "I just don’t want to wait {i}too much{/i} because, well...melon."

    scene goodmorning39
    with dissolve

    a "Well...all of us girls are ready to go whenever. "
    a "I think we’re just waiting on Sensei to pack his things before heading over to the bus stop."
    ka "I’m...also ready whenever you want to leave. I wouldn’t want to be a burden by messing up your plans, so...my schedule is entirely up to you guys."
    m "Melon."
    s "Yes, Maya. Melon."
    m "Melon now."
    s "…"
    s "Melon now."

    scene wintersky
    with dissolve2

    "I wind up packing up my things rather quickly given that we’re only going to be gone for two days and that I...barely have anything to bring either way. "
    "Then, before long, the six of us make our way over to the bus stop, each carrying our own possessions apart from Karin- who is repenting for the watermelon tragedy by carrying Maya’s bag."
    "She offered to carry the melon itself, but...well, you can probably imagine how that went."
    "A few minutes go by with us waiting at the bus stop and gazing up at the sky, trying to figure out whether or not the snow will end by the time we get to the beach."
    "Or if it’s even snowing there to begin with."
    "It would be easy to check the weather and find out within a matter of seconds, but it’s not like any of us really trust weather forecasts in the first place."
    "Besides, life is better with an added layer of mystery thrown into the mix."
    "Life is better with an added layer of basically anything thrown into the mix, though."
    "But that’s mostly because it just sucks on its own and requires a multitude of spices to be even somewhat palatable."

    scene black
    with dissolve2

    "The bus arrives just as the snowfall ends and we all pack our things into overhead storage receptacles- melon included."
    "Ami and I sit together as everyone else finds a different place on the bus."
    "She falls asleep on my shoulder on the way and I can make out the faint smell of her shampoo."
    "It’s different than normal."
    "And slightly nostalgic."
    "………"
    "……"
    "…"

    play sound "phonebeep.wav"

    s "Hm?"

    "I get a text message just as I’m about to close my eyes as well and look down at my phone to see who it is."
    "Chances are it’s just Ayane on the other side of the bus, checking in to see what I’m-"

    ni "{i}Hey.{/i}"
    s "…"
    s "{i}Hey.{/i}"
    "…"

    play sound "phonebeep.wav"

    ni "{i}Are you busy this weekend?{/i}"
    s "{i}Are you actually trying to make plans with me?{/i}"

    play sound "phonebeep.wav"

    ni "{i}Are you busy or not? I don’t have all day to be texting, you know.{/i}"

    play sound "phonebeep.wav"

    ni "{i}In case you don’t remember, I’m very, very famous.{/i}"
    s "{i}Sorry, but I have plans.{/i}"
    s "{i}We can do something when I get back, though.{/i}"

    play sound "phonebeep.wav"

    ni "{i}Okay.{/i}"

    play sound "phonebeep.wav"

    ni "{i}Bye then I guess.{/i}"

    stop music fadeout 15.0

    "My phone finds its way through a maze of even more nostalgia (There’s quite a bit of it on this bus) and makes its way back into my pocket."
    "I gaze out of the window, letting the scent of Ami’s hair invade my nostrils, and find the skeleton of a fully decomposed animal."
    "One I recall seeing sometime before."
    "I think of how it died."
    "And ultimately follow that train of thought up to the point where it becomes far too dangerous to follow anymore."
    "I jump off board and chase after it, though."
    "Hoping that wherever it’s heading is somewhere I’ll be able to see some day."
    "But then I lose again."

    $ renpy.end_replay()
    $ maya_love += 1
    $ secondbeach1 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach2
...
```