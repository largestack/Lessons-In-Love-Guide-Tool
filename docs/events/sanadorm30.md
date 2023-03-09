# Tortoises and the Concept of Friendship
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm30&go=Go)



## Event preconditions
✅Sana love greater than or equal to 30

✅Event "[Sana: Self-Medication](./bar30.md)" is completed (event=bar30)

✅Day of week is not Thursday



## Next events
None

## Event properties
* ID: sanadorm30
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm30:
    play sound "knock.mp3"
    stop music fadeout 10.0

    s "Hey, Sana. Are you around?"

    "I knock on Sana’s door and instantly hear the volume from her TV turned down a few notches."

    sa "Sensei?..."
    s "Correct. What other male would be visiting you in the middle of the night?"
    sa "Maybe it’s my...secret boyfriend..."
    s "Don’t joke about things like that. My heart isn’t prepared for it."

    "I can hear her giggle in response as she mutes whatever show she’s watching, followed by the faint tapping of her footsteps as she comes to the door."

    play sound "lock.mp3"

    sa "You can come in..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I pull open the door and walk into Sana’s room to find it devoid of virtually all light save the glow of the TV and a few stray rays of moonlight creeping in through the blinds."

    scene sanatv1
    with dissolve
    play music "love.mp3"

    s "I’m not interrupting anything, am I?"
    sa "You are...but it’s okay."
    sa "I was just watching a movie."
    s "No Ayane tonight?"
    sa "Is that...why you’re here?"
    s "If I was here to see Ayane, why would I have shouted your name when I knocked on the door?"

    scene sanatv2
    with dissolve

    sa "Good point..."
    sa "But yes...no Ayane. She had to go home for something tonight."
    s "Home as in...Amamiya mansion-home?"
    sa "That...is her home, so yes..."
    s "Oh. Well hey, that just means more time for the two of us to be alone together, right?"

    scene sanatv3
    with dissolve

    sa "Right...so no funny business."

    if bonus == True:
        s "But being alone is the best possible time for funny business."
        s "The lights are off and everything."

        scene sanatv4
        with dissolve

        sa "If you’re going to be in that kind of mood...maybe it’s best if I just watch my movie alone..."
        s "Wait, no. I’ll be good. I promise."
    else:
        s "I wouldn't ever dream of it. I value you far too much and will be on my best behavior."

    scene sanatv5
    with dissolve

    sa "You better be...this is one of my favorite movies..."
    sa "I’ve seen it a million times so we can still talk but..."
    sa "Try to touch me and I’ll...cut your hands off..."
    s "Don’t tell me you’ve been hanging around Yumi now, too, have you?"

    if bonus == True:
        s "Actually, wait. She would have threatened to cut something else off instead."

    scene sanatv2
    with dissolve

    sa "Is it...okay if I sit back down now? Or do you want to keep talking about Yumi?..."
    s "Oh, feel free. I’m perfectly content with never bringing her up again."
    sa "That sounds...kind of rude. But I get it.."

    scene sanatv6
    with fade

    "Sana hops onto her bed and curls up into a ball, nearly knocking over the plate of food in front of her."
    "Her eyes immediately focus in on her movie where-"

    s "…"
    sa "…"
    s "Why is that guy sawing off his leg?"
    sa "It’s the only way he can free himself."
    s "I feel like there has to be an easier way to do that."
    sa "Well...there {i}was{/i}. But it kind of went down the drain at the start of the movie..."
    s "Oh...I see."
    sa "That would be...a really funny joke for anyone who’s seen this before..."
    s "I don’t doubt it."
    s "I had no idea you were into stuff like this, though, Sana."

    scene sanatv7
    with dissolve

    sa "I love horror movies! They’re my...absolute favorite!"
    sa "Ayane and I try to watch one together every weekend when she isn’t with Ami and Maya."
    s "And on the nights she is, I’m guessing you just watch them alone?"

    scene sanatv8
    with dissolve

    sa "Well, yes...But you don’t need to make me feel like a loser because of it..."
    s "Oh, I wasn’t trying to. I’d be more than happy to come over and watch stuff like this with you when your normal partner is away."

    scene sanatv7
    with dissolve

    sa "Really?!"
    sa "I mean...Rin already said she wouldn’t mind coming either but..."
    sa "On days that both her and Ayane can’t make it, I’ll keep you in mind!"
    s "Well...thank you for making me your second backup plan?"
    sa "Of course!"

    scene sanatv9
    with dissolve

    sa "I’m glad you don’t think it’s weird, though..."
    sa "Some people see stuff like...gore and...blood and whatnot and they get scared or grossed out."
    sa "But none of that bothers me at all. I actually really like blood."

    scene sanatv10
    with dissolve

    sa "Oh, but I mean like...movie blood. And video game blood, too, thanks to Rin."
    sa "I had no idea how much I’d like shooting people until she showed me the light."
    sa "Real blood is still kind of gross, though. "
    s "I would certainly hope you weren’t also intrigued by the blood of real human beings. "
    s "I was beginning to think that whole thing about cutting off my hands might be true."

    scene sanatv11
    with dissolve

    sa "Heheh...maybe it is?..."
    sa "People can get crazy ideas from watching movies and playing games, Sensei..."
    sa "Do you have...any idea how many lives I have watched end? How many I’ve taken myself?..."
    s "You know, it’s finally starting to make sense why you chose the ogre warrior in that game you guys played on the beach."

    scene sanatv12
    with dissolve

    sa "I wasn’t an ogre warrior...I was an orc barbarian..."
    s "Aren’t they the same thing?"
    sa "No. Ogres have layers."
    s "What does that even mean?"
    sa "Like an onion. Layers..."
    s "...Yeah, I still don’t get it."

    scene sanatv9
    with dissolve

    sa "Then we’ve got another movie to watch after this one..."
    sa "The next one isn’t really scary, though."
    sa "Unless you’re afraid of donkeys..."
    s "They’re actually my biggest fear."

    scene sanatv13
    with dissolve

    sa "Really?...That’s strange...Did something happen with a donkey when you were younger?..."
    s "Sana, I was obviously kidding."

    scene sanatv14
    with dissolve

    sa "B-But...you sounded so serious!"
    sa "And the look in your eyes clearly said “I hate donkeys!”"
    s "My biggest fear is dying. Donkeys are like, seventh on the list."

    scene sanatv12
    with dissolve

    sa "Everyone is afraid of dying...that doesn’t count."
    sa "I’m moving donkeys up to sixth place."
    s "If that’s what makes you happy, feel free."
    sa "It would make me happier if they were first place and you didn’t lie to me..."
    s "Why are you so upset about this? I lie to you all the time."

    scene sanatv14
    with dissolve

    sa "What?! Why?!"
    sa "What did I ever do to you?!"
    s "Again, I’m only kidding..."
    s "When is Rin going to teach you about picking up on peoples’ cues?"
    s "She seems to have been doing a fine job in coaxing you out of your shell, but you’ve clearly still got a ways to go."

    scene sanatv15
    with dissolve

    sa "Leave me alone. I like my shell..."
    sa "Tortoises live for...hundreds of years, you know..."
    sa "Do you have any idea how often they come out of their shells? Never."
    sa "Also, tortoises aren’t...pressured to make friends with all of the other tortoises..."
    s "Do tortoises even understand the concept of friendship?"
    sa "Probably...they’re wise and...have plenty of time to learn."
    s "Okay, okay. Sorry for telling you that you still have a ways to go. "
    s "You’ve improved a lot. Really."

    scene sanatv9
    with dissolve

    sa "Well...thanks...But I was only kidding anyway."
    sa "If my teacher says that I should become more social, I owe it to him to do that..."
    s "Why are you talking about your teacher in third person? {i}I'm{/i} your teacher. And I’m right here."

    scene sanatv16
    with dissolve

    sa "Obviously because it’s embarrassing..."
    sa "I embarrassed myself enough the last time you saw me drinking..."
    sa "I need a cooldown period before I’m able to do something like that again..."
    s "I’m not really sure how getting drunk and opening up about yourself is as embarrassing as thanking me for being your teacher, but sure."
    sa "Everything is embarrassing if it’s something you’re not used to saying...or doing..."
    sa "Even now, I’m embarrassed just to be sitting next to you..."
    sa "I can’t even eat my dinner because...my hands are shaking so much..."

    "Now that she mentions it, I can notice that she's quivering, albeit only slightly."
    "Having her hands tucked into her sleeves definitely helps hide it, but knowing that it’s going on has made it incredibly more apparent."

    s "Should I get off of the bed? I know you always prefer to sit on the couch when we’re together."
    sa "…"
    sa "No, it’s okay..."
    sa "As long as you count this toward my tortoise."
    sa "I mean shell."
    sa "Count it toward my shell."
    sa "The...thing I’m coming out of."
    s "Right..."

    scene sanatv17
    with dissolve

    sa "I’m not doing a very good job, am I?"
    s "I’m not here to judge. I’m just here to talk to my favorite closet-horror freak and watch some guy chop his appendages off."
    s "Normal teacher stuff."

    scene sanatv18
    with dissolve

    sa "Heheh...Yeah. Normal teacher stuff."
    s "…"
    sa "…"

    "The two of us sit in silence for another few moments as the movie carries on. "
    "Even though she’s constantly draped in black and her wall is covered in spider stickers, it’s definitely a little weird seeing Sana’s eyes light up every time a closeup of something gory happens on the screen."

    if bonus == True:
        "She’s like a kid in a candy shop. Just she’s a little past kid-age and the candy is dismembered body parts."
    else:
        "She’s like a kid in a candy shop. Just she’s well past kid-age and the candy is dismembered body parts."

    "But hey. To each their own, I guess."
    "I’m into [teenage]girls and Sana’s into dead people. "
    "That’s just the way the cookie crumbles."

    sa "You’re...a good second backup, Sensei..."
    sa "Thanks for watching the movie with me."
    sa "Things like this...are a lot more fun when you have friends with you."
    s "Like you said before, feel free to reach out whenever everyone else can’t make it."
    s "I’ll drop whatever I’m doing and the two of us can watch more people disfigure themselves in order to survive."
    sa "That’s the most...romantic thing anyone has ever said to me..."
    s "Well try not to fall too hard, got it?"

    scene sanatv19
    with dissolve

    sa "Heheh...in your dreams..."
    s "…"
    sa "…"
    s "Are you winking at me? I really can’t tell with your hair in the way, but I think you are."

    scene sanatv17
    with dissolve

    sa "Umm...yeah...I was winking..."
    sa "I guess I should probably cut my hair soon, huh?..."
    sa "Even my facial expressions are becoming hard to read..."
    sa "Communication is difficult enough as-is..."
    s "Please don’t cut your hair. I think you’re adorable this way."

    scene sanatv14
    with dissolve

    sa "Ah! Bed! Compliments! No! Bad!"

    scene black
    with dissolve2

    "The movie comes to an end not long after that and, just like she said she would, Sana puts on the movie that is meant to introduce me to ogres."
    "After roughly thirty minutes, I come to the conclusion that I would much prefer horror movies over whatever this is."
    "Also, donkeys move up several spots on my list of most-feared things."
    "Oh, and this happens as well."

    scene sanatv20
    with dissolve

    "Sana winds up passing out very early on and eventually, albeit unconsciously, finds her way into my lap."
    "It was easy to tell she was going to pass out sooner or later, given that her head kept bumping into my shoulder while she was nodding off."
    "And each time that happened, she’d apologize and say it was just an accident."
    "Well, in the end, it appears that she ran out of accidents and now my hand is falling asleep as her body is cutting off the blood flow I need to keep it running."
    "Woe is me, I guess."
    "I’m impressed that I can still find something to complain about even with a cute girl asleep on top of me."

    scene black
    with dissolve2

    "I somehow manage to make it through the movie."
    "Sana never wakes up."
    "Well, not while I’m there, at least."
    "I imagine she’ll wake up tomorrow."
    "It would be a real bummer if she doesn’t."
    "How would I explain that to the police?"
    "…"
    "I manage to get her off of me without waking her up and pull her blanket over her."
    "And, last but not least-"
    "I box up the dinner she never ate and take it home with me as a reward for learning about ogres."

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm30 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanecowgirlrep:
    play sound "knock.mp3"

    ay "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        jump ayanecowgirlrepx
    else:
        $ ayane_lust += 1
        stop music fadeout 5.0

        "{i}Ayane's lust has increased to [ayane_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label ayanedorm25:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
    if sana_love >= 25 and bar25 == True and beachvacation16 == True and sanadorm25 == False:
        jump sanadorm25
    if sana_love >= 30 and bar30 == True and day != 4 and sanadorm30 == False:
        jump sanadorm30
...
```