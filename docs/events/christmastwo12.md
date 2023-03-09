# The Smile, The Face
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo12&go=Go)


Part of event chain [New Age Entrepreneurs](./christmastwo11.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo12
* Group: Main
* Triggered by label: christmastwo11

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo12:
    scene yuricouch1
    with dissolve2

    s "Excuse me, but I was wondering if any of you would be able to tell me where I could find some lesbians."
    no "I’d be more than happy to point you in the right direction if you’d be willing to tell me what you intend to do with them."
    s "Nodoka, are you actually drinking or have you just been holding that wine glass to look sophisticated all night?"
    o "Oh, she’s drinking alright. Nodoka just has weirdly high alcohol tolerance."

    scene yuricouch2
    with dissolve

    no "I must remain vigilant at all times. You never know when a beautiful woman might show up and attempt to bed me."
    r "I think she’s just a really calm drunk. It’s not like we can really judge by any of the things she’s saying since she’s always saying...Nodoka things."
    s "So what you’re saying is that Nodoka is the cool one and you two are just losers."

    scene yuricouch3
    with dissolve

    o "There something wrong with being a loser now?"
    r "We just don’t really like alcohol. We tried it at the dorm war fashion show thing and we both thought it was kind of gross."
    o "It’s like our taste buds are totally in sync or something."
    r "Yeah! And it was even more like that last night when they were touching each other!"

    scene yuricouch4
    with dissolve

    o "Well, I guess that’s a thing Sensei knows now. That was a fun secret for twenty hours."
    s "Congratulations? I’m not really sure what to say here."
    o "Then talk about something else, man."
    s "How was it?"

    scene yuricouch5
    with dissolve

    o "Or be even weirder about it."
    r "It was {i}awesome.{/i}"
    r "And it wasn’t even me who made the first move! How crazy is that?!"

    scene yuricouch6
    with dissolve

    no "Oh? Otoha conveniently left that detail out when I made her describe the night to me in vivid detail. "
    no "If she skimped on that aspect, who knows what else she could have possibly left out?"
    o "Okay, first off, you really don’t need to keep a diary of every single lesbian experience I have."
    no "I do, but please continue on with your second point."
    o "Second, does it really matter who initiated it? It was just a kiss. It’s not like it was a big deal or whatever."
    r "It was a {i}bunch{/i} of kisses and it was a {i}very{/i} big deal."

    scene yuricouch7
    with dissolve

    o "Uhh...anyway! How’s your...Christmas? You warming up to the new teacher yet?"

    if bonus == True:
        no "They’re basically joined at the genitals already."
    else:
        no "They’re basically joined at the fingers already."

    s "I believe the phrase is joined at the hip."

    scene yuricouch8
    with dissolve

    no "You think I don’t know that?"
    o "So I take it she’s here to stay then?"
    s "Do you not want her around or something?"
    o "Nah, it’s nothing like that. I was just finally starting to get the hang of never worrying about homework and stuff."
    s "For what it’s worth, I doubt Imani is going to change anything about how the class is run. So there’s a high chance of you just never having homework again for the rest of your life."
    o "I think you mean the rest of the school year."
    s "I said what I said."
    no "Interesting. It sounds to me like Sensei might have a little information that he isn’t willing to share with the class."
    s "If I shared everything I know with all of you, none of you would ever be able to look at me again."
    o "Ew."
    no "I would."
    r "I would too. But only if Otoha is cool with it. If she’s not, I’ll pretend that I’m {i}not{/i} into it, but I totally will be. Just in secret. Yeah."

    play sound "phonebeep.wav"
    scene yuricouch9
    with dissolve

    o "Ugh. Well, speaking of shit I’m not into, the woes continue."
    r "Parents again?"
    no "They’re really all over you tonight, aren’t they?"
    o "Yuuuuuup. But I guess I can kind of understand where they’re coming from since it’s the first Christmas I’ve had away from home."
    r "Can you tell them I said hi this time?"
    o "No. And stop asking that."
    s "Can you tell them {i}I{/i} said hi?"

    scene yuricouch10
    with dissolve

    o "What? No. Go away. You’ve already ruined any chance of ever talking to either one of my parents."

    if bonus == True:
        s "Are you still torn up over the porn thing?"
        r "Porn thing? Have you been watching porn with my girlfriend?"

        if rinbetrayed == True:
            r "Does that mean what I think it means? "
            r "Are you planning on fucking me over {i}again?{/i}"

        s "No, Rin."
    else:
        s "Are you still torn up over the Spongebob thing?"
        r "Spongebob thing?"

    scene yuricouch11
    with dissolve

    if bonus == True:
        o "Right, I never told you. But he was in my dorm room when my mom called one night and his first thought was to start quoting some fucking raunchy ass porn video he memorized."
        no "Unfortunate. If I were there as well, I would have joined in on the fun."
        s "You know we can always just make our own fun. Right, Nodoka?"
        no "Let me hold this wine glass and pretend to be sophisticated for a few more hours before I get back to you."
        r "If it makes you any more comfortable, I promise I won’t make any sex noises if you tell your parents I said hi."
        o "Well, can’t say that’s a sentence I expected to hear tonight."
        o "Besides, I’m just texting them anyway. It’s literally impossible for them to hear anything like that through a text."
        no "Did you hear that, Sensei? We’re free to make as many lewd noises as we want."
    else:
        o "Right, I never told you. But he was in my dorm room when my mom called one night and his first thought was to start singing that song about the greasy spoon or whatever."
        no "I love that song. I will gladly sing it with Sensei right now."

    scene yuricouch12
    with dissolve

    o "Okay, as unsurprised as everyone here would be if the two of you decided to do that, I’m going to ask you to not. "
    o "I kind of need my ears to work if I’m ever going to be a singer and I’m afraid that hearing either of you two moaning or...grunting would kinda ruin that career path for me."

    if bonus == False:
        no "Did that song have grunting in it? I don't remember that."

    r "I think you’ll make it no matter what the two of them do, Otoha. You’re so talented. It’s amazing."

    scene yuricouch13
    with dissolve

    o "Huh? What? Me? Stop."
    r "I mean it. Seeing you working so hard every day, like...makes me want to give it my best too."
    o "I mean...it’s not {i}every{/i} day..."
    r "Then however many days it is- which feels like a lot to me, but I guess that could be just because I always want to be around you."
    no "Here they go. Kumon-mi’s newest power couple- getting their yuri all over the couch."
    o "I just...have to stay focused or I’ll fall behind, you know?"
    o "I know that I can get a little {i}too{/i} sucked in while writing music and stuff, but you can always...I don’t know, try and tell me to stop if you really...want to see me or something."
    s "Wow, you two really {i}are{/i} getting your yuri all over the couch."
    s "I feel really sorry for whatever cleaning crew is tasked with-"
    ya "Ring ring ring~"
    s "Hm?"

    play sound "static.mp3"
    scene yuricouch14 with flash
    stop sound
    stop music

    s "..."
    s "Yasu?"
    ya "Ring ring ring. It comes in threes."
    ya "Ring ring ring. It shakes the trees."
    ya "Ring ring ring. It burns your eyes."
    ya "Ring ring ring. Surprise, surprise."
    s "..."
    ya "..."
    s "What?"
    ya "Something is here."
    s "I hope it’s an ambulance because I think you may have snapped."
    ya "Snapped?"
    s "Gone insane. Lost all grip on reality."
    ya "Aren’t you the one who’s losing grip, Sensei?"
    s "I don’t know what you’re talking about."
    ya "You’ll find out soon."
    ya "Ring ring ring~"
    s "Yasu-"

    play sound "static.mp3"
    scene yuricouch15 with flash
    stop sound
    play sound "phonering.mp3"

    o "Oh my- are you fucking kidding me? Why do they have to call?"
    r "You’re...not going to have to leave, are you?"
    o "Fuck if I know. God forbid I actually get to relax for a single night without having to check in with my parents every two minutes."
    no "Just don’t answer. What are they going to do about it?"
    o "Stop paying for my vocal lessons? Stop paying for my phone bill? I don’t have a job. I can’t afford all of this on my own."
    r "Otoha-"
    o "Just...give me a second..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene yuricouch16 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    ya "The smile, the face...the light before dawn..."
    ya "It’s buried beneath us..."
    ya "And...everything’s..."
    ya "..."
    ya "Oh."
    ya "I can’t hear it."

    scene yuricouch17
    with dissolve

    ya "I..."
    ya "What?..."
    mo "Um...Sir? Do you mind if I just...stand near you for a second?...I felt awkward with Otoha just...right in front of me..."
    s "..."
    o "Mom? What do you want? I already told you I was spending Christmas with my friends this year."
    o "..."

    scene yuricouch18
    with dissolve

    o "What are you talking about? I absolutely {i}did{/i} tell you."
    o "..."
    o "Then check your fucking text messages and-"
    o "..."
    o "Yes! I did mean to curse! You’re being totally unfair!"
    o "..."
    o "Because I’d rather just be with my friends this year! It’s not like I’m quitting the family or something. "
    o "..."

    scene yuricouch19
    with dissolve

    o "Well, what did Dad say? Because..."
    o "..."
    o "Can you at least {i}put him on?{/i} Because I highly doubt he’s making as big of a deal out of this as you are."
    o "..."

    scene yuricouch20
    with dissolve

    o "Fine! Whatever! I'll come back!"
    o "But it makes literally zero sense that I’m old enough to live in the dorms, but {i}not{/i} old enough to-"

    scene yuricouch21
    with dissolve

    o "..."
    o "Did..."
    o "Did she really just hang up on me?.."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yuricouch22
    with dissolve2

    r "So, uhh...that didn’t sound like it went too well."
    o "It didn’t. And now I have a headache, so that’s wonderful."
    r "What...happened?"
    o "My mom is pissed off because apparently being born into the Okakura family means you’re not allowed to spend Christmas with your friends or something."
    o "I don’t know- it’s just one more stupid rule out of the hundred million of them I have to put up with on a daily basis."

    scene yuricouch23
    with dissolve

    r "So...you’re leaving? Like...now?"
    o "I guess. Especially since I was spot on with the “I’m holding your career and communication” hostage thing. That was one of the first things she jumped to."
    r "Well...how much are your lessons? Maybe I can save up enough from the cafe for-"

    scene yuricouch24
    with dissolve

    o "Rin, no. Use your money to buy yourself new basketball shorts or...get your guitar set up or something. I’m not going to let you use it on me."
    r "But if it’s to support your passion, I-"
    o "My passion will be fine. My {i}Christmas{/i} on the other hand...well, the tail end of that is pretty much fucked."
    r "Um..."

    scene yuricouch25
    with dissolve

    r "It...doesn’t have to be?"
    o "What? No, it kind of does. Like, I don’t really have a choice. I have to go back to my parents or we won’t be able to text each other weird emojis at random hours of the night anymore."
    r "I know you have to leave, but...what if I came with you?"

    scene yuricouch26
    with dissolve

    o "Like...downstairs? I figured you would walk me to the lobby anyway, so-"
    r "No, Otoha..."
    r "To your parents’ house..."
    o "Uhh..."
    r "We’ve been, like...dating for a little while now and I still have no idea what they’re like and-"

    scene yuricouch27
    with dissolve

    o "Okay, uhh...yeah. That’s probably not a good idea."
    o "I obviously really like you, but there’s no reason for you to meet my parents."
    o "It’s going to be like, really boring anyway. Like, I’m probably just going to go to sleep when I get there."
    r "Is being in a relationship really not a good enough reason to meet them?..."
    o "It’s really not. I mean, I haven’t met {i}your{/i} parents either so like, it’s obviously not just a me thing."

    scene yuricouch28
    with dissolve

    r "You can meet them whenever you want! They’ve actually been wondering when they’d get to see you ever since we started dating."
    r "Do your parents like...not want to meet me or something?"
    o "..."
    o "Uhh..."

    scene yuricouch29
    with dissolve

    r "Wait..."
    r "Do your parents..."
    r "Even {i}know{/i} about me?..."
    o "..."
    r "..."
    o "Do...they {i}have{/i} to?"

    scene yuricouch30
    with dissolve

    r "..."
    o "Rin, it’s nothing against you. Really."
    r "But...I don’t understand. I know I can be like, clingy and annoying sometimes, but I still think I’m a good person more often than not."
    r "Is it just because it’s Christmas? Can I maybe...meet them {i}eventually?{/i} I just don’t understand why you have to hide-"

    scene yuricouch31
    with dissolve

    o "It’s because you’re a fucking girl, dude."
    r "Because I’m..."
    r "But...what does-"
    o "We can’t all have fucking...cool, accepting, lesbian parents like you. "
    o "If my parents found out I was dating a girl, I'd be literally fucked. They’d take everything away from me. "
    o "And I just...can’t risk that sort of thing right now."
    r "..."
    o "But, uhh...maybe one day when I can like, support myself and shit. If we’re even still together by then."
    r "What is that supposed to mean?"

    scene yuricouch32
    with dissolve

    o "Just that I know I sound like a real asshole right now."
    r "..."
    o "Listen, can I maybe...call you about this later? I don’t really want to do this in front of the whole class."

    scene yuricouch33
    with dissolve

    r "Will you even be able to? What if your parents overhear you talking to a girl? Is {i}that{/i} going to get you in trouble?"
    o "Rin, I’m sorry...Really."

    scene yuricouch34
    with dissolve

    r "Yeah, I know. But, uhh...at least we’re still dating! That’s...good! Anyway, enjoy Christmas with your parents!"
    o "Rin-"
    r "Please leave the room now. I don’t want to cry in front of you."
    o "..."
    r "..."
    o "I’m really sorry..."

    play sound "dooropen.mp3"
    scene yuricouch35
    with dissolve

    "Otoha awkwardly exits the room without making eye contact with anyone."
    "And as much as I want to condemn her for her actions tonight...I can’t."
    "She’s a [teenage]girl caught in the clutches of an iron fist capable of squeezing her until she bursts at the drop of a hat."
    "It only makes sense that she’d want to preserve her feelings over that of someone else- even if that person is someone she’s decided to commit to."
    "“Commit” in the loosest possible sense of the word, of course."
    "It’s hard to assign a high score to any sort of commitment that allows you to leave the room with your partner on the verge of emotional collapse."
    "Maybe Otoha’s just a bad person."
    "Or maybe she’s just grown so used to Rin being on the verge of collapsing that when her knees start to buckle a little more than normal, she has a tough time noticing."
    "I can forgive her for that."
    "What everyone else decides to do with it is entirely on them."

    f "..."
    r "..."
    f "Let’s sit down."

    scene yuricouch36
    with dissolve

    f "I’m here. It’s okay."
    r "All I wanted was-"
    f "We can talk about it later if you want. "
    f "Just take a second to sit down and breathe right now. Trust me."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo12 = True

    jump christmastwo13

label christmastwo13:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
with dissolve

    tk "What?! No! You’re supposed to fear me! My business is obviously going to be better! I have the financial backing of the Tsukioka foundation! We’re famous!"
    ch "If Chinami doesn’t know you, you probably aren’t famous enough."
    tk "But...we are! We’re important! Just because you don’t know about us doesn’t mean we’re not!"

    scene wizardparty24
    with dissolve

    ch "Excuse me. Tsubasa? Can Chinami have some peanuts as a snack, please?"
    tb "No, Chinami. Your secondary sister already warned me that you would try and pull something like this, and I already promised I wouldn’t let it happen."
    ch "That was no sister of Chinami’s. That was an assassin sent by a government agency who plans to take down Chinami-Corp. Peanuts, please!"
    tb "No, Chinami."
    ch "Rats!"

    scene wizardparty25
    with dissolve

    tk "Chinami-Corp is...a prominent enough business that even the government is attempting to intervene? Are you sure it was an assassin, Chinami?"
    ch "Maybe! Chinami’s memory gets foggy when she is hungry."
    tk "When she’s..."

    scene wizardparty26
    with dissolve

    tk "Then we will have a Christmas feast!"
    tk "Mother! Call the kitchen! Order two of everything on the menu! And tell them if they’re not here in ten minutes that they’re fired!"
    tb "Tsukasa, please stop firing kitchen staff in every establishment we enter. There are only so many cooks left in the city."
    ch "Chinami thinks a feast sounds fun!"

    scene wizardparty27
    with dissolve

    ch "But Chinami doesn’t have any money since she invests it all back into her company."
    tk "Never fear, Chinami. Tsukasa has {i}all{/i} of the money. And she’s interested in hearing more about how you run your business."
    tk "I forgot to mention it, but Tsukasa has {i}also{/i} been intending to find a business partner lately. And since Chinami is close to the same age as her, Tsukasa thinks she might be a good fit."
    tb "Tsukasa, dear, are you really going to start talking like that as well? Because I have no idea how I’m going to explain it to your father."

    scene wizardparty28
    with dissolve

    tk "Silence, mother! This is just how the new age of entrepreneurs speaks! "
    tk "Does Chinami accept Tsukasa’s feast proposal? Chinami can consider it an investment for the future if so."
    ch "Chinami accepts and is pleased to open business relations with you!"
    ch "She was already very excited to meet another girl her age, but had no idea it would be such a successful venture!"

    scene wizardparty29
    with dissolve

    tk "Chinami...I think this is the beginning of a very beautiful friendship."
    ch "Chinami is excited to finally have a friend and will try to forget that you hurt her feelings by calling her a peasant earlier."
    tk "Textbook rival speak, Chinami. Sometimes, you need to psyche out your opponent before they even know they’re competing."
    ch "Chinami doesn’t care anymore. She just wants to eat."
    tk "Mother! The feast!"
    tb "I’m calling right now, dear..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."


    scene wizardparty30
    with dissolve2

    c "Yeah...you’re probably right. I bet she's doing fine, but..."
    y "..."
    y "But what? "
    y "Havin’ second thoughts about standing around and staring at our fuckin’ teacher all night?"
    c "..."

    scene wizardparty31
    with dissolve

    c "You know what? Maybe I should just run over there and check on her to make sure everything’s okay before...staring at our “fucking teacher” all night."
    c "You wanna come with me?"
    y "Sure. But only cause the alternative is standing around here by myself and looking like a fucking wack job."

    scene wizardparty32
    with dissolve

    c "True. But hey! At least {i}you’d{/i} get a turn to watch Sensei flirt with the rest of the class instead of me!"
    y "Jesus, I can taste the salt from here."
    c "What salt? I’m totally fine and not jealous at all!"
    y "Mhm. And I’m a happily married housewife with three kids and a puppy."
    y "Let’s just fuckin’ get this over with."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmastwo11 = True

    "........."
    "......"
    "..."

    jump christmastwo12
...
```