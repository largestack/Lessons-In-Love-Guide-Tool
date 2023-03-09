# Unexpected Profession
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimepornshop&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 0



## Next events
* [Main: Walk in the Park](./day38.md)
* [Makoto: Completely Platonic](./makotodorm5.md)

## Event properties
* ID: firsttimepornshop
* Group: Makoto
* Triggered by label: pornshop
* Triggered by branch label: pornshop

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label firsttimepornshop:
    play music "citylife.mp3" fadein 2.0
    scene pornshop1
    with dissolve

    if bonus == True:
        "I decide to check out the local porn shop because...well, it feels a lot more empowering to actually purchase porn rather than just browsing for it online. "
    else:
        "I decide to go to the local DVD store, but quickly discover that it is anything but that and I feel very let down."
        "However, as an adamant supporter of small businesses, I decide to peruse the selection anyway."

    if bonus == True:
        "Besides, I have no idea when the next time I'll have sex is...so this will suffice in holding me over in the meantime."
        "Also, who doesn't love porn? There is absolutely no way this trip could possibly go wrong."

    q "Welcome in. Please take your-"

    scene pornshop2
    with dissolve

    q "Ah?!"

    "A [young_girl] at the front desk calls out to me, but abruptly stops for some reason."
    "I take a quick look around the store to see if maybe she's reacting to someone else but quickly confirm that it must have been something {i}I{/i} did."
    "What, though? I've only been inside for like, five seconds."

    q "We...are closed!"
    s "But the sign outside said you were open for another two hours."

    q "That sign is old! Please leave now!"

    scene pornshop3
    with fade

    "I make my way over to the counter as I'm tired of shouting across the room and the girl immediately shields her face."
    "She looks to be the age of one of my students, so I don't hold it against her for getting embarrassed about working in a place like this-"
    "But she should at least be {i}somewhat{/i} helpful to customers, shouldn't she?"
    "Or...maybe this is another one of those {i}no males around{/i} type of deals that I heard Ami talk about?"
    "If this girl doesn't have any experience helping male customers..."
    "Well, honestly, that just makes me want her help even more."

    q "What...uh..."
    q "What can I...do for you?..."
    s "..."
    q "..."
    s "Wait a minute..."
    q "Of course...take as long as you-"

    scene pornshop4
    with dissolve

    mak "Aah!"
    mak "Un...Unhand me right now! I'll call the cops! I mean it!"
    s "...Makoto?"
    mak "Nope! No Makoto's here! You must be confusing me for someone else!"
    s "You look completely different without your glasses on."
    mak "Never mind my glasses! What the Hell are you doing in here, Sensei?!"
    mak "You know what kind of store this is, don't you?"
    s "I'm actually just stopping by to give you your homework. I looked up your address in the school registry."

    scene pornshop4r
    with dissolve

    mak "Wait...really? But I could have sworn-"

    if bonus == True:
        s "That was obviously a lie. I'm here to buy porn."

        scene pornshop5
        with hpunch

        mak "Can't you just use the Internet for that sort of thing?! That's what everyone else does!"
        s "Can you really afford to be saying that as the employee of a porn shop?"
        mak "No!"
        mak "I mean...yes?!"
        mak "I mean-"
        mak "I don’t know what I mean!"
    else:
        s "Yes. Here you go."

        "I hand Makoto her homework."

        mak "Thank you. That was very kind."
        s "I was unaware that you worked in this establishment, Makoto."
        mak "I am so embarrassed that you are now aware of my workplace."

    scene pornshop6
    with dissolve

    s "Listen, I get that it's probably embarrassing to be seen somewhere like this by your teacher...but I'm not going to hold it against you."
    s "This is your family's business, right? I think it’s admirable that you're helping out here."
    s "Now, can you please point me toward the teen section?"

    scene pornshop6r
    with dissolve

    mak "That's it. I am going to kill myself tonight."
    s "Oh come on. Isn’t it better to be dealing with me than some random guy?"

    scene pornshop7
    with dissolve

    if bonus == True:
        mak "Honestly?..."
        mak "No. No, this is ten times worse."
        s "This might be shocking news for you, but teachers watch porn too."

        scene pornshop7r
        with dissolve

        mak "That doesn't mean I have to be okay with it!"
        mak "Now that you know I work {i}here{/i} it...it changes everything!"
        mak "I'm supposed to be the diligent one! The one who always follows the rules and...doesn't sell vibrators five nights a week!"
        s "You can be whatever you want to be. If selling vibrators empowers you, I'll even buy one. Right now."
        mak "For what?! Stop making this even weirder for me by being okay with it when it is obviously very, very wrong!"
    else:
        mak "I mean...I'd prefer to not be dealing with either..."

    s "For what it's worth, it wouldn't make any difference to me if you worked here or some fast food restaurant. A job is a job and you just happened to wind up with this one."

    scene pornshop6
    with dissolve

    mak "Well...thank you, Sensei. That's-"
    s "In fact, I implore {i}more{/i} girls your age to work in places like this. Because not only would it bring more customers in, it would help-"

    scene pornshop8x
    with dissolve

    mak "Okay, you know what? Just...pick something and get out. It's clear that arguing about this is going to somehow negatively affect our relationship, and I would very much prefer to not do that."
    s "Great. So what do you recommend?"
    mak "..."
    mak "Huh?"
    mak "Me?"
    s "Yeah. What’s the big ticket item here? What should I buy?"
    mak "You’re...asking me for recommendations?"
    s "Yeah. You're the porn expert, aren't you?"

    scene pornshop6
    with dissolve

    mak "My mom is the expert...I just kinda...you know..."
    s "Ahh. So you're just a porn {i}hobbyist.{/i}"

    scene pornshop8x
    with dissolve

    mak "No...I am a normal girl."
    s "Normal girls watch porn and you shouldn't be ashamed to admit that you do too."

    if bonus == True:
        mak "It’s not that I {i}don’t{/i}...it’s just not something I planned on talking about to {i}you.{/i}"
        s "But it's the first thing we've realized that we have in common with one another."

        scene pornshop7r
        with dissolve

        mak "We have plenty of other things in common! We're both intellectuals! We both wear glasses! We both-"
        s "Have a series of tags we gravitate toward when we're alone in our rooms. I understand you."

        scene pornshop8x
        with dissolve

        mak "No, I really don't think you do..."
        s "Listen, your secret’s safe with me. Don’t worry. Just give me a recommendation and I’ll be on my way."
        s "After that, we can forget this little meeting ever happened."

        "That obviously isn't true. I plan on coming here all the time."
        "I'm just not going to let Makoto know that since I don't {i}actually{/i} want her to kill herself tonight."

        scene pornshop6
        with dissolve

        mak "Umm..."
        mak "Well...I...kind of need to know what...sort of things you're into to be able to recommend anything..."
    else:
        s "I watch all kinds of stuff. They used to call me the {i}stuff watcher{/i} back in college in between all of those times where they'd shove me into lockers."
        mak "..."
        mak "Can you at least tell me...some of the stuff you're interested in so I can make a recommendation?"

    if bonus == True:
        s "Are you asking me what turns me on right now?"
        mak "I...guess so?..."
        s "Makoto, I am your {i}teacher.{/i} You can't just ask me things like that."

        scene pornshop7r
        with dissolve

        mak "What is this horrible side of you and why am I just finding out about it now?!"
        s "I'm just kidding. You can ask me about my turn-ons whenever you want."
        mak "I repeat! What is this horrible side of you and why am I just finding out about it now?!"

        "It looks like I'm going to have to give Makoto a little more info as to what I'm looking for."
        "The only issue is what exactly I'm going to tell her."

        s "Let's see..."
        s "I'm looking for-"

        menu:
            "Mature/MILF Porn":
                s "Do you have anything with mature women?"
                mak "Like...ones around your age? Or...older?"
                s "How much older do you have?"

                scene pornshop8r
                with dissolve

                mak "How much older do you {i}want?...{/i}"
                s "I'm not sure. I've never really thought about it before."
                mak "So you're just...taking a shot in the dark here?"
                s "An educated shot. I know what I'm in the mood for. But I am trusting you to make the final decision."
                mak "..."
                s "..."
                mak "Please never come here again after tonight."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and checks out a few DVDs."

                mak "Umm...Sensei...do you have a preference for...you know...breast size?"
                s "Up to you, Makoto. I appreciate all breasts equally."
                mak "How kind of you..."

                "Makoto searches around for another minute or two before eventually returning to the counter without anything in her hand."

            "Student/Teacher Porn":
                s "Do you have anything involving a teacher and a student?"

                scene pornshop9
                with dissolve

                mak "Involving what?!"
                s "A teacher and a student. Or students. No more than ten, though."
                s "Oh, and if you can find any with glasses, that would be much appreciated."
                mak "There is...absolutely no way you don't understand how this sounds!"
                s "Oh, I know exactly how this sounds. I'm just interested in seeing how you handle this revelation."

                scene pornshop9r
                with dissolve

                mak "What is happening to my life all of a sudden?"
                s "Oh, come on. This is a totally normal thing for someone in my position to fantasize about."
                s "Don't pretend you haven't thought about it from the other side of things."

                scene pornshop9r2
                with dissolve

                mak "What goes on in my mind is for me and me only! I don't need you of all people trying to figure out what goes on in there!"
                s "All I'm saying is that the two of us aren't so different. And that you should be happy I'm interested in girls like you."

                scene pornshop9r3
                with dissolve

                mak "It's not that I'm not happy..."
                mak "It's just...a lot to take in at once..."
                s "Don't worry. I'll go slow."
                mak "..."
                s "..."

                scene pornshop9r4
                with dissolve

                mak "..."
                mak "I wonder if I should leave a suicide note..."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and starts checking out a few DVDs."

                mak "Sensei...all of the girls I'm seeing with glasses...look a tiny bit too close to me..."
                s "Perfect. I'll take them all."
                mak "A-All of them?! Just how much free time do you have?!"

                "Makoto begins shoveling all of the student/teacher DVDs she can find into her arms...only to put them all right back and return to the counter minutes later with absolutely nothing."

            "The weirdest shit you've got":
                s "Well, this isn't easy to talk about, but..."
                s "I’m not really into...'conventional' pornography."

                scene pornshop10
                with dissolve

                mak "And...what does that mean exactly?"
                s "You not understanding just means you haven’t been tainted by the evils of the world yet."
                mak "The...evils of the world?..."
                mak "But how is that supposed to help me find-"
                s "You know what? Just do a couple laps around the store and grab me the weirdest thing you can find."
                mak "..."
                s "..."
                mak "Ugh..."

                scene pornshop8
                with dissolve

                "Makoto walks over to a rack near the wall and checks out a few DVDs."
                "Most of them wind up being immediately put back onto the shelves but, every once in a while, Makoto finds something of note and runs it by me."

                mak "Sensei...This one has a chicken on the cover..."

                "Unfortunately, it's never enough."

                mak "Is...Is that okay?"
                s "Weirder, please."
                mak "Weirder than a chicken?..."

                "Makoto looks through a few more rows of DVDs before coming back without anything in her hands."
    else:
        s "Mainly board games and long walks on the beach."
        s "Oh! Do you have the Wedding Singer on DVD? I would very much like to watch that with my accountant later."

    scene pornshop6
    with dissolve

    mak "Yeah, I tried...but I really can't do this."
    mak "I think it might be better if you just use the Internet after all..."
    s "How about you just follow me around the store and I point out all of the stuff I'm interested in?"
    s "That sounds like it would work, right?"
    s "Oh, and maybe after that, you could show me all of the stuff {i}you're{/i} interested in and-"

    scene pornshop11
    with dissolve

    mak "Oh, look at the time! We’re closed!"
    s "No you're not. It's only been like ten minutes since I walked in and-"
    mak "Thanks for stopping in, Sensei! It was nice seeing you!"
    mak "Please never come back and forget where I work now!"

    scene black
    with dissolve2

    if bonus == True:
        "Makoto begins pushing me to the door, but I refuse to leave this place without any porn."
    else:
        "Makoto begins pushing me to the door, but I refuse to leave this place without something to watch tonight."

    "In a desperate attempt to avoid leaving empty-handed, I reach out and grab the first DVD I see on the way out of the shop."

    mak "Hey! You can't just-"
    mak "Ugh, never mind! Just take it! I’ll pay for it myself!"

    "I give up resisting once I have something in my hands and Makoto is eventually able to push me outside, quickly locking the door behind me."

    mak "Goodnight, Sensei! You were never here and neither was I!"
    s "Goodnight, Makoto. See you tomorrow night."
    mak "I sure hope not!"

    "Left alone with nothing but my new DVD and the night sky, I glance down to inspect the cover."

    if bonus == True:
        s "“After School Service: Student Council Punishment Games”"
        s "..."
        s "I can work with this."
    else:
        s "“Napoleon Dynamite?” Ugh!"

        "I turn around, determined to return the DVD as I refuse to watch this pathetic drivel, but Makoto does not let me back in =/"

    $ renpy.end_replay()
    $ firsttimepornshop = True
    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label porn3to4:
    play music "citylife.mp3" fadein 2.0
    scene pornshop9
    with dissolve

    "I decide to pay Makoto a visit at the porn shop."
    "Of course, she isn’t exactly happy to see me there."
    "I spend the next twenty minutes trying to convince her to help me
    find something I can take home only to be pushed out the door yet again."
    "If she treats {i}me{/i} like this, I can only imagine how she handles normal customers..."

    scene black
    with dissolve

    $ makoto_love += 1

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"

    stop music fadeout 3.0
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label pornshop5:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
label pornshop:
    if makotoblock == True:
        "I should leave Makoto alone for now..."
        jump satnightmenu
    if makoto_love >= 0 and firsttimepornshop == False:
        jump firsttimepornshop
...
```