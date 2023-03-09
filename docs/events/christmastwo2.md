# The Reliable and Totally Legitimate Princess Imani
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo2&go=Go)


Part of event chain [Three Amigos](./christmastwo1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo2
* Group: Main
* Triggered by label: christmastwo1

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo2:
    scene christmastwomaid1
    with dissolve2
    play music "maidcafe.mp3"

    ima "I’ve gotta admit, this is not what I was expecting for a first night out with my new amigos, but I am all about it."
    ima "I’ve never been to a maid cafe before so I’m kinda like, fighting off the culture shock right now, I guess."
    s "Your surname is Imai. Aren’t you half Japanese?"

    scene christmastwomaid2
    with dissolve

    ima "How can you be so sure that’s my real last name and that I’m not just trying to trick you into thinking I’m amigo material?"
    s "I can’t. I was just asking a question."

    scene christmastwomaid3
    with dissolve

    ima "Well, fine! If you’re going to be so pushy about it, yes! I am half Japanese!"
    ima "I’ve returned home because I’m actually a princess and I’m here to collect my inheritance."
    s "Right. So then why are you working as a teacher?"

    scene christmastwomaid4
    with dissolve

    ima "Where are {i}you{/i} from Wakana?"
    s "You really need to stop dodging my questions by asking questions to someone else. It has happened two times already today and I would be lying if I said I wasn’t annoyed."
    w "I’m from...my apartment."
    ima "Cool cool cool cool cool cool cool. And where did you get that tea? No one’s come to the table yet."
    w "I texted my significant other and had her prepare it for me beforehand. The walk here was quite cold and I didn’t want to just sit around waiting for tea to brew while freezing to death."

    scene christmastwomaid5
    with dissolve

    w "Non-literal death, of course. I’m contractually obligated to say that now so no one thinks I’m going to kill myself. "
    s "Well, thank you for offering some to us, Wakana."
    w "Over my non-literally dead body. Get your own."
    ima "So, you come here often, Sensei?"
    s "Are you hitting on me right now?"
    ima "Do you {i}want{/i} me to be hitting on you right now?"
    s "I don’t {i}not{/i} want you to be hitting on me right now."
    ima "Oh, come on. You mean to tell me that one of the like, seven dudes in Kumon-mi is single and doesn’t have anyone who’d get pissed off at him for flirting with some foreign girl?"
    s "I mean, the first part of that is true, but not so much the second. Also, there are a lot more than seven men left in this city."
    ima "Well make sure to have some of ‘em sign up on Tinder at your next super-secret man meeting because I haven’t had anyone to swipe for in ages now."

    scene christmastwomaid6
    with dissolve

    if bonus == True:
        w "And to think that just an hour ago you were accusing the two of {i}us{/i} of having a sexual relationship..."
        u "A what now?"
    else:
        w "You know, I've thought about it, and I think Osako would like Australian Shepherds the most."

    os "Uhh...Wakana?"

    "Oh, comedic timing. You never let me down."

    scene christmastwomaid7
    with dissolve

    w "Hello, my precious and forgiving kitten with short term memory loss. I love you."

    if bonus == False:
        "I wonder if Wakana is only so bad with Osako-related dog knowledge because she has been calling her a kitten for so long. That seems like a plausible thing to think."

    os "How are you feeling? Do you need anything? Is the tea good? We’re out of the kind you like, so I had to use one you’ve never had before and-"

    scene christmastwomaid8
    with dissolve

    w "I’m fine, my darling. I do not need anything. The tea is nice."
    ima "Awwwwww, my best friend is so cute when she’s in love."

    scene christmastwomaid9
    with dissolve

    w "{i}Best{/i} friend? We’ve known each other for roughly one hour."
    ima "And it’s been one of the greatest hours of my life."
    u "Umm...who might you be, Princess?"

    scene christmastwomaid10
    with dissolve

    ima "Ha! I told you I was a princess! And you didn’t believe me!"
    s "It’s just what the maids call their female customers. Women are princesses and men are masters. "
    s "Also, you respond to Uta-chan when she speaks to you, damn it."

    scene christmastwomaid11
    with dissolve

    u "Th-Thank you, Master..."
    os "Hey, can we talk in the hall for a minute? "
    w "Hm? Is something wrong?"
    os "Well, not {i}wrong{/i}...just..."
    os "Can you just come with me for a second?"

    scene christmastwomaid12
    with dissolve

    w "Yes. But I am bringing my tea and you can not stop me."
    os "That’s fine..."
    w "I’ll be back momentarily, but chances are you won’t even notice I’m gone."
    s "That’s not another jab at me for never visiting you, is it?"
    w "{i}You won’t even notice I’m gone.{/i}"

    scene christmastwomaid13
    with dissolve

    "Wakana and Osako step out into the hallway and, in other news, Uta probably thinks I have a tenth girlfriend now or something."

    u "So, uhh...who are you? I thought I overheard something about Tinder?"
    u "Are you two...you know..."
    ima "Know what?"
    ima "Please tell me in vivid detail so I can say no and then laugh at you and make you feel embarrassed."
    s "It’s not a date, Uta-chan."

    scene christmastwomaid14
    with dissolve

    a "Of course it’s not a date, Uta-chan. Sensei would never date anyone ever because he knows it would make me so sad that I might accidentally tie him up and not let him leave home ever again."
    ima "Yeah, I hate when I get sad and accidentally do that."
    s "Hey, Ami. You’re working late tonight."

    scene christmastwomaid15
    with dissolve

    a "I’m picking up extra hours so I can buy presents for all of my friends since my uncle doesn’t give me an allowance anymore."
    a "Also, who is this girl and why are you with her?"
    s "This is Imani. She was filling in for Wakana while she was in the hospital."
    ima "That’s right. "
    ima "Oh, and I’m also your new student teacher."

    scene christmastwomaid16
    with dissolve

    s "Wait, what?"
    ima "Surprise!"
    ima "I’ve known since Monday. This just seemed like a good spot to break the news."
    ima "I was holding it in so I could find the best chance to use it for dramatic effect. "
    s "Well, you...certainly picked a time, alright."

    "Is Imani really going to be a student teacher for my class?"
    "What...exactly is that going to mean for my “methods” of just having everyone do whatever they want all the time?"
    "Don’t tell me she’s going to want me to actually {i}teach{/i} now, is she?"

    u "Wait, why are we getting a student teacher? None of the other classes have one."

    scene christmastwomaid17
    with dissolve

    ima "You know, it might be hard to believe since you seem like a really smart girl who’s benefited greatly from my new Senpai’s teachings, but the school just thinks he kind of sucks for some reason."
    s "Hey. That’s not a fair evaluation of my character."

    scene christmastwomaid18
    with dissolve

    u "No, it kind of is."
    a "Also, Uta is nowhere close to really smart, so I hope your teaching is a little better than your judgement or it will be like nothing’s changed at all."

    scene christmastwomaid19
    with dissolve

    u "Ami-chan, why must you hurt me so? To be called dumb by a fellow dummy makes me feel even...dumber. "
    u "Wait, is dumber even a word? Or is it more dumb?"
    ima "Oooookay! So maybe you’re not that smart! But that’s just all the more reason to rely on me!"
    a "But what if we don’t want to rely on you?"

    scene christmastwomaid20
    with dissolve

    ima "Hm? What do you mean by that?"
    a "What I mean is that our class is kind of...different."
    a "Sensei has a very...unique way of teaching, and having another teacher around, {size=-15}especially an attractive one,{/size} just doesn’t sound like it will work."

    scene christmastwomaid21
    with dissolve

    ima "Hey, I get it. Change is scary and blah blah blah listen to me, I’m an adult. "
    ima "I’m not going to just waltz into class tomorrow and-"
    s "Wait, tomorrow?"
    ima "Yeah, I start tomorrow. "
    s "But Wakana doesn’t come back until Monday."
    ima "Well then I guess her students are getting a day off. Can I finish now?"
    ima "What I was saying is that I’m not going to just waltz into class tomorrow and change the way you guys have been doing stuff all year."
    ima "I’ll just be around to help anyone who needs it or wants it while, at the same time, keeping Sensei out of trouble."

    scene christmastwomaid22
    with dissolve

    u "What’s Makoto gonna do then? Those are like, all of her favorite things."
    a "Hopefully, she’ll just die. "
    s "Ami, come on."
    a "Sensei, I don’t want a student teacher. I want you and only you. Forever and ever and ever and ever and ever and-"
    u "We get it, Ami. You love your [uncle]."

    scene christmastwomaid23
    with dissolve

    a "And ever and ever and ever and-"

    if bonus == True:
        ima "Man, you get to teach your {i}niece{/i}? That’s awesome. I wish I got to teach my family."
    else:
        ima "Oh shit, I had a cousin who used to call me her little pogchamp! Do you guys eat popsicles together?!"

    scene christmastwomaid24
    with dissolve

    u "Is your family in Japan too, Princess Imani?"
    ima "Nah, they’re still over in Ghana doing Ghana stuff. How about you, Uta-chan? I’d say you look like you come from a big family, but I’ve already been wrong about you once soooo-"

    "Oh, good. Here we go."

    u "Just my mom and dad and my brother, but my brother is in jail. I had a grandpa too but he died of terminal cancer."

    scene christmastwomaid25
    with dissolve

    ima "Man, maid cafes are fucking dope. Where else will people just dump their traumas all over me before I can even order food?"
    s "Honestly? Pretty much everywhere around here. I’m learning that it’s kind of just a thing people do in Kumon-mi."
    u "You think the brave and adorable Uta-chan would be traumatized by something like watching a loved one slowly fade away into nothingness?"
    s "That seems like a pretty fair thing to be traumatized by, Uta-chan."

    scene christmastwomaid26
    with dissolve

    u "Tsk tsk tsk. Oh, Master. You don’t know the first thing about Uta-chan, do you?"
    s "I know that you lure people into karaoke booths in order to prey upon them."

    scene christmastwomaid27
    with dissolve

    u "Th-th-th-th-that wasn’t Uta-chan! That was normal Uta! And she wasn’t preying on anybody! She just got caught in the moment! "
    a "And ever and ever and ever and-"

    scene christmastwomaid28
    with dissolve

    a "I suddenly feel like I’m supposed to be suspicious of something."
    ima "Well, looks to me like {i}somebody{/i} must have a {i}pretty{/i} lively classroom if these two girls are a sign of things to come."
    s "Honestly, these two are on the easier side."

    scene christmastwomaid29
    with dissolve

    u "Rude. I'm not easy at all."
    s "Not like that, Uta-chan."
    ima "Well, hey. I’m up for pretty much whatever. It’s not like I’ve got anything else going on in Kumon-mi anyway."
    ima "I’m looking forward to working with you, Sensei. "
    s "Imani, you’re probably going to question what I mean by this, but I just need you to go along with it when I say that there will be minimal work involved."
    ima "You know, I think I’m starting to figure out why they shoved me in your class instead of somebody else’s."
    s "I’m sure you’ll confirm that belief on your first full day of class. "
    s "But, in the meantime, we should probably order something since we’ve now been here for...quite a while."

    scene christmastwomaid30
    with dissolve

    u "Oh! Umm...Master? Would it be okay if I pulled you aside for a second? I just had a quick little question for you and stuff."
    s "Sure, but we should probably try to stay away from wherever Osako and Wakana went. They’ve been gone for a long time and I think they might be making out or something."

    scene black
    with dissolve2

    "I leave the table and Ami immediately begins interrogating Imani about all sorts of topics that I’m sure won’t make her feel strange or unwelcome at all."
    "That’s not me being sarcastic either. I’ve only known her for a short period of time, but I feel like it’s very hard to throw Imani off of her game."
    "And while having her around {i}all{/i} the time sounds like it could become problematic in a...variety of ways, I’m not going to immediately just write it off."
    "For all I know, the two of us could get along really well."

    if bonus == True:
        "Also, she didn’t seem entirely opposed to the threesome idea earlier, and I see that as a huge plus."

    scene christmastwomaid31
    with dissolve2

    u "..."
    s "So...what’s up? What did you need to ask me about?"
    u "Well, I..."
    u "I was just wondering if...tomorrow after school..."
    u "You could maybe like..."
    u "Come over?"
    s "..."

    "For entirely unknown reasons, it suddenly becomes harder to stand."

    s "I will go anywhere for you, Uta-chan."

    scene christmastwomaid32
    with dissolve

    u "Not...for Uta-chan. "
    u "For normal Uta."
    s "Normal Uta?"
    u "Yeah..."
    s "You...do realize how this sounds, right?"
    u "What if I told you...I already called my parents?"
    s "Well, I’d first confirm that you didn’t tell them who I am or where I live. But after that, I’d-"

    scene christmastwomaid33
    with dissolve

    u "Uhh- actually! I forgot to mention that Io is going to be there too. And that...well, she’s the one who wanted me to ask you to come over in the first place."
    u "I just...went about asking in a really weird way, I guess. Hahaha..."

    if bonus == True:
        s "Yet again, lured into a false state of arousal by a tiny girl in a maid costume."
    else:
        s "Yeah, you should really focus on improving that part of yourself."

    scene christmastwomaid34
    with dissolve

    u "So...even if it wasn’t Io and it really was just me...you’d come?"
    s "Is that even a question? Of course."

    scene christmastwomaid35
    with dissolve

    u "I see..."
    s "..."
    s "Why are you being so weird all of a sudden?"
    u "Weird in what way?"
    s "Weird in the fact that you’re not mindlessly flirting with me and that you’re blushing like you’ve been in a sauna for three hours."
    u "I guess my face does feel a little hot..."

    scene christmastwomaid36
    with dissolve

    u "B-But that’s just because I {i}wanted{/i} you to think I was embarrassed about asking! I mean, why would I feel nervous about asking you to come over when you’ve been over so many times before?!"
    u "That would be totally weird! And it’s not like I have any intention of letting you put your hands on me or anything!"
    s "Okay, that’s getting back on track. But you still seem a little off and-"

    scene christmastwomaid37
    with dissolve

    u "A-Are you coming or not?! Io made you a Christmas present and it’s taking up too much space in our dorm!"
    s "Space? What space?"
    u "That’s exactly the problem! I had to crawl under a table just to get to my skirt this morning!"
    s "Have you considered, you know, storing your clothes somewhere that isn’t directly on the floor?"

    scene christmastwomaid38
    with dissolve

    u "Nonsense. The floor is where clothes are {i}supposed{/i} to go. If that wasn’t the case, it wouldn’t be so big."
    s "I’ll make sure to drop by, Uta. Whether or not Io is there."

    scene christmastwomaid35
    with dissolve

    u "Cool...yeah."
    u "Io will be really happy."
    s "And you?"

    scene christmastwomaid34
    with dissolve

    u "Me?"
    s "Yeah. You’re the one asking. I’m not just dropping by to make Io happy."
    u "..."
    s "..."

    scene christmastwomaid36
    with dissolve

    u "That’s for me to know and you to find out!"
    s "What?"
    u "I...I don’t know!"
    u "I’ll see you tomorrow!"
    s "..."

    scene black
    with dissolve2

    s "But..."
    s "We still haven’t ordered..."

    $ renpy.end_replay()
    $ uta_love += 1
    $ christmastwo2 = True
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo3

label christmastwo3:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
scene wakanareturns33
    with dissolve

    ima "Maybe some ear plugs so I don’t hear anything when you two start going at it?"

    if bonus == True:
        s "Leaving the office would also suffice, you know."
    else:
        "How does she know I am such a loud hugger?"

    w "Please don’t insinuate that any of what she’s saying bears any ounce of truth whatsoever."
    ima "I can’t leave. What if someone saw me come in here after you two and they think {i}I’m{/i} a part of this secret tryst?"
    s "Wouldn’t leaving before us sort of quell that notion?"

    scene wakanareturns34
    with dissolve

    ima "Nooooo because then they’ll think I’m bad at stuff and that I couldn’t keep up with all of the action! I’m a part of this now!"

    if bonus == True:
        s "Well, either we have a threesome or we all leave this office together and just...go home since it’s already well past school hours."
    else:
        s "I am so confused and scared."

    scene wakanareturns35
    with dissolve

    ima "Hmmmmmmmmmm..."

    if bonus == True:
        w "I don’t believe Osako would take kindly to the idea of a threesome she isn’t involved in."
        s "Would she...take kindly to the idea of one she {i}is{/i} involved in?"
        w "Maybe? I’ve never asked."
    else:
        w "I am realizing now that I have never asked Osako about her favorite breed of dog. I have failed as a significant other."

    scene wakanareturns36
    with dissolve

    ima "Wait! But then what will happen to me?! Three plus one does not equal three! I know this because I am a teacher!"

    if bonus == True:
        w "In lieu of any sexual activities, I propose that the three of us simply leave here together and...find something else to do if we’re not yet done with this...reunion-slash-introduction."
    else:
        w "I do not have any idea what this strange, potentially intoxicated teacher is saying, but I propose that the three of us do a thing."

    scene wakanareturns37
    with dissolve

    w "Does that work for you?"
    s "I mean...I was kind of planning on just going home, but if you really want to keep hanging out, I guess I can do that instead."
    w "How kind of you, making time for your recently near-departed friend."

    if bonus == True:
        ima "I’m game! Hanging out normally sounds a lot less...sticky than a threesome, too."
        w "My only condition is that any and all discussions about {i}threesomes{/i} cease immediately, as I was already intending to visit Osako at the maid cafe."
        w "I’ve just added the two of you to the plan as well because...friendship."
    else:
        ima "I’m game! I love doing things!"

    scene wakanareturns38
    with dissolve

    ima "I’m gonna cry. It’s been years since I’ve gone out with coworkers."
    w "If you cry, I’m rescinding your invitation and cancelling our friendship indefinitely."
    ima "I’ll...{i}*sniff*{/i}"
    ima "I’ll do my best..."

    scene black
    with dissolve2

    "Somehow or another, I wind up getting dragged into a get together with Wakana and Imani."
    "Well, I guess dragged isn’t really an accurate term since I’m not really {i}against{/i} the idea of spending time with the two of them."

    if bonus == True:
        "I would have just much preferred the original idea since the new one doesn’t contain group sex."
        "But alas, those are thoughts I can not allow myself to be burdened with in the presence of someone who could eliminate me at the drop of a hat."

    stop music fadeout 10.0

    "Actually, now that she’s in my mind- I wonder how Osako’s doing with the whole Wakana situation."
    "I’d decided to stay out of her affairs so she could have time to figure things out with Wakana, but..."
    "Now that Wakana is doing, at least on a surface level, much better...I wonder if any of those worries I was, well, {i}worried{/i} about have vanished."
    "But just thinking that won’t help."
    "In fact, thinking rarely ever does anything to begin with."
    "I’ll just continue to go with the flow, hang out with a small group of coworkers like a normal functioning adult, and see how things play out from here."
    "Without any interference from me."

    $ renpy.end_replay()
    $ wakana_love += 1
    $ imani_love += 1
    $ christmastwo1 = True

    "{i}Wakana’s affection has increased to [wakana_love]!{/i}"
    "{i}Imani’s affection has increased to [imani_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo2
...
```