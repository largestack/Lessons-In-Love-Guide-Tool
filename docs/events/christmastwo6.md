# Tokimeki Labyrinth (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Everything Evil](./christmastwo5.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo6
* Group: Main
* Triggered by label: christmastwo5
* Chain sources: christmastwo5
* Chain sources path: christmastwo5

## Official wiki page

[Tokimeki Labyrinth](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo6&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo6:
    scene christmashome1
    with dissolve2
    play music "christmasyay.mp3"

    a "Oh, good! You’re home. "
    a "I was starting to think you secretly hated me and were just never coming back."
    s "You think that every time I get up to go to the bathroom."
    ay "Welcome home, Sensei! I tried to put up mistletoe so we could kiss and no one would be allowed to get mad, but Ami took it down."

    scene christmashome2
    with dissolve

    a "You taped it to your forehead! Of course I took it down!"
    m "What’s wrong with {i}you?{/i}"
    s "Me? What do you mean?"
    m "You look...bad."
    s "Thank you, Maya. You really have a way with words sometimes."
    m "You know what I mean."

    "Do I really seem so off that even Maya is able to pick up on it?"
    "I figured the walk home would be more than enough to clear my head, but...I guess not."
    "Maybe it’s just the weather again?"

    if bonus == True:
        "That’s sure as hell a better scapegoat than the probability of me molesting a girl only to be immediately forgiven by her and then...given a gift?"
        "It’s weird to say this, but I kind of wish Molly was a little more torn up about this than she is. "
        "At least that would justify all of the...{i}feelings{/i} I’ve had since Halloween."
        "Feelings are annoying. And I’m annoyed that they haven’t started hiding again yet."

    s "I’m fine. What are all of you up to? I’m not really sure what a pre-Christmas party Christmas party consists of."

    scene christmashome3
    with dissolve

    a "Just watching movies and eating a bunch of cakes Ayane brought over. There’s some left on the counter if you want any."
    s "No thanks. I’m probably just going to go to sleep early tonight."

    scene christmashome4
    with dissolve

    a "What?! No! Why?"
    ay "Are you so excited for the real party that you don’t want the {i}pre{/i}-party to spoil it?"
    sa "I...didn’t think you were looking forward to it that much, Sensei..."

    scene christmashome5
    with dissolve

    sa "Oh! Um...before I forget...my mom wanted me to ask if...you could come help decorate the bar tomorrow morning..."
    s "Why? So she can have something to stare at when the place is inevitably dead all night?"
    m "Brutal."
    sa "They’re...having a Christmas party...and she actually expects it to be busy..."
    s "Well good for her for never giving up hope."
    s "Now, if you’ll please excuse me-"

    scene christmashome6
    with dissolve

    a "No! You really can’t leave yet! Not until Niki shows up!"
    s "Wait, Niki is coming? Why?"

    scene christmashome7
    with dissolve

    a "Well...no. But she’s performing a new Christmas song for a variety show tonight and you have to be here for it! "
    s "But I don’t even really like Niki’s music. It’s too...pink."

    scene christmashome8
    with dissolve

    a "I don’t care how much I love you. In this house, we treat Niki Nakayama with respect. "
    a "Especially now that I’ve been accepted as her honorary little sister."
    m "Oh, wonderful. Does this mean she’s gotten rid of her other one? Because that would confirm once and for all that Christmas miracles {i}are{/i} real."

    scene christmashome9
    with dissolve

    a "Oh...right. Sorry, Maya. I know you get all grumpy whenever anything even remotely related to Noriko comes up."
    m "I don’t get {i}grumpy{/i}. I get murderous. "
    m "You’re not giving my hatred enough credit."
    a "My mistake..."
    ay "I think Niki’s going on soon, Sensei. So if you really {i}are{/i} tired and aren’t just trying to get away from a bunch of people who love you very much, you won’t have to wait around for long."
    ay "{i}Also{/i}, if you just happen to find the mistletoe {i}that I hid in the medicine cabinet{/i} we can kill a few minutes by kissing in front of everyone!"
    sa "I...feel the need to...tell you that I don’t love-"
    ni "{i}Hi, everyone! Thank you all so much for coming out to see me on this very special holiday!{/i}"

    scene christmashome10
    with dissolve

    a "Ah! My queen! She speaks!"
    a "Everyone shut up and gather around the TV!"

    scene black
    with dissolve2

    "Just as Ami asks, everyone directs their attention to the front of the room, but none do so as enthusiastically as she does."
    "I think it’s a little weird how obsessed with my ex-girlfriend my [niece] is, but it’s not like she actively chose to be obsessed with her for that reason."
    "And it’s not like I can expect her to stop now that-"

    a "Sensei! Stop thinking! Niki is talking!"

    scene christmashome11
    with dissolve2

    s "How could you hear me thinking?"
    sa "Wow...she...really does look like Noriko..."
    a "Oh, right! You listen to like...metal and stuff. Right, Sana?"
    sa "Yeah...I don’t know if...I’ve ever heard Niki’s music before."
    a "I’m sure you’ll love it. She’s super talented and super pretty and super nice and-"
    ay "Are you sure you don’t want to get a little closer, Sensei?"
    s "No thanks. I’ve seen Niki up close plenty of times."
    ay "Oh, no. I meant to me."
    ay "No one’s paying attention."
    m "I’m still here..."
    ay "Okay. No one except {i}Maya{/i} is paying attention. And she {i}definitely doesn’t like you{/i}, so she won’t care at all."
    a "And super funny and super awesome and-"

    stop music fadeout 15.0

    ni "{i}Before I start singing...I just want you all to know that...you’re the reason I can do this.{/i}"
    ni "{i}You’re what gives me the courage I never had when I was younger! And I think that you should have courage too!{/i}"
    ni "{i}So please, enjoy this new song!{/i}"
    ni "{i}Even if you’re one of those people who sometimes has a hard time enjoying anything.{/i}"
    ni "{i}It might come as a little bit of a surprise, but I used to be one of those people.{/i}"
    ni "{i}You’re never alone! Because you’ll always have me!{/i}"
    ni "{i}And I’m never alone because I’ll always have you!{/i}"
    ni "{i}Miracles are real!{/i}"
    ni "{i}Please enjoy! Tokimeki Labyrinth!{/i}"

    play music "tokimekilabyrinth.mp3"

    a "Ahhhhhhhhhhhhh! Niki!! I love you!"

    scene black
    with dissolve2

    "{i}Meanwhile...{/i}"
    "........."
    "......"
    "..."

    scene christmashome12
    with dissolve2

    if bonus == True:
        ki "Noriko, I know you’ve probably heard this enough by now, but I really want your sister to just fucking go to town on me."
        n "Is this just what you’re going to do from now on? Just constantly tell me about all of the people you want to fuck you?"
        ki "Hey, don’t blame me for everyone else being like, crazy attractive and shit."
        ki "I want you to fuck me too, but it’s not like I’m going to beg or anything."
    else:
        ki "Noriko, I know you’ve probably heard this enough by now, but your sister looks like she can carry a large amount of bagels very easily."

    n "God! Fuck! Why does Nee-chan have to be so fucking perfect?! How do I compete with that?!"

    scene christmashome13
    with dissolve

    n "What if Sensei’s watching this right now?! What if he’s falling in love again as we speak?!"

    if bonus == True:
        ki "If Sensei is watching this, it’s probably safe to assume he’s either: A) masturbating. Or B) fingering one of our classmates."
        ki "Thinking about it is just going to drive you crazy."
        n "How will hearing those options help?!"
    else:
        ki "If Sensei is watching this, it means he's not watching Seinfeld. That doesn't seem possible"
        n "Kirin, shut the fuck up about Seinfeld!"

    scene christmashome14
    with dissolve

    ki "Hey, why are you yelling at me?! I just wanted to watch your hot sister sing a Christmas song and now it’s suddenly counseling hour."
    n "Ugh, I don’t know. I’m just really nervous about tomorrow."

    scene christmashome15
    with dissolve

    ki "Why? You’re not even coming."
    n "I’m not {i}completely{/i} ditching the party. Didn’t I tell you I still planned on dropping by to give Sensei his present?"
    ki "Probably, but it’s such a boring present that I must have just forgotten that conversation ever happened."

    scene christmashome16
    with dissolve

    n "It’s not boring! It has a load of sentimental value and the potential to change our relationship forever!"

    if bonus == True:
        ki "Yeah, yeah, whatever. If I were you, I’d just give him a handjob. He’d probably like that more."
    else:
        ki "Yeah, yeah, whatever. If I were you, I’d just give him a bunch of animal horns."

    scene christmashome12
    with dissolve

    n "Ugh. You’re such a fucking horny bitch."
    ki "Aww, thank you. That’s so sweet."
    n "..."
    ki "..."
    n "FUCK! WHY IS SHE SO PERFECT?!"

    scene black
    with dissolve2

    "{i}Meanwhile, underneath where we just were...{/i}"
    "........."
    "......"
    "..."

    scene christmashome17
    with dissolve2

    if bonus == False:
        f "And that's how I figured out how to levitate bottles of green tea."

    o "Oh, I forgot to ask- are we still going shopping before the party tomorrow? I still have to get Nodoka a present."

    scene christmashome18
    with dissolve

    r "Man, you got so lucky with your Secret Santa draw! I would have loved to get Futaba or Nodoka."
    r "Like, what the hell am I supposed to buy for Yasu? A hair brush?"
    f "I picked up my present on the way home today, but I’ll still come to the mall with you guys if you want me to."

    scene christmashome19
    with dissolve

    r "Dude, why wouldn’t we want you to? You’re part of the group. We love having you around."
    f "Just...so you two could maybe...be alone?"

    scene christmashome20
    with dissolve

    r "Oh, Otoha and I are taking it slow. We really only hold hands and cuddle and stuff."
    r "Alone time is for more serious couples who do serious stuff together. Right, Otoha?"
    o "Uhh...right. Hahaha..."

    scene christmashome21
    with dissolve

    f "Well, since we’ll probably be gone all day tomorrow, I’ll just call my parents and wish them a merry Christmas now. I think they should still be awake."
    r "Tell them I said hi! And that I love them! And that you are still somehow growing in the chest region despite already being miles ahead of everyone!"
    f "I’ll...make sure to do that, Rin..."

    scene christmashome22
    with dissolve

    r "Oh! And tell them I won’t mind if they decide to buy me a Christmas present this year!"
    r "I know they didn’t last year, so if you could {i}really{/i} just hammer in the fact that we’re basically sisters, it would be rad!"
    f "I’ll...make sure to do that as well, Rin..."

    scene christmashome23
    with fade

    r "Hah..."
    r "You’re warm."
    o "I think I feel...pretty normal. Maybe you’re just cold?"

    scene christmashome24
    with dissolve

    r "Maybe."
    o "..."
    r "..."
    r "You’re blushing."

    scene christmashome25
    with dissolve

    o "Is there a problem with blushing now?"
    r "No. I just thought you looked cute."

    scene christmashome26
    with dissolve

    o "Do you...not {i}always{/i} think I’m cute?"
    r "Of course I think you’re always cute. I just also think there are times where you’re extra cute."
    r "Like right now."

    scene christmashome27
    with dissolve

    o "..."
    r "..."

    scene christmashome28
    with dissolve

    o "..."
    r "..."

    scene christmashome29
    with dissolve

    o "..."
    r "..."

    scene christmashome30
    with dissolve

    o "Hah..."
    r "What? Are you tired or-"

    scene christmashome31
    with dissolve

    r "Mm!"
    o "Mn...chu..."
    r "..."
    o "Mm...nn...mm..."

    scene christmashome32
    with dissolve

    o "Mnch...mmm...mmn~"
    r "Chu...ahm...hah.......ah~"

    scene christmashome33
    with dissolve

    r "Mm...mm! Hah......ahn..."
    o "Mlm...unh...mnn.......mmmm~"

    scene christmashome34
    with dissolve

    o "Hah......ah..."
    r "Well...that was...unexpected."
    o "..."
    r "..."

    scene christmashome35
    with dissolve

    o "One more time?"
    r "Yes, please."

    scene christmashome36
    with fade

    "{i}Several minutes later...{/i}"

    play sound "dooropen.mp3"
    scene christmashome37
    with dissolve

    f "Hah...sorry about that. The conversation lasted a little longer than expected."

    scene christmashome38
    with dissolve

    f "So, what time tomorrow were we..."
    r "Mm~ Mmn...Otoha..."
    o "Chu...mnf...mm~"
    f "..."

    scene christmashome39
    with dissolve

    f "{i}*Ahem*{/i}"
    f "Oh no. I seem to have forgotten to call my aunt as well. Please excuse me for...a longer amount of time."

    play sound "dooropen.mp3"
    scene christmashome36
    with dissolve

    r "Ahm...mmm...mm!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene christmashome40
    with dissolve2

    a "WAAAAAAAAH! NIKI! YOU’RE THE ONLY PERSON WHO UNDERSTANDS ME!"
    sa "I...um..."
    sa "Didn’t really like the song, but...I’m happy you...found someone you like so much..."

    scene christmashome41
    with dissolve

    m "So, now that you’ve been forced to sit through whatever that was, are you still calling it a night?"
    ay "Are you trying to get him to stay up later because you’ll {i}miss{/i} him, Maya?"
    m "No. I’m just smart enough to know that once he’s out of the picture, everyone else will inevitably want to go to sleep as well. And I am very tired."
    s "Or maybe...you’re just actually excited for the Christmas party tomorrow and don’t want to wait any longer."

    scene christmashome42
    with dissolve

    m "Yup. You got me. Goodnight, everyone. I am so excited to be packed into a small, hot room with nineteen other girls tomorrow night."

    scene black
    with dissolve2

    "Not seeing much reason to stay awake, I also decide to head to bed."

    if bonus == True:
        "This time, however, I decide to lock my door so Ayane can’t mount me in the middle of the night."
        "I’m not really sure how tomorrow’s party will compare to last year’s (If...you can even call it {i}last{/i} year? How does that work exactly?) but, if there is anything I {i}do{/i} know...it’s that it’s going to be lively."
        "The class size has nearly doubled and, unless we have some new venue planned out that I haven’t heard of, I think it’s pretty safe to assume that chaos will ensue and..."

        s "...Fuck."

        "I forgot to buy Miku a Christmas present..."

        s "..."

        "Oh well."
        "I’ll just buy one on the way back from Sara’s tomorrow."
    else:
        "I sure hope Santa Claus brings me lots of presents tomorrow."

    $ renpy.end_replay()
    $ christmastwo6 = True
    $ ayane_love += 1
    $ ami_love += 1
    $ sana_love += 1
    $ maya_love += 1
    stop music fadeout 7.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 6
    hide friday onlayer date
    show saturday onlayer date

    jump saralust20intro

label christmastwo7:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
mo "Then we were both mind controlled by Alliance shadow priests who made the evil hug happen."

    s "That’s essentially the complete opposite of how things played out in my head."

    scene dodgingsnowflakes35
    with dissolve

    mo "You went for the worst case scenario, and I went for the best."

    if bonus == True:
        mo "Besides, even if I wasn’t conscious for the whole ordeal, I wouldn’t hate you for just letting one out on my cosplay."
        s "You probably should, Molly. That's not really something you should be okay with."
        mo "I believe you’re forgetting how much of a degenerate I am, Sir. And how you’ve already seen me going to town on myself in the past."
        mo "I don’t really mind having {i}that{/i} sort of relationship with you. "
    else:
        mo "Besides, even if I wasn’t conscious for the whole ordeal, I'm pretty much fine with you hugging me whenever you want."

    scene dodgingsnowflakes36
    with dissolve

    mo "Well...by {i}that{/i}, I don’t mean that I’m ready to start...you know, touching {i}each other{/i}...I think that’s something I should clarify."
    mo "I just mean that I...don’t really mind you knowing me on a more personal level..."
    mo "For whatever reason, you’re attracted enough to me to [masturbate] in the same room...and I’m attracted to you as well..."
    mo "So if we both happen to be in the same place at the same time and...are both feeling the need to...you know...without touching each other..."
    s "Molly, what exactly are you trying to propose right now? Because, whatever it is, it’s weird."

    scene dodgingsnowflakes37
    with dissolve

    mo "I have absolutely no idea, Sir. I’m simply recalling several mutual masturbation scenes in games I have played and trying to apply them to real life."
    s "This is absolutely not how I thought this conversation was going to end up."

    scene dodgingsnowflakes38
    with dissolve

    mo "I know, but..."
    mo "Can you please be my friend again, Sir?"

    if bonus == True:
        mo "And, if you’re going to ejaculate on me, confirm that I am awake first? "

    s "..."

    if bonus == True:
        mo "Or just...don’t ejaculate on me at all if you think that’s weird."
        mo "After all, we have no idea what {i}really{/i} happened and it could have just been some sort of...accident?"
        s "New idea. How about we just...try and put this behind us and not make any further plans about when and where it’s okay to orgasm?"
        mo "Okay, Sir. That sounds fine to me."
        mo "Also, and forgive me if I’m asking this at an inappropriate time, but do you {i}always{/i}...you know..."
        mo "Let out {i}that much?{/i}"
        s "..."
        mo "It just...seemed like a lot..."
        s "..."
    else:
        mo "..."

    mo "Nevermind. Forget I asked that. "

    scene dodgingsnowflakes39
    with dissolve

    mo "Oh! And also, hypothetically, if you were going to ask for something for Christmas, what would it be?"
    s "Not a wardrobe."
    mo "I...uhh...okay?"
    s "Are you the one who got me for Secret Santa this year, Molly?"
    mo "Of course not. This is entirely hypothetical. And, on a completely unrelated note, it is extremely convenient that we were able to have this conversation {i}before{/i} the gift exchange."

    if bonus == True:
        mo "It would have been extremely awkward for me to give you a present without clearing up the great ejaculation mystery first. Hypothetically, of course."
        s "I have several comments on those last couple sentences, but I’m going to hold them to myself and just tell you to {i}hypothetically{/i} get me a gift card or something."
        mo "A gift card, Sir? Is that really what you’d want?"
        s "There aren’t many things I want. So either do that or just...get me whatever you think I’d like."
        mo "Hypothetically, you mean."
        s "Right..."
        s "Hypothetically."
    else:
        s "Yes, because now I can show you all three hundred pages of my Christmas list."
        mo "That is so many pages."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I don’t stick around much longer than that because, despite the conversation actually managing to smooth things over to some extent, I still can’t help but feel uncomfortable around Molly."
    "I’m pretty sure she notices this, too, as she slides closer to the edge of her bench and further away from me."
    "It’s no longer just inches between us."
    "It still feels like miles, though."

    $ renpy.end_replay()
    $ molly_love += 5
    $ mollysad = False
    $ christmastwo5 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}I wonder if you’ll ever find out what really happened on Halloween!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo6
...
```