# Official Unofficial Double Date
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo8&go=Go)


Part of event chain [The First Signs of Fraying Threads](./halloweentwo7.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo8
* Group: Main
* Triggered by label: halloweentwo7

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo8:
    scene otohadoubledate1
    with dissolve

    s "Hey. What’s going on?"
    o "Hey. You should date Futaba."
    f "What are you doing?!"
    s "Yeah, what {i}are{/i} you doing? You’re supposed to be the one who doesn’t want me to do anything like that."
    s "Remember your job here, Otoha."
    o "I don’t mean like {i}date{/i} date, obviously."

    if bonus == True:
        s "You want me to just use her and then dump her? What kind of friend are you?"
    else:
        s "You want me to just hug her and then dump her? What kind of friend are you?"

    scene otohadoubledate2
    with dissolve

    r "She’s talking about a double-date, Sensei."
    r "Nodoka has coordinated a spontaneous game of truth or dare in the corner of the room and Futaba doesn’t want to go because she gets nervous with stuff like that."
    f "Sensei...please just...ignore this conversation and go back to the other table..."
    s "I can’t. I already had a cool and memorable send-off."
    o "Yeah, yeah. I'm just trying to make this a double date."
    o "But like...I mean, if you {i}want{/i} to date Futaba like, for real, you probably should."
    s "Again, remember your role here."

    scene otohadoubledate3
    with dissolve

    if bonus == True:
        o "No, no. Think about it. Futaba’s not only more mature than pretty much everybody in our class, but she’s also more {i}developed{/i} than everybody in our class."
        o "It’d be just like dating a real, live adult woman! Do you think you’d be okay with that?"
        s "…"
    else:
        o "No, no. Think about it. You like hugs. She likes hugs. What's there not to love?"
        s "Probably the fact that I am her teacher."

    f "I’m so sorry..."

    if bonus == True:
        s "There’s no reason to apologize. I’m fine with being your temporary date for the night."
    else:
        s "There’s no reason to apologize. I guess it's fine as long as it's pretend."
        s "I used to play house all the time when I was little so I'm pretty great at pretending."

    scene otohadoubledate4
    with dissolve

    f "What? No, I...Come on. "
    s "I don’t see the big deal. Everyone else will just think I’m sitting at the table like I normally would."
    s "But what they {i}won’t{/i} know is that I’m secretly your temporary boyfriend...Frank."

    scene otohadoubledate5
    with dissolve

    r "Frank?"
    f "Why are you Frank? I don’t want to date Frank. I don’t even know Frank."
    o "Okay, okay. If you’re Frank, we should give Futaba a codename as well."
    f "If this is how dating works, I think I’m okay with just...not ever doing that."
    s "Futaba can be Clarissa- a single mother of three who works nights at a local hostess club."

    scene otohadoubledate6
    with dissolve

    f "What is happening?! Why do I have kids now?!"
    r "I wanna be Jazmin, the badass leader of an underground fight club! But not like, {i}secret{/i} underground. Literally underground."
    r "Also, my blood type is A- and I have a pet alligator who killed Clarissa’s dog three years ago, which started our rivalry."
    f "Why is my dog dead now?!"
    o "Wow. Dating is awesome."
    s "Alternatively, I can just be Sensei and we can have a normal conversation before Futaba’s face gets any redder and she winds up fainting."

    scene otohadoubledate7
    with dissolve

    r "Aww. I already miss Frank. He always had so much to say."
    f "I...appreciate you switching back to your normal self...but we {i}still{/i} don’t have to call it a double-date..."
    f "You can just sit next to me like you normally do and...we can watch these two be...girlfriend and girlfriend."
    s "What? Now I’m not good enough for you?"

    scene otohadoubledate8
    with dissolve

    f "Y-You know that’s not it! I just don’t want you feeling pressured to...do something like that just so I can...fit in..."
    s "Hah..."

    scene otohadoubledate9
    with fade

    s "I’m not doing this so you can “fit in.” I’m doing it because it changes literally nothing and doesn’t bother me."
    s "So unless it bothers {i}you{/i} for some reason, what’s the harm in just temporarily assuming the roles of people who are dating for the duration of a conversation or two?"
    o "Weird to say this, but I’m on Sensei’s side. "
    o "Just go along with it, Futaba. It’s not like you two are {i}actually{/i} dating or anything."
    o "It’s just a fun way to make you {i}not{/i} the third wheel anymore while also making things a little less awkward for Rin and me."

    scene otohadoubledate10
    with dissolve

    r "Wait, are things awkward?! What did I do wrong?!"
    o "Huh? No...nothing. I’m just...I don’t know."
    o "It’s still kind of embarrassing...holding hands and stuff in public."
    o "Awkward probably wasn’t the right word. Just...new?"
    r "Is it because of my glove? I’ll take off the glove. "
    f "I don’t think the glove is the problem, Rin..."

    scene otohadoubledate11
    with dissolve

    f "I think it’s...normal for people to feel a little awkward right after they start dating..."
    r "I’ll say. You felt awkward before even {i}temporarily{/i} dating Frank and now he’s gone forever."
    f "I just mean that it’s...not your fault..."
    f "And...I guess now I understand a little better why we were trying to make this into a double date rather than just a normal conversation."
    r "I want to agree but, honestly, all I can think about is Otoha’s hand."
    r "I was expecting a firm grip, but she actually feels really dainty and fragile."
    o "That’s...probably just the glove getting in the way."

    scene otohadoubledate12
    with dissolve

    r "Ah! So it was the glove after all!"
    f "I’m sure I sound like a broken record in saying this again, but...I’m sorry."
    s "No need to apologize when it’s become overwhelmingly apparent that you are the glue holding this table together right now."
    f "I’m really not...I’m just hanging out with my friend and her new girlfriend..."
    f "And I guess my...my..."
    f "My..."
    s "Temporary boyfriend?"

    scene otohadoubledate13
    with dissolve

    f "Umm...y-yeah..."
    f "Which sounds weird to say even if it’s just temporary..."

    "Futaba begins lightly tapping one of her legs underneath the table, which I’m pretty sure is a telltale sign of nervousness."

    if bonus == True:
        "I wouldn’t normally point that out or, perhaps, even notice it. But it’s currently causing a very apparent jiggle in her chest region that I would cite as a particularly crucial element to this scenario."
        "Boobs are so cool."
    else:
        "I hope that this conversation ends soon so that she can go back to having fun and not worrying about stuff."

    o "So...is it an official {i}unofficial{/i} double date? Has Futaba accepted Frank-Sensei’s tentative confession?"

    scene otohadoubledate14
    with dissolve

    f "Um...y-yeah...I...accept..."
    o "Just don’t cry when you inevitably have to break up when he leaves the table."
    f "I will...try not to."
    r "Or just date for real. There’s always that."

    scene otohadoubledate15
    with dissolve

    f "Uhh...Rin?"
    r "What? If you two just dated for real, you wouldn’t have to {i}actually{/i} break up when he leaves the table."
    r "Otoha even said it earlier. If there’s anyone who it would be totally cool for Sensei to date, it would be you."
    o "I mean...that’s a {i}little{/i} different from how I said it."
    f "I...understand that...but I don’t really think now is the best time to talk about that..."

    scene otohadoubledate16
    with dissolve

    r "Is there ever going to be a {i}better{/i} time than right now?"
    r "You look adorable. Sensei is in a good mood. The setting is romantic. And Nodoka’s not even here to make things weird."
    s "You know I’m here, right? Because it’s a little weird hearing you strategize about turning this into a real relationship when I’m a part of the conversation."

    scene otohadoubledate17
    with dissolve

    f "Hahah...how many times have I apologized tonight?..."
    s "I’m not sure, but I’m assuming you’re tacking another one on now."
    r "Sensei, you think Futaba is pretty, right?"
    r "Why not just make it official and actually get together with her? That way, we could have {i}real{/i} double dates all the time and not have to pretend anymore."

    scene otohadoubledate18
    with dissolve

    f "{i}Rin...what are you doing?...{/i}"
    o "Yeah, what’s going on?"
    o "I realize I’m the one who started this, but don’t you think you might be taking things a little too far?"
    r "How? By trying to get two of my favorite people together? Is that a...weird thing for me to want?"
    f "Sensei...please excuse us for a moment..."
    s "Uhh...sure. We don’t have to break up yet, but if anyone asks, I’m-"
    f "{i}A minute please, Sensei...{/i}"
    s "Right. Got it."

    scene black
    with dissolve

    "I back away from the table and wonder why two consecutive groups with seemingly infallible friendships have started combating one another over spontaneous, trivial blips in the radar that is life."

    if bonus == True:
        "Then I go talk to Molly because she is currently drinking all by herself and her thighs look particularly alluring tonight."
    else:
        "Then I go talk to Molly because she is currently drinking all by herself and I want to make sure she's doing okay."

    scene otohadoubledate19
    with dissolve

    f "What are you doing? Why are you putting us on the spot like that?"
    r "I wasn’t trying to put you on the spot. I just...like you guys and..."
    r "And you like Sensei, don’t you? "
    r "Like, what if the only thing that’s preventing you two from getting together is the fact that you haven’t tried asking him out yet?"
    f "That’s...still not your place to get involved."

    scene otohadoubledate20
    with dissolve

    r "I just wanna help! Is that really so bad?"
    f "When you’re forcing it down our throats, yes. Yes, it is bad, Rin."

    scene otohadoubledate21
    with dissolve

    o "Even if she does like him, we can’t be that direct, dude. "
    o "It’s fine to make jokes and try to push them a little closer together, but when you’re literally listing the reasons they should date, it’s...different."
    o "It stops becoming a joke and...well, makes shit weird."
    o "We can’t put Futaba in an uncomfortable position like that."
    r "But...that’s not what I..."

    scene otohadoubledate22
    with dissolve

    f "Is...Is everything {i}okay{/i} with you right now, Rin?"
    r "What do you mean “Okay?” I look normal, right? I’m acting normal, right?"
    f "You look fine, but..."

    scene otohadoubledate23
    with dissolve

    o "Do you want to go? We can leave if you want."
    o "I don’t really know the...signs of your depression yet, but if you’re not feeling well-"
    r "What are you guys talking about? I’m totally fine. I’m just trying to help everyone out."
    o "You’re sure it’s not anything else?"
    r "I...yeah! Yeah, of course! What else would it even be?"

    scene otohadoubledate24
    with dissolve

    f "I’m sorry if I...falsely assumed something was wrong...but you {i}can’t{/i} be saying things like that, Rin. I need to...handle stuff like this on my own."
    r "I just...don’t want you to get overwhelmed..."
    r "I think you’re great and that...you deserve all of the love in the world. "
    r "I was just trying to...I don’t know, funnel some of it into you?"
    f "Just..."
    f "Let’s just treat this like any other night, okay?"
    f "No talk about...double dates or...romance or anything..."

    if futabahalloween2win == True:
        r "But...Futaba..."
        r "He literally chose you out of {i}everyone{/i} earlier."
        r "You have a real shot right now."

        scene otohadoubledate25
        with dissolve

        f "I don’t have any more of a shot right now than I did yesterday."
        f "Or last week or...any other day."
        f "Sensei’s...really nice to me. And yes, I do like him."
        f "But...he’s not ever going to {i}date{/i} me, Rin."
        r "Don’t say that...You don’t know that..."
        f "If something changes, you’ll be the first to know."
        f "But right now...I’m happy with the way things are."
        f "I’m happy just knowing that the person I admire looks at me and doesn’t immediately compare me to either of you."
        f "That’s honestly...more than I ever expected to get."

        scene otohadoubledate26
        with dissolve

        f "And..."
        f "And I don’t want him getting scared away..."
        r "Futaba...No...I..."
        o "Anyone who would ever get scared away from you doesn’t deserve to even breathe the same air, Futaba."
        o "You’re amazing and we’ll stop with all of the double date stuff."
        o "And...we’re sorry."
        o "Really."

    else:
        scene otohadoubledate27
        with dissolve

        o "Got it. "
        o "We’ll stop everything right now. And we’re sorry for pushing things a little too far. "
        f "Thank you, Otoha..."
        r "I’m really sorry, Futaba...I don’t really know what got into me..."
        f "It’s okay, Rin. Just...please be more careful about the things you say sometimes."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene otohadoubledate28
    with dissolve

    s "Everything okay over here? No shattered remnants of broken bonds or anything like that?"
    f "Nothing of the sort...Everything is fine."
    o "Sorry shit got all weird. I’ll take the blame since it was all pretty much my idea."
    o "Let’s just...hang out or whatever and talk about completely unrelated stuff. Like...movies or...uhh..."
    o "Has anyone else watched Squid Game yet?"

    scene otohadoubledate29
    with dissolve

    f "Oh my God. It was so good, right?!"
    o "Right?!?! And that part with the glass bridge? Wild. Absolutely fucking wild."
    r "…"
    s "…"

    scene black
    with dissolve2

    "The conversation carries on for another ten minutes before I finally decide it’s in my best interest to just leave."
    "Not only did I not have anything to contribute to their extremely emphatic discussion about some Korean television show, but I had a creeping suspicion that my presence was causing Rin to feel...off."
    "That could just be me being self-centered, though."
    "I guess it’s equally probable that her sudden swap to silence had absolutely nothing to do with me and was just the result of realizing she’d disappointed a friend."
    "Futaba recovered well, though."
    "I would have been uncomfortable in her position too."

    if bonus == True:
        "Hell, I was uncomfortable in {i}my{/i} position- but that was moreover because I was worried I’d have to explain to yet another girl why I don’t want to date them."
        "That crisis was averted in its entirety, though."
        "And now?"
        "I must return to the drunk girl in an extremely tight dress to make sure she does not drink herself into a coma."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ halloweentwo8 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump halloweentwo9

label halloweentwo9:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
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
...
```