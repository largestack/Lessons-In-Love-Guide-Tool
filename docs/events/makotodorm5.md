# Completely Platonic
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotodorm5&go=Go)



## Event preconditions
✅Makoto love greater than or equal to 5

✅Event "[Makoto: Unexpected Profession](./firsttimepornshop.md)" is completed (event=firsttimepornshop)

✅Event "[Makoto: Teacher's Pet](./makotofirsthall.md)" is completed (event=makotofirsthall)



## Next events
* [Makoto: Sowing the Seeds](./makotonew2.md)

## Event properties
* ID: makotodorm5
* Group: Makoto
* Triggered by label: makotodorm
* Triggered by branch label: makotodorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Makoto's door and wait for her to-"

    mak "Just a minute!"

    "Well, I didn't have to wait long."
    "I lean against the wall and wait for her to finish doing whatever it is she's doing, wondering if she'll actually let me in or not."
    "Given that this is Makoto we're talking about and I am a teacher, I'm sure she will."
    "But I'm also sure there will be some sort of questioning as well since this is very likely against some sort of rule."

    scene platonicredux1
    with fade
    play sound "dooropen.mp3"

    mak "Sorry, I was just-"
    mak "Wait...Sensei? What are you doing here? Do you need me for something? Is everything okay? Do you-"
    s "Everything is fine. I was just looking to kill some time before going home for the night."
    mak "Kill some time? And...how exactly do you plan to do that?"
    s "Maybe...we could hang out in your room or something?"

    scene platonicredux2
    with dissolve

    mak "M-My room?! But...but why would you want to go in there?!"
    s "It makes more sense than hanging out in the hallway, doesn't it?"
    s "Unless you don't think we're close enough or something."

    scene platonicredux3
    with dissolve

    mak "I mean...do you really think we're that close?"
    mak "I suppose I {i}have{/i} probably spent more time with you than anyone else, save Ami..."
    mak "But...I don’t know. This just seems like...a lot, all of a sudden."
    s "Are you...uncomfortable being alone with me, Makoto? Because you seem to be making a pretty big deal out of this."

    scene platonicredux2
    with dissolve

    mak "Because it is a big deal, Sensei!"
    mak "And the room is a mess anyway so-"
    s "Makoto."

    scene platonicredux4
    with dissolve

    mak "W-What?..."
    s "If my class representative doesn't trust me enough to let me into her room, I might have to choose another one."

    scene platonicredux2
    with dissolve

    mak "You wouldn’t dare! Also, isn't that blackmail?!"
    s "Is there a rule in the student handbook against blackmail?"
    mak "I don't...think so? But I’m pretty sure there are several laws against it!"
    s "Then I guess I’ll just have to start looking for-"

    scene platonicredux3
    with dissolve

    mak "Um, wait!"
    mak "I...suppose I might be making a bigger deal of having a boy in my room than I should..."
    mak "I mean, how much different could having you around be compared to someone like Miku?"
    mak "Sure, you're twice my size and...twice my age and...in a position of power and-"
    s "Yeah, I get it. Now, are you going to open the door or what?"
    mak "Y-Yes..."
    mak "As long as you’re okay with me..."

    scene platonicredux5
    with dissolve

    mak "Uhh...okay with {i}it!{/i} Not okay with me! Saying {i}me{/i} made it sound like I was insinuating something inappropriate, which I absolutely was not!"
    mak "I understand that it's totally normal for a teacher to visit a student's dorm room at night and I am going to stop yelling right now because this probably sounds very suspicious!"
    s "Good call, Makoto..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Of course, I never intended to actually blackmail Makoto."
    "I haven't been around for long, but even the short amount of time I {i}have{/i} spent here has been way more than sufficient in revealing exactly how much she does for me."
    "In fact, I don't think I've had to sign a single paper yet."
    "Signing papers is probably a thing teachers have to do, right?"
    "I honestly don't know- which is further proof of exactly how useful Makoto has been."
    "I just understand the type of girl she is and I understand how to get what I want out of people like her."
    "She's lucky I don't want much."
    "........."
    "......"
    "..."

    scene makotofirstdorm1
    with dissolve2

    mak "So...here we are..."
    mak "Just a boy and a girl alone in a [high_school] dorm room..."
    mak "Just...two people in a completely platonic relationship gathering in a private location in the middle of the night..."
    mak "Plain old normal stuff. No rules being broken here."

    if bonus == True:
        s "It's strange that you’re still embarrassed by something like this even after hanging out with me in a building that sells fake vaginas."
    else:
        s "Why are you so embarrassed? I am an educational professional first and foremost. I have no romantic or sexual interest in you."

    scene makotofirstdorm2
    with dissolve

    if bonus == True:
        mak "This is entirely different! You came to the porn shop to buy things, not to see me!"
        mak "Well...at least the first time!"

    mak "Today, you're actually here for me, though! And I'm just...trying to wrap my head around what that could possibly mean."
    s "Why does it have to mean anything? You should know better than anyone that there's no scientific reason compelling people to come together."

    scene makotofirstdorm3
    with dissolve

    mak "Well, actually...there are plenty of scientific reasons that would explain a thing like that. And several of which would likely be relevant here."
    mak "But...you would clearly know that as well, so...chances are you only said there {i}weren't{/i} reasons because you'd prefer I ignore their existence for the time being..."
    mak "Perhaps this is some sort of...riddle, maybe?...But what could you possibly-"
    s "Makoto, I just wanted to see you. It's that simple."

    scene makotofirstdorm4
    with dissolve

    mak "It is?..."
    s "Of course."
    s "Now, if you wanted to spend our time together watching porn, that would be totally acceptable as well."
    s "I understand better than anyone how hard it is being away from that for too long. You don't have to hide your pain from me."

    scene makotofirstdorm2
    with dissolve

    mak "There is no {i}pain!{/i} I'm perfectly comfortable being away from pornography and am in no way dependent on it!"
    s "That just sounded like a really complicated way to say you're better than me."
    mak "Do you truly spend {i}that much{/i} time rotting away your brain with that stuff?"
    mak "What if you become addicted and started neglecting your responsibilities as a teacher? That sort of thing can happen, you know."

    "I'm pretty sure it already has and I have done virtually no teaching whatsoever."

    mak "If that happens I'd..."
    mak "Well, it would probably be up to me to get you back to normal and..."

    scene makotofirstdorm3
    with dissolve

    mak "Actually...that does sound like it might be fun now that I think about it..."
    mak "Just you and me...studying and...teaching each other all sorts of..."
    s "..."
    mak "..."

    scene makotofirstdorm5
    with dissolve

    mak "Um...before I start getting excited...do you think it might be okay for me to maybe...help you teach the class one day?"

    "Was...Makoto about to get turned on from a fantasy of us studying?..."

    mak "Just...as training, of course. You know, since I plan on becoming a teacher one day and whatnot."
    s "You can teach the class every day if you want. That will give me more time to sleep."
    s "I'm not sure if I can let you take over as counselor, though. That seems like more of a {i}me{/i} thing."

    "It doesn't, really. I just don't want to surrender the opportunity to be alone with a variety of attractive teenage girls."

    scene makotofirstdorm6
    with dissolve

    mak "Oh, umm...funny you should bring that up...because there’s something I’ve been wondering lately."

    if bonus == True:
        mak "That time we were alone in there and you...you know...massaged me..."
        mak "That was, like...just a {i}me{/i} thing, right?..."
        mak "Like...there's no way you're just calling people in there to relieve their stress through...umm...{i}physical{/i} treatment, are you?"
        s "Would there be a problem if I was?"
        mak "There would be a multitude of problems if you were."
        mak "But...I'd be able to overlook it if it was just a thing you did for me since...the two of us are close and everything."
        mak "In fact, I...I probably wouldn't have even minded if-"

        scene makotofirstdorm6r
        with dissolve

        mak "A-Actually! I don't even know what I was about to say there."
        mak "Please forgive me for my mind being all over the place, Sensei. It's been a long day and...I tend to ramble when I get exhausted."
        s "Sounds to me like someone could use another massage."

        scene makotofirstdorm2
        with dissolve

        mak "You mean...right now?! In my bedroom?! Where the...bed is?!"
        s "That {i}is{/i} typically where you keep the bed, yes."
        mak "I...I don't really know if...that's the best place for..."

    else:
        mak "I think Miku has been hiding various cans of soup in this room without telling me. I am not sure what I am to do next."
        s "Do you like soup? Because I have an idea if you do."
        mak "It's fine, I guess. There are just so many kinds."
        mak "I wouldn't know which one to eat first."
        s "You're right. That does sound rough."
        mak "Yeah..."
        s "Maybe you can just kill her? Everyone has been acting a lot nicer to me ever since I started doing that."

    scene makotofirstdorm6r2
    with dissolve

    mak "Just...forget I even asked about the whole massage thing! This is quickly approaching non-platonic levels in my head and that...that would not be good at all."

    "I disagree wholeheartedly, but will keep my comments to myself for now so as to not risk scaring her away."

    mak "I’ve just been really curious about why everyone seems to be in higher spirits lately and...figured your new {i}methods{/i} might have something do with it."
    mak "Assuming the...massages are part of your new teaching strategy. Which I am very much hoping they are not {size=-15}for everyone except me{/size}."
    s "You're probably just only looking at specific girls or something."
    s "I'm sure Ayane has been in high spirits lately because I've been giving her more attention than normal, but I can't imagine someone like Yumi or Maya seeming any different at all."

    scene makotofirstdorm7
    with dissolve

    if bonus == True:
        mak "But...why only give Ayane more attention than normal? As everyone's teacher, shouldn't you be distributing your time among...well, {i}everyone?{/i}"
        s "Maybe? That's not really something I think about."
        mak "It...probably should be."
        s "And it probably is. It's just a lot easier to please someone like Ayane than it is to please someone like Yumi, I guess."
        mak "Pleasing Ayane doesn't sound particularly difficult given her...uhh..."
        s "Innate desire to have my children?"
    else:
        mak "Didn't you literally just tell me?"
        s "Shut up and stop accusing me of things just because I haven't threatened your life yet, Makoto."

    scene makotofirstdorm7r
    with dissolve

    mak "Can you word it in a slightly less disgusting way next time?"
    mak "It is annoying enough having to listen to the overtly-sexual nonsense coming from her mouth and I don't want to have to hear it coming from yours as well."
    s "Is that jealousy I hear, Makoto?"

    scene makotofirstdorm8
    with dissolve

    mak "Jealous? Me? Don't be absurd."

    if bonus == True:
        mak "What would I have to be jealous about, Sensei?"
        mak "Ayane's nonsense is just that, isn't it? Nonsense?"
        mak "Don't tell me you've actually been up to anything {i}inappropriate{/i} with her."
        s "Can you define {i}inappropriate{/i}, please?"
        mak "..."
        s "..."
        mak "Do I really have to?"
        s "You know what? I'm just going to go with no. That seems like the safe answer."

        scene makotofirstdorm2
        with dissolve

        mak "I take exception to how uncertain you sound right now."
        mak "The two of you aren’t involved in some sort of...illicit relationship, are you?"
        s "Can you define {i}illicit{/i}, please?"
        mak "..."
        s "..."
    else:
        s "Ayane would never get jealous over something like this."

    scene makotofirstdorm8r
    with dissolve

    mak "{size=-15}That fucking bitch...{/size}"
    s "Makoto?"

    scene makotofirstdorm5
    with dissolve

    mak "Yes, Sensei?"
    s "You doing okay?"
    mak "Of course, Sensei."
    s "Good...Well, just to reiterate, nothing weird is going on in my office and I'll do my best to contain my unearthly desire to massage everyone to you and you only."
    mak "I greatly appreciate that. Thank you."
    s "Any time. So, feel free to stop by my office whenever you like."
    mak "Absolutely. I’ve been meaning to drop by recently anyway."
    s "Oh yeah? Why's that?"

    scene makotofirstdorm6
    with dissolve

    if bonus == True:
        mak "I just...realized it might be time for me to start thinking about college and wanted to explore some options with you."

        "Why is she already thinking about that as a freshman? Shouldn't she be focusing more on just...making it through high school first?"

        s "You sure you don’t want a massage instead?"

        if day26 == True:
            mak "I’m sure. And I already told you that we probably shouldn’t be doing that stuff in[school], didn’t I?"
            mak "Save your massages for when we're somewhere else."
            s "Just not in school and not in your bedroom..."
            s "Wait. Does that mean-"
            mak "I would sooner die than allow you to massage me at my work."

            "Damn it."

        else:
            mak "Very sure. School is clearly not the place for things like that."

        scene makotofirstdorm7
        with dissolve

        mak "As for everywhere else, though...I think it might be okay under the right circumstances..."
        s "Those circumstances being?..."

        scene makotofirstdorm8
        with dissolve

        mak "I'm not quite sure as I've yet to make a list."
        mak "It would have to be on rare occasions only, though. I’m afraid I’d become too dependent on your {i}skills{/i} if you were to just start rubbing my shoulders each time we met."
        s "I mean... there are {i}other{/i} areas I can-"
        mak "Don't you dare finish that sentence."
        s "What's wrong? I was obviously just referring to your back and your neck and...an assortment of other safe-for-work areas."
        mak "Let’s just stick to the shoulders for now, okay?"
    else:
        mak "I've just..."
        s "..."
        mak "..."
        s "You've just what, Makoto?"
        mak "..."

        "Makoto becomes suspiciously quiet and, after a bit of thinking, I figure out why."

        s "So...it's been you the whole time."
        s "You are the one who has been hiding the soup. It was never Miku."
        mak "I am sorry, Sensei. I didn't want you to hate me."

    scene black
    with dissolve

    if bonus == True:
        "Makoto and I hang out for a little while longer and, unfortunately, the topic of massages fizzles out."
        "I was pretty confident I'd at least get to {i}touch{/i} her tonight on account of our apparent mutual {i}interest{/i} in one another, but-"
        "Perhaps she's not interested in the same way I am just yet?"
        "She'll get there soon enough, though."
        "There's only so much willpower a person can have- and when you're surrounded by sex on a day-to-day basis, I can't imagine that not eating away at you."
        "Being alone with the person you admire will only exacerbate that craving."
        "She can block out her curiosities as much as she wants, but the walls keeping them contained will only hold for so long- and I will be the one to hold her after that."
        "Eventually, the two of us decide it's best for me to leave as Miku informs Makoto that she's on the way home."
        "And just like that, without even a moment of contact, I'm headed back to my house..."
    else:
        s "It is too late for that, Makoto."
        s "Goodbye forever."
        mak "Sensei noooooooooo D="

    $ renpy.end_replay()
    $ makotodorm5 = True
    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]! You can now spend
    time with her in her room!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudorm5:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label makotodorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if makoto_love >= 5 and firsttimepornshop == True and makotofirsthall == True and makotodorm5 == False:
                jump makotodorm5
...
```