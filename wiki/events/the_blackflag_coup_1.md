This page has the same name as others. For full listing see bottom of [the base page](the_blackflag_coup.md).

#Information
 - Title: The Blackflag Coup
 - ID: flavour_tluukt.19
#Description
The Blackflag Coup
#Options

___
##And after we win, Drolakand will be ours!

###Available if:
<li>overlord of is Drolakand</li>

###Efects:<ul><li>tooltip:</li><ul><li>create subject:</li><ul><li>subject type = tributary_state</li><li>subject = F32</li></ul></ul><li>declare war with cb:</li><ul><li>who = event_target:tluukt_drolakand_overlord</li><li>casus belli = cb_monster_vs_civ</li></ul><li>F32:</li><ul><li>join all offensive wars of = F28</li></ul><li>event target:tluukt drolakand overlord:</li><ul><li>If every owned province is core is F32:</li><ul><li>change controller = F32</li></ul></ul><li>If bulwar proper region has owned by is event target:tluukt drolakand overlord, and does not have core is F32:</li><ul><li>add claim = F28</li></ul><li>hidden effect:</li><ul><li>event target:tluukt drolakand overlord:</li><ul><li>the event [The Blackflag Coup](../events/the_blackflag_coup.md) happens</li></ul></ul></ul>

___
##[Root.Monarch.GetTitle] [Root.Monarch.GetName] will soon learn the proper way of punishing the impertinent.

###Available if:
<li>None of the following:</li><ul><li>overlord of is Drolakand</li></ul>

###Efects:<ul><li>add casus belli:</li><ul><li>target = F32</li><li>type = cb_force_tributary_mission</li><li>months = 240</li></ul><li>If bulwar proper region has owned by is event target:tluukt drolakand overlord:</li><ul><li>add claim = F28</li></ul></ul>
