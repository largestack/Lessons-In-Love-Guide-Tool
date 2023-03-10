# Imprinting (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 10

* Event [The Flavor of Love](./cafesugar.md) (Rin) is completed)

* Event [Names of Our Children](./dojo10.md) (Ayane) is completed)

* Event [Home Sweet Home](./ayanedorm5.md) (Ayane) is completed)



## Next events

* [Main: Recall](./day96.md)
* [Ayane: Far From Fantasy](./ayanenew2.md)
* [Rin: Nothing Was Missing, Except Me](./cafe20.md)

## Event properties

* Id: ayanenew1
* Group: Ayane
* Triggered by label: callayanemorning
* Triggered by branch label: callmorning
* Triggered by path: callmorning->callayanemorning->ayanenew1

## Official wiki page

[Imprinting](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanenew1&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayanenew1:
    play sound "phonebeep.wav"

    "I tap on Ayane’s name in my phone and wait for her to answer."
    "I know that it’s relatively early in the morning...and I know that it isn’t really like me to go out of my way to make plans as soon as I wake up..."
    "But I also know that Ayane has verbally confirmed a desire to have sex with me and that I must now do things I would not normally do in order to make that happen."
    "I also had a dream about it, which further justifies the fact that I am now listening to a constant ringing that may or may not determine where my penis ends up today."

    play sound "phonebeep.wav"

    ay "Sensei? "
    s "Good morning."
    ay "Good morning, indeed! Why are you calling me so early? Did something happen?"
    ay "Did Ami fall in a well?"
    s "Yes, and I need your help to get her out."
    ay "Darn it. I was hoping you’d suggest using this as an opportunity to have me replace her as your niece and hope no one notices."
    s "Your hair isn’t even the same color."
    ay "Tell that to the five bottles of red hair dye I just ordered off of Amazon Prime. I can be your new Ami within the hour."
    ay "Seriously, though, what’s up? You never call me. I didn’t even think you’d be awake right now."
    s "I want to see you."

    with hpunch
    play sound "glass.mp3"

    ay "Ah!"
    s "...Everything okay?"
    ay "Yeah, sorry. I just felt the need to throw the glass I was holding across the room after hearing that. In a good way, of course."
    ay "Sorry, Sana!"
    s "..."
    ay "Do you...want to maybe go out for coffee or something? I was actually about to head over to Koi Cafe to study for our standardized tests and stuff."
    s "..."

    "While I want to say “No” or “I’d rather go somewhere less public,” I also understand that things being too easy would take away from the value of the gift I’m soon to be given."
    "And so I will swallow my pride and watch a rich girl study for the morning instead of enacting some of last night’s lingering fantasies both with and to and on her."

    ay "Sensei? Are you still there? "
    s "Yeah. Just thinking."
    ay "About me?"
    s "There’s a more complicated answer to that question, but the short version is “yes.”"
    ay "Great! I guess I’ll start heading over then. See you soon, future husband!"
    s "Ayane, I’m not-"

    play sound "phonebeep.wav"

    s "...your future husband."

    scene black
    with dissolve2

    "Well, looks like deflowering my niece’s best friend will have to wait until she is more confident about standardized tests or...something like that."
    "I guess it wouldn’t hurt to at least pretend to be a teacher every once in a while, though."
    "I just hope Ayane doesn’t wind up actually needing me to {i}teach{/i}, though, since it’s still way too early in the morning to be bothered with that."
    "I will be a teacher in name and appearance only."
    "At all other times-"
    "I will be the worst man I can be."
    "........."
    "......"
    "..."

    scene ayanecafe1
    with dissolve2
    play music "cafe.mp3"

    "I show up to the cafe to find Ayane already studying at the counter and, apparently, she also took the liberty of ordering for me based on years of secondhand experience in what I like."
    "Or at least what I would like if I was actually the person she wants me to be."
    "All things considered, though, her choices are fine and I don’t mind them at all. "
    "I don’t consider myself a very picky eater, though, so chances are I would have been fine with literally anything she chose."

    ay "So, what brought this on? And don’t tell me it was Ami actually falling into a well because she just sent me a picture of her and Maya at the mall. "
    ay "Unless the well is in the mall. Or leads to the mall. Or-"
    s "Aren’t you supposed to be studying?"
    ay "Aren’t you supposed to be loving me?"
    s "I don’t think that’s in my job description."
    ay "Really, though...should I be taking this as a sign of good things to come? Or is it more of a sign that you just didn’t have anything else to do and I was the second name in your phone after Ami?"
    s "I’d probably say it's closer to a sign of things to come, I just don’t know if any of them would be considered “good.”"
    ay "Ominous. That makes it sound like you’re either here to kill me or to ask me to kill someone else."
    s "I’m just here to hang out with you and maybe look like a teacher in the process."
    s "Besides, I come to this place in the morning all the time. It’s not like this is some crazy, unheard of event or something like that."

    scene ayanecafe2
    with dissolve

    ay "You come {i}here?{/i} Isn’t this a little far from your house for a morning coffee routine?"
    s "It’s not {i}that{/i} far. And Rin works here, so I normally get to talk to her as well."

    scene ayanecafe3
    with dissolve

    ay "Hmm..."
    s "What?"
    ay "Oh, nothing. "
    ay "I just would have chosen a different place to meet up if I knew the {i}real{/i} object of your affection was currently behind the counter making cappuccinos for old ladies."
    s "Ayane-"

    scene ayanecafe4
    with dissolve

    ay "I’m obviously kidding, Sensei. I know better than anyone how important the bond you and I share is. "

    scene ayanecafe5
    with dissolve

    ay "And I’m not going to worry too much about Rin stealing you away from me when, in all actuality, she’d probably try to steal {i}me{/i} away from {i}you{/i} first."
    s "No one is stealing anyone from anyone because no one here belongs to anyone else."

    scene ayanecafe6
    with dissolve

    ay "False!"
    ay "My body and mind belong to you and you only, Sensei. And you are free to do with them as you please so long as the first time is special."

    scene ayanecafe7
    with dissolve

    ay "But I guess yelling about the future of our relationship in a crowded cafe isn’t really the brightest or most secretive idea and you seem to be in teacher-mode today."
    ay "So, if you wouldn’t mind helping me with-"
    q "Blackest of night...darkest of day...hear and feel the magic that courses through these veins..."

    scene ayanecafe8
    with dissolve

    q "What is thy wish, children of the nameless? Nectar of the gods? A draught of unspeakable potency? Or perhaps...{i}a lemon poppy seed muffin.{/i}"
    s "..."
    q "..."
    ay "One draught of unspeakable potency, please."

    scene ayanecafe9
    with fade

    q "Understood. Now, if you’d please hold out your palms for me to collect but the smallest portion of blood...I can begin the alchemical process."
    s "Should we call 911?"
    ay "That won’t do anything, Sensei. We need to call 119 in Japan."
    ay "Besides, that’s just how Molly speaks. She’s in one of the other classes at our school."

    scene ayanecafe10
    with dissolve

    mo "You have entered the realm of none other but the Gem of the Emerald Isle and yet you sit before her with nothing but half-iced doughnuts and a {i}coffee noir.{/i}"
    mo "Do you quiver with anticipation, Sir?"
    s "Anticipation for what?"
    mo "The Molly route! This is simply a cameo to hold you over while you grind your stats, for I do not appear until later in the game."
    s "Right. Do you actually work here? Or did you just steal that uniform from someone?"
    mo "I can guarantee I work here, Sir."

    scene ayanecafe11
    with dissolve

    mo "Now, please order something from me. It is my first day and I need to keep this job or my gacha addiction is sure to drain me entirely."
    s "I’m good, thanks. "
    mo "Fair enough. I suppose I will just have to compose the draught for your female party member, then."

    scene ayanecafe12
    with fade

    ay "What’s in the thing I ordered anyway? I didn’t see that on the menu here."
    mo "It is a mixture of every single syrup and milk we have, packed into one extremely potent beverage. "

    "I’m just going to assume that Rin is the one who’s been training her."

    ay "Sounds good...ish!"
    mo "It might be. I have no idea. I’ve only had a job for three hours and haven't tried anything yet."
    mo "Anyway, adieu! Until the sun no longer sets above us..."

    scene ayanecafe13
    with dissolve

    ay "Until the...but where else would it even set?"
    s "I obviously don’t know that girl very well, but I think it would probably be best if we just ignored everything she ever says from this point on."

    scene ayanecafe14
    with dissolve

    ay "Deal! That gives me more time to focus on what’s really important to me anyway."
    ay "So, where was I?..."

    scene ayanecafe15
    with dissolve

    ay "Oh! Right, so...it would probably make the most sense to have you help with language arts stuff since that’s what you’ve always liked the most."
    ay "Not to mention that you seem to be getting a little burnt out on teaching in general given that your new primary objective is being everyone’s friend instead."
    s "I prefer less “friend” and more “mysterious, cool older guy.”"
    ay "You can be the mysterious, cool older guy and still teach, Sensei. Come to think of it, that’s pretty much what you’ve always done since you used to be a tutor and stuff."
    ay "At least that’s what Ami says. I was never fortunate enough to have you actually tutor me back then."
    ay "And sure, you’ve helped me with homework a few times, but that was mostly me pretending to not know stuff so I could sit really close to you."
    s "Have you really always been this crazy?"

    scene ayanecafe16
    with dissolve

    ay "Not {i}always.{/i} Just since I learned about the wonders of boys and imprinted on one."

    "That’s probably a good way to put it...albeit with a few caveats."
    "From what I understand, imprinting doesn’t typically happen this late into life, but I’m not about to argue the science of how badly Ayane wants my penis inside of her."
    "I am simply here to pretend that I am a teacher."
    "And all of the strange compulsions I’m feeling to actually help right now are not actually real."
    "None of this is real."
    "This is a new world filled with new and pretty things."
    "Things for me. Things-"

    scene ayanecafe17
    with dissolve

    ay "Hey! Here’s an idea! How about we relive the old days a little and I pretend to not know stuff {i}again{/i} and just gaze lovingly into your eyes until we get kicked out of here?"
    s "I’m beginning to think that’s exactly what you’ve been doing this entire time and that you didn’t need to study at all."
    ay "..."
    s "..."

    scene ayanecafe18
    with dissolve

    ay "Okay, so...it’s {i}possible{/i} that the original plan was to come here with Sana so I could help {i}her{/i} study."
    ay "Which means it’s also possible that I asked her to stay behind so I could meet up with you instead."
    s "Which means it’s also possible that Sana flunks out of school and it’s all your fault for abandoning her in her time of need."

    scene ayanecafe19
    with dissolve

    ay "What?! No! It has to be at least a {i}little{/i} bit your fault, since-"

    scene ayanecafe20
    with dissolve

    ay "Oh! Oh, I get it. You need {i}me{/i} to take the fall so you can keep your job."
    s "I mean...that would be great. But that was also kind of a joke, so..."

    scene ayanecafe21
    with dissolve

    ay "No...No, I know what I must do. And if you need both Sana and me to get kicked out of school in order for me to prove my love, I’ll do it."
    ay "But if Ami ever makes it back from the well, you need to tell her that I am your new niece and that she is no longer needed since she never got kicked out of school for you."
    s "The metrics you use to define your love are getting progressively stranger every day."
    ay "And we’re still in the very beginning. Imagine how things will look ten years from now when we have fifteen children."
    s "That would be-"
    ay "Highly improbable as it would take 135 months to go through 15 pregnancies- and that’s with zero downtime between popping them out."


    scene ayanecafe14
    with dissolve

    ay "But if I’m able to have more than one at once, we’ve got a chance! Believe in me, Sensei!"
    s "This might sound selfish, but I’m a lot more worried about how {i}I’d{/i} fare in that situation."
    ay "Then...believe in the me that believes in you!"
    s "..."
    ay "Or just believe in me! I’ll figure it out!"
    s "..."
    ay "..."

    scene ayanecafe21
    with dissolve

    ay "You know, I could really go for a draught of unspeakable potency right now..."

    scene black
    with dissolve2

    "Sensing that Ayane doesn’t need to study at all, the two of us wind up eating breakfast and drinking coffee until the sun starts to set."
    "She leaves the cafe with her virginity still intact-"
    "And I leave the cafe with a lemon poppy seed muffin."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanenew1 = True
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label ayanenew2:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label callayanemorning:
    if ayane_love >= 10 and cafesugar == True and dojo10 == True and ayanedorm5 == True and ayanenew1 == False:
        jump ayanenew1
...
```