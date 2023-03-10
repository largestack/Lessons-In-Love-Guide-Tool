# Happier Things (Uta)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Uta love greater than or equal to 10

* Event [War's End](./dormwar17.md) (Main) is completed)



## Next events

* [Uta: Facetime With My Mom](./utadorm15.md)

## Event properties

* Id: utamaid10
* Group: Uta
* Triggered by label: utamaid
* Triggered by branch label: utamaid
* Triggered by path: utamaid->utamaid10

## Official wiki page

[Happier Things](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utamaid10&go=Go) for more details.

## Event code

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid10:
    scene utamaidten1
    with fade
    play music "maidcafe.mp3"

    "Once again, I find myself spending way too much time and way too much money at the maid cafe."
    "I’ve been here for going on two hours so far and, despite several other customers coming in, I’ve managed to keep Uta-chan all to myself."
    "This has, of course, come at a great cost."
    "And if Yumi winds up being cut off of my phone plan as a result, I have no regrets."

    s "Hey, Uta. How would you feel about Yumi working here so I don’t have to pay for her cell phone anymore?"

    scene utamaidten2
    with dissolve

    u "Yumi? Working here?"
    u "Not just anybody can be a maid, Master. This line of work takes a surprising amount of skill and perseverance."
    s "True. She might be a “business owner,” but I don’t think she’s quite conniving enough to hold down the fort here."

    scene utamaidten3
    with dissolve

    u "Now you’re startin’ to get it."
    s "Also, aren’t you going to ask about why I’m paying for her phone bill?"

    if bonus == True:
        u "Is it cause she’s poor and you want her to touch your wiener?"
        s "That-"
        s "I mean, you’re not entirely wrong."
        s "I don’t think you’re allowed to say “wiener” while you’re working, though."
    else:
        u "Nope! Cause I know you'd do it for me too if I asked!"

    u "Master is a special customer who won’t tell my boss even if I start doing really mean things like spitting in his food or stealing money directly out of his wallet."
    s "To be fair, I think I’ve already proven that my wallet is as good as yours."

    scene utamaidten4
    with dissolve

    u "Poor Ami. She’s so dedicated to you and yet here you are, flirting with her senpai. "
    s "Yes but, on the bright side, she at least has some spending money now."

    scene utamaidten5
    with dissolve

    u "But not as much as {i}I{/i} do..."
    u "You know, Master...maybe if you bought Uta-chan a car...you would get to see her a little more often."
    s "I haven’t even bought a car for myself yet."
    u "Wanna share one?"
    u "You’ve gotta put it in your name, though, cause I don’t have any credit history yet."
    s "Please don’t push me on this because I {i}will{/i} cave if you’re the one asking."
    u "Pleeeeease, Master? Uta-chan’s been such a good girl."

    scene utamaidten6
    with dissolve

    u "She even made all this delicious food for you all by herself."
    s "I know for a fact that you have other maids cooking in the back room. "
    u "But if you use your imagination, it’s exactly like {i}I{/i} made it, right?"
    s "Wrong. And you’re not getting a car."

    scene utamaidten7
    with dissolve

    u "But...but I wanted to take you somewhere special to me..."
    s "…"
    u "I guess you hate me, though..."
    s "What is this “special” place you were going to take me to, Uta-chan?"

    scene utamaidten8
    with dissolve

    u "The mall. "
    s "That’s hardly special."
    u "Isn’t any place special as long as you leave happier than you were when you arrived?"
    s "Not if it comes at the cost of half of my salary and-"
    s "Oh. Wait. That's around the same amount I'm spending here."

    scene utamaidten9
    with dissolve

    u "Yup! And this place is the most special place on earth to you!"
    u "You’ve really got to stop being so easy, though, Master. Uta-chan might be the perfect maid and she might like you very much, but you still work just as hard as-"
    s "I’m going to stop you right there because we are both well aware that I do not work hard at all."

    scene utamaidten10
    with dissolve

    u "Thanks, I don’t know if I was gonna be able to finish that sentence anyway."
    u "In fact, I’m pretty sure I worked harder on the whole dorm wars thing than you’ve worked since I transferred in."
    s "That’s a very fair assessment. However, I implore you to remember who it was that {i}judged{/i} those competitions."

    if bonus == True:
        u "Did having your childhood girlfriend ride your morning wood while Makoto and I spectated tire you out?"
    else:
        u "Did having your childhood girlfriend giving you a sleeping potion tire you out?"
        s "Well, that {i}is{/i} the purpose of a sleeping potion. Also-"

    s "Noriko’s {i}sister{/i} was my childhood girlfriend. Not Noriko."
    s "Also, how do you know that?"

    scene utamaidten11
    with dissolve

    u "I didn’t..."
    u "I was just makin’ a joke and now I know a thing that’s gonna really upset Maya when she finds out you’re cheating on her."
    s "For the millionth time, Maya and I are not dating."
    u "Does Maya know that?"
    s "Maya will tell you the same exact thing."

    if bonus == True:
        u "Maya told me you two go at it all night long."
    else:
        u "Maya told me you like to sleep under the bed sometimes."

    s "I know Maya well enough to confirm that this is not a thing she would ever say."

    scene utamaidten12
    with dissolve

    u "A-ha! So you {i}are{/i} dating!"
    s "No."

    if bonus == True:
        u "I bet you two bang like bunnies in her dorm room while Ami is here at the cafe!"

        "{i}God I wish.{/i}"

        s "Ami works mornings. Even I’m not so much of a degenerate that I would wake up extra early just to go have sex with someone."

        scene utamaidten13
        with dissolve

        u "Wh...What if that someone was..."
        u "Me?..."
        s "…"
        u "…"
        s "I would go a year without sleeping if it meant even seeing you naked."
    else:
        u "So you admit it!"
        s "No."

    play sound "thump.mp3"
    scene utamaidten12
    with hpunch

    u "A-ha! I knew it!"

    if bonus == True:
        u "And sorry, Master! But you’re still a bajillion years away from seeing Uta-chan’s little girls up close and personal!"
        u "Maya, though-"
        s "I feel like that’s somehow even further off."

    scene utamaidten14
    with dissolve

    u "I feel like you’re a bad judge of character."
    u "Didn’t you see how she freaked out when Noriko transferred in? Why would she have done that if she didn’t feel something for you?"
    s "Because she feels many {i}negative{/i} things about Noriko."
    u "And that’s not just you in denial?"
    s "You know what? Let’s just talk about something else."
    u "Must be kinda exhausting having so many people you’ve gotta split your time between, huh?"
    s "It’s less exhausting if I can manage to keep all of that time a secret from literally everyone."
    u "Aren’t ya telling the wrong person? I can’t be trusted with that kinda info."
    s "It’s fine because I’m telling Uta-chan and not Uta."

    scene utamaidten15
    with dissolve

    u "Ah! Loophole!"
    u "Uta-chan doesn’t go to[school], so all of the secrets she knows disappear and reset each time she switches character modes!"
    u "You’re a genius, Master!"
    s "No, I’m just very good at concealing inevitable truths from myself and everyone around me."

    if dormwarfloor1win == True:
        scene utamaidten16
        with dissolve

        u "Speakin’ of inevitable truths...enjoy your stay with the stupid floor one girls during the beach trip and not with us cuter, spunkier gals from the second floor!"
        s "Sounds to me like someone is still a little bitter about losing."
        u "As bitter as the black coffee that I also made for you all by myself."
        s "It’s a little less impressive making coffee than it is making like four different entrees."
        s "Thankfully, you didn’t make any of those, so it’s not something we should worry about right now."

        scene utamaidten14
        with dissolve

        u "Did you at least have fun?"
        u "Makoto and I busted our butts and, even if my floor doesn’t get to keep you overnight, I still feel like we all got a little closer to you and everybody else."

    if dormwarfloor2win == True:
        scene utamaidten12
        with dissolve

        u "Speakin’ of inevitable truths, how ‘bout those second floor gals, right?!"
        s "Is it time to brag about your recent victory?"

        if bonus == True:
            u "It’s time to brag about Uta Ushibori’s recent victory! Uta-chan has no affiliation with that tiny bundle of boobies!"
            s "Well, I’m glad that you won. It was a well fought battle and I’m excited to-"
            u "Get busy with a bunch of thirsty girls in the middle of the night?!"
            s "Shh. Maya could be around the corner and we don’t want her to get jealous."

            scene utamaidten15
            with dissolve

            u "Ah! Good point! If you’re cheatin’ on her, we’ve gotta keep it a secret!"
            s "Thank you for understanding, Uta-chan."
            u "Yeah! If Maya finds out and kills you, who else will buy every item on the menu three times a week?"
            u "I’ve gotta make money somehow, Master!"
            s "Oh."
            s "Oh..."

            scene utamaidten14
            with dissolve
        else:
            u "We're the fucking best! Ain't nobody got shit on us!"
            u "Fucking floor one chumps think they're all that. They ain't shit! Fuck 'em!"
            s "You are so vulgar in the Patreon version."
            u "Fuckin' right I am!"

        u "Did you have fun, though?"
        u "During the dorm war, I mean."
        u "Makoto and I busted our butts on that thing."

    if dormwartie == True:
        scene utamaidten16
        with dissolve

        u "Speakin’ of inevitable truths, how the heck did the dorm war end in a tie?!"
        s "Uta, do you understand what the word “inevitable” means? Because that outcome was definitely not something predetermined and it’s my fault things ended up that way."
        u "Then why’d ya let that happen?! That was a great chance to prove to us second floor girls that we’re not too far behind the rest of the crowd!"
        s "I just judged the competition based on who I thought should win. It wasn’t about who is further ahead or further behind in terms of relationships with me."

        scene utamaidten14
        with dissolve

        u "I know, I know..."
        u "Just kinda anticlimactic to spend the whole weekend fighting and then not even have a winner."
        u "Did you at least have fun, though?"

    s "Yeah. I had a lot of fun. And I’m sure the beach will be just as good."

    scene utamaidten17
    with dissolve

    u "Yeah...what’s up with that, by the way?"
    s "What do you mean?"
    u "I mean like, why organize a trip to the beach in winter? Isn’t that a little weird?"

    "It’s not like that was the {i}original{/i} plan."
    "We just...apparently do that every other cycle or something?"

    if bonus == True:
        "I still have no idea how or why it works, but I’m not about to question the mysteries of the universe if they're going to create more opportunities for me to see girls with less clothing on."

    s "Beats me. But a vacation is a vacation."

    scene utamaidten18
    with dissolve

    if bonus == True:
        u "Ahh, yes. Yes. Of course you wouldn’t question the reasoning behind it because you know you’ll get to stare at my butt for {i}real{/i} this time."
        s "Exactly."
        u "Do what you must. But please do not touch the merchandise without first putting a down payment on it."
        s "Is everything I spend here not enough of a down payment?"
        u "Cheating is bad, Master. I can not support your efforts to mislead Princess Maya no matter how much you like my butt."
    else:
        u "Here's hoping I don't see anyone drown this time."
        s "What?"

    u "On a more serious note, though, I am kinda worried about this whole beach thing."

    if bonus == False:
        s "How is that more serious?"

    u "We had a couple ponds and stuff in Nara, but I’ve never been in the ocean before."

    scene utamaidten19
    with dissolve

    u "You gonna protect me from sharks and stuff? And make sure I don’t drown?"
    s "I was kind of planning on just watching from the sidelines and then probably going back to my room to relax."

    if bonus == True:
        "And by relax I mean have sex with an assorted variety of girls because it is much harder to contain myself in situations where I am permanently erect."

    scene utamaidten20
    with dissolve

    u "Ugh! You and Io are exactly the same! Always bein’ so...antisocial and stuff."
    u "Like, what’s so hard about goin’ out there and havin’ fun?! Jeez!"
    s "Having fun is exhausting. I’d much prefer to keep myself separated from that side of existing and simply reap the benefits that come from {i}other{/i} people having fun."

    scene utamaidten21
    with dissolve

    u "Guh. No wonder she snuck into your room instead of joining in on our slumber party."
    s "Uhh..."
    s "I’m just going to assume she told you and that you’re not secretly surveilling my every move."

    scene utamaidten22
    with dissolve

    u "Yeah, but don’t get mad at her about it. I kinda forced it out of her."
    u "Io can be really complicated, but I know how to deal with her for the most part."
    u "Takes one to know one and all that."
    s "I definitely don’t see any sort of resemblance between the two of you, so I’m not sure how accurate that last statement is."

    scene utamaidten23
    with dissolve

    u "Okay. Maybe I’m a little {i}less{/i} complicated than her...but that doesn’t mean what you see is what you get."
    u "We’re all a little complicated in our own ways, Master."
    u "Io...me...you..."
    u "But that’s what makes us people. Nobody can be happy all the time and we’ve all gotta do everything we can to keep a smile on our faces, even when it seems impossible to do that."
    s "Am I going to be charged extra for this life lesson? Because I’m kind of running out of money."

    scene utamaidten24
    with dissolve

    u "Course not."
    u "I’m just sayin’ that you can never really know what somebody is like unless you spend lots and lots of time with them."
    u "That’s why I feel comfortable saying I’m not much different than Io."
    u "We’ve just got...unique ways of handlin’ the stuff that hurts us the most."
    u "I’m sure you do too."
    u "But it’s not up to me to point out your bad sides. ‘Specially not while I’m wearin’ a maid outfit."
    s "Excuse me, Uta-chan, but you shouldn’t be pointing out or acknowledging that I even {i}have{/i} bad sides while you’re wearing that outfit."

    scene utamaidten25
    with dissolve

    u "R-Right...I’m sorry, Master."

    scene utamaidten26
    with dissolve

    u "So, back to happier things!"
    u "How ‘bout you tell me what exactly went down with you and Io at your hotel room?"
    u "She kinda skimped me on the deets."
    s "I wish the answer was exciting or interesting, but it’s actually kind of depressing."
    u "I’m all ears, Master! Let Uta-chan wash those worries away!"

    scene black
    with dissolve2

    "I tell Uta about the morning after Io snuck into my room, but conveniently leave out all of the details about how said morning ended up."
    "It’s one thing having Io know about Chika, but trusting someone like Uta with that information seems like it could lead to catastrophe rather quickly."
    "It’s strange having one girl who loves secrets but can’t keep them paired with a second girl who hates secrets and {i}does{/i} keep them."
    "But I guess there’s not much helping it."
    "Maybe the two of them do have more in common than I realize."
    "But, at least on a surface level-"
    "I can’t see it at all."
    "I stay for another hour or so before Uta needs to stop talking to me and focus on closing the store."
    "And, as always, I head home with my hands in my pockets- one of them wrapped tightly around a wallet that is much lighter than normal."
    "This girl is going to bleed me dry."

    $ renpy.end_replay()
    $ utamaid10 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label utamaid20:
...
```

## Code that triggers this event

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
    if uta_love >= 5 and utamaid1 == True and day > 5 and utamaid5 == False:
        jump utamaid5
    if uta_love >= 10 and dormwar17 == True and utamaid10 == False:
        jump utamaid10
...
```