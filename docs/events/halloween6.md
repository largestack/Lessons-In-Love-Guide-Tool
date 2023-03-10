# They're Just Lights (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Sexy Land](./halloween5.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween6
* Group: Main
* Triggered by label: halloween5
* Chain sources: halloween5
* Chain sources path: halloween5

## Official wiki page

[They're Just Lights](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween6&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween6:
    scene nightsky
    with dissolve2
    play music "blueair.mp3"

    "My footsteps lead me down a familiar path."
    "I walk and I walk and I walk-"
    "And I look up the entire time."
    "I see stars."
    "The thing about the stars, especially on nights like this, is that they make all of our theories almost float away in a sense."
    "It makes me think-"
    "If there are things this beautiful, anything is possible."
    "It defies logic. "
    "It defies reason."
    "Yet, I still believe it while my head is raised. "

    s "…"

    "These aren’t my thoughts."

    play sound "static.mp3"
    scene mayabeach1
    with flash
    scene nightsky
    with flash
    stop sound

    "These are someone else’s thoughts. "
    "Someone who likes stars much more than I do."
    "To be honest, I don’t really care for them at all."
    "Or at least, I don’t think I do."
    "Do I?"
    "Did I?"
    "How did the old Sensei feel about stars?"
    "And did he also have problems wrapping his head around the borderline nonsensical theories that come with them?"
    "How can stars be beautiful?"
    "They’re just lights."
    "Just splotches of brightness in an otherwise empty sky, getting in the way of where the true beauty lies."
    "Beauty is buried behind everything. "
    "And so we must filter and push our way through waves of shit in order to get to it."
    "That’s right."
    "The stars are shit."
    "These are my thoughts."
    "I’m sorry, Maya."

    scene yumihalloween1
    with dissolve

    "Oh."
    "That’s strange."
    "Amidst the sea of stars, I {i}do{/i} manage to find something beautiful."

    y "What...are you doing here?"
    s "I’m on my way to the bar. What are {i}you{/i} doing here?"
    s "And what are you wearing?"

    scene yumihalloween2
    with dissolve

    y "What, am I not allowed to wear something different once it gets colder?"
    y "It’s fucking freezing tonight. "
    s "It’s cold but it’s not {i}that{/i} cold."
    y "I’m not...good with cold weather. Makes my skin all tight and dry and shit."
    s "Your hair is different too."

    scene yumihalloween3
    with dissolve

    y "Jesus, can I not change anything about the way I fucking look without you commenting on it?!"
    y "Don’t you have somewhere to be?!"
    s "Sorry. I was just thinking that it fits you."

    scene yumihalloween4
    with dissolve

    y "Course it fuckin’ fits me. Ponytails are boyish or sporty or whatever and I basically just act like a fucking guy, so..."
    y "Sorry for not being out here in a fucking dress."
    s "You should dress like this more often, Yumi."
    y "Can’t. Gets too fuckin' hot sometimes and I'm not good with heat either."
    s "So if you’re not good with the cold or the heat, what are you good with?"

    scene yumihalloween5
    with dissolve

    y "My fists."
    y "Now beat it."
    s "Intimidating."
    s "Are you going to fight me?"
    y "Are you going to leave me alone?"
    s "Probably not now that I’ve run into you."

    "I take a step closer to Yumi and notice her move back on the bench as soon as I do."
    "She winces as the feeling of cold wood seeps through her clothing and comes into contact with her back."
    "I stop moving closer."
    "I can’t blame her for reacting that way given our...No, {i}my{/i} history."

    scene yumihalloween6
    with dissolve

    y "Do whatever you want. Not like you ever fuckin’ listen to me anyway."
    s "I won’t stay long. I have a party to get to."

    scene yumihalloween7
    with dissolve

    y "Party? What kind of person is so lonely that they would invite {i}you{/i} to a party?"
    s "Just a few people my age. No one you really know."

    if streets15 == True:
        "Well...technically, she’s met Haruka before. But I’m not about to bring up the cafe again when I already know how upset she was about not getting that job."

    scene yumihalloween8
    with dissolve

    if bonus == True:
        y "Hah. Yeah right. You hanging out with people your own age? I’m not falling for that."
    else:
        y "Hah. Yeah right. You hanging out with actual friends? I’m not falling for that."

    y "How fucking stupid do you think I am?"
    s "...No, I’m being serious."
    s "There won’t be a single [teenager] there."

    scene yumihalloween9
    with dissolve

    y "Holy shit, you actually {i}are{/i} being serious, aren’t you?"
    y "What the fuck is going on here? "
    s "I’m not as bad as you-"

    "I cut myself off when I realize that I {i}am{/i} as bad as she makes me out to be."
    "I need to stop saying things like that around Yumi."

    scene yumihalloween10
    with dissolve

    y "As bad as I {i}what{/i}?...Make you out to be?"
    y "Cause, yeah. You kind of are."
    s "And here I was hoping you wouldn’t have been able to finish that sentence."
    y "Well how else would it have fucking ended?"
    s "I don’t know. But at least I tried, right?"

    if bonus == True:
        y "Still, though. You and people your own age having a Halloween party? Don’t you think that’s a little out of character?"
        y "Shouldn’t you be at home sniffing your [niece]’s laundry or something?"
        s "I’ll have you know I have not done that even once. "
    else:
        y "Still, though. You and other {i}real{/i} people having a Halloween party? Don’t you think that’s a little out of character?"

    s "And what about you? Shouldn’t you be out with Chika trying on Halloween costumes or something?"

    scene yumihalloween11
    with dissolve

    y "I’m not going to wear a fucking Halloween costume. I’m not a kid anymore."
    s "And Chika is? "
    y "No, but Chika is a fucking popular-ass people-person and does {i}all{/i} of that trendy shit."
    y "Things like that aren’t meant for people like me."
    y "Besides, don’t even know what the fuck I’d dress up as in the first place."
    y "Everyone’s probably just going to look slutty as fuck anyway."

    "Based on how the two costumes I’ve seen so far have been a full suit of armor and a dolphin, I highly doubt that is going to be the case."

    s "Are you going to come to the party at least? "
    y "Are you?"
    s "I am."
    y "Then no, I’m good."
    s "Would you have gone if I told you I wasn’t going?"
    y "…"
    s "…"

    scene yumihalloween12
    with dissolve

    y "Probably not."
    y "I don’t see why it matters, though. "
    y "Chika would be the only one excited to see me there. Everyone else would probably just feel awkward or scared or some shit."
    s "Probably. But whose fault is that?"
    y "Oh, definitely mine. I won’t argue with that at all."
    y "But it’s not like just showing up and being all like, “Hey guys! Happy Halloween!” is going to change anyone’s opinion of me."
    y "I’ve made my bed and now I’ve gotta fuckin’ lay in it."
    s "Sure, but isn’t tomorrow also your birthday? Missing out on a party {i}and{/i} being alone for your birthday sounds pretty sad, I won’t lie."

    scene yumihalloween13
    with dissolve

    y "Wh-"
    y "Why do you know about my birthday?!"

    scene yumihalloween14
    with dissolve

    y "Did...Did Chika fucking tell you?! I’ll fucking kill her."
    s "What’s wrong with me knowing your birthday?"
    s "Afraid I’m going to throw a surprise party for you or something?"

    if bonus == True:
        y "No! I just don’t want you going home and thinking “Wow, I’m getting closer to Yumi! I know her birthday! Maybe she’ll suck me off soon!” or something."
    else:
        y "No! I just don’t want you going home and thinking “Wow, I’m getting closer to Yumi! I know her birthday! Maybe it's okay to hug now!” or something."

    s "How are those things connected at all?"

    scene yumihalloween15
    with dissolve

    y "Everything is connected, you fucking moron."
    y "If you learn something about someone, intentional or not, you’re going to wind up thinking that you’re getting closer to them."
    y "Then those thoughts fucking snowball and just roll all over any other thoughts you have until the ball gets so fuckin’ big that you feel like you’re a part of it."
    y "But I don’t wanna be a fuckin’ snowball and I don’t want you to think any more about me than you already do."
    y "Which is probably a lot because you’re a fucking creep."
    s "Do you think of {i}me{/i} often, Yumi?"

    scene yumihalloween16
    with dissolve

    y "Oh please. The second I start thinking about you for more than five seconds a day, I’m just going to kill myself."
    s "Afraid of the snowball effect?"

    scene yumihalloween3
    with dissolve

    y "So what if I am?!"
    y "Besides, birthdays are fucking stupid anyway. It’s not like it’s an actual holiday or anything."
    y "Not everyone wants to be the center of fucking attention. Some people just want to be left alone."
    s "And I’m assuming you’re one of those people?"

    scene yumihalloween16
    with dissolve

    y "Oh gee, I wonder what gave you that idea?"
    y "It’s not like I literally spend my entire life hiding away from everyone or anything."
    s "You don’t seem to ever hide away from Futaba."
    y "Kinda hard to when she’s the size of-"
    s "Yumi."

    scene yumihalloween17
    with dissolve

    y "…"

    "Yumi decides against finishing her sentence, and I doubt it's because I stopped her."
    "I’m not sure if she genuinely feels bad or if she’s just holding back because Futaba isn’t around, but I’m glad to see that she’s willing to at least try to contain herself now."

    y "Habit."
    y "My bad."
    s "Don’t apologize to me. Apologize to her."
    y "Nah. I don’t regret any of the shit I’ve said. I just shouldn’t say as much of it."
    y "I’d get mad as fuck if someone was always makin’ fun of me. "
    y "But then again, I also wouldn’t just let that shit fly. "
    y "I’d actually do something about it. And she never fucking does anything."
    y "But there’s no use in talkin’ about someone who ain’t around. "
    y "..."
    s "..."
    y "This party thing you’re going to-"
    y "Is it close to the dorms?"
    s "Not really. Why?"
    y "Just wondering."
    s "…"

    "She wasn’t planning on asking me to walk her back, was she?"

    s "Are you going to stay out here much longer, Yumi? It’s kind of late, isn’t it?"
    y "Kind of, I guess. I don’t know. Haven’t really thought about it."
    s "Why do you always seem to be out and about in the middle of the night?"

    scene yumihalloween5
    with dissolve

    y "I could ask you the same fucking question."
    y "I feel like I can’t go anywhere anymore without you bumping into me like it’s part of some fucking script or something."
    y "It’s like the fucking city itself keeps trying to force us together and not realizing that I hate your fucking guts."
    s "You think the city is somehow responsible for all of these chance encounters?"

    scene yumihalloween18
    with dissolve

    y "What else would it be?"
    y "God?"
    y "Fate?"
    y "Neither of those things are real."
    y "So saying that Kumon-fucking-mi is responsible is as good a guess as any."
    y "Whatever is responsible, though, I want it to stop."
    y "I miss all of the peace and quiet I used to get before you started getting all..."
    y "However you are now."
    s "What do you mean by that?"
    y "..."

    scene yumihalloween19
    with dissolve

    y "If I ask you something really fucking weird, will you promise not to laugh at me?"
    s "It really depends on how weird the question is."
    s "Any reason you suddenly want to ask?"
    y "Just...something I’ve been wondering."
    y "But on second thought, it would probably make me sound insane and I probably already look fucking weird being out here alone in the middle of the night."
    y "So never mind."
    s "Yumi, just ask-"

    scene yumihalloween20
    with dissolve

    y "Have you, like..."
    y "Lost...some of your memories or something?"
    s "…"
    y "…"

    scene black
    stop music

    "///////////////////////////////////////////////////////////////////////////////////////////////////////////"

    y "Um..."
    y "S-"
    y "Sensei?..."

    play music "sweetervermouth.mp3"
    play sound "static.mp3"
    scene tree3
    with flash

    "//////MULTIPLE ERRORS DETECTED IN TERMINAL 23"
    "//////RESET NECESSARY TO RESUME STANDARD OPERATIONS"
    "//////USER2 IS NOW CONTROLLING TERMINAL 23"
    "//////..."
    "//////..."
    "//////..."
    "//////USER2 LACKS THE PERMISSIONS NECESSARY TO RESET SYSTEM"
    "//////PLEASE ENSURE ALL WIRES ARE PROPERLY CONNECTED BEFORE TRYING AGAIN"
    "//////..."
    "//////..."
    "//////..."
    "//////USER2 LACKS THE PERMISSIONS NECESSARY TO RESET SYSTEM"
    "//////TERMINAL 23 IS NOW LOCKED"
    "//////CONTACT ADMINISTRATOR FOR ADDITIONAL ASSISTANCE"
    "//////TERMINATING CURRENT PROCESS AND REROUTING TO THE NEXT AVAILABLE PATH"

    $ renpy.end_replay()
    $ halloween6 = True
    stop music

label halloween7:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```