# Spotless Mind
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo17&go=Go)


Part of event chain [No Escape](./christmastwo16.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo17
* Group: Main
* Triggered by label: christmastwo16

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo17:
    scene norikospresent1
    play music "hometown.mp3"

    "Somehow, I wind up in front of Noriko. "
    "She holds a box that is both familiar and unfamiliar at the same time- which I’m sure sounds strange to you, but there’s no other way I can think of describing it."
    "I’m assuming this is that present she was telling me about a while back. "
    "I still have no idea what to expect but, having grown to know this girl relatively well over the last several months, it’s safe to assume it’s likely something with some sort of...sentimental value."
    "Despite her appearance, Noriko’s consistently been one of the most sentimental people I know."
    "And I see no reason for her to break that pattern now- on a night that I’m sure she wishes she could have enjoyed with me in a different sort of way."
    "Perhaps in the future, if there even is one."

    n "Heeeeeey..."
    n "I went up to the hotel room to find you, but Makoto told me you were busy with Miku, so...I figured I’d just wait around in the lobby until you showed up."
    n "Did she like her present? "
    s "Yes and no. It’s a little complicated."

    scene norikospresent2
    with dissolve

    n "Yeah...I can...definitely relate to that."
    s "I take it that’s for me, then?"
    n "Yeah..."
    s "Am I allowed to open it?"

    scene norikospresent3
    with dissolve

    n "Huh? Yeah. Why wouldn’t you be?"
    s "I’m just getting mixed signals between you and the box itself and I’m currently choosing sides."
    n "Well...I guess I should be pretty nervous then, huh?"
    s "Probably not. I can’t imagine myself ever choosing a box over you."

    scene norikospresent4
    with dissolve

    n "Yeah...we’ll see about that..."
    s "Give it here, then. There’s no better place to break the rules than a hotel lobby and I am now determined to go against that box’s wishes."
    n "You know it wasn’t the {i}box{/i} who wrote “Do not open” on itself, right?"
    n "Also, can we maybe, like...not do this in here? I’d like to be somewhere a little more private since I’m probably going to cry."
    s "I don’t know if I like the idea of whatever this present is making you cry, but if going somewhere else is what it takes for me to figure it out, sure."
    s "I’m assuming Kirin told you about the boiler room, then?"

    scene norikospresent3
    with dissolve

    n "Boiler room? What are you talking about?"
    s "Oh. Nevermind. I just figured that’s what you meant with the whole “privacy” thing."
    s "I’m mostly under the impression by now that Kirin just tells you everything immediately after it happens and-"
    n "What were you and Kirin doing in-"

    scene norikospresent5
    with dissolve

    n "Actually...no. That’s not important right now. I’ve only got a little while until I have to head back and...I kinda need you to see this before that."
    s "You’re leaving already? Why?"

    scene norikospresent6
    with dissolve

    n "I don’t {i}want{/i} to leave."
    n "I just think I’ll have a harder time staying around after you see what’s inside the box."
    s "..."
    n "Um...anyway..."
    n "I’m pretty sure the roof is unlocked...and it’s not that cold out tonight, so we can probably do this up there?"
    s "Stairs and boxes, my two favorite things. "
    s "Lead the way. I’ll be right behind you."
    n "Not for long, you won’t."

    scene black
    with dissolve2

    "I’m not exactly sure what Noriko means by that, but I follow her regardless."
    "And, of course, she’s the type of person to take the stairs instead of the elevator. "
    "So on top of having to ascend what feels like an ungodly amount of stories, I have to deal with the exhaustion of actually moving now as well."
    "But if this is what it takes for her to cry in a contained environment rather than one that a classmate could pop into at any given moment, I guess it’s just something I have to deal with."

    scene clearnightsky
    with dissolve2

    "As we open the door and step out onto the roof, I wonder how many more girls I’ll be forced to watch cry before the night comes to an end."
    "So much for Christmas being the most magical night of the year- if that’s even a thing people say."
    "But I guess that crying in itself is sort of magical in a way."
    "Not everyone is in tune enough with their feelings to do something like that. And many of the people who {i}are{/i} would just...rather not."
    "I’d say I hate it myself, but it’s been so long at this point that I don’t know if I can even attribute such a strong word to the idea of tears."
    "I will say with utmost certainty, though, that it’s a lot harder to hate something when you’re only experiencing it secondhand. "
    "The two of us approach the edge of the hotel and sit down on the concrete rooftop."
    "It’s cold. Much colder than the air itself."
    "And despite being face to face with a girl prepared to be wounded all for the sake of tightening the rope wrapped around us-"
    "All I can think of is wanting to go back inside."

    scene norikospresent7
    with dissolve2

    "The box sits in my lap the same way she would when she was younger."
    "That’s not a memory, just an educated guess based on all that I’ve heard from her."
    "I’m sure she’s thinking something similar right now."

    n "So...how was the Christmas party without me being around? Any...I don’t know, quieter?"
    s "Is this the part where you start stalling because you’re worried about how things are going to play out?"

    scene norikospresent8
    with dissolve

    n "Ugh. I really should have tried rationing out all the times I’ve done that. I could seriously benefit from that tactic right now if you weren’t already familiar with my tricks."
    s "Guess you’re going to have to come up with a new method if you want some additional time in the future."
    s "Or not, since the world is just going to repeat itself soon anyway."

    scene norikospresent9
    with dissolve

    n "What, are we in some kind of movie right now?"
    n "You gonna tell me that the only reason you don’t remember me is because you went all Eternal Sunshine on yourself?"
    s "I have no ideas what that is."
    n "Well, we should watch it together if you still want to be around me after tonight."
    s "Noriko, I’m not going to find the severed head of someone I care about inside of this box, am I? Because you seem really worried that whatever is in here is going to make me...dislike you or something."
    n "What if it was a severed head of someone you {i}didn’t{/i} like? Then what?"
    s "You’re stalling again and I’m not falling for it."
    n "You can’t fault me for trying."
    s "Can I open this now, then? Or do you know some spiritual hack where opening boxes facing west is somehow a good luck charm?"
    n "You can open it. "
    n "You’ve waited long enough."

    scene norikospresent10
    with dissolve

    "I peel back the tape covering the box and place it on the concrete."
    "The wind sweeps it away and carries it off the ledge immediately."
    "There’s some sort of metaphor or symbolism to be gleaned from that, but I can’t be bothered to decode it right now."
    "There’s nothing lavish or exciting inside of the box- "
    "Just a stack of what appear to be organized papers with neat, half-cursive handwriting covering them."
    "I’m assuming that whatever the {i}present{/i} is lies within these pages."

    scene norikospresent11
    with dissolve

    s "..."
    n "..."
    s "..."
    s "What is this?"

    scene norikospresent12
    with dissolve

    n "Your past."
    n "Or a little piece of it at least."
    n "We’d need a lot more boxes to pack up our entire history."
    s "Did you write these?"
    n "..."
    s "..."
    n "No."

    play sound "static.mp3"
    scene nikil1 with flash
    stop sound

    n "Nee-chan wrote all of these for you after you disappeared."
    n "There were hundreds of them. "
    n "She must have been writing one every single day for...I don’t even know how long."
    n "But obviously, she had no idea where to send them."

    play sound "static.mp3"
    scene nikil2 with flash
    stop sound

    n "Not at first, at least."
    n "And even when you started seeing me again, it’s not like I could have just...delivered these to you."
    n "Like...I had no idea they even existed until I was going through her closet the other day."
    n "And if Nee-chan knew in the beginning that I was getting to spend time with you but not her, it would have broken her even more."

    play sound "static.mp3"
    scene nikil3 with flash
    stop sound

    n "She loved you...so, so, so, so much."
    n "More than I ever did. More than I ever {i}could.{/i}"
    n "{i}How can I compete with that, Sensei?{/i}"
    n "I spent so much time psyching myself up and trying to win your affection like it was some sort of...{i}contest{/i} that I lost sight of how I started with the biggest handicap of all."
    n "I’ve been second place forever. In everything."
    n "And if it wasn’t with Nee-chan, it was with Maya."

    play sound "static.mp3"
    scene nikil4 with flash
    stop sound

    n "I’m just the...younger, spunkier version of the girl you used to love. And she’s still the same person she’s always been. So like...what's the point of {i}me?{/i}"
    n "Even if I’ve changed...even if the...{i}perfect{/i} girl I dreamt up for you is completely to your liking...I still don’t have what she did."
    n "I don’t have that history."
    n "The...backlog of emotions and kisses and whatever other shit you guys did to each other before I even understood grammar. "
    n "I couldn’t keep hiding this from you."

    play sound "static.mp3"
    scene nikil5 with flash
    stop sound

    n "I mean...I {i}could{/i} have kept hiding it from you. And it probably would have made my chances a million times better..."
    n "But that wouldn’t be fair. To you...or Nee-chan...or even me in a sort of really roundabout way that I can probably justify if you give me enough time."
    n "So...yeah. "
    n "If you can’t remember the past, I’ll bring the past to you."
    n "Even if it’s not my place to do that."
    n "Even if I have to steal embarrassing stuff out of my older sister’s closet because, at least until today, she was too stubborn to even think about telling you."

    play sound "static.mp3"
    scene norikospresent13 with flash
    stop sound

    n "That wasn’t the last one, you know. "
    n "There were tons more after that."
    n "Even when my parents were getting on her case about how it was becoming an unhealthy obsession...she never stopped."
    n "She never stopped loving you."
    n "And she never will."

    scene norikospresent14
    with dissolve

    n "Ugh. Right on cue. I told you I was going to cry."
    s "..."
    n "If your memories really are gone, I’m sure you might believe that these could just be fake or something..."
    n "And I have no way of proving they’re not."
    n "But, no matter what you choose to believe or...what you decide to do from here on out...I think you should at least consider Nee-chan’s feelings."
    n "Mine too, if you can...but..."
    n "Alas..."
    n "Second place forever..."
    s "..."
    n "..."
    s "..."
    n "..."

    scene norikospresent15
    with dissolve

    n "Sensei?"

    play sound "pop.mp3"
    stop music
    scene black
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene smile with flash
    stop sound
    play music "sanctuary.mp3"

    "///////////////////////CONGRATULATIONS"
    "///////////////////////YOU HAVE BEEN SELECTED TO PARTICIPATE IN A CUSTOMER SATISFACTION SURVEY"
    "///////////////////////THIS SERVER WILL BE UNDERGOING SCHEDULED MAINTENANCE SOON"
    "///////////////////////SYSTEMS WILL REMAIN OFFLINE FOR AN INDETERMINATE AMOUNT OF TIME ONCE MAINTENANCE BEGINS"
    "///////////////////////YOUR PARTICIPATION IN THIS SURVEY WILL BE GREATLY APPRECIATED"
    "///////////////////////ONCE THE SURVEY IS COMPLETE, YOU WILL BE ABLE TO ACCESS “CARE PACKAGE”"
    "///////////////////////WOULD YOU LIKE TO BEGIN THE SURVEY NOW?"

    menu carepackageq:
        "Yes":
            "///////////////////////THANK YOU FOR YOUR PARTICIPATION"
        "No":
            "///////////////////////INPUT NOT ACCEPTED"
            "///////////////////////AT LEAST ONE SURVEY IS NEEDED PRIOR TO BEGINNING SCHEDULED MAINTENANCE"
            "///////////////////////REPEATING QUESTION"
            "///////////////////////WOULD YOU LIKE TO BEGIN THE SURVEY NOW?"
            jump carepackageq

    "///////////////////////WHICH ONE OF THESE WORDS BEST DESCRIBES YOUR CURRENT STATE OF MIND?"

    menu:
        "Callous":
            $ cpcallous = True
        "Calm":
            $ cpcalm = True
        "Concerned":
            $ cpconcerned = True

    "///////////////////////HOW OFTEN DO YOU EXPERIENCE “dreams?”"

    menu:
        "Infrequently":
            $ cpinfrequent = True
        "Frequently":
            $ cpfrequent = True

    "///////////////////////DO YOU EVER WISH YOU WERE SOMEWHERE ELSE?"

    menu:
        "Yes":
            $ cpyes = True
        "No":
            $ cpno = True

    "///////////////////////WHICH OF THE FOLLOWING IMPROVEMENTS WOULD YOU BE MOST INTERESTED IN?"

    menu:
        "Faster movement speed":
            $ cpmovementspeed = True
        "Memory backup":
            $ cpmemory = True
        "Additional penetration":
            $ cppenetration = True
        "Vision":
            $ cpvision = True

    "///////////////////////DO YOU BELIEVE IN GOD?"

    menu:
        "Yes":
            $ cpgodyes = True
        "No":
            $ cpgodno = True

    "///////////////////////THANK YOU FOR TAKING THE TIME TO COMPLETE THE CUSTOMER SATISFACTION EXIT SURVEY"
    "///////////////////////YOUR CARE PACKAGE IS CURRENTLY BEING PROCESSED"

    stop music
    scene black

    "///////////////////////THIS COULD TAKE UP TO SEVERAL MINUTES TO COMPLETE"
    "///////////////////////PLEASE REMAIN CALM WHILE NECESSARY ELEMENTS ARE RESTORED FROM OUTDATED VERSIONS"
    "///////////////////////..."
    "///////////////////////..."
    "///////////////////////..."
    "///////////////////////..."
    "///////////////////////..."
    "///////////////////////..."

    play sound "pop.mp3"
    scene norikospresent16
    $ renpy.pause(8, hard=True)
    play sound "pop.mp3"
    scene norikospresent17
    play music "memories.mp3"

    "///////////////////////MEMORY SUCCESSFULLY RETRIEVED"
    "///////////////////////PLEASE REMEMBER ALL I DO FOR YOU"
    "///////////////////////EVEN WHEN IT SEEMS IMPOSSIBLE"

    scene norikospresent18
    with dissolve

    s "Shouldn’t we be watching Christmas movies right now?"
    s "It feels kind of weird to be watching anime when we told your parents we were going to do our {i}own{/i} Christmas stuff instead of what they wanted to do."
    ni "Are you kidding? Why would we watch something that lame when the newest episode of Gunfighter Z: Machine War Paradox Chronicles comes out tonight?"
    s "Why are anime titles always so long? I don’t get it."

    scene norikospresent19
    with dissolve

    ni "Well, you’re more than welcome to go back downstairs and play with Noriko instead if you want. Since you’re too much of a loser to watch giant robots blow up other giant robots, I mean."
    s "No thanks. She keeps trying to sit on my lap and it’s weird."

    scene norikospresent20
    with dissolve

    ni "I know, right?! She thinks you’re like, her {i}actual{/i} big brother or something. And my parents see no problem with it at all."
    s "I don’t think there’s a {i}problem{/i} with it, I’d just rather hang out with you."

    scene norikospresent21
    with dissolve

    ni "W-Well of course you’d rather hang out with me than some kid. That’s barely even a compliment."
    s "Then why are you blushing so much?"

    scene norikospresent22
    with fade

    ni "I...I’m not blushing! It’s just hot in my stupid room because my parents won’t turn the stupid heat off!"
    s "Don’t you have a thermostat in here? Just turn it down yourself if you’re hot."
    ni "Yeah, but...I don’t know how to use it..."
    s "You’re completely helpless, aren’t you?"
    ni "If you’re so smart, why don’t you do it?!"
    s "Because you’re not actually hot. You’re just saying that."
    ni "Why would I lie?! Also, shut up! Gunfighter is about to come on!"

    scene norikospresent23
    with dissolve

    s "I’ll just turn the heat down myself."
    s "Even if your parents would get mad at {i}you{/i} for doing it, they-"

    scene norikospresent24
    with dissolve

    s "..."
    ni "..."
    ni "[[REDACTED]? What’s wrong?"
    s "I..."
    s "Nothing."
    s "I’m fine."
    s "I’m actually feeling a little cold, though...so I don’t think I’m going to turn the heat down after all."
    ni "Cold? Oooooh...{i}maybe there’s a ghost in the room?{/i}"
    s "Yeah...maybe..."
    ni "[[REDACTED], no. I was obviously kidding. There’s no such thing as ghosts. They’re-"
    n "{i}You’re such a good boy.{/i}"

    play sound "static.mp3"
    scene norikospresent25 with flash
    stop sound

    n "{i}It’s no wonder I fell in love with you.{/i}"
    n "{i}You try so hard to keep this side of you away from everyone that when it finally comes out, you just seem a million times cuter.{/i}"
    n "{i}You know, the best part about being in second place is that even if I don’t win, I always have a really clear view of the goal.{/i}"
    n "{i}I’ll keep running, Sensei. Forever and ever. Even when I know I can’t win.{/i}"
    n "{i}Even when my legs give out.{/i}"
    n "{i}And, who knows? Maybe the next obstacle I put down will wind up knocking someone else over instead of me.{/i}"

    scene norikospresent26
    with dissolve

    n "Merry Christmas."
    n "Maybe next year I’ll get you a present that doesn’t immediately make me cry."
    s "I..."
    s "I remembered something..."
    n "Was it nice?"
    s "..."
    n "I bet it was."

    scene clearnightsky
    with dissolve2

    play sound "phonebeep.wav"

    "My phone suddenly goes off in my pocket."

    n "Looks like my time here is up..."
    n "You better answer that, Sensei."
    n "I bet it’s someone really important."
    s "..."

    "Noriko leaves the roof and I struggle to regain enough control of my hands to reach for my phone."
    "I look down at one of the letters and notice that I’ve been gripping it so tightly that it’s begun to crinkle and tear."
    "I can still see it- the vision of an old bedroom."

    if bonus == True:
        "The scent of baked goods leaking in through the crack under the door and the feeling of my dick going numb from having to lie on it for so long to conceal an erection."

    "I can still imagine her face and the hue of her cheeks when I called her out for blushing."
    "But why {i}that{/i} night?"
    "Why would I recall something so small and insignificant when I’m sure there were thousands of other memories I made with her that were ten times bigger?"
    "I don’t know."
    "I don’t know anything other than the fact that it’s true now. That Niki is who she says she is."
    "And so is Noriko, even if her new fascination is taking over the role of a martyr in an effort to get me back together with someone who she both loves and loathes all at once."

    play sound "phonebeep.wav"

    "My phone goes off again."
    "I place the letter back inside of the box, closing it tightly and subconsciously reaching for the tape that had been carried off the ledge just moments ago."
    "Of course, I grasp nothing but the air itself."
    "But then-"
    "I recover enough control to gaze into a small, electric rectangle and see who the cause of these beeps has been."

    ni "{i}Come downstairs right now. I know you’re up there. I need to talk to you. It’s important. Please.{/i}"
    ni "{i}I’ll be in front of your hotel. Noriko gave me the address. And come alone. Don’t bring her. Please.{/i}"
    s "..."

    $ renpy.end_replay()
    $ christmastwo17 = True

    jump christmastwo18

label christmastwo18:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
s "And your solution is to just keep letting that happen?"
    mi "I told you already...I’m on Team Makoto..."
    mi "I can’t be-"

    scene mikubear23
    with dissolve

    mi "Mmm! Mm..."
    mi "I...can’t be...mnch...doing this..."
    mi "It’s bad...it’s...really...really...bad..."

    scene mikubear27
    with dissolve

    s "You seem to be enjoying this quite a bit for someone who allegedly doesn’t want it."
    mi "I doubt {i}you’re{/i} havin’ any fun, though. I’ve got no friggin’ idea what to do with my tongue. I’m still new to this. "
    s "That’s fine. We can practice."
    mi "..."
    s "..."
    mi "I’ve gotta tell her, Sensei..."
    s "You don’t."
    mi "I do..."
    s "You don’t. "
    mi "I do. Every time I look at that bear, it’s gonna remind me of this. "
    s "Then get rid of the bear."

    scene mikubear28
    with dissolve

    mi "You kidding?! No way! This is the first time anyone’s ever given me somethin’ like that! And it was friggin’ {i}you{/i} of all people."
    mi "I’m gonna treasure it forever!"
    s "Then don’t complain about how it makes you feel when you look at it. "
    s "Accept what happened here tonight and take solace in the fact that the person you’re interested in is interested in you."
    s "Makoto doesn’t need to know that. No one does."

    scene mikubear24
    with dissolve

    mi "Sensei...thank you again for the present, but..."
    mi "I kinda...think I need a little time to myself to...figure out what to do."
    s "I’m assuming that means we’re done making out then?"
    mi "I guess so..."
    mi "Sorry again for attacking you like that..."
    s "You can attack me as often as you want so long as we’re not in public."
    mi "Stop sayin’ such...dangerous things, Sensei..."
    mi "It’ll only make it harder for me..."

    scene black
    with dissolve2

    "Miku and I break apart. "
    "But she breaks a little bit more."

    scene mikubear29
    with dissolve2

    if bonus == True:
        "{i}Welcome to Lessons in Love!{/i}"
        "{i}A game where you get to put your penis inside of girls dealing with trauma, no matter how bad of an idea they may think it is!{/i}"
        "{i}Occasionally, your actions will cause things like this to happen.{/i}"
        "{i}But that’s okay! Because, most of the time, it won’t even be your fault.{/i}"
        "{i}You are a shadow, after all.{/i}"
        "{i}You are everything I want you to be.{/i}"
        "{i}And slowly, but surely, you are becoming even more.{/i}"
        "{i}There is something buried underneath your feet.{/i}"
        "{i}And something above as well.{/i}"
    else:
        "{i}Welcome to The Legend of the Huggy Boy, a completely uncensored video game that has absolutely nothing to do with Lessons in Love!{/i}"
        "{i}There is nothing here!{/i}"
        "{i}It's all just empty.{/i}"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmastwo16 = True
    $ miku_love += 10

    "{i}Miku’s affection has increased to [miku_love]!{/i}"

    stop music

    "/////////////////////////////EVENT COMPLETE"
    "/////////////////////////////ATTEMPTING TO DOWNLOAD CARE PACKAGE"
    "/////////////////////////////..."
    "/////////////////////////////..."
    "/////////////////////////////..."
    "/////////////////////////////DOWNLOAD SUCCESSFUL"
    "/////////////////////////////PLEASE CONTINUE WALKING. YOU ARE VERY GOOD AT IT."

    play sound "static.mp3"
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    scene maggotgod1 with flash
    scene maggotgod2 with flash
    stop sound

    jump christmastwo17
...
```