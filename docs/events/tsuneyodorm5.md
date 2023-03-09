# Drug Use & Jump-Rope
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyodorm5&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 5

✅Event "[Tsuneyo: Snake Venom](./ramen1.md)" is completed (event=ramen1)

✅Event "[Tsuneyo: The Life of a Blue Whale](./tsuneyofirsthall.md)" is completed (event=tsuneyofirsthall)



## Next events
* [Tsuneyo: A Short List](./ramen10.md)
* [Tsuneyo: The Man Who Loves Nothing](./tsuneyodorm10.md)

## Event properties
* ID: tsuneyodorm5
* Group: Tsuneyo
* Triggered by label: tsuneyodorm
* Triggered by branch label: tsuneyodorm

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyodorm5:
    play sound "knock.mp3"

    "I knock on Tsuneyo’s door and wait to see if she’s around."
    "I doubt that there has ever been another male to visit her at home, so it’s not like I’m going to hold it against her if she doesn’t feel comfortable letting me in."
    "She might be aloof and...strange, but it’s not like she lacks common sense."
    "I think."
    "Who really knows, though?"

    t "Who is it?"
    s "Your teacher."
    t "Oh. Hello."
    t "Business hours don’t start for another thirty minutes."
    s "So you’ll let me in if I wait out here for thirty minutes?"
    t "Yes."
    s "Wait, what kind of business are you even running in there?"
    t "Ramen."
    s "You run a ramen shop out of your dorm as well?"
    t "Dorm?"
    t "Ah-"

    "It is just then that Tsuneyo seems to realize something."

    stop music fadeout 10.0

    t "I’m sorry. I’m still not used to living here."
    s "How did you confuse a dorm room for a noodle house?"
    t "Every house is a noodle house if you try hard and believe in yourself."
    s "…"
    t "…"
    t "You may enter."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Tsuneyo pulls the door open from the inside and I wander into the room, nodding at her as I do so."

    scene tsuneyofirstdorm1
    with dissolve
    play music "oldweather.mp3"

    if mollydorm5 == False:
        "The place is...more or less what I expect it to be. Filled with various [teenage]girl things and..."
        "And a giant portrait of Tsuneyo’s favorite food."

    else:
        "It feels a little different being in here to see Tsuneyo instead of Molly. "
        "And that’s not saying I don’t like her or anything. I obviously do since I came to visit her. She’s just...you know."
        "But at least this finally gives me a chance to ask about the giant portrait of ramen on the wall."

    scene tsuneyofirstdorm2
    with dissolve

    t "I apologize for forgetting where I was. That happens sometimes."
    s "That’s not a good thing to happen on a persistent basis."
    t "There are worse habits."
    t "Like drug use. Or jump-rope."
    s "I’m struggling to see how exactly jump-rope is a bad habit...but you do you, Tsuneyo..."
    t "Then you have not jumped enough ropes in your life."
    s "I suppose I have not."
    t "Would you like a tour of the room? There are no ropes involved."
    s "None? Damn. There go my plans."
    t "I do not understand."
    s "Figures. You can show me around if you’d like. I can't imagine it will take very long."
    t "I understand."
    t "Please follow me."

    scene tsuneyofirstdorm3
    with fade

    "Tsuneyo leads me over to her bed and immediately begins the “tour.”"

    t "This is where I sleep. "
    t "You will notice several llamas on the shelf above my bed."
    t "There is a simple reason for this."
    s "Is the reason that you like llamas?"
    t "Correct."
    s "Who could have possibly seen that coming?"
    t "Your sarcasm irritates me."
    s "You’ll get used to it."
    t "I hope not."

    scene tsuneyofirstdorm4
    with dissolve

    t "To the right of the llamas, you may have noticed a large bowl of ramen."
    t "This is because-"
    s "You like ramen?"

    scene tsuneyofirstdorm3
    with dissolve

    t "You are ruining the tour."
    s "Sorry. Even with your love for noodles, though, I'm surprised that portrait is...as big as it is."
    s "It’s probably even more eye-catching than all of Molly's figures and some of them aren't even fully clothed."
    t "Thanks, bro."

    scene tsuneyofirstdorm4
    with dissolve

    t "The most interesting part of this particular bowl of ramen is that it was not made by me."
    s "Who was it made by, then?"
    t "I do not know. It simply arrived here one day and I did what any rational woman would do and hung it up directly beside my bed."
    s "Yup. Seems rational enough."

    scene tsuneyofirstdorm3
    with dissolve

    t "I have never lived with another [teenage]girl before, but I understand that we are supposed to cover the wall in things we like."
    t "And I could not get actual noodles to hang properly."
    s "..."
    t "..."
    s "Please tell me that was a joke."
    t "That was a joke."

    "Hey, I finally caught one. Maybe I’m beginning to understand Tsuneyo after all?"

    s "Here’s the thing, though, Tsuneyo."

    scene tsuneyofirstdorm5
    with dissolve

    t "Ah-"
    s "Normally, [teenage]girls will hang up posters of...their favorite bands or TV shows. Or in Molly’s case, a bunch of weird stuff."
    t "Is liking noodles strange?"
    s "Liking them as much as {i}you{/i} do is strange. It’s time to develop new hobbies."
    t "Hobbies?"
    s "Yeah. Like, didn’t you say you did Kendo when you were younger? How about hanging up...Kendo stuff?"

    scene tsuneyofirstdorm3
    with dissolve

    t "Oh. Please allow me to use that topic for what people in show business call a “segue.”"
    t "Follow me, please."

    scene tsuneyofirstdorm6
    with fade

    "Tsuneyo quickly moves past me before turning around and mirroring her pose from the first section of the tour."

    t "Welcome to the more interesting side of Tsuneyo Tojo."
    s "I don’t think stacking a few bamboo swords in the corner really qualifies as interesting. It's barely even a hobby if you don't use them."
    t "Would you prefer I attacked you with them?"
    s "That was a joke too, right?"
    t "..."
    s "..."

    scene tsuneyofirstdorm7
    with dissolve

    t "...Yes."
    s "The hesitation right there did not make me feel comfortable."

    "If Tsuneyo actually {i}did{/i} attack me, it’s not like I wouldn’t be able to defend myself, right?"
    "I mean, she can’t be that good at Kendo, can she?"

    s "I would have liked watching you do all that sword stuff whenever you were into that, Tsuneyo."

    scene tsuneyofirstdorm6
    with dissolve

    t "Really? Why?"
    s "I don’t know. Just feel like it would be kind of cool to see you...actually doing something."
    s "I doubt it was anything intense, but still-"
    t "I was the national junior Kendo champion three years in a row."
    t "It was the only thing I ever left home for."
    s "Wait...national? As in the entire nation?"

    scene tsuneyofirstdorm7
    with dissolve

    t "Does that word have another meaning I am unaware of?"
    s "…"
    s "If...you won the national championship three years in a row, why did you stop?"

    scene tsuneyofirstdorm6
    with dissolve

    t "To take care of my father and carry on the family’s legacy."
    s "The noodle legacy?"
    t "The noodle legacy."
    s "You gave up an amazing talent for that?"
    t "There is no talent more amazing than making soup."
    t "Not having to train gives me more free time, though. I can do anything I want now."
    t "I am essentially a soup god."
    s "Weren’t we literally just talking about how you need hobbies apart from your job, though?"
    t "That was a topic you brought up without my participation. Do not lump me in with the likes of you, damn it."

    scene tsuneyofirstdorm8
    with dissolve

    t "Now that I am a normal [high_school] girl, I am free to make my own decisions and choose my own hobbies."
    t "Thankfully, the Emerald Guardian has recently informed me of a wonderful sounding game where you can kill people and not be prosecuted for it."
    t "This is the path that I will walk congruently alongside noodles."
    s "What, like a...video game or something?"
    t "There is no video involved. It is called Dungeons & Dragons."
    t "She says she is going to teach me."
    t "If that goes well, I may replace my ramen portrait with a creature that I have always known is fake. The dragon."
    s "Don’t try and trick me into forgetting what you said at the ramen shop, Tsuneyo."

    scene tsuneyofirstdorm9
    with dissolve

    t "Ah-"
    s "Still, though...it’s good that you and Molly seem to be getting along."
    s "You’re kind of polar opposites, so I wasn’t sure how that would work out."
    t "I imagine it is due to my lack of personality."
    s "Hey now, there’s no need to put yourself down about it."
    s "What you lack in personality, you make up for in the desire to improve."
    t "…"
    s "…"

    scene tsuneyofirstdorm10
    with dissolve

    t "…"

    "Well, looks like her little put-down right there was supposed to be a joke as well."
    "But hey, least I was able to catch one today."

    t "The Emerald Guardian was right..."
    t "I am a “normie” after all."
    s "A what?"
    t "It means normal person. I think."
    t "I was under the impression being normal was the right thing to do, but she makes it sound like I am evil."
    t "Perhaps it is time for me to move back home. I am not prepared for this world."
    s "You can’t move out yet. What will happen to Noodles?"
    t "That’s exactly why I have to go home. The noodles need me."
    s "No, no. I mean Noodles the bird. The one that we named."

    scene tsuneyofirstdorm11
    with dissolve

    t "Oh! {i}Noodles!{/i}"
    t "Yes. Noodles would be quite lonely without me. "
    t "Your [niece] with the soft legs keeps trying to “rescue” him, but I wish she would stop."
    t "He is well-fed. I have been making sure of it."
    s "Well, at least I don’t need to take a guess about what you’re feeding him."
    t "That’s right."
    s "Can birds really survive off of just n-"
    t "Bird seed."
    s "…"
    t "My father taught me about the right things to feed birds when I was still a little girl."

    "That's...actually kind of cute."
    "I guess Tsuneyo’s relationship with her father is one of those more loving and sentimental ones?"
    "Is she really okay spending so much time here when he’s so sick?"

    scene tsuneyofirstdorm12
    with dissolve

    t "I remember it vividly."
    t "We would wake up early every morning and head to the backyard to feed the chickens."
    t "It was almost as if they were part of the family."
    t "And then, once they were fully grown, we would snap their necks and pluck their bodies clean of feathers for use in our food."

    "Okay, never mind. I’m sure her father will be fine alone."

    s "You...were trained to kill chickens as a little girl?"

    scene tsuneyofirstdorm13
    with dissolve

    t "I was trained to kill many things as a little girl."
    t "My father is incredibly protective."
    t "If he knew I was alone in a room with a man, he would have you executed."
    s "…"
    t "…"
    s "You’re not going to tell him about this, are you?"
    t "I am."
    s "But...you just said that he’d have me executed."
    t "Yes."
    s "Are you...trying to have me killed?"
    t "..."
    s "Tsuneyo."

    scene tsuneyofirstdorm9
    with dissolve

    t "Ah-"
    s "I’m not ready to die yet. You can’t tell your father about this."

    scene tsuneyofirstdorm13
    with dissolve

    t "That would be breaking the rules, though."
    s "It’s okay to break rules every once in a while."
    t "But if I break the rules, all of my teeth will turn to liquid."
    s "What the fuck has your father been teaching you?"
    t "That my teeth will turn to liquid if I break the rules. Please pay attention."
    s "Just...please don’t tell him. Okay? I promise to keep spending money at the restaurant as long as he doesn’t know that I visit you here."
    t "How much money?"
    s "Does it matter?"
    t "Yes."
    s "This is starting to sound like extortion. "
    t "It is, more or less."
    s "I’ll spend...a good amount of money. I promise."
    t "…"
    s "…"
    t "Fine."
    t "But I am not doing it for you. "
    t "I’m doing it for Noodles."

    scene tsuneyofirstdorm14
    with dissolve

    t "You participated in naming him, so I don’t think he’d be happy if you were to suddenly vanish."
    s "I think it’s safe to say there would be a lot of unhappy people if I were to suddenly vanish."

    scene tsuneyofirstdorm13
    with dissolve

    t "I wouldn’t mind."
    s "Thanks, Tsuneyo."
    t "You’re welcome."

    scene black
    with dissolve2

    "I decide against asking her if that last one was a joke or not since I’m mildly afraid of the answer I’d receive."
    "But, at the end of the day, I was able to spend some more time alone with her."
    "And even if she threatened to kill me and admitted to murdering animals, I feel like the two of us managed to grow closer..."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm5 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label tsuneyodorm10:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyodorm:
    if tsuneyo_love >= 5 and ramen1 == True and tsuneyofirsthall == True and tsuneyodorm5 == False:
        jump tsuneyodorm5
...
```