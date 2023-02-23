#Information
 - Title: Trial of Castan II Beastbane: The Basilisk Appears
 - ID: castanortrials.414
#Description
Trial of Castan II Beastbane: The Basilisk Appears
#Options

___
##Grab an old molt and escape, it may be good enough

###Available if:
<li>has country flag [beastbane_trial_beast_asleep](../flags/beastbane_trial_beast_asleep.md)</li>

###Efects:<ul><li>set country flag [beastbane_trial_molt_grabbed](../flags/beastbane_trial_molt_grabbed.md)</li><li>the event ˻castanortrials.416˼ happens</li></ul>

___
##Shoot it full of arrows while it is unaware

###Available if:
<li>Any of the following:</li><ul><li>has country flag [beastbane_trial_beast_hunting](../flags/beastbane_trial_beast_hunting.md)</li><li>has country flag  beastbane_trial_beast_asleep</li></ul>

###Efects:<ul><li>If has country flag is [beastbane_trial_beast_asleep](../flags/beastbane_trial_beast_asleep.md):</li><ul><li>set country flag [beastbane_trial_sleeping_arrow_ambush](../flags/beastbane_trial_sleeping_arrow_ambush.md)</li></ul><li>else:</li><ul><li>set country flag [beastbane_trial_hunting_arrow_ambush](../flags/beastbane_trial_hunting_arrow_ambush.md)</li></ul><li>the event ˻castanortrials.415˼ happens</li></ul>

___
##We'll have one chance - sneak up and attack a weak spot!

###Available if:
<li>has country flag [beastbane_trial_beast_hunting](../flags/beastbane_trial_beast_hunting.md)</li>

###Efects:<ul><li>set country flag [beastbane_trial_occupied_ambush](../flags/beastbane_trial_occupied_ambush.md)</li><li>the event ˻castanortrials.415˼ happens</li></ul>

___
##Run away

###Available if:
<li>has country flag [beastbane_trial_being_hunted](../flags/beastbane_trial_being_hunted.md)</li>

###Efects:<ul><li>set country flag [beastbane_trial_ran](../flags/beastbane_trial_ran.md)</li><li>castanor trials fail effect = yes</li></ul>

___
##Ashen skies! No avoiding a fight now...

###Available if:
<li>has country flag [beastbane_trial_being_hunted](../flags/beastbane_trial_being_hunted.md)</li>

###Efects:<ul><li>the event ˻castanortrials.415˼ happens</li></ul>
