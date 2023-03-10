# Seeds (Tsuneyo)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Tsuneyo love greater than or equal to 15

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Tsuneyo: Moe Fan Service](./tsuneyodorm15.md)

## Event properties

* Id: ramen15
* Group: Tsuneyo
* Triggered by label: ramenshop
* Triggered by branch label: ramenshop
* Triggered by path: ramenshop->ramen15

## Official wiki page

[Seeds](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ramen15&go=Go) for more details.

## Event code

File: (install folder)\game\TsuneyoEvents.rpy

Code:
```python
...
label ramen15:
    scene ramenfifteen1
    with fade
    play music "kashiwagi.mp3"

    "I arrive at the ramen shop to find a rather...despondent looking Tsuneyo."
    "Or maybe she’s just tired. I don’t know."
    "I can never really tell with her."

    s "Tsuneyo, how are you feeling right now?"
    t "Like the world is crumbling down around me and I am but a lonely sheet of kombu."
    s "Okay, so despondent it is."
    t "I’m so tired."
    s "Or maybe not."
    s "You’re really not helping me out here."

    scene ramenfifteen2
    with dissolve

    t "I’m sorry. "
    t "It was very busy before you showed up."
    t "Thank you for scaring the rest of the customers away. I needed a break."
    s "The store was empty when I arrived, though."
    t "They must have sensed that you were coming."
    t "The Emerald Guardian says you have a holy aura."
    t "There are many people who can probably feel it."
    t "Especially since most people in this area are old and dying."
    t "Why is it that people who are closer to death care more about religion than those who are young?"
    s "Do we need to get into that right now?"
    s "I haven’t even touched my dinner yet."
    t "You haven’t ordered dinner yet."
    s "Oh. I thought that bowl next to you was for me."
    t "That is a strange thing to assume."
    s "Well you kind of just placed it there as soon as I sat down, so I figured you were preemptively getting me something."
    t "Oh. No."
    t "I placed it there for comfort."
    t "There is something soothing about a bowl of miso ramen sitting beside you during casual conversation. Don't you agree?"
    s "No. What? Why?"

    scene ramenfifteen3
    with dissolve

    t "Who knows? Perhaps that’s just the way things are..."
    s "Don’t just look off into the distance like that was some sort of revelatory thing to say."

    scene ramenfifteen4
    with dissolve

    t "Fine. Then I will look directly at you for the rest of the night."
    t "Even when it starts to make me feel sick."

    if bonus == True:
        t "Are you enjoying this, you pervert?"
        s "Yes, Tsuneyo. My biggest fetish is eye contact."
    else:
        t "Are you enjoying this, Father?"
        s "Why did you just call me that?"
        t "Call you what?"
        s "Father."
        t "I did no such thing. You have potatoes in your ears."

    "The sounds of car horns leak under the old metal door of the ramen shop, showing that even places as devoid of life as the old district still have some sense of urgency to them."
    "Inside of Tojo Ramen, however, that never seems to be the case."
    "Well, at least while I’m here."
    "It’s definitely a little suspicious how Tsuneyo claims it was packed just moments before I showed up."

    s "What do you think the reason you were so busy tonight is?"
    s "It seems like just another day to me."
    t "We always get busier in the winter. "
    t "Can you think of anything more relaxing than a bowl of ramen on a cold night?"
    s "See, that makes a lot more sense than leeching comfort off of just having one next to you. "
    s "It’s just weird that I never see anyone here."
    t "You’re a liar."
    t "You purchased dinner for the intimidating blonde woman once."
    t "And then there was that horrible girl with the black and white stripes."
    s "How is Kaori horrible? She just wanted a job."
    s "If anything, you’re horrible for being the only roadblock between her and her mission to work at every single restaurant in Kumon-mi."
    t "Tsuneyo Tojo needs no assistance. "
    t "My father never would have agreed to her working here anyway."
    s "Why? She’s surprisingly competent in a...really weird way."
    t "Like me?"
    s "Yes, but also no. I don’t think I’d call you surprisingly competent."
    t "That’s fair."
    t "But the real reason is her tattoo."
    s "Oh, yeah that makes sense. "
    s "With all the Yakuza hanging around here someone might...look at her the wrong way and think she’s on their turf or something?"
    t "No. My father just doesn’t like spiders."
    s "That...makes more sense than what I said."
    s "I always forget that arachnophobia is an actual thing people have."

    scene ramenfifteen5
    with dissolve

    t "Really? The research I’ve done about fear shows it as one of the most common phobias out there."
    s "Yeah, but it’s just- wait, why are you researching phobias?"
    t "Fear plays a big role in determining a person’s actions."
    t "I thought that if I could understand what everyone is afraid of, I would have an easier time talking to them."
    t "What I have learned in the process is that there are fears of everything. "
    t "This world is so scary."
    s "Are you afraid of spiders as well, Tsuneyo?"
    t "I think so. "
    t "It’s not a fear that makes me want to run or scream, but an uneasy feeling that sits in the pit of my stomach like undercooked pork."
    s "I think that’s still technically fear, though."
    t "Probably."
    t "Are you afraid of anything, Sensei?"
    s "Me?"
    t "You."
    s "…"
    s "Death, I guess?"
    t "Ahh, deathophobia."
    s "I think it has a more...scientific name than that."
    t "Is it the act of dying or what comes after that scares you?"
    s "I guess the act of dying since reincarnation is now a confirmed thing."

    "Probably. "
    "If that {i}is{/i} what actually happened to me."
    "I don’t even know how to describe my situation at this point."
    "Who knows?"
    "Maybe I’ll just wake up one day and this will all have been one, long dream."
    "What an ending that would be."

    t "You believe in reincarnation?"
    s "You don’t?"
    t "No. My father never believed in that so neither do I."
    s "You know you don't have to believe things just because your father does, right?"
    t "I want to, though. It makes everything easier."
    s "Well...what do you think happens, then?"

    scene ramenfifteen6
    with dissolve

    t "I’ve always been under the impression that we’d be buried and grow into trees."
    s "I don’t really think burying people works that way."
    s "We’re not seeds."
    t "Not yet."
    t "But what if after we die, all of the unused nutrients in our body leak out in thin strips like roots."
    t "What if every forest we see is actually a graveyard?"
    s "What would that make graveyards, then?"

    scene ramenfifteen7
    with dissolve

    t "Maybe that’s...where we bury trees?"
    s "Looks like your theory fell apart, huh?"

    scene ramenfifteen8
    with dissolve

    t "I’m just trying to repeat the things I’ve learned. "
    t "None of it really makes sense to me. But I have plenty of time to think when I’m not helping customers."
    s "You should be thanking me for always sending everyone else away, then. "
    s "Me coming here is pretty good for you in that sense."

    scene ramenfifteen9
    with dissolve

    t "Until it drives down sales and we can’t afford electricity anymore."
    t "But as long as you only come at night, we can still profit in the morning."
    s "Does your father come down and run the store in the morning still?"
    t "No, he’s unable to leave his room."
    t "I meant mornings on the weekend."
    t "We’re closed during the mornings on weekdays because I have to receive an education."
    s "You know you could solve that problem by hiring {i}someone else{/i} to work here, right?"
    t "But spiders."
    s "It doesn’t {i}have{/i} to be Kaori. What about Yumi?"
    t "She would be a better candidate, but I’m afraid she would call all of the customers “Mom.”"
    s "She did that with one person...and that one person {i}was{/i} her mom."
    t "That’s just what she wants us to think."
    t "I can see it now-"
    t "{i}Mom, where do we keep the noodles?{/i}"
    t "They are in the back, my child."
    t "{i}Thanks, Mom! I love you.{/i}"
    t "I love you too."
    s "There’s a flaw in your logic. It implies Yumi has the capability to love something."
    t "If she can not love, how can I expect her to treat the food here with the respect it deserves?"
    t "Can she even cook?"
    s "Well...no. Probably not."

    scene ramenfifteen10
    with dissolve

    t "Then there’s no point, is there?"
    t "Besides, running Tojo Ramen alone helps me protect all of its secrets."
    t "What would happen if a competitor discovered the special ingredient in our shio broth?"

    "Sorry, Yumi."
    "Can’t say I didn’t try."
    "It really would have been nice if she were able to work here."
    "It’s not far from Chika’s house and it’s not like she ever comes to[school] during the day anyway."
    "But {s}god{/s} God forbid someone discovered Tsuneyo’s secret broth."

    s "Well, if you ever get tired and don’t want to depend on my presence for a break, it might be worth looking into getting some extra help."

    scene ramenfifteen11
    with dissolve

    t "The Samurai of Flavor needs no help."
    t "My father was kind enough to entrust the business to me, so the least I can do is honor his wishes and not hire a spider."
    s "I think you’re forgetting about the {i}definitely human female{/i} that spider was attached to."
    t "Spiders are just humans with more legs."
    s "…"
    s "No, Tsuneyo."

    scene ramenfifteen12

    t "Ah-"
    s "I just don’t want you overworking yourself and then...getting buried and turning into a tree or whatever it was you assumed happened to people after death."

    scene ramenfifteen13
    with dissolve

    t "I can’t die yet."
    t "There is no one to bury me."
    t "Even if my father was able to regain his strength, leaving the room would prove to be very difficult for him."
    t "I’d turn into a tree wherever I died."
    t "And there’s nowhere I go that would be a convenient location for a tree."
    t "Imagine a situation where you came into the restaurant today and tried to have this exact conversation, but with a tree between us."
    t "It would be very difficult."
    s "Might be good for the atmosphere, though. It’s definitely a little stuffy in here."
    t "Fuck you. Get out of my store."
    s "Just because you found out “fuck you” isn’t an actual curse doesn’t mean it’s okay to keep using it as an insult on me."
    t "But there is no one else who makes me mad and it’s a very fun thing to say."
    t "You can fuck me too if you want. You’d be surprised by how fun it feels."
    t "Try it."
    s "…"
    t "Hurry up and fuck me, Sensei."

    if bonus == True:
        "I pull my phone out and open up the voice recording app."
        "I think I’m about to acquire a new ringtone."
        "It will go really well with my wallpaper of Makoto stuffing a dildo in her mouth."

        s "Can you say that one more time, Tsuneyo?"
    else:
        "I pull my phone out to create a voice memo that will allow me to avert blame should Tsuneyo ever accuse me of trying to blackmail her into achieving better grades."

        s "I am Sensei, the date is today, and I am recording this memo for my own protection."

    play sound "phonebeep.wav"

    t "Why won’t you fuck me? Is it too hard?"
    t "I’ll be okay. I’m a strong woman."

    play sound "phonebeep.wav"

    s "Thanks."

    if bonus == False:
        s "Please know that I don't support any of this and, despite it being a funny misunderstanding of a common term, I do hope you will soon learn to not speak in this way. Also-"

    s "I have to make sure none of the other girls ever hear this."
    t "You’re right."
    t "It would be bad if they found out we were fucking each other this early in our relationship."

    scene ramenfifteen14
    with dissolve

    t "Perhaps I will fuck the Emerald Guardian as well."
    t "Are there rules about girls fucking other girls?"

    "Tonight went from weird to awesome very quickly."
    "Tojo Ramen is the best."

    s "I think you should try, Tsuneyo."
    s "If you believe in yourself, even your wildest dreams can come true."

    scene ramenfifteen15
    with dissolve

    t "That sounds horrifying."
    t "If my dream from last night came true, our eyes would fall out and our teeth would liquify."
    s "Okay, maybe not dreams like that. I meant more like...goals."
    t "Like in soccer?"
    t "The short girl on our soccer team touched me inappropriately."
    t "Are you saying I can fuck her too if I believe in myself?"

    scene ramenfifteen16
    with dissolve

    t "Oh no! Do I have to fuck the entire soccer team?!"
    t "I’ve never even talked to most of them! "
    s "Hey, your father’s hearing isn’t...abnormally good or anything, is it?"
    s "I’m kind of worried about him hearing this and then defying all expectations and coming downstairs to kill me with his Yakuza friends."

    scene ramenfifteen17
    with dissolve

    t "He can barely hear anything anymore, but you make a good point."
    t "He’d be very upset to hear that his daughter was going around fucking everyone after finally being allowed out of the house."

    "It just keeps getting better and better."

    scene ramenfifteen18
    with dissolve

    t "I still apparently have much to learn about the proper way to fuck, but I’m hoping you will continue to teach me."

    if bonus == True:
        s "Don’t worry, Tsuneyo. I will fuck you as many times as you want."
    else:
        s "I will teach you many things, but none of them as gross and unnecessary as that."

    scene ramenfifteen19
    with dissolve

    if bonus == True:
        t "Even though I’m terrible and have no idea what I’m doing?"
        s "Even then."
        t "How long until we can team up and fuck other people together?"
        t "I am overjoyed just thinking about the shock on their faces when we fuck them at the same time."
        s "Soon, Tsuneyo. "
        s "Soon, we will fuck-"

    q "*Ahem*"

    scene ramenfifteen20
    with dissolve

    t "…"
    s "…"

    scene ramenfifteen21
    with dissolve

    yu "…"
    t "Oh. Good evening."
    t "Welcome to Tojo Ramen. Please let me know if you have any questions about the menu."
    s "…"
    yu "…"
    s "Hey, Yuki."
    yu "…"
    s "…"
    t "The air in this room has gotten quite strange."
    t "You two are acquainted, correct?"
    t "Perhaps you should fuck each other to lighten the mood."
    s "Tsuneyo, not a good time."
    t "It’s always a good time to fuck."
    yu "You know what? I’m not even hungry anymore."
    yu "Just gonna pretend this never even happened."

    scene ramenfifteen20
    with dissolve

    "Yuki leaves just as quickly as she arrived and several moments of silence pass before Tsuneyo finally decides to say something logical."

    t "Perhaps it would be best if we only fucked each other in private from now on?"
    s "Yeah..."
    s "Yeah, that’s probably for the best."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ ramen15 = True
    $ tsuneyo_love += 1
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ramen20:
...
```

## Code that triggers this event

File: (install folder)\game\TsuneyoEvents.rpy

Code:
```python
...
label ramenshop:
    if tsuneyo_love >= 0 and ramen1 == False:
        jump ramen1
    if tsuneyo_love >= 5 and ramen1 == True and ramen5 == False:
        jump ramen5
    if tsuneyo_love >= 10 and ramen5 == True and tsuneyodorm5 == True and ramen10 == False:
        jump ramen10
    if tsuneyo_love >= 15 and christmas7 == True and ramen15 == False:
        jump ramen15
...
```