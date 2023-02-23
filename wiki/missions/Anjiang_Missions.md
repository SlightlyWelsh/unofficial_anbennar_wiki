This is a list of all [missions](missions.md) of [Anjiang](Anjiang.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="anjiang_often_travelled">A Path Often Travelled</a><br />*The road between our lands and Tughayasa are controlled by a number of different powers. While many welcome the business that the steady stream of our envoys provides, others require a more discrete course. We must ensure that our runners can reliably navigate those foreign rodes, be it by friendship or subterfuge.* | <li>anjiang path:</li><ul><li>type is all</li><li>owner:</li><ul><li>Any of the following:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 50</li></ul><li>has spy network from:</li><ul><li>this nation</li><li>value is at least 30</li></ul></ul></ul></ul> | <li>add government reform = anjiang_court_of_envoys_reform</li><li>add historical friend = R05</li><li>R05:</li><ul><li>add historical friend = Y04</li></ul> | [Words of Wisdom](#anjiang_words_of_wisdom)<br /> |
| <a name="anjiang_second_seat">Second Seat of the Oracles</a><br />*In recent years, the section of the Golden Highway between our capitol and Tughayasa has been increasingly known as 'The Seers' Walk'. Many of our land's promising students venture to their mountains for tutelage, and many of their Oracles spend as much time in our lands as they do theirs. \n\nTo many, Anjiang is already called 'The Second Seat of The Oracles'. We must ensure our capitol is worthy of the title.* | <li>4853:</li><ul><li>has tax building trigger yes</li></ul><li>4853:</li><ul><li>development is at least 25</li></ul> | <li>If every known country has religious school has group is raheni, and religious school has school is starry eye school:</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = anjiang_second_seat_opinion</li></ul></ul><li>set country flag [anjiang_second_seat](../flags/anjiang_second_seat.md)</li> | [A Path Often Travelled](#anjiang_often_travelled)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="anjiang_words_of_wisdom">Words of Wisdom</a><br />*The seers of Tughayasa have long since been among our closest allies. While logistics have typically made direct military support impossible, the boons of this kinship are far more valuable than any number of blades. The seers are possessed of a gift in foresight - a gift they are willing to share the spoils of with us. It is imperative that we do not allow this relationship to fade.* | <li>Any of the following:</li><ul><li>R05:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>None of the following:</li><ul><li>exists is Tughayasa</li></ul></ul> | <li>the event [The Coming Storm](../events/the_coming_storm.md) happens</li> |  |
| <a name="anjiang_pull_back_curtain">Pull Back The Curtain</a><br />*Dark tidings arrive from the seers - Our erstwhile allies in Yingzhin are, according to their sight, plotting some grand scheme against us. \n\nWhile we may not be fortunate enough to know the details quite yet, we at least know where to find them.* | <li>spymaster is at least 1</li><li>Any of the following:</li><ul><li>has spy network in:</li><ul><li>Y10</li><li>value is at least 40</li></ul><li>All of the following:</li><ul><li>Y10:</li><ul><li>does not exist</li></ul><li>owns core province 4849</li></ul></ul> | <li>the event [Pulling Back The Curtain](../events/pulling_back_the_curtain.md) happens</li> | [Words of Wisdom](#anjiang_words_of_wisdom)<br /> |
| <a name="anjiang_strike_first">Strike First</a><br />*With the truth revealed, Yingzhin has been by large ousted from the League. With neighbors on all sides eyeing hungrily at their lands, a great many of our own ranks call to return the smallfolk of the area to the League's protection. \n\nUnder our banner this time, of course.* | <li>owns core province 4849</li> | <li>4849:</li><ul><li>add province modifier:</li><ul><li>name = anjiang_eyes_wrath</li><li>duration = 3650</li><li>hidden = no</li></ul></ul> | [Pull Back The Curtain](#anjiang_pull_back_curtain)<br /> |
| <a name="anjiang_summit_river">Summit Of The River</a><br />*Recent years have seen our once-strong League fracture and fade. Territory has been lost, allies have turned against us, and even the ill-fated city of Szicheng chose to die alone rather than stand at our side. A summit has been proposed of the remaining members of the League - one where we shall seek out a unification of our states. \n\n More cynical voices urge caution, however - making public this proposal without first proving ourselves worthy to lead will undoubtedly end in failure.* | <li>Any of the following:</li><ul><li>Y06:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>None of the following:</li><ul><li>exists is Y06</li></ul></ul><li>OR:</li><ul><li>Y07:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>None of the following:</li><ul><li>exists is Y07</li></ul></ul><li>OR:</li><ul><li>Y08:</li><ul><li>has opinion:</li><ul><li>this nation</li><li>value is at least 100</li></ul></ul><li>None of the following:</li><ul><li>exists is Y08</li></ul></ul> | <li>the event [The Summit of the Yan](../events/the_summit_of_the_yan.md) happens</li> | [Strike First](#anjiang_strike_first)<br /> |
| <a name="anjiang_visit_augur">A Visit From The Augur</a><br />*The ascent of our state has given rise to an ever-growing influence with our Seer allies. So much, in fact, that the great Augur of their order has scheduled a visit to our capitol. We must make preparations for a fitting reception, so that we may recieve his boon.* | <li>religious unity is at least 1</li><li>temple is at least 10</li> | <li>set country flag [anjiang_pulse](../flags/anjiang_pulse.md)</li><li>add ruler modifier:</li><ul><li>name = magic_realm_divination_foresight</li><li>duration = 365</li></ul> | [Summit Of The River](#anjiang_summit_river)<br />[Second Seat of the Oracles](#anjiang_second_seat)<br />[Drive Out The Demons](#anjiang_drive_demons)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="anjiang_blade_evil">A Blade Against Evil</a><br />*The wretches of Jinqiu have been a threat to the League for as long as anyone can remember - doubly so since the fall of Caoying granted them a direct border to our own lands. While their cities are by no doubt grander than ours, they remain politically isolated. \n\nA proper coalition of states may very well prove sufficient to restore the League's lands, and more besides.* | <li>4851:</li><ul><li>owned by is this nation</li></ul><li>jinqiu area:</li><ul><li>type is all</li><li>owned by is this nation</li></ul> | <li>moryokang area:</li><ul><li>add permanent claim = ROOT</li></ul><li>country gets the modifier anjiang_against_evil for 20 years</li> | [Words of Wisdom](#anjiang_words_of_wisdom)<br /> |
| <a name="anjiang_blade_red">A Blade Stained Red</a><br />*Even further west lie the Oni and their tributaries. Demons and corruptors of men, these horned beasts are even more wicked than the monsters of Jinqiu! \n\nThese monsters, and the men who have made pacts with them, must be put to the sword so that the land may be put to righteous use by righteous men, such as ourselves. What's more, a second successful military campaign might just win the favor of other states of the League.* | <li>moryokang area:</li><ul><li>type is all</li><li>owned by is this nation</li></ul> | <li>the event [Rooting Out Evil](../events/rooting_out_evil.md) happens</li><li>set country flag [anjiang_stained_red](../flags/anjiang_stained_red.md)</li> | [A Blade Against Evil](#anjiang_blade_evil)<br /> |
| <a name="anjiang_drive_demons">Drive Out The Demons</a><br />*The mountains to the north have long since been home to the demonic 'Oni'. Slavemasters and spirit-defilers, a Haless which is still host to their ilk will forever be a tainted land. It is the duty of any decent person to bring about their end, should they have the opportunity.* | <li>anjiang area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>has owner religion</li></ul><li>jinqiu area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>has owner religion</li></ul><li>moryokang area:</li><ul><li>type is all</li><li>owned by is this nation</li><li>has owner religion</li></ul> | <li>country gets the modifier anjiang_drive_demons until otherwise removed</li> | [A Blade Stained Red](#anjiang_blade_red)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |