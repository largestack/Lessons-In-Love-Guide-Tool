# Endless Torment (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 20

* Event [First Words](./ayanedorm15.md) (Ayane) is completed)



## Next events

* [Ayane: Still Young](./ayanedorm20.md)

## Event properties

* Id: dojo20
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo
* Triggered by path: dojo->dojo20

## Official wiki page

[Endless Torment](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dojo20&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label dojo20:
    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene ayanelay1
    with dissolve
    play music "sakuya4.mp3"

    ay "Hah...hah...hah..."
    ay "Oh my god..."
    ay "That was...so much...more intense...than it normally is..."
    s "I think I’m going to die..."
    s "I had no idea you could even do that with your legs."

    scene ayanelay2
    with dissolve

    ay "It’s not like I...wanted to!"
    ay "I just...needed to listen to orders or...I’d get in trouble..."
    s "You did well..."
    s "I’m not going to lie, I thought you’d crack under the pressure with all of the other girls watching."

    scene ayanelay3
    with dissolve

    ay "I’ve told you before, haven’t I? I don’t mind if people watch. It just puts pressure on me to do even better."

    scene ayanelay4
    with dissolve

    ay "But to think we’d have to spar the instructor herself...especially at our skill level..."
    ay "That’s just not fair. I could barely even land a hit."
    s "I think I landed one or two, but I doubt she even felt it."

    "Ayane and I just finished our training session for the day and are taking a much-needed and well-deserved rest."
    "Who would have thought that the wooden floor of the dojo could ever feel so comfortable?"
    "But I guess anything would be comfortable after expelling almost all of your energy for what feels like no purpose whatsoever."
    "In fact, no one in the entire dojo was even able to land a substantial blow on the instructor."
    "And here I was thinking this was just some random training ring for novice martial artists."

    scene ayanelay5
    with dissolve

    ay "[ayanemaster], I think we might be in trouble. What will we do if the two of us can never defeat her?"
    ay "Will we simply give up our homeland? Is she destined to be the true ruler of Kumon-mi?"
    s "Why are you grabbing my arm? Let go of me."

    scene ayanelay6
    with dissolve

    ay "Perhaps this is what must be done, though."
    ay "Our clans have been at war with one another for centuries...millennia even..."
    ay "Maybe it’s up to you and I to put an end to all of that?..."

    scene ayanelay7
    with dissolve

    if bonus == True:
        ay "What do you say, [ayanemaster]?...Are you ready to start a family?"
        s "Absolutely not. Let go of my arm."
        ay "But I like your arm. It’s big and strong and makes me feel safe."
        s "That’s great, but there’s a time and a place for everything. You clinging to me doesn’t exactly make me look like a model citizen."
    else:
        s "Absolutely not. Let go of my arm, you harlot."

    scene ayanelay8
    with dissolve

    if bonus == True:
        ay "It’s just a little grab. No one cares. It’s not like we’re having sex."
        s "What kind of warped perception do you need to have on the world to think the only
        inappropriate thing to be doing in public is having sex?"
        ay "I don’t know. But I’m not letting go. You’ll have to pry your arm away from my-"
    else:
        ay "But I paid good money of this on the black market!"

    scene ayanelay9
    with dissolve

    ay "Ah! My arm!"
    s "It’s {i}my{/i} arm, psycho."

    scene ayanelay10
    with dissolve

    ay "All I ever do is love you, and yet you break my heart."
    ay "Alas...pain is all the Amamiya dynasty has ever known. Perhaps this
    will not be the end to years of endless torment after all."
    s "Can we go back to resting now?"

    scene ayanelay11
    with dissolve

    ay "Sure! Goodnight, [ayanemaster]. Please wake me up when class is over so we can walk home together."
    s "Ayane-"
    ay "Every time you push me away, I’m only going to want you more~"
    s "So if I push you away now-"

    if bonus == True:
        ay "I’ll grab your penis and start waving it around in front of everyone like
        it’s a sparkler at a summer festival."
        s "…"
    else:
        ay "I will shrink down to microscopic size, climb inside of you, and build a home in your heart."

    s "That doesn’t sound fun at all."
    ay "It won’t be. So I suggest you let me stay like this until I fall asleep or someone tells us to break apart."
    ay "But until then, please let me hold onto you."
    ay "I’ve been feeling a little down lately and I need to be as close as possible to you so I can recharge."

    "That’s strange. It’s not like Ayane to admit when she’s upset or in a
    bad mood or whatever it is that she’s feeling right now."
    "I wonder what’s going on?"

    s "You’ve been feeling down?"
    ay "Yeah."
    s "Why?"
    ay "I don’t really wanna talk about it right now. It’s stupid."
    s "You know you can-"
    ay "Sensei. Please don’t ask me again."
    ay "I’ll tell you soon. I just don’t want to think about it right now."
    ay "I love you a lot, but even I can’t help but get a little angry if you keep asking me
    things when I tell you not to."
    s "…"
    s "Okay then."

    if bonus == True:
        s "But if someone tells you to get off of me, please don’t wave my penis around like a firework."
        ay "I won’t. That will only happen if you try to get away yourself."

    scene ayanelay12
    with dissolve

    ay "See how nice I can be when you’re obedient?"
    s "Aren’t you supposed to be the obedient one?"
    ay "I {i}am{/i} obedient. I’ll do whatever you want me to do whenever you want me to do it."
    s "Except talk about your feelings."
    ay "I’ll talk about my feelings for {i}you{/i}."
    s "I know about those already."

    scene ayanelay11
    with dissolve

    ay "I know you do. But I want to remind you again anyway so it stays in your head."
    ay "I love you more than anything in the world."
    ay "I love the way your arm feels when you let me squeeze it."
    ay "I love the way you knock on my door when you visit me at night."

    scene ayanelay12
    with dissolve

    ay "I love the way you look at me when I tell you all of these things."
    ay "I love the way you care so much about me even when you pretend not to."

    "This is...new."
    "It’s actually kind of heartwarming to spend a moment like this with Ayane without her-"

    scene ayanelay13
    with dissolve

    if bonus == True:
        ay "I love the way your giant dick feels when you put it in my-"
        s "Okay, Ayane. I get it. You love me."
    else:
        ay "And I really love the third season of Seinfeld."
        s "What?"
        ay "I used to watch it with Kirin."
        s "??????????????"
        ay "(Mimics funny bass line)"
        s "Ayane stop"

    scene ayanelay14
    with dissolve

    ay "You’re not gonna let me finish? I was just getting to the good part."

    if bonus == True:
        s "I don’t know if you’ve realized this, but I’m wearing sweatpants and I really don’t
        want to have to walk out of here with an erection."
        ay "Yeah, that would be pretty bad, wouldn’t it?"
        ay "If only having sex in public were legal. You could just let it out inside of me
        and walk out of here like nothing ever happened."
        s "How did we get back to this?"
        ay "I’m horny now."
        s "You’re always horny."
        ay "It’s easier to forget other stuff when I think about sex."
        s "…"
        s "What?"
    else:
        ay "(Continues mimicking funny bass line)"
        s "Ayane why"

    scene ayanelay11
    with dissolve

    ay "Nothing. Just thinking out loud."
    ay "I’m going to keep my eyes closed now, Sensei. Can I put your arm around me and sleep on your shoulder?"
    s "What? No. This already looks bad enough as is."
    ay "Boo~"
    ay "I guess I’ll just sleep like this, then. "
    ay "Oh, and I have a gun on me, so don’t even think about trying to run away. Got it?"
    s "Why do you always have a gun on you?"
    ay "To protect myself from muggers or anyone who tries to steal my boyfriend."
    s "…"
    s "Ayane, I’m not your-"
    ay "Goodnight, Sensei~ I love you so much."
    s "…"
    s "Ayane?"
    ay "…"

    "Ayane falls asleep seconds later, still exhausted from sparring just moments ago."
    "She was one of the last girls to go up, but despite her lack of time doing this compared to many of the others, she was actually really impressive."
    "I’ve learned by now that she’s the type of girl to never stop pursuing what she wants. And hey, if she actually wants to be a martial artist, more power to her."
    "But at the same time, that sort of mindset can be destructive. "
    "People who spend their entire life chasing one thing often forget the importance of others."
    "And no, I’m not talking about karate anymore."
    "I’m talking about me."
    "Why does she like me so much when I haven’t done anything to even almost warrant deserving that?"
    "What is it about me that is magnetizing her?"
    "Is it because she thinks I’m playing hard to get?"

    scene black
    with dissolve2

    "…"
    "Or is it something else?"

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo20 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label dojo25:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
    if ayane_love >= 10 and ayanenew1 == True and ayanenew2 == False:
        jump ayanenew2
    if ayane_love >= 20 and ayanedorm15 == True and dojo20 == False:
        jump dojo20
...
```