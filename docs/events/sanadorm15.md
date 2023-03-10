# Shaking The Tree (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 15



## Next events

* [Ayane: Still Young](./ayanedorm20.md)

## Event properties

* Id: sanadorm15
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm
* Triggered by path: sanadorm->sanadorm15

## Official wiki page

[Shaking The Tree](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm15&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm15:
    play sound "knock.mp3"

    s "Hey, Sana. Are you in there?"
    sa "Is...Is that you, Sensei?..."
    sa "Do you...need something?..."

    "Sana decides to call out from behind the door instead of timidly walking up and whispering through it this time."
    "My mission to teach her public speaking is now complete and I have officially done all I can possibly do for this girl."

    stop music fadeout 5.0

    s "I was wondering if you wanted to hang out."
    sa "Um...I can't..."
    s "Why not?"
    sa "Um...because...I’m..."
    sa "Because I'm...in my pajamas..."
    s "..."
    sa "..."
    s "That's it? That's your reason?"
    sa "...Huh?"
    s "What, are you embarrassed to be seen that way or something? Because I really don't care."
    sa "I...uhh...maybe...a little bit?..."
    sa "But I...feel bad since you came all this way, so...I guess you can still come in..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I figure that the only reason Sana would be embarrassed to be seen in her pajamas is that they might reveal a bit more skin than normal-"

    scene games1
    with dissolve2
    play music "love.mp3" fadein 3.0

    "But my theory falls flatter than, well...Sana. Because she's even more covered up than normal."

    sa "Um...h...hi..."

    "And also too cute to be an actual human being."
    "Since when am I attracted to girls wearing sweaters that weigh probably more than they do?"

    scene games2
    with dissolve

    sa "Umm...Sensei?...Are you okay?..."
    sa "Why are you just...looking at me like that?..."
    s "Sorry. I zoned out for a second as I came to terms with a new aspect of myself."

    scene games3
    with dissolve

    sa "I..umm...okay?..."
    sa "I don't really know what that means, but...I'm happy if that...makes you happy..."
    s "Just out of curiosity, aren't you a little warm? It’s summer and you’re in a hoodie meant for someone my size."
    sa "I...like to keep the air on really high, so...I don’t mind..."
    sa "I kind of like...being bundled up like this..."

    "Now that she mentions it, it {i}is{/i} borderline freezing in here. I’m actually kind of regretting not wearing a hoodie myself, but I honestly don't even think I own one."

    s "So, what were you up to before I showed up and ruined your night? Studying?"

    scene games1
    with dissolve

    sa "I don't...really like studying..."
    sa "I was just...playing games and stuff..."
    s "First, can you confirm that I'm not actually ruining your night? Because I kind of expected you to deny that and you just completely ignored it."
    sa "You...didn't ruin my night, Sensei..."
    s "Thank you. So, what game are you playing?"
    sa "Um...it's...a game called Animal Crossing..."
    sa "You kind of just...build a village and run around it doing...village stuff..."
    sa "But it’s...really fun and you can...easily lose track of time while playing it..."
    s "Can't say I’ve ever heard of it. "
    sa "You...can watch if you want?"
    sa "Which...actually doesn't sound very fun, so...I'm sorry for suggesting it..."
    s "It sounds better than doing nothing, so sure. I'm in."

    scene games3
    with dissolve

    sa "You’re...okay with just watching?..."
    sa "Because I...have games we could play together instead..."
    sa "I just...have to sell my turnips first..."
    s "I really don’t mind, Sana. You looked happy when you were talking about the animal game or whatever, so I'd like to check that out if you're still okay with it."

    scene games1
    with dissolve

    sa "Oh...yeah. Of course I'm...okay with it..."
    sa "I'll even let you...choose what outfit I wear..."

    "God, I wish that sentence meant what I wanted it to mean."
    "Perversions aside, though, do people really have fun playing a game where you just...manage a village and...sell turnips?"

    scene games5
    with fade

    "Sana walks over to the bed and grabs a handheld console off of her end table. I follow suit and take a seat next to her."
    "Surprisingly, she actually moves closer to me once I sit down."
    "I'm sure it's just to give me a better view of the game, but I like to think it's because she's starting to feel more comfortable around me for reasons beyond my comprehension."

    sa "Okay, so..."
    sa "I guess I...can just show you around the town first..."
    s "You built all of that?"
    sa "Well, there are some things already built when you first get here...but I did organize most of it, yeah..."
    sa "It took...way longer than I'd like to admit, though..."
    s "I see. And what’s that building there?"

    scene games6
    with dissolve

    sa "That’s the museum. It’s where you put bones and stuff."
    s "This game is much more violent than it looks."
    sa "Not...human bones, Sensei...Ones you find in the ground..."
    s "I think you should relocate your village to somewhere with a brighter history."
    sa "Heheh...I guess I...should have just called them fossils..."
    sa "But, umm...you can also put stuff like...fish and bugs into the museum as well..."
    sa "It's like a...big building for all of the stuff you can collect..."
    s "And all of this is just laying around outside?"

    scene games5
    with dissolve

    sa "Well...there's some searching involved, but...yeah. Kind of..."
    s "And who’s that guy over there? What does he do?"

    scene games6
    with dissolve

    sa "That’s one of the villagers. He just...walks around all day."
    s "What a life."

    "I say, momentarily forgetting that that's essentially all I do as well."

    sa "Oh! I should show you my house too. I...I worked really hard on it, so..."
    sa "So...don't say anything mean about it, please..."

    "It's nice hearing how excited Sana gets when she’s talking about all of this stuff."
    "It's the first time I've ever really seen her in {i}her element{/i} and, despite the fact that I'd never use my free time on something like this, I'm glad she's found something she enjoys."
    "I don't want to say it makes me {i}happy{/i} or anything like that, but it does make me feel like the two of us are getting a little closer."
    "It's just odd knowing that the deciding factor in making me think that is her showing me her bug collection in a virtual museum."

    s "So, is there like, an objective to this game?"

    scene games5
    with dissolve

    sa "Mmm...not really. But also...kind of?..."
    sa "Since other people can visit your island...there’s always a lot of pressure to have it look as nice as possible..."

    scene games7
    with dissolve

    sa "Oh! Look...There’s someone here now."
    s "That’s a person you know in real life?"
    sa "It’s someone...you know in real life as well..."
    s "That...does not look like anyone I know in real life."

    scene games8
    with dissolve

    sa "Would you...be surprised if I told you it was Ami?..."
    s "Ami plays this game too? I had no idea."
    sa "She probably...plays in her room when you’re not looking..."
    sa "You two...spend a lot of time together...don't you?"
    s "More than anyone else, I guess. But she also sleeps in the same building as me, so it's a bit of an unfair advantage."
    s "That's interesting, though. I didn’t realize you two were close enough to be playing games together."

    scene games5
    with dissolve

    sa "You see...that’s...what I like about games..."
    sa "You don’t really need to be close with someone to play with them..."
    sa "Take Ami for example..."
    sa "She’s not here because she likes me..."
    sa "She’s here because she needs oranges."
    s "I’m sure that’s not-"
    s "Oh. She's shaking an orange tree."
    sa "Heheh...see? I told you..."
    s "That doesn't mean she doesn't like you, though, Sana. It-"
    sa "Sensei...it's okay. Liking each other doesn't really matter in places like this..."
    sa "And I'm not even upset that she's taking my resources...because I can always go to her island and take hers as well..."
    s "So it’s like an entire world where people just...take stuff from each other?"

    scene games6
    with dissolve

    sa "It’s a world where everyone shares...and helps each other out..."

    scene games5
    with dissolve

    sa "It’s much better than this world...and that’s why I spend so much time here..."
    sa "I actually..."
    sa "I actually get to feel included."
    s "…"

    "It’s kind of confusing hearing her say something so lonely in such an uplifting way."
    "But, as I learn more about Sana, I’m starting to realize that’s just the sort of person she is."
    "A person who would rather shrug off the things that make her sad than directly confront and overcome them."
    "It’s a great quality to have, don't get me wrong-"
    "But it can also dramatically backfire."
    "I'm sure that's just me thinking too much about too little, though."

    sa "Oh, right! You still haven't picked my outfit."
    sa "Now...let's see what there is to choose from..."

    scene black
    with dissolve2

    "Sana goes on to play her game for another hour or two, showing me essentially everything there is to know about it."
    "And while I have no intention of actually purchasing it, I fully believe that I could now survive in the world where everyone shares."
    "The world where everything that's taken can be immediately replaced."
    "Where everyone gets along and everyone feels included."
    "The exact opposite of the place we fall asleep at night."

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm15 = True
    stop music fadeout 3.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
...
```