# Remnants of Forgotten Memes
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe5&go=Go)



## Event preconditions
✅Molly love greater than or equal to 5

✅Event "[Molly: NTR & Pregnancy](./mollycafe1.md)" is completed (event=mollycafe1)



## Next events
* [Molly: Something Out of a Nukige](./mollycafe10.md)

## Event properties
* ID: mollycafe5
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe

## Event code
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe5:
    scene cafe_night
    with dissolve
    play music "cafe.mp3"

    "I decide to spend another night at the cafe and see what Molly is up to."
    "I wound up getting sidetracked along the way, so I’m a little later than normal, but they’re still open by the time I get there, so...at least that's good."
    "After stepping closer to the counter and realizing there isn’t anyone behind it, however, I begin to wonder if I'm a little too late after all and that...Molly just forgot to lock the doors or something."
    "That seems like a thing she would do."
    "But just as I'm about to leave, I hear some strange sound effects coming from the corner of the room..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mollyphonegame1
    with dissolve2

    "I take a step closer to the sounds to find none other than my favorite Irish student (Out of one total) tapping away at what I imagine is a game on her phone."
    "She’s humming happily along with the song that's playing and is so wrapped up in it that she doesn’t even notice I’m here."
    "Would this be cause for concern if I were an actual customer? Of course. "
    "But I’m not, so I suppose I'll continue letting her do her thing until she notices me."

    mo "Hmm hm hmmm. Hm hmmm hmm hmmm~"
    s "…"
    mo "Hmmmm hm HMMMM. HMMM hmm HMMM~"
    s "…"
    mo "HMMMMMM HMM HMM HMM HMMMHMMMM~"

    "The song picks up the pace and Molly’s fingers begin to dance quicker across the screen."
    "This must be one of those rhythm game things I’ve heard Ami talking about in the past."
    "And even though Molly seems to be having a good time, I’m not sure if I want to just stand here and watch her for the next...however long I’m going to be here for."

    s "Molly."

    scene mollyphonegame2
    with hpunch

    mo "AH! I DIDN’T DO IT, I SWEAR!"
    s "...Didn’t do what?"

    scene mollyphonegame3
    with dissolve

    mo "Oh. It’s you."
    mo "Top o’ the mornin’, Sir."
    s "It’s the middle of the night. And stop saying “Top o' the mornin'” just because you’re Irish. It’s cliche."

    scene mollyphonegame4
    with dissolve

    mo "I had to say it at least once, Sir. I think it's some sort of...unwritten rule for Irish characters."
    s "Anyway, what are you up to? Playing a game?"

    scene mollyphonegame5
    with dissolve

    mo "I {i}was{/i} in the middle of a full combo until you decided to show up and scare the pants off of me."
    s "Your pants are very much on right now."
    mo "My metaphorical pants. The ones I wear over my normal pants. They only come off when I get scared."
    s "Molly, you’re a really weird girl. You know that, right?"

    scene mollyphonegame6
    with dissolve

    mo "Yes! I've been being reminded for as long as I can remember. But that’s what makes me so lovable!"
    mo "Besides, you’re pretty weird yourself. Aren’t you, Sir?"
    s "In what way?"
    mo "I used 'Detect Thoughts' on you when you weren’t paying attention in class the other day."

    if bonus == True:
        mo "You think about some pretty unsavory things, Sir."

    "As much as I want to say that the sort of magic Molly is referring to is impossible, I literally watched a girl her age reset the world a little while ago."
    "So I guess nothing is off limits, really."
    "But either way, I doubt Molly has actual mind-reading powers and that this was probably just a lucky guess."
    "If she {i}actually{/i} had mind-reading powers, she would know that I've been picturing her without her clothes on this entire time."

    s "Okay, Molly. If you’re so smart, what am I thinking right-"

    scene mollyphonegame7
    with dissolve

    mo "You really want me to say it, Sir?"
    mo "What if the security cameras in here record audio? You could get in a loooooooot of trouble~"
    s "…"
    mo "…"

    "I'm just going to assume that she's only able to successfully guess these things because I am a generally creepy person."

    s "As a growing boy, I believe I should be forgiven for all of the impure thoughts plaguing my mind."

    if bonus == True:
        scene mollyphonegame8
        with dissolve

        mo "That can't be true, Sir. You should have stopped growing a long time ago. "
        mo "Even I am barely growing at this point and you’re much older than I am."
        s "It was a joke, Molly. Now, I only grow when I get excited."

        scene mollyphonegame9
        with dissolve

        mo "Ahh! Penis joke!"
        mo "I’ve read enough eroge to know what you mean by that!"
        s "Oh, right. I forgot that you were an expert in all things depressing."
        mo "What’s so depressing about spending hundreds, if not thousands of hours seducing fictional characters?!"
        mo "It's all of the fun with none of the cleanup!"
        s "Cleanup?..."

        scene mollyphonegame10
        with dissolve

        mo "Bodily fluids! Scrunched up tissues! Messy hair! The whole kitten caboodle!"
        s "Wow. Your mind is even further gone than I thought."
        mo "You’re the one who asked, Sir! Don’t pretend you don’t know what I’m talking about!"

        scene mollyphonegame11
        with dissolve

        mo "Besides, who even cares if somebody is into that kinda stuff? It’s not like 2D romance hurts anybody."
        s "I know that. You can be into whatever you want to be into. I’m just messing around with you."
        s "Do I think it's depressing? Yes. But I'm not about to stand between you and whatever weird fetishes you have."
    else:
        mo "Yes you are, and I am very proud of you."
        s "Thank you, Molly. You always know how to turn my frown upside down."

    scene mollyphonegame12
    with dissolve

    mo "Thank you, Sir! Appreciated! I was worried we were about to reach a bad end!"
    s "A bad end this early in your story would be really unfortunate."
    mo "Reviews would plummet. I can hear it now..."
    mo "“This game is too hard! How do I escape the time loop?! Where is the walkthrough?!”"
    s "I’m not sure what any of that means, but I doubt there’s anyone out there who’d be so detached from reality that they’d complain about something like that."

    scene mollyphonegame13
    with dissolve

    mo "You clearly haven’t spent enough time on the Internet."
    s "No, I really haven’t."
    mo "It’s a freakin’ battlefield out there, Sir. "
    mo "Bodies scattered across the plains...The remnants of forgotten memes, desperately clawing their way out of the depths of the Earth..."
    mo "It is literally Hell. And I haven't even told you about Twitch chat yet."
    s "Well then, why do you spend so much time on the Internet if it's that horrible? Wouldn’t it be better to go out and do, you know, real-life stuff?"

    scene mollyphonegame14
    with dissolve

    mo "Real life is hard..."
    mo "The progression system is hidden...and you can’t even check your affection scores with everyone."
    mo "You’ve actually gotta think about stuff...and I've never been good at that."

    scene mollyphonegame8
    with dissolve

    mo "You know, Sir- I read in one game that life is like a staircase. You’ve just gotta keep on climbing."
    mo "Otherwise, if you start to overthink it, you’ll have trouble taking the next step."

    scene mollyphonegame15
    with dissolve

    mo "But to that, I pose a follow-up question!"

    "A fire ignites within Molly’s eyes as she so passionately adds to the quote she just mentioned."
    "Like, a literal fire. There’s actual fire in her eyes. It’s terrifying."

    mo "What that quote does not take into mind is the existence of the escalator!"
    mo "There is a way to live life without climbing up anything!"
    mo "It is possible to rise by just standing still and waiting for everything to pass by you!"
    mo "Is it fulfilling? No! But if you wind up at the same place, it’s much more economical!"

    scene mollyphonegame16
    with dissolve

    mo "And so I, Molly MacCormack, have vowed to live a life on the escalator."
    mo "Who needs stairs when ANYTHING can be stairs?! THE WORLD IS MY STAIRCASE!"
    s "Is it hot closing your eyes with fire still inside them?"
    mo "It burns with the white hot intensity of a thousand suns."
    s "Then open them back up."
    mo "The flames have sealed my skin shut. I shall never see again."
    mo "Please cast 'Cure Wounds' as a third level spell on me, Sir."
    s "I...don’t know how to do that."
    mo "Just touch my head. I’ll act out the rest."
    s "I can’t touch your head until we reach the $5k stretch goal."
    mo "We hit that goal a long time ago, Sir. That line should have been changed with the revamp."
    s "Okay, but I'm still not touching your head. I don't know where it's been."
    mo "Life truly can be cruel sometimes."
    s "It really can."

    scene mollyphonegame7
    with dissolve

    mo "Regardless, I shall persevere. Even in the face of adversity, I shall not falter! I shall not admit defeat at the hands of life itself!"

    scene mollyphonegame12
    with dissolve

    mo "And also because...I'd be letting you down, too..."
    s "…"
    mo "…"

    scene mollyphonegame6
    with dissolve

    mo "How was that? Did I sound like a real character in a dating sim, Sir? "
    mo "Have I advanced to the lead heroine role yet?"
    s "For someone who isn’t interested in live humans, you certainly seem pretty set on becoming an actual love interest. "
    mo "Just in the metaphorical sense. I would be a horrible girlfriend if it actually came down to it."
    s "Why do you say that? You’re weird, but I think you’d be fine if you found the right partner."

    scene mollyphonegame12
    with dissolve

    mo "Thank you, Sir! Please ignore my face if it suddenly changes colors! This always happens when I receive compliments from those I admire!"
    s "You admire me?"

    scene mollyphonegame15
    with dissolve

    mo "Of course I admire you!"
    mo "From the moment I first laid eyes on you, I knew our contract would be one strong enough to outweigh the prying eyes of any non-believer!"
    mo "Together, you and I can weed out the darkness...and bring light back to this dying world!"

    scene mollyphonegame9
    with dissolve

    mo "Oh! But I raid with my guild on Tuesdays and Wednesdays, so we’ll have to weed out the darkness on the other five days of the week instead."
    mo "If that's okay with you, I mean."
    s "Sure, Molly. We can weed out the darkness whenever your schedule allows for it."

    scene mollyphonegame15
    with dissolve

    mo "Excellent!"
    mo "Thank you for understanding and accommodating my hours of availability."
    mo "Now, if you would also be willing to postpone the start of[school] for several hours so I can sleep in-"
    s "Changing[school] hours isn’t really something I’m allowed to do. I would have done that a long time ago if it was."

    scene mollyphonegame5
    with dissolve

    mo "I figured...It was worth a shot, though..."

    scene mollyphonegame6
    with dissolve

    mo "I already like you more than Ms. Watabe anyway, so there’s not really any point in complaining."
    mo "Plus, I already had some friends in your class, so everything's coming up Molly!"
    mo "I just need to work on getting Tsuneyo to like stuff other than noodles and I’ll have pretty much everything I’ve ever wanted."
    s "Pretty much? What else are you missing?"
    mo "A life-sized, realistic statue of my waifu that I can hug before I go to bed at night."
    mo "And an RTX 3080."
    mo "That line didn't even need to be changed since they're still basically unavailable everywhere."
    s "A...what?"
    mo "It doesn’t matter!"
    mo "The point is, as long as the bond between us is not severed, I feel as if all of my dreams will come true!"
    mo "Please do not abandon me! I need you!"
    mo "Think of it like one of those recruitment systems in an MMO where we need to be next to each other to gain an EXP buff!"
    s "Molly, I have no idea what you’re talking about."

    scene mollyphonegame12
    with dissolve

    mo "That’s fine! No one ever does!"
    mo "I’m just happy to have met you! That’s all! Even if you don’t like anime and call me weird all the time!"

    "As always, I have a hard time comprehending what Molly means- but I’m glad that she seems happy at the very least."
    "The truth is, I’m starting to enjoy spending time with her as well. "
    "There are plenty of girls in my life now with a bit more energy than I’m used to..."
    "But I think something about how I {i}never{/i} have any idea what Molly is talking about really...sets her apart from the rest."
    "Now, seeing her in a romantic light is obviously a much different question."
    "Especially when factoring in that I...think she might only be attracted to 2D characters?"

    if bonus == True:
        "But either way, I'm excited to see where this relationship heads..."

    s "I'm happy to have met you too, Molly."
    mo "R...Really?"
    mo "You mean that, Sir?"
    s "Of course. Even if I don't like anime and call you weird all the time."

    scene mollyphonegame11
    with dissolve

    mo "That's totally fine!"
    mo "I won't let you down, Sir! I promise!"

    scene black
    with dissolve2

    "..."
    "You know, maybe this 'contract' thing won't be so bad after all."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe5 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollycafe10:
...
```

## Code that triggers this event
File: \game\MollyEvents.rpy
Code:
```python
...
label mollycafe:
    if molly_love >= 0 and mollycafe1 == False:
        jump mollycafe1
    if molly_love >= 5 and mollycafe1 == True and mollycafe5 == False:
        jump mollycafe5
...
```