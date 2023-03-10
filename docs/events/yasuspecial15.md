# Sore Thumb (Yasu)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 500

* Event [Life is Changing](./chapthree8.md) (Main) is completed)

* Event [Down The Rabbit Hole](./church15.md) (Yasu) is completed)



## Next events

* [Yasu: Mother Duck](./church20.md)

## Event properties

* Id: yasuspecial15
* Group: Yasu
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->yasuspecial15

## Official wiki page

[Sore Thumb](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yasuspecial15&go=Go) for more details.

## Event code

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label yasuspecial15:
    scene yasugenres1
    with dissolve2
    play music "summerwind.mp3"

    "It’s a completely normal and peaceful day in my office."

    play sound "dooropen.mp3"
    scene yasugenres2
    with dissolve

    "Nevermind."

    mo "Sir!"
    s "What, Molly?"
    mo "The three of us require your assistance! Or...guidance! Or something!"
    s "Why? Aren’t you supposed to be at your club right now?"
    f "This actually...is our club activity for the day. We’re teaching Yasu about manga."
    s "I see."
    s "Just so we’re all on the same page here, you guys know I that I am pretty much entirely unfamiliar with manga, right?"
    mo "Aye!"
    s "And that asking me for help with this is essentially pointless because of that."
    mo "Aye!"
    s "Okay, cool. I just wanted to make sure."
    f "So...you’ll come with us, then?"
    s "I’m not sure. Why not leave my involvement up to Yasu? You know, since her new thing is apparently just ghosting on me without a care in the world."

    scene yasugenres3
    with dissolve

    ya "Ghost?"
    mo "Oof. That sort of crit would take most other people out in one shot, Sir. I’m surprised you’re still able to stand up after that."
    f "You and...Yasu have been spending time together?"
    s "If by spending time with her you mean her offering me eggs and then immediately leaving in the middle of conversations, yes."
    f "That’s not...really what I meant, no."

    scene yasugenres4
    with dissolve

    ya "I’m sorry, but...I don’t remember this at all."
    s "You don’t remember having a “summer celebration” with a bunch of rabbit dolls in that weird cathedral and drinking tea made from back alley leaf litter?"
    ya "I remember the celebration, but I don’t remember your presence."
    ya "Which made me very sad since I brewed extra tea for you."

    scene yasugenres5
    with dissolve

    f "Wait...you...drank tea made of leaves you found on the ground?"
    ya "Special leaves that the one with many eyes blew onto the sacred asphalt behind the place He falls asleep at night."
    mo "Are we going to ignore the “party with rabbit dolls” part? Or is that something we just expect out of her ghostliness at this point?"
    s "Wait, Yasu- do you really not remember me being there?"

    scene yasugenres6
    with dissolve

    ya "I waited so long for you that Touka sent one of her fancy cars to come pick me up so I wouldn’t have to walk home during what she called the “witching hour.”"
    ya "Now, you’ll have to wait until next summer for divine protection."
    mo "Or just find yourself a paladin. Which, not gonna lie, is far easier said than done, Sir."
    s "I’ll be fine without “divine protection.” What I’m more concerned about is the fact that I now have memories of a thing that apparently never happened."
    mo "Perhaps this is just some sort of dream you’re remembering, Sir? Yasu doesn’t seem like the type to cast {i}vanish{/i} in the middle of casual conversation."
    s "Maybe. It’s just weird that I’d also remember the names of her stuffed rabbits."

    scene yasugenres7
    with dissolve

    ya "The rabbits do not belong to me. They belong to everyone."
    ya "They are His ears...and carry forth the whispers too soft for Him to hear on His own."
    ya "All shapes and all sizes. "
    ya "All forms and all colors."

    scene yasugenres8
    with dissolve

    ya "Except red."
    ya "Red is bad."
    mo "I take great offense to this."
    s "Well, I don’t really remember what colors or sizes they were...but does the name “Wormwood” ring a bell?"

    scene yasugenres9
    with dissolve

    mo "Aye! That’s a card from the World of Warcraft TCG that allows you to put a target ally into-"
    ya "Yes! Wormwood is an emissary! One who carries all sorts of information about the history of the church! "
    mo "Yeah! Or that!"
    ya "I am glad you remember him!"

    scene yasugenres10
    with dissolve

    ya "But I don’t understand how that would be possible. He only appears to me on special occasions and you were not at the celebration."
    s "I’m telling you I was, though..."
    ya "Did you drink the tea?"
    s "No. I-"
    ya "You should have drank the tea. It is possible your body was detached from your mind as a result of your failure to do so."

    "Or it’s possible that Yasu is insane and simply doesn’t remember the fact that we had an entire conversation about her god at a table full of stuffed animals."
    "I guess that wouldn’t really explain the sudden vanishing of them, though..."
    "But it’s entirely possible I just lost track of time again. It obviously wouldn’t be the first time something like that happened."
    "And it sure as hell makes a lot more sense than vanishing rabbits or the sudden introduction of “amnesia” to the list of mental issues Yasu likely needs to be professionally diagnosed with."
    "I do feel a little better knowing that there was no conscious decision to ghost me, though."
    "And I guess it’s fine to prioritize that over the idea of false memories because, let’s face it, I’ve become a bit of an expert when it comes to memory related issues."
    "Just don’t tell that to Maya or she’ll probably get sad and reflective."

    f "Yasu...I really don’t think you should be making tea out of things you find on the ground..."

    scene yasugenres11
    with dissolve

    ya "You would change your mind if you had some. It is the cure for all things and would quell the sadness in your heart that eats away at your innards like carrion birds."
    f "The feeling you’re describing sounds...more like a virus you may have gotten from-"
    mo "Can we stop talking about carrion birds and tea leaves and get back to the topic at hand? "
    mo "We’re here to enlist Sensei’s help for Yasu’s reeducation process, aren’t we?"
    s "Reeducation process?"

    scene yasugenres12
    with dissolve

    ya "I am broken beyond repair and these two wonderful and helpful girls are going to help fix me."
    f "We’re not going to {i}fix{/i} you, Yasu...We just want to help you figure out what type of manga you like since you’ve never read any and...have decided to join the manga club despite that."
    mo "Shh. Stop. Don’t say anything that might make her question her decision. We need every member to stay in the club or we’ll all wind up in costumes at Sensei’s house."
    ya "That sounds delightful."

    scene yasugenres13
    with dissolve

    f "No...that sounds very embarrassing..."
    s "As supportive as I am of the idea of everyone coming over to my house and putting on cosplay, I still don’t understand how I am supposed to help Yasu figure out what kind of manga she likes."
    s "Especially when I don’t even know what kind of manga {i}I{/i} like."
    mo "As the club advisor, that is probably something you should know, Sir."
    s "As the club president, you should be off doing your job instead of dragging me into it as well."
    mo "But, Sir! If I’m not annoying you every hour of every day, what purpose do I even have?"
    s "Have you been talking to Io lately?"
    mo "Sir. {i}No one{/i} has been talking to Io lately."
    s "You know what? That’s fair."
    ya "I like her hair. It reminds me of the grass."

    scene yasugenres14
    with dissolve

    f "Sensei...the reason we need your help is less of an actual {i}need for help{/i} and more the fact that...Yasu seemed upset that you weren’t going to be at club."
    s "What? Really?"
    ya "Summer can only do so much for the sounds I hear. Having you nearby makes them even clearer. "
    mo "Did you hear that, Sir? Are you really going to say no to a line as cute as that?"
    s "Yes."
    mo "Strike that. Are you really going to say no to a line as cute as that {i}knowing that Yasu will also be in cosplay?{/i}"
    f "In addition to wanting you there...Yasu was also upset that we weren’t dressing up today..."
    s "See, this is a detail that should have been revealed from the start. This changes everything."
    ya "I hope that you are not repulsed by the sight of a worm in beautiful clothing. "
    ya "If you are, just close your eyes. You need not see for me to feel your presence. But you must be present for me to see. "
    ya "Do you see?"
    s "No. But I’m not about to try and figure it out when I know that something much more interesting than this awaits in the club room."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    s "Okay. Everybody out. Come on."
    mo "Quest complete! Fantastic job, Yasu! "
    mo "Remind me to come up with a nickname for you as soon as possible. You’ve earned it."
    ya "I have earned nothing but a life of servitude for-"
    f "Oh, look. We’re here..."

    scene yasugenres15
    with dissolve2

    f "Sensei...you can wait out here with me while Molly helps Yasu get changed..."
    mo "I hope you like crimson demons, Sir. Because what you’re about to see is bound to make you {i}explode.{/i}"
    ya "Demon? But demons are bad. I don’t want to be a demon."

    scene yasugenres16
    with dissolve

    mo "Well...the name is more of a technicality than anything. The character is basically just a fire mage."
    ya "But warlocks and mages are also enemies of God. "
    ya "Do you have anything with wings?"
    mo "Uhh...not on hand, no. But you’ll be fine. It’s just pretend, okay?"
    mo "Now, get in there and start stripping. We don’t want the Herald of the Adolescents waiting too long, do we?"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "Molly shoves Yasu into the club room and Futaba lets out a hearty sigh, showcasing just how exhausting the introduction of everyone’s favorite cult member to their friend group is."
    "She tells me a little about how she expected things to settle down after Rin left. "
    "But apparently, having someone completely new to the nerd world around has awoken something in Molly that she is having trouble containing."
    "And while I’d like to talk about how I’m sure this is all just temporary and that Yasu will adjust and Molly will settle down in no time at all, both of those things are obviously untrue."
    "In fact, I can’t fathom {i}any{/i} scenario where Yasu doesn’t stick out like a sore thumb."
    "But I’m glad she’s trying. "
    "Even if her efforts are currently resulting in her being dragged around like a puppy on a leash by a small Irish girl."
    "Even before that, though, Yasu was already on a leash."
    "She probably has been for a very long time now."
    "We should be happy that we can see what this new one is attached to."
    "........."
    "......"
    "..."

    scene yasugenres17
    with dissolve2

    mo "Ta-dah! Yasumin! "
    mo "And it only took me one night to adjust the costume for her size!"
    mo "Yasu! Say the line!"
    ya "Boom!"
    mo "Close enough!"
    s "I’m not sure if it lives up to the one from the dorm wars, but I accept and appreciate this greatly and thank all of you for allowing me to be involved."
    mo "Don’t thank us, Sir! Thank Yasu for her ideal cosplay figure and extremely unique and only mildly creepy aesthetic."
    ya "Do I look like a real manga character now?"
    s "Sure. But with an extra dimension, which makes things even better."
    mo "Debatable! "

    scene yasugenres18
    with dissolve

    f "So...have you thought at all about what genre you’d like to try first, Yasu?"
    f "We have all different types of books here. Ami and Maya even brought in most of their collection for you to sort through if you’d like."
    mo "I don’t know if Yasu’s ready for any of the stuff Maya reads. PunPun isn’t really entrance level material unless you’re looking to an-hero."
    ya "What is entrance level material? I would like to stay away from anything with gratuitous violence or premarital sex."

    scene yasugenres19
    with dissolve

    mo "Okay. Well, that rules out pretty much Rin’s entire collection, so...let’s see what else we can find laying around here."

    scene black
    with dissolve2

    "Molly and Futaba begin sorting through a few boxes while Yasu and I stand awkwardly in the corner, occasionally making eye contact- which may or may not be a sin according to her religion."
    "I take the fact that she hasn’t spontaneously burst into a fit of tears to be a good sign, though, and let the awkward silence bridge the ever growing gap between us in the form of a temporary respite."
    "There’s still a great deal I don’t understand about her. Particularly the parts where she vanishes and leaves me alone at a table full of eggs, but things like that can wait until another day."
    "For now, I’m just interested in seeing how she functions as a normal misfit girl, trying to fit in with people who genuinely {i}want{/i} her to fit in-"
    "And likely making everyone very uncomfortable in the process."

    scene yasugenres20
    with dissolve2

    mo "Question! How gratuitous {i}is{/i} “gratuitous violence?” "
    mo "Can there be any violence at all? Because there are a lot of very accessible shonen manga that serve as an awesome gateway to the world of anime!"
    ya "Umm..."

    scene yasugenres21
    with dissolve

    f "Is all romance off the table as well? Or just romantic series with...um...premarital sex?..."
    f "Because romantic subplots are essentially impossible to avoid in fiction, but there are a lot of fantasy series I enjoy that barely focus on it at all. And I think you’d love those!"
    ya "That...sounds like it might be okay..."
    s "What about this?"

    "I pick up the first book I see on top of a stack that looks relatively safe for work. And after skimming through the pages, I can say with utmost certainty that there is no premarital sex or gratuitous violence."
    "It doesn’t really seem like there’s much of {i}anything,{/i} though."
    "It’s just...people talking."

    scene yasugenres22
    with dissolve

    mo "Whatcha got there, Sir? You digging into Ami’s slice of life pile?"
    f "Oh, I think something like that might be good for Yasu as well."
    ya "Slice of life? "
    s "I guess that’s what I’m holding, sure."
    ya "It’s not violent?"

    scene yasugenres23
    with dissolve

    mo "Not that kind of slice, Yasu."
    mo "In fact, here’s a little weebnote for you."
    mo "Slice of life is a genre of anime and manga that focuses primarily on the lives of the {i}characters{/i} in the story and less on a unified and major coherent plotline."
    mo "That’s not to say there’s never any sort of plot at all, though. A lot of SoL series can blend in action and drama without ever abandoning their roots."
    mo "It’s something people tend to gravitate to after overloading themselves on more serious or action-packed series to sort of...unwind or reset."
    mo "But that doesn’t mean you can’t start there! And the one Sensei is holding would actually be a great one to go with since I’ve already finished it and can confirm there is zero sex at all!"

    scene yasugenres24
    with dissolve

    ya "Hooray for no inappropriate content!"
    mo "Yeah! Hooray, I guess!"
    mo "I still think you should maybe {i}consider{/i} shonen, though, since a lot of it nowadays is-"
    f "Just let her have this, Molly."

    scene black
    with dissolve2

    "I hand the book over to Yasu, who accepts it with the least creepy smile I have seen out of her thus far."
    "She opens it up and begins reading very slowly, focusing for far too long on each and every page as if she’s taking in every last detail and every last line."
    "I’m sure that the artists involved would be happy to see this, but even then I think they’d believe it to be a tad excessive."
    "Molly and Futaba cross the room and take their places beside me like we’re some sort of proud, polyamorous couple watching our daughter take her first steps."
    "I’m just a little disappointed because her steps are in a direction that I’m not particularly interested or invested in."
    "But hey, this is the first time I’ve ever seen a smile like that out of her."
    "And it’s a lot more infectious than those that have been induced by her god."
    "Yasu continues reading until the sun begins to set while the rest of us talk quietly amongst ourselves."
    "When the final bell rings, Yasu closes her book and thanks all of us for our help."
    "But not before grabbing three more books of what I expect and hope are the same genre. "

    $ renpy.end_replay()
    $ yasuspecial15 = True
    $ yasu_love += 1
    stop music fadeout 7.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label church20:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
    if totaldays >= 400 and day == 1 and halloweentwo13 == True and norikospecial20 == False:
        jump norikospecial20
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
    if totaldays >= 424 and kirindorm25 == True and day == 1 and chikaspecial40 == False:
        jump chikaspecial40
    if totaldays >= 455 and chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and day == 4 and christmastwo1 == False:
        jump christmastwo1
    if totaldays >= 500 and chapthree8 == True and church15 == True and yasuspecial15 == False:
        jump yasuspecial15
...
```