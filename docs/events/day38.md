# Walk in the Park
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day38&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 38

✅Event "[Makoto: Unexpected Profession](./firsttimepornshop.md)" is completed (event=firsttimepornshop)

✅Event "[Main: Cleaning Duty](./day36.md)" is completed (event=day36)



## Next events
* [Main: This Town Has Two Halves](./day44.md)
* [Makoto: Rising of the Tide](./pornshop10.md)

## Event properties
* ID: day38
* Group: Main
* Triggered by label: saturdayafternoon
* Triggered by branch label: saturdayafternoon

## Event code
File: \game\script.rpy
Code:
```python
...
label day38:
    scene newwalk1
    with dissolve2
    play music "justbehappy.mp3"

    "I decide to stop by the park on my way home in hope of bumping into a mysterious and flirty transfer student, but wind up bumping into Makoto instead."
    "And all before I even had the chance to get my mandatory afternoon inner monologue started..."

    mak "Huh?...Sensei? What are you doing here?"

    "As you can see, she is just as surprised as I am."

    s "I was about to ask you the same question. You interrupted my fated meeting with a mysterious transfer student."
    mak "But...we don’t have any transfer students. I just checked the register yesterday."
    s "Why? Are you really so obsessed with school that you need to read over a list of all your classmates just to stay occupied?"

    scene newwalk2
    with dissolve

    mak "{i}No...{/i}I was just curious about whether or not you've been correctly marking down everyone's absences. Which you haven't."
    s "You really need more friends."

    scene newwalk3
    with dissolve

    mak "I have a perfectly adequate amount of friends, thank you very much!"
    mak "Now, what's all this about a mysterious transfer student?! What do you know that I don't?!"
    s "There is no actual transfer student. I was just daydreaming about the chances of running into a cute girl."
    s "Thankfully, I appear to have encountered one that I don't even need to bother going through introductions with."

    scene newwalk4
    with dissolve

    mak "Ah..."
    mak "D...d..."
    s "D...?"

    scene newwalk5
    with dissolve

    mak "D...Don't just go from insulting me to complimenting me that quickly! It makes it hard to think!"
    s "Anyway, I’m really just here to kill some time. But what about you? I figured you'd have work today."

    scene newwalk6
    with dissolve

    mak "I do have work today, we’re just not open yet."
    mak "We've tried opening earlier in the past, but we have been historically dead during regular business hours, so it's really not worth the effort."

    if bonus == True:
        s "That makes sense. Sunsets are nice and whatnot, but looking at them doesn't really make you want to masturbate."
    else:
        s "Right. No one watches movies during the day. Movies are a night time activity."

    scene newwalk7
    with dissolve

    mak "Why must you ruin every conversation almost immediately?"
    s "Because if I didn't, you'd probably keep talking about porn shop data or something. And that just sounds boring."
    mak "Well, forgive me for taking an interest in statistics. Would it make you happier if I spent more of my time actively {i}consuming{/i} the material we sell?"
    s "It-"
    mak "Please don't actually answer that question."
    s "Damn it."

    scene newwalk8
    with dissolve

    mak "Oh, umm...While I'm already on the topic of asking for forgiveness..."
    mak "I'd like to apologize for my outburst in the classroom the other day."
    mak "I realize that it was completely out of character for me to...even consider that you'd be willing to spend your free time outside of school with me, so..."
    mak "I won’t hold it against you if you want to just...forget everything I said or pretend it never happened."
    s "Why would I do that? In fact, doesn't the fact that I'm talking to you right now kind of prove that I {i}do{/i} want to spend time with you outside of school?"
    mak "Not if it's...based entirely on coincidence and not something we proactively planned on doing."
    s "Well, if you don't have anything else to do, how about we {i}proactively plan{/i} to hang out until you have to leave for work?"
    s "Unless you were on your way to study right now or something. Which you probably were because you are Makoto and that is what you do."

    scene newwalk9
    with dissolve

    mak "I'll {i}actually{/i} have you know that I have banned myself from studying today."
    mak "Instead, I've been trying to enjoy myself by taking a relaxing walk in the park."
    mak "It’s actually kind of nice. The weather here has been perfect lately, hasn't it?"
    mak "I can't even remember the last time it rained."
    s "Wait...yeah. Why hasn't it rained yet?"

    "I know month-long periods without rain aren't impossible, but it's been bright and sunny every single day since I woke up here."
    "That...has to lead to some sort of environmental problems eventually, doesn't it?"

    mak "Who knows? Perhaps we're just in the early stages of a drought?"
    mak "For now, though...would you...you know..."

    scene newwalk10
    with dissolve

    mak "Actually...nevermind. It's a lot more embarrassing asking out loud than I thought it would be?"
    s "Really? Even after I suggested doing exactly what you were about to suggest like two minutes ago?"

    scene newwalk11
    with dissolve

    mak "So...So you do want to go for a walk with me! Well...thank you very much for asking, Sensei! I would love to!"

    scene black
    with dissolve2

    "You know, with how much Makoto obviously likes me, I figured she'd be getting flustered a lot more frequently than she actually does."
    "Granted, she's still near the top of the chart when it comes to that incredibly specific demographic-"
    "But the fact that she's able to keep herself composed at all is sort of a testament to how...composed and diligent she is as a person."
    "It's those traits of hers that make the points in time where she {i}does{/i} get flustered all the more appealing, though."
    "I know I give her shit about how much time she spends studying and, honestly, I can't imagine ever stopping that with how fun it's been so far."
    "But-"
    "I do think she's interesting."
    "And not just because I am going to have sex with her one day."

    scene makpark1
    with dissolve2

    mak "Heheh...this feels kind of weird, doesn't it?"
    s "You think so? It feels pretty normal to me."
    mak "But...this isn't like the hall at school. You and I have never actually spent time together like this before."
    mak "Also...there's the whole issue of you being a teacher...and me being a student..."
    mak "And we're walking around a public park, no less. Anyone who sees us likely thinks this is some sort of...date."
    mak "It's like something straight out of a shoujo manga- a genre of book I absolutely do not read."
    s "What is-"

    scene makpark1r
    with dissolve

    mo "Uh-oh! Looks like it's time for a weebnote!"
    mo "Shoujo manga is a genre of comics aimed at young girls that typically focuses on blossoming romances between two unlikely candidates!"
    mo "I'm sure that doesn't sound familiar at all, does it?"

    scene makpark1r2
    with dissolve

    mak "Did you hear something just now?"
    s "Me? No."
    s "Anyway, I can’t say I’m all that familiar with shoujo manga. Though, I do feel slightly more informed about it all of a sudden..."

    scene makpark2
    with dissolve

    mak "So, do you come to this park often, Sensei?"
    mak "I have to say, I didn’t peg you as the type to enjoy public spaces like this."
    s "This is actually the first time I’ve been here. I didn't even know this place existed."
    mak "It actually didn't until just a short while ago."
    mak "One of my favorite things about Kumon-mi is how it's always changing. It's like...every time you wake up, there's something a little different going on."
    mak "We didn’t even have the cafe until recently. Now, it’s one of the most popular spots in town."
    s "Is that somewhere you go often?"

    scene makpark3
    with dissolve

    mak "No more than the average person, I suppose."
    mak "It seems like it would be a nice place to study if only it was a little quieter. Unfortunately, I don't think I'd be able to focus with how busy it always seems to be."

    scene makpark2
    with dissolve

    mak "I do like coffee, though. The pot I keep in my room is actually one of the first things I bought with my own money."
    s "Just try to keep it away from Miku if possible. I don’t want to imagine how hard she'd be to keep up with while hopped up on caffeine."

    scene makpark4
    with dissolve

    mak "Oh, you don’t have to worry about that. Miku actually hates coffee."
    mak "She needs to put almost eight tablespoons of sugar in one cup to even drink it. It's {i}that{/i} you should be worried about, Sensei."
    s "That sounds somehow even more terrifying..."

    scene makpark5
    with dissolve

    mak "She’s doing her best...but I agree that she can be a bit hard to keep up with on occasion."
    mak "I just wish she'd focus a little more on her studies so I don’t have to move onto the next grade without her."
    s "I could...maybe invite her over to my place for private tutoring? That doesn't sound creepy, does it?"

    scene makpark5r
    with dissolve

    mak "Wait...you offer private tutoring sessions at your house?"
    mak "Doesn’t that go against section 9C of the student handbook?"

    if bonus == True:
        mak "I could have sworn that students weren’t allowed to enter the residence of a teacher without express permission from the principal."

        "What kind of[school] actually puts a rule as specific as that in their student handbook?"

        s "I...am an exception to that rule."
        mak "Do you..."
        mak "Do you mind if I ask why?"
        s "..."
        mak "..."
        s "I do, actually."
    else:
        s "No, actually. After personally reviewing the handbook, I contacted the principal directly to see if I could be formally added in as an exception to the rule."
        s "You see, I think knowledge shouldn't be limited to just several hours a day. I am ready to teach all of you at all hours of the day, any time you're willing to learn."

    scene makpark5r2
    with dissolve

    mak "Well...umm..."
    mak "If that's the case..."
    mak "Would you maybe...mind if {i}I{/i} came over for a private session one day?"

    "You know, I expected Makoto to care a little more about my blatant shattering of section 9C...but I guess the idea of being alone with me combined with {i}learning{/i} managed to outweigh that."
    "There's no way she believes that I'm an exception to the rule, so I guess that even {i}she's{/i} okay with breaking a few of them if she's able to get something she wants out of it."
    "Of course, that will not stop me from teasing her about this because that sounds fun."

    s "I don't think so, Makoto. You don't really seem to need tutoring. My time is better spent on other girls."

    scene makpark6
    with dissolve

    mak "Wha-"
    mak "Just because I'm at the top of the class doesn't mean that I don't struggle with certain things too!"
    mak "I need tutoring just as much as the next girl, Sensei!"
    s "Do you? Or do you just want to be alone in my house with me?"

    scene makpark7
    with dissolve

    mak "Well...umm..."
    mak "I suppose that's...just a thing that would {i}have{/i} to happen for the...purpose of furthering my education."
    mak "Or something."
    s "..."
    mak "..."
    s "You just want another massage, don't you?"

    scene makpark8
    with dissolve

    mak "No! I don't want another massage!"
    s "I don't know if I believe you."

    scene makpark8r
    with dissolve

    mak "I just...need to learn everything I can since I also want to be a teacher some day."
    mak "And...I feel like if I’m ever going to get to where I want to be in order to do that...I probably need to learn from the best."

    "Was the person in this body before me {i}really{/i} that great of a teacher?..."
    "Just what the Hell did he do to get Makoto to think so highly of him?"

    s "If that's all it is, you can come over whenever you want."
    s "I’ll have to make sure I warn Ami ahead of time, though. I don’t think she’d take too kindly to a girl showing up unannounced, student or not."

    scene makpark5r2
    with dissolve

    mak "Hahah...yeah."
    mak "She...really loves you, doesn’t she?"
    s "I {i}am{/i} her uncle after all."

    "Kind of."

    mak "Agreed...I have my issues with Ami, but...you two make a good pair."
    mak "I'd almost feel a little guilty for intruding because of that."
    s "Almost?"
    mak "Well..."

    scene makpark8r2
    with dissolve

    mak "Let's just say my thirst for knowledge vastly outweighs how I feel about her."

    scene black
    with dissolve2

    "Makoto and I walk around for a little while longer before the time comes for us to part ways."
    "I mention coming over to her family's shop tonight and she begs me not to because that is what she {i}always{/i} does when I suggest such a thing."
    "All in all, nothing really changes."
    "The time we spend outside of school isn't all that different from the time we spend {i}in{/i} it."
    "Sure, there's a tinge of additional suggestiveness sprinkled onto different portions of our conversations...but it's all entirely normal apart from that."
    "Maybe that's a good thing, though?"
    "Maybe the relaxing life that Makoto wants doesn't require the wide open world? Maybe she can find comfort in the same building she spends every Monday through Friday in?"
    "Or maybe a life of comfort just isn't possible for her at all if even this is not enough to turn her into someone else."
    "I believe she's fine the way she is, albeit slightly flawed...But we're all flawed in our own ways and that alone doesn't make us worth giving up on."
    "She says goodbye to me with a smile on her face- and if it weren't for the glow of the sun illuminating her true feelings, I'd likely believe it."
    "Unfortunately for both of us, it's much easier to see in the light."
    "And so I know that smile is no smile at all."
    "But-"
    "It's still beautiful in its own backwards way."
    "........."
    "......"
    "..."

    scene makpark9
    with dissolve2

    y "…"
    y "…"
    y "…"
    y "…"
    y "…"

    scene black
    stop music

    $ renpy.end_replay()
    $ day38 = True
    $ makoto_love += 1

    "{i}Makoto's affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label day40:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label saturdayafternoon:

if totaldays >= 38 and firsttimepornshop == True and day36 == True and day38 == False:
    jump day38
...
```