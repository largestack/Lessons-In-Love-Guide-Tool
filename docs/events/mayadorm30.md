# What it Means to Be Destroyed (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 30

* Event [FLAVOR BEAM!](./mayadorm25.md) (Maya) is completed)

* Event [Beginnings. Endings. Things in Between.](./norikoinvite2.md) (Noriko) is completed)



## Next events

* [Maya: Now More Than Ever](./shrine30.md)
* [Maya: A Place That Can Only Exist in Our Minds](./mayadorm35.md)

## Event properties

* Id: mayadorm30
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm
* Triggered by path: mayadorm->mayadorm30

## Official wiki page

[What it Means to Be Destroyed](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm30&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm30:
    play sound "knock.mp3"

    "I knock on Maya’s door."

    stop music
    play sound "static.mp3"
    scene whyme with flash
    scene whereareyou with flash
    scene whygodwhy with flash
    scene 3 with flash
    scene anotherbox1 with flash
    stop sound
    play music "hometown.mp3"

    "I carry a box."

    m "Thank you for your help."
    m "I understand how hard it must have been to find the time to help me do this again."
    s "Don’t mention it. And there’s no need to be so polite."
    m "There’s not?"
    m "In that case, you make me sick."
    s "That’s more like it. This is the Maya I know."
    m "Why are you not staying away from her?"
    s "Is this about Noriko again?"
    m "Have I ever asked you to stay away from anyone else?"
    s "You."
    m "That’s different. I’m just difficult, not dangerous."
    s "Well, at least you’re self-aware."
    s "Why is Noriko dangerous, though? She hasn’t even done anything yet."
    m "“Yet” is the key word."
    m "She has a long history of getting in the way."
    m "A history that, and this may come as a shock to you, I’d rather not repeat."
    s "And here I was thinking you’d do anything to get back into your weird comfort zone of replaying the same[school] year over and over again."
    m "That “comfort zone” is anything but comfortable for me."
    m "It’s like someone is shoving toothpicks under my fingernails and sliding them around until my nails fall off."
    m "Would you not say the same for yourself right now?"
    s "What do you mean?"
    m "With each passing day, do you not find it harder to conceal the true nature of who you really are from all of the people who think you’re someone else?"
    m "It will all come crashing down soon."
    s "And how exactly will Noriko make that happen any-"
    m "Noriko can’t keep a secret."
    m "She’s also a hyper obsessive stalker who has been looking for you for years now."
    m "You should thank me for keeping her away as long as I have."
    s "…"
    m "…"
    s "How were you the one who kept her away?"

    scene anotherbox2
    with dissolve

    m "That doesn’t concern you."
    s "It definitely concerns me, Maya."
    s "In fact, pretty much everything you’ve been doing lately concerns me."
    s "How much do you know about me and what good does it do to keep it all locked away?"
    m "The “good” it does is keep you {i}here.{/i}"
    s "How is that good? All you ever do is try to get rid of me."
    m "Not “here” on a physical level. “Here” as an idea."
    s "...What?"

    scene anotherbox3
    with dissolve

    m "Can you really not follow along after all this time?"
    m "You’re so annoying."
    m "I’ve made it overwhelmingly clear that I don’t want you around me because it will make things exponentially more difficult for both of us."
    m "Particularly me."
    m "But I’m completely content with you continuing to exist as long as you stay away."

    scene anotherbox4
    with dissolve

    m "Several of the very few people I actually care about rely on you in more ways than you can imagine."

    scene anotherbox5
    with dissolve

    m "And the more you remember, the less likely it is for you to continue living."
    m "Even if what you’re doing right now could barely be called “living” anyway."
    s "You know that as a fact? That me just...learning things could be that dangerous?"

    scene anotherbox6
    with dissolve

    m "An irrefutable one."
    s "And I should just...take your word for it and trust you instead of Noriko?"
    m "Yes. That is what I want you to do."
    s "You can see how this doesn’t sound like a very good deal to me, right?"
    m "Does it? I assumed maintaining possession of your body and its accompanying consciousness would be quite appealing to a narcissist like you."
    s "Don’t talk like I’m the only narcissist in this room."
    m "Are you insinuating that I possess the same inherent need to be admired as a man who spends virtually all of his free time nurturing his relationships with [teenage]girls?"
    s "Well...when you put it that way, no."
    s "But you do center the world around yourself."
    m "Do I?"
    s "I mean, I’m pretty sure that you’ve literally said that before."
    m "So you now magically believe everything I say without even making an effort to discern the subtext or circumstance?"
    m "You really are annoying."
    s "…"
    s "Seriously...are you okay, Maya?"

    scene anotherbox7
    with dissolve

    m "I’m fine. Stop asking that. "
    m "In fact, stop asking me any questions at all."
    m "Just do what I say and live the way I tell you to if you don’t want to risk disappearing."
    s "Now {i}that{/i} is something that could barely be called “living.”"
    m "I can’t remember the last time I had to deal with this type of behavior from you."
    m "It’s like even when I want to be serious, you just treat everything like it’s some sort of game."
    m "And-"
    s "I know. “This isn’t a game.” "
    s "You’re like a broken record."
    s "“Stay away from me. Noriko is evil. I love watermelon. Stars are neat.”"

    scene anotherbox9
    with dissolve

    m "Your impression needs some serious work. I don’t sound anything like that."
    s "Your voice is a little higher than mine, sure. But those are definitely sentences you’ve said before."
    m "I’ve never done something as stupid as calling the stars “neat.”"

    scene anotherbox10
    with dissolve

    m "Wait, how did we even get to this?! This was supposed to be a serious confrontation!"
    s "I don’t want it to be serious anymore. "
    s "I just want to hang out with you and carry weird boxes to the[school] in the middle of the night."
    s "And I don’t want you telling me how I should be living {i}my{/i} life when you’re barely living your own."

    scene anotherbox11
    with dissolve

    m "…"
    s "…"
    m "There’s nothing wrong with the way I’m living."
    s "I’ll believe that as soon as I start seeing you do something that will make {i}you{/i} happy instead of just...keeping the world moving or whatever."

    scene anotherbox12
    with dissolve

    m "Is simply being alive not reason enough to be happy?"
    m "Things are already falling apart. "
    m "And I’m sure that’s my fault for...even thinking about doing anything for myself in the first place."
    m "What’s so wrong with complacency? "
    m "Why can we not enjoy the days we’re given without attempting to stitch them together into something bigger?"
    m "Why does there need to be anything bigger at all?"
    s "You realize I can’t answer any of those questions, right?"

    scene anotherbox13
    with dissolve

    m "Because you’re useless."
    m "And your inability to take direction is forcing us ever so closer to the brink of destruction."
    m "And of course I’m the one who needs to figure out how to steer us away from it."
    m "How nostalgic."
    s "Nostalgic?"
    s "Have we been “destroyed” before?"
    m "Many times."
    m "Just...in different ways."
    s "I don’t know what that’s supposed to-"
    m "Close your eyes."
    s "What?"
    m "Just close them."
    m "I want to take you somewhere special to me."
    s "…"
    s "You’re not going to push me off the roof, are you?"
    m "…"
    s "…"

    scene anotherbox14
    with dissolve

    s "Don’t just smile and look away without answering that question."
    m "Despite how much I may want to, I’m not going to hurt you."
    m "It will only take a few minutes."
    m "It’s not far."
    s "…"
    m "…"
    s "Fine."

    scene black
    with dissolve2

    s "But you’re going to have to hold my-"
    m "This way, please."
    s "Wait, you’re not even going to guide me? "
    s "We’re on the third floor. There are stairs."
    m "Well then I hope you’ve remembered how many there are."
    m "Left up here."
    s "…"

    "I wind up slowly following Maya out of the[school] and back out into the cold winter air."
    "I’m able to move a little quicker once we get outside due to there being no looming threat of sudden verticality changes..."
    "But it’s still a painfully difficult journey nonetheless."
    "I don’t remember if it was snowing on the way here or not- and I can’t really tell if it’s snowing right now."
    "But it’s certainly cold enough to-"

    if bonus == True:
        play sound "static.mp3"
        scene mayacg8
        with flash
        scene mayasweep5
        with flash
        scene mayadormten21
        with flash
        scene mayasit2
        with flash
        scene mayayay2
        with flash
        scene reset8
        with flash
        scene mayabeach10
        with flash
        scene anotherbox15
        with flash
        stop sound
        play music "comfort.mp3"
    else:
        play sound "static.mp3"
        scene anotherbox15
        with flash
        stop sound
        play music "comfort.mp3"

    s "…"
    m "…"
    s "Did you buy me this?"
    m "It was the least I could do after making you walk all the way to[school] with me."
    s "What is-"
    m "Just drink it. "

    scene anotherbox16
    with dissolve

    "I crack open the can and take a sip."
    "It’s a sort of semi-sweetened iced coffee that causes a wave of nostalgia to sweep over me as I press my back against the cold alley wall."

    s "…"
    m "…"

    "Of course, things are once again awkward between the two of us and I feel a sudden urge to speak out."
    "The weird thing with Maya is that I’m not even sure if I should try breaking
    the ice in times like these or not."
    "I feel like more than half the time she just tells me to stop talking."

    scene anotherbox17
    with dissolve

    m "How is it?"

    "She decides to speak first this time."

    s "It tastes familiar."
    m "Not too familiar, I hope."
    s "Worried I’ll remember too much and cause the world to blow up?"
    m "Does the thought of that not terrify you?"
    s "Sure it does. I just highly doubt some can of coffee would be the final nail in the coffin."
    m "I see."

    scene anotherbox18
    with dissolve

    m "I’ve heard before that things like tastes and scents often teleport people back in time, albeit to a significantly lesser extent than we’ve already experienced firsthand."
    m "A means of evoking childhood memories or significant periods of time that hold great emotional weight for a person."
    m "Things like this are likely safer than brute-forcing your past back into your mind, I believe."
    m "Has that rebel slut tried anything this simple yet?"
    m "Or is she still feeding you memories out of her hand like you’re an animal in a fucking zoo?"

    scene anotherbox19
    with dissolve

    s "Woah."
    m "What?"
    s "That was...uncalled for."
    m "Forgive me."
    m "It’s probably hard to notice, but I’m not quite fond of her."
    s "You..."
    m "I?"
    s "Sorry. I’m just trying to figure out a way to ask you for information without directly asking you for information."
    m "Perhaps you’d like to run something she told you past me?"
    m "Confirming or denying those bits of information likely won’t have any adverse effects."
    s "Then-"
    s "I used to tutor you as well, right?"
    m "Correct."
    s "How long ago was that?"
    m "It’s probably best to not ask me timeline related questions when my perception of time itself has been warped beyond recognition."
    m "We go back quite some time, though."
    s "That’s really odd."
    m "Why is that odd?"
    s "Because that...journal thing I found in my room says I don’t know anything about you. Why would I write that if it’s not true?"

    scene anotherbox17
    with dissolve

    m "Have you considered that perhaps you’re not the one who wrote it?"
    s "I mean, {i}I’m{/i} obviously not the one who wrote it."
    m "I mean someone outside of that body entirely."
    s "Uhh...no."
    s "A mildly creepy journal containing basic information on everyone does not seem like something that would have been made by one of the girls."
    m "Then I suppose it's about time I come out and just admit to creating it on account of your ineptitude rearing its ugly head once again."
    m "Besides, hiding it any longer doesn’t seem to make much sense anyway. "
    s "But...why-"
    m "It got quite tiring seeing so many people fail miserably on day one."
    m "As you noticed, I attempted to make myself as unappealing as possible by saying you didn’t know anything about me and that I don’t like men-"
    m "But I suppose I am just that irresistible after all."
    s "…"
    m "…"
    m "Are you surprised?"
    s "Surprised is a bit of an understatement."
    m "I don’t think it should have been that hard to realize. But, then again, it’s {i}you{/i} we’re talking about."
    m "I’m sure there are plenty of other things Iying around your room that I’ve put there as well."
    m "I just can’t remember any more of them off the top of my head."
    s "I don’t know if I should thank you for the push or if I should reprimand you for going through my things."
    m "Neither. Continue to do exactly as you’re doing now. "
    m "With the one minor exception of completely cutting ties with Noriko Nakayama."
    s "I’m not going to cut ties with Noriko, Maya."
    m "What if I say please and pout at you the way Ami does?"
    s "As much as I would love to see that, the answer is still no."
    m "Then let me ask you this-"
    m "She’s already made it apparent that you have disappeared on her before, correct?"
    m "Why do you think you may have done that?"
    s "Well, that wasn’t {i}me{/i} who did that."
    m "But if it was?"
    s "If it was, then...I would like to know why."
    m "Do her bug-eyes and horrible taste in clothing not already tip you off?"
    m "There are a million reasons to keep your distance from that girl. "
    m "And a million other reasons that I will continue to remind you of every time I see her or hear her mentioned."
    s "I’m fully prepared for that."
    s "So I will continue to do as I always do and dodge your threats in favor of an easier, more entertaining life."

    scene anotherbox20
    with dissolve

    m "Ugh...can you at least stop trying to look cool by leaning against the wall like that?"
    s "No can do. Looking cool and mysterious is kind of my thing."
    s "Just like your thing is bossing me around and pretending not to like me."
    m "I am not “bossing you around,” I’m trying to help you."
    s "Well, thanks. But if I need help, I’ll ask for it."

    scene anotherbox21
    with dissolve

    m "And if {i}I{/i} need help?"
    s "Then I’ll help you."
    m "Wrong answer. You were supposed to say you’ll leave me alone and let me handle it by myself."
    s "Oh."
    s "Well then..."
    s "I guess I’ll just do that."

    scene black
    with dissolve2

    "I finish my drink and walk Maya back to the dorm."
    "Or at least I try to."
    "She decides halfway that she wants to go back to the[school] for some reason."
    "I offer to come with her, but she turns me down and says it’s something she’d rather be alone for."
    "I don’t argue, as arguing with Maya has never once turned out in my favor."
    "Even if she loses, she just winds up coming back to the same point over and over until it wears you down."
    "The thing is, I’m not easily worn down."
    "Or perhaps I’m just so worn down already that I can’t possibly get any worse."
    "So no matter how many times she tells me to leave her alone-"
    "Or how many times she tells me to leave Noriko alone-"
    "I’ll continue to do as I please."
    "For if this world is going to end-"
    "I want to be the cause of it."

    $ renpy.end_replay()
    $ mayadorm30 = True
    $ maya_love += 1
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayadorm35:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
        if maya_love >= 15 and shrine15 == True and mayadorm15 == False:
            jump mayadorm15
        if maya_love >= 20 and shrine20 == True and yumidorm10 == True and mayadorm20 == False:
            jump mayadorm20
        if maya_love >= 25 and shrine25 == True and mayadorm25 == False:
            jump mayadorm25
        if maya_love >= 30 and mayadorm25 == True and norikoinvite2 == True and mayadorm30 == False:
            jump mayadorm30
...
```