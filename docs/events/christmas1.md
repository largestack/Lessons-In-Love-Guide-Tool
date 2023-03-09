# Snow-Covered Footprints
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas1&go=Go)


Part of event chain [Changing of Seasons](./hoorayanotherreset.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmas1
* Group: Main
* Triggered by label: hoorayanotherreset

## Event code
File: \game\script.rpy
Code:
```python
...
label christmas1:
    scene chap1done
    $ renpy.pause(7, hard=True)
    scene black
    with dissolve2
    scene chap2
    with dissolve2
    $ renpy.pause(7, hard=True)
    scene black
    with dissolve2
    $ renpy.pause(2, hard=True)

    "………"
    "……"
    "…"

    scene firstwinter1
    with dissolve2
    play music "shrinemaiden.mp3"

    "Maya was right about things restarting a little...different than normally this time."
    "Instead of being sent back in time or back in physical-location or whatever happened during my first trip into the ether (?), we just opened our eyes and saw snow."
    "The lack of anything dramatic happening made the fact that we still had our hands linked together relatively awkward for the both of us."
    "Which probably explains why Maya quickly yanked her hands away from me the second her eyes opened."
    "It seems she was right about things going smoothly this time."
    "Even if I haven’t seen anyone else in the streets on the way back from[school], I have a pretty positive outlook for what’s to come when we get home."
    "Oh."
    "Did I forget to mention?"
    "That “important matter” we needed to attend to after our reset was nothing more than Maya sleeping over at the house with Ami and Ayane."
    "And here I was thinking something interesting was going to happen."

    m "I knew it would be cold but I didn’t actually think it would snow right away."
    m "It normally takes at least a few days for that to happen."
    s "I guess it really {i}is{/i} good you came dressed for the occasion after all."
    s "Aren’t you cold in shorts, though?"

    scene firstwinter2
    with dissolve

    m "Not really."
    m "Neither the cold nor the heat bother me all that much."
    m "I do prefer things to be like this, though."
    m "Not having to put my hair into a ponytail saves me several seconds every morning."
    s "Or you could just not put your hair into a ponytail during the summer."
    m "My neck would get hot."
    s "But the heat doesn’t bother you all that much."
    m "Because I put my hair into a ponytail."
    m "You really don’t understand how girls work, do you?"
    s "I guess not."
    s "I really do wish you would have informed me about this beforehand, though. "
    s "I could have tried out one of those thicker T-shirts I bought at the mall the other day."

    scene firstwinter3
    with dissolve

    m "What color did you go with this time? Grey?"
    s "...Yes."
    m "Same as always then."
    m "I guess some things never change."

    "I want to say it’s some sort of huge revelation that the original Sensei also chose the color grey but, in all actuality, it’s probably only due to the fact that there was a sale on that particular color the day I was in the store."
    "Not like the selection had all that much to choose from to begin with, but-"
    "Well, I guess things like that don’t even matter."
    "I have nothing to gain from looking into the way the last person who used this body handled it."
    "They’re free to wear whatever color they want wherever they are now."
    "And I’ll continue to choose things that reflect how little I have to share with the world."

    m "Oh. We need to stop somewhere on the way back."
    s "What? Where? Why?"
    m "Convenience store."
    m "We need an excuse for why we’re showing up together at the same time."
    s "I didn’t even think of that."
    m "You never do."
    m "I’ve done this a few times now."
    s "I’m surprised even an excuse would make them feel normal about this."
    m "Do you feel out of place?"
    s "You mean walking back to my house in the middle of the night with you? Yeah, kind of."

    scene firstwinter4
    with dissolve

    m "But just think of all the cute girls waiting for you when you get home."
    s "There are only two cute girls waiting for me right now."
    m "Yes, but that’s two more than you deserve."
    s "Thanks, Maya."

    "She was right when she said some things never change."
    "But, strangely enough, that makes me all the more comfortable right now."
    "I recall a conversation we had in the past about how I would act if she randomly turned into a completely different person one day."
    "I’m glad to know that hasn’t happened."
    "And I hope it will continue to not happen."
    "For my sake-"
    "And hers, I guess."
    "Though, I guess it might be better for her in the long run to not have to endure something like this anymore."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "Maya and I stop at a convenience store close to my house that Ami and I visit in the morning sometimes."
    "We grab a few snacks and drinks and other assorted items to make it look like we came here on purpose and are not returning empty-handed."
    "Ami’s already suspicious of the relationship between Ayane and me, so having her be suspicious with Maya next would just be way too bothersome."
    "And Maya would probably vomit at even the slightest insinuation of something going on between the two of us."
    "………"
    "……"
    "…"
    "{i}A thousand snow-covered footprints later...{/i}"

    play sound "dooropen.mp3"

    s "I’m home."

    "I quickly kick my shoes off at the door and place all of the bags we brought back from the convenience store on the kitchen counter."

    scene firstwinter5
    with dissolve
    play music "normalday.mp3"

    "The sound of hurried footsteps follow as Ami and Ayane run up to me the second the door opens."
    "And Ami’s hair is...very long when it’s down."
    "Well, it’s very long when it’s in twintails as well. But {i}this{/i} is just intimidating."
    "Maybe I should take her to get a haircut soon?"

    a "Welcome home! I missed you!"
    ay "I missed you too, Sensei! I almost left when I found out you weren’t here, but that would have just been plain rude to Ami."
    a "Sensei, make sure you don’t look at Ayane at all tonight."

    if bonus == True:
        a "She keeps her hoodie zipped down so you’ll look at her chest. Isn’t that super perverted and not at all a desirable quality in a girl?"
        ay "Sensei. Quick. Look down here. Don’t let Ami’s words distract you from the true prize."
        m "Uhh...I’m here too, you know."
    else:
        m "That's right. Look at me instead."

    scene firstwinter6
    with dissolve

    a "Oh. Hi, Maya."
    m "…"
    m "What do you mean, “Hi, Maya?”"
    ay "It’s a greeting. You say that to people when you are...well, you know, greeting them."
    m "Why is his greeting so much better than mine?"
    s "I’m just more popular than you, I guess."

    scene firstwinter7
    with fade

    m "Well that just doesn’t make any sense at all."
    s "Don’t worry, Maya. I still like you."
    m "If Hell was real I’d tell you to go there right now."
    s "Since it’s not, are you going to come up with a better insult? Or are you just going to call me disgusting again?"
    m "I’m too tired to insult anyone right now. "
    m "Please excuse me while I go put my pajamas on."
    m "Must I say that several more times at a higher volume so you don’t enter the room and say something like, “Oh, I didn’t hear you?”"
    a "Don’t worry, Maya! We’ll keep him out here. You can go get changed."

    scene firstwinter8
    with dissolve

    m "Thank you."
    m "Now, please excuse me."

    scene firstwinter9
    with dissolve
    play sound "dooropen.mp3"

    "Maya storms past me and into Ami’s room, leaving me alone with two girls who are likely going to spend the rest of the night fighting over me."
    "My life really is difficult at times."

    scene firstwinter10
    with fade

    a "What’s her deal?"
    a "You didn’t do anything weird to her while you guys were out, did you?"
    s "To Maya? No. She’d erase me."

    "Probably."

    ay "I don’t think you did anything weird, Sensei. Maya just gets really angry and confused whenever anyone shows affection for you."
    s "No wonder she’s always so uptight. I like to think I’ve become pretty well liked over the last several months."
    ay "Last several {i}years{/i} in our cases. Ami and I like you more than anyone, I think. Ami being in second place, of course."

    scene firstwinter11
    with dissolve

    a "What were you guys even doing out there in the snow?"
    s "Are you really going to ignore what Ayane said just now? I thought that would set you off."
    a "Ayane? Is she here?"

    scene firstwinter12
    with dissolve

    ay "Hey! Being ignored hurts even worse than being insulted."
    s "I bumped into Maya at the convenience store and wound up being forced to carry all of the snacks she bought for you guys back here."
    s "And when I say {i}she{/i} bought them I mean she made {i}me{/i} buy them as payment for me inconveniencing her by crossing her path."

    "I find it slightly shocking how easy it is to make up a believable lie about where Maya and I were today- even if it was slightly rehearsed."

    s "So you’ve been here since[school] ended?"

    if bonus == True:
        a "School? What are you talking about? It's Christmas Eve and we're on winter break until Monday."
    else:
        a "College? What are you talking about? It's Christmas Eve and we're on winter break until Monday."

    a "And even if we weren't, it's still Saturday. How do you not know that?"

    scene firstwinter13
    with dissolve

    a "Wait?! Did they change the schedule?! When are we supposed to go back?!"
    a "Have you been going to[school] this whole time and not telling me about it?! Is this a test?!"
    a "What’s going on?!"

    "That’s...strange."
    "I’ve never had to deal with winter break before on account of winter...not even being a thing until right now."
    "Were we really supposed to start here? Or was this some sort of accident?"

    s "I’m sure the schedule hasn’t changed. Just feeling a little out of it right now."
    ay "Is it from the cold? Do you need me to warm you up?"
    ay "Come, Sensei! I’ll warm the bath for you!"
    s "I can warm the bath myself, thanks."

    scene firstwinter14
    with dissolve

    ay "Boo..."
    a "Maybe you should head to sleep early if you’re not feeling good?"
    a "We were probably just gonna stay up and watch movies or something anyway."
    s "Yeah, maybe."

    "I do feel extremely tired, but I imagine that has less to do with the after-effects of time travel and more to do with walking several miles through snow in my normal T-shirt instead of the thicker one."
    "I feel like Winter will be enjoyable in the long run, though. I’d much rather deal with walking through the snow than dodging rays of sun for days at a time."

    a "Besides, we need to start preparing for the party early tomorrow morning and you’ll probably complain if you don’t get enough rest."
    a "Actually, you’ll probably complain no matter what. But at least Makoto is handling the hotel and stuff."

    "Just before I decide to go to sleep, I’m hit with an abundance of strange information."

    s "So, Makoto is okay now?"

    scene firstwinter15
    with dissolve

    a "Was she...ever {i}not{/i} okay?"
    ay "She’s seemed pretty normal to me lately. But I guess Sensei knows her a little better than either of us do."
    s "She hasn’t seemed different to either of you lately?"
    a "Different? No. Strict and annoying? Yes."
    s "Huh..."

    "Did changing where we are in time somehow...{i}fix{/i} Makoto?"
    "That’s good, I guess, but..."
    "I feel like now I won’t ever figure out why she got all weird in the first place."
    "I’ll have to talk to her at the-"

    s "...Party."
    ay "Hm? What about the party?"
    s "Would you mind explaining to me what this party is about again?..."

    scene firstwinter16
    with dissolve

    ay "Oh! Let me!"
    ay "Since the beach trip was such a success and the Halloween party was pretty awesome as well, we’re going to throw a class Christmas party!"
    ay "Like Ami said before, we’re going to have it in a hotel and everyone has already confirmed that they’re coming."
    ay "Even Yumi is going to be there, so it’s already a pretty big deal."
    s "And when you say {i}everyone{/i} does that include Molly and Tsuneyo?"

    scene firstwinter17
    with dissolve

    "I go out on a limb and try to find out even more about what’s going on in this version of Kumon-mi, potentially exposing myself in the process."
    "If this is a timeline where those two haven’t joined our class, I’ll probably just sound like a perverted teacher who has his eye on students from other classes."
    "But at this point, I don’t think something like that would even make these girls think any less of me."

    a "…"
    ay "…"
    s "…"
    a "Well, I know those two are weird but...I can’t see any reason why they wouldn’t come to the party if they’re part of the class."

    "Good..."
    "The idea of them not being around was weighing on me more than I ever expected it to."

    if bonus == True:
        "But I guess even someone like me can succumb to the emotions of [teenage]girls when they break down in my arms about how much they don’t want to leave me."
    else:
        "The idea of them not being around makes me really sad since I wouldn't be able to keep track of their education anymore."

    s "So, just to recap..."
    s "Makoto is fine, Molly and Tsuneyo are still my students, and we are having a Christmas party in a hotel room."
    a "Uhh...yes?"
    a "Why are you being so weird about it?"
    s "Is there anything else I need to know?"

    scene firstwinter18
    with dissolve

    a "Uhh..."
    ay "..."

    scene firstwinter17
    with dissolve

    a "I...love you?"
    ay "I love you as well. It would be good for you to know that."
    s "I meant anything regarding our immediate future..."
    a "Uhh..."

    if ayanelust10 == False:
        scene firstwinter19
        with dissolve

        a "Oh! Kirin is coming to the party as well."
        a "But other than that, I don’t think there’s anything important you need to know."

    else:
        scene firstwinter20
        with dissolve

        a "Oh! Kirin is coming to the party as well."
        a "But other than that, I don’t think there’s anything important you need to know."
        ay "…"

        "That...might be uncomfortable for some people."

    s "Got it. Thanks for letting me know."

    scene black
    with dissolve2

    "A Christmas party, huh?"
    "Can’t say I didn’t see something like that coming sooner or later."
    "Did I expect it to be the first thing that happened to me after winter’s long-awaited arrival? "
    "Nope. Not one bit."
    "But, in true Sensei-fashion, I’m not going to complain about seeing all of my students together in one place."
    "I’m sure that whatever comes next will be a good start to this brand new cycle in a life I never dreamed I’d have."

    "{i}Congratulations on making it to the second chapter of Lessons in Love!{/i}"
    "{i}The following events are part of a special event chain and will play from start to finish in succession.{/i}"
    "{i}You will not have free-time to use during this chain.{/i}"
    "{i}Once it is complete, you’ll be free to act as you please once more and-{/i}"
    "{i}Since it’s officially Winter, expect a few changes around the city!{/i}"
    "{i}That’s all for now...but have a Merry Christmas or Happy Hannukah or whatever other holiday you celebrate!{/i}"
    "{i}Cherish your loved ones, for you never know when something horrible may happen to them!{/i}"
    "…"
    "{i}Roughly thirty minutes later...{/i}"

    scene firstwinter21
    with dissolve2

    s "…"
    ay "Mm...Sen...sei..."
    a "…"
    s "Weren’t they planning on watching movies all night?"
    s "And where is Maya?"
    s "She went to get changed like forty-five minutes-"

    play sound "dooropen.mp3"
    scene firstwinter22
    with dissolve

    m "Sorry. I passed out as soon as I got dressed and-"

    scene firstwinter23
    with fade

    m "…"
    s "…"
    m "What are you doing?"
    s "Oh, you know. Just hanging out."
    m "Did you drug them?"
    s "Do you think I’d need to?..."
    m "Unfortunately not. But that doesn’t make this any less weird for me."
    m "I can’t fall back asleep so soon after taking a nap. What am I supposed to do now?"
    s "…"
    s "Want to hang out?"
    m "…"
    s "…"
    m "I’m suddenly feeling very tired again."
    m "Goodnight."

    play sound "dooropen.mp3"
    scene firstwinter24
    with dissolve

    "Yup."
    "Can’t say I didn’t see that coming."

    scene black
    with dissolve2

    "I sit around for a few minutes longer before my leg and my arm fall asleep and I am forced to push the girls off of me."
    "Neither of them wake up, so I carry them back to Ami’s bedroom and haphazardly toss both of them onto the bed, hoping that doing so doesn’t wake Maya up."
    "Miraculously, it manages not to."
    "Even more miraculously, neither Ami nor Ayane wake up as well."
    "And before I know it, all three of them are passed out on the bed together in true [teenage]girl sleepover fashion."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve
    stop music fadeout 10.0

    "I walk into the bedroom, ready to call it a night after an {i}extremely{/i} eventful day."
    "But, surprisingly enough, nothing bad happened."
    "And even though I spent most of the day with Maya, my head only hurts a little bit."
    "I guess things are looking up after all."

    scene black
    with dissolve2

    "But it’s only a matter of time before they get worse again."
    "That’s just how life is."
    "So I guess I’ll try to submerge myself in happy thoughts for the time being."
    "And pretend that everything horrible is stuck somewhere deep underneath the ground."

    $ renpy.end_replay()
    $ christmas1 = True

    "………"
    "……"
    "…"

label christmas2:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
s "Messy? What do you mean by {i}messy?{/i}"
    m "I told you the first time, didn’t I?"
    m "That sometimes, things go wrong when I try to do this."
    m "Ushering in a change in temperature, which basically equates to a change in the world itself, sometimes mixes with all of the other things that need to be reset and causes a hiccup in the process."
    m "It’s incredibly inconvenient and I’m pretty sure it’s directly tied to both my mental state and how willing {i}God{/i} is to listen."
    s "I am suddenly significantly more worried about this."

    scene secondreset17
    with dissolve

    m "Rest assured, I am of sound body and mind right now and foresee this particular reset going smoothly."
    m "In fact, I am so sure of this reset’s success that I have dressed for the occasion and am ready for snow immediately upon completion."
    s "That’s good at least. "
    s "Waiting at that bistro for Ami and me to show up after[school] would probably be annoying without your current get-up."

    scene secondreset7
    with dissolve

    m "Oh, about that."
    m "That’s probably not going to happen this time."
    s "What?"
    m "We have somewhere else we need to be when we’re done here."
    s "How do we already have plans for the future?"
    m "Because the future is also the past. Or something."
    s "This world makes no sense at all."
    m "Nothing makes sense- but here we are. Alone at the end of the world."
    m "The same as always."
    m "Now, close your eyes."

    scene black
    with dissolve2

    s "Are you going to hug me again?"
    m "Reluctantly."

    "Maya takes a step toward me and stops inches away."
    "The sound of her breathing is drowned out by the vacuum of space, but I can feel her eyes on me."
    "It makes me uncomfortable and my posture may or may not be reflecting that right now."
    "I obviously can’t see anything with my eyes closed."

    m "Actually..."
    m "Let’s try this."
    m "Give me your hands."
    s "My hands?"

    scene secondreset18
    with dissolve2

    "Maya’s fingers curl around mine, which I’m sure is a lot easier on her than actually wrapping her arms around me."
    "This way, she’s able to keep her body from pressing up against mine and can continue pretending that I’m actually heartless instead of accidentally hearing the beating of said muscle in my chest."

    m "You are annoyingly tall."
    s "You are obnoxiously short."

    if bonus == True:
        m "I’m only slightly shorter than I’m supposed to be at my age."
        m "Your height surpasses that of the average Japanese adult male by at least five inches."
        s "Do we need to be closer than this after all? Should I lift you up?"
        m "Try to lift me and I will reset the world by myself."
        s "But then how will I make it to whatever place we’re supposed to go to after this?"
        m "I will go alone. It would be easier that way anyway."
        s "Well thank you for going out of your way for me."
        m "And thank you in advance for not lifting me up."
    else:
        m "We should kiss."
        s "Ew, stop."
        m "Oh my fucking god this is so annoying."
        m "Brb, reset time."

    scene secondreset19
    with dissolve

    m "…"

    "My eyes are still closed, so I can’t tell what Maya is doing."
    "But something about the way her hands begin to hold onto mine a little tighter tells me that-"

    play sound "static.mp3"
    stop music
    scene happy1 with flash
    scene helpme with flash
    scene happy2 with flash
    scene helpme with flash
    scene happy3 with flash
    scene helpme with flash
    scene happy4 with flash
    scene helpme with flash
    scene happy5 with flash
    scene helpme with flash
    scene happy6 with flash
    scene helpme with flash
    scene happy7 with flash
    scene helpme with flash
    scene happy8 with flash
    scene helpme with flash
    scene happy9 with flash
    stop sound
    $ renpy.end_replay()
    $ hoorayanotherreset = True
    jump christmas1
...
```