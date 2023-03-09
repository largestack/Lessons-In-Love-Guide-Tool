# Snake Venom
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen1&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 0

✅Event "[Main: Lifting the Curse](./day154.md)" is completed (event=day154)



## Next events
* [Main: What's Done is Done](./beachvacation1.md)
* [Yumi: Token Tsundere](./streets20.md)
* [Tsuneyo: Between the Slurps of Pork Broth](./ramen5.md)
* [Tsuneyo: Drug Use & Jump-Rope](./tsuneyodorm5.md)

## Event properties
* ID: ramen1
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop

## Event code
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramen1:
    scene firsttsuneyoramen0
    with dissolve
    play music "kashiwagi.mp3"

    "I show up at a seedy ramen shop in the second half of town."
    "A noodle-sanctuary in a land of shit."
    "Or as Tsuneyo calls it, home."
    "The walls are stone and stained with years worth of pork broth condensation, turning what I’m sure was a once-spotless restaurant into..."
    "Well, into this."
    "But this is the ideal place for a dish like ramen."
    "It’s not meant to be fancy. It’s not meant to be {i}gourmet.{/i}"
    "It’s just food that warms the heart."
    "Or at least what’s left of it."

    scene firsttsuneyoramen1
    with dissolve

    t "Good evening. Welcome to Tojo Ramen."
    t "Please take your time looking over the menu and let me know if you have any questions."
    s "…"
    s "Tsuneyo."

    scene firsttsuneyoramen2
    with dissolve

    t "Ah-"
    s "You do realize it’s me, right? Your teacher?"
    s "You don’t have to give me the same customary greeting that you give everyone else."
    t "There is no customary greeting. Everyone else just sits down."
    t "I have decided to greet you as today is a day to celebrate."
    s "To celebrate {i}what{/i} exactly?"
    t "A curse free life."
    s "You’re still going on about the curse?"
    t "I am. The Emerald Guardian informed me that it was not a curse after all. Who knew?"
    s "I did. I literally told you."
    t "I don't remember that."
    s "Well, it happened."
    t "I apologize. I often find myself having a hard time paying attention while you're talking."
    t "But you are alive. And that is all that truly matters."
    s "I'm offended by the first part of that statement, but applaud you for ending on an insightful note."

    scene firsttsuneyoramen3
    with dissolve

    t "I am full of nothing but wisdom and noodles."

    "Tsuneyo passes me a menu after having just fulfilled her noodle-mention-quota for the night."
    "I take a moment to look it over and realize that everything on the menu is insanely cheap."
    "It didn’t occur to me the first time I came here since I...wound up paying for two people, but I’m surprised Tsuneyo’s family is even able to stay in business with prices like these."
    "I feel like they haven't been updated in decades."

    s "Hey, Tsuneyo."

    scene firsttsuneyoramen2
    with dissolve

    t "Ah-"
    s "Why is everything so cheap here?"

    scene firsttsuneyoramen1
    with dissolve

    t "Cheap?"
    s "Yeah. You’re charging next to nothing for virtually every dish on the menu."
    t "Oh. You mean {i}cheap.{/i}"
    s "...That’s exactly what I said?"

    scene firsttsuneyoramen4
    with dissolve

    t "I suppose it may have something to do with the people who live in this half of town."
    t "I’m sure you have noticed, but the old district is not in the best of shape."
    t "The most populous demographic in the area is the elderly. And next is the poor."
    t "Everyone else lives much further away."

    scene firsttsuneyoramen1
    with dissolve

    t "All of the people stuck here are simply waiting to die."
    s "That’s...dark."

    scene firsttsuneyoramen3
    with dissolve

    t "Yes. I suppose it is."
    s "…"
    t "…"

    scene firsttsuneyoramen1
    with dissolve

    t "Do you know what you’d like to order?"

    "What kind of mood whiplash is this? Jumping straight from condemning the entire population here to taking my order?"
    "I know Tsuneyo doesn't have much experience holding conversations, but...she at least has to learn how to transition between topics."

    s "Uhh...can you tell me what the “Red Dragon” is?"
    t "It is the red version of the Green Dragon."
    s "So it’s...spicier, I’m guessing?"
    t "Yes. Just like in ancient times."
    t "The red dragons were much more dangerous than the green ones."
    s "But dragons didn’t actually exist in ancient times. Those were just fairy tales."
    t "…"
    s "…"

    scene firsttsuneyoramen5
    with dissolve

    t "…"
    s "Did you...really not know that?"
    t "This is a shocking revelation."
    t "All this time, I have been explaining the difference between the dishes by mentioning the dragons of ancient times."
    t "Why did no one stop me?"
    s "Well, you deal with mostly old people, right? They probably thought it was cute that you still believed in them."
    t "Are old people actually evil?"
    s "A lot of the time, yeah."

    scene firsttsuneyoramen6
    with dissolve

    t "I must remain vigilant in the face of the elderly. They could attack at any moment."
    s "It's fine. They'll die before the rest of us, so you likely won't have to remain vigilant for very long."

    scene firsttsuneyoramen1
    with dissolve

    t "I look forward to that day with great anticipation. Praise be."
    s "Praise be."
    s "Wait, what are we praising?"
    t "Noodles, perhaps?"
    s "Well...anyway, I guess I’ll have the Green Dragon since it's...less red than the Red Dragon."
    t "I understand."
    t "One Green Dragon, coming up."
    t "As a word of advice, dragons are not real. The dish is based on a fictional creature from fairy tales."
    s "Yes, Tsuneyo. I am the one who taught you this."
    t "You are lying. This is information I have known all along."
    t "Now, please excuse me while I go craft a dish named after a fictional creature that did not actually exist in ancient times."

    scene firsttsuneyoramen0
    with dissolve

    "Tsuneyo disappears behind the curtain leading to the kitchen and I can hear her beginning to search through some shelves or cabinets or something."
    "I wonder why she’d need to go back there when it looks like all of the ingredients are right behind her?"
    "Maybe the Green Dragon requires some sort of...{i}special{/i} ingredients they store in the back?"
    "Oh well. Not like it matters anyway. I’m just glad to be able to eat something."
    "Coming to this part of town is always draining, both physically and mentally- and I'm barely able to stay awake as-is."

    scene firsttsuneyoramen1
    with dissolve

    t "I have returned."
    s "Oh, good timing."
    t "This ain’t my first rodeo, bro."
    s "Still at it with the whole informal speech thing?"
    t "Am I improving?"
    s "You're getting worse, actually. That was extremely unnatural."

    scene firsttsuneyoramen6
    with dissolve

    t "Ugh..."
    s "It’s fine. I’m already teaching one girl how to improve her public speaking and, weirdly enough, you seem much more open to learning."

    scene firsttsuneyoramen7
    with dissolve

    t "You offer additional classes?"
    s "Well...not {i}exactly.{/i} I kind of just show up to her work every once in a while and...accidentally insult her until she improves."
    t "Did you come here to insult me?"
    t "On my home turf?"
    t "Watch your step, bro."
    s "Tsuneyo, you can’t just keep adding bro to sentences to make them informal. That isn’t how it works."
    t "Are you sure? Because I have studied our Yakuza clientele and have heard them use that word many times before."
    s "Why in the world are the Yakuza coming to a ramen shop in the middle of the old district?"

    scene firsttsuneyoramen8
    with dissolve

    t "Because I am a food magician. "
    t "My flavors are unparalleled in the world of ramen."
    t "They also occasionally used the back room to do business before my father fell ill."
    s "What kind of business were they doing back there exactly?..."
    t "Apparently, they work in real estate."
    t "And all this time, I thought they were some sort of gang."
    t "If more people knew their true goal was to provide affordable housing, I believe less people would fear them."
    s "…"
    t "…"
    s "You're not serious, are you?"

    scene firsttsuneyoramen9
    with dissolve

    t "Huh?"
    t "What did I do now?..."
    s "Nothing, Tsuneyo. I can’t teach you two valuable life lessons in one day."
    t "Why is talking to you so much harder than it is talking to anyone else?"
    s "Who knows? Even I don’t understand my actions sometimes."
    s "It’s like, I’ll just be walking around, minding my own business...and suddenly, I’m sitting in a ramen shop teaching some girl about dragons."

    scene firsttsuneyoramen1
    with dissolve

    t "That sounds extremely similar to what happened here today."
    s "It {i}is{/i} what happened here today."
    t "Oh. Right. Of course."
    t "…"
    t "Perhaps it was hunger that landed you here? That would make sense, would it not?"
    s "It would, but I don't think that's something you need to verbally rationalize."
    t "Would you prefer to eat in silence?"
    s "I don’t even have any food yet."
    t "It’s cooking."
    t "The Green Dragon requires special preparation."
    s "What kind of special preparation? I don't even know what I-"
    t "Snake venom."
    s "…"
    t "…"

    "Don’t tell me that’s what she was doing when she went into the kitchen?"

    s "On second thought, I don’t know if I want the Green-"
    t "It was a joke."
    s "…"
    t "Surprise."
    s "You really need to work on your delivery."
    s "Everything you say comes out in the same tone, so I can never tell when you’re kidding or not."
    t "Do you really think we would use snake venom in ramen?"
    t "That is absurd."
    t "It would never work."
    t "..."

    scene firsttsuneyoramen10
    with dissolve

    t "Unless..."
    s "Unless what? What are you thinking right now?"
    t "Tell me- how much do you cherish your life?"
    s "Enough to not agree to whatever you want me to agree with. "
    t "That is a shame. I had an excellent idea for a new menu item."
    s "How is it excellent if you don’t even know it’s safe to consume?"
    t "With great risk comes great reward. Thomas Jefferson said that."
    s "Thomas who?"

    scene firsttsuneyoramen11
    with dissolve

    t "Is he a mythical creature as well?!"
    s "No, I just wanted to see how you'd react if I pretended he was."

    scene firsttsuneyoramen12
    with dissolve

    t "That’s a relief. I was beginning to think everything I was taught had been a lie."
    t "Life was much simpler before I had to begin using my knowledge in real life."
    s "Yeah. I can see how homeschooling might leave some people behind."

    scene firsttsuneyoramen1
    with dissolve

    t "I will do my best to learn the right meanings to things in your class."
    s "Just...try and have fun. Knowledge comes second."
    t "I understand. I will do my best to prioritize having fun over improving myself as a person."
    s "There you go. Just don’t expect too much from me and I'm sure you'll have a decently fulfilling school life."
    t "My expectations could not be any lower."
    s "Well, that's kind of insulting."
    t "Another joke. Ha ha ha ha ha."
    s "The {i}real{/i} joke here is your sense of humor."
    t "…"
    s "…"
    t "…"
    s "…"
    t "Wow. You’re even worse than I am."
    s "That was not my proudest moment just now."
    t "You should be ashamed."
    s "I am. You don't have to-"
    t "Get out of my restaurant, you bastard."
    s "…"
    t "…"
    s "That was a joke too, right?"
    t "…"

    scene firsttsuneyoramen8
    with dissolve

    t "I’ll be right back."

    scene black
    with dissolve2

    "Tsuneyo disappears behind the curtain yet again and retrieves a large green bowl filled with assorted toppings."
    "She ladles the broth from behind her into it and places the dish in front of me."
    "After combing through it with my chopsticks to confirm that there are no traces of snake parts or any other strange ingredients, I dig in."
    "………"
    "It’s heavenly."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ ramen1 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen5:
...
```

## Code that triggers this event
File: \game\TsuneyoEvents.rpy
Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
...
```