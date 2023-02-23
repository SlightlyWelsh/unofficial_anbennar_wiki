#Information
 - Title: Corruption among the [Root.GetClergyName]
 - ID: 5098
#Description
Corruption among the [Root.GetClergyName]
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 2.0 if is lucky
 - Multiplied by 0.66 if has advisor is treasurer

#Options

___
##Cleanse the temple.

###AI weighting:
AI weights this option at 55
 - Multiplied by 0 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>add devotion = 10</li><li>add stability or adm power = yes</li><li>reduce estate church loyalty effect = yes</li></ul>

___
##Fine the sinners.

###AI weighting:
AI weights this option at 45


###Efects:<ul><li>add devotion = -10</li><li>add years of income = 0.75</li><li>add corruption = 0.5</li><li>add estate church loyalty effect = yes</li></ul>

___
##As long as the state gets a slice of the pie.

###Available if:
<li>ruler has personality is embezzler_personality</li>

###Efects:<ul><li>highlight = yes</li><li>add devotion = -15</li><li>add years of income = 1</li><li>add corruption = 1</li><li>add estate church loyalty effect = yes</li></ul>

___
##The [Root.Monarch.GetTitle] will personally crack down on these sinners.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is incorruptible</li></ul>

###Efects:<ul><li>highlight = yes</li><li>add devotion = 15</li><li>add stability or adm power = yes</li><li>add corruption = -2</li></ul>
