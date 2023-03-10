# Self-Esteem (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 14



## Next events

None

## Event properties

* Id: day14
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->day14

## Official wiki page

[Self-Esteem](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day14&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label day14:
    scene futabaoffice0
    with dissolve2
    play music "phantomthief.mp3" fadein 2.0

    "And so comes the end of another[school] day."
    "Today was..."
    "Well, let's just say it was a little different than what I'm used to."
    "I've obviously known about Yumi's habits when it comes to bullying some of the other girls but, up until today, I figured that was only a thing she did when I wasn't around."
    "As it turns out, she could not care less about that and is perfectly open to insulting everyone even with an authority figure ten feet away from her."
    "Of course, her target today wound up being the one she spends so much time on that it could practically be considered a hobby- Futaba."
    "I was so shocked by Yumi's brazenness that I wasn't even able to step in to try and stop her right away- prompting Makoto to speak up instead because she is a better teacher than me."
    "I {i}did,{/i} however, tell Yumi to come to my office after class so I can...do something that I haven't quite figured out yet."
    "But seeing as it's been thirty minutes since the final bell rang and she still hasn't knocked, I'm beginning to think that won't be happening."

    play sound "knock.mp3"

    s "..."

    "Or maybe she just has a horrible grasp on the concept of time."

    f "Sensei? May I come in?"

    "Or maybe it's not her at all and she really just...isn't coming."

    s "Sure. The door is open."

    play sound "dooropen.mp3"
    scene futabaoffice1
    with dissolve

    f "Uhm...good afternoon."
    s "Hey, Futaba. I didn’t expect to see you today."
    f "Well, I...wasn't really expecting to come today, but..."
    s "If this is about the Yumi thing, I feel like I should warn you that there is a very small chance she might show up while you're here."

    scene futabaoffice2
    with dissolve

    f "I...saw her leaving school, so...I don't think that's going to be happening..."
    s "Ah. Well, that explains why I only called it a {i}small{/i} chance. I figured something like that might happen given the type of person she is."
    f "Is this...a bad time?"
    s "Considering my only appointment was just cancelled, nope. Take whatever time you need. I've got nothing else going on."

    scene futabaoffice3
    with dissolve

    f "I won't be long..."
    f "I'm just...a little upset and...thought that talking about it might help. "
    f "And Rin has work today, so...I couldn't go to her instead. I'm sorry if that's an inconvenience."
    s "You know, I actually tried talking to Yumi last week about this and-"
    f "And she probably just shrugged it off, right?..."
    s "Oh. Yeah, sorry. I'm sure you've heard all of that before."

    scene futabaoffice4
    with dissolve

    f "Oh! I'm so sorry! I didn't mean to interrupt you! It's just...like you said, I've...already heard this before..."
    f "But...you don't have to apologize just because I'm too sensitive, Sensei. You didn't do anything wrong at all."
    s "Either way, I'm sorry that this keeps happening to you."

    scene futabaoffice5
    with dissolve

    f "And I'm sorry to keep troubling you by coming here afterwards..."
    f "It's not like I'm expecting anything to change, but...just talking to an adult about it is enough to put me at ease for a little while."
    f "It really helps...knowing that you're looking out for me. Even if that...doesn't really stop Yumi from doing things anyway."
    s "Yeah. Well, Yumi is a fucking bitch and you should probably just ignore anything she ever says to begin with."

    scene futabaoffice6
    with dissolve

    f "S-Sensei?"
    f "Are you sure it's okay for you to say things like that?..."
    s "Are you going to tell anyone I said it?"
    f "Well...no, but-"
    s "Then it's fine. Besides, that girl’s been nothing but cold to me since I met her."
    s "I'm starting to doubt that there's anyone who can actually get through to her and that she won't understand what she's putting others through until {i}she's{/i} put through something herself."

    scene futabaoffice7
    with dissolve

    f "I’m...sure she has her own problems..."
    f "For all we know...she could have already gone through more than either one of us."
    s "Sure, maybe. But that still wouldn't be an excuse for her to take everything out on you."

    scene futabaoffice8
    with dissolve

    f "I think...it would be less of a problem if I knew how to actually stand up for myself..."
    f "I feel like someone else always has to step in because I’m too...cowardly to actually do anything..."
    f "This...isn't new either. I've never been good when it comes to confrontation."
    f "You'd think that dealing with this for so long would have...maybe prepared me or something, but..."

    scene futabaoffice9
    with dissolve

    f "I guess it's kind of hard to stand up for myself when I...don't really see anything worth standing up {i}for?...{/i}"
    f "Does that make sense?"
    s "I mean...it does. But why would you feel that way? I think there's plenty about you worth defending."

    scene futabaoffice10
    with dissolve

    "Futaba focuses on the floor for a few moments as she summons the resolve to respond."
    "The truth is, I knew the answer to my question before I even asked it. But keeping it to myself without letting any words out into the open won't bring us closer."
    "My silence would do absolutely nothing for her."
    "The same goes for pretending to understand her...or pretending to relate."
    "All a person can do at a time like this is feign ignorance and gently pull the words out of someone else when they won't fall out on their own."

    f "Um...Well..."
    f "I just...don’t agree with that..."
    f "I...don't see myself as the type of person who's...worthy of being defended..."
    f "Which makes it feel so much worse a lot of the time since everyone always has to stick up for me..."
    f "I just..."

    scene futabaoffice11
    with dissolve

    f "I don't really like myself, I guess."
    s "Why, though? I think you’re great. And everyone except Yumi would probably agree."
    f "Thank you...really...But hearing something like that isn’t enough to change how I feel."
    f "It’s just..."
    f "It's really hard..."
    f "Looking at the other girls sometimes, I mean..."
    f "I'm sure it sounds petty, but...I can't help but be a little jealous."
    f "If I..."
    f "If {i}I{/i} could look like Yumi...I'd be so happy..."
    f "So the fact that she's always the one to point out how I don't?..."
    s "..."

    scene futabaoffice12
    with dissolve

    f "Being heavy..."
    f "Is {i}really{/i} hard, Sensei..."
    s "..."

    "I honestly have no idea how I’m supposed to reply to something like this and am reminded once again of the hesitance I face when stepping into this room each day."
    "I'm not qualified to make anyone feel better about themselves- not when, more often than not, I can't even pinpoint how {i}I{/i} personally feel."
    "The natural reaction here would be...reassurance, right? "
    "But something about that just seems so...expected."
    "Would the true owner of this body have more to offer than just the insistance that this person who has a hard time looking at herself should just...look a little closer?"
    "Or are all of us equally worthless when it comes to changing one's perception of themself?"
    "I don't know."
    "But I can't stay silent forever."

    scene futabaoffice13
    with dissolve

    f "I’m sorry for being such a downer all of a sudden...I know you’re probably uncomfortable hearing something like this from me..."
    f "I mean...there’s no way you could honestly look at me and tell me not to worry about it. Not when you see the difference with your own eyes every single day."
    s "..."
    f "..."
    s "Futaba."

    scene futabaoffice14
    with dissolve

    f "Y...Yeah?..."
    s "I'm going to tell you something right now, but you're going to have to keep it between us. Got it?"
    f "Um...sure. I...already expect everything that happens in here to remain confidential, so..."
    s "Good."
    s "In that case, I find you extremely attractive."
    f "..."
    s "..."

    scene futabaoffice15
    with dissolve

    f "Uhh...sorry, but...I don't think I heard you quite well..."
    s "That's fine. I don't mind saying it again."
    f "Wait. You don't-"
    s "I think you're extremely attractive and that the way you think about yourself is wrong."
    f "..."

    scene futabaoffice16
    with hpunch

    f "You...You do?!"
    s "Yup. But again, don't tell anyone I said that."
    f "Sensei...that's...wait..."
    f "I'm...still a student! Being attracted to me would mean-"
    s "We don't have to talk about what it means. But sitting here and listening to you talking about how you don't like yourself is tough to do when I feel the exact opposite way, you know?"
    f "I...I..."
    s "Plus, without being too specific, I'm sure there are plenty of girls in this school that envy certain parts of you."
    f "That's-"
    s "Inappropriate? Yeah, probably. But I didn't say any specifics, so all you can really do is {i}assume{/i} and file this under some sort of gray area."

    scene futabaoffice17
    with dissolve

    f "Sensei...do you..."
    f "Really think I’m pretty?..."
    f "Me?..."
    s "Is that weird?"
    f "Yeah...I think so..."
    f "No one’s ever looked at me like that before...let alone an adult..."
    f "I don’t...really know what to say..."
    s "I mean, you don’t have to say {i}anything.{/i} I just don’t want you to feel down on yourself anymore and...this was all I could think of saying to try and snap you out of it."
    s "I'm sure it didn't do much, though. So if there's anything you want from me in the future, don't hesitate to ask."

    scene futabaoffice18
    with dissolve

    f "Th-Thanks! But I, umm...I think you’ve already helped me enough for now..."
    f "I...probably just need a little more time to...process what I just found out, but...uhh..."
    f "I..."
    f "I'm also..."
    f "{size=-15}Attracted to you...{/size}"
    s "What was that? I couldn't hear you."

    scene futabaoffice19
    with dissolve

    f "Good. It was...extremely embarrassing."
    s "I see..."

    scene futabaoffice20
    with dissolve

    f "Umm...I really am feeling a little better now, though..."
    f "It makes me really happy knowing you don’t look at me the same way Yumi does..."
    s "I’m pretty sure I don’t see anything the same way Yumi does, so I wouldn’t worry about that too much."
    f "Heheh...I guess I’ll...try not to, then."
    s "Really, though- feel free to drop by whenever you’re feeling down."
    s "I accept house calls too, starting right now. I might have to charge you, though, depending on what sorts of services you're after."

    scene futabaoffice21
    with dissolve

    f "Okay! Uhh...thank you! But I think that...your office is fine and...I..."
    f "I don't know what...sorts of...services you are referring to..."
    s "Would you like a list? Let me just a grab a pen and-"

    scene futabaoffice22
    with hpunch

    f "No thank you! I'll be on my way now!"
    f "I'm sorry again for taking up so much of your time!"
    s "You really don't have to leave if-"
    f "Goodbye, Sensei! Thank you for the...information you shared with me today!"
    f "I promise I won't tell anyone!"

    scene futabaoffice0
    with dissolve
    play sound "dooropen.mp3"

    f "Goodbye again!"
    s "..."

    scene black
    with dissolve2

    "I hope I didn't scare Futaba off by admitting to her that I've been looking at her as more than just a student."
    "I doubt she's the type to do anything malicious or...irresponsible with the information, but I guess you can't ever be too sure about anything in this life."
    "At the very least, I hope she takes solace in the fact that there is someone out there fantasizing about her while continuously writing herself off as unwanted and undesirable."
    "The sadder truth, however-"
    "Is that I want everyone."
    "And that she's no more special than the rest of them."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ day14 = True

    "{i}Futaba's affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label day16:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
...
```