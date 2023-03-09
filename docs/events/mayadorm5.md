# Secrets Worth Keeping
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm5&go=Go)



## Event preconditions
✅Maya love greater than or equal to 5

✅Day of week is not Friday

✅Event "[Ami: Home Away From Home](./amidorm5.md)" is completed (event=amidorm5)



## Next events
* [Ami: Back Out in the Heat](./amidorm15.md)
* [Maya: Rewind/Repeat/Refuse](./mayadorm10.md)

## Event properties
* ID: mayadorm5
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label mayadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on the door and wait for Maya to answer."
    "Chances are she won’t respond if she knows it’s me, so I decide to keep quiet instead."
    "A few seconds go by and no one comes to the door, but I can clearly hear movement on the other side...so, chances are that I'm just being ignored."
    "That's fine, though. Because I have learned by now that repeatedly annoying Maya almost always gets her to respond to me."
    "That said, all I have to do is keep knocking."

    play sound "knock.mp3"

    s "..."
    m "Hah..."
    m "Who is it?"
    s "..."

    play sound "knock.mp3"

    "I knock again, still not wanting to reveal my presence even though the chance of Maya realizing it's me is already quite high."

    m "Ugh...hold on."

    "I manage to win in the end. Persistence really is key with girls like her."

    scene firstmayadorm1
    with fade
    play sound "dooropen.mp3"

    m "Wow. Who could have ever predicted that it was you knocking and not some other random person who didn't want to reveal their voice?"
    s "You're so smart, Maya."
    s "Are you not hanging out with Ami tonight?"
    m "Ami isn’t home tonight. And I have other things I need to be taking care of anyway."
    s "Does this mean we can't hang out?"
    m "..."
    s "..."

    scene firstmayadorm2
    with dissolve

    m "Are you out of your mind?"
    m "How many more times must I tell you to leave me alone before you actually...you know, start doing that?"
    s "I’ve already decided that I'm going to just perpetually bother you, so you may as well just quit while you're ahead and stop asking me to leave you alone."
    m "Can you at least make yourself useful and hold this? It's heavy."
    s "Oh, yeah. Sure."

    scene firstmayadorm3
    with dissolve

    "Maya hands the box over to me and it is way heavier than I expect it to be. I guess this is what I get for annoying her, though."

    s "What's in here? Can I open it?"
    m "Are you suddenly illiterate? It says ‘don’t open’ right there on the box."
    s "I'm not illiterate. I just thought I might be an exception to that rule."

    scene firstmayadorm4
    with dissolve

    m "Why on earth would {i}you{/i} of all people be an exception to that rule when I like you less than literally everyone else?..."
    s "I don't know. Just a feeling I had."
    m "I won’t even let you into the room and you think I’m going to let you look at my personal belongings?"
    m "What's next? Leisurely walks through the park and long talks about our future?"
    s "Sure. That sounds fun."
    m "Die."
    s "Chill out. I'm not going to look inside if you really don't want me to."
    s "It just seems really suspicious to write “don’t open” on a box. So it's not my fault for being curious."

    scene firstmayadorm5
    with dissolve

    m "You’re...curious about a lot of things, aren’t you?"
    s "Curiosity is human nature, after all."
    m "I suppose. But what is it that makes {i}you{/i} curious? Are you incapable of assimilating to this new world on your own? Are you looking for guidance?"
    m "Because, as much as you would like me to be your tour guide of {i}all things Kumon-mi{/i}, I believe that role should belong to Ami."
    s "I’m perfectly capable of {i}assimilating.{/i} I just want to put you into a position where you might accidentally reveal your secrets to me."

    scene firstmayadorm5r
    with dissolve

    m "I see."
    m "And what makes you think I have any secrets worth keeping?"
    s "We all have secrets worth keeping, don’t we?"

    scene firstmayadorm3
    with dissolve

    m "..."
    s "...?"
    m "Hm."
    s "What? Did that answer surprise you?"
    m "Perhaps. You sounded almost human for a moment."
    s "Thanks. I think that’s the closest to a compliment that I’ve ever received from you."
    m "Don’t jump for joy just yet, as I still have no intention of telling you anything."
    m "Getting ‘my secrets’ out of me simply won’t happen. I’ve had too much practice keeping them."
    m "In fact, I am so confident in my ability to do so, that I am going as far as letting you handle a very important box right now."
    m "A box that, despite your desire to open it, I know will remain shut."
    s "You {i}know{/i} that?"
    m "Would you like to try and prove me wrong?"

    "Should I open the box?"

    menu:
        "Don’t open the box":
            s "..."
            m "..."

    scene firstmayadorm5r
    with dissolve

    m "See? I know how these things work."
    m "Now, if you’d be so inclined, please help me carry this elsewhere."
    s "Where exactly is ‘elsewhere?’ Because I’m not exactly in the mood to carry this across town this late at night."
    m "Oh? Then I suppose I will venture forth into the dark on my own."
    m "What is the worst thing that could possibly happen to a small, cute girl wandering off alone in the dark?"
    s "Are you...actually trying to convince me to come with you right now?"
    m "I don't have to. I know you are going to come with me regardless of what I say because you are attracted to me."

    if bonus == False:
        s "Nuh-uh."
        m "Shut up. Yes you are."

    m "And I would be foolish to deny you the opportunity to indulge in that attraction of yours as doing so would mean that {i}I{/i} would have to carry this box."
    m "And I just don't want to do that."
    s "…"
    m "…"
    m "Now-"
    m "Please follow me."

    scene black
    with dissolve2
    stop music fadeout 5.0

    "So..."
    "I guess I have to carry a box now?"
    "........."
    "......"
    "..."
    "{i}Several minutes later...{/i}"

    scene secretsredux1
    with dissolve2
    play music "thesleepingcity.mp3"

    s "You’re going to have to tell me where we’re going eventually..."
    m "Sorry, did you say something? I couldn't hear you over your unrelenting desire to sleep with me."
    s "First off, stop using your divine powers to listen to my thoughts."
    s "Second, I asked you to tell me where we're going."
    m "Oh. So you haven't figured it out already?"
    s "Not really. You have to remember that I'm not that familiar with this place yet."
    s "The only thing I know in this direction is the[school]."
    m "Then I suppose that is where we are headed."
    s "Would you mind explaining why we need to carry a box that says ‘don’t open’ on it to the[school] in the middle of the night?"
    m "Would you believe me if I told you that the box was full of explosives and that I plan on demolishing the school tonight?"
    s "Uhh..."
    m "That was obviously a joke."
    s "I wouldn't call it {i}obvious.{/i} In fact, I think your delivery needs a little work."
    m "You’re the one who should be focusing on delivery right now. I’m only here to act as a chaperone."
    s "Was that another joke? Because if so, you are very bad at this."

    scene secretsredux2
    with dissolve

    m "Perhaps it was. Perhaps it wasn’t."
    m "I'm afraid you'll never be close enough to me to understand my sense of humor."

    "Those words carry a bit more weight to them as Maya stays several steps away from me the whole trip."
    "I can feel her glaring back at me from time to time, but whenever I decide to walk a little faster in order to catch up, she does the same."
    "I’m not sure why she’s so opposed to coming any closer, but I chalk it up to the fact that I don't really hide my attraction toward her and that we're all alone in the middle of the night."
    "This exact scenario would excite several other girls I know, I'm sure."
    "But for Maya, it appears to do anything but."

    s "You can walk a little closer to me you know."
    m "And why would I do that?"
    m "It won't change when we arrive at our destination, so the distance between us doesn’t make much of a difference, does it?"
    s "No. But it would help me feel a little less...weird."

    stop music fadeout 10.0

    m "That's nice. But I don't really care about your feelings."
    s "Are you saying that staying this far apart {i}doesn't{/i} make you feel weird?"
    m "Was what I said really that hard to understand?"
    s "No. I just-"
    m "Good. Then there's no need for us to change positions whatsoever."
    m "I’m very glad we were able to resolve this peacefully."

    scene black
    with dissolve2

    "Nothing changes."
    "The two of us just keep walking."
    "........."
    "......"
    "..."

    scene secretsredux3
    with dissolve

    s "Are we almost there? Because my arms are really starting to get tired."
    m "Are they? I remember you being a bit stronger."
    m "What a shame that one of your very few uses isn't even all that useful to begin with."
    s "Well, excuse me for not being used to a new body yet."
    m "No matter. We've just arrived anyway."
    m "May I have the box?"

    scene black
    with dissolve2

    "I hand the box to Maya and take a moment to loosen up my shoulders as they've grown tight from carrying it for...what I'm pretty sure is several miles at this point."
    "Maya takes a quick look at the door in front of us, which is one I've never entered before, before sliding it open with her foot and disappearing inside."

    m "Please wait one moment."
    m "And don't go anywhere."
    s "Why? Will you get scared if I leave you here on your own?"
    m "Not as scared as you would be without me."
    s "Oh? Is that another joke?"

    play sound "slidedoor.mp3"

    m "I wonder."
    "........."
    "......"
    "..."

    play sound "slidedoor.mp3"

    scene secretsredux4
    with dissolve

    m "Okay. I’m done."
    s "Done with what, exactly?"

    scene secretsredux3
    with dissolve

    m "That doesn’t concern you."
    s "I'd say it does after spending my entire night helping you."
    m "Wow. One whole night. You're like a regular messiah or something, aren't you?"
    s "..."

    scene secretsredux4
    with dissolve

    m "Listen...we should probably get going."
    m "{i}You{/i} may be allowed here after dark, but I could get into a lot of trouble if someone sees me."
    s "You realize I'm one of those people who could discipline you for this, right?"
    m "Oh, please. You’re barely even a teacher."
    s "You know...that's kind of fair. Carry on, Maya."
    m "Please stop saying my name. It makes my skin crawl."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene secretsredux5
    with dissolve

    m "…"
    s "…"

    "Things between us have been eerily quiet since we left the[school]."
    "It's not like I expected them {i}not{/i} to be considering that the distance between us feels like it's less {i}distance{/i} and more of just some other plane of existence, but still."
    "I expected there to be more bickering."
    "More insults."
    "More anything."
    "All we have right now is silence, though."
    "Silence and the creeping acceptance that there's a side to this relationship that she'll probably never let me see."

    m "…"
    s "…"

    "I get caught somewhere between the desire to keep looking away and another that would mean forcing everything she knows out of her."
    "How would I do that, you ask?"
    "Ask me again when it isn't dark and I'll consider letting you know."

    m "Hey."
    s "...?"

    "Surprisingly enough, it’s Maya that breaks the silence before I do."

    m "Are you thirsty?"
    s "Uhh...I guess a little bit. I {i}did{/i} just carry some random box halfway across town."
    m "That wasn't anywhere close to halfway across town, but your exhaustion is understandable."
    m "Do you have time for a minor detour?"
    s "A detour? To where?"
    m "Excellent. Please, follow me."

    scene black
    with dissolve2

    s "That...was not an answer to my question."
    m "Perhaps it's best that you get used to me not answering your questions {i}now{/i} if you're going to continue asking them."

    "Maya leads me into an alleyway illuminated by the moonlight and a pair of vending machines."
    "She drops a few coins into one of them and, in what seems like a conditioned reflex, presses a button in the middle row."

    m "Here."

    scene vend1
    with dissolve2
    play music "encounter.mp3"

    s "Thanks..."
    m "You’re welcome."

    "I crack open the can and take a sip."
    "It’s a sort of semi-sweetened iced coffee that causes a wave of nostalgia to sweep over me as I press my back against the cold alley wall."

    s "…"
    m "…"

    "Of course, things are once again awkward between the two of us and I feel a sudden urge to speak out."
    "The weird thing with Maya is that I’m not even sure if I should try breaking the ice in times like these or not."
    "I feel like more than half the time she just tells me to stop talking."

    s "Well...this is new."
    m "Is it?"
    s "Yeah. I mean, it's almost like the two of us are actually hanging out, right?"
    s "It’s much different than helping you carry things or visiting you at the shrine."
    m "We’re not hanging out. I’m just repaying you for helping me."
    s "I know. But it still feels kind of new."
    m "…"
    m "I see."
    s "This drink is really good, by the way. What is it?"
    m "..."
    m "I’m not sure."
    s "Well, thanks again either way. It...it kind of reminds me of something."
    s "I think."
    s "I definitely recognize it from somewhere. I'm just...not really sure where."
    m "Is that so?"
    s "Yeah. Well, probably. I guess."
    s "I can't really say anything with certainty anymore."
    m "This is the only vending machine in town that sells that. So chances are you've just been here before."
    s "Are you some sort of vending machine enthusiast or something?"
    m "Is that even a thing?"
    s "Probably. There are enthusiasts for basically everything in this day and age."
    m "Even teenage girls."
    s "There are probably a lot more of those than you would like to imagine."
    m "I'm aware- as the amount I would like to imagine is zero and I'm currently standing next to at least one."
    s "And you still bought a drink for him? Daring."
    m "Well...even someone like me can take risks every once in a while."

    "The conversation comes to a dead stop once again and the two of us are left in silence."
    "Every few minutes, a car will speed by and the sound of screeching tires will vibrate through the alley, bouncing off of the walls."
    "Those sounds, combined with the incessant humming of this pair of vending machines, creates what feels like an urban symphony."
    "I want to fall asleep to it."
    "Unfortunately...I should probably be getting this girl home before it gets too late."

    s "Did you want to head out now?"
    m "Are you done drinking?"

    scene black
    with dissolve2

    "I take a few more sips from the can and kill it, tossing it into a nearby garbage bin."

    s "Yeah. I'm ready when you are."
    m "I see..."
    m "Then, yes."
    m "I suppose we should be heading back now..."

    "Our return to the dorm doesn’t take too long, especially now that I'm not being held back by a surprisingly heavy cardboard box."
    "When we finally reach the entrance, Maya does not say goodbye. She just nods at me and quickly walks back into the building as if she's already forgotten the lengths I went to for her tonight."
    "I can't say I expected any less, though."
    "I know she doesn’t like being around me. {i}Everyone{/i} knows she doesn't like being around me."
    "So tonight was probably just one more hassle for her...even {i}if{/i} I was helping her out for the majority of it. "

    s "..."

    "Oh well."
    "There's no use thinking any more about it right now."
    "I'll just have to keep bothering her..."
    "Until there's nothing left for her to do but fall for me."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayadorm5 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayadorm10:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
...
```