# The Way it Scatters (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Secret Weapon](./harukalust25.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo10
* Group: Main
* Triggered by label: harukalust25
* Chain sources: harukalust25
* Chain sources path: harukalust25

## Official wiki page

[The Way it Scatters](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo10&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo10:
    scene scavengerhunt1
    with dissolve2
    play music "soda.mp3"

    $ totaldays += 1
    $ day += 1
    hide saturday onlayer date
    show sunday onlayer date

    mak "Good morning, everyone. I hope you slept well since the competition you’re about to take part in is likely going to consume the majority of your day."
    mi "That’s right, gals! Silence them phones and button those blouses cause these next few hours are gonna have you wishing you were drawn for the date war instead!"
    n "But I {i}was{/i} drawn for the date war."
    a "Yeah, just brag about it, why don’t you? Real nice, Noriko."
    ay "So, what are the rules for this exactly? Is there an entire list of things we have to find or...is this going to be one of those scavenger hunts where we need to inconvenience other people in order to win?"
    ki "Also, is this really going to take that long? Because I was kind of hoping I’d get to see the maid war thing."

    scene scavengerhunt2
    with fade

    mak "The maid war is actually going to be starting in about an hour. So unless you find the {i}one{/i} item on the list almost immediately, I can’t imagine you’re going to make it."
    ki "Ugh, seriously? I wanted to see Io in a dress."
    mi "Please. Io in a dress? You’re more likely to see {i}me{/i} in a pair of khakis."
    ki "I have literally seen that before."
    mi "Pfft. As if. Khakis are so outdated it’s, like...not even funny anymore."
    n "When were they ever funny?"
    mak "Do you guys actually want to hear the rules? Or would you rather sit here and talk about pants for the next hour or two?"
    mi "Obvs the pants, Makoto. But it ain’t like I expect you to understand with that two layered crop top combo you’ve got going on. Ugh, talk about elementary school. Am I right?"

    scene scavengerhunt3
    with dissolve

    mak "I don’t like this side of you."
    mi "Settle. You’re killing the vibe."

    scene scavengerhunt4
    with dissolve

    mak" Hah..."
    mak "Somewhere in the residential section of the old district, Miku and I have hidden one of her old soccer trophies."
    mak "Whichever pair of you finds it first will be crowned the victor and earn your floor a point for the Dorm Wars."
    mak "Maps of the area will be provided for anyone who wants them. It is also urged to not approach any of the homeless people you may find wandering the streets. Please be careful."
    a "Wait, what?"
    mak "Each competitor has chosen a partner for this contest, and those partners are free to assist in whichever ways they see fit."
    mak "However, this does not include sabotaging the other team’s search...and any attempt to do so will be met with a disqualification."
    a "Ugh, darn it! There goes our plan."
    mi "Makocchi and I will be hangin’ out around here and waitin’ for y’all to come back with the trophy. But if it winds up taking too long, we’ll probs just peace it and go chill somewhere else. SNS."

    scene scavengerhunt5
    with fade

    ki "Do we need one of those maps? Because I’m not really into the idea of, you know, {i}not{/i} winning Sensei."
    n "We do not. I know these streets like the back of my hand, so you definitely made the right choice in choosing me as your partner."
    ki "Well, who else was I going to choose? Because, as far as I’m concerned, Miku won’t even exist again until Monday."
    ki "Also, the longer I get to look at you in that costume, the better. Please never wear your normal clothes again. Thanks."

    scene scavengerhunt6
    with dissolve

    n "Thanks, Kirin. I’d like to say the same to you but you are legit whoring it up right now."
    ki "In the trashy way? Or the way that makes you want to bone me?"
    n "Those things don’t have to be mutually exclusive. I can guarantee you I’ll have at least one dream about this in the near future."
    ki "That’s good enough for me. But keep in mind that my bed is always ten feet away and that you can always-"
    a "For the love of all that is holy just make out already!"

    scene scavengerhunt7
    with fade

    a "I swear, you two are less like roommates and more like...I don’t know. People who want to have sex with each other."
    n "That’s not a fair assessment when Kirin wants to have sex with literally everyone."
    ki "Not {i}everyone.{/i} Yasu gives me the creeps."
    n "Oh, come on. We both know the crazy ones are always the best lays."

    scene scavengerhunt8
    with dissolve

    ki "How do you know that when the closest {i}you’ve{/i} ever come to getting fucked is the time you slipped in the bathhouse and wound up on top of me?"
    n "Let the record show that I still don’t appreciate what you did with your knee back then."
    ay "Want to...maybe start looking for the trophy? Seems like Makoto and Miku have already stopped paying attention to us."
    a "I don’t blame them with the world’s horniest dorm room over there being all...horny and stuff."
    a "I should probably get one of those maps, though, since neither one of us has any idea where we are right now."
    a "You should probably get one too. Since we’re not allowed to sabotage floor two’s plans, it might be best if we change our strategy and split up so we can cover more ground."
    ay "Do you, uhh..."
    ay "Do you really think that would be for the best?"

    scene scavengerhunt9
    with dissolve

    a "Hm? Do you have a better idea?"
    ay "Just...I kind of figured staying together would make more sense. It’s easy to get lost around here and...we could look out for each other if those homeless people are actually threatening."
    a "I mean...I guess that’s okay, but...we’re already dealing with a bit of a disadvantage since Noriko is from around here."
    ay "Yeah but, at this rate, the two of them might not ever start looking and will just waste away the rest of the day by “being horny and stuff.”"
    a "Okay, fine. We’ll figure out a way to fully utilize the strength of two sets of eyes in one place. But if we wind up losing a point over this decision, I am going to have your head."
    ay "Is that fair when I’ve already {i}earned{/i} us one point?"
    a "Yes. A million times yes. And don’t try to convince me otherwise because serious-mode Ami is not having any of that today."

    scene black
    with dissolve

    a "Makoto! Map, please!"
    mak "Oh, good. I was beginning to think I went to the effort of drawing them for nothing."

    scene scavengerhunt10
    with dissolve2

    mak "Good luck. And please let Ayane hold the map as I’m not sure you possess the mental capacity to actually read it."
    a "Of course I can read a friggin’ map! Who do you think I am?!"
    mak "Some sort of gremlin perhaps?"
    mi "Ain’t you two friends now?"

    scene scavengerhunt11
    with dissolve

    mak "Who? Ami and me? Don’t be ridiculous. The only reason I’ve started going over her house is to tutor her."
    mi "Friends ain’t supposed to lie to each other, {i}Makocchi.{/i}"
    mak "And stop calling me Makocchi or I’m never doing your hair again. This new persona of yours is going to your head."

    scene black
    with dissolve2

    mi "Sure thing, Makocchi. Just don’t leave me for Ami, kay?"
    mak "I’m tempted to just leave you as a whole right now..."

    "........."
    "......"
    "..."
    "{i}A while later...{/i}"
    "{i}Like, a long while. Not a short one.{/i}"
    "{i}Let’s say it’s about an hour.{/i}"

    scene scavengerhunt12
    with dissolve2

    ki "Is it just me, or does the sky look unusually pink today?"
    n "I think that means tomorrow is supposed to bring good weather. It’s some old superstition or something."
    ki "How does that even happen anyway? I thought the sky was blue because of, like...the ocean."
    n "The way air molecules scatter light means sometimes redirecting the colors with shorter wavelengths like blue or green away from us."
    ki "But there’s still some blue out there."
    n "I’m not a fucking meteorologist, Kirin. I don’t know what you want from me."
    ki "Some assistance in...literally anything would be nice. We haven’t even started looking for the trophy yet."
    n "We don’t have to {i}look{/i} when I already know where it is."

    scene scavengerhunt13
    with fade

    ki "Are you kidding?! I’m missing the maids because of you!"
    n "Well excuse me for creating the perfect opportunity for you to ask about how my date went last night."

    scene scavengerhunt14
    with dissolve

    ki "Wait. Does that mean you finally-"
    n "No. I did not fuck him."

    scene scavengerhunt15
    with dissolve

    ki "Sounds like a pretty shitty date, then."
    n "We don’t all need sex in order to feel alive, you know."
    ki "Also, how do you know where the trophy is already? Aren’t you worried that Ayane and Ami are going to find it?"
    n "See that huge bush? Beside the abandoned house with the blue roof? If you look closely, you can see the trophy tucked away in there."
    n "If Ami and Ayane get close, I’ll slide down this ledge assassin-style and do a cool flip or something before swiping it up for us."
    ki "I think we should go get it now."
    n "I think you’re only saying that because you don’t want to talk about how my date went for some reason."
    n "And oh boy...I wonder what that reason could possibly be."
    ki "Not this again, please. I already told you I don’t feel that way about him."
    n "And how many more times do you think you’ll need to tell {i}yourself{/i} that before you actually believe it?"

    scene scavengerhunt16
    with dissolve

    ki "Fine. Tell me how your stupid, sexless date went. Did you do that thing you were talking about? Or did you wind up chickening out instead?"
    n "I did it. And I’m pretty sure I got through to him as well."

    if datewarnoriko == True:
        ki "No wonder you won, then. A grand gesture like that isn’t going to fail to someone like Futaba who probably just read him a fucking book or something."
        n "Futaba is sweet and I’m sure her date went well too."
        n "And yes, I did win. But that victory is just one small step in what is going to be an all-out war for my future. And having someone to talk to about that war would mean a lot to me."
        ki "That lovey-dovey stuff doesn’t sit right with me. So here’s hoping you find a different friend in the near future so I can go back to being a feelingless fuck buddy."
        n "If you’re going to refuse to be happy yourself, at least be happy for {i}me.{/i} There’s no need to rob yourself of {i}every single{/i} positive emotion that comes your way."
        ki "Keep talking and I’m going to feel obligated to pay you for this spontaneous counseling session."
        n "I just wanted you to know I did well."
        n "And that I’m going to keep doing well."
        n "So your time is running out."

        scene black
        with dissolve2
        stop music fadeout 7.0

        ki "Sucks for me, then...I guess."
        n "Hah..."
        n "Come on, let’s go get ourselves a point."

    else:
        scene scavengerhunt17
        with dissolve

        ki "What? Then how the fuck did you lose?"
        n "Probably {i}because{/i} I got through to him, if I had to guess."

        scene scavengerhunt18
        with dissolve

        n "Sensei’s been weird with feelings for as long as I’ve known him. But things got way worse after Ami’s parents died in an accident."
        n "For a while after that, I didn’t get to see him at all. But when I finally {i}did...{/i}he felt like a different person, almost."
        n "Or...maybe less like a different person and more like there was some kind of impenetrable layer around him, preventing anything from getting through."
        n "Imagine that’s you. Imagine you grow so used to feeling nothing that when you finally {i}do{/i} feel something, you can’t figure out how to process it."
        n "I think that’s what happened with him last night."
        n "So it’s obvious I’d lose after shocking him like that...but that’s fine. Because winning was never really my goal in the first place. And it doesn’t really fit me either."
        n "Futaba and the rest of the first floor girls can take their point. I don’t care."

        scene black
        with dissolve2
        stop music fadeout 7.0

        n "I’ll be happy just knowing I was the only person able to break through to him last night."

    "........."
    "......"
    "..."

    if amifingered == False:
        $ renpy.end_replay()
        $ dormwartwo10 = True

        "{i}Meanwhile...in the other half of town...{/i}"

        jump dormwartwo11

    else:
        scene scavengerhunt19
        with dissolve2
        play music "blueair.mp3"

        a "Let’s see...if that wall thing is...here...that means that...the big line on the map is probably..."
        a "I don’t know. Maybe Makoto was right and I have no idea what I’m doing with this thing. But you know whose fault it {i}really{/i} is? The phone companies for not mapping this place out on the GPS."
        a "Maybe that can be how your family’s business starts spreading into stuff that doesn’t involve bubble wrap, Ayane."
        a "I know you don’t really care about money and all that, but just think of how cool it would be to run your own company. I say you pitch it to your dad if he ever turns the smooth jazz down."
        ay "..."
        a "..."

        scene scavengerhunt20
        with dissolve

        a "Ayane?"
        ay "Oh, sorry. I zoned out for a second. Were you saying something?"

        scene scavengerhunt21
        with dissolve

        a "For real? What’s the point in teaming up if I’m going to be the one doing all of the work?!"
        a "I brought you along because I thought you’d be able to help! And also because Maya refuses to come here, but still!"
        ay "Sorry, Ami. I’m just feeling a little out of it today."

        scene scavengerhunt22
        with dissolve

        a "This is what you get for practicing your stand-up routine so much, you know. I told you to slow down. Overworking yourself is bad for you."
        a "I feel like you didn’t even use half of the jokes you prepared either, but I guess this isn’t really the time or place to be talking about contests that are already over."
        a "Just get your butt into gear so we can make sure it's our floor that gets Sensei, okay?"
        ay "Y...Yeah. Got it. My bad."

        scene black
        with dissolve2

        "........."
        "......"
        "..."

        scene scavengerhunt23
        with dissolve2

        a "Ugh...it’s no use. Even {i}with{/i} the map it feels like we’re just going in circles."
        a "If you have any suggestion for different ways to look or even...hiding places that somebody like Makoto would think of but not normal people like us...it would be great."
        a "In fact, literally anything would be great. I’m getting desperate over here and my feet hurt. I want to go home."
        ay "..."
        a "..."

        play sound "static.mp3"
        scene scavengerhunt24
        with flash
        stop sound

        a "Oh, come on! Don’t tell me you’re zoning out again!"
        a "Earth to Ayane! Wake up! If you need coffee, I say we knock on some random person’s door and see if they have a thingy we can use."
        a "I can’t guarantee that it’ll taste any good or if the water will even be safe to drink, but if poisoning you is what it takes to get you to speak up, I’m willing to try it."
        ay "I’m here. Sorry."
        ay "Just a little under the weather."
        a "You? The girl who always preaches about eating healthy and taking care of your body?"
        a "Whatever's wrong with you, I hope {i}I{/i} don’t catch it."
        a "Because if I get sick, {i}Sensei{/i} is going to get sick. And then everybody is going to get sick because we all share a classroom and germs are evil."
        a "You know what? Maybe you should head back to the hotel if you’re not feeling well. I’m sure you’ll be able to get a room for yourself since you always carry that black card around."
        ay "Actually..."
        ay "Do you think we could maybe take a little break from searching for a while?"
        a "A break? Why? We’ve only been doing this for an hour and we haven’t even found a clue yet."
        ay "I know, I know."
        ay "There’s just..."
        ay "There’s something I want to talk to you about."

        play sound "static.mp3"
        scene scavengerhunt25
        with flash
        stop sound

        a "Of course! You know I’m always here for you, Ayane."
        a "Whatever it is, you can let me know."
        ay "Yeah...Yeah, I guess it’s easy to say that now, but...it’s not really an easy topic to just...bring up."
        a "Why not? Do you not trust me? Because I’ve never let you down before, have I?"
        ay "Not...that I can think of...no."
        a "Then what’s the problem? Just say it. It’s not like I’m going to judge you or anything."
        ay "This isn’t...really about {i}me...{/i}"

        play sound "static.mp3"
        scene scavengerhunt26
        with flash
        stop sound

        a "It’s not?"
        ay "I mean...maybe a little...but it’s less about me and more about..."
        ay "Well...{i}you.{/i}"
        a "Me?"
        a "Did I do something to make you mad?"
        ay "That’s not it..."
        a "Sad?"
        ay "Again, not really. No."
        a "So...something with me is making you act weird...but I didn’t do anything to make you mad {i}or{/i} sad?"
        a "I don’t get it."

        scene scavengerhunt27
        with dissolve

        ay "Like I said, it’s a hard topic to just bring up."
        a "Well...whatever it is, rest assured that I’ll be happy to talk about it!"
        a "You’re my best friend in the whole world. You have been for years. And there isn’t anything that’s going to change that."
        ay "Ami..."
        a "I mean it! You mean the world to me and-"
        ay "Ami, I know about you and Sensei."

        stop music
        play sound "static.mp3"
        scene 1 with flash
        scene 5 with flash
        scene scavengerhunt28 with flash
        stop sound

        a "..."
        ay "Do you see now why it wasn’t easy for me to bring up?"
        ay "Like...how am I supposed to address that?"
        ay "And yeah, it would have probably been better to do this {i}not{/i} in the middle of a competition, but if you really want to know why I’m acting so weird, {i}that’s{/i} it."
        ay "It’s because I know. I know that you and Sensei-"
        a "So what?"
        ay "...What?"

        scene scavengerhunt29
        with dissolve2

        a "I said...so what?"
        ay "Do you really not see-"
        a "Is there a problem with that, Ayane?"
        a "The fact that I {i}fuck{/i} my uncle?"
        ay "Ami..."
        ay "You’re his {i}niece...{/i}"

        play sound "static.mp3"
        scene 1 with flash
        scene 5 with flash
        scene scavengerhunt30
        with flash
        stop sound
        play music "ibelieve.mp3"

        a "That’s right."
        a "I’m an insatiable...{i}incestuous{/i} little girl who gleefully lays on her back and lets her uncle climb on top of her and pin her down by her wrists."
        a "Who obediently spreads her pussy for him every time he asks...and moans every single time he thrusts into her with his monster-sized penis."
        a "And when I’m {i}not{/i} fucking him, I’m {i}thinking{/i} about fucking him."
        a "It’s my favorite thing in the whole wide world, making him happy. Being happy {i}together.{/i}"
        a "And the two of us are happiest when we’re covered in sweat and cum and forgetting everything that’s happened."
        ay "Ami..."
        a "Don’t act surprised. You know how badly I’ve wanted his dick inside of me ever since you started coming over to the house."
        a "God, it took him {i}way too long.{/i} I can’t even remember how many times I must have fingered myself under his blanket. How many holes I must have torn in my underwear while waiting for the big day."
        a "And between you and me, since we’re {i}such good friends,{/i} I’ve even put a few of my pubic hairs in his food because I believed it would make him want to fuck me {i}more.{/i}"
        a "They were tiny, sure. But I think they did the job since...well, just look at what we're talking about."
        ay "..."
        a "Does that make you think any less of me, Ayane?"
        a "Do I {i}disgust{/i} you?"
        a "Am I a bad girl because the only thing that gets me wet anymore is the thought of my uncle’s cock?"
        a "Or can you still be my friend knowing that the next time I don’t respond to your text right away, it’s probably because I’m wrapping my legs around him and screaming out his name?"
        ay "Why are you-"

        play sound "static.mp3"
        scene scavengerhunt31
        with flash
        stop sound

        a "Why am I what?"
        a "Deranged?"
        a "{i}Broken?{/i}"
        a "You probably don’t realize this because your parents are still {i}alive,{/i} but it isn’t very fun watching them die."
        a "In fact, that sort of thing can leave a lasting impression on someone."
        a "It can change who they are and what brings them joy."
        a "Then blah blah blah, sad timeskip stuff..."
        a "And now the only thing that makes me feel good anymore is being a walking fuck-doll for Sensei to use whenever he gets too hard from having pretty girls like {i}you{/i} fawn over him all day."
        ay "Ami, slow down. Please."
        a "I’m not going to stop."
        a "And neither is Sensei."
        a "This is who we are."
        a "And we don’t need someone like you getting in the way of-"

        scene scavengerhunt32
        with dissolve

        ay "Ami, I’m not trying to stop you!"
        a "..."
        ay "..."
        a "..."
        ay "..."

        scene scavengerhunt33
        stop music

        a "Hah?"
        ay "I just wanted to hear it from you!"
        ay "I know you love him and..."
        ay "And yeah, I think it’s kind of gross for you to be doing that with someone you’re related to. But if that’s really what {i}you{/i} want, then...fine!"
        ay "I’m just worried about you!"
        ay "That’s all!"
        a "You’re..."
        a "You’re...worried?"
        a "About me?"
        ay "Yes! Of course!"
        ay "I love you!"
        a "..."
        ay "..."
        ay "I really do love you..."
        a "..."

        scene scavengerhunt34
        with dissolve

        a "Well, now I just feel like an asshole."
        ay "Ami, you...you went through something horrible at a very young age. Something that, like you said, can leave a lasting impression on someone."
        ay "I’ll never know what that’s like. And I’ll never understand how it feels to be in your shoes."
        ay "But if you truly, from the bottom of your heart, believe that your...relationship with Sensei is a byproduct of true love and not trauma, that’s fine."
        ay "I can accept that."

        scene scavengerhunt35
        with dissolve2

        ay "I just..."
        ay "I didn’t want you to feel like you’re all alone..."
        ay "And that there’s no one you can talk to about it..."
        ay "Because...I..."
        ay "That’s how..."
        a "..."
        ay "That’s how I..."

        play sound "static.mp3"
        scene happily with flash
        stop sound
        $ renpy.pause(5, hard=True)

        $ renpy.end_replay()
        $ dormwartwo10 = True

        jump dormwartwo11

label dormwartwo11:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
"In the end, everyone won."
            "And by everyone, I mean just Haruka and me."
            "But I regret nothing and will sleep easy knowing that I have, once again, made the correct choice."

            $ renpy.end_replay()
            $ haruka_love += 1
            $ haruka_lust += 1
            $ harukalust25 = True
            $ harukabjwin = True
            $ dorm2war2points += 1

            stop music fadeout 5.0

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "{i}Haruka’s lust has increased to [haruka_lust]!{/i}"
            "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
            "........."
            "......"
            "..."
            "{i}Early the next morning, in the second half of town...{/i}"

            jump dormwartwo10

        "Sara":
            s "Sara..."

            scene surprisebjcontest40
            with dissolve

            sar "Mmf! Yes! I knew...mmf...you’d choose me!"
            h "What?! But I clearly have the deeper throat! Which means that I am mathematically the winner! Hooray for floor two!"
            sar "That’s not...how it works...Haru-chan!"

            with sexfade
            with sexfade
            scene surprisebjcontest41
            with cumflash
            with hpunch

            sar "MMMMMMMMMMMMMM!!!!!!!!!!!!"

            scene black
            with dissolve2

            "........."
            "......"
            "..."

            scene surprisebjcontest45
            with dissolve2

            sar "Thanks for the meal."
            h "This is a great injustice and I feel as if I have been betrayed by both of you tonight."
            s "While your...uhh...esophagal depth is commendable, there was just more passion in Sara’s blowjob."
            s "And as the former captain of the competitive blowjob varsity team, I-"

            scene surprisebjcontest46
            with dissolve

            h "I don’t want to hear it. Friendship ended with Sara. Maki is my best friend now."
            sar "This calls for a celebration. Who’s up for a second round?"
            h "Not me. It’s like 3:00 AM and my jaw hurts, so I’m going home."

            scene surprisebjcontest47
            with dissolve

            sar "Holy shit, it’s 3:00 AM?"
            h "Yup. We gave Sensei head for roughly 90 minutes. I hope you’re proud of yourself."
            sar "I..."

            scene black
            with dissolve2

            sar "Maybe just a {i}short{/i} second round, then?"
            h "Goodnight, Sara."
            sar "Haru-chan, wait! You’re my ride!"

            "In the end, everyone won."
            "And by everyone, I mean just Sara and me."
            "But I regret nothing and will sleep easy knowing that I have, once again, made the correct choice."

            $ renpy.end_replay()
            $ sara_love += 1
            $ sara_lust += 1
            $ harukalust25 = True
            $ sarabjwin = True
            $ dorm1war2points += 1

            stop music fadeout 5.0

            "{i}Sara’s affection has increased to [sara_love]!{/i}"
            "{i}Sara’s lust has increased to [sara_lust]!{/i}"
            "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
            "........."
            "......"
            "..."
            "{i}Early the next morning, in the second half of town...{/i}"

            jump dormwartwo10
...
```