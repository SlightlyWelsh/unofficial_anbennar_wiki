#Information
 - Title: [From.GetName] and the Ultakal Decree
 - ID: goldisland.17
#Description
[From.GetName] and the Ultakal Decree
#Options

___
##We are just, and shall give it back to them

###AI weighting:
AI weights this option at 50
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 50
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 100
 - Multiplied by 1.5 if has opinion has who is FROM, and has opinion has value is 150


###Efects:<ul><li>5239:</li><ul><li>remove core = ROOT</li><li>cede province = FROM</li><li>add core = FROM</li></ul><li>FROM:</li><ul><li>the event [The Golden Island](../events/the_golden_island.md) happens</li></ul><li>lake federation lose 2 points = yes</li><li>custom tooltip = restablish_decree_tooltip</li><li>hidden effect:</li><ul><li>clr global flag [federation_crisis_goldisland](../flags/federation_crisis_goldisland.md)</li></ul><li>hidden effect:</li><ul><li>set global flag [federation_golden_island_timer](../flags/federation_golden_island_timer.md)</li></ul></ul>

___
##Ultakal is the property of the Federation Leader!

###AI weighting:
AI weights this option at 15
 - Multiplied by 2 if does not have opinion has who is FROM, and has opinion has value is 0
 - Multiplied by 3 if does not have opinion has who is FROM, and has opinion has value is -50
 - Multiplied by 5 if does not have opinion has who is FROM, and has opinion has value is -100
 - Multiplied by 30 if is rival is FROM


###Efects:<ul><li>hidden effect:</li><ul><li>set global flag [federation_crisis](../flags/federation_crisis.md)</li></ul><li>the event [The Refusal](../events/the_refusal.md) happens</li></ul>
