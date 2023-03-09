# Creatures of Habit
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chapthree5&go=Go)


Part of event chain [The Great Migration](./chapthree4.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: chapthree5
* Group: Main
* Triggered by label: chapthree4

## Event code
File: \game\chap3.rpy
Code:
```python
...
label chapthree5:
    scene postapocalypsekaraoke1
    with dissolve2
    play music "summerwind.mp3"

    "The rest of the day proceeds as if nothing traumatic or worrying ever happened at all."
    "It’s just me, two girls who recently made it through the end of the world-"
    "And two other girls who, at this point in time, seem to care more about what songs they’re going to sing than the state of the universe or what it means to be alive."
    "But I guess I can’t blame them for that considering how, up until a few hours ago, they {i}potentially{/i} didn’t even exist."
    "And I say “potentially” because my recent run-in with a half-invisible Maya has cast a shadow on all that I understand about world resets (Which wasn’t very much to begin with)."
    "Were they gone at all? Or were they just...temporarily invisible?"
    "Would I have seen them if I had just used the thirty seconds it would have taken to peer into their rooms instead of acting out of fleeting nepotism and disregarding their existences in favor of someone else?"
    "I don’t know."
    "{i}None{/i} of us know, not even Maya."
    "But I guess that’s why she didn’t put up much of a fight when I was dragged along to another karaoke trip today."
    "And I guess that’s why she’s been cautiously staring at me for the last twenty minutes with her customary disdain replaced with concern. "

    s "Can I help you with something?"
    m "..."
    ay "Can {i}I{/i} help you with something?"
    m "{i}Both{/i} of you can help me with something. The only issue is that I am a creature of habit and am not very good when it comes to actually asking for help."
    s "You ask me to help with your boxes all the time."

    scene postapocalypsekaraoke2
    with dissolve

    m "I do not. That’s just something you happen to do of your own volition because, whether it be conscious or not, you are also a creature of habit."
    ay "Boxes?"
    s "Yeah, she- "
    s "Wait, didn’t you-"
    m "Pardon me for interrupting, but there are more pressing matters at hand than discussing which of my belongings I keep hidden."

    scene postapocalypsekaraoke3
    with dissolve

    ay "Are we allowed to talk about the end of the world around Ami and Uta?"
    s "I normally just do it anyway. It’s not like they’re going to think we’re serious or anything."
    ay "Hey, Ami. The world is on repeat and Maya thinks I’m carrying Sensei’s baby."
    m "First off, stop it."
    m "Second, the two of them are so wrapped up in their own conversation that we could say {i}anything{/i} right now and it would likely go completely unnoticed."
    ay "Hey, Ami. Maya’s in love with-"

    scene postapocalypsekaraoke4
    with dissolve

    m "Thirdly, fuck off."
    ay "Hey, you’re not allowed to be mean to me anymore. We share a special bond now."
    m "The {i}bond{/i} we share has not changed in the slightest. You just happen to understand slightly more about our...{i}situation{/i} now."

    scene postapocalypsekaraoke5
    with dissolve

    ay "I actually think I understand {i}less.{/i}"
    m "I’ll fill you in shortly. It’s just not something I can really gloss over in the time it takes to get from school to the karaoke bar."
    m "Which is why I suggest we make normal, human conversation for the time being rather than discussing things like boxes and time travel."
    s "Wow, what a completely normal and human suggestion."

    scene postapocalypsekaraoke6
    with dissolve

    m "Or we can just not talk at all. That’s fine too."
    ay "I think we made her mad."
    m "I’m not mad."
    s "I have a feeling we’re going to be doing that a lot from now on since I finally have someone normal to talk to about all of this reset stuff."

    scene postapocalypsekaraoke7
    with dissolve

    m "I am not {i}abnormal.{/i} I’m the most “normal” person here."
    ay "Sensei! You’ve finally accepted my obsession and compulsion to be with you at all times as a normal character trait! I was beginning to think this day would never come!"
    s "No matter how you look at it, something like that is a lot more common than godly powers that allow you to manipulate the world at will."
    m "It is not {i}at will{/i} and there are no {i}powers.{/i} And since you apparently need to be reminded, anyone can-"
    s "Maya, can you be quiet for a second? I’m trying to talk to Ayane right now."

    scene postapocalypsekaraoke8
    with dissolve

    m "You-"
    ay "Sensei! I {i}knew{/i} the apocalypse would bring us closer together!"

    scene postapocalypsekaraoke9
    with dissolve

    u "Woah, what kinda conversation are we missin’ out on over there?"
    a "Apocalypse?"
    u "If you guys know something about the world ending, now’s the time to let the class know. "
    ay "Oh, it already did. You don’t have to worry, Uta."
    u "Uhh...what?"
    s "See? You’re getting the hang of this already, Ayane. Just keep being non-chalant about it and no one will ever realize you’re serious."
    ay "Maya can also turn invisible and Sensei walks around the school naked sometimes."

    scene postapocalypsekaraoke10
    with dissolve
    stop music fadeout 20.0

    u "Is..."
    u "Is that how you found out? Did she see him and, like...tell you about it or something?"
    ay "Yes."
    u "Oh."
    u "Cool."
    u "I’m..."
    u "Uhh..."
    u "I guess I’m gonna go back to my conversation with Ami now."
    a "You guys sure talk about weird stuff when I’m not involved..."

    scene black
    with dissolve2

    "Somehow or another, we manage to avoid making Maya mad for the rest of the walk to the karaoke bar."
    "But that’s probably just because she stays quiet until we finally make it there..."
    "........."
    "......"
    "..."

    scene postapocalypsekaraoke11
    with dissolve2
    play music "utasings.mp3"

    "She does open up again once we finally arrive, but it’s really just to fill in Ayane on all of the stuff I figured she would have been filled in on when she first made it to the roof."
    "She goes over how it’s something that happens every four-ish months or so, but how it’s something she has to “feel” rather than something she can mark on her calender. "
    "She goes over how the disappearance of everyone has stopped impacting her the way it did in the beginning."
    "She goes over how the world is part of a never ending cycle that she alone has witnessed and that tampering with it has never yielded any meaningful results."
    "But the one thing she goes over for longer than all of the others is the fact that something like {i}this{/i} has never happened."
    "And that throughout all of the time Maya has spent in these loops, Ayane and the rest of the girls have remained as mere pieces on a chess board, playing their part before ultimately being removed and packed away."
    "She doesn’t know what this means. She makes that very clear."
    "Because of that, she wants to be careful. "
    "But while news like this would sound like utter nonsense to anyone else, Ayane listens closely and never once dismisses anything Maya says. I mean...why {i}would{/i} she at this point after all she’s seen?"
    "This all happens while two other girls, loud and gleefully oblivious off in their own room, sing as if their pending removal from the chessboard we call life is not in store for them-"
    "And that it is impossible to dread anything if you are not acutely aware of it."

    scene postapocalypsekaraoke12
    with fade

    m "I believe that about sums up the basics of our situation. So, if you have any questions, now would be the time to ask them."
    ay "And...what if I have like, a million questions? Because I obviously believe you, but...there’s still a ton that I don’t get."
    ay "Like...why {i}me?{/i} And if Sensei is the only other person who’s ever made it up to the roof with you, why him?"

    scene postapocalypsekaraoke13
    with dissolve

    m "If I knew the answer to that, I would have included it in my speech just now."
    m "But the connection to Sensei is why I was and still {i}am{/i} confident about the reasoning that led to you joining us."

    scene postapocalypsekaraoke14
    with fade

    ay "Even if that {i}was{/i} true, which it’s not, that wouldn’t explain why {i}you{/i} always make it to the roof."
    ay "Unless you’ve been, like...secretly pregnant this whole time or something. Which would be both very weird and extremely offensive to me, the girl who actually {i}wants{/i} a baby."
    m "I am decidedly not pregnant."
    ay "Neither am I, but you still don’t believe me."
    m "Oh, I believe that you’re not pregnant {i}now.{/i} What I don’t believe is that you weren’t pregnant {i}then.{/i}"
    ay "Then as in-"

    scene postapocalypsekaraoke13
    with fade

    m "When you made it to the roof."
    ay "The first time? The one I don’t remember? Or-"
    m "Both times. "
    ay "So...what? The baby just...goes away once I respawn or something like that?"
    m "Or something like that."
    m "My theory is that Sensei’s lingering DNA inside of your system formed some sort of connection between the two of you that {i}tricked{/i} the world into believing you were an extension of him."
    ay "But then what about you? Or, wait- what about Ami? She has tons of Sensei’s DNA in her."
    s "Please don’t say it like that."
    m "While that may be true, the link between them is a lot slimmer than that of a parent and child. "
    ay "Well...what about you, then? How come you’re, like...patient zero?"

    scene postapocalypsekaraoke12
    with dissolve

    m "Again, this is something I’d gladly share with you if I actually knew."
    m "But the truth is that the vast majority of what has happened lately is brand new to me...and that all I can do is simply develop and test theories. "
    m "If something can be proven wrong, I am more than willing to accept it."
    ay "I {i}did{/i} prove the last one wrong, though! I really wasn’t-"
    m "I’m not calling you a liar. I’m saying you could have made a mistake or...whatever tests you took could have been...I don’t know- broken or something. That can happen, right?"

    scene postapocalypsekaraoke15
    with fade

    ay "Given how much time you’ve been doing this, I figured you would have had a better argument than “pregnancy tests can be broken.”"
    m "I’m sure if this was a thing that happened thousands of times before, I would. But the fact of the matter is that it hasn’t and I do not. So all I can do is guess."
    m "If you have a better guess for why you made it to the roof multiple times, I’d be happy to hear it."

    scene postapocalypsekaraoke16
    with dissolve

    ay "Maybe it’s based on...how much we love Sensei?"
    ay "Maybe our love is just so powerful that the world-"
    m "Theory rejected. Love is not something that can be accurately quantified, so the idea of that being the single factor determining which consciousnesses are reset is laughable. "
    m "Unless you’re actually able to test that theory, I suggest you put it to rest."
    ay "We could always have a “Who loves Sensei more” competition. "
    m "I concede. You win. "
    ay "You’re only saying that because you know you would have lost anyway."

    scene postapocalypsekaraoke13
    with fade

    m "Yes. Sure."
    m "Regardless, understanding {i}why{/i} Ayane made it to the roof could be the key to understanding...well, {i}anything{/i} about this world. "
    m "If it’s something we can test, we have to test it. "
    m "Which is why I’ve come up with a foolproof plan to confirm once and for all whether or not my theory is accurate."
    s "And that plan is?"

    scene postapocalypsekaraoke12
    with dissolve

    m "The two of you can’t have sex until the next reset."

    scene postapocalypsekaraoke17
    with fade

    ay "..."
    s "..."

    scene postapocalypsekaraoke18
    with dissolve

    ay "..."
    s "..."

    scene postapocalypsekaraoke19
    with dissolve

    ay "Do you have any other plans?"

    scene postapocalypsekaraoke20
    with fade

    m "Are you kidding? I’ve been living in a never ending cycle for as long as I can remember that we have an opportunity to finally start understanding and {i}that{/i} is your response?"
    ay "You see, I’ve just got a very high sex drive and-"

    scene postapocalypsekaraoke21
    with dissolve

    m "I don’t want to hear about your sex drive! I want to figure out what’s going on! Which, need I remind you, includes {i}you{/i} now!"
    ay "I...I know that! It’s just...well...this is all happening so quickly and..."
    ay "And...you see...my sex drive is-"

    scene postapocalypsekaraoke22
    with dissolve

    m "Can you shut up about your sex drive for one minute?!"
    u "Woah. I know Ayane’s pretty open about that sort of thing, but I didn’t really think we were at, like...intervention territory yet."
    u "You know what? I’ll just head back in for one more song and let the three of you finish whatever this is."

    scene postapocalypsekaraoke23
    with dissolve

    m "Hah..."
    m "We’ll resume this talk later..."
    m "But for the time being, {i}please{/i} take what I said into consideration."
    m "It might sound “difficult” to you, but I am extremely serious about this. "
    u "..."
    s "..."
    ay "..."
    u "You, uhh..."
    u "Tryin’ to help Ayane out with her sex drive, Maya?"

    scene postapocalypsekaraoke24
    with dissolve

    m "..."
    u "..."
    m "Today sucks. I am going to sing now."

    scene postapocalypsekaraoke25
    with dissolve

    u "I say just let her do it even if you’re not into girls, Ayane. She seems determined and confident and those are good qualities when it comes to that sort of thing."
    u "She probably knows what she’s doing."
    ay "I sure hope so..."

    scene black
    with dissolve2

    "Ayane disappears into the room with Maya and Ami while Uta remains out in the hall with me, stopping me by grabbing my sleeve once I try to move past her..."
    "........."
    "......"
    "..."

    scene postapocalypsekaraoke26
    with dissolve2

    u "So, uhh..."
    u "Are you...not going to sing today, Sensei?"
    s "You know, the last time I even {i}thought{/i} about doing that, some tiny girl with glasses tackled me and we almost kissed. Me staying away from the mic is the safest bet for everyone."

    scene postapocalypsekaraoke27
    with dissolve

    u "Hahah...yeah...I guess when you put it that way...it makes sense..."
    u "Besides, you’ve got three whole girlfriends in there right now. Who knows what sort of stuff you’d get up to if any of them decided to...you know...{i}tackle{/i} you."
    u "Even if what {i}I{/i} did was like 99%% accidental and wasn’t really a “tackle,” you know?"
    s "..."
    u "..."

    scene postapocalypsekaraoke28
    with dissolve

    u "A-Anyway! Enough about awkward past experiences and...things that would get me in trouble with the girls next door."
    u "Are you excited for the whole...club swap thingy that’s going on?"
    s "Me? Not really. It doesn’t really impact me in any way. "
    s "If anything, it might actually even save me some time after school since everyone will already be doing stuff and won’t have to come to me for counseling."

    scene postapocalypsekaraoke29
    with dissolve

    u "Well...{i}I’m{/i} excited. "
    u "It’s been a while since I’ve done any of the stuff old Uta was into. "
    u "And I’ve been feeling kinda...nostalgic lately...or something."
    u "Do you ever get like that, Sensei?"
    u "Do you ever feel like...I don’t know..."
    u "Like history is kind of repeating itself?"
    s "Probably not in the same way you do."
    u "Heh...yeah."
    u "Probably not."

    scene postapocalypsekaraoke30
    with dissolve

    u "E-Either way! I hope you’ll come see me in club sometime."
    u "I might not be able to knock your socks off the way I do at the maid cafe, but I’m sure you’ll be impressed! "
    s "I’m sure I’ll be there a lot, but...I don’t think you’ve mentioned which club you’re joining yet."
    u "That’s cause I’m still waiting on one other person to sign on. But seeing as her options are pretty limited, I’m confident I’ll get her to agree by the end of tomorrow. "
    s "And if she doesn’t?"
    u "If she doesn’t..."
    u "Then she’s grown a lot more than I have."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ chapthree5 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    "I step into the bedroom to be met with an unfamiliar sensation."
    "A natural heat, not an artificial one brought on by the house’s radiators, permeates throughout the room and reminds me of why I was so thankful for the winter in the first place."
    "The trip back home from the karaoke bar was uneventful."
    "The dinner Ami made when we returned was uneventful."
    "Everything after what happened on the rooftop was uneventful."
    "But that’s okay."
    "That’s okay."
    "Because everyone is still here."

    scene black
    with dissolve2

    "Because I am still here."
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day += 1
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date

    jump chapthree6

label chapthree6:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
scene summerclass36
    with dissolve

    n "THE BAND IS GETTING BACK TOGETHER, BITCHES!"
    sa "You two were...in a band together?..."
    o "Kind of, yeah. It’s not like we ever really played any shows or anything. My parents were always weird about that."
    o "But it’ll be a hell of a lot easier to hide now that I don’t live at home anymore. Plus, Noriko’s like, a ridiculous fucking bassist."

    scene summerclass37
    with dissolve

    n "What can I say? I’m an expert when it comes to fingering."
    o "Please don’t say things like that around my girlfriend."

    scene summerclass38
    with dissolve

    n "Speaking of which! You’re gonna join too, right?! Having another guitarist would mean that all we’re missing is a drummer and, like...{i}maybe{/i} someone on keys if we want to go full K-On."
    r "Me? Uhh..."
    r "Y...Yeah! Totally! I’d love to join you guys if Otoha is okay with it!"
    o "Are you kidding? Why wouldn’t I be okay with that? I’d love to be in the same club as you. "

    scene summerclass39
    with dissolve

    f "Wait, Rin...what about the manga club?"
    r "...Fuck."
    f "Does this mean you’re planning on leaving?"
    r "Well..."
    r "I..."
    o "I’m not going to get offended if you want to stay in manga club, Rin. I just think it would be cool to be in the same club together."

    scene summerclass40
    with dissolve

    r "No, I...I really want to join the light music club with you guys! I’ve always wanted to be in something like that and...and I want to spend more time with you!"
    r "It’s just...I don’t...really know what to do."

    scene summerclass41
    with dissolve

    f "Well...whatever you {i}do{/i} decide to do...know that I won’t take it personally."
    f "But if you {i}are{/i} planning on leaving the manga club...you should at least talk to Molly about it. "
    f "It wouldn’t be right to just...abandon her without saying anything."
    r "Yeah...I know...just..."

    scene summerclass42
    with dissolve

    r "Ugh...this would be so much easier if we were allowed to be in two clubs at once."
    o "What about you, Nodoka? You’ve been awfully silent over there."
    o "Any idea what club you’re joining yet?"

    scene summerclass43
    with fade

    no "Heh heh heh..."
    no "As if there was ever a choice to begin with..."

    scene summerclass44
    with dissolve

    no "Skintight...spandex...school swimsuits..."
    no "Changing and showering together..."
    no "Touching each other’s bodies..."
    f "I...don’t think that’s part of the-"
    no "The medley of assorted shampoos blending together into the single purest, most mouth-watering aroma a person could ask for..."

    scene summerclass43
    with dissolve

    no "Not to mention the probability of wardrobe malfunctions is exponentially higher in the swim club than any other club this school has to offer..."
    no "Hearing all of that, do you truly think there could be any other place for me?"

    stop music fadeout 10.0

    o "Nope. That’s pretty much you, alright."
    f "Well...at least you’re honest."
    sa "Is Nodoka always this...um..."
    o "Whatever you’re going to ask, the answer is yes."
    n "Sometimes, I think Nodoka might like girls even more than you do, Rin."
    r "..."
    n "..."
    n "Rin?"
    r "Um..."
    r "I think...um..."
    r "Maybe I want to...join the swim club as well..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ chapthree4 = True

    "........."
    "......"
    "..."

    jump chapthree5
...
```