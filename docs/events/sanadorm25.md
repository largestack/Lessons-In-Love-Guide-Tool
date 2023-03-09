# The Girl in the Black Dress
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm25&go=Go)



## Event preconditions
✅Sana love greater than or equal to 25

✅Event "[Sana: Life is a Tomato](./bar25.md)" is completed (event=bar25)

✅Event "[Main: See You in the Morning](./beachvacation16.md)" is completed (event=beachvacation16)



## Next events
* [Sana: Self-Medication](./bar30.md)

## Event properties
* ID: sanadorm25
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm25:
    play sound "knock.mp3"

    s "Sana, are you up to anything right now?"
    sa "Sensei? Just...a minute, please!"

    "I can hear Sana yell from behind her door."
    "Well, it’s not exactly a yell. This {i}is{/i} still Sana we're talking about."
    "It’s more like the noise a mouse makes when you turn on the lights in the middle of the night and cause it to go scurrying off to the other side of the room."
    "Just...somehow even less intimidating."

    scene girlinblackredux1
    with fade
    play sound "dooropen.mp3"

    sa "Um...G...Good evening..."
    s "Hey. What's going on? You didn't have to come out of your room."

    scene girlinblackredux2
    with dissolve

    sa "Well...I was actually...on my way out already..."
    s "Am I interrupting something?"
    sa "No, I just...thought I’d go for a walk tonight."
    s "Well, I graciously accept your invitation for me to come along."

    scene girlinblackredux3
    with dissolve

    sa "I...guess there's no stopping you now..."
    sa "Just so you know, though...I don’t really have anywhere in mind..."
    sa "So we might just...walk around in circles...or something..."
    s "Wow. You really know how to have a good time, don’t you?"
    sa "I do my best..."

    scene girlinblackredux4
    with dissolve

    sa "I could always...leave you behind...you know?"
    sa "Being seen with someone like you might...cramp my style..."
    s "Who taught you to speak like this? Because it sure as Hell wasn’t me."

    scene girlinblackredux1
    with dissolve

    sa "I think Rin might be rubbing off on me..."
    sa "She’s also been...helping me get better at talking to people in her spare time..."

    "Well...that definitely makes a little more sense than Sana just suddenly thinking she’s better than me."
    "Rin is essentially Kumon-mi's resident expert at playful banter, so Sana’s in good hands."
    "I just hope she doesn’t become a little...{i}too{/i} much like Rin because I'm not quite sure how I'd handle her calling me {i}homie.{/i}"

    sa "So...are you ready to go or...did you want to stop somewhere first?.."
    s "Where would I even stop? Does the dorm suddenly have a gift shop that no one's told me about or something?"
    sa "No, I...I don’t know..."
    sa "I'm just...trying to be polite..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "The two of us set off down the road and pass by several shops closing down for the night."
    "Sana doesn’t seem eager to stop at any of them...She literally just wants to walk. That's it."
    "Which is fine, I guess. I mean, I’m no stranger to going out without a gameplan in mind..."
    "But the fact that Sana wants to do something like this with me is an occurrence I didn’t think would be happening for quite a while."
    "Maybe that talk we had on the beach helped her get a little more comfortable with me after all?"
    "………"
    "……"
    "…"

    scene sanabench1
    with dissolve2
    play music "retrospect.mp3"

    sa "Okay...we’ll stop here for now."
    s "Finished with your weird, aimless walking plan?"
    sa "It’s...only weird if you make it weird..."
    sa "What’s wrong with two friends going out for a walk in the middle of the night?..."

    scene sanabench2
    with dissolve

    sa "I told you during vacation that I start getting a little...happier once the weather changes."
    sa "And tonight is the coldest it’s been in a while..."

    scene sanabench1
    with dissolve

    sa "Don’t you think so, Sensei?..."
    s "I mean...Sure, I guess. I haven’t really been paying much attention to the weather."
    s "I’m not dying from heat exhaustion, though. So that’s definitely a good sign."

    scene sanabench3
    with dissolve

    sa "Yeah...it’s kind of miraculous we’ve made it this far...isn’t it?"
    sa "Through Summer, I mean."
    sa "Every time it rolls around, I think to myself...Sana...you’re going to go out and...do things..."
    sa "But then I take one look at the forecast and change my mind for the next six months..."
    s "Does this mean you’re going to actually do things this winter?"
    sa "Maybe..."
    sa "Though...I’m not really sure what there is to do with my grand total of two friends..."
    s "How about karaoke?"

    scene sanabench4
    with dissolve

    sa "I’ve heard some rather...unpleasant stories about how Ayane acts during karaoke."

    "I’m suddenly stricken with a traumatic flashback involving Ayane and some song she sung in Spanish."
    "Maybe it’s best if Sana doesn’t go down that path after all?..."

    scene sanabench1
    with dissolve

    sa "I...wouldn’t be surprised if Rin was a good singer, though..."
    sa "I can’t really speak to how good I would be since I’ve never really...done something like that before, but..."
    sa "How about you, Sensei? Are you a good singer?"
    s "Is this you inviting me to Karaoke?"

    scene sanabench5
    with dissolve

    sa "As long as you can keep it a secret from Ayane."

    scene sanabench6
    with dissolve

    sa "Ah! That came out wrong!"
    sa "I didn’t mean it like that!"
    sa "I just meant...so we wouldn’t have to hear Despacito!"
    s "Calm down, I know what you meant."

    scene sanabench7
    with dissolve

    sa "Guh..."
    sa "I really need to be more careful..."
    sa "I feel like the more I learn to actually speak with you...the worse I get at saying the right thing..."
    sa "Is that supposed to happen?"
    s "I guess so. That sort of thing just comes with the territory."
    s "Ready for another lesson, Sana?"

    scene sanabench8
    with dissolve

    sa "You mean...right now?"
    sa "You normally only teach me speaking stuff at the bar..."
    s "Now is as good a time as any. Please take note of this extremely vital information."

    scene sanabench9
    with dissolve

    sa "Give it to me."

    scene sanabench6
    with dissolve

    sa "Wait! That came out wrong too!"
    sa "Just teach me whatever it was you wanted to teach me!"
    s "Right...well-"

    scene sanabench9
    with dissolve

    s "The more you talk, the more mistakes you’ll make."
    s "You’d think that learning how to speak publicly would put an end to things like that, but it's actually the opposite."
    s "One of the biggest downsides to becoming a good speaker is that your mistakes become more visible than ever."
    s "Once people start associating you with your linguistic skills, those same people will pounce on any slip-up just so they can feel better about themselves."
    s "So, if you think your problems are just going to go away once you get the basics down, you’ve got another thing coming."

    scene sanabench8
    with dissolve

    sa "That was a lot more detailed than a normal lesson..."
    sa "You didn’t even ask me to roleplay."
    s "To be fair, your roleplaying during that game you guys played over vacation left me a little intimidated."
    s "Which is strange because it was also one of the cutest things I’ve ever seen you do."

    scene sanabench3
    with dissolve

    sa "I...was hoping you’d never bring that up..."
    sa "I got so wrapped up in the game that I...didn’t even realize you were there..."

    scene sanabench1
    with dissolve

    sa "But thank you. For actually teaching me something today."
    sa "Even if your lesson was just...another cynical outlook on how people take advantage of others."
    s "Hey, at the end of the day, lessons like that are the ones that really matter."
    s "You never know when someone is going to just show up and ruin everything."
    sa "Yeah, yeah...You’re a cynic...I get it."
    s "…"
    s "I don’t like what Rin is doing to you."

    scene sanabench10
    with dissolve

    sa "Heheh...Even I’ll admit that it feels kind of weird being so casual with you..."
    sa "If I ever start calling you...homie, though..."
    sa "You can execute me."
    s "Thanks, Sana. I’ll remember that."

    scene sanabench8
    with dissolve

    sa "Wait..."
    sa "You won’t...actually execute me...will you, Sensei?"
    s "…"
    sa "Sensei?..."
    s "…"

    scene sanabench6
    with dissolve

    sa "Why aren’t you saying anything?!"

    stop music
    scene sanabench11

    sg3 "Perhaps he has forgotten how?"
    sa "…"
    s "…"

    play sound "static.mp3"
    scene sanabench12
    with flash
    stop sound

    sg3 "Oh, how pitiful it is to forget."
    sg3 "To let go of something you love."
    sg3 "Especially something as beautiful as speech itself."

    scene sanabench13
    with dissolve
    play music "stopwind.mp3"

    sg3 "I take it that the two of you know each other well?"

    "A mysterious girl appears before us spinning an umbrella around behind her back."
    "It hasn’t rained much since I’ve been reborn here, so I’m a bit curious as to why she’s carrying something like that around with her."

    sa "Umm...he’s my...teacher..."
    sg3 "A teacher? That’s wonderful."
    sg3 "It sounded like your lesson wasn’t going very well, though."
    sg3 "To teach requires participation on both ends."
    sg3 "So why has the man beside you suddenly gone quiet?"
    s "Can we help you with something?"

    scene sanabench12
    with dissolve

    sg3 "Ahh...So you {i}can{/i} speak after all..."
    sg3 "And here I was thinking that things were about to get interesting."
    sa "Interesting?...What...do you mean?..."

    play sound "static.mp3"
    scene sanabench14
    with flash
    stop sound

    sg3 "Oh?"
    sg3 "You want to know?"
    sa "Well...you just..."

    scene sanabench15
    with dissolve

    sg3 "Hahah...hahahahahah!!!"
    sg3 "The end of days approaches!"
    sg3 "Before long, little things like these talks...the looks you give each other...will be naught but memories."
    sg3 "And all of the time you two have spent will be wiped clean."
    sg3 "Like old ink being stripped from a dry-erase board."
    sg3 "The dawning of a new age is upon us."
    sg3 "But for what purpose?"
    sg3 "And why now?"

    scene sanabench12
    with dissolve

    sg3 "‘Tis not my place to say."
    sg3 "I'm just a messenger."
    sg3 "What I can tell you, though..."
    sg3 "Is that you are not prepared for what has yet to come."

    scene sanabench13
    with dissolve

    sg3 "Do you believe in {s}god{/s} {s}GOD{/s} {s}GoD{/s} God?"
    s "What does that have to do with anything?.."
    sg3 "It’s a simple question."
    sg3 "Surely you can answer it...can't you?"
    sg3 "Yes or no?"
    s "..."
    sg3 "Hmm...interesting."
    sg3 "Perhaps you'd rather answer something like this, then-"
    sg3 "What waits for you at the end of the world?"
    sg3 "Is it something wonderful?"
    sg3 "Or is it-"

    play sound "static.mp3"
    scene sanabench16
    with flash
    stop sound

    sg3 "Something sad?..."

    "Tears stream down the girl’s face and drop to the ground below her."
    "They mix with the sound of her umbrella as it cuts through the wind."
    "These are the only sounds we can hear."
    "Something is wrong."

    sa "Are you...okay?"

    scene sanabench17
    with dissolve

    sg3 "Oh..."
    sg3 "Oh no..."
    sg3 "You don’t know..."
    sg3 "How simply tragic..."

    "The girl locks eyes with me, ignoring Sana completely."

    sg3 "You pitiful...lost soul..."
    sg3 "How will you ever find your way home?"
    s "…"

    scene sanabench18
    with dissolve

    sg3 "It’s okay..."
    sg3 "You don’t have to say anything..."
    sg3 "You’ll reach for salvation soon enough..."
    sg3 "And when you do, I’ll be there to catch you as you tumble further and further from everything."
    sa "Sensei...what’s going on?..."
    s "I have no idea..."
    sg3 "Of course you don’t."
    sg3 "There’s no way you would."
    sg3 "Not yet at least."

    scene sanabench19
    with dissolve

    sg3 "…"
    s "…"
    sa "…"

    "She pauses for an uncomfortably long time."
    "Neither myself nor Sana find it in ourselves to speak out."

    sg3 "{i}You’ve seen God.{/i}"
    sg3 "I can see it in your eyes."
    sg3 "Oh, how envious I am..."
    sg3 "To think he’d grace {i}you{/i} with his presence..."
    sg3 "And yet will do naught but {i}speak{/i} with me."
    sa "Should we maybe...call someone?..."

    scene sanabench12
    with dissolve

    sg3 "There’s no need..."
    sg3 "I see I’ve already overstayed my welcome."
    sg3 "I suppose I’ll just go back to hiding now."

    scene sanabench13
    with dissolve

    sg3 "Farewell, Sensei."
    sg3 "May the path before you be lit and clear of callousness."
    sg3 "And, to the girl in the black dress-"
    sg3 "Please know that he is happy now."

    scene sanabench12
    with dissolve

    sg3 "Until we meet again..."

    scene sanabench20
    with dissolve

    "The girl turns around and skips away from us, twirling her umbrella the entire time..."

    scene sanabench21
    with fade

    sa "…"
    s "...Sana?"
    sa "I-"
    sa "What just...happened?"
    s "Why are you crying?..."
    sa "I saw her tears and I just..."
    sa "I..."
    sa "I don’t know..."

    scene sanabench22
    with dissolve

    sa "I’m..."
    sa "I’m...scared..."
    sa "The world’s not really going to end...is it?"
    s "Of course not. That was probably just some lunatic off of her medication."
    s "I wouldn’t think too much of it."
    sa "I don’t want to but..."
    sa "My heart is beating so quickly..."

    scene black
    with dissolve2

    "Sana and I remain on the bench for another twenty minutes or so while she composes herself."
    "I try to reach for her hand to calm her down but she swats me away and seems even more adamant about not being touched than normal."
    "Why was that girl able to make a huge impact on her by just spouting nonsense?..."
    "…"
    "And who was she talking about in the end there?"

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm25 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "{i}You walk her back to the dorm.{/i}"
    "{i}She trembles the entire way.{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm30:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
    if sana_love >= 25 and bar25 == True and beachvacation16 == True and sanadorm25 == False:
        jump sanadorm25
...
```