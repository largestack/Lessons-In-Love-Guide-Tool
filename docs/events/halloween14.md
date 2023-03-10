# Kadrillionbilliontrillion (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Pry With a Smile](./halloween13.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: As Loud as a Whisper Can Be](./day214.md)
* [Ayane: Regularly Scheduled Programming](./dojo25.md)
* [Makoto: Aftermath](./pornshop20.md)
* [Miku: Thighs On-Demand](./soccer25.md)
* [Haruka: Performance Review](./harukadate10.md)
* [Kaori: The Best Ways to Rub a Cock](./kaoridate5.md)

## Event properties

* Id: halloween14
* Group: Main
* Triggered by label: halloween13
* Chain sources: halloween13
* Chain sources path: halloween13

## Official wiki page

[Kadrillionbilliontrillion](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween14&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween14:
    scene mollydrunk1
    with fade
    play music "letsfuckingo.mp3"

    f "U-Umm! Molly! I think you may have had a little too much to drink..."
    mo "NONSENSE, FUTABA! IF 'ME FAT'ER COULD SEE ME NOW, HE’D BE PROUD!"
    mo "SURE, HE’D PROBABLY SAY 'ME SKIRT IS A LITTLE TOO SHORT AND T'AT I DON’T NEED AN EYEPATCH-"
    mo "AND T'AT I SPEND TOO MUCH TIME PLAYIN' GAMES AND SHOULD PROBABLY MAKE SOME “REAL FRIENDS” BUT-"

    scene mollydrunk2
    with dissolve

    mo "Hey wait a *hic* sec. T'even {i}are{/i} real friends? Aren’t the ones I have online just as good?"

    scene mollydrunk3
    with dissolve

    mo "ACCEPT ME FOR WHO I AM, DAD!"
    mo "AND STOP LOOKING UNDER MY BED! IT’S WHERE I KEEP ALL THE GOOD STUFF!"
    f "I’m not your father. I’m Futaba. And I don’t care what you keep under your bed."
    f "I just think it might be good if you calmed down a bit before you hurt anyone. Or yourself."

    scene mollydrunk4
    with dissolve

    mo "Ta’ heck ye talkin’ about wit’ all ‘tis hurtin eachot’er nonsense?"
    mo "T’ain’t even possible for me ta hurt a fly let alone anot’er human bein’."
    mo "D’even if’a could, s’not like we ain’t already gonna die anyway. "

    scene mollydrunk5
    with dissolve

    mo "LIVE, FUTABA! LIIIIIIIIIIIIIIIIVE!!!!!!!!!"
    f "I barely understood any of that..."

    scene mollydrunk6
    with fade

    a "Tsuneyo? What’s wrong? Why are you looking at me like that?"
    t "I’ve done a bad thing."
    a "...Okay?"
    t "I let the Emerald Guardian consume too many alcohols and now she thinks Futaba is her dad."
    a "Yeah, I can hear her yelling from all the way over here, but why does that mean you have to put your hand on my shoulder?"
    t "That just kind of happened."
    t "This fabric is soft."
    a "Th-thanks...I sewed it myself."
    t "I am impressed, but there are more important matters at hand."
    t "Are you able to do anything to fix the Emerald Guardian?"

    scene mollydrunk7
    with dissolve

    a "I don’t really know if there’s anything you can do to {i}fix{/i} a drunk person."
    t "So she will remain this way forever?"
    a "Well, no...she’ll probably go back to normal tomorrow."
    a "But I don’t know if ‘normal’ for Molly really matches the ‘normal’ for everybody else."
    t "And to think that mere hours ago we were sharing both tears and a man."
    t "It pains me to see how far she’s fallen."

    scene mollydrunk8
    with dissolve

    a "Wait, what do you mean by sharing a man? There is only one man around here and he is my [uncle]."
    t "Correct. He taught us a valuable lesson about life and then took us into his arms."
    t "It was a gripping moment."
    a "I don’t care what it-"
    t "Get it? Gripping?"
    t "As in we were gripping each other."
    t "Like a hug."
    t "It is a joke."
    a "..."
    t "Please laugh. I need the encouragement."

    scene mollydrunk9
    with dissolve

    a "Don’t touch my [uncle] anymore! I don’t care what kind of lesson it involves!"
    a "And don’t touch me either!"

    if bonus == True:
        t "I’m so sorry. I just feel compelled to keep touching members of your family for some reason."
    else:
        t "I’m so sorry. I was possessed by a demon three years ago and the demon loves you two."

    t "I will try and be better."

    scene mollydrunk10
    with dissolve

    a "Huh? Well, I mean...I guess I’m not really mad or anything...just kind of jealous."
    a "But I’m sure you wouldn’t do anything weird with him anyway so-"
    t "Everything I do is weird, so I probably would."
    a "Yeah, but..."
    a "Oh well. I guess it doesn’t really matter."

    scene mollydrunk11
    with fade

    mo "Heeeeey. Know what'cha need, Futaba? "
    mo "Ya need a good ole’ beer. T’will solve all ‘yer problems."
    mo "D’offer ya some a’ mine but t’would be an indirect kiss."
    mo "Kinda like one 'a t’ose yuri shows where ‘ta girl gets all embarrassed ‘cause she ain’t aware she likes girls yet."
    f "Put down the can, Molly. Please."
    f "I’d take it out of your hands but I’m afraid you’ll spill it all over me and this costume was kind of expensive to make."
    mo "Ha! ‘Yer tellin’ me. Have any idea how many lattes I needed ‘ta make to buy ‘ta fabric for ‘tis dress? "
    mo "Like a kadrillionbilliontrillion! "
    mo "Fookin’ crazy if ‘ye ask me. S’just coffee, ain’t it? Can fookin’ make it in ‘yer room f’ya really want."

    scene mollydrunk12
    with dissolve

    mo "‘Tis little can ‘a paradise, t’ough. Y’can’t make ‘tis in ‘yer room. I’ll tell ya ‘tat much. "

    scene mollydrunk13
    with dissolve

    mo "DAD! WHERE ARE ‘YE?! LOOK AT WHAT ‘YER DAUGHTER HAS BECOME!"
    mo "‘FONLY ‘YE WERE MORE ACCEPTIN’ OF ME AT A YOUNG AGE! I WOULDN’T HAVE TURNED TO ‘TA DRINK!"
    mo "I HOPE ‘YER HAPPY NOW! DAD!! "
    mo "AHHHHHHH!!!!"

    scene mollydrunk14
    with fade

    r "Oh you’ve gotta be fucking kidding me."
    m "Uhh..."
    c "Is Molly drunk? Is that what she’s been doing this entire time?"
    c "I didn’t even realize there was alcohol here."
    r "She must have went looking for it or something. It’s like she’s {i}trying{/i} to be a stereotype."
    m "How much do you even need to drink to start acting like that?"

    scene mollydrunk15
    with dissolve

    c "I have no idea, but I can’t help but feel like we should maybe do something about it."
    c "Where is Sensei when you need him? Or Makoto for that matter?"
    m "He’s probably the one who did this in the first place."
    m "He would be of no help here."
    r "Yeah, I think this might just be something Molly has to deal with alone."

    scene mollydrunk16
    with dissolve

    c "Aren’t you two really good friends? Isn’t there something you can say to her that would calm her down?"
    r "The only thing I can think of is giving her more until she passes out and I think you might be talking about something different."
    c "Oh God..."
    c "I think...I think I should go do something about this."
    r "Well, uh...good luck? I’m gonna hang out over here where it’s still safe."

    scene black
    with dissolve

    "{i}Somewhere nearby...{/i}"

    if bonus == True:
        s "Well, that definitely wasn’t what I had in mind when Makoto said she had something to talk about."

        "I make my way out of the guest room and head back toward the main hall to join the girls for the rest of the party."
        "Makoto wanted to rest for a while after losing her virginity (Which is fair, I guess), so I’m heading back alone."
        "Which, now that I think about it, is actually pretty good for me."
        "I can probably say I just had to bring her home early because she was feeling sick or something."
        "Here’s hoping Makoto can’t summon the strength to move her legs and destroy that excuse for me."
        "Now, to get back to-"

    scene mollydrunk17
    with dissolve

    a "WHERE ON EARTH HAVE YOU BEEN?!"
    a "Molly is drunk, Miku looks all upset, and Tsuneyo [molest]ed me!"

    if bonus == True:
        s "I was walking Makoto back-"
    else:
        s "NOWHERE. AND DEFINITELY NOT HUGGING ANYONE."

    s "Wait, what was that last one?"
    a "Well, it wasn’t like, {i}actually{/i} [molesting] me, but she touched my shoulder for a really long time and kept staring into my eyes like she was in love with me."
    s "Oh. Well that’s significantly less exciting."

    "I turn away from Ami for a moment and address the girl behind her."

    s "Happy birthday, Yumi. I’m glad you could make it."

    scene mollydrunk18
    with dissolve

    y "Oh. Uhh, thanks I guess."
    y "Back to normal now?"
    s "What do you mean by-"
    a "Sensei! You need to do something."

    scene mollydrunk19
    with dissolve

    s "Do something about what? "
    a "The drunk [teenager] that Futaba and Chika are trying to calm down as we speak!"
    s "I’m sure they’re a lot better at handling something like that than I would be."

    if bonus == True:
        y "Probably. You’d just take advantage of her or something."
    else:
        y "Probably. You’d just attack hug her or something."

    s "Thanks, Yumi. Again, really glad you could make it."

    scene mollydrunk20
    with dissolve

    a "For real, though! Where were you? And what happened to Makoto?"
    s "She was feeling sick so I walked her...somewhere."
    a "Somewhere?"
    a "So you just...left her in a random place while she was feeling sick?"
    s "Sure, yeah. That sounds about right."

    scene mollydrunk21
    with dissolve

    a "Oh, okay. Well that sounds good to me."

    scene mollydrunk22
    with dissolve

    a "But you’ve still gotta do something about-"
    s "Yeah, yeah. I’ll try. "
    s "Not making any promises, though."

    scene black
    with dissolve

    "I step away from Ami, who follows closely behind me as I make my way over to Molly, Futaba, and Chika."

    scene mollydrunk23
    with dissolve

    mo "Heeeeeeeeeeeeeeeeeeeeeeeeey~"
    mo "How about you an’ me get outta here and go play some games at my place, Sir?"
    mo "I’ve got a whole drawer o’ stuff I t’ink ya’d be really into."
    s "Weird. I don’t remember her accent being this strong a few hours ago."
    f "I think drinking made it a lot worse than it normally is."
    mo "T’aint true one bit. Drinkin’ don’t make any’tin worse. Right, Sir?"

    if bonus == True:
        mo "Sohowaboutit? We gonna get outta here? ‘Ye gonna princess carry me and make me into a real wom-"
    else:
        s "It actually makes everything worse. I recall a time back when {i}I{/i} was in college where-"

    scene mollydrunk24
    with dissolve

    mo "*hic*"
    mo "Guh..."
    mo "I t'ink I’m gonna t'row up..."
    c "Just take it easy, Molly. Try not to talk too much. "
    c "In fact, it would probably be {i}really{/i} really good if you didn’t talk at all, okay?"
    c "Do you need some water? Bread?"
    c "Well, actually, I don’t think there’s any bread here. Would...wedding cake help?"

    scene mollydrunk25
    with dissolve

    mo "I’m gonna *hic* miss you so much, Sir. I don’t want a new teacher. "
    c "Maybe...{i}you{/i} could tell her to stop talking, Sensei?"
    c "Everything I say to her is just going over her head."
    f "Molly...you could very well be in Sensei’s class again next year. You don’t know that you're not yet."
    mo "We need to *hic* spend more time together before it'sss...toolate..."
    mo "'Yer 'ta only one I trust wit’ my *hic* phone...Sir..."
    c "Her...phone?"
    c "Are you guys like, texting buddies or something?"
    s "I don’t even have Molly’s phone number, so no."
    mo "All ‘ye gotta do is ask!"
    mo "I gots...plenty’a stickers ‘ta send ‘ye on LINE, man. "
    mo "And a bunch of cosplay photos just *hic* pickin’ up dust in me’ camera roll."

    scene mollydrunk26
    with dissolve

    mo "*hic*"
    mo "Just gonna rest me eyes for a wee bit."
    mo "T’would be a shame if someone were ‘ta take advantage of me in ‘me drunken stupor."
    s "Yeah, I don’t think that will be happening tonight."
    c "Or any night."
    s "...Or any night."

    scene mollydrunk27
    with dissolve

    f "So what do we do now?"
    f "The party isn’t supposed to end for another few hours and I don’t think Molly can carry on much longer."
    c "Maybe there’s like, a guest room or something we could-"
    s "Nope. No guest rooms here."

    scene mollydrunk28
    with dissolve

    c "You checked already?"
    s "Yeah, earlier when I was setting the place up with Makoto. "
    s "The only spare room is full of...spare party stuff."
    c "You mean like extra chairs or something?"
    s "Yes. That is exactly what I mean."
    f "Well, I suppose we could ask Ayane if it’s okay to have Molly sleep in her room."
    s "That seems like a much better idea."

    if bonus == True:
        "I don’t even know if Makoto was able to dress herself after we finished having sex."
        "I can’t imagine that someone walking into a spare room and finding her laying there passed out and covered in semen would be a good look for either of us."
        "So...Sorry, Molly. Looks like you’ll need to travel a tiny bit further in order to get some rest tonight."

    mo "I’m fiiiiiiiiine. T’ings like t’is are bound ‘ta happen when ya have a bit much. "
    mo "I’ve got *hic* Irish, blood. I’m...ready to go!"

    scene mollydrunk29
    with dissolve

    if bonus == True:
        mo "‘Ye hear t’at, Sir? I’m *hic* ready to go. In more ways t’an one."
        mo "H-scene *hic* incoming~"
        c "I don’t know what an H-scene is but I feel like I don’t approve of it."
        f "You don’t. I can confirm that for you."
    else:
        s "Please calm down, Molly. Things might not be all that bad right now, but if you don't nip this drinking issue in the bud, next Halloween could be even worse."

    c "Maybe we should just leave her here after all?"
    f "Yes, I think that might be for the best."

    play sound "phonebeep.wav"

    "I feel my phone vibrate through my pocket and pull it to see that I’m getting a call from..."
    "Haruka?"
    "What does she want right now?"

    play sound "phonebeep.wav"

    scene mollydrunk30
    with dissolve

    s "Hello?"
    mo "Tch! Stupid phones. Stealin ‘me teacher away from me."

    if bonus == True:
        h "HEY, PENIS MAN."
    else:
        h "HEY, HUGGY BOY."

    s "…"
    s "Hello, Haruka."
    h "I’M DRUNK~"
    s "Yes, I can tell. "
    h "Wanna come fix my pipes?"
    s "I’m kind of in the middle of-"
    h "Maki’s pipes too~"

    play sound "phonebeep.wav"

    "I hang up the phone and turn back to the girls, ready to disappoint them."

    s "Duty calls."

    scene mollydrunk31
    with dissolve

    c "Huh? Who was that?"
    f "Is something wrong, Sensei? Are you leaving already?"
    s "A friend of mine is having a bit of an emergency and needs my help as soon as possible."
    c "Is everything okay? Because we’re having a bit of an emergency here as well."
    mo "I can *hic* stand. T’aint no emergency here."
    mo "I’m *hic* fine on ‘me own ‘til ‘me legs give out."
    mo "Help 'yer friend..."

    scene mollydrunk32
    with hpunch

    mo "BUT KNOW T'IS, SIR."
    mo "EVEN IF YE' LEAVE ME HERE FOREVER-"
    mo "I WILL ALWAYS LOVE YOU!"
    c "…"
    f "…"

    scene mollydrunk33
    with dissolve

    mo "T’s wit’ all ‘ta starin’? I saw him first so he belongs ‘ta me!"
    c "You were actually one of the last people to see him."
    f "Sensei doesn’t believe in love in the first place."
    s "As much as I’d like to stay here and argue over Molly’s love for me, I really do need to get going."

    if bonus == True:
        "Like Hell am I going to miss the chance for a threesome with Haruka and Maki, even if this room is packed to the brim with other equally cute girls."
    else:
        s "My friends are in trouble and I must pretend to know things about plumbing."

    scene mollydrunk34
    with dissolve

    c "Well, I guess we’ll...see you in[school] tomorrow then?"
    mo "I ain’t comin’ to *hic*[school] tomorrow."
    mo "Or ever again! I quit! "
    s "I’ll see {i}all three{/i} of you tomorrow. Tell the others I said goodbye."
    f "I hope everything turns out okay. "
    f "We’ll take care of Molly, so don’t worry about that."
    s "I’m not worried at all. Thanks, girls."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I use my phone to ping the closest cab and patiently tap my foot as I wait for it to show up at the Amamiya estate."
    "Haruka and Maki were all over each other at the bar last night, so I’d be excited going over there even if it was just to watch."

    if bonus == True:
        "I just hope this doesn’t wind up being some cruel practical joke where I’m actually being summoned to fix pipes."

    "…"
    "Wait a minute."

    if bonus == True:
        "Am I really about to have a threesome with Maki when I just took her daughter’s virginity like an hour ago?"
        "I deserve some sort of award for this, I think."
    else:
        "Did I leave my wallet in the bathroom?"

    $ renpy.end_replay()
    $ halloween14 = True

    "………"
    "……"
    "…"

    if haruka_lust >= 10:
        jump harukalust10

    else:
        jump harukalust10skip

label harukalust10:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```