# Girls in Spandex (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 400

* Event [All is Bright. All is Beautiful.](./secondbeach18.md) (Main) is completed)

* Event [The Happiest Girl in the World](./rindate50.md) (Rin) is completed)

* Event [Lifejacket](./rindorm50special.md) (Rin) is completed)

* rinbetrayed equal to True (unknown variable)

* Event [Things Like Stairs](./ramen30.md) (Tsuneyo) is completed)

* Event [Walkthrough](./mollydorm30.md) (Molly) is completed)

* Event [Hotel Rooms](./nikidate15.md) (Niki) is completed)

* Day of week is Friday



## Next events

None

## Event properties

* Id: halloweentwo1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->halloweentwo1

## Official wiki page

[Girls in Spandex](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo1&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo1:
    scene secondhalloweenintro1
    with fade
    play music "phantomthief.mp3"

    "Well, it’s the end of my day and I’m alone in my office...which probably means something interesting is about to happen."
    "Sure, there have been plenty of days where that hasn’t been the case, but since I’ve already begun inner-monologuing, I think it’s safe to assume today isn’t one of those days."
    "The only question now is {i}who{/i} is going to show up and {i}what{/i} they’re going to want from me."
    "The beach trip is over and done with. Some hearts have been broken (One, to be specific) and others renewed. (Again- one, to be specific.)"

    if bonus == True:
        "I’ve even partially fixed my connection with my idol ex-girlfriend who, unbeknownst to her hordes of raging fans, is actually a shirt-stealing, half-nerdy pervert who excels at tongue wrestling."
        "In fact, now that I think about it, I could probably quit teaching and publish a wordy exposé about her and just live off the money that makes for the rest of my life."
        "But, then again, that would negatively impact the probability of me having sex with her in the future, so it might not be the best idea."
    else:
        "So, the only thing left to do is get to work on my exposé that ousts Niki Nakayama as a shirt-stealing jerkburger."
        "Will it put my educational career at risk? Maybe. But it is my duty to protect Kumon-mi from losing any more clothing to her manipulation tactics."
        "I will accept whatever repercussions may come as a result of this takedown article. The world will know my name soon, enough- which I have also yet to uncover myself for some strange reason."

    s "…"

    "{i}Unless I can think of a pseudonym.{/i}"

    play sound "knock.mp3"

    sa "Um...Sensei? Are you...free right now?"
    s "Hm? Oh. Yeah."
    s "Come on in, Sana."

    scene secondhalloweenintro2
    with dissolve
    play sound "dooropen.mp3"

    sa "Sorry for the sudden intrusion..."
    s "It’s fine. I was just trying to think up a pseudonym to use for an upcoming takedown article of a beloved public figure."
    s "Do you have any ideas?"

    scene secondhalloweenintro3
    with dissolve

    sa "You’re...going to take someone down?"
    s "Maybe. I was going to put a little more thought into it, but it appears the time has come to get roped into yet another fun misadventure with you and...whoever else is involved."
    sa "Misadventure?"
    s "That’s why you’re here, isn’t it? To tell me about some sort of special event that will proceed to consume the rest of my day- possibly even more?"

    scene secondhalloweenintro4
    with dissolve

    sa "I’m...actually here to remind you about tonight’s Halloween party at Ayane’s house..."

    "I look down at my phone to confirm the date and it appears that my hunch was spot on."
    "It only makes sense that the Halloween party would be today considering...well, the fact that it’s Halloween."
    "But I’m not really one to keep track of specific dates."
    "To me, life is just a series of the same seven days over and over and over again, and it’s up to everyone else to remind me of which days are decidedly more significant than others. "
    "It’s strange that Sana had to be the one to tell me about it, though. Normally, this would be a job for Ami or Ayane or something."

    s "Well, your reminder has been received. Now what?"

    scene secondhalloweenintro5
    with dissolve

    sa "I think...now, I’m supposed to take you over to the manga club..."
    s "Ahh, yes. What better person to take me to the manga club than someone who is not in the manga club?"
    sa "Well...I would normally agree, but...all of the other girls are already in their costumes and...didn’t want to walk through the halls like that..."
    sa "And...they needed your help deciding which one...looks the nicest."
    s "Ahh. Well, yes. That is certainly a job only {i}I{/i} can do."
    s "Why aren’t you dressed up, though? Don’t you want to be in this contest too?"

    if sanafashion == True:
        s "I already have a proven history of choosing you to win fashion shows, so..."

    scene secondhalloweenintro6
    with dissolve

    sa "N-No! That’s...okay..."
    sa "I don’t...even know what I’m going to be yet..."
    s "What? The party is tonight, though, isn’t it?"
    sa "I...figured I’d just...go through some of my mom’s old clothes and stuff..."
    sa "I’m...not very good at choosing Halloween costumes..."

    if bonus == True:
        s "But the sex dolphin was great."
    else:
        s "But the dolphin suited you so much."

    scene secondhalloweenintro7
    with dissolve

    if bonus == True:
        sa "I-It wasn’t a sex dolphin!"
        sa "S-S-Sex dolphins aren’t even real!"
        s "Tell that to Sexy Land, Sana."
    else:
        sa "How?! What does that mean?!"
        s "Oh, you know. Just Sexy Land stuff."

    scene secondhalloweenintro8
    with dissolve

    sa "I’m...still trying to forget about Sexy Land..."

    scene black
    with dissolve2
    stop music fadeout 30.0

    "I get off of my chair, accepting that I likely won’t have to actually {i}counsel{/i} anyone today on account of the whole party thing, and let Sana lead the way out."
    "I think along the way that it’s strange how I’m letting her lead {i}anything{/i}, but I guess with how much she’s been growing lately, it only makes sense."

    if bonus == True:
        "I mean, it’s not like she’s pushing me up against the lockers and grabbing my crotch. She’s literally just walking me down the hall."
        "But even that much is a big deal for her when she could barely even hold a conversation with me back at the start of everything."
    else:
        "As her teacher and nothing else, I am so proud of how far she's come."

    s "…"
    sa "Sensei? You’ve been quiet..."
    s "Sorry. Just getting nostalgic."
    s "I’m proud of you, Sana."
    sa "Uhh...for...what, exactly?"

    if bonus == True:
        s "Nothing. I’m ready to be pushed up against the lockers whenever you are."
        sa "Oh...uhh..."
        sa "What?..."
    else:
        s "For everything."
        s "If I ever develop an immortality potion, you will be one of the first ten people to receive it."
        sa "..."
        sa "Thank...you?..."

    "………"
    "……"
    "…"

    scene secondhalloweenintro9
    with dissolve2
    play music "shiningstarinstrumental.mp3"

    "I make my way into the manga club room to be immediately swarmed by a group of[school] girls in spandex."
    "Nice."
    "Sana, not wanting to be involved in this at all apart from her assistance in guiding me here, takes a seat in the corner of the room and begins playing some sort of game on her phone."

    mo "Why hello, traveler. I see that fate hath been kind enough to coordinate this ever-welcome crossing of our paths."
    s "Hi, Molly. And hello to everyone who is actually human."
    s "What great costumes that I am definitely just seeing now for the first time."
    f "That...makes it sound like you’ve somehow seen them before?..."
    mo "Impossible, for this wanderer has not only no vision, but no {i}sight{/i} as well."
    s "Are those...not the same thing?"

    scene secondhalloweenintro10
    with dissolve

    mo "Nay, traveler. Sight is a power granted to only those worthy of bearing the Auge der Verurteilung."
    mo "‘Tis such a blessing that allows me, the Prinzessin der Verurteilung, to protect thee from harm as you tread lightly throughout this realm and dominion!"
    s "Cool."
    a "Sana told you about the party, right?"
    s "Yeah. And I want to say it came out of nowhere, but that’s probably on me and not something I can really hold against any of you."
    ay "Sensei! Aren’t you glad I decided to wear something that isn’t a full suit of armor this year?"
    ay "As much as I liked my last costume, I wound up feeling really lonely when you were looking at everyone other than me all night."

    scene secondhalloweenintro11
    with dissolve

    a "Hey, Ayane. Remember that “joke” I made about how letting you dress up as Lumine should mean that you have to keep your mouth shut for the entire night?"
    ay "Yup! It was hilarious, Ami. Especially because I know you love me and would {i}never{/i} want me to keep my mouth shut for that long."
    a "Are you sure about that?"
    r "Sup, homie! You confused walking into a room with a bunch of girls dressed in weird fantasy costume things?"

    if rinbetrayed == True:
        s "I'm more confused about why you're suddenly back to-"
        r "Dressing up? Why, because it's Halloween, of course!"
        s "I mean...I'm not against it. I just figured you might be sitting this one out on account of-"
        r "Getting too old for this sort of thing? Nope! Still fun!"
        r "Everything's totally normal and I have no idea what you're talking about."
        s "..."
        r "..."

        "Well...I guess Rin is better now?"

        f "Um...anyway...I think Molly wanted to get your thoughts on how all of us look since...she’s the one who made all of the adjustments to our outfits."
    else:
        s "Yes. But that doesn’t mean I’m any less excited to be here."
        f "I think...Molly wanted to get your thoughts on how all of us look since...she’s the one who made all of the adjustments to our outfits."

    s "Just the adjustments? She didn’t make the whole costumes this time?"

    scene secondhalloweenintro12
    with dissolve

    mo "Just who do you think I am, Sir? Even someone as adept with a sewing machine as I could not hope to accomplish such a task without an extraordinary amount of both supplies and time."
    s "Well, it certainly seemed like you had enough time to memorize all of those weird German sounding words."
    mo "Fair point. I accept defeat and will work harder in the future."
    r "Sensei, you’re coming to the party again this year, right?"
    s "Of course. Why wouldn’t I?"
    r "I don’t know man. Didn’t you just find out about it? What if you, like...have other friends now?"
    a "Sensei doesn’t need other friends when he has us."
    s "As you can see, Rin, my [niece] won’t let me do anything else."
    f "Well, um...we’re happy to have you again..."
    f "So if you...wanted to leave the room {i}without{/i} choosing which one of us is the cutest...I’m sure that would be fine..."

    scene secondhalloweenintro13
    with dissolve

    r "Dude, just do the thing I told you and you’ll win for sure."
    f "I...don’t know about that, Rin..."
    mo "Sensei, I {i}do{/i} hope you know that you’re not porting out of this realm until you choose a winner."
    s "As much as I’d love to, aren’t you guys missing someone?"
    s "I remember there being a sixth person in the picture that I {i}totally did not see{/i}."
    a "Well that’s certainly not suspicious or anything."
    ay "I believe Sensei wholeheartedly because I love him and he would never lie."
    mo "Sir, if you are referring to Maya, she is hiding in the corner of the room."
    m "Ugh. Great."

    scene secondhalloweenintro14
    with fade

    s "Well, hello there."

    if bonus == True:
        m "Are you attempting to sound predatory on purpose or is that just a convenient coincidence?"
        s "A little of both, probably."
        s "You’re cute when you’re not dressing up as me for Halloween."
        m "I’m aware. I don’t need you to remind me of this."
        s "That’s fine. But I’m going to remind you anyway and no one can get mad at me because that is the actual purpose I was brought to this room for."
        m "Hooray."
    else:
        m "Hello."
        s "You sure look spiffy, Maya."
        m "Thanks. You look pretty spiffy yourself."
        m "Would be a real shame if the two of us were to trip into each other and have our lips touch or something."

    a "Okay! So, to prevent Sensei from flirting with Maya anymore, how about we finally get to our contest thingy?!"

    scene secondhalloweenintro9
    with fade

    s "Fine by me."
    s "Is there anything I have to know about judging or am I literally just picking the person I think looks the best?"
    mo "Just whoever you think looks the best, Sir."

    if bonus == True:
        mo "Choices like this are a staple in h-games and can typically have much bigger consequences than you’d expect!"
    else:
        mo "Choices like this are a staple in dating sims and can typically have much bigger consequences than you’d expect!"

    r "Or no consequences at all! The fun is in not knowing if what you did was right or wrong until it’s too late to change anything!"
    s "So basically, what you’re saying is that the pressure is on."
    mo "Exactly, Sir. But don’t fret!"
    ay "I’ll love you no matter who you pick, Sensei."
    a "So will I. But you better pick me anyway."
    r "I vote for Futaba because boobs."
    f "I’ll...vote for Rin because she voted for me."

    scene secondhalloweenintro15
    with dissolve

    mo "Sana! Lights, please!"
    sa "What? I...have a job?..."
    mo "Of course! We need the room lights to go off before turning the spotlight on to make us all look cooler and more...awesome and stuff."
    sa "But...I don’t even know where-"
    sa "Wait...is this it?"

    play sound "lightswitch.mp3"
    scene secondhalloweenintro16
    with dissolve

    mo "No. That’s the red accent light. It turns down all of the other colors and just makes the reds more visible and stuff."
    a "I accept this light."
    ay "It’s the one right next to that one, Sana."
    sa "The one right...oh! This!"

    play sound "lightswitch.mp3"
    scene secondhalloweenintro17

    mo "Yeah! There we go!"
    mo "Places, everyone!"

    scene black
    with dissolve2

    "The girls begin to line up in single file fashion as if this is something they’ve already rehearsed."
    "Which, now that I think about it, isn’t really something I’d put past them if Ami, Ayane, and Molly are involved."
    "Which isn’t to say that Molly puts me on the same pedestal as the other two. But she seems to like large scale contests like this."

    if bonus == True:
        "And the validation she’ll receive in knowing how attracted I am to all of the costumes she assisted in tailoring (To an unknown extent) may offset some of her newfound misery."
        "But hey, I don’t really have the time to be caring about the sadness of others right now when I have an entire room of [teenager]s seeking validation."
        "Let the contest commence."
    else:
        "And the validation she’ll receive in knowing how impressed I am with her artisanal craftsmaship is sure to brighten up her afternoon."
        "Which is great! She could really use the pick-me-up right now based on all of the sadness she's had to deal with lately."

    scene secondhalloweenintro18
    with dissolve

    mo "First up is Sensei’s very own [niece] and the first thing he sees every morning, Ami Arakawa- cosplaying the fiery, yet lovable...Outrider Amber of the Knights of Favonius!"
    a "Um...okay, it feels kind of weird being judged like this now. This is nothing like the rehearsals at all."
    mo "Nonsense, Ami! Just do what you do best and stand there absorbing your [uncle]’s lascivious gaze!"

    if bonus == False:
        s "It is not {i}lascivious{/i}. This is a look of pride and admiration and a little jealousy because I kind of want to wear that costume."

    m "You’re disgusting."
    s "Me or Molly? Because I didn’t do anything."
    m "Both of you."

    scene secondhalloweenintro19
    with fade

    mo "Next up is the lovely and humble astrologist Mona Megistus, cosplayed by Maya Makinami! So many M’s!"
    s "Astrologist?"
    m "Don’t misconstrue this as me believing in astrology. Frankly, I think it’s a big joke and think even the term “pseudoscience” is too kind in describing it."
    m "However, astrology functions differently in the game than it does in real life and I see the character as just some other girl with nice legs who also likes stars."
    s "Well, it looks really good on you."
    m "Thanks. Now, please look at Ayane instead and continue ignoring that I was ever even here."

    scene secondhalloweenintro20
    with fade

    mo "Moving things right along and complying with Maya’s demands, here comes Ayane Amamiya as our very own main character, Lumine!"
    mo "Banished to years of only being viewed as a lovable, backseat love interest while Ami sits up in the front, it is Ayane’s mission to have Sensei make {i}her{/i} into the main heroine this time."
    mo "Please also note that I did not write that description and it was handed to me on an index card prior to Ayane taking the stage."
    s "You’re not a “backseat” character, Ayane..."

    scene secondhalloweenintro21
    with dissolve

    if bonus == True:
        ay "I {i}can{/i} be if you want me to."
        mo "Ooh! What brilliant and flirtatious execution! That’s our bubblewrap princess for you!"
    else:
        ay "{i}You'd take that back if you knew where I've been hiding all of the bodies.{/i}"
        s "What?"

    scene secondhalloweenintro22
    with fade

    mo "Up next we have Ganyu of the Liyue Qixing and- what’s this?! Is Futaba BUSTing out of the gate by accentuating her most deadly asset?"

    if bonus == True:
        r "Atta girl, Futaba! Knock him dead!"
        r "Just not literally because then we’d be murderers and {i}I can’t go down that path again...{/i}"
        s "Are you sure you’re in [high_school], Futaba?"
        f "I don’t...really want to talk right now..."
        f "I’m...too embarrassed for listening to Rin’s idea."
        s "Well...it is definitely working."
        mo "A harsh but realistic admittal from our protagonist!"
        mo "But with a few girls left to take the stage, this is still anyone’s game!"
    else:
        s "My eyes! Put those away!"
        f "I am sorry. It will not happen again."

    scene secondhalloweenintro23
    with fade

    mo "Which...brings us to Jean."
    mo "Can someone else announce this part? My throat suddenly hurts."
    r "So, how ‘bout Futaba’s boobs. Right?"
    s "I mean...I wouldn’t go discounting your outfit just because Futaba looked great."
    s "You’re really cute as well."
    r "Yeaaaaah, but I’m also off limits. And Otoha might get jealous if you call me cute and stuff."
    s "Otoha isn’t even here."
    r "Otoha is always here in spirit."
    s "Is she dead now?"
    r "Would I be smiling if she was?"
    s "Not unless..."
    s "{i}You killed her...{/i}"
    r "…"
    s "…"

    scene secondhalloweenintro24
    with dissolve

    r "You know too much..."

    scene secondhalloweenintro25
    with fade

    mo "W-What’s this?! A last minute entry?!"
    sa "What?...No...I..."
    sa "I was just...going to get my bag..."
    sa "I didn’t mean to get in the way..."
    mo "Too bad! Because now you’re an official contestant in the Halloween pre-game fashion show!"
    s "Good luck, Sana."

    scene secondhalloweenintro26
    with dissolve

    sa "I’m not even supposed to be up here!"

    scene secondhalloweenintro27
    with fade

    mo "And last but not least is I...Fischl von Luftschloss Narfidort, Prinzessin der Verurteilung..."
    s "...What?"

    scene secondhalloweenintro28
    with dissolve

    mo "Molly MacCormack as another girl with chuunibyou syndrome. Cute, right?"
    s "I have no idea what anything you just said means."
    mo "Then it looks like it’s time for another weebnote!"
    mo "Chuunibyou syndrome is the name for the delusional outlook shared by many [adolescent]s in which they create and live in false realities to help cope with insecurities or escape growing up!"
    mo "It’s typically a short-lived phase, but can sometimes spiral out of control and carry on for much greater lengths of time, turning otherwise lovable characters into socially awkward nightmares!"
    s "That sounds extremely familiar."
    mo "You’re telling me, Sir!"

    scene secondhalloweenintro29
    with fade

    mo "So, which one of us is it going to be?!"
    mo "Remember! This is an important decision that may or may not influence your future with whichever girl you choose!"
    r "Or not! Again, you’ll never know until it’s too late."
    s "This somehow feels a lot heavier than the dorm war fashion show. I don’t know if I’m ready."
    a "When in doubt, pick Ami. That’s my philosophy."

    if bonus == True:
        ay "What a weird way to say “Choose Ayane because she’ll let you do stuff in the backseat.”"
    else:
        ay "What a weird way to say “Choose Ayane because she is better than Ami in every way.”"

    f "I...still think Rin looks the best."
    r "Counterpoint: Boobs."
    mo "Go on, Sir! Choose!"

    menu:
        "Ami":
            s "I’m going to go ahead and give this victory to Ami."

            scene secondhalloweenintro30
            with dissolve

            a "Ah!! Really?!"
            a "I really won?!"
            a "You think I’m prettier than everyone else in the room?! And that you’ll stay with me forever and ever no matter what?!"
            s "I was more or less just choosing your costume, but sure. That doesn’t sound so bad."

            scene secondhalloweenintro31
            with dissolve

            ay "Congratulations, Ami. I still wish Sensei picked me, but I respect his decision."
            ay "If you were {i}my{/i} [niece], I’d treasure you dearly."
            a "I’m so happy...I don’t even know what to say!"
            a "Thank you!"
            a "Thank you, thank you, thank you!"
            a "And...And I love you!"
            a "Yeah!"
            s "You don’t have to thank me. Just...doing my best as an impartial judge."
            a "Are you sure you’re being impartial? And that you’re not just choosing me because I make your bed and cook you breakfast and wake you up and warm the bath for you and-"
            s "Yes, you do a lot of things for me. Everyone knows that."
            s "Now, accept your victory and stop making the other girls jealous. This was hard enough {i}without{/i} any of you trying to kill each other."

            $ ami_love += 5

            "{i}Ami’s affection has increased to [ami_love]!{/i}"

            $ amihalloween2win = True

        "Ayane":
            s "I think...I’m going to have to choose Ayane for this."

            scene secondhalloweenintro32
            with dissolve

            ay "Ahhhhh! Sensei!"

            if bonus == True:
                ay "Is it because of the backseat stuff?! I can have a limo here in five minutes!"
                s "It’s because I think you look the best. No ulterior motives involved."
                ay "Are you sure? Because I could probably even make it {i}four{/i} minutes if I ask nicely enough."
            else:
                ay "Is it because of the backseat stuff?! Because there were really only two bodies that will ever be missed and-"
                s "It’s because I think you look the best. And besides, I know you'd never actually kill anyone."
                ay "HAHAHAHAHA. NOPE. NOT ME. HAHAHAHAHA."

            a "I thought for sure you were going to pick me..."
            s "Well, Ami...that’s because you’re delusional and {i}always{/i} expect me to pick you."
            a "Yeah, so?"
            s "I just think Ayane deserves this one."

            scene secondhalloweenintro33
            with dissolve

            if bonus == True:
                ay "Mmmmmmmmm! I wanna scream! But then somebody would probably barge into the room and see you with a bunch of girls in costume and get you fired."
                s "I’m sure that if I was ever going to get fired from this[school], it would have happened by now."
            else:
                ay "Mmmmmmmmm! I wanna scream! But the last time I screamed, everyone within a ten mile radius melted."
                s "Please don't scream."

            $ ayane_love += 5

            "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

            $ ayanehalloween2win = True

        "Maya":
            s "The winner of this contest is..."
            s "Maya."

            scene secondhalloweenintro34
            with dissolve

            m "{i}Hah...{/i}"
            s "What? Shouldn’t you be excited about winning?"
            m "I didn’t {i}want{/i} to win. I didn’t even want to be involved in this contest."
            m "I just wanted to wear a costume of a character I liked without the fear of being ogled at or judged for doing so."
            m "All picking me is going to do is upset literally everyone else."
            s "Everyone else was going to get upset no matter what. I just decided to choose the person I-"
            m "Just...stop talking."
            m "Thank you for voting for me or whatever, but I really wish you would have just picked someone else..."

            $ maya_love += 5

            "{i}Maya’s affection has increased to [maya_love]!{/i}"

            $ mayahalloween2win = True

        "Rin":
            s "The winner of this contest is..."
            s "Rin."

            scene secondhalloweenintro35
            with dissolve

            r "Wait...Rin?"
            s "Rin."
            r "I...won?"
            r "Why?"
            s "Probably because I think you deserve to win."
            r "Uhh, wait. No. Hold up. Are you sure? Me? Instead of everyone else?"
            r "Instead of Futaba’s boobs?"
            r "Me? Rin Rokuhara?"
            s "Why is this so hard for you to believe?"

            scene secondhalloweenintro36
            with dissolve

            r "I don’t know, dude! I just could have sworn you were going to pick somebody else!"
            r "Choosing me is like...well, it’s not a homie choice! I have a girlfriend now!"
            s "So what? The task was choosing who I wanted to win and that’s what I did. End of discussion."

            scene secondhalloweenintro37
            with dissolve

            r "I...yeah. Okay? Okay."
            r "Thanks...Sensei..."

            $ rin_love += 5

            "{i}Rin’s affection has increased to [rin_love]!{/i}"

            $ rinhalloween2win = True

        "Futaba":
            s "The winner of this random Halloween contest thing is...Futaba."

            scene secondhalloweenintro38
            with dissolve

            f "Fu...taba?..."
            f "But...I'm...Futaba..."
            s "Yup. I choose you."

            if bonus == True:
                s "And before anyone asks, no. It wasn’t just because of her chest."

                "It did help, though."

            f "But..."
            f "No. No, you don’t really mean that, do you?"
            r "Dude! Accept your victory! You look fucking {i}hot{/i}."
            r "Sensei would have been an idiot for {i}not{/i} choosing you."
            f "I...I just didn’t expect this at all..."
            ay "I support the Futaba pick. I think she looks great as well."
            f "Are you sure you don’t want to...pick again maybe? It’s not too late to...vote for who you really want."
            s "I already did."
            s "I’ve told you time and time again that you’re cute. Consider this just one more step in me confirming that."

            scene secondhalloweenintro39
            with dissolve

            f "Okay..."
            f "Even if it’s just a little contest...having you choose me like this...really makes me happy..."

            $ futaba_love += 5

            "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

            $ futabahalloween2win = True

        "Molly":
            s "Well, after careful, internal deliberation...the winner of this contest is Molly."

            scene secondhalloweenintro40
            with dissolve

            mo "Do...do my ears deceive me?!"
            mo "I did spend an absurd amount of money on this costume, but I still would have wagered that you’d pick someone else, Sir!"
            s "Maybe in some other timeline, I would have. But I think you look the “best” and, since I can only choose one...I guess it had to be you."
            mo "Really? Even though I annoy you?"
            mo "Even though we had a lengthy discussion recently about how I’ve all but given up on real human beings and that I will forever devote myself to dating games?"
            mo "You’re still going to choose me after all of those flags have already been raised?"

            scene secondhalloweenintro41
            with dissolve

            s "I guess so."
            s "Congratulations, Molly. You deserve it."
            mo "Th...Thank you, Sir!"
            mo "As previously mentioned in your warning about this choice...I will not forget this!"

            $ molly_love += 5

            "{i}Molly’s affection has increased to [molly_love]!{/i}"

            $ mollyhalloween2win = True

        "Sana":
            s "The winner of this contest is..."

            scene secondhalloweenintro42
            with dissolve

            s "Sana."
            a "…"
            sa "…"

            scene secondhalloweenintro43
            with dissolve

            sa "What?!"

            if sanafashion == False:
                s "You heard me, official Halloween costume winner."
            else:
                s "You heard me, two time fashion contest champion."

            sa "I wasn’t even competing in this one!"
            mo "Actually, Sana...you formally entered the competition when you stepped into the spotlight."
            mo "If you didn’t want to participate, you should have been more careful."
            ay "Congratulations, Sana! I would have picked you too."
            sa "I didn’t want to be picked! I don’t even have a costume yet!"
            s "You don’t need one. That’s how cute you are."
            a "Ugh...Sana being in this contest made it unfair to the rest of us..."

            scene secondhalloweenintro44
            with dissolve

            sa "I wasn’t in the contest! This is all a big misunderstanding!"

            $ sana_love += 5

            "{i}Sana’s affection has increased to [sana_love]!{/i}"

            $ sanahalloween2win = True

    scene black
    with dissolve2
    stop music fadeout 40.0

    "After I name the winner, it becomes clear that it’s time for all of the girls to start getting ready for tonight’s party."
    "Apparently, some of the others have already started heading over to the Amamiya mansion to help set things up."

    if bonus == True:
        "And fortunately, I wasn’t forced to go along with Makoto and participate in that stage of the party this year, saving me a fair amount of energy to use on more important matters- like sex."
        "Hopefully."
        "But, if that winds up not being the case, at least I’ll be a little less exhausted when I wind up having to deal with a drunken Molly or...anything else along those lines."

    "Regardless...I, too, begin to make my way out of[school] alongside everyone else."
    "But, just as I make it to the lockers, Sana approaches me for the second time today (A new all-time record) and asks me to accompany her to her mother’s bar and help bring over some decorations for the party."
    "And while this sounds {i}technically{/i} a little easier than the hours I spent setting things up with Makoto, I can’t help but be a little upset."
    "My short-lived desire to spend the moments before a party I just found out about in silence has, unfortunately, come to an end."
    "But..."
    "On the bright side, at least things at Sara’s were rather...{i}lively{/i} last Halloween."
    "If I’m going to be tagging along with Sana, I can at least hope for a repeat of that..."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloweentwo1 = True
    $ rinsad = False

    jump halloweentwo2

label halloweentwo2:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day114
    if totaldays >= 120 and day103 == True and day91 == True and day120 == False:
        jump day120
    if totaldays >= 121 and day85 == True and day103 == True and day121 == False:
        jump day121
    if totaldays >= 126 and day103 == True and streets15 == True and chikadorm15 == True and day126 == False:
        jump day126
    if totaldays >= 128 and day103 == True and day126 == True and day == 5 and day128 == False:
        jump day128
    if totaldays >= 138 and day103 == True and day130 == True and day85 == True and day138 == False:
        jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
...
```