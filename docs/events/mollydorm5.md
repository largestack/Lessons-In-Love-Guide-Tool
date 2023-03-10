# Torrent of Power (Molly)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Molly love greater than or equal to 5

* Event [NTR & Pregnancy](./mollycafe1.md) (Molly) is completed)



## Next events

* [Molly: Something Out of a Nukige](./mollycafe10.md)
* [Molly: The Dark Entity](./mollydorm10.md)

## Event properties

* Id: mollydorm5
* Group: Molly
* Triggered by label: mollydorm
* Triggered by branch label: mollydorm
* Triggered by path: mollydorm->mollydorm5

## Official wiki page

[Torrent of Power](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollydorm5&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm5:
    play sound "knock.mp3"

    "I knock on Molly’s door and wait to see if she responds. "
    "Honestly, I’m not even sure if she’ll be around today...but it’s worth a shot I guess..."
    "I know she works night shifts at the cafe, and it’s not like there’s really any reason for someone other than her or Tsuneyo to come up here for the time being..."

    if bonus == True:
        "But hey, maybe I’ll luck out and she’ll be the leader of some cool lesbian orgy club or something."
        "That would be neat."

    mo "Who goes there?! "
    mo "Have you come to vanquish me?!"
    mo "Prepare yourself, mortal! For I, Molly MacCormack-"
    s "Molly, it’s me. I’m not here to vanquish you."
    mo "That...That voice..."
    mo "Could it be?..."
    s "...Could it be what?"
    mo "Come in..."
    mo "The preparations have already been made."

    scene black
    with dissolve

    "...What preparations?"

    play sound "dooropen.mp3"

    "I sigh to myself and push open the door to Molly’s room."
    "………"
    "……"
    "…"

    scene firstmollydorm1
    with dissolve

    if tsuneyodorm5 == True:
        "I step into Molly’s room and take in the scenery yet again."
        "I hadn’t really paid much attention to Molly’s side of the room when I came to visit Tsuneyo, but now that I’m actually observing it, it seems..."
        "Expensive."

    else:
        "I step into Molly’s room and am greeted by, more or less, exactly what I expected to see."
        "Her side of the dorm is equipped with a bunch of anime memorabilia, a nice looking computer, and several weird looking chairs."
        "While Tsuneyo’s side is..."
        "Well, it has noodles."

    scene firstmollydorm2
    with dissolve

    mo "Hello and welcome to Casa Del Molly! Otherwise known as the “Sanctuary!”"
    s "I’m pretty sure this is just Dorm #6."
    mo "Tomato, tomato."
    s "That phrase really doesn’t have the same impact when it’s spelled out."

    scene firstmollydorm3
    with dissolve

    mo "Whatcha up to, Sir? I’m assuming you’re here for a reason, right? "
    mo "It’s not like a teacher would just visit a [young_girl]’s dorm room just to hang out."
    s "…"
    s "Actually, Molly. I think there’s something you might have to learn about me."
    s "I sort of do this with everyone. Just...show up at their room and get them to kill time with me, I mean."

    scene firstmollydorm4
    with dissolve

    mo "You’re allowed to do that? There aren’t like, rules against guys in girls’ dorms and stuff?"
    s "If there are, I’ve broken them probably several hundred times by now."
    mo "Wack."
    s "You don’t have a problem with it, do you? I know we haven’t really spent much time together but-"

    scene firstmollydorm5
    with dissolve

    mo "Of course I don’t have a problem with it! If anything, this is an excellent development! A great chance to prove my worth!"
    mo "Tell me, Sir. Do you like scantily dressed women? Some even stripped down to their underwear?"

    if bonus == True:
        s "Is this a trick question? Because I feel like this is a trick question."
        mo "No tricks here, Sir. Just degeneracy."
        mo "As it just so happens, I have quite the collection of anime figures, and several of them are wearing next to nothing!"
        s "Oh, those. Yeah I can see those from here. I’m not really into that, to be honest."
    else:
        s "Ew, no. That sounds gross. I only like fully clothed women with a complete disinterest in any form of relationship apart from hug-based ones."

    scene firstmollydorm6
    with dissolve

    mo "Whaaaaat? Not even a little? But I spent so much money on them."

    if bonus == True:
        s "Who spends that much money on plastic anime girls?"
    else:
        s "On women? I am calling the police."
        mo "No, Sir. Anime figures."
        s "Clarify that beforehand, you lunatic."
        s "Do you really spend that much money on them?"

    scene firstmollydorm2
    with dissolve

    mo "I do. And I regret nothing."
    mo "In fact, I’m prepared to spend every penny I earn for the rest of my life on fueling my hobby."
    s "You should probably put together a steady source of income first."
    s "I can’t imagine your part time barista gig will be enough to fuel a hobby as expensive as that."
    mo "I’ll figure out a way to make it work. I won’t have time for games and stuff if I get a full-time job."
    s "Well, just keep in mind that you’ll only be able to live in the dorm for another couple years."
    s "After that, it’s either find work or get used to living on the streets."
    mo "I wouldn’t fare well on the streets. I’ve only known Japanese for a couple years."
    s "Wait, really? You have a bit of an accent, but your pronunciation is spot-on."
    mo "Never underestimate the power of learning through anime, Sir."
    mo "Combine that with language exchange chat rooms and you have one happy, informed weeb, Sir."
    s "Molly, can you please explain to me what a weeb is? I suddenly feel the need to be informed. "
    mo "Are you sure, Sir? What if some plebeian complains about it in the comment section?"
    s "What comment section?"
    mo "No idea, Sir. But here is your daily weebnote! "
    mo "Weebnote: A weeb is any non-Japanese person who becomes obsessed with anime and Japanese culture to the point where it becomes almost cringeworthy."
    s "So like, a foreign otaku?"
    mo "Precisely. "
    s "I don’t really see a problem with that. People like what they like."

    scene firstmollydorm7
    with dissolve

    mo "If only everyone else looked at things that way."
    mo "I can’t even cosplay at conventions in Japan without people lookin’ at me all weird and stuff."
    mo "I’m lucky enough that the manga club accepts me, but even that I kinda had to beat my way into."
    s "Oh come on. That can’t be true. Ami and Rin are in that club and they’re accepting of pretty much everyone. "
    mo "That’s true. But even then it’s like, I can’t help but feel like they looked at me a little weird at first."

    scene firstmollydorm2
    with dissolve

    mo "But hey! They’re two of my best pals ever now and I couldn’t be happier to be livin’ out my dreams in the land of the rising sun!"

    "Interesting."
    "I guess Molly’s just seemed so...overly-confident so far that it never really occurred to me that there was a time where she felt out of place."
    "But I can absolutely understand why."
    "It must be hard looking different than everyone else. Especially in a place as closed off as Kumon-mi. "

    if ayanedorm15 == True:
        "In fact, I remember Ayane telling me something a while back about how outsiders aren’t really as accepted here as they probably should be."
        "And even then, she was talking about Japanese outsiders from different prefectures."
        "I can only imagine what it’s like for someone from a completely different country."

    else:
        "But I guess foreigners are bound to be looked at strangely no matter where they are. That’s just human nature, unfortunately."

    mo "Well, uhh, anyway! How do {i}you{/i} feel about cosplay, Sir?"
    mo "Are you one of those people who thinks it’s embarrassing? Or are you one of those people who thinks it’s the greatest thing ever?"
    s "Is there no middle ground?"
    mo "There is not."
    s "Oh. Well it wouldn’t matter anyway because I’d definitely choose option two."

    scene firstmollydorm4
    with dissolve

    mo "Really? Even though you don’t like anime and stuff?"
    s "You don’t need to like anime to appreciate girls in cute costumes. And I very much appreciate that."

    scene firstmollydorm2
    stop music fadeout 10.0

    mo "Then perhaps you can still be saved after all..."
    mo "For you see...I, Molly MacCormack, am a self-proclaimed master-cosplayer!"
    s "Adding “self-proclaimed” to the title really takes away from how impressive it is, but I can’t say I’m not intrigued. "
    mo "Would you like to see a little sample?"

    "Fuck yes I would. But it’s not like I can just come out and say-"

    s "Fuck yes I would."

    "Damnit."

    scene firstmollydorm9
    with dissolve

    mo "Excellent...{i}Excellent{/i}."
    mo "Then...If you would be so kind as to follow me to the bed...We can get started."
    s "Yes please."

    scene black
    with dissolve

    "Molly shyly turns around and hops onto her bed."
    "I follow quickly behind her and she-"

    scene firstmollydorm10
    with hpunch
    play music "rapid.mp3"

    mo "{i}Darkness blacker than black...darker than dark...{/i}"
    mo "{i}I beseech thee...combine with my deep crimson.{/i}"
    mo "{i}The time of awakening cometh!{/i}"
    s "Uhh..."

    scene firstmollydorm11
    with dissolve

    mo "{i}Justice fallen upon the infallible boundary...{/i}"
    mo "{i}Appear now as an intangible distortion!{/i}"
    mo "{i}I desire for my torrent of power...a destructive force!{/i}"
    mo "{i}A destructive force without equal!{/i}"
    mo "{i}Return all creation to cinders and come out from the abyss!{/i}"

    scene firstmollydorm12
    with dissolve

    mo "{i}EXPLOOOOOOOO...SION!{/i}"
    s "…"
    mo "…"
    s "…"
    mo "…"
    s "…"
    mo "…"

    scene black
    with dissolve
    stop music fadeout 5.0

    "Molly drops her staff and hops off of the bed, skipping over to her computer desk."

    scene firstmollydorm13
    with dissolve
    play music "sweetvermouth.mp3"

    mo "So? Whaddya think? Pretty cool, right?"
    s "I mean...it was a cool monologue. But I don’t really know if I would count just a staff as cosplay."

    scene firstmollydorm14
    with dissolve

    mo "That’s where you’re wrong, Sir. A good cosplayer must not only wear the costume, but embody the personality of the character as well."
    s "Okay, sure. But there was no costume at all."
    mo "The costume is in my wardrobe."
    s "…"
    mo "…"
    s "Are you going to put it on?"

    scene firstmollydorm15
    with dissolve

    if bonus == True:
        mo "R-Right now?...With you just...standing there watching me?"
        mo "I know that you’re my master, but this is..."
        s "Actually, on second thought, don’t worry about it. I’m sure I’ll see it eventually and I imagine that speech took a lot out of you."
    else:
        mo "Right now?"
        s "Of course not. When you are in private and do not feel any discomfort as a direct result of my presence."
        mo "Oh. Probably."
        s "Cool. Also, nice speech."

    scene firstmollydorm14
    with dissolve

    mo "I’ve practiced it like two-hundred times. In fact, Tsuneyo probably even knows it now from how much I’ve been doing it lately."
    s "I...would very much like to see her attempt to do what you just did."
    mo "We will convince her together."
    mo "She’s gorgeous so I wanna see her get dressed up too."
    mo "And Ami."
    s "My Ami?"
    mo "Your Ami. She’s been wanting to cosplay for a while and we’re close to the same size, so I’m gonna let her try on some of my stuff."

    if bonus == True:
        s "Please, for the love of god, show me when you do."
        mo "I will have her send pictures. "
        s "Thanks Molly. I had no idea you were such a great-"
        mo "500 Yen each."
        s "...Salesman."
        mo "I learned from a wise man that I must start making more money as soon as possible or I will be forced to live on the streets. "
        s "…"
        mo "…"
        s "500 Yen each?"
        mo "500 Yen each."
        s "Deal."
    else:
        s "Just make sure the fabric isn't too scratchy. She has soft skin and I do not want her to get hurt."
        mo "I understand, Sir. I will take good care of her."

    scene black
    with dissolve2

    if bonus == True:
        "Molly and I shake hands and I feel like I’ve just agreed to doing something very suspicious."
        "But hey, suspicious is pretty much my middle name at this point. "
        "And if the only thing separating me from seeing a bunch of cute girls in costumes is some pocket change, so be it..."
        "..."
        "I would have probably even paid more if she asked."
    else:
        "Molly and I shake hands. I am glad that she is going to protect my accountant."

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollydorm5 = True
    stop music fadeout 5.0

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mollydorm10:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label mollydorm:
    if molly_love >= 5 and mollycafe1 == True and mollydorm5 == False:
        jump mollydorm5
...
```