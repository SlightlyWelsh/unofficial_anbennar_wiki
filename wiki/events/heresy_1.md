This page has the same name as others. For full listing see bottom of [the base page](heresy.md).

#Information
 - Title: Heresy!
 - ID: random_event.8
#Description
Heresy!
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Father, your will be done

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>If has saved event target is origin of bishop:</li><ul><li>define advisor:</li><ul><li>type = inquisitor</li><li>skill = 1</li><li>culture = event_target:origin_of_bishop</li></ul></ul><li>else:</li><ul><li>define advisor:</li><ul><li>type = inquisitor</li><li>skill = 1</li></ul></ul><li>add papal influence = 10</li><li>add estate church loyalty effect = yes</li><li>reduce meritocracy effect = yes</li><li>If has advisor is natural scientist:</li><ul><li>kill advisor = natural_scientist</li></ul><li>If has advisor is philosopher:</li><ul><li>kill advisor = philosopher</li></ul><li>If has advisor is artist:</li><ul><li>kill advisor = artist</li></ul><li>If has advisor is theologian:</li><ul><li>kill advisor = theologian</li></ul></ul>

___
##Poison the Provost's lunch, next time!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if has estate is estate church, and does not have estate loyalty has estate is estate church, and estate loyalty has loyalty is 30


###Efects:<ul><li>add adm power = 50</li><li>reduce estate church loyalty effect = yes</li><li>add papal influence = -20</li></ul>

___
##The [Root.Monarch.GetTitle] will take care of this.

###Available if:
<li>ruler has personality ancestor:</li><ul><li>key is pious</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add adm power = 50</li><li>add papal influence = -5</li></ul>
