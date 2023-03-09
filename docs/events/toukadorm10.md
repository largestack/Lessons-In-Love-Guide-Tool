# House Call
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukadorm10&go=Go)



## Event preconditions
✅Touka love greater than or equal to 10

✅Day of week is not Thursday

❌Event "[Main: Glued to the Sky](./christmastwo20.md)" is completed (event=christmastwo20)



## Next events
* [Touka: A Commoner's Tour of Summer](./toukaspecial15.md)

## Event properties
* ID: toukadorm10
* Group: Touka
* Triggered by label: toukadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukadorm10:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on Touka’s door and wait for her to answer. "
    "Immediately upon knocking, however, I am graced by the suspicious sound of laughter."
    "Now, laughter on its own isn’t really something I’d ever call suspicious."
    "But I want to remind you exactly where I am right now, and exactly who it is that resides behind this door."
    "Could it be that Touka and Yasu’s friendship has finally reached a point where they both understand {i}and{/i} leisurely banter with one another?"
    "Is Yasu even capable of such a thing?"
    "Or...is this occasion truly a suspicious one after all?"

    s "..."

    "Seeing as there is no answer, I take it upon myself to enter anyway as this is a matter I must investigate to ensure the safety of both my students and myself."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I’m sure I’m probably just overcomplicating things by thinking something is afoot here, but that sort of thing happens all the time when I’m standing outside of doors."
    "It’s just a habit, I guess- envisioning what’s on the other side."
    "What could go wrong."
    "What could go right."

    scene toukahair1
    with dissolve2

    "But, on most occasions, definitely wrong."

    tb "Oh my. Could it be that you’ve wandered into the incorrect room, Sensei?"
    to "Yes. {i}Could it be that you’ve wandered into the incorrect room, Sensei?{/i}"
    ya "Touka, that hurts."
    to "Shut up and deal with the pain, Yasu. It wouldn’t hurt so much if you would actually brush your hair every once in a while. "
    ya "Okay, Touka. I will do as you say as long as it means I can have beautiful hair like yours one day."
    to "I suppose there is no harm in dreaming. "
    s "Hey, Tsubasa. I didn’t realize you were going to be here."
    tb "The same goes for me. I didn’t believe you were even permitted to enter the girls’ dormitories. But I suppose I’m not very well acquainted with the rules of public schools, so I’m likely wrong."
    s "To be fair, I’m not very well versed in them either and I work for one."

    scene toukahair2
    with dissolve

    to "W-What Sensei means to say is that he’s been coming on occasion to...assist with my studies! "
    tb "Does this have something to do with his inquiry about your bed at the Christmas gathering?"
    to "I’m sure it-"

    scene toukahair3
    with dissolve

    to "Wait, you asked my mother about the bed?! Why?!"
    to "I already informed you that it’s a standard bed with rapid sleep capabilities! What else do you need to know?!"
    tb "I advised him of the same. But now, I’m suddenly intrigued by his need to come all the way over here to aid with your studies. "
    tb "Which subjects is Touka struggling with, exactly?"
    s "Uhh..."

    menu:
        "Physical Education":
            s "She’s been really struggling when it comes to gym class. She just can’t seem to keep up with the other girls."

            scene toukahair4
            with dissolve

            to "Okay, {i}that{/i} is entirely untrue! I would never struggle keeping up with any of the girls in our class!"
            to "Save the small one with the auburn hair, but I’m beginning to believe she may have been raised by wolves. She moves far too quickly for a [young]girl."

            "Is {i}that{/i} why Miku never brings up her past?"
            "Also, this entire scenario is untrue and I don’t know why this particular addition to it is what’s setting Touka off."

            tb "You are...tutoring my daughter in physical education?"
            s "I am."
            to "You’re not! Tell her it’s for...English!"
            s "I am here to teach your daughter about physical education and biology."

            scene toukahair5
            with dissolve

            to "Ugh. Why do I even bother?"
            tb "I was unaware she was struggling. Touka has always seemed very athletic to me, but I suppose I haven’t paid much attention to those outside of our bubble. "
            tb "Is that really something you can tutor her in {i}here,{/i} though? You don’t require some sort of...gymnasium?"

        "Economics":
            s "Touka doesn’t seem to grasp the basic concepts of economics- likely due to her inexposure to the middle class or the true value of money."

            scene toukahair4
            with dissolve

            to "Wha- no! That’s not true at all!"
            to "Even if I lack the same sort of {i}exposure{/i} as the other girls, I completely understand and appreciate the value of money! Probably even more than most!"
            to "As the heir to the Tsukioka family business, it is absolutely essential that I understand something as {i}basic{/i} as economics."
            s "You bought a one million yen painting for Makoto on Christmas."

            scene toukahair6
            with dissolve

            tb "That’s it? I told you it was okay to spend a little more."
            to "Did I go under budget? I will admit that seeing the limit written in USD did confuse me a bit, so I apologize if that is what happened."
            to "In my defense, however, conversion rates are not exactly reliable or even relevant at the moment due to Kumon-mi’s isolation from the rest of the world."
            s "You weren’t under budget. You spent more on that present than Makoto has probably ever even seen before."
            to "Oh."
            to "Well, how is that bad?"
            s "It’s bad because it just shows how little you know about money. "
            tb "Darling, I had no idea this was such an issue for you. Perhaps we should ask your father to hold off on transitioning until you’re more comfortable with-"

        "Animal Husbandry":
            s "Touka has been having a really tough time with our animal husbandry course."

            scene toukahair6
            with dissolve

            tb "Is that true, dear?"
            tb "You’ve always been so good with the horses. I assumed animal husbandry would be a walk in the park for you."
            to "I...was unaware we even had an animal husbandry course."
            s "See what I mean? This is how far behind she is."

            scene toukahair7
            with dissolve

            tb "Well, that won’t do at all. Everyone knows how important and essential animal husbandry is to the average, everyday Japanese citizen."
            s "Yup. That is definitely a thing everyone knows."
            s "But, you know- if Touka would just stop strangling all of the kittens we bring in for educational purposes, I wouldn’t have to go out of my way and come here to teach her more about proper husbandry."

            scene toukahair8
            with dissolve

            tb "Touka! You’ve been strangling defenseless kittens?!"
            to "Absolutely not! And, just as I assumed, we don’t have an animal husbandry class at all!"
            to "Probably!"
            to "At the very least, there have not been any kittens!"

            scene toukahair9
            with dissolve

            tb "Oh dear. Then who is it that’s been strangling them? "
            tb "We have to find out before it’s too late."
            tb "But I suppose I shouldn’t get in the way of your husbandry class so Touka can be prepare for when-"

    scene toukahair10
    with dissolve

    to "Mother, no. He is here to tutor me in English."
    to "{i}Like he always does at this time on this specific day of the week.{/i}"
    ya "I have never seen Sensei-"
    to "{i}Like he always does at this time on this specific day of the week.{/i}"
    ya "..."
    tb "Touka, you know I’m fluent in English, don’t you. Why haven’t you asked me for assistance?"
    tb "The entire kitchen staff can speak it as well. It’s becoming an essential language."
    to "The kitchen staff changes monthly, mother. They are not a reliable source of information."
    tb "Yes, I agree. I don’t know where your sister picked up that hobby, but your father really needs to do something about it."

    scene toukahair11
    with dissolve

    to "R-Regardless! Sensei is {i}definitely{/i} here to teach me, seeing as there is no other reason for him to ever come to this room!"
    tb "Well, let me say now that I admire his dedication."
    tb "It takes a special type of person to do something like this out of the kindness of his heart."
    s "What can I say? I’m a pretty great guy."
    tb "And here I was beginning to think that you hadn’t been taking my daughter’s education seriously."
    to "Oh, {i}what a shame that would be.{/i}"

    scene black
    with dissolve2

    "Touka finishes messing around with Yasu’s hair and sends her back over to her side of the room, where she takes a seat and begins staring at the wall in typical Yasu fashion."
    "Tsubasa proceeds to down the rest of her wine in one gulp without so much as batting an eye- a skill I believe she may have acquired after years of dealing with her youngest daughter."
    "She then gestures for me to take a seat on the completely normal bed between her and Touka- who suddenly appears very exhausted for some unknown reason that definitely doesn’t have to do with me."

    scene toukahair12
    with dissolve2

    to "Hah..."
    tb "Oh, darling. Needing a little extra help when it comes to your education is nothing to be ashamed about."
    tb "Just blame it on your upbringing. It is both accurate {i}and{/i} a reasonable excuse when it comes to explaining your perceived inadequacies."
    to "I am not ashamed, Mother. I just wish I had {i}remembered my lessons were going to be tonight{/i}."
    to "Because not only does this interrupt the rare chance for the two of us to spend time together, I look...entirely unprepared to learn."

    scene toukahair13
    with dissolve

    tb "Oh my- you’re right. How incredibly informal of us."
    tb "If I had known you were going to come tonight, I would have postponed our monthly slumber party."
    s "And if I had known this was something you two had been planning, I would have rescheduled Touka’s totally-legitimate English tutoring session."
    to "My, what a lovely offer. I do suppose we’ll take you up on that. Right now."
    tb "Oh, don’t be silly, Touka. As much as I care about our relationship, I also care about you becoming the best person you can be."
    tb "And that person just happens to be fluent in English the same way her mother is."

    scene toukahair14
    with dissolve

    to "Hah..."
    s "..."

    "Touka shoots me a glance that I can immediately tell means that I’m going to owe her a favor in the future, but I guess that’s fine."
    "I’m sure that a large part of why she’s helping disguise one of my many casual visits to her dorm room is to just make {i}herself{/i} look good-"
    "But, as a self-centered man who is also made to look good in the process, I can’t help but thank her for that."
    "Being indebted to someone isn’t exactly a thing I like, though."
    "So if I can prevent having her attempt to cash in her hook on me before she has an actual opportunity to, I probably should."

    s "We can have our totally legitimate tutoring session another time, Touka. It’s fine."

    scene toukahair15
    with dissolve

    to "Pardon my asking, but...what exactly is the catch?"
    s "No catch. Just don’t want to get in the way of something that’s important to you."
    to "Okay, but..."
    to "What is the catch?"
    s "Am I not allowed to do nice things?"
    to "Not really, no. Or at least you don’t seem to possess the capability to actually enact any without something in return."
    tb "Touka, that is no way to speak to your teacher."
    to "Apologies, Mother."

    scene toukahair16
    with dissolve

    tb "Thank you very much for offering to do that, Sensei. My daughter and I don’t get to spend as much time together as either one of us would like."
    tb "Well, {i}this{/i} daughter. My other daughter and I spend almost {i}too{/i} much time together. But she is a...special case."
    s "Why not spend more than one night per month together if that’s the case? I can’t imagine that’s really enough."
    s "Especially with Yasu...existing."
    tb "I quite like Touka’s roommate actually. Her reaction to seeing the manor for the first time was adorable."

    scene toukahair17
    with dissolve

    s "Why has Yasu gotten to see your house but I haven’t?"
    to "Because I don’t believe you’d be able to conduct yourself appropriately if you were to come."
    s "..."
    s "But you think Yasu-"
    to "I said what I said, Sensei."
    to "The fact of the matter is, Mother and I {i}can’t{/i} spend more time together. We’re far too busy for that sort of thing."
    s "Are you? Because all you have is school and Tsubasa has been just...I don’t know. Watching your sister, maybe?"

    scene toukahair18
    with dissolve

    tb "Oh, I do much more than that."
    tb "I spend most of my time overseeing the Tsukioka Foundation's hospitality and real estate branches."
    tb "I’m sure it sounds boring to you, but I’m actually quite good at it."
    s "I don’t think I’ll ever understand how your family transitioned from bubble wrap to basically owning the city."
    tb "Yes, well...the last few years have certainly been very kind to us."
    to "When I was younger, Mother and I had much more time to spend together. But with the family becoming a more prominent figure in the city, it’s just not possible anymore."

    scene toukahair19
    with dissolve

    tb "Ahh, how lovely it would be to go back, though."
    tb "All of those summers spent at our vacation homes...the laughs we shared...the joyous ruckus caused by an expensive band of animatronic animals..."
    s "..."
    s "The what?"
    to "Maybe this summer will be a little different, though?"
    to "Perhaps the small break in the school year would give me the time to see how you handle your end of the family business, Mother?"

    "If there {i}is{/i} a break, that is."
    "If I remember correctly, there was a small one for Christmas just before our first party...but I have no idea how summer vacation works or...if that’s even a thing we get."

    scene toukahair20
    with dissolve

    tb "I think that sounds wonderful, dear. But don’t you think your time might be better used experiencing a {i}real{/i} summer vacation for the first time?"
    tb "You finally have the opportunity to do so- and it’s one that neither your father nor myself ever had. I wouldn’t risk losing that if I were in your position."

    scene toukahair21
    with dissolve

    to "But...I don’t really understand what that entails."
    to "I have a hard enough time following what it is the common folk do during normal parts of the year. The idea of a vacation with them is just...not one that I think I’m fully prepared for yet."
    s "I mean, you did go on the beach trip with everyone recently. Just think of it like that except...the right weather."
    tb "If you don’t understand how it works, just {i}ask{/i}, dear. There’s no harm in that."
    tb "I’m sure your teacher would love to show you how everyone else spends their summer vacations."

    scene toukahair22
    with dissolve

    s "I would?"
    to "Is that...something you’d actually consider, Sensei?"
    to "You {i}have{/i} shown me the ropes of other aspects of the outside world- as frayed as they may have been."
    to "If you’d be willing to show me how a standard, commoner summer would look like as well...I’d consider myself greatly indebted to you."

    scene toukahair23
    with dissolve

    s "Well, that {i}does{/i} sound a lot better than me being indebted to you."
    s "It would just probably make a little more sense to ask one of your other-"
    to "I’m going to stop you right there in order to save both my heart and my pride, Sensei."
    s "Good call. Wouldn’t want your mother knowing you don’t have any-"
    to "Again, I am going to stop you right there."
    tb "Don’t have any what, Touka? Is it something we can provide you?"
    to "Sadly, no. It is not, Mother."

    scene black
    with dissolve2

    if bonus == True:
        "Sensing that it’s time for me to leave, I get off the bed only to be followed up by the Tsukiokas who, when combined, surpass everyone else on this floor put together in terms of breast volume."
    else:
        "Sensing that it’s time for me to leave, I get off the bed only to be followed up by the Tsukiokas who, when combined, surpass everyone else on this floor in terms of awesomeness and hugability."

    "Does that have anything to do with the matter at hand? No."
    "But when the two of them stand next to one another, it’s something I can’t help but notice and appreciate."

    scene toukahair24
    with dissolve2

    if bonus == True:
        "You know, on closer inspection, I think they might win out the combined-floor {i}ass{/i} category as well."
        "This family is rich in far too many ways."
    else:
        "Wow they are so cool."

    tb "Thank you again for allowing Touka and I to spend the rest of the night together. We truly do appreciate it."
    tb "It’s a shame about your lesson, but I’m sure the two of you will make up for it soon enough."
    tb "Especially with you agreeing to teach her about middle class summers and all."
    s "Did I agree to that yet? Because I still don’t really think I’m the right person to-"
    tb "Oh, nonsense. I’m sure you’ll do perfectly fine. Perhaps you can make a field trip out of it?"
    s "Right. Because nothing says {i}vacation{/i} like a planned, school-funded educational trip."
    tb "I wouldn’t mind funding it if money is the issue, of course."
    s "Not really what I was getting at."
    to "Things have been a bit warmer as of late, Sensei. Perhaps you can show me a few things the next time we meet up outside?"
    s "Oh, I’ll show you some things alright."
    to "Splendid. Thank you so much."
    tb "What a generous man you are, going to such lengths for my daughter."

    if bonus == True:
        s "I’m pretty good at all things involving length, so to speak."
    else:
        s "Anything for her education."

    scene toukahair25
    with dissolve

    tb "We {i}are{/i} still talking about education, yes?"

    if bonus == False:
        s "That is what I just said, yes."

    to "Mother! Ew! Don’t say things like that while winking at my teacher!"
    to "In fact, don’t wink at him to begin with! It is strange and unpleasant!"

    scene toukahair26
    with dissolve

    tb "Touka, dear. If there’s anything you need in order to make the most of your summer vacation training course, don’t hesitate to let me know."
    to "I won’t, but...I think it’s less of a training course and more of an...orientation?"
    s "I don’t think I’d call it either of those two things."

    "Especially when I still have no idea what I can even show Touka when her biggest summer memories involve an...animatronic animal band?"

    scene toukahair27
    with dissolve

    tb "I suppose we’ll be seeing you around, then? If there won’t be any lecturing done tonight, we should probably be getting back to Yasu’s hair."
    tb "It is...quite unkempt."
    s "Sure. But if she converts either one of you two, I don’t know how much time I’ll be able to spend with you anymore."
    to "Oh, don’t worry about that. I’ve taught my mother the “boop” technique and we’ve come up with a rule where we poke Yasu every time she begins to rant."
    tb "I’m very excited to try this on my youngest daughter as well. Though I can’t imagine it being nearly as effective."
    s "Well, have fun poking Yasu and being related or something. I’ll get out of your way now."
    to "Thank you again for postponing our totally legitimate English lesson, Sensei. It was a very nice thing to-"
    tb "You know I don’t actually buy that. Right, dear?"
    to "..."
    s "..."
    to "{i}Run.{/i}"

    scene black
    with dissolve2

    "I quickly exit Touka’s bedroom and force myself back into the state of mind where Tsubasa doesn’t believe I just show up to her daughter’s room for no reason whatsoever."
    "That aside, though, I’ll have to start thinking about summer-related activities to teach Touka about soon."
    "That might sound easy to you, but I’d like to use this opportunity to remind you that I only visit a select few locations every week- and I’m sure she’s already seen at least most of them."
    "Either way, I should be thankful that unknowingly interrupting another rare mother-daughter get together did not end in tragedy or suspicion."
    "At least...not any suspicion that was outwardly revealed to me."
    "I have no idea what Tsubasa will choose to believe in her own mind, but..."
    "I guess I can wishfully think it works out in my favor."
    "Especially since that’s all I ever really do anyway."

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukadorm10 = True
    stop music fadeout 5.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label toukaspecial15:
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
    if touka_love >= 10 and day != 4 and christmastwo20 == True and toukadorm10 == False:
        jump toukadorm10
...
```