#Information
 - Title: Local Militias Organize
 - ID: disaster_vampire_masquerade.100
#Description
Local Militias Organize
#Mean Time to Happen:
Base time = 1 days

#Options

___
##They have our support.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = masquerade_disaster_militia_desc</li><li>influence = 4</li><li>duration = 5475</li></ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = masquerade_disaster_militia_desc</li><li>loyalty = 5</li><li>duration = 5475</li></ul><li>event target:province:</li><ul><li>add province modifier:</li><ul><li>name = masquerade_adventurer_militia</li><li>duration = 5475</li></ul></ul><li>add manpower = 1.500</li><li>goto = province</li><li>event target:province:</li><ul><li>add local autonomy = 10</li></ul></ul>

___
##We cannot support this.

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>add estate influence modifier:</li><ul><li>estate = estate_adventurers</li><li>desc = masquerade_disaster_militia_desc</li><li>influence = 3</li><li>duration = 5475</li></ul><li>event target:province:</li><ul><li>add province modifier:</li><ul><li>name = masquerade_adventurer_militia</li><li>duration = 5475</li></ul></ul><li>add manpower = 0.500</li><li>goto = province</li></ul>
