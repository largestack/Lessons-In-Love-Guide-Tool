# Smile Guide (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Prisoner](./ayanelust10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation13
* Group: Main
* Triggered by label: prisonerx
* Chain sources: ayanelust10
* Chain sources path: ayanelust10

## Official wiki page

[Smile Guide](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation13&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation13:
    q "...sei?"

    "I feel a light tapping on my shoulder. Like someone is trying to wake me up but is a little worried about doing so."

    q "Can we...talk for a little while?..."
    s "…"

    scene rinintheinn1
    with dissolve
    play music "lastdailysong.mp3"

    s "...Rin?"
    r "I’m sorry to wake you up..."
    r "I just...wanted to come see you for a little while..."

    scene rinintheinn2
    with dissolve

    "I come to my senses to find a teary-eyed Rin near the side of the bed, nervously tugging on the sheets and glancing around the room."

    s "Is something going on?"

    scene rinintheinn3
    with dissolve

    r "Maybe..."
    r "I don’t know."
    r "I mean, technically, nothing has happened yet."
    r "But a thing might happen and I’m nervous and I’m panicking and I kind of just wandered in here hoping you’d be around."
    s "Well I’m definitely around."

    scene rinintheinn2
    with dissolve

    r "Yeah. You are."

    scene rinintheinn3
    with dissolve

    r "So uhh...did you hear that me and Chika are hanging out tonight?"
    s "I did. And I’m imagining that’s a big part of why you’re on the verge of tears."
    s "Are you thinking of telling her?"

    scene rinintheinn4
    with dissolve

    r "Thinking...yeah. Actually doing it is a whole other thing."
    r "I don’t want it to seem like I’m just getting swept up in the momentum of vacation and stuff."
    r "And I’ve never confessed to anyone before so I don’t even know what I would do."
    s "Isn’t it as simple as just...telling her how you feel?"
    s "I’m not really the best when it comes to any sort of feelings, so sorry if it’s more complicated than that."

    scene rinintheinn3
    with dissolve

    r "It’s definitely more complicated than that..."
    r "Especially considering that we’re both girls."

    scene rinintheinn6
    with dissolve

    r "Chika’s popular and...even if in some crazy reality she were to accept my confession, doing that would probably make a lot of her friends look at her differently."
    s "..."

    "Has Rin already decided that she’s going to be rejected?..."

    s "What’s this about a ‘crazy reality?’ You’re making it sound like you’ve already given up."

    scene rinintheinn7
    with dissolve

    r "There’s a big difference between giving up and accepting how things are."
    r "When she and I were talking last night...I figured out that there’s basically no chance of this working out in my favor."
    r "She definitely has feelings for somebody. But it’s a million-percent not me."
    s "…"
    r "…"

    scene rinintheinn9
    with dissolve

    r "Do you know who it {i}is{/i}, though?"
    r "Because I’m pretty sure I do."
    r "And I've gotta say, it's pretty surprising to me."

    scene rinintheinn8
    with dissolve

    r "But it’s fine...We can’t help who we fall in love with."
    r "I mean, maybe I’m supposed to be rejected?"
    r "Maybe that’s just...what needs to happen in order for me to move on?"
    r "What do you think, Sensei?"
    r "We’re good friends now..."
    r "Tell me how you feel."
    s "Why does how I feel matter at all?"
    r "Why wouldn’t it?"
    s "Because this isn’t about me."

    scene rinintheinn7
    with dissolve

    r "Heh...Yeah."
    r "You’re right."
    r "You’ve helped me enough as is. I shouldn’t be pushing any more problems onto you."
    r "It’s not fair."
    s "..."

    "{i}Not fair.{/i}"
    "What is fair, exactly?"
    "And what's all of this about pushing her problems onto me?"
    "If anything, Rin has been keeping her problems {i}away{/i} from me."

    s "Is that why you didn’t tell me you started hurting yourself again? You're afraid of getting me more involved?"

    scene rinintheinn10
    with dissolve

    r "Huh?"
    r "What are you talking about?"
    s "One of your friends recently opened up to me about how worried they are about you."
    r "What? Why?"
    s "She saw your arm."
    r "When would anyone have even-"

    scene rinintheinn11
    with dissolve

    r "…"
    r "It was Molly, wasn’t it?"
    s "You really think I’d tell you-"

    scene rinintheinn12
    with dissolve

    r "Definitely Molly."
    r "Listen...it isn’t what it sounds like."
    r "I promise that I haven’t done anything like that since you caught me."
    r "She probably just saw some of my old scars since I didn’t put any concealer on them that day."
    r "Do you want to check? There’s nothing there. I promise."
    s "...It’s fine."
    s "I don’t need to check."
    s "I’m supposed to trust you."
    r "Mhm...And I’m supposed to trust you too."
    r "…"
    s "…"
    r "Do you mind if I sit on the bed?"
    r "I’m starting to feel this weird power dynamic just kneeling at your side."
    s "Of course..."

    scene black
    with dissolve

    "Rin pulls herself off of the ground and moves closer to me. "
    "The two of us back against the headboard, but she doesn’t look at me for some reason."
    "She’s not normally the type to stray from eye contact when she isn’t in depression-mode, so it makes me a little uncomfortable."
    "But I suck it up and deal with it for the time being."
    "This is her time to vent."
    "And I told her I’d be there for her if anything like that happened over the weekend."

    scene rinintheinn13
    with dissolve

    s "…"
    r "You’re not wearing a shirt."
    s "Are you just now realizing this?"
    r "I was a little distracted by my own feelings before, but now that we’re on the bed together I’ve become increasingly aware of it."
    s "Should I put one on?"
    r "Nah...It’s okay. "
    r "Everyone else is doing stuff right now anyway. No one will see us and get the wrong idea or anything."
    s "I see."

    scene rinintheinn14
    with dissolve

    r "So do you...have any advice for a girl on her deathbed?"
    s "You’re not on your deathbed, Rin. "
    r "Mental death bed."
    r "I’m probably gonna...shut down for a little bit after tonight."
    r "I don’t think I’ll be able to prevent it even with you there."
    s "But what if in that “crazy reality” of yours, Chika says yes to you?"

    scene rinintheinn15
    with dissolve

    r "Then I’d shut down out of joy. It would be a horrible first impression as a girlfriend."
    s "Yeah, I think that would be a turn-off for me too."
    r "Really? So you don’t think I’m girlfriend material, Sensei?"

    if bonus == True:
        s "Well...I never said that."
        r "What am I then? The mistress? The friend with benefits?"
        s "I haven’t even received any benefits yet."
        r "What are you talking about? I showed you my boobs once, didn’t I?"
        r "Not calling them a benefit is pretty rude."
        s "Well it's not like you showed me them under the best conditions."
        r "Wanna see them again now?"
        s "These aren’t really the best conditions either."
        s "I will patiently await the day that you flash me without tears in your eyes."
    else:
        s "I do not think any of you are girlfriend material, for you are my students."
        s "But if I were to date any of you, it would likely be Futaba as she is the best at handling eggs."

    scene rinintheinn16
    with dissolve

    r "Hahahah! This is exactly why you and I have gotten so close."
    r "But there’s one thing that confuses me about all of it."
    s "And what’s that?"

    scene rinintheinn17
    with dissolve

    if bonus == True:
        r "You’ve had plenty of opportunities to push me into being more than just a buddy, but you’ve never really taken advantage of any of them."
        r "Is that really because you’re trying to protect me? Or is it something else?"
        s "What else would it be?"
        r "Don't know. Maybe you don’t think I’m pretty."
        r "Or maybe I'm just too damaged or something like that."
        s "Are you asking me to try and push things further?"
        r "Absolutely not. I’m thankful that you’ve been the way you’ve been. It’s just a little weird when I think about some of the stuff you say."
    else:
        r "Well...you've never really seen {i}me{/i} handle any eggs. So how do you know that Futaba is so much better at it?"
        s "Because I know about your secret omelette club."
        r "...how did you find out?"
        s "..."
        r "..."

    scene rinintheinn18
    with dissolve

    if bonus == True:
        r "You’re kind of a pervert, aren’t you, Sensei?"
        s "Why would you willingly climb into bed with me if you think that?"
        r "Because of my anti-pervert barrier. You won’t touch me as long as I’m crying."
        r "Which is exactly why I want you to let me sleep here tonight."
        s "…"
        r "…"
        s "I’m sorry, what?"
    else:
        r "You know what? Forget it."
        r "I'm just gonna cut to the chase and ask you if you'll let me stay here tonight."
        s "Absolutely not, Rin. Just sleep with the rest of the girls."

    scene rinintheinn19
    with dissolve

    r "You really think I’ll be able to sleep in the same room as Chika immediately after she rejects me? "
    r "Come on. You know me better than that."
    r "I want to sleep next to you."
    r "And I want you to rub my head and tell me everything will be okay."
    r "And I want to pass out knowing that someone is there to protect me."

    scene rinintheinn13
    with dissolve

    r "And also...I won’t really be able to do anything stupid as long as you’re here with me."
    r "So if I try to get up or something, just squeeze me really tight and don’t let me go."

    if bonus == True:
        s "You’re giving your shirtless teacher permission to squeeze you and not let you leave the bed in the middle of the night?"
        r "That is correct."
        s "And you’re calling {i}me{/i} the pervert?"
    else:
        s "I said no and that is final."

    scene rinintheinn20
    with dissolve

    r "Is there a problem with that?"

    if bonus == True:
        s "Not really. Just pointing out the flaws in your logic."
        r "Logic doesn’t apply to a maiden in love. "
        r "My mind is Chika and nothing but Chika."
        r "And some really depressing stuff, too, I guess. But mostly Chika."
    else:
        s "Yes. Why doesn't anyone ever listen to me?"

    "A moment of silence passes by as Rin makes more room in her mind for unrequited love."
    "There’s no telling how the night will go for her, but if it’s anything like I expect it to be, I’m not sure if tragedy is enough to even describe it."

    scene rinintheinn21
    with dissolve

    r "Do you think I’m just being impulsive right now? In regard to confessing, I mean."
    r "Should I maybe...wait a little longer?"
    s "{i}Can{/i} you wait a little longer?"
    r "I don’t know. Probably not. "
    r "I can barely even look at her, dude. And each time our eyes meet I just instantly go red."
    r "I keep thinking to myself, “There’s no way she doesn’t notice.”"

    if chikadorm20 == True:
        r "But then she goes and accuses me of liking {i}you{/i} and I’m just like...how would she even get that idea?"
        s "I don’t like the way you said ‘you’ there, but I get it."

    else:
        r "But then she goes and asks if {i}Molly{/i} is the one I’m into."
        s "You mean, {i}Molly{/i} Molly?"
        r "Yes. {i}Molly{/i} Molly."

    scene rinintheinn22
    with dissolve

    r "Girls are dumb. I don’t know how you put up with us all the time."
    s "It definitely helps that you’re all cute."

    scene rinintheinn23
    with dissolve

    r "Can I be really real for a second?"

    if bonus == True:
        s "Of course. But like I said, if you’re going to flash me, please wait until you’re not crying anymore."

        scene rinintheinn24
        with dissolve

        r "I’m not gonna flash you, idiot."
        r "I just want to know..."

    scene rinintheinn23
    with dissolve

    r "If..."
    r "If there’s anything...going on between you and Chika."
    s "…"

    if chikadorm20 == True:
        "I knew this question was coming."
        "In fact, I’m guessing that was probably the reason for this entire visit."
        "I’m not sure how the conversation between those two went last night, but Chika clearly gave Rin the idea that something was happening between us."
        "And frankly, it’s not her fault."
        "It’s my fault for doing exactly what Rin didn’t want me to do."
        "I pursued a relationship with the girl she claims to love."
        "And I did it all while calling the one sitting next me, the one doing her absolute best to hold back her tears-"
        "A friend."

        r "Tell me the truth..."
        r "I’ve seen the way you look at her."
        r "I've seen how she looks at you."
        r "How..."
        r "How far has it gone?"
        s "…"

        scene rinintheinn25
        with dissolve

        r "Have you kissed her, Sensei?..."

        if bonus == True:
            r "Have you...put your fingers inside of her?..."
            r "Did she suck your dick?..."
            r "How far has it gone?..."
            r "And why haven’t you told me about it?"
            r "We’re supposed to be friends."
            r "You’re supposed to tell me things."
            r "Just like I’ve told you everything about me."

            scene rinintheinn26
            with dissolve

            r "But...you went and did this..."
            r "And now you’re not even saying anything..."
            r "I won’t get mad...I just want to hear it from you."
            r "I want to know what’s making her smile so brightly when it’s clearly not me."
        else:
            r "Or...even worse..."
            r "Have you two..."
            r "Hugged?..."
            s "..."
            r "..."
            r "Come on..."

        scene rinintheinn27
        with dissolve

        r "At least...give me that..."

        "I can’t hide the truth from her any longer."
        "Rin deserves to know what’s been happening."
        "That way, she can confess with a clear conscience."
        "If she even wants to confess after hearing it straight from my mouth."

        if bonus == True:
            s "We’ve...done some things..."

            scene rinintheinn28
            with dissolve

            r "What kind of things, Sensei?..."
            r "Things you’re embarrassed to talk about?"
            s "Things I don’t think you need to hear."
            r "Even though I’ll never be able to do them with her?"
            s "...You don’t know that."
            r "Of course I do...she loves you..."
            r "And whatever you’re doing seems to be working based on how excited she gets whenever you come up..."
            s "…"

            scene rinintheinn29
            with dissolve

            r "How pretty was she when you touched her?..."
            r "What was she wearing?"

            scene rinintheinn30
            with dissolve

            r "I...I want..."
            r "I want to know..."
        else:
            s "Rin..."
            s "I am bad, bad boy..."
            r "How bad, Sensei?"
            s "..."
            r "Tell me how bad you are."
            s "..."
            s "I hugged her."
            r "Sensei...why?"
            s "Because I am the huggy boy."
            s "Hugging is what I do."
            s "I am so sorry."

        scene rinintheinn31
        with dissolve

        r "Sensei..."
        r "It hurts."
        r "It hurts so bad."
        s "..."
        s "I know it does. "
        s "But it will go away."
        r "Will it?"
        s "It will. "
        r "I...still...trust you..."
        r "Even though you..."
        r "..."
        r "Please...just...hold me for a little while..."
        r "I need to...feel something..."

        scene rinintheinn32
        with dissolve

        "With no words, I pull Rin closer to me and she instantly breaks into tears."
        "Before the end of the day, this girl will likely experience heartbreak a second time."
        "The first was at the hands of me."
        "A man who broke the one and only promise she ever asked him to make."
        "And the second will be at the hands of the opposite end of that promise."
        "The world is filled with horrible things-"
        "And I am among them."

        if bonus == True:
            "But this is something I’ve known all along."
            "What more are relationships than tools to use to your advantage?"
            "Rin knows this. "
            "She has to."
            "It’s why she doesn’t blame me for fingering the girl she loves."
            "It’s why she needs {i}my{/i} shoulder to cry on right now."
            "Because we’re all dependent on one another."
            "Just some for different reasons than others."
            "And that’s not to say I’m not sorry."
            "I am."
            "I never wanted her to cry like this."
            "But at the same time-"
            "I was never going to reject Chika."
            "I only said I would."

        scene black
        with dissolve2

        if bonus == True:
            "We can’t help who we fall in love with."
            "But we can help falling in love."
            "And love is such a confusing word."
            "The worst word that doesn’t begin with the letter T."
        else:
            "I am the huggy boy."
            "I am the one who hugs."

        "{i}A heart snapped like a twig and crushed underfoot.{/i}"
        "{i}Directly above the place where dreams become reality.{/i}"
        "{i}Where all sins are forgiven. Where all bonds are temporary.{/i}"
        "{i}Thus is the fleeting life we live.{/i}"
        "{i}Everything will be over before we know it.{/i}"
        "{i}So we have no time to sit idly by and wait for others to make their move.{/i}"
        "{i}Seize the day. Throw yourself into the wishing well.{/i}"
        "{i}And before you forget-{/i}"
        "{i}Make your dreams come true.{/i}"

        $ rinbetrayed = True

    else:
        s "There's nothing going on."
        s "I told you I wouldn’t do that to you. And I meant it when I said it."

        scene rinintheinn33
        with dissolve

        r "You...really didn’t do anything?"

        if chikatownfirst == True:
            "Well...the truth is we did kiss."
            "But Rin doesn’t need to know that."
            "It was nothing. "
            "Just two people caught up in the moment."
            "If I was truly malicious, I could have taken things further."
            "But I didn’t. "
            "So not telling her is fine."

            s "I really didn’t..."

        else:
            s "I really didn’t..."

        r "But...wait."
        r "I don’t get it. Why does she seem so into you then?"
        r "You’ve at least been spending time together, right?"
        s "Of course we have. Chika’s a friend of mine, just like you are."
        s "And you and I haven’t done anything, have we?"

        scene rinintheinn34
        with dissolve

        if bonus == True:
            r "Somehow or another, no. We haven’t done anything."
            s "It’s because you cry too much."
            r "And also how I think penises are kind of weird."
            s "Well I think you’re kind of weird."
            r "Yeah but the difference is you still hang out with me, and when I come to see you, I’m not coming to see your penis."
            s "Well, how would I know that? You could have strange motives."
            r "You’re right. The whole bisexual thing is just a front."
            r "I actually don’t like girls at all. It’s all just one big ploy to see your dick."
            s "Hey, all you need to do is ask."
        else:
            s "Sometimes, guys and girls can have relationships without either of them ever wanting the other as more than a hug partner."
            s "I call it the hug cycle and you can read about it in my new book, {i}The Five Hug Languages.{/i}"

        scene rinintheinn35
        with dissolve

        r "In all seriousness, though...thank you..."
        r "This entire time, I’ve been worried that something might happen if I take too long."
        r "And when I noticed you guys starting to see each other more and more, I couldn’t help but let my mind wander."
        s "Did it ever wander to anything {i}interesting?{/i}"

        if bonus == False:
            s "Like riding a sweet rollercoaster together?"

        scene rinintheinn36
        with dissolve

        r "Wh-what?! Of course not! "
        r "I mean...maybe once or twice! But most of the time you weren’t there and-"
        r "Actually, I’m just not even going to talk anymore! K thanks bye!"

        scene rinintheinn37
        with dissolve

        "Rin goes to get off the bed but I pull her closer and she quickly finds a comfortable place against me, playfully slapping my chest with the back of her hand."

        if bonus == True:
            "She laughs like a [young_girl] would with an older brother."
            "An older brother consoling his sister after her first breakup."
            "Just, in this case, Rin hasn’t been broken up with."
            "In fact, the real struggle hasn’t even begun."
            "That doesn't come until later."
            "But if she can find the willpower within her to follow her heart, I have faith that she’ll come out a stronger person in the end."
            "It’s why I didn’t betray her."
            "Even though I’m the scum of the Earth, I do believe that there are some relationships worth preserving."
            "This is one of them."
            "I can tell by her smile."
        else:
            s "Why can't I ride the rollercoaster with you"
            r "You are too top heavy. It will throw off the balance of the cart and kill both of us."
            r "I am not ready to die."
            s "I would make a good cushion to land on, though."
            s "You can sacrifice me if that is what you need to hear."
            r "Thank you, Sensei. I will think more about this."

        scene black
        with dissolve2

    "Rin winds up falling asleep in my arms."
    "Crying truly is exhausting at times."
    "I let her rest for around half an hour before deciding to wake her up."
    "I’m not sure what time she intends to meet up with Chika, but I do know that I shouldn’t let it get too dark before that happens."
    "At the very least, I’d like to go back to the beach and walk around for a bit."
    "I feel like I’ve been cooped up here for quite some time now."
    "Rin wipes the tears from her eyes as she comes to."
    "And before we know it, the two of us are walking shoulder to shoulder down the shoreline."
    "But only one of us will likely come back unscathed."

    $ renpy.end_replay()
    $ rin_love += 1
    $ beachvacation13 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

label beachvacation14:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
scene black
    with dissolve

    "………"
    "……"
    "…"

    scene whatwelove60
    with dissolve

    ki "Thanks for letting me play with you two, Sensei!"
    ki "I hope this teaches you guys a lesson about when and when not to go crazy on each other."
    ay "I’m...I’m so sorry..."
    ay "I never meant to actually get caught..."
    ay "I had no idea..."

    scene whatwelove61
    with dissolve

    ay "You’re not...you’re not mad...are you?!"
    ay "This doesn’t mean you’ll have to stop...seeing me...does it?"
    s "Of course not. Like Kirin said, everything is going to go back to normal now."
    ki "Yup! Cheer up, Ayane! It’s all over and done with!"
    ki "Plus, he even came inside you. Just like you wanted."
    ki "We all win!~"

    scene whatwelove62
    with dissolve

    ay "What are you doing?..."
    ki "Hm? What do you mean?"
    ay "Why would you walk in on us like that?"
    ay "You...you know how much he means to me."
    ay "I told you."
    ki "Hmmm...Ooooh yeah. That does ring a bell, now that you mention it."
    s "Let’s just...forget this ever happened. "
    s "Nothing is going to change, Ayane. I promise."

    scene whatwelove63
    with dissolve

    ay "...Okay."
    ay "I trust you."
    ay "And I love you..."
    s "…"
    ki "…"

    "I can’t just not say it back in a situation like this."
    "Ayane is close enough to breaking as-is."
    "I can let her have this one."

    s "I love you too."

    scene whatwelove64
    with dissolve

    ki "Yaaaaay. A happy ending. In more ways than one."

    scene whatwelove65
    with dissolve

    ki "Let’s get out of here and chat for a bit, Ayane."
    ki "It’s clear that this upset you, so I think I at least owe you an apology."
    ay "...Okay."
    ay "I’ll talk to you later, Sensei."
    ay "I’m sorry again."
    ay "And I love you."
    s "I love you too, Ayane..."

    play sound "slidedoor.mp3"
    scene whatwelove66
    with dissolve

    "Kirin grabs Ayane by the arm and pulls her out of the room. "
    "I remain standing there in the doorway for a moment, still in shock."
    "Will things really go back to normal after this?"
    "There’s no way they can...right?"
    "The look in Ayane’s eyes the moment she was caught-"
    "It’s like every exhibitionist joke she ever made was killed right then and there."
    "Every ounce of joy in her faded away."
    "And she was left with nothing but what I had inside of her."

    scene black
    with dissolve

    "…"
    "I think I need to take a nap."

    $ renpy.end_replay()
    $ ayanelust10 = True
    $ ayane_lust += 1
    stop music fadeout 5.0

    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "………"
    "……"
    "…"

    jump beachvacation13
...
```