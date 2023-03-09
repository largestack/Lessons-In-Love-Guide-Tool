# Transmogrification
Molly event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm25&go=Go)


Part of event chain [Tír na nÓg](./mollycafe25p2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: mollydorm25
* Group: Molly
* Triggered by label: mollycafe25p2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label mollydorm25:
    play sound "dooropen.mp3"
    stop music fadeout 20.0

    "Molly and I escape back into the warmth of the dorm just as the night decides to get all fucking annoying and start showing off how fast it can make the wind go."
    "She appears a little confused the moment I start following her upstairs, but makes no effort to actually stop me."
    "I imagine there’s a chance she’s just worried that she’ll have to think up some sort of {i}actual{/i} quest reward or whatever it was I was promised-"
    "But I imagine there is an even {i}better{/i} chance that she’s just confused about where things will go from here as a whole."
    "So am I, to be honest. "

    if bonus == True:
        "I mean, surely I wouldn’t be seizing this opportunity to make some sort of move on a cute girl fighting off both the sting of rejection and sleep deprivation, would I?"

        s "…"

        "I remain silent in hopes that asking myself this rhetorical question will somehow push me in either direction."
        "Unfortunately-"

    scene mollydormchanging1
    with dissolve
    play music "love.mp3"

    "I somehow wind up inside of her room."
    "Now, the reason I use the word {i}un{/i}fortunately isn’t because I’m worried about how forcing a girl into an uncomfortable position will feel-"
    "But it’s because I feel slightly bad that Molly can’t really do anything to change that."
    "Nor do I know if she {i}would{/i} change that, given the opportunity."
    "All I know is that she said she was worried that being back here would cause her to start thinking."
    "Sometimes, however, I think it’s better to act without any thought put into things at all."
    "Hence, bedroom."

    mo "Sir, if this is about your quest reward, I’m afraid I don’t have one on hand right now."
    s "Eh. I don’t need a reward. "
    s "I’m just bored."
    mo "Darkness has already consumed the land, and yet you beg for more of Molly MacCormack?"
    mo "What would Arborea say?"
    s "I’m sorry, who?"
    mo "Apologies, Sir. I meant Ami."
    mo "Does she not spend each night in silence, awaiting both your presence and a single genre tag that forces people to download a video game without even reading the description first?"

    if bonus == False:
        s "What are you talking about? Ami and I are in no way, shape, or form related."
    else:
        s "As if that would ever happen."

    s "Besides, I’m sure Ami is fine. Chances are she’s already asleep."

    scene mollydormchanging2
    with dissolve

    mo "Ahh, sleep..."
    mo "I remember those days well. T’was back when I was just a lass."
    mo "Long before I’d given up on ever experiencing the taste of sweet slumber ever again."
    s "Cool. More time to hang out with me."

    scene mollydormchanging3
    with dissolve

    mo "Sir, you have been suspiciously nice to me all night. It’s beginning to feel like you may have accidentally activated my route instead of someone else’s."
    s "I’m just doing what I always do. It’s up to you whether or not this is about to become {i}your{/i} route."
    mo "It’s never up to the heroine, Sir. That’s just an illusion meant to trick readers into believing they’ve done more than click buttons and set a few invisible flags to “True.”"
    s "Well, whatever it is, I’d still like to kill a little time before heading back home."
    s "Unless you’re planning on letting me crash here, that is."

    scene mollydormchanging4
    with dissolve

    mo "Well...I suppose I wouldn’t have much of an issue for that. Party members sleep together and manage to avoid getting physical all the time. "

    if bonus == True:
        s "I mean...we don’t have to {i}avoid-{/i}"

    mo "The main issue is that the Kendo Princess normally comes home around this time as well, and I can’t imagine she would feel very comfortable with this...sudden development."
    s "Then I’ll just stay until Tsuneyo is back."

    scene mollydormchanging5
    with dissolve

    mo "That seems like a respectable decision."
    mo "The issue now is that I would like to switch transmogrifications, which I can not do with you standing there gawking at me."

    if bonus == True:
        s "I have no idea what you just said to me."
        mo "Pajamas, Sir. I would like to get changed."
        s "Oh, sure. Go right ahead."
        mo "…"
        s "…"
        mo "{i}Without you gawking at me.{/i}"
        s "Oh."
        s "Yeah, I can’t help that."

        scene mollydormchanging6
        with dissolve

        mo "But...you have already seen me without my armor on once before. "
        s "Yeah, which is why I don’t think it’s a big deal."
        s "Just keep talking. It’s only weird if you decide to make it weird."
        mo "It appears that you have already decided to make it weird. Cease holding your actions and use them to look away."
        s "Hey, you still owe me a quest reward. This would be a good time for that, wouldn’t it?"

        scene mollydormchanging7
        with dissolve

        mo "Ahh...lookin’ to barter, are ye?"
        mo "How about this then, Sir?"
        mo "The Halloween party is just a short while away. What if I told you I could give you a behind the scenes glimpse at the costumes of various girls in our class?"
        s "Go on."
        mo "So long as you manage to keep me out of your line of sight for the duration of my transmogrification, I’ll show you."
        s "I don’t know, Molly. Real life still sounds a little better than a few pictures."
        mo "It is six girls, Sir."
        s "Six? Damn it. That’s so many."

        scene mollydormchanging8
        with dissolve

        mo "The costumes are rather form fitting as well. If you look closely enough, you can see {i}everything{/i}, Sir. "
        s "Everything?"
        mo "Right down to the last mana circuit."
        s "Tch."

        "I click my tongue like some sort of anime protagonist and accept that this proposition will be the end of me. "
        "Well, the end of my chances of seeing Molly naked right now."
        "I’m sure I’ll be able to see the real thing up close sooner or later."
        "Just...it probably won’t be soon {i}enough.{/i}"

        scene black
        with dissolve2

        s "Okay, fine. "
        s "But I reserve the right to trade away the picture and turn around at any moment."
        mo "What kind of ass backwards deal is that, Sir? Roll for persuasion."
        s "Roll for what?"

        play sound "dice.wav"

        mo "Geh. Fine, I’ll roll for ya and-"
        mo "Brigid’s bosom, it’s a natural twenty."
        s "Is that good or bad?"
        mo "Good for you, bad for me. You win your wonky barter clause, Sir. But please do try to not invoke it."

        scene mollydormchanging9
        with dissolve

        s "Do you just keep dice on you at all times or something?"
        mo "Of course, Sir. You never know when you’re going to need a D20. And dice apps just can’t compete with the feeling of a nice, solid one in your hands. "
        s "I’ve got a nice solid one right here."

        scene mollydormchanging10
        with dissolve

        mo "A D20?"
        s "A penis."
        s "It was an erection joke."

        scene mollydormchanging11
        with dissolve

        mo "O...Oh! Yes! I knew that."
        mo "Nothing beats a good ole...dirty joke. That’s for sure."
        s "Why are you the one making things weird after finally convincing me not to?"

        scene mollydormchanging12
        with dissolve

        mo "Hah...Who knows, Sir?"
        mo "You should be happy I haven’t pounced on you and demanded that we kiss, yet."
        s "Should I? Because that sounds a lot like a thing that I would enjoy."
        mo "Doubtful, Sir. You find me annoying and have already confirmed with ye’ own eyes what I watch when I’m...indulging myself."
        s "Why would knowing you [masturbate] to pictures of Rin make me not want you?"

        scene mollydormchanging13
        with dissolve

        mo "Some would equate even minor actions like that to NTR, Sir."
        mo "Some men just have so little confidence that they get angry if even cartoons don’t pay sufficient attention to them."
        s "That’s just sad."
        s "Thankfully, we are both real people and those sorts of things don’t apply to us."
        mo "I thank you for the privilege to [masturbate] to my friends without the fear of losing you, Sir."
        s "You’re welcome, Molly."
        s "I’d appreciate to be included in those fantasies from time to time as well, though."

        scene mollydormchanging14
        with dissolve

        mo "‘Tis hard when you’re nothing more than a ghost on the Internet, Sir."
        mo "Why should I submit to fantasy when there are so many accessible swimsuit pictures of people I’m attracted to?"
        s "I thought fantasizing about stuff was kind of your thing?"
        mo "Not all of the time, Sir."
        mo "Just most of it."
        s "So, what I’m hearing is that the key reason you [masturbate] to Rin instead of me is because she has a social media profile."
        mo "Aye, Sir. The profile helps."
        s "Molly, this is the single best argument anyone has given me for starting one of those things yet."

        scene mollydormchanging15
        with dissolve

        mo "I’m glad to have been of service, Sir! "
        mo "Now, come! Feast your eyes upon tonight’s quest reward in the form of six girls in costumes you will likely not recognize!"

        scene black
        with dissolve
    else:
        scene black
        with dissolve

        s "Understood. I will now close my eyes to avoid the next part of the event."
        mo "Thank you. I appreciate how unwilling you are to make any romantic advances on me given the nature of our relationship."

    "Molly removes her cell phone from a pile of clothes she left near the door and begins to make her way over to the bed, swiping through various images until she finds the one she needs."
    "I take a seat beside her and she pulls her knees closer to her chest before tilting her screen up and showing me my apparent reward."

    scene mollydormchanging16
    with dissolve

    mo "So, I’m sure you have no idea what any of this is, nor do I imagine you want me to educate you, but here you go."
    mo "The members of the manga club...and Ayane have decided to do a group cosplay for Halloween this year."

    scene mollydormchanging17
    with dissolve

    s "Why doesn’t Ayane just join the club as well if she’s going to keep doing literally everything with you guys anyway?"
    mo "Something about wanting to save more time for when you two elope, I believe."
    mo "Is that really all you have to say, though? I was expecting more of an excited reaction out of you, Sir. "

    if bonus == True:
        mo "Especially with all of our thighs being out there in the open."
        s "Oh, don’t get me wrong, I think you all look great. "
        s "But, if anything, I’m just more excited to see you all in person now."
    else:
        s "Absolutely not. I am respectable and kindhearted man who is just very excited for Halloween."

    scene mollydormchanging18
    with dissolve

    mo "You will not have to wait much longer, Sir."
    mo "I intend to make this Halloween one that I will remember for the rest of eternity! Especially after losing most of my memories of the last one!"
    s "You were...extremely drunk."

    scene mollydormchanging19
    with dissolve

    mo "You probably should have called an ambulance. I could have died."

    if harukalust10 == True:
        s "Sorry. I had...things to do."
        mo "What sort of thing would be more important than saving a student’s life?"

        if bonus == True:
            s "A threesome with two cat girls."
            mo "Oh."
            mo "Well...yes. I understand completely, if that was the case."
        else:
            s "I was volunteering at the local soup kitchen, providing meals for the homeless."
            mo "You're such a good guy, Sir."
            s "Yes. I am."

    else:
        s "Sorry. I had..."

        play sound "static.mp3"
        scene harukalusttenskip3 with flash
        scene mollydormchanging19 with flash
        stop sound

        s "I had to fix some pipes..."
        mo "…"
        mo "What?"
        s "Doesn’t matter."

    s "Anyway, what else do you have for me?"
    mo "I’m sorry?"
    s "That can’t be the only picture, can it?"
    mo "There are some on the other girls’ Instagrams, but the only extra ones I had were of Rin from when I tailored hers...and I deleted all of those."
    s "Really? Not going to keep them around to-"
    mo "Please don’t, Sir. It still hurts, even if I’m not acting torn up about it."

    if bonus == True:
        s "That’s weird. Because we were talking about it a few minutes ago and you seemed totally fine then."
    else:
        s "I understand. We can stop talking about this now."

    scene mollydormchanging20
    with dissolve

    mo "I know."
    mo "But seeing her again made it hard."
    mo "I’m only good at running away from my problems when they’re not trying to catch up, I suppose. "

    if bonus == False:
        s "Molly pls."

    mo "My movement speed just isn’t fast enough."
    s "Well, I’m not going to keep pestering you about it. I’ve done enough of that today and I’m starting to think I might be doing to {i}you{/i} what you always do to me."
    mo "I don’t mind. It’s nice having friends again."
    s "Okay, I guess I’ll pester you one last time in informing you that you {i}do{/i} still have friends."
    s "Getting into a fight over liking someone isn’t enough to destroy something like that. And, if it is, it was probably a shitty friendship to begin with."

    scene mollydormchanging21
    with dissolve

    mo "Sir, you are forgetting how things ended. It may not sound as bad for someone who wasn’t there, but it was extremely awkward for even my standards."
    mo "And need I remind you that I have very high standards for what is and isn’t awkward?"
    s "No reminder is necessary. You’re probably the most socially awkward person I know apart from Tsuneyo or Kaori or...Yasu-"
    s "Why are so many of you awkward?"
    mo "The point, Sir. You are losing it."
    s "Right, sorry. "
    s "What I’m saying is that apart from the various...{i}special{/i} cases, the only other person I know who is almost as awkward as you is Rin."
    s "Which means that she’s more likely to just get over this than anyone else."
    s "Maybe."

    scene mollydormchanging22
    with dissolve

    mo "That “maybe” causes me a great deal of worry, Sir."
    s "Well, if you’re {i}that{/i} worried...just go talk to her."
    mo "I don’t know...the last time I took someone’s advice about this, I was either duped or...I greatly misunderstood that person."
    mo "The great downfall occurred just shortly after that, when I had already chosen the path I was going to walk."

    scene mollydormchanging23
    with dissolve

    mo "But...as the gears screeched to a halt and all of the cogs in this machine called “life”  stopped spinning, I knew something needed to be done."
    mo "If only I had known that “something” was the opposite of what the voice inside of my head commanded of me."
    s "…"
    mo "…"
    s "So, are you going to talk to her or not?"

    scene mollydormchanging24
    with dissolve

    mo "What, like...right now?"
    s "Sure. Rin stays up late, doesn’t she?"
    s "And if there’s anything I’ve learned about serious situations in the dorms, it’s that a person’s roommate is almost always conveniently missing exactly when they need to be."
    mo "You know, Sir...Now that you mention it, I do remember Futaba mentioning something about going to the bookstore with Nodoka tonight."
    s "See what I mean? Now is as good a time as any."

    scene mollydormchanging25
    with dissolve

    mo "I don’t know..."
    mo "Rin said she wanted to take a break from speaking for a while."
    mo "And...and what if Otoha is there?"
    s "At this hour? Her mother would never allow that."
    mo "…"
    s "…"

    "Molly takes a moment to think about what her next move is going to be."
    "I’m sure it's hard deliberation considering her only options are “keep indefinitely being sad” or “risk becoming more sad in order to be less sad right now,” but...those are kind of the only options we ever have."
    "And even if time does have a way of mysteriously healing things, it doesn’t mean it’s exciting to just sit back and let that happen."
    "The most ideal scenario right now would be for Molly and Rin to {i}both{/i} be happy."
    "And if I have to put someone else’s well-being at stake in order to risk that, so be it."

    mo "Will you...come with me?"
    s "Me? Why?"
    mo "Moral support, I suppose."
    mo "Our party hasn’t disbanded yet, so...just think of it as another side quest."
    s "…"

    if bonus == True:
        s "Fine. But the reward for this better be more than just a picture of my students wearing clothes, skin tight or not."
    else:
        s "Fine. But you owe me a soda."

    scene mollydormchanging26
    with dissolve

    mo "Understood, Sir. And thank you."
    mo "But...I still don’t know what I should say."
    s "When in doubt, just be honest. "
    s "That’s what I always do and it only backfires like...less than half of the time."
    mo "...Slightly less than half? Or significantly less than half? Because I do not feel good about those odds if it is the former."
    s "Doesn’t matter. You’ve already decided and I’m going to be there with you every step of the way."
    s "Unless you or Rin asks me to leave. "
    s "If that happens, I imagine I’ll put up a fight for a little while but ultimately just go anyway."
    mo "…"
    s "…"

    scene mollydormchanging23
    with dissolve

    mo "{i}Hah...{/i}"
    mo "Good thing we stopped at that leyline earlier. Otherwise, there is no way I’d allow you to talk me into this."
    s "Sure you would. You just needed an excuse to do something you already wanted to do, and telling you this is just one more example of my brutal honesty making things better."
    mo "That didn’t make anything better at all..."

    scene black
    with dissolve2

    "Molly decides to keep her pajamas on for the trip back downstairs- probably because it would look weird to get dressed up for a second round of rejection."
    "Or, in the best case scenario- the {i}first{/i} case of her and Rin trying to make things work."
    "We just have to hope at this point that Rin is still awake."
    "But given how excited she still seems to have a girlfriend, I imagine it’s possible she hasn’t slept at all since the beach."
    "But hey, that puts her back into the same category as Molly, even if the two of them have already begun to drift apart."
    "Maybe this small similarity, albeit the result of opposite extremes, is all they’ll need in order to get closer again."

    play sound "dooropen.mp3"

    s "…"

    "Or maybe it will end things once and for all."
    "You can’t ever really know until it’s too late, can you?"

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump rindorm50special

label mollydorm30:
...
```

## Code that triggers this event
File: \game\MollyEvents.rpy
Code:
```python
...
scene mollywind16
    with dissolve

    mo "No...It’s true, Sir."
    mo "And I’ve known it to be true for quite some time. "
    mo "If I was...prettier or...cooler like someone like Chika or Otoha, you and I wouldn’t be on this bench right now."
    mo "I’d have won."
    mo "But I made the executive decision to put all of my stat points into categories that didn’t matter as much as aesthetics to some people."
    mo "Which is fine. We all have different things we look for in partners."
    mo "I just wish it wasn’t too late to change where I allotted those points, is all."
    s "It’s not, though."

    scene mollywind17
    with dissolve

    mo "But, Sir...you {i}have{/i} to say that."
    mo "You’re the protagonist."
    mo "It’s your job to make us feel loved or wanted. "
    mo "We can’t just change who we are now after spending so many years figuring it out."
    s "These are the exact years you’re supposed to be {i}using{/i} to figure it out, though."
    s "Even if Rin {i}doesn’t{/i} think you’re pretty, which I don’t think is the case, there are plenty of people who do."
    s "And it might sound kind of weird, but a lot of people are really attracted to foreigners in Japan."

    scene mollywind18
    with dissolve

    mo "Well, {i}that{/i} was mildly racist. "
    s "I didn’t mean it in a bad way."

    scene mollywind19
    with dissolve

    mo "{i}*Sniff*{/i} No, it’s fine. I know you meant no harm."
    mo "I’m sure I’m overreacting. It’s just hard not to think certain things when you share literally {i}every{/i} interest with the person you like and they still won’t give you a shot."
    s "Some people just want something different from them, I guess."
    mo "Otoha isn’t that far off from Rin, Sensei."
    s "Okay, sure. But we shouldn’t be using Rin as the basis for {i}anything{/i} when she is about as composed as..."
    s "I can’t even think of a comparison. She’s a wreck."

    scene mollywind20
    with dissolve

    mo "A wreck I’ll never get to have or hold."

    if bonus == True:
        mo "Or get all hot and bothered with while playing h-games."

    s "No. But you {i}have{/i} kissed her before, which is more than a lot of people can say."

    if rinbetrayed == False:
        "Not including me, of course. I’m in that same boat. But Molly doesn't need to know that."

    mo "I don’t think it’s fair to count what happened on Christmas as a real kiss, Sir."
    mo "I've done some more thinking on the matter and, as far as I’m concerned, I still haven’t had my first."
    s "Really? Not even going to pretend you had your first with the girl you like just to make yourself feel better?"

    scene mollywind21
    with dissolve

    mo "The only thing that makes me feel better is gaming, Sir! And anime! That is all I need!"
    s "That’s so depressing."
    mo "Maybe! But this is the person I am! "
    mo "This is Molly MacCormack!"
    mo "And...if you don’t like that...Go dtachtfadh an diabhal thú!"
    s "Yeah. Gothafababable and dhtafghdadadad."

    scene mollywind22
    with dissolve

    mo "Pfft!"
    mo "Thank you for trying, Sir. I felt quite similar when I was learning Japanese. "
    s "I did my best. "
    s "But, on another note, I am done sitting on this bench. It is fucking cold."

    scene mollywind23
    with dissolve

    mo "Then...off to the original side quest we go!"
    mo "There were no physical rewards for this one, but I do believe we have increased our social link!"
    s "Yeah. And we’ve grown a little closer as well."

    scene mollywind24
    with dissolve

    mo "Oh, Sir...You still have so much to learn..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25p2 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump mollydorm25
...
```