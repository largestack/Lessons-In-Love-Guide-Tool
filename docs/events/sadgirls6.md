# Rolling Stop
Maki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls6&go=Go)


Part of event chain [Again, I Can't Recall](./sadgirls5.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: sadgirls6
* Group: Maki
* Triggered by label: sadgirls5

## Event code
File: \game\MakiEvents.rpy
Code:
```python
...
label sadgirls6:
    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    scene makidrive1
    play music "goodmorning.mp3"

    a "Sensei?..."
    a "I’m sorry to wake you up so early, but..."
    a "There’s a stranger in our house."
    s "..."
    a "..."

    scene black
    with dissolve

    s "I’m going back to sleep."
    a "You’re going to leave me to die just like that?!"

    scene makidrive2
    with dissolve

    s "Ami, if there was an actual stranger in our house, I know for a fact you wouldn’t be calmly discussing it with me after gently waking me up."
    a "Okay...So maybe it isn’t a {i}stranger{/i} per se, but it’s still someone who shouldn’t be here!"
    s "Then tell them to go home. I’m tired."
    a "I tried! But she walked right past me and poured herself a cup of coffee that I made for {i}you{/i} and then sat down on the couch like she owned the place!"
    s "Ugh...who is it then? Noriko? Ayane?"
    a "It’s that frickin’ lube dealer again! And she didn’t even bring any samples this time!"

    "Maki? "
    "She’s {i}here?{/i}"

    s "If it’s her...I’ll be up in a second. I just need to get dressed."

    scene makidrive3
    with dissolve

    a "What do you mean, “{i}If it’s her?”{/i} How the heck am I supposed to interpret that?"
    s "You can interpret it by making more coffee since Maki has apparently taken mine."

    scene makidrive4
    with dissolve

    a "Fine! But only because I love and would do whatever you tell me, no matter what it is."
    s "I’m aware. Thanks, Ami."

    scene black
    with dissolve2

    "Ami leaves the room and I bring myself to my feet, throwing on the shirt Molly made for me- a shirt that was neatly folded by my “beloved” niece and placed on my desk sometime this morning."
    "If Maki’s here, it can really only mean one of two things."
    "Either the conversation she had with Sara yesterday dramatically failed and she has nowhere else to turn to-"
    "Or it {i}didn’t{/i} fail. And she just needs my help with Makoto again because she can’t figure out how to believe in herself as a parent."
    "I’m not sure why that would cause her to believe in {i}me,{/i} a significantly worse “parent,” but if she’s already here, I shouldn’t keep her waiting."
    "Especially since every second I spend not supervising Ami when she’s near her increases Maki’s chance of being poisoned."

    scene makidrive5
    with dissolve2

    maki "Morning. Do you always sleep this late?"
    s "It’s like 8:00 AM."
    maki "I know. I just figured I’d try making a joke that isn’t depressing, dark, or sexual. Which is probably why it didn’t come out very funny."
    s "While I admire the effort, I {i}would{/i} like to know what you’re doing here."
    maki "Not even going to {i}try{/i} waking up first? Just gonna jump straight to business?"
    maki "Sit down. Have a cup of coffee. Take your time. I’m in no rush."

    scene makidrive6
    with dissolve

    a "You {i}drank{/i} his coffee. Now I have to brew more since {i}somebody{/i} doesn’t have any manners."
    maki "While you’re at it, would you mind making some more for me as well? I’ve been up since 4:00 AM, so I can kind of use it."
    a "Would you like me to add a little something to it that will help you sleep better tonight? {i}Much{/i} better?"

    "Okay. So, apparently supervising Ami won’t stop her from trying to poison Maki either. That’s...good to know."

    s "Ami, don’t poison our house guests please."

    scene makidrive7
    with dissolve

    a "You never let me do anything fun anymore!"
    maki "Thanks for looking out for me. I roofied myself once just to see what it was like and, honestly? It’s not really all it's cracked up to be."
    s "I...don’t think that’s a thing people really “crack up” to be all that exciting."

    scene makidrive8
    with dissolve

    "Ami returns to the kitchen, giving me an opportunity to press a little further about Maki’s reason for coming. "

    maki "Want to go for a drive?"

    "But before I can even ask, she opens her mouth and says that."

    s "Depends. Are you so deeply distressed that you’re going to drive us off a cliff?"
    maki "No. But I {i}will{/i} drive at least 20 mph over the speed limit and make plenty of rolling stops."
    s "You’re lucky Kumon-mi uses American measurement systems or I wouldn’t even know how fast that is."
    maki "And you’re lucky that the roads aren’t busy this early in the morning. Rolling stops are dangerous."

    scene makidrive9
    with dissolve

    maki "Especially when-"
    s "Talk about something else."

    scene makidrive10
    with dissolve

    a "Hm? Did I miss something?"
    s "No."
    maki "..."
    s "..."
    a "...?"

    scene makidrive11
    with dissolve

    maki "Got it."
    maki "Anyway, as I was saying, you’re coming with me. I’ve got a {i}little{/i} bit of a problem I could use your help with."
    s "Does that problem wear glasses and get straight A’s?"
    maki "Usually. Right now? Not really."
    a "Does this have something to do with Makoto getting called to the office the other day?"
    a "Because if she’s been starting trouble, I don’t know if I’ll feel safe in class anymore. "
    a "As the class president, she should be-"
    s "Knock it off, Ami."

    scene makidrive12
    with dissolve

    a "I was only kidding this time!"
    maki "Makoto’s fine. We’re just having some family problems right now."

    scene makidrive13
    with dissolve

    a "Family problems?..."
    maki "It’s nothing you need to worry about."
    a "..."
    maki "...?"
    s "Ami?"

    scene makidrive14
    with dissolve

    a "Oh! Umm..."
    a "Coffee!"
    a "I’ll...be right back."

    scene black
    with dissolve2

    "Strangely enough, Ami retreats to her room without being told after bringing the two of us a fresh pot of coffee."
    "I guess saying “strangely enough” is a little...dismissive, though. Especially when it’s likely that she’s in the early stages of putting two and two together."
    "But while I wish I could stick around and see firsthand just what that dramatic realization does to her, I have been given a job."
    "I am not sure if it is a job that I can handle...nor a job I even {i}want,{/i} but Maki’s assertion (Combined with her exceedingly flattering soccer mom getup) forces me to come along regardless of what I want."
    "And before I know it, I find myself in the passenger seat of a car- checking three times to make sure my seatbelt is buckled."
    "........."
    "......"
    "..."

    scene makidrive15
    with dissolve2

    maki "Are you nervous?"
    s "About what? Seeing Makoto?"
    maki "About anything. You’ve been biting your nails and staring out of the window ever since I started the car."
    maki "My driving isn’t {i}that{/i} bad, is it?"
    s "Your driving’s fine. I didn’t even realize I was acting strangely."
    s "I don’t know. Maybe I {i}am{/i} nervous about seeing Makoto. But it would be a more...subconscious thing than me actively going over it in my head."
    s "Cheering people up isn’t really one of my specialties."
    maki "Yeah, that’s one of many things we have in common. And probably the most boring and depressing out of all of them as well."
    s "So, how is she doing exactly? And...better question, what do you want {i}me{/i} to do about it?"
    maki "I’m pretty sure she hasn’t left her room since I took her home on Friday. But I was out for a good portion of the day yesterday, so I guess it’s possible she got up to use the bathroom or something."
    s "I really hope so."
    s "I’m surprised you felt comfortable leaving her, though. I figured you’d be attached at the hip right now."
    maki "To be completely honest, I’m pretty sure that would just makes things worse for her."
    maki "Miku’s been staying over, though. And at least Makoto doesn’t try to keep {i}her{/i} away."
    maki "I dropped her off back at the dorm this morning. Poor girl’s gotten less sleep than both of us."

    if kirinkill == False:
        s "Yeah, well..."
        s "I think we both probably know why."

        scene makidrive16
        with dissolve

        maki "I mean...{i}I{/i} know why. Do {i}you{/i} know why?"
        s "I know enough about her past to piece it together. I just don’t really know the specifics."

        scene makidrive15
        with dissolve

        maki "Huh."
        maki "You two are closer than I thought. "
        maki "Miku doesn’t normally share that with people she doesn’t completely trust."
        s "To be fair, I didn’t exactly learn it from {i}her.{/i}"
        maki "At the risk of harboring a vendetta against whoever told you, I’m going to suggest that we cut this conversation short and just...leave it at our mutual understanding of Miku’s sadness."
        maki "That girl’s been through enough. Talking about this without her knowing just doesn’t sit right with me."
        s "Fair enough. I wasn’t trying to get the details out of {i}you{/i} or anything."
        maki "If Miku trusts you, she’ll tell you. That’s really all you need to know."

    else:
        s "She really cares about Makoto, doesn’t she?"
        maki "Yeah..."
        maki "Yeah, she does."

    "Maki goes back to focusing on the road as a long and uncomfortable silence emerges from the backseat of her car and crawls its way onto the center console."
    "In this abrupt, unwelcome separation comes the realization that I am biting off much more than I can chew right now."
    "That realization grows and festers with every passing stoplight, infecting my body and liquefying my teeth to the point where I can no longer bite anything."
    "It doesn’t make a difference whether or not Maki intends to drive us off a cliff when I started falling to my death the moment I checked my seatbelt for the third time."
    "I want this car to turn around."
    "I want the suffering to end without my intervention- because if there is anything I have learned over my time here, it is that the past repeats itself."
    "And that if my ways of handling Makoto were even the slightest bit successful, I wouldn’t have to keep fixing her."

    maki "You’re doing it again."
    s "Doing what?"
    maki "Biting your nails. "
    s "..."
    maki "You should stop. It’s gross."

    scene black
    with dissolve2

    "Maki continues driving, twenty miles per hour over the speed limit on almost every street we take."
    "But she stops at every stop sign."
    "........."
    "......"
    "..."

    scene makidrive17
    with dissolve2

    maki "So, uhh...do you mind if I get mildly sappy for a minute or two before I take you up to see Makoto?"
    s "Take as long as you like because I still have no idea what I’m going to say to her."
    maki "I mean...I don’t think you really need to say {i}anything.{/i} It’s not like I expect you to go up there and be like, “Hey, Makoto. Sorry your dad’s dead. Feel better now.”"
    maki "She just..."
    maki "I don’t know. I keep wanting to say this is something I should be able to handle on my own, but...the more I think about it, the more I realize that might be the exact problem."
    maki "Makoto can’t see {i}me{/i} without also seeing her father. And it’s that constant reminder that I think is making this so hard for her."
    s "So...serious question. Do you think she can see {i}me{/i} without seeing her father?"

    scene makidrive18
    with dissolve

    maki "I think..."
    maki "Okay. So, you’re obviously the only male authority figure left in her life now. And one that she admires greatly."
    maki "But even with that, I don’t think she’ll ever see you as anything more than her teacher or...maybe a schoolgirl crush."

    "I think it’s a lot more than just a {i}crush{/i} at this point..."

    maki "That girl just...does better with people like you than people like me. It’s a respect thing."
    maki "Like, how is she going to be consoled by someone she automatically associates sex jokes and dildos with? "
    maki "Each time I try to hold her hand, she’s probably thinking “Wow, this hand has touched so many sex toys.”"
    s "I haven’t seen Makoto since Friday, but I’m pretty sure that is not what she’d be thinking."

    scene makidrive19
    with dissolve

    maki "I don’t {i}know{/i} what she’d be thinking, though. I {i}never{/i} know what she’s thinking because her brain is on another level than mine."
    maki "She’s stubborn. She needs someone on the {i}same{/i} level as her to talk to or she’s just going to keep circling the drain."
    s "With all due respect, I think Makoto is several levels above me as well."
    maki "She might be. But I don’t think she sees it that way."
    maki "To her, you’re a role model. Someone she aspires to be. Someone she’ll actually {i}listen{/i} to because you’re not just a joke to her."
    maki "You’re not {i}me.{/i}"
    s "..."

    scene makidrive20
    with dissolve

    maki "Oh, and if you’re having second thoughts about this, I’m not giving you a ride home. I am out of other options and turning to you is pretty much my last ditch effort."
    s "Have you considered {i}time?{/i}"

    scene makidrive21
    with dissolve

    maki "Well, obviously! But time alone doesn’t cure anything when it feels like the walls are closing in around you."
    maki "I need her to feel safe. I need someone to stop those walls from closing in and I’m not strong enough to hold them back on my own."
    s "For what it’s worth, I think you are. But fuck it. I’ll give it a shot. "
    s "If this doesn’t work though and your daughter just winds up becoming even {i}worse{/i} due to something I said, you owe me free porn forever."
    maki "That’s so much porn!"
    s "Yes. I have a problem."
    maki "Okay, fine. But don’t go screwing this up on purpose just to fuel your addiction. "

    "So either Makoto cheers up or I get free porn forever. At least I can’t lose anymore."

    s "Deal. Pleasure doing business with you."
    s "Maybe I’ll even throw in an added bonus of trying to cheer {i}you{/i} up if whatever methods I use on Makoto actually work."

    scene makidrive22
    with dissolve

    maki "Oh, come on...You don’t have to worry about me. "
    maki "I’ve got two close friends who can cheer me up when I need it. You’re here for my daughter."
    s "I am. But I’m here because {i}you{/i} brought me. Which means that you deserve something too."

    scene makidrive23
    with dissolve

    maki "Then I’d like to sacrifice my reward for an additional serving of Makoto’s happiness."
    s "You know...you’re a pretty great mom for someone who thinks they’re a pretty {i}shitty{/i} mom."
    maki "Tell me that again when I don’t feel pressured to rely on a third party to console my daughter because I suck at it."
    maki "And then again when I stop being creeped out by how {i}off{/i} she looks when she’s grieving."

    "..."
    "Wait..."

    scene makotoflashback with fade

    mak "Until everything melts down and reforms into one disturbing mass of flesh, complete with twelve smiles. "
    mak "One for each girl in class that you [masturbate] to while all alone in bed at night."

    scene makidrive23
    with fade

    "Oh no."

    s "Uhh..."
    maki "Welp! Time to go. Makoto’s not going to cheer {i}herself{/i} up."
    s "On second thought, maybe I’ll-"

    play sound "dooropen.mp3"
    scene black
    with dissolve
    stop music fadeout 20.0

    maki "Nope! No more procrastinating. We’ve talked for long enough."
    s "But what if I’m also creeped out by her?"
    maki "You’re like three times her size. What do you possibly have to be afraid of?"
    s "You sell whips. What do {i}you{/i} have to be afraid of?"
    maki "Are you suggesting that I {i}whip{/i} my daughter? I’m into some weird shit, Sensei, but that’s just crossing a line."
    s "Hah..."

    "Maki leads me up a dark staircase, but it’s not dark enough to conceal the array of framed photos hanging on her wall."
    "They’ve all been turned backwards."

    $ renpy.end_replay()
    $ maki_love += 3
    $ sadgirls6 = True

    "........."
    "......"
    "..."

    jump sadgirls7

label makiinv3:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
maki "ONE FUCKING TIME!"
    maki "YOU CALLED ONE TIME!"

    scene harukaandco30
    with dissolve

    maki "Is that seriously all I’m worth to you?"
    maki "Did you think you could just fucking show up here with {i}flowers{/i} in your hand and make it all okay? "

    scene harukaandco31
    with dissolve

    maki "Don’t tell me I shouldn’t be holding things in when letting them out makes the whole world fucking implode."
    maki "And don’t pity me either. Because the idea of someone who can’t handle her own problems telling me how to handle {i}mine{/i} is just insulting."
    sar "She doesn’t mean that, Haru-chan...She doesn’t."
    maki "It’s not fair."
    maki "It’s just not fair."
    maki "Why couldn’t my husband live too?"
    maki "Why couldn’t I have gotten the same call you did?"

    scene harukaandco32
    with dissolve

    h "Because I’m lucky...theres nothing more to it than that."
    h "If the outcome of our phone calls was based on who we are as people or how decent we’ve been to each other...I know our positions would be swapped right now."
    h "And I know that you would have been the first one to get in contact with me."
    h "I wasn’t, and I’m sorry for that. I’ll be sorry for it for the rest of my life."
    h "What I won’t do is give up on telling you when I think you’re making things harder for yourself than they have to be."
    h "No one’s expecting you to hold yourself together, and I’m sure that includes your daughter."

    scene harukaandco33
    with dissolve

    h "Also, I didn’t buy you these flowers to try and make everything okay. I bought them because I think you deserve something nice now that everything else has been taken away from you."
    h "And also because I was pressured into it by some woman in the convenience store who may or may not be the mother of one of my employees."
    h "The point is, I wasn’t there for you when I should have been. "
    h "But I’m here now, asking for forgiveness when I know I don’t deserve it because beneath the selfishness and inability to look forward, I love you."

    scene harukaandco34
    with dissolve

    maki "Haruka, I...I didn’t mean to hit you. I’m just..."
    maki "It really hurts..."
    maki "I’ve never felt so alone before..."
    h "Sara, can you take these flowers from me for a second?"
    sar "Huh?...Sure, but..."

    scene harukaandco35
    with dissolve

    h "Come here."
    h "I don’t care that you hit me, Maki. It’s not a big deal."
    maki "You’re...{i}sniff...{/i}only saying that because...{i}sniff...{/i}you like it rough..."
    h "No. I’m saying that because after all of the times you’ve been there for me, the least I can do to make it up to you is let you knock me around a little bit."
    maki "Just...{i}sniff...{/i}be there for {i}me.{/i} That’s all I want..."
    h "I will. I promise. "
    h "But in the meantime, cry as much as you want. I took the day off to spend it with you. And if that means becoming a handkerchief, so be it."
    h "Also, I hope that you’re okay with blue. The girl at the convenience store said it might be too “aggressively apologetic.”"
    maki "{i}Sniff...{/i}"
    maki "Blue is my favorite color..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2

    "Again, I can’t recall where the day went."
    "After leaving the cafe, I wandered the streets...half-expecting to bump into a girl fighting a war with herself behind the scenes, trying to reclaim what little sense of dignity I haven’t already robbed her of."
    "The fact that I didn’t find her at all speaks volumes about the shape she must be in right now."
    "But at least she’s not alone in her misery- for even further behind the curtain are two more girls. "
    "They both wear glasses. Both have blue eyes. And they both just lost a man who, even in death, will remain far more important to them than I ever will."
    "Which is why I’m not with them right now."
    "Sometimes, it’s necessary to settle for second place."
    "It’s necessary to detach yourself from things you became unintentionally glued to."
    "To slip out of your skin...and wander deep into the darkness, for that’s the only place you won’t be able to hurt anyone."

    scene black
    stop music

    "But sometimes, the ones you fear hurting find {i}you.{/i}"
    "Because, contrary to what you may believe-"
    "You are never truly alone in the dark."
    "{i}In the bowels of the night, unconscious as you are, you swallow a spider.{/i}"
    "{i}You awaken with a mouth full of eggs.{/i}"

    $ renpy.end_replay()
    $ sadgirls5 = True

    play sound "static.mp3"
    scene spider1 with flash
    scene spider2 with flash
    scene spider3 with flash
    scene spider4 with flash
    stop sound
    jump sadgirls6
...
```