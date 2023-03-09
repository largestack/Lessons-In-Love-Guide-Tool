# Milk, Eggs, and Water
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day89&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 89

✅Event "[Main: Girl-Talk](./day65.md)" is completed (event=day65)



## Next events
* [Haruka: Drunk Again](./harukadate1.md)

## Event properties
* ID: day89
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day89:
    scene harukastore0
    with dissolve
    play music "justbehappy.mp3" fadein 4.0

    s "Milk...eggs...water..."
    s "Wait, what does she need me to {i}buy{/i} water for? Can’t she just use the tap?"

    "I’m on my way home from[school] and-"
    "Actually, let me correct that."
    "I {i}was{/i} on my way home from[school]...but then Ami decided to text me a list of things I apparently need to pick up on the way home."
    "They’re all relatively simple ingredients, so it’s not like it’s a hassle or anything, but..."
    "Well, let's just say that I wanted to use my night for something other than just running errands."

    s "..."

    "She won't mind if I'm a little late, right?"
    "Maybe I can hang around here for a little while before heading back?"
    "It’s not often that I’m in this part of town, so...I doubt there's any harm in me checking out a few extra shops or something."
    "Worse comes to worst, I can always just tell Ami I got lost."

    scene black
    with dissolve2

    "I cross the street and immediately find a small cafe I've never seen before."
    "Without putting any thought into it, I push open the doors and wander inside- hoping to find a beautiful girl that is at least slightly open to the idea of having sex with me."

    scene harukastore1
    with dissolve

    "And I wind up finding Haruka."
    "Cool."

    h "Ah..."
    s "Oh, hey. What are you doing here?"
    h "..."
    s "Haruka?"

    scene harukastore2
    with dissolve

    h "Yeah, hey! Sorry, I just...wasn't expecting to see you out of nowhere."
    h "I'm just dropping by to grab some dinner for tonight, but..."
    h "I actually left my wallet at home..."
    h "So...now I am about to {i}postpone{/i} dinner and...go get that."
    oldl "Haru-chan, you don’t need to go home, dear. You’re here every day."
    oldl "Let this one be on us. The least we can do to pay you back is give you a free meal every once in a while..."

    "An old woman, presumably the store owner, calls out to Haruka from behind the counter."

    scene harukastore3
    with dissolve

    h "What? No! I couldn’t do something like that to you!"
    h "You remember I run a cafe as well, right? I know what it's like to miss out on a sale because of forgetful people like this."
    h "Just...give me like half an hour and I'll be right back. I promise."
    s "You live around here, Haruka?"

    scene harukastore4
    with dissolve

    h "Right around the corner, actually."
    h "I used to stop by this place every day with my-"
    h "My..."

    scene harukastore5
    with dissolve

    h "My {i}friend.{/i}"
    s "..."
    h "My...uhh..."
    h "My friend and I would come here all the time and...meet up for dinner and stuff."

    scene harukastore2
    with dissolve

    h "But...enough about me! Do you live around here as well?"
    h "I’ve only seen you at the cafe and...the bistro that one time- so I have no idea if you’re local or not."
    s "I don't really live around here, no. Just...passing by while running some errands."
    s "It's no big deal, though. I'll probably just wind up taking the bus home anyway."

    scene harukastore6
    with dissolve

    h "You don’t have a car?"
    s "Is that surprising?"

    scene harukastore7
    with dissolve

    h "What? No, I...I didn’t mean anything bad by it, I swear. I mean, it's not like you even really {i}need{/i} one in Kumon-mi."
    h "I can always give you a ride home if you want, though."

    scene harukastore2
    with dissolve

    h "Only thing is we’d need to head back over to my place first since I didn't drive here."
    h "Plus, I'd also like to come back and pick up dinner once I can actually, like...you know. Pay for it."
    s "Are you sure? I wouldn’t want to burden you."

    scene harukastore4
    with dissolve

    h "Dude, it’s totally fine. I don’t mind at all. In fact, I welcome the company. I just cleaned my living room and no one's been around to be impressed by how nice it looks."
    s "Do you not have people over very often?"

    scene harukastore8
    with dissolve

    h "No one other than the same two people who have been coming around for years now."
    h "Apart from them, it's probably been...three or four years since anyone else came over?"
    s "Wow."
    h "I am incredibly lonely. Please comfort me by blessing me with your presence."

    scene harukastore9
    with dissolve

    h "Platonically, of course. I promise I’m not hitting on you."

    scene harukastore10
    with dissolve

    h "{i}Unless...{/i}"

    scene harukastore10r
    with dissolve

    h "Wait? What? No. Don't be awkward, Haruka. Just be yourself."
    s "I...don’t really know how to interpret this exchange, but if you’re that determined to have me over, I’ve got no problems at all."
    s "I can’t stay that long, though. My [niece] is expecting me with groceries."

    scene harukastore6
    with dissolve

    h "Wait, you live with your [niece]? I had no idea."

    if bonus == True:
        s "Of course you had no idea. We’ve only had like two real conversations since we’ve met."
    else:
        s "That sort of thing is common in Kumon-mi from what I understand."
        h "I should probably brush up on my knowledge of the city since I live here and stuff."
        s "I would be willing to help you. We have only had a handful of conversations since we've met and are missing out on valuable time to educate ourselves."

    h "Yeah, but that’s {i}your{/i} fault. It’s not like you don’t have my number."
    s "And pretty soon, I’ll have your address as well."

    scene harukastore10r2
    with dissolve

    h "…"
    s "I’m sorry. That sounded a lot creepier than I wanted it to."
    h "I don't know, man. I might be having second thoughts about this now that I know there's a chance for you to stalk me."

    scene harukastore10r3
    with dissolve

    h "But at the same time...it's not like being stalked would be {i}that{/i} bad, would it?..."
    s "Uhh..."

    scene harukastore2
    with dissolve

    h "Well, uhh...either way, we should probably get a move on if I don't want my dinner to be ice cold by the time I pick it up."
    s "Sure. I felt weird just standing around without ordering anything anyway."
    h "Great. It’s not far, I promise. We'll be there in like...fifteen minutes tops."

    scene black
    with dissolve2

    "Haruka and I walk through her neighborhood together, chatting about various cafe-related things to help kill time along the way."
    "For someone who is apparently extremely lonely, she’s surprisingly good at holding a conversation."
    "I don't know if I'm only thinking this due to association, but she's kind of like a...more mature version of Rin in a way."
    "I’m sure all the time she's spent in customer service helps with being able to talk to people, but it’s still surprising getting wrapped up in a conversation this...easy."
    "Who knows? Maybe she and I just have the type of personalities that bounce well off of one another."
    "And maybe the natural progression of these first stages of friendship will start feeling a little {i}less{/i} natural once she starts letting her guard down."
    "........."
    "......"
    "..."

    scene harukastore11
    with dissolve

    h "Welp, here we are!"
    h "Congratulations on being the first man here in God knows how long."
    s "Thanks for having me. Also, {i}wow- what a clean living room.{/i}"
    h "Thanks for humoring me. I don't get those sorts of casual compliments from Sara."
    h "Any time she's here, she just goes straight for the wine and it's...off to the races."
    s "Well, Sara is an alcoholic and I am not. Comparing the two of us doesn't really work all that well."

    scene harukastore12
    with dissolve

    h "Ehh...I don't really know if I'd say {i}that.{/i}"
    h "Sara might have a drinking problem, but you guys are actually pretty similar in a bunch of ways."
    s "What sort of ways are you referring to?"
    h "That's..."
    h "I don't know. It's kind of hard to talk about without making it sound like I'm both judging you and dishing out details about her that she probably wants to be kept secret for now."
    s "Well, that's not ominous at all."

    scene harukastore12r
    with dissolve

    h "S-Since we're on the topic of her, though...there's..."
    h "Well, there's something I've been kind of wondering."
    h "And if this is too personal or whatever, you can just tell me to mind my own business."
    s "I think I see where this is going, but shoot. What do you want to know?"

    if sarasex == True:
        if bonus == True:
            scene harukastore12
            with dissolve

            h "Well, uhh..."
            h "I know you guys have been...you know...{i}intimate{/i} with each other..."
            h "But like...are you guys officially a thing? Or just...kinda messing around?"
        else:
            h "Well, uhh...I know you guys have...you know...hugged..."
            h "But like...is it serious hugging? Or...not serious hugging?..."

        scene harukastore13
        with dissolve

        h "N-Not like there’s anything wrong with either of those! Like...you’re obviously both consenting adults who seem to like each other and..."

        scene harukastore14
        with dissolve

        if bonus == True:
            h "And Sara is certainly very up front about her...{i}needs.{/i}"
        else:
            h "I definitely know that hugs aren't really a thing to get all AHHHHHHHHHHHHHHHHHH about, but..."

        h "I guess I'm just kind of curious. That's all."
        s "I see..."

        scene harukastore15
        with dissolve

        h "I'm sorry. That was weird to ask, wasn't it?"
        s "A little, yeah. But I don't really mind."
        s "The thing is, when it comes to Sara..."

    else:
        h "Well, uhh...I know you guys hang out sometimes, but like..."
        h "I also know how Sara is."
        s "How she is? What do you mean by that?"

        scene harukastore16
        with dissolve

        h "She...just...kinda really likes attention."
        h "Like {i}really{/i} likes it..."
        h "Which isn't me talking shit or anything. She has the same needs all of us have."
        h "And since you're the first guy that's been in her life for like, years-"
        s "I get what you're saying. And I don't know if I should be saying this or not, but she already tried having sex with me once."

        scene harukastore16r
        with dissolve

        h "And you...turned her down? But she's so hot."
        s "She is. But her daughter was also like, two rooms away."
        h "That..."
        h "Kinda makes it even hotter though..."
        s "..."
        h "Can we pretend I didn't just say that? Because {i}I'm{/i} going to pretend I didn't just say that."
        s "I don't know if I should tell her what you just said or not."
        h "Please don't. That was supposed to be an internal thought. It just...got out on accident."
        s "Yeah...I can relate to that."
        h "So...was it just the thing with her daughter that held you back? Or...do you have like...other reasons?"
        s "Well..."
        s "When it comes to Sara-"

    menu:
        "I’m interested in her":

            $ sarainterest = True

            if bonus == True:
                s "I guess I {i}am{/i} kind of interested in her. She seems like a really nice girl...just very horny."
                s "Not like there’s any problem with that. In fact, I-"
            else:
                s "I am interested in her, but on a sheerly platonic level in which the two of us will occasionally hug, but mostly just try to help Sana with her school work."

            scene harukastore17
            with dissolve

            h "I’m...gonna stop you right there."

            if sarasex == True:
                if bonus == True:
                    h "I’ve already heard things from her that I can’t unhear."
                    s "Oh? What is that supposed to mean?"
                    h "I...am going to keep my comments to myself for right now."
                    h "But if any of it is true...I am both very impressed and extremely jealous. But I would also like you to forget that I just said that."
                    s "I don't know if I can."
                else:
                    h "I don't want to hear any more about hugging than I've already heard."
                    s "If that sentence gave you the impression that I am trying to hug her daughter, I would like to make it known now that I am not."

            else:
                h "I don’t want to hear wherever this is going."
                s "Really? Not even a little?"
                h "No way, Jose."

        "I’m not interested in her":

            $ sarainterest = False

            s "I don’t really see Sara that way. At least...not right now."
            s "She’s definitely hot, but...I just can’t really imagine how her daughter would feel if she found out."

            scene harukastore16
            with dissolve

            h "Oh my God, you’re totally right. I didn't even think about that."
            h "That would be like, super weird for her, wouldn’t it? If my high school teacher was banging my mom, I don't even know what I would have done."
            s "Exactly. So I think it would probably be for the best right now if Sara and I just...stay the way we are."
            h "That takes some serious willpower, dude. Sara’s hot as hell. She was really popular back in [high_school] too."
            h "But...I guess that’s really all I can tell you about that. The rest will have to come from her."

    scene harukastore11
    with dissolve

    h "But anyway, I guess that pretty much answers my question. I was just wondering if you guys were like, exclusive or not."
    s "Gotcha. Yeah, we’re definitely not {i}exclusive.{/i} So if you're trying to flirt with me right now, please be advised that I am 100%% single."

    scene harukastore19
    with dissolve

    h "Oh yeah? Your [niece] wouldn’t get mad if you brought a girlfriend over?"

    if bonus == True:
        s "Well...bringing you over would be a completely different story."
        h "I’m sure it would be. Us girls can be super protective, you know?"
    else:
        s "Woah, chill. I feel like telling you I was single may have given you the wrong idea."
        s "The only reason I am single is because I am in a committed relationship with our Father in Heaven. And my mission here is help everyone be happier and...know more things."
        h "Hey, you're not the only one who knows things, Sensei."

    scene harukastore20
    with dissolve

    h "In fact, this one time-"
    h "…"
    s "…"
    h "…"
    s "…"
    h "…"
    s "…"

    stop music
    scene harukastore21

    h "Hah-"
    s "…"
    h "…"
    s "…"
    h "…"
    s "…"
    h "…"

    scene harukastore22
    with dissolve

    h "{size=-15}I’ll be right back.{/size}"

    scene harukastore23
    with dissolve
    play sound "dooropen.mp3"

    s "…"
    s "…"
    s "…"
    s "…"
    s "…"

    scene black

    "The people we love go away sometimes, don’t they?"

    play sound "static.mp3"
    scene happyharuka1 with flash
    scene happyharuka2 with flash
    scene happyharuka1 with flash
    scene happyharuka3 with flash
    scene happyharuka1 with flash
    scene happyharuka4 with flash
    scene happyharuka5 with flash
    scene happyharuka6 with flash
    scene happyharuka5 with flash
    scene happyharuka7 with flash
    scene harukastore20 with flash
    stop sound
    play music "justbehappy.mp3"

    h "I’m back!"

    if bonus == True:
        h "Sorry about that."
        h "I’m not really sure what came over me right there."
        s "Great. I’m glad you’re okay now."
        h "Yup!"
        h "So, where were we?"
        s "{s}Do you miss him?{/s} I think you were trying to flirt with me."
        h "Was I? That doesn’t sound very much like me. Are you sure?"
        s "{s}Tell me about the things you feel.{/s} Pretty sure. I guess I could be wrong, though."
        h "Hmm...I think you are! I’m not really one for flirting, so..."
        s "{s}Do you long to be touched once more?{/s} Well, if you ever change your mind..."
        h "If I ever change my mind, {i}what?{/i}"
        s "{s}I will defile the body that once belonged to him.{/s} I guess we’ll have to find out, won’t we?"

        scene harukastore19
        with dissolve

        h "Hmm..."
        h "I guess we will."

        scene black
        with dissolve2

    if bonus == False:
        scene black
        stop music

        h "Just kidding!"

    "Haruka drove me home shortly after that."
    "Ami yelled at me for forgetting to buy milk, eggs, and water."
    "All in all, it was a pretty normal day."

    $ renpy.end_replay()
    $ day89 = True
    stop music fadeout 4.0

    "………"
    "……"
    "…"

    if bonus == True:
        "{i}Haruka went home and furiously [masturbate]d.{/i}"

    "{i}Everyone lived happily ever after.{/i}"

    jump endofweekday

label day91:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
$ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
    if totaldays >= 89 and day65 == True and day89 == False:
        jump day89
...
```