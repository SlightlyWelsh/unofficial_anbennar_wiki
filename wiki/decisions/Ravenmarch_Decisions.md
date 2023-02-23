This is a list of all [decisions](decisions.md) in the category "Ravenmarch_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="ravenmarch_attack_folly">Prepare the Reconquest of Dostanor</a><br />*Let our officers know it is time to strike at those who wrongfully squat on our Dostanor, and that petty prince of the Empire cannot expect aid from their emperor!* | <li>is not at war</li><li>any neighbor country:</li><ul><li>Any of the following:</li><ul><li>any owned province:</li><ul><li>region is daravans_folly_region</li></ul><li>owns 447</li></ul></ul><li>manpower percentage is at least 0.75</li><li>None of the following:</li><ul><li>war exhaustion is at least 0.1</li></ul><li>NOT:</li><ul><li>any neighbor country:</li><ul><li>any owned province:</li><ul><li>region is daravans_folly_region</li></ul><li>truce with is PREV</li></ul></ul> | <li>custom tooltip = The Emperor will not defend any imperial prince that unlawfully owns any part of Dostanor, and will white peace from the war after one day. However, the war targets other allies will still fight.</li><li>If random neighbor country has any owned province has region is daravans folly region:</li><ul><li>save event target as = ravenmarch_war_target</li></ul><li>declare war with cb:</li><ul><li>who = event_target:ravenmarch_war_target</li><li>casus belli = cb_annex</li></ul><li>set country flag [folly_attacked](../flags/folly_attacked.md)</li><li>hidden effect:</li><ul><li>emperor:</li><ul><li>the event [Peace Out Emperor](../events/peace_out_emperor.md) happens</li></ul></ul> | <li>mission completed is ravenmarch_homeward_bound</li><li>None of the following:</li><ul><li>has country flag [folly_attacked](../flags/folly_attacked.md)</li></ul><li>any neighbor country:</li><ul><li>Any of the following:</li><ul><li>any owned province:</li><ul><li>region is daravans_folly_region</li></ul><li>owns 447</li><li>None of the following:</li><ul><li>is subject of is this nation</li></ul></ul></ul> |
| <a name="ravenmarch_change_triumvirate_court">Pray to the Triumvirate</a><br />*Perhaps it is time to re-dedicate our prayers and tithes to another god of the Triumvirate Court?* | <li>None of the following:</li><ul><li>has country modifier ravenmarch_triumvirate_court_ryalan_dominance</li></ul><li>NOT:</li><ul><li>has country modifier ravenmarch_triumvirate_court_corin_dominance</li></ul><li>NOT:</li><ul><li>has country modifier ravenmarch_triumvirate_court_nerat_dominance</li></ul> | <li>the event [Blessings of the Triumvirate Court](../events/blessings_of_the_triumvirate_court.md) happens</li> | <li>has reform ravenmarch_triumvirate_court</li> |