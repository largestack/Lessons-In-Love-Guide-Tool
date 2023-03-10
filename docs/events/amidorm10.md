# No One Can See Us (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 10

* Day of week is a weekend

* Event [O World](./day60.md) (Main) is completed)

* Event [Home Away From Home](./amidorm5.md) (Ami) is completed)

* Event [No Romeo](./day24.md) (Main) is completed)

* Event [Something Darker](./amisroom10.md) (Ami) is completed)



## Next events

* [Ami: Back Out in the Heat](./amidorm15.md)

## Event properties

* Id: amidorm10
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm
* Triggered by path: amidorm->amidorm10

## Official wiki page

[No One Can See Us](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm10:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Ami's door and wait for her to answer."
    "I wound up getting sidetracked and showed up a bit later than usual tonight."
    "I wouldn’t be surprised if Ami and Maya were already getting ready to go to bed at this point."

    a "Sensei?..."
    a "Is that you?"
    s "It is."

    "I hear a deep breath from behind the door."
    "Ami holds the air in for several seconds before letting it back out."
    "After that, she lets something else in."
    "Something that, unlike oxygen, will only kill her in the end."

    a "The door is open."

    scene black
    with dissolve2

    "I grip the handle."
    "I open the door."

    scene amidormten1
    with dissolve2
    play music "sensei.mp3"

    "And I come face to face with a girl who loves me more than anyone."

    a "Hey...What are you doing here so late? I didn't think you were going to show up today."
    a "Especially since it's...the weekend and everything."
    s "What would it being the weekend have to do with whether or not I come here?"
    a "It's just...well, you normally do {i}other{/i} stuff on the weekends, don't you?"
    s "Just out of curiosity, what sort of life do you think I live when I'm away from you?"

    scene amidormten2
    with dissolve

    a "Idunno. But whatever it is, I hope it’s something I’d approve of."
    a "Remember that if anything bad ever happens to you, it's kind of like that bad thing is happening to me as well."
    a "So...make sure you’re staying safe out there. And don’t forget to check in every once in a while."

    if bonus == True:
        s "Sometimes, I feel like you’re even more of a parent than I am."

        scene amidormten3
        with dissolve

        a "Hahah...I don't really know about that..."
    else:
        s "Thank you, Ami. You are always looking out for me and I greatly appreciate it."
        s "Just don't tell me you love me because it makes me nervous and I will be forced to respond in kind so I do not damage your feelings."

    scene amidormten2
    with dissolve

    a "I just love you a lot and felt like reminding you, that’s all."
    s "Thanks, Ami."
    a "Thanks Ami {i}what?{/i}"
    s "..."
    a "...?"

    "I sigh to myself, knowing full well what she wants to hear."

    s "I love you too."

    if bonus == False:
        "Damn it. It has happened again."

    scene amidormten3
    with dissolve

    "I mask the reluctance in my voice by reaching out and ruffling Ami’s hair, and she rubs her head against me like a cat excited to be pet after a long day away from its owner."
    "Honestly, at this point, I don’t think I’m going to be able to avoid saying I love Ami. Not when she's...not only dependent on it, but..."
    "I mean...just look at how happy she is right now."
    "From nothing more than three words."
    "I don't get it."

    a "Heheh...If you don't cut it out, my hair is gonna be all crazy tomorrow. "
    s "Did you just take a shower? It's wet."
    a "Mhm. And you should know by now how long it takes for my hair to dry."
    s "Well, you've got more of it than basically everyone else in the class combined so...yeah. That's going to happen."

    "I ignore Ami's suggestion to stop messing with her hair and take even more of it into my hands, letting it fall through my fingers like-"
    "Like-"
    "_____________"
    ##LIKE HERS???
    "I had a thought, but the thought went away."
    "Ami lets out a sigh, finally opening her eyes an...uncertain amount of time later."

    scene amidormten4
    with dissolve

    a "Oh well...I guess I can’t stop you from messing with me even if I try."

    if bonus == True:
        s "That’s right. You’re my [niece], which means I can do whatever I want to you, {i}whenever{/i} I want to."
        a "Hahah...Well...You're definitely not wrong about that."
    else:
        a "I am your accountant after all. And some would say that's like having no hair whatsoever."
        s "Who would say that? I have never heard that before."
        a "(Airplane noises)"

    s "Where's Maya, by the way? I figured she'd be here right now with how late it is."

    scene amidormten5
    with dissolve

    a "Maya’s...actually staying somewhere else tonight...So I’m here alone."
    s "Really? Where is she-"
    a "Can we not talk about Maya right now, please?"
    s "Oh. Uhh...I'm sorry?"

    scene amidormten6
    with dissolve

    a "You don't have to {i}apologize.{/i} It's just..."
    a "Don't you maybe wanna ask me about, like...if I’m comfortable being here by myself? Or...something like that?"
    s "I mean, I’ve been late coming home a few times in the past and you’ve never really said anything about it."
    s "Is being alone something you’re afraid of?"

    scene amidormten6r
    with dissolve

    a "Without really getting into it...it's probably my biggest fear of all."
    a "Just...not really in the way you're talking about. You know?"
    s "..."
    a "And...And it's not like I {i}enjoy{/i} being alone. So even if I'm not scared, that doesn't mean I want things to stay like this."
    s "I’m sure you could always ask to crash with one of the other girls. I can't imagine they'd have a problem with-"

    scene amidormten6
    with dissolve

    a "I think I'd...prefer if {i}someone else{/i} stayed here with me instead."
    s "…"
    a "…"
    s "Is that an invitation?"
    a "If I say yes...will you stay with me tonight?"
    s "Sure. But, just to be sure, you’re positive Maya's not coming back, right? Because I can't imagine she'd be happy to find me here at this hour."

    scene amidormten6r
    with dissolve

    a "Didn't I ask you not to talk about her right now?"
    s "I didn't mean anything by it. I'm just trying to make sure we don't wind up in the middle of some misunderstanding."
    a "{size=-15}Would it really be a misunderstanding?{/size}"
    s "What was that? I couldn't-"

    scene amidormten6
    with dissolve

    a "Umm...if it’s okay with you...I thought it might be nice if the two of us...slept in my bed together."
    a "I know it's small and that it would make more sense for you to just sleep in Maya's, but..."
    a "I really want to be with you tonight, Sensei."
    s "I’m fine with that. Are you sure you're comfortable with it, though?"

    scene amidormten7
    with dissolve

    a "O-Of course I'm comfortable with it! We've been doing that sort of thing forever, haven't we?"
    a "Just think of...how many times I've fallen asleep in your arms and..."

    scene amidormten6
    with dissolve

    a "And how safe they made me feel..."

    if bonus == True:
        a "Remember when you cuddled me on the couch the other day? I loved that. And I was able to fall asleep right away."
        a "So...if you cuddle me again..."
        a "I, ummm..."
    else:
        a "Like when you reached into my trachea the other day...I was able to fall asleep right afterward."
        a "So I was kind of hoping you could maybe, like...get the rest of the colors out or..."

    a "You're not really going to make me spell it out for you, are you?"

    "As much as I would love having her 'spell it out' for me, she obviously doesn’t have to."
    "Is an open invitation to sleep in her bed strange considering she's a teenage girl and I'm nothing more than a secondhand, stand-in father with the faintest trace of my blood somewhere inside of her?"
    "Yes."
    "It would be one thing if she were still much younger."
    "It would be one thing if she were too young to recreationally entertain the thought of the two of us as anything more than what we truly are."
    "But I guess that what we truly are on the inside is just a mess of veins and arteries coursing through us like wires. Machine hearts and mechanical brains- all incessantly malfunctioning."
    "What we truly are is empty despite even those artificial components."
    "But if we latch on tightly enough to one another, we might be able to make one whole machine."
    "I guess when you look at us as nothing more than different coats of carbon, the parts we wish to exchange with one another don't mean much."
    "I guess when you look at us as nothing more than two uniquely shaped masses of flesh that we can spill ourselves all over one another and it won't mean anything."
    "So, no. This girl does not need to spell anything out for me."
    "For there are not enough letters in the alphabet to properly convey the thoughts that I have and desires I must either suppress or fall victim to here in this very bedroom."

    a "Umm...Sensei?..."
    s "..."
    a "..."
    s "Let's go to bed."

    scene black
    with dissolve2

    if bonus == True:
        "Ami gets on the mattress first, but she doesn't retreat beneath the covers."
        "I do the same and, soon enough, the disgusting misled lifeforms we are begin to merge into one horrific monstrosity of forbidden desire and untapped passion."
        "She faces me and pierces through my skull with the most beautiful eyes I have ever seen."
    else:
        "........."
        "......"
        "..."

    play sound "static.mp3"
    scene whygodwhy with flash
    scene whyme with flash
    scene amidormten8 with flash
    stop sound

    "Do you believe in God?"
    "I like to say I don't, but the truth is I am scared."
    "I am scared that he or she or it or they or that might exist."
    "And I am scared that these eyes belong to him or her or it or them or that."
    "There is no other explanation for how much of the world I see inside of them."

    a "…"
    s "…"

    "I lose track of how long we stare at each other for."
    "For all I know, we could be days into this exchange right now- locked in a state of stasis that will soon spell our undoing as it is us alone that have ceased to be."
    "Soon, I will need to make a decision."
    "I can feel it approaching quicker than the expedited delivery of blood from my machine heart through the wires of my body."
    "I can feel the earth begin to shake."

    play sound "static.mp3"
    scene amidormten9 with flash
    stop sound

    a "Hi..."
    s "Hey..."
    a "This feels kinda weird, doesn’t it?"
    a "Should I turn around?"
    s "You can do whatever you want. I don’t really care."
    a "Really?"
    a "I think...I’ll stay like this for a little while then."
    s "This isn't too romantic for you?"
    a "What if I want it to be romantic?"
    s "Then you have a problem."
    a "So do you, Sensei."
    a "We're each others' problems."
    a "But no one can see us in here."
    a "It’s like our own little world."

    scene amidormten10
    with dissolve

    a "But...you know what?"
    a "Even if anyone {i}could{/i} see us in here...I wouldn't care at all."
    a "You’re my favorite person in the entire universe. And as long as you’re happy here, I’m happy."

    scene amidormten11
    with dissolve

    a "Are you happy here, Sensei?"
    s "What does it mean to be happy, exactly?"
    a "Can you answer my question first before asking something that big and vague?"
    s "Not without understanding it."
    a "Then...isn't being happy just...not worrying about anything?..."
    a "Come to think of it, describing happiness is kinda hard, huh?"
    s "Are you worried about anything right now, Ami?"
    a "I'm not."
    a "Are you?"
    s "I'm not."
    a "So...does that mean you're happy then?"
    s "..."
    a "..."
    s "As close as I’ll ever be, I guess."
    a "Oh yeah? You can’t get any closer?"
    s "There's not really any way of knowing until I get there, right?"
    a "Hmm..."
    a "I have an idea."

    scene amidormten12
    with fade

    "Ami gets even closer to me and entangles her fingers with mine."
    "I think of them like enoki mushrooms, poking out of the ground and invading the garden that is the same hand I use to pleasure myself to all types of horrible thoughts."
    "Even ones like this."
    "Ones that don't belong anywhere near this fragile creature."
    "Ones that I will force on her regardless because the light of her prism is so faded that it appears as if she wants them."
    "Her face is close enough for me to taste the mint of toothpaste clinging to the air periodically pushed out from between her lips in between breaths."
    "I wish she'd hold it in."
    "I wish she'd stop holding me."

    a "Are you happier yet?"
    s "You think my happiness is in direct relation to how close we are?"
    a "I think {i}my{/i} happiness is in direct relation to how close we are. And I think that you're just like me, sooooo..."
    s "Maybe you're right, then."
    a "Heheh...I thought so."
    s "..."
    a "..."
    a "I’m {i}really{/i} happy right now, Sensei."
    a "I wouldn’t mind staying like this for the rest of forever."
    a "Or at least until Maya gets back."
    s "You're not supposed to be talking about Maya right now."
    a "Right, right. Sorry."
    a "Here's another idea, then."
    a "How about we play a little game?"
    s "What kind of {i}game{/i} did you have in mind?"
    a "A question game. We both have to ask each other something, and we need to answer as honestly as possible or the other person can do whatever they want to the liar."
    s "Hmm..."
    a "Sounds fun, right?"
    s "Why don't we just watch TV instead?"

    scene amidormten13
    with dissolve

    a "Hey, come on! My idea is way better than that!"
    s "How can you be so sure that hearing the truth from me is what you {i}want{/i} to hear?"
    s "What if the question you ask me is one of many situations in life where lying would be better?"

    scene amidormten14
    with dissolve

    a "What...do you mean by that?..."
    s "…"
    a "…"

    "Neither of us say anything for another few minutes."
    "Ami might be an airhead at times, but she’s not an idiot. And she knows there's a much more calculating side to my retort than it may seem at first."

    if bonus == True:
        "Anyone in our situation right now would understand just how dangerous words can be at such close proximity."
        "But for every one of those people, there is one more who would act on impulsive desires."
        "A person who would not use words, but instead reach out and take this girl as their own."
        "When did I deviate from that path?"
        "Did I deviate at all?"
        "Months ago, before spending time with her, I would have fucked this little girl's brains out without a second thought."
        "But now?"
        "I don't know."
        "Things feel different somehow."
        "Like one wrong move will smash the illusion and end everything just as quickly as it started."
    else:
        "She's an accomplished CPA with an extensive background in financial services who always knows exactly what to deduct and how it will impact my return."

    a "Sensei..."
    s "Yeah?"
    a "I'm going to ask you a question."
    a "One that you don't have to worry about honesty for since it will be something that has immediate consequences."
    a "But I...have to ask it anyway."
    a "I can't hold it in any longer. I really can't."
    s "..."
    a "..."
    a "Sensei..."
    a "Will you lose yourself with me?"

    menu:
        "Yes" if bonus == True:
            jump amidormtouchx
        "Hugging you, I guess" if bonus == False:
            s "I am thinking about how we should hug."
            a "What? That's it."
            s "I think hugs are good and that we should hug each other more frequently from this point forward."
            a "But what would the others think?"
            s "Nothing because we are not related and it's just a hug, Ami. Come on."
            a "Okay. We can hug, I guess."

            scene black
            with dissolve

            "We hug, I guess."

            $ renpy.end_replay()
            $ amifingered = True
            $ ami_love += 1
            $ amidorm10 = True
            $ swimming = True

            "{i}Congratulations! You have hugged your [niece]!{/i}"
            "{i}Ami’s affection has increased to [ami_love]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat
        "...":
            s "..."
            a "..."
            s "I don't really want to answer that question, Ami."
            a "Why not?"
            s "Because doing that would change everything."
            a "Does that mean...you {i}don’t{/i} want anything to change?"
            s "I...don’t know what I want."
            s "I just know that, right now...I don't want to answer that question."
            a "…"

            "Ami's expression doesn't change."
            "There's no look of disappointment or relief or...anything, really."
            "She remains locked in stasis while I have figured out a way to break out of it."

            s "If it makes you feel any better, I will confirm that I {i}do{/i} feel happier now."

            scene amidormten12
            with dissolve

            a "Hm..."
            a "That does make me feel a {i}little{/i} better, I guess."
            a "You should really try to play along with my games, though."
            s "Oh? And why is that?"
            a "Because you never know when I might want to stop playing them."
            s "I refuse to play along with you one time and you're threatening to cut me off forever?"
            a "The one who's cutting us off is you...right now."
            a "Even in our own little world, you didn't give in."
            a "You're so strong, Sensei."
            a "But I guess that's just one more reason why I love you so much."
            s "..."
            a "{i}I love you too, Ami. You're so pretty.{/i}"
            s "Wow, I don't even have to talk anymore."
            a "Heheh...you really don't."
            a "I always know exactly what you're going to say."
            a "Even when I don't want to."

            scene amidormten15
            with dissolve

            a "But anyway...I guess I should probably try and sleep now."
            s "Already? Don't want this moment to last forever anymore?"
            a "It already ended, unfortunately."
            a "I’m glad I got to cuddle with you, though."
            a "Oh, and if you want your hand back at any point tonight, too bad."
            s "Oh, great."
            a "Goodnight, Sensei."
            a "I’ll never forgive you if you leave me while I'm sleeping."
            s "Goodnight, Ami."
            s "I make no promises."

            scene black
            with dissolve2
            stop music fadeout 10.0

            "Ami falls asleep shortly after that."
            "It probably goes without saying as I'm still here talking to you, but I don't."
            "I hang around for another hour and do yet another thing that she doesn't want me to do in leaving her behind."
            "But..."
            "That's what I think is best for her."
            "And if there is anything I want to protect in this very moment beside myself..."
            "It is the first girl I saw upon waking up here."
            "And the one who loves me more than anyone else in the world."
            "........."
            "......"
            "..."

            $ renpy.end_replay()
            $ amifingered = False
            $ amidorm10 = True
            $ ami_love += 1

            "{i}Ami’s affection has increased to [ami_love]!{/i}"
            "………"
            "……"
            "…"

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label mayadorm5:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
...
```