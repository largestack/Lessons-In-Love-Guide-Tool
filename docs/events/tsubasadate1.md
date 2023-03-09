# Everbloom
Tsubasa event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsubasadate1&go=Go)



## Event preconditions
✅Tsubasa love greater than or equal to 0

❌Event "[Touka: Something Less Lonely](./toukaspecial15p3.md)" is completed (event=toukaspecial15p3)

❌tsubasanumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: tsubasadate1
* Group: Tsubasa
* Triggered by label: calltsubasamorning
* Triggered by branch label: callmorning

## Event code
File: \game\TsubasaEvents.rpy
Code:
```python
...
label tsubasadate1:
    play sound "phonebeep.wav"

    "I tap on Tsubasa’s name in my phone and wait for her to answer."
    "Is it weird for me to be casually phoning the wealthiest woman in all of Kumon-mi first thing in the morning? Yes."
    "But after many phone calls with Ayane, who I believe is in second place after the entirety of the Tsukioka family’s women, I think I’m prepared."
    "Especially after hearing how Tsubasa’s been itching to start sneaking away from her normal life again."
    "Well, {i}itching{/i} probably isn’t the most accurate description of her feelings- but it makes me feel a little more like she’s doing this to see me and not just to feel...un-rich for a short burst of time."
    "Oh well. I guess we’ll just have to see how things play out. "
    "Here’s hoping that I can provide her a bit more entertainment than her husband can."
    "Interpret that however you want."

    play sound "phonebeep.wav"

    tb "Well, hello. I can’t say I was expecting you to call so soon after exchanging numbers."
    s "Just deciding to switch things up a bit. Are you doing anything today?"
    tb "I’m afraid I am. Well, at least in some sense. "
    tb "I’m mostly free so long as I remain at home. But I must remain nearby in the event that I’m needed for anything involving the acquisition of another hotel for the brand."
    s "Expanding your empire this early in the morning?"
    tb "Yes, well, Tsukasa was so smitten with the red-ish light district the other day that she insisted we move into that part of the city as quickly as possible."
    s "I guess I should call back some other time, then?"
    tb "I suppose. Unless you’d be willing to make the trip here, of course."
    s "I don’t think I own any clothes nice enough to really look the part."
    tb "Oh, I wouldn’t worry about that at all. It wouldn’t be the first time we’ve opened up parts of the manor for a tour. "
    tb "And seeing as I’m here, I could serve as your personal guide. It would be my thanks for your recent assistance in what is soon to be the next section of a corporate takeover."

    "Is it really okay for me to go to Touka’s house without receiving her blessing?"
    "Probably not. But I’m going to do it anyway because I want to make her life harder and Tsubasa and I are technically friends or something now."

    s "Send me the address and I’ll head over, I guess."
    tb "Splendid! I’ll have someone pick you up at the gate once you arrive."
    tb "See you soon."

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "So, I guess I’m going to have to meet up with some random person first if I’m going to make my way into the Tsukioka manor."
    "With my extremely limited knowledge of rich people, however, I assume that’s just par for the course."
    "All I can really do at this point is hope that A) Touka doesn’t find out. And B) That Touka’s {i}father{/i} doesn’t find out."
    "From what I understand, their relationship isn’t really as strong as it once was, but I would imagine it’s at least strong enough to not want his wife inviting other men over just yet."
    "Yet again, though, I’m wrong just as often as I’m right."
    "He could very well be into that sort of thing."
    "Or I could very well be walking into a death trap."
    "There’s only one way to find out."

    play sound "phonebeep.wav"

    "I receive a text from Tsubasa with her address and, after doing a quick search online to figure out exactly where she lives, I begin to make my way over."
    "........."
    "......"
    "..."

    scene tsubasatour1
    with dissolve2
    play music "tsukiokamanor.mp3" fadein 3.0

    "Upon arriving at the Tsukioka residence, I’m escorted through several different gardens, ultimately leading to one much {i}bigger{/i} garden where Tsubasa is hanging out."
    "She diverts her attention away from the crystal clear waters of a manmade pond I will never be able to afford and sets her sights on me- a man so clearly out of place that it must be comical to her."
    "It was certainly comical for me the other day, so I see no reason to disbelieve things wouldn’t be the same when flipped on their head."

    tb "Welcome. I take it you found the manor okay?"
    s "Why do you have so many gardens?"

    scene tsubasatour2
    with dissolve

    tb "In case one breaks down, of course."
    s "..."

    scene tsubasatour3
    with dissolve

    tb "I’m sorry- was that not funny? My husband always laughs at that joke."
    s "Always? Meaning you have told it more than once?"
    tb "When you’re married and spend nine tenths of your life in one place, you tend to run out of material."
    s "Well, either your husband has a horrible sense of humor or he’s just trying to make you feel funny."

    scene tsubasatour4
    with dissolve

    tb "It’s likely the former, to be quite honest."
    s "On a related note, does he know I’m here?"

    scene tsubasatour5
    with dissolve

    tb "Why do you ask?"
    s "I’d just feel a little weird personally if my wife invited some guy to my house without telling me."
    tb "You’re married? I had no idea."
    s "What? No. That was rhetorical."
    tb "You’re not married?"
    s "Do I really look like the married type to you?"

    scene tsubasatour2
    with dissolve

    tb "No. Which I suppose would make my darling Chika very happy for the time being."
    s "Was that supposed to be a joke as well? Because, if so, you’re zero-for-two so far."
    tb "Less of a joke and more of a...wistful observation."
    tb "And, to answer your question from earlier, my husband does not know you’re here."
    tb "He’s very busy and, with a house this large, I doubt we’d be able to find him even if we tried."
    s "What a wonderful problem to have."
    tb "Apologies again for not being able to step away, but I’m sure you’ll come to find that there’s plenty to do on these grounds. And I’m not just talking about gardening, of course."

    scene tsubasatour1
    with dissolve

    tb "What I would suggest, seeing as this is your first time here and all, is a brief tour of the premises. We should be able to cover at least half of it today if we begin now."
    s "I was kind of figuring this would be more of a “You and I just hang out and talk” type of thing."
    tb "Can we not do both?"
    tb "I see this is as an...introduction to my world. And if my world isn’t interesting to you, who’s to say the two of us would find any joy in talking at all?"
    tb "To understand each other, we must first know where the other comes from. And it would bring me a great deal of joy knowing you’d at least humor me in indulging this thought of mine."
    s "So instead of sneaking away today, you’re deciding to turn around and run head first into the thing you’re interested in getting away from?"
    tb "“Sneaking” is only exciting if it’s on occasion, Sensei. If I were to entirely abandon this life, it would be more akin to simply {i}running{/i} away."
    s "Well, it doesn’t seem like I really have any say in this to begin with, so I’ll accept your tour of wealth and try my best to look impressed as you show me all of the nice things you have."

    scene tsubasatour6
    with dissolve

    tb "Fantastic."
    tb "Oh, and if we bump into Touka, just pretend you do not see her. She’d be very embarrassed knowing you’d come to visit her home without her knowledge. "
    s "She’s here?"
    tb "Perhaps. She {i}does{/i} live here, after all. "
    tb "She may be getting more accommodated to life in her dorm room, but that can’t compare at all to what we’ve built over the years."

    scene tsubasatour1
    with dissolve

    tb "But I’m sure you’ll understand by the end of the tour."
    tb "Now, shall we go?"

    scene black
    with dissolve2

    "Tsubasa peels herself away from a bridge I’m sure she spends hours a week looking out over in a mix of admiration and longing."
    "She takes a place beside me, one that I imagine was filled much more frequently by the man she fell in love with at a younger age, only to have it go vacant in years subsequent. "
    "I can not tell if she’s comfortable or not, but it wouldn’t change my position either way if she isn’t."
    "I exist to fill the holes others can not fill on their own- whether they want them there or not."
    "Whether they want me there or not."
    "Whether I want to be there or not."

    scene tsubasatour7
    with dissolve2

    tb "Tell me, do you notice anything different about {i}this{/i} garden compared to the several others you’d passed on your way to me?"
    s "Not really, no."
    tb "{i}Well,{/i} the key difference between this and the others is that {i}this{/i} particular rock garden has been around since the Edo period. "
    tb "The Tsukioka family is one dating back to the origins of Kumon-mi, and this garden has been {i}mostly{/i} untouched for all of its history. "
    tb "And despite not being born into this family, I’ve taken quite a liking to it. There’s something very special about history, whether it be familial or personal."
    tb "And I remember the first time I ever saw this garden as if it’s the back of my hand."
    s "You wear gloves like 90%% of the time, Tsubasa."

    scene tsubasatour8
    with dissolve

    tb "Well...yes. But that doesn’t mean I don’t remember what my own hands look like, Sensei."

    scene tsubasatour9
    with dissolve

    tb "The first time I ever saw this garden was on a trip to meet my husband for the first time."
    tb "Arranged marriages are still very common in our world, you see. And before I was even introduced to Tomonori, I fell in love."
    tb "Even being from an almost equally affluent family, I’d never seen something like this in one’s own residence before."
    tb "And I suppose it may make me sound a bit materialistic, but I had no intention of abandoning a place like this from the moment I laid eyes on it."
    s "So what you’re telling me is you married your husband for an old rock garden?"
    tb "What I’m telling you is that I married into a family I wanted to be a part of. That I wanted to continue carving out a name for. And I likely would have done that even if my husband wasn’t a good man."

    scene tsubasatour10
    with dissolve

    tb "But I got lucky. He {i}was{/i} a good man. And we made two beautiful daughters together. Daughters who will, one day, walk through this rock garden with their prospective husbands."
    tb "Who will ultimately bring more people into our world. More people to fall in love with the history."
    tb "What makes this particular garden so different is that it’s a physical reminder of all of that, Sensei. "
    tb "It’s something I can look out on while pondering what the other women who married into the family felt about it."
    tb "Generations of people, all witnessing the same thing at different points in time..."
    tb "If that doesn’t sound magical to you, I don’t know what will."
    s "..."

    scene tsubasatour11
    with dissolve

    tb "Just kidding. I know {i}exactly{/i} what will."
    tb "Now, if you’ll follow me-"

    scene black
    with dissolve2

    "Tsubasa leads me through the rest of the garden and over to a large building resembling a shrine."
    "She removes an old, rusted key from somewhere inside of her sleeve, sliding it into the door and slowly pushing it open."
    "The doors creak as if they haven’t been opened in centuries, but upon stepping inside and seeing how clean and well-kept everything is, I know that can’t be true."
    "And she was right."
    "This does seem magical."

    scene tsubasatour12
    with dissolve2

    "Magic isn’t real, though. "
    "And I know that, behind whatever history {i}this{/i} room holds, it’s just another room at the end of the day."
    "It doesn’t matter who died here or who {i}will{/i} die here- it’s an empty box filled with pretty things that exist for no real purpose."
    "Much like most of the world, but with a fresher coat of paint on it."
    "It’s only magic for a moment."

    tb "Would you care to take a guess at what this room is?"
    s "I can’t imagine anything I say would come even remotely close."
    tb "This is the Tsukioka family ceremony room. It’s where I married my husband and where my daughters will marry theirs."
    tb "Assuming anyone will ever take Tsukasa, that is."

    scene tsubasatour13
    with fade

    s "You {i}all{/i} get married in here?"
    tb "As per tradition, yes. It’s the sole purpose of this room. "
    s "I’m having a very hard time picturing Touka getting married."
    tb "I imagine that’s because you’ve only seen her as a student."
    tb "Touka’s been just as invested in the history of our family as me ever since she was a little girl."
    tb "She’s likely too embarrassed to say anything about it to you, but she’s been dreaming of the day she gets to stand here beside her lover for years."
    s "Yeah, still not really able to picture it."

    scene tsubasatour14
    with dissolve

    tb "Has she told you that we were planning on arranging her marriage as well?"
    tb "We had several suitors picked out, but I could always tell she was never really comfortable with the idea."
    tb "They all wound up in space anyway, though, so it’s not like the plan would have come to fruition even if we hadn’t decided to...rethink things."
    s "Well, I’m sure she was really happy with that decision. I can’t imagine her doing {i}anything{/i} that’s commanded of her, let alone marrying someone."
    tb "I think you’d be very surprised at what Touka would be willing to do for her family. "
    tb "Or anyone, for that matter."
    tb "I often think that the reason my youngest daughter is so devilish is because my oldest wound up being such an angel."
    tb "But, I suppose that basically sums up what {i}this{/i} particular room is used for."
    tb "Come. I’ll show you around some of the others. "
    tb "You’ll soon find that all things serve some sort of purpose."

    scene black
    with dissolve2

    "Tsubasa continues our tour of the Tsukioka manor for what feels like an eternity."
    "Every corner we round is doused in history and, I don’t know if it’s just due to spending so much time around them or if it really {i}is{/i} an innate interest in all things Tsukioka-"
    "But she knows every single story. And she tells them as if she were there for the origins."
    "I wonder what it’s like having so much pride in something."
    "The only pride I have is that of the sinful sort. There’s nothing that I can look at or hold and think, “This is a part of me.”"
    "But even if that was something I {i}could{/i} do, I imagine I’d be more focused on just figuring out where that part belongs so I can start putting myself back together."
    "Maybe one day when time is no longer limitless."
    "Maybe one day when I actually want to."

    scene tsubasatour15
    with dissolve2

    tb "We’ll cap off today’s portion of the tour with our indoor arboretum- another family relic that’s been an important part of our history for centuries."
    tb "A long time ago, before industrialization took up its scythe and laid waste to our lands, Kumon-mi was covered in trees and filled with wildlife."
    tb "You’d never be able to tell with how things look today, but that doesn’t mean all traces of the past are gone."
    tb "This “arboretum” holds but one tree- an everblooming sakura, kept alive by extremely specific climate controlling, imported soil, and a fair bit of willpower."
    s "I didn’t realize trees had “willpower.”"
    tb "Why wouldn’t they? They’re alive, after all. Just like you and I."
    tb "In fact, I’d wager they’re even {i}more{/i} alive than us. "
    tb "Just think of how much this tree has seen. All of those stories I recounted for you today would be actual {i}memories{/i} for something that’s been alive as long as our sakura."

    scene tsubasatour16
    with dissolve

    s "I don’t want to be the bearer of bad news, but I’m pretty sure trees can’t retain memories."
    tb "Of course I know that. But if they {i}could{/i}, imagine just how many of them there would be."
    tb "I suppose the importance of this particular transplanted piece of nature isn’t in what it {i}could{/i} hold, however, and rather what it stands for. "
    s "Which is?"
    tb "Perseverance. "
    tb "To be the only remaining trace of what was once an important part of the world...I believe there is something special about that."
    tb "Every other aspect of this tree’s world has been, and forgive the pun, cut down. "
    tb "All that remains is the ground itself, and even that ground would not suffice in keeping it alive anymore."
    tb "In here, though..."
    tb "In this world created for the sole purpose of sustaining it..."
    tb "It can live."
    tb "And I think that’s beautiful."
    s "..."
    tb "Has my explanation floored you to the point of speechlessness? "
    s "Not particularly. "
    s "I just think it’s interesting how you can speak so highly of things other people would see as boring or unimportant at surface level."
    tb "As I said earlier, this is my world. It’s one that I chose and one that I {i}would{/i} choose if the chance to do so repeated itself."
    tb "Of course I’ll be able to find the right berries to pick when I know where all of them grow."
    s "If that’s a figure of speech, I’m not really following."
    tb "I’m saying that I know why everything here is so special because I have had the time to learn. "
    tb "I’m sure it’s not far off from how your family feels about...arcade machines or...what were those silly things we ate called again? Toucans? "
    s "Tacos...and those aren’t really a thing that carry some sort of emotional weight for people who don’t grow up without arboretums or marriage-rooms. "
    tb "Well, whatever it is you find special, then. "
    tb "I believe that there is beauty in all things. And even if {i}you{/i} do not, that’s something I wanted to show you."
    tb "As a friend who wants to be a part of your world and who wants to share hers with you."

    scene tsubasatour17
    with dissolve

    tb "I suppose there is one more place we can stop before our day comes to a close, though. Something I’m sure {i}all{/i} people can appreciate and not just those with an affinity for history. "
    s "Am I finally getting to see the animatronic band I’ve heard so much about?"
    tb "Heavens, no. That’s at one of our vacation homes."
    tb "You’ll see what I’m referring to in no time at all."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ tsubasadate1 = True
    $ tsubasa_love += 1

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"
    "........."
    "......"
    "..."

    jump tsubasadate1p2

label tsubasadate1p2:
...
```

## Code that triggers this event
File: \game\TsubasaEvents.rpy
Code:
```python
...
label calltsubasamorning:
    if tsubasa_love >= 0 and toukaspecial15p3 == True and tsubasadate1 == False:
        jump tsubasadate1
...
```