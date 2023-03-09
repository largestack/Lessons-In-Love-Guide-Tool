# No, You
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library35&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 35

✅Event "[Rin: Ten Steps Forward](./rindorm35.md)" is completed (event=rindorm35)

✅Event "[Futaba: A Tree Falls in the Forest](./futabadorm30.md)" is completed (event=futabadorm30)



## Next events
* [Futaba: Overload](./futabadorm35.md)

## Event properties
* ID: library35
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label library35:
    scene futabarinlib1
    with dissolve
    play music "morningmoon.mp3"

    "I walk into the library to find Futaba and Rin caught in a conversation amidst an otherwise empty room."
    "The two of them don’t notice my presence right away so I decide to eavesdrop on their conversation and listen into whatever juicy stuff girls talk about when they’re alone."

    r "Yeah so I basically just kept rolling 5’s the entire night."
    r "I’m thinking of buying new dice, but I can’t figure out which color I want."
    f "I have an extra pair I could give you. I don’t really have a use for two sets and it’s not like I’m going to switch back and forth mid-game or anything."

    "Okay, this conversation is boring. It’s time for me to step in."

    scene futabarinlib2
    with dissolve

    s "Aren’t girls supposed to talk about fun stuff while there aren’t any guys around?"
    r "What do you mean? D&D is tons of fun. Don’t complain just cause you’re a buzzkill."
    s "What are you even doing here? Don’t you have work today?"
    f "Rin took the day off and is going to hang out with me here."

    scene futabarinlib3
    with dissolve

    r "Of course I took the day off. You’re always there to help me out, so who would I be to not be around for you?"
    s "First Nodoka and now Rin. People seem to be flocking to you all of a sudden, Futaba."

    scene futabarinlib4
    with dissolve

    f "It really does seem that way. All I did was let my hair down. "
    f "I had no idea it would make this much of a difference."
    s "Is that just how you’re going to keep it from now on?"
    f "I don’t know...I do like all of the attention I’m getting all of a sudden."
    f "Even if that attention is really only from you two and Nodoka."
    r "Sooo Sensei finally met Nodoka. Any thoughts? Love at first sight?"
    s "Why would I fall in love with her at first sight?"
    r "Because you both wear glasses and...write stuff?"
    s "Makoto and I both wear glasses and write stuff as well."

    scene futabarinlib5
    with dissolve

    r "Oh my God, are you in love with Makoto?!"
    r "I knew something fishy was going on with you two!"
    s "Shh, quiet. She’ll hear you."
    f "She {i}is{/i} rather fond of you..."
    f "I personally wouldn’t be surprised if, well, you know..."
    s "Okay, well let’s not drag her into this and make things any more complicated than they need to be."
    s "Rin."

    scene futabarinlib6
    with dissolve

    r "Me."
    s "You said something about being there for Futaba when she’s always there for you."
    r "I did."
    s "What does that mean?"
    r "It’s cause she hasn’t been feeling well. I thought you knew that?"
    f "Umm...I’m...right here..."
    f "I’d appreciate it if you two wouldn’t talk about me like I’m not..."
    s "I did, but I still don’t know exactly what is wrong."

    scene futabarinlib7
    with dissolve

    r "It’s...a fever. Right?"
    r "I've told her over and over to hold off on working until it breaks, but she seems weirdly adamant about still coming despite having to spend literally the whole day here."

    scene futabarinlib8
    with dissolve

    f "Well...it’s the only time I really get to see you and...you know. Books. And stuff."
    s "As much as I appreciate being next to books in your top interests, it would mean a lot to me if you’d put yourself first for once."
    r "For real. We have books in our dorm. The[school] will understand if you’re not feeling well."

    scene futabarinlib9
    with dissolve

    f "Can we not do this right now?"
    f "It’s not like working in the library is physically exhausting. I just need to stand around and...make sure I enter the returns into the computer."
    r "No one’s even here, though. Can't you just-"

    scene futabarinlib10
    stop music

    f "Just fucking drop it, okay?! "
    f "I appreciate that you’re looking out for me, but I’m fine!"

    "I guess it’s good that no one else is around today as Futaba would clearly be making a scene if anyone was."
    "I think this might be the first time I’ve ever heard her raise her voice and it’s...strange."
    "I can’t say I like it. "
    "Something’s definitely going on with her."
    "And if Rin nor myself is able to get it out, I’m beginning to worry that we really might just have to let her deal with it on her own."
    "I suppose that’s fine, though."
    "I’ve always believed that solving things on your own is the best way to become stronger."
    "And while I’ve definitely been trying to help her to a certain extent, it’s impossible to deny that most of this has been due to my own curiosity rather than a need to make her feel better."

    r "Woah..."
    r "I’m..."

    scene futabarinlib11
    with dissolve
    play music "beyondthewayoftime.mp3" fadein 5.0

    f "Oh- no! {i}I’m{/i} sorry! "
    f "I didn’t mean to yell at you like that. I’ve just been under a lot of stress lately and..."
    f "And I wish you two wouldn’t keep trying to get involved."
    f "It’s nice but it really is just making things...a little harder for me."
    s "We just want you to know that we’re here for you."

    scene futabarinlib12
    with dissolve

    f "I get that...but what help does it do to just keep saying you’re there for someone over and over and over?"
    f "I obviously know that you’re there for me and I’m glad you are...but if I wanted your help, I would have accepted it by now."

    scene futabarinlib13
    with dissolve

    f "With my parents traveling as much as they have my whole life, I’ve never really had anyone to {i}care{/i} for me during times like this."
    f "Until Rin, that is."
    r "Don’t."

    scene futabarinlib14
    with dissolve

    f "Huh?"
    r "Don’t say anything about how you need to deal with certain things on your own."
    r "That’s where you were going, wasn’t it?"
    r "{i}Until I met Rin, I was always alone. But she can’t fix everything.{/i} Blah blah blah independence and responsibility or whatever. Get real."
    r "I wouldn’t be so worried about you if you would actually start taking care of yourself."

    scene futabarinlib15
    with dissolve

    f "Are you saying...I can’t take care of myself?"
    r "No, I’m saying you {i}won’t{/i} take care of yourself. It’s different."
    r "You’re perfectly capable of doing it and you still choose not to."
    r "Then you get all mad when the people who are closest to you start to notice something is going on."
    s "Okay, I’m beginning to think Rin knows a little more about what’s {i}going on{/i} than I do."
    f "I’m beginning to think that, too. And I’d appreciate it if she and I could talk about it {i}alone{/i}, Sensei..."

    scene futabarinlib16
    with dissolve

    r "I want him here."
    r "He’s important to me."
    r "And he’s important to you too."

    "I can’t help but feel like I’ve somehow gotten wrapped up in a rare dispute between best friends when all I wanted to do was hang out with Futaba."
    "But obviously, these are [teenager]s we’re dealing with. Things like this are bound to happen and I should never believe otherwise."
    "This is still Futaba’s call, though. If she doesn’t want me here, I shouldn’t be here."
    "She and Rin can talk about this and I’ll just...avoid confrontation and pick up where we left off once the matter is resolved."

    s "Thanks, Rin. But I’ll step away for a little while and let the two of you talk."
    s "If Futaba wants to keep something secret, she shouldn’t be obligated to share it."

    scene futabarinlib17
    with dissolve

    r "Even if it’s dangerous?..."
    s "It’s still up to her to decide."
    s "I’ll be back in a few minutes."
    r "…"
    f "…"

    scene black
    with dissolve

    "I quietly make my way out of the library and lean up against the wall."
    "No one is around, so it doesn’t look like the two of them will be interrupted any time soon."
    "But, in the event that someone {i}does{/i} show up, I can probably just use my teacher-powers to tell them the library is closed or something."
    "………"
    "……"
    "…"
    "{i}Meanwhile...{/i}"

    scene futabarinlib18
    with dissolve

    r "Futaba..."
    f "What?"
    r "I love you."
    r "Soooooo ‘effing much."
    r "But you need. To. Stop. This."
    r "It’s dangerous."
    f "Stop what, Rin?"
    f "What are you saying?"
    r "You’re really going to make me say it?"
    f "You didn't have any problems making {i}me{/i} say it when I found out you were cutting yourself. So, yeah. I am."
    r "Fine, then. I'll say it."

    scene futabarinlib19
    with dissolve

    r "When was the last time you ate anything?"
    f "Yester-"
    r "{i}Without{/i} fucking...throwing it up right away."
    f "..."
    r "I know that's what's going on..."
    r "You did the same fucking thing in middle[school]."
    r "You don’t want Sensei to know because it’s embarrassing, right?"
    r "You know he’ll just say something about how he thinks you’re beautiful no matter what. "
    r "But you don't think that."
    r "And no compliments mean {i}anything{/i} if you don’t think that...Right?"
    r "It’s just like how I have to lean on hurting myself to feel better sometimes."
    r "I get it. I really do."
    f "…"
    r "Say something."
    f "You don’t get it. It’s not the same thing."
    f "You don’t have actual {i}reasons{/i} to feel the way you do. You’ve said it yourself a million times."
    f "It just happens..."

    scene futabarinlib20
    with dissolve

    f "Rin..."
    f "I love you too. More than anyone."
    f "All I’m doing is trying to feel a little better about myself."
    f "And it’s been working! I’ve...lost a few pounds ever since the beach and...And I’ve even started wearing my hair differently."
    f "I'm reinventing myself!"
    f "Things are getting better!"
    f "I’ll go back to normal soon."
    f "I just want to be a little happier first."
    r "Things like this don’t make you happier! They make it worse! You're literally destroying your body."
    f "Good. This body deserves to be destroyed."
    f "And besides, isn't this the pot calling the kettle black right now?"

    scene futabarinlib21
    with dissolve

    r "Fuck the pot and fuck the kettle!"
    r "This is your best-friend...your {i}sister{/i} begging you to stop killing yourself because you don't like how you look!"
    r "We can go to the gym together! I’ll go on a diet with you! I’ll do whatever you want!"
    r "Just cut it out already!"
    f "Rin..."
    r "I mean it! I’m not kidding!"
    f "…"
    r "…"

    scene futabarinlib22
    with dissolve

    f "You’re..."
    f "You're not going to tell him...are you?"
    r "Of course not! "
    r "We would have wound up in this same conversation today whether he was here or not."
    r "He doesn’t have anything to do with this."
    r "I’m so fucking worried about you. So worried I couldn’t even work."
    r "I get that you’re unhappy, but we can start fixing that together! Just like last time!"
    r "Please...for me."

    scene futabarinlib23
    with dissolve

    f "…"
    r "…"
    f "I’ll try."
    f "For you."
    f "But that's all I can promise."
    f "I don't know if it will work or not."
    f "But I'll try."
    r "I love you so much."
    r "Thank you."
    f "I love you too."
    f "Thank {i}you{/i}."
    f "Even if you’re annoying and won’t let me do things my way."
    r "You never let me do things my way either. This is just me returning the favor."
    f "Hehe...I guess you’re right."
    f "Should we...maybe tell Sensei it’s okay for him to come back in yet?"

    scene futabarinlib24
    with dissolve

    r "Umm...hold on one sec."
    r "My mascara isn’t running down my face right now, is it?"
    r "Don’t want to give away that I was crying or anything."

    scene futabarinlib25
    with dissolve

    f "You look fine..."
    f "More than fine."
    f "You’re beautiful."
    r "No, {i}you’re{/i} beautiful."
    f "No, you."
    r "No, {i}you.{/i}"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    play sound "slidedoor.mp3"

    r "Excuse me, is there a teacher available to assist two [young_girls] in the library?"
    r "There are so many hard-to-reach books and our tiny arms simply can not reach any! Whatever shall we do?"
    s "I am a teacher. I can obtain hard-to-reach books."
    r "Wonderful! Come quick!"

    scene futabarinlib26
    with dissolve
    play sound "slidedoor.mp3"

    s "Hey. Glad to see you two didn’t kill each other."
    s "I was worried that Rin needed help burying a body or something just now."
    f "Nope. No bodies to be buried just yet. "
    f "We’re fine now. Thanks for stepping out and letting us talk alone."
    s "Hey, it’s not my responsibility to solve every problem. Some things are better fixed by others."
    s "I’m just here to hang out with [teenage]girls."
    f "Well you get two of them today, so be happy about that while you still can."
    s "Oh, I will be. Don’t worry."

    scene black
    with dissolve2

    "The rest of the morning goes by rather quickly."
    "Futaba remains pretty lethargic throughout, but I chalk it up to whatever mystery-ailment is plaguing her as she seems in good spirits otherwise."
    "I’m not sure what the two of them said to each other to diffuse the situation so quickly but, whatever it was, I’m glad. "
    "I didn’t particularly like seeing angry-Futaba, and I’m perfectly content with never having to see that again, if at all possible."

    $ renpy.end_replay()
    $ library35 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label futabainvite1:
...
```

## Code that triggers this event
File: \game\FutabaEvents.rpy
Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
    if futaba_love >= 25 and futabanew3 == True and library20 == True and library25 == False:
        jump library25
    if futaba_love >= 30 and futabadorm25 == True and beachvacation16 == True and library25 == True and library30 == False:
        jump library30
    if futaba_love >= 35 and rindorm35 == True and futabadorm30 == True and library35 == False:
        jump library35
...
```