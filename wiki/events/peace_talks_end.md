#Information
 - Title: Peace Talks End
 - ID: fed_religious.34
#Description
Peace Talks End
#Options

___
##Missing localisation: fed_religious_34_a

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>clr global flag [lake_appeasing_tension](../flags/lake_appeasing_tension.md)</li><li>REB:</li><ul><li>set variable:</li><ul><li>tension = 0</li></ul><li>change variable:</li><ul><li>which = tension</li><li>which = yukel_resolve</li></ul><li>change variable:</li><ul><li>which = tension</li><li>which = enuuk_resolve</li></ul><li>change variable:</li><ul><li>which = tension</li><li>which = kodave_resolve</li></ul></ul><li>If has REB has check variable has tension is 150:</li><ul><li>If random known country has country flag is [kodave_leader](../flags/kodave_leader.md):</li><ul><li>the event [The Breaking Point](../events/the_breaking_point.md) happens</li></ul></ul><li>else:</li><ul><li>If has REB has check variable has which is yukel resolve, and check variable has which is enuuk resolve; and  has REB has check variable has which is yukel resolve, and check variable has which is kodave resolve:</li><ul><li>the event [White Peace](../events/white_peace.md) happens</li></ul><li>Else if has REB has check variable has which is enuuk resolve, and check variable has which is yukel resolve; and  has REB has check variable has which is enuuk resolve, and check variable has which is kodave resolve:</li><ul><li>If random known country has country flag is [enuuk_leader](../flags/enuuk_leader.md):</li><ul><li>the event [Enuuk Prevails](../events/enuuk_prevails.md) happens</li></ul></ul><li>Else if has REB has check variable has which is kodave resolve, and check variable has which is yukel resolve; and  has REB has check variable has which is kodave resolve, and check variable has which is enuuk resolve:</li><ul><li>If random known country has country flag is [kodave_leader](../flags/kodave_leader.md):</li><ul><li>the event [Kodave Prevail](../events/kodave_prevail.md) happens</li></ul></ul><li>else:</li><ul><li>the event [White Peace](../events/white_peace.md) happens</li></ul></ul></ul>
