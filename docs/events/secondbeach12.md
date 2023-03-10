# Left Out in Light (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Into the Woods](./chikalust20.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach12
* Group: Main
* Triggered by label: secondbeach11floor2
* Chain sources: chikalust20
* Chain sources path: chikalust20->chikalust20

## Official wiki page

[Left Out in Light](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach12&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach12:
    $ totaldays += 1
    $ day = 7
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date


    "{i}You manage to sleep through the night.{/i}"
    "{i}But you dream of nothing.{/i}"

    scene norikowakeup1
    with dissolve2
    play music "wewereangels.mp3"

    "I walk outside to be met with a rather mysterious temperature given how the air felt in this exact place less than twelve hours ago."
    "It’s actually warm out this morning."
    "And while I don’t know if this is just some strange coincidence or a sign from a god I don’t believe in, I accept it."
    "Also, if this {i}is{/i} a sign, whoever that god may be is making a pretty good argument for itself right now. "
    "I applaud him or her or it for waiting for such a good opportunity to grant us warmth, for I now have a significantly higher likelihood of seeing girls in less clothing for the duration of the day."
    "But then the wind blows and sprays my blazer with a thin layer of mist and I go back to hating any and all gods that may or may not exist or whatever."
    "Oh, and then Noriko shows up."

    play sound "static.mp3"
    scene norikowakeup2 with flash
    stop sound

    n "Hey! Good morning!"
    n "Did you sleep well?"

    if dormwarfloor2win == True:
        s "Kind of, I guess."
        s "I was a little surprised to not see you there when I woke up, though."

        scene norikowakeup3
        with dissolve

        n "Yeaaaaaah...as it turns out, I may have cuddled you a little too hard and some of the girls thought it was kind of weird and asked me to stop."

        scene norikowakeup4
        with dissolve

        if bonus == True:
            n "But, on the bright side, I didn’t drug you this time! You were totally knocked out by your own doing and I, in no way, had anything to do with you sleeping in so late and so heavily."
            s "Saying it like that does make you seem a little suspicious, though."
            n "I tend to say a lot of stuff that makes me seem more suspicious than I actually am. It’s kind of my thing."
        else:
            n "But, on the bright side, no sleeping potions were involved this time!"

        s "So, what then? You all just decided to let me stay in there by myself instead of swarming me?"

        scene norikowakeup2
        with dissolve

        n "Pretty much, yeah."
        n "Touka got up first to go for her morning walk or something and then came back in telling us all how nice it was outside."
        n "The rest is pretty much history, I guess."
        n "Io kicked you a few times to see if you’d wake up, but you were like {i}out of it{/i} out of it, if you know what I mean."
        s "I’m pretty sure you mean I was out of it."
        n "Yup! That!"

    else:
        s "Kind of, I guess."

        if bonus == True:
            s "Ami and Ayane had a little trouble sharing me and I’m pretty sure Chika wound up staying awake the entire night to make sure neither of them went too far."
        else:
            s "Chika rubbed my tummy and made me warm milk after Ami and Ayane scared me."

        scene norikowakeup5
        with dissolve

        n "Really? That’s super cool of her."
        n "I’m sure she had her own reasons that I would be very upset to hear, but I’ll still probably thank her anyway."
        n "I realized again last night just how much Ayane likes you, so it makes me a little happy knowing nothing {i}really{/i} intense went on during the sleepover thingy."
        s "You were with Ayane last night?"

        if bonus == True:
            n "Yeah. We talked about masturbating and stuff."
        else:
            n "Yeah. We talked about tongues and stuff."

        s "I can very much see how that would lead to you reaffirming her feelings about me."
        s "You’re not worried about Ami, though?"

        if bonus == True:
            n "Not really. Ami’s part of the family and will never marry you or have your babies or anything, so if you two want to secretly go at it without anybody knowing, I guess that’s fine."
        else:
            n "Not really. I'm kind of hoping she'll become my accountant one day, so...yeah."

        if amifingered == False and bonus == True:
            s "Luckily for you, I can’t see that happening anytime soon."
            s "Or...ever, for that matter."
            n "That {i}is{/i} lucky for me! But very unfortunate for Ami. "
            n "Here’s hoping she doesn’t wind up resorting to the same thing I did when I was little and the person I liked was already interested in somebody else."
            s "What did you do when you were little, exactly?"
            n "Not telling. But something tells me you probably would have found out if my floor won the dorm war."

        else:
            s "That really wouldn’t bother you?"

            scene norikowakeup6
            with dissolve

            if bonus == True:
                n "Well...okay, yeah. It would bother me a little."
                n "But the idea of you with {i}anyone{/i} bothers me and Ami’s not really any different from the rest."
                n "But I’m also willing to accept that you’re able to make your own decisions and that I’m not an absolute choice or anything despite how much I want to be, sooooo...yeah."
                n "I’ve just gotta get you to like me more, I guess. I don’t know."
            else:
                n "Why would I hire someone who would bother me?"

        scene norikowakeup7
        with dissolve

        n "Wait, why are we even talking about this? Tell me about the rest of the night."
        n "I thought about coming to visit, but Makoto caught me as I opened the door and said a whole bunch of stuff about “accepting defeat” and then kicked me out."
        s "It was...fine. A little anticlimactic, but fine."

        scene norikowakeup6
        with dissolve

        n "I see..."
        n "Well...maybe we’ll get to do this again some day and you’ll wind up staying with us next time?"
        n "I wonder if...by then, we’ll be..."
        s "…"
        n "…"
        s "Be what? Finish your sentence."

        scene norikowakeup4
        with dissolve

        if bonus == True:
            n "Nah. I’ll just show you what I mean soon instead."
            s "Right..."
        else:
            n "Hug...buddies?..."
            s "=D !!!!!!!!!!!!"

    s "So, that aside, what’s the plan for today?"

    scene norikowakeup8
    with dissolve

    n "Plan? Are we supposed to have one of those?"
    n "I think we were just gonna do whatever. "
    n "I know a lot of the girls are back over where they keep the picnic tables and stuff, so I was gonna head over there soon if you wanted to come."
    n "I’m sure basically all of them would be happy to see you."
    s "Sure, that sounds-"

    scene norikowakeup9
    with dissolve

    ni "…"
    s "…"
    n "Hm? That sounds {i}what?{/i} Why did you stop?"
    s "There’s, uhh...an idol behind you."
    n "An...idol?"

    scene norikowakeup10
    with dissolve

    n "Ah! Nee-chan! I didn’t know you were here!"
    ni "Are you fucking kidding me? Yes you did."
    ni "How many beaches do you think there are in Kumon-mi?"
    n "More than one? I don’t know. I’ve never counted them before."
    s "What’s going on here?"

    scene norikowakeup11
    with dissolve

    ni "That’s what I should be asking you, dick!"
    ni "{i}This{/i} is why you couldn’t see me this weekend? Because you were going on a romantic getaway with my little sister?"

    if bonus == True:
        ni "You realize how old-"
        n "Yup! Sensei knows so there’s no reason to continue that sentence."
    else:
        n "Yup! We've had this planned for months."

    scene norikowakeup12
    with dissolve

    ni "You are playing a dangerous game, Noriko. Remember who’s paying for your phone."

    if bonus == True:
        n "Oh, come on. You hogged him for the first like...six million years of our lives. It’s my turn to get some time with him now that I’m not in training bras anymore."
    else:
        n "Oh, come on. You hogged him for the first like...six million years of our lives. It’s my turn now!"

    s "If it’s any consolation, Niki, I am also paying for the phone bill of several [high_school]ers."

    scene norikowakeup13
    with dissolve

    ni "How is that consolation?! That’s fucking weird!"

    if bonus == False:
        ni "Also, what the fuck is a collegeer?! No one calls them that!"

    "Niki takes off her fancy sunglasses and tosses them into a bag positioned off screen. I promise it is there."

    ni "Also, no one has told me why you two are together yet! "

    if bonus == True:
        n "You guessed it correctly the first time, Nee-chan. Sensei and I are on a romantic getaway and were moments away from christening every room in this here inn."
    else:
        n "You guessed it correctly the first time, Nee-chan. Sensei and I are on a romantic getaway."

    scene norikowakeup14
    with dissolve

    ni "There better be a good fucking explanation for this or neither of you two are leaving here alive. "
    s "It’s just some[school] trip thing. Don’t kill me. "
    s "A better question is why {i}you{/i} are here. Don’t you have like...idol stuff to do or whatever?"

    scene norikowakeup15
    with dissolve

    ni "Why yes, I do. Thank you for asking and acknowledging my...awesomeness."
    ni "I’m actually here {i}because{/i} of “idol stuff.”"
    ni "I have a photoshoot for a swimsuit calendar this afternoon and the agency managed to snatch up a room at this inn from some rich family who bought the rest of them. "
    s "I see. And where will I be able to purchase this calendar?"

    if bonus == False:
        s "I think it would make an excellent Christmas gift for my accountant."

    scene norikowakeup16
    with dissolve

    ni "Heh. I’ll see if I can use one of my many, {i}many{/i} connections to get you one once it’s printed."
    n "Um, hello? Cute girl literally {i}in{/i} a swimsuit right next to you two in search of praise. Send help."

    scene norikowakeup17
    with dissolve

    if bonus == True:
        ni "Not much I can do until you grow a little bit more, Noriko. Don’t blame me for being significantly more attractive and adored by all."
    else:
        ni "Oh, hi. I didn't see you there."

    n "{i}I know where you sleep, bitch.{/i}"
    s "So, since you’re going to be doing a photoshoot or whatever, does this mean you won’t have any free time?"

    scene norikowakeup18
    with dissolve

    ni "The only free time I have is literally right now. I’m on a tight schedule- which is exactly why I tried to tell you about this ahead of time. "
    ni "But no. You already made plans with my sister because you subconsciously want to be reminded of me without having to admit that you were wrong for abandoning me years ago."

    if bonus == True:
        n "Or...and hear me out here...maybe his tastes just haven’t changed since he was a [teenager]."
        ni "They sure fucking better have. "
    else:
        n "Or...and hear me out here...maybe I've been the true huggy girl all along?"

    s "Can you at least come say hi to a few of the girls? I know at least two of them would be really excited to see someone as...awesome and amazing as you."

    "I obviously don’t remember much about Niki (Assuming any of my background is true) but, the one thing I absolutely {i}do{/i} know is that her ego is very easily stroked."
    "And, just like with the whole thing about paying for[teen]phone bills, I can relate."

    scene norikowakeup19
    with dissolve

    ni "Well, duh. I’m Niki Nakayama. It would be weirder if there {i}weren’t{/i} girls excited to see me."
    ni "But even though I have a {i}little{/i} free time, it’s not like I can just go wherever you want to take me and-"
    n "Ami should be there, Nee-chan."

    scene norikowakeup20
    with dissolve

    ni "Ah..."
    n "She’s a big fan, too. She’s been listening to you this whole time. "

    scene norikowakeup21
    with dissolve

    ni "Mnh..."
    s "Is that really all it takes to sway her?"
    n "Nee-chan spent years worrying about you and Ami after what happened."
    ni "Even though you couldn't have cared any fucking less about what I was or wasn’t worrying about."
    ni "Besides, it’s not like she’ll remember me as {i}me{/i} when I only met her once or twice. She’ll just see me as...Niki."
    s "But...you are Niki."

    scene norikowakeup22
    with dissolve

    ni "You know that’s not what I mean. "
    s "Sure, she’ll probably ask you for an autograph and...cry or something. But if you really were worried about her, wouldn’t you want to at least see who she is or...what she looks like now?"

    scene norikowakeup23
    with dissolve

    n "I’m with Sensei on this one."
    n "In fact, I’m enforcing the Nakayama Sisters’ Rule #74 at this very moment. You are unable to refuse."
    ni "Rule #74 at a time like this? But...what would I even say? "
    ni "“Hi, Ami. I’m a famous idol you listen to on the radio, but I’m also your [uncle]’s ex and have been worried about you for years. Want to take a selfie together?”"
    s "Can I just quickly touch on the fact that you two have an absurd amount of rules? What does rule #74 even do?"

    scene norikowakeup24
    with dissolve

    nni "Nakayama Sisters’ Rule #74: If a Nakayama sister believes the other is making a decision they will regret, they can enact this rule to strip them of free will and force one to act for the other."
    s "Okay, first off- you two are creepy."
    s "Secondly, how old were you when you came up with that? I thought this was going to be a kid thing at first, but that was a very professionally worded rule."

    scene norikowakeup25
    with dissolve

    ni "It’s more like a law, I guess. But it wouldn’t exist if there wasn't a reason for it, so..."
    ni "If Noriko is going to enact Rule #74 now, I don’t really have a choice other than to go along with it."
    s "Having a sister sounds exhausting."
    nni "It is."

    scene norikowakeup26
    with dissolve

    nni "Pfft..."
    s "...?"

    scene black
    with dissolve2

    "The Nakayama sisters erupt into a fit of laughter as I am left to stand beside them, wondering how far back this goes and whether or not it’s something I ever found out about."
    "Perhaps in a previous life-"
    "Perhaps then, I would have understood more about their silly rules."
    "About what their relationship is with not only each other, but with me and the girl Niki was apparently so worried about for years."
    "It must have been hard having to live with those thoughts."
    "I wonder why, if that person from back then was actually me-"
    "I wonder why they locked her out."
    "She seems kind enough."
    "Sure, she’s a stuck up princess but, if what I understand about her is correct, isn’t she only like that because of me?"
    "If so, why did I leave her behind?"
    "Everything I learn about those two makes the past seem brighter-"
    "But perhaps the issue is that it’s becoming so bright that it’s too blinding to see anything else."
    "And perhaps the reason Maya is so hesitant to me finding out any more about it is because its inescapable light will consume the world I’m in now."
    "Maya is in that world, so I don’t blame her for not wanting to be consumed."
    "But I also shouldn’t be blamed for occasionally quelling the misery of others when it requires minimal effort on my end in order to do so."
    "All I’m doing is walking down the beach with two cute girls who love me."
    "Well, one cute girl who loves me and one other cute girl who hates me."
    "But also loves me."
    "Probably."
    "And if the three of us happen to bump into one more girl who loves me-"
    "One more girl who goes back just as long as the two of them, if not longer-"
    "If that happens, it will just be a coincidence."
    "It will not be my fault."
    "Nothing is ever my fault."

    scene norikowakeup27
    with dissolve

    n "Onward! To [niece]hood!"
    ni "Are you really just going to let her pull you along like that?"
    s "I...guess so?"

    scene norikowakeup28
    with dissolve

    ni "Hah...you’ve always been too nice to her. You just let her do whatever she wants."
    ni "No wonder she’s this obsessed with you now instead of chasing after someone actually worth the time and effort."
    s "Sorry, but aren’t you the same Niki Nakayama who tried to invite me on a work trip because she couldn’t get enough of me?"

    scene norikowakeup29
    with dissolve

    ni "Of course not."
    ni "I’m the Niki Nakayama who tried to invite you on a work trip because I didn’t want to carry my own luggage."
    ni "But it’s fine now. I just got one of the people from the agency to do it instead. I don’t need you anymore."
    s "Then I guess I’ll just go back to enjoying my romantic getaway with your little sister and-"

    scene norikowakeup30
    with dissolve

    ni "Yeah, yeah. Do whatever you want. I know you’ll come crawling back soon enough."
    ni "Just keep on walking, [nikitemp]. You have a grand total of roughly ten minutes with me and you shouldn’t be wasting them on your textbook sarcasm."
    s "..."

    scene black
    with dissolve2

    "I begrudgingly do as I’m told and shut my mouth, though I’m not sure why."
    "We continue walking along the shoreline together until the entrance of the beach and its accompanying picnic tables come into view."
    "And in the hundreds of seconds it takes to get there, not one feels out of place."

    $ renpy.end_replay()
    $ niki_love += 1
    $ noriko_love += 1
    $ secondbeach12 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach13

label secondbeach13:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
s "That does sound likely, yes."
                n "Yeah. And it would turn into a whole thing where I’d wind up losing my virginity and being really loud and waking everybody up."
                n "Unless you wanna go back to your room and-"
            else:
                n "True. But it's comforting knowing the huggy boy is so much larger than me. It will make the hugs feel more important."
                s "Call me the huggy boy again. It warms my heart."
                n "You are the huggy boy."

            ki "Noriko, shut the fuck up. I’m trying to sleep."

            scene floor2sleepover53
            with dissolve

            n "No! You shut up! This is a big moment for me!"

            if bonus == True:
                ki "You like Sensei. We get it. Can’t you just sleep quietly or whatever?"
            else:
                ki "He is the huggy boy. We get it. Can’t you just sleep quietly or whatever?"

            n "Aren't you supposed to be swimming right now?!"

            scene floor2sleepover52
            with dissolve

            n "So anyway, where were we?"
            n "Oh right. Spoons."

            if bonus == True:
                n "If you hate being the little spoon that much, just make sure you do an awesome job as the big spoon next time."
                n "And hey, who knows? Maybe I won’t have my pants on then and we'll be in a place where it's actually safe to put it in?"
            else:
                s "Such a great utensil."
                n "They're okay, I guess."

            s "That’s a horrible thing to say to someone right before going to sleep."

            scene floor2sleepover54
            with dissolve

            n "That’s fine. "

            if bonus == True:
                n "I heard that if you go to sleep hard, you’ll have sex dreams. "
                n "Besides, maybe you’ll get lucky and I’ll subconsciously reach my hand down a little too far and give you a sleep-handie or something."
                s "This isn’t helping."

            n "I love you, Sensei."

            if bonus == True:
                s "Noriko, you-"
                s "Oh. Wait. That helped."
                n "Are you telling me you got soft from hearing me say I love you?"
                s "Not soft. Just soft{i}er{/i}."
                n "So mean."
            else:
                s "I will never love anyone who thinks spoons are just {i}okay.{/i}"
                n "Is that so, huggy boy?"

            ki "Noriko, oh my fucking God."

            scene floor2sleepover53
            with hpunch

            n "FUCK OFF, KIRIN! JESUS."

            scene black
            with dissolve2

            "Noriko makes small talk for a while longer, but I eventually find my consciousness fading."
            "It feels strange falling asleep with the arms of someone other than Ami or Ayane wrapped around me, but I guess if anyone was going to be next in line, it’s another girl I’ve known forever."
            "Sure, it would probably make a little more sense if it was her sister instead, but given the...pattern of girls I’ve been seeing, Noriko definitely fits the bill."
            "And even though I’ve been forced into the position of the little spoon, I don’t really feel out of place."
            "Then again, I don’t feel {i}in{/i} place either."
            "I just kind of...feel, I guess."
            "Which is more than I can say most of the time."
            "…"
            "Somehow, Noriko falls asleep before I do."
            "I follow her into the darkness shortly after."

            $ renpy.end_replay()
            $ secondbeach11 = True
            $ molly_love += 1
            $ tsuneyo_love += 1
            $ uta_love += 1
            $ io_love += 1
            $ otoha_love += 1
            $ nodoka_love += 1
            $ touka_love += 1
            $ yasu_love += 1
            $ kirin_love += 1
            $ noriko_love += 1
            stop music fadeout 7.0

            "{i}Your affection with everyone on the second floor has increased by 1!{/i}"
            "………"
            "……"
            "…"

            jump secondbeach12
...
```