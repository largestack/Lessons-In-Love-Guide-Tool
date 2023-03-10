# The Place She Falls Asleep At Night (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Tell Me When](./sarabar25.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: Three Amigos](./christmastwo1.md)

## Event properties

* Id: sarabar25p2
* Group: Sara
* Triggered by label: sarabar25
* Chain sources: sarabar25
* Chain sources path: sarabar25

## Official wiki page

[The Place She Falls Asleep At Night](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sarabar25p2&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label sarabar25p2:
    scene sarawindow1
    with dissolve2

    "I follow Sara over to the window and get my first ever look at the view from her...apartment or...condo or...you know what? I’m not really sure what to call it here."
    "The place she falls asleep at night."
    "Except for on the nights she doesn’t."
    "Believe it or not, I don’t have any idea what it’s like to be a single mother, so I’m not really sure how much something like that weighs on her ability to close her eyes."
    "I watch as her breath makes contact with the glass, fogging it up and forcing me into a rare memory of windows from when I was younger."
    "Just, in my mind, there’s no reflection staring back at me."
    "No array of city lights injecting their glow into my eyes through a reinforced, transparent pane serving as the one and only barrier between me and the puddle I’d be if I were to just fall through it."
    "I wonder if the fall would kill us from here."
    "Probably not, now that I think about it. "
    "This is only the second story. We’d have to land perfectly in order for that drop to end our lives."
    "I’m not sure why I’m thinking about this now, though."
    "Nor do I have any idea of why seeing her like this would make me {i}almost{/i} remember something from the past when I assumed it to be all but abandoned."

    sar "Do you notice anything different about me, Sensei?"
    s "Different?"
    sar "You don’t, do you?"
    s "Uhh..."
    sar "I let my hair down."
    s "..."
    sar "It was up just a minute ago."
    sar "Do you know what that means?"
    s "...Not really, no."
    sar "It means I’m more comfortable now."
    s "I had no idea you were so intimidated by your pint-sized daughter that it was actively affecting your comfort level."

    scene sarawindow2
    with dissolve

    sar "That’s obviously not what I meant. Of course I’m comfortable with Sana. "
    sar "I just mean that I’ve officially moved into “relax” mode...and that you being here and towering over me like that isn’t putting me on edge."
    s "I didn’t really expect it would. Based on past experiences, you might actually even be a little {i}too{/i} comfortable around me."

    scene sarawindow3
    with dissolve

    sar "Is there such a thing as that?"
    s "Yes. Yes, there is."
    sar "This feels nice, you know."
    sar "Not just standing here, looking out at the street like this...I’m talking about the entire night."
    s "Is this the part where you start trying to add me into your family again?"

    if sarasex == False:
        sar "It’s not."
        sar "You’ve already made it clear that you have no intention of ever looking at me that way."
        sar "But I can still feel happy right now even if we’re just friends, can’t I?"
        s "You can feel however you want to feel. It’s just not going to change how {i}I{/i} feel."
        sar "Then, as a friend, can I ask you a question?"
        sar "A real question. Not one about the two of us or...even helping out with the bar."
        sar "I just want to know how you feel about something."
        s "Then...by all means."
    else:
        sar "No..."
        sar "Yes..."
        sar "Maybe?"
        sar "I know you’re not looking for a real relationship right now, but I’d be lying if I told you it didn’t feel like the two of us were actually dating sometimes."
        sar "You really don’t think this would be nice? Ending every night with this view?"

        if bonus == True:
            sar "Hovering close enough behind me that you could pull me in and make me yours at a moment’s notice?"
            s "I mean, I’m pretty sure I could do that right now and you wouldn’t object in the slightest."
            sar "Tonight, I think I would, actually."
            s "Oh?"
            sar "Yeah..."
            sar "You see, there’s something that’s been on my mind for a little while now, and it’s something I couldn’t really just come out and ask in front of Sana."
            s "What do you mean?"
        else:
            s "I think that'd be pretty nifty. I'm still too scared of girls to want to date you, though."

    scene sarawindow4
    with dissolve

    sar "Do you think deciding to raise Sana on my own was the best thing to do after her father left?"
    sar "Or would it have been better to just find some other guy and pull him into the picture? Not out of love or anything, but out of...obligation? Is that the word I’m looking for?"
    s "That’s a pretty heavy question to just drop on me out of nowhere, Sara."
    sar "If you think that’s heavy, you’d be an even worse mother than I am."

    scene sarawindow5
    with dissolve

    sar "I knew it was going to be hard, you know. After he left."
    sar "But when you’re on your own and have to look after someone else, you need to carry so much weight that it feels like your arms are just going to...break off sometimes."
    s "I am well aware of how horrible a mother I would be, but I don’t really think it’s my place to tell you whether or not you should have just roped some unsuspecting guy in to help you."
    s "Especially not after directly proving how bad you are at choosing men."

    scene sarawindow6
    with dissolve

    sar "It’s not like I just asked Sana's dad to be with me one day, you know? He had just as much to do with it as I did."

    if bonus == True:
        sar "I didn't just wake up one morning and think, “I want to have a baby with my teacher.”"
    else:
        sar "I didn't just wake up one morning and think, “I wonder if he knows about the stork”"

    s "Based on personal experience, I’m not sure how honest that statement is."
    s "I feel like there are several girls in my class that think that first thing every morning."

    scene sarawindow7
    with dissolve

    if bonus == True:
        sar "And how many of them are you sleeping with?"
    else:
        sar "And how many of them are you hugging?"

    s "I hope that’s just a rhetorical question and that you’re not accusing me of anything right now."

    if bonus == True:
        sar "Well, based on {i}my{/i} personal experience, every high school teacher I’ve ever had has fucked me. So it’s not like it would be the most shocking revelation in the world."
        s "{i}Every{/i} teacher?"
    else:
        sar "Well, based on {i}my{/i} personal experience, every high school teacher I’ve ever had has hugged me. So it’s not like it would be the most shocking revelation in the world."
        s "Wow. It sounds like you were very popular and huggable."

    sar "Mhm. I mean, I only had one, but that’s still a 100%% success rate. Or failure rate, depending on how you look at it."
    s "Ahh. So it’s not just our high school that enforces that “One teacher for everything” policy."
    sar "Isn’t your high school the only that’s left in Kumon-mi now?"
    s "The other one still exists. It’s just at the bottom of a hole somewhere."
    sar "Aren’t we all?"
    s "Well, that’s a lot more negative of a statement than I’m used to from you."

    scene sarawindow8
    with dissolve

    sar "You know, I feel like for most mothers, there are a lot of memories that they look back on and smile."
    sar "But for me, it’s like every single memory I look back on is either filled with tragedy or just...me making some sort of mistake."
    sar "I tried really hard, too."
    sar "I really did."
    sar "And I’m still trying now. But it’s like every single day, I have to figure out how to tie a new knot around Sana so she doesn’t drift off and leave me completely and utterly alone."
    s "I doubt she’s-"
    sar "People leave me, Sensei. It’s what they do."
    sar "Sometimes it’s purposely, sometimes it’s not. But it happens."
    sar "I thought Sana’s father was different. I thought he was going to be there forever."
    sar "I thought all of those things he promised weren’t just empty words, but reflections of his heart even clearer than ours in this glass."

    if bonus == True:
        sar "But I guess having just one teenage girl to sleep with isn’t enough for some people."
    else:
        sar "But I guess having just one hug buddy isn’t enough for some people."

    sar "It’s like..."
    sar "It’s like all men start out great, but the second a kid comes into the picture, the worst parts of them come out and replace all of the good ones."
    s "I’m sure that happens the other way around, too, though."
    s "I’m sure there are just as many mothers who can’t handle parenthood as there are fathers."
    sar "Are you talking about me?"

    scene sarawindow9
    with dissolve

    s "No. All things considered, I think you did fine. Sana might be quiet and awkward, but she’s a good person. And you should be at least somewhat proud of yourself for that."
    sar "{i}Fine{/i} isn’t good enough for a childhood."
    sar "It could have been {i}better{/i}. Things could have been better."
    sar "She could have had such an amazing life if I had just been a little smarter when I was her age and waited for someone to {i}actually{/i} love me rather than just...pretend to."
    s "Maybe. But she’s only Sana because she exists now. If you had waited any longer, you could have wound up with a completely different kid."

    scene sarawindow10
    with dissolve

    sar "A...different..."
    sar "Umm...anyway...I just..."
    sar "I don’t...really know."
    sar "I didn’t have much of a childhood."
    sar "So when it came time to raise...children of my own, I just did whatever I wished would have been done for me when I was their age."
    sar "You know that thing that some parents do with their kids when they’re trying to teach them to swim? Like...how they just toss them into the water and let them figure it out on their own?"
    s "Wait, did you actually do that?"
    sar "Oh, no. I’m just using that as a metaphor."

    scene sarawindow11
    with dissolve

    sar "I was able to figure out how to swim eventually...and I was able to climb out of the pool...but it was only just barely."
    sar "And all the while, instead of anyone trying to help, it’s like they were watching me struggling for my life and either laughing or just walking away."
    sar "If I had someone...{i}anyone{/i} to lean on back then...I can only imagine how much happier Sana would be now."
    sar "And..."

    scene sarawindow12
    with dissolve

    sar "And..."
    s "..."
    sar "..."

    scene sarawindow13
    with dissolve

    sar "..."
    s "And what, Sara?"
    sar "..."
    sar "What were {i}your{/i} parents like, Sensei?"
    s "Mine? I don’t really remember."
    s "Why do you ask?"
    sar "Because you turned out to be a decent person."
    sar "And I guess I’m kind of wishfully thinking, in the nicest way possible, that your parents weren't all that great..."
    sar "And that you succeeded at becoming who you are in the face of people who doubted you..."
    sar "Or ignored you when you needed help the most..."
    sar "Or beat you for speaking out of line..."
    sar "Or beat you for staying out a little past curfew..."

    scene sarawindow14
    with dissolve2

    sar "Or beat you for ever even speaking at all!"
    sar "But you were just a little girl!"
    sar "And all you wanted was a place to come home to that you weren’t terrified of!"
    sar "No wonder I would stay out late!"
    sar "No wonder I needed help!"
    sar "It’s because I’ve been all alone since the beginning!"
    sar "Since before there were any kids involved!"

    scene sarawindow15
    with dissolve

    sar "And I just..."
    s "..."
    sar "I’ve never known what the {i}right{/i} thing to do is. So even if I {i}do{/i} the right thing, I’ll still wind up questioning myself."
    sar "I thought falling for an adult who understood the world would have been enough to help me get at least {i}that{/i} much."
    sar "To figure out how to...take care of someone else."
    sar "So that my children could come home and talk to me without having to wait their turn..."
    sar "Without having to worry about waking up an extra hour early on weekdays just so they can figure out how much makeup they need to cover black eyes or bruises."
    sar "I just wanted to be a good mom..."
    sar "That’s all I wanted..."
    sar "But..."
    sar "It's like the world didn't want me to be one."
    s "..."
    sar "..."
    s "That’s been the best sales pitch for turning me into an honorary Sakakibara yet."

    scene sarawindow16
    with dissolve

    sar "Pfft!"
    sar "I’m sorry. I’ve been really emotional lately. And waiting to pour all of that out on you instead of Sana is just one more potential mistake I’m making in the world of parenting."
    s "Not as big of a mistake as {i}actually{/i} inviting me into the world of parenting."

    scene sarawindow17
    with dissolve

    s "Listen, I’m not going to spend the next ten minutes trying to tell you that things are going to get better or that you’re safe now or anything like that-"
    s "Frankly, things could get even worse for you any day now."
    sar "Well, that’s not very reassuring."
    s "You’re right, it’s not. Sometimes, horrible things happen to people who don’t deserve them. And you’ve been on the receiving end of that for basically forever."
    s "But if it helps in the slightest to hear me say that {i}you don’t deserve it...{/i}"
    s "Well, that’s really all I can do."
    s "Any more consolation than that would just be pity, and I’m sure you don’t want any of that."
    sar "Oh, no. Pity away. This whole crying thing is actually kind of fun when my tears aren’t dripping into my wine glass."
    s "Then I guess it’s kind of good I’m such a horrible employee and didn’t get you a drink after all, huh?"
    sar "Yeah, I guess it is good."
    sar "This does mean that I’m going to have to fire you, though. Because not only will you not listen to your boss, but that obnoxiously handsome face of yours is starting to distract one of my employees."
    s "Damn Yuki. Spending all of her time fantasizing about me instead of learning how to mix drinks."
    sar "I’m not talking about Yuki, dummy."
    s "I know. But it’s common knowledge that you’re in love with me already and it’s no fun just pointing that out over and over."

    scene sarawindow18
    with dissolve

    sar "First off, rude."

    scene sarawindow19
    with dissolve

    sar "Second, I’m talking about my daughter."

    if bonus == True:
        s "Sana? I’m pretty sure her feelings for me are nothing more than “Please don’t bone my mom.”"
        sar "You know she has {i}my{/i} blood, right? There is no way that is the only thing she thinks about you."
        s "Don’t cancel out your daughter’s purity just because you were horny for your high school teacher."
        sar "Don’t expect her to be “pure” just because she’s tiny and quiet."
        sar "Who we are on the outside has absolutely no bearing on the versions of ourselves we keep locked away."
        sar "For example, I didn’t {i}look{/i} like a girl who was fucking the teacher. But just a few years later, I was begging him to stay while holding a baby with one hand and a carrot with the other."
        sar "In hindsight, the carrot probably made my plea look a little less serious, but the moral of the story is to expect the unexpected."
        sar "And also that carrots are the root of all evil."
        s "This conversation took a weird turn."

        scene sarawindow20
        with dissolve

        sar "All I’m saying is to not be surprised if Sana winds up being a little less pure than you expect her to be."
        sar "She’s still my daughter, and all she knows is what she’s grown up around. IE: Sex toys and romance novels."

        if bar50 == True:
            sar "Also, she asked me about condoms the other day and I’m still trying to figure out what that was all about."
            s "Wow, really? I have absolutely no idea why that is something she would have brought up to you."

        sar "Just..."
        sar "Don’t let her do anything stupid, okay?"
        sar "Don’t let her be another me."
        s "I can assure you that having your daughter harbor my children is at the very bottom of my to-do list."

        "Fucking her, on the other hand, is an entirely different story. But Sara just asked me to prevent her from doing anything “stupid” and I don’t think that’s stupid at all."
    else:
        s "Ewwwwwww, stop. I can't look at Sana that way. She's too...Sana."

    scene sarawindow21
    with dissolve

    if bonus == True:
        sar "Are you telling me you’d say no if a girl as cute as my daughter wanted to sleep with you?"
        s "My instinct here makes me want to tell you I {i}would{/i} say no...but I also think you might be the type to get insulted if I told you I wouldn’t."
        sar "You’re right. This {i}could{/i} go both ways, couldn’t it?"
        s "Can I just elect to not answer?"
        sar "What? You’re really not going to clear up that you wouldn’t have sex with my daughter if she asked you to?"
        s "Okay, fine. I wouldn’t have sex with your daughter if she asked me to."
        sar "Are you insane? She’s the cutest thing in the world. How dare you?"
        s "Wow. There’s really no winning this after all."
    else:
        sar "Are you telling me you’d say no if a girl as cute as my daughter wanted to hug you?"
        s "Maybe! I don't know! This is a lot of pressure, Sara!"

    sar "Whatever the case, just..."
    sar "Try and make sure she has a good life in school, okay?"
    sar "Despite how much I want to, I can’t watch her every hour of every day."
    sar "And..."
    sar "Well, let’s just say there aren’t a lot of people who could have survived what I went through in high school."
    s "That makes it sound like there was a little more pain than just a promiscuous teacher and abusive parents."
    sar "Of course there was."
    sar "I’m pretty sure I’m cursed."
    s "You really expect me to believe that?"
    sar "Not really."
    sar "But I wouldn’t expect anyone to believe it."
    sar "I wouldn’t expect anyone to believe or even {i}understand{/i} anything I went through back then."
    sar "And if keeping Sana happy will prevent her from ever being forced to endure any of it-"
    sar "Well, I’d do anything."

    scene sarawindow22
    with dissolve

    if bonus == True:
        sar "But, thankfully, she has a super great teacher who only {i}possibly{/i} wants to have sex with her! And I think that’s a good start!"
        s "Okay, so, remember how you were concerned a little while ago about what to do and {i}not{/i} do as a parent? I think this is “not do” territory."
        sar "Hey, I’m not the one doing anything. I’m just saying that us Sakakibara girls have both extremely high sex drives {i}and{/i} a thing for teachers. Do with that information what you will."
        s "Stop assuming the level of your daughter’s sex drive if you don’t want to negatively affect the way I think of her."
        sar "Negatively? I think my sex drive is one of my best qualities. Are you telling me that I should maybe consider {i}not{/i} wanting to have sex all the time?"
    else:
        sar "But, thankfully, she has a super great teacher who only {i}possibly{/i} wants to hug her! And I think that’s a good start!"
        sar "She takes after me, you know. Crazy hug drive. I can feel it."
        sar "Does it make you feel weird that I'm always thinking about performing the hug ritual?"

    if sarasex == True:
        s "No. You stay exactly the way you are."
        sar "Awwwww~ That’s a really cute thing to say for someone who doesn’t want to marry me yet."
        s "“Yet” kind of implies that I might eventually change my mind."
        sar "You will."
        sar "An angel told me."
        s "Sure thing, Sara."
        s "Sure thing."

        scene black
        with dissolve2

        if bonus == True:
            "I fight away the urge to take Sara back to her bedroom as I remember what she said a little earlier about not wanting to go down that path tonight."
            "And while it’s a minor inconvenience to me, I can’t blame her for the desire to feel wanted in a way that doesn’t end up with semen oozing out of her for once."
            "Especially since it’s clear now that that’s all she’s ever wanted."
            "Not the semen part- but the part where she can look out at the city like this and think to herself, even if only briefly, “This is nice.”"
            "And it is. That much, I will concede."
            "But, just as all things must, our time together comes to an end."
            "..."

        "On the way down the creaky staircase of the bar, the one that I’d still be able to make my way up even if it were destroyed, I have a thought-"
        "How happy would Sara be if I elected to stay the night?"
        "Not as a sexual partner, but as someone who genuinely wants to be near her. And hear more about the atrocities that plagued her when she was younger- still not relenting all this time later."
        "I’m sure she’d love that."
        "But, just as I’m about to turn around and turn that hypothetical scenario into reality-"
        "One of her stairs cracks."
        "And I no longer feel comfortable enough to go back up."
        "........."
        "......"
        "..."

        $ renpy.end_replay()
        $ sara_love += 2

        "{i}Sara’s affection has increased to [sara_love]!{/i}"

        scene sarawindow23
        with dissolve2

        "I wind up somewhere vaguely familiar on the way home."
        "I know I’ve been here before, but I can’t remember when."
        "And, unfortunately, I can’t quite remember how to get back or...when I even started heading here instead of just taking the normal path home."
        "Thankfully, my phone still has a little battery left and-"

        q "Are you lost?"
        s "..."

        scene black
        with dissolve2

        "{i}The happiest day -- the happiest hour{/i}"
        "{i}My sear'd and blighted heart hath known,{/i}"
        "{i}The highest hope of pride and power,{/i}"
        "{i}I feel hath flown.{/i}"
        "{i}For on its wing was dark alloy,{/i}"
        "{i}And, as it flutter'd -- fell{/i}"
        "{i}An essence -- powerful to destroy{/i}"
        "{i}A soul that knew it well.{/i}"

        scene sarawindow24
        with dissolve2

        s "..."
        q "..."
        s "Who are you?..."
        q "A girl, obviously."
        q "Have you ever seen one before?"
        s "I see many of them every day."
        q "Oooooh, a sarcastic type, are you?"
        q "And here I was ready to give you directions."
        s "I’ll be fine. I can just use the GPS app on my phone."
        q "Hmmmm..."
        q "Are you sure about that?"
        s "Yeah, I-"
        s "Wait, when did it die? My battery was fine like a second ago."

        "I try pressing the power button on my phone to see if I’d just accidentally turned it off or something, but there's no luck."

        q "Funny how things work out sometimes, huh?"
        q "And when you least expect it, too."
        s "How did you know my phone was dead?"
        q "Hmmm..."
        q "A guess?"
        s "I’m not sure if I believe that."
        q "You can believe whatever it is you want to believe."
        q "That’s the best part of being alive. Isn’t it, Sensei?"
        s "...How do you know my name?"
        q "Your name is Sensei?"
        q "I just thought you looked like a teacher."
        s "I didn’t realize you could “look” like a teacher."
        q "It’s the glasses."
        q "So, do you want me to tell you the way back or not?"
        s "How do you even know where “back” is?"
        q "You’re sure asking a lot of questions for some random guy alone in the middle of nowhere."
        s "And you’re sure acting suspicious for a teenage girl alone in the middle of the night."
        q "I think I'm acting completely normal, thank you very much."
        q "You're the weird one."
        s "Then...since we’ve finally gotten our introductions out of the way, can you tell me how to get back now?"
        q "Sure."
        q "But you’re going to owe me a drink if we ever bump into each other again, got it?"
        s "Whatever you say."
        s "So, where do I go?"
        q "First step-"
        q "Close your eyes."
        s "What?"
        q "Just listen to me. I know what I’m talking about."

        scene black
        with dissolve

        s "Fine. Whatever. I’ll play along."
        q "Great! Now, spin around three times and say “Olly olly oxen free!”"
        q "Oh, then jump as high as you can. Like, really, really high."

        scene bedroom_night
        stop music

        s "Listen, if you’re just going to-"
        s "..."
        s "What?"

        "I look down to find my phone in my hands once again."
        "The battery isn’t dead anymore."

        s "..."

        "What just happened?..."

        scene black
        with dissolve2

        "I take a moment to collect my thoughts, but I’m unable to find them all."
        "Then, not knowing what else to do this late at night, I make the executive decision to rule my strange meeting with that girl as just yet another blackout."
        "Just..."
        "It felt so much different than all of the others."

        $ anewkey = True
        $ sarabar25p2 = True

        "........."
        "......"
        "..."

        if day == 7:
            jump advancetomon
        if day == 1:
            jump advancetotues
        if day == 2:
            jump advancetowed
        if day == 3:
            jump advancetothurs
        if day == 4:
            jump advancetofri
        if day == 5:
            jump advancetosat
        if day == 6:
            jump advancetosun

    else:
        s "With me? Yeah. I think I’ve made that pretty clear."
        sar "Hey, you don’t have control over my thoughts."

        if bonus == True:
            sar "I’m allowed to {i}want{/i} to have sex with you all the time. I’m just not allowed to actually do it."
            s "What a convenient loophole."
            sar "{i}Speaking{/i} of convenient holes..."
            s "..."
            sar "..."
            s "You’ve been spending too much time with Maki."
        else:
            s "I do now!"

        scene black
        with dissolve2

        if bonus == True:
            "I don’t stay much longer."
            "As I head for the door, I hear Sara mention something along the lines of not thinking she’ll be able to fall asleep tonight."
            "I don’t ask why, as I’d like to leave it open ended."
            "If I heard the real answer, it might spoil my walk home."
            "So, in blissful ignorance of the horrible things I’m sure she’ll feel, I’ll force myself to pretend that the reason for her insomnia is me."
            "And that all of the darkness fermenting within in her will be replaced by the illusion of my seed- filling her insides with not only warmth-"
            "But her neverending desire to know what it means to be loved."
            "But that, just like everything else-"
            "Is an illusion."
        else:
            "I cast a spell on Sara that allows me to ready her mind."
            "{i}Sensei has gained the ability [[Mind Reading]!{/i}"

        $ renpy.end_replay()
        $ sara_love += 2
        $ sarabar25p2 = True
        stop music fadeout 10.0

        "{i}Sara’s affection has increased to [sara_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label saralust20intro:
...
```

## Code that triggers this event

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
sa "And even then, you’ll have to swim away with it dangling off of your lip, hanging there until the day you die."
            s "..."
            sa "I have to leave now."
            sa "And..."
            sa "And I want you to come with me."
            sa "But you won’t, will you?"
            s "..."
            sa "..."
            sa "I..."

            scene saranewapt30
            with dissolve

            sa "I’m fine with not having a dad, you know."

            play sound "dooropen.mp3"
            scene saranewapt31
            with dissolve

            s "..."

            "And just like that, Sana leaves."

            scene black
            with dissolve2

            "It’s a strange note to part on, but I think I understand what she means."
            "And it’s not all that different from what she’s been slowly but surely trying to help me understand for a while now."
            "She has no intention of ever accepting the life her mother wants for her. Or, for {i}us{/i}, rather."
            "I’m not sure when I started being included, but it’s pretty much inevitable that it’ll just keep going on forever at this point."
            "Sana doesn’t want me to be here right now-"
            "But she knows that it’s not her place to drag me along with her."
            "And so she’s trusting me, something I wouldn’t recommend to anyone, to not do something that will hurt her."
            "Or-"
            "At least that’s how I’m interpreting it."
            "But, for all I know-"
            "I could very well be wrong."
            "And I could very well hurt her even when I do everything in my power to avoid that."
            "That’s...just the way things are sometimes."

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

            jump sarabar25p2
        else:
            s "You mean when you got into a fight with your mother's dresser?"
            sa "I think...I think it wants a rematch..."
            s "Are you ready? Have you been training?"
            sa "That's...kind of what I need your help for."
            sa "Can you send me...um...videos of people you think are really strong when you get home tonight?..."
            s "Of course, Sana. Good luck with your battle."
            sa "Th-Thanks..."
            sa "Also...try not to hug my mom tonight..."
            s "I will only hug her if she wants me to."
            sa "Ugh..."

            scene black
            with dissolve2

            $ renpy.end_replay()
            $ sana_love += 1
            $ sarabar25 = True

            "{i}Sana’s affection has increased to [sana_love]!{/i}"
            "........."
            "......"
            "..."

    else:
        "It doesn’t last much longer and, once it’s over, Sana gathers her things and heads for the door."
        "She looks back at me and, strangely enough, in the one second of eye contact that I make with her, it seems like she’s telling me that she trusts me."
        "I’m sure it’s not easy for her to just leave me alone with her mother when she’s fully aware of her feelings for me-"
        "But it’s something she elects to do regardless."
        "I’m not sure what I did to deserve this, but I’m not about to make a break for the door to see if she’s really okay with leaving two adults alone in a dark room together."
        "And hey, maybe it’s something even less exciting?"

        if bonus == True:
            "Maybe trust has nothing to do with it and Sana just has absolutely no romantic or sexual feelings for me, making this just an average, everyday goodbye."
        else:
            "Maybe trust has nothing to do with it and Sana just has absolutely no feelings for me whatsoever?"

        "And, if that’s the case-"
        "So long, Sana."
        "Have a safe trip home- and don’t think too much about whatever you expect to happen in this room."
        "I’m sure that whatever comes next will be something you didn’t really want to be here for anyway."

        $ renpy.end_replay()
        $ sarabar25 = True

        "........."
        "......"
        "..."

        jump sarabar25p2
...
```