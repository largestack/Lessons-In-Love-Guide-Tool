# Someone Else's Skin
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikuspecial50&go=Go)



## Event preconditions
✅Miku love greater than or equal to 50

❌Event "[Main: Glued to the Sky](./christmastwo20.md)" is completed (event=christmastwo20)

❌Event "[Miku: Chrysalis](./mikudorm45p2.md)" is completed (event=mikudorm45p2)

✅mikunumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: mikuspecial50
* Group: Miku
* Triggered by label: callmikuafternoon
* Triggered by branch label: callafternoon

## Event code
File: \game\MikuEvents.rpy
Code:
```python
...
label mikuspecial50:
    play sound "phonebeep.wav"
    stop music fadeout 10.0

    "I tap on Miku’s name in my phone and wait for her to answer."

    if bonus == True:
        "I figure that since soccer practice is over, now is the best time to invite her to the mall and take all of her clothes off."
        "Are there going to be other steps in between those two things? Of course. But I’m a lot less interested in those than I am in the end goal here."
        "Even if that goal will likely be obscured by a curtain since I doubt Miku’s level of aggression has moved far past spur of the moment makeout sessions."
        "Guess there’s only one way to find out, though."

    play sound "phonebeep.wav"

    mi "..."
    s "..."
    s "Miku?"

    play music "lifeismostlygood.mp3" fadein 3.0

    mi "Heeeeeeeeeeeeeeeeeey..."
    s "..."
    mi "..."
    s "If you’ve been kidnapped and can’t talk about it, cough and I will call the police."
    mi "I ain’t locked in somebody’s trunk right now, Sensei. I’m friggin’ nervous, okay?"
    s "About what?"
    mi "Well...aren’t ya callin’ me to go on that date thingy we talked about?"
    s "I guess, but I don’t really see why you’d be nervous about that when we’re together all the time."
    mi "It’s less the whole “spendin’ time together” part and more the “I’m gonna look like an idiot” part."
    s "Then just...don’t try on idiotic looking clothes? Is that good moral support?"
    mi "Not really, no. "
    s "Well, do you want to meet up or not? Because if you’re going to back out-"
    mi "No! We can still meet up! I’ve just gotta get ready!"
    s "Fine. But if you show up with another handwritten intervention sign, I am leaving you stranded at the mall."
    mi "Okay, good. Cause I was wonderin’ how I was gonna carry it all the way over there in the first place."
    mi "But anyway! I’ll see you there!"
    mi "And please don’t make fun of me when ya see me! "
    s "But why-"

    play sound "phonebeep.wav"

    s "..."

    "Miku hangs up the phone and I’m suddenly left wondering what exactly I would be making fun of her {i}for.{/i}"
    "The only thing I can think of is that stuff Makoto said the other night about doing her hair. But it’s been way too short of a time for it to finish growing and-"

    play sound "static.mp3"
    scene amisepiathing with flash
    stop sound

    a "The same way Maya can eat more than her body weight in food and Ayane can materialize guns and giant bananas out of thin air."
    a "Cute girl magic!"

    play sound "static.mp3"
    scene noonsky with flash
    stop sound

    s "No...there’s no way."

    scene black
    with dissolve2

    "I’m sure I’ll figure out whatever it is Miku is concerned about as soon as I make it to the mall."
    "........."
    "......"
    "..."

    scene mikugirly1
    with dissolve2

    "Miku somehow manages to make it there before me and sends me a text about where to meet up with her."
    "However, when I approach the meeting spot, I only see a tree."
    "I wonder if that means anything."

    s "{i}Ahem.{/i}"

    scene mikugirly2
    with dissolve

    mi "Ah!"
    s "..."
    mi "..."
    s "Miku, stop pretending to be a tree and look at me."
    mi "I don’t wanna. I look weird."
    s "I can neither confirm nor deny that on account of your face being shielded, but I can assure you that you probably look fine."
    mi "Sayin’ “probably” kinda makes it sound like ya ain’t so sure, Sensei."
    mi "I know you’re supposed to dress a little better than normal for stuff like this, but I barely even feel like Miku right now."
    s "I feel like that should technically make things easier."
    s "If you don’t feel like Miku, you can act like whoever it is you {i}do{/i} feel like and come out from behind the tree since there would be nothing to be embarrassed about."
    mi "The heck are you even talkin’ about right now? That didn’t make any sense at all."
    s "Just come out from behind the fucking tree, Miku."
    mi "..."
    s "..."

    scene mikugirly3
    with dissolve

    mi "Did ya really have to curse at me?"
    s "Is that...really you?"

    scene mikugirly4
    with dissolve

    mi "I told ya it was weird! This kinda look doesn’t suit me at all! And my hair hasn’t been this long in years! It keeps gettin’ in my eyes!"
    s "Where did you even get that outfit? I thought the whole purpose of us coming here was to buy you summer clothes?"

    scene mikugirly5
    with dissolve

    mi "Makoto got it for me as a present to celebrate my first time going out with a boy."
    s "Well, that explains why it fits you so well. There isn’t really anyone who knows you better than she does."

    scene mikugirly6
    with dissolve

    mi "Fits me well? You kiddin’ right now? My arms feel so exposed that I can barely even remember I’m wearin’ a shirt."
    mi "Or a...blouse, I think? What am I supposed to call this thing, Sensei? I have no friggin’ clue."
    s "Let’s just call it “cute” and get on with our date, then."

    scene mikugirly7
    with dissolve

    mi "Cute?! Oh God- is this how Karin always feels when ya tell her she looks like that?! I think I’m finally startin’ to get it!"
    s "Miku, step away from the tree."

    scene black
    with dissolve2

    mi "Fine! I’m goin’! But if you start laughing, I’m runnin’ the heck outta here!"

    "........."
    "......"
    "..."

    scene mikugirly8
    with dissolve2

    s "Wow."
    s "What a turnaround."
    mi "That’s what I’m sayin’. S’like I’m a completely different person right now. Nearly jumped outta my socks when I looked in the mirror before leavin’."
    s "Don’t get me wrong, I thought the whole “tomboyish charm” thing was adorable most of the time, but I think this works just as well."
    mi "Even if it ain’t really normal Miku anymore?"
    s "I don’t see why there can’t be two normal Mikus. All that should really matter is whether or not {i}you{/i} like it."
    mi "How am I supposed to know that, though? I don’t really have any idea how I feel right now."
    mi "It’s harder to move around in this...my arms and legs are cold...and I keep feelin’ like people are starin’ at me cause they think I’m some crossdressin’ [teenage]boy."
    mi "But I guess...it doesn’t look as bad as I expected it to when I first saw the outfit."
    mi "I still think it’d look better on somebody like Makoto, though. Sure, she’d have to shrink a few sizes to get it on, but I think she’d make me look like the friggin’ poser I am if she were to wear this."
    s "I don’t know. I think it fits you really well."
    mi "You also thought a stuffed bear fit me well, so you’re probably just confusin’ me for a normal girl or somethin’."
    s "Nah. I know full well that despite everything you say, you’re just as “girly” as everyone else."

    scene mikugirly9
    with dissolve

    mi "Am not!"
    s "Is that really something you want to be arguing?"
    mi "I don’t know! Maybe?! I feel...weird! And now {i}you’re{/i} lookin’ at me too and it’s really makin’ me wanna change back into somethin’ more comfortable!"
    s "I wouldn’t be staring so much if I wasn’t so attracted to you, so this is kind of your fault."

    scene mikugirly10
    with dissolve

    mi "Not sure how you can feel that way about somebody like me, but...thanks."
    mi "I still don’t really think it works, but...I guess I could maybe wear this again in the future if ya actually {i}do{/i} like it as much as ya say."
    mi "Right now, though...I don’t really think I’m comfortable in this, Sensei..."
    mi "And I kinda wanna just go put somethin’ else on."
    mi "Havin’ to focus on lookin’ pretty {i}and{/i} bein’ on a date is like...some advanced level technique. I ain’t ready to multitask like that just yet."
    s "Fortunately, I don’t think you need to focus at all in order to be pretty."

    scene mikugirly11
    with dissolve

    mi "Stop bein’ so cool! Can’t ya see I’m goin’ through a crisis right now?!"

    if bonus == True:
        s "What do you want to do then? Go find an outfit that makes you feel more like “normal” Miku and less like the Miku that is presently giving me an erection?"
        mi "Don’t go gettin’ one of those in public! People are already lookin’ over here because of the crossdressin’ boy you’re hangin’ out with!"
        s "Stop calling yourself a boy and go take your clothes off."
        mi "Now?! This is goin’ way too fast!"
    else:
        s "What do you want to do then? Go find an outfit that makes you feel more like “normal” Miku and less like the Miku that I presently want to hug?"
        mi "Yes! But I am having a difficult time choosing a store! Whatever will we do?!"

    s "Just choose a store, Miku. Preferably sometime before summer."

    scene mikugirly12
    with dissolve

    mi "Uhh...maybe that place Chika works at, then? They looked like they had a pretty decent variety when we went there that one time."
    s "Choose literally any other store."

    scene mikugirly13
    with dissolve

    mi "You avoidin’ Chika now? How come?"
    mi "This another one of those girls Makoto’s suspicious of you spendin’ too much time with?"
    s "Perhaps. I just know she’d get a little jealous if she saw me with you."

    scene mikugirly14
    with dissolve

    mi "Chika? Jealous of me? You kiddin’?"
    mi "She’s like...superstar pretty. And I’m just some weirdo walkin’ around in clothes clearly made for someone else."
    mi "She’d probably laugh me outta the store before gettin’ jealous about something like that."
    s "I think you’re gravely misunderstanding how cute you are, Miku."
    mi "And I think you’re just gravely...wrong. But if it makes ya feel better, we can go somewhere else."

    scene mikugirly15
    with dissolve

    mi "After that, though...we’re gettin’ ice cream whether ya like it or not."
    s "Do I...seem like the type of person who is anti-ice cream?"
    mi "You seem a little anti-everything, Sensei. But if we’re gonna be goin’ out on dates, you’re gonna be buyin’ me ice cream. Those are just the rules."
    s "If that is what must be done..."

    scene black
    with dissolve2

    if bonus == True:
        "Despite being far more comfortable with the idea of {i}dating{/i} than I assumed she’d be, Miku still can’t seem to let go of the idea that she just doesn’t belong in feminine clothing."
        "And, as excited as I am to get her out of said clothing, I do wish she’d maybe try and look at herself a little harder."
        "I guess feeling a little discomfort is to be expected though when you’ve finally got the opportunity to move around in someone else’s skin."
        "She just needs to grow into it."
        "Don’t share that thought with her, though. She’ll think it’s a shot at her breasts."
        "Or...lack thereof, I suppose."
        "Either way, the two of us walk through the mall together, mostly ignoring the fact that Miku is wearing a dress, and wind up at another familiar store."

    "........."
    "......"
    "..."

    scene mikugirly16
    with dissolve2

    mi "What do you think, Sensei? Are high waisted shorts a little too girly, too? Should I try and get somethin’ a little...lower-waisted? Or would that just be called “normal?”"
    mi "This is exactly why I hate shoppin’ for stuff. I’ve got no idea how any of this fashion mumbo-jumbo works."
    s "Why does it matter if they’re girly or not? Who cares?"
    s "No one is expecting you to keep up the same appearance forever and I have no idea why you’re so dead set on it."

    scene mikugirly17
    with dissolve

    mi "I don’t wanna hear that from somebody who’s been wearing the same heckin’ blazer for as long as I’ve known him."
    s "I’m only wearing this because it reminds me of the first time we kissed."

    if bonus == True:
        mi "Ya think I’m actually gonna fall for that? You’re just smooth talkin’ me cause ya think it’ll get me to put out in the dressing room. I know your games, Sensei."
        s "Makoto should have never told you anything. That line would have worked out better if you didn’t know I was routinely having sex with your best friend."
    else:
        mi "Ya think I’m actually gonna fall for that?"

    scene mikugirly18
    with dissolve

    mi "What about this one? Is {i}this{/i} one too girly?"
    s "..."

    "Wow. I guess Miku really {i}is{/i} unfazed by the whole thing between Makoto and me, then."
    "I...don’t know how I feel about that."
    "But I guess she does hang out with Kirin a fair bit, so maybe she’s just been negatively influenced in some way."
    "If you can even call the acceptance of relationships existing outside of your own personal bubble “negative” to begin with."
    "Which you can’t, because that’s just how life works."
    "But it would still be nice for her to get a {i}little{/i} bit jealous."

    scene black
    with dissolve2

    mi "Okay...I..."
    mi "I think I’ve got somethin’."
    mi "Yeah...Yeah, this’ll work."
    s "Need me to come in there with you?"
    mi "I know how to dress myself, ya friggin’ horn dog! Just wait out here and I’ll be done in a sec!"

    "Maybe one day..."
    "........."
    "......"
    "..."

    scene mikugirly19
    with dissolve2

    mi "..."
    s "..."
    mi "Good? Bad? What’s the verdict?"
    s "You look nice. I think I prefer the dress, though."
    mi "I like the dress too, but...I just ain’t ready yet, Sensei. Stuff like this is what I’m more comfortable in."
    mi "I’m fine with tryin’ to go a little more outside of my comfort zone, but...I’ve gotta take baby steps."
    mi "Ain’t always right to expect yourself on the starting roster if it’s your rookie season, ya know?"
    s "Not really, but I’ll trust your judgement."
    s "What you wear or the way you choose to style your hair doesn’t really make any difference to me. So as long as you’re happy, I’m fine with it."

    scene mikugirly20
    with dissolve

    mi "Guess it’s settled, then! Summer Miku’s makin’ her debut appearance before summer even begins!"
    mi "She’s also about to actually spend money on clothes for the first time in forever! So that’s a big step in...some sorta direction as well! Thanks for the help, Sensei!"
    s "What help? All I did was stand here and say you look cute a few times."

    scene mikugirly21
    with dissolve

    mi "Exactly! That was all ya needed to do."
    mi "Sometimes, girls just need moral support. We say a bunch of stuff that’s been squirmin’ around our minds cause we want ya to disagree with us."
    mi "You not doin' that means you passed the test!"
    s "Test?"

    scene mikugirly22
    with dissolve

    mi "The test to prove that I actually {i}do{/i} like ya after all!"
    mi "Sorry Makoto, but Miku Maruyama ain’t backin’ down any time soon!"

    scene black
    with dissolve2

    "Miku goes back into the dressing room to gather the dress her {s}best friend{/s} rival bought for her and decides that she’s just going to keep wearing her {i}new{/i} new outfit for the rest of the “date.”"
    "While we’re waiting in line to pay, it becomes increasingly apparent that mostly all of her nerves have departed with the addition of new clothing or, to harken back to an earlier metaphor-"
    "A different set of skin."
    "We leave the store in a hurry as Miku returns to her normal self and, within a matter of minutes, she has the {i}other{/i} thing she came here for as well..."
    "........."
    "......"
    "..."

    scene mikugirly23
    with dissolve2

    mi "Here! I went ahead and got you vanilla since you seem so boring and normal all the time."
    s "That’s a very offensive thing to say to someone who just bought you ice cream."

    scene mikugirly24
    with dissolve

    mi "I’m obviously just kiddin’, Sensei. I don’t think you’re normal at all."

    if bonus == True:
        mi "Ain’t nothin’ even remotely normal about gettin’ locked inside of a love triangle with two students. Let alone ones as young as-"
        s "Yes, thank you for acknowledging how inappropriate and abnormal our situation is. I would never have recognized it otherwise and I thank you for setting me down the right path."
        mi "Well, wherever that path is headed, I hope I can walk it with ya."
        mi "I might not be as smart or feminine as the other girls, but I’ve got tons of energy and I can’t think of anybody I’d rather spend it on than you."
        mi "Now eat your friggin’ ice cream before it starts to melt!"
        mi "We’ve got lots more hangin’ out to do!"
    else:
        s "Are you bullying me right now?"
        mi "Gimme all your lunch money, punk!"
        s "But I just bought you ice cream D="

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ miku_love += 3
    $ mikuspecial50 = True
    stop music fadeout 20.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm50

label mikudorm50:
...
```

## Code that triggers this event
File: \game\MikuEvents.rpy
Code:
```python
...
label callmikuafternoon:
    if mikublock == True:
        "I should probably leave Miku alone for now..."
        jump callafternoon
    if chapthreeactive == True:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    if christmas7 == False:
        play sound "phonebeep.wav"

        "I tap on Miku's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer. I guess she's busy right now."

        jump callafternoon
    if miku_love >= 50 and christmastwo20 == True and mikudorm45p2 == True and mikuspecial50 == False:
        jump mikuspecial50
...
```