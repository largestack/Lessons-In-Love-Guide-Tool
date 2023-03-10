# You and Me (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 15

* Event [Past/Present/Future](./shrine10.md) (Maya) is completed)

* Event [Rewind/Repeat/Refuse](./mayadorm10.md) (Maya) is completed)



## Next events

* [Main: Recall](./day96.md)
* [Maya: Takoyaki](./mayadorm15.md)

## Event properties

* Id: shrine15
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->shrine15

## Official wiki page

[You and Me](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine15&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine15:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "I arrive at the shrine and discover that Maya is nowhere to be seen."
    "That’s come to be expected at this point, though."
    "I know she's already denied it but, to be 100%% honest, I wouldn’t be surprised if she was using some sort of weird divine powers to sense my location and hide from me."
    "Though, I will say...avoidance aside, I have felt at least {i}slightly{/i} closer to her lately."
    "She even lets me in her room now. That must mean something, right?"
    "Sure, it might be due to the fact that I’ll just bother her even more if she {i}doesn’t{/i} let me in...but what if it's not?"
    "What if underneath the miko dress, there's a girl who-"
    "Who-"

    s "..."

    "My thoughts quickly get wrapped up in the image of what is underneath Maya's dress and I forget what I was previously thinking about."

    s "..."

    "I-"

    s "..."

    "I should probably try and find her..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene noonsky
    with dissolve
    stop music fadeout 20.0

    s "Is...she even here today?"

    "I wander the grounds for a good ten minutes without seeing Maya anywhere."
    "I’m not sure what the schedule for a shrine maiden is like but I'm pretty sure I've heard her say in the past that she's here every weekend."
    "I stop and think for a moment that maybe something happened to her."
    "That maybe someone else got wrapped up in the same thoughts that flooded my head just moments ago."
    "That someone else {i}was{/i} able to find her...and that they acted on them."
    "And that there could be some alley not far from here with a torn hakama and the slender body of a servant of {s}God{/s} god pressed up against the wall."
    "If only I had made it here sooner."

    scene black
    with dissolve2

    "I begin to make my way to the steps of the shrine when the glow of the sun redirects my attention to an area I’ve never seen before."
    "It seems that there is a separate section of the shrine hidden behind a large tree and a few unused donation boxes."

    s "..."

    "I guess one last lap around the grounds wouldn't do any harm."
    "………"
    "……"
    "…"

    scene glowofthesun1
    with dissolve2
    play music "shrinemaiden.mp3"

    "A normal [teenage]girl stands with her head hung low in the glow of the sun as it bleeds its way through broken tree branches."
    "It seems she hasn't noticed my presence as of yet."
    "And she looks so peaceful and beautiful in this moment that I have second thoughts of disturbing her at all."

    play sound "static.mp3"
    scene tree3 with flash
    scene glowofthesun1 with flash
    stop sound

    "But then I remember I need to raise my affection level with her."
    "I remember the sensation of the weakest part of me hardening just moments ago at the thought of what lies underneath that robe."
    "And so I call out, disrupting her midday slumber- killing the peace and beauty along with it."

    s "Ma-"
    m "Good afternoon."

    scene glowofthesun2
    with dissolve

    m "It seems that no place here is truly sacred anymore."
    m "And just when I was starting to believe I’d be able to avoid you today."
    s "It only took me about fifteen minutes to find. I wouldn't call your mission a complete failure."
    m "I suppose not. It might not seem like much to you, but fifteen minutes of peace and quiet goes a long way when you're around."
    m "I did what I could with what little time I had. But I suppose I knew that would come to an end soon enough."
    s "Are you saying you knew I was coming?"

    scene glowofthesun1
    with dissolve

    m "I suppose."
    s "Divine powers again?"
    m "If only it were that simple."

    "A long silence fills the gap between us."
    "I can feel it attempting to force me back toward the stairs I ascended just a short while ago, but I have a hard time tearing myself away from the sight before me."
    "Bathed in the glow of the sun is a girl staking her case as the most forbidden fruit of all."
    "More forbidden than the one with my blood."

    play sound "static.mp3"
    scene amiclass with flash
    scene glowofthesun1 with flash
    stop sound

    "More forbidden than the one who {i}wishes{/i} for that blood."

    play sound "static.mp3"
    scene ayaneclass with flash
    scene glowofthesun1 with flash
    stop sound

    "Before me lies a servant of God who often looks like she'd rather not serve at all."
    "One who shuns not only Him, but me. A girl who walks her own path despite the many hands that attempt to pull her down others."
    "I want to pull at her as well."
    "Not just her hair and not just her clothes, but her. Herself. Down a path that I'm afraid of taking on my own."
    "But what I hope to gain from her company is still uncertain to me."
    "What I hope to gain from almost anything is uncertain to me."
    "But what disgusts me the most is that the one thing I {i}am{/i} certain about wanting would leave her a spasming mess on the floor of my bedroom."
    "The fact that I can think that at all in a place like this is proof that God truly is dead."
    "Either that...or he has simply abandoned us."

    play sound "static.mp3"
    scene mayaclass with flash
    scene glowofthesun5 with flash
    stop sound

    m "What do you want? Why are you coming closer?"
    s "I don’t know."
    s "I just want to, I guess."
    m "Ugh...Don’t you have other places to be? Like...literally {i}anywhere{/i} else?"
    s "Not really, no."
    m "For the love of whoever lives here...stop using your free time on me. I mean it."
    m "There is absolutely nothing good that can come of this."
    s "Nothing at all?"

    scene glowofthesun6
    with dissolve

    m "That's right."
    m "Nothing at all."
    m "You’re close enough to ruin as-is."
    m "One wrong move or strange circumstance may send you spiraling out of control."
    m "You’ll wind up in a place you’ve never seen before."
    m "And suddenly, you’ll be back at the beginning of everything."
    m "Please avoid this string of unfortunate events by spending your time with other girls."
    s "I think I’m good. Getting closer to you is my primary objective right now."

    scene glowofthesun7
    with dissolve

    m "Tch-!"
    m "Stop..."
    m "Treating this..."
    m "Like a fucking game."
    m "I understand how ecstatic you must be to find yourself in a new world surrounded by so many adoring girls...but those girls are {i}people.{/i}"
    m "And as much as I hate to admit it, so are you."
    m "Do not call me an {i}objective.{/i} Not when it lessens the impact of everything I have done so far."

    "That’s...an unusual look for her."
    "I don't think I've ever seen Maya look genuinely angry before."

    s "..."

    "Maybe...I {i}am{/i} pushing her a little too far, after all?"

    scene glowofthesun8
    with dissolve

    m "Why? Why don’t you ever listen to me?"
    s "I...don't really know."
    m "I swear, this version of you is perhaps the most irritating one yet."
    m "Perhaps it's not too late to trade it in for a different one."
    s "I can probably help with that. Do you still have your receipt?"

    scene glowofthesun9
    with dissolve

    m "Why would I keep a receipt for something I never wanted in the first place?"
    s "Bookkeeping, maybe? I don't really know how you handle stuff like that."
    m "Please...just leave this place and carry on with your day. Thank you."
    s "..."

    "Maybe I should try talking to her in a more...{i}Maya{/i} sort of way?..."
    "You know. Appeal to her with vague, thought-provoking questions about different kinds of...spiritual or existential ideas or something."
    "That might work a little better than just...annoying her until she caves."

    s "Hey..."
    m "I said leave."
    s "How do you feel about...fate?"

    "I say the first vague, thought-provoking thing that comes to mind."

    m "..."
    s "..."

    scene glowofthesun10
    with dissolve

    m "What?..."
    s "You know. Fate."
    s "Do you have any...thoughts on it or anything?"
    m "And...why exactly would you ask me something like that?"
    s "Just wondering."
    s "I realize I’ve asked you plenty of questions since showing up here in Kumon-mi...but I thought that maybe I should try asking you something a little different this time."
    m "But why {i}that{/i} question, of all things?"
    s "No reason, I guess. It just sort of came to me."
    m "..."
    s "Or maybe it's because I was just {i}fated{/i} to ask you that?"
    m "..."
    s "..."
    s "I'm sorry."

    "Maya stays quiet for an uncomfortably long time, not reacting to my subpar attempt at a joke."
    "I can’t tell if this means I chose the right topic or the wrong topic."
    "She doesn't normally take this long to respond to...anything, though. So I'm beginning to think that-"

    scene glowofthesun11
    with dissolve

    m "I don’t like this question."

    "Well...I guess it was the wrong topic after all."
    "I’ll just have to think of something else instead."
    "I open my mouth, hoping the right words somehow fall out on their own...but before anything falls, she speaks again."

    m "Fate is...well..."
    m "Inevitable?"
    m "There aren't many things I will openly admit to believing in when it comes to the world and all of its many horrible mysteries."
    m "But that..."
    m "Actually, no. No, I don’t think {i}belief{/i} has anything to do with it at all."
    m "Fate exists. It’s all around us."

    scene glowofthesun12
    with dissolve

    m "Do you remember my talk about how we all see the same thing as one another, just...filtered through different lenses?"
    s "That thing about how we’re all living in some never ending cycle or whatever?"
    m "Yes. That we’ll all wind up in the same place regardless of the decisions we make."
    m "Do you not see the resemblance this carries to your question?"

    "Now that she mentions it, what Maya was talking about back then is essentially the same thing I’m asking her now."
    "I didn't mean it like that, though. I didn't put any thought into this question at all."
    "It was just a random thought that fell out of my head and into her hands."
    "But I’m not sure she realizes that."
    "In her head, she's probably thinking that I’m starting to come around to her unwavering, weird perception of the universe."

    s "I...remember the talk we had. But what I remember more than that is how you fell asleep sitting up at the end of it."
    m "Oh, that? I wasn’t sleeping. I was just waiting for you to leave and {i}pretending{/i} to be sleeping so you would do that."
    s "..."
    m "But that’s beside the point."
    m "{i}You’re{/i} not supposed to be asking questions like these. That is my job and you are stealing my personality."
    m "It’s disgusting. You should be ashamed. Please stop."
    s "Are you...afraid of being written off or something? Because that's not really my intention here."

    scene glowofthesun13
    with dissolve

    m "I'm..."

    "Maya seems to have a hard time answering the question as she trails off and focuses on a line of ants from one place to the next."
    "If she {i}is{/i} afraid of being left and that's why she doesn't want to speak up-"

    m "No."
    m "That’s not it."
    m "I’m just unsure about whether or not you bringing this up has any implications for the immediate future."
    s "What? How would a simple, pointless question like that be able to influence {i}anything{/i} to that extent?"
    m "Don't call it simple...and don't call it pointless. I don't want to hear that."
    m "What matters most is that this is a deviation from the way things are supposed to work."
    m "{i}You{/i} don't ask me questions like this. You just try to get me to like you and fail miserably."
    s "Well, would you prefer I just continue flirting with you instead?"
    m "I..."
    s "..."
    m "I don't really know..."

    "She pauses once more."
    "For a moment, I think I catch a glimpse of her lower lip trembling. But before I'm able to confirm anything, she speaks again."

    scene glowofthesun14
    with dissolve

    m "You’re changing."
    s "...What?"
    m "You’re changing."
    s "In...a good way? Or a bad way?"
    m "A way."
    s "So...can I take this as confirmation that you’re beginning to like me?"
    m "Is that really what you’re concerned about right now?"
    m "Aren’t there more pressing matters at hand?"
    s "More pressing than the affection of a cute shrine maiden? I doubt it."

    scene glowofthesun14r
    with dissolve

    m "Hah...Maybe I spoke too soon..."
    m "Maybe you aren’t changing after all."
    m "Yes...That has to be it."
    m "This was simply a fluke."
    m "An accidental deviation with no real meaning to it."
    s "Exactly. Like I said, I was just trying to say something that you-"
    s "Hey, wait a minute. Why do I feel like what you just said was kind of insulting?"
    m "I don't know. You started talking on your own without letting me finish."
    s "Well, what more did you have to say?"
    m "Not much."

    scene glowofthesun15
    with dissolve

    m "Just that everything is connected."
    m "Life and death..."
    m "Day and night..."
    m "Summer and winter..."
    s "You and me?"
    m "..."

    "I half-expect Maya to greet me with her token deadpan glare after that line but, instead...she focuses on the clouds passing overhead and lets out a sigh."

    m "Yeah..."
    m "You and me..."
    s "…"
    m "…"

    scene black
    with dissolve2

    "The clouds Maya was focusing on passed over the sun seconds later, blacking out the glow that had been dyeing her dress gold."
    "The conversation did not pick up again after that."
    "She just kept looking up-"
    "Even after the light had gone away."
    "…"
    "I left her in her secret hiding place and walked away from the shrine."
    "I'm not sure how long it took for her to notice."

    $ renpy.end_replay()
    $ shrine15 = True
    $ maya_love += 1
    $ connect = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine20:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
...
```