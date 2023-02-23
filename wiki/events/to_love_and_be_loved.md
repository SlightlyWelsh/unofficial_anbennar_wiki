#Information
 - Title: To Love and Be Loved
 - ID: consort_events.6
#Description
To Love and Be Loved
#Mean Time to Happen:
Base time = 1200 months
 - Multiplied by 4 if has ruler has personality is malevolent personality, and has ruler has personality is naive personality, and has ruler has personality is cruel personality, and has ruler has personality is infertile personality, and has ruler has personality is babbling buffoon personality
 - Multiplied by 1.2 if has ruler has personality ancestor has key is charismatic negotiator; and has ruler has personality ancestor has key is silver tongue; and has ruler has personality ancestor has key is well connected
 - Multiplied by 0.9 if has ruler has personality ancestor has key is kind hearted; and has ruler has personality ancestor has key is benevolent
 - Multiplied by 0.9 if has ruler has personality is sinner personality, and has ruler has personality is drunkard personality

#Options

___
##Let the [Root.Monarch.GetTitle] have [Root.Monarch.GetHerHis] heart's desire.

###Efects:<ul><li>goto = consort_home</li><li>set ruler flag [has_lowborn_consort](../flags/has_lowborn_consort.md)</li><li>define consort:</li><ul></ul><li>add ruler modifier:</li><ul><li>name = consort_of_the_people</li></ul><li>event target:consort home:</li><ul><li>add province modifier:</li><ul><li>name = home_of_consort</li><li>duration = -1</li></ul></ul><li>capital scope:</li><ul><li>add province modifier:</li><ul><li>name = nobles_displeased_with_consort</li><li>duration = 3650</li></ul></ul><li>add prestige = -20</li><li>add legitimacy = -20</li></ul>

___
##Marrying a lowborn? Totally out of the question!

###Efects:<ul><li>set ruler flag [turned_down_marriage_offer_for_love](../flags/turned_down_marriage_offer_for_love.md)</li></ul>
