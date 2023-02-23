#Information
 - Title: The [empty_neighbor_target.GetAreaName] Company
 - ID: colonial.1
#Description
The [empty_neighbor_target.GetAreaName] Company
#Mean Time to Happen:
Base time = 1 days

#Options

___
##This can only be good.

###Efects:<ul><li>goto = empty_neighbor_target</li><li>event target:empty neighbor target:</li><ul><li>create colony = 200</li><li>add province modifier:</li><ul><li>name = "colonial_boom"</li><li>duration = 7300</li></ul></ul></ul>

___
##Direct them to an existing colony

###Available if:
<li>owner:</li><ul><li>num of colonies is at least 1</li></ul>

###Efects:<ul><li>goto = root</li><li>owner:</li><ul><li>If random owned province is a colony:</li><ul><li>add province modifier:</li><ul><li>name = "colonial_boom"</li><li>duration = 1825</li></ul><li>add colonysize = 100</li></ul></ul></ul>
