# A Brief Moment in Time
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukastreets5&go=Go)



## Event preconditions
✅Touka love greater than or equal to 5

✅Event "[Tsuneyo: Blackout](./ramen20.md)" is completed (event=ramen20)

✅Event "[Noriko: Mouthjob](./convenience5.md)" is completed (event=convenience5)

✅Event "[Touka: Fish Out of Water](./toukadorm1.md)" is completed (event=toukadorm1)



## Next events
* [Touka: Loser](./toukadorm5.md)

## Event properties
* ID: toukastreets5
* Group: Touka
* Triggered by label: toukastreets
* Triggered by branch label: saturdaymorning

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukastreets5:
    scene toukaolddis1
    with dissolve
    play music "wewereangels.mp3"

    "I make my way over to the same area between my house and the[school] where I last found Touka battling a vending machine."
    "Today, there is no battle. Just a girl standing in the middle of the sidewalk, curiously surveilling her surroundings and probably assigning new rich-person names to everyday commoner objects."
    "Or...trying to figure out how they work and-"
    "I don’t know. But she’s clearly confused to some extent because why else would anyone just stand around in the middle of a mild snowstorm?"
    "I make my way over soon after spotting her, letting the crunch of the ground beneath my feet signal my arrival."

    scene toukaolddis2
    with dissolve

    to "Oh, Sensei. Good morning."
    to "If you had not shown up soon, I would have continued exploring on my own. Needless to say, I am very happy you did."
    s "So you {i}weren’t{/i} just standing around trying to figure out how commoner objects work? You were waiting for me?"

    scene toukaolddis3
    with dissolve

    to "I may be inexperienced, but I am not an imbecile. I know how all of these things function."
    s "So it’s just vending machines you have a problem with, then?"

    scene toukaolddis4
    with dissolve

    to "In my defense, I do have experience with those types of machines. I had just never encountered one that wouldn’t accept my money before..."
    to "Let alone a voice activated one with an added visual element. But at least it is making the streets of Kumon-mi a safer place."

    "Wait, does she still think I wasn’t joking about that part?"
    "Please let me be around whenever she tries to use one again."

    scene toukaolddis5
    with dissolve

    to "So, can I assume that you are here to work as my guide and that you are not simply passing by?"
    s "Just passing by, actually. See you later."
    to "Ha ha ha. That was a rhetorical question, Sensei. I know you are here to see me. "
    to "You do not need to be embarrassed."
    to "I’m sure that being out and about with me may make you look significantly worse by comparison, but there is barely anyone outside today."
    s "Yeah, that tends to happen when it snows. This area is a lot busier in the summer."
    s "Also, being seen with you will not make me look worse. "
    s "If anything, since most of the people out here are just like me, they’d probably just think {i}you{/i} look nice and not think anything of me at all."
    to "I don’t see how that invalidates any of what I said, but as long as you will still be my tour guide, I can look past it."
    to "So, where would you have me go today?"
    s "Oh, it’s up to me?"

    scene toukaolddis2
    with dissolve

    to "Well...yes."
    to "I know absolutely nothing about this area and you seem to know quite a bit."
    to "Should I be researching places I would like to go and informing you of them beforehand? "
    to "I really don’t know the best way to approach things like this, nor where I should start for the authentic commoner experience."
    s "Weren’t you supposed to stop using that word?"

    scene toukaolddis6
    with dissolve

    to "Yes, but...{i}lower middle class{/i} is so much harder to say. And it does not seem like you mind very much."
    s "I don’t, really. Especially since I’ve called you a spoiled rich girl on several occasions now. "

    scene toukaolddis7
    with dissolve

    to "Spoiled?! Me?!"
    s "...Yes."

    scene toukaolddis8
    with dissolve

    to "Yes, I suppose that {i}is{/i} right now that I think about it."
    to "I apologize for my reaction. I’m just not used to being so accurately insulted. "

    scene toukaolddis5
    with dissolve

    to "But, that all ends today! Because I am going on a wholesome adventure with my teacher who is going to be very patient and encouraging with me!"
    s "Patient, maybe. Encouraging, probably not."
    to "Oh, stop. What could possibly go wrong? "
    to "I’m sure that wherever you take me will be somewhere I can ease into and experience at my own pace."
    to "Only a {i}truly{/i} horrible man would toss me into the deep end. And you are only partially horrible based on what I’ve seen thus far."
    s "…"
    to "…"

    scene black
    with dissolve

    s "You know, I think I've got just the place. "
    s "It’s kind of a long walk, though."
    to "That’s fine! I’ve packed plenty of snacks and beverages for the two of us and slept surprisingly well last night!"
    s "What if I didn’t show up today?"
    to "Well...I suppose I would have had to find something else to do with all of the items I brought."
    to "Regardless! I am refreshed and raring to go! "
    to "Lead the way, Sensei! I’m sure you will take me somewhere nice!"
    s "Yeah..."
    s "We’ll see about that."

    scene wintersky
    with dissolve

    "Now, “nice” is a subjective term a lot of the time."
    "There are things certain people find interesting or endearing that others can’t seem to grasp even after prolonged exposure or being forced to consume or experience them."
    "Basically, there are things that you can “train” yourself to like."
    "And right now, essentially everything Touka can and will experience falls into that exact boat."
    "Of course she’d never view any of what us “normal people” see as nice when she’s been conditioned to accept nothing less than the best of what life has to offer."
    "So, with that in mind, the best course of action right now isn’t to slowly ease her into the life that everyone else leads."
    "It’s to do exactly as she {i}doesn’t{/i} want me to do and toss her into the deep end."
    "But that’s okay, because I’m sure her exceedingly rich family has paid for years worth of swimming lessons."
    "And I’m sure that if they didn’t and she winds up drowning, they’ll throw a lavish funeral to celebrate her depressingly short life."
    "Either way, I know where I’m taking her."
    "And it’s somewhere that no amount of snacks or beverages can possibly prepare her for."
    "………"
    "……"
    "…"

    scene toukaolddis9
    with dissolve2

    to "…"
    s "…"
    to "Where...are we?..."
    s "This is the second half of town. Or the old district, if you’d rather call it that instead."
    to "Is this...some sort of theme park? What am I looking at here?"
    s "Not a theme park. Just a low income area where people even worse off than me live."
    s "I figured it might help to show you the polar opposite of your life rather than something boring like a bowling alley or an ice skating rink."

    scene toukaolddis10
    with dissolve

    to "I love ice skating, actually. Would you like to accompany me some day?"
    s "Not particularly. "
    to "How sad. "

    scene toukaolddis11
    with dissolve

    to "This place, though..."
    to "You said that people...{i}live{/i} here?"
    s "{i}Die{/i} here is probably more accurate."
    s "Most of the people in the old district are either...well, {i}old{/i} or homeless. Or a mixture of both of those two things."
    s "But that doesn’t mean there aren’t outliers."

    scene toukaolddis12
    with dissolve

    to "You don’t mean to tell me that there are students in our[school] who call a place like this home, do you?"
    s "There are a few in our class, actually."
    s "Tsuneyo...Chika...That one girl you find more intimidating than me who I can’t remember the name of."

    scene toukaolddis13
    with dissolve

    to "I...suppose I do see how someone like Yumi could live here. She needed to learn her...intimidation tactics somewhere."
    to "But you say that Chika lives here as well? The one who my mother is familiar with?"
    s "Yeah. Her and Yumi live in an apartment over here together."
    s "They’re taking care of a little girl with an immunodeficiency disorder as well. "
    s "It’s pretty impressive, to tell you the truth."

    scene toukaolddis14
    with dissolve

    to "This isn’t another one of your pranks, is it?"
    to "Because I can be depressingly compassionate at times, and it would be very mean for you to make me feel bad about things that simply aren’t true."
    s "It’s true. I’d take you there, but Chika doesn’t let just anyone near her sister since it could get her sick."

    scene toukaolddis15
    with dissolve

    to "I see..."
    to "So she really does live here after all. "
    s "You're not crying again, are you?"
    to "I am. But can I truly be blamed for that? "
    to "This news comes as a bit of a shock to me, Sensei."
    to "My initial reaction was asking if this place was a theme park. "
    to "I didn’t think for a moment that there were people, let alone ones as kind as that girl, {i}living{/i} in a place like this."

    scene toukaolddis16
    with dissolve

    to "And taking care of a sick little girl as well..."
    s "…"
    s "I guess taking you here was a bad idea after all, huh?"
    to "No. In fact, hiding this from me would have made me feel even worse. "
    to "At least now I can try to wrap my head around how things could have possibly gotten to this point."
    to "We’ve only been here for several minutes and I already can’t fathom the idea of calling this area “home.”"

    scene toukaolddis17
    with dissolve

    to "There are people slumped up against walls...tucked into alleyways and trying to keep themselves warm."
    to "It’s snowing, Sensei. They’re going to get sick. Perhaps even worse."
    s "Probably. But that’s just the hand these people were dealt."
    s "We’re lucky to be where we are with that in mind."
    to "Lucky is an absolute understatement. This is abhorrent and I will not stand for it."

    scene toukaolddis18
    with dissolve

    to "Excuse me! Can you tell me your name?"

    "Touka wanders away from me for a moment and crouches down beside an old man half-asleep near the side of a rundown house."
    "I can’t make out the look on his face from where I stand, but I notice a distinct lack of teeth as he opens his mouth to try and respond to Touka."
    "She proceeds to reach into her bag and pull out a handful of snacks for the man, placing them neatly beside him."
    "His eyes light up and, for a brief moment in time, things are less horrible."

    to "Hi there...My name is Touka."
    to "Are you cold?"
    om "..."
    to "You poor thing..."
    to "You can’t even talk, can you?"
    to "I don’t have much on me at the moment, but please take all of this. You need it much more than I do."
    om "…"
    to "Don’t worry about thanking me. Just eat and try to stay warm, okay? The snow will only last so-"

    stop music
    play sound "static.mp3"
    scene ayhh2 with flash
    scene ayhh4 with flash
    scene ayhh10 with flash
    scene ayhh7 with flash
    scene ayhh8 with flash
    scene toukaolddis19 with flash
    stop sound
    play music "noriko.mp3"

    "73 75 64 64 65 6e"

    n "Uhhhhhh..."
    to "Sensei, what is this place?"
    n "Before that, what is this pairing?"
    n "Since when do the two of you hang out outside of[school]?"

    scene toukaolddis20
    with dissolve

    to "Uhh...let’s see...Noriko, correct?"
    n "Yeah..."
    n "And you’re Touka, right?"
    to "Right! Though our teacher seems to forget that rather frequently."
    to "Sensei was just giving me a tour of the old district as it is my first time here."
    to "Then he suggested something about wanting to come here, but was so taken aback by my generosity moments before that he has been mostly speechless ever since."

    scene toukaolddis21
    with dissolve

    to "Is this a...shop of some sorts?"
    to "Do you mind if I take a quick look around? There are so many interesting things here."
    n "Uhh, yeah. Go ahead."
    to "Splendid!"

    scene toukaolddis22
    with dissolve

    "Touka begins to look around the store and I find myself slightly confused and standing at the counter with Noriko."

    scene toukaolddis23
    with dissolve

    n "Hey...are you okay? You seem kind of out of it right now."
    s "I...think so?"
    s "I remember walking around with Touka, but I don’t really remember anything about coming over here."
    n "Hmm..."

    scene toukaolddis24
    with dissolve

    n "Maybe you just realized that a trip to the old district without coming to see me is no trip at all?!"
    s "Sure, let’s go with that."
    s "Since when do you work mornings, though?"

    scene toukaolddis25
    with dissolve

    n "I don’t really have a set schedule. I just kinda work whenever I want to work and stuff."
    n "Today just happens to be one of those days."
    n "Is it my turn to ask a question now?"
    s "I mean, you’re going to ask it anyway, so sure."
    n "Why are you showing her around the old district?"
    n "I get that you like to hang out with everybody and stuff, but...it seems like kind of a weird place to take {i}her{/i} of all people."
    s "That’s exactly why I brought her here."
    s "She’s been having trouble getting accustomed to the life of a middle class citizen and-"
    to "Sensei! What are these?!"
    s "Hold on one second, Noriko."

    scene toukaolddis26
    with fade

    s "Touka, what-"
    to "Are these candy?! Can we buy some?!"

    if bonus == True:
        n "{i}Oooooooooooooooooooh my god.{/i}"
        s "…"
        to "I’m not normally allowed to eat candy on account of what it can do to my body, but today is a special occasion and-"
        s "Touka, I’m going to need you to listen very carefully for a moment."

        scene toukaolddis27
        with dissolve

        to "Listen to what? Did I do something wrong?"
        to "This isn’t actually a museum, is it? There were price tags, so I assumed I could purchase the items on display and-"
        s "Those are condoms."
        to "Condoms?"
        s "Not candy."
        to "Not candy?"
        s "..."
        to "..."

        play sound "entrybell.mp3"

        n "Welcome in!"
        s "You can’t eat condoms, Touka."
        to "…"
        cust "…"

        play sound "entrybell.mp3"

        n "Bye! Please come again!"

        scene toukaolddis28
        with dissolve

        to "Hmm...condoms..."
        to "I feel as if I’ve heard that word before. But what did it mean again?"
        s "I’m sure your mother or...manor staff must have taught you sexual education, right?"
        to "Yes, but what would-"
    else:
        s "Yes."

    scene toukaolddis29
    with hpunch

    to "Ah!"

    if bonus == True:
        s "You remembered?"

        scene toukaolddis30
        with dissolve

        to "I remembered."
        to "This is extremely embarrassing."
        s "Just think of how it would be if you tried to eat them."
        to "I have sullied your good name by acting so inappropriately in public."
        to "And after you took the time out of your day to show me a true middle class...sex shop?"
        s "Convenience store. They just sell condoms because it’s...convenient, I guess."
        s "But you can also buy snacks and drinks here as well."
        to "Doesn’t it make people feel strange buying food and beverages from a store that sells contraceptives?"
        s "Surprisingly, no."
        to "I see."
        s "…"
        to "…"
    else:
        s "Touka?"
        to "I got so excited about buying the candy that I appear to have dropped it."
        n "You must pay for that! I demand it!"

    s "Are you ready to leave now?"
    to "Yes. I believe I am."

    scene black
    with dissolve2

    if bonus == False:
        n "Come back here, candy destroyers!"

    "Touka and I say goodbye to Noriko without purchasing anything."
    "She proceeds to confusedly wave at us as we depart the store and I receive a flurry of text messages moments later with nothing but question marks."
    "Not knowing how to reply, I slide my phone back into my pocket and slowly escort the richest girl in Kumon-mi back to the safer part of town."
    "I got to see a different side of her today, though."
    "And a side that, while overwhelmingly naive, is still endearing."
    "I just hope she doesn’t wind up trying to get too involved in things she doesn’t understand."
    "I may have taken her there today, but I don’t think a place like that is really fit for a girl like Touka."
    "Eventually, we wind up back near the vending machines where this all started and go our separate ways."
    "Instead of just standing around staring during today’s separation, though, I can hear Touka softly humming something to herself as she gleefully skips away."

    $ renpy.end_replay()
    $ toukastreets5 = True
    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label toukadorm10:
...
```

## Code that triggers this event
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukastreets:
    if touka_love >= 0 and toukastreets1 == False:
        jump toukastreets1
    if touka_love >= 5 and ramen20 == True and convenience5 == True and toukadorm1 == True and toukastreets5 == False:
        jump toukastreets5
...
```