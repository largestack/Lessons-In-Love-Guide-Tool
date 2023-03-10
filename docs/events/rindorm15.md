# Boundaries (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 15

* Event [Rin's Secret](./rindorm10.md) (Rin) is completed)



## Next events

* [Rin: Window of the Waking Mind](./cafe15.md)

## Event properties

* Id: rindorm15
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm15

## Official wiki page

[Boundaries](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm15&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm15:
    play sound "knock.mp3"

    "I knock on Rin's door and wait for her to answer."
    "The faint sound of her humming some song I've never heard before is quickly replaced by a series of demands that I have no intention of fulfilling."

    r "Get out of here, loser! How many times do I have to tell you to stop coming around without some sort of offering?"
    s "Is that...a thing you told me?"
    s "Besides, I shouldn't have to pay an admission to see one of my students."
    s "In fact, you should probably be the one paying me for house calls now that I think about it."
    r "I didn't even call you, though? You can't just drop by unannounced and charge me for it. That's an abuse of power."
    s "I'll waive the fee if you let me in. I'm bored and need something to do."
    r "Okay, okay. Nobody's charging anybody. I was just messing with you."
    r "Come back later, though. Kind of in the middle of something here."
    s "And what are you in the middle of, exactly?"
    r "Waiting for the rest of this body I found to melt. They really don't make sulfuric acid like they used to, do they?"
    s "Can I at least know whose body it is?"
    r "Mmm...not sure. And I think it might be past the point of identification since I started with the head."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Doesn't mean I can't try. If you've killed one of your classmates, I'd like to at least confirm which one it is."
    r "Wait? What? No! I wasn't kidding! Stay out!"
    s "Why? There's no way you have an actual-"

    scene boundariesredux1
    with dissolve
    stop music

    s "Oh."
    s "So that's what you were in the middle of."
    r "..."
    s "..."
    r "You..."
    s "..."

    scene boundariesredux2
    with hpunch
    play music "sweetvermouth.mp3"

    r "Sensei, what the actual fuck?! You can't just walk into someone's room whenever you want!"
    s "In my defense, you provided probable cause for investigation. I was just trying to be a good person."
    r "Probable cause?! To barge into a girl's room while she's changing?!"
    s "To stop the...dissolving of a body?"
    r "There is obviously no body!"
    s "There is very much a body. Just not one I expected to see this much of so early on."

    scene boundariesredux3
    with dissolve

    r "Yeah, you're telling me..."
    s "So...what's new?"
    r "..."
    r "Are you fucking kidding?"
    s "What-"

    scene boundariesredux4
    with hpunch

    r "Get the fuck out of here, dude! I'm feeling totally fucking violated right now!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "See, that was all you needed to say. I'm gone."
    r "Cool! Bye!"

    play sound "lock.mp3"

    s "In the future, it might be smart to tell someone you're getting changed instead of dissolving a body if you don't want them to come in."
    r "Oh, yes! My bad, Sensei! How stupid I was to think there was a right way and wrong way to tell someone to stay out of your room!"
    s "I'm glad you have seen the error of your ways."

    play sound "thump.mp3"

    r "Fuck you, jerk!"
    s "What did you just throw at the door?"
    r "A fucking book. And now I have to go {i}back{/i} to the door and pick it up because it landed halfway open and I don't want the cover bending."
    s "So, you're still naked and right on the other side of this door right now?"
    r "I wasn't {i}naked!{/i} I just didn't have a bra on!"
    s "Oh, so it's fine if I come back in?"
    r "Touch that fucking door knob again and I swear to god I will actually find a way to procure sulfuric acid."

    "I find myself back out in the hall, speaking through the door to a factually {i}not{/i} naked Rin."
    "Needless to say, she is mad. Which she has every right to be."
    "I made the conscious decision to invade her privacy for the sake of a joke and am now paying the price for it."
    "But do I regret that even a little? Absolutely not."
    "In fact, I'd do it all over again if I didn't think she would actually find some way to dissolve my body in sulfuric acid."

    r "Are you still there?"
    s "Are you still not naked?"
    r "You fucking...yes. I am decidedly un-naked now. And I will let you back into the room under one condition."
    s "Yeah, I guess it would only be fair if you got to see me without my clothes on as well."
    r "That's obviously not what I'm talking about!"

    play sound "lock.mp3"

    r "Just fucking come in. But know that I am very, very, very, very, VERY mad at you."

    play sound "dooropen.mp3"

    "Once again, I open the door. Just this time, I have permission."
    "........."
    "......"
    "..."

    scene boundariesredux5
    with dissolve2

    r "..."
    s "..."
    s "Oh no. Your condition is an apology, isn't it?"
    r "Do I not deserve one?"
    s "You do. I'm just not very good at them."
    s "Will you accept a series of compliments instead?"
    r "Compliments under these circumstances would likely only make me angrier."

    scene boundariesredux6
    with dissolve

    r "That was really fucked up, dude. Like, I'm not even kidding."
    r "Don't do that again."
    s "You know I didn't actually mean any harm, right?"
    r "You don't have to {i}mean{/i} harm to actually harm someone, you know. Like, what if it was someone other than me that you walked in on?"
    r "What if it was someone who wanted to get you in trouble? Because they'd definitely be able to after that little stunt."
    s "I'm sorry. It won't happen again."
    r "..."
    s "..."
    r "You mean it?"
    s "As much as I possibly can."
    r "..."
    s "..."

    scene boundariesredux5
    with dissolve

    r "Hmph..."
    s "..."
    r "..."

    scene boundariesredux6
    with dissolve

    r "Do you know what this means, Sensei?"
    s "What...{i}what{/i} means?"
    r "As of today..."
    r "Everyone in our class has officially seen my boobs."
    s "..."
    r "..."
    s "I want to say I'm glad to be a part of the club, but I don't know if now is really the right time."

    scene boundariesredux7
    with dissolve

    r "Hah...It is what it is. There's no way to go back in time and change it from happening. I'll just have to...always lock the door now or something."
    s "To be fair, that's something you should have already been doing."

    scene boundariesredux8
    with dissolve

    r "Why? We all see each other without our clothes on all the time. It barely makes a difference anymore."
    s "I mean...doesn't it make a difference for {i}you?{/i}"
    r "Are you implying that, since I'm bisexual, I'm unable to strip in front of my classmates without getting turned on?"
    s "Kind of, yeah."
    r "That is an extremely rude thing to say."
    r "It is also 100%% accurate."
    r "But it's {i}not{/i} because I am bisexual, Sensei..."
    r "It's because I am a fucking pervert."
    s "I feel like I'm getting to see a whole new side of you today, and that's not just because I got to see you topless a few minutes ago."

    scene boundariesredux9
    with dissolve

    r "Whatever. You're welcome for the new fantasies, loser."
    r "So, what brings you here today? Apart from the whole peeping tom thing."
    s "Just trying to kill some time, I guess. And time normally seems to move a bit faster with you around."
    r "Well, thanks for-"

    scene boundariesredux10
    with dissolve

    r "Wait, that {i}was{/i} a compliment, right? I can’t really tell."
    s "I think so? Just like with apologies, I'm not really great at those either."

    scene boundariesredux9
    with dissolve

    r "Well, thanks. You’re pretty fun to be around too. When you're not invading my privacy, I mean."
    s "So, where’s Futaba tonight?"
    s "It’s pretty late. I figured she’d be home by now."

    scene boundariesredux11
    with dissolve

    r "{i}Gasp!{/i} Does this mean that you have finally fallen for my beloved roommate and borderline-sister, Futaba Fukuyama?"
    s "Did you just say {i}gasp{/i} out loud instead of actually gasping?"
    s "Also, all I did was ask where she is. That doesn't mean I'm in love with her."

    scene boundariesredux12
    with dissolve

    r "Futaba is sleeping at a friend’s place tonight."

    if day < 5:
        s "Really? Even though we have school tomorrow?"
    else:
        s "Really? That’s new."

    r "Yup. One of our friends from middle[school]."

    scene boundariesredux13
    with dissolve

    r "Well, mostly her friend I guess. The two of us never really hit it off the way they did."
    r "Though...there are certainly {i}some{/i} things we do see eye to eye on."
    s "Girl friend or guy friend?"

    scene boundariesredux14
    with dissolve

    r "Would you be jealous if I said it was a guy?"
    s "Maybe a little bit. I’d like to at least meet him first if he’s going to be corrupting one of my students."
    r "Well, I guess you lucked out then. Because Nodoka is {i}definitely{/i} a girl."
    s "I'm feeling a little put off by the emphasis on that {i}definitely.{/i}"
    r "Let that be your hint on what exactly she and I see eye to eye on, then."
    s "Ahh. Another lesbian."

    scene boundariesredux15
    with dissolve

    r "Our forces grow stronger by the day."
    r "Also, bisexual."
    s "Whatever the case, knowing Futaba's not off in the arms of some random guy will help me sleep a little better. So thanks for clarifying, Rin."

    scene boundariesredux16
    with dissolve

    if cafe10 == True:
        r "Speaking of which, didn't you say something about sleeping troubles at the cafe a few days ago?"
        s "Yeah, but that doesn't really have anything to do with Futaba. Or...anyone for that matter?"
    else:
        r "Have you been having trouble sleeping lately or something?"
        s "Not really. It's just a phrase."

    r "You sure? Need me to come over and read you bedtime stories or something?"
    s "As long as you read some to Ami as well. I'm sure she'd like that."
    r "Ami can be pretty weird at times, but I don't really think she'd go for me randomly showing up one night and reading to her."
    s "It's worth a shot, I think."

    scene boundariesredux17
    with dissolve

    r "I'll add it to my rapidly growing list of things to do...Which actually allows me to segue into this!"

    scene boundariesredux12
    with dissolve

    r "Go home."
    s "What? But I didn't even do anything wrong this time."
    r "This time, no. But I already had plans with somebody else tonight and you are currently getting in the way of them."
    s "Is {i}your{/i} secret companion also a girl? Or are you sneaking away to-"
    r "I'm gonna cut you off right there and remind you that I greatly prefer girls over guys so, if you're going to get jealous, it should probably be over a female."
    r "Which it is."
    s "Going on a date this late at night?"

    scene boundariesredux18
    with dissolve

    r "A date? Oh god, no. It's nothing like that at all."
    r "It's just a friend from a different class."
    s "It might be a little too early to say this, but I didn't think there were any girls you {i}weren't{/i} attracted to."

    scene boundariesredux17
    with dissolve

    r "It's not that I'm not attracted to her. She's actually really pretty."
    r "She's just a little too much like me."
    s "And...that's a problem?"
    r "Would {i}you{/i} want to date yourself, Sensei?"
    s "With the penis or without the penis?"
    r "Why not both?"
    s "Okay, I'm going to let you leave now."

    scene boundariesredux12
    with dissolve

    r "We can leave together. She's in a different dorm, so I have to go meet up with her elsewhere anyway."
    r "Wow, look at me. Forgiving you {i}and{/i} letting you walk with me even though you stole a glimpse at my delicate, maiden body earlier. I'm so awesome."
    s "And extremely humble, too."
    s "After you, Rin."
    r "Why thank you, sir. You're such a gentleman when you're not being a pervert."
    s "Yeah, well...it takes one to know one."

    scene black
    with dissolve2

    "Rin and I exit the dorm together, but she breaks away just a few minutes later as it turns out we're heading in opposite directions."
    "Without anything left to do, I decide to just go home and call it an early night."
    "I'm surprised that I managed to get off as easy as I did after the stunt I pulled, but I'm not about to try and heat up the water again once it's finally cooled off enough to get into."
    "As such, I attempt to shelve all of the impure thoughts clouding my mind on the journey home but, as always-"
    "I fall victim to them in the end."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm15 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm20:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
...
```