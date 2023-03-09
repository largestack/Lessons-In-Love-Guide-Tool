# Loser
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukadorm5&go=Go)



## Event preconditions
✅Touka love greater than or equal to 5

✅Day of week is not Thursday

✅Event "[Touka: A Brief Moment in Time](./toukastreets5.md)" is completed (event=toukastreets5)



## Next events
* [Main: Operation: Firestarter](./day318.md)
* [Yasu: Repentance](./yasudorm10.md)

## Event properties
* ID: toukadorm5
* Group: Touka
* Triggered by label: toukadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label toukadorm5:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm2

    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Touka’s door and wait for her to answer. "
    "I saw Yasu leaving the building on my way in, so at least I’m going in there knowing that I won’t have to figure out how to deal with her this time around."
    "If Touka even lets me in, that is."
    "I realize she’s been starting to warm up to me, but it’s not like she particularly likes me very much yet. "
    "And without her roommate being around to provide whatever...sense of comfort someone like Yasu can provide, she may very well be completely opposed to this."

    to "The door is unlocked. You may enter."

    "Or she may not be opposed at all and will just invite me in without question. "
    "Nice."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene toukapjs1
    with dissolve
    play music "thesleepingcity.mp3"

    "I push open the door to find Touka dressed {i}significantly{/i} down compared to her usual self, and I can’t help but be taken aback for a moment."

    if bonus == True:
        "Not just because she looks like an almost entirely different person, {i}but because she is fucking stacked. Holy shit.{/i}"
    else:
        "I make sure to maintain my distance so I do not cause her any discomfort."

    to "Did you forget something?"
    s "Is that your way of asking me to compliment you?"

    scene toukapjs2
    with dissolve

    to "Wait, you’re not Yasu. "
    s "I am not."
    s "Yasu knocks on her own door?"

    scene toukapjs1
    with dissolve

    to "Yasu does many strange things. I’ve decided it’s best if I just stop questioning them altogether."
    to "What brings you here, Sensei? "
    s "Before that, don’t you want to take a second to get all embarrassed about being seen in your pajamas by a commoner?"
    to "Not particularly. I have a very nice body, as you may have noticed. "
    s "Oh I have definitely noticed."

    scene toukapjs3
    with dissolve

    to "Oh. So you {i}want{/i} me to be embarrassed. That’s how it is."
    s "I mean, a slight blush wouldn’t kill you."

    scene toukapjs1
    with dissolve

    to "Well I apologize, but I will not be blushing or awkwardly avoiding your gaze tonight, for I am the picture of perfect health for a girl my age."
    s "Well, you...certainly take after your mother in at least one area."
    to "Is that any way for an educational professional to be talking to a student?"
    s "Not really. But Tsubasa already said you have to listen to me and-"
    to "I know what she said. "
    to "And if you’ve come here to belittle me some more or hold her words over my head, please have the decency to do it some other time."
    s "What if I’m here to say a bunch of nice things about you instead?"
    to "You? Act out of genuine kindness rather than self interest or curiosity? "
    to "I haven’t been here very long, but even I find that statement laughable, Sensei."
    to "…"

    scene toukapjs4
    with dissolve

    to "Though...it would make me feel a {i}little{/i} better, I suppose."
    s "Is something wrong? You seem less...pompous than normal tonight."

    scene toukapjs5
    with dissolve

    to "Do you expect lacing your concern with ridicule to gain you any favor in this conversation?"
    to "Look at me for a moment. Not at my chest, but at me. "
    to "Does it {i}look{/i} like something is wrong?"
    s "I mean, kind of. Yeah."
    to "Then it is safe to assume that something is wrong. There’s no need to ask."

    scene toukapjs6
    with dissolve

    to "How unfortunate that the one area I hoped you’d handle differently is the sole area that you approach the same way as everyone else."
    s "…"
    s "Do you want to be left alone or something?"

    scene toukapjs7
    with dissolve

    to "If that’s what you think is best."
    to "Though, if you’d like to keep me company instead, I won’t reject it."
    to "It’s not like anyone else is going to be knocking on the door anytime soon."

    "Ahh, so this is more of that."
    "I guess it would be exhausting or depressing or whatever else you want to call it if you go from having the world served to you on a silver platter to browsing the Internet all by yourself each night."

    s "Still having a hard time blending in?"
    to "…"
    s "…"

    scene toukapjs8
    with dissolve

    to "May I stand?"
    to "It’s impolite for me to let this conversation carry on while appearing so informal. I should be facing you, at the bare minimum."
    s "You don’t need to handle everything so formally. If you want to sit, that’s fine."
    to "If I wanted to sit, I would not have asked if it was okay for me to stand."
    to "So, with that in mind, may I stand?"
    s "I...I guess?"

    scene toukapjs7
    with dissolve

    to "Thank you very much."

    scene black
    with dissolve

    "Touka closes out a window on her laptop to prevent me from seeing it. But I highly doubt it was anything unsavory based on her posture."
    "She straightens out her tanktop and pats the sides of her leggings to smooth out any creases before taking her place a foot or two in front of me."

    scene toukapjs9
    with dissolve

    to "To answer your question, yes. I’m still having a hard time blending in."
    to "I realize that I am likely just impatient, but it is not a good feeling walking into class each morning and knowing that you are being judged despite doing absolutely nothing at all."
    to "I know I say strange things from time to time that “normal” people would laugh at, but I have yet to say enough to any of the other girls to warrant laughter whatsoever."

    scene toukapjs10
    with dissolve

    to "I probably would have been better off if none of them had a history at Kumon-mi Academy."
    to "But the fact that some did...means that I arrive here with not just a head full of hope and a heart full of naivety-"
    to "But an extensive background of preconceived notions and expectations that were not swallowed along with everything else the sinkhole claimed."
    to "I did not have any friends in my last[school], as I’m sure you know."
    to "I attended my own classes and had my own teachers, and communicating with me in general wasn’t prohibited or anything like that, but..."
    to "It didn’t seem like anyone ever wanted to do it. "
    to "Like they saw me as some girl that they could get in trouble for approaching, even though I’d smile and wave at every single student who walked past my window."

    scene toukapjs11
    with dissolve

    to "I’m sure that me complaining like this means absolutely nothing to you...especially now that I know how hard some people in our class have it."
    to "But the fact that I can still feel people looking at me and immediately jumping to the idea of “it must be so easy to be her” stings more than I ever imagined it would."
    to "I do not expect you to numb that sting."
    to "And I do not particularly expect you to care."
    to "But I do ask that you, at the bare minimum, acknowledge that I am not perfect or unwavering."
    to "I am a {i}real{/i} girl with {i}real{/i} feelings."

    scene toukapjs12
    with dissolve

    to "And I would very much like {i}real{/i} friends so I don’t have to spend so much time sitting in my room by myself."
    s "..."
    to "..."
    s "You’re crying again."
    to "Yes. I have been crying a lot lately. Please stop pointing it out."
    s "I don’t have a problem with it or anything. I actually think it’s cute."

    scene toukapjs13
    with dissolve

    to "My sadness is not cute! It is sad! Feel bad for me!"
    s "No, I just mean it’s nice being reminded that you {i}are{/i} an actual person and not some rich girl stereotype like I thought you were at first."

    scene toukapjs14
    with dissolve

    to "Ha..."
    to "I did some research on the stereotypical views people have of girls like me and can confirm that, to at least some extent, I fit the bill depressingly well."
    to "But simply not knowing how things work around here does not make me any less deserving than anyone else."

    scene toukapjs15
    with dissolve

    to "But...{i}ahem{/i}!"
    to "I should not be airing out those worries in front of you."
    to "I have learned through experience that letting my emotions get the best of me scares off those who have been selected to teach me."
    s "So you’ve gone from trying to get me fired to fighting off tears in an effort to keep me. And in just a few short dorm visits, too."
    to "I have given you the benefits of many doubts and will continue to do that until I no longer find it constructive."

    scene toukapjs16
    with dissolve

    to "And I will admit that I felt myself gradually slipping toward just that, but airing out more of my worries tonight has quelled the storm for at least the time being."
    to "It was also very nice of you to not interrupt me during my explanation."
    s "I can be serious when I have to be. Besides, it’s weird seeing you not acting...weird."
    to "I’m sure it came across as quite a shock at first, but I’m already feeling a little better now that I’ve gotten to talk about it."
    to "Yasu and I have been doing a little better too, in case you were wondering."
    s "Oh yeah?"
    to "We’re still nowhere near companions, but I no longer feel as if she is going to kill me in my sleep. Which is a dramatic improvement, if I do say so myself."
    s "Wow, you’re already braver than I am then."

    scene toukapjs17
    with dissolve

    to "Hahah! I suppose I am."

    scene toukapjs18
    with dissolve

    to "Okay. Now that the sad part is out of the way, I suppose there’s no longer a reason to stand."
    to "Let’s take a seat and talk a little more if you don’t mind."
    to "I have plenty of time to do this because I am what most people here would call a “loser.”"

    scene toukapjs19
    with fade

    "Touka sits down on an expensive looking ottoman and I find a place beside her."
    "There isn’t much room on it, so we need to sit relatively close together. But she is the one who chose this seat and so she is the one that must pay."

    if bonus == True:
        "I am absolutely not deterred at all from being so close to such an...endowed [teenage]girl."
        "Yup. Feeling totally normal right now."

    to "So..."
    to "Now what do we do?"
    s "We can keep talking about you, I guess. We seem to be on a roll in that regard."
    to "Is there anything in particular you’re interested in hearing?"
    s "I’m going to preface this by saying I mean it in the least offensive way possible-"
    to "Oh, wonderful. What a great sign."
    s "...But was there anything difficult about your life outside of Kumon-mi Academy?"
    s "I know you mentioned losing teachers and have an apparent disposition to the word “princess-”"
    to "But you want to know what the worst of the worst is."
    s "Right."
    to "I see."
    to "Yes, I suppose I would also be curious if I came across someone who I imagined was simply breezing through life without any issues whatsoever."

    scene toukapjs20
    with dissolve

    to "But the question you ask can not really be answered in a simple manner, as it’s been something I’ve been dealing with since I was born."
    s "Please don’t tell me you’re going to admit to having some sort of terminal disease now that we're finally starting to get closer."

    scene toukapjs21
    with dissolve

    to "I’m afraid that’s exactly what I’m about to do."
    s "What-"
    to "The disease of being born a woman to someone who, more than anything, wanted a male heir."
    s "Jesus, don’t call that a disease. I thought you were dying for a second."

    scene toukapjs22
    with dissolve

    to "The Tsukioka family is very much one of tradition."
    to "We’re wealthy now due to the entrepreneurial spirit of my grandfather-"
    to "But even before then, there were long periods of great wealth for the family that can be traced all the way back to the early Edo period. "
    to "And one thing that virtually every single iteration of the family held true to...was bearing no more than two children per every male figurehead. "
    to "As such, the first male born to every father would go on to inherit everything possessed by them at the time of their death."
    to "But seeing as my father has already had two daughters and will not break family tradition, that responsibility defaults to me as the first born. "
    to "Even though I’m not the gender he wished for."
    s "And you’d call that the hardest part about your life?"

    scene toukapjs23
    with dissolve

    to "I was born in a very fortunate place in time to a very fortunate family."
    to "It’s just unfortunate that I must work harder for my father’s approval than I would have had to if I had been born looking the way he desired."
    to "He's a good father...and he does love me."
    to "But sometimes, it feels like the only way to make him proud at all is to surrender myself to the male heir of some other family with even greater power than ours."
    to "Of course the issue with that is that there are no males anywhere and that I absolutely would not want to get married right now."

    scene toukapjs24
    with dissolve

    to "Maybe one day, though."
    to "I can only imagine how excited you are to be married into the Amamiya family."
    s "…"
    to "…"

    scene toukapjs25
    with dissolve

    s "Hah..."
    to "Did I say something wrong?"
    to "I apologize if I killed the conversation, but she seemed so excited at the prospect of settling down with you and-"
    s "Didn’t I tell you to not believe anything Ayane says?"
    to "If it was just her word, I’d understand but..."
    to "Ever since running into you two at the dojo, I felt some sort of connection."
    to "Do you mean to tell me there is nothing there?"
    s "I mean to tell you that if there is, it doesn’t concern you. And wouldn’t be something I’d want to talk about even if it did."

    scene toukapjs26
    with dissolve

    to "I’m very sorry...I meant no offense. "
    to "I was just interested in hearing a little more about how you intend to spend the rest of your life."
    to "My path is mostly clear, so...hearing how things are for those who have not been born into set courses...sometimes makes me feel rather warm inside."
    to "But if that’s not an area you’d like to touch on...I will respect that."
    s "Let’s just...move onto something a little different."

    scene black
    with dissolve2

    "Touka’s idea of “something different” is telling me more about her family’s history which, and this might come as a surprise, {i}I’m not very interested in.{/i}"
    "But she does seem to enjoy talking about it and...I do enjoy sitting next to her and {i}watching{/i} her talk about it, so I don’t try to stop her."
    "I let her talk until her mouth gets dry and she needs to get a drink from the vending machine outside."
    "I follow her into the hall as it’s getting late and I should probably be heading home anyway."
    "But I don’t leave until I confirm to myself that she is still doing the vending machine power pose I taught her the other day."
    "I’m so proud of her. "
    "And so excited for her to find out from a very confused classmate that she has been making herself look like an idiot for quite some time now."
    "Fortunately, she’s a very cute idiot."
    "And I find myself becoming more interested in her with each passing day."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm5 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label yasudorm10:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label toukadorm:
    if touka_love >= 1 and day != 4 and toukafirsthall == True and toukadorm1 == False:
        jump toukadorm1
    if touka_love >= 5 and day != 4 and toukastreets5 == True and toukadorm5 == False:
        jump toukadorm5
...
```