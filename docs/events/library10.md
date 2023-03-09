# Upside Down
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library10&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 10



## Next events
None

## Event properties
* ID: library10
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label library10:
    scene upsidedownredux1
    with dissolve2
    play music "morningmoon.mp3"

    "I stop by the library first thing this morning."
    "The impending exams that had flipped this place on its head recently have finally ceased to be and Futaba and I can now go back to being normal."
    "Or at least as normal as we can be as a student and the man who is trying to fuck her."

    f "Thanks so much for helping out lately, Sensei. I really don’t know what I would have done without you."
    s "I’m sure you would have managed. It’s just a library after all."

    f "Calling it {i}just{/i} a library really diminishes the work I do, you know."
    f "If I had been doing everything on my own, organizing all of the shelves would have taken twice...or maybe even three times as long."
    f "I wouldn’t have had any time left to write that assignment you gave me."
    s "Oh, right. That's a thing I asked you to do."
    s "How is that coming, by the way? We haven’t really talked much about it since then."

    scene upsidedownredux2
    with dissolve

    f "I, uhh..."
    f "I think...I’m finally ready to show you something."
    f "But it's not done yet, so...you have to promise not to laugh if it doesn’t live up to your expectations..."
    s "Don't worry, Futaba. I won't laugh even if it's the worst thing I've ever read."

    scene upsidedownredux3
    with dissolve

    f "Was that...supposed to make me feel better? Or..."

    "Futaba nervously slides a notebook across the table to me."
    "I quickly flip through the pages to find that her story is the only thing written in it."
    "Why she decided to write it in the {i}middle{/i} of the book instead of where any sane person would write it, I have no idea."
    "But it appears to be only a few pages long, so I should be able to knock it out rather quickly."

    s "Futaba...You know you could have used your normal notebook, right? You didn’t have to buy a new one just for this."

    scene upsidedownredux4
    with dissolve

    "Futaba shakes her head once in disagreement. The long braid draped over her shoulder dances across her chest and quickly catches my eye before settling back in place."

    f "I figured it would be best to buy a new one so you wouldn't go snooping through my notes."
    s "Oh? Are you keeping something in there that I should be worried about?"

    scene upsidedownredux5
    with dissolve

    f "’Worried’ probably isn't the right word...But I’d definitely prefer if you didn’t see anything in there."

    if bonus == True:
        s "I get it. It’s not unusual for a girl your age to want some privacy."
        s "I guess I'll just have to ask one of your classmates what sorts of things you've been writing about me in there."
        f "Umm...please don't."
    else:
        s "Futaba, it's fine. Twilight sold millions of copies and only had like, three adjectives used across four books."
        f "Guh..."

    s "I was kidding. Your notes are {i}your{/i} notes and...all I'll read is whatever you just handed to me."

    scene upsidedownredux4
    with dissolve

    f "Thank you, Sensei...But again, please don't expect too much."
    s "You've already surpassed my expectations with this avant-garde approach of writing in the middle of the book, so I'm already at the edge of my seat."
    f "Well, I-"

    scene upsidedownredux6
    with dissolve

    f "Wait, what? The middle of the book?"

    scene black
    with dissolve

    "I carefully flip back to the start of the story and begin to read..."
    "Futaba quickly gets out of her chair and stands beside me, causing me to think for a moment that maybe she'd given me the wrong notebook on accident."
    "But once I begin reading and she doesn't stop me, I realize that might not be the case at all."

    scene upsidedownredux7
    with dissolve

    f "What is-"
    f "That's not my handwriting..."
    s "{i}Somewhere, in the middle of nowhere, there is a house.{/i}"
    s "{i}This house, which seems ordinary on the outside, is actually anything but.{/i}"
    s "{i}You see, this house is upside down.{/i}"
    s "{i}Normally, if you flip a house on its head, the people inside of it will fall down.{/i}"
    s "{i}But the girls living in this one don’t.{/i}"
    s "{i}In fact, some of them even prefer to live this way.{/i}"

    "I pause for a moment and wait to see if Futaba has anything to say, but she remains as still and silent as a corpse."

    s "{i}You see, this house sits at the edge of the universe.{/i}"
    s "{i}And much like the country we live in, this place has its own set of rules.{/i}"
    s "{i}Don’t stay up too late, don’t eat more food than you require in a day, and don’t question Papa.{/i}"
    s "{i}It’s that easy!{/i}"
    s "{i}As long as the rules are followed, everyone can live a happy life devoid of any negative feelings whatsoever.{/i}"
    s "{i}It’s a truly wonderful place!{/i}"
    f "..."
    s "..."

    s "Umm...Futaba...What exactly am I reading?"

    scene upsidedownredux8
    with dissolve

    f "I have no idea...I've never seen this book in my life."
    s "So...you just happened to give me someone {i}else's{/i} creative writing project instead?"
    s "It's okay to be embarrassed with your work, but denying that you wrote it is just-"

    scene upsidedownredux9
    with dissolve

    f "I really didn't write this, though! I swear!"
    s "Well, did you swap notebooks with someone on accident or something?"
    f "I...I don’t think so? I hadn't even taken this one out of my room until today..."
    f "I don’t understand this at all..."
    s "Should we keep reading? It's not over yet."
    f "I...suppose we can? But this is...really starting to weird me out."

    scene upsidedownredux10
    with dissolve

    "Futaba moves a little closer to me as I try to find where we left off..."

    s "{i}There are so many books here, yet none of them say anything. I wonder why that is?{/i}"
    s "{i}Is it because I’ve already read them, or because I simply cannot see?{/i}"
    f "Whose perspective is this coming from?..."
    s "I don’t know. It was being narrated a minute ago, but...it seems to have swapped storytellers or something."
    f "This is so weird...I have no idea how this happened..."

    "I continue reading."

    s "{i}The smell was horrible coming from the boiler room.{/i}"
    s "{i}It was like burnt rubber mixed with rotting flesh. A truly horrible scent.{/i}"
    s "{i}No matter how hard I try to forget it, it clings to my nostrils and sticks in my hair.{/i}"
    s "{i}It makes me want to shed my skin.{/i}"

    scene black
    with dissolve

    s "Okay. That's enough of that."

    "I abruptly close the notebook and toss it back onto the table."
    "Futaba looks down at it for a moment like she's caught in a daze before sitting back down to regain her composure."

    scene upsidedownredux11
    with dissolve

    f "I don't get this at all...it was a brand new notebook..."
    s "You don’t think...Rin could have a similar notebook or something, do you? Or maybe she's just trying to fuck with you?"
    s "You two share a dorm. I don't think it's impossible that she-"

    scene upsidedownredux12
    with dissolve

    "Futaba starts shaking her head before I can even finish my sentence."

    f "It’s not possible. I’ve read Rin’s writing before and it’s nothing like this. The handwriting is different too."
    f "This is just plain creepy..."
    s "It was definitely weird...but I wouldn't put past someone as weird as her to write something like this."
    f "It wasn't Rin, Sensei...I'm absolutely certain of that."
    s "..."
    f "..."
    s "Well, I guess it would probably be for the best to just throw that thing away or...bring it to the lost and found or something."

    scene upsidedownredux13
    with dissolve

    f "I agree. I'll be sure to do that as soon as I leave here today."
    s "As for {i}your{/i} story, do you think it’s still in your dorm room somewhere?"

    scene upsidedownredux14
    with dissolve

    f "I really hope so! I've been working hard on it and...am not comfortable with anyone other than you reading it just yet."
    s "Well, check when you get back and let me know. It sucks we couldn’t read it today after all the effort you put in."

    scene upsidedownredux15
    with dissolve

    f "It’s fine. If anything, I’m sorry that you had to read something as weird as...whatever {i}that{/i} was just now."
    s "There’s no need to be sorry, Futaba. Well, unless this is some really abstract, confusing prank that you're pulling on me. If that's the case, you can apologize and I will accept."

    scene upsidedownredux16
    with dissolve

    f "I'm not really the type of person to play pranks on others...nor would I understand how this would even count as a prank."
    s "Then I guess we'll just have to live in a state of perpetual mystery in which we never discover why this happened or who was responsible for it."
    f "I'll ask Rin just to be sure, but...again, I really don't think it was her..."
    s "Let's just try to put it behind us for now and...hang out like we always do. Without any weird boiler rooms or indiscernible narrators."
    f "Good idea, Sensei...I know we didn't read much of it, but..."
    f "That story was really starting to make me feel a little uncomfortable..."

    scene black
    with dissolve2

    "Futaba and I continue to talk for the rest of the morning, never once returning to the words found inside of that strange notebook."
    "She wasn't the only one who felt uncomfortable, though."
    "Even now, each time I think about it, it feels like my stomach is tying itself in knots."
    "Or at least something like that."
    "I eventually leave the library."
    "The knots untie themselves."

    stop music fadeout 5.0

    $ renpy.end_replay()
    $ library10 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library15:
...
```

## Code that triggers this event
File: \game\FutabaEvents.rpy
Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
...
```