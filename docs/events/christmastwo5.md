# Everything Evil (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Dodging Snowflakes](./christmastwo4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo5
* Group: Main
* Triggered by label: christmastwo4
* Chain sources: christmastwo4
* Chain sources path: christmastwo4

## Official wiki page

[Everything Evil](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo5&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo5:
    play sound "static.mp3"
    scene dodgingsnowflakes18 with flash
    stop sound

    "I-"
    "..."
    "What was I thinking just now?"

    mo "..."
    s "..."

    play sound "static.mp3"
    scene m
    stop sound

    "M is for Molly; Y is for Yarn."
    "I is for Invisible; and A is for Arms."
    "S is for Silence; then I once again!"
    "Then a little more silence so we can pretend."

    play sound "static.mp3"
    scene dodgingsnowflakes18 with flash
    stop sound
    play music "merrychristmasmrlawrence.mp3"

    mo "..."
    s "..."
    mo "What did you do to me?"
    s "... "

    play sound "static.mp3"
    scene dodgingsnowflakes19 with flash
    stop sound

    mo "Did we..."

    "No."

    mo "Did..."
    mo "Did you..."

    "No."

    play sound "static.mp3"
    scene dodgingsnowflakes20 with flash
    stop sound

    if bonus == True:
        mo "Did you take advantage of me, Sensei?"
    else:
        mo "Did you log into my account while I was gone and leave me naked in the middle of Stormwind?!"

    s "No."

    if bonus == True:
        mo "Did you fuck my tight virgin cunt while I was passed out drunk and vulnerable?"
    else:
        mo "Do you have any idea how expensive that repair bill was?!"
        s "I-"

    mo "Did you do it?"
    s "No."
    mo "Did you like it? "

    if bonus == True:
        mo "Did it feel good inside of me? "
    else:
        mo "Did it feel nice inside of my character?"

    mo "Did it feel nice being in control?"
    s "No."
    mo "I can still feel it if I close my eyes, you know."

    if bonus == True:
        mo "My insides being stirred by your thick cock...so big that it could cause irreparable damage to my vagina and prevent me from ever wanting to have sex again."
        mo "I can still feel it if I close my eyes, you know."
        mo "My teacher’s dick, tearing me in half."
        mo "Was it that hard to hold yourself back?"
        s "Molly-"
        mo "Did you rape me, Sensei? "
        mo "Did you take advantage of me, Sensei?"
        mo "Why?"
        mo "What did I ever do to you?"
        mo "Did you like it at least?"
        mo "Can you tell me that?"
        mo "Did you rape me, Sensei? "
        mo "Did you {b}RAPE{/b} me, Sensei?"
    else:
        mo "The gryphons."
        mo "The dwarves."
        mo "I can feel all of it."

    mo "Why?"
    mo "Why did you do it?"
    mo "Tell me."
    mo "Tell me."
    mo "Tell me you-"

    play sound "static.mp3"
    scene dodgingsnowflakes18 with flash
    stop sound

    mo "Sir?..."
    mo "Why?..."
    mo "Why have you been avoiding me?..."
    s "..."

    scene dodgingsnowflakes21
    with dissolve

    mo "Did..."
    mo "Did I do something wrong?..."
    s "..."
    mo "What did I do?..."

    scene dodgingsnowflakes22
    with dissolve

    mo "I don’t really remember anything from before I woke up, so if I...maybe {b}FORCED{/b} you into doing something you didn’t want to-"
    s "That’s not it, Molly..."

    scene dodgingsnowflakes23
    with dissolve

    mo "Well then what {i}is{/i} it, Sir?! I’ve been trying to talk to you for almost two months now and this is the first time you’ve said anything to me!"
    s "I didn’t really know what {i}to{/i} say."

    scene dodgingsnowflakes24
    with dissolve

    mo "Rin, I could understand...but having you abandon me as well? I didn’t expect that at all..."
    s "..."
    mo "Did {i}you{/i} do something to-"
    s "I should get going."

    scene dodgingsnowflakes25
    with dissolve

    mo "Like hell ‘ye should get going! Talk to me!"
    s "Yelling in the hallway won’t-"
    mo "Then I’ll yell in my room! I’m tired of avoiding eye contact! I miss you, Sir! I’ll understand!"

    play sound "static.mp3"
    scene black with flash
    stop sound

    "No you won’t."
    "How are you going to understand something I don’t?"
    "How are you, the one person who should be more skeptical of this than {i}anyone{/i}, leading the charge?"
    "Why do you want to know?"
    "Isn’t it better to hide from the truth when the truth has the chance to be everything evil and more?"
    "Do you {i}want{/i} to be hurt?"

    play sound "static.mp3"
    scene dodgingsnowflakes26 with flash
    stop sound

    "We somehow end up here- the last place I want to be."
    "And while we’re just inches apart, it feels closer to miles."
    "Am I the one overthinking this?"
    "Am {i}I{/i} out of my mind for spending so much time coming to terms with what did or did not happen that, now that there’s a chance to resolve it, I’d rather just leave?"
    "What does she want me to say?"

    s "What do you want me to say?"

    "I can not leave, so I flounder."

    mo "I don’t know, Sir...Anything?"
    mo "How..."
    mo "How was your day?"
    s "You didn’t pull me in here to talk about my day, Molly."

    scene dodgingsnowflakes27
    with dissolve

    if bonus == True:
        mo "Fine, then! I guess I’ll just stop beating around the bush and ask you why I woke up with jizz all over my Halloween costume! "
    else:
        mo "Fine, then! I guess I’ll just stop beating around the bush and ask you why you sent me video you took of you huggin' me in the dark at Ayane's mansion!"

    s "I don’t know."

    if bonus == True:
        mo "What do you mean you don’t know?! It was yours, wasn’t it?!"
    else:
        mo "What do you mean you don’t know?! You even smiled at the camera and flashed a thumbs up before yellin' some stuff about how you are the huggy boy!"
        s "I {i}am{/i} the huggy boy..."
        mo "But why, Sir?! The huggy boy is only supposed to hug in the light!"

    s "..."
    mo "..."

    scene dodgingsnowflakes28
    with dissolve

    mo "Ugh..."
    mo "Sir, I don’t know how {i}you{/i} think {i}I{/i} feel about this whole...thing-"
    mo "But I can tell you that I’d rather figure it out than just let it stew in my head for the rest of the school year."
    s "Let me ask you this, then. What’s the worst thing you think could have happened?"

    scene dodgingsnowflakes29
    with dissolve

    mo "The worst thing? Probably me convincing you to do something you didn’t want to. I’ve heard the horror stories of what I’m like when I’m drunk, Sir. "
    mo "And I saw the...results."
    mo "I think it’s perfectly plausible for me to assume that as a possibility."
    s "What if those roles were reversed?"
    s "What if I..."
    mo "..."
    s "..."
    mo "What if you convinced {i}me{/i} to do something I didn’t want to?"
    s "What if there was no convincing at all?"
    s "What if I saw an opportunity to take something from you and just did it without a second thought?"
    mo "Is..."
    mo "Is that what happened?..."
    s "Would you believe me if I told you I didn’t know?"
    mo "Well...my memory’s still really foggy...but I don’t think you were drinking at all that night, Sir."
    s "I wasn’t."
    mo "Then why wouldn’t you remember?"
    s "Maybe I just zoned out? That happens sometimes."
    s "I don’t have anything that would come anywhere close to a believable answer."

    scene dodgingsnowflakes30
    with dissolve

    mo "I don’t really know how zoning out would lead to...what it did..."
    mo "But if you’re really being honest, Sir...and you really {i}don’t{/i} remember what happened...I can tell you now that I highly doubt it was anything {i}really{/i} bad..."

    scene dodgingsnowflakes31
    with dissolve

    s "..."
    mo "And...without saying too much and making this any more embarrassing for either one of us...I think you can probably believe me when I say I’d know if...yeah."
    mo "In fact, the only pain I felt at all was from the hangover I had the next morning. So I have a hard time believing your “worst case scenario” is the truth, Sir."
    s "..."

    scene dodgingsnowflakes32
    with dissolve

    if bonus == True:
        mo "Do you remember the conversation we had outside of the dorm before the Halloween party? The one about...experimenting and...sex with real human beings instead of cartoon characters?"
    else:
        mo "Do you remember the conversation we had outside of the dorm before the Halloween party?"
        s "No."
        mo "Oh. Well I'm going to talk about it anyway."

    mo "I didn’t say much about it afterward, but I’d be a damn liar if I said it didn’t stick around in my mind after that."
    mo "And it’s because of that that I was worried {i}I{/i} might have been the one to take things a little too far."
    mo "Halloween was a really bad night for me, Sir. Even {i}before{/i} my costume was ruined."
    mo "I was feeling lonely and weak and...and other things. And I vaguely remember wanderin’ into a dark room to just...be by myself-"
    mo "And then the next thing I know, it’s like you and I never had any talk at all and that we were as good as strangers."
    mo "I was just kind of hoping you’d tell me what happened so that I can stop tryin’ to piece it together on my own."
    mo "But if you really {i}don’t{/i} remember..."
    mo "I guess we’ll never know. "
    s "You’re a little more accepting of my “I have no idea what happened” story than I thought you’d be."

    scene dodgingsnowflakes33
    with dissolve

    mo "Call me naive, Sir, but I don’t think you’d lie about something like this to me."

    if bonus == True:
        mo "For all I know, you could’ve just gotten the urge to relieve yourself and decided to go full degenerate all over my belly as a prank."
        s "That doesn’t sound like a very good prank."
        mo "No, but there are certainly worse things you could have done."
        s "We don’t know that for sure, though."
        mo "Do we {i}have{/i} to know it for sure? Or can we just...I don’t know, make a guess?"
        s "Are you really okay with making a guess as serious as this? "
        s "Because, and this might sound surprising coming from someone like me, I’ve been having a pretty tough time with this."
        s "I’d never hurt you intentionally. Accidentally? Of course. And I fully accept that I’m likely going to do that multiple times in the future."
        s "But I’d never force myself on you."
        mo "I know that, Sir."
        mo "And it's that exact thing that makes me okay with kind of just...assuming whatever happened was something we {i}both{/i} wanted...instead of just one of us..."
        mo "But...thank you for saying that either way."
        s "Please don’t thank me for being somewhat of a decent person in this one, very specific scenario."
    else:
        s "I lie about all sorts of things. I am a very bad boy."

    scene dodgingsnowflakes34
    with dissolve

    mo "If you want my guess of what happened, Sir...I think it’s probably something like this."
    mo "I was drunk and wandered into a dark room."
    mo "You followed me in there for...whatever reason ye’d have to follow me in there."

    if bonus == True:
        mo "I blabbed on about Rin and Otoha and...probably got a little turned on."
        mo "Then...me being turned on probably got {i}you{/i} turned on-"
        mo "Then we both masturbated in the dark, you came on my costume, and I passed out."
    else:
        mo "Then we were both mind controlled by Alliance shadow priests who made the evil hug happen."

    s "That’s essentially the complete opposite of how things played out in my head."

    scene dodgingsnowflakes35
    with dissolve

    mo "You went for the worst case scenario, and I went for the best."

    if bonus == True:
        mo "Besides, even if I wasn’t conscious for the whole ordeal, I wouldn’t hate you for just letting one out on my cosplay."
        s "You probably should, Molly. That's not really something you should be okay with."
        mo "I believe you’re forgetting how much of a degenerate I am, Sir. And how you’ve already seen me going to town on myself in the past."
        mo "I don’t really mind having {i}that{/i} sort of relationship with you. "
    else:
        mo "Besides, even if I wasn’t conscious for the whole ordeal, I'm pretty much fine with you hugging me whenever you want."

    scene dodgingsnowflakes36
    with dissolve

    mo "Well...by {i}that{/i}, I don’t mean that I’m ready to start...you know, touching {i}each other{/i}...I think that’s something I should clarify."
    mo "I just mean that I...don’t really mind you knowing me on a more personal level..."
    mo "For whatever reason, you’re attracted enough to me to [masturbate] in the same room...and I’m attracted to you as well..."
    mo "So if we both happen to be in the same place at the same time and...are both feeling the need to...you know...without touching each other..."
    s "Molly, what exactly are you trying to propose right now? Because, whatever it is, it’s weird."

    scene dodgingsnowflakes37
    with dissolve

    mo "I have absolutely no idea, Sir. I’m simply recalling several mutual masturbation scenes in games I have played and trying to apply them to real life."
    s "This is absolutely not how I thought this conversation was going to end up."

    scene dodgingsnowflakes38
    with dissolve

    mo "I know, but..."
    mo "Can you please be my friend again, Sir?"

    if bonus == True:
        mo "And, if you’re going to ejaculate on me, confirm that I am awake first? "

    s "..."

    if bonus == True:
        mo "Or just...don’t ejaculate on me at all if you think that’s weird."
        mo "After all, we have no idea what {i}really{/i} happened and it could have just been some sort of...accident?"
        s "New idea. How about we just...try and put this behind us and not make any further plans about when and where it’s okay to orgasm?"
        mo "Okay, Sir. That sounds fine to me."
        mo "Also, and forgive me if I’m asking this at an inappropriate time, but do you {i}always{/i}...you know..."
        mo "Let out {i}that much?{/i}"
        s "..."
        mo "It just...seemed like a lot..."
        s "..."
    else:
        mo "..."

    mo "Nevermind. Forget I asked that. "

    scene dodgingsnowflakes39
    with dissolve

    mo "Oh! And also, hypothetically, if you were going to ask for something for Christmas, what would it be?"
    s "Not a wardrobe."
    mo "I...uhh...okay?"
    s "Are you the one who got me for Secret Santa this year, Molly?"
    mo "Of course not. This is entirely hypothetical. And, on a completely unrelated note, it is extremely convenient that we were able to have this conversation {i}before{/i} the gift exchange."

    if bonus == True:
        mo "It would have been extremely awkward for me to give you a present without clearing up the great ejaculation mystery first. Hypothetically, of course."
        s "I have several comments on those last couple sentences, but I’m going to hold them to myself and just tell you to {i}hypothetically{/i} get me a gift card or something."
        mo "A gift card, Sir? Is that really what you’d want?"
        s "There aren’t many things I want. So either do that or just...get me whatever you think I’d like."
        mo "Hypothetically, you mean."
        s "Right..."
        s "Hypothetically."
    else:
        s "Yes, because now I can show you all three hundred pages of my Christmas list."
        mo "That is so many pages."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I don’t stick around much longer than that because, despite the conversation actually managing to smooth things over to some extent, I still can’t help but feel uncomfortable around Molly."
    "I’m pretty sure she notices this, too, as she slides closer to the edge of her bench and further away from me."
    "It’s no longer just inches between us."
    "It still feels like miles, though."

    $ renpy.end_replay()
    $ molly_love += 5
    $ mollysad = False
    $ christmastwo5 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}I wonder if you’ll ever find out what really happened on Halloween!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo6

label christmastwo6:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
i "In the future, if you ever want to give me a return present or anything like that, just give me a hug. I’ll always accept one of those from you."

    if bonus == False:
        s "=D !!!!!!!!!!!!!!!!!!!!!!!!"

    i "Which isn’t me insinuating that I want you to hug me right now. Even though I do. I just understand that you’re still probably put off by the fact that I made you something so large that-"
    u "Just fucking hug him, Io. "
    i "Can I? Please?"
    s "I don’t know. I still feel kind of put off by the fact that you made me something so large that-"

    scene dodgingsnowflakes13
    with dissolve

    u "Hug the Io, damn it!"
    u "Do you have any idea how much she busted her butt on this thing? The least you can do is give her some of that sweet, G-rated loving!"
    s "Okay, fine. Go."

    scene dodgingsnowflakes14
    with fade

    i "Woo! Hug-based victory! All of the calluses and splinters are suddenly worth it!"
    s "You should value your time and talent more. This sort of payment would never hold up in the business world."
    i "That might be true! But you know what else is true?"
    s "What, Io?"
    i "I like you."
    s "Yes, you’ve made that quite apparent."
    i "Let’s run away together. All three of us."

    scene dodgingsnowflakes15
    with dissolve

    u "Wait a sec, I’m coming too?"
    i "Of course you are. You’re my best friend. Do you have any idea how awesome it would be to leave everything behind {i}except{/i} for you two?"
    u "I..."
    i "..."

    "I obviously have no intention of doing any of this, but I guess it’s fine to let Io fantasize for a little while."
    "One hug in exchange for tens of hours of work isn’t really fair, so I’ll just consider this an added bonus that tips the scale a little further in my favor."

    scene dodgingsnowflakes16
    with dissolve

    u "Where...would we go?"
    s "Wait, are you actually considering this?"
    i "Anywhere and everywhere. Just the three of us. "
    u "That sounds...nice, but..."
    u "You know, I just can’t see myself having fun watching you two all...huggy all the time."

    if bonus == True:
        s "I am definitely not a “huggy” person."
    else:
        s "That is very unfortunate because I am all huggy all the time."

    i "You wanna join in? We’ve got room for one more."

    scene dodgingsnowflakes17
    with dissolve

    u "Oh, no...That’s your present. I didn’t get Sensei anything, so...I’d just be getting in the way."
    i "Suit yourself then. He’s really comfy. And suspiciously cold."
    s "I don’t see what’s suspicious about walking here in the snow, but I’m glad to hear that you’re comfortable."
    s "Now, if you could please let go, I’d like to make arrangements for how exactly I’m going to get this thing out of here..."

    scene dodgingsnowflakes14
    with dissolve

    i "You really don’t hate it, Sensei?"
    s "No. And I didn’t hate the robot either. Stop assuming I’m just going to hate everything that you do when history very much begs to differ."
    i "I make no promises."
    i "Oh! And, I forgot to ask earlier, but are you coming to the Christmas party tomorrow? Because you being there directly influences whether or not yours truly will be in attendance. "
    s "I will, but don’t take that as me agreeing to spend the entire party with you since I normally wind up getting pulled around at events like this."
    i "That’s fine. I don’t mind pulling a little bit. It’s good exercise. "
    s "Then I will see both you and Uta tomorrow."
    u "Yeah..."
    u "It should be fun."
    i "Do you want me to just keep the wardrobe closet thing right where it is until you can figure out how to get it out of here?"
    s "I mean...do you have other options for where you could put it?"
    i "No. I don’t know why I asked that. I’m an idiot. No wonder you won’t date me."

    scene black
    with dissolve2

    s "Okay, that’s enough hugging for tonight."
    i "I completely understand and thank you for managing to put up with it for so long."
    s "Right. Well, I’ll see you two tomorrow, I guess."
    i "Okay! Goodnight, Sensei! See you tomorrow!"
    u "Goodnight, Sensei."

    play sound "dooropen.mp3"

    "I make my way out of the dorm room and begin to flip through a mental list of contacts to determine who would best be able to help me with this."
    "Within a matter of seconds, I’m able to cut the list down to just Haruka and Maki since they’re the only people I know who can drive."
    "Well, Niki too, I guess- but she’s probably off being famous somewhere."
    "I’m not sure if either one of my choices has a vehicle large enough to fit my present but, at the same time, I-"

    stop music

    $ renpy.end_replay()
    $ christmastwo4 = True
    jump christmastwo5
...
```