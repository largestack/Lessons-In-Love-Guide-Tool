# Self Care (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 40

* Event [In Search of Summer](./chikaspecial40.md) (Chika) is completed)



## Next events

None

## Event properties

* Id: mall40
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall
* Triggered by path: mall->mall40

## Official wiki page

[Self Care](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mall40&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall40:
    scene chikashopping1
    with fade
    play music "mall.mp3"

    "I head to the mall for the afternoon and, like clockwork, Chika immediately finds me and makes her way over."
    "Surprisingly enough, she’s able to abstain from grabbing onto me and actually shows some restraint this time."
    "And all it took was making her think I was about to break up with her."
    "It’s funny how people are willing to change once you threaten to take away the things they love."
    "And it’s even funnier when you don’t even have to get the full threat out of your mouth in order to do that."
    "Anyway, here’s hoping I don’t have to break her heart again today in order to get her to act how I want."

    c "Hey! Great timing."
    s "Leave it to me to show up right when you clock out for break."

    scene chikashopping2
    with dissolve

    c "Actually, I’m not even working today. "
    s "Did you get fired after customers complained about the adult male constantly hanging around the store hitting on you?"

    scene chikashopping3
    with dissolve

    c "I don’t really think that’s something I would get fired for. If anything, people would probably just call the cops thinking you’re harassing me."
    s "Fair point. If you’re not fired, though, why bother spending time at the mall? Don’t you see enough of this place?"

    scene chikashopping4
    with dissolve

    c "Coming to the mall as an employee and coming to the mall as a customer are two completely different things, Sensei."
    c "You probably just don’t understand because you wear the same thing every day."
    s "But...so do-"
    c "Anyway, I came here with Yumi and Chinami, but the two of them are off doing something else right now."
    s "Well, why aren't you with them?"
    s "You weren’t wandering around in hopes that I’d just show up, were you?"
    c "I mean, I’m kind of always hoping you’ll show up. But nah, I’m just shopping."
    s "Since when do you have the money to shop?"
    c "Since you started paying for my phone, obviously. Plus, I’ve been picking up a lot more hours since it’s getting close to Christmas."
    c "So, I figured why not treat myself to a little present?"
    s "Hmm..."

    scene chikashopping5
    with dissolve

    c "Why {i}hmm?{/i} What did I do this time?"
    s "I just figured you’d be using that money on stuff for Chinami."

    scene chikashopping6
    with dissolve

    c "I...I am! I just wanted to get something for myself, too! "
    c "What’s wrong with a little self care to make yourself happy every once in a while?"
    s "Well, nothing’s {i}wrong{/i} with it. You’re free to use your money however you want."

    scene chikashopping7
    with dissolve

    if bonus == True:
        c "Good. Because I’m tired of seeing Noriko and Touka with their fancy underwear in the locker room. It’s making me feel like some kind of...lower class blob."
        s "If it’s any consolation, I think you look great in your-"

        scene chikashopping8
        with dissolve

        c "No! I want to feel sexier!"
        s "Why? I’m pretty sure that neither of those girls are looking down at you for not being able to afford the things they can."
        s "Who cares about what they think?"

        scene chikashopping9
        with dissolve

        c "It’s not {i}just{/i} about what they think."
        c "I wanted to like, you know...surprise you and stuff."
        c "And even if like, nobody else can see what I’m wearing under my clothes, having something nicer under there would make me feel...more desirable and stuff."
        c "I don’t know. It’s probably dumb."
        s "Nah. I get it now that you’ve explained it like that."
        s "Plus, this finally gives me the chance to see you modeling lingerie for me, and I have been waiting for that for a very long time."
    else:
        c "Good. Because there's this one clown costume I really like and-"
        s "Say no more. Let's go."

    scene chikashopping10
    with dissolve

    c "Really?! You’ll come with me?!"

    if bonus == True:
        s "Are you really that surprised that I’m agreeing to come see you with less clothing on? Because that’s one of my absolute favorite things to do."
    else:
        s "Are you really that surprised that I’m agreeing to come see you in a clown costume? I've been trying to do this for ages."

    c "I’m not really surprised at all. I’m just happy. "

    scene chikashopping2
    with dissolve

    c "Plus, it means I can finally show you something I’ve been keeping a secret for a little while now."
    s "That is...both alluring and mildly suspicious?"
    c "It’s nothing huge- just something I’ve wanted for a long time that I finally pulled the trigger on."

    if bonus == True:
        c "Now, hurry up and follow me if you want to see me in my underwear."
    else:
        c "Now, all aboard the Chika express if you're ready for a honkin' good time."

    scene black
    with dissolve2

    s "What, are we not just going to the store you work at?"
    c "Not today. There’s a sale at this other place on the opposite end of the mall and I want to check out what they have."

    "Chika tries to reach for my hand, probably out of instinct, but manages to catch herself before following through with it."
    "I’m sure it’s a weird position to be in for her- like she’s being pulled in two different directions at once."
    "On one hand, I’m constantly telling her to be careful about giving ourselves away and doing everything in our power to keep this a secret..."

    if bonus == True:
        "But, on the other hand, I’m now following her through a semi-crowded mall during the holiday season in an attempt to watch her try on new underwear."
    else:
        "But, on the other hand, clowns."

    "I’m a little annoyed at myself for this, but I ultimately choose to stop caring for at least a little while."
    "Eventually, Chika leads me into a store that definitely does not sell anything for men and starts browsing through a few racks of clothing."
    "She quickly dismisses most of the stuff she sees, and in the process of doing so, I can make out some of the price tags."
    "I breathe a sigh of relief knowing that it’s nothing expensive and that she isn’t just throwing away her money to try and impress me."
    "And I don’t know if her pride is just too strong to admit it, but I’m willing to put money on the fact that she’s only here because the sale they’re having is making everything semi-affordable."
    "I guess there’s no point in putting money on anything when there’s no chance for a return, though."

    scene chikashopping11
    with dissolve2

    "In fact, with the way Chika is looking at me, I’m beginning to think that there might be money to be {i}lost...{/i}"

    s "..."
    c "..."
    s "What? Why are you looking at me like that?"
    c "Like what?"
    s "Like you’re trying to seduce me."

    if bonus == True:
        s "You know we’re past that, right? Seduction serves no purpose anymore. I’m already very attracted to you."
    else:
        s "I have no interest in that sort of sinful relationship."

    c "Oh yeah?"
    c "Then, before I try stuff on, I’d like to make you a little trade offer."

    "Here it comes- the inevitable loss of income."

    if amifingered == True:
        "I hope Ami never learns this trick."

    c "So...I found something that I really like, but it’s a little out of my price range."
    s "..."
    c "And what I was thinking was..."

    scene chikashopping12
    with dissolve

    c "You could maybe buy it for me?"
    s "..."

    if bonus == True:
        s "Is there another end to this trade? Or are you just asking me to buy you underwear for nothing in return?"
    else:
        s "Is there another end to this trade? Do I get anything?"

    scene chikashopping13
    with dissolve

    if bonus == True:
        c "If you buy it for me, I’ll let you fuck me in the dressing room."
    else:
        c "If you buy it for me, I’ll let you hug me while I'm wearing it."

    s "..."
    c "..."

    "You know, this is starting to sound like a pretty good investment after all."

    s "Fine, but..."
    c "But what? "
    c "Nervous that we’ll get caught?"
    s "I think that’s a pretty reasonable thing to be nervous about."

    scene chikashopping14
    with dissolve

    c "It’ll be fine. The girl working here still owes me a favor from when I gave her a tampon."
    s "I feel like you’re getting a much bigger favor out of this than she did."
    c "It was a while ago, so I’ve accrued interest or whatever. "
    c "So, what do you say? "
    c "Wanna do it?"

    if bonus == True:
        c "It’s pretty cramped in there, so you’ll probably have to fuck me up against the wall, though."
    else:
        c "It’s pretty cramped in there, so you’ll probably have to hug me really tightly, though."

    s "Oh no. However will I survive?"

    scene chikashopping13
    with dissolve

    c "Heheh~"
    c "Who says you will?"

    scene chikashopping15
    with dissolve

    s "..."
    s "Chika, that’s a really weird thing to say before luring me into a private room."

    if bonus == True:
        jump mall40x
    else:
        scene black
        with dissolve
        stop music fadeout 8.0

        "Chika pulls aside the curtain to the dressing room, but it is filled with chickens and there is nowhere for her to put on the clown costume. She says the shoes are too large."
        "Not knowing what else to do, we decide to play with the chickens for a little while. But then Yumi and Chinami show up and we have to stay quiet because we want to keep the chickens to ourselves."

        jump mall40p2

label mall40p2:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
    if chika_love >= 5 and mall5 == False:
        jump mall5
    if chika_love >= 10 and mall10 == False:
        jump mall10
    if chika_love >= 15 and chikadorm15 == True and day79 == True and mall15 == False:
        jump mall15
    if chika_love >= 20 and chikadorm20 == True and mall20 == False:
        jump mall20
    if chika_love >= 40 and chikaspecial40 == True and mall40 == False:
        jump mall40
...
```