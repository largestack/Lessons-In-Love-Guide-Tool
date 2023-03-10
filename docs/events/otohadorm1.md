# Conversations Outside of a Girls’ Dorm (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Man Who Would Be King](./nodokadorm1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Nodoka: Cracks in the Armor](./nodokalibrary1.md)
* [Otoha: Japanese Summer](./otohapark1.md)

## Event properties

* Id: otohadorm1
* Group: Otoha
* Triggered by label: nodokadorm1
* Chain sources: nodokadorm1
* Chain sources path: nodokadorm1

## Official wiki page

[Conversations Outside of a Girls’ Dorm](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohadorm1&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label otohadorm1:
    scene otohadark1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    o "Welp, that was fucking weird."
    s "You don’t actually need help carrying anything, do you?"
    o "No. I don’t actually need help carrying anything. "
    o "I just figured you could probably use a break after whatever the hell that was."
    s "I take it that means you don’t have any idea either?"
    o "Not a clue."
    o "Nodoka and me have been friends for a little while but we’re not like, {i}super{/i} close or anything."
    o "Like, it was a little weird how far she went to get me to move over here in the first place."
    o "So understanding her right off the bat is kind of too much for me to be able to do right now."

    scene otohadark2
    with dissolve

    o "But if I figure anything out, I’ll be sure to let you know."
    o "She’s not really one to ever explain herself, though. "
    o "I’ve heard similar stories in the past about how she’s taken things too far and wound up causing some people to feel really uncomfortable."
    o "We can probably just chalk it up to her being a weirdo, though."
    s "Well I’m definitely used to dealing with “weirdos” by now, so one more surely won’t change anything."
    o "Hey, man. You said it, not me."
    s "You can say it too, if you want. It’s not like I’d go around telling everyone that you called them weird."

    scene otohadark3
    with dissolve

    o "No no no. That’s not what I’m getting at."
    o "Like, yeah, you’ve got a truck load of...eccentric people in your class, but I think everyone has their own reasons for acting how they do."
    o "So I don’t mean they’re weird in like, a negative way or whatever. They’re weird in the kind of way that makes them interesting to talk to."

    if bonus == True:
        s "Sure. Though, trying to have someone admit that they want to hook up with everyone in a room isn't exactly the “good” kind of weird that you’re alluding to."
    else:
        s "I think Nodoka was probably just trying to start a dance team. That sounds like a thing she would do."

    scene otohadark4
    with dissolve

    o "I think what Nodoka was doing was a little more than that, dude."
    o "I’m pretty sure she was just seeing how far she could push you without you snapping back at her or whatever."
    o "You did pretty well, all things considered. "
    o "I’m just hoping she’s not up there feeling all weird about it now. "
    s "I’m pretty sure she’s just ordering pizza. I don’t think she cares too much about the aftermath."

    scene otohadark2
    with dissolve

    o "No, but the two people she’s up there with do."
    o "And she’s also really close to Futaba, so she might feel weird if she’s suddenly uncomfortable or something."
    o "I don’t know, man. I’m not great at this whole positive reinforcement thing. "
    o "I just want to make sure things don’t get weird again once we go back up."
    s "Not even the good kind of weird?"

    scene otohadark5
    with dissolve

    o "Pfft, no. Not even the good kind of weird."

    scene otohadark6
    with dissolve

    o "Is it too much to ask to just have a chill night with my friends?"

    if bonus == True:
        o "I just got here. I’m not ready for weird[teen]drama yet. Especially drama involving some dude who’s way too old to even be hanging around us."
        o "So thanks for not admitting to manipulating the entire girls' dorm or whatever it was that we’re assuming Nodoka wanted you to do."
        o "You made my life slightly easier by holding back."
        s "No problem. I’m going to ask that you rescind your comment about me being too old, though. That hurt."
        o "Dude, you’re totally too old. I’m not rescinding anything."
    else:
        s "At this college? Yes. Things are not allowed to be normal here."
        o "Sometimes, I wish we could all just hang out and eat white bread together."

    s "Your rationality regarding this topic isn’t something I normally deal with. I don’t know if I should be relieved or offended."
    o "Be whatever you want to be. That’s what my mom always says. "

    scene otohadark7
    with dissolve

    o "As long as “whatever you want to be” doesn’t include “musician,” of course."
    s "I definitely don’t think you have to worry about me pursuing that career path any time soon."

    scene otohadark6
    with dissolve

    o "Good. Last thing I need is some old guy showing up to one of my shows and stealing my entire audience."

    "A cold breeze forms from wherever it is wind comes from (My guess is the sky, but I’m sure it’s a little more complicated than that) and attacks the two of us outside of the dorm."
    "I rarely have extended conversations out here, but...they're kind of nice in a weird sort of way."
    "The good kind of weird, obviously."
    "We left any residual “bad” weirdness upstairs with one girl I can’t understand and two that I’m starting to."
    "Is it strange that I’m not sure which of those two categories Otoha fits into yet?"
    "I want to say that I get who she is and what she’s thinking-"
    "But if there’s anything I’ve learned from my time in Kumon-mi, it’s that you can never truly know anything."

    if bonus == True:
        "I’ve also learned that having sex with [teenager]s is awesome and suddenly feel the need to remind you of that."
        "I’m sure if Nodoka could hear my thoughts, she’d be smiling right about now."

    scene otohadark8
    with dissolve

    o "Hey. So, umm...there {i}is{/i} another reason I wanted to come down here with you."
    s "Otoha, if you wanted to confess to me, it would have been a lot easier to just do it during Nodoka’s rant before."

    scene otohadark9
    with dissolve

    if bonus == True:
        o "Dude, I already told you you’re way too old. "
        o "So old that I’m asking you for advice instead of asking you to like...hold my hand or whatever."
    else:
        o "Dude, no. I just want some advice."

    s "Advice? I feel like you’re going to regret this decision."
    s "I am very bad with advice."
    o "And I’m bad with a lot of stuff. But what the hell will avoiding it solve?"
    o "Worse comes to worst, I can just blame {i}you{/i} for my life falling apart and use that momentum to write some cool midwest emo shit or something."
    o "Rin would be all about that."
    s "Yeah. I understand exactly what you’re talking about right now."

    scene otohadark10
    with dissolve

    o "Good. Because Rin’s...kind of what I wanted to talk to you about."
    s "Ahh. Yeah, I guess that explains why you didn’t want her to tag along."
    s "So much for that thing you said about not talking about people behind their back, though."

    scene otohadark11
    with dissolve

    o "Yeah. So much for that..."
    s "So, what is it you want to know about her?"
    s "I don’t mean to brag, but I’ve gotten to know her pretty well over the definitely-only-one[school] year we’ve known each other for."
    o "Weird choice of words, but I’m just kind of curious about...I don’t know. What kind of person she is, I guess?"
    s "Do you not already know what kind of person she is by now? Don’t you two talk like all day, everyday?"
    o "It’s like, 80%% Rin talking and 20%% me figuring out how I'm supposed to reply. "
    o "I get that she’s nice and has her own problems that she’s still working out or whatever, but like...I’m kind of confused, you know?"
    o "Like, didn’t she like some other girl right before me? "
    o "It’s really flattering...all of the things she says about me. But I can’t help but feel like I’m just the flavor of the month or something."

    scene otohadark12
    with dissolve

    o "There are so many parks with so many girls."
    o "If she fell for {i}me{/i} so quickly...who’s to say that won’t happen again with the next rocker chick she lays her eyes on?"
    s "No one would say that won’t happen, because it very well may."
    o "Right? So then why should I believe-"
    s "Because you’re at the part of your life where what's happening right now matters a lot more than what’s going to happen in a few weeks."

    scene otohadark13
    with dissolve

    o "Wait. I am?"
    o "I thought I was at the part of life where I {i}should{/i} be thinking about my future."
    s "That’s what most people in my position would probably tell you. I work a little differently, though."
    s "I think the best way to ensure that your future winds up being something exciting is to live freely day to day."
    s "That way, you won’t have any regrets weighing you down once you get older."
    o "Okay but like, what about gaining experience and like...furthering my education and stuff."
    s "Two sacrifices that must be made in exchange for happiness."
    o "…"
    s "…"

    scene otohadark14
    with dissolve

    o "This is very bad advice, Sensei."
    s "Hey, no one is perfect. "
    s "Point is, if you want to learn more about Rin, learn more about her by spending time with her."
    o "I’m going to, totally. I think she’s really cool."
    o "I don’t know if I want to like, {i}date{/i} her, but being around her has been fun so far."
    o "She’s just kind of..."
    o "I don’t know. A little too much for me sometimes?"
    o "She has {i}a lot{/i} of personality."
    s "True. But so does Nodoka and you two seem to be doing well so far."

    scene otohadark15
    with dissolve

    o "I can’t help but feel like I do nothing but attract loud or...strange people."
    s "Have you tried taking some of your rings off?"
    o "What...would that do?"
    s "I don’t know. Make you seem less...cool?"
    o "I hope it’s a little more than just my jewelry that makes people gravitate to me."

    scene otohadark16
    with dissolve

    o "Who knows at this point, though? "
    o "It’s gotta be {i}something{/i} weird like that if I keep attracting so many girls."
    s "To be fair, there are a lot less guys around to attract now. "
    o "Ahh, yes. When in doubt, blame it on the space war. "
    s "It wouldn’t be the first time, I can tell you that."

    scene otohadark17
    with dissolve

    o "What would you do in my shoes, Sensei?"
    s "What do you mean?"
    o "About Rin. "

    if bonus == True:
        s "Oh. Uhh..."
        s "I think the complete answer to that question would be better received by someone like Nodoka rather than you."
        s "I’m not sure you’re prepared for what I’d say."
    else:
        s "I think you should love her and cherish her forever like the good girl you are."
        o "Thanks, Sensei."
        s "I also think you should both get mohawks. That's what I would do in your shoes."

    scene otohadark18
    with dissolve

    o "Uhh...no. Probably not, if that’s the direction you’re going to take things in."
    s "Hearing what I’d do shouldn’t influence you at all anyway. Live your life how {i}you{/i} want to. Not how someone else would."
    s "Whatever you do decide on, though, be gentle with her."

    if bonus == True:
        s "And I’m not talking sexually this time because she has so much pent up sexual frustration at this point that I don’t think being gentle would-"
    else:
        s "But if you {i}do{/i} wind up wanting a mohawk-"

    scene otohadark19
    with dissolve

    o "Dude."
    s "Sorry. I couldn’t help myself."

    scene otohadark20
    with dissolve

    o "It’s fine. I’ll be as gentle as I can with...whichever direction we wind up going in."
    o "I don’t want to hurt her. But I don’t know if I can make her happy either. "
    o "If I’m going to be making my own choices now, I shouldn’t be making any that I can’t get behind 100%% of the way."
    o "It’s kind of crazy to me how quickly some people are willing to jump into things like...confessing their feelings when I can’t even figure out what mine are."
    s "You write music don’t you? Maybe you’re just...using up all of your emotions on that?"

    scene otohadark21
    with dissolve

    o "Right. Because emotions are a finite resource that you can run out of if you use too many."
    s "You joke, but what if that’s actually true?"
    o "If that’s true, this world is an extremely sad place."
    r "Oh! There you two are."

    scene otohadark22
    with dissolve

    "This world {i}is{/i} an extremely sad place."
    "If it was any sadder, we’d all shrivel up and die."
    "Which I’m sure is something we’ve all felt like doing at least once or twice."
    "Maybe even thousands of times, depending on the person. "
    "Take these two, for example."
    "They’re both smiling, are they not?"
    "Which smile do you think is harder to maintain?"
    "The one belonging to the girl who wants to love, yet doesn’t know how? "
    "Or the one that belongs to the girl who doesn’t seem to be capable of {i}not{/i} loving?"
    "The correct answer is that both smiles are impossible to maintain."
    "Because this world is miserable."
    "And smiling at all is pointless when smiles die faster than anything known to man."
    "And yet-"
    "And yet they’re still so inexplicably beautiful."
    "Maybe tonight, outside of a building filled with dying smiles, I can convince myself to not wish these ones away."

    o "Yo. Welcome to the party."
    r "Thanks for having me. "

    scene otohadark23
    with dissolve

    r "What are you guys up to? You’ve been down here for a while."
    o "Just hanging out. "
    o "I had some stuff I wanted to ask him and was afraid Nodoka was going to pounce on him if he hung around any longer."
    r "Yeah, that was weird. She seems fine now, though."
    r "You look a little happier than normal, Sensei. Did talking to Otoha put you in a good mood or something?"
    s "Me? Looking happy? Are you forgetting who I am, Rin?"
    r "Hmm...It could just be the light, I guess."

    scene otohadark24
    with dissolve

    r "Oh. We decided on pepperoni, in case you were wondering. "
    r "I’m sure that’s been on your minds since the two of you came down here so...I just thought I should come let you know and stuff."
    o "Thanks, Rin. We were about to head back up anyway, though."
    s "Nah. You two go. I’m going to head home."

    scene otohadark25
    with dissolve

    r "Wait, I didn’t mess anything up by showing up at a weird time, did I?"
    r "I was just...feeling like a third wheel up there and...wanted to be with you two instead."
    o "You don’t have to leave, Sensei. You can come back up if you want."
    s "It’s fine."

    if rindorm45 == True and rinbetrayed == False:
        s "Besides, the last time I ate pizza with Rin, something happened that I probably shouldn’t talk about."

        scene otohadark26
        with dissolve

        r "Ah! Hey!"
        r "Why are you bringing that up now of all times?!"
        s "Because it’s more fun to leave after making you flustered."
        r "Sensei! Come on!"
        o "…"

    s "Ami’s probably waiting for me at home anyway. It’s already pretty late."

    scene otohadark27
    with dissolve

    o "Ami?..."
    o "You mean...the Ami from our class?"
    o "Does that...mean what I think it means?..."
    o "I thought hanging around Rin meant you liked girls a little less...you know..."
    s "Ami is my [niece], Otoha."
    o "…"
    s "…"

    scene otohadark28
    with dissolve

    if bonus == True:
        o "I knew that!"
        o "I was just kidding anyway!"
    else:
        o "Is that supposed to explain things better?! Because it really doesn't!"

    r "…"
    s "What are {i}you{/i} looking at?"
    r "It’s...really not because of me?"
    s "It’s totally because of you."
    s "But also because of some other stuff."
    r "I...really don’t care if you stay, you know. I wasn’t trying to get rid of you by coming down here or anything."
    s "Don’t worry about it. Just tell the others that I said goodnight."
    s "And tell Nodoka to deposit whatever points I wound up earning tonight into my account. She knows the bank information."

    scene otohadark29
    with dissolve

    r "Roger that! Quest accepted!"
    o "Uhh...well, goodnight I guess?"
    o "We should...talk again sometime, if that’s cool."
    o "It’s weirdly relaxing talking to an adult who isn’t telling me to do my homework. Even if that adult is my teacher and probably {i}should{/i} be telling me that."
    s "Homework is for losers."
    s "Goodnight, you two."

    scene otohadark30
    with dissolve

    r "Goodnight! Be safe on the way home, okay?"
    o "Goodnight, Sensei. I’ll...see you in[school], I guess."

    scene black
    with dissolve2

    "I leave the dorms without the need to stomach the strange sensation that comes with sneaking around."
    "To walk down several flights of stairs in hopes of not being spotted by someone I wasn’t there to see."
    "It’s one of the very few positive sides to conversing outside rather than in someone’s bedroom."
    "And while it’s not something I expect to become a regular occurrence, it made sense this time around."
    "And I didn’t even have to carry any boxes."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohadorm1 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadorm5:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```