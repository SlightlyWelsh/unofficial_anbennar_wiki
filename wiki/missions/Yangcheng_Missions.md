This is a list of all [missions](missions.md) of [Yangcheng](Yangcheng.md)

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="yangcheng_yanzhong_proposal">The Yanzhong Proposal</a><br />*Yanzhong has always been our closest ally within the League, as well as our school's greatest sponsor. While already fairly amenable to the unification proposals, a show of goodwill should solidify that. \n\nWe will approach them with an offer regarding the local trade routes, one which is clearly one-sided in their favor. The message will be obvious - we are interested in the goodwill of all.* | <li>reverse has opinion:</li><ul><li>Y08</li><li>value is at least 200</li></ul><li>Y08:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 60</li></ul></ul> | <li>4859:</li><ul><li>add trade modifier:</li><ul><li>who = ROOT</li><li>duration = 3650</li><li>power = -20</li><li>key = yangcheng_proposal</li></ul><li>add trade modifier:</li><ul><li>who = Y08</li><li>duration = 3650</li><li>power = 20</li><li>key = yangcheng_proposal</li></ul></ul><li>add trust:</li><ul><li>who = Y08</li><li>value = 5</li><li>mutual = yes</li></ul> | [The Reunion of 1445](#yangcheng_reunion)<br /> |
| <a name="yangcheng_sympathetic_officers">Sympathetic Officers</a><br />*Guhe has typically been a close friend of the academy, and a considerable number of their military officials hail from our lecture halls. So long as we can maintain a strong diplomatic bond with their state itself, those within their ranks who are sympathetic to our cause should be able to more freely advocate for us.* | <li>army strength:</li><ul><li>Y07</li><li>value is at least 1</li></ul><li>employed advisor:</li><ul><li>category is MIL</li></ul><li>Y07:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 65</li></ul></ul> | <li>Y07:</li><ul><li>add army tradition = 5</li></ul><li>add trust:</li><ul><li>who = Y07</li><li>value = 5</li><li>mutual = yes</li></ul> | [The First Summit](#yangcheng_first_yanszin)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="yangcheng_reunion">The Reunion of 1445</a><br />*While not an enshrined institution of the school, so-called 'Reunions' are not an uncommon occurence. Oftentimes simple excuses for alumni to drink and mingle with old friends, they nonetheless serve an important role as grounds for much more candid political discussion. \n\nWith plans already in place for such an event to begin soon, the topics of discussion will no doubt turn to the League's current troubles.* | <li>is year is at least 1445</li> | <li>the event [The Dour Affair](../events/the_dour_affair.md) happens</li> |  |
| <a name="yangcheng_first_yanszin">The First Summit</a><br />*With at least partial support from the rest of the League, it is prudent to at least 'test the waters', as it is often said. Our diplomats do not believe any official solutions will be borne from this gathering, but having open discussion and support on the matter will at least ensure that those not in favor will take the matter seriously.* | <li>reverse has opinion:</li><ul><li>Y07</li><li>value is at least 150</li></ul><li>reverse has opinion:</li><ul><li>Y04</li><li>value is at least 150</li></ul> | <li>the event [The Gathering at Yanzhong](../events/the_gathering_at_yanzhong.md) happens</li> | [The Bookends](#yangcheng_bookends)<br />[The Yanzhong Proposal](#yangcheng_yanzhong_proposal)<br /> |
| <a name="yangcheng_second_yanszin">The Second Summit</a><br />*With special projects completed to improve the demeanor of the naysayers, it is finally time to give the Yanszin proposal another try.* | <li>Any of the following:</li><ul><li>Y07:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 80</li></ul><li>is not at war</li></ul><li>owns core province 4950</li></ul><li>OR:</li><ul><li>Y04:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 80</li></ul><li>is not at war</li></ul><li>owns core province 4853</li></ul><li>OR:</li><ul><li>Y08:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 80</li></ul><li>is not at war</li></ul><li>owns core province 4859</li></ul><li>OR:</li><ul><li>Y10:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 80</li></ul><li>is not at war</li></ul><li>owns core province 4849</li></ul> | <li>inherit = Y10</li><li>inherit = Y08</li><li>inherit = Y07</li><li>inherit = Y04</li><li>If has 4859 has owned by is ROOT:</li><ul><li>set capital = 4859</li></ul><li>clr country flag [yangcheng_allow_debates](../flags/yangcheng_allow_debates.md)</li> | [Changing The Future](#yangcheng_future)<br />[Sympathetic Officers](#yangcheng_sympathetic_officers)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="yangcheng_bookends">The Bookends</a><br />*Yingzhen has always been something of an oddity among the League. While the rest of the League finds itself led by the most accomplished graduates and the most experienced statesmen available, the voting in this backwater tends to veer towards the opposite. Those once considered incompetent find greater heights in the government, and... somehow, they tend not to do all too poorly. \n\nCorruption and deceit reign supreme in those lands, and a growing contingent of those investigating the matter believe that the city's power rests not in the Mayor's hands, but in some sinister cabal. Knowing this, some careful planning may leave us able to free the current mayor from these strings - leaving him in our debt.* | <li>reverse has opinion:</li><ul><li>Y10</li><li>value is at least 150</li></ul><li>has spy network in:</li><ul><li>Y10</li><li>value is at least 50</li></ul> | <li>Y10:</li><ul><li>the event [A Friend's Plea](../events/a_friend_s_plea.md) happens</li></ul><li>add trust:</li><ul><li>who = Y10</li><li>value = 5</li><li>mutual = yes</li></ul> | [The Reunion of 1445](#yangcheng_reunion)<br /> |
| <a name="yangcheng_future">Changing The Future</a><br />*Anjiang is perhaps the closest thing to a 'rival' that our state has within the League. Our relations are cordial, of course, but the zealots of that city are far more inclined to listen to the words of their Raheni seers than any measured reason. Nonetheless, with some proper theological debate (as well as the ever-growing consensus among the rest of the League), we may just be able to convince them that the seers' portends support our cause.* | <li>has spy network in:</li><ul><li>Y04</li><li>value is at least 35</li></ul><li>employed advisor:</li><ul><li>type is theologian</li></ul><li>Y04:</li><ul><li>trust:</li><ul><li>Y06</li><li>value is at least 65</li></ul></ul> | <li>Y04:</li><ul><li>the event [Change The Future](../events/change_the_future.md) happens</li></ul><li>add trust:</li><ul><li>who = Y04</li><li>value = 5</li><li>mutual = yes</li></ul> | [The First Summit](#yangcheng_first_yanszin)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="yangcheng_debate">Debate Clubs</a><br />*Public debates are a longstanding tradition of the Yangcheng Schools. Argument for its own sake is considered a sort of art, and being able to defend a position which one may not even hold is a well-respected achievement. In the face of our intentions to bring the League closer together, many of our officials believe that even the small act of having our more recognizable figures taking part in some of the more popular debates could assist us in our relations with the rest of the League.* | <li>monthly adm is at least 10</li><li>monthly dip is at least 10</li><li>monthly mil is at least 10</li> | <li>set country flag [yangcheng_allow_debates](../flags/yangcheng_allow_debates.md)</li><li>custom tooltip = yangcheng_debate_tt</li> | [Amidst Dusty Tomes](#yangcheng_dusty_tomes)<br /> |
| <a name="yancheng_great_school">The Great School</a><br />*A proper education is the key to any good administrator, and our growing influence across Yanshen only gives credance to that. As the great university becomes a more ingrained part of the state itself, it has becomes more apparent that its reach must grow with its charge. Even in the far corners of our realm, from the smallest village to the greatest metropolis, an educated and honorable man must lead the way. The facilities of our school must be expanded so that its services are available to all who will have a part in shaping the future.* | <li>num of owned provinces with:</li><ul><li>value is at least 3</li><li>has terrain city_terrain</li></ul> | <li>4861:</li><ul><li>add building construction:</li><ul><li>building = university</li><li>speed = 1</li><li>cost = 0</li></ul></ul><li>set country flag [yangcheng_pulse](../flags/yangcheng_pulse.md)</li><li>custom tooltip = yangcheng_pulse_tt</li> | [Debate Clubs](#yangcheng_debate)<br /> |

| Mission | Completion requirements | Effects | Prerequisites |
| ----- | ------ | ----- | ------ |
| <a name="yangcheng_dusty_tomes">Amidst Dusty Tomes</a><br />*There exists a saying throughout central Yanshen, that one who's path in life appears listless and uncertain is 'Chasing Faheng'. It refers to a popular local legend of an ancient, vast gold mine that once existed in the region - one that was destroyed and lost to the ages in the wake of Jaher's invasion, all those years ago. \n\nFor most of recent history, academic consensus has been that the mine never existed and that the legend was but a legend. However, a merchant from Yanzhong recently approached the school bearing a collection of golden ingots bearing an unknown Mark. While this gold is not conclusive proof of anything, a number of scholars have been inspired to open proper efforts to seek the ancient mine - just in case there is truth to it, after all.* | <li>Y05:</li><ul><li>Any of the following:</li><ul><li>has spy network from:</li><ul><li>Y06</li><li>value is at least 25</li></ul><li>has opinion:</li><ul><li>Y06</li><li>value is at least 50</li></ul></ul></ul><li>Y27:</li><ul><li>Any of the following:</li><ul><li>has spy network from:</li><ul><li>Y06</li><li>value is at least 25</li></ul><li>has opinion:</li><ul><li>Y06</li><li>value is at least 50</li></ul></ul></ul> | <li>the event [Golden Mysteries](../events/golden_mysteries.md) happens</li> |  |
| <a name="yangcheng_faheng">Faheng's Pit</a><br />*With a considerable number of samples acquired from the surrounding lands, it is time we dedicated resources to the proper analysis of them. Every account must be verified, and every stone must be tested. If the mine exists, there will be traces of it.* | <li>treasury is at least 50</li><li>employed advisor:</li><ul><li>type is natural_scientist</li></ul> | <li>add government reform = yangcheng_xuezhe_reform</li> | [Amidst Dusty Tomes](#yangcheng_dusty_tomes)<br /> |
| <a name="yangcheng_stories">Stories In Stone</a><br />*A number of samples from the region to our south seem to indicate the presence of at least some amount of gold. Unfortunately, local records are sparse on the matter. Many of our officials suggest reaching out to some of the few Dwarves in Haless, so that we might employ their expertise.* | <li>Y27:</li><ul><li>Any of the following:</li><ul><li>has spy network from:</li><ul><li>Y06</li><li>value is at least 50</li></ul><li>has opinion:</li><ul><li>Y06</li><li>value is at least 125</li></ul></ul></ul><li>any known country:</li><ul><li>has country modifier dwarven_administration</li><li>has opinion:</li><ul><li>Y06</li><li>value is at least 100</li></ul></ul> | <li>4895:</li><ul><li>add permanent claim = ROOT</li></ul> | [Faheng's Pit](#yangcheng_faheng)<br /> |
| <a name="yangcheng_restoration">Restoration Efforts</a><br />*After a great deal of testing and covert prospecting, our dwarven friends have identified where they believe the old mine is located. Deep within a collapsed cave in the area known as 'Godou', a few old mining tools have been found - as well as a number of golden nuggets. The area must be taken for our own ends before anyone else can capitalize on our studies.* | <li>4895:</li><ul><li>owned by is this nation</li></ul><li>treasury is at least 150</li> | <li>4895:</li><ul><li>change trade goods = gold</li></ul><li>If has any known country has country modifier is dwarven administration, and any known country has opinion has who is Y06, and has opinion has value is 100:</li><ul><li>4895:</li><ul><li>add dwarven minority size effect = yes</li></ul><li>small increase of dwarven tolerance effect = yes</li></ul> | [Stories In Stone](#yangcheng_stories)<br /> |