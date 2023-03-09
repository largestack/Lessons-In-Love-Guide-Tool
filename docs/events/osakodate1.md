# Pressure Point
Osako event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=osakodate1&go=Go)


Part of event chain [Soup, or Another Year With You](./wakanadate5.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Osako: Floating Forever, Unfulfilled](./osakodojo1.md)

## Event properties
* ID: osakodate1
* Group: Osako
* Triggered by label: wakanadate5

## Event code
File: \game\OsakoEvents.rpy
Code:
```python
...
label osakodate1:
    if bonus == True:
        "Osako, who must now distract herself from the idea of being tied up and teased by her girlfriend later tonight, exits the apartment by my side and leads me down the stairs."
    else:
        "Osako, who must now distract herself from the thought of her girlfriend doing the Fortnite dance, exits the apartment by my side and leads me down the stairs."

    "Just like she said, it’s not a far walk as I can already make out the light of the convenience store from around the corner."
    "………"
    "……"
    "…"

    scene osakoconvenience1
    with dissolve2

    os "So..."
    os "Can’t really say I expected to find myself out with you of all people on my anniversary."
    s "Hey, you’re the one who invited me. I was more than willing to go home."
    os "I know, I know."
    os "It’s just..."

    scene osakoconvenience2
    with dissolve

    os "It’s the first time Wakana’s ever gone out of her way to contact anyone who isn’t me, I think."
    os "Normally she’s just all like-"

    scene osakoconvenience3
    with dissolve

    os "Why would I expel the energy necessary to call someone when I have absolutely nothing to gain from doing so?"
    s "Wakana would say {i}that?{/i} No way."
    s "That’s impossible."

    scene osakoconvenience4
    with dissolve

    os "It was just a little weird, you know? "
    os "Like, I’m glad that she finally has a friend and whatnot, but it’s just..uncharted territory, I guess."
    s "We’re not particularly close or anything, if that’s what you’re worried about."
    s "I normally wait until a person’s significant other is in space before I think about making a move on them."
    s "And even then it’s a sort of case by case basis."
    os "Is that supposed to make me feel more comfortable about this?"
    s "If you’re uncomfortable as it stands, isn’t that on you in the first place?"

    scene osakoconvenience5
    with dissolve

    os "Of course it is. It’s just..."
    os "I’m totally in love with Wakana and, despite her tendency to repeat the same thing over and over and over, she’s always been a little unpredictable."
    os "Like she doesn’t completely understand how other peoples’ feelings work. Myself included."
    os "But she tries for me, at least. And I love that about her just like I love everything else."

    scene osakoconvenience6
    with dissolve

    os "Shit, what am I even saying right now? You don’t want to hear about this."
    s "I don’t...{i}not{/i} want to hear about it either."
    s "You said you had something to talk to me about, so I figured through context clues that it would just be you ranting about how much you love goth girls for a few minutes or something."

    scene osakoconvenience7
    with dissolve

    os "Not just {i}any{/i} goth girls, dick. Wakana specifically. "
    os "Frankly, I’m still surprised she even settled for me in the first place considering that my style is essentially the polar opposite of hers."
    s "You’re both cute in your own ways."

    scene osakoconvenience8
    with dissolve

    os "Stop calling me cute or I’ll break your kneecaps."
    s "I’m sorry."
    s "Can I still call your girlfriend cute, though? Or is that off limits too?"
    os "You can call her whatever you want so long as you don’t try to make any actual moves on her."
    s "You’re not afraid she’d actually go along with it, are you? Because she clearly likes you a lot if she’s going to ask people for help just to try and cook something for you."

    scene osakoconvenience9
    with dissolve

    os "I like to think that too."
    os "But...I don’t know."
    os "Even though we tell each other we love one another all the time, she still feels weirdly distant on occasion."
    os "And, it’s probably self-explanatory due to the whole karate thing, but I have a tendency to be a little...defensive, I guess."
    os "Not just with myself but with anything I want to protect."
    os "And I swore back in college that I’d protect her for the rest of my life, even if she didn’t want me to."
    s "So, if she never accepted your confession, you’d just...stalk her every hour of every day and defend her from anyone who tried to get close?"
    os "Yeah...probably...I don’t know."
    s "Well, that’s not creepy at all."

    scene osakoconvenience10
    with dissolve

    os "I can’t help it, okay?! "
    os "Wakana’s not like a normal person! She’s like a...scared little puppy that you need to be really gentle and careful with if you ever want her to warm up to you!"
    s "I mean, I never had to do that."

    scene osakoconvenience11
    with dissolve

    os "That’s...exactly why I feel so weird about all of this."
    os "And a big part of why I wanted to talk to you."
    os "For some reason, Wakana warmed up to you almost right away."
    os "Way quicker than she did with me and the two of us are in an actual relationship now."
    os "So I can’t help but overthink that since it’s just...a brand new thing I’ve never had to deal with."
    s "I’m not going to steal your girlfriend, Osako."

    "Probably."
    "Especially since I’d likely die the second I tried anything."

    os "It’s not just the actual act of you “stealing” her. It’s a...fear I have that maybe she’ll realize that she wants something else."
    os "And that we’ll revert to being friends or something if she starts thinking that things aren’t as good as they could be with a different person."
    s "I’m going to be honest, you were the last person I thought I’d have to coach some self-esteem back into."
    os "I’m going to be honest too and say that you’re the last person I thought I’d ever have to talk to about this."
    os "Just being strong physically doesn’t make me strong as a person, you know. I’m actually annoyingly sensitive when it comes to stuff like this."
    os "Wakana’s the tough one. But I think a lot of that is just because she doesn’t really see the world the same way most other people do."
    s "…"
    os "…"

    "We’ve already made it to the convenience store, but have yet to set foot inside and disturb the employees with our decently personal conversation."
    "A conversation I had a feeling was going to be inevitable from the moment I got Wakana’s phone number."
    "I’m not entirely used to engaging in relationships with people whose significant others are not {i}missing{/i}, so at least I can be glad this is happening now rather than later."
    "Preferably, I’d like if it wouldn’t happen at all."
    "But not even my life can be as convenient as that."

    s "I have a question for you."

    scene osakoconvenience8
    with dissolve

    os "You do? About Wakana?"
    s "More or less."
    s "My question is...if you really do care about her, shouldn’t you {i}want{/i} her to figure out whether what she truly wants is you or not?"

    scene osakoconvenience12
    with dissolve

    os "I do. But that doesn’t mean I’m not going to worry about it as well."
    os "She’s everything to me. And the thought of that changing is just..."
    s "Let me clarify that I don’t think you need to worry about that. "
    s "I haven’t known Wakana for long, but the things she said about you today made me realize that she’s so into you that she wouldn’t even consider romance with someone else."
    os "Consideration doesn’t really have anything to do with it."
    os "Wakana’s not as...calculated as she might make it seem. She’s actually pretty neurotic and impulsive at times. "
    os "She can think one thing but then do something else. And things like that aren’t always easy to suppress, which is why I’ve always kept a close eye on her."

    scene osakoconvenience13
    with dissolve

    os "Well...I kept a close eye on her even before I knew that because...holy shit, she’s so hot. "
    os "But yeah. "
    os "I guess I just think everything right now is a little too good to be true."
    os "And that one day she’ll snap out of what’s been such a happy dream for me and move onto bigger and better things."

    scene osakoconvenience14
    with dissolve

    os "I don't know."
    os "Sorry for springing this on you out of nowhere. I’m just really afraid of losing her and...I guess I wanted you to know that?"
    s "Why are you wording that like a question?"

    if bonus == True:
        os "Probably because I still don’t understand {i}why{/i} I wanted you to know that when you’re already fucking Ayane."
    else:
        os "Probably because I still don’t understand {i}why{/i} I wanted you to know that when you’re already Ayane's hug partner."

    s "…"
    os "…"
    s "I’m-"
    os "You totally are."
    s "You don’t-"
    os "Don’t even try to deny it. It’s so obvious."
    s "…"
    os "…"

    scene osakoconvenience15
    with dissolve

    if bonus == True:
        "Damnit, Ayane."
        "Why must your love for me be so powerful?"
    else:
        "I do really love her hugs."

    os "I’m also a little mad that you got to see Wakana in an apron. I wanted that to just be a {i}me{/i} thing."
    s "She looked surprisingly...homely for a woman who would likely have trouble microwaving instant ramen."
    os "And on that note, we should probably head inside so we’re not out here looking like we actually enjoy each other’s company."

    scene osakoconvenience16
    with dissolve

    s "Wait...are {i}both{/i} of you tsundere?"
    os "Hm? Wakana, maybe a little bit. "
    os "But you’d absolutely know if I had any feelings for you. I make very little effort to actually hide them."
    s "This hurts me. "

    scene osakoconvenience17
    with dissolve

    if bonus == True:
        os "Well, sorry to hurt ya even more, but that weird banana shaped muscle you’re already sharing with Ayane would be a no-go for me in the first place."
    else:
        os "Well, sorry to hurt ya even more, but I'm not into guys in the first place."

    s "So it’s not just me, it’s men in general."
    s "That somehow makes me feel a little bit better."
    os "It’s also kinda you. "
    os "You’re fine to talk to...but even if I did like dudes, you're too much of a wimp."
    s "…"
    os "…"
    s "Okay, time to shop."

    scene black
    with dissolve

    "Osako and I enter the convenience store and I can immediately tell just how often she does this."
    "She moves through the narrow aisles with surgical precision, placing ingredients neatly into a basket that she grabbed just beyond the store’s automatic doors. "
    "There’s little to no conversation on the inside, which I imagine is due to the fact that we last left off on the...sheer concept of penises."
    "But, at the same time, I feel like Osako has already said everything she wanted to say in the first place."
    "She’s madly in love with Wakana Watabe. This much is entirely irrefutable."
    "In fact, even if the two of them wound up breaking up, I can see Osako sitting quietly on a porch somewhere, growing old and withering away while thoughts of Wakana still dance around in her head."
    "I wonder if I’ll ever be able to feel that way about anyone."
    "And then I think about all of the people who feel that way about me."
    "It ruins my night."
    "………"
    "……"
    "…"

    scene osakoconvenience18
    with dissolve

    os "Okay! Now we’re ready to make actual soup that isn’t filled with Jell-O."
    s "Oh, am I coming back with you?"
    os "Nope! By “we” I meant Wakana and I."
    s "Wakana and {i}me{/i}."
    os "Fuck off. Only Wakana can correct {i}I{/i}."
    s "Now you’re just fucking with me on purpose."
    os "Damn right me am."

    scene osakoconvenience19
    with dissolve

    os "Thank you, though."
    os "Not just for hearing me out, but for being a friend to the girl I love more than anything else in the world."
    os "And remember...if you {i}do{/i} try anything, I know of seven different pressure points on your body that could kill you instantaneously."
    s "There is no way that’s true. "
    os "Play your cards right and you’ll never have the displeasure of finding out!"
    s "It’s terrifying how you can smile like that while threatening to kill me."
    os "If it’s to protect my cute little fallen angel, I can do anything."

    if bonus == True:
        s "You mean anything except feeling totally comfortable with her associating with someone of the opposite sex because you’re afraid she’ll suddenly discover how awesome she thinks penises are."
    else:
        s "You mean anything except feeling totally comfortable with her associating with someone of the opposite sex."

    scene osakoconvenience20
    with dissolve

    os "Okay, now you’re just being an asshole."
    s "I’m always an asshole. You just don’t have enough experience with me to realize that."
    os "I have even more experience with you than Wakana does. I’ve been giving you karate lessons for like...I don’t even know how long now."
    s "Correction- you’ve been {i}trying{/i} to give me karate lessons. "
    s "You have yet to succeed."

    scene osakoconvenience19
    with dissolve

    os "Oh yeah? Looks like I might have to try a little harder next time, then."
    os "Hope you’re ready to feel sore all over for the next year."
    s "What are you going to do to me?"
    os "Hm. Maybe reveal one of those seven pressure points?"
    s "If I delete Wakana’s number from my phone, will you allow me to keep my life?"

    scene osakoconvenience21
    with dissolve

    os "You don’t have to stop talking to her or anything, dude."
    os "Just...keep in mind that she’s everything to me. And that without her I’d be absolutely nothing."
    s "Sounds good. "

    if bonus == True:
        s "Anyway, enjoy getting tied up and edged tonight."
    else:
        s "Anyway, enjoy combing your girlfriend's hair and doing a whole bunch of other cute feminine things I only kind of want to be included in."

    scene osakoconvenience22
    with dissolve

    os "I will, thank you very much!"

    if bonus == True:
        os "And I hope {i}you{/i} enjoy sexting one of your students!"
        s "I don’t really do that. I much prefer actual physical-"
    else:
        s "Do you think that maybe someday I could...also drop by and-"

    os "Die!"

    if bonus == True:
        os "I mean...bye!"
        os "Go away!"
    else:
        s "I'm sorry...I just wanted to feel included once..."
        s "I am very uncomfortable with who I am as a person."

    scene black
    with dissolve

    if bonus == True:
        "Osako storms off in the opposite direction with a shopping bag pressed firmly between a set of fingers that will likely wind up inside a coworker of mine tonight."
        "I contemplate whether or not this “sexting” thing is truly worth it-"
        "But then realize that I have a perfectly good lesbian fantasy to continue playing out in my head as soon as I get home."
    else:
        "Osako leaves and I cry for a few hours."
        "I am so sad."

    $ renpy.end_replay()
    $ osako_love += 1
    $ osakodate1 = True
    stop music fadeout 5.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label osakodojo1:
...
```

## Code that triggers this event
File: \game\WakanaEvents.rpy
Code:
```python
...
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
...
```