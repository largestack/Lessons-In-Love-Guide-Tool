# Nonetheless, I'm Here (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 0

* Event [Caterpillar](./day247.md) (Main) is completed)



## Next events

* [Io: The Girl with the Dragon Tattoo](./bathhouse5.md)

## Event properties

* Id: bathhouse1
* Group: Io
* Triggered by label: bathhouse
* Triggered by branch label: bathhouse
* Triggered by path: bathhouse->bathhouse1

## Official wiki page

[Nonetheless, I'm Here](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bathhouse1&go=Go) for more details.

## Event code

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse1:
    scene firstbath1
    with dissolve
    play music "io.mp3"

    "It’s the middle of the day and yet I find myself in the bathhouse."
    "Normally (And I use the word “normally” lightly since coming here in general isn’t exactly something I’d typically do)-"
    "Normally, I’d wait for it to be dark out. "
    "I mean, taking a bath in the afternoon is kind of pointless."
    "Isn’t it?"
    "Sure, there’s always the possibility of coming somewhere like this to relax-"
    "But something about having to pay to get naked and sit in a giant, wet rectangle while cold winter air attacks my skin doesn’t scream “relaxing.”"
    "It does scream, though."
    "Just not a noise I’m able to discern."
    "But-"
    "Nonetheless, I’m here."

    i "Welcome in. You can pay up here before-"
    i "Oh."
    i "Sensei. It’s you."

    scene firstbath2
    with dissolve

    s "Hey. How’s work going?"
    i "Fine, I guess."
    i "You’re here early. "
    i "And alone."
    i "Trying to kill time or something?"
    s "Or something, yeah."

    if bonus == True:
        i "Well, the discount I talked about is still on the table if you want it."
        i "You’re a few hours early for the peep-show, though. No Uta until at least 8:00 tonight."
        s "So I can’t come here to hang out with you?"
    else:
        s "Am I not allowed to come here to hang out with you?"

    scene firstbath3
    with dissolve

    i "I mean, you {i}can{/i} if you want. It just doesn’t seem like it would be very exciting to spend your afternoon off in a place like this."

    if bonus == True:
        i "Unless you’re just trying to sneak a peek at anyone else weird enough to come at this time of day."
        i "If that’s the case, this is exactly where you’d want to be."
        i "Just try to be discreet about it, though. I’ve got a crowbar under the counter and I’ve been given the okay to break it out if anyone gets weird."
        s "A - That’s very intimidating."
        s "B - Why even have a co-ed changing room if you’re worried about things like that?"
    else:
        s "I see nothing unexciting about good personal hygiene."
        s "Personally, I don't understand why there isn't more privacy in a place like this."
        s "I would be willing to invest if the issue is a financial one."
        i "It is not."
        s "Then why? Why must you create such an unsafe business?"

    scene firstbath4
    with dissolve

    i "My aunt’s idea. "
    i "We were actually thinking of just getting rid of the male section entirely and making this an all-female bathhouse after the war started."
    i "But we’ve got a fair share of customers who cherish their privacy and rent out the men’s side for themselves."
    s "Guilty as charged."

    if bonus == True:
        s "That was all Ayane’s idea, though."
    else:
        s "I am very rich."

    scene firstbath5
    with dissolve

    i "I’m not just talking about you."
    i "We’ve got several pairs of regulars who do the same exact thing a few times a week."

    if bonus == True:
        i "Most of them don't have the same sort of age gap you two have, but still."

    i "You’d be surprised by how many people prefer their privacy here."
    i "Could be body image issues, couples looking for alone time, sports teams wanting a communal place to wind down after a game-"
    i "Or green-haired, blue-eyed [teens] who thrive in empty spaces."
    s "...I’m not disturbing you, am I?"
    i "Sorry, that clearly didn’t come out the way I wanted it to."
    i "You’re fine."
    i "I already told you that I’m starting to like the time we spend together, even if the vast majority of it is me cryptically hinting at my backstory."
    s "Why be cryptic at all? Why not just tell me?"

    scene firstbath6
    with dissolve

    i "Tell you what?"
    i "What part do you want to know, exactly?"
    s "Well, you hate secrets, don’t you? "
    i "They’re the worst. "
    s "Just...tell me one of those, then. "
    i "Mm...I don’t think I can."
    i "Secrets are exhausting but it’s not like they don’t exist for a reason."
    i "For example, even though I keep saying stuff about how I like being around you, don’t you think there are a few things you could say that would change that?"
    i "Something you’re not proud of?"
    i "Something I couldn’t possibly understand?"

    if amifingered == True:
        play sound "static.mp3"
        scene amisfirsttime34
        with flash
        scene firstbath6
        with flash
        stop sound
    else:
        play sound "static.mp3"
        scene amidormten12
        with flash
        scene firstbath6
        with flash
        stop sound

    i "I’m just a [young_girl] after all."
    i "There are plenty of things I don’t know, even if I like to pretend there aren’t."

    scene firstbath7
    with dissolve

    i "Wanna trade?"
    i "You try to make me hate you and I try to make you hate me?"
    s "..."
    s "I’m not looking to make any enemies today, so how about you just tell me how you wound up in a place like this?"

    scene firstbath8
    with dissolve

    i "Heh. Weirdly enough, that’s probably one of the hardest questions you could ask me."
    i "Want to accept my prepared, cop-out answer instead?"
    s "Sure. Hit me."

    scene firstbath9
    with dissolve

    i "I woke up and walked here. The end."
    s "I feel like you could have done a little better if that was an actual {i}prepared{/i} remark."
    i "Could have, yes. But I didn’t. So you’ve gotta take what you can get."

    "“I walked here” really is a cop-out answer. She wasn’t kidding."
    "But it’s not like I expect her to spill her guts out on the floor in front of me when our relationship is still just getting started."
    "I get the feeling that whatever is happening here is going to take a long time to unravel."
    "I’m sure you’ve heard by now that if you were to remove your intestines and stretch them out across the floor, you’d wind up with around fifteen feet worth of organs, right?"
    "So, even if she {i}were{/i} to spill her guts out, it would take an astounding amount of work on my end to fully uncover them."
    "And sure, “astounding” may sound like a stretch given that it’s only fifteen feet-"
    "But fifteen feet is a long way to go in a number of ways."
    "That’s three whole Io’s."
    "I guess what I’m really trying to say is that it’s possible to spill your guts out and still only give someone a fraction of what’s really there."
    "In order to fully understand anything, you need to get your hands dirty. "
    "Feel those intestines slipping between your fingers-"
    "Memorize each and every groove-"
    "And then put them back together...and shove them back inside so whoever gave them to you can eat or drink once more."
    "Praise be."

    scene firstbath10
    with dissolve

    i "It’s not a bad place, though, this bathhouse."
    i "The fridge upstairs is always stocked with food, the bed is warm, and no one bothers me other than Uta whenever she has some spare time to herself."
    i "I think I may have even called it home on several occasions."
    i "I never mean to when it happens. I {i}am{/i} just a visitor after all."
    s "Same here."

    scene firstbath7
    with dissolve

    i "You also don’t feel at-home where you live, Sensei?"
    s "I’m starting to, I think."
    s "But I definitely don’t think this place was made for me."
    i "This “place” probably wasn’t made for anyone."
    i "When I called myself a visitor, I was doing it in more of a “This is just my aunt’s home” sort of way. But yeah, I guess it parallels how I am...or how {i}we are{/i} as a whole."
    s "You remind me a lot of one of the other girls in class when you say things like that."
    i "I think I’m supposed to ask which one but, honestly, I really don’t care."
    i "If whoever you’re talking about sounds the same as me during a time like this, I can’t imagine she’d like discovering our apparent connection either."
    i "You don’t develop this kinda mindset by just watching TV and listening to music, you know?"
    i "You’ve gotta see stuff. {i}Feel{/i} stuff."
    i "And then you’ve gotta figure out how to lock it all away so no one can discern your vulnerabilities."
    i "Chances are, whoever that girl is, she's remarkably unhappy."

    scene firstbath10
    with dissolve

    i "Haha~ This is fun!"
    i "I don’t normally get to talk about stuff like this! Let alone while I’m working."
    i "And I’m pretty sure Uta isn’t mature enough to handle these kinds of discussions yet, so I’m glad I can keep up with you."
    s "To be fair, you’re the one doing most of the talking so, from my perspective, it feels more like I’m trying to keep up with you."

    scene firstbath11
    with dissolve

    i "Maybe we’re trying to keep up with each other?"
    i "Like...we’re both on treadmills facing one another and no matter how quickly we run to meet up, the belt-speed just gets faster."

    scene firstbath12
    with dissolve

    i "It’s fucking torturous. Isn’t it?"
    i "You just want to make it to the goal line and you can’t because life is a cruel bitch and keeps figuring out ways to push you back."
    i "I fucking hate it, Sensei. I hate all of it."

    scene firstbath13
    with dissolve

    i "But I guess that line of thinking is self-destructive."
    i "And I guess I actually really want you to like me after all."
    i "So I guess I’ll stop being immature for the next few minutes."
    s "You seem to be doing a lot of guessing right now."

    scene firstbath14
    with dissolve

    i "Always am. Just the way I’ve become, I suppose."
    i "Second guessing even the most obvious answers."
    s "Well, whatever the case, you’re free to be as self-destructive as you want."
    s "Just don’t hold it against me if I can’t help you when you need me most."
    s "I have an admittedly hard time resolving things."
    i "And I have an admittedly hard time accepting help, so that’s probably good for both of us."
    i "As long as we can keep talking like this, I’m pretty sure I can keep the treadmill running."
    i "It would hurt like hell falling off and getting thrown across the room, so I’ll definitely avoid that any way I can."

    scene firstbath6
    with dissolve

    i "As far as the bathhouse goes, though, I really {i}did{/i} just wake up and walk here."
    i "Just not in the way you might be expecting."
    s "Wait, what?"

    scene firstbath15
    with dissolve

    i "Hehehe~ Nothing! Just ignore that."
    i "Just a little metaphor I thought up on the spot so my cop-out answer would become less...cop-outy. "
    s "…"

    "I break out my hidden dictionary of metaphors and try to figure out what Io means by that."
    "I give up somewhere near page 23 and stop attempting to decode what a confusing girl like her could possibly be thinking."
    "I settle on something close to “turning over a new leaf” and don’t bother digging any deeper."
    "Sometimes, what’s buried beneath the surface isn’t worth uncovering."
    "This could very well be one of those cases."

    s "Well, as long as you keep coming here, I’ll keep coming here as well."

    scene firstbath14
    with dissolve

    i "Wanna apply for a part time job? I could show you how to scrub the floors."
    i "We could use a few more hands around here, anyway."
    s "As much as I’d love to...scrub floors...my current job already takes up most of my time."
    i "You sure? Cause you’d get an employee discount that would stack on top of the one I already gave you and you’d basically get to bathe for free at that point."
    s "I can already bathe for free at that place called “home.”"

    scene firstbath16
    with dissolve

    i "Sorry, Sensei, but we’re not all fortunate enough to have one of those."
    i "Luckily, I’ve got the dorm now. And that’s starting to feel like one, slowly but surely."
    i "Even if no one wants to talk to me and I don’t want to talk to any of them."
    i "It’s a place I can lay my head and fall asleep without the worry of burdening anyone."
    i "A worry that I probably shouldn’t have somewhere like this, but that I still can’t seem to shake."
    i "Nonetheless, I’m here."
    i "Surrounded by bathwater and body scrubs."
    i "Making the best of what I have-"
    i "Even if that is absolutely nothing."

    scene black
    with dissolve2

    "Io and I talk for a little while longer."
    "It’s hard to tell when it becomes dark due to the blacked out windows but, at some point, it does."
    "And that part arrives just before I realize I’ve spent far too much time here and decide to head back outside and find something else to do."
    "As I leave, Io smiles."
    "I don’t know whether or not the smile sticks around the second I make it outside."

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse1 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label bathhouse5:
...
```

## Code that triggers this event

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse:
    if io_love >= 0 and day247 == True and bathhouse1 == False:
        jump bathhouse1
...
```