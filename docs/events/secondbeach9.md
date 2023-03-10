# Alderaan (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Legacy of Thaum Pt. III: Changeling](./secondbeach8.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach9
* Group: Main
* Triggered by label: secondbeach8
* Chain sources: secondbeach8
* Chain sources path: secondbeach8

## Official wiki page

[Alderaan](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach9&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach9:
    scene mollyosako1
    with dissolve2
    play music "hometown.mp3"

    ay "Molly! Wait up!"
    n "What’s going on? What the hell happened in the like, five minutes I was out of the room for?"
    mo "Stop following me!"
    ay "No! If you’re feeling down, it’s okay to talk about it!"
    n "Uhh, Molly? I have no idea what happened, but Ayane is right. "
    n "I’m sure that whatever it is is just temporary. Life is too short to spend on negative emotions like this."
    mo "I frickin’ know that! I just wanna cry alone!"

    scene mollyosako2
    with dissolve

    n "Mind cluing me in on what happened exactly? Molly’s kinda got a right to cry by herself if she wants to."
    ay "I know, I know. That’s what I do to handle basically everything ever."
    ay "But there’s clearly a little more going on than just her wanting to cry...and I want to make sure it isn’t something that’s going to wind up ruining or destroying any friendships in the process."

    scene mollyosako3
    with dissolve

    mo "I’m not destroying anything! It’s not me!"
    ay "That’s not what I was saying, Molly..."
    mo "Rin’s the one who shouldn’t have gotten mad! It’s {i}my{/i} campaign that {i}I{/i} made for {i}us!{/i}"
    mo "Yeah, it might be kind of immature! But it’s really important to me and she clearly doesn’t care about it!"
    n "I think Rin cares, Molly. She just-"

    scene mollyosako4
    with dissolve

    mo "What do you know?! You weren’t even there!"
    n "Uhh...right. Good point."
    ay "She’s right, though. Rin really does care."
    ay "About the campaign. About spending time with everyone."
    ay "About you."
    ay "She just wanted to share some of that fun with a new friend of hers. And all of us were okay with it."
    ay "You normally {i}love{/i} the idea of anyone joining in on the campaign. How come Otoha was an exception to that?"
    mo "I...I don’t have to explain myself to you!"
    ay "No, you don’t. "
    ay "But I’d really appreciate it if you tried."

    scene mollyosako5
    with dissolve

    mo "{i}*Sniff*{/i}"
    mo "I don’t think my charisma is high enough to get it out in a way that will make sense."
    mo "This was just the one thing I didn’t think would be touched by...someone else."
    mo "Was I mean? Maybe a little bit. But you’re on {i}my{/i} side, right? "
    mo "Like...letting someone else just jump in like that defeats the purpose of the...campaign, and..."
    ay "Why do there have to be sides?"
    ay "Why can’t we just go back, apologize to Otoha for yelling at her, and then keep playing?"
    ay "You were looking forward to this, weren’t you? Just like all of {i}us{/i} were looking forward to it."
    ay "We don’t want to let something like this get in the way of that."

    scene mollyosako6
    with dissolve

    mo "You think {i}I’m{/i} the one who should apologize?"
    ay "Not for getting upset, of course not. But you yelled at someone who basically just sat there and took it."
    ay "Otoha gave up on playing as soon as you said you didn’t want her to. She was just going to watch."
    ay "And Sensei’s watched us a few times in the past, so there’s clearly no problem with being spectated."
    ay "I just don’t understand why you’re acting like this all of a sudden."
    mo "It’s a free country! I can cry if I want and I don’t have to explain myself!"
    ay "You’re not understanding, Molly. It’s fine to cry, but not when it’s going to hurt other-"
    n "Sorry, Ayane. But I think I might know what’s going on here."

    scene mollyosako7
    with dissolve

    mo "What could you possibly know? You weren’t even in the room for two minutes."
    n "So you’re {i}not{/i} jealous of Otoha because Rin is crushing on her? "

    scene mollyosako8
    with dissolve

    mo "Wha-"
    mo "I...I have no idea what you’re talking about!"
    ay "Oh my God..."
    ay "Of course..."
    ay "How didn’t I notice?"
    ay "That would explain everything."
    n "Molly, we’re three girls alone on the beach. We’re not going to judge you for having a crush on a friend."
    mo "I don’t have a crush on anyone!"
    n "Are you denying it because she’s a friend? Or because she’s a girl? "
    n "Because if you’re worried about the latter part, I like girls too. That sort of thing just happens at all girls[school]s...and in the world in general. "
    n "There’s nothing to be ashamed of."
    mo "I’m not ashamed of anything! Stop following me!"

    scene mollyosako9
    with dissolve

    ay "Molly...I’m so sorry I didn’t notice earlier. I wouldn’t have even chased after you if I knew that’s what it was."
    mo "…"
    mo "I never said that’s what it was."
    n "Well, if I’m making a mistake, I’m really sorry."
    n "But, to anyone out there who might be listening in from behind a tree or something, it’s okay to like whoever you want."
    n "You don’t have to feel bad about it just because they’re interested in someone else."
    n "Sometimes, the hardest ones to get are worth the chase. Even when you know it’s going to hurt at times."

    scene mollyosako10
    with dissolve

    n "Right, Ayane?"
    ay "Huh?"
    n "What? You and I are rivals in love."
    n "You don’t mean to tell me that I’m the only one that's been getting jealous whenever Sensei is with other girls, do you?"
    ay "…"

    scene mollyosako11
    with dissolve

    ay "No. You're definitely not."
    ay "In fact, even the thought of you knowing him longer than me makes me sick to my stomach."
    ay "But I’m not ashamed to follow my heart. And I know that I have a better chance at ending up with Sensei than anyone."
    n "And I wish you luck in that regard."
    n "But I’m going to beat you."

    scene mollyosako12
    with dissolve

    n "See, Molly? If Ayane and I can have feelings for someone without destroying any relationships in the process, what’s stopping you from owning up to your feelings as well?"
    n "Unless I actually {i}am{/i} wrong and you don’t like Rin. If that’s really the case, this is probably a very awkward situation for you right now."
    mo "{i}*Sniff*{/i}"
    mo "I’m not admitting anything, but..."
    mo "I’m...flattered you two have followed me this far..."
    mo "But...in the event that I actually {i}did{/i}...feel that way about her...it would be a much different scenario..."
    mo "You two have loved Sensei for as long as you can remember. "

    if bonus == True:
        mo "I’m not even a romanceable character in Rin’s metaphorical eroge. That’s how far off the map I am in her eyes."
    else:
        mo "I’m not even a romanceable character in Rin’s metaphorical dating sim. That’s how far off the map I am in her eyes."

    n "That’s not true. "

    if bonus == True:
        n "Even if you two are just friends, I’m sure she’s at least rubbed one out to some kinda fantasy of you before. "
        n "That sorta thing is just inevitable at the end of the day."
        n "Hell, even {i}I’ve{/i} rubbed one out to you before and we’ve only talked like two or three times."
    else:
        n "Even if you two are just friends, I’m sure she’s at least contemplated putting your tongue in a jar before."
        n "Hell, I have that dream with virtually everyone. And I'm pretty sure that's just a normal thing for girls."

    scene mollyosako13
    with dissolve

    mo "I...beg your pardon?"
    ay "Um..."
    n "You too, Ayane."
    n "Sensei was there for that fantasy, though."
    ay "…"
    n "…"

    scene mollyosako14
    with dissolve

    ay "Uhh...I think what Noriko is trying to say is that...nothing is impossible!"
    ay "And even if you’re feeling like an undisclosed friend of yours that you may or may not have feelings for is out of reach...he or she never really is!"
    n "Yeah! That!"
    mo "…"

    scene mollyosako15
    with dissolve

    mo "Hah..."
    mo "You two are clearly less versed in the world of RPGs than I am, so allow me to do a little bit of explaining."
    mo "There are many boss fights out there in which the player character is scripted to lose. "
    mo "And if I {i}am{/i} feeling like an undisclosed friend of mine that I may or may not have feelings for is out of reach...he or she really is."
    mo "Do you know how it feels to share clothes with the person you secretly love?"
    mo "To help fit them for costumes, hiding the redness of your face and how easily it gives away your intentions or desires?"
    mo "To smell the scent of her lotion when she puts it on in your dorm room?"
    mo "Or how to rid your brain of the image of her as she storms into the shower and asks to borrow your conditioner?"
    mo "How she sees or feels {i}nothing{/i} for you, but {i}everything{/i} for everyone else?"
    mo "This is all rhetorical, of course."
    mo "I’m just basing this off of...some game I played."

    if bonus == True:
        n "Again, she’s totally fingered herself to some kind of fantasy of you before. I can promise that’s a thing."
    else:
        n "Again, tongue jar. I'm being super serious right now. It's a thing."

    scene mollyosako16
    with dissolve

    ay "I think that might just be a {i}you{/i} thing, Noriko."
    n "Really?"

    if bonus == True:
        n "Look me in the eyes and tell me with a straight face you’ve never [masturbate]d to me before."
    else:
        n "Look me in the eyes and tell me with a straight face that you wouldn't put my tongue in a jar."

    scene mollyosako17
    with dissolve

    ay "I’m sorry. But I just love Sensei so much that those fantasies are reserved for him and him only."
    n "Oh you son of a bitch."

    if bonus == True:
        mo "If you are going to follow me around the beach...could you perhaps attempt to avoid the discussion of your...self-pleasure habits?"
    else:
        mo "If you are going to follow me around the beach...could you perhaps attempt to avoid the discussion of tongues?...I am deathly afraid of them."

    scene mollyosako18
    with dissolve

    os "Oooookay. Looks like I may have picked a weird time to go for a walk."
    ay "Osako! Perfect!"

    scene mollyosako19
    with dissolve

    os "Huh? What?"
    os "What’s perfect?"

    if bonus == True:
        os "I don’t really want to talk about...{i}that{/i} sort of thing with girls your age."
        n "Can you at least confirm that it’s normal for friends to [masturbate] to other friends? I’m trying to prove a point."
    else:
        n "How it's totally normal to fantasize about taking a friend's tongue off and then putting it on display for all of your other friends to see."

    scene mollyosako20
    with dissolve

    os "Uhh...what?"
    mo "Ayane...I was okay with you two following me around, but a person I’ve never met before is-"
    ay "Is even better! Here. Come."
    mo "Hey! Wait!"

    scene mollyosako21
    with fade

    ay "If you have no idea who a person is, wouldn’t that make it a little easier to talk to them about this?"
    ay "Your worry seems to be about ruining relationships- but without a relationship to ruin, what’s there to be afraid of?"

    if bonus == True:
        os "Can someone tell me what’s going on here? Because all I know is that this involves self-pleasure and strangers and those are two big red flags."
    else:
        os "Can someone tell me what’s going on here?"

    scene mollyosako22
    with dissolve

    ay "My friend here may or may not have undisclosed feelings for an undisclosed friend of an undisclosed gender."
    os "Oh."
    os "Well, you’ve certainly bumped into the right person, then."
    ay "Can you maybe talk to her for a little while? Just to kinda help her take her mind off of things."
    mo "I...don’t want to talk..."
    os "Then don’t."
    os "But, as someone who was very likely in the same position as you at one point, I’d be fine with sitting next to you in silence for a little while."
    os "Kinda why I’m out here in the first place."

    scene mollyosako23
    with dissolve

    mo "Do you..."
    mo "Do you like video games?"
    os "Uhhhhhhhh I’m...really good at pinball?"

    scene mollyosako24
    with dissolve

    mo "Hah...I guess I’ll take what I can get..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene mollyosako25
    with dissolve

    ay "I feel like such an idiot."
    n "For not realizing the Rin thing?"
    ay "It’s so obvious in hindsight. "
    ay "Rin’s consistently the first person Molly asks to do anything with."
    ay "And whenever she’s not around, Molly’s mood totally changes. "
    ay "Kinda like she’s distracted or...something like that."
    ay "And all this time I thought it was just because the two of them were close, but..."
    n "So...I obviously wasn’t around for whatever went down-"
    n "But how did Otoha handle it?"

    scene mollyosako26
    with dissolve

    ay "Like anyone would have, I guess."
    ay "She didn’t really say anything. She just kind of sat there and let Molly go off on her."
    ay "Rin was the one who started getting Molly really heated up when she stuck up for her instead of just letting her get yelled at."
    n "I see..."
    n "Do you know what they’re up to now?"
    ay "No clue. I chased after Molly as soon as she stormed out."
    ay "I imagine they’re probably still in the room."
    n "Gotcha..."
    ay "…"
    n "…"

    scene mollyosako27
    with dissolve

    if bonus == True:
        ay "Have you really [masturbate]d to me before?"
        n "Oh yeah. Why would I lie about that?"
        ay "That just seems...so random."
        n "Hm."
        n "Well, like I said, Sensei was there too."
        n "Have you really not had any threesome fantasies?"

        scene mollyosako28
        with dissolve

        ay "Not really, no."
        ay "I think girls are cute, but I’m not really sexually attracted to them."
        ay "I’d probably be willing to do something like that as long as Sensei is there, but I’d never really go out of my way to seek one out."
        n "So like..."
        n "Have you and Sensei actually...you know."

        scene mollyosako29
        with dissolve

        ay "Have we what?"
        n "Like...had sex?"
        n "Or done anything together, really."

        scene mollyosako30
        with dissolve

        ay "Why? Are you jealous?"
        n "Well...yeah."
        n "You’re really pretty. And you clearly love him a lot. "
        n "And...in a lot of ways...you kind of became the new “me” once I wasn’t around anymore."
        n "So I’m definitely jealous. "
        n "Like, I spent all of these years trying to turn myself into what I imagined he wanted out of a girl. "
        n "But then I look at you and then back at myself and can’t help but think, “Did he maybe...change?”"

        scene mollyosako31
        with dissolve

        ay "He changes all the time. "
        ay "With every single person and every single situation."
        ay "But I know from all of the time I’ve spent with him that he’d never want us to be anything other than who we already are."
        ay "And, if I’m being honest-"
        ay "I’m really jealous of you too."
        n "But not jealous enough to [masturbate] to me."
        ay "No, Noriko."
        ay "Not jealous enough to [masturbate] to you."
    else:
        ay "Have you really had dreams about taking my tongue before?"
        n "Oh, no. I was just fucking around."
        ay "Oh."
        n "..."
        ay "..."
        n "{i}Unless...{/i}"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene mollyosako32
    with dissolve2

    os "…"
    mo "…"
    mo "Are you really just going to sit there?"
    os "This is what you wanted, isn’t it?"
    os "Sometimes, the best way to make yourself feel better is to take a deep breath and just reflect on the things you could have done differently."
    mo "…"
    mo "But I don’t really know what I could have done differently."

    scene mollyosako33
    with dissolve

    os "Well...what did you do in the first place?"
    mo "Nothing, really. "
    os "There’s your answer then."
    mo "I...don’t get it."
    os "Well, uhh...like I said, I’m kind of a pinball person and not a game person, but I know enough about some older ones that I can probably cook up some kind of metaphor."
    os "You know those little block things in Mario Kart that give you turtle shells and shit once you drive into ‘em?"
    mo "Of course."
    os "Well...you can’t ever really come in first place if you don’t use those powerups, right?"
    os "And if you don’t use 'em shortly after you get them, you’ll wind up passing by other blocks and missing out on {i}more{/i} of the powerups."
    os "That’s kinda what love is like."
    os "If you don’t jump on every single opportunity to try and put yourself in a better position, everyone is gonna just cruise right by you."

    scene mollyosako34
    with dissolve

    os "For a long while, that’s kind of...exactly what I did."
    os "There was this one girl I was head over heels in love with."
    os "And it was really scary at first...you know, trying to get her to understand that I saw her as more than just...her."
    os "But...as time went by, the desire to hold her and make her mine just started festering and eating me alive from the inside out."
    os "And the first turtle shell box thing I ever encountered was some poetry assignment we had in[school]."

    scene mollyosako35
    with dissolve

    os "She loved poetry."
    os "Well, still loves. It’s one of her favorite things."
    os "But...dorky old me back then was like...what if I memorized something she’d like and...maybe made eye contact with her or something while reading it? "
    os "So I did. Eye contact and all."
    os "And the second her eyes met mine...it became an addiction."
    os "I started finding every fuckin’ turtle shell I could get my hands on, frantically pushing buttons and moving from one place to the next trying to get her to notice me."
    os "If I’d never started taking that approach..."
    os "Well, I don’t really know if I’d be here today."

    scene mollyosako36
    with dissolve

    mo "You...contemplated suicide?"
    os "What? Oh. No. Sorry. I just meant that...we literally came here today together."
    os "And she’s here as a chaperone, so..."
    mo "Chap-"

    scene mollyosako37
    with dissolve

    mo "Are you Miss Watabe’s girlfriend?!"
    os "I am. "
    os "But I never would have become that without working for it."
    mo "Wow..."
    mo "You are...not at all what I was expecting."
    os "Yeah...I get that a lot."

    scene mollyosako38
    with dissolve

    os "This, uhh...{i}undisclosed friend{/i} of yours..."
    os "Does she have a name?"
    mo "She doesn’t exist. But if she did, her name would likely be something like...Ren or...Ran..."
    os "Well, whatever her name {i}would{/i} be, some people just won’t understand things unless you tell them."
    os "And if you want her to know, that might be what you have to do."
    mo "What do I do if I {i}don’t{/i} want her to know?"
    os "Why wouldn’t you want her to know?"
    mo "Because I’m not her type."
    mo "And it might make things weird."
    os "Aren’t things weird now?"
    mo "Only because I made them that way."
    os "Then you’ve got two options. Either apologize and move past it-"
    os "Or make things even weirder and hope that she’s a weird enough person to not inherently hate it."

    scene mollyosako39
    with dissolve

    mo "She {i}is{/i} pretty weird..."
    mo "Or would be if she actually existed. Which she doesn’t."
    os "I’m sure."
    os "At the end of the day, all you can really do is try. Maybe it works out, maybe it doesn’t."
    os "But if you’re already wandering down the beach crying and talking to strangers, I think it’s safe to say that, as-is, things {i}aren’t{/i} working out."
    os "And that, personally, I’d try to do something about it."
    mo "…"
    mo "Thank you, Miss Watabe’s girlfriend."
    os "Osako. "
    mo "Thank you, Osako."
    os "Don’t mention it, random upset foreigner girl."
    mo "Molly."
    os "Don’t mention it, Molly."

    scene mollyosako40
    with dissolve

    os "Now, if you’ll please excuse me, I’d like to silently stare at the stars reflecting off of the water for a little while longer before heading back to my room."
    os "But if you ever need someone to talk to and there isn’t a beach around to bump into randoms, Ayane’s a good bet as well."
    os "She can be a little pushy, but she’s got a good heart."
    mo "I know..."
    mo "Her wisdom is rather high for a rogue as well."
    os "Sure. Whatever that means."
    os "You’re welcome to stay here, you know. Being broody and reflective is surprisingly helpful at times like this."

    scene mollyosako41
    with dissolve

    mo "I suppose a fair bit of brooding won’t do any harm if it’s only occasional."
    mo "Though, it’s hard for me to look up at the stars without grieving over the destruction of Alderaan."
    mo "Oh. Alderaan is-"
    os "Star Wars. I know."
    mo "Rip in peace, Alderaan."
    mo "Rip in peace..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach9 = True
    stop music fadeout 7.0

    "………"
    "……"
    "…"
    "{i}Somewhere else...{/i}"

    jump secondbeach10

label secondbeach10:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
f "Molly..."
    a "What...was that all about?"
    r "Who cares? If she’s going to be a bitch to people, she should get treated like a bitch back."
    r "Otoha did literally nothing wrong. All she did was ask to play and Molly decided to fucking explode."
    o "…"
    t "I have never witnessed her act in such a way before."
    a "Maya...did you want to chase after her as well?"
    m "…"
    m "No. "
    m "Whatever it is, I doubt there’s anything I can do about it."
    sa "I..."
    sa "I don’t even...really know what-"
    r "Don’t bother, Sana. "
    r "I highly doubt it’s anything worth actually chasing after her for."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach8 = True

    "{i}Welcome to Lessons in Love!{/i}"

    if bonus == True:
        "{i}In Lessons in Love, you can trade in affection points for blowjobs.{/i}"
    else:
        "{i}In Lessons in Love, you can trade in affection points for hugs.{/i}"

    "{i}Also, girls cry a lot.{/i}"
    "{i}It’s really sad.{/i}"
    "{i}Let’s go help one feel better!{/i}"

    play sound "static.mp3"
    scene gamemenumin with flash
    stop sound

    "{i}Click the button to make Molly feel better!{/i}"

    menu:
        "Button":
            play sound "static.mp3"
            scene ayhh3 with flash
            scene ayhh14 with flash
            scene ayhh7 with flash
            scene ayhh1 with flash
            scene ayhh2 with flash
            scene mollybuthappier1 with flash
            stop sound

    "Lavender's blue, dilly, dilly "
    "Lavender's green "
    "When I am king, dilly, dilly "
    "You shall be queen"

    play sound "static.mp3"
    scene tree1 with flash
    scene tree2 with flash
    scene tree3 with flash
    scene treefall1 with flash
    scene mollybuthappier2 with flash
    stop sound

    "Who told you so, dilly, dilly "
    "Who told you so? "
    "'Twas my own heart, dilly, dilly "
    "That told me so."

    play sound "static.mp3"
    scene whygodwhy with flash
    scene whyme with flash
    scene whythesky with flash
    scene u with flash
    scene mollybuthappier3 with flash
    stop sound

    "Lavender's green, dilly, dilly "
    "Lavender's blue "
    "If you love me, dilly, dilly "
    "I will love you"

    "{i}Click the button once more!{/i}"

    menu:
        "Button":
            scene lessons
            stop music
            $ renpy.pause(10, hard=True)

            $ molly_love += 1

            "{i}Molly’s affection has increased to [molly_love]!{/i}"

            scene black

            "………"
            "……"
            "…"

            jump secondbeach9
...
```