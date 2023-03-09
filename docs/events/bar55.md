# Black Sandy Beaches
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar55&go=Go)



## Event preconditions
✅Sana love greater than or equal to 55

❌Event "[Main: No Strings Attached](./imanispecial1.md)" is completed (event=imanispecial1)

❌Day of week (Mon-Sun) is before Friday



## Next events
* [Ayane: How the World Works](./ayanesanabeach1.md)
* [Main: Metronome In Love](./rikaspecial1.md)

## Event properties
* ID: bar55
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label bar55:
    scene sanakaoribar1
    with fade
    play music "calmbar.mp3"

    "I make my way over to the bar (The regular one, not the second bar that I secretly visit on Fridays now) and find that, for some reason, Kaori is working here again."
    "I’m not sure why, considering that today is, at least to my knowledge, not a special occasion or holiday.  But I’m also not about to put any amount of thought into why Kaori does...well, anything."
    "Instead, I’ll just focus on the small girl beside her."

    k "Welcome once again, Friendburger! The special dizzy drink of the day is-"
    s "Hey, Sana. Working alone again tonight?"
    sa "So far...not really..."
    sa "Kaori keeps helping the customers before I...even have a chance to..."
    s "Kaori? Is she here right now?"

    scene sanakaoribar2
    with dissolve

    k "Do not give into the foul temptations of your sight balls’ endless longing for the dark! The Queen of Spiders stands before you! In the same place as always!"
    s "Always? You’ve worked here like three times."

    scene sanakaoribar3
    with dissolve

    k "So you {i}can{/i} see. "
    k "That was not a very funny human joke, Friend. Invisibility is a terrifying sickness that comes to claim us all one day. I was worried my time may have expired for a sixtieth of a minute."
    sa "That...would be called a “second...”"
    s "Thank you, Sana- for taking up my role as Kaori’s unofficial human tutor. It feels like just yesterday that I was coming here to teach {i}you{/i} how to be human."

    scene sanakaoribar4
    with dissolve

    sa "Is that...why you were coming here? It wasn’t...to teach me how to be more...umm...confident when it comes to...speaking?"
    k "If you want my human opinion, I think your speaking is nice. Your voice reminds me of glass and the color periwinkle."
    s "Confidence...humanity...they’re kind of interchangeable at this point, I think. That’s why it’s okay for people like Kaori to breathe the same air as us. "
    s "She never makes any sense, but her confidence in the act of {i}making{/i} no sense helps her blend in pretty well."
    s "On the other end of the spectrum, you have zero confidence, but are also one of the most unremarkable and exceedingly average human beings I have ever encountered."
    s "You don’t have to blend in at all since you’re already a part of the background. "
    s "So I guess that, in a sense, my job here is done. You’re as human as you’ll ever be."

    scene sanakaoribar5
    with dissolve

    sa "Un...remarkable?..."
    sa "Exceedingly...average?..."
    sa "Are you...calling me...boring?..."
    s "Yes."

    scene sanakaoribar6
    with dissolve

    sa "W...Why?! Did you come here just to...hurt me?!"
    s "Hey, being boring isn’t bad. I like being with you because it’s relaxing and I never have to worry about you drugging me or threatening to tie me up and do things to my body."
    sa "Who are you spending your time with that makes you worry about those things?!"
    s "Pretty much everyone. Which is why I like you. It’s a nice change of pace."

    scene sanakaoribar7
    with dissolve

    sa "This is the strangest...compliment I’ve ever received..."
    k "And you say that I am bad at human conversation, Friend. Can you not see that you are making the tiny human uncomfortable?"
    sa "I’m not...uncomfortable...I..."
    sa "I think I am...offended..."
    s "Offended? "

    scene sanakaoribar8
    with dissolve

    sa "Y...Yes."
    sa "You made me mad...and..."
    sa "And for that...you will pay."
    s "..."
    sa "..."

    scene sanakaoribar9
    with dissolve

    sa "Hah...I tried...being intimidating to...change things up, but...I...just sounded stupid...didn’t I?"
    k "You did not sound like yourself. The mini Sara spawn that I know of is never intimidating. Like a tiny gerbil but with marshmallows for teeth and only one eyeball."
    sa "I’ll just accept that...my test of “humanity” is finally complete and...that Sensei has no use for me anymore..."
    s "To be completely honest, though...you have improved a lot. In terms of speaking, I mean. Which I will now clarify as the {i}actual{/i} purpose of all of these visits."
    s "And in a sense...I think your test {i}is{/i} complete. But that doesn’t mean I don’t have any more use for you."

    scene sanakaoribar10
    with dissolve

    sa "C...Complete?..."
    sa "But I still..."
    sa "Keep...pausing...in the middle of...sentences..."
    s "Yeah, but I think that just might be how you talk. When you look at the amount you’ve {i}accomplished{/i} since we’ve met one another, it’s a lot more than most."
    s "You’ve made a bunch of friends...you can stand next to Kaori without getting scared...Hell, you’ve even joined the light music club. "
    s "That’s a lot, Sana. I’m really proud of-"
    sar "Light music club?! "

    scene sanakaoribar11
    with fade

    sar "Since when are you in the light music club?! Since when are you in any club at all?! Why didn’t you tell me?!"
    sa "I didn’t tell you b...because I knew you would...act like this..."
    sar "Like what?! Excited that my little girl is finally finding her place in the world?!"
    sa "Um...yes?..."

    scene sanakaoribar12
    with dissolve

    sar "Why have you been hiding my daughter’s character growth from me?"
    s "Why is it up to me to relay her growth to you?"
    sa "Why are we...still talking about {i}me?...{/i}I would like to...go back to being...unremarkable now..."

    scene sanakaoribar13
    with dissolve

    sar "Absolutely not! You are {i}my{/i} daughter and the world will know of your adorableness! I don’t care if I have to burn down all of Kumon-mi to show them."
    sa "Please don’t...burn down the city for me...This summer is already...hot enough..."

    scene sanakaoribar14
    with dissolve

    yu "Sara, I get that you like your daughter and that’s totally chill. But I ain’t afraid of kickin’ your ass if you burn down both my job and apartment. I ain’t goin’ back to the streets, you hear me?"
    sar "Shut up. If you can be proud of your daughter for putting some girl into a coma, I can be proud of my baby for becoming a rock star. "
    sa "M...Mom! I...don’t even know how to...play anything yet..."

    scene sanakaoribar15
    with dissolve

    sar "{i}Yet!{/i} Which means you {i}will!{/i} And I don’t care if I have to burn down all of Kumon-mi to ensure that!"
    s "Where did this sudden fascination with arson come from? "
    sar "From the burning love I feel for my mini Sara spawn."
    sa "I have a name! And can we stop talking about me now?!"

    scene sanakaoribar16
    with fade

    "Sara decides to give her daughter a break and retreats to the corner of the bar with Yuki after she finishes dealing with a table full of customers."
    "It’s not much being just {i}one{/i} table, but it’s more than usual for a random school night. "
    "And if Sara can afford having four people on shift at once, I think it’s safe to say things might actually be turning around for the Sakakibaras."
    "With the youngest of them managing to turn things around for herself as well, I can’t help but feel something reminiscent of what normal people would call “happiness” bubbling up inside of me."
    "But then again, I could just be lightheaded from having so many attractive girls in matching outfits standing in close proximity to me. "
    "You’d think the novelty of that would have worn off by now, but...nope. "

    k "If you do not want us to talk about you, what do you suggest we speak of, mini Sara spawn? "
    k "The lack of patrons in this establishment signals to me that this would be a good opportunity to become close to one another as I will be standing in this spot more frequently going forward."
    s "You will?"

    scene sanakaoribar17
    with dissolve

    k "The time has come for a new companion! One that I must acquire additional moneys for! And also because being around Aunt Yukiburger makes me happy!"
    sa "I’m also...going to have to spend more time with my club, so...I won’t be able to help out around here as much anymore..."
    sa "Having Kaori help is...well...it’s a lot of things...but I...think it will be for the best..."
    s "Think you’ll be able to survive a room full of loud, energetic girls playing what I assume will be loud, energetic music?"
    sa "The music...I don’t mind...but it might be...hard fitting in with everyone at first since...they’re all so cool and I’m...umm...what was it again?..."
    s "Unremarkable and exceedingly average?"

    scene sanakaoribar18
    with dissolve

    sa "R...Right..."
    k "You seem to care a lot for the mini Sara spawn, Friend. Is this what humans call love?"

    scene sanakaoribar19
    with dissolve

    sa "Wh-What?! No! Of...Of course not!"
    k "Then why is the temperature of your tiny human body steadily rising? "
    k "Size has naught to do with reaching sexual maturity, mini Sara. Not when cats are primed and ready to reproduce at only four months old!"
    sa "That’s...way too young!"
    s "Yeah, that just made me uncomfortable."

    scene sanakaoribar20
    with dissolve

    k "There is no reason to feel discomfort, Friend! Intercourse creates more fluffy animals and if you want to create more animals with the Sara spawn, I think you should! "
    s "Sana-"
    sa "No! Absolutely not! I am not...looking for a...mate!"
    s "I was just going to ask if you loved me like Kaori suggested."
    sa "I don’t even {i}like{/i} you!"
    s "Well, that’s just rude."

    scene sanakaoribar21
    with dissolve

    sa "That’s...not what I..."
    sa "Uh..."

    scene sanakaoribar22
    with dissolve

    sa "So, uhh...animals! Right?"
    k "Would you like to learn more about the rituals of mating and-"
    sa "Nope! Something...entirely unrelated to that!"
    k "Baby animals?"
    sa" Uhh...closer...but still not what I had in-"

    scene sanakaoribar23
    with dissolve

    k "What is your favorite baby animal, Friend? They are all good and there are no wrong answers. So please answer correctly!"
    s "But-"
    k "Too slow! The correct answer is the baby sea turtle!"
    k "Did you know that in a single nesting season, sea turtles can lay over one thousand eggs?!"
    k "That is so much egg! Glorious egg!"
    sa "I wonder if...Koi Cafe is hiring?..."
    s "My favorite baby animal is the lamb because all of the bad things you do in life can be forgiven by ritualistically sacrificing one."

    scene sanakaoribar24
    with dissolve

    s "Without the shedding of blood, there is no forgiveness of sin. And while sacrifices at the behest of  gods run deeper than the rivers of our ancestry, our ability to accept and embrace them does not."
    s "A long time ago, a group of men in suits showed up at my doorstep. We took them in and fed them after wiping the blood from our hands and were swiftly rewarded with eternal life."
    s "That is why I can still smile today. Why I can drink and be merry. Why I can stand before you two in my purest form. "
    s "I am eternal. All of this exists for me. "
    s "And none of it would be possible without a pile of lifeless baby sheep and blood smeared over the door of my home to attract more visitors."
    s "I can’t wait to have sex with both of you at the same time."
    sa "..."
    k "..."

    scene black
    stop music

    "INCORRECT RESPONSE PROVIDED."
    "THE EVENT WILL NOW REVERT TO ITS PREVIOUS STATE."
    "PLEASE BE ADVISED THAT THIS PROCESS IS STILL UNDERGOING TESTING AND THAT ADDITIONAL ABNORMALITIES MAY OCCUR."

    scene sanakaoribar24
    play music "calmbar.mp3"

    sa "I wonder if...Koi Cafe is-"
    s "I concur that the ideal baby animal is the sea turtle. Oh, glorious egg."

    scene sanakaoribar25
    with dissolve

    k "You did it! You got it right! Congratulations!"
    sa "I...really don’t like when you two...speak...like that..."
    s "Like what?"
    sa "Like...saying things that don’t really make sense..."
    sa "It makes me...a little uncomfortable...like...like something...weird is..."

    scene sanakaoribar26
    with dissolve

    sa "Is...going on..."
    k "There is nothing weird about the baby sea turtle, mini Sara! They are at their most adorable when they have to flip-flap flip-flap across black sandy beaches, dodging talons of predators along the way."

    scene sanakaoribar27
    with dissolve

    k "In a sense, that is what we all do every day in this human life!"
    k "We wake up and slide our fleshy motion tubes out of our soft rectangle, hoping that the giant welcome box we live in does not dissolve into the earth!"
    k "Then, we pour ourselves a deep ceramic plate of sugar squares coated in cow juice to ward off the evil as we make our way into the world itself!"
    k "But before we can leave, we have to stare back at ourselves! "
    k "Thank our organs and remember to smile! "
    k "For the moment we forget to do those things, the welcome box becomes an {i}unwelcome{/i} box."

    stop music
    play sound "static.mp3"
    scene sanakaoribar28
    with flash
    stop sound

    k "And it all decays from there."

    play sound "static.mp3"
    scene sanakaoribar29
    with flash
    stop sound
    play music "calmbar.mp3"

    yu "What are you doing?"
    sar "Who, me? Oh, you know...Just being irresponsible with my money and buying Sana a drum set as an early Christmas present."
    yu "Oh, shit. "
    yu "Here’s hoping she ain’t a piece of shit like my daughter and doesn’t toss it off a bridge."
    sar "I doubt she’ll be strong enough to lift it. Us Sakakibaras aren’t exactly known for our {i}strength.{/i}"
    yu "What {i}are{/i} you known for, then? Apart from running the least popular bar in all of Kumon-mi."

    scene sanakaoribar30
    with dissolve

    sar "Hmm..."
    yu "..."
    sar "..."

    scene sanakaoribar31
    with dissolve

    sar "Wanting to fuck our teachers?"
    yu "Dude."

    play sound "static.mp3"
    scene sanakaoribar32
    with flash
    stop sound

    s "So, Sana...you’ve made new friends...joined a club...and can now (At least partially) conquer a conversation with the single most confusing person I have ever encountered."
    s "Would it be preemptive to label today’s meeting as a graduation and finally put an end to your training arc?"
    sa "It...doesn’t feel like much of a...graduation and...and I still have a lot of improving to do, but..."
    sa "If you think...I’ll be okay...then I’ll probably be okay..."
    k "Congratulations, mini Sara. Most people do not make it to the amount of words I was able to say to you. They always run away."
    k "I will reward you by writing your name in my special notebook of friends. And, if you do not count animals, you are one of the first ten entries! "

    scene sanakaoribar33
    with dissolve

    sa "Uhh...thanks...but I...I don’t really...need a reward for...existing..."
    s "How about a drink then?"

    scene sanakaoribar34
    with dissolve

    sa "Why do all of the adults I know always encourage me to drink?..."
    k "I will not allow the mini Sara to consume the dizzy drinks on my watch. "
    k "She may have reached the age of sexual maturity, but is still far too young to partake in an activity as hellacious as the consumption of alcohol! "
    k "You may reward her with a child instead."
    sa "I...think I’m going to refuse...both of those things..."
    sa "I...talk too much when I drink and...and I want to start...talking...{i}without{/i} that..."
    s "Then...I guess it’ll just be an entirely unceremonious graduation and we’ll all go on with our lives in the exact same fashion we’ve been going about them thus far."

    scene sanakaoribar35
    with dissolve

    k "By dodging the talons of predators!"
    s "..."
    sa "..."
    sa "By..."
    sa "Dodging the talons of predators..."

    scene black
    with dissolve2

    "The three of us make a toast, but I am the only one who drinks."
    "That is, until Sara and Yuki rejoin me and the rest of the night goes by with us constantly asking Kaori for refills."
    "Sana goes home somewhere around my third or fourth beer, but I don’t see her leave."
    "Around my sixth, I begin to wonder if it has anything to do with the fact that she’s already accustomed to never saying goodbye to those she cares about."
    "Around my ninth, I think of a lamb."
    "Though, I’m not quite sure why."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar55 = True
    stop music fadeout 7.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label ayanesanabeach2:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
    if sana_love >= 35 and utamaid5 == True and christmas7 == True and bar35 == False:
        jump bar35
    if sana_love >= 40 and sanadorm35 == True and bar40 == False:
        jump bar40
    if sana_love >= 45 and thirdreset3 == True and futabadorm45 == True and bar45 == False:
        jump bar45
    if sana_love >= 50 and day351 == True and sarasex == True and sanadorm50 == True and bar50miss == False and bar50 == False:
        jump bar50
    if sana_love >= 55 and imanispecial1 == True and day < 5 and bar55 == False:
        jump bar55
...
```