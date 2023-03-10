# Caught in the Vortex (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 25

* Event [A Place Like This](./streets25.md) (Yumi) is completed)



## Next events

None

## Event properties

* Id: yumidorm25
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm
* Triggered by path: yumidorm->yumidorm25

## Official wiki page

[Caught in the Vortex](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm25&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm25:
    play sound "knock.mp3"
    stop music fadeout 15.0

    "…"
    "I knock on Yumi’s dorm and wait to see if she’ll answer."
    "I haven’t stopped by her room since the incident with her mother, so I’m not really sure if she’s feeling embarrassed or down about it."

    y "Yeah? What do you want?"
    s "It’s me. "
    y "I know who it is, numnuts. You knock louder than anyone."
    s "Well, can I come in?"
    y "Now? No. I’m trying to sleep."
    s "But your light is on. I can see it through the bottom of the door."

    "To be honest, no I can’t. But Yumi doesn’t know that, so I’m calling her bluff."

    y "Stop peeking into my room, you creep! What if I like sleeping with the light on?! Is that a fucking problem?"
    s "Yumi, just let me in. I don’t want to stand out here all night."
    y "Oh my fucking god. Fine."
    y "Just come in. The door is open."

    scene black
    with dissolve
    play sound "dooropen.mp3"
    play music "love.mp3"

    "I make my way into Yumi’s dorm, kicking over a plastic bag of empty water bottles she’d placed directly in front of the door for some reason."

    scene yumidormtwofive1
    with dissolve

    y "You know you’re picking those up, right?"
    s "Of course I do..."

    "Not being an absolute heathen, I begin to pick up the bottles that have since gone rolling across the floor...even if it’s Yumi’s fault that I knocked them over in the first place."

    s "Did you actually try cleaning your half of the room for once? "
    y "So what if I did? I’ve gotta make more fucking room somehow."
    s "It might be worth not putting your garbage directly in front of the door next time, though."
    y "It might be worth checking your surroundings before you come waltzing in like you own the place."
    s "That aside, how are things?"

    scene yumidormtwofive2
    with dissolve

    y "Oh, please tell me you didn’t come all the way here just to ask me how my day went."
    y "It was shit, just like every other day. Thanks for asking. Now leave."
    s "I’m not leaving yet. There’s something I’ve been wanting to talk to you about, and I didn’t really get a chance when we went to the ramen shop."

    scene yumidormtwofive3
    with dissolve

    y "And have you considered if I actually {i}want{/i} to talk about that? "
    y "If it's about my mom, I’m pretty sure that I made it very clear I want nothing to do with her when I stormed out of the place."
    y "But hey, the job hunt needs to continue now I guess...So you can keep pretending you care about me for a little while longer."

    "I finish picking up the bottles and toss the bag {i}next{/i} to the door- not in front of it like an absolute monster."

    s "Well, I’m not going to force you to talk about anything. But I do think it might be good for you if you got some of it off your chest. "
    s "Does Chika know about your situation at least?"

    scene yumidormtwofive4
    with dissolve

    y "Of course she knows. She’s my best friend."
    y "You’re just some dude trying to get into my pants. And you can’t make that stupid skirt joke again because I actually {i}am{/i} wearing pants this time."
    s "Correct me if I’m wrong here, but I’m pretty sure the only time I’ve ever seen you smile is when I made that joke."

    scene yumidormtwofive5
    with dissolve

    y "I told you to never fucking mention that again!"
    s "You brought it up. I’m just trying to add to the conversation."

    scene yumidormtwofive6
    with dissolve

    y "If you want to add to the conversation, bring up something that actually matters."
    s "You mean like your mom?"

    scene yumidormtwofive5
    with dissolve

    y "No! Not like my fucking mom!"
    y "And another thing! Why the fuck do you know her? How does that even happen?"
    s "The day that you and I were {i}supposed{/i} to have dinner at the ramen shop, she came out of the bathroom and tried consoling me."
    s "I’m pretty sure she thinks we’re dating."

    scene yumidormtwofive7
    with dissolve

    y "Why the fuck would she think that?! That’s disgusting!"

    if bonus == True:
        s "I’m pretty sure she also accused me of, and these are not my words- {i}putting it in the wrong hole.{/i}"
    else:
        s "I don't know. Maybe we sounded like a good couple?"

    scene yumidormtwofive8
    with dissolve

    y "Okay, time to leave. Get the fuck out and please never say another word to me ever again."

    "Yumi tries to push me out of the room, but suddenly stops when I say this-"

    s "She talked about you, too, you know."

    scene yumidormtwofive9
    with dissolve

    y "…"
    y "Can’t imagine it was anything good."
    y "I don’t even remember the last time I saw her."
    y "She ran out a long fuckin’ time ago. Real shit mom, if you ask me."
    s "Well, she didn’t say anything {i}bad{/i} at least..."

    "Though, to be honest, I can’t remember her saying anything good either."
    "I’m pretty sure our talk was about something like kids just wanting to do their own thing at the end of the day, which is abundantly true in Yumi’s case."

    y "Of course she doesn't have anything bad to say. She barely ever saw me."
    y "Surprised she even remembers my face. "
    s "Like you said, you two have the same eyes."

    scene yumidormtwofive10
    with dissolve

    y "You literally didn’t even notice that until I pointed it out."
    s "Yeah, that’s why I said they were your words. I’m just trying to figure out what’s going on between you two."
    y "Nothing, obviously. "

    scene yumidormtwofive11
    with dissolve

    y "And now the one fuckin’ place I probably had an actual shot at turned me away."
    s "Did you use the noodle strategy?"

    scene yumidormtwofive5
    with dissolve

    y "Yes! I used the stupid fucking noodle strategy!"
    y "And it actually worked until my fucking MOM walked in with my TEACHER!"

    scene yumidormtwofive10
    with dissolve

    if bonus == True:
        y "Least I don’t have to worry about you fucking {i}her{/i} since she’d kick your ass if you ever tried to pull that shit."
    else:
        y "Least I don’t have to worry about you hugging {i}her{/i} since she’d kick your ass if you ever tried to pull that shit."

    s "Yeah, she probably would. I won’t deny that."
    s "She’s a rather...intimidating woman. "

    scene yumidormtwofive11
    with dissolve

    y "Yeah, being a Yakuza-wife will do that to you."
    s "...I’m sorry?"

    scene yumidormtwofive12
    with fade

    "Yumi sighs heavily and moves to her bed, resigning herself to the fact that this is going to be a thing that we talk about."

    y "Oh, come on. Don’t act like you don’t fucking know."
    s "I really don’t, though. Don’t the Yakuza dress a little less...spiky? "
    s "She seemed like more a biker-gang sort of girl."

    scene yumidormtwofive13
    with dissolve

    y "Well since you’re so fucking curious about my mom all of a sudden, how about I give you a little rundown of her life?"
    y "She dropped out of [high_school], joined a biker gang, met my dad, had me, left both of us, and now she apparently likes ramen."
    y "The end. That’s the life of my mom."
    y "Oh, and also, throw a few years of drug abuse into the mix as well. Really great role model."

    "Suddenly, Yumi’s attitude begins to make a little more sense."
    "I always knew there was something going on in the background with her but...I didn’t realize how intense it was."

    y "Any fucking questions?"
    s "Yeah."
    s "Was it hard?"

    scene yumidormtwofive14
    with dissolve

    y "Which part?! The one where my mom left me or the one where my dad is in the Yakuza?!"
    y "Actually, don’t even answer that! Because the answer is obviously yes!"

    scene yumidormtwofive15
    with dissolve

    y "And you know what the craziest part is? I’d be fucking {i}fine{/i} if I decided to follow in either of their footsteps. "
    y "Sure, there’d be a chance of me gettin’ addicted to crack or cocaine or whatever the fuck she was doing when I was growing up, but at least I’d have a place to belong."
    y "But nope. All I do is sell TVs and crash at my friend’s place, freeloading off of her because I don’t know what else there is to fuckin’ do in Kumon-mi."

    scene yumidormtwofive16
    with dissolve

    y "And like...why the fuck am I even telling you any of this? Not like you can do anything to change it."
    y "Just the bullshit circumstances I was born into. "
    s "It’s probably because you want to vent."
    y "Probably. I just...never thought I’d fucking see her again. "
    y "But I guess it makes sense that I did."
    y "Someone like her has no way of escaping a place like this. "
    s "Technically, no one has a way of escaping a place like this."

    scene yumidormtwofive17
    with dissolve

    y "Yeah, but that’s a new thing. I meant before."
    y "When she ran out, she could have gone fucking anywhere."
    y "But no. She’s still here."
    y "There’s something about this fucking city that just sucks people in and never lets them out. "
    y "And if there’s anything I got from her, it’s the fact that I’ve also just decided it’s okay to be caught in the vortex."

    scene yumidormtwofive18
    with dissolve

    y "Oh good, and now I’m about to cry. Knew this would happen as soon as I started ranting."
    s "Go ahead and cry if you want."
    s "I’m the only one here right now. I’m not going to tell anyone."

    scene yumidormtwofive19
    with dissolve

    y "Stop fucking being nice to me! It doesn’t help!"
    y "Call me a fucking bitch or something!"

    if bonus == True:
        y "Tell me I’m a kid and I need to fucking get over it!"
        y "{i}That{/i} is the shit that helps! Not all this fake-ass compassion that you’ve conveniently decided to save for the moments when I feel like complete garbage."

    "Part of me wants to do exactly what she’s telling me to."

    if bonus == True:
        "The truth is that she {i}is{/i} just a kid and that this is something she needs to get over."

    "There’s no time to cry over things like family or the circumstances we grew up with."
    "Doing that will just hold us back."

    if bonus == True:
        "But something about seeing cute girls cry just makes me want to {s}destroy{/s} protect them."
        "And I need to {s}ravage{/s} be nice to her or I might wind up seeing her break right in front of my eyes."

    scene yumidormtwofive20
    with dissolve

    y "God fucking damnit. Say {i}something{/i} at least so I don’t feel like a fucking moron sitting here talking to myself."
    s "How about we just talk about the next step in the Yumi Revitalization Project instead?"

    scene yumidormtwofive21
    with dissolve

    y "So what?...You’re just going to ignore the fact that I was crying in front of you?"
    s "Were you? I didn’t even notice."
    y "Oh, please. You don’t have to pretend you didn’t see it."
    s "See what? I really don’t have any idea what you’re talking about."
    s "We had a conversation about your mom. I found out about how shitty your background is. And then we started brainstorming ways to fix it."
    s "That’s all that happened here tonight."

    scene yumidormtwofive22
    with dissolve

    y "Oh. Uhh..."
    y "Cool."
    y "..."
    y "Thanks. "
    s "For what?"
    y "For letting me rant and...not rubbing my weakness in my face."
    y "It literally kills me inside to say this, but I respect that."
    y "Even if you’re a spineless pig."
    s "Why do you always have to ruin the sweetest moments between us by insulting me?"
    y "Why do you have to be so fucking...insultable?"
    s "Fair point."
    s "Let’s just figure out our next course of action and...save your family issues for another time."
    y "Or never. Preferably never."
    y "The further I am from them, the better."
    y "Gotta...carve out my own path or whatever other inspirational bullshit {i}normal{/i} teachers tell their students."
    s "Yeah. Those definitely wouldn’t be my words."

    if bonus == True:
        s "Mine would be a lot more controversial."
        s "And mildly sexual."
        y "Yes, because you’re a fucking creep."
        y "Now...let’s think of some more fucking options. Please."

    scene black
    with dissolve2

    "Despite our best efforts, Yumi and I aren’t really able to think of anything."
    "Instead, we go for a walk to the convenience store and I wind up buying her a few cups of instant noodles that she can ration throughout the week."
    "Or whenever she wants."
    "Frankly, it doesn’t matter to me."
    "We split apart on the way back to the dorm and go our separate ways. "
    "The entire walk home, I can’t help but try to wrap my head around Yumi’s situation."
    "As horrible as it may be, it still doesn’t excuse the way she acts, though."
    "But it at least helps me understand it."
    "At the end of the day, I’m just glad I was finally able to learn something about her."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ yumidorm25 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm30:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
    elif yumi_love >= 5 and streets10 == False:
        play sound "knock.mp3"

        s "Hey Yumi, are you in there?"
        "..."
        "There's no answer."
        jump doorknock
    if yumi_love >= 15 and yumidorm10 == True and cafe20 == True and yumidorm15 == False:
        jump yumidorm15
    if yumi_love >= 20 and streets20 == True and yumidorm20 == False:
        jump yumidorm20
    if yumi_love >= 25 and streets25 == True and yumidorm25 == False:
        jump yumidorm25
...
```