# Young At Heart (Osako)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Osako love greater than or equal to 15

* Event [Don't Hold Back](./wakanaspecial15.md) (Wakana) is completed)



## Next events

* [Osako: House of the Unholy](./osakodate20.md)

## Event properties

* Id: osakodate15
* Group: Osako
* Triggered by label: utamaid
* Triggered by branch label: utamaid
* Triggered by path: utamaid->osakodate15

## Official wiki page

[Young At Heart](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=osakodate15&go=Go) for more details.

## Event code

File: (install folder)\game\OsakoEvents.rpy

Code:
```python
...
label osakodate15:
    scene osakokaraoke1
    with fade
    play music "maidcafe.mp3"

    os "..."
    s "..."
    os "..."
    s "..."
    s "You are not the maid I asked for {i}or{/i} wanted."
    os "Tough shit, because I’m the maid you got. You think I’m any happier about this than you are?"
    s "You should be, as I’m pretty sure that’s what you’re being paid for."
    os "Bite me."
    s "Here is my first command. I demand a shorter maid whose name starts with the letter “U” and ends with “ta-chan.”"

    scene osakokaraoke2
    with dissolve

    u "I’m sorry, Master! But little ole’ U-to the-ta-chan’s totally booked up at the moment! Can’t you do her a big favor and settle for Osako-chan just this once?"
    u "So long as she’s wearing that uniform, you don’t have to worry about her putting you in an ankle lock or whatever the heck it is they do in karate."
    s "Is that true, Osako? Am I safe here?"
    os "Depends on how many of my buttons you manage to push."
    s "Which ones am I {i}allowed{/i} to push?"
    os "Not whichever one you’re trying to push right now."
    u "Jeez. Get a room, why don’t ya?"

    scene osakokaraoke1
    with dissolve

    "I wind up at the maid cafe- a place I probably wouldn’t have bothered coming to if I had known I was going to be partially ignored by my favorite employee."
    "Please don’t tell Ami I said that."
    "Anyway, due to word finally starting to get around about this place and the increase of business brought on by summer, I have found myself in the company of another employee who, while good, is no Uta-chan."
    "Thankfully, I don’t think I’ll have to deal with her for very long as the cafe should be closing in about thirty minutes or so."
    "Which is just enough time for me to test this maid’s abilities and see how much she has grown now that she has accepted this as a second near full-time job."
    "Even if it’s a job I’m pretty sure she’s only keeping to satisfy some sort of sexual desire."

    s "You know, I haven’t heard you call me “Master” today. Do I need to file a formal complaint?"
    os "Do I need to formally file my foot in your ass?"

    "She fails the maid test almost immediately."

    s "Can you at least do the thing?"
    os "What thing?"
    s "The thing Uta-chan does to make sure my food tastes delicious."
    os "The flavor beam?"
    s "Yeah. Not to be confused with the death beam- another move I have recently learned that she has."

    scene osakokaraoke3
    with dissolve

    os "Bzzzzzt. "
    os "Your food tastes better now."
    s "You don’t even have a cool rhyme to go along with it?"

    scene osakokaraoke4
    with dissolve

    os "Man, I brought you your damn omelet. Do you really have to spend the rest of your time here trying to get a rise out of me?"
    s "I know it might seem like that’s my goal here, but what I’m {i}really{/i} trying to do is help you. You know, like how you help me with karate."
    os "You have made a total of two or three attempts out of what feels like thousands to actually learn anything inside of the dojo."
    s "And you’ve made how many attempts here?"

    scene osakokaraoke5
    with dissolve

    os "I make plenty of attempts with the other guests. There’s just something about the idea of acting that way to you that makes me throw up in my mouth a little."
    s "If you’re a decent maid when it comes to everyone else, how come I’m the only one you’re serving right now while Uta-chan is busy with literally every other table?"
    os "Just because I’m okay doesn’t mean I can compete with somebody who’s not only way younger, but way more experienced when it comes to this sort of thing."
    os "If I was still a teenager, I guarantee you I’d have more than one table right now. But unfortunately,  life has gone on for me and I must now deal with customers like you who only want cutesy girls."
    s "You’re cute in your own way."

    scene osakokaraoke6
    with dissolve

    os "Oh yeah? And what way is that?"
    s "The way that if I ignore your face and only look at your body, I can pretend that you’re still just as young as Uta."
    os "You need professional help."
    s "What I need is a better maid."

    scene osakokaraoke7
    with dissolve

    u "Are you two in love yet? Or is Osako-chan still a full fledged lesbian?"
    os "Still a lesbian, but thanks for checking. Especially since everyone knows that’s the sort of thing that can just change whenever I want it to."
    s "If Uta-chan can train herself to stop being sexually attracted to sea creatures, I believe that anything is possible."

    scene osakokaraoke8
    with dissolve

    os "To...what?"
    u "So anyway! Ignoring what Sensei just said, do you want to actually come to karaoke after work today?"
    u "You made the mistake of telling me Miss Watabe is feeling under the weather earlier, so you have no excuse to back out on me this time!"
    os "Is caring for my ailing girlfriend not good enough of an excuse?"
    u "Not when there are songs that need to be sung, it’s not! My grandpa that I used to care for would agree with me if he could but, unfortunately, he-"
    os "Yup. He’s dead. You don’t have to remind me every shift, you know."
    s "I wouldn’t bother inviting Osako. She’s made it clear that she’s already past the prime of her life and can’t really do what young people do anymore."

    scene osakokaraoke9
    with dissolve

    os "I’m still younger than you, you know! Stop making it sound like I’m on my death bed just because I mentioned being pretty and perkier during my high school years!"
    u "Do you want to come too, Sensei? The more the merrier! Plus, having a chaperone might prevent the two of us from winding up on the floor again!"

    scene osakokaraoke10
    with dissolve

    os "You’re so much better than him. Why would you ever put yourself in a situation where he can tackle you to the ground?"
    u "What if I’m the one who tackled him?"
    os "That-"

    scene osakokaraoke11
    with dissolve

    os "Actually, that tracks. I’ve seen firsthand how weak this guy is. I think Uta could probably take you down on a good day."
    os "I don’t really understand why she {i}would{/i} when she’s like four leagues ahead of you, though."
    s "Uta-chan, I don’t want Osako-chan to come to karaoke with us. She’s really killing the vibe right now."
    os "If you’re trying to sound young, it’s not working."
    s "You’re one to talk, being so far out of your prime and all."
    u "Master, you’re going to have to speak a little louder if you want grandma Osako to hear you. Her ears ain’t what they used to be."

    scene osakokaraoke12
    with dissolve

    os "Screw it! You want me to come?! Fine! I’ll show both of you I‘m still young at heart! And when I’m done with that, I’ll work on stealing some of your regular customers!"
    os "Just because I’m not your age anymore doesn’t mean I’m invalid! There’s still demand for people like me! "
    s "Maybe at the local retirement home. "

    scene osakokaraoke13
    with dissolve

    os "Again, I am {i}younger{/i} than you!"
    u "Yeah, but Sensei passes the vibe check. And the only kinda vibe Osako-chan knows is the one she uses on Miss Watabe."

    scene osakokaraoke14
    with dissolve

    os "That’s it! Osako-chan, special move! Double-fisted death beam!"
    u "Osako-chan, no! You’re still not ready! You could hurt yourself!"
    s "Those aren’t even fists."
    os "Shut up, shut up, shut up! Just die already!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Uta and I manage to survive the double-fisted death beam (With no actual fists involved) and make it through the rest of the shift without issue."
    "And, being dead set on proving that she is not a “grandma” like Uta suggested, Osako remains true to her word and joins the two of us for a trip to the karaoke bar once the maid cafe closes."
    "Upon arrival, Uta books us a room and, before Osako and I are even able to sit down, she has already booted up the machine and begun singing her first song..."
    "........."
    "......"
    "..."

    play music "utasings.mp3"
    scene osakokaraoke15
    with dissolve2

    os "I barely know any of these songs."
    s "Nothing from back when you were young?"
    os "You mean less than ten years ago? Not sure."
    os "I might recognize some of them if I got to listen to them first but, based on titles alone, I don’t really recognize any of these."
    s "Not a music person?"
    os "Not really. All my free time in high school went toward karate. And all my free time in college went toward Wakana- who isn’t much of a music person either."
    os "We never really did stuff like this. That was more of a...popular girl sort of thing."
    s "Neither one of you strike me as the “popular” type, so that makes sense."

    scene osakokaraoke16
    with dissolve

    os "Yeah...well you don’t seem like you were all that popular either, smartass."
    os "Guess you’re right, though. I was never {i}unpopular{/i} or anything. I actually had a good amount of friends in high school, but they were all, like...club friends. Not people I spent any free time with."
    os "College was totally different. As soon as I started seeing Wakana, I barely even {i}talked{/i} to anyone else anymore. But I never really cared about that since I had her."

    scene osakokaraoke17
    with dissolve

    os "Probably goes without saying, but she was always a bit of an outcast. You can’t really look the way she does and expect {i}not{/i} to be."
    os "But one of my favorite things about her is...that never really seemed to be an issue for her."
    os "She did what she wanted and didn’t care about what anyone else had to say about it."
    os "I still love watching her do that today. And I love how...non-judgemental she is when anyone else wants to do their own thing as well."
    s "She judges {i}me{/i} all the time."
    os "You’re a grown man hanging out with teenage girls. She’d be a bad person if she {i}didn’t{/i} judge you for that."
    os "But if you randomly took up some niche hobby like...painting models or articulating animal skeletons, I doubt she’d think you’re weird for it."
    os "Actually, she’d probably like the skeleton one. That seems like a very {i}Wakana{/i} thing."
    s "Do you ever worry that you might be basing too much of your current self on her?"

    scene osakokaraoke18
    with dissolve

    os "What do you mean?"
    s "It just sounds kind of like you stopped existing as {i}Osako{/i} once you met her. Now you’re just {i}Wakana’s{/i} Osako. "
    os "That’s not true. I still have plenty of interests that I don’t share with Wakana."
    os "At the same time, though, why would being {i}Wakana’s{/i} Osako rather than just {i}Osako{/i} be a problem if that’s what makes me happy?"
    s "It’s not at the moment. But if something ever happened to her, what would that mean for you? "
    s "Aren’t you afraid of the possibility of losing the one thing that makes you {i}you?{/i}"
    os "Of course. It’s my greatest fear of all. "
    os "But fear is something that is meant to be confronted, not avoided."
    os "I’m not going to change who I am based on “what ifs” when the person I am today, codependent or not, is the happiest version of myself I’ve ever been."

    scene osakokaraoke19
    with dissolve

    os "All this...stereotypical “fun stuff” that other people do has just never really been a factor for either one of us. So it’s not like we’re even missing out on anything."
    os "In a way, the fact that she's always been so focused on living for {i}herself{/i} has helped me validate the way I've always felt in the back of my mind."
    os "It was always a little weird to me that I never felt regret or remorse for spending time on my training when others would ask me to come hang out with them."
    os "It’s like...I {i}wanted{/i} to feel bad since I knew I was letting people down...But I didn’t really have the {i}time{/i} to feel bad since it would just distract me."
    s "How is that any different from how you feel now? What changed?"
    os "What changed is I don’t {i}want{/i} to feel bad anymore."
    os "If somebody gets bogged down by me not coming along with them, that’s on them- not me."
    os "Parents...friends...family..."
    os "We worry so much about what everyone around us thinks that we often forget to think for ourselves. Life is so much better once you learn to just...leave all that behind."
    s "If that’s true, how come you get so offended every time we make fun of you for not being young anymore?"

    scene osakokaraoke20
    with dissolve

    os "Because I know you’re wrong and that I could blindfold myself and {i}still{/i} kick both of your asses as the same time."
    s "That’s even more worrying since I know there must be at least five blindfolds inside of your apartment."
    os "One for every weekday."
    u "Aaaand done! Your turn to show off your pipes, Osako. I know that following the great Uta-chan is no easy task, but I’m sure that if you try your best, you-"

    scene osakokaraoke21
    with dissolve

    os "Yeah, yeah, yeah. Just shut up and listen, Uta."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "Osako finally finds a song she recognizes and takes the mic from our self-proclaimed MC’s hands."
    "Before I can blink my eyes, their places are swapped. But instead of my gaze landing on the girl it almost always lands on, it gets caught on a nail hanging off of the main stage."
    "And it cuts me deeper than the ones I routinely walk on."
    "........."
    "......"
    "..."

    scene osakokaraoke22
    with dissolve2
    play music "hallelujah.mp3"

    u "Osako, what the heck? This song isn’t fun at all."
    os "Shut up. It’s the only song I recognized the name of and I don’t care if you like it or not."
    u "It’s not that I don’t {i}like{/i} it. It’s just that...well, you know! It seems like something my grandma would sing if she wasn’t knockin’ boots with my grandpa up in Heaven."
    s "Just let her sing, Uta. Your songs are always too energetic for me anyway."
    u "Ugh! What’s a girl gotta do to get some excitement up in here?!"

    "Osako takes a deep breath..."
    "And then slowly opens her mouth..."

    scene osakokaraoke23
    with hpunch

    os "I'VE HEEEEEARD THERE WAAAAAS A SECRET CHORD!!!! "
    os "THAT DAAAAAAVID PLAYED AND IT PLEEEEEASED THE LORD!"
    os "BUT YOOOOUUUU DON’T REAAAAALY CARE FOR MUSIC...DO YOU?!?!?!?!"

    scene osakokaraoke24
    with fade

    os "IT GOOOOOOES LIKE THIS...THE FOURTH...THE FIFTH!!! "
    os "THE MINOR FALLS, THE MAJOR LIFTS!!!!!!!"
    os "AND DAA DA DAAA DA DAAA DA HAAAAALLELUUUUUJAH!!!!"
    u "..."
    s "..."
    u "I’ve gotta go return some video tapes."
    s "I’ll come with you."

    scene black
    with dissolve2

    os "HAAAAALLELLUUUUJAH! HAAAAAALLLELUUUU- Wait, where are you guys going? I thought Uta was singing again after this?"
    u "Sensei, split up! She can’t catch both of us!"
    os "Wha-"
    os "Get back here! I haven’t even finished yet!"

    $ renpy.end_replay()
    $ osakodate15 = True
    $ osako_love += 1
    $ uta_love += 1
    stop music fadeout 10.0

    "{i}Osako’s affection has increased to [osako_love]!{/i}"
    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label osakodate20:
...
```

## Code that triggers this event

File: (install folder)\game\UtaEvents.rpy

Code:
```python
...
label utamaid:
    if uta_love >= 0 and day247 == True and utamaid1 == False:
        jump utamaid1
    if uta_love >= 5 and utamaid1 == True and day > 5 and utamaid5 == False:
        jump utamaid5
    if uta_love >= 10 and dormwar17 == True and utamaid10 == False:
        jump utamaid10
    if uta_love >= 20 and bathhouse20part2 == True and utadorm15 == True and utamaid20 == False:
        jump utamaid20
    if uta_love >= 25 and utaarchery1 == True and utamaid25p1 == False:
        jump utamaid25p1
    if osako_love >= 15 and wakanaspecial15 == True and osakodate15 == False:
        jump osakodate15
...
```