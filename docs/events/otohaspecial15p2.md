# White People (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [King Midas](./otohaspecial15p1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Otoha: King Midas](./otohaspecial15p1.md)
* [Otoha: Breaking Character](./otohadate20.md)

## Event properties

* Id: otohaspecial15p2
* Group: Otoha
* Triggered by label: otohaspecial15p1
* Chain sources: otohaspecial15p1
* Chain sources path: otohaspecial15p1

## Official wiki page

[White People](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohaspecial15p2&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohaspecial15p2:
    scene otohapostcafe1
    with dissolve2
    play music "cafe.mp3"

    "After a long and mostly awkward walk, the three of us make it to the cafe to find things significantly busier than I have ever seen before."
    "What’s even worse is that Molly appears to be the only person working."
    "I’ll give you a few seconds to think about that."
    $ renpy.pause(3, hard=True)
    "Yeah. I know."

    mo "Uhh...okay! So, the line starts at the left and-"
    cussy1 "What’s a caramel macchiato? "
    mo "Well, it’s an espresso beverage with-"
    cussy2 "This line is taking forever. I want to speak to the manager."
    r "Oh man. I’ve seen this once before. Tourist bus."
    r "Good thing Molly’s working. She’s the only person on staff who even speaks English."
    o "Oh, right. Sometimes I forget that we’ve been speaking in Japanese this whole time."
    mo "Uhh...I’m actually the only person working right now. But if you’ll just be patient-"
    cussy3 "Did you just tell my wife to be patient?! How dare you! Now I would like to speak to the manager as well!"
    mo "Do you people even listen? I’m trying-"
    cussy4 "You people?! What is that supposed to mean?! The racism in this country is absurd!"
    mo "I’m not even Japanese! I’m European, just like you!"
    s "Why do we even have tourists? The city’s been closed for years."
    r "They all live in one giant hotel building in the Entertainment District and only leave a few times per year. Always in packs."
    s "Is this going to be a new subplot?"
    o "Can Molly really handle all of those people by herself?"
    r "Molly can barely handle one customer by herself, let alone an entire bus worth. But hey, at least they’re speaking her native tongue."
    mo "Okay! Everybody line up! I have no idea who to help first if you’re gonna come at me like this is some sort of gauntlet!"
    r "Hah..."
    cussy1 "The temperature in here is too high! Can we turn it down? "
    cussy2 "My son wants to watch TV! "
    cussy3 "I’m allergic to whipped cream!"
    mo "No, no, and...don’t get it then? Uhh...let’s see..."

    scene otohapostcafe2
    with dissolve

    r "Guys, I’m sorry. I know we came over here to cool things down and show Otoha that she {i}doesn’t{/i} have to work until her body gives out...but I’ve gotta help Molly. "
    o "Do you know enough English {i}to{/i} help? "
    r "Not really, but I’ll figure something out. I can’t just leave her hanging like this."

    scene otohapostcafe3
    with dissolve

    r "Is that okay? I’ll try and be quick. I promise."
    o "It’s fine. I’ve been alone with Sensei before and I’m somehow still alive. "
    o "Plus, I doubt he’ll try anything weird in a cafe full of white people. They {i}love{/i} calling the police."
    r "Okay. Come get me if you need me, alright?"
    s "Are we just going to ignore Otoha’s casual racism right there?"

    scene otohapostcafe4
    with dissolve

    r "Otoha, do you promise you’ll be nice to the white people while I’m gone?"
    o "As long as Sensei promises to not do anything that will make them call the police."
    s "There it is again. You can’t keep getting away with this."
    r "{i}Both{/i} of you be good. I have to go save Molly’s life. "

    scene black
    with dissolve2

    "Otoha (Who may or may not be mildly racist?) and I make our way through the labyrinth of Europeans to an unoccupied table not far from the end of the line."
    "Ideally, I would have liked sitting a little further away as it’s excruciatingly loud where we are, but it seems that every other table has yet to be cleaned —likely on account of the whole one employee thing."
    "But hey, if anyone can get Molly out of this rut, it’s Rin. "
    "Because even if she doesn’t speak the same language as all of the customers in the store right now, she {i}does{/i} know how to make a beverage."
    "It just...might not be the beverage any of those customers actually order."
    "........."
    "......"
    "..."

    scene otohapostcafe5
    with dissolve2

    o "..."
    s "..."
    s "I can’t tell if I like this new look or not."
    o "Are you physically attracted to girls who look like they just crawled out of the sewer?"
    s "Maybe?"
    o "Then you probably like this new look."

    scene otohapostcafe6
    with dissolve

    o "It’s not staying, though. I’ll be going back to normal in the morning."
    s "How come?"

    scene otohapostcafe7
    with dissolve

    o "Uhh...because this is the result of neglecting my personal health and hygiene for an entire weekend and is not indicative of a healthy lifestyle?"
    o "Also, having my bangs drop down in front of my eyes obscures my vision. I need to be able to see so I don’t...accidentally kiss the wrong girl or something."
    s "Or me."

    scene otohapostcafe8
    with dissolve

    o "Honestly, that would probably be more forgivable. "
    s "Cool, come here while she’s not looking."

    scene otohapostcafe9
    with dissolve

    o "Dude, come on. Not the time."
    s "I can’t think of a better time. I’ve barely seen you at all ever since the Dorm Wars ended. Though, that is for reasons I can’t really bring up without sounding clinically insane."
    o "Acknowledging the fact that I’ve been a complete dick to you for months wouldn’t make you sound clinically insane. It would make {i}me{/i} sound like a bitch, though."
    o "But that’s fine because I’m starting to realize that’s precisely what I am."
    s "Well, you did just slap your biggest fan in the entire world across the face with absolutely no consequences whatsoever."
    s "And you did throw a bit of a tantrum after Rin lost her trivia competition. Which is significantly more forgivable, but...still not a good look for you."
    s "And you {i}did{/i} skip out on the Christmas party for-"

    scene otohapostcafe10
    with dissolve

    o "I get it, okay? You don’t have to go and name every single thing."
    o "I’m in...this weird headspace lately that I’ve been having a lot of trouble pulling myself out of and I’ve been...kind of taking that out on the people who are around me."

    scene otohapostcafe11
    with dissolve

    o "I really {i}am{/i} sorry, though. I {i}have{/i} been wanting to say that, I’ve just had no idea how to approach you about it."
    o "I want shit to go back to normal. Or...at least whatever “normal” was for us since you’ve always been kind of a huge creep. Who has also seen my girlfriend’s boobs."
    s "They’re really nice. I won’t lie to you."

    scene otohapostcafe12
    with dissolve

    o "Right? They’re so much bigger than they look when she has her clothes on."
    s "Oh, good. I didn’t realize you two had actually made it that far yet."

    scene otohapostcafe13
    with dissolve

    o "There...have been pictures exchanged. As far as real life goes, though-"

    scene otohapostcafe14
    with hpunch

    o "Wait, why am I telling you this?! You’re my teacher! Stop me next time I go too far!"
    s "I’m not just your teacher, Otoha. I’m your {i}friend.{/i}"

    scene otohapostcafe15
    with dissolve

    o "Eww...gross."
    s "Isn’t that kind of what I was at the peak of our “normal,” though? "
    s "That’s what you want to go back to, right?"

    scene otohapostcafe16
    with dissolve

    o "I...guess. I don’t know. It just feels like things kind of shifted with us around Halloween and..."
    o "It pains me to admit this, but I’m kind of...jealous of you."
    s "Jealous? Of {i}me?{/i} Why? "
    s "You’re a hot, talented prodigy with a girlfriend who would do anything for you, a vocal coach who thinks you’re going to be a star, and attentive parents. Why would you be jealous of {i}me?{/i}"
    o "Because..."
    o "Because of Rin."
    s "..."
    o "You guys have this kind of chemistry that I can’t really figure out how to replicate. I don’t know."
    o "Maybe it’s because we weren’t ever really {i}friends{/i} the way you guys were since she’s been pining after me from the get-go."
    o "It’s not just with you either. I’ve been jealous of everyone that comes near her. Even Futaba sometimes, who is literally zero percent lesbian and not a threat at all."
    s "I don’t think Rin is going to leave you for anyone else if that’s what you’re worried about, Otoha."
    o "That’s the worst part. You’re probably {i}right.{/i} I just can’t seem to get a handle on that and keep lashing out at everyone regardless."
    o "Like, Chika fucking hates me now because she can see through that. But instead of appreciating her for caring that much about Rin, I automatically interpret it as “Chika wants to fuck her.”"
    o "And {i}you{/i} would hate me as well if you weren’t waiting to pick me up on the rebound or something because I’ve been nothing but cold to you for months."
    s "That is {i}why{/i} I like you."

    scene otohapostcafe17
    with dissolve

    o "What?"
    s "You and Yumi are pretty much the only girls in the class who see through all of the shit I do while not being afraid to point out how wrong all of it is. "
    s "I’m not going to hate you for seeing me as who I really am. "
    s "In fact, I wouldn’t hate you even if you went around and told everyone I’m having sex with Chika."

    scene otohapostcafe18
    with dissolve

    o "..."
    s "I know you know. Rin told me she accidentally spilled the details. You don’t have to play dumb. We can talk about it."

    scene otohapostcafe19
    with dissolve

    o "Gotcha..."
    s "Does it disgust you?"
    o "I need to be careful to not say the wrong thing right now because it will turn what was supposed to be an apology into...something else I’d have to apologize for."
    s "We’ve fucked probably a hundred times by now. And I have no intention of stopping — even if she’s half my age and half my size. "
    s "{i}Does that disgust you?{/i}"
    o "..."
    s "..."
    o "Do you love her?"
    s "Does it matter?"

    scene otohapostcafe20
    with dissolve

    o "{i}What are you doing, man? {/i}"
    o "If you know it’s wrong, why don’t you stop?"
    o "Dragging innocent girls down with you isn’t going to make you feel good at the end of the day. It’s just going to hurt them as well."
    s "And you want to protect Rin from that...don’t you?"
    o "I just don’t understand, Sensei. It’s not abnormal for people to {i}feel{/i} immoral shit like that from time to time, but once you start acting on those feelings...can you ever really be forgiven?"
    s "What do you think?"
    o "I think you can do better than this."
    o "In fact, I {i}know{/i} you can do better than this."

    scene otohapostcafe21
    with dissolve

    o "You’re...back together with Niki, aren’t you? Why don’t you just stay with her? "
    s "..."
    s "How did-"
    o "Because she’s happy. Like {i}really{/i} happy."
    o "She hasn’t said anything about it to me because why would she? But I can hear it in her voice. "
    s "Niki and I..."
    o "..."
    s "It’s complicated. "

    scene otohapostcafe22
    with dissolve

    o "{i}It’s only complicated because you keep running around and fucking teenage girls! It doesn’t have to be that way!{/i}"
    o "Chika’s the only one I know of, but who’s to say there’s not more?"
    s "There are."
    o "{i}Why?...{/i} "
    o "Why are you not trying to get a handle on this when it’s well within your power to do that? I don’t get it."
    s "You sound just like her sometimes, you know."
    o "Who?"
    s "Niki."

    scene otohapostcafe23
    with dissolve

    o "Oh, great. Just what I needed to hear."
    s "I mean it. I had a similar conversation with her recently and it all boiled down to the fact that I’m just...probably beyond saving at this point."
    o "You’re not beyond it, you don’t {i}want{/i} to be saved. Which is...really fucking annoying."
    o "There are tons of us out there who are struggling to keep the shitty parts of ourselves locked away and you’re just running around and flashing those parts of yourself for the whole world to see."
    o "That’s not the example you need to be setting."
    s "Am I a bad influence on you, Otoha?"

    scene otohapostcafe24
    with dissolve

    o "I think...you {i}are.{/i}"
    o "I can keep you out better than the other girls, sure- but when you’re around someone every single day, parts of that person are going to naturally start rubbing off on you after a while."
    o "Sensei, I want things to go back to normal with us...I want to be able to laugh and call you a creep the next time you barge into my room because I {i}know{/i} my girlfriend loves you. And I want to as well."
    o "But I’m afraid of what will happen to me if you stay the way you are."
    s "You don’t think...your freakout thing today was because of {i}me,{/i} do-"

    scene otohapostcafe25
    with dissolve

    o "No! No, no, no! That was a totally different thing! That’s more of the Otoha who can’t get her thoughts in order right now!"
    o "But there’s an Otoha somewhere underneath that who {i}isn’t{/i} drowning yet...and she needs someone to throw her a lifejacket instead of holding her head underwater."
    o "{i}I need help.{/i}"
    o "I really need help..."
    s "With...what? What do you need?"

    scene otohapostcafe26
    with dissolve

    o "Uhh..."
    o "So..."
    o "I know you already said you wouldn’t care if I went around telling everyone about you and Chika, but...I’m gonna pretend you {i}didn’t{/i} say that to try and like...use it as a bargaining chip for a sec?"
    s "Uhh...okay?"
    o "So, uhh..."
    o "You remember how I didn’t come to the Christmas party?"
    s "I do. And I also remember how torn up Rin was the whole time."
    o "Yeah, well..."
    o "There was a good reason for that. And by “good” I mean bad. There was a {i}bad{/i} reason."
    o "You, see..."
    o "Uhh..."
    o "While you guys were off having fun and doing...holiday stuff, I was-"

    scene otohapostcafe27 with dissolve
    with hpunch

    o "Ah!"
    r "Hi! We’re almost done. My English sucks. I just wanted to take a five second break to tell you how much I miss you and appreciate your existence on this planet."
    r "Also, I love you. And I know you don’t want to say it back yet and that’s totally cool. Also, you’re hot."
    r "Anyway, bye. "

    scene otohapostcafe28
    with dissolve

    r "Love you too, Dad. You don’t have to say it back either."

    scene otohapostcafe29
    with dissolve

    "Rin walks back up to the counter and I’m suddenly left with a significantly quieter Otoha now that our conversation has been interrupted."

    o "..."
    s "..."
    o "Hah..."
    s "What were you saying just now?"
    s "About what happened on Christmas..."
    o "..."
    s "..."

    scene otohapostcafe30
    with dissolve
    stop music fadeout 3.0

    o "It doesn’t matter."
    o "Just...stop being such a weirdo all the time, okay?"
    o "Let’s be...{i}friends.{/i}"
    o "I have to get along with you if she does. And it’s not like I think you’re the worst or anything as-is."
    s "Otoha-"
    o "I can’t handle any more today. "
    o "Please leave it at that."

    scene black
    with dissolve2

    "I leave it at that..."
    "And the day comes to an end without me ever discovering what it is she has to hide from me."

    $ renpy.end_replay()
    $ otohaspecial15p2 = True
    $ rin_love += 1
    $ otoha_love += 1

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label otohadate20:
...
```

## Code that triggers this event

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
o "I’m so embarrassed...and disappointed in myself...and so, so fucking stupid. I seriously can’t believe that just happened."
    o "And on top of that, I look like a serial killer and haven’t changed my clothes since Friday. So yeah, life’s not really coming up Otoha right now."
    r "When did this start?...And, better question, what {i}is{/i} this?"
    o "I don’t know...fucking...this just happens when I get too many...feelings, sometimes."
    o "It’s like...all I can think of is trying to write them down accurately, but then nothing ever makes sense and it drives me insane and I’ve always just...locked myself up until it was over."
    o "Just...can’t really do that anymore now that I live in a dorm with nineteen other girls. One of which I’m dating."
    o "I’m sorry you had to see me like this. Both of you. I know it’s not pretty."
    s "Well...you seem a little better now. But maybe it’d be for the best if you took a little break from writing to just...cool down or something?"

    scene otohasnewhair31
    with dissolve

    o "Cool down?! Now?! But I’m so fucking close to-"
    r "Otoha."

    scene otohasnewhair32
    with dissolve

    o "Yeah...you’re right. Sorry. I’m still kind of...caught up in the...colors...Uhh...no...No, thats not the right way to word it. Uhh...fuck. Give me a second."

    scene otohasnewhair33
    with dissolve

    r "This new song you’re writing..."
    r "It’s not about me...is it?"

    scene otohasnewhair34
    with dissolve

    o "Uhh..."
    o "I don’t...I don’t really like talking about my songs until they’re done, so..."
    r "Will you let me hear it once it’s finished?"
    o "..."
    o "Y-Yeah. Totally. You can...hear it...when it’s done. That’s fine."
    r "I’m looking forward to it..."
    o "..."
    r "..."
    s "Well...I should probably leave you two alone now that Rin is no longer at risk of being mutilated by her lover."

    scene otohasnewhair35
    with dissolve

    r "I wouldn’t mind having a bodyguard for the rest of the night now that it looks like Otoha doesn’t need to be alone anymore."
    o "I’d still...kind of like to be alone..."

    scene otohasnewhair36
    with dissolve

    r "But it would make me {i}reeeeeeeally{/i} happy if we could all go to the cafe together. And I could definitely use the pick me up after all I’ve been through tonight."

    scene otohasnewhair37
    with dissolve

    o "That’s mean...you know I can’t say no to you right now."
    r "Just for a little while? I’ve wanted to see you all weekend and I’d hate for this to be the way that ended."
    o "Are you...okay with me looking like this, though? Because I don’t really think I can do my makeup right now. My hands are all {i}blah{/i} from writing and erasing things all day."

    scene otohasnewhair38
    with dissolve

    r "Leave it to me! Years of self-mutilation have made me into a wizard with makeup and I have been practicing to one day apply my girlfriend’s since elementary school!"
    s "Welp, once again, I’ll leave you to it and-"

    scene otohasnewhair39
    with dissolve

    r "Nonsense! You’re coming too!"
    s "{i}Why?{/i}"

    scene otohasnewhair40
    with dissolve

    r "Because I don’t want this to be {i}your{/i} final memory of the weekend either. Let’s just all have some fun the way we normally do and put all of this drama behind us. Cool?"
    r "Barring Futaba, all my favorite people are here with me right now. And nothing would make it easier to put this all behind us than overpriced, caffeinated beverages I will receive at a discounted rate."
    o "I can’t have dairy..."

    scene otohasnewhair41
    with dissolve

    r "Soy milk exists. Now stop trying to make up excuses and go sit on the bed so I can make you look presentable. "

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I wind up walking around the room as Rin “fixes” Otoha to collect the shards of broken glass from things  that she and Nodoka have decided weren’t important enough to preserve."
    "I can’t help but contort my worldview until pieces of Rin are scooped into my hands alongside the shards. "
    "Is {i}she{/i} worth preserving in the eyes of someone who nearly shattered her just moments ago?"
    "Or will she eventually slip through Otoha’s fingers as part of another unfortunate “accident?”"
    "That remains to be seen."
    "And hopefully next time, I won’t be around for it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ otohaspecial15p1 = True

    jump otohaspecial15p2
...
```