#Information
 - Title: Unfair Competition
 - ID: colonial_nation.189
#Description
Unfair Competition
#Mean Time to Happen:
Base time = 1 days

#Options

___
##[Root.Adm_Advisor.GetName] will deal with this.

###Available if:
<li>has adm advisor yes</li>

###Efects:<ul><li>add adm power = -50</li><li>add prestige = -2</li></ul>

___
##We can always ask for the Church's mediation

###Available if:
<li>religion is catholic</li><li>Any of the following:</li><ul><li>employed advisor:</li><ul><li>type is theologian</li><li>religion is catholic</li></ul><li>employed advisor:</li><ul><li>type is inquisitor</li><li>religion is catholic</li></ul></ul>

###Efects:<ul><li>If random owned province does not have religion is catholic:</li><ul><li>add province modifier:</li><ul><li>name = colonial_missionaries</li><li>duration = 3650</li></ul></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 10</li></ul></ul>

___
##Some rumors about their reputation may flip the coin...

###Available if:
<li>dip tech is at least 3</li><li>Any of the following:</li><ul><li>has dip advisor yes</li><li>ruler has personality ancestor:</li><ul><li>key is silver_tongue</li></ul><li>consort has personality is silver_tongue_personality</li><li>ruler has good dip personality is yes</li><li>dip is at least 4</li></ul>

###Efects:<ul><li>add dip power = -50</li><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -5</li></ul></ul>

___
##Seize these seditionists!

###Efects:<ul><li>capital scope:</li><ul><li>spawn rebels:</li><ul><li>type = pretender_rebels</li><li>size = 2</li></ul></ul></ul>
