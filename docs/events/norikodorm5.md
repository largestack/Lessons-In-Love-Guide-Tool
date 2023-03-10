# Semi-Constructive Criticism (Noriko)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Noriko love greater than or equal to 5

* Event [Love, Dorms, and Other Things](./kirindorm10.md) (Kirin) is completed)

* Event [Nakayarakawayama](./convenience1.md) (Noriko) is completed)



## Next events

* [Noriko: Mouthjob](./convenience5.md)

## Event properties

* Id: norikodorm5
* Group: Noriko
* Triggered by label: norikodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->norikodorm->norikodorm5

## Official wiki page

[Semi-Constructive Criticism](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikodorm5&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikodorm5:
    play sound "knock.mp3"
    stop music fadeout 25.0

    "I knock on Noriko’s door and wait for her to answer."

    if bonus == True:
        "I’ve yet to be able to spend any time alone in there with her and, if we’re ever going to get even half as close as she wants the two of us to, that’s probably something I should start doing."
        "It’s not only beneficial to her, though, of course."
        "I have plenty to gain from one more questionable relationship."
        "Especially one revolving around the sole creature in this universe that the girl responsible for resetting it hates."
        "Frankly, there’s a distinct lack of logic in my decision to continue reaching out to Noriko- but is logic really a necessary trait when consequences are no more real here than they would be in a book?"
        "I was placed here to do as I please. "
        "Which, if you’ve realized anything about me so far, is to have sex with the girls I find attractive."
        "Noriko is attractive."
        "Maya is attractive."
        "I will defile both of them or die in the process."
        "Such is life."
    else:
        "I hope she is ready to party because I am feeling saucy tonight."

    play sound "knock.mp3"

    s "Noriko, are you in there?"

    "I can hear the volume of distorted, intentionally messy rock music being turned down from the inside."
    "Seems like she didn’t hear me the first time I knocked."

    n "Is somebody there?"
    s "Yes, someone is here. It’s me."
    n "Oh crap! You can come in, Sensei!"
    n "Sorry to keep you waiting, I didn’t hear you at first."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "It’s fine. Don’t worry about it."

    scene norikowalk1
    with dissolve
    play music "wewereangels.mp3"

    n "Well of course I’m going to worry about it."
    n "What if you decided to go hang out with somebody else since I didn’t answer the door right away?"
    s "I’m usually a bit more persistent than that."
    s "If I made it to three knocks, though...that’s where I start getting angry."
    n "Hmm...I see, I see. So don’t let you get to three knocks. Got it."
    n "What’s an angry Sensei like, anyway? I’m pretty sure I’ve only seen you happy, neutral, and sad."
    n "I can’t ever recall a time where you like, {i}really{/i} got pissed off."
    s "I’m pretty sure the only time I’ve gotten pissed off in the last several months is when one of your classmate’s little sisters kept questioning a book I was reading to her."

    scene norikowalk2
    with dissolve

    n "What?! You never read me stories when I was little!"
    n "I thought time had worn you down, not made you a family man!"
    n "Though, this does bode well for the future of the Nakayarakawayamas."
    s "Please stop using that incredibly long last name. Something about it really triggers something in my brain to just-"

    scene norikowalk3
    with dissolve

    n "Explode?"
    s "…"
    n "Oh, bright idea. Is there anywhere safe the two of us could go to light stuff on fire?"
    n "It’s great for stress relief and might help you get some of your memories back."
    s "Was I...a pyromaniac previously?"
    n "I meant more of the “being alone with me” part."
    s "Aren’t we alone together now?"

    scene norikowalk4
    with dissolve

    n "We’re not. Big Brother is always watching, Sensei."
    s "Okay, so either you have a second sibling I don’t know about or that was an Orwell reference."
    n "Obviously it’s an Orwell reference. If I had a brother, I’d have made him track you down years ago and beat you up for moving without telling me."
    s "And if that brother was younger than you?"

    scene norikowalk5
    with dissolve

    n "I’d...be making sure his tutor doesn’t start teaching him anything weird."
    s "Uh-oh. I know an implication about myself when I hear one."
    s "What sort of weird stuff did I teach you about?"

    scene norikowalk6
    with dissolve

    n "Nothing we wouldn’t have learned about eventually."
    n "Like 1984, for example. I think we were like...ten years old when you started making us read that?"
    s "That is far too young for that piece of literature."
    n "Probably. Like, I don’t even think Maya was into stuff that complicated back then and she was just as weird as you were."
    n "{i}I’m{/i} the normal one here. "
    n "But I guess I should be thanking you since that book was the first of many steps on my way to becoming a real freedom fighter."
    s "And how exactly are you fighting for freedom, Noriko?"
    n "The only way a girl my age can be, through expression."
    n "Not like I can make any sort of real change until I build up a background or profile for myself and people start taking me seriously."
    n "I just hope I’m not too burnt out by the time I get out of [high_school] to actually do something that will make a difference."

    "If you ever {i}make{/i} it out of [high_school], you mean..."

    s "Then...if you could change anything in the world, what would you change first?"
    n "Our relationship status."
    s "Our relationship matters more to you than like...climate change?"
    n "They both matter. But if you want to know what would make me happiest, it’s that."
    s "I think freedom fighters are supposed to be thinking of the greater good, not themselves."
    n "Aren’t you attempting to inhibit my freedom by imposing that belief on me?"
    n "This is exactly what I’m fighting against, Sensei."
    s "I just can’t imagine many people will back your cause if it’s portrayed the same way outside of this dorm room."
    n "Well, I’ve still got a few years to iron out the kinks."

    scene norikowalk7
    with dissolve

    n "I {i}am{/i} going to do something, though."
    n "Even if it’s just changing one person’s life or like...adopting a kid or something like that."
    n "It’s hard to feel like you have a purpose in the world without a tangible symbol of that purpose, you know?"
    s "Not really. But if you ever need some semi-constructive criticism, you know where to look."

    scene norikowalk8
    with dissolve

    n "And it’s the same place I’m always looking anyway..."
    s "…"
    n "Can you just like, hurry up and remember me already?"
    n "I say a lot of stuff that would be ten times cuter if you only understood the connotations."
    s "I think that one was pretty easy to understand."
    n "So you remember how I always followed you around the house and stared at you when I was three?"
    s "Oh. Well, okay then. I guess there was a bit of subtext to that."
    n "There’s subtext to everything about me. I built myself around trying to catch your eye."
    n "But alas, I was never the favorite."
    s "I guess it must have been hard falling in love with someone that your sibling is-"

    play sound "static.mp3"
    scene yumis2
    with flash
    scene norikowalk9
    with flash
    stop sound

    s "…"
    n "Sensei?"
    s "How did we get here?"

    scene norikowalk10
    with dissolve

    n "Well...first, I told you I wanted to go for a walk since I’m still not that familiar with this area yet."
    n "And then {i}you{/i} said something like, “I guess I still have some time to kill.”"
    n "And then we opened the door and said hi to Uta who was trying to feed our dorm-bird crackers."
    n "And then we walked for a little while and wound up here."
    s "I feel like I almost remembered something."

    scene norikowalk11
    with dissolve

    n "An important thing?! Or like a thing you had for breakfast?!"
    n "Not that breakfast isn’t important, of course! It's the most important meal of the day!"
    s "An important thing."
    s "Probably. "
    s "It’s just a feeling, though. And one that’s gone now anyway."

    scene norikowalk12
    with dissolve

    n "Mmm!"
    n "Don’t lure me in like that! You know those memories are what my character arc is based around!"
    n "The sooner you get them back, the sooner I can move onto the next phase!"
    s "And that next phase is?"

    scene norikowalk13
    with dissolve

    n "Showing my parents and my sister that I was {i}not{/i} crazy and that there was always something special about the two of us."
    n "A little hope goes a long way, Sensei."
    n "I don’t claim to understand you or anything. There are still a million things I don’t know about you, and I’m sure you’ll find that out in no time at all."
    n "But there’s a lot more to falling in love than simply “understanding.”"

    scene norikowalk14
    with dissolve

    if bonus == True:
        n "Like looking at somebody and thinking, “Yeah. I’ll still want to have sex with you in twenty years,” or “I would know what to order you for dinner if you were in the bathroom when the waitress showed up.”"
    else:
        n "Like looking at somebody and thinking, “Yeah. That's a person I'd like to make a bone necklace with.”"

    n "Stuff like that."
    s "That sounds like something Ayane would say."

    scene norikowalk15
    with dissolve

    n "Ahh, yes. Ayane."
    n "She loves you a lot."
    n "I think she’s hiding something, though."
    n "I can feel it."
    s "We’re all hiding something."
    n "Do you think I’m hiding something?"
    s "Probably. "
    s "It would certainly be easy to in your position."
    n "You’re right. I could manipulate you all I want into thinking things that never happened {i}actually{/i} happened."

    scene norikowalk16
    with dissolve

    n "And yet, I find myself wishing every night that you’ll just come back home..."
    n "That one day I’ll wake up and hear the doorbell ring...and then rush downstairs and pretend I’m not excited to see you..."
    n "And you’ll pat my head and tell me I look cute..."

    scene norikowalk17
    with dissolve

    if bonus == True:
        n "And then you’ll go upstairs and finger my sister."
        s "You wish for that, too?"
        n "That part I’d be fine with leaving out. It’s the {i}first{/i} few that I want back the most."
        s "Our dynamic would have drastically changed if it was the last one you wanted most."
    else:
        n "And then you’ll go upstairs and hug my sister."
        s "To be fair, she could probably use a hug. She is very grumpy."
        s "But wouldn't that make you sad?"

    scene norikowalk18
    with dissolve

    n "Well that would still be better than it is now, right?"
    s "…"
    s "For me or for you?"
    n "For both of us."
    s "I didn’t realize you felt that way about your sister."
    n "I just mean that...at least if you were with Niki, there would be some sort of...return to normalcy, I guess."
    n "Even though I found “you” it’s still not the full “you.”"
    n "You’ve got a whole new life now...and a whole group of girls who would kill me if it meant being able to absorb all of my happy memories with you."
    n "And I would kill too if it meant being able to absorb just a few of the ones they’ve made this[school] year."
    s "I think I get what you’re saying, but I’m not sure where you’re going with it."
    n "What I mean is that if you were with my sister, I’d at least know where you are every night."
    n "Because right now, I can't even walk down the hall without thinking, “I wonder which door he's behind?”"
    s "..."

    scene norikowalk19
    with dissolve

    n "Sorry."
    n "I knew that would be something you didn’t want to hear, but I went and said it anyway."
    n "I just miss you. That’s all."
    n "The best thing for me is really just whatever nets me the most time with you...because I have no idea if you’ll just disappear again one day or not."
    s "It's really unfortunate just how possible that is."

    scene norikowalk20
    with dissolve

    n "Disappearing?"
    n "But...why?"
    s "This might sound weird, but I could technically disappear at any moment whether I like it or not."
    s "But it wouldn’t be something like moving or running away from you or whatever it was that happened in the past."
    n "You’re not actually like, a ghost or something, are you?"
    n "Because that would make this a lot harder to explain to my parents when we start dating."
    s "I just mean that the next time I disappear, there’s a chance you will too."
    s "And everyone, really."
    s "I’m not exactly sure how it works."

    scene norikowalk21
    with dissolve

    n "I don’t know if I’m just too [young]to follow this train of thought, but you don’t look like you’re messing with me."
    n "What’s going on? What do you mean by all of us disappearing?"
    s "I’m just saying that when someone fades away, the world stops existing."
    s "If I “disappear,” everyone else also disappears because I’m not there to perceive them anymore."
    n "And you think that’s equivalent to them just not existing at all?"
    s "Right."
    n "Isn’t that like...super selfish?"
    n "Like, wouldn’t you care about what happened to me if you just vanished again? How I’d process all of that?"
    s "I know enough about you already to assume that you’d just start looking again."
    n "Well...yeah. Probably. But I wouldn’t be happy about it."
    n "What about Ami or Ayane, though? Or Maya?"
    s "Ami and Ayane would take it the worst."
    s "Maya would throw a party."

    scene norikowalk22
    with dissolve

    n "Huh."
    n "Guess a lot can happen in just a few years."
    s "Again, though, I think it would be closer to them all just disappearing as well."
    s "One goes out, another comes in. "
    s "Think of it like starting a brand new world with a brand new version of you and a brand new version of me."
    s "No one disappears. They just get recycled."

    scene norikowalk23
    with dissolve

    n "Okay, I’m lost. "
    n "I’m normally good with these sorts of topics and stuff, but what you’re describing sounds like something out of an anime."
    n "Or at least some religion I’ve never heard of before."

    "Given her ties to the past, I was hoping these words would have had some sort of impact on Noriko."
    "Like maybe, by some strange twist of fate, she’d acknowledge the possibility of the world resetting and memories being wiped."
    "But I guess I’m still not great at explaining things I don’t understand."
    "And it’s not like I’ve been gaining any useful information from Maya lately either, especially in her current state."
    "Oh well."
    "Back into the unknown then, I guess."

    s "I’ll just make things simple by saying...don’t worry about me disappearing again."
    s "I can’t say any more than that, but you seem naive enough to trust me on this."

    scene norikowalk24
    with dissolve

    n "I don’t have to be {i}naive{/i} to trust you, Sensei. I can just {i}trust{/i} you."
    s "If you want, sure. I just can’t imagine why you ever would."
    s "I’m not the same person-"
    n "You are."
    n "Now get back to giving me a tour of the area so I’m able to find an ATM without getting lost in the future."

    scene black
    with dissolve2

    "Everything is casual from that point on."
    "There are no further discussions on spirituality and the domino effect that would come with someone’s memory being wiped."
    "Just ATMs, streetlights, and the soft hand of a peculiar girl."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ norikodorm5 = True
    stop music fadeout 10.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label norikodorm10:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
...
```