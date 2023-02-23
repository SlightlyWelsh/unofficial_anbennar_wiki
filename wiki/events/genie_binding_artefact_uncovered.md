#Information
 - Title: Genie Binding Artefact Uncovered
 - ID: new_sun_cult.280
#Description
Genie Binding Artefact Uncovered
#Options

___
##Excellent!

###Available if:
<li>event target:nsc possible artefact target:</li><ul><li>has province flag [nsc_working_artefact](../flags/nsc_working_artefact.md)</li></ul>

###Efects:<ul><li>custom tooltip = nsc_gathered_a_working_artifact_tt</li><li>If has check variable has which is numOfWorkingArtefacts, and check variable has value is 5:</li><ul><li>clr country flag [nsc_digging_artifacts](../flags/nsc_digging_artifacts.md)</li><li>set country flag [nsc_using_artifacts](../flags/nsc_using_artifacts.md)</li></ul><li>event target:nsc possible artefact target:</li><ul><li>clr province flag [nsc_working_artefact](../flags/nsc_working_artefact.md)</li></ul></ul>

___
##Oh no!

###Available if:
<li>event target:nsc possible artefact target:</li><ul><li>None of the following:</li><ul><li>has province flag [nsc_working_artefact](../flags/nsc_working_artefact.md)</li></ul></ul>

###Efects:<ul><li>add prestige = -1</li></ul>
