# Again, I Can't Recall (Haruka)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [To Anyone Who Passes By](./sadgirls4.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: sadgirls5
* Group: Haruka
* Triggered by label: sadgirls4
* Chain sources: sadgirls4
* Chain sources path: sadgirls4

## Official wiki page

[Again, I Can't Recall](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls5&go=Go) for more details.

## Event code

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
label sadgirls5:
    scene harukaandco1
    with dissolve2

    h "Hah..."
    r "How’d it go? Were you able to say everything you wanted to say?"
    h "Who knows? I think it went well, but I’m notoriously bad at judging how things are going while they’re actually, you know, {i}happening.{/i}"

    scene harukaandco2
    with dissolve

    r "Well, you’re not alone there. I think Otoha’s mad at me since I didn’t talk Chika out of joining the light music club with us."
    h "You left the manga club? It’s not because of the whole Molly thing, is it?"
    r "No. That doesn’t really have anything to do with it."
    h "Okay. Good. Because I’m calling her in and the two of you are going to be running the rest of the shift together."

    scene harukaandco3
    with dissolve

    r "I’m sorry, what?"
    h "Think you can deal with each other long enough to keep the cafe from burning down?"
    r "Haruka, you understand that leaving me alone to run the shift with Molly means that I’m {i}basically{/i} going to be running things alone, right?"
    h "Yeah. But I trust you and think you can handle it."

    scene harukaandco4
    with dissolve

    r "Oh, you’re {i}good.{/i} You know I won’t be able to say no after flattery like that."
    r "Fuck it. Bring on the weeb. I got this shit."
    h "Thanks, Rin. I appreciate that."

    scene harukaandco5
    with dissolve

    r "What are {i}you{/i} gonna do, then? Go meet up with Makoto’s mom? Or are you gonna go back home and try to erase all the traces of Sensei for when your husband comes back?"
    h "I still have no idea when my husband will be coming back, nor do I understand what “traces” Sensei would even leave behind."
    r "Oh, you know. Condoms. Razors. All kinds of...manly stuff. Whatever dudes carry around with them."

    if harukasex == False:
        scene harukaandco6
        with dissolve

        h "He has no need for condoms when that’s absolutely not the type of relationship we have."
        r "Hey, I didn’t say they had to be for {i}you.{/i} He’s a popular guy, you know? He could be slamming some girl he just met on the street right now and we’d have no idea."
        r "I just hope he didn’t leave all his condoms at your house."
        h "Rin."

    else:
        scene harukaandco6
        with dissolve

        h "You know, I’d really appreciate it if you’d stop pointing out my infidelity now that my husband has come back into the picture."
        r "Why? If your heart’s with Sensei, what good does waiting on him even do?"
        h "Rin-"
        r "I’m serious, Haruka."
        r "I love you and want you to be happy. And I feel like you’ll be making a big mistake if you just cut everything off because of one phone call."

        scene harukaandco7
        with dissolve

        h "You should know by now that this isn’t something I can just {i}cut off.{/i} It’s a lot more complicated than that."
        r "Well, whatever the case may be, I’d like to reinforce my role on Team Sensei. And no, it’s not just because I want to watch you guys do it."
        r "Which I might."
        r "I mean, what? Who said that?"
        r "Don’t fire me."
        h "Rin...stop."

    scene harukaandco8
    with dissolve

    r "So, what now? How are you gonna kick off your girls’ day out on the town?"
    h "We’re not going {i}out on the town.{/i} And frankly, I’d be surprised if Maki even {i}would{/i} go out on the town with me after how I treated her yesterday."
    r "Well, it’s not like you meant to treat her that way, is it? You had your own stuff going on. It’s only natural to think about that first."
    r "As long as you can apologize and be sincere about it, I’m sure you guys can work it out."
    h "Yeah...I’m just not really sure how to apologize for something as serious as this. Especially when she’s going through one of the hardest things she’ll ever have to right now."

    scene harukaandco9
    with dissolve

    r "Yeah...after starting to piece things together, I can kinda see that..."
    r "I wish I had some sort of advice I could give you...but I’ve never really been good at dealing with that sort of thing myself either and-"

    scene harukaandco10
    with dissolve

    r "Wait! What about flowers?"
    h "Flowers?"
    r "Yeah! "
    r "Any time my mom gets into a fight with my {i}other{/i} mom, she always buys her flowers to say she’s sorry. Then, before you know it, they’re back to normal like there was never any fight at all."
    r "This might not work since you and Maki don’t have sex with each other, but I think it’s worth a shot!"
    h "Who says Maki and I don’t have sex with each other?"
    r "..."
    r "Come again?"

    scene harukaandco11
    with dissolve

    h "Kidding."
    h "But...yeah. Maybe a gesture like that {i}would{/i} make things a little bit better. Thanks for the suggestion, Rin."
    r "..."
    r "Were you really kidding just now? And, if so, can you tell me you {i}weren’t?{/i}"
    h "Nope. I’ve got things to do. "

    scene harukaandco12
    with dissolve
    stop music fadeout 15.0

    h "I’ll call Molly now and make sure she comes over, but I’m going to head out if that’s okay with you. You’ll be fine alone for a little while, right?"
    r "..."
    h "Rin?"
    r "..."
    h "..."
    h "Okay. See you later, then."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Somewhere else, shortly after....{/i}"

    scene harukaandco13
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "{i}Flowers, flowers, all around us; to grow and then decay-{/i}"
    "{i}To parallel our livelihoods and mirror passing days.{/i}"
    "{i}When you speak into that mirror, what is it you will say?{/i}"
    "{i}Are you excited for the future? Or do you wish it all away?{/i}"
    "{i}To heart, my friends and family! For these mirrors are just jokes!{/i}"
    "{i}The flowers reek of simile! The metaphors of oak!{/i}"
    "{i}Reverse! Return! Repeat your words! If you keep them in, you’ll choke.{/i}"
    "{i}Press the flowers to your nose; breathe them in like smoke.{/i}"
    "{i}- The girl who cannot breathe{/i}"

    "Hello!"
    "Narrator here again."
    "Did you miss me?"
    "I’ve decided to drop in and speak to you directly about what might be happening while you’re away."
    "It’s come up in the past — the question of trees falling in forests and whether or not they make sounds — and I’d like to confirm here and now that they do!"
    "The issue is that the sounds happen so far away from all of us that’s it’s kind of hard to pinpoint exactly {i}what{/i} noises are produced."
    "So all we have to go off of are past experiences. Memories of what sounds {i}should{/i} be made and how long they will last."
    "Perhaps what you will see next is one of those assumptions. "
    "Or perhaps I just like playing games with you."
    "Does it happen?"
    "Does it not?"
    "You will never know!"
    "But I will."
    "And you are lucky that I am willing to share even this much."
    "Sayonara."

    h "Let’s see...I think flowers should be-"
    q "You! With the boobs! Come here!"

    scene harukaandco14
    with dissolve

    h "Huh? Me?"
    q "Yes! You! Help me!"
    h "Umm..."
    q "Hurry! This is an emergency! My entire life hangs in the balance of this very decision!"

    scene harukaandco15
    with fade

    h "How can I-"
    q "Pink or blue?!"
    h "Uhh...can I ask what the occasion is?"
    q "Repentance!"
    h "I think I need a little more to go off of than just that."

    scene harukaandco16
    with dissolve

    q "I think pink is probably the right choice. Blue comes on too strong. Pink is like “Please forgive me,” while blue is like “I’m fucking sorry, okay?” "
    h "Umm..."

    scene harukaandco17
    with dissolve

    q "Here. Take these. I have made my decision and you look like you’re here for flowers as well."
    h "Is that...really how I-"

    scene harukaandco18
    with dissolve

    q "..."
    h "Well, I guess I don’t have to {i}look{/i} for flowers anymore."
    q "Mmm...I don’t know about this. I’m starting to have second thoughts about pink. "
    q "You know, this whole ordeal would be a hell of a lot easier if they had yellow. I always get yellow. This is the first time I have ever been faced with such a tough decision."

    scene harukaandco19
    with dissolve

    q "Also, hi. Nice to meet you. I swear I’m not normally as crazy as this. You just caught me at a weird time."

    scene harukaandco20
    with dissolve

    h "Oh, it’s fine. This is nothing compared to one of the girls I have to deal with pretty much every day."
    q "You have kids?"
    h "Me? No way. Just a bunch of part timers at a cafe I own about a mile away from here. "

    scene harukaandco21
    with dissolve

    q "Cafe?"
    h "Uhh...yeah. Like...you know. A place that serves coffee?"
    q "Dude, I know what a cafe is. I was just thinking that’s a crazy coincidence since my daughter also works at a cafe about a mile away from here. "
    q "I’m not allowed to go there, though. She says I’ll embarrass her. But I don’t seem that embarrassing, do I?"
    h "Um...just out of curiosity, your daughter wouldn’t happen to be-"

    scene harukaandco22
    with dissolve

    q "Interested in coming to work for you instead? No way. She loves her job. Even {i}if{/i} I’m not allowed to go there. But nice try, random rival cafe lady. "
    h "What? No, I-"
    q "Anyway, it was nice talking to you! Hope that whoever you’re giving those flowers to likes the color blue and how aggressively apologetic it is!"

    scene harukaandco23
    with dissolve

    q "Oh! And if you need a card as well, they’re to the right of the check-out counter!"
    q "If you bend all the corners, they’ll even give you a discount!"

    play sound "entrybell.mp3"

    q "Anyway, bye! Time to go salvage my love life!"
    storec "Wait, miss. You still have to pay for-"
    q "Sorry, can’t talk right now! Keep the change!"
    storec "...those."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Roughly one hour later, in a room less joyous.{/i}"

    scene harukaandco24
    with dissolve2

    "I have no poem nor words of consolation for you this time."
    "Just a glimpse into what may or may not be happening behind your back."
    "And how things can be painful even without you."
    "Sometimes, a tree falls so hard that it can be heard from miles away."
    "And other times-"
    "It’s like an entire forest has collapsed."

    maki "{b}FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUCK!!!!!!!!!!!!{/b}"
    maki "FUCK FUCK FUCK FUCK FUCK! WHY US?! AM I NOT STRUGGLING ENOUGH ALREADY?! I NEED TO STRUGGLE {i}MORE?!{/i}"
    sar "Hey...you’re going to be okay. You’ve been doing great without him. Much better than me, at least."
    maki "I DON’T WANT TO DO IT WITHOUT HIM, SARA! I DON’T WANT TO DO THIS ALONE!"
    maki "I LOVED HIM! I {i}STILL{/i} LOVE HIM! AND NOW HE’S FUCKING GONE! JUST LIKE THAT! WITHOUT EVEN SAYING ANYTHING!"
    maki "DO YOU HAVE ANY IDEA WHAT THE LAST THING I SAID TO HIM WAS?! DO YOU?!"
    sar "Maki..."
    maki "Here! I’ll tell you! It was “Don’t fuck too many aliens!”"
    maki "{i}That{/i} was the last thing I ever said to him! And I can’t take that back!"
    maki "I never thought something like this would happen, Sara! I never realized how cruel and unfair life can be! "

    scene harukaandco25
    with dissolve

    sar "I know...I know..."
    sar "It really is cruel, isn’t it?..."
    sar "How we never realize how close to the end things are..."

    play sound "static.mp3"
    scene harukaandco26
    with flash
    stop sound

    maki "THAT FUCKING IDIOT!"
    maki "WHY DID HE TELL ME EVERYTHING WOULD BE FINE?! WHY DID I BELIEVE HIM?!"
    maki "THIS ISN’T FINE AT ALL! THAT FUCKING MORON! ASSHOLE! UNGRATEFUL BASTARD!"
    maki "FUCKING...DOUCHEBAG! WORTHLESS PIECE OF SHIT! HOW COULD YOU FUCKING DO THIS TO US?!"
    sar "That’s right...let it all out..."
    sar "It’s okay to cry here..."

    scene harukaandco27
    with dissolve

    maki "WAAAAAAAAAAAAAAAAAaaAaAAAAaaaaaahhh!!!!!!!!!!!!!"
    maki "MASAHIRO!!! YOU FUCKING ASSHOLE!!! HOW COULD YOU?!?! HOW COULD YOU?!?!?!?!?!"
    h "Maki...why did you hold this in for so long?"
    maki "HOW THE FUCK WOULD YOU KNOW HOW LONG I’VE HELD IT IN, HARUKA?!"
    maki "WHILE YOU WERE BUSY CELEBRATING, I WAS BREAKING THE NEWS TO MY BABY GIRL THAT THE MAN SHE'S LOOKED UP TO SINCE SHE WAS LITTLE IS NEVER COMING HOME!"
    h "I’m not here to make excuses. Not being there for you was horrible of me. But you’ve always been the type to hold things in until they don’t fit anymore and-"
    maki "THIS IS DIFFERENT! "
    maki "I {i}HAVE{/i} TO DO THAT NOW! IT’S NOT A CHOICE ANYMORE!"
    maki "I’M A SINGLE FUCKING PARENT NOW! I HAVE TO BE STRONG! "
    maki "I CAN’T JUST FUCK AROUND ANYMORE! SOMEONE ELSE’S FEELINGS ARE AT STAKE!"
    h "I’m not saying you should fuck around...I’m saying that your daughter is smart enough to realize you’re hurting too and-"

    play sound "static.mp3"
    scene sadflash1 with flash
    scene sadflash2 with flash
    scene sadflash3 with flash
    scene harukaandco28 with flash
    play sound "slap.mp3"
    with hpunch

    maki "STOP TALKING TO ME LIKE YOU UNDERSTAND WHAT’S GOING ON! STOP TALKING LIKE YOU UNDERSTAND HOW I FEEL!"
    sar "Maki! She was just trying to-"
    maki "SHE SHOULD HAVE BEEN THERE! SHE SHOULD HAVE BEEN THERE FOR ME!"

    scene harukaandco29
    with dissolve

    maki "How many times have you called me to cry about your problems?! How many times have I sat there listening to them?! Consoling you for things you shouldn’t even have to be consoled for!"
    maki "Your husband is still alive and mine has been dead for two fucking months! Two months, Haruka!"
    maki "My daughter lost her father and you didn’t even come over to see how we were doing!"
    h "I called-"
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

label harukalust25intro:
    scene surprisebjcontest1
    with dissolve2
    play music "acoustic.mp3"

    ima "Okay! All set. "
    s "I have several questions."
    ima "No. I will {i}not{/i} let you try on my earrings. "
    s "That...is not one of them. "
    ima "Then either ask them now or be forced to listen to me inaccurately guess what they may be for the rest of the night."
    s "Question one: why are the Kanda sisters behind the counter?"
    ka "You know, I really wish I had an answer to that."
    ki "I do. Karin’s annoying need to always ensure that everything goes well kicked in when we walked into the hotel and she realized there wasn’t a receptionist working. "
    ki "It’s the same thing that happened last year. Tell her to go take a fucking break or something."
    ka "It’s fine. I think I just work here now. It’s sad that I’ll have to quit my clubs, though. But alas."
    s "Question two: why are you holding only one key?"
    ima "Because I didn’t realize you were coming and we only have three rooms. Which means that floor one is in one room, floor two is in the other, and you and me are in the third."

    scene surprisebjcontest2
    with dissolve

    ki "I’d be happy to come stay with you guys as well if-"
    ima "Absolutely not. Go away. "

    scene surprisebjcontest3
    with dissolve

    ka "It’s best to let the adults just have their own room, Kirin. "
    ki "Yeah, best for {i}them.{/i} How come nobody ever cares about what {i}I{/i} want?"
    ka "Don’t worry. As the senior customer relations manager for this hotel, I’ve made sure that Sensei and Imani received a room with two beds."
    ka "I’ve also contacted the custodial staff for a privacy curtain so they will not have to look at each other at any point and we will all go home happy and chaste."
    ki "Talk about an oxymoron."
    ima "Any more questions, Senpai? Or are you ready to go be happy and chaste?"
    s "Talk about an oxymoron."

    scene surprisebjcontest4
    with dissolve

    ki "At least you understand me."
    s "I only have one more question. Does Ami know?"
    ima "She will if we hang around here any longer. Or if Kirin decides to run her mouth or something."
    s "Of course Kirin is going to run her mouth. That’s what she does."
    ki "Hey. I can do other stuff with my mouth too. Talking isn’t {i}all{/i} I’m good for."

    scene black
    with dissolve

    s "Okay, yeah. Let’s go. I feel like I might accidentally invite her if we stay here any longer and I don’t think you’d be into that."
    ima "Woo! Sleepover with Senpai! Sure hope he can’t make out the silhouette of my bodacious body through the privacy curtain!"
    s "I don’t think “bodacious” is the right adjective to-"
    ima "One more word and you’re sleeping on the floor. I don’t even care if there are two beds."

    "........."
    "......"
    "..."

    scene surprisebjcontest5
    with dissolve2

    s "Are you sure you’re okay with this?"
    ima "Why wouldn’t I be? You gonna try making a move on me in the middle of the night?"
    s "Beats me. You’ve slept at my house before and I was able to abstain then. Guess we’ll find out soon if a curtain is enough to keep these burnings passions of mine at bay."
    ima "So long as those burning passions don’t wreck the hotel room. I don’t want to risk Touka’s mom seeing that one of the security deposits wasn’t refunded."
    s "Yeah, because if there’s anything we know about Tsubasa, it’s that she’s extremely frugal with her money."
    ima "All I’m saying is that, A: you don’t get rich by wasting security deposits. And B: I like it gentle."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "We manage to make it to our room without anyone other than the Kandas seeing us, but it’s clear that most of the girls are still awake judging from the laughter and chatter bleeding through their doors."
    "I imagine that word will soon spread about my presence in this hotel and that Imani may potentially be assassinated before the night ends. "
    "So if I am going to have sex with her before she dies, I should probably hurry and get to that as soon as we step inside."
    "........."
    "......"
    "..."

    if saralust20 == True and haruka_lust >= 25 and sara_lust >= 25:
        jump harukalust25
    else:
        scene surprisebjcontest6
        with dissolve2

        ima "..."
        s "..."
        ima "Senpai."
        s "What?"

        scene surprisebjcontest7
        with fade

        ima "It appears that we’ve been assaulted by the cliche “one bed” trope."
        s "Assaulted? More like blessed."
        ima "Oh, look. Free slippers."
        s "There are more exciting things to be discussing than free slippers, Imani."
        ima "And a few major problems, too. Karin’s sure to be demoted for this."

        scene surprisebjcontest8
        with fade

        s "So...now what?"
        ima "Isn’t it the man who’s supposed to take charge at times like this? Come hither, vile fiend."
        s "Nice. Nothing gets me in the mood quite like archaic language."
        ima "Nothing gets {i}me{/i} in the mood quite like the feeling of somebody secretly watching my every move."
        s "I didn’t realize you were an exhibitionist."
        ima "Just wait until you see my sex tape. That’ll teach you more about me than any hotel banter ever could."
        a "Where can I find it?"

        scene surprisebjcontest9
        with dissolve

        ima "I’ve got it posted on my LinkedIn just in case I need it for professional reasons. Send me a contact request and I’ll forward it to you at my earliest convenience."
        ima "My rates are low and I’m always looking for work."
        s "How long have you been standing there?"

        scene surprisebjcontest10
        with dissolve

        a "Did you really think I was going to just let you and Imani sleep together? The reason I begged you to come to the hotel was so you could sleep with {i}me.{/i}"
        ima "That doesn’t sound very kosher."
        s "She means it in the wholesome way."
        ima "In {i}that{/i} costume? I ain’t buying it. I’ve seen more of Ami’s legs today than I thought I ever would. And Tsuneyo wasn’t lying when she said they’re great."

        scene surprisebjcontest11
        with dissolve

        a "{i}Miss Imai,{/i} would you please accompany me to the first floor girls’ hotel room? We’ve cleared out a spot on the floor for you to sleep."
        ima "Hah..."
        ima "Guess I’ll have to buy my own slippers after all."

        scene black
        with dissolve2

        "Ami escorts Imani away from what seemed like it was going to be a good opportunity for the two of us to finally “take the dive” before returning on her own several minutes later."
        "Unfortunately for her, the rest of the class united in the decision to keep {i}her{/i} out of my room shortly after that and, before I know it, {i}she{/i} is being escorted out of the room as well."
        "As such, I wind up getting dressed and climbing into bed alone."
        "But I dream of a future in which that didn’t happen."

        stop music

        "It’s a dream much happier than that of the night before."

        $ harukalust25skip = True
        $ imani_love += 1

        "{i}Imani’s affection has increased to [imani_love]!{/i}"
        "........."
        "......"
        "..."

        jump dormwartwo10

label harukalust25:
...
```

## Code that triggers this event

File: (install folder)\game\HarukaEvents.rpy

Code:
```python
...
scene harukaoutdoor25
        with dissolve

        h "I feel like I’m going to stop forgetting my ring as much when I leave the house now."
        h "There’s not really anyone I feel the need to appeal to like that anymore."
        h "Because, thanks to a certain close friend of mine, I now understand that there’s more than one way to dispel loneliness."
        h "That there are plenty of ways to feel full without being filled up."
        h "Because at the end of the day...what I already have should be enough for me."
        h "And that reaching for any more would just be greedy."
        s "..."
        h "..."
        s "Want to make out?"
        h "Nope."

        scene harukaoutdoor26
        with dissolve

        s "Wow. You really have turned over a new leaf."
        s "Back in the beginning, you’d just make out with me without even asking."
        h "Okay, first off, that only happened one time and I was extremely drunk."
        h "Second, I’m still kind of upset about it. So don’t joke like that."
        h "Third, do you even {i}want{/i} to make out with me? Or do you just feel weird that I forced you into a sentimental conversation when your biggest goal in life is to avoid those?"
        s "Yes and yes. "
        h "Well, too bad. Because a phone call I received yesterday has reminded me of just how long I am willing to wait."
        h "And no handsome man with a well-defined body and mysterious aura will change that."
        s "If only I was less mysterious."

        scene harukaoutdoor27
        with dissolve

        h "Yes. If only."

    "A moment of silence washes over the two of us as the streets finally begin to fill with people."
    "But seeing as we’ve already passed the points of our conversation that demand secrecy, I don’t see much of an issue with it."
    "To anyone who passes by, we probably just look like lovers."
    "Ironically enough, that’s the one thing we’ll never be."
    "Haruka’s heart belongs to someone else."

    if harukasex == True:
        "I’m just the man who took it."
    else:
        "And it’s not as if I’d take it anyway."

    scene harukaoutdoor25
    with dissolve

    h "Anyway..."
    h "I guess it’s about time we head back in. "
    h "All those people on the street will soon remember they need coffee in order to survive and then turn to me in desperation."
    s "You’re going to stay here?"

    scene harukaoutdoor28
    with dissolve

    h "I mean...yeah. That {i}is{/i} my job."
    s "I just figured you might want to go spend time with Maki or something since she’s already on her way to the bar."
    s "She hasn’t shown any weakness to {i}me{/i} yet, but I’m pretty sure that brave facade she’s putting on won’t last nearly as long as she wants it to."
    s "Having another friend around might be good for her."
    h "I..."
    h "I didn’t realize you cared so much about her."
    s "Who says {i}she’s{/i} the one I care about?"
    h "..."
    s "..."

    scene harukaoutdoor29
    with dissolve

    h "Ahh..."
    s "..."
    h "I’d have to call Molly in."
    h "Do you think she and Rin will be able to get along for the rest of the day? Or are they still on bad terms?"
    s "Beats me. There’s only one way to find out, isn’t there?"
    h "I guess so..."
    h "Here’s hoping I still have a cafe to return to tomorrow."

    scene black
    with dissolve2

    "I leave Haruka’s side and blend in with the crowd as I begin to ponder over what else I can possibly do today."
    "I toy with the idea of showing up to the bar as well, but..."
    "I think that whatever is going on there would probably be best left between the girls."
    "I don’t belong anywhere with that level of uninhibited emotion."
    "Where I do belong is amidst a sea of faceless others, each focusing solely on where the day will bring them."
    "Paying no mind to me."
    "So to anyone who passes by, ignore me."
    "I’ll figure out where to go on my own."
    "Just focus on yourself."
    "Find your own way home."

    $ renpy.end_replay()
    $ sadgirls4 = True
    $ haruka_love += 1

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "........."
    "......"
    "..."

    jump sadgirls5
...
```