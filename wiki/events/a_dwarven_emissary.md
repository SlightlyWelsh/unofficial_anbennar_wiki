#Information
 - Title: A Dwarven Emissary
 - ID: flavor_lodhum.14
#Description
A Dwarven Emissary
#Options

___
##We have other, more pressing concerns; humour them

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if is rival is H77, and is rival is F26
 - Multiplied by 1.5 if has opinion has who is H77, and has opinion has value is 125; and has opinion has who is F26, and has opinion has value is 125
 - Multiplied by 2 if has trust has who is H77, and trust has value is 70; and has trust has who is F26, and trust has value is 70
 - Multiplied by 1.5 if has alliance with is H77, and has alliance with is F26


###Efects:<ul><li>add dip power = 100</li><li>reverse add opinion:</li><ul><li>who = H77</li><li>modifier = opinion_grateful</li></ul><li>set country flag [accepted_lodhum_friendship](../flags/accepted_lodhum_friendship.md)</li></ul>

___
##We shall teach them the meaning of 'bleeding hearts'

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.8 if does not have manpower percentage is 0.3
 - Multiplied by 0.75 if has num of loans is 4
 - Multiplied by 1.5 if has army strength has who is H77, and army strength has value is 0.4
 - Multiplied by 2 if has army strength has who is H77, and army strength has value is 0.6
 - Multiplied by 2 if has total development is 200
 - Multiplied by 2 if has total development is 250
 - Multiplied by 2 if has total development is 300
 - Multiplied by 3 if is a great power


###Efects:<ul><li>custom tooltip = flavor_lodhum.14.tooltip</li><li>If has event target:global lodhum elf enemy 1 has tag is ROOT:</li><ul><li>custom tooltip = flavor_lodhum.14.tooltip2</li></ul><li>else:</li><ul><li>custom tooltip = flavor_lodhum.14.tooltip3</li></ul><li>set country flag [denied_lodhum_friendship](../flags/denied_lodhum_friendship.md)</li><li>If is controlled by the AI:</li><ul><li>add manpower = 10</li><li>country gets the modifier lodhum_ai_war_buff for 10 years</li></ul></ul>
