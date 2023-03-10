# At Least It's Not Christmas (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Mechanical Bull](./halloween8.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween9
* Group: Main
* Triggered by label: mikumount
* Chain sources: halloween8
* Chain sources path: halloween8->halloween8->mikumountx

## Official wiki page

[At Least It's Not Christmas](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween9&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween9:
    scene halloweenparty1
    with dissolve
    play music "letsfuckingo.mp3"

    "Within half an hour, the Amamiya family’s dojo (Which is apparently a thing they have) goes from mostly empty to completely filled with girls."
    "All of the snacks that Makoto and I purchased at various grocery stores throughout the day were replaced by food from a nearby catering company-"
    "Which I would be totally fine with if that catering company did not promptly throw everything we’d spent the afternoon preparing directly into the trash."
    "Also, what the Hell did they even bring to this party? "
    "I haven’t taken a close look yet, but I’m pretty sure I can see a wedding cake, fried rice, a giant squid, and pancakes from here."
    "And that’s not even everything."

    ay "So, Sensei! What do you think of my house so far? "
    ay "Pretty impressive, right?"
    ay "It’s the second largest estate in all of Kumon-mi! "
    s "Well first off, I haven’t seen the inside of your {i}actual{/i} house yet, just this extra building."
    s "And second, do you really mean to tell me you’re not the richest person in the entire city? "
    ay "Well, I don’t really know my dad’s net worth or anything, I just know that the other house is bigger than ours."
    ay "I think it’s just some snobby rich people that live there or something, though. I’m clearly still humble and lovable and cute and stuff."
    ay "As you can see, I have not yet been fully consumed by greed and will accept a smaller wedding if you so desire."
    ay "I even had a cake brought here for that exact purpose!"

    scene halloweenparty2
    with dissolve

    a "Hey, wait a second! You said that you just liked the taste of wedding cake better than normal cake!"
    a "You didn’t say there was going to be an actual wedding!"
    ay "Because there isn’t."

    scene halloweenparty3
    with dissolve

    ay "Yet."
    a "How are we still friends? Why do I continue to accept this?"
    s "You look very pretty, Ami."

    scene halloweenparty4
    with dissolve

    a "Hehe~ Thank you!"

    "I manage to diffuse Ami’s anger in the only way I know how."
    "It would be problematic for her to kill someone in the middle of a Halloween party, and I haven’t even gotten a chance to mingle with everyone yet."
    "I need to at least choose my favorite costume before this turns into some sort of murder-mystery."
    "Speaking of which, I’m surprised Ami was able to make something as lavish as what she’s wearing now with what little supplies she picked up from the mall."
    "Is my [niece] actually talented?"
    "Who would have thought?"

    scene halloweenparty5
    with dissolve

    ay "I agree, Ami. You look adorable."
    ay "I’m really surprised you were able to pull that off in just a day."
    a "Aww, stop. You’re probably the only person I know who could pull off looking cute in a full suit of armor, so that means a lot coming from you."
    ay "Oh, please. My costume isn’t nearly as impressive. I just had it refitted to suit my body type instead of that of a middle aged man. "
    a "Well it was definitely worth it. It’s probably my second favorite costume here, right next to Maya’s."
    ay "Agreed. Maya’s costume is clearly superior to all of ours. "
    ay "I’ve never seen her look this cute before."
    ay "I had to have Sana hold me back to prevent me from jumping all over her when she first walked in tonight."
    s "Okay, now I’m intrigued."
    s "I didn’t think Maya would be dressed up so...impressively, as you two put it."
    s "What is her costume and where can I find her?"

    scene halloweenparty6
    with dissolve

    ay "Oh, you probably won’t like it, Sensei. It’s kind of a thing only us girls would be interested in."
    a "Probably Ayane and me more than anyone else. "
    s "Is it like...an inside-joke or something?"
    ay "Nononono, it’s just-"
    a "Oh, look! Here she comes now!"

    "I turn around to find Maya and-"

    scene halloweenparty7
    with dissolve

    s "…"
    m "Hey."
    s "…"
    m "…"
    s "Are you supposed to be me?"
    m "My goal was to dress as a clown."
    m "I believe I have succeeded."
    s "For someone who hates me so much, you look really cute dressed up as me."
    m "You’re just a narcissist. I look average at best right now."

    scene halloweenparty8
    with dissolve

    a "I personally think you look better than ever~"
    ay "Agreed. What are you doing after the party, Maya?"
    m "Going to sleep. And I do not appreciate the way you two are looking at me right now."
    s "Has everyone forgotten that the real me is right here?"
    s "Do I need to put on a shrine maiden outfit to return the favor or something?"

    scene halloweenparty9
    with dissolve

    m "Yes."
    m "That is sure to teach me a lesson."
    m "Should I run home and grab one for you?"
    a "Umm...I love you, but I don’t think I’d wanna see you in something that...girly, Sensei."
    ay "I’m open to it."
    ay "Not exactly what I have in mind when I think about you, but I’m willing to accept you no matter how you dress."
    ay "Unlike Ami, who has just confirmed that she does not love you enough to let you dress how you want."
    ay "I finally win."
    s "I never said I {i}want{/i} to dress that- Actually, never mind. "
    s "I’m going to go talk to some of the others. I’d be a rude guest of honor if I only spent time with you three, who practically live at my house."
    a "I...{i}do{/i} live at your house. It’s not ‘practically.’"
    m "Oh no. Sensei is leaving. Whatever will we do to pass the time now?"
    s "If you’re going to dress as me you should at least come up with a decent impression or something."
    m "Oh, right. I had one planned. Hold on."

    scene halloweenparty10
    with dissolve

    m "Hah..."

    "Maya takes a deep breath and prepares herself for whatever sort of mockery she’s about to make of me."

    scene halloweenparty11
    with dissolve

    m "Teenagers are the best. "
    m "Can I hang out in your room? "

    if bonus == True:
        m "Why is everyone I know so cute?"
        m "I am a horrible person."
    else:
        m "Want to hug?"
        m "I'm really cute."

    scene halloweenparty12
    with dissolve

    if bonus == True:
        m "Is that enough?"
        s "I think it needs work."
    else:
        m "Whoops. That last one was an accident."

    scene halloweenparty13
    with dissolve

    a "Well...it wasn’t {i}completely{/i} accurate, but it wasn’t completely {i}inaccurate{/i} either."
    ay "Agreed. She didn’t capture any of his good points. Like how kind and compassionate he is."

    if bonus == True:
        ay "Or how big his-"
    else:
        ay "Or that thing he does where he steals your shoes in the middle of the night and hides berries in them."
        s "Hahah. I love doing that."

    scene halloweenparty14
    with dissolve

    m "Why does everyone like you so much?"
    s "I have no idea, Maya. But I’ll talk to you later."
    s "I’m going to go tell everyone how cute I think they are."
    m "No, really. {i}Why does everyone like you so much?{/i}"

    scene black
    with dissolve

    "I walk away from the three of them while Ami and Ayane are still locked in their thoughts and make my way over to the table Rin and Futaba are sitting at."

    scene halloweenparty15
    with dissolve

    r "Oh, uhh, hey! "
    r "Don’t look at me. I’m suddenly embarrassed for some reason."
    f "Rin’s self-conscious about her...increase in chest-size."
    r "I’ve gotta keep my arm like this or it will just be sideboob everywhere."
    r "I know that’s kind of the point of the costume but it definitely feels weird when there are this many people around."
    r "Especially Chika even though I’m like totally, absolutely, positively over her."
    s "It’s okay to still think she’s attractive, Rin."

    scene halloweenparty16
    with dissolve

    r "God I want to rip her friggin’ costume off."
    f "Th-That aside...how are you doing tonight, Sensei?"
    f "How was your date with the...strange girl from the restaurant yesterday?"
    s "Kaori? It was fine I guess."
    s "I wouldn’t really call it a date, though."
    s "We just kind of walked into an alleyway with a bunch of chickens in it and then I collapsed."
    s "Actually, why don’t you tell me a little about {i}your{/i} night instead? How are you guys doing?"
    s "And what are you even supposed to be?"

    scene halloweenparty17
    with dissolve

    r "Hipper-class heavy cruiser, Prinz Eugen. Straight outta Germany."
    s "So...you’re a boat?"
    r "Yes."
    s "Interesting. "
    r "Very. "
    f "And I’m...umm...Mami Tomoe from Madoka Magica..."
    f "I’m sure you don’t know what that is so...yeah..."
    s "Well either way, you two look cute."

    scene halloweenparty18
    with dissolve

    r "Don’t fall in love too hard, Sensei!"
    r "I’ll just break your heart the second you confess to me on the beach and you’ll go on to spend the next few weeks in inner turmoil."
    f "As you can see, Rin is still not completely over what happened back then."
    r "So much salt."
    r "But boats float on saltwater so my costume is a metaphor for me getting over it."
    r "Just kidding."
    r "I kinda just want to bang the character."
    r "Which doesn’t mean I’m attracted to boats or anything."
    r "Well, I'm also not {i}not{/i} attracted to them and-"
    r "…"
    r "Actually, I’m gonna go to the bathroom now. I’ll be right back."

    scene halloweenparty19
    with dissolve

    "Rin quickly leaves the table and walks in a very strange route to avoid crossing paths with Chika, who seems to be absorbed in her phone on a bench in the corner of the room."
    "Yumi is nowhere to be seen, so I’m pretty sure Chika’s still trying to get her to come over here or something."

    f "She’s been staring at her all night."
    s "I’m not surprised. She was into her for years and Chika is dressed...rather provocatively tonight."

    if bonus == True:
        f "To be fair, I’m sure we’d all dress like that if we looked like her."
        s "I think it would be a great idea if you were to all just dress like that anyway. "
        f "If it were up to you, I doubt anyone of us would be wearing costumes at all right now."
        s "Ahh, that’s where you’re wrong, Futaba."
        s "I’ll obviously never say no to nudity, but there’s a certain allure that comes with Halloween costumes that a man simply can not pass up."
        f "Girls like costumes too, you know?"
        f "It might have been nice for you to get dressed up as something or someone."
        s "Does my standard apparel not excite you?"
        f "Not...particularly."
        f "It’s more the situations that you put me into that do..."
        f "But I don’t really want to talk about that surrounded by everyone in class, so..."
        s "Fair enough. I was about to go say hi to some of the others anyway."
        s "I’m sure I’ll see more of you later tonight, though."
    else:
        s "She is a grown woman and is certainly allowed to dress that way if she wants to, but I do not see the appeal and wish she would wear something less revealing."
        s "Anyway, I have to go do stuff. But I'm sure I'll see more of you tonight?"

    scene halloweenparty20
    with dissolve

    f "Of course. Are you staying the entire time?"
    s "Unless something comes up, yeah. Who knows at this point?"
    f "Well...I guess I’ll see you around then."
    f "Feel free to come hang out at our table later if you want."

    scene black
    with dissolve

    "I’m sure I’ll wind up doing just that at some point. "
    "But for now, the meeting and greeting (Well, I guess technically just greeting since I’ve met all of these people) must continue."

    scene halloweenparty21
    with dissolve

    "I stop at the catering table to greet Makoto and Miku on my way over to Chika."
    "It appears at first glance that the two of them have already gotten over this morning’s incident, but I’m sure it’s bound to come up again at any moment."

    if bonus == True:
        mi "Heya, Sensei! Makoto says the two of us aren’t allowed to be alone together anymore since I gave ya an erection this morning."
    else:
        mi "Heya, Sensei! Makoto says the two of us aren’t allowed to be alone together anymore since her memories are still caught up in the other timeline."

    mak "This is what’s best for everyone."
    mak "I’m sure you understand."

    if bonus == True:
        s "Hold on just a second. I had that erection before Miku even came into my room."
        mi "I think that’s probably true. I don’t think Sensei would have gotten one from me unless he’s been secretly into boys this whole time."
        mak "As a matter of fact, I don’t believe he is."
        mak "But still, it would be in everyone’s best interest if you remain at least six feet apart at all times from now on."
        mi "Gotta leave room for Jesus, ya know?"
        s "Thank you for being the authority on everyone’s best interest, Makoto."
        s "I wish you would have said something about this decision during the {i}entire day{/i} we spent together so I could clear up any misunderstandings."
        mak "Oh. So I misunderstood Miku grinding all over your lap this morning?"

        scene halloweenparty22
        with dissolve

        mi "Hey! Wait a gosh darn second! I wasn’t grindin’ anything! I don’t even know how to do whatever that means!"
        mak "I’m sorry, Miku. The music is so loud that I can’t understand what you’re trying to say. "
        mak "If you’re apologizing for trying to seduce the teacher before he woke up this morning, then apology accepted. "
        mak "Just don’t do it again or I’ll have to report it to the[school]."
    else:
        s "I don't."

    scene halloweenparty23
    with dissolve

    mi "Hey, don'tcha think that witch costume suits her a little too well?"
    s "Yeah, she looks gorgeous in it."

    scene halloweenparty24
    with dissolve

    mak "Hehe~ Thank you~"
    mi "Nonono, I meant like, {i}cause she’s bein’ a real witch right now.{/i}"

    if bonus == True:
        mi "{i}We really didn’t do anything weird and I keep thinkin’ she’s gonna shank me when I’m not payin’ attention.{/i}"
        mi "{i}And Karin’s busy tonight so I can’t even hire a bodyguard.{/i}"
        s "Karin is strong but I don’t think she’d be willing to fight off anyone who actually wants to stab you, Miku."
    else:
        s "Don't talk about your friends that way or they'll all wind up leaving you."
        s "{i}That's what happened to me, at least...{/i}"
        mi "But I keep thinkin' she's gonna try and kill me! She's got a fire in her eyes like I've never seen!"

    s "Just run away if she tries anything."
    s "Or better yet, fly. You have wings tonight."

    scene halloweenparty25
    with dissolve

    mi "Holy heck! Ya don’t think they actually work, do ya?!"
    s "Please do not jump off of anything high trying to find out. I want to clarify that since I’m never sure what you’re going to take seriously or not."
    mak "Speaking of taking things seriously, Sensei, there’s something I’d like to discuss with you later if you get some time."
    mak "Obviously, you need to say hello to everyone first, so just come see me whenever you have an extra moment."
    mak "I can assure you it will be worth your time."
    s "Huh? Oh, yeah. I can do that."
    mak "Great. "

    if bonus == True:
        mak "Now, if you’ll please excuse Miku and me, I’d like to continue lecturing her about the risks that come with sex before marriage."
    else:
        mak "Now, if you’ll please excuse Miku and me, I’d like to continue lecturing her about how butter is made."

    scene halloweenparty26
    with dissolve

    mi "AAAAAHHH!!! JUST KILL ME ALREADY!!!!"

    scene black
    with dissolve

    "I take a step past Miku as she crumbles under Makoto’s clutches and falls to the ground."

    if bonus == True:
        "Fortunately, I am far too busy to involve myself in discussions about pre-marital sex and have decided to talk to Chika instead."
    else:
        "Fortunately, I already know how butter is made so I do not feel pressured to stay for the lecture."

    scene halloweenparty27
    with dissolve

    "Now {i}this{/i} is a rare sight."
    "Chika sits by herself without even a semblance of a smile on her face."
    "Maybe the thing with Yumi is hitting her harder than I thought it would."
    "I know she cares about her a lot, but I didn’t think she’d get this offended by her just...doing what she wants to do when that’s always what Yumi does in the first place."

    s "Hey. What are you up to?"

    scene halloweenparty28
    with dissolve

    c "Oh, hey! "
    c "Just texting and stuff."
    c "Did I look like a loner over here?"
    c "Come over to keep me company?"
    s "I guess you could say that."
    s "Talking to Yumi, I’m guessing?"

    scene halloweenparty29
    with dissolve

    c "Yeah. I feel really bad."
    c "I honestly might get out of here and just go hang out with her at my place if I can’t get her to come."
    c "She always winds up having to spend her birthday alone and I shouldn’t be letting stuff like that happen when I’m really the only friend she has."
    c "Like, even when she used to chill with all of those guys her dad knew, they never really paid much attention to her."
    c "She’s like a lost puppy just lookin’ around for a mama-dog and-"

    scene halloweenparty30
    with dissolve

    c "Oh no! Now I’m thinking of Yumi as an actual puppy and it’s even more sad!"
    c "Do you have a handkerchief I could borrow or something? I don’t wanna cry and ruin my makeup."
    s "I am definitely not the type to carry a handkerchief around. Sorry, Chika."

    scene halloweenparty31
    with dissolve

    c "It’s fine. If I strain my eyes I can probably just trap my tears with my eyelids and prevent them from running down my face or whatever."
    s "That...is one of the saddest things I’ve ever heard."
    c "Sadder than spending your birthday and Halloween alone at the same time?"
    s "At least it’s not Christmas."
    c "Heh...Yeah, I guess you’ve got a point there."
    c "I was just hoping that after the beach thing, she’d realize that not everybody hates her and that it’s okay to show up to group activities and stuff."
    s "To be fair, she didn’t make much of an effort at the beach either."

    scene halloweenparty32
    with dissolve

    c "She never makes much of an effort anywhere. That’s why you and me have to try so hard to protect her."
    s "…"

    "I’m not sure how it falls on {i}me{/i} to protect Yumi when she’s capable of making her own decisions- even if more than half of those decisions are wrong."
    "But I guess it wouldn’t hurt going out of my way for her every once in a while."

    s "Hey, why don’t you tell her that I’ll stop covering for all of her absences if she doesn’t show up to the party for at least an hour?"

    scene halloweenparty33
    with dissolve

    c "Ooh! That actually might work! Great idea, Sensei!"

    scene halloweenparty34
    with dissolve

    "Chika begins typing out a message to Yumi at light-speed and then pauses for a few seconds after tapping what I assume is the ‘send’ button."

    s "Any response yet?"

    play sound "phonebeep.wav"

    c "Just got one."
    c "…"
    s "...And?"
    c "She says “Fuck you.”"
    s "Oh."

    scene halloweenparty35
    with dissolve

    c "I think it’s a good “Fuck you,” though."

    if bonus == True:
        s "There is only one good way to use those words together and I am almost positive it is not what you’re talking about."

        scene halloweenparty36
        with dissolve

        c "Heh."
        s "Wait, {i}is it?{/i}"
        c "Of course not. But I thought about it for a second and now I’m trying to figure out if I should be jealous of Yumi or not for doing stuff with you in my imagination."
        s "Please tell me more about what’s happening in your imagination, Chika."
    else:
        s "There is no such thing. Now, tell her to wash her mouth out with soap."
        s "Or, better yet, give me a hug."

    scene halloweenparty37
    with dissolve

    c "No thanks~ Gotta focus on getting my friend here."
    c "Maybe you should go talk to whoever is in the dolphin costume? She’s been looking at you all night."
    s "The dolphin costume? That’s Sana."

    scene halloweenparty38
    with dissolve

    c "Wait, {i}Sana{/i} is in the dolphin costume?! That’s like, totally unexpected."
    c "And why is she staring at you so much if that’s true?"
    s "I’ll be sure to let you know if I find out."

    scene black
    with dissolve

    "I step away from Chika and begin heading to my next target."
    "I do hope she’ll be able to convince Yumi to come. "
    "I’m not sure if my strategy will work, but it’s definitely something I can imagine a tsundere falling for."

    if bonus == True:
        "If she even is a tsundere and not just some girl who literally wants to rip my dick off."

    scene halloweenparty39
    with dissolve

    s "…"
    sa "…"
    m "…"
    m "I can’t tell if I like Halloween or not."
    s "Sana, did you need something?"
    s "Chika informed me that someone in a dolphin costume has been staring at me the entire night."
    s "And seeing as there are no other dolphin costumes to be found-"

    scene halloweenparty40
    with dissolve

    m "Well {i}you’re{/i} just a regular Sherlock Holmes, aren’t you?"
    s "Can it, Maya."
    sa "U-Um...Y-Yes!"
    sa "I...don’t really know what to do at...p-parties..."
    sa "But Maya came to sit with me right before you showed up, so..."
    m "That’s right. Your assistance is no longer needed. Goodbye."
    s "Are you friends with Maya now, Sana?"

    scene halloweenparty39
    with dissolve

    m "Now? Were we not friends previously?"
    sa "W-We were?! But we’ve never really...talked alone before..."
    m "You don’t really need to talk in order to be friends with someone, do you?"
    s "I think you...kind of do?"

    scene halloweenparty40
    with dissolve

    m "Interesting. I suddenly have significantly less friends than I thought I did."
    m "How sad."
    sa "A new friend..."

    scene halloweenparty39
    with dissolve

    m "Correct. And as your friend, is it okay if I ask how long you intend on staying inside of the dolphin costume for?"
    m "It has to be hot in there, right?"
    sa "Yes but...I look silly with my hair up so..."
    sa "It’s kind of embarrassing...not being inside of the dolphin."
    m "Why wear a dolphin costume in the first place?"
    m "Also, what is Sexy Land?"
    sa "I...still haven’t had the heart to look it up..."

    scene halloweenparty41
    with dissolve

    m "Then I will. I’m kind of curious now."
    s "…"
    sa "…"
    m "Oh."
    m "Well, I definitely don’t like that."
    sa "What...is it exactly?"

    scene halloweenparty42
    with dissolve

    "Maya holds up her phone to Sana, who takes...quite a long time looking it over."

    sa "…"
    s "Can I see next?"
    m "Absolutely not."
    s "You know I can just look it up myself, right?"
    m "Feel free. I will not be showing you this."
    sa "…"
    s "…"

    scene halloweenparty43
    with dissolve

    sa "…"
    s "Sana?"

    scene halloweenparty44
    with dissolve

    sa "I..."
    sa "I need to go think about some things..."

    scene halloweenparty45
    with dissolve

    "Sana leaves the table and suddenly, Maya and I are alone together at a party."
    "That is not something I ever expected to happen."

    m "I bet we look very strange right now to anyone who looks over here."
    s "We’d look significantly less strange if we weren’t matching."
    m "And we’d look even stranger if you had decent fashion sense."
    m "Thankfully, your style carries the same amount of excitement as an order of plain toast, so we at least look generic."
    s "You say that, but I really do think you look cute."
    m "Stop saying that. It’s weird."
    m "Looking cute was not the point. I want to annoy you."
    s "You’re not slipping into the tsundere role for real this time, are you?"
    m "No, I just genuinely want to annoy you. I mean it."
    s "Why do I feel like you’re being serious?"

    scene halloweenparty46
    with dissolve

    m "Because...I am?..."
    s "Sure, Maya."
    m "What do you mean “Sure, Maya?” "
    m "I am Maya and I am sure. "
    m "If I wanted you to think I was cute I’d just wear the same things I always wear. That’s the most effective tactic."
    s "{i}Sure, Maya.{/i}"

    scene halloweenparty47
    with dissolve

    m "I hate you so much."

    scene black
    with dissolve

    "I pull my chair out and turn around to see if I can figure out where Sana’s gone, but it seems she’s already disappeared."
    "That being said, there are only two students I have yet to see."
    "Well, other than the one who hasn’t shown up, that is."
    "I walk past Ami and Ayane on my way to the opposite side of the room, patting each of them on the head at the same time so they don’t kill each other, and finally stop at Molly and Tsuneyo."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloween9 = True

label halloween10:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```