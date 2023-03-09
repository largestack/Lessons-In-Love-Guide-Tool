# Unsleeping Aegis
Tsuneyo event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyodorm25&go=Go)



## Event preconditions
✅Tsuneyo love greater than or equal to 25

✅Event "[Main: All is Bright. All is Beautiful.](./secondbeach18.md)" is completed (event=secondbeach18)



## Next events
* [Molly: Resurrection Sickness](./mollycafe25.md)
* [Tsuneyo: Things Like Stairs](./ramen30.md)

## Event properties
* ID: tsuneyodorm25
* Group: Tsuneyo
* Triggered by label: tsuneyodorm
* Triggered by branch label: tsuneyodorm

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label tsuneyodorm25:
    play sound "knock.mp3"

    "I knock on Tsuneyo’s door and wait for her to answer."
    "I can hear the sound of some video game or something from outside, so it’s probably safe to assume that Molly is also home given that Tsuneyo is...well, Tsuneyo."
    "I honestly can’t even imagine her playing video games."
    "Or...really doing anything apart from cooking or following Molly around."
    "But hey, I’m sure there has to be at least {i}one{/i} game out there that everyone can enjoy."

    t "You may enter."

    play sound "dooropen.mp3"
    scene black with dissolve

    "I open the door and make my way into Tsuneyo’s room to see what she’s up to."
    "........."
    "......"
    "..."

    scene tsuneyonumberonemobilegame1
    with dissolve

    "And, as it turns out, my assumption from several seconds ago is completely incorrect and Tsuneyo actually {i}is{/i} playing a game."
    "Is this character development?"

    s "Hey, what’s going on? It’s not like you to be spending the night on your computer."
    t "The Emerald Guardian has asked that I train myself in the art of virtual combat."
    t "As a junior master of the art of Kendo, I imagined something like this would be very easy."
    t "But I am currently struggling to even perform the most basic of commands."
    t "How will I ever show my face around her again if I can not keep up with her character?"
    s "Just beat her in real life combat and prove once and for all that playing video games is a waste of time."

    scene tsuneyonumberonemobilegame2
    with dissolve

    t "Can anything be called a waste of time if it is something a person enjoys?"
    t "While I do not appreciate this form of entertainment very much, the Guardian has devoted her life to it."
    s "What kind of game would a real, live person actually dedicate their life to anyway?"

    play sound "static.mp3"
    stop music
    scene raid1 with flash
    scene raid2 with flash
    scene raid3 with flash
    scene raid4 with flash
    scene raid5 with flash
    scene tsuneyonumberonemobilegame3 with flash
    stop sound
    play music "rapid.mp3"

    t "The name of the game is Raid: Shadow Legends."
    s "Oh. Then forget everything I just said, because Raid: Shadow Legends is the number one mobile game of all time."
    s "I didn’t realize you were also a Raider, Tsuneyo."
    t "Guess again, bro. Because I’ve been spending a lot of time on this game lately, and I’ve gotta say, the hype is real."
    t "With over seven characters and graphics, the video game is certainly a game that you play."
    s "You’ve got that right, Tsuneyo."

    scene tsuneyonumberonemobilegame4
    with dissolve

    t "Ah-"
    s "Are you gasping because I said your name again?"
    t "No. I just struggle to breathe every time I am not playing Raid: Shadow Legends, the number one mobile game in all of Kumon-mi."
    t "Did you know that for every new person who plays Raid: Shadow Legends, there is at least one more person playing Raid: Shadow Legends?"
    s "That...yeah. Yeah, that’s how playing the game would work."

    scene tsuneyonumberonemobilegame5
    with dissolve

    t "Raid: Shadow Legends is also very easy to learn. "
    t "If a sheltered girl with minimal computer experience like myself can learn how to log in, I’m sure that even the most technologically disadvantaged people out there can also learn."
    t "And with right now being a day, it is the best possible time to download the game and press the buttons that cause the game to do things."
    s "Do you have a favorite champion, Tsuneyo? Because I’m really fond of Nekhret the Great in the Undead Hordes faction and his “Unsleeping Aegis” passive ability."
    t "I like Mario the Plumber from the Plumber’s Guild. He can jump."
    s "Wow. I didn’t realize there was also a character like that in Raid: Shadow Legends."
    t "There wasn’t until recently. "
    t "As it turns out, Raid: Shadow Legends exhausted the list of possible champions and has now begun taking over other game markets and consuming their characters."
    t "I would not be surprised if you and I were the next ones in line."
    s "Why would either of us get thrown into Raid: Shadow Legends? We’re not characters in a video game and, even if we were, there’s no way a developer like...whoever makes it would approach us."
    t "I believe Raid: Shadow Legends is made by EA Sports. It’s inside of the game."
    s "I think you butchered their slogan a little, but that’s fine. I’m sure it’s only a matter of time before the developers of Raid catch on to this event and-"

    scene raid6

    s "Oh, fuck."
    t "Why has everything suddenly gone so dark? "
    t "I am scared."
    s "It’s probably because you went so off-script and started talking about stuff that isn’t actually in Raid."
    t "Nonsense. There is no way the original developers of titles like-"

    scene raid7

    t "Oh. The screen changed again."
    s "Double fuck."
    t "I stand corrected. What have we done?"
    s "{i}I{/i} haven’t done anything. It’s you and the rest of the girls who keep bringing up copyrighted products and titles. "
    s "I’m just trying to be a likable protagonist."
    t "And how is that going for you?"
    s "Horribly. "

    play sound "static.mp3"
    scene tsuneyonumberonemobilegame6 with flash
    stop sound

    t "Woah."
    s "Nevermind what’s on your monitor, Tsuneyo. Tell me more about [[Censored due to DMCA claims]."
    s "Oh, god damn it."

    scene tsuneyonumberonemobilegame7
    with dissolve

    t "I suppose the time has come to move on."
    t "If we spend the next several minutes continuing to talk about this, more people will cancel their support for Selebus."
    s "You’re right. God forbid fourth wall breaking comedy finds its way into a game that is definitely serious 100%% of the time and hasn’t already been adding similar jokes for over one year as of October 8th, 2021."
    t "I can see the exit surveys now."

    scene raid8
    with fade

    s "You know, this world would be a much better place if more people would realize that some things exist just because a creator wants them to."
    t "That is correct, Sensei. The entire purpose of art is to express a certain idea or a feeling. And the moment artists let people control what they create, art ceases to be."
    s "Shhhh, they’ll call us pretentious again and that hurts our feelings."
    t "Oh, right. Instead of continuing this discussion, why don’t we simply wait ten seconds to see what happens?"
    s "Good idea. That will also give us an ample amount of time to continue guilt-tripping everyone into giving us their money to fight back against the totally real DMCA claims. "
    t "Sounds good to me, bro."

    scene raid9
    with dissolve10
    play sound "static.mp3"
    scene ayhh15 with flash
    scene ayhh13 with flash
    scene ayhh12 with flash
    scene ayhh10 with flash
    scene tsuneyonumberonemobilegame8 with flash
    stop sound
    play music "sweetvermouth.mp3"

    t "And that is why I do not normally like video games."
    s "…"
    t "Sensei?"
    s "Oh, sorry. I just feel like we got involved in something really weird that I...am having trouble remembering."
    t "I have heard you mention several problems involving your memory in the past. Do you believe it could be pertaining to that?"
    s "Nah. I’m sure it’s nothing."
    s "But please continue telling me more about your relationship with video games and how it pertains to our meeting tonight."

    scene tsuneyonumberonemobilegame9
    with dissolve

    t "I believe the Emerald Guardian is experiencing heartbreak for the first time, so I would like to do more things outside of the box to help her feel better."
    t "However, there are not many boxes in this room and the possibilities seemed far too great for me to choose just one."
    t "So, I decided to simply start doing something else she likes so she does not have to always play alone."
    t "I am very bad, though. So I believe I may have to start trying something else."
    t "If only she liked more games that did not take place inside of computer screens."
    s "I mean, haven’t you been watching her play that one game she plays with all of the other girls? Why not learn that?"

    scene tsuneyonumberonemobilegame10
    with dissolve

    t "I did. But it seems as if my presence in that game may have caused a bit of a rift since that is when the Guardian’s heart showed its first signs of cracking."
    s "I don’t really get what you mean by that, but I’m sure there are some other {i}actual{/i} games Molly enjoys."
    s "Like...what did you have in mind? Board games or like...playing cards or something?"

    scene tsuneyonumberonemobilegame11
    with dissolve

    t "Mahjong perhaps?"
    s "Mahjong? Isn’t that more for...older people?"
    t "Possibly."
    t "I learned by watching my father play a long time ago."
    t "It seemed very complicated, but he was always happy whenever he won and very sad whenever he lost."
    s "I would imagine it’s because he was gambling."

    scene tsuneyonumberonemobilegame12
    with dissolve

    t "To exist is a gamble in itself."
    s "Sure. But not for money."

    scene tsuneyonumberonemobilegame13
    with dissolve

    t "I suppose it would have made sense if there was money involved."
    t "That would certainly explain all of the money that was on the counter as he played."
    s "...What else did you think that money could have been?"
    t "Noodle money, paid in advance. I do not know."
    t "I was [young]and naive and did not think much of it."
    t "Now, I am older and slightly less naive, so I am able to better understand the meaning behind certain situations."

    scene tsuneyonumberonemobilegame14
    with dissolve

    t "My father is likely a gambling addict and I am set to inherit his debt."
    t "Now I {i}must{/i} teach the Emerald Guardian to play so I can push that debt onto her instead."
    s "So, your new method of cheering Molly up is to riddle her with debt before she finishes [high_school]?"

    scene tsuneyonumberonemobilegame15
    with dissolve

    t "I do not know what to do, Sensei. It is beginning to feel as if some wounds require nothing but time to heal."
    s "I mean...yeah. That’s kind of how it works."
    s "Having friends is nice and all when they can make you feel more...valid or whatever, but I’ve always believed the best way to get over anything is to let time take control."
    s "Sure, it’s a bitch more often than not, but it’s a hell of a lot better than a game."
    s "Right now, Molly’s options are either keep running forever...or wallow in misery until that misery is less...miserable."
    t "Neither of those seem like very good options."
    s "Nope. But what can you do?"
    t "Apparently nothing."
    s "Exactly. Her problems are her problems."
    s "It’s nice that you want to help her, but not if you’re going to be busting your ass trying new things that are just making {i}you{/i} feel worse. You know what I mean?"

    scene tsuneyonumberonemobilegame8
    with dissolve

    t "I do not think so. Now, I just feel inclined to find something to make you happier as well."
    s "What? Why?"
    t "Because even if I do not like you, I still like you."
    s "...What?"
    t "Tell me, is there something you would like to do that would make you feel more significant as a human being?"

    if bonus == True:
        s "Yes, but I don’t think we’re at that level yet."
        s "And it would really only make me feel more significant for a short burst of time until I go home and lay down again and it all gets worse."
    else:
        s "You can help me find my old baseball trophies so I can remember how I was always the most improved player every year."

    scene tsuneyonumberonemobilegame16
    with dissolve

    t "Perhaps I could teach you kendo?"
    s "What? Why would that be your first choice for “things that will make me feel more significant?”"
    t "Despite your physique, you appear to be weak and fragile."
    t "Perhaps, if you could defeat an enemy in combat, you will level up and gain skill points to distribute into various categories like “Happiness” and “Confidence.”"
    s "I don’t really know much about games nowadays, but I don’t think those are categories you can just put points into."
    s "Besides, which “enemies” would I even defeat? Everyone I know likes me."
    s "Even the people that {i}don’t{/i} like me probably like me. They just need more time to realize it."
    t "What an optimistic way of looking at things."
    s "I’m not really known for my optimism, but I’m also not really known for my kendo and would much rather fake being positive than have to learn something like that."
    s "Besides, I’m already enrolled in a karate class."

    scene tsuneyonumberonemobilegame17
    with dissolve

    t "You are learning karate?"
    s "I mean...no. But I {i}am{/i} enrolled."
    s "And by “enrolled” I mean that I just show up there whenever I want and talk to Ayane."

    scene tsuneyonumberonemobilegame16
    with dissolve

    t "As long as doing that makes you feel less horrible inside, I can accept it."
    t "I will keep the kendo offer on the table, though."
    t "Nothing makes a person feel better than slaughtering a foe. I am sure you are no exception to that very common rule."
    s "I didn’t realize the purpose of kendo was to “slaughter.”"
    t "Neither did any of my adversaries in the national competition. That is why they lost."
    s "You know...sometimes, I feel like you could secretly kill all of us if you really wanted to."
    t "Sometimes, I feel that way as well."
    s "Great. That’s not terrifying or anything."
    t "What is even more terrifying is the prospect of a situation in which I would need to do that."
    s "And on that note, I’m going to go back home and hang out with my [niece]- a person who would definitely not ever kill me."
    s "Everyone else? Maybe. But definitely not me."

    scene tsuneyonumberonemobilegame12
    with dissolve

    t "I understand."
    t "Thank you for stopping by to talk to me about violence tonight."
    s "That’s...not really why I came."
    t "But it was the end result, which means it will be all I take away from this conversation."
    t "I do not see how this will help me cheer up the Guardian at all."
    s "Me neither. But, if worse comes to worst, you can always just...slaughter her?"

    scene tsuneyonumberonemobilegame18
    with dissolve

    t "Sometimes, I believe you to be a machine who only exists to come up with the worst possible answers to things."
    s "That’s...as good a theory as any, I guess."

    scene black
    with dissolve

    s "Goodnight, Tsuneyo."
    t "Ah-"
    t "Goodnight to you as well."
    t "If you come up with a good way to assist the Guardian in not feeling sad anymore, please inform me."
    t "It is my role as her newly appointed squire to keep her in top form."
    s "I...will do just that."

    play sound "dooropen.mp3"

    "I make my way out of the room feeling as if I’d been there for much longer than I actually was."
    "It’s nice knowing that Tsuneyo is looking out for Molly in regard to the whole Rin thing, but I’m confused about whether or not she knows what’s {i}actually{/i} wrong."
    "Would Tsuneyo doing something like...learning to play games or teaching Molly mahjong really help her get over heartbreak?"
    "Nothing can be that simple, can it?"
    "And...if it is that simple, can it really be called heartbreak at all?"
    "…"
    "I don’t know why I’m thinking about this right now."

    if bonus == True:
        "I slide my phone out of my pocket and begin to distract myself with porn on the way home."
    else:
        "I slide my phone out of my pocket and begin to distract myself with videos of excited dogs seeing their owners after long periods of time."

    "Something like this is much easier than...whatever I was doing before."
    "I’ve already forgotten."

    $ renpy.end_replay()
    $ tsuneyo_love += 1
    $ tsuneyodorm25 = True
    stop music fadeout 5.0

    "{i}Tsuneyo’s affection has increased to [tsuneyo_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm25:
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
    if tsuneyo_love >= 10 and ramen10 == True and tsuneyodorm5 == True and tsuneyodorm10 == False:
        jump tsuneyodorm10
    if tsuneyo_love >= 15 and ramen15 == True and day != 1 and tsuneyodorm15 == False:
        jump tsuneyodorm15
    if tsuneyo_love >= 20 and tsuneyodorm15 == True and day != 5 and day247 == True and tsuneyodorm20 == False:
        jump tsuneyodorm20
    if tsuneyo_love >= 25 and secondbeach18 == True and tsuneyodorm25 == False:
        jump tsuneyodorm25
...
```