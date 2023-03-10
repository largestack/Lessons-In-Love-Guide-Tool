# The Deep End (Tsubasa)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Everbloom](./tsubasadate1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: tsubasadate1p2
* Group: Tsubasa
* Triggered by label: tsubasadate1
* Chain sources: tsubasadate1
* Chain sources path: tsubasadate1

## Official wiki page

[The Deep End](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsubasadate1p2&go=Go) for more details.

## Event code

File: (install folder)\game\TsubasaEvents.rpy

Code:
```python
...
label tsubasadate1p2:
    if _in_replay:
        play music "tsukiokamanor.mp3"

    "Tsubasa leads me away from the everblooming sakura into a hall full of old Japanese paintings I should probably know the names of but don’t."
    "I wouldn’t doubt if some of them are originals that I’m meant to be impressed by, but I refuse to be impressed by anything that’s so easily duplicated."
    "My untrained eye wanders from canvas to canvas, hoping to pick up even a fragment of what makes this dimension so palatable for someone like Tsubasa, but I get caught up on her instead."
    "Beauty is supposed to be in the eye of the beholder anyway. And despite how frequently these eyes deceive me, I know what it is that I would prefer to waste away my days observing."
    "There are no paintings that can bring me joy."
    "Maybe once upon a time there were-"
    "But there aren’t any left now."
    "And if there are, I imagine they’re locked behind more doors in this palace than I’ll ever be able to open."
    "Tsubasa says some things as she leads me down the hall, but none of them attach to whatever part of my brain is meant to process them."
    "It isn’t until she leads me into a wide open, half-misty room that I remember what we’re doing or how to listen."

    scene tsubasapool1
    with dissolve2

    tb "This is one of Touka’s favorite additions to the manor and one that most people we bring here tend to enjoy very much."
    tb "It’s nothing extravagant or historical like a special tree or a ceremonial room, but it houses a borderline-olympic sized heated pool."
    tb "I used to spend a lot of time here when I was younger. I’m afraid I can seldom make the room in my schedule at this point, though."

    scene tsubasapool2
    with dissolve

    s "If there's anything I've learned today, it's that you’re a lot busier than I ever really imagined you were."
    tb "Did you assume I was just some woman living off of her husband’s money without making an effort to actually accomplish anything?"
    s "I don’t know if my thoughts were {i}that{/i} specific."
    tb "It’s that sort of perception that comes with the territory when you marry into the most influential family in a city."
    tb "I can guarantee you I’ve heard it all before."

    scene tsubasapool3
    with dissolve

    tb "Of course, though, that’s not even remotely true."
    tb "I suppose it’s just in my nature to always be doing {i}something{/i}. I have a hard time pulling myself away from anything that could be called “productive” in some form."
    tb "Which is why you’ll see me...offering to give tours. Or offering to babysit. Or offering to check in on remote onsens for the sake of the family business."
    tb "I suppose that last one was a tad relaxing, though. "
    tb "Even with all of the noise."

    scene tsubasapool4
    with dissolve

    s "I have no idea what you’re talking about. Chika and I were just watching TV."
    tb "You’ll have to tell me what program. I can’t remember the last time I enjoyed {i}watching TV{/i} that much."

    play sound "water1.mp3"

    to "Wha-"
    to "Sensei?"

    scene tsubasapool5
    with fade

    to "What are you doing here?..."
    s "Being shocked at how you’re still in [high_school]."
    to "Yes, but {i}what are you doing here?{/i}"
    tb "I invited him over to give him a tour of the manor, dear. I figured it was the least I could do to offer him thanks for his time at the arcade and...surrounding areas the other day."
    to "I see..."
    s "Have you been in there this whole time?"

    scene tsubasapool6
    with dissolve

    to "I’ve been in here for at least an hour. If I’d known you were coming, I would have put on something more presentable."
    s "No worries. What you’re wearing is totally fine. "

    scene tsubasapool7
    with dissolve

    to "Are you enjoying the tour, at least? I’m assuming Mother already told you about the rock garden? She always likes to open up with that."
    tb "I also showed him the golden room and told him all about how you’ve been dreaming of getting married there one day."

    scene tsubasapool8
    with dissolve

    to "Wha- Mother?! "
    to "Sensei has no interest in that! And those were just silly, girlish dreams!"
    tb "Oh? So you {i}don’t{/i} want to be married in the golden room anymore?"
    to "I...well..."
    tb "Touka darling, come out of the pool if you’re going to hold a conversation with us. It’s bad manners staying in there."

    scene tsubasapool9
    with dissolve

    to "Hah...yes, Mother..."

    scene black
    with dissolve2

    "Touka exits the pool and wrings her hair back out into the water."

    if bonus == True:
        "If her mother wasn’t standing beside me, I’d use this opportunity to make some perverted comment about the angle of her body as she does this."
        "But, at the risk of forming an erection in the process of mentally describing that, I will elect to abstain."
    else:
        "The environment thanks her."

    scene tsubasapool10
    with dissolve

    tb "Oh my. Are you {i}still{/i} growing, dear? You may even surpass me at this rate."

    if bonus == True:
        "Nevermind. Some things just can’t be contained."

    to "Mother, stop! Weren’t you {i}just{/i} speaking of bad manners?!"

    scene tsubasapool11
    with dissolve

    tb "Oh, yes. Silly me. I was so impressed with your...progress, that I’d forgotten your teacher was even here."
    s "I completely understand. I forgot as well for a second."
    to "If you two are done objectifying me for now, I would like to go get dressed into something more suitable for the remainder of Sensei’s tour."

    scene tsubasapool12
    with dissolve

    tb "Oh, his tour is just about over for the day. I’ve been dragging him around all morning. Though, I suppose he {i}was{/i} willingly following me, so perhaps he enjoyed it?"
    s "I just didn’t want to get lost in the entire mini-city you’ve built for yourselves."
    to "Have you really been here for that long? Why wasn’t I informed of this?"
    s "I honestly didn’t even think you’d be okay with me coming."
    to "I’m...mostly indifferent to you coming. But if you’re {i}here{/i}, I believe I should be involved in some way."

    scene tsubasapool13
    with dissolve

    tb "I apologize for not telling you, dear. I’d just assumed you wanted the rest."
    to "{i}My{/i} rest aside, I thought you had meetings today? "
    tb "I was on call for meetings regarding some of the properties we saw the other day- but it appears that none of them ever happened."
    tb "Or at least no one’s been able to find me to inform me about them. You know our manor staff, though, so that doesn’t seem very probable."
    to "Well...regardless, I’m going to go get changed."

    scene tsubasapool12
    with dissolve

    to "Please inform me if you’re ever going to come here again. It’s one thing to appear casual at the dorms, but as the heiress of the Tsukioka Foundation, I can’t afford to be seen like this here. "
    to "I have a reputation within the manor to uphold. "
    tb "I won’t tell anyone if you don’t, dear. Now, go get dressed. We’ll stay here until you return."
    to "Okay..."
    to "Don’t go anywhere."

    scene tsubasapool14
    with dissolve

    "Touka grabs a towel off of a nearby rack and dries herself off before disappearing into the hall of a thousand paintings."
    "That’s not an accurate number- just an estimation."

    tb "My lord. It feels like just the other day I was purchasing her luxury training bras. "
    s "That’s an item that probably shouldn’t exist."

    scene tsubasapool15
    with dissolve

    tb "But it does, and so she had them. Not for very long, though, as you can probably assume."
    s "So I guess we’re talking about your daughter’s breasts now. Not really how I imagined this tour ending after 90%% of it was a history lesson."

    scene tsubasapool16
    with dissolve

    tb "Just some passing commentary. That wasn't a topic I intended to remain on any longer- at least not without her present for it."
    s "I feel like having her present for it would make things even weirder. "
    tb "Perhaps it would."
    tb "Though, I wouldn’t say the same about what I feel we must discuss next."
    s "Which is?"

    scene tsubasapool15
    with dissolve

    tb "Would you find it rude if I took my shoes off? I don’t want to get in the pool, but I’d like to dip my feet in for a moment while we await my daughter’s return."
    s "Do whatever you want, it’s your house."
    tb "Excellent. Then, don’t mind me."

    scene black
    with dissolve2

    "Tsubasa sits down on a fancy looking beach chair and unstraps whatever the elegant looking sandal things she’s wearing are called."
    "She catches me looking at her for a moment and kindly waves me off so she can remove her stockings as well and, reluctantly, I oblige."
    "Once she’s done, she returns to me and sits down in front of the pool, hiking her dress up and dipping her toes into the water."
    "I sit beside her, mostly certain and even more uncomfortable about what I believe she wants to discuss next."

    scene tsubasapool17
    with dissolve2

    tb "..."
    s "..."
    tb "Do you know what it is I want to talk about, Sensei?"
    s "Probably, but I’d prefer to not guess and just have you get it over with so I don’t have to risk guessing incorrectly."
    tb "Then I suppose I’ll “get it over with” and save us the difficulty of prodding at one another until it’s out in the open."
    tb "A young lady who I’ve grown rather fond of lately seems to believe that the two of you are involved in an exclusive relationship with one another."

    if bonus == True:
        tb "But that young lady is just that. {i}Young.{/i}"
        tb "And while I’m no stranger to the prospect of marrying someone older given that women have been traded between affluent families like cattle for centuries-"
        tb "I can’t help but get a little caught up when it comes to wrapping my mind around your situation."

        "You know, when I first told Tsubasa that I’d be okay with spending more time with her, I worried that something like this might come up."
        "She’s one of the only people Chika trusts enough to talk about our “relationship” with, which is kind of odd considering Tsubasa was, at one point, just some random woman at an onsen."
        "But she’s much more than that now. To Chika, at least."
        "And to Tsubasa, Chika is important as well."
        "So it only makes sense that she’d ask me about this now that she finally has an opportunity to."
        "The only issue is that I don’t know what the right thing or the wrong thing to say is."
        "Tsubasa seems like a rational and understanding person but, at the same time, she’s someone I’ve only known for a little while."
        "And I’m less important to her than a surrogate daughter."
        "In fact, I doubt I bear any sort of importance in Tsubasa’s life at all."
        "So, I should probably tread carefully here."
    else:
        "Oh no. She knows about the hugs."

    s "What are you asking me?"

    scene tsubasapool18
    with dissolve

    tb "Oh? Is that a trace of attitude I’m hearing?"
    s "Not intentionally. I’m just not sure how to answer a question that hasn’t been asked yet."
    tb "And I’m not quite sure what I want to hear. "
    tb "On one hand, I want the young lady I care about to be happy. But when you really think about what it is that’s {i}making{/i} her happy, the waters get a little muddy."
    s "I don’t-"

    if bonus == True:
        tb "You are a grown man sleeping with a girl in [high_school]. Sleeping with your {i}student.{/i}"
    else:
        tb "I know about the hugs."
        s "Oh no."

    tb "Aren’t you even a little worried about what could happen to you if that information were to get out?"
    s "..."
    tb "..."
    s "Are you grilling me as a friend or a parent right now?"
    tb "Can it not be both?"
    s "Not when my answer would change based on yours."
    tb "Then I suppose we can say I’m asking you as a friend."
    s "I see."

    scene tsubasapool19
    with dissolve

    s "Of course I’m worried about what would happen if that information were to get out."
    s "And yet, I don’t really do anything to try and stop it apart from just...asking her to keep quieter."
    tb "Do you love her?"
    s "..."
    tb "..."
    s "Not the way I’m supposed to."
    tb "And how is it you are {i}supposed{/i} to love someone?"
    s "The same way she loves me, I guess."
    tb "Hm."

    scene tsubasapool18
    with dissolve

    s "You know, you can be pretty intimidating when you want to be."
    tb "Women in power are good at that sort of thing."
    tb "But if you want the truth, I’m not really appalled by what you do."
    tb "Like I said, that sort of thing doesn’t mean much to me when I’ve gone my whole life hearing stories of other women from {i}my{/i} family being shipped off to men twice their age."
    tb "It loses its impact after a while."
    tb "What I’m worried about is whether or not you’re going to hurt that young girl- whether it be intentional or unintentional. Because I don’t know if she’d be able to handle it."
    s "..."
    tb "..."
    tb "Just going to stay silent forever?"
    s "Sometimes, silence is the best answer."
    tb "And you think this is one of those times?"

    scene tsubasapool20
    with dissolve

    s "I’m not sure what this is."
    s "But if I had to guess, I’d wager that I {i}am{/i} going to hurt her."
    s "Life isn’t even half as convenient as it would need to be in order for me to avoid that."
    s "But I don’t intend to leave her side either. "
    s "I don’t really think I could."
    s "Even if she winds up hating me for something I’ve done or...{i}will{/i} do in the future, I’ll be there for her."
    s "So at least she won’t have to hurt alone."
    s "Granted, I’m not sure how much help my presence will be- especially when I’m worse at cheering people up or even just talking than anyone else I’ve ever met."
    s "But I’ll be there."
    s "She doesn’t have to be alone anymore."
    tb "..."
    s "..."

    "I think about how the water would feel against my skin."
    "I shrug it off."
    "That’s all I ever do."

    tb "That was a good answer."
    tb "We can’t prevent ourselves from hurting the people we care about. All we can do is pray it doesn’t happen and be prepared to suture the wounds if it does."
    tb "As long as you’re not just using the girl, I can accept the nature of your relationship."
    s "At first, that’s exactly what it was."
    tb "But it’s not anymore, is it?"
    s "..."
    tb "..."
    tb "Ah."
    tb "Silence."
    s "It’s the best answer sometimes."

    scene tsubasapool21
    with dissolve

    tb "I certainly picked an interesting class to enroll my daughter in, didn’t I?"
    s "Probably the worst one possible. And I’ve always been a little curious about why."
    s "You’ve known about Chika and me since the beginning. I figured that would be all you need to know to keep Touka away."

    scene tsubasapool22
    with dissolve

    tb "Tell me...How deep do you think this pool is, Sensei?"
    s "What?"
    tb "When Touka was a little girl, she really wanted to learn how to swim."
    tb "We hired an entire team of renowned instructors to teach her. People from all over the globe, since they were still allowed in back then. "
    tb "We spent {i}so much{/i} money trying to help that little girl swim."
    tb "But none of it worked."
    tb "No matter who we hired or what their methods were, she just couldn’t learn."
    tb "But one day, while the two of us were lounging near the poolside, I recalled a story one of my girlfriends told me about how {i}she{/i} learned to swim when she was younger."
    tb "Her mother pushed her into the pool."
    tb "Terrified and wanting nothing more than to stay alive, her instincts kicked in and she managed to swim back to the ledge and pull herself out."
    s "You...pushed your daughter into the pool knowing full well she didn’t know how to swim?"

    scene tsubasapool23
    with dissolve

    tb "And now you’re her teacher."
    tb "Sometimes, forcing people to do things they’re not comfortable with is the best way to move them forward."
    tb "I’ve known from the beginning that you were the exact opposite of what Touka needs."
    tb "And I think that’s exactly what makes her need you the most."
    s "..."
    tb "..."

    if bonus == True:
        s "Okay. But you have literally heard me have sex with a girl the same age as your daughter."
        tb "Lots of it."
    else:
        s "Okay. But you know about the hugs. I am evil."
        tb "(Airplane noises)"
        s "Well said."

    s "..."
    tb "..."
    tb "Are we ending the conversation here?"
    s "Yeah, I think we probably should."

    scene black
    with dissolve2

    "Tsubasa and I sit in silence until Touka returns wearing the same white dress she had on when I first met her."
    "Everything goes back to normal. "
    "And I, once again, manage to slip through the cracks of morality as I find that my newest acquaintance might also be a little broken as well."
    "Just in a much more beautiful way than I am."

    $ renpy.end_replay()
    $ tsubasa_love += 1
    $ tsubasadate1p2 = True
    stop music fadeout 5.0

    "{i}Tsubasa’s affection has increased to [tsubasa_love]!{/i}"

    jump saturdaynight
...
```

## Code that triggers this event

File: (install folder)\game\TsubasaEvents.rpy

Code:
```python
...
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
...
```