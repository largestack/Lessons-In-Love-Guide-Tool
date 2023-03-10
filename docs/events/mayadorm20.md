# Close Your Eyes (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 20

* Event [Nothing is Real](./shrine20.md) (Maya) is completed)

* Event [Yumi Revitalization Project](./yumidorm10.md) (Yumi) is completed)



## Next events

* [Maya: Watermelons and Violin](./shrine25.md)

## Event properties

* Id: mayadorm20
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm
* Triggered by path: mayadorm->mayadorm20

## Official wiki page

[Close Your Eyes](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm20&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm20:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Maya’s door and wait for her to respond."

    m "Ah, right on time."
    m "Please hold on."
    s "Uhh...okay. But what exactly am I holding on for?..."

    "I hear Maya sifting through a few things in her room before making her way to the door."

    play sound "dooropen.mp3"
    scene firstmayadorm1
    with fade

    m "It’s less of a matter of you holding {i}on{/i} and more of a matter of you just...holding in general."
    m "Here, take this."

    scene firstmayadorm3
    with dissolve

    "Maya hands me a rather curious box and I’m suddenly stricken with intense deja vu."

    s "What is this?"
    m "Heavy. That’s why you’re holding it."
    s "No, I mean...in general."
    s "This isn’t the first time you’ve made me carry a random box in the middle of the night and...that's a strange thing to have a person do multiple times."
    m "And?"
    s "And I was wondering if you’d tell me what’s in it this time."
    m "Why would I do that?"
    s "Because we’re best friends?"

    scene firstmayadorm4
    with dissolve

    m "Ew. Don’t even joke about that."
    m "If you’re going to gross me out, I’d rather just carry the box there myself."
    s "All I did was say we’re best friends. It’s not like I was hitting on you."
    m "Saying we’re best friends is somehow even worse than hitting on me."
    s "How?"
    m "I don’t know, it just is. Stop it."
    s "So, are we going to the[school] again?"

    scene firstmayadorm3
    with dissolve

    m "Yes. Is that a problem?"
    s "Yes. But only because I have no idea what I'm bringing there."
    m "You’ll find out eventually. "
    m "I can’t guarantee you’ll be thrilled when you do, though. The answer isn't particularly {i}exciting.{/i}"
    s "Maya, if there is a watermelon inside of this box, I am going to be very mad."
    m "Why on earth would I ever bring a watermelon {i}away{/i} from me? That doesn't make any sense at all."
    m "Your theory is stupid and full of holes."
    s "Just tell me what's inside."
    m "Why do you even want to know?"
    s "You can’t write “Don’t Open” on a box and expect me to not ask things like this."
    s "In fact, pretty much any time there’s a sign telling me {i}not{/i} to do something, I feel compelled to act against it."
    m "I see."
    m "Question: If I start wearing a shirt that says “Please get to know me” on it, will you finally leave me alone?"
    s "You know, at that point, I think I might have to. That’s an admirable amount of dedication."
    m "I’ll place an order tonight."
    m "Thank you for letting me know beforehand. It was nice knowing you."
    m "Actually, nevermind. No it wasn’t."
    s "…"
    m "…"
    s "Can we just take this thing to the[school] now?"
    m "I thought you’d never ask."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Maya and I make our way through the dimly lit streets toward the[school]."
    "We don’t see anyone else along the way, which is mildly confusing given that it isn’t {i}that{/i} late yet."
    "But that’s fine, I guess."
    "Strange things typically seem to happen when I’m with Maya, and a lack of pedestrians isn’t really anywhere near the top of that list."
    "………"
    "……"

    play sound "slidedoor.mp3"
    "…"

    scene mayanightschool1
    with dissolve2

    "Maya finishes what she came here to do rather quickly."
    "She comes out of the classroom and moves directly over to the window, not paying any mind to me."
    "Meanwhile, I’m still trying to figure out exactly what is going on."
    "What’s so important about delivering a box to[school] in the middle of the night?"
    "And why does she need my help in order to do it?"
    "Also...why does she treat this like it’s a completely normal thing when it doesn't make any sense whatsoever?"

    play music "blueair.mp3"

    m "Because it {i}is{/i} completely normal."
    s "...What?"

    scene mayanightschool2
    with dissolve

    m "You were wondering why I don't see any issue with having you deliver various boxes to school in the middle of the night, weren’t you?"
    s "Yeah, but...how did you know that?"
    m "You’re easy to read."
    m "I know you much better than you think I do."
    m "Though, a lot of that is due to how simple-minded and annoying you are."
    s "I don’t really think the {i}annoying{/i} part was necessary or relevant there, but I guess I kind of get it when it comes to the simple-minded part."
    s "It’s true that my train of thought isn't exactly packed to the brim with passengers."
    s "{i}You{/i} on the other hand..."

    scene mayanightschool1
    with dissolve

    m "Yes. I’m frustratingly hard to read, I know."
    m "So much so that it eats you up inside."
    m "You wish you could tear the thoughts directly out of my head, don’t you?"
    s "I think that, more than anything, I want you to {i}tell{/i} me about them."

    scene mayanightschool3
    with dissolve

    m "Oh?..."
    m "What a rare response."
    s "Was it not to your liking? I can try again if you want."
    m "It’s not that. I just expected you to agree with me."
    m "You're normally quite irritated with my harshness by the second box."
    s "There aren’t many occasions where I openly agree with you, so that was probably a fair assumption."
    m "There really aren’t many, are there? The subject of my secrecy is one that you’ve been adamantly against as of late, though."
    m "I figured refusing to give in yet again would push you over the edge and make you even more irritating than normal tonight."
    s "I mean...it’s definitely frustrating. But there’s no point forcing anyone to do anything they don’t want to do."
    m "That’s not true. I forced you to carry something here for nothing in return and I have no regrets whatsoever."
    m "Sometimes, forcing people to do things they’re not comfortable with is the best way to move them forward."
    m "Wouldn't you agree?"

    if bonus == True:
        play sound "static.mp3"
        scene yumi14
        with flash
        scene mayanightschool3
        with flash
        stop sound
    else:
        play sound "static.mp3"
        scene frown
        with flash
        scene mayanightschool3
        with flash
        stop sound

    s "Not sure."
    s "Hasn't really come up."
    m "Really?"
    s "Really."
    m "I think there’s someone who would be very upset to hear you say that."
    s "There’s always someone upset to hear anything."
    m "Agreed."

    scene mayanightschool1
    with dissolve

    m "Which is why I’ve found it’s best to simply not talk about my deepest thoughts."
    m "I’m not good at dealing with people who are hurting. Or upset. Or...people in general, for that matter."
    m "It’s one of the reasons I never come to the graveyard with you."

    play sound "static.mp3"
    scene amiani9
    with flash
    scene mayanightschool1
    with flash
    stop sound

    s "Were you close with Ami’s parents?"
    m "Have you given up on referring to them as your brother and his wife?"
    s "It...still feels a little strange calling them that when I have no idea who either of them are."
    m "I see."

    "Maya pauses and locks her eyes on the stars she loves so much for a moment or two."
    "She looks beautiful in the moonlight."
    "I think about telling her, but know that it will only end in tragedy."

    scene mayanightschool4
    with dissolve

    m "I wasn’t close with them."
    m "Ami and I didn’t become friends until a later point."
    s "Well, then what else is stopping you from coming to their grave? It’s not like you have any sort of attachment or anything."

    scene mayanightschool5
    with dissolve

    m "That’s a good question."
    m "What {i}is{/i} stopping me?"
    s "…"
    m "…"
    s "Do you have an answer? Or are you just being weird and leaving things open-ended for the millionth time?"

    scene mayanightschool4
    with dissolve

    m "Did you expect me to actually answer that?"
    m "I literally just finished talking about how secretive I am and now you want me to tell you a secret?"
    m "Just how stupid are you?"
    s "Okay, there’s no need to be rude. I was just asking a question."
    s "The least you can do after I help you carry {i}another{/i} stupid box here is-"

    scene mayanightschool6
    with dissolve

    m "Don’t call it stupid."
    s "…"
    m "…"

    "Maya sounds unusually stern."
    "I’ve only seen her this way a few times, and each one has been after I’ve talked too much or asked a few too many questions."
    "And, while it’s true that I may have been doing that again tonight, I feel like this anger is placed elsewhere."
    "Even if I don’t know what’s in the box, I can surmise that whatever it is must be of some importance to her."
    "Hooray for the powers of common sense and deductive reasoning."

    s "My bad. I didn’t mean it."

    scene mayanightschool1
    with dissolve

    m "..."
    m "It’s fine. "
    m "I can only imagine how frustrating it must be to be forced into a role you never wanted, without any explanation as to why you’re performing it."
    m "But you did a good job."
    m "Thank you."
    s "No need to get sappy. All I did was carry a box."
    m "You carried a burden. It’s different."
    s "...I’m sorry?"

    scene mayanightschool2
    with dissolve

    m "There’s no hidden meaning in that. I just meant it must have been a burden on you to carry it."
    m "I made you do something you didn’t want to do, and now I must make it up to you."
    s "Oh, you don’t have to worry about that."
    s "Just spending time with you is enough to make me happy."

    scene mayanightschool5
    with dissolve

    m "Heh..."
    m "If only it were that easy."
    m "I know better than most that making you happy takes a lot more effort than just walking to[school] at night and pawning off some fleeting thoughts on you."
    m "But thank you for pretending. You’ve always been good at that."
    s "..."

    scene mayanightschool7
    with dissolve
    stop music

    m "Now-"
    m "How about I treat you to a drink?"

    if bonus == True:
        play sound "static.mp3"
        scene mayacg8
        with flash
        scene mayasweep5
        with flash
        scene mayadormten21
        with flash
        scene mayasit2
        with flash
        scene mayayay2
        with flash
        scene reset8
        with flash
        scene mayabeach10
        with flash
        scene vend1
        with flash
        stop sound
        play music "comfort.mp3"
    else:
        play sound "static.mp3"
        scene vend1
        with flash
        stop sound
        play music "comfort.mp3"

    m "How is it?"

    "I crack open the can and take a sip."
    "It’s a sort of semi-sweetened iced coffee that causes a wave of nostalgia to sweep over me as I press my back against the cold alley wall."

    s "…"
    m "…"

    "Of course, things are once again awkward between the two of us and I feel a sudden urge to speak out."
    "The weird thing with Maya is that I’m not even sure if I should try breaking the ice in times like these or not."
    "I feel like more than half the time she just tells me to stop talking."

    s "Well...this is new."
    m "…"
    s "…"
    s "Maya?"

    scene vend2
    with dissolve

    m "Oh, sorry."
    m "I must have stopped paying attention for a minute."

    "This is exactly what I’m talking about."
    "One minute, everything seems fine between us...and the next, she’s pretending I don’t exist."
    "It doesn’t make any sense."

    s "I was just thinking that it feels a little weird being out here with you. That’s all."
    s "But if you don’t want to talk, that’s fine. We can just stand here and relax for a while before heading back."

    scene vend1
    with dissolve

    m "Right..."
    m "Yes."
    m "That would probably be for the best..."

    "And so the two of us stand there in silence, incapable of figuring out the best way to break the ever-growing glacier between us."
    "I like Maya."
    "I really do."
    "But at this rate, who’s to say if we’ll ever actually grow any closer?"
    "My relationship with her isn’t like the one I have with Yumi."
    "No matter how much time I spend with Maya, it seems like the way she looks at me doesn’t change at all."
    "It’s like she’s staring through me at times. Like I’m such an insignificant part of her life that it just...doesn’t even matter."
    "You’d think after resetting the entire world, the two of us might have bonded somewhat, but..."
    "I don’t know."
    "I’m sure she’s reset the world countless times by now."
    "I’d be tired if I was her, too."
    "So I’ll just..."
    "Finish this coffee and let her have a few moments to herself."

    scene black
    with dissolve2

    "The walk back to the dorm isn’t as silent as the time we spent in the alley."
    "Maya mentions a few things about how Molly has been getting on her nerves lately and how she wants to trade her for another new student."
    "Unfortunately, I don’t think I’m able to pull off a move like that, so Maya will need to suffer a little longer."
    "But we all must suffer in this life."
    "And no, I’m not talking about Molly anymore- I’m talking about life in general."
    "Sometimes, we’re completely incapable of dealing with the smallest things."
    "Whether it be carrying boxes-"
    "Or finding things to talk about in a random alleyway in the middle of the night-"
    "This world is filled with confusion."
    "But it’s also filled with cute girls and the sensations that come along with violating them."
    "And so we must press on."

    stop music

    "{s}THE FUTURE IS BRIGHT{/s}"
    "{s}CLOSE YOUR EYES{/s}"
    "{s}TURN OFF THE LIGHTS{/s}"
    "{s}DO EVERYTHING YOU CAN TO BRING THE DARKNESS BACK{/s}"
    "{s}Or prepare to be swallowed by it.{/s}"

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayadorm20 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayadorm25:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
        if maya_love >= 20 and shrine20 == True and yumidorm10 == True and mayadorm20 == False:
            jump mayadorm20
...
```