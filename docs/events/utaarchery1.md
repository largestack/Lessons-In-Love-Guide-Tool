# Impulse
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utaarchery1&go=Go)


Part of event chain [Cupid's Arrow](./ioarchery1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Uta: Where Wishes Come True](./utamaid25p1.md)

## Event properties
* ID: utaarchery1
* Group: Uta
* Triggered by label: ioarchery1

## Event code
File: \game\UtaEvents.rpy
Code:
```python
...
label utaarchery1:
    scene utadownbad1
    with dissolve2

    u "Sensei? When did you get here?"
    s "Somewhere around when you started holding hands with Wakana. I left though since I figured you two probably wanted to be alone."

    scene utadownbad2
    with dissolve

    u "Ah...Yeah, I don’t really know how Osako-chan would feel about me stealin’ her girlfriend out from underneath her. "
    s "I’m honestly surprised she even kept that job. I figured it was just a temporary thing while the dojo was stuck in limbo."

    scene utadownbad3
    with dissolve

    u "Gotta make that money somehow, Sensei. Osako-chan’s gotten a taste of that sweet nectar and ain’t ever looking back. "
    s "Don’t talk about Osako tasting nectar anywhere near Wakana. She’s already worried I’m going to steal her woman."
    w "I can hear you, Arakawa."
    s "See? She’s terrified."

    scene utadownbad4
    with dissolve

    i "Are you done being an archer now? Can we go back to being friends?"
    u "Do we always stop being friends whenever I do something for myself?"
    i "Uta, I have extreme social anxiety. We stop being friends whenever I can’t see you."
    u "Io, the fact that you function at all is something I think we should be proud of. "
    i "I’m not sure if I’d call what I do “functioning,” but I am in an extremely good mood right now, so...what the heck. Sure. Let’s all be proud of me for a minute."
    i "Just a minute, though. Any longer than that and I will actually die."

    scene utadownbad5
    with dissolve

    u "You?...In a good mood?..."
    u "You and Sensei weren’t playing tonsil hockey behind the storage building, were you?"
    i "Even better. He was opening up to me."
    s "I said literally one thing."

    scene utadownbad6
    with dissolve

    u "Hah...it’s like the leaderboard of this harem changes every time I close my eyes. "
    u "Gonna have to break out my notebook when we get back home and see which spot you’re in now, Io."
    s "You don’t actually have a harem leaderboard, do you?"

    scene utadownbad7
    with dissolve

    u "Well, what else am I gonna do in class? You don’t make me study anymore. "
    u "I’m like four pages of harem notes away from starting a whole betting ring, Sensei. Do you have any idea how much money there is to be made off of this?"
    s "Am I just a toy to you?"

    scene utadownbad8
    with dissolve

    u "No. But you {i}are{/i} a toy to Uta-chan. And I can swap personas any time I like, Master."
    s "Marry me."

    scene utadownbad9
    with dissolve

    u "What do you think you’re doing, Sensei? Proposing to someone in the bottom ten when you’ve got a higher ranked girl right next to you?"
    i "In his defense, I am definitely not marriage material. In fact, I think even the concept of marriage is archaic and stupid. Why should we have to sign a sheet of paper to prove that we-"

    scene utadownbad10
    with dissolve

    u "Shush."
    i "Okay."
    s "Can I ask who number one in your...weird ranking thing is?"

    scene utadownbad11
    with dissolve

    u "I mean...you {i}can.{/i} I’m just not sure if you want to know the answer."
    s "Why wouldn’t I want to know the answer?"
    u "Cause it’s Ami."
    s "..."
    i "{i}Hah...{/i}"
    u "See? Even Io’s disappointed in you and she’s your number one fan."
    s "First off, no one should be disappointed in me when this ranking clearly has nothing to do with-"
    u "Ah-ah-ah. Before you go saying “this ranking has nothing to do with how I treat girls and is based on how much they love me,” it {i}absolutely{/i} has {i}everything{/i} to do with how you treat us."
    u "Ami gets more special treatment than anybody. "
    u "Combine that with the fact that she’s also one of the most vocal about her love for you {i}and{/i} how you guys go way, way back and you’ve got a combined Uta-chan certified compatibility score of...9.7/10."
    s "That is way too high of a score for my compatibility with my {i}niece.{/i}"

    scene utadownbad12
    with dissolve

    u "Love comes in all kinds of forms, Sensei."
    s "Is that why you had a crush on a sponge?"

    scene utadownbad13
    with hpunch

    u "Don’t bring the sponge into this! That was basically a zillion years ago! My tastes have changed since then! I like humans now!"
    i "Uhh..."
    u "Great! Now Io knows about the sponge! Look what you did!"
    s "I thought Io already knew about the sponge."
    i "I feel like I know less and less every time you say “sponge.”"

    scene utadownbad14
    with dissolve

    ki "Io! Wakana says you have to come help me clean up the storage room since you sat around all day being worthless."
    i "What? Since when is that a thing I get punished for?"
    w "Kanda-san, if you call me “Wakana” one more time, I will see to it that you’re removed from this club and sent off to practice kyudo in the sinkhole."
    s "I think this is your chance, Io."

    scene utadownbad15
    with dissolve

    i "But I want to keep hanging out with you and Uta. My day finally became bearable."
    u "We’ll be here when you get back, Io. I ain’t doing anything today. Sensei and I will just hang out and..."
    u "And I guess that’s it. We’ll just hang out."
    ki "Greenie! Hurry the fuck up! I have shit to do after this!"

    scene utadownbad16
    with dissolve

    i "Stop calling me that, you incorrigible bimbo! I have a name!"
    ki "Yeah but you throw a hissy fit whenever I use that as well. Just get over here and help me clean already. "
    i "Fine. But if you expect me to talk to you while we’re in there, I’m walking right back out."

    scene utadownbad17
    with dissolve

    i "I’ll be back, I guess..."
    u "Uhh...yeah. Have fun. "

    "Io wanders off to join Kirin in the shed and, despite my suggestion that she try and befriend her just a short while ago, I have a creeping feeling that that won’t be happening today."
    "On the bright side, though...she {i}did{/i} agree to contributing in some way, which is more than I’d typically expect from her. "
    "Who knows? Maybe she really {i}is{/i} so desperate to please me that she’s going to actually start taking a few steps forward?"

    u "..."

    "Or maybe she’s just trying to somehow increase her place in the unofficial harem ranking."

    scene utadownbad18
    with dissolve

    u "So, now that you’re alone with Uta-chan (Archer form), what do you wanna do? You ever use a bow before?"
    s "Do I look like the type of guy who has used a bow before?"
    u "No. But you look like the type of guy who’s {i}about{/i} to."
    s "What?"

    scene black
    with dissolve

    u "Come on! Take this! I’ll show you how it’s done!"
    u "I’m not as good of a teacher as Miss Watabe, but if you’re gonna learn this from anybody else, I’m probably the one you wanna come to!"

    "Uta hands me the bow (Which I have no idea how to hold properly) before grabbing my waist and redirecting me toward the targets at the far end of the range."
    "That part I probably could have figured out on my own, but I’m not about to deny any amount of physical contact from Uta-chan."

    scene utadownbad19
    with dissolve2

    "{i}This{/i} level of physical contact is not what I expected, though."
    "Instead of coaching me from the sidelines or nearby like I expected her to, Uta takes her place directly behind me and rests her hands on my arm and my wrist respectively."
    "Her chestguard presses up against my back and robs me of a sensation I have longed for, but my imagination does its job and fills in the blanks for me so I don’t miss out entirely."
    "Then, from what feels like miles below, a bright and joyous voice with a mild rasp to it cuts through the air, crawls up my back, and nests in my ears."

    u "Don’t pay any attention to me, okay? Just straighten out your limbs and try to stand up straight."
    u "Also, please don’t let go of the string. I don’t want it to snap back and break all of my fingers off."
    s "You’re sure asking a lot out of a first-timer, huh?"
    u "Yeah, but only cause I think you’d be pretty good at this with some practice."

    scene utadownbad20
    with dissolve

    u "Your body’s kinda huge, Sensei. And your figure is great too. "
    u "If a girl my size is able to handle a bow as well as I can, just imagine how the snap will sound when {i}you{/i} launch your arrow."
    s "I’d say we should find out, but I think you said something about wanting to keep your fingers."
    u "That is correct. Updating my harem ranking will be hard if I can’t write anymore."
    u "Also, don’t get cocky thinking your shot will echo across the range on the first try. There’s a lot more to kyudo than raw power. That’s only a tiny part of it."
    u "I’m just saying it {i}could{/i} sound beautiful one day. And that you {i}might{/i} be great at this if you keep practicing."
    s "I’m open to practicing as much as you want so long as we can always do it like this."

    scene utadownbad21
    with dissolve2

    u "Uh..."
    s "What’s wrong?"
    u "..."
    s "..."
    u "..."
    s "..."

    scene utadownbad22
    with dissolve

    s "Uta? "
    u "We can practice whenever you want."
    s "I get that. But you’re-"
    u "I’m just making sure your posture stays good. You can keep ignoring me."

    scene utadownbad23
    with dissolve

    s "I think that might be a little easier said than done."
    u "I’d say I’m happy to hear that, but that would basically be the same thing as admitting that-"
    i "What are you guys doing?"

    scene utadownbad24
    with hpunch

    u "UHH! NOTHING! ARCHERY! POSTURE! "
    u "JUST...HELPING SENSEI WITH HIS FORM!"
    i "Cool, but...why are you yelling?"
    u "Because I’m...in the zone?"
    i "Huh. Well, I’m done for now if you guys want to-"
    u "Actually! Uhh...I have to talk to Sensei about something he just told me!"

    scene utadownbad25
    with dissolve

    s "You do?"
    u "SHH! She saw me hugging you! Act sad."
    s "But I-"
    u "Sensei! Please!"

    scene utadownbad26
    with dissolve

    s "I’m sad and I need Uta’s help for some reason."
    u "S-See?! The poor guy’s basically in tatters! But give me a few minutes with him and I’ll whip him right back into shape for you, Io!"
    i "For me? Why would that be for me? If Sensei’s actually feeling down, shouldn’t you be doing that for {i}him?{/i}"
    u "That’s...yes! That’s what I meant! But you are also here, so...when I return, you will also reap the benefits of...his happiness!"
    i "..."
    u "..."

    scene utadownbad27
    with dissolve

    i "You’re acting really weird right now. "
    u "I just..."
    u "I feel really...bad for him...because of the sad thing he told me..."
    s "It really is sad."
    u "{i}Just start walking away. She’ll wait.{/i}"
    s "I’m going to start walking away now."

    scene utadownbad28
    with dissolve

    u "We’ll be back in a few minutes, Io! Don’t...go anywhere!"
    s "I sure hope I don’t stay sad any longer."
    u "{i}Give it a break, Sensei! Your acting sucks!{/i}"
    i "..."
    i "..."
    i "..."
    i "What the heck just happened?"

    scene black
    with dissolve2

    "........."
    "......"
    play sound "slidedoor.mp3"
    "..."

    scene utadownbad29
    with dissolve2

    u "(Screaming internally)"
    s "I feel like you could have handled that a little better."
    u "Yeah, you’re one to talk with all of that “I’m so sad! Woe is me!” crap! Those acting chops wouldn’t last you one minute in a maid cafe!"

    scene utadownbad30
    with dissolve

    s "Hey, you sucked too. I’m starting to think you get your powers from the uniform."
    u "It definitely helps!"
    s "So, are you going to tell me why you pulled me into this-"

    scene utadownbad31
    with dissolve

    s "Wait...where even are we?"
    u "The tea ceremony room. "
    s "We have a tea ceremony room?"
    u "We have a whole tea ceremony club. They just happen to use one of the buildings near the archery range since this is where they keep all the...old school stuff, I guess."
    s "Okay, but then...why exactly did you pull me into the tea ceremony room?"

    scene utadownbad29
    with dissolve

    u "I have no idea! It just happened! "
    u "At first, it was probably because I didn’t want Io to think anything suspicious was going on, but now I realize that this just makes everything look even {i}more{/i} suspicious!"
    s "Then...should we go back out there?"
    u "No! Because coming in here for just one minute would make everything even {i}more{/i} suspicious!"

    scene utadownbad32
    with dissolve

    s "You really dug yourself into a hole this time, didn’t you?"
    u "Ahhhh! What am I doing, Sensei?!"
    s "You’re being suspicious as hell, that’s what."

    scene utadownbad33
    with dissolve

    s "Or...wait. I think the word is “sus” now. I’ve been hearing the other girls say that lately."
    u "Okay. I need to sit down."

    scene black
    with dissolve2

    "Uta takes her shoes off and sits down on the tatami mat, pulling her knees up to her chest and gently rocking back and forth as I lower myself to meet her."
    "It’s clear that, for some reason, this spur of the moment decision has already turned into spur of the moment regret, but that doesn’t mean we can’t figure out some way to enjoy it."
    "Especially since her best friend is probably still standing exactly where we left her and attempting to wrap her head around everything currently going on."
    "But hey, that’s fine. Because I’m doing the exact same thing."

    scene utadownbad34
    with dissolve2

    "Or, at least that’s what I {i}was{/i} doing before finally getting to look at Uta’s face- which is currently redder than I have ever seen it before."

    s "..."
    u "..."
    s "You just wanted to be alone with me for a little while longer, didn’t you?"
    u "Wh...What makes you think that?"
    s "The face. The rocking back and forth. The nervous poke war your index fingers are having with one another right now."
    u "I’m just...really nervous around tea. "
    s "You know, you’ve said a lot of questionable things over the brief time I’ve known you, but that one really makes me question just what type of person you are, Uta."

    scene utadownbad35
    with dissolve

    u "I’m...not good at thinking things through, okay?! My whole life is a series of weird, impulsive decisions! This is just the first time you’ve gotten wrapped up in one."
    s "There was also the one time in-"
    u "The karaoke collision was an accident! Not an impulse!"
    s "Was almost kissing me {i}after{/i} the collision an accident too?"
    u "Nope! Because that part never happened and it’s all one big fantasy you dreamt up!"
    s "Ahh, okay. Just making sure."
    s "For the record, though- I don’t really think being impulsive always has to be a bad thing. I {i}like{/i} being alone with you. Just...probably not when Io is also expecting to be here."

    scene utadownbad36
    with dissolve

    u "AAAAAAAAAHHHHHHHHHHHHH! "
    s "Uta, chill. It’s really not a big deal. "
    s "Io knows all about you, right? Because, if that’s the case, explaining to her that you just impulsively dragged me in here should fix pretty much every misunderstanding you’re worried about."
    u "It’s {i}because{/i} she knows me so well that I’m worried, Sensei! I’m only like this under very specific circumstances!"
    s "And those circumstances are?"

    scene utadownbad37
    with dissolve

    u "Circumstances I must be very careful with."
    s "And why is-"
    u "Because I don’t want them to get me in trouble. "
    u "And because I’m..."

    scene utadownbad38
    with dissolve

    u "I’m afraid it might happen again..."
    s "Afraid that...{i}what{/i} might happen again?"

    scene utadownbad39
    with dissolve

    u "You mind just giving me a minute to catch my breath and...not make any more impulsive decisions? Cause I’ve only made one so far and even that’s got the potential to flip my life on its head."
    s "I still think you might be overthinking this. I’m pretty sure Io will understand."
    u "I might be using the word wrong, but I’m pretty sure that would be ironic."
    s "How come?"
    u "Because my history of {i}not{/i} thinking about things is the only reason I ever met Io in the first place."

    scene black
    with dissolve2

    "When we leave the tea ceremony room, we find Io crouched over the body of a dead caterpillar- slowly allowing dirt to sift through her fingers and cover it up."
    "She hosts a makeshift funeral for the bug with Uta and I as guests...and doesn’t once question where we disappeared to."
    "She’s too happy to have us back."

    $ renpy.end_replay()
    $ utaarchery1 = True
    $ uta_love += 1
    stop music fadeout 5.0

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label utamaid25p1:
...
```

## Code that triggers this event
File: \game\IoEvents.rpy
Code:
```python
...
scene ioarchery10
    with dissolve

    s "I’m just saying I think you two have a lot in common and that you’d be able to talk without inherently hating one another."
    s "At the very least, it seems like she wants to be friends with {i}you.{/i}"
    i "I don’t really care about what Kirin wants. "
    s "Do you care about what I want?"
    i "Of course."
    s "Just not when it’s something that conflicts with your own personal interests?"

    scene ioarchery11
    with dissolve

    i "Where’s this coming from? I just wanted to hang out with you and have fun. If I wanted to confront my demons first thing in the morning, I would have medicated before leaving the house."
    s "Just a thought. I could have kept it inside but I figured that was pointless since you don’t keep {i}anything{/i} inside ever."

    scene ioarchery12
    with dissolve

    i "I keep plenty inside."
    s "Like what?"
    i "Like how I hate that {i}you{/i} like Kirin when she’s just one out of millions of other fakes wandering around Japan, hoping to find something to make her feel whole."
    i "I also hate her lack of understanding when it comes to people’s boundaries as she would literally {i}not{/i} stop questioning me about you on the way back home from the Christmas party."
    i "But I realize that’s less of a thing I was keeping inside and more of a thing I just didn’t share with you due to lack of timely relevancy. "
    s "She questioned you on the way back home from the Christmas thing?"
    i "Relentlessly. And the vast majority of it was extremely personal. Things no one should just blatantly and unabashedly discuss despite barely knowing one another."

    scene ioarchery13
    with dissolve

    s "Yeah...that sounds like her."
    i "I’ve got...limits, you know? Like, not everything is easy for me to just talk about."
    i "And if I had somebody in my life who was always trying to force that out of me...well, things would suck even more than they do right now."
    s "I get that. But I also think you also have to understand that if things suck right now, they’re going to keep sucking for the rest of forever unless you actually do something about it."
    s "Would you rather get to know someone who’s interested in getting to know {i}you,{/i} despite all of the obstacles you throw their way...or someone who’s shown no interest in you whatsoever?"
    i "The latter. Anyone who shows any interest in me has extraordinarily bad taste."
    s "Try it again but with less self-loathing."

    scene ioarchery14
    with dissolve

    i "But that’s so hard! You’re taking away my most defining trait!"
    s "Yeah, well when your most defining trait is also your biggest weakness as a person, it’s good to peel it back every once in a while."
    s "Being depended on is cool and all and I’m glad that you...think you’re whatever that weird burrowing sperm fish is-"
    i "Anglerfish. "
    s "Yeah, that. I’m glad you’re able to think up weird metaphors about our relationship because it solidifies my sense of importance when it comes to your life and...that’s a thing I think I need."
    s "But I also want you to be able to exist on your own because you remind me of myself and I still don’t really know how to do that."

    scene ioarchery15
    with dissolve

    i "Did you just..."
    i "Did you just open up to me?"
    s "I guess. But I did it more for myself than I did for you."
    s "Watching you “succeed” would be for my own personal benefit at the end of the day. And if getting you to feel uncomfortable in pursuit of that is what it winds up taking, I {i}want{/i} you to be uncomfortable."
    i "Me...making more friends...will somehow make {i}you{/i} feel better about {i}yourself?{/i}"
    s "It’s weird how our minds work sometimes, isn’t it?"

    scene ioarchery16
    with dissolve

    i "That’s so strange. Because any time I think of you forming more relationships, I just get pissed off and jealous."
    s "Not all of my relationships are sexual, you know."
    i "I guess not. But according to Kirin, the ones you care most about are. "
    i "Why she’d somehow spin that into pressuring {i}me{/i} to crumble when she very obviously likes you as well, I don’t get. "
    i "But I guess that all of our minds are little messed up when you start applying actual logic to them."
    s "..."
    i "..."
    i "Is it too much to ask for a brain that doesn’t break down every time you try to use it?"
    s "It’s too much to ask for anything. Life is going to give us what it gives us and all we can do is scarf it down or starve ourselves. There’s no third option."
    i "Life kind of sucks, doesn’t it?"
    s "Why else would we constantly try to distract ourselves from it?"
    i "..."
    s "..."
    i "This was a good talk. I enjoyed this."
    i "I figured I was still like, a year away from learning anything about you. So the fact that I now think I understand something is..."
    i "I guess for lack of a better term-"
    i "A good distraction."

    scene black
    with dissolve2

    "Io and I leave our spot behind the storage building and wander back into the lives of everyone else, knowing full well that our prior distraction had overstayed its welcome. "
    "I’m glad she has another one now, though."
    "What I’m not glad about is that it now feels like a small piece of me is missing."
    "But when I’m the one who ripped it off and so carefully placed it into her hands, I don’t really have any right to complain."
    "When we round the corner, I step on something soft. "
    "It sticks to my shoe and I have to kick the dirt in order to get it off."
    "I won’t tell you what it was."

    $ renpy.end_replay()
    $ ioarchery1 = True
    $ io_love += 1

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "........."
    "......"
    "..."

    jump utaarchery1
...
```