#Information
 - Title: Trials of Castan
 - ID: castanortrials.12
#Description
Trials of Castan
#Options

___
##I will prove myself worthy.

###AI weighting:
AI weights this option at 50
 - Multiplied by 5 if has ruler has personality is righteous personality, and has ruler has personality is zealot personality, and has ruler has personality is bold fighter personality, and has ruler has personality is naive personality


###Efects:<ul><li>If has mission completed is urviksten gerudian trials:</li><ul><li>custom tooltip = urviksten_mission_completed_auto_win</li><li>hidden effect:</li><ul><li>the event [Coronation of a New Castan!](../events/coronation_of_a_new_castan.md) happens</li></ul></ul><li>else:</li><ul><li>hidden effect:</li><ul><li>the event [The Trials of Castan](../events/the_trials_of_castan.md) happens</li></ul></ul></ul>

___
##The risk is too great...

###AI weighting:
AI weights this option at 10
 - Multiplied by 5 if has ruler has personality is craven personality, and has ruler has personality is careful personality, and has ruler has personality is sinner personality
 - Multiplied by 0 if has mission completed is urviksten gerudian trials


###Efects:<ul><li>add ruler modifier:</li><ul><li>name = castanortrials_refused_trial</li><li>duration = -1</li></ul></ul>
