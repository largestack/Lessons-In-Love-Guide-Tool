# The Girl with the Dragon Tattoo (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 5

* Event [Nonetheless, I'm Here](./bathhouse1.md) (Io) is completed)



## Next events

* [Io: Unnamed Wooden Robots](./iodorm5.md)

## Event properties

* Id: bathhouse5
* Group: Io
* Triggered by label: bathhouse
* Triggered by branch label: bathhouse
* Triggered by path: bathhouse->bathhouse5

## Official wiki page

[The Girl with the Dragon Tattoo](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bathhouse5&go=Go) for more details.

## Event code

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse5:
    scene ioyuki1
    with dissolve
    play music "normalday.mp3"

    "I show up at the bathhouse to find Io happily humming to herself and scrubbing away at the floor with a brush basically the same size as her."
    "There’s no one else around at the moment (That I can see, at least) and the volume from some sports broadcast is turned up loud enough that she doesn’t hear me enter."
    "It looks like she’s in a good mood, though."
    "I never really know what I’m going to be getting into when I go see her, but at least I’ve been given a sign of good things to come in that childish smile of hers."
    "Probably. "
    "To be fair, I’m half-expecting her to make everything awkward and uncomfortable the second our conversation starts."
    "She’s quite good at that, if I’ve learned anything about her by now."
    "Which I think I have."
    "Again, probably."

    i "So is staring at [high_school] girls a hobby of yours or something?"
    i "This is the second time I’ve caught you just looking at me and not saying anything."
    s "I should have known you saw me walk in. The volume of the TV deceived me into thinking you somehow didn’t."

    scene ioyuki6
    with dissolve

    i "Of course I saw you. You’re impossible to miss."
    i "Do you have any idea how many people of your size come in here? Like, none."
    i "Well, obviously at least one. But you get what I’m saying."
    s "Yes, I am tall. Thank you for noticing."
    i "So, here to hang out with me? Or are you actually going to use the bath this time?"
    i "If it’s the latter, you’re going to have to wait a little while. I’ve got someone in the men’s section right now."
    s "I mean, I’m not {i}opposed{/i} to sharing, but I kind of just came here for you anyway."
    i "Well good, because the girl in there doesn’t really like people intruding on her private time."

    if bonus == True:
        s "Now that I have confirmed it is a woman, I would like to reinforce that I {i}really{/i} do not mind sharing."
    else:
        s "What if I like...wore a blindfold and stayed really far away or something? I'd have no intention of peeking, but this woman sounds safer than the ones I normally associate with."

    scene ioyuki3
    with dissolve

    i "Sensei, I literally {i}just{/i} told you she likes being left alone."

    if bonus == True:
        i "Just because I like you and I’ve seen your penis doesn’t mean I’ll let you walk all over me."
        s "Then you’re already far too advanced for me to comprehend. That combination normally works wonders."
        i "You know, I’m glad that you’re starting to open up to me the way I open up to you...but lengthy conversations about your sexcapades are not really a thing I’m interested in."
        s "Then what {i}are{/i} you interested in? Besides scrubbing the floors of a bathhouse, I mean."
    else:
        s "I don't like how hurting my feelings is becoming your new hobby."

    scene ioyuki4
    with dissolve

    i "This isn’t a hobby. I do this to make money and help my aunt."
    i "My real hobbies are stuff like...baseball and...camping."
    i "Actually, I’ve got quite a few hobbies now that I think of it."
    i "I also like hiking...and building stuff...and those cool serial killer documentaries they have on Netflix."
    s "And not a single “girly” thing to be found."

    scene ioyuki5
    with dissolve

    i "Uhh...isn’t that a little sexist?"
    i "You’re not gonna make fun of me for not being into the same sort of stuff Uta is into, are you?"
    s "Oh, not at all. If anything, your interests are easier for me to understand than hers. "
    s "It’s actually kind of refreshing seeing someone who’s into such...normal things."
    i "Putting it that way just makes me sound boring..."
    i "Where are you trying to go with this?"
    s "No clue. "
    s "How’d you get into all of that, though?"

    scene ioyuki6
    with dissolve

    i "It’s just what I’m into, you know? There doesn’t have to be some long backstory about why I like baseball. I just...like baseball."
    i "It’s that simple."
    s "Fair enough. I was just opening up a window for you to talk more so I don’t feel pressured to think up a conversation topic."

    scene ioyuki5
    with dissolve

    i "It’s been five minutes and you’re already struggling with that? You’re even worse than me, Sensei."
    s "True, but at least I try."

    scene ioyuki7
    with dissolve

    i "Heheh~ True."
    i "At least you try."
    fv "Io! Can you spot me some of that conditioner I like?"

    scene ioyuki8
    with dissolve

    yu "You know, the one in the black bottle that smells like-"

    scene ioyuki9
    with dissolve

    yu "Oh."
    yu "What are you doing here?"
    s "I was about to ask you the same question."
    i "We’re out of the one you like but we should have more by Monday. "
    i "Want me to get my personal bottle from upstairs for you? It’s basically the same thing."

    scene ioyuki10
    with dissolve

    yu "Nah. I’ll survive without it. No need to go out of your way for me."
    i "You sure? I don’t mind if it’s for you."
    yu "Yeah, I’m good. No worries."
    s "I take it you two are familiar with one another?"

    scene ioyuki11
    with dissolve

    i "This is the girl I was talking about before- the one who likes being left alone."
    i "But I take it you two...know each other in some way?"

    if bonus == True:
        yu "Yeah. He’s boning my daughter."
    else:
        yu "Yeah. He hugged my daughter."

    scene ioyuki12
    with dissolve

    i "Uhh...come again?"

    if bonus == True:
        s "Okay, hold on a second. I am not {i}boning your daughter.{/i} She’s just a student in my class and I’m helping her find a job."

        "I would absolutely bone her if given the opportunity, though."
        "But I’d bone pretty much anyone if given the opportunity and-"
        "This is not a thing I should be thinking right now."
    else:
        s "And I'd do it again, too."

    i "Wait wait wait wait wait. Yuki’s daughter is in our class?"

    scene ioyuki13
    with dissolve

    yu "So I hear."
    yu "Smartass lookin’ girl. Probably wearin’ that same old long-ass skirt I used to wear when I was in[school]."
    i "Long skirt..."
    i "Wait, Yumi?"
    i "Holy shit, how did I not realize this?"
    yu "Probably better off not tellin’ her we’re close. She’ll just get pissed off and threaten to beat your ass or somethin’."
    s "Yup, definitely sounds like Yumi."

    scene ioyuki14
    with dissolve

    yu "Yeah. I’m sure you know all about her, don’t you?"
    s "As her teacher, not her lover."
    i "I’m gonna stop you two right there since I feel like this is skirting into uneasy territory."

    scene ioyuki15
    with dissolve

    yu "Hah...Yeah."
    yu "No use talkin’ about that shit right now. "
    yu "Still weird findin’ out you’re in the same class as my kid, though. "
    yu "Knew you switched[school]s but didn’t think a coincidence like that was gonna pop up."
    i "I’m more interested in whatever coincidence brought {i}you two{/i} together."
    i "It’s like a weird little family reunion we’ve got going on right now. Just none of us are related and one of us is naked."
    yu "Not naked...Got a towel on."
    s "We bumped into each other at a ramen shop one day."
    s "And then again at...that same ramen shop."
    yu "I don’t go many places, alright? Give me a fuckin' break."
    i "Oh, okay. Okay. So you’re not really {i}friends{/i}, just acquaintances."
    s "Something like that, sure."

    scene ioyuki16
    with dissolve

    i "Which means you probably haven’t seen {i}that{/i} yet."
    yu "That?"
    yu "You have any idea what she’s talkin’ about?"
    s "How would I know? You’re the one with {i}that{/i}."
    yu "I don’t even know what {i}that{/i} is. How am I supposed to know I actually have it?"

    scene ioyuki17
    with dissolve

    i "Yuki! Show him your tattoo!"
    yu "Ooooooh, {i}that{/i}."
    s "Again, Yuki and I are hardly acquainted and there’s no way she’d-"
    yu "Sure."
    yu "Long as I can do it in the men’s locker room and not out here in the co-ed one."
    yu "Not really a thing I want most people seeing."
    s "Wait, really?"

    scene ioyuki18
    with dissolve

    i "Yay!"
    yu "What’s wrong, man?"
    yu "You ain’t the type to get all nervous and shit when a girl takes her clothes off, are you?"

    if bonus == True:
        s "Quite the opposite, actually. "
        yu "That’s kind of just as bad."
        yu "Just don’t touch me and we’re good."
        yu "It’s on my back so it’s not like I’m showin’ you my tits or anything. Just totally normal shit."
        i "Woo! Let’s get you two into the locker room! It's game time!"
    else:
        s "I am. Girls intimidate me and often make me feel very small."

    scene black
    with dissolve2

    "Io locks the entrance to the bathhouse so no one can come in and then immediately shows us to the men’s locker room."
    "And when I say “shows us to” I mean she gets behind me and pushes me inside."

    if bonus == True:
        "I’m not sure why. I would have gladly walked in on my own."
        "Even if it’s just from behind, the chance to see Yumi’s mom without clothes on is an opportunity I would never miss out on."

    "………"
    "……"
    "…"

    scene ioyuki19
    with dissolve

    yu "Remember, touch me and I’ll cut your fucking hands off."
    s "Deal. "
    i "That’s right. Only {i}I’m{/i} allowed to touch Yuki."
    yu "Io ain’t allowed to touch me either."
    i "I’m going to anyway. Watch."
    yu "Let’s just get this shit over with. "
    yu "It ain’t even that impressive. "

    scene black
    with dissolve

    "Yuki turns around and begins to slowly lower her towel."
    "It isn’t until it gets halfway down her back that I {i}really{/i} notice how pale she is."
    "Paired with the fluorescent light, she’s almost like a ghost."
    "………"
    "……"
    "…"

    scene ioyuki20
    with dissolve

    "Her towel stops just as it reaches her ass (An anticlimactic finale, I know) and I’m suddenly faced with a Yakuza-esque tattoo taking up her entire back."
    "I’m sure this is part of the reason why she takes up this side to herself whenever she’s here."
    "There aren't a lot of Japanese people who'd be willing to...overlook something like this."
    "But I-"

    s "I think it’s-"
    i "SO COOL!"

    scene ioyuki21
    with dissolve

    "Io appears before I’m able to finish my train of thought and places her hand directly on Yuki’s back."
    "I’ve gotta say, for someone who doesn’t like girls, she seems to be handling her, of all people, rather well."
    "But I guess Yuki isn’t exactly the most feminine person around."

    yu "Hah..."
    yu "You’re lucky I like you, Io."

    scene ioyuki22
    with dissolve

    i "Sensei! Isn’t this like, the coolest thing you’ve ever seen?"
    i "The first time I saw it was actually on the camera and I was so impressed that I ran out to meet her in the bath."
    yu "Fuckin’ horrible first impression."
    i "Oh, I was the absolute worst. I know."
    i "But it was so awesome that I couldn’t stay away."
    yu "Well I’d be more than happy to give it to ya if that were possible."
    yu "Shit’s a fuckin curse, if ya ask me."
    i "Sensei, do you think I’d look good with a tattoo like that?"

    if bonus == True:
        s "I’d have to see you without a shirt on first to figure that out."
        yu "Hey. Don’t forget I’m still here."
        yu "If you two are gonna fuck, go do it on the girl’s side. I still need to take a bath and I don't wanna watch that shit."
        i "I think I want one but like, not as big as Yuki’s."
        i "It doesn’t have to be on my back, either. Anywhere would be fine."
        i "Oh! We should get them together!"
        i "Sensei, let’s go get tattoos!"
        s "Uhh...Yeah, I think I’m good."
        yu "Aight, time to beat it, you two. Still dry as fuck and not feelin' it."
        yu "Kinda ruinin’ my me-time right now."
        i "Fine, fine. We’re leaving."
    else:
        s "No, your body is a temple and you should not disgrace it with such atrocious art."
        yu "Dude wtf"

    scene ioyuki23
    with dissolve

    i "Thanks for showing Sensei your tattoo, Yuki!"

    if bonus == True:
        i "I know how long it’s been since you’ve taken your clothes off in front of a man and-"
        yu "Get...out..."
        i "Yes ma’am!"
    else:
        yu "Wtf"

    scene black
    with dissolve2

    "Io quickly scurries out of the room, picking up her floor brush as she does so."
    "I follow behind her and the two of us quickly return to our earlier conversation once we’re in the lobby again."
    "She goes back to talking about her hobbies and how much she apparently likes body art and-"
    "After another thirty minutes of that, Yuki rejoins us."

    scene ioyuki24
    with dissolve

    yu "You’re still here? Don’t you have like, shit to do or whatever?"
    yu "Yumi have a job yet?"
    s "No shit to do and I’m not sure what Yumi is up to right now."
    yu "Well that makes two of us then."

    scene ioyuki25
    with dissolve

    yu "Uhh..."
    yu "Listen."
    yu "I know this will probably sound fucking dumb or whatever but like..."
    yu "If you’d want to meet up at the ramen shop again sometime and talk about her...or other shit, that would be cool."
    yu "I kinda still owe you for payin’ for me the first time...so it would be on me."
    yu "Just don't buy anything fuckin' expensive. I'm not made of cash."

    "Yuki proceeds to tell me her phone number and I give her mine in return."
    "We don’t make any concrete plans or anything so I guess I’ll just...call her whenever I call her."
    "I have to say, this is definitely not how I envisioned myself acquiring her number."
    "Hell, I didn’t envision that at all, to be honest."
    "But it’s a thing I have now, so I might as well get to know her."

    $ yukinumber = True

    "{i}Congratulations! You now have Yuki’s number!{/i}"

    scene ioyuki26
    with dissolve

    "After entering my number into her phone, Yuki nods at Io and heads outside..."

    i "..."
    i "So...Yuki, huh?"
    i "You ever gonna call her?"
    s "Maybe."
    s "You don't have a problem with that, do you?"
    i "Why would I have a problem? She gave it to you so you can do whatever you want with it."
    i "Call her, don’t call her. Not up to me."
    i "She’s not...a bad person or anything. I like her a lot."
    i "So it would...only make sense if you liked her too."

    scene ioyuki27
    with dissolve

    i "Sorry. I’m probably being weird. Am I being weird?"
    i "Yeah, I’m definitely being weird."
    i "Let’s just go back to talking about normal stuff again."

    scene black
    with dissolve2

    "At her behest, Io and I return to standard banter and, before long, it’s time for her to go on break."
    "I offer to walk around the city with her for a little while to help kill time, but she adamantly refuses going out in the cold as she doesn’t want to get dressed."
    "I don’t blame her. Getting dressed is horrible."
    "Wearing pajamas out in public should be socially acceptable. It would solve so many problems."
    "But that has nothing to do with where I’m going now, which is-"
    "…"
    "Huh."
    "Where am I going again?"

    $ renpy.end_replay()
    $ io_love += 1
    $ bathhouse5 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label bathhouse10:
...
```

## Code that triggers this event

File: (install folder)\game\IoEvents.rpy

Code:
```python
...
label bathhouse:
    if io_love >= 0 and day247 == True and bathhouse1 == False:
        jump bathhouse1
    if io_love >= 5 and bathhouse1 == True and bathhouse5 == False:
        jump bathhouse5
...
```