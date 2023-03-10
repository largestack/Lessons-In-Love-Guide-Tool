# The Big Sleep (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 35

* Event [Third Place](./amimaid30.md) (Ami) is completed)

* Event [Stop Looking For Answers](./shrine35.md) (Maya) is completed)



## Next events

* [Ami: Heaven for Human Blood](./amidorm40.md)
* [Main: The WAP Man](./day295.md)

## Event properties

* Id: amidate35
* Group: Ami
* Triggered by label: callamiafternoon
* Triggered by branch label: callafternoon
* Triggered by path: callafternoon->callamiafternoon->amidate35

## Official wiki page

[The Big Sleep](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidate35&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amidate35:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’ve yet to see her come home with a new bathing suit, so unless she’s been hiding it from me for some reason, I doubt she’s gone to the mall yet."
    "I’m also aware that roughly half of the reason she’s been abstaining is due to the fact that I have not yet invited her."
    "So, without really knowing what else to do with my day, I decide to take Ami on a little trip."
    "It’s amazing how easily you can get me to actually do things when I know I won’t have to pay for them."

    play sound "phonebeep.wav"

    a "Sensei! I was just thinking about you."
    s "What? No way. What a strange turn of events."
    a "Ha ha ha. That was so funny I forgot to laugh."
    s "But...you just-"
    a "So, what’s up? Are you just calling to hear my voice or are you looking for some Ami-time?"

    if bonus == True:
        s "Ami-time sounds exhausting. I was just going to see if you wanted to take off your clothes in a dressing room for me."
        a "In public?! But that’s-"
        a "Oh wait, is this about the swimsuit?"
        s "You bet."
        a "{i}Tch...{/i}"
        s "Was that frustration I just heard?"
        a "Nope! No frustration at all!"
        a "I’m actually on the bus headed home right now, but I can just get off at the mall instead if you want to meet there!"
        a "I’m really sorry we don’t get to travel together but-"
        s "Sure, I’ll see you there."
        a "Wait. I was about to say something really cute and-"
    else:
        s "Kind of. I want to do something nice for you to reward you for always going above and beyond when it comes to accounting, and I know you have wanted a new swimsuit as of late."
        s "Would you be able to find the time to accompany me to the mall today?"
        a "Of course! Thank you for finally acknowledging all of my hard work and-"

    play sound "phonebeep.wav"

    "I hang up the phone after I finish making plans with Ami and start heading over to the bus stop."

    scene black
    with dissolve

    "The bus schedule is pretty packed around this time of day, so I imagine I won’t have to wait long."
    "And since Ami’s already on one heading back from work, I doubt that the one I get on will just so happen to have her sitting there acting all surprised once I reach the top step."
    "Yeah. Nothing convenient like that would ever happen to someone like me."
    "………"
    "……"
    "…"

    scene mall2
    with dissolve
    play music "shiningstarinstrumental.mp3"

    "Huh. I thought for sure that narrating a line like that was an omen for things to come, but apparently not."

    if bonus == True:
        "I make it to the mall after a decently quick bus ride in which an older woman (So old that I didn’t even contemplate the idea of having sex with her as more than just a passing thought) fell asleep on my shoulder."
        "I didn’t bother waking her up, though, considering she will likely die in the next several years and needs all the rest she can get until then."
        "To sleep before the big sleep."
        "Oh, what a sleep that must be."

    if amimaster.lower() in ["sensei"]:
        a "About time you showed up, Sensei!"

        scene amimalltwo1
        with dissolve

    else:
        a "About time, [amimaster]!"

        scene amimalltwo1
        with dissolve

        s "What do you think you’re doing, calling me that in public?"
        a "What’s wrong? It’s not like anybody else is paying attention."
        a "And I like calling you that. It reminds me of how close we are."
        s "I mean, I don’t care. I just don’t want someone getting the wrong idea."
        a "Blah blah blah. Who cares what people think? We’re here to get our love all over each other and stuff. I’m gonna call you what I want to call you."
        s "Can you define exactly what you mean by “getting our love all over each other?”"
        a "Nope!"

    a "How was the bus ride over?"
    a "I thought for a second that you were going to mysteriously appear on the same bus as me after our call, but it just didn’t happen."
    s "Screw the bus, what happened to your hair?"

    scene amimalltwo2
    with dissolve

    a "Huh? What do you mean?"
    a "Are you talking about my bangs?"
    s "Yeah. Aren’t they normally straight? How did you get them to...not be straight anymore?"

    scene amimalltwo3
    with dissolve

    a "The same way Maya can eat more than her body weight in food and Ayane can materialize guns and giant bananas out of thin air."
    a "Cute girl magic!"
    s "Oh, okay."
    s "Well that explains everything."

    scene amimalltwo4
    with dissolve

    a "Yup! Cute girls are special creatures who normal laws and rules don’t apply to!"
    a "So you should never question things like that because it won’t make any difference whatsoever."
    s "Hey, if you want to have magical bangs, that’s your right. You can have whatever kind of bangs you want, Ami."

    scene amimalltwo5
    with dissolve

    a "So, anyway!"
    a "I wanted to check Le Vetefrenchwordstore where Chika works because they normally have a small selection of off-season stuff."
    a "But I don’t like the way Chika looks at you, so you can just wait in the corridor while I pop in and out really quick."
    s "I am not waiting outside while you talk to Chika."

    scene amimalltwo6
    with dissolve

    if bonus == True:
        a "But what if she tries to steal your penis like Sada Abe?!"
        s "Who?"

        scene amimalltwo7
        with dissolve

        mo "Weebnote...kind of!"
        mo "Sada Abe was a geisha and prostitute who lived from 1905 - 1971 and ultimately became famous for suffocating her lover to death!"
        mo "Well, the suffocating part wasn’t what made her famous. But what came after did!"
        mo "You see, Sada Abe took it upon herself to sever the penis of the man she loved more than anything else in the world and then carried it around for weeks afterward!"
        mo "Not all good things last forever, though. Abe was eventually sentenced and spent five years in prison."
        mo "If someone did something like that today, they’d likely spend much longer in jail. So don’t go cutting any penises off, kids!"

        scene amimalltwo8
        with dissolve

        "Molly proceeds to walk away from us without saying another word and disappears into some video game store."

        a "Well, that was weird."
        s "Yes, but I feel like we learned a valuable lesson."

        scene amimalltwo9
        with dissolve

        a "Did you really need an Irish girl to show up and tell you that cutting off penises is wrong?"
        s "Not that. The lesson we learned is cute girl magic is real and can also cause people to show up exactly when they’re needed."
        a "But...then the buses-"
        s "Never mind that, Ami. Let’s just start heading over to Le Vetefrenchwordstore and get your clothes off."

        scene amimalltwo10
        with dissolve

        a "Yeah! Stripping in a public dressing room with my [uncle]!"
        s "Please don’t yell things like that..."
    else:
        a "Okay, fine! But don't come crawling back to me when I find a {i}new{/i} client and I'm not willing to do your taxes anymore!"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene amimalltwo11
    with dissolve

    c "Ah! Sensei! I had no idea you were going to show up today!"
    s "Hey, Chika. It is for my safety and yours that I think you should only minimally acknowledge my existence today."
    c "Understood!"

    scene amimalltwo12
    with dissolve

    c "Hey, Ami! Out on a date with your [uncle] today?"
    s "It’s not a-"
    a "Yes. We are on a date. That is what is happening."
    c "Fun! Making him buy you something nice?"

    scene amimalltwo13
    with dissolve

    a "Actually...I was kind of hoping you still had some stuff from summer in stock."

    if bonus == True:
        s "She’s also using her own money. I would never force my [niece] to wear a swimsuit in the winter just for the fun of it."

        scene amimalltwo14
        with dissolve

        a "Why would you say something that suspicious when that isn’t even close to what’s actually happening?"
        c "Yeah, that just makes me think that’s a thing you {i}would{/i} do, Sensei."
        s "You know, I’m really not sure why I said that."
        s "Please continue minimally acknowledging my existence."
        c "...Okay."

    scene amimalltwo15
    with dissolve

    if bonus == True:
        c "Anyway, yeah. We’ve still got some summer stuff. It’s all on clearance right now too since no one’s buying swimsuits."
    else:
        c "Yeah. We’ve still got some summer stuff. It’s all on clearance right now too since no one’s buying swimsuits."

    c "So as long as you think you’ll be able to maintain your figure or...size until beach season rolls back around, buying one now is totally fine."

    if bonus == True:
        a "Oh, the last thing I’m worried about is growing out of it. That won’t be happening."

        "So much for holding out hope on becoming “sultry and sexy...”"
    else:
        a "I am fully grown and have a fast metabolism. This will allow me to remain the same exact size indefinitely."

    c "Cool! Then yeah, come to the back with me and I’ll show you where everything is."
    a "Great!"
    a "Oh, would you mind if Sensei came into the dressing room with me, though?"

    scene amimalltwo16
    with dissolve

    c "Uhh..."

    if bonus == True:
        s "Ami, why? Why would you say this?"
        a "What’s wrong, Sensei? We’re family. You’ve seen me in my underwear tons of times."
        a "Don’t tell me you’ve been looking at me strangely, have you?"

        "This fucking demon."

        c "I mean...there have definitely been dads who have helped their kid daughters in the dressing room before but..."

        scene amimalltwo17
        with dissolve

        a "Oh...I understand..."
        a "Sensei’s raised me since I was a little girl, but...since he isn’t technically related to me that way..."

        "{i}This fucking demon...{/i}"

        c "Wait, no! I didn’t mean it like that! It’s totally fine if that’s...what you need!"
        c "But it’s...kind of...definitely a little weird since he’s an adult and...you’re a [teenage]girl..."

        scene amimalltwo18
        with dissolve

        a "Yay! Thank you, Chika!"
        c "Uhh...yeah..."
        c "Just...probably don’t say anything about this to anybody else."

        scene black
        with dissolve

        "Chika leads Ami to the back of the store and directs her to a bin full of items that no one picked up during summer."
        "I’m sure they would have had a chance to sell if the seasons didn’t abruptly change, but that’s beside the point."
        "Ami grabs a few swimsuits, holding them up to her tiny body and closely judging whether or not she will embarrass herself by attempting to put them on."
        "Suffice it to say, most of the swimsuits wind up right back in the bin."
        "But, eventually, she finds a few she likes and heads into the dressing room."
        "I don’t follow right away because, even though Chika gave us permission, it still feels fucking weird."
        "But the second Chika is distracted by another customer, I seize the opportunity to join Ami and see what she looks like in a “less childish” bathing suit..."

        scene amimalltwo19
        with dissolve

        a "Finally..."

        "The answer: Still pretty childish."

        s "Yes, sorry for not being brazen enough to do the thing that one of your classmates said right to our faces is weird and socially unacceptable."
        a "Why do you always care so much about what is “socially acceptable?”"
        s "Ami, I am one of the last people who should ever be aligned with social acceptance."
        s "But when you’re an adult male in my position, you need to be a little careful when it comes to certain things."
        a "Like following your [niece] into a dressing room?"
        s "Like following my [niece] into a dressing room."
        s "You look really cute, though."

        scene amimalltwo20
        with dissolve

        a "Really?! I don’t look like I’m trying too hard?!"

        "I will never get over how convenient it is to just dodge difficult conversations by telling Ami she is cute."
        "If I had a dollar for every time I’ve taken advantage of that, I could probably buy her every single swimsuit in her cart right now."
        "Also, it definitely helps that I’m not even lying in telling her that."

        if ami_virgin == False:
            "In fact, if Chika wasn’t working right now, I’d probably even toy with the idea of taking things a little further with Ami for a few minutes."
            "Obviously, I’m not going to do that, though."
            "Because not only would that be socially unacceptable, I’m pretty sure having sex in the mall is entirely illegal."
            "And I refuse to live the rest of my alternate but also potentially not alternate (?) life in jail."
        else:
            "Sure, I {i}try{/i} not to view Ami in a sexual light because of...reasons. But it’s absolutely undeniable that she appeals to me in a multitude of ways."
            "There are just certain things you should always be able to say no to, though."
            "I just wish those things weren’t so hard all of the time."

        scene amimalltwo21
        with dissolve

        a "Um...I’ll probably just wind up buying this one, then..."
        s "Did you even try the other ones on yet?"
        a "Yeah. I tried a few of the other ones while you were waiting outside, but this is the one I thought looked the best."
        a "And having you call me cute is...kind of all the validation I need anyway."
        s "I mean, I always think you’re cute, so my word should probably be taken with a grain of salt."

        scene amimalltwo22
        with dissolve

        a "And...And the ponytail? Is that good too?"
        a "My hair goes all over the place in the water and having it bundled up in one tail instead of two might not {i}look{/i} as good, but-"
        s "It looks great."

        scene amimalltwo23
        with dissolve

        a "Okay...then yeah...I’m gonna get this one..."
        s "What’s with you acting all bashful all of a sudden?"
        s "Like five minutes ago, you were manipulating Chika into just letting me in here."
        s "What’s going on?"

        if ami_virgin == True:
            scene amimalltwo24
            with dissolve

            a "Just...feeling a little strange now that you’re in here is all."
            a "Trying to make sure I don’t say or do anything that might get us in trouble."
            s "…"
            a "…"
            s "You know, there was a thing out there I kind of wanted to check out."
            a "That’s fine...I’ll...start putting my normal clothes back on now and we can head out..."

        else:
            scene amimalltwo25
            with dissolve

            a "I wasn’t horny five minutes ago..."
            s "Why are you always getting horny in inconvenient locations?"
            a "Why are you always making me horny in inconvenient locations?"
            s "I have done literally nothing. You need to learn self-control."
            a "{i}I{/i} need to learn self-control? You have sex with your [niece]."
            a "Not that I think that's a problem or anything, obviously."
            s "Okay, we could {i}both{/i} do with learning a little self control. But you are the culprit here and I am an innocent man trying to not sully the workplace of one of your peers."
            a "We can’t even sully it a little bit?"
            s "No, Ami."
            a "Not even hand stuff?"

            scene black
            with dissolve

            a "Wait, Sensei!"
            s "If I stay in there any longer, there will be no turning back."
            a "I don’t wanna turn back! I want you!"

        "I step into the front room again and wait for Ami to finish changing back into her normal clothes."
        "Chika is still stuck tending to the same customer as before, so I don’t have to awkwardly talk about “how things were in there” or whatever it was that she was definitely going to ask me."
        "Ami returns a few minutes later with her new swimsuit in her hands and ultimately winds up getting rung up by one of the other employees."
        "Neither of us say goodbye to Chika, but it’s not like we really had a chance to anyway."
    else:
        s "I would mind. That is not something I have any interest in doing. I just wanted to reward you and make sure you are adequately dressed for the beach."
        a "Oh, I apologize for misunderstanding. Please wait out here, if that is the case."
        s "I will do just that."

        scene black
        with dissolve

    if ami_virgin == True:
        scene black
        with dissolve2

        "Eventually, we board the bus and start heading home."
        "Ami brings up the prospect of the two of us going out to eat or something along those lines, but I refuse as there is something else I want to do with my day instead."
        "Thankfully, we manage to get back into town shortly before nightfall and the two of us wind up amicably parting ways."
        "It wasn’t the most exciting or action packed of days I’ve spent with Ami, but it was still a fun one regardless."
        "Plus, she even got a new swimsuit out of it."

        if bonus == True:
            "And I’m excited for not only that, but the prospect of everyone else who decides to buy swimsuits prior to our next trip to the beach...whenever that may be."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amidate35 = True
        $ amidorm40miss = True
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdaynight


    else:
        "Eventually, we board a bus and start heading home, but Ami decides that the day is not yet complete and that she wants to go out to eat with me."
        "I refuse at first but completely cave once she informs me that she’ll be paying for this as well."
        "Listening to her happily hum the tune to one of Niki’s songs as it plays on the radio, I close my eyes and wait for whatever stop we're supposed to get off at to approach."
        "………"
        "……"
        "…"

        scene amimalltwo26
        with dissolve

        s "You know, you should probably eat more than just french fries, Ami."
        a "But I love french fries."
        a "And I bought them with my own money, so it’s not like you can even say something like “Bahhh you’ll eat right under my roof!”"
        a "Also, this isn’t even your roof. Back off of my french fries."
        s "I was...unaware that you felt so strongly about them."

        scene amimalltwo27
        with dissolve

        a "Did you have fun today, Sensei?"
        a "I know it wasn’t like an {i}actual{/i} date since we’re always spending time together and stuff...but I really like getting to do things like this with you."

        if bonus == True:
            a "You know...being out in public. Trying on clothes for you. Eating stuff together."
            a "It’s kind of like we’re in a real relationship. Or at least what I imagine a real relationship feels like."
            s "I guess it does kind of feel like a relationship when you put it that way."
        else:
            s "It made me feel like a little boy again."

        scene amimalltwo28
        with dissolve

        a "Right?! And wasn’t it lots of fun?!"
        s "Sure. It was a lot of fun. I won’t deny that."

        scene amimalltwo29
        with dissolve

        if bonus == True:
            a "Then make it official and start dating me for real."
            s "..."
            a "...?"
            s "You know I can’t do that."
            a "Why not?"
            s "Do you really need to ask? There are hundreds of reasons."
            a "And there are hundreds of reasons you {i}should{/i} do it."
            a "If you’re worried about everyone thinking it’s weird because we’re related, I don’t think you have to."
            a "Sure, people will probably think it’s weird {i}at first,{/i} but once they see how happy we are, I’m sure they’ll be fine with it."
            s "You think just seeing two people happy together is enough to support them?"
            a "Sure? Why not."
            s "So if I started dating someone else and looked happy with them, you’d support it?"

            scene amimalltwo30
            with dissolve

            a "Nope!"
            s "See what I mean?"
            a "Nope! Cause I also know you can’t be happy with anyone else."
            a "You and me are gonna be together forever cause that’s how things are meant to be."
            a "And we’re gonna buy tons more bathing suits and eat tons more french fries because we both think those things are fun and we love each other very, very much."

            scene amimalltwo31
            with dissolve

            a "And if anyone ever tries to ruin that, I will do horrible things to them."
            s "You do realize that if “anyone tries to ruin that” it will be me, right?"
            a "You want to ruin me? Your adorable [niece]? Who cooks you breakfast every morning and lets you cum on her face?"
            s "I don’t know what I want. But I know that a relationship isn’t anywhere near the top of the list."
            a "But it will be one day, right?"
            s "I have no idea."
            a "It will be one day."
            s "Ami-"
            a "It will be one day."
            s "…"
            a "…"
        else:
            a "Did you just tell me I looked fat?"
            s "What? No?"
            a "Is it because of the french fries?"
            s "You can eat as many french fries as you want. You deserve them."
            a "I'm watching you, Sensei."
            a "{i}I'm watching you.{/i}"

        "I want to say something like “the restaurant goes quiet and an uncomfortable silence finds its way between us,” but Niki is on the radio in here as well."
        "It’s like her voice has been following me all fucking day."
        "Like it’s just seeping into my ears and criticizing me for going on a date with my [niece] and not pushing her away the same way I would with anyone else."
        "For not telling her that “It {i}won’t{/i} be one day.”"
        "And for being afraid to steal away her smile just because I know why it looks the way it does- held together by Scotch tape and glue."

        a "Do you want a french fry? They’re extra salty today."
        s "French fries only exist when they’re extra salty. Any other time they’re just-"
        a "Rectangular potato strings. I know. Do you want one or not?"
        s "…"
        s "Fine."

        scene black
        with dissolve

        "I take the fry from Ami."
        "And then ten more."
        "And then an entire order because apparently she knew I was going to do this."

        if bonus == True:
            "I might not want a relationship with her-"
            "But my god, would it be easy to have one."

        $ renpy.end_replay()
        $ ami_love += 1
        $ amidate35 = True
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amilust15:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label callamiafternoon:
    if ami_love >= 35 and amimaid30 == True and shrine35 == True and amidate35 == False:
        jump amidate35
...
```