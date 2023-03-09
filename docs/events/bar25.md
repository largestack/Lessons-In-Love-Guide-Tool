# Life is a Tomato
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar25&go=Go)



## Event preconditions
✅Sana love greater than or equal to 25

✅Event "[Sana: Nice Weather We're Having](./sanadorm20.md)" is completed (event=sanadorm20)

✅Event "[Maki: Beautiful Porn Salesman](./makidate1.md)" is completed (event=makidate1)



## Next events
* [Main: The Value of Sharing](./halloween1.md)
* [Sana: The Girl in the Black Dress](./sanadorm25.md)
* [Maki: Maki Miyamura's Mom-Mode Mission](./makidate5.md)

## Event properties
* ID: bar25
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label bar25:
    scene bartwofive1
    with fade
    play music "calmbar.mp3"

    "I decide to spend yet another night at the bar killing time with Sana."
    "Without me even having to ask, she grabs a beer from the cooler and slides it over to me with an uncharacteristic smile on her face."

    s "In a good mood tonight?"
    sa "Hm?"
    sa "Why do you ask?..."
    s "You seem a lot less nervous than usual."
    sa "Do I?"
    sa "I’m just...a little relieved that my mom isn’t around...That’s all."
    s "Ahh. Yeah, I can imagine it probably takes a load off of your mind knowing that she can’t show up and randomly embarrass you."

    scene bartwofive2
    with dissolve

    sa "You don’t get the half of it..."
    sa "It’s only been getting worse lately too..."
    s "Really? Did something happen?"

    scene bartwofive3
    with dissolve

    sa "Yes."
    s "...Explain?"
    sa "{i}You{/i} happened."
    s "Saying it with that sort of expression makes you seem more like Yumi and less like Sana."
    s "Give me back my favorite bartender."

    scene bartwofive2
    with dissolve

    sa "I’m only kidding..."
    sa "Though...it is true that my mom has been {i}really{/i} annoying ever since you started coming around..."
    sa "She keeps asking me questions about you and...I have no idea how to answer even half of them..."
    s "Well, what kind of questions? Maybe I can help?"

    scene bartwofive4
    with dissolve

    sa "Huh?...Well...it’s not like I’ve...kept track of them or anything..."
    sa "They’re mostly just random things like what kind of food you like or...what you do for fun."

    scene bartwofive2
    with dissolve

    sa "I think...she thinks we might be closer than we actually are..."
    s "Well, aren’t we?"
    s "I like to think that we’ve at least sort of transcended the teacher/student thing by now, right?"
    sa "Well...I don’t think I’ve ever had another teacher who routinely shows up in my room...so I guess so."
    sa "But I still don’t know much about you either..."

    "To be fair, even {i}I{/i} don’t know much about myself."
    "This version of me, at least."
    "It’s not like I can just sit down with Ami and ask something like, “Hey, what was I into a couple years ago? How different did I act?”"
    "It’s a confusing situation. "
    "And it definitely doesn’t help that there isn’t really anything I find appealing other than..."
    "Well, having conversations with [younger_girls] in the middle of the night."
    "But hey, at least it feels a little more normal talking to one in a bar rather than a porn shop..."

    s "Well how about this-"
    s "Do {i}you{/i} have any questions for me, Sana?"

    scene bartwofive4
    with dissolve

    sa "Are you...going to answer them?"
    s "I believe that was implied, yes."
    sa "And...are you going to ask me any?"
    s "...Do you want me to?"

    scene bartwofive1
    with dissolve

    sa "Sure...We can make it a sort of...game. Or something..."

    scene bartwofive5
    with dissolve

    sa "Like...we could take turns getting to know more about each other..."
    sa "Something like that might be easier for me since I can’t really...steer conversations myself."
    maki "What’s all this about steering conversations?"

    scene bartwofive6
    with dissolve

    s "..."
    maki "...?"
    s "Maki?"
    maki "Yes! That is me. Maki."
    s "What are you doing here?"
    maki "Drinking, I hope."

    scene bartwofive7
    with dissolve

    maki "Is your mom around tonight, Sana?"
    sa "Huh?...Oh, umm...No. She had plans with a friend tonight."
    maki "And I wasn’t invited? Damn that tramp."

    scene bartwofive2
    with dissolve

    s "Do you know who that woman is?"
    maki "Maki! Do I need to say it even louder?"
    sa "That’s umm...the..."

    scene bartwofive5
    with dissolve

    sa "That’s the...porn-lady..."

    scene bartwofive8
    with fade

    "Maki walks up to the bar and takes her place on the stool directly beside me."
    "What sort of woman gets dressed up like that to come to the bar all by herself?"
    "She realizes this place doesn't ever have any customers, right?"

    maki "Porn-lady isn't really the best nickname I could have asked for. But I guess I can take it."

    if bonus == True:
        scene bartwofive9
        with dissolve

        maki "Heh...Take it."
        maki "Like a dick."
        maki "Get it?"
        s "Yes, Maki. I get it."

    scene bartwofive10
    with dissolve

    maki "Were you two in the middle of something? I could have sworn I overheard a chat about the question-game."
    sa "Y-Yes...We were going to do...something like that..."
    sa "But I don’t think we were going to ask the sort of questions you’d be interested in..."
    sa "At least I hope not..."
    maki "Hmm okay, okay. Well don’t let me interrupt you. "
    maki "Could I bother you for a glass of wine, though?"
    sa "Oh...umm...Sure. "
    sa "I’ll be right back..."

    scene bartwofive11
    with dissolve

    "Sana walks to the other end of the counter and opens a brand new bottle of red wine, pouring it carefully into a glass."

    maki "Another student of yours?"
    s "Another student of mine."

    if bonus == True:
        maki "Do you have any girls who {i}don’t{/i} work in businesses not suited for their age group?"
        s "A few. None as impressive as a porn shop, though."
        maki "I think that’s the first time anyone’s referred to my shop as impressive."
        maki "Thank you for your kind words. I’ll knock 500 yen off of your next fleshlight in order to thank you for them."
    else:
        maki "Radical."
        maki "Hey, want to go jet-skiing sometime?"

    s "You truly know the way to a man’s heart, don’t you?"

    scene bartwofive12
    with dissolve

    "Sana comes back a minute or two later and places a glass in front of Maki, who immediately picks it up and begins sipping away."

    sa "I...take it you two know each other?..."
    maki "Know each other? We’re practically inseparable."
    s "We’ve hung out a couple times."
    sa "That’s...worrying."
    maki "What’s truly worrying is your mother, dear."
    maki "Is she okay?"

    scene bartwofive13
    with dissolve

    sa "I...think so? Why do you ask?"
    maki "Well, because she was one of my regular customers and I haven’t been seeing her much at all lately."
    s "Sara is a regular at the porn shop?"

    scene bartwofive14
    with dissolve

    if bonus == True:
        maki "Oh, please. If I had a dollar for every dildo I’ve sold that woman, I’d have enough to open two more stores."
        s "I’d hope that you’re profiting at least a dollar from every sex toy you sell."
        s "You might need to raise your prices if that’s not the case."
    else:
        maki "She never buys anything. She just likes to run in circles around the store screaming about how her love life is falling apart."

    sa "Umm...can we...talk about something else?..."
    sa "I don’t really..."

    scene bartwofive15
    with dissolve

    if bonus == True:
        maki "Oh gosh. Of course! I forgot how innocent and untainted you are. So different from your perverted mother."
    else:
        maki "The only other thing I have any knowledge about is the North American Free Trade Agreement."

    s "This is probably why you weren’t invited out tonight, Maki."

    scene bartwofive16
    with dissolve

    maki "Rude!"
    sa "Umm...to get things back on track...maybe we should do the question thing...another time?"

    if bonus == True:
        s "I think we’re still fine as long as Maki agrees to not make things perverted."
        maki "You overestimate me, good sir. Of course I'm going to make things perverted."
    else:
        s "I think we're fine as long as Maki promises to not bring up NAFTA."
        maki "You understimate my power."

    scene bartwofive17
    with dissolve

    maki "But go ahead and play your game, dear. I have a daughter, too, so I know when I need to take the back seat."
    sa "You...have a daughter?..."
    s "That’s Makoto’s mom."
    sa "…"
    maki "…"
    s "…"

    scene bartwofive18
    with hpunch

    sa "What?!"
    sa "Like...class president Makoto?"
    maki "Yes, yes. Please tell me more about how impressive my daughter is. I live for it."

    scene bartwofive19
    with dissolve

    sa "Well...I guess that explains why you know her a little better then..."
    sa "For a second, I was worried you were also a...regular customer..."
    maki "What are you talking about? Of course he’s-"
    s "Okay, Sana. Question game starts now."
    s "Ask me whatever you like."

    scene bartwofive20
    with dissolve

    maki "Mm!"
    sa "Um...uhh...it’s kind of hard when you put me on the spot like that..."
    maki "Hard like a-"
    s "Maki."

    scene bartwofive21
    with dissolve

    maki "MMM!!!!"
    sa "Umm...okay...how about this..."
    sa "If you had to...describe your outlook on life with...a vegetable...what vegetable would it be?"
    s "...That’s your question?"
    sa "Yeah. That’s the question I chose and you need to answer it or...I’ll kick you out of the bar."
    s "But then you’d be alone with the porn lady."

    scene bartwofive22
    with dissolve

    maki "I don’t think your mother would like that very much. I'm a bad influence."
    sa "Answer the question...or else."
    s "Wow, Sana. Maybe you {i}are{/i} improving your social skills? It’s not like you to put your foot down. Especially in front of other people."
    sa "Vegetable. Tell me."
    s "Maybe...a tomato?"

    scene bartwofive23
    with dissolve

    sa "Wait...isn’t the tomato a fruit?"
    s "Oh, don’t even start. That’s a whole other game."
    maki "Why a tomato?"
    s "Probably because...On the outside, it pretty much always looks fine."
    s "But sometimes, you’ll bite into one and it'll be outright rotten."
    s "That’s kind of how I look at life, I guess."
    s "Approach everything normally, but don’t be surprised if things turn out horrible all of a sudden."
    sa "…"
    maki "…"
    s "…"

    if bonus == True:
        maki "You need to get laid."
    else:
        maki "You need a hug."

    scene bartwofive24
    with dissolve

    sa "When you put it that way...I kind of agree..."

    if bonus == True:
        sa "Not about the...l-laid part, though..."
    else:
        sa "Not about the...hug, though..."
        sa "Hugs are immoral..."

    sa "There’s not really any way to tell when things will go bad..."
    sa "Which is...one of the reasons I don’t like tomatoes."
    s "Is one of the other reasons that they’re a key ingredient in-"
    sa "Don’t...even think about it, Sensei..."
    maki "Don’t think about what? Am I missing out on an inside joke here?"
    s "Didn’t you come here to drink?"
    s "What happened to taking the back seat and letting us have our conversation?"
    s "This could be a breakthrough moment for Sana."

    scene bartwofive25
    with dissolve

    if bonus == True:
        maki "Good luck breaking through {i}anything{/i} with that attitude."
        s "…"
        sa "Um...what does she mean by...breaking through {i}anything{/i}?..."
        sa "Did I do something wrong?..."
        maki "Yes. Tell her, Sensei. Tell her all about what you want to break through."
        s "It’s just some...adult humor. Don’t pay any mind to her."
    else:
        maki "That girl couldn't break her way out of a paper bag. Look at those weak, little arms of hers."
        s "Leave her alone. She is a health inspector."
        sa "I am...confused about the relevance of my occupation in regard to-"
        s "It’s just some off brand humor. Don't worry about it, Sana."

    scene bartwofive26
    with dissolve

    sa "Well...no matter what type of humor it is...I’m glad we have the same vegetable answer..."
    s "Have you adopted the way of the tomato as well, Sana?"
    sa "Um...I guess so?"
    sa "I wouldn’t really call it the way of the tomato, though...that sounds kind of silly."
    s "Yeah. We’ll think up a better name for it in the future."

    scene bartwofive27
    with dissolve

    sa "Did you...maybe want to ask me something now...Sensei?"
    sa "It’s not much of a game if we just...stop after the vegetable..."

    "Hmm..."
    "A question for Sana."
    "Is there anything I’ve been wanting to ask her? "
    "It could be something as simple as just asking her what kind of music she likes."
    "But I feel like now might be a good opportunity to pry a little further into her past."
    "Sana’s never really elaborated on her personal life or any problems but..."
    "Well, Maki is right next to us and serving as a sort of ‘block’ right now."
    "So maybe sticking with a simple question would be good for the time being?"
    "I can always ask her more personal things some other time."

    s "How about this..."
    s "If you were magically granted the ability to play any instrument what would it be?"

    if bonus == True:
        maki "Skin flute."
    else:
        maki "Horseradish."

    s "Maki."

    scene bartwofive28
    with dissolve

    sa "I’m kind of...relieved that you chose something like that and not anything weird..."
    s "No weird questions until at least Round-3. That’s the rule."
    sa "Well...I don’t understand what rule you’re talking about...but I think it would be fun to play the drums."
    s "The drums? Really? You seem like more of a...keyboard player than a drummer."

    scene bartwofive29
    with dissolve

    sa "Heheh...I can see why you’d say that..."
    sa "But who we are on the outside doesn’t always match who we are on the inside..."
    sa "Maybe there’s a...drummer inside of me that’s just dying to come out some day?"

    scene bartwofive27
    with dissolve

    sa "Obviously...something like that won’t ever happen..."
    sa "But if magic were involved and...I could make the choice myself..."
    sa "Definitely drums..."

    scene bartwofive30
    with dissolve

    sa "I’d also look super awesome and...badass behind a drum set...Right, Sensei?"
    s "…"
    sa "…"
    s "…"

    scene bartwofive31
    with dissolve

    sa "Why aren’t you saying anything?..."

    scene black
    with dissolve2

    "The conversation carries on for a full hour after that."
    "We go back and forth asking each other seemingly pointless things and slowly but surely chipping away at what makes each of us tick."
    "One thing I realize is that almost every single one of Sana’s answers is something I don’t expect to hear."
    "It, once again, reminds me that there really might be a lot more to her than she lets on."
    "And hiding somewhere deep within that tiny frame of hers-"
    "Lies a super awesome, badass drummer just waiting to escape."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar25 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar30:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
...
```