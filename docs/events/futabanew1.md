# Broken Flowers
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabanew1&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 15

✅Event "[Futaba: Self-Insert](./library15.md)" is completed (event=library15)



## Next events
* [Futaba: Great Burdock Leaves](./futabanew2.md)

## Event properties
* ID: futabanew1
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label futabanew1:
    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Futaba’s door and wait for her to answer, knowing full well that she will because she is Futaba and I am the knight in shining armor that she dreams about each night."
    "It’s not a role I ever imagined assuming, and I’m not about to start acting chivalrous now that I’ve come out and acknowledged it."
    "But it {i}is{/i} nice knowing that someone out there is willing to entrust their whole self to me."
    "I say this despite having not yet taken any of the interesting parts of her into my arms."
    "I say this despite not having anything to save her from."

    f "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I steel my nerves in preparation for a late night encounter with a damsel undistressed. "
    "Her room smells of the same lavender perfume she so commonly wears."
    "And my mind sinks to the same depths it so commonly hides away in."
    "........."
    "......"
    "..."

    scene futabarevision1
    with dissolve2
    play music "love.mp3"

    f "Hey...Sorry for looking like this again. I planned on spending the rest of the night writing, so I got changed as soon as I came home."
    f "I hope...that’s okay?"
    s "It will never {i}not{/i} be okay. And I’m glad to see you’re still throwing yourself at this story."

    scene futabarevision2
    with dissolve

    f "I would have had a harder time {i}not{/i} throwing myself at it after all of the encouragement you gave me after reading the first part."

    scene futabarevision3
    with dissolve

    f "In fact, I’ve already made tons of changes! I even brought Pedro back to life!"
    s "Good. He never deserved death in the first place."

    scene futabarevision4
    with dissolve

    f "No...I actually felt really bad when I seriously started thinking about it. Which...I probably shouldn’t since he’s just a character I made up, but..."
    f "It’s kind of hard...{i}not{/i} getting attached to...people and creatures inside of your head, don’t you think?"
    s "Well, I haven’t written anything in...longer than I can remember. But I get what you’re saying."

    scene futabarevision2
    with dissolve

    f "Pedro isn’t...the only character that’s changed either."
    s "Oh? Does my- "
    s "Or, uhh...sorry. {i}Does the male character{/i} have anything interesting about him yet? Or is he still the...blank slate he’s designed to be?"

    scene futabarevision5
    with dissolve

    f "I don’t think he’s a blank slate at all. I actually...really like him for who he is in the beginning of the book. And he’ll develop even more as the story progresses."
    f "All of the biggest changes...actually involve the heroine of the story."
    s "Oh?"

    "Well, that’s unexpected. I was pretty sure that Futaba’s Mary Sue esque protagonist was just her version of a self-insert-"
    "A way to sneak into her story on a more personal level without naming the character “Futaba.”"
    "But apparently, she wasn’t good enough to make the final cut."
    "Take that as you will."

    s "Why did you change her, exactly? The story seemed...completely built around her."

    scene futabarevision6
    with dissolve

    f "And it still is."
    f "But...I read the story again right after you left the library...and something about her just didn’t sit right with me."
    s "Do you know what that {i}something{/i} was?"
    f "Flaws."
    f "All of the best protagonists are flawed. They all have problems...traumas...things that make them feel more human."
    s "Well, the girl in your story was lonely, wasn’t she? I figured her reclusive nature was her biggest flaw."
    f "I don’t...really think that being lonely is a flaw. That’s more of a...result. And the way I had it portrayed made her feel like a victim of sorts."
    f "I never wanted that."
    f "That’s why she didn’t sit right with me. It felt wrong to have her enjoying herself and living her best life without ever revealing her...true colors to anyone. Or any of the things that make her whole."
    s "You have...gotten significantly better at writing since the last time we spoke."

    scene futabarevision7
    with dissolve

    f "D-Don’t just jump the gun and go saying things like that before even reading the changes, Sensei."
    f "This is just my...experience as a reader coming into play. I still have a long way to go before I can create something I’m completely proud of."
    f "Until then, I just have to...keep trying things in different ways and hoping they come out a little more interesting..."

    scene futabarevision8
    with dissolve

    f "After all, I..."
    f "I want the heroine to entertain you. And what’s the point in getting to know someone when all they are can be found on just one small sheet of paper?"

    scene futabarevision9
    with dissolve

    f "A-A-And by “you” I meant the reader! Not {i}you!{/i}"
    f "I want...anyone who reads the story to be interested in the protagonist! Even if...you {i}are{/i} the only person I plan on showing this to!"
    s "This is the same exact “mutated reflection” I was talking to you about."

    scene futabarevision10
    with dissolve

    f "Huh? It is?"
    s "Yeah. It’s only natural for a writer to put a little bit of themself into the main character of a story they’re writing. "
    s "You didn’t like how flawless the heroine of your story was because she didn’t remind you at all of how you see yourself, right?"

    scene futabarevision11
    with dissolve

    f "Well, umm...I...I suppose that’s at least...somewhat true..."
    f "It’s...It’s not as if I was...modeling the main character after myself or anything. That would be...conceited..."
    f "Wouldn’t it?"
    s "If it was, I don’t think you would have spent the whole day trying to make the character worse."

    scene futabarevision12
    with dissolve

    f "Using the word “worse” is...a little hurtful. I think...a person’s flaws are one of the many things that can make that person beautiful."
    f "It’s only when there are...far too many of them that people become ugly..."
    s "And how many {i}flaws{/i} would you say that you have, Futaba?"
    f "..."
    s "Futaba-"
    f "If I tried to write them all down, I’d run out of paper."
    s "..."
    f "..."

    scene futabarevision7
    with dissolve

    f "But, umm...I know that’s not really something you want to hear about and...you’ve already given me {i}one{/i} assignment, so it’s not like I can just tack on another one."
    f "Especially one as silly as that...I’m just...I’m just being a little dramatic. That’s all."
    f "All of this talk about flawed characters and...what heroines are supposed to be like has made me a little self conscious. It’ll pass in no time at all and...I’m sorry for talking so much about it."
    s "It’s fine. I don’t really think you were telling the truth anyway."

    scene futabarevision10
    with dissolve

    f "You...don’t?"
    s "Nope. Because if having too many flaws really made someone undesirable, you’d stop smiling every time you see me."
    f "..."
    s "..."
    f "Was that...a line from a book?"
    s "You think I could have just remembered a specific, relevant quote like that off the top of my head? Of course that wasn’t from a book."
    f "You should...put it in one. You’re so much better at this than I am."
    s "Yeah, well, I’ve probably had a lot more practice than you. I’m a teacher after all. "

    "Even if this isn’t something I would have chosen to do on my own."

    scene futabarevision4
    with dissolve

    f "Umm...do you...maybe want to step outside for a little while?"
    f "I think a...break might be nice. I’ve been kind of going nonstop since I got back and..."
    f "I’d like to talk a little more...if that’s okay."
    s "It’s fine. But I think you might want to get dressed first. I can’t imagine you’d be very happy with the whole world seeing you like that when you’re still embarrassed about {i}me{/i} seeing you in that condition."

    scene futabarevision13
    with dissolve

    f "{size=-10}It’s only a problem because it {i}is{/i} you...{/size}"
    s "Hm? What was that?"

    scene futabarevision7
    with dissolve

    f "Oh! Umm...nothing! "
    f "Just...please go wait in the hall for me."
    f "I’ll get changed and...be back in a moment."

    scene black
    with dissolve2

    "I exit the room, but my mind stays put to watch one of my students undress."
    "She’s thinking about me right now. She has to be."
    "It only makes sense for her to be thinking about me when I’m right here and she is right there, hastily removing her pants so I’m not kept waiting long."
    "I would help her if she’d only ask."
    "Just like with writing, I would teach her all there is to know about love in its most bestial, physical form."
    "I think the same things about her that she thinks about me."
    "But I am different."
    "I would indulge in my desires."
    "And she would rather bring form to her flaws than allow me to peel them back like underwear, stuck to the damp petals of a flower unplucked from its original garden."

    s "..."

    "Hurry up and finish before I return to the depths."

    "........."
    "......"
    "..."

    scene futabarevision14
    with dissolve2

    "We eventually make our way outside and I am able to force away the urge to undress her on my own."
    "I don’t know where her mind ends up, but based on the nonexistent distance between her right arm and my left, I think I may have won the race toward the fleeting purity of this blossoming connection."
    "The petals are mine to pluck as soon as the flower finishes blooming."
    "Oh, if only spring would come tonight."

    f "..."
    s "..."
    f "The..."
    f "The character in my story isn’t...an {i}exact{/i} representation of me, you know..."
    s "I still haven’t met the new version, so I’ll hold my comments until I do."
    f "And I..."
    f "I want you to know that...I don’t think you’re as flawed as you suggested earlier."
    f "I think you’re really amazing, Sensei. And...it probably sounds silly, but...I wouldn’t trade even moments like this one for anything."
    s "I see."
    f "Y...Yeah..."

    scene futabarevision15
    with dissolve

    f "I guess I...just wanted you to know that before the night comes to an end..."
    s "Then I’ll say the same thing to you."
    s "You’re not even half as flawed as you think you are."
    f "Have you stopped to think that...maybe I just haven’t been revised yet?"
    f "You haven’t seen the flaws because...they haven’t been added into my story yet."
    f "Who’s to say if you’ll still be saying things like that when they are?"
    s "Hm."

    scene futabarevision14
    with dissolve

    s "Well, the same goes for me, I guess."
    s "Here’s hoping we don’t wind up hating each other once we learn a little more."
    f "You’d...have to do something {i}really{/i} bad to get me to hate you, Sensei..."
    s "I’m sure I will eventually."
    f "So...until then..."
    f "Is it okay for me to stay with you like this?"
    s "Like what, exactly?"
    f "..."
    s "..."
    f "Don’t worry about it..."
    f "It would just make me sound dumb if I said it out loud."
    s "Then write it down. You’re getting pretty good at that now, aren’t you?"
    f "Maybe, but..."
    f "I think that some thoughts are just better left as daydreams."

    scene black
    with dissolve2

    "Neither one of us speaks another word for the next ten minutes, but there is a silent understanding that we’re both here because we want to be."
    "And that we’re both much uglier than we want to be as well."
    "Somewhere around the eleventh minute, our arms stop touching."
    "Somewhere around the twelfth, Futaba heads back inside."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabanew1 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabanew2:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
...
```