# To Catch Me If I Fall (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Shelter](./beachmas20.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: slumberreset1
* Group: Main
* Triggered by label: postbeachmas1
* Chain sources: beachmas20
* Chain sources path: beachmas20->beachmas20

## Official wiki page

[To Catch Me If I Fall](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=slumberreset1&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label slumberreset1:
    $ totaldays += 1
    $ day = 3
    hide tuesday onlayer date
    show wednesday onlayer date

    scene poempoem1
    with dissolve2
    $ renpy.pause(5, hard=True)
    scene black
    with dissolve
    scene poempoem2
    with dissolve2
    $ renpy.pause(6, hard=True)
    scene black
    with dissolve2
    play music "goodmorning.mp3"

    "A noise at the front door pulls me from the first bit of rest I’ve been able to obtain since my eyes closed late last night."
    "I don’t have it within me to open them and find out who it is that may be coming to either greet me or chop my body into pieces and, honestly, I’m not sure which of those I’d even prefer right now."
    "I know you’re probably thinking it’s a bit too early for fatalism...and that I should just tear myself away from this much-needed slumber to either fuck or fuck off, but fuck you."
    "Christmas is over. The beach trip is over. And without any idea of what to look forward to or {i}when{/i} to look forward to it, this unfamiliar bed is nothing more than a chamber I can lock myself into stasis with."
    "Wake me up when this is all over- for I suddenly remember what it’s like to dream."
    "And I don’t like it."
    "I don’t like it at all."

    to "{i}Makoto! What are you doing?{/i}"
    mak "What does it look like I’m doing? I’m going to wake him up. That’s why we came here, isn’t it?"
    to "{i}Well...yes. But to traipse right on over to him without any regard for his personal space is rather...rude. Don’t you think?{/i}"
    mak "Does he even have any personal space {i}left{/i} after haphazardly distributing it between all twenty of us?"
    to "Mm. I suppose that is a fair point."
    to "Very well. Proceed. But know that I will not be able to help you if you are dragged under the covers in a fit of lustful, delirious rage."
    mak "I think I’ll manage."

    "The sensation of a fingertip repeatedly prodding at my cheek makes it clear to me that I am not about to be murdered or chopped up or whatever it is I {s}said{/i} thought before."
    "It’s unfortunate, really. For the last twelve or so hours and all of the thoughts and feelings brought on by them have reminded me of how much I hate feeling anything in the first place."

    play sound "static.mp3"
    scene christmasyay with flash
    stop sound

    "This graphic becomes relevant again."

    mak "Hey. You. Wake up. "

    "While it may not be the season anymore, I have a hard time believing its aftertaste will be departing my metaphorical tongue any time soon."
    "If only there was another that could coat mine with foreign saliva and a taste reminiscent of something more enjoyable."
    "Something like watermelon."

    scene makototoukawakeup1
    with dissolve2

    "But I suppose I’ll have to settle for this instead."
    "It’s just unfortunate since her spit is the only thing I {i}haven’t{/i} taken from her yet and watching her cling to her last bit of freedom has been nice thus far."
    "All good things come to an end, I guess."

    mak "Oh, good. You’re alive."
    s "Barely."
    mak "Long night? "
    s "Something like that."
    mak "Does it have anything to do with all of that crumpled up paper on the table? "
    s "Yeah. Decided to leave the beach early so I could grade all of the assignments Imani has been giving you. I’m turning over a new leaf."

    scene makototoukawakeup2
    with dissolve

    mak "Mhm. And I’m suddenly a lesbian."
    s "Congratulations, Makoto. "
    mak "Bite me."
    to "Um...good morning, Sensei. I’d ask if you slept well, but...I get the feeling that was not the case."
    s "And I get the feeling that I am waking up a lot later than normal right now."
    to "Last I checked it was about...1:00 PM. So I figured it would be best if I were to come here myself and make sure you were sleeping and not...well, dead."
    s "Why would you bring Makoto here if my death was a real possibility in your mind?"
    to "I obviously wouldn’t have been able to carry your body myself. You are exceedingly large for a Japanese man, Sensei."
    mak "Those papers...what are they?"
    s "What?"

    scene makototoukawakeup3
    with dissolve

    mak "They’re obviously not our assignments. And considering I haven’t seen you so much as {i}lift{/i} a pen in what feels like years, I’m a little...confused."
    mak "You haven’t started writing again, have you?"
    s "I don’t see why it matters."
    mak "It matters because it’s a substantial change in what I would call an...incredibly predictable life pattern."
    mak "That paired with the fact that you disappeared for an entire night suggests something big might have happened in-"
    to "Now, now, Makoto. I’m sure Sensei was just bored from having to spend the night in a brand new place without any of his...uhh...{i}belongings.{/i}"
    s "Belongings?"
    to "..."
    s "..."
    s "Are you talking about porn?"

    scene makototoukawakeup4
    with dissolve

    to "N...No! Though, I will admit that I am at least partially regretful in regard to not providing some sort of comparable...stash of magazines, as I am acutely aware of the male tendency to hide such material."
    s "There’s still time to right your wrongs, Touka."
    to "I’d really rather not."

    scene makototoukawakeup5
    with dissolve

    mak "Sensei, seriously. If you’re actually writing again, that’s a big step. And it’s one that I think we should talk about as it’s one of the reasons I always looked up to you in the first-"
    s "Drop it, Makoto. If I want to talk to you, I’ll talk to you. But I am currently in the process of waking up after maybe one hour of sleep and I just...don’t feel like it right now."

    scene black
    with dissolve2

    "There’s a moment of silence as Makoto and Touka both cease conversation and stare at me like I’m some sort of caged animal or art installation."
    "But as I lean up in bed, they’re reminded that I’m only slightly less human than the two of them- and they bring themselves to their feet as I do my best to mimic that."
    "The feeling of the bedroom’s tatami on my soles startles me at first due to the night and day contrast between that and the cold, hard wood I’ve grown accustomed to."
    "Each of them sense this and take a half-step forward to try and catch me in the event that I fall before realizing that they’re just being overly-cautious."
    "It’s annoying having people who care about you so much."
    "Though, I assume I wouldn’t be quite as annoyed if I understood why they’d want to prevent me from falling in the first place."
    "Some people are just naturally kind, I suppose."
    "..."
    "I wonder what that’s like."

    scene makototoukawakeup6
    with dissolve2

    mak "..."
    to "Is something wrong, Makoto?"
    mak "Hm? No. That painting just looks...eerily familiar."
    to "That’s likely because it was created by the same artist who painted the one I gifted you last Christmas."
    mak "Oh, good. So now {i}Sensei{/i} has a near-priceless piece of art. What a great person to trust with such an important item."
    to "Don’t be ridiculous. That one is a mere replica worth only a tenth of the original’s value. "
    mak "And where is the original? Your bathroom?"
    to "My dorm room, actually. You should come visit one day. It would be nice having someone else to keep an eye on Yasu from time to time."

    scene makototoukawakeup7
    with dissolve

    mak "Am I visiting as a {i}friend{/i} or a babysitter? Because that greatly influences my answer."
    s "Is my apartment your new hang-out spot or something? Are you two just going to chat here while I go on with my day?"

    scene makototoukawakeup8
    with dissolve

    mak "Oh, sorry. I forgot your self-esteem crumbles any time you’re not the center of attention."
    to "Sensei does make a good point, though. It is quite rude for the two of us to make plans without him while we’re guests in his home."

    scene makototoukawakeup9
    with dissolve

    mak "Don’t you literally own the building?"
    to "It is probably best if we do not discuss which buildings I do and do not own. I would not like to make anyone feel insignificant in the face of my family’s vast sphere of influence and wealth."
    mak "Yeah...it might be a little too late for that."
    s "So...question. What did you tell everyone when I disappeared last night? Because there’s no way our...{i}prolonged absence{/i} went unnoticed. "

    scene makototoukawakeup10
    with dissolve

    mak "I’m not really a fan of the way you said {i}prolonged absence{/i} right there..."
    to "It’s true that our absence was noted by several of the girls who tend to keep a closer eye on you, but I’m sure I needn’t remind you I wasn’t the girl you {i}initially{/i} ran off with."
    s "Yeah...and what happened to her as well? "
    mak "Who is “her?” Who are you running around with now?"
    s "I’m afraid that’s confidential, Makoto."

    scene makototoukawakeup11
    with dissolve

    mak "Yeah...what else is new?"
    to "I’m actually quite surprised to find out that she didn’t wind up here as well, considering she never made it back to the inn last night."
    s "What?"
    to "There’s no need to worry, though. Both Ayane and Ami have been in contact with her and she is fine."
    to "In regard to {i}your{/i} disappearance, you’ll be pleased to know that I handled it to the best of my ability and that there was only {i}one{/i} search party that sprouted up as a result of your disappearance."
    s "Oh, good. That’s not nearly as bad as it could have been."

    scene makototoukawakeup12
    with dissolve

    mak "Some say that Ami is {i}still{/i} out there to this day..."
    s "The day has barely changed, Makoto..."
    to "{i}Ahem.{/i} I believe this is the part where you praise me for both my reliability and proactivity. "
    mak "As if Sensei is going to praise anyone for literally any-"
    s "Great job, Touka. You’re a real life saver."

    scene makototoukawakeup13
    with dissolve

    to "Ah!"
    mak "Hey! What the fuck?!"
    to "You said my real name and everything!"
    mak "Praise me now! I’ve done way more for you than Touka has!"
    s "Makoto, she bought me an apartment."
    mak "Yeah, and I've...done things I can't repeat out loud! How much more do I have to do until that's worth an apartment?!"
    s "Fine, here. You’re very smart and very pretty and I’d be nowhere without you. Happy?"

    scene makototoukawakeup14
    with dissolve

    mak "M...Maybe."
    to "Do you have any other questions, Sensei? "
    s "Yeah. What did you tell everyone exactly?"
    to "That you had an important business meeting."
    s "In the middle of the night on Christmas?"
    to "That’s just how important the meeting was."
    s "And people actually believed it?"
    to "Oh, not at all. But just knowing that you were safe seemed to be enough for most of them."
    to "Apart from the one search party, that is. Which still contained roughly half of the class. But seeing as you’re still alive and well, I’d say everything worked out just fine!"
    to "It might be good to lay low for a while, though. Ami is very mad."
    s "Right..."
    s "Anyway, do you mind if I make a phone call? There’s someone I should probably, uhh...follow up with."
    to "Go right ahead. Makoto and I will step out onto the balcony once she regains her senses."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene makototoukawakeup15
    with dissolve2
    play sound "phonebeep.wav"

    m "Huh?"
    m "..."
    m "..."

    scene makototoukawakeup16
    with dissolve
    play sound "phonebeep.wav"

    m "Uhh...hi?"
    s "{i}Why do you sound so concerned?{/i}"
    m "Because you’re calling me? I don’t remember giving you permission to do that."
    s "{i}I didn’t realize I needed permission.{/i}"
    m "Well...what do you want?"
    s "{i}Why didn’t you ever go back to the inn last night?{/i}"
    m "You realize I could ask you the same exact question, right?"
    s "{i}Maya-{/i}"

    scene makototoukawakeup17
    with dissolve

    m "{i}Why the fuck do you think I never went back?{/i}"
    m "I obviously wasn’t acting like myself. I was...sick. Or something."
    s "..."
    m "..."
    m "Hello?"
    s "{i}I think we should probably talk about what happened.{/i}"

    scene makototoukawakeup18
    with dissolve

    m "Ugh...I hate talking."
    s "{i}I can assure you I hate it just as much.{/i}"
    m "I propose that we ignore it and go back to despising one another. "
    s "{i}That would certainly be the easiest route, wouldn’t it?{/i}"
    m "..."
    s "{i}Maya?{/i}"

    scene makototoukawakeup19
    with dissolve

    m "Yeah...uhh...I guess we can...{i}talk.{/i}"
    m "But I’m kind of-"
    s "{i}Great. Be at the park by my house in an hour.{/i}"
    m "Wait. I-"

    play sound "phonebeep.wav"
    scene makototoukawakeup20
    with dissolve

    m "Sensei? Are you still there?"

    scene makototoukawakeup21
    with dissolve

    m "Did he seriously just hang up on me?"
    ay "Hm? He? Did Sensei call?"

    scene makototoukawakeup22
    with dissolve

    m "Worse. He {i}hung up{/i} on me."
    ay "Is he okay? How did his business meeting go?"
    m "Business meeting? What business meeting?"
    ay "It was the excuse Touka gave for why he suddenly disappeared last night. "
    m "And you believed it?"
    ay "No. I just didn’t want to think about the alternative."

    scene makototoukawakeup23
    with dissolve

    m "Hah...well, whatever the case, we suddenly have somewhere else we need to be. Hurry up and eat your lunch so we can go."
    ay "Oh, I’m not hungry. But you can take as much time as you need and-"

    scene black
    with dissolve

    ay "Wait, where’d all of your food go? Weren’t there three full takoyaki boats right next to you a second ago?"
    m "I’m done. Let’s go."
    ay "Wow...One day, you’re going to tell me how you do that."
    m "Let’s focus on fixing the world first..."

    "........."
    "......"
    "..."

    scene makototoukawakeup24
    with dissolve2

    to "Tell me, Makoto...how large is this “shopping mall” exactly? My mother told me stories about them was I was younger, but I didn’t think I’d ever get to {i}see{/i} one."
    mak "I...wouldn’t get your hopes up too high. It’s not {i}that{/i} exciting. Though, I’m sure having Miku there will make it a lot more, um...{i}active{/i} than it would be otherwise."
    to "Splendid. I do hope Yasu doesn’t get lost along the way. It will be her first time riding a bus alone."
    mak "Sensei, if you don’t have anything else going on, why don’t you come with us?"
    s "When did you two get so close?"

    scene makototoukawakeup25
    with dissolve

    mak "When I realized Touka was a good person."
    s "And this sudden cheerful attitude...is that thanks to her as well?"

    scene makototoukawakeup26
    with dissolve

    mak "Who knows?"
    mak "Who {i}cares?{/i}"
    to "If you do come along, will you promise not to teach me any more fake commoner rituals like your exceedingly {i}hilarious{/i} vending machine chant? "
    s "I’ve got other plans, actually. Just made them while you two were out on the balcony."
    to "I see. Very well, then. "
    to "Tell Maya I said hello."

    scene makototoukawakeup27
    with dissolve

    mak "{i}Maya?{/i}"
    mak "Is {i}that{/i} who you were with before Touka showed up last night? "
    s "Thanks, Tomonori. I appreciate that."

    scene makototoukawakeup28
    with dissolve

    to "Of all the names, why did it have to be that one?!"

    scene black
    with dissolve2

    "The three of us leave the apartment together, but head in different directions once we make it to the street."
    "I’m still not sure what purpose this apartment will serve in my life considering I don’t plan on uprooting everything and just...keeping it here instead, but..."
    "It might be nice having somewhere quiet that no one really knows about."
    "Well, no one other than Makoto and Touka."
    "But those two are different from the rest of the class."
    "And I’m not sure if there is any amount of weight I could place on them that would cause them to break or bend."

    $ renpy.end_replay()
    $ slumberreset1 = True
    $ makoto_love += 1
    $ touka_love += 1
    stop music fadeout 15.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    jump slumberreset2

label slumberreset2:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
label postbeachmas1:
    "........."
    "......"
    "..."
    jump slumberreset1
...
```