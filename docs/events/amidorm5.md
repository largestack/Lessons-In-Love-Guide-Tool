# Home Away From Home
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm5&go=Go)



## Event preconditions
✅Ami love greater than or equal to 5

✅Day of week is not Monday

✅Day of week is not Friday



## Next events
* [Ami: No One Can See Us](./amidorm10.md)
* [Maya: Secrets Worth Keeping](./mayadorm5.md)

## Event properties
* ID: amidorm5
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label amidorm5:
    play sound "knock.mp3"

    "I knock on the door. I figure that if Ami’s around, she won’t have a problem letting me in."
    "Unfortunately, I can’t say the same for Maya. So hopefully-"

    play sound "dooropen.mp3"
    scene firstamidormredux1
    with fade

    m "..."

    "Well, I guess this is a thing I have to deal with now."

    m "What are you doing here?"
    m "You realize I sleep in this room, don't you? Are you trying to prevent that from ever happening again?"
    s "Is Ami around by any chance?"
    a "Maya? Who’s out there?"
    m "No. Ami isn't around right now."
    s "But I just-"
    m "Listen, I'm not letting you inside. So if you could just leave here right away, it would be-"
    a "Wait, is that Sensei’s voice I hear out there?! Are you turning away my beloved uncle right now?!"

    scene firstamidormredux2
    with dissolve

    m "Ugh, why does she always have to be so loud?"
    s "Will you let me in if I promise to not speak to you? Because I really did just come here to see Ami."

    scene firstamidormredux1
    with dissolve

    m "Of course you did."
    m "You always do."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I'm not quite sure what Maya meant by that last part...but she let me into the room in the end, so I really can't complain."
    "........."
    "......"
    "..."

    scene firstamidorm1
    with dissolve2

    a "Sensei! I’m so glad you finally made it! I feel like I've been waiting forever for you to come check out my room."
    a "I’ve been doing a {i}ton{/i} of decorating lately. I even went down to the library and made Futaba print out a bunch of pictures for me."
    a "Isn't it super awesome in here? Doesn't it make you want to move in with us?!"
    s "Is that a couch over on your side of the room? How did you afford that?"

    scene firstamidorm2
    with dissolve

    a "I didn't. Maya and I found it on the side of the road and called Ayane to help us carry it back."
    a "It was super heavy and we almost died."
    m "Correction: {i}I{/i} almost died. You didn't even touch the couch."

    scene firstamidorm3
    with dissolve

    a "What are you talking about? I sat on it before you guys picked it up. That counts as touching, doesn't it?"
    a "Besides, if I didn't guide you guys up the stairs while you were carrying it, it never would have made it up here."
    m "..."
    a "Whatever, Maya. Stay silent. You know I helped."
    m "Uh-huh."
    s "You could have just called me, you know. I’m no weightlifter, but I’m pretty sure that I’m stronger than a few teenage girls."

    scene firstamidorm4
    with dissolve

    a "I tried! But then Maya got all {i}Maya{/i} on me and said that she'd never talk to me again if I tried getting you to help as well!"
    s "That seems like a pretty dramatic repercussion for asking someone stronger than you to help you carry something."
    m "I regret nothing."

    scene firstamidorm5
    with dissolve

    a "Anyway, secrets aside, do you wanna hang out with us? It's not like we had any plans, so we can pretty much do whatever you want, Sensei."
    s "Sure. That's kind of why I came over here anyway."

    scene firstamidorm6
    with dissolve

    m "Oh wow, look at the time. I suddenly have to leave."
    a "Ugh. Of course you do..."

    scene firstamidorm8
    with dissolve

    "Maya quickly gets up and scurries past me into the hall. I try to make eye contact with her on her way out, but she doesn't so much as glance at me."
    "I still have no idea what her problem with me is, but...I doubt it's one that I can just get to go away overnight."

    play sound "dooropen.mp3"

    m "Later, Ami. I'll be back once I'm done with the...things I have to do. Or something."
    m "Anyway, bye."
    a "Yeah...See you later, Maya."

    scene firstamidorm9
    with dissolve

    a "…"
    s "…"
    a "Sorry about that, Sensei. I guess Maya just...doesn't like you for some reason."
    s "Woah, really? I had no idea."
    a "Anyway, I hope you're okay with it just being the two of us in here."
    s "Of course I am. That's how it always is at home, isn't it? Well, at least for now."
    s "This place is pretty nice, Ami. I wouldn't hold it against you if you just decided to live here full time."

    scene firstamidorm10
    with dissolve

    a "What...What kind of [niece] would I be if I abandoned you to come live here?! There's no way I could leave you alone for that long!"
    a "Without me, you’ll starve! And none of your clothes will ever get washed!"
    a "Your life would be in ruin! You need me, Sensei! You need me more than you realize!"
    s "Wow, okay. You don't need to freak out about it. I'm fine with you staying at home. I just didn't think you'd really want to, I guess."

    scene firstamidorm9
    with dissolve

    a "Of course I want to, Sensei..."
    a "There's no place I'd rather be than where the two of us began our life together."
    s "Well...I'm glad you feel that way. Because my life has gotten pretty convenient thanks to you."

    "Not like I know how convenient it was {i}before{/i} Ami showed up, but that's a different story."

    a "I'm glad, Sensei. That's all I could ever really ask for."
    s "That said, if you ever need help with anything around your dorm like, you know...{i}lifting a couch,{/i} please just let me know."
    s "If you wind up hurting yourself doing something like that, it will inconvenience me as well. So please be careful."
    a "Heheh...of course."
    a "And who knows? Maybe Maya will feel a little more comfortable about you coming in here now that you've seen the inside of our room?"

    "Yeah, I don't think that's going to happen."

    scene firstamidorm11
    with dissolve

    a "You wanna take a closer look at my stuff, though?! It’s all really cool and is only {i}kinda{/i} like my room at home."
    s "So there are no anime posters or brightly colored manga or stuffed animals?"
    a "..."
    s "..."
    a "...Nooooo?"

    "I sigh to myself, not fully understanding both Ami's hobbies and her inability to spot just how similar this is to a room I've already grown accustomed to."

    s "Let’s see what you’ve got, Ami..."
    a "Yay! Attention!"

    scene firstamidorm12
    with dissolve

    "I take a step to the side and begin to look over Ami’s part of the dorm."
    "Her walls are lined with, as I predicted just moments ago, anime posters and manga."
    "There's a quote from an Emily Dickinson poem on her dry erase board, which is rather surprising given that this is Ami and-"
    "Well, I can't imagine Ami reading {i}anything{/i} that doesn't involve romance or...magical girls or something."
    "Suffice it to say, everything looks pretty close to how I imagined it would be."
    "I'm sure that for some girls, a first trip into their room would be kind of like a key to unlocking who they really are or...what they really like."
    "But for Ami, it's like I'm using that key to lock myself inside. And I don't know any more about her now than I did even yesterday."

    scene firstamidorm13
    with dissolve

    a "So, what do you think? Is it cool? Cause I think it’s cool."
    a "But if you don’t think it’s cool then it’s probably not cool."
    a "Please tell me it's cool."
    s "It’s {i}cool,{/i} Ami. Don’t worry."
    s "You have, uhh...a lot more manga than I expected, though."

    scene firstamidorm14
    with dissolve

    a "Well, umm...I guess it might be good that...you've forgotten how much you've bought for me?"
    a "Which isn't to say that {i}I{/i} haven't bought any for myself, but...most of it is from you."
    a "But like, the entire bottom row next to the Sailor Moon poster is all stuff I’ve bought with my own money! So you should...be pretty impressed about that!"
    s "Why exactly would I be impressed about your...ability to purchase books?"

    scene firstamidorm15
    with dissolve

    a "You should be impressed because I’m responsible now! And I know how to manage my money!"
    s "That’s great and all, but...where is that money even coming from? Because I don’t give you an allowance."

    scene firstamidorm16
    with dissolve

    a "I’m sorry, Sensei, but I’m afraid that information is classified."
    s "What? Why?"
    a "I can tell you if you really want. But then I'll have to kill you."
    s "Just what the hell are you doing in your free time, Ami?"

    scene firstamidorm13
    with dissolve

    a "Nothing bad, I promise. You don’t have anything to worry about."
    s "You realize that using that line normally just makes people worry even more, right?"
    a "Maybe I...{i}want{/i} you to worry about me then?"
    s "Nah. You're old enough to make your own decisions. Probably."

    scene firstamidorm17
    with dissolve

    a "I am?"
    s "Sure. Why not?"
    a "So...if I find a stray cat on the side of the road and want to take it home to live with us, I can?"
    s "Well, no. Because that impacts me directly since it is {i}my{/i} house. But if you want to take it here, feel free."
    s "Not that I imagine the dorms allow you to keep pets, but yeah."

    scene firstamidorm13
    with dissolve

    a "Are you sure, Sensei? What if I let you pick the name?"
    s "Do you really think something like that would sway me into letting you have a pet?"
    a "No. But what do I have to lose beside a cat I don't even have yet?"
    s "..."
    a "..."

    "It's times like this that call for the cop-out answer every legal guardian keeps hidden in their back pocket at all times."

    s "I’ll think about it."

    scene firstamidorm18
    with dissolve

    a "Yay!"
    a "I promise to help take care of it if you let me get one, okay?"
    s "{i}Help?{/i} You wouldn't be handling {i}all{/i} of its care?"

    scene firstamidorm17
    with dissolve

    a "All of it? No. I still have school. What if something happened to it while I was gone?"
    s "Ami, I am your teacher. I literally walk {i}with{/i} you to school."
    a "That's true. But with how much you've been slacking off lately, do you really {i}have{/i} to even come anymore?"
    s "You know, that's a fair response. Good job."

    scene firstamidorm13
    with dissolve

    a "So I can get a cat?!"
    s "No."

    scene firstamidorm19
    with dissolve

    a "Why do you hate me so much?!"
    s "I don't hate you. I just think that sometimes, you forget how hard my job can be."
    s "And even if you {i}are{/i} responsible for your age, you're still not at my level yet. You have a little while to go before I let you get some sort of pet."

    scene firstamidorm20
    with dissolve

    a "Yeah. I can only imagine how hard it must be to have a bunch of girls who do nothing but love you and try to gain your approval all day."
    s "Hey. That comes with its own set of difficulties."
    a "Uh-huh...I’m sure it does, Sensei..."

    scene black
    with dissolve2

    if bonus == True:
        "Eventually, Maya returns and the time comes for me to head out so the two of them can study for whatever standardized tests are coming up soon."
        "The thought of staying around to help them with that crosses my mind for a brief moment but, once I really think about it, I'm not even sure if I'd be of any help."
        "It's been a long time since I've brushed up on all things academic and I have no idea if what little knowledge I {i}do{/i} still possess is even relevant anymore."
        "As such, I leave the two of them behind and set out toward home, hoping that my decision doesn't cause the two of them to flunk out of school and ruin their lives."
        "If it does, though, at least Ami will finally have the time to take care of a cat."
    else:
        "I try to Naruto run out of the room, but my arms wind up hitting the door frame and it stings really badly."
        "I hope I don't get a bruise. I have always bruised easily. My mom said I was kind of like a banana."
        "I miss her a lot sometimes."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidorm5 = True
    stop music fadeout 3.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}You can now spend time with her in her dorm room!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label amidorm10:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
...
```