# New Age Entrepreneurs (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Walking on Eggshells](./christmastwo10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo11
* Group: Main
* Triggered by label: christmastwo10
* Chain sources: christmastwo10
* Chain sources path: christmastwo10

## Official wiki page

[New Age Entrepreneurs](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo11&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo11:
    scene wizardparty1
    with dissolve2

    y "Holy fucking shit. I will literally never understand why anyone would willingly have a child."
    y "Like, I can kind of understand it with babies because some people just think they’re fucking cute or whatever."

    scene wizardparty2
    with dissolve

    y "But as soon as they’re old enough to like, think and shit, they’re just fucking exhausting."
    c "Wow. You really got all of that from just hanging out in Chinami’s room for five minutes?"
    y "Five minutes? That really how long I was in there for? Felt like a fucking month."
    c "Ten max, but probs closer to five. How was the room? Everything look clean enough?"

    scene wizardparty3
    with dissolve

    y "You know you coulda just came with me to check, right? Not sure what the point of waitin’ around in the lobby was if you were just gonna come right back up here."
    c "I just wanted to make sure you found the place okay. I trust you enough to take my sister to a specific room all by yourself."
    y "Well, I sure hope I didn’t just drop her off in some random one. Feel like it might be a little tougher to get her back than it was to drop her off."
    c "Hm? Sorry, what was that? I thought I heard Sensei say my name just now and I stopped paying attention."
    y "Oh, okay. Didn’t realize you were gonna be playing the “creepy stalker girlfriend” game again tonight. No wonder you fuckin’ ran back here as fast as you could."

    scene wizardparty4
    with dissolve

    c "I don’t think you’re understanding how hard it is to run in this outfit. You should be more impressed."

    if bonus == True:
        y "The only thing I’m {i}impressed{/i} by is your ability to stay so fucking devoted to a dude who probably jerks it to pictures of you in the school bathroom."
    else:
        y "The only thing I’m {i}impressed{/i} by is your ability to stay so fucking devoted to a dude who probably plastered a photo of you to a stuffed animal so he can hug it all the time."

    scene wizardparty5
    with dissolve

    c "You really think so?!"
    y "Chika, that’s not a fucking compliment! "

    if bonus == True:
        c "You mean to tell me you wouldn’t feel a little flattered if somebody was jerking off to pictures of {i}you{/i} in the school bathroom?"
    else:
        c "You mean to tell me you wouldn’t feel a little flattered if somebody did that for you?!"

    y "No! I’d feel fuckin’ sketched out! That’s not a thing I want people to do!"

    scene wizardparty6
    with dissolve

    if bonus == True:
        c "Yeah, well, you’re a prude and it’s time for you to accept that somebody is probably going to masturbate while thinking about you one day."
        c "Assuming you stop shit talking everyone all the time, of course."
        c "Unless they’re into the whole hatefucking thing, which...honestly, I think is kinda hot."
    else:
        c "Yeah, well, we're all going to die anyway. So we might as well just accept whatever affection people are willing to give us."

    y "What the absolute fuck is happening to you?"

    scene wizardparty7
    with dissolve

    c "{i}Love...{/i}"
    y "Also, I’m not just mindlessly shit talking everybody anymore. I’ve been tryin’ to get better with that shit."
    y "Like, I haven’t said {i}anything{/i} to Futaba ever since I apologized to her."

    scene wizardparty8
    with dissolve

    c "Wait, you haven’t said {i}anything{/i} to her since then? Isn’t that kinda like, going backwards?"
    y "Uhh...no? The fuck are you talking about?"
    c "I just figured you two might wind up getting a little closer after that. I’m sure Futaba would be open to like, hanging out or something."
    c "Which would also mean you’d have more to do than just waiting around for me all the time."
    y "I’m good. One teacher-obsessed friend is exhausting enough as-is. Besides, she’s got plenty of other people to be around all the time."
    y "I’m fine with being alone. I don’t like, thrive off of constant validation the same way you do or whatever."
    c "You really don’t get even a little bit lonely sometimes?"
    y "Dude, I’ve been basically alone my whole life. I’d feel fucking weird if I {i}wasn’t{/i} alone."

    scene wizardparty9
    with dissolve

    c "Your backstory always makes me so sad."
    y "{i}Why?{/i} It’s not like you’re living the princess life either."
    y "We’re two [teenage]girls raising a little brat and trying to just keep shit afloat without losin’ your apartment or gettin’ her sick. We ain’t got time to fuckin’ feel sorry for each other."
    c "Yeah...Yeah, I guess you’re right."
    c "I wonder how Chinami’s doing with Tsubasa. I hope she’s not nervous being around new people."
    y "She’s fuckin’ Chinami. I’m sure she’s fine."
    c "I really hope so..."

    scene black
    with dissolve2

    "{i}Meanwhile...{/i}"

    scene wizardparty10
    with dissolve2

    tk "Bow before me, peasant! I am Tsukasa Tsukioka, of the esteemed Tsukioka Family! "
    tk "But I’m sure I don’t have to explain who the Tsukiokas are to you, do I? Our name is everywhere! On every building! Every park bench! "
    tk "We own this city! You are nothing! And you answer to me now!"
    tb "Tsukasa, please play nice. Chinami does not have to answer to you."
    ch "Chinami doesn’t know who the Tsukiokas are, but she doesn’t go outside very much, so that’s probably why."

    scene wizardparty11
    with dissolve

    tk "What do you mean you don’t know who we are? I thought everyone knew who we were."
    ch "Not Chinami! Chinami thinks you’re just another stranger!"
    tk "A...stranger?"

    scene wizardparty12
    with dissolve

    tk "Mother, do you hear this? The peasant girl doesn’t know who we are. Are we not famous among the lower class?"
    tb "We’re not “famous” at all, dear. We’re privileged enough to live the life that we do, so it is up to us to not throw that back in the faces of those less fortunate. "
    tb "There will always be people who don’t know us because we have never taken the time to get to know {i}them.{/i}"
    tk "Does Papa know about this? Because Papa told me that everyone loves the Tsukiokas and that we can have whatever we want whenever we want."
    ch "Chinami isn’t even allowed to go outside without asking first! If she becomes a Tsukioka, will she also be able to do anything she wants?"

    scene wizardparty13
    with dissolve

    tk "Aha! So you {i}do{/i} wish to become my underling! I can not say I blame you, peasant. Especially since you are being forced to wear rags like {i}those{/i} instead of lavish, expensive dresses!"
    ch "Chinami loves her clothes, though. And they look much warmer than yours."

    scene wizardparty14
    with dissolve

    tk "Mother! How do I get her to stop speaking and listen to my speech? I’m trying to expand our empire, but she keeps saying words and ruining everything!"
    tb "Our empire is large enough, dear. Not everyone has to be a part of it."
    ch "Is Chinami a Tsukioka yet? Is she allowed to eat peanuts? Because Chinami is allergic to peanuts and doesn’t want to be that way anymore."
    tb "You can’t just decide to not be allergic to things anymore, dear. It doesn’t work that way no matter {i}how{/i} much money you have."
    ch "Chinami is saddened by this news."

    scene wizardparty15
    with dissolve

    tk "And why do you talk like that?! Do they not teach you proper grammar in public school?! Is that something only us “privileged” people know about?"
    ch "Chinami doesn’t go to school, so she has no idea. This is just the way she talks."
    ch "She is a successful business owner, though! And the top purveyor of giraffes and giraffe-related merchandise in all of Kumon-mi!"

    scene wizardparty16
    with dissolve

    tk "In all of Kumon-mi? That sounds very impressive."
    ch "It is! Chinami is reporting at least 50%% growth year over year!"
    tk "Mother! Has Papa penetrated the giraffe industry yet?"

    scene wizardparty17
    with dissolve

    tb "Your father hasn’t penetrated anything in quite a while, dear."
    tb "In fact, I’m beginning to think that he may have forgotten how."
    tk "Lies! I bet Papa penetrates all types of things! In fact, I bet he’s penetrating giraffes at this very moment! He will not be out-penetrated by this petulant child!"

    scene wizardparty18
    with dissolve

    tb "Tsukasa! Stop saying “penetrate” right this instant! It is making your mother very angry!"
    tk "Fine, Mother! I love you! Please forgive me!"

    scene wizardparty19
    with dissolve

    tb "Lord, grant me the strength I need to make it through the night...."

    scene wizardparty20
    with fade

    tk "So...if you really {i}are{/i} a successful business owner...what is your business called?"
    ch "Chinami’s business is called Chinami-Corp! It stands for Chinami Corporation! And Chinami calls it that because it is a corporation that could not exist without Chinami."

    scene wizardparty21
    with dissolve

    tk "Naming your first business after yourself? That sounds quite impressive, {i}Chinami.{/i}"
    tk "But if you think for a second that I will allow you to continue dominating this...niche industry of giraffe ownership in Kumon-mi, you have another thing coming!"

    scene wizardparty22
    with dissolve

    tk "You see, I’ve been meaning to start my own business as well, and it just so happens that {i}I{/i} was planning on selling giraffes and...giraffe-related merchandise!"
    tk "Your days are numbered, Chi-"
    ch "Chinami is excited to hear about future competition and wishes your business great success in the future!"

    scene wizardparty23
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

label christmastwo12:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
"........."
    "......"
    "..."

    scene ioxmashall26
    with dissolve2
    play music "stpartynight.mp3" fadein 3.0

    a "Sensei! I’m going to ignore the fact that you were gone for so long and jump straight to asking if you heard me sing or not!"
    s "I did. It was very impressive, Ami."
    a "Yeah?! Do you think Niki would be proud?!"
    s "Sure. Why not?"
    m "Where have you been?"
    s "With Kirin and Io outside of a boiler room. It’s a long story."
    m "That’s...certainly a combination of characters."
    ka "Io? Who is that?"

    scene ioxmashall27
    with dissolve

    a "She’s another girl in our class, but she never really talks to anyone, so you probably didn’t know she existed."
    ka "And she’s...friends with Kirin?"
    a "I...don’t think so? At least I’ve never really seen them together before."
    s "I wouldn’t say they’re friends, but they're walking back to the dorms together now, so at least that’s a thing."

    scene ioxmashall28
    with dissolve

    ka "Kirin left? Why? She was supposed to walk back with me tonight. I would have left early if I knew she wasn’t having fun."
    a "You can leave with us instead, Karin. You spend more time hanging out in our group anyway."
    m "Does them leaving have anything to do with what may have happened outside of this boiler room thing?"
    s "Maybe. Maybe not. Anyway, what have you guys been up to?"

    scene ioxmashall29
    with dissolve

    ka "Well...I was worrying about why you and Kirin left together...but I feel kind of...really stupid for that now..."

    "I subconsciously thank Io for showing up and becoming a part of my alibi, even if she almost broke down in the process of doing so."

    m "That seems like a plausible thing to worry-"
    s "And you, Ami?"
    a "Oh, you know. Just singing and...waiting for you. So basically what I’m always doing, but with more of a Christmas vibe."
    a "Have you eaten anything yet? We ordered a million more cakes for the party since we finished everything at our house last night."
    s "I’m assuming “we” means Maya?"

    scene ioxmashall30
    with dissolve

    m "I regret nothing."
    ka "I also...b...baked one if you want to try that, Sensei!"
    ka "Actually, nevermind! Don’t! I’m sure the others are better! Hahaha!"
    s "Karin, why are you laughing about that?"

    scene ioxmashall31
    with dissolve

    ka "I have no idea! Hahahahaha!"
    m "So, do you intend to stay in this room for the rest of the party? Or are you bound to go wandering around again?"
    s "Worried you’ll miss me too much if I leave?"
    m "Quite the opposite, actually. I’m trying to plan my night so I see as little of you as possible."

    "It’s really amazing how she can still pretend she hates me this much even after starting to let the truth slip out."
    "But I guess she has plenty of experience after all those years of hating other iterations."
    "Or...other versions of this same iteration?"
    "I still have no idea how it works. I’m just glad to be sentient right now."

    s "I’ll probably stick around for a little while, get pulled into some drama, come back, get pulled into more drama, and then bump into you on the roof or something."
    s "That’s how things normally go, at least."

    scene ioxmashall32
    with dissolve

    m "Joke's on you. The roof here is closed."
    a "Roof? When did you try to go to the roof?"
    a "Is this about stars again? You know you can take a break from stars on Christmas, Maya. They’re not going anywhere."

    scene ioxmashall33
    with dissolve

    m "Thank you, Ami. This changes everything. All this time, I was under the impression that they were just going to disappear."
    m "I can now celebrate Christmas like the normal [teenage]girl I am. Hooray."

    scene ioxmashall34
    with dissolve

    a "You don’t have to be a jerk about it, you know..."

    scene black
    with dissolve2

    "{i}Meanwhile...{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo10 = True

    jump christmastwo11
...
```