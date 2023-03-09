# Outcry of the Hunted Hare
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidate50&go=Go)


Part of event chain [Wither](./kaoridate25.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: amidate50
* Group: Ami
* Triggered by label: kaoridate25

## Event code
File: \game\AmiEvents.rpy
Code:
```python
...
label amidate50:
    $ totaldays += 1
    $ day = 7

    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
    else:
        "ERROR ADVANCING TO SUNDAY"

    play music "beginningoftheend.mp3"

    "To see a World in a Grain of Sand\nAnd a Heaven in a Wild Flower"
    "Hold Infinity in the palm of your hand\nAnd Eternity in an hour"
    "A Robin Red breast in a Cage\nPuts all Heaven in a Rage"
    "A Dove house filld with Doves & Pigeons\nShudders Hell thr' all its regions "
    "A dog starvd at his Masters Gate\nPredicts the ruin of the State "
    "A Horse misusd upon the Road\nCalls to Heaven for Human blood"
    "Each outcry of the hunted Hare\nA fibre from the Brain does tear "
    "I wind up being swallowed by the bed sometime in the middle of the night."
    "My skin fuses to the fabric of the sheets and I need to peel it off each time I roll over to get a dose of colder air."
    "I hear the door open at several points but never have the resolve to open my eyes and see who it is."
    "Nor do I {i}need{/i} to because it could only be one person."
    "I hear it close just as often as I hear it open- but I guess it wouldn’t really be possible to hear one without the other now that I think about it."
    "I clutch the sheets and focus on the threads of fabric, fraying from being constantly used and abused over the years."
    "I wonder if these too are wiped clean each time I come down from the rooftop under a starlit sky."
    "And, if not, perhaps it’s time for new ones."
    "I poke a hole in them with my index finger and proceed to sink the tip of it into the mattress."
    "It’s soft."
    "Not like the flesh of a [young]girl, but like a mattress."
    "The door opens again. It is the same girl."
    "This time, she makes it to the foot of the bed and crouches down to whisper something into my ear."

    q "{i}I can’t sleep.{/i}"

    "The words register, but mean close to nothing as I’m unable to react or respond."
    "In fact, these thoughts likely aren’t even my own."
    "I am asleep."
    "I’ve been swallowed."
    "And there is nothing left for me here. "
    "The rest of the night or the day disappears."
    "I can’t tell which it was or is."

    scene her1
    with dissolve4

    s "..."
    te "..."
    te "Good morning."
    s "..."
    te "What? Aren’t you glad to see me?"
    s "..."

    "I am asleep."
    "I’ve been swallowed."
    "And there is nothing left for me anywhere."

    te "You’re late, you know."
    te "And look at you- sleeping in on the lord’s day. You need to wake up or God will cut your hands off and feed them to his angels. It’s true because I said so."
    s "..."
    te "Room for one more in there? If you’re so insistent on going to Hell, I may as well come with you. "
    s "..."
    te "..."
    te "Fine."
    te "But, you know..."
    te "Sooner or later, you’re going to have to come out of there."

    play sound "static.mp3"
    scene her2 with flash
    stop sound

    a "..."
    s "..."

    "I awaken regurgitated, covered in acids and fluids I carried with me out of some sort of celestial esophagus. "
    "And before me stands one of the only things that I have come to terms with loving."

    a "..."
    s "..."
    s "Is that-"
    a "Yeah."
    s "..."
    a "Does it...look okay?"
    s "..."

    "I remember that dress."
    "I-"

    play sound "static.mp3"
    scene her3 with flash
    stop sound

    a "Sensei?..."
    a "Should I...have not worn this?..."
    a "I know I said I’d never touch any of the things we locked away, but..."
    s "Good morning, Ami."
    a "..."
    s "..."

    scene her4
    with dissolve2

    a "Good morning, Sensei..."
    s "..."
    a "I had a bad dream."
    s "..."
    a "..."
    s "You can tell me about it on the way there."

    scene black
    with dissolve2

    "Ami nods through a half-broken smile and the sound of suppressed delight crosses her teeth as if it’s a point of no return."
    "In some ways, I think it might be."
    "But just like the morning’s first moments of joy, I suppress them enough to crawl out of bed and hug my [niece]."
    "She cries into my shoulder without saying a word."
    "She grows stronger by the day."
    "I fade into the background."

    scene sky
    with dissolve2

    "The two of us make our way to the bus stop and Ami talks a bit about how she spent the majority of last night filtering through boxes in the attic that once belonged to her mother."
    "She tells me about how much she’s been missing her lately and how the recent increase of exposure to the sun has reminded her of her youth."
    "She says this as if her youth has already vanished."
    "In a sense, I can see why she would think that."
    "The world was stripped away from her, leaving nothing but a melancholic deadbeat to care for her when he can’t even properly care for himself."
    "Only now, in this second shot at life, are the traces of her youth resurfacing- and even those are plagued by an unending misery in which she’ll never be able to truly overcome them for she can never grow old."
    "We’re all trapped in cages resembling personal hells, and I often forget how cramped hers is sometimes."
    "It wouldn’t have to be that way if she’d only stop leaving so much room for me."
    "We get on the bus and sit near the back. No one else rides with us."
    "The sun sneaks higher than the trees and the clouds and blinds me to the point where I need to give up a hand just to block its rays for the duration of the trip."
    "It makes it harder to pay attention to Ami’s recollection of her nightmare, but I do what I can because I know how hard it must be for her to tell me about it."
    "It goes something like this:"
    "She got to dance with her mom."

    scene her5
    with dissolve2

    "O world-"
    "Where have you gone?"

    a "..."
    s "..."

    "Ami stands before the resting place of her parents in complete silence, trying to find the words to summarize all of the anguish she’s felt without them."
    "I’m sure she’ll counteract it with tinges of good things, but are there truly enough of them to offset the underlying misery in what it means to be eternally alone?"
    "Are those fleeting moments of joy joyous enough to quell even a fraction of the pain she must have felt tying a sash around her mother’s dress?"
    "What about the feelings that spilled from whatever mirror she glanced into to make sure it fit right?"
    "What sort of things will she say to quiet the rumbling beneath us?"
    "And what should I say to her when they all fall flat?"

    a "..."
    s "..."

    "Ten more minutes of silence."
    "Then words."

    a "You looked better in this than I do."
    a "I don’t think I’ll ever be as tall as you, so I made a few adjustments to keep it from dragging."
    a "You always got upset with me when I got my dresses dirty...so I didn’t want to disappoint you...because I know you’re always watching."
    a "I wonder if you’d still seem as tall if I got to stand next to you today?"
    a "When I was little, it kind of felt like you were the biggest thing of all."
    a "But with a name like yours, I guess that was kind of bound to happen, huh?"
    a "Um..."
    a "So...let’s see..."
    a "Oh! We had another Christmas party recently."
    a "There was a little bit of drama, but I think most of us had fun overall."
    a "I sang in front of everyone, too! And, just so you know, I’m a lot better now than I used to be when we would sing together."
    a "You had such a beautiful voice."
    a "I still get that old song you’d sing to me in bed stuck in my head every now and then."
    a "Daisy...Daisy...Give me your answer do...and look! My hairpin even has one in it! Nice touch, right?"
    a "..."
    a "I miss you, Mom."
    a "More than anything in the world."
    a "Sensei misses you too, but he’s too afraid of looking weak around me to admit it."

    play sound "static.mp3"
    scene her6
    with flash
    stop sound

    a "Um...I’m doing okay in school, I think..."
    a "It’s kind of hard to tell with how Sensei grades stuff. When there...{i}is{/i} stuff to grade. Which...isn’t very often."
    a "And...um...the manga club is going well. We’re all reading this one series I think that you’d like a lot."
    a "The plants from our old house are still alive somehow. I’ve been taking good care of them since you’ve been gone and they’ve lasted way longer than I ever thought they would."
    a "Um...I’m a maid now. But not like a real maid. I just work at a cafe. I’d show you the dress if I could."

    scene her7
    with dissolve

    a "I still eat right before bed sometimes, which is a thing I probably shouldn’t be telling you since you’ll get mad at me- but I kind of promised I’d tell you everything, so..."
    a "I...uhh..."
    a "I miss you? Which I think I’ve said already but I really miss you so I’m just going to say it again."
    a "Daddy, too. Can you tell him that? Sensei’s been doing an okay job as my new dad, but he doesn’t pay enough attention to me sometimes and...uhh..."
    a "Did I...mention I...really miss you, Mom?..."

    play sound "static.mp3"
    scene her8
    with flash
    stop sound

    se "I miss you too, my sweet girl."
    se "There’s not a single day that goes by where I don’t think of you."
    se "I’m sorry I can’t be there to watch you grow."
    se "I’m sorry I can’t be there to help you fix up my old dresses- which you look beautiful in, by the way. Much better than I ever did."
    se "But most of all-"
    se "I’m sorry you feel so alone."
    se "I do too."
    a "..."
    se "I’m always here, though."
    se "Even if you can’t see me."
    se "Even if you can’t feel me."
    se "I can still feel you, Ami."
    se "You’re as warm as ever."
    a "Do you think she’s here, Sensei?"
    s "..."
    se "..."
    a "Do you...think she’s listening?"
    a "I hope I look okay...I really wanted to be pretty for her today."
    s "You are..."
    s "I’m sure she’d be proud."
    a "..."
    se "Can you look at me, Ami?"
    a "..."
    s "..."
    se "..."
    se "I didn’t think so."
    se "I have to go now. I have things to do."
    se "But take care of yourself, okay?"
    se "And your uncle too. He’s helpless on his own."
    se "I love you, Ami."
    a "I love you, Mom."

    play sound "static.mp3"
    scene her9
    with flash
    stop sound

    a "..."
    s "..."
    a "She was here..."
    a "I know she was..."

    scene black
    with dissolve2

    "A gust of wind tears thousands of cherry blossoms away from their home and off to someplace new."
    "My eyes follow them because there’s somewhere else they’d rather not look."
    "Ami falls to her knees and begins to sob uncontrollably."
    "It was only a matter of time."
    "But, all things considered, she’s been a lot more composed this time around than the last."
    "I won’t pretend to know why or even search my mind for clues, for I know the second I find any that they’ll pour out from my mouth even faster than the tears in Ami’s eyes."
    "This is a moment for her and her only."
    "I can not allow my constant need to involve myself in every facet of everyone’s lives to get in the way of that."
    "She must cry."
    "She must cry until her eyes swell shut."
    "And then she must get off the ground-"
    "Wipe the dirt from her mother’s dress-"
    "And smile."

    scene her10
    with dissolve2

    a "Okay...now it’s your turn."
    s "My turn?"
    a "They were important to you too, Sensei. You can’t just {i}not{/i} speak to them."
    s "Ami, I don’t really want to ruin a good moment by expressing my thoughts on talking to the deceased."
    a "I bet {i}they{/i} would talk to you if you were the one who died. I know I would."
    a "You’re not allowed to die, though. I love you too much."
    s "I will do my best to continue...indefinitely living."
    a "Um...can I ask for something selfish?"
    s "I already told you that I’m not giving you an allowance anymore. Stop trying to revive that when you already have a job."

    scene her11
    with dissolve

    a "The only reason I have a job is because you think all of the things I do for you aren’t worth new clothes and manga and stuff."
    s "And I will remain steadfast in that belief, but please carry on with your selfish request, whatever that may be."

    scene her12
    with dissolve

    a "I don’t want to go home just yet."
    a "I want you to spend the entire day with me."
    a "I want it to be a real date."

    if amifingered == True:
        s "A real date sounds fine. Especially since I very likely know how it will end with you."

        scene her13
        with dissolve

        a "Sensei! My parents are literally right there! You can’t say that!"
        s "Say what? It’s not like I said {i}how{/i} it will end. I just-"
        a "They were adults when they died! They will obviously know what you mean by that!"
        s "Again, I technically didn’t do anything wrong just now."

    else:
        s "What do you mean by a “real” date, Ami? Because I’ve already told you that-"

        scene her10
        with dissolve

        a "I know what you’ve told me. And I’m not expecting you to change that or do anything you think is weird that {i}really isn’t that weird{/i}, but I understand."
        a "Even if nothing comes of it, I want to go on a date."
        a "I want to spend the entire day with the person I love more than anything else in the world."
        a "I deserve it every once in a while if you’re really not going to give me an allowance."
        s "..."
        a "..."
        s "You know you’re really annoying sometimes, right?"
        a "I’m supposed to be annoying. I’m your [niece]."
        s "I don’t really think it works that way..."

    s "But fine. I’ll go on a date with you."

    scene her14
    with dissolve

    a "Yay! A whole day with Sensei that I only kind of had to force out of him!"
    s "Here’s hoping the next part of it is significantly less painful and tear-filled than the first."

    scene her10
    with dissolve

    a "Oh, it will be. I already know where we’re going. And it’s somewhere I think you’ll like a lot."
    s "That is a bold claim. There are not many things I like."
    a "Well, you just wait, Sensei. Because this place is going to knock your socks off."
    a "I just..."
    a "I just wanna talk to my mom one more time before we leave, okay?"
    s "..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    s "Obviously. Even I wouldn't say no to that."
    a "Heheh~ You know you can talk too if-"
    s "I’ll be waiting at the entrance. Take your time."
    a "Sensei! At least stay here if you’re not going to talk to them!"

    "Ami lowers herself to her knees and places both hands upon her parents’ grave."
    "There are no gusts of wind or homeless cherry blossoms to distract me from the sight this time."
    "I watch her break down once again, knowing full well that it will likely not prepare me for the many more times I’ll have to watch her do this exact thing."
    "Some things, you can never get used to."
    "And the pain of someone you genuinely love is one of them."
    "I press my hands together and attempt to pray {i}for{/i} something {i}to{/i} happen."
    "Nothing happens."
    "Not even a gust of wind."

    $ renpy.end_replay()
    $ ami_love += 3
    $ amidate50 = True

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump amidate50p2

label amidate50p2:
...
```

## Code that triggers this event
File: \game\KaoriEvents.rpy
Code:
```python
...
scene black
    stop music

    "{i}Why does everything have to hurt so much?{/i}"

    yu "Yo, are you fuckin’ for real?!"
    yu "You’ve gotta call your electric company or some shit, Tsuneyo. This is gettin’ out of hand."
    t "Tojo Ramen sincerely apologizes for the inconvenience. Please remain calm while I attempt to restore the power."
    s "Looks like we probably should have gone to the convenience store after all."
    t "Why would we go there? We have all of the green onions we need and leaving work would not be convenient for anyone."
    s "I wasn’t talking about you, Tsuneyo. I was talking about Kaori and me."
    t "How rude of you to not invite me. I will not forget this."
    yu "Aight, I’m gettin’ outta here. Just put my shit on my tab and I’ll pay you back next-"

    play sound "imscared.mp3"
    scene kaoribridge15
    play music "sanctuary.mp3"

    yu "JESUS fuck, that noise ain’t easy to get used to."
    s "..."
    yu "Wait, where’d Kaori go? She afraid of the dark or something?"
    s "I think she’s said something about that in the past, but...I don’t think she’d really run away because of a five second blackout."
    s "Or how she could even find the door, now that I think about it."
    yu "Tsu-chan, you cool with puttin’ everything on my tab? That girl’s my niece and I probably shouldn’t be lettin’ her wander around in the dark over here."
    yu "No offense but this part of town ain’t exactly the safest thing around."
    t "Tojo Ramen understands and thanks you for your patronage. Please rest assured that these blackouts will no longer happen after today."
    t "For the sake of my business, I can not allow this to continue."
    yu "Yo, you comin’? Should probably help look for her since you’re the one who brought her here and all that shit."
    s "..."
    s "Yeah."
    s "Yeah, I’ll help."

    scene black
    with dissolve2

    "I follow Yuki out of Tojo Ramen burdened by the sensation of a large pit in my stomach."
    "By the time I make my way out into the open air, the pit grows."

    play sound "static.mp3"
    scene kaoribridge16
    with flash
    stop sound

    "I’m unsure of exactly what it grows {i}into{/i}, however."
    "I can feel thin roots sinking into some organs I probably couldn’t name if they were placed on an autopsy table in front of me...and wonder how much of my body’s resources are being siphoned away by them."
    "I wonder if removing them would be as simple as removing weeds from a garden."
    "A plucking motion- followed by a twist. "
    "A lift of the hand to observe the dirt falling off. To observe what wildlife clings to them, acting as yet another siphon."

    yu "Kaori? You around? "
    yu "I’ll give you a ride home. Just need you to like...come out and shit."
    s "..."

    "I look, but I don’t look far."
    "I don’t know how, but I can tell we aren’t going to find her."
    "Of course, I can’t bring myself to say that because I don’t want Yuki to worry."
    "And I guess {i}I{/i} don’t want to worry either."
    "Everything will be okay."
    "Everything is normal."

    play sound "static.mp3"
    scene kaoribridge17
    with flash
    stop sound

    "Everything is normal."

    scene black
    with dissolve2

    "Yuki gives up on searching and decides to go home."
    "I do the same."

    stop music

    "{i}Kaori’s aff____________________xxxxxxxxxxxxxxx{/i}"
    "........."
    "......"
    "..."

    scene kaoribridge18
    with dissolve2

    "Ami was sleeping on the couch when I came home."
    "All of her clothes were off."
    "She is getting so big."

    scene black
    with dissolve2

    "Sleep."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ kaori_love += 1
    $ kaoridate25 = True

    jump amidate50
...
```