# Under the Table (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 30

* Event [Two Hours](./futabadorm25.md) (Futaba) is completed)

* Event [See You in the Morning](./beachvacation16.md) (Main) is completed)

* Event [A Book About Dragons](./library25.md) (Futaba) is completed)



## Next events

* [Futaba: A Tree Falls in the Forest](./futabadorm30.md)

## Event properties

* Id: library30
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library
* Triggered by path: library->library30

## Official wiki page

[Under the Table](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library30&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library30:
    scene nodokafirst1
    with dissolve
    play music "morningmoon.mp3"

    "I walk into the library first thing in the morning to be greeted by a rather unusual sight."
    "And by unusual I mean a sight I have literally never seen before."
    "Typically, Futaba will spend her mornings rearranging books or...picking up books, or..."
    "Well, you get the point."
    "There are a lot of books involved."
    "It’s not often she actually engages with anyone other than me."
    "Is this girl planning on stealing Futaba away from me?"

    s "Who are you and what do you want with my librarian?"
    lt "{i}Your{/i} librarian? Futaba didn’t tell me the two of you were in that sort of relationship."
    lt "Sincerest apologies for what I am about to tell you, but this {i}librarian{/i} has been my property for several years now."
    lt "I’m willing to share her as long as you go through the proper request process. There are several caveats, however."

    scene nodokafirst2
    with dissolve

    lt "No touching, no teasing, no flirting, no talking, no exchanging of gifts (Including those sexual in nature), no staring and, most importantly-"

    scene nodokafirst3
    with dissolve

    lt "No-doka."
    s "I have no idea what that last one even means."
    no "It’s my name. Nodoka Nagasawa, a friend of Futaba’s from another[school]."

    if bonus == True:
        no "I’ve seen her exposed breasts more times than you."
    else:
        no "I can eat more spaghetti than you."

    "I wouldn’t be so sure about that..."

    scene nodokafirst4
    with dissolve

    f "Nodoka was in town on a...business trip, I guess?"
    f "She decided to stop by before heading back to the outer-barrier."
    s "Business trip? How old are you?"

    if bonus == True:
        no "Old enough. You need not concern yourself in my private ordeals."
        s "…"
        no "…"
        s "You’re not some sort of prostitute, are you?"
        no "Not that I am aware of."
        no "Are you the type to hire those sorts of people? If so, would you mind if I asked you some questions?"
    else:
        no "Well, obviously I am in college. Japanese women are just petite by nature."
        s "You are right. I apologize for assuming that was not the case. I just haven't heard much about you from Futaba as of yet, but I am excited to see where your story leads."
        no "Say, do you know anything about genome mapping?"

    no "It’s for research, I swear."
    s "Right. {i}Research{/i}."
    f "No, it really is for research, Sensei. "
    f "Nodoka is a writer and tends to dive into rather...unsightly topics at times."

    if bonus == True:
        no "My favorite is [incest]. It’s truly fascinating in fictional settings. Wouldn’t you agree?"
        s "Futaba is literally in the same class as my [niece]. I’m not going to share my opinion of [incest] with you. Fictional or not. "
    else:
        no "I don't know if I'd call genome mapping unsightly, but I do my best."
        s "..."

    scene nodokafirst5
    with dissolve

    no "Your lack of a response is the only response I need! Thank you very much!"

    if bonus == True:
        "What a strange character..."
    else:
        "Wow, she must be a real genius if that was the only research she needed."

    s "Anyway, were you planning on hanging out with your friend today, Futaba?"
    s "If so, I can just leave you two to it and go figure something else out."

    scene nodokafirst4
    with dissolve

    no "No need. I need to be heading out anyway."
    no "I just wanted to drop by and see if Futaba’s grown anymore since the last time I saw her several weeks ago."

    if bonus == True:
        no "She refused to take her shirt off in the library, though, so I don’t think I’ll be getting an answer today."
    else:
        no "Fortunately, she appears to be the exact same height."

    scene nodokafirst6
    with dissolve

    f "You never change, do you?"
    no "Why would I? I’m perfect the way I am. Just like you’re perfect the way you are."
    f "Well, thanks Nodoka. I’m glad to hear-"
    no "Let’s get married. "
    f "...No."
    no "Damn it. You’ll agree to that one day."
    f "I really won’t..."

    scene nodokafirst7
    with dissolve

    if bonus == True:
        no "You there. Glasses-companion. Let me know if you can figure out Futaba's latest cup-size."
    else:
        no "You there. Glasses-companion. Let me know if you can figure out how many clouds there are."
        s "Like...total? Doesn't the amount change?"
        no "Beats me."

    s "Is that for research as well?"
    no "No. It’s for my own personal records."
    s "I see. That’s good enough for me. I’ll have Futaba send you a message once I find out."
    f "Why are you agreeing to this? And why do I have to be the one to send the message?"
    no "Because I don’t give my number to strangers."

    scene nodokafirst8
    with dissolve

    no "But anyway, thanks for letting me visit for a little bit."
    no "This library is much smaller than the one I’m used to, but it’s cute. It’s got a sort of...rustic charm to it."
    no "Maybe I’ll come back one day?"

    scene nodokafirst9
    with dissolve

    no "Sayonara, Futaba! And you as well, mystery-man!"
    s "My name is Sensei."
    no "No it isn’t!"

    "Nodoka exits the library and leaves Futaba and I sitting there in silence for a little while."

    f "So anyway, that’s Nodoka."
    s "She seems...fun."
    f "She’s a lot. "

    scene nodokafirst10
    with dissolve

    f "She’s one of the smartest people I know, though. You should read some of her work if you ever get the chance."
    s "Where would I find it? Is she online or something?"
    f "I can...umm...maybe send you a few links?"
    s "Do you have my number? Or email address or anything?"

    scene nodokafirst11
    with dissolve

    f "Well, no...But if you wanted to maybe...give it to me or something...that would be okay."
    f "That’s not too weird to say, right?"
    f "I promise I’d only text you if I need something or...have to give you something."
    s "You can text me whenever you want. I don’t care."

    scene nodokafirst12
    with dissolve

    f "Really?! You mean it?!"

    scene nodokafirst13
    with dissolve

    f "Oh! Umm. Sorry. I didn’t expect to react that way."
    f "I don’t know what came over me."
    s "It’s fine. Don’t worry about it."

    "I take my phone and slide it across the table, giving Futaba the go-ahead to enter her contact info."
    "She nervously does so and, before long, both of our phones are back in our respective pockets."

    $ futabanumber = True

    "{i}Congratulations! You now have Futaba’s phone number!{/i}"

    s "So, now that your friend is gone and the two of us are alone, there’s been something I’ve been meaning to ask you."

    scene nodokafirst14
    with dissolve

    if bonus == True:
        f "Umm...it’s nothing...you know...{i}sexual{/i}, is it?"
        f "I’ve accepted that we have that type of relationship now but I still don’t know if I’m comfortable...you know, {i}helping{/i} you out in the library."
        f "There are people around and-"
    else:
        f "I don't know how many clouds there are, Sensei..."

    s "I was actually just going to ask if everything was okay."
    f "…"

    scene nodokafirst15
    with dissolve

    f "Huh?"
    f "What do you mean?"
    s "I mean that we haven’t really talked about what randomly sent you home from the beach."
    s "Molly was pretty upset that you weren’t able to play that game with everyone, and that seemed like something you’d be really into."
    f "…"
    s "…"
    f "…"
    s "…"

    scene nodokafirst16
    with dissolve

    if bonus == True:
        f "On second thought, maybe I could...give you a handjob...under the table or something..."
        s "As much as I love under-the-table handjobs, it sounds to me like you’re trying to hide something."
    else:
        f "On second thought, maybe I do know how many clouds there are."
        s "You bitch."

    scene nodokafirst17
    with dissolve

    if bonus == False:
        s "Apart from that, though, it seems like you're hiding something."
        f "I'm not hiding anything..."
    else:
        f "I’m not hiding anything...I just want to...give you a...h-handjob..."

    s "That doesn’t sound very confident, Futaba."
    f "Why would you even want to know that? I look fine now, don’t I?"

    "I hadn’t noticed before, but now that I’m paying closer attention, Futaba does look a little bit...off."
    "I can’t really pinpoint exactly what’s wrong, but something’s different."
    "And no, I’m not talking about her hair being down. It’s something more than that."

    s "I want to know because I care about you."

    scene nodokafirst18
    with dissolve

    f "S-Sensei...You can’t just come out and say that all of a sudden...it’s embarrassing."
    f "There are people around. Someone might hear you."
    s "What’s so bad about people hearing that I care for one of my students? I care about all of you."
    f "It’s just...someone might get the wrong idea."
    s "Well that’s on them, then. But don’t worry about other people right now."
    s "If something is bugging you, it’s okay to tell me."

    scene nodokafirst19
    with dissolve

    f "Th-thanks...but I’m pretty sure I’d rather keep this thing to myself if that’s okay."
    f "It’s not like...a really big deal or anything. It would only create more problems for you."

    scene nodokafirst20
    with dissolve

    f "But I’ll be better for it in the long run. Just worry about yourself and let me deal with my issues on my own."
    s "...It’s not about Yumi, is it?"
    f "It’s not. She actually hasn’t even said anything to me since the beach."

    "Huh...if Yumi’s not the source of her problems this time, I wonder what is?"
    "I know her family lives overseas so...maybe it’s something that has to do with them?"
    "Either way, it doesn’t look like she’s willing to reveal whatever’s going on right now, so I should probably just talk about something else."

    s "So, Nodoka."

    scene nodokafirst21
    with dissolve

    f "Yes, Nodoka."
    f "She’s cute, isn’t she?"

    if bonus == True:
        s "If there’s anything I’ve learned about girls that I’m {i}involved{/i} with it’s to never talk about how cute other girls are around them."
        f "I don’t see a problem with you thinking she’s cute. {i}I{/i} think she’s cute and I’m not planning on leaving you for her."
        f "Though, I think she'd be quite happy if I did."
        s "If you do decide to do that, please let me know in advance so I can buy a video camera."
    else:
        s "I think she might be in love with you."

    scene nodokafirst22
    with dissolve

    f "Please stay out of my first lesbian relationship. You and I are no longer together."

    if bonus == False:
        s "Wait, when were we ever together?"

    f "What we had was fun, but it was as fleeting as a summer breeze."
    f "You were just an old tooth that happened to be pushed out by a new one."
    s "That first metaphor was a little stronger than the tooth one."

    scene nodokafirst23
    with dissolve

    f "We can’t all be Nodokas, you know? I’m doing my best."
    s "That’s right. You are doing your best. And that’s really all that matters."

    scene nodokafirst15
    with dissolve

    f "Hm? Why are you getting serious all of a sudden?"
    s "I didn’t mean to. It just kind of slipped out, I guess."
    s "Maybe I’m subconsciously worried about you since you’re keeping your first ever secret from me."

    scene nodokafirst10
    with dissolve

    f "Who said this is the first?"
    f "Either way, I think you should {i}subconsciously{/i} stop because it’s harder for me to smile when you’re not smiling."
    f "And yes, I know that line probably needed some work as well."
    s "It was better than the tooth one at least. That one still hits me the wrong way for some reason."
    f "Yes, yes. I know it was bad. I won’t talk about teeth anymore."
    s "I appreciate that."

    "I pull my phone out of my pocket and check the time to find that it’s getting close to lunch."
    "Since the two of us don’t seem to have anything else going on, maybe Futaba will want to come out for a little bit?"
    "No harm in asking, I guess."

    s "Hey, are you doing anything after this?"

    scene nodokafirst15
    with dissolve

    f "Like, after the library? Not really. Why?"
    s "Did you want to come get lunch or something? I’m probably going to head out soon."

    scene nodokafirst21
    with dissolve

    f "That does sound fun, but I need to stay here for pretty much the entire day today."
    f "Thank you for inviting me, though. It makes me happy to hear that...you want to spend more time with me and stuff..."
    s "You have to spend the whole day here? Aren’t you a volunteer?"
    f "I am, but that doesn’t mean I can just leave whenever I want."

    scene nodokafirst24
    with dissolve

    f "I have a responsibility and I can’t walk away from it. That’s what it means to be an adult."
    f "But of course you wouldn’t know that since you’ve given up on teaching and just want to hang out with everybody instead."
    s "Don’t question my methods. Your grades are better than ever."

    scene nodokafirst25
    with dissolve

    f "Grades? We have grades?"
    f "I thought we were just messing around."
    s "We were, but I’m giving you an F now for losing faith in my patented system."

    scene nodokafirst13
    with dissolve

    f "An F?! You can’t do that! I thought we were just joking!"

    scene black
    with dissolve

    "Little does Futaba know, I’m the most serious man in the world."
    "I never joke about anything."
    "Just kidding."
    "But either way, I’m significantly less willing to spend my entire day wasting away in a library than Futaba is."
    "Who cares about responsibility when there are more important, more fulfilling things to be doing?"
    "I offer to buy Futaba something and bring it over in order to make her double-volunteer-shift a bit more bearable, but she shrugs off my act of generosity and tells me she brought something with her."
    "What a bitch."
    "Just kidding again."
    "Not knowing what else to do, I stop at a nearby burger joint and grab a quick lunch before getting on with my day..."

    $ renpy.end_replay()
    $ library30 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label library35:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
    if futaba_love >= 25 and futabanew3 == True and library20 == True and library25 == False:
        jump library25
    if futaba_love >= 30 and futabadorm25 == True and beachvacation16 == True and library25 == True and library30 == False:
        jump library30
...
```