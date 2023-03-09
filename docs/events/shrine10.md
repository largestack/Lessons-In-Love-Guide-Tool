# Past/Present/Future
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine10&go=Go)



## Event preconditions
✅Maya love greater than or equal to 10



## Next events
* [Maya: You and Me](./shrine15.md)

## Event properties
* ID: shrine10
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label shrine10:
    scene shrine_noon
    with dissolve
    play music "hammockofpeace.mp3"

    "I have to stop and catch my breath after finally reaching the top of the shrine's stairs which, and I know this will sound crazy, seem to multiply each time I come here."
    "Perhaps it's due to the fact that it's been getting hotter every day lately..."
    "But it's gotten to the point where the stairs themselves are more of a barrier to me coming here than Maya's incessant commands to distance myself from her."
    "I like Kumon-mi. I mean, why wouldn't I when it seems like everything here was planted with me in mind?"
    "But this weather needs to stop."
    "The fact that I don’t see anyone else around is a testament to that."
    "I guess they all decided it was better to relish in the comfort of their air conditioned apartments than to venture forth to this inglorious hellscape."
    "But here I am once again at the house of {i}God,{/i} searching for who I imagine is His/Her/Its most reluctant servant."

    scene mayasit1
    with fade

    "Fortunately, I don't have to search for long."
    "It seems that this heat has managed to get to Maya as well as she takes shelter in the shade provided by the shrine."

    s "Hey. There wouldn't happen to be a room with air conditioning over here, would there?"
    m "…"

    "Maya doesn’t answer. She simply sits there, unflinching and unbothered by my sudden appearance."
    "Though, perhaps it's not right to really call it {i}sudden{/i} anymore when visiting her is something that's becoming more and more normal with each passing day."
    "The lights behind her attempt to contest the sun in terms of brightness but do nothing more than distract me from what I really want to look at right now."
    "I suppose that might be the point, though. Especially given that Maya has yet to respond to me."

    s "You’re not asleep, are you?"

    scene mayasit2
    with dissolve

    "Slowly, her eyes open and make contact with mine."

    m "Asleep...Awake...Is there really any difference?"
    s "Yes."
    m "I thought that if I ignored your existence entirely, you might go away."
    m "I regret to see that is not the case."
    s "Well, I apologize for letting you down."

    scene mayasit1
    with dissolve

    m "Please sit if you are going to speak with me."
    m "You are obnoxiously tall and I do not want to put any unnecessary strain on my neck."
    s "Sure...but only since you asked so nicely."

    "I take a seat in front of Maya and observe her posture."
    "She sits in perfect seiza position and I can't help but be impressed by how much repetition and muscle reconfiguration it must have taken to make her look like such a statue."
    "I am unable to mimic her, so I simply take my place in a more comfortable position on the floor and hope that I am able to dodge the wrath of God."

    m "You’re thinking something strange, aren’t you?"
    s "Two things, actually. One you'd probably be interested in and one you wouldn't."
    m "You don't intend to tell me the more interesting one, do you?"
    s "Nah. I figure you'll go off on your own tangent soon enough and I don't want to give you any openings."
    m "Is the thought I wouldn't be interested in as vile and objectifying as I expect it to be?"
    s "Do you actually want to know that? Or are you just being sarcastic and confrontational again?"

    scene mayasit2
    with dissolve

    m "I wonder."
    s "I was just admiring how proper you look. That’s all."
    m "I see."
    m "That’s all? Because that seems excessively normal by your standards."
    s "I’ll let you know if anything else comes up."

    scene mayasit1
    with dissolve

    m "Please don't. There is only so much I can take when it comes to the prying eyes of an older man."
    s "Why do you always have to be so hostile toward me?"

    scene mayasit2
    with dissolve

    m "Why do you ask?"
    s "Because I don't get it. I feel like I could say absolutely nothing to you and you'd still do everything in your power to get me to leave."
    m "I likely would. The thought of you standing there in silence while I sit with my eyes closed disturbs me greatly."
    s "I'm not here to {i}disturb{/i} you, Maya."
    m "I have a hard time believing that based on your...persistence."
    s "You realize there are plenty of other girls who would envy this level of persistence from me, right?"
    m "Your tone has suddenly shifted. Have I offended you in some way?"
    s "I'm not {i}offended.{/i} You just...confuse me, I guess."
    m "And what exactly are you confused about?"
    s "Your...outlook on things. Why you think the way you do."
    m "Which {i}things{/i} are you referring to?"
    s "I don't know? Me...relationships...the world-"
    m "Which world?"
    s "Uhh...this world? The one we’re living in."
    s "The first time I came here, you spouted some ridiculous theory about how I’d been...reincarnated or something."
    s "That's not something a normal girl would just come up with off the top of her head, you know. How did you get like this?"
    m "Why are you pretending that was such a {i}ridiculous theory{/i} when we both know it's the truth?"
    m "What could hiding your existence from me, the only person who acknowledges and understands it, possibly do for you?"
    s "..."

    scene mayasit1
    with dissolve

    m "I see everything that you see."
    m "The past. The present. The future."
    m "Every second of it, filtered through a lens unfamiliar to you."
    m "Our sights and memories of the times we wake up and the times we go to sleep may not play in perfect harmony, but the ones we share in this very moment do."
    m "So focusing on what's happening now, while easy, will do absolutely nothing for either one of us in the grand scheme of things when we should be more worried about what happens {i}next.{/i}"

    scene mayasit2
    with dissolve

    m "Which gives me an excellent opportunity to harken back to what you asked when you first showed up today-"
    m "Whether I was awake or asleep."
    m "Does that really make a difference to you knowing what you know now?"
    s "What do I know now? Because nothing you just said makes any sense to me."

    scene mayasit4
    with dissolve

    m "That’s because you’re an idiot."
    s "Are you sure it's not because you're just a fucking weirdo?"
    m "Since you're apparently incapable of following along, perhaps I’ll put it in terms that even someone like {i}you{/i} can understand."

    scene mayasit3
    with dissolve

    m "The key to uncovering this world...or any world for that matter..."
    m "Is {i}perception.{/i}"
    m "There is no defining law of the universe...nor any written guide of what means what or who needs who."
    m "There is no {i}anything.{/i}"
    m "There can't be."
    m "And the reason for that is simple."
    m "Nothing is real."
    m "Well...at least not in the traditional sense."
    m "Technically, everything {i}is{/i} real. But only because that is the way we have decided things to be."
    s "What?"
    m "What I am saying is that this has all happened before...and it will happen again."
    m "Over and over and over. "
    m "Attempting to understand {i}why{/i} things are that way instead of just accepting them is nothing more than a waste of time."
    s "..."
    m "We all see different things...experience different things...yet we still somehow always wind up in the same exact place."
    m "As long as that happens, do the means of how we get there really make any difference?"
    s "What I really want to know is how you ended up {i}here.{/i} What happened to you that made you see life as just...some..."
    m "Predestined string of events, only mildly changing with each passing iteration?"
    s "Sure. That."
    s "Is there, like...some sort of trauma you're keeping locked away or something?"

    scene mayasit1
    with dissolve

    m "Is there anything more traumatic than simply being born?"
    s "Wow."

    scene mayasit2
    with dissolve

    m "I apologize. That was unnecessarily dark."
    m "And I’m sure it hits a bit close to home seeing as you were born {i}again{/i} not too long ago."
    s "{i}Or was I?{/i}"
    m "You were. That isn't even up for debate anymore."
    s "Fine, whatever. But if I'm some sort of...reincarnated soul, what does that make you? Some sort of spirit or something?"

    scene mayasit1
    with dissolve

    m "No."
    m "I am a normal [teenage]girl."
    m "We are but two normal people having a normal conversation on a normal day."
    m "What happened before this and what will happen after it is all part of a cycle."

    scene mayasit2
    with dissolve

    m "We will continue living the lives we have now until they come to their end."
    m "And when that happens, we will start over."
    m "You will meet me and I will meet you."
    m "You will visit me on days like today and discuss why I am the way I am while I keep you at arms length."
    m "You will do your best to learn more about me and I will do my best to ensure that never happens."
    m "It will continuously spiral, much like life itself...circling the drain before disappearing, only to return once things have been purified."
    m "The spiral will continue until you can't even close your eyes without seeing me."
    m "But I will never be any closer to you than an image you can conjure up at will."
    s "..."

    scene mayasit1
    with dissolve

    m "It’s the same for all people, not just you and I..."
    m "This is nothing more than an endlessly repeating string of events. And every single one will be wiped clean after a set amount of time."
    m "So, in order to avoid all of that, it’s best that we just live without thinking."
    m "It's best that we just go our respective ways, neglecting to hurt others as that will prevent us from being hurt in return."
    m "Doesn’t a life like that sound nice and simple?"
    m "Because that is the life I want to lead."
    m "And you are merely getting in the way of things by involving yourself with me."
    s "…"
    m "…"

    "The two of us sit there in silence for what feels like an eternity."
    "Part of me wants to come out and say that Maya’s thoughts on what this life is are...warped beyond recognition, but..."
    "I actually think I get it. Albeit in an incredibly roundabout way."
    "What I think she means is that there are people who live in the moment...and that there are people who live in the past or the future."
    "But Maya has somehow found a way to live in all three at once."
    "I'm sure my way of interpreting that is cutting out a great deal of...weird cosmic influence or whatever it is that's going on in her head-"
    "But I think I understand."
    "I just don't agree with her."
    "If this really is one big cycle where we all end up right back where we started, wouldn't we {i}want{/i} to try and shake things up?"
    "What good does peace bring us if it's not something that can be shared?"
    "And what's the point in avoiding hurting and being hurt if the recycling of those emotions makes it like we never hurt at all?"

    scene mayasit2
    with dissolve

    m "You’ve gone quiet. Could it be that you are finally deciding to leave me alone?"
    s "No. I'm going to annoy you forever."
    m "Oh, joy. Thank you so very much."
    s "Maya, if this really is one big cycle...what I decide to do right now won’t make much of a difference in the long run, right?"

    scene mayasit4
    with dissolve

    m "Is that really all you took from that? Because that's, like...the faintest trace of what I was trying to say."
    s "Get better at expressing yourself, then."
    m "I am plenty good at expressing myself. It's not my fault you're such an idiot who can't follow along."
    s "It's not that I can't follow along. I just-"
    m "Listen. It’s hot and I want to be left alone."
    m "So either you sit here in silence...or you go bother someone else. Okay?"

    scene mayasit1
    with dissolve

    m "I’ve already used up way too much energy by just speaking with you. I’m going to take a nap now and attempt to recover some of that."
    s "Are you really going to take a nap while sitting like that? That can't possibly be comfortable."
    m "…"
    s "…"
    m "…"
    s "…"
    m "…"
    s "…"
    s "Hah..."

    scene black
    with dissolve2

    "It’s hard for me to tell if Maya ever does fall asleep or not, given that her posture remains unmoving for the next thirty minutes."
    "Feeling bored and overheated, I eventually decide to head back into town."
    "I don't think Maya and I became closer today-"
    "But if any of what she said is true, I doubt it would change anything if we did."

    s "..."

    "I don't really want to think about that right now."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine10 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label shrine15:
...
```

## Code that triggers this event
File: \game\MayaEvents.rpy
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
...
```