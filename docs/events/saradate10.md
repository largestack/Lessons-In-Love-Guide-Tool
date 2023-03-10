# Uptown Girl (Sara)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sara love greater than or equal to 10

* Event [Like it's Any Other Day](./nikidate5.md) (Niki) is completed)

* Event [Waiting for Anything](./sanadorm35.md) (Sana) is completed)

* saranumber equal to True (unknown variable)



## Next events

* [Otoha: Japanese Summer](./otohapark1.md)

## Event properties

* Id: saradate10
* Group: Sara
* Triggered by label: callsaraafternoon
* Triggered by branch label: callafternoon
* Triggered by path: callafternoon->callsaraafternoon->saradate10

## Official wiki page

[Uptown Girl](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=saradate10&go=Go) for more details.

## Event code

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label saradate10:
    play sound "phonebeep.wav"

    "I tap on Sara’s name in my phone and wait for her to answer."
    "It’s relatively windy out today, but that doesn’t stop me from wanting to wander around outside for a bit."
    "And if there is anyone I know who likes wandering around the city with me (And routinely stopping to buy candy because she is a child trapped in a woman’s body), it’s Sara."
    "But hey, if a few stops at convenience stores are all it takes to be seen in public with an attractive woman that’s actually close to my age..."
    "I guess that’s a price I’m willing to pay."

    play sound "phonebeep.wav"

    sar "Mmn...hello?..."
    s "Hey. You’re not just waking up now, are you?"
    sar "What time is it?..."
    s "It’s a little past noon."
    sar "Ngh..."
    sar "I drank too much last night..."
    s "Yeah, that sounds on-brand."
    s "Want to subject yourself to sensory overload and go walk around the urban district for a little while?"
    sar "Mnh...when?"
    s "Like, now."
    sar "Guh...okaaaaay."
    sar "I’ll start getting ready..."

    play sound "phonebeep.wav"

    "Sara hangs up and I begin to make my way to the same huge office building we normally meet at when we decide to visit that part of town."
    "Knowing that it will likely be a while until she gets there, I stop for coffee at a nearby cafe (One without any [[confirmed] manga club members working) and pick something up for Sara as well."
    "………"
    "……"
    "…"

    scene saranikiboard1
    with dissolve
    play music "justbehappy.mp3"

    "Unfortunately, she is one of those cowards who is incapable of drinking black coffee, so I wind up consuming two drinks instead of one."
    "That’s fine, though."
    "Caffeine is one of those drugs that you can’t overdose on."
    "Probably."
    "And, even in the event that I somehow did, she’ll be here to call an ambulance."
    "I’m sure today will proceed just fine with all of that in mind."

    s "You look really good for someone battling a hangover right now."
    sar "Thanks~ "
    sar "The trick is to just drink more as soon as you wake up so your brain can go back to feeling good."
    s "That’s not a trick, that’s alcoholism."
    sar "I just call it having a good time."
    s "That is also alcoholism."
    s "You have a problem."

    scene saranikiboard2
    with dissolve

    sar "I do not! It’s not like I do this every morning, Sensei. "
    sar "I just got a call from Haru-chan really late last night because she was feeling all lonely again."
    sar "So the two of us did what any good friends would do and got drunk on the phone and cried to each other about all kinds of stuff."
    s "I’m kind of glad I don’t have any friends as close as that. That sounds horrible."

    if sarasex == True:
        scene saranikiboard3
        with dissolve

        sar "That’s not true. I’m your friend, Sensei~"
        sar "And I think we’re plenty close."

        if bonus == True:
            sar "So close that you get to stick it in me while my daughter is downstairs. Isn’t that great?"
            s "For us? Yes. For your daughter? No."
            sar "Well {i}I{/i} think it’s great."
            sar "Don't you think it’s like...about time we told her, though?"
            sar "At least that way, we probably wouldn’t have to worry about her walking in on us."
            s "I prefer to keep my relationships secret, if you don’t mind."
            s "Especially from people as pure as Sana."

            scene saranikiboard4
            with dissolve

            sar "Oh, please. She’s a growing girl. I’m sure she gets up to all sorts of stuff while she’s alone."
            s "Take that back. I will not allow you to tarnish that girl’s image."
            sar "I’m just saying, I know I did when I was her age. "
            sar "But I was also having sex with my teacher when I was her age, soooo..."
            sar "Maybe I just have a thing for teachers?"
        else:
            sar "Some might even say we're like a sandwich. Just two meats stuck together, waiting to be consumed by a large man."
            s "No one would say that."
            sar "You never know, Sensei."

    else:
        scene saranikiboard5
        with dissolve

        sar "That’s not true, Sensei. I think we’re plenty close."
        sar "Even if you won’t accept my love."
        s "I’ve accepted it. I just can’t return it."
        sar "Yeah, that."
        sar "But if you ever feel like calling me in the middle of the night to get drunk and cry, I’ll always be there. Kay?"
        s "This is not a thing I will ever want. But thanks, Sara."
        sar "Of course~"

        scene saranikiboard6
        with dissolve

        sar "Though, I suppose at this point you’d rather just call my daughter and talk to her instead, wouldn’t you?"
        s "I’m not quite sure what you’re insinuating with that."
        sar "Just that she’s getting awfully warmed up to you out of nowhere."

        if bonus == True:
            sar "Maybe on account of you visiting her dorm room at night?"
        else:
            s "I am the only person who knows she is a health inspector. It is a bond we share now."

        scene saranikiboard7
        with dissolve

        sar "Maybe if I was still her size..."

        if bonus == False:
            s "Maybe if you were a health inspector."
            sar "..."

        s "…"
        s "Okay, anyway, why don’t we talk about something else?"
        sar "Embrace my youthful jealousy, Sensei...Embrace it~"
        s "It’s less of a youth thing and more of an...innocence thing."
        s "And even then, nothing like that is even close to happening between Sana and me."

        if bonus == True:
            sar "But...if the opportunity arose..."
            s "…"
            sar "Come on. If there’s anyone who knows what teachers like you think about in their spare time, it’s me."
            sar "I was barely a freshman when I started sleeping with mine."
        else:
            sar "Okay. Thank you for being honest with me. I appreciate you as a person and respect your decision to not pursue a further romantic relationship with her."
            s "No prob."

    "It’s crazy right now to think of Sana doing anything remotely close to what Sara was doing back then."

    if bonus == True:
        "Will that {i}stop{/i} me from thinking about it? Of course not. "
        "My mind lands on that almost every time I walk into her room."
        "But it’s just so far out of reach at this point that I don’t even bother addressing it."
        "Sara, though-"
        "Those experiences went on to shape the rest of her life."
        "A lot of people say that the first few years of a child’s life are what go on to sculpt them as a person."
        "I don’t think I agree with that."
        "I think that people tend to find themselves in their[teen]years- particularly their years in [high_school]."
        "Which is why I’m so worried about how everyone I know will eventually break down and die."
        "And how I, too, will become the man who abandoned Sara and her family."
    else:
        "She is such a good girl."

    s "Do you regret it at all?"

    scene saranikiboard8
    with dissolve

    if bonus == True:
        sar "What? Sleeping with my teacher? "
    else:
        sar "What? Hugging my teacher until the stork showed up and gave me my children?"

    s "Yeah."
    sar "Hmm...I guess I do sometimes."
    sar "I definitely loved him. "
    sar "But now I have an adorable little girl who’s going to wind up becoming a better version of me when she's older. And that’s fine."
    sar "Besides, even if he wound up being unfaithful, I needed someone like that back then."
    s "Have you always been this-"
    sar "Needy?"

    scene saranikiboard9
    with dissolve

    sar "Probably."
    sar "Yeah, I’d say so."
    sar "I was kind of like an...anti-Sana when I was in [high_school]."

    if bonus == True:
        sar "Instead of closing myself off from everyone, I chose to stay wide open instead."
        sar "I would have let anyone in regardless of who they were or what they wanted from me."
        sar "And I wound up falling for the first person to ever look at me as a girl."
        sar "Well, the first older person at least."

        scene saranikiboard10
        with dissolve

        sar "There were plenty of boys who liked me back then, but I never really had any interest in them since they were all just kids."
        sar "Like, what could they do for me that I couldn’t do for myself?"
        s "Well, you just wanted to feel loved, right? That’s what you’re making it sound like."
        sar "I think “protected” is a little closer to what I was looking for."
        sar "It would make me happy when I’d get a confession from a boy, but none of them would ever make me feel as safe as someone older with more...power and stuff."
    else:
        sar "Instead of closing myself off from everyone, I started a popular polka group and learned how to play the accordian."

    scene saranikiboard11
    with dissolve

    sar "Which is probably one more reason I like you so much."

    if bonus == True:
        s "The only power {i}I{/i} have is determining whether a handful of [teenage]girls will make it through their first year of [high_school] or not."

        scene saranikiboard12
        with dissolve

        sar "You’ve got a lot more power than that, Sensei."
        sar "You have an entire class of girls who look up to you and learn from you."
        sar "And with barely any men around, you’re pretty much the only male figure they have in their lives."
        sar "Given those kinds of circumstances, I think it’s pretty miraculous you’re as decent as you are."
    else:
        s "What?"

    scene saranikiboard13
    with dissolve

    sar "If only the same could have been said about Sana’s dad..."

    if bonus == True:
        s "I take it he was one of those people who abused his position?"

        scene saranikiboard14
        with dissolve

        sar "Will you think I’m dumb or gullible if I say he was?"
        s "I think you’re dumb and gullible now."
    else:
        s "What does that have to do with anything?"
        sar "Oh, you know."
        s "Sara, I don't even like the accordian."

    scene saranikiboard15
    with dissolve

    sar "Hey!"
    s "I’m kidding..."

    "Kind of."

    s "Of course I won’t think that. "
    s "I don’t know what things were like for you when you were that age, and I don’t know what must have been going through your mind in order to deal with that."
    s "But it’s not crazy to believe someone would have taken advantage of you in the position."

    scene saranikiboard16
    with dissolve

    sar "Good recovery. I like you again."
    s "Good. Those ten seconds you didn’t were really suspenseful. "

    scene saranikiboard17
    with dissolve

    sar "Heheh~"
    sar "Either way, what’s done is done. "
    sar "All things considered, I think I’m in a pretty good place now."
    sar "I own a business."
    s "That’s failing."
    sar "I have a nice apartment."
    s "That you live by yourself in and are likely overpaying for."
    sar "And I have the cutest daughter in the world."
    s "Who can’t hold a conversation to save her life."

    scene saranikiboard15
    with dissolve

    sar "You’re mean today! Let me have something!"
    s "You have my arm. Any more and you’ll start getting ahead of yourself."

    scene saranikiboard11
    with dissolve

    sar "Oh ho ho~ Are you saying I get to keep this arm all to myself?"
    s "Sure. For now. "
    s "I do want something in return, though."

    if bonus == True:
        sar "Ooooh? Do we need to go somewhere a little more private, [saramaster]?"
        s "It’s nothing like that."
        s "I just want you to tell me more of your story sometime."

        scene saranikiboard18
        with dissolve2

        sar "…"
        s "I’m obviously not going to call you at 2:00AM to get drunk and cry, but I’d like to hear more about how you wound up where you are now."
        s "I know surprisingly little about you for a girl who is allegedly “wide open.”"

        "I’m also sure that figuring out what makes Sara tick is sure to help me grow a little closer to Sana as well."
        "And, even if it doesn’t, I’m interested in seeing how things got to this point."
        "And how I might possibly be able to avoid forcing that onto anyone else in the future."

    sar "Do you want to get married?"
    s "What?"
    s "No?"

    scene saranikiboard19
    with dissolve

    sar "Heheh~ Just checking..."
    sar "I’d love to tell you more of my story sometime."
    sar "And I’d love to hear yours as well."
    s "…"
    sar "…"
    s "Yeah, I don’t know if-"

    scene saranikiboard20
    with dissolve

    sar "Oh! Here’s a good place to start now!"

    scene saranikiboard21
    with fade

    "Sara lets go of my arm and skips over to a local concert hall, displaying a gigantic billboard of-"

    s "Uh-oh."
    sar "When I was a little girl, I wanted to be just like that one day."
    sar "Someone the entire world would gaze at with envy."
    sar "A person that boys would adore and that girls would look up to."

    if bonus == True:
        sar "But now I’m washed up and emotionally spent before even hitting the middle of my thirties."
    else:
        sar "But now I’m just...washed up and emotionally spent."

    sar "Do you like girls like that, Sensei?"
    sar "They make your heart race, don’t they?"

    scene saranikiboard22
    with dissolve

    sar "Or maybe they make you feel a little something else?"

    if bonus == True:
        sar "Doesn’t seeing that cute girl up there make you want to just grab her and corrupt-"
    else:
        sar "Doesn’t seeing that cute girl up there make you want to just take her to the zoo and show her the elephants?"

    scene saranikiboard23
    with dissolve

    sar "…"
    s "…"

    scene saranikiboard24
    with fade

    sar "Why aren’t you saying anything?"
    sar "Don’t tell me that...{i}you{/i} wanted to look like that one day, too?..."
    s "That..."
    s "Is my ex-girlfriend."
    sar "…"
    s "…"

    scene saranikiboard25
    with dissolve

    sar "Oh, come on! Like I’d ever believe that you dated {i}Niki.{/i}"
    sar "She’s like...an icon in Kumon-mi. "
    sar "I don’t really follow idols the way I used to, but she’s on TV all the time and..."
    sar "And you still haven’t told me you’re kidding yet..."

    scene saranikiboard26
    with dissolve
    play sound "phonebeep.wav"

    sar "What are you-"

    scene saranikiboard27
    with dissolve

    sar "What are you doing? I have no idea who-"

    play sound "phonebeep.wav"

    ni "Haven’t I told you not to call me in the middle of the day before?! I’m fucking busy!"

    scene saranikiboard28
    with dissolve

    sar "Um...is this..."
    ni "…"
    ni "Who the fuck are you?"
    sar "A friend of...your ex-boyfriend’s..."
    sar "Is this really Niki Nakayama?"
    ni "Teehee~ Apologies, miss! That was my manager on the phone just now."
    ni "Would you mind putting your {i}friend{/i} on the line for sec? There's something I need to talk to him about~"

    scene saranikiboard29
    with dissolve

    sar "She, uhh...wants to talk to you..."
    s "…"
    sar "…"
    ni "Hello? "
    ni "Are you still-"

    scene saranikiboard30
    with dissolve
    play sound "phonebeep.wav"

    sar "Ah!"
    sar "You just...hung up on Niki..."
    s "This is what’s best for everyone."

    scene saranikiboard31
    with dissolve

    s "Do you believe me now?"
    s "You should have been able to recognize her voice if you know her, right?"
    sar "…"
    s "…"

    if sarasex == True:
        if bonus == True:
            sar "I’m...having sex with Niki Nakayama’s ex-boyfriend?..."
        else:
            sar "I hugged a person Niki Nakayama hugged?..."

        sar "Did I...Did I finally make it after all?"
        s "…"
    else:
        sar "It’s suddenly starting to make a lot more sense why you don’t like me the same way I like you."
        s "…"

    scene black
    with dissolve2

    "Sara is a little too shocked to carry on hanging out after that."
    "There’s also the fact that she needs to start getting ready for work, but it’s not like that’s ever stopped her before."
    "All things considered, I think this was a pretty good afternoon."
    "I got to learn a little more about Sara...and also got to make myself look a lot cooler than I actually am in the process."
    "Now, as long as Niki doesn’t-"

    play sound "texttone.wav"

    s "…"

    play sound "texttone.wav"

    s "…"
    s "I’ll just..."
    s "Read those later..."

    $ renpy.end_replay()
    $ saradate10 = True
    $ sara_love += 1
    stop music fadeout 5.0

    "{i}Sara’s affection has increased to [sara_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label sarabar20:
...
```

## Code that triggers this event

File: (install folder)\game\SaraEvents.rpy

Code:
```python
...
label callsaraafternoon:
    if saranumber == True and bar15 == False:
        "I think I should probably get to know Sara a little better before calling her."
        jump callafternoon
    if sara_love >= 0 and bar15 == True and saradate1 == False:
        jump saradate1
    if sara_love >= 10 and nikidate5 == True and sanadorm35 == True and saradate10 == False:
        jump saradate10
...
```