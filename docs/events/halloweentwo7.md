# The First Signs of Fraying Threads
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo7&go=Go)


Part of event chain [Porcelain Labyrinth](./halloweentwo6.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo7
* Group: Main
* Triggered by label: halloweentwo6

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo7:
    if amilust20 == True:
        scene cupcaketable1
        with dissolve
        play music "letsfuckingo.mp3"


        "By the time we make it back, Ami still hasn’t fully recovered."

        if bonus == True:
            "I’m hoping that ends soon, though, as her continuing to address herself in third person after disappearing with me will be suspicious for a number of reasons."
            "I don’t think the initial assumption for any of those reasons will be particularly {i}sexual{/i}, though, because...well, a change in speech patterns isn't normally a result of that."
            "But it would be suspicious nonetheless."
            "I’m counting on you, Ami."
        else:
            "It was a really good hug and I probably squeezed her a little too hard."

        a "Guhhhhhhhhhhhhh.............................."
        m "…"
        sa "…"
        ay "You doing okay, Ami?"

        scene cupcaketable2
        with dissolve

        a "Yup! Totally normal Ami here! Nothing to worry about!"

        "Hell yeah. "

        a "Anything...fun happen while we were gone?"

    else:
        scene cupcaketable2
        with dissolve
        play music "letsfuckingo.mp3"

        a "Hey! Sorry we were gone for so long. "
        ay "No need to be sorry! I’m sure the “Hall of many bathrooms” can be a little hard the first few times."
        ay "You’ll get the hang of it one day, Ami."
        a "No, Ayane. "
        a "No I will not."

        "Ami and I make it back to the party after giving up on our search for Noriko and take our places at the “Primarily manga club” table."
        "I’m not really sure how these girls organize their cliques, but that’s what I’m going to call this table until someone gives it a better name."
        "Even if...only two of the girls here are in that club."

        a "So...did anything fun happen while we were gone?"

    scene cupcaketable3
    with dissolve

    m "Fun? No."
    m "But Uta-nyan tried to teach Tsuneyo her flavor beam technique and failed miserably before being summoned over by a bunch of the others to...do something."
    m "I became distracted by cupcakes and stopped paying attention."
    a "That makes sense."
    m "I think it was a game."
    s "It’s rare to see food in front of you that has...yet to be eaten, Maya."

    scene cupcaketable4
    with dissolve

    m "You...You {i}do{/i} know how food works, correct? Eating it is what you are supposed to do."
    s "Yes, Maya. I’m not a fucking idiot. I just meant that you-"
    a "Yes, yes. Maya eats a lot and somehow still manages to stay skinny. We know."

    scene cupcaketable5
    with dissolve

    m "What does my weight have to do with anything? That wasn’t even brought up."
    a "I know. I just get annoyed by how pretty you are sometimes and then my jealousy leaks out without me realizing it."
    m "Oh. Well, thank you. "
    ay "While we’re on the topic of looking pretty, do you notice anything different about Sana, Sensei?"
    s "You mean apart from her gas mask that has now gone missing?"
    sa "My...hair is a little different too, but...I’m sure you didn’t notice..."
    s "Oh. Yeah, not really. "
    s "I always notice when your other eye is showing, though. So that has to be good for something."

    scene cupcaketable6
    with dissolve

    ay "Sensei! Always pretend that you notice when a girl changes her hair, even if you don’t!"
    s "Are you telling me to live a life of lies, Ayane? I would never hide anything from you girls."
    a "You’re literally lying right now. "
    ay "I’m not asking you to {i}lie!{/i} Just to...be a little nicer."
    ay "Sana has now been brave enough to show us her belly {i}twice{/i}! Once during the dorm war and once now!"
    ay "She deserves all of the love and encouragement we have to offer!"
    sa "Ayane...you...don’t have to...say all that..."
    s "Well, it’s definitely true that this “costume” is a bit more revealing than what she normally wears."
    s "I just figured pointing it out would make her embarrassed and cause her to run away and I really don’t want to get caught in the bathroom labyrinth again."

    scene cupcaketable7
    with dissolve

    sa "It’s...actually not as confusing as it seems..."
    sa "You just have to kind of...memorize which directions you went in and...stuff..."
    s "Yes. Because, as we all know, I have the best memory around."
    s "Besides, it’s not like this was a conscious decision, was it? You just raided your mom’s closet and, presumably, chose the weirdest shit you could find."

    scene cupcaketable8
    with dissolve

    sa "Um...yeah..."
    sa "Of course I’d never...put thought into looking like...this..."
    sa "I just felt...obligated to dress up, I guess..."
    ay "Sensei! You’re ruining our chances of ever seeing Sana’s belly again by not validating her!"

    if bonus == True:
        s "Uhh...it’s a good belly?"
    else:
        s "Forget her belly. Her costume in general is just a {i}real{/i} showstopper."

    scene cupcaketable9
    with dissolve

    sa "N-N-N-N-No it’s not! Stop looking!"
    s "I have no idea what I am supposed to be doing right now. "
    m "You are making that quite clear."
    s "Is it your turn to be validated, Maya? "
    s "Will complimenting you now open up more opportunities for you to wear costumes in the future? Or should I just savor this moment while it lasts?"

    scene cupcaketable10
    with dissolve

    m "Complimenting me is literally pointless when I would choose any one of these five cupcakes over you any day of the week."
    a "You can compliment me, Sensei! "

    if amihalloween2win == True:
        s "Was winning the contest earlier not enough for you?"
        a "It’s never enough! Give me more love!"
        a "Give me everything! I want it all!"
        s "Jesus, calm down."

    elif ayanehalloween2win == True:
        ay "Or me! Compliment me!"
        s "I already complimented you earlier when I chose your costume over all of the others."

        if bonus == True:
            ay "True. But after I called the limo for the backseat stuff you requested, you never showed up and it hurt my feelings!"
            s "How would you have even explained-"
        else:
            ay "True. But as I sank my fingernails into the rotting flesh of a body I stored in the backseat of that old Lincoln in the parking lot-"

        s "You know what? Nevermind. I don’t want to know."

    else:
        s "I compliment you like every day. Isn’t that enough?"
        a "Nope."
        ay "You only compliment me every {i}other{/i} day. Can I have one?"
        s "No. The time for compliments is over."

    s "Maya, would you really choose the cupcakes over me?"
    m "Without a second thought."
    s "Really?"
    m "Yes."
    s "Even after-"
    m "Yes."
    s "But-"
    m "Cupcakes."

    scene cupcaketable11
    with dissolve

    a "It’s not like Maya {i}needs{/i} the compliments or anything anyway. She’s not like Sana or Ayane or me."
    m "How am I not like any of you?"
    a "Because you’re confident, obviously."
    m "So is Ayane. You and Sana are the ones with self-esteem issues."
    m "Not that I want to be complimented in the first place. I’m just pointing out the flaws in your logic."

    scene cupcaketable12
    with dissolve

    a "Hah...I know..."
    a "It’s my fault for not believing in myself. It’s just hard when you’ve been pretty much the same way ever since we met."
    a "You’re always so sure of yourself but, like...at the same time, it’s like you don’t even care."
    a "And you don’t do anything to keep it up and it’s just...so natural for you."
    m "Why are you making yourself sound like an undesirable slob? You’re the cutest girl at this table."
    m "No offense to Sana and Ayane."

    scene cupcaketable13
    with dissolve

    ay "None taken!"
    sa "I...think that’s fine, too..."
    a "See, it's hearing that exact sort of thing from you all the time that makes it so hard for me to believe that!"
    ay "Come to think of it, you’ve always been really supportive of Ami, haven’t you?"
    m "Sure. I guess."
    m "I just think she’s cute. Why is this becoming a thing?"
    m "Also, why is the only thing you grabbed off of the buffet table corn? {i}That{/i} is what we should be talking about right now. Not our thoughts on each other's aesthetics."

    "I’ve been all but removed from the conversation."
    "But that’s okay, because I know that any minute now, I’ll be forced to make yet another choice about who I think is prettier."

    scene cupcaketable14
    with dissolve

    a "What do you think, Sensei? Am I cuter than Maya?"

    "See?"

    s "I-"
    m "No. You stay out of this. Why are you even at our table? This is reserved for costumed guests only."
    s "If that’s the case, Sana needs to leave too. That doesn’t count as a real costume if she doesn’t even know what it is."

    if sanahalloween2win == True:
        m "It’s certainly more than {i}no{/i} costume, and that didn’t dissuade you at all from still choosing her as the cutest earlier."
        s "Okay. But it’s still not a costume."
        m "Shut up."

    scene cupcaketable13
    with dissolve

    a "Why {i}have{/i} you always been so supportive of me, Maya?"
    a "Like, you’ve probably called me cute more than Sensei has. And I {i}force{/i} him to do it on a near daily basis."
    s "I’m not being {i}forced{/i} to do anything."
    m "Is everyone just unified in thinking that there needs to be some ulterior motive in me thinking you’re cute? Why is this happening?"

    scene cupcaketable15
    with dissolve

    a "Because it’s annoying hearing that from {i}you!{/i}"
    m "But...why?"
    a "Because I’ve always wanted to be more like you! You’re confident and cool and smart and stylish and pretty!"
    m "Again, Ayane exists-"
    a "Ayane is just confident, smart and...kind of pretty, I guess!"

    scene cupcaketable16
    with dissolve

    ay "Hey! {i}I’m{/i} cool! Sensei thinks I’m cool!"
    s "Oh, good. I still exist after all."

    scene cupcaketable17
    with dissolve

    a "You’re just...I don’t know."
    a "I’m glad you’re so nice to me all the time, but it’s just hard figuring out if it’s {i}real{/i} or not."
    a "So when you’re all like “Oh Ami, you’re the cutest girl at the table” when you’re at the {i}same{/i} table it’s like “Ahhhhhhhhh Mayaaaaaa!!!!” you know?"
    m "Um..."
    m "Not...really? "

    scene cupcaketable18
    with dissolve

    a "Hah...whatever. Forget it. "
    m "…"
    ay "Soooo...Halloween! Right?"
    s "I can’t tell if that exchange was a fight or a bonding experience."
    a "Just ask Maya what she thinks and go with that. You’re just gonna side with her anyway."
    m "Why would Sensei side with me over you in literally any scenario?"

    scene cupcaketable19
    with dissolve

    a "I don’t know, Maya. Why {i}would{/i} he?"
    m "…"
    a "If I’m the perfect [niece] and everything Sensei needs wrapped into one little package, what reason would he have to do something like that?"
    s "Okay. So it’s definitely a fight."
    ay "Ami...All Maya did was compliment you. There’s no reason to get all...like this."
    a "Oh, come on. You know she’s been warming up to him lately. She barely even calls him disgusting anymore."
    m "I literally just said that I would take any one of these five cupcakes over him like two minutes ago."

    if bonus == False:
        m "Besides who cares if I'm secretly in love with him? It's not like it's a big deal or anything. Like, I'm open about it at this point and no one ever even acknolwedges it."

    a "Yeah, you say a lot of things."
    a "And sure, I don’t understand most of them, but I’m not as stupid as you think."

    scene cupcaketable20
    with dissolve

    m "Are you okay?"
    m "I really wasn’t trying to start-"
    a "Blah blah blah Maya is the cutest girl at the table and Ami is just Ami. Let’s move on."
    sa "…"
    ay "Ami..."
    a "That’s my name!"
    s "I’m going to second Maya’s question and ask if you’re okay. You’re acting weird all of a sudden."

    if amilust20 == True and bonus == True:
        "Did I...fuck her so hard that she turned into a different person?"

    a "I’ve just been losing sleep lately. I’m probably cranky."
    s "Is there any reason {i}why?{/i} Or..."
    a "Nope! Just a thing that happens sometimes. "
    a "I wouldn’t worry about it unless I start getting a fever."
    ay "Do you want to lay down? I can ask Geoffrey to get off the phone with the Irish Mafia and set up a futon for you."
    ay "Or you could go back to the main house and use my bed. I don’t really mind."
    s "Can we not just gloss over the Irish Mafia thing?"

    scene cupcaketable21
    with dissolve

    a "Is he really dealing with them again? I thought he moved past that confusing, yet suspiciously depressing and dramatic stage of his life."
    ay "Oh, you know Geoffrey. Always getting up to no good."
    s "What?"

    scene cupcaketable22
    with dissolve

    s "I-"
    m "…"
    s "…"

    "Maya shoots me a look that, without any words, says something along the lines of “Just let it happen.”"
    "I’m sure she’s just glad that whatever Ami’s minor outburst there was over, but I’d be a liar if I said I wasn’t interested in finding out a little more."
    "I mean, I’d be a liar even if I didn’t say that. Lying is kind of my thing. But that’s beside the point."
    "I don’t want to step on Maya’s toes (Mostly due to the fact that they would shatter into a million pieces) but I feel like if I {i}don’t{/i}, this could snowball into something bigger."
    "“How much bigger” is a question that, unfortunately, none of us would be able to answer right now...but it’s certainly a concern."

    m "…"
    s "…"

    "The look doesn’t fade- but as I slide my hands into my pockets and begin to let Maya have her way, I think back to something Ami said just minutes ago."
    "That “I’m just going to side with her anyway.”"
    "Is that what I’m doing right now?"
    "Am I disregarding Ami’s feelings and just rolling with what Maya wants because I...think she knows stuff?"
    "And, if that’s true...how does Ami know about it?"
    "At the end of the day, Maya doesn’t know anything anymore."
    "Well, close to anything. "
    "She still knows how the resets work for the most part. Probably."
    "But she’s just as lost as everyone else concerning the rest of the world."

    ay "And {i}that’s{/i} why Geoffrey had to sell one of his kidneys."
    sa "What a...brave man..."
    a "That still doesn’t explain the koala, though."
    s "Jesus, how much did I miss just now?"

    scene cupcaketable23
    with dissolve

    ay "Do you want to meet him, Sensei?! He should be off the phone any minute now!"
    s "Sure. I guess it wouldn’t hurt to finally meet your-"
    r "Senseiiiiiii! Taaaaaaaaaable!!!!!!!!"
    s "Or not. I have been, once again, summoned by a girl who I am contractually obligated to prioritize over any male."

    "I signal to Rin that I’ll be there in just a second before attempting to figure out how to end this conversation in a way that doesn’t make everything that happened totally meaningless."
    "The issue with that is that I get stuck on some pole I don’t know the name of in a course of mental gymnastics centered around the idea that {i}everything{/i} is inherently meaningless."
    "And if that much is true, it means that there’s nothing I can say to anyone right now that would either rationalize or explain what happened because..."
    "Well, some things just happen because they happen."
    "Girls fight. Best friends are no exception."
    "Maya called Ami cute. Ami thinks Maya is cute and used that as an excuse to do some venting."
    "Is this the time and place for that? Of course not. But it’s a thing that happened and it’s not on any of us to judge her for it when we already know her self-control is about as solid as a...marshmallow?"
    "I try to think of things that are pretty solid, but not {i}too{/i} solid for the sake of my metaphor."
    "I think I succeed."
    "Anyway, here is what I came up with for my wise parting words to mend the first signs of fraying threads in Ami and Maya’s relationship."

    s "I’ll talk to you later, I guess."

    scene cupcaketable24
    with dissolve

    a "Okay!"

    if bonus == True:
        a "Don’t stare at Futaba’s boobs for too long. If you do, they’ll entrance you and you won’t love me anymore."
        s "That is a tall order."
        s "Besides, you know I don’t love you for your chest."
        ay "That’s probably because there’s nothing there yet."
    else:
        a "Don’t forget to get any itemized receipts for anything you purchase from the wet bar!"
        ay "Aren't all bars wet?"

    scene cupcaketable25
    with dissolve

    a "…"
    ay "Love you."
    m "…"
    sa "…"
    s "Okay, then. Later."

    scene black
    with dissolve

    if bonus == True:
        "I slowly back away from the table just as it's overtaken by the scornful aura of a [niece] undeveloped."
        "But if I listen closely enough, I can still hear the burning desire to survive and grow dripping off of their cupcake-laden tablecloth."
    else:
        "........."
        "......"
        "..."

    $ renpy.end_replay()
    $ halloweentwo7 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    jump halloweentwo8

label halloweentwo8:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
n "But I can’t control everything, Kirin."
    ki "Can you control your legs? Because if so, we can walk right on out of here and pretend this little breakdown never even happened."
    ki "If we can find our way back, that is. This house has so many fucking bathrooms."

    scene norikobathroom22
    with dissolve

    n "It really does! What is up with that?!"
    ki "I don’t know. Just...rich people shit I-"

    scene norikobathroom23
    with dissolve

    ki "Wait...did you hear that just now?"
    n "Hm? Hear what?"

    scene norikobathroom24
    with dissolve

    ki "I don’t know, but...I could have sworn I heard someone come in here."
    n "{i}*Sniff*{/i}...Ngh..."

    scene norikobathroom25
    with dissolve

    n "How’s my makeup? Do I look okay?"
    ki "No. You look like you just watched your dog get run over by a car."
    n "Don’t joke about that. My dog actually {i}was{/i} hit by a car a long time ago."
    ki "And you’re still crying about it? Get over yourself."
    ki "Come here. Let me see your face."
    n "Okay...but if you try to kiss me again, I swear. "
    ki "Shh. Lemme see."
    ya "How precious it is to see the misguided continue to wander."
    ya "Through the twists and turns of this porcelain labyrinth, pushed deep behind the shadows that few dare to journey beyond."
    ya "It is almost as if this is where they belong."
    ya "Trapped within the confines of a temporary prison, with all the things required to convert it into the loveliest of homes scattered throughout it, waiting to be arranged."
    ya "I hope they are enjoying their stay here- away from the blanket of despair being draped over the others."
    ya "Something horrible is coming. How will you remain warm?"
    ya "Return."
    n "Yasu?..."

    scene norikobathroom26
    with fade

    ya "Hello again."
    n "What are you doing in here? Where’s Touka?"
    ya "I appear to have gotten lost. How ironic."
    ki "Uh...what about that is ironic, exactly?"
    n "Probably cause like...she’s always talking about helping those who are lost find their way or something?"
    ya "Are you interested in finding the way as well?"
    ya "I can show you if you are."

    scene norikobathroom27
    with dissolve

    ki "Oh, damn. I can see everything from this angle."
    n "I’m...okay for now. But thank you."
    n "Do you need help getting back to the party? Kirin and I were just about to leave."
    ya "That sounds wonderful. Thank you so much for your assistance."
    ya "I’m sorry for being such a burden."
    n "It’s fine. Don’t worry about it at all."

    scene norikobathroom28
    with dissolve

    n "You ready, Kirin?"
    ki "…"
    n "…"
    n "Kirin?"

    scene norikobathroom29
    with dissolve

    ki "Oh. Uhhhhhhhhh..."
    ki "Actually, you two can go on without me. I’ll catch up with you in a little while."
    n "Are you...sure? Because...we’re kind of in a maze and..."
    ki "Yup. I’m good. Bye now."

    scene norikobathroom30
    with dissolve

    n "…"
    ya "She’s so pretty."
    n "…"
    n "Have..."
    n "Have we really been in the men's room this entire time?"

    scene black
    with dissolve2
    stop music fadeout 5.0

    "{i}Noriko and Yasu head back to the party!{/i}"
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloweentwo6 = True

    jump halloweentwo7
...
```