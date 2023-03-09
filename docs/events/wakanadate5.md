# Soup, or Another Year With You
Wakana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=wakanadate5&go=Go)



## Event preconditions
✅Wakana love greater than or equal to 5

✅Event "[Wakana: To the River](./wakanadate1.md)" is completed (event=wakanadate1)

✅Event "[Kaori: Clouds](./kaoridate15p3.md)" is completed (event=kaoridate15p3)

✅wakananumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: wakanadate5
* Group: Wakana
* Triggered by label: callwakananight
* Triggered by branch label: callnight

## Event code
File: \game\WakanaEvents.rpy
Code:
```python
...
label wakanadate5:
    play sound "phonebeep.wav"

    "I tap on Wakana’s name in my phone and wait for her to answer, hoping that, wherever she is, it isn’t at[school]."
    "I really don’t like the idea of her using my friendship for the sole purpose of grading papers faster, but I have a creeping suspicion that last time was not {i}actually{/i} the last."

    play sound "phonebeep.wav"

    w "I want to fucking die."
    s "Hey, Wakana. I’m glad to hear you’re doing fine."
    w "I need your help."
    s "I’m not grading any more papers for you."
    w "Good. What you did to those papers could barely be called “grading” to begin with."
    s "In my defense, you never told me to grade them {i}correctly{/i}."
    w "I hope you choke and die on the next thing you eat."
    w "When is the soonest you can get here?"
    s "You're not going to feed me, are you? "
    w "Not at this rate."
    s "I’m sorry, what?"
    w "Cooking is difficult. I need help."
    s "From me?"
    w "From anyone. This is an absolute emergency."
    s "Why not ask your girlfriend for help?"
    w "Because I can’t. Are you coming or not?"
    s "…"

    "Well...it’s not like I have anything else to do."

    s "Normally, my [niece] is the one that cooks. I don’t really know-"
    w "Wonderful. I’ll see you in five minutes."
    s "But I don’t even know where you live yet."
    w "Figure it out, imbecile. I don’t have time for these pathetic games of yours."
    s "What does that-"

    play sound "phonebeep.wav"

    s "…"

    "I feel like people have been hanging up on me a lot lately."
    "I am very much not a fan of this."

    scene black
    with dissolve

    "I start walking in a random direction and hope that it’s the right one."
    "Thankfully, I {i}do{/i} receive a text from Wakana several minutes later with the address of her apartment complex and begin to make my way there..."
    "………"
    "……"
    "…"

    scene wakanatriestocook1
    with dissolve
    play music "normalday.mp3"

    s "…"
    s "Well, this is an exciting coincidence."

    "So, as it turns out, my favorite non-me teacher is the next door neighbor of my favorite waitress."
    "I knew the address looked familiar when Wakana sent it to me, but I didn’t really expect it to be {i}this{/i} familiar. "
    "If I had known she lived next to Kaori, I would have just asked {i}her{/i} to help Wakana cook."
    "If...Kaori even knows how to cook and isn’t just strictly a waitress."
    "Also, I’d need to be positive that Wakana wouldn’t be cooking anything with chicken."
    "Even though Kaori eats chicken."
    "You know what? I don’t even know why I’m thinking about this when Kaori isn’t the one I’m here to see."
    "I’ll just knock on Wakana’s door and-"

    play sound "static.mp3"
    scene wakanatriestocook2
    with flash
    stop sound
    stop music

    john "Greater love has no one than this: to lay down one’s life for one’s friends."
    john "You are my friends if you do what I command."
    john "I no longer call you servants, because a servant does not know his master’s business."
    john "Instead, I have called you friends, for everything that I learned from my Father I have made known to you."
    s "…"
    john "…"
    s "Hi, John."
    john "Sup."

    scene wakanatriestocook1
    play sound "knock.mp3"
    play music "justbehappy.mp3"

    "I knock on Wakana’s door and completely ignore my most recent exchange with a chicken."

    w "Come in right now. The door is unlocked."
    s "Can you be a little happier to see me at least?"
    w "No. Open the fucking door."

    scene black
    with dissolve

    "Why is it that I decided to walk across town to help a woman in a committed relationship cook despite having no idea how to do so myself?"
    "And why was John just standing outside underneath a light without Kaori?"
    "Why is tonight so weird by even the standards of my life?"

    scene wakanatriestocook3
    with dissolve

    w "Let’s do this."
    s "…"

    "Am I actually asleep right now?"
    "There’s no way any of this is actually happening, right?"

    s "I need an explanation."
    w "I need a fucking drink."
    s "What is happening right now?"

    scene wakanatriestocook4
    with dissolve

    w "Hah...it’s my anniversary with Osako and I want to do something nice for her since she’s always the one who does...everything."
    w "But I am entirely useless outside of[school] and hope that having someone else equally as useless will not only help in some way, but make me feel better about my shortcomings as a lover."
    s "Well, you called the right guy. If there is anyone who can make other people look better by simply being next to them, it’s me."

    scene wakanatriestocook5
    with dissolve

    w "Wonderful. Except you omitted the detail where {i}you{/i} were the one who called {i}me{/i}."
    w "As if I’d ever stoop so low as to contact you first. Please."
    s "Wakana...you’re not actually a tsundere, are you?"

    scene wakanatriestocook6
    with dissolve

    w "If by “tsundere” you mean “woman who would sooner copulate with a meat cleaver,” then yes. I believe I am."
    s "I feel like you would immensely regret that decision seconds in."
    w "They both seem like incredibly regrettable decisions. Now, help me."
    s "With what? What are you even trying to make?"

    scene wakanatriestocook7
    with dissolve

    w "I don’t know...soup?"
    s "In a frying pan?"
    w "...Cake?"
    s "...In a frying pan?"

    scene wakanatriestocook8
    with dissolve

    w "I told you I don’t normally do this, didn’t I?!"

    "I harness my inner Tsuneyo and tell Wakana everything I know about cooking soup."

    s "Okay, okay."
    s "First, you’re going to need a pot."

    scene wakanatriestocook9
    with dissolve

    w "Okay."
    w "Then what?"
    s "That’s all I’ve got."

    "I’m sorry, Tsuneyo."

    scene wakanatriestocook10
    with dissolve

    w "I was not designed for love."
    s "Same."
    s "Let’s just see what you have in your house and try to go from there."
    s "Worse comes to worst, Osako comes home and you can play up how bad you are at cooking and be all endearing about it or something."

    scene wakanatriestocook11
    with dissolve

    w "Me? Endearing?"
    w "She’s the cute one. I just lie on the bed and have her rub my feet all night."
    s "Why does she like you again?"

    if bonus == True:
        w "I don’t know. Foot fetish, maybe?"

    w "Doesn’t matter. Just...go look around for ingredients or something."
    s "I think you would know better where you keep all of the ingredients in this apartment."
    w "And you’d be greatly mistaken in doing so."

    scene wakanatriestocook12
    with fade

    "I walk past Wakana into the living room slash bedroom to begin my search."

    w "When I said search, I meant the fucking kitchen, you pathetic baboon."

    scene wakanatriestocook3
    with fade

    "I immediately return to Wakana after slightly invading her privacy."

    s "I figured I could cover the bedroom while you handled the kitchen."
    w "I {i}sleep{/i} in that room. And rather frequently, might I add."
    w "Now the entire thing needs to be professionally cleaned before I can even set foot inside."
    w "Thank you for making my night so much more difficult than it already was."
    s "I barely stepped inside."
    w "I’d need it professionally cleaned if you even {i}thought{/i} about stepping inside."
    w "Open some cabinets. Check the freezer. Do something. Anything."
    w "Osako should already be on her way home."
    s "And you waited this long? Are you insane?"

    scene wakanatriestocook8
    with hpunch

    w "Less talking, more scavenging! Go go go!"

    scene black
    with dissolve

    if bonus == True:
        "I do as Wakana says (Not because I believe it will increase my chances of having sex with her, but because she kind of scares me) and start frantically opening cabinets."
    else:
        "I do as Wakana says and start frantically opening cabinets."

    "My search ends with several things that I think might...probably work in soup: salt, chicken stock, and some weird packet with red stuff in it."
    "That last one is a shot in the dark, but it’s not like I have any idea what I’m doing and bringing only two things to the table sounds lame."

    w "Okay...I found some things."
    w "What do you have?"
    s "Salt, chicken stock, and some red stuff."
    w "Red? That sounds spicy. Osako doesn’t like spicy."
    s "Just trust me on this, Wakana."
    w "I..."
    w "Fuck it. Throw it in."

    "Wakana manages to find a pot and we each take turns dumping our hauls into it."
    "Among her ingredients is a full carrot, some instant noodles, half a bottle of mayonnaise, and several soy sauce packets from a take out restaurant."

    scene wakanatriestocook13
    with dissolve

    w "How do you think this will be?"
    s "Horrible."
    w "How hot do we make it? Is it possible to burn soup?"
    s "I say just turn it up as high as it goes if Osako is on her way home. That way, we can make sure it’s completely cooked by the time she gets here."
    w "Fine. But if the soup burns, I’m pouring it down your throat. Wasting food is unacceptable when there are children all over the world dying of starvation."
    s "Sucks to be them."

    scene wakanatriestocook14
    with dissolve

    w "It sucks to be anyone. Life is miserable and we’re all going to die."
    s "You know, food is nice and all, but what I think would make Osako {i}really{/i} happy is if you were able to not hate yourself for a day."
    w "I’m even worse at that than I am at cooking."
    s "I also think she would have appreciated it if you just bought her something instead."

    scene wakanatriestocook15
    with dissolve

    w "No. It has to be handmade."
    w "I can avoid cooking like the plague 364 days out of the year, but on this one, I need to at least {i}try.{/i}"
    w "If I can overcome this hurdle, Osako will see that I am not just a self-loathing blob of hatred with complete control over this apartment’s interior design."
    s "You mean all of that black and purple in the living room wasn’t Osako’s choice?"
    w "Excuse me for wanting to share my somber view of the world and its inhabitants with all who choose to enter my home."
    s "And how many people enter this home, exactly?"
    w "Osako. And now you, I suppose."
    w "While we wait for this to finish cooking, would you mind looking up the price of professional cleaners?"
    s "I’ll just ask Makoto to come here and do it if it’s really that much of an issue. She’ll be here in like five minutes if I ask her to be."
    w "Please don’t bother Miyamura with such a trivial task when she should be burying her nose in a textbook and exercising that prodigal brain."
    w "Also, is it just me, or is the soup turning solid?"
    s "Yeah, I noticed that as well."
    w "That’s not supposed to happen, is it?"
    s "Probably not."

    play sound "dooropen.mp3"
    scene wakanatriestocook16
    with dissolve
    stop music fadeout 5.0

    os "Wakana! Happy anniversary! Sorry I had to spend most of the day working but, I-"

    scene wakanatriestocook17
    with dissolve

    os "I..."
    os "What is he doing here?"
    s "Absolutely nothing."
    w "Hah...I suppose the jig is up."
    os "Jig?...What jig?"
    os "What are you talking about?"

    scene wakanatriestocook18
    with dissolve

    os "What’s going on? Why are you in our apartment?"
    os "I knew Wakana and you were friends, but since when are you two-"

    scene wakanatriestocook19
    with dissolve

    w "I’m sorry, Osako. I truly am."
    os "Sorry for what?...What happened?"

    scene wakanatriestocook20
    with dissolve

    w "I wanted to cook dinner for you to celebrate our anniversary, but I am inherently incapable of doing anything other than teaching."
    w "And so I called the only other person I’m in regular contact with to assist me, but lo and behold, he is inherently capable of even less."

    "Is Wakana actually covering for me right now? Or did she just forget that I’m the one who called her?"
    "Either way, I don’t bother refuting the thing about me being even less capable than her because this is probably something I should stay out of until it cools down a little."

    scene wakanatriestocook21
    with dissolve
    play music "thesleepingcity.mp3"

    os "Wakana...you..."
    os "You did that for me?"
    os "But you hate cooking. This is the first time you’ve even tried since last year, and that time you weren’t even able to figure out how to turn the stove on."
    w "I’m sorry, Osako. I’ll accept gracefully if you want to put me out of my misery."

    scene wakanatriestocook22
    with dissolve

    os "Nonononononono, it’s totally okay. I’m really happy you tried."
    os "I was just a little surprised to see you with someone else when I came home. That’s all."
    os "I...guess I just kind of figured it would be just us tonight."
    s "I was really only dropping by to help Wakana. I’ll leave now."

    scene wakanatriestocook23
    with dissolve

    os "Uhh...sorry if it seemed like I was accusing you of something."
    os "I...get jealous a little too easy, I guess."
    s "I’m sure I’d feel the same way in your shoes."
    s "Also, do you have any idea what that packet of red stuff in the pantry was? Because the soup very clearly came out wrong and I would like to confirm that it was Wakana's fault."

    scene wakanatriestocook24
    with dissolve

    os "Packet of...red stuff?"
    s "Yeah. It was between a packet of blue stuff and a packet of yellow stuff."
    os "Blue stuff...and...yellow-"

    scene wakanatriestocook25
    with dissolve

    os "Jell-O?..."
    w "Oh. You like Jell-O."
    w "Perhaps dinner isn’t ruined after all."

    scene wakanatriestocook26
    with dissolve

    os "How about I just...run to the convenience store really quick and grab some real ingredients for the two of us to make dinner with?"
    os "I can show you how to cook if you really do want to learn for next year."
    w "If you’d be so kind as to do that..."
    os "Of course. Anything for you."
    s "And on that note, I’ll be leaving."
    s "But I’d like to part with saying happy anniversary and-"

    scene wakanatriestocook27
    with dissolve

    os "Actually, why don’t you tag along with me if you’re on your way out?"
    os "There’s something I kind of want to talk to you about anyway."
    s "Please don’t quit the maid cafe just because you got to keep your job at the dojo."
    os "I’m not allowed to quit the maid cafe. Wakana would kill me."
    w "Humanely. But yes."
    s "Are you sure? It seems like I’ve already kind of gotten in the way of things by turning your soup into a sugary dessert."
    os "Yeah, I’m sure. It won’t take long anyway since it’s only right down the road."

    scene wakanatriestocook28
    with dissolve

    os "Babe, could I ask you to maybe clean out the pot for me while I’m gone?"
    w "You want me to throw away the dinner I worked so hard on?"
    os "I...uhh..."
    os "I mean, I guess we could {i}try{/i} eating it if that’s-"
    w "I’m joking."
    w "Of course I’ll clean out the pot for you."
    w "Hurry home, though."

    if bonus == True:
        w "I bought a new rope that should be a little easier on-"
    else:
        w "I learned one of the Fortnite dances to impress you and-"

    scene wakanatriestocook29
    with hpunch

    os "JUST...T-TELL ME ABOUT IT LATER!"
    w "So cute. Please do hurry back."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ wakana_love += 1
    $ wakanadate5 = True

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"

    jump osakodate1

label wakanadate15:
...
```

## Code that triggers this event
File: \game\WakanaEvents.rpy
Code:
```python
...
label callwakananight:
    if wakanadate1 == False:
        play sound "phonebeep.wav"

        "I tap on Wakana's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."

        "I guess she's busy tonight."
        jump callnight

    if wakana_love >= 5 and wakanadate1 == True and kaoridate15p3 == True and wakanadate5 == False:
        jump wakanadate5
...
```