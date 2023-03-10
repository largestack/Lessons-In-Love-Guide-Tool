# Skulls (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 5

* Event [The Flavor of Love](./cafesugar.md) (Rin) is completed)



## Next events

None

## Event properties

* Id: rinfirstvisit
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rinfirstvisit

## Official wiki page

[Skulls](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rinfirstvisit&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rinfirstvisit:
    play sound "knock.mp3"

    "I knock on Rin's door and wait for her to answer, not knowing quite sure how this is going to go since I've never actually hung out with her in her room before."
    "To be fair, though, out of all of the girls in the class, she definitely seems like one of the few who would let me in without question."

    if rinfirsthall == True:
        "Hell, I'm pretty sure she would have let me in a little while back if she hadn't left her keys at school."

    "But I guess all I can really do at this point is hope she comes to the door and doesn't think I'm here with any ulterior motives."
    "Which I kind of am, of course. But I obviously don't want her to {i}think{/i} that."

    r "Who goes there?"
    s "Your teacher."
    r "My teacher? What?"
    r "Hold on a second."

    scene black
    with dissolve

    "I hear some shuffling from inside of the room as Rin makes whatever preparations are necessary to come greet me."
    "The sound of some drawers closing is immediately succeeded by the light tapping of her shoes as she puts them on and decides to come greet me in the hall instead...."

    play sound "dooropen.mp3"

    scene skullsredux1
    with dissolve

    r "What's up? It's not like you to just show up at my door. You're more of a {i}show up everywhere else{/i} kind of guy."
    s "Yeah, well I'm running out of other places to run into you, so I figured I'd come directly to your dorm this time."
    r "Anything in particular bring you here? Or were you just in the mood to see my face for whatever reason?"
    s "To be fair, it's a pretty nice face and I should be forgiven for seeking it out during my free time."

    scene skullsredux2
    with dissolve

    r "You sure you don't have anything more important to do?"
    s "More important than hanging out with my favorite barista?"
    r "Favorite out of...how many, exactly?"
    s "Hey, for all you know, I could be a regular at tons of cafes."

    scene skullsredux3
    with dissolve

    r "You wouldn't dare..."
    s "I could be convinced to drop all of them if a certain somebody lets me in her room, though."

    scene skullsredux4
    with dissolve

    r "Sure. That didn't sound predatory at all."
    s "It sounded better in my head."

    scene skullsredux1
    with dissolve

    r "Why my room, though? Wouldn't it make more sense for us to like, go somewhere else or something?"
    s "I'm just...interested in seeing the same thing you see every morning?"
    r "Yikes. Your game needs some serious work, Sensei. You're much better at cafe banter than dorm room banter."
    s "I will do my best to improve for both of our sakes."

    scene skullsredux4
    with dissolve

    r "I'll take your word for it."
    r "I'll also let you into my room if you promise not to only stop going to other cafes, but to stop saying weird and creepy shit."
    s "I don't know if you understand how hard that last part will be for me to accomplish."
    r "Then I suppose we will have to find out together!"
    r "Now, onward to Casa del Rin!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Rin guides me into the room and unstraps her boots after realizing that the two of us won't be going anywhere any time soon."
    "I direct my attention to what is easily apparent as her side of the room before she takes her place in front of me, unsure of how to proceed."

    scene skullsredux5
    with dissolve

    r "So, I guess if you're going to mug me, now is the best possible time."
    s "I'll abstain until the tour is over at the very least."
    r "Good call. It'll be a more effective shakedown if you know where all the good stuff is first."

    scene skullsredux6
    with dissolve

    r "Well...if there {i}was{/i} any good stuff, I mean."
    r "Our room's way outdated compared to all of the other ones on this floor."
    r "We've been waiting for our upgrade for literally forever but Futaba kept offering to wait because her heart is too big for her body."
    s "What sort of {i}upgrade{/i} are you waiting for exactly?"

    scene skullsredux7
    with dissolve

    r "Pretty much everything. The school is kind enough to provide standard beds and stuff, but I think our floor and our color scheme is supposed to be changed or something too."
    r "It's just annoying since I've got tons of stuff I want to hang up but {i}can't{/i} since I'll just have to take it all down once the thing starts."
    r "So...yeah. This is it for now. Sorry it's not really anything to write home about."
    r "My side is on the right and Futaba’s is on the left."
    r "She’s obviously not here right now, so it looks like it's gonna be just you and me for the indefinite future."
    s "And you don’t feel weird being alone in your room with an older man?"
    r "Well, I didn't until you said that."
    s "I told you not sounding creepy wasn't going to work out."

    scene skullsredux8
    with dissolve

    r "It's fine. We're still cool. I know you're not the type to try anything weird or whatever."

    scene skullsredux9
    with dissolve

    r "Besides, let's just say I have countermeasures in place in the event that you {i}do{/i} try anything."
    s "What...sort of countermeasures are you referring to, exactly?"
    r "Nothing. Just don't look behind me."
    s "Why? What's-"

    scene skullsredux10
    with fade

    "I finally direct my attention to Rin's wall only to find a shelf comprised entirely of what appear to be...authentic human skulls."

    s "There's no way those are real, right?"
    r "What kind of weirdo would keep fake human skulls on a shelf? Come on, Sensei."
    s "What kind of psychopath would keep real ones?"
    r "The kind who was nice enough to let you into her room! Is your way of showing thanks going to be insulting all of my things?"
    s "Are those even legal to own?"
    r "Hey, I won't tell anyone if you don't. Leave my friends out of this."

    scene skullsredux9
    with dissolve

    s "Okay. So I understand that there are real countermeasures in place now. Thank you for showing me."
    r "Any time, Sensei. Always willing to share my hobbies with a friend."
    s "So...do you have any hobbies aside from collecting body parts?"

    scene skullsredux11
    with dissolve

    r "Nothing exciting. Just playing guitar and listening to music and stuff."
    s "I guess that explains why you're always wearing headphones, then."
    r "Hey, I don’t {i}always{/i} wear them. I’m headphone-less at work, aren’t I?"
    s "I think you're technically supposed to be headphone-less at school as well, but it's not like I plan on enforcing that any time soon."
    r "Good, cause I'm running out of room on my shelf."
    s "I'm going to ignore that casual threat of murder and ask you about your guitar."
    r "What would you like to know, good sir?"
    s "How long have you been playing?"

    scene skullsredux12
    with dissolve

    r "Not for super long, but long enough to be pretty decent at it."
    r "I've always loved music and stuff so my mom wound up buying me one for my birthday one year."
    r "Needless to say, I've been kinda hooked ever since."
    s "Would you be able to play something for me?"

    scene skullsredux13
    with dissolve

    r "Like...Like now?"
    s "Sure. Why not?"
    r "Uhh...probably because it's super embarrassing?"
    s "You're not as good as you say you are, are you?"
    r "That's really not the problem here, Sensei."
    s "What's the problem, then?"
    r "The problem is that if I sit down and play guitar for you, it'll be an important moment that winds up heavily influencing the direction our relationship goes."
    r "Haven't you ever played a dating sim before? Or watched literally any sort of indie romance film?"
    s "I have not done either of those things, no."
    r "Jesus. Next, you're going to tell me you don't listen to music either."
    s "..."
    r "..."

    scene skullsredux14
    with dissolve

    r "Holy fuck!"
    s "Is there some sort of crime against...not listening to music?"
    r "Not a real one, but a social crime- yeah!"
    r "Only creepy, borderline-sociopathic serial killers don't listen to music! That's like, an inarguable fact!"
    r "Why would you even want to hear me play guitar if you don't like music? Wouldn't it bore you? Would you just walk away halfway through?"
    r "I have so many questions!"
    s "Well, I apologize for not being a standard human, but you can take solace in the fact that I am probably not going to kill you."

    scene skullsredux15
    with dissolve

    r "You know I'm gonna have to show you some stuff now, right? I can't just let you live a life without music in it. That's no life at all."
    s "Do whatever you want. It's not like I hate music or anything. It just...never stuck with me, I guess."
    r "Wack. You're a weird dude, Sensei."
    s "You have a shelf full of human skulls."

    scene skullsredux16
    with dissolve

    r "No. I have a shelf full of {i}friends.{/i} It's very different."
    s "..."
    r "..."
    s "Okay. Well, on that note, I should probably get going. Ami normally complains if I’m late."

    scene skullsredux7
    with dissolve

    if bonus == True:
        r "Oh, right! I totally forgot you two were even related."
    else:
        r "Oh, right! I totally forgot that she was a live-in accountant, something that is completely normal and not at all strange in Kumon-mi."

    r "Tell her I said hi, okay?"
    s "Sure. I-"
    r "Wait. Actually, {i}don’t{/i} tell her I said hi. Because I know Ami and she’d probably be like 'Where did you see Rin?' And then you’d be all like 'In her room.'"
    r "And then she'd be all like 'In her ROOM?' and then you would be all like 'Yeah. She's got skulls.'"
    r "And then it would just be weird for everybody and no one would win."
    r "So, yeah. Don't say hi."
    s "..."
    r "..."
    s "Okay."

    scene skullsredux9
    with dissolve

    r "Neat. Well, I guess that about wraps things up then."
    r "Thanks for dropping by, Sensei. Make sure to bring an offering the next time you show up."
    s "I'll come by again, but...I don't know if I can guarantee the offering part."
    r "Yeah, we'll see about that."
    s "Right...Goodnight, Rin."
    r "Night, Sensei! See ya round!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ rin_love += 1
    $ rinfirstvisit = True

    "I exit Rin's room and..."
    "Honestly, I think I know even less about her now than I did {i}before{/i} I entered."
    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "{i}You can now spend time with her in her room!{/i}"

    stop music fadeout 3.0

    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm6to9:
    play sound "knock.mp3"

    "..."

    r "Come in!"

    play sound "dooropen.mp3"

    scene rindormgen
    with fade

    "Rin invites me in again and the two of us kill time together in her room."
    "She shows me some of the music she’s been into lately and a lot of it seems eerily depressing."
    "I’m surprised that someone as cheerful as her listens to things like this, but
    I guess it’s never good to judge a book by its cover."
    "Plus, she collects human skulls so it’s not like she’s exactly “normal.”"
    "Eventually, Futaba sends her a text that she’s on her way back and
    the two of us decide it’s best for me to head out."

    scene black
    with dissolve

    $ rin_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"

    stop music fadeout 2.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabadorm6to9:
    play sound "knock.mp3"

    "..."

    f "Come in!"

    play sound "dooropen.mp3"

    scene futabadormgen
    with fade

    "Futaba lets me in and the two of us spend some time together."
    "Apparently, she was planning on spending the night studying."
    "I feel kind of bad for interrupting her, so I decide to help her out to the best of my ability."
    "It never ceases to amaze me how diligent and dedicated she is when it comes to[school]."
    "I’m glad that she's able to stay motivated despite her lack of confidence in herself..."

    scene black
    with dissolve

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabadorm10:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
...
```