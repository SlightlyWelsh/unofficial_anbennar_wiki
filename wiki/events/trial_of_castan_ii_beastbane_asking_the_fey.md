#Information
 - Title: Trial of Castan II Beastbane: Asking the Fey
 - ID: castanortrials.412
#Description
Trial of Castan II Beastbane: Asking the Fey
#Options

___
##Uh oh

###Available if:
<li>has country flag [beastbane_trial_fey_failure](../flags/beastbane_trial_fey_failure.md)</li>

###Efects:<ul><li>hidden effect:</li><ul><li>random list:</li><ul><li>50:</li><ul><li>modifier:</li><ul><li>factor = 3</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_adventurer_chosen](../flags/castanor_trials_candidate_adventurer_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_noble_chosen](../flags/castanor_trials_candidate_noble_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_mage_chosen](../flags/castanor_trials_candidate_mage_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 2.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>mil = 6</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>mil = 5</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>mil = 4</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>ruler has personality = strict_personality</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>ruler has personality = bold_fighter_personality</li></ul><li>modifier:</li><ul><li>factor = 2</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>ruler has mage personality = yes</li></ul><li>set country flag [beastbane_trial_fey_fight_success](../flags/beastbane_trial_fey_fight_success.md)</li></ul><li>50:</li><ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>ruler has personality = craven_personality</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_academic_chosen](../flags/castanor_trials_candidate_academic_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_dignitary_chosen](../flags/castanor_trials_candidate_dignitary_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>has reform = original_castanor_trials_reform</li><li>has country flag [castanor_trials_candidate_priest_chosen](../flags/castanor_trials_candidate_priest_chosen.md)</li></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>NOT:</li><ul><li>mil = 3</li></ul></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>NOT:</li><ul><li>mil = 2</li></ul></ul><li>modifier:</li><ul><li>factor = 1.5</li><li>NOT:</li><ul><li>has reform = original_castanor_trials_reform</li></ul><li>NOT:</li><ul><li>mil = 1</li></ul></ul><li>set country flag [beastbane_trial_fey_fight_failure](../flags/beastbane_trial_fey_fight_failure.md)</li></ul></ul><li>the event [Trial of Castan II Beastbane: Ambushed!](../events/trial_of_castan_ii_beastbane_ambushed.md) happens</li></ul></ul>

___
##Forward, to the den of the beast!

###Available if:
<li>has country flag [beastbane_trial_fey_success](../flags/beastbane_trial_fey_success.md)</li>

###Efects:<ul><li>If has country flag is [beastbane_trial_tracking_failure](../flags/beastbane_trial_tracking_failure.md):</li><ul><li>set country flag [beastbane_trial_beast_hunting](../flags/beastbane_trial_beast_hunting.md)</li></ul><li>else:</li><ul><li>set country flag [beastbane_trial_beast_asleep](../flags/beastbane_trial_beast_asleep.md)</li></ul><li>the event [Trial of Castan II Beastbane: The Basilisk Appears](../events/trial_of_castan_ii_beastbane_the_basilisk_appears.md) happens</li></ul>
