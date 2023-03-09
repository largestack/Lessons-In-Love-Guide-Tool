# A Woman's Heart
Sara event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=saradate1&go=Go)



## Event preconditions
✅Sara love greater than or equal to 0

✅Event "[Sana: Carry Me Home](./bar15.md)" is completed (event=bar15)

✅saranumber equal to True (unknown variable)



## Next events
* [Sara: Third Wheel](./sarainvite1.md)
* [Sara: A Mostly Empty Home](./sarainvite2.md)

## Event properties
* ID: saradate1
* Group: Sara
* Triggered by label: callsaraafternoon
* Triggered by branch label: callafternoon

## Event code
File: \game\SaraEvents.rpy
Code:
```python
...
label saradate1:
    "I guess it wouldn’t hurt to give Sara a call. "
    "I’ve been meaning to get to know her a little better, and it’s not like I have anything else planned for the day."

    play sound "phonebeep.wav"

    "I pull my phone out of my pocket and press on her name in my contacts."
    "It rings a few times before she finally decides to answer."

    play sound "phonebeep.wav"

    sar "Helloooo? Who's this?"

    "Oh, right. I never gave her my number."
    "I just plugged hers into my phone after she wrote it on a receipt that one night and have been leaving it alone ever since."

    s "It’s your daughter’s teacher. What are you up to right now?"
    sar "Oh, hey! I was starting to think you’d never call me."
    sar "I’m just setting up the bar right now. Why?"
    s "I’m looking for something to do and was wondering if you’d want to go out."
    sar "Like, now? Tonight? "
    s "Yeah. But if you have to set up the bar, it’s-"
    sar "No no no no! I’d love to hang out. I can just have Sana finish setting up when she gets here."
    sar "I’ll tell her I went out to buy groceries or something."
    s "Are you sure that’s okay?"
    sar "Of course! Is there anywhere you’d want to meet?"
    s "Let’s just walk around the city or something. I’ll text you an address and we can meet there in around an hour."
    sar "Sounds good! See ya soon~"

    play sound "phonebeep.wav"

    s "…"

    "It is just then that I realize I don’t know the address of any specific place in the city."
    "…"
    "I guess I’ll just have to look up a random building and have her meet me there."

    scene black
    with dissolve

    "I take a few minutes to research notable locations in the urban district of Kumon-mi and,
    after finding one rather large looking building, decide on that as our meeting spot."
    "………"
    "……"
    "…"

    scene saradate0
    with dissolve
    play music "normalday.mp3"

    "I show up in the designated spot before Sara, which is a good sign. "

    if bonus == True:
        "Obviously, the two of us aren’t formally dating or anything like that, but it still feels good to have done something right by today’s standards."
        "I’ve gotten so used to letting my immoral side take over that small things like showing up on time to a date are all that’s left to make me feel like a good person."
        "And if Sara were a character in an anime, I’m sure she’d be just as impressed as I am with myself right now."
    else:
        "I don't go into the city by myself often, so I was very worried that I was going to get lost and be abducted by a stranger."

    scene saradate1
    with dissolve

    sar "Hey there, stranger~"
    sar "Did I keep you waiting long?"

    "This is the part where the guy normally says “No, not at all,” despite arriving half an hour early or something along those lines."
    "Just, in this case, I really {i}did{/i} just arrive a few minutes ago."

    s "Nah. I just got here myself."

    scene saradate2
    with dissolve

    sar "Awe~ You’re not just saying that to make me feel bad about being a little late, are you?"
    s "I’m not. I really did just get here."
    sar "Right, right..."
    sar "Well, I guess I’ll play along if it’ll make you happy."

    scene saradate3
    with dissolve

    sar "Would you, uhh...mind explaining why we’re meeting in front of {i}this{/i} place,
    though? This isn’t really a typical meeting spot."

    "I turn to the side to see that we're in front of the headquarters for some unfamiliar cell phone company. "

    if bonus == True:
        s "Uh...Nothing turns girls on quite like...multi-billion dollar corporations, right?"

        scene saradate4
        with dissolve

        sar "Woooow. Who is it that spilled the secret to a woman’s heart to you, [saramaster]?"
        s "Just something I picked up over the years, Sara."
        sar "I can tell. I’m so horny now. Please make love to me beneath the giant 5G banner towering over us."
        s "I’m afraid I can’t. 5G Causes cancer and I couldn’t possibly do that to someone as beautiful as you."
        sar "If it’s for you, [saramaster], I’d let you do me under {i}6G{/i}."
        s "…"
        sar "…"
        s "This is possibly the strangest flirting exchange I’ve ever been involved in. I feel like I should apologize."
    else:
        s "I am sorry. This is a terrible date. Feel free to leave now."

    scene saradate5
    with dissolve

    if bonus == True:
        sar "No! Don’t apologize! That was totally fun."
        sar "It made me feel [young]again."
        s "Aren’t you only like 30? That’s still really young."
        sar "I guess by mom-standards, yeah. But I’m no [teenager] anymore, that’s for sure."
    else:
        sar "No, no! It's totally fine. I like cell phones and I like you."

    scene saradate6
    with dissolve

    sar "So please continue to flirt with me~ I would very much appreciate that."
    s "That I can do, Sara. That I can do..."

    scene black
    with dissolve

    "The two of us wind up walking around the city for about an hour or so, stopping at a few convenience stores along the way to buy Sara candy."
    "Yes, apparently she really likes candy. And I mean {i}really{/i} likes candy."
    "In fact, she’s almost like a little kid any time we pass a store that sells chocolate."
    "I even needed to talk her out of going into a few of them given just how many shops there are around here that sell things like that..."

    scene saradate7
    with dissolve

    sar "Wow. We’ve been together almost a full hour and you’re not bored of me yet."
    sar "Maybe we {i}are{/i} meant to be together after all."

    if sarasex == True:
        if bonus == True:
            s "Well, it’s not like we haven’t already {i}been{/i} together, if you catch my drift."

            scene saradate8
            with dissolve

            sar "Not like that, perv! I meant like, you know, as a {i}thing{/i}."
            s "Like...friends with benefits?"
            sar "No! Like..."
            sar "Like I could be your girlfriend. Or something."
            s "This is the first “date” you and I have gone out on and you already want to be my girlfriend?"
            s "Doesn’t that seem a little premature?"
        else:
            s "Well, it’s not like we haven’t already hugged, so..."
            sar "I'm gonna poke your face now."
            s "What? Why? That's entirely unnecessary."

        scene saradate9
        with dissolve

        sar "Whaaaat? No way! I don’t think so at all."
        sar "I mean, you seem pretty tolerable of me and stuff. And you’re cute."
        s "Sara. Why are you poking my face?"

        scene saradate10
        with dissolve

        if bonus == True:
            sar "Oh, and your penis is super big and I don't think I could ever go back to a normal size one now~"
            s "Sara. Hands. There’s an entire family like ten feet away from us."

            scene saradate9
            with dissolve

            sar "Sorry. Heheh~"
            s "You’re still poking me..."
            sar "What’s wrong with a little poking? Am I not allowed to have fun on my day off?"
            s "This isn’t your day off. You just pawned work off on your daughter so you could hang out with me."
        else:
            sar "I heard somewhere that there is a special pressure point inside of the face that can force someone to fall in love with you when poked."

        scene saradate11
        with dissolve

        sar "And I wouldn’t have done that if I didn’t want you to be my new boyfriend."

        "Okay, so...I know Sara and I are close to the same age. And dating in our age group is a lot different than it is when you’re a [teenager]."
        "But even by those standards, she’s still coming on strong."
        "Either she’s incredibly lonely, or she just really {i}really{/i} likes me for some reason beyond my comprehension."

        s "Let’s just...hang out a few more times before committing to anything, okay?"

        if sarainterest == True:
            sar "Why?~ Haruka already told me you like me. Don’t you wanna make sure no other handsome teacher can come sweep me away?"
            s "I’m pretty sure I’m the only male teacher in the[school], so I don’t think that will be an issue."

        else:
            sar "Boo~ You’re no fun, [saramaster]."

        sar "I guess if you’re not ready to date, though, that’s fine. I get it."

        scene saradate12
        with dissolve

        sar "We both have other people that are important to us that we should focus on."
        sar "I have my daughter...You have your [niece]..."
        sar "And I can’t imagine they’d feel normal about becoming related all of a sudden."
        s "Yeah, I can’t imagine that e-"
        s "Wait, related? I thought we were just talking about dating."

        scene saradate7
        with dissolve

        sar "For now. Heheh~"
        s "…"

    else:
        s "I..."

        "I think back to when I turned Sara down in her apartment a while back."
        "I still don’t fully understand what it was about that situation that made me say no to her, but..."
        "I can’t help but wonder if that’s had any sort of impact on how she sees me?"
        "Judging by the flow of the conversation so far, it certainly doesn’t feel that way."
        "But...oh well. I guess it’s just part of human nature to wonder about things like this."
        "I’m sure it’s no big deal."

        s "Are you sure you’d even want to date someone like me?"

        scene saradate13
        with dissolve

        sar "Are you sure you {i}wouldn’t{/i} want to date someone like me?"
        sar "Because if you’re thinking I’m the type who just throws herself at everyone...I’m really not."
        sar "I just...kind of feel comfortable with you for some reason."

        scene saradate14
        with dissolve

        sar "But I know you’re not realistically thinking of me that way, so we can just move on. I’m
        sorry for taking the joke too far."

    scene saradate14
    with dissolve

    sar "Um, all that stuff aside, I’ve actually been wondering something lately."
    sar "You know how you’ve been coming to the bar a lot?"
    sar "Is there anything you think I should be doing that I’m not already doing?"
    sar "The place is going downhill fast and I’m not really sure how long I can keep going at this rate."
    s "What makes you think I know anything about running a bar?"
    sar "Nothing at all! But from a customer’s perspective, you seem to keep coming back. And
    I doubt it’s just because of my daughter and me."
    s "…"
    sar "…"
    s "…"

    scene saradate15
    with dissolve

    sar "Wait a second! It {i}is{/i} because of my daughter and me!"
    s "I thought that was pretty obvious..."

    scene saradate16
    with dissolve

    sar "Ugh! I’m doomed after all!"
    sar "We were fine until all of the men started disappearing, but now it's like we're imploding or something!"
    sar "I can’t rely on our cute faces to keep the place open, can I?!"
    s "I’m sorry to stray away from the topic at hand, but that face makes you look a lot more like Sana than normal."

    scene saradate15
    with dissolve

    sar "She’s my daughter! Of course we look alike!"
    sar "Now, back to talking about the bar! "
    sar "What should I do to make it better?!"
    s "I am {i}not{/i} qualified to answer this question. I’m not even qualified to help
    Sana with her social skills and I’m somehow doing that."
    s "I’ve pretty much exhausted my ability to help."

    scene saradate17
    with dissolve

    sar "Well..."
    sar "Can you at least keep coming by and spending lots of money then?"
    s "…"
    sar "Pleeeeeeeease?"
    s "I was never going to stop in the first place..."

    scene saradate18
    with dissolve

    sar "Yay! More time with [saramaster] and more money for rent! You’re officially my favorite customer!"
    s "Well, thanks. But at least wait until you have a few more to give me that title. It feels kind of meaningless as-is."
    sar "Nope. Title’s all yours. No refunds. Sorry~"

    scene saradate19
    with dissolve

    "The conversation suddenly comes to a halt as Sara’s excitement turns into a mix between
    what seems like appreciation and admiration. "

    sar "Um..."
    sar "I had a really good time today."
    sar "We can...do this again, right?"
    sar "I really don't want this to be like...a one time thing."
    s "Sure. I had fun too."
    s "How about I just call you the next time I’m free and we do something again then?"
    sar "...Yeah."
    sar "Yeah, I’d like that a lot..."

    scene black
    with dissolve2

    "The two of us get off the bench a few minutes later and begin the journey home."
    "We wind up splitting apart near the halfway point so neither of us are forced to walk in the direction opposite our respective homes."
    "Sara returns to the bar, while I return home to grab a change of clothes and something to eat..."
    "All things considered, today was a good day."
    "Sara is certainly...{i}fun{/i}, if not anything else..."

    $ renpy.end_replay()
    $ sara_love += 1
    $ saradate1 = True
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label saralust5:
...
```

## Code that triggers this event
File: \game\SaraEvents.rpy
Code:
```python
...
label callsaraafternoon:
    if saranumber == True and bar15 == False:
        "I think I should probably get to know Sara a little better before calling her."
        jump callafternoon
    if sara_love >= 0 and bar15 == True and saradate1 == False:
        jump saradate1
...
```