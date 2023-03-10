# Supermom (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 10

* Event [Nothing to Do](./sanafirsthall.md) (Sana) is completed)



## Next events

* [Main: The 'S' Word](./day70.md)
* [Main: What's Done is Done](./beachvacation1.md)
* [Sana: Anywhere At All](./sanadorm10.md)
* [Sana: Carry Me Home](./bar15.md)

## Event properties

* Id: bar10
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar10

## Official wiki page

[Supermom](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar10&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar10:
    scene sarabar1
    with dissolve2
    play music "calmbar.mp3" fadein 2.0

    "I enter the bar to be greeted by a tragic sight."
    "It seems that Sana has aged fifteen years or so since the last time I've seen her."
    "I contemplate to myself the possibility of her concealing a tragic hormonal disease from me, but then remember the key detail of her being a human being."
    "Which means that, more than likely, this is the original owner of her DNA."
    "In other words, it looks like Sana's mom is working tonight."

    q "Well...hi!"
    q "Can't say I've seen you around before."
    q "Come on over. I don't bite."

    scene sarabar2
    with fade

    q "What can I get you? As a heads up, we're pretty low on...a lot of things right now."
    s "Just a beer is fine, thanks."
    q "Coming right up."

    scene sarabar0
    with dissolve

    "The woman heads over to the cooler and grabs the same beer I always have when I'm here."
    "Not like there are any options to begin with, but at least it's one that I've come around to enjoying."

    scene sarabar3
    with dissolve

    q "Aaaand one beer. Want me to leave your tab open or are you gonna be a loser and abandon me after one drink?"
    s "Well, I {i}was{/i} thinking about being a loser tonight, but with words like {i}abandon{/i} sneaking into the conversation, I don't know if I should anymore."

    scene sarabar4
    with dissolve

    q "That’s the spirit! Plus, now you get to hang out with me free of charge. And that's something I make everyone else pay extra for, you know."

    "Add that to the list of reasons this bar is failing, I guess."

    s "Thanks a lot for the discount. I feel even less inclined to abandon you now."

    scene sarabar3
    with dissolve

    q "Don’t mention it. It's not every day somebody like you walks in."
    s "You mean a customer?"

    scene sarabar4r
    with dissolve

    q "Well, uhh...I was {i}going{/i} to say somebody handsome. But...yeah. I guess what you said is...just as accurate."
    q "At least we're known for {i}something,{/i} I guess. I would have preferred it didn't involve how dead the place is, but I guess beggars can't be choosers."
    s "I only know because I've become sort of a regular here. There's no word on the street about the place or anything like that."

    "Though, I can't imagine it wouldn't help if there was."

    scene sarabar5
    with dissolve

    q "Wait, you're a regular {i}here{/i}? At this bar? The one we're currently inside of?"
    q "Are you sure you don’t have us confused with some other place?"
    s "It's definitely this place. I'm sure."
    q "It’s just weird that I’ve never seen you before if you’re a regular..."
    s "That's probably because the younger version of you is typically the one who helps me."

    scene sarabar4
    with dissolve

    q "Aww! My sweet little girl Sana is- wait. You're not saying I look old, are you?"
    s "You look very young. Just...also understandably older than the smallest girl I know."
    q "She's doing okay, then? I had no idea she'd been actually helping anybody lately."
    s "She’s...doing her best. She needs a little work still, but I’m helping her get there."

    scene sarabar5
    with dissolve

    q "Helping her get there? What do you mean?"
    s "I mean that, as her teacher, I can't let her permanently struggle when it comes to common social skills."

    scene sarabar6
    with dissolve

    q "Oh my god, {i}you're{/i} Sana's teacher?! It’s so nice to finally meet you!"
    sar "I’m Sara! I always figured our first meeting would be, like...not inside of my bar."
    s "Life can be unpredictable at times, I guess. Meeting here is much more interesting than in my office, at the very least."

    scene sarabar5
    with dissolve

    sar "I’m really surprised, though. All this time, I was under the impression you were a woman. You're so young, too."
    sar "How old are you? If you don’t mind me asking, I mean."
    s "Uhh..."

    "...How old {i}am{/i} I?"

    if bonus == True:
        s "I’m...34."
    else:
        s "I have lived for countless millennia. I am eternal."

    "I spit out the first number that comes to mind."
    "I should probably ask Ami if I have an ID tucked away anywhere, since I don't think I've seen it since starting my new life."

    scene sarabar6
    with dissolve

    sar "Wow! That means you and me are almost the same age! I can’t believe Sana never told me!"
    s "What {i}I{/i} can’t believe is that you're a mother. You could probably pass as one of my students if you wanted to."

    scene sarabar3
    with dissolve

    sar "Well, I {i}do{/i} still fit in my old uniform if you ever wanna test that theory out a little more..."
    s "..."
    sar "...is what I {i}would{/i} be saying if I was not such a dedicated mother who always puts her daughter first!"
    s "Oh, sorry. The only reason I went silent is because I was fantasizing."

    scene sarabar6r
    with dissolve

    sar "Oh, thank god. I thought I set a new record for the time between an introduction and a fallout for a second."

    "Did Sana really come out of this woman? The two of them couldn't be any further apart."

    scene sarabar7
    with dissolve

    sa "Mom, I finished cleaning the glasses. Did you want me to-"
    s "Hi, Sana."

    scene sarabar8
    with dissolve

    sa "Ah-"
    sa "Oh...I...I see that..."
    s "I finally met your mom, yes."

    scene sarabar9
    with dissolve

    sar "Hey! You let me think your teacher was a woman this whole time and never even bothered correcting me! How come?!"
    sa "I...just...I don't know..."
    sar "Any other mom would totally ground you right now, you know. You’re lucky I'm the best."
    sa "R-Right..."

    scene sarabar10
    with dissolve

    sar "So, are there any good stories about Sana from[school]? Please tell me if there are."

    scene sarabar11
    with dissolve

    sa "Mom! Stop! I already told you...I don’t really talk to anyone..."

    scene sarabar12
    with dissolve

    sar "Well, that's not true! What about that cute blonde girl that comes over sometimes?"
    sar "Oh! Ayane! That was her name. I think."
    sar "Or...Ayaka?"
    sar "Anya?..."

    scene sarabar13
    with dissolve

    sa "It's...Ayane..."

    "Poor Sana. It seems like even she has trouble dealing with how outgoing her mother is."
    "Luckily for her, I'm going to decide {i}against{/i} embarrassing her in front of her mother as I believe it will increase the chances of her eventually sleeping with me."
    "Ulterior motives reign supreme once again."

    s "I’m afraid I don’t have any interesting stories to share, unfortunately."

    scene sarabar14
    with dissolve

    sar "Awe! Darn it! If anything happens, though, you have to let me know. That's a new rule starting right now."

    scene sarabar15
    with dissolve

    sar "Oh! I know! I’ll give you my number so you don't have any excuse not to!"
    sa "Mom! Stop! Sensei doesn’t want your number!"
    sar "Doesn't he need it, though? I'm your emergency contact and I need to know if something bad ever happens."
    sar "Being able to hear embarrassing stories with the push of a button is just an unfortunate side effect, I'm afraid."

    "Sara swiftly scribbles her number on a sheet of receipt paper and somehow slides it over to me without Sana noticing."
    "Despite what her daughter says, I gladly accept it."

    sa "Mom!"
    sar "What’s the problem, dear? I’m just trying to keep tabs on my precious little girl."
    sa "I can...take care of myself!"

    scene sarabar16
    with dissolve

    sa "Besides...Sensei...would...never let anything bad happen to me...so..."
    sar "…"
    sa "…"

    scene sarabar17
    with dissolve

    sar "Well, well, well..."
    sar "What do we have here?"

    "Sara shoots me a slightly suggestive glance as Sana looks away from us."
    "And, without beating around the bush, I'm pretty sure it's her insinuating that her daughter might have a little crush on me."
    "I doubt it's true, but I'm not going to argue it because I want it to be."

    sar "So...{i}Sensei...{/i}my little girl seems to believe that you’ll protect her from the evils of life. Is this true?"
    s "More or less."
    sa "Sensei...I’m sorry my mom talks so much..."
    sa "Her...brain is...um..."
    sa "She has an...illness that makes her...say things and..."
    sar "Oh, stop. I do not."

    scene sarabar18
    with dissolve

    sar "Sensei, you know I'm not sick, right?"
    s "I mean...I don't {i}know{/i} that...but based on my experiences tonight, I have no reason to assume you are?..."
    sar "Exactly!"
    sar "I'm just a totally normal super cool, super young, supermom."
    sar "And if my daughter trusts you with her well-being, I guess I do too."
    sar "Welcome to the bar, Sensei."
    sar "I imagine we'll be seeing each other quite often from now on."
    sa "I...really hope not..."

    scene black
    with dissolve2

    "I wind up staying for a few more drinks and chatting with Sara about all sorts of things."
    "She’s the first person my age that I’ve felt some sort of connection with. And she {i}does{/i} genuinely seem to care about Sana in that ‘overbearing mom’ sort of way."
    "The two of them are like oil and water. You know they won't work well together, but the immense curiosity of combining two incompatible components is enough to pique your curiosity."
    "The night moves on and I observe as their respective spills combine."
    "I feel no need to clean anything up."
    "I simply enjoy a few more drinks and then head home."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar10 = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 5.0
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar15:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
...
```