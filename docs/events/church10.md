# Sakura Season
Yasu event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=church10&go=Go)



## Event preconditions
✅Yasu love greater than or equal to 10

✅Event "[Yasu: Repentance](./yasudorm10.md)" is completed (event=yasudorm10)

❌Day of week is Sunday



## Next events
None

## Event properties
* ID: church10
* Group: Yasu
* Triggered by label: church
* Triggered by branch label: church

## Event code
File: \game\YasuEvents.rpy
Code:
```python
...
label church10:
    scene black
    with dissolve
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    scene clearnightsky with dissolve2
    play music "newhope.mp3"

    "On nights like tonight, I find myself wandering somewhere between complacency and cowardice."
    "Trying to skirt the line between what it means to fall into form and what it means to break free."
    "But free from what?"

    if bonus == True:
        "The only thing preventing me from floating away is a small anchor surgically inserted into every girl I know. "
        "An anchor that grows as a direct result of how much “warmth” I give them, as someone like Yasu would put it."
        "With each orgasm comes an increased connection that will evolve into increased emotional damage depending on who finds out what and when."
        "And yet I stray..."
        "Further and further into the darkness that some see as light, with my hands clasped together. "

    "My fingers go to war with one another, using the sharp edges of nails to claw away at others who look just like them on the opposing side."

    if bonus == True:
        "A whole other world, though not at all dissimilar to the one they’ve spent 31 years familiarizing themselves with."
    else:
        "A whole other world, though not at all dissimilar to the one they’ve spent 5000 years familiarizing themselves with."

    "That’s the overly intellectual, artistic way of saying that I begin to pick at my nails."
    "I lose track of how hard I must be doing it and manage to cut myself."
    "Blood flows out."
    "Not a lot of blood. But enough to remind me of the color of my [niece]’s hair. "
    "Hers is a lighter shade of red."
    "Just like [[redacted]."

    scene yasublind1
    with fade

    "I make my way into New Hope Cathedral and attempt to shake off any uneasiness that may have snuck into my mind on the journey over."
    "The walk isn’t as bad as the one I so commonly take to the second half of town."
    "In fact, coming here allows me to pass through several locations that make the cold seem not that cold at all."
    "Some nights, when the temperature is low enough, I like to watch the exhaust fumes from the pipes of closing restaurants clash with the winter wind and explode into gray vapor."
    "I like to walk through it, half expecting to feel something, but remembering as I pass through that I, too, am vaporous. "
    "And that the reason I can not feel is not that there are no feelings to be felt, but that I have already felt them all."
    "There is nothing left for me here."

    ya "Blessed be those who give up their eyes."
    ya "Who trade in their sight for the sake of a prize."
    ya "Blessed be those who reach out their hands."
    ya "Who sit in the church, so outside He can stand."
    ya "Good morning, Sensei."
    s "You could tell I was here?"

    play sound "static.mp3"
    scene churchglow1 with flash
    scene yasublind2 with flash
    stop sound

    ya "Of course."
    ya "The door isn’t exactly quiet. "
    ya "And it’s not like anyone else has ever visited me here before."
    s "Right."
    s "So...are you having fun?"
    ya "Not at all."
    ya "I am barred from having fun tonight, you see."
    ya "And so I shall sit here, thinking nothing. Seeing nothing. Being nothing."
    ya "All so He can feel what it means to be alive once more, if even for a fraction of a second."
    s "Well I guess I better go then. I’m a really exciting guy and don’t want you to accidentally enjoy yourself or anything."
    ya "There’s no need to go anywhere, Sensei. I can talk."
    ya "In fact, I’d love for you to stay and chat."

    if bonus == True:
        ya "Though, I implore you not to look at me or attempt to take advantage of me."
        ya "I’m rather defenseless tonight."
        s "You’re barely over five feet tall and I’m pretty sure I could snap you in half with one arm."
        s "You’re rather defenseless every night."
        ya "Hehehe~ "
        ya "Yes. I suppose you’re right about that. "
        ya "But that’s not what I am talking about. "
        ya "Please, take a seat."
    else:
        ya "Do you understand my language yet?"
        ya "(Airplane noises)"

    s "…"

    if bonus == False:
        ya "(Airplane noises again)"

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene yasublind3
    with dissolve

    s "…"
    ya "…"
    s "…"
    ya "Feel free to sit down whenever you like, Sensei."
    s "I’m right next to you."
    ya "Oh. I’m very sorry. You were much quieter than I anticipated."
    s "Yasu."
    ya "Yes?"
    s "I’m really going to need an explanation for this."
    ya "You wish to learn more about he who sleeps?"
    s "I wish to learn more about Yasu who blindfolds herself with tape in the middle of a church at night."
    ya "A much less interesting story, though one I’d be happy to tell."
    s "Please keep it as minimally propagandic as possible."
    ya "Hehehe~ "
    ya "Of course."
    ya "I doubt this aspect would convert you to a believer either way. "
    ya "It is simply how we show our thanks."
    s "How {i}you{/i} show your thanks."
    ya "For now."
    ya "More will come, if they do not already exist."
    ya "They could always be hiding as well."
    ya "I would not blame them if they were."
    ya "Have you ever wanted something you couldn’t have?"

    play sound "static.mp3"
    scene attempting with flash
    stop sound

    s "I-"
    s "…"
    ya "Actually, let me tell you a little anecdote that will explain things better than a simple question would."
    ya "A baby is born. There is no sense in giving it a name."
    ya "It is a normal baby. All of the parts are there."
    ya "The ears, the mouth, the nose, the limbs, the eyes. Everything."
    ya "But some of the parts don’t work."
    ya "If life worked the way a conveyor belt in a shop that mass produces dolls works, and this baby was to be a biomechanical retail product, those parts could be replaced."
    ya "If the arms bent the wrong way, it would receive new arms."
    ya "If the ears heard nothing but a high pitched noise, reminiscent of screeching tires or the whisper of melting plastic, those too could be replaced."
    ya "And while that much reigns true for humans to some extent, one thing that is almost always guaranteed is that those born blind will never see."
    ya "They can not comprehend the colors of the world. "
    ya "They can not gawk at the beauty of the sakura season, smiling as petals fall off of the trees and into their outstretched hands."
    ya "The baby in this anecdote refuses to accept that."
    ya "He grows older."
    ya "He lives for thousands and millions and billions and trillions of years and sees absolutely nothing."
    ya "He lives for so long that his notoriety grows and he becomes known around the world as the man who sees nothing."
    ya "Some people, whether it be through inspiration or pity, wind up surrendering their eyes to him in an effort to restore his vision."
    ya "His original eyes are removed in favor of the new ones, but none of them work."
    ya "The spare eyes are kept in a jar in his home, but the jar gains vision itself and must be put out of its misery."
    ya "He begins to sew the eyes to his body, thinking that maybe his brain would realize what he was attempting to do."
    ya "It realized nothing."
    ya "Eventually, the man was covered in eyes. And yet, he was just as blind as he was when he was born."
    ya "He accepts that he will never see and hides himself away in the depths of a sewer."
    ya "And he sleeps for years."
    ya "He becomes depressed and gives up on eating."
    ya "He dies."
    ya "But he lives for so long before that, covered in eyes to the point of being unable to move...that his other senses begin to dissipate."
    ya "The near deafening silence of a sewer in an abandoned town, where the only sound to be heard is the occasional drip of rain-"
    ya "He tunes it out."
    ya "The taste of the retinal fluid sliding across his tongue and down the back of his throat-"
    ya "He tunes it out."
    ya "All senses are numbed to the point where, when he passes onto the second plane, he does not even realize he has passed."
    ya "But that’s when something wonderful happens."

    play sound "static.mp3"
    scene yasublind4 with flash
    stop sound

    ya "He sees for the first time."
    ya "Not through his own eyes or the eyes that had been gifted and then sewn onto him, as those had all faded into nothingness with his descension."
    ya "But through the memories of the eyes of others, swimming through the air around him."
    ya "Each vision flowed into him. And in return, he shared himself with the visions."
    ya "It was then that he realized he was born as he was for a reason. "
    ya "That being born without vision was not a setback, but the mark of something beautiful."
    ya "Every year of agony was counteracted with a lifetime worth of wonderful sights."
    ya "The birth of all children. Fireworks in the summer. The long awaited sakura season."
    ya "He could smell the petals and hear the sizzle of grilled meat at food stands lining unfamiliar courtyards."
    ya "And yet it all felt so familiar."

    play sound "static.mp3"
    scene yasublind5 with flash
    stop sound

    ya "And then it stopped."
    ya "He had gotten a taste, but the taste vanished as quickly as it had appeared."
    ya "The whispers in the wind saw how quickly the man of many eyes was changing. Growing."
    ya "And it frightened them."
    ya "They started giving their memories to other people instead. "
    ya "People who were not lusting after the chance to start anew, but a chance to relive their lives despite hating so much of them."
    ya "This made the blind man sad."
    ya "But still, he held out hope."
    ya "He knew that one day, word of his story would reach someone."
    ya "Someone who would bridge the gap and connect him to the world."
    ya "But how?"
    ya "The answer to that question is why I am blind tonight."
    ya "I have foregone my own vision so that he may see in my place."
    ya "And I would forego it for the rest of eternity if it meant that he who suffers most would not have to suffer any longer."
    ya "But it does not work that way. "
    ya "I can only sacrifice my sight on nights like tonight."
    ya "Nights where we haphazardly wander between complacency and cowardice, skirting the line between our own comfort and the things we fear the most."
    ya "Do you understand now, Sensei?"
    s "…"
    ya "…"
    s "…"
    ya "…"
    ya "Sensei?"

    play sound "static.mp3"
    scene yasublind6 with flash
    stop sound

    s "Huh? What?"
    ya "Do you understand the reason for the tape over my eyes?"
    ya "I’m sure the anecdote sounded rather silly if you’re unfamiliar with the story I based it off of, but I’m happy with how accurate it was."
    s "I..."

    scene yasublind7
    with dissolve

    s "Yeah...sure."

    "Again, I managed to zone out while talking to Yasu. Though, this time, I’m pretty sure it was entirely out of boredom."
    "I’m not really one for long winded stories, let alone ones that go on to explain whatever weird religious purpose there is for blindfolding herself."
    "It’s probably just safe to assume it has something to do with that prayer she’s always whispering about giving up eyes."

    ya "Wonderful. "
    ya "If I were allowed to have fun tonight, I would jump for joy."
    ya "But unfortunately, I have to be available for God until he’s able to function on his own again."
    s "What do you mean, “function on his own?”"
    ya "He doesn’t handle the cold very well. It makes his legs lock up and his teeth chatter."
    ya "So I allow him to see through me when he wants to."
    ya "I do wish he’d call on me more often, though."
    ya "But I suppose that without many happy memories, there is only so much he can gain from peering into my looking glass."
    s "…"
    s "I feel like I should ask you to embellish on that “lack of happy memories” thing. That sounds important."
    ya "What is important right now is devoting myself entirely to Him."
    ya "This is His night. And all stories regarding Yasu Yasui must be shelved until that subsides."
    ya "Perhaps ask me again when the heat returns and I am free to switch colors."
    ya "But, until then-"
    s "May the path be a path or whatever. Yeah."
    ya "May the path you walk be free of callousness."
    ya "Thank you for visiting tonight."
    ya "I’m sorry I could not be as “entertaining” as I normally am."
    ya "But I need to focus or He will get angry."
    ya "And things get very loud when He is angry."
    s "Right..."
    s "Well, uhh..."
    s "Goodnight then."
    ya "Goodnight."
    ya "Safe travels."
    ya "Remember to sleep facing up tonight."

    scene black
    with dissolve2

    "I make my way out of the church and back into the street."
    "I walk by a local restaurant and move through the steam leaking out of its exhaust pipe."
    "I feel nothing."

    $ renpy.end_replay()
    $ church10 = True
    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label church15:
...
```

## Code that triggers this event
File: \game\YasuEvents.rpy
Code:
```python
...
label church:
    if yasu_love >= 0 and ramen20 == True and church1 == False:
        jump church1
    if yasu_love >= 5 and church1 == True and church5 == False:
        jump church5
    if yasu_love >= 10 and yasudorm10 == True and day == 7 and church10 == False:
        jump church10
...
```