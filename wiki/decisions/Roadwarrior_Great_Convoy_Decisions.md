This is a list of all [decisions](decisions.md) in the category "Roadwarrior_Great_Convoy_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="roadwarrior_upgrades">Upgrade the Great Convoy</a><br />** | <li>if:</li><ul><li>limit:</li><ul><li>None of the following:</li><ul><li>has reform roadwarrior_upgrades_on_the_go</li></ul></ul><li>capital scope:</li><ul><li>Any of the following:</li><ul><li>has terrain dwarven_hold</li><li>has terrain  dwarven_hold_surface</li></ul></ul></ul><li>None of the following:</li><ul><li>has country modifier roadwarrior_upgrading</li></ul> | <li>the event [Upgrading Our Crew](../events/upgrading_our_crew.md) happens</li> | <li>Country is Roadwarrior</li><li>has reform roadwarrior_great_convoy</li> |
| <a name="roadwarrior_teleport">Overdrive the Engine</a><br />** | <li>capital scope:</li><ul><li>Any of the following:</li><ul><li>has terrain dwarven_hold</li><li>has terrain  dwarven_hold_surface</li><li>has terrain   dwarven_road</li></ul></ul><li>None of the following:</li><ul><li>is at war</li></ul><li>NOT:</li><ul><li>has country modifier roadwarrior_recent_overdrive</li></ul> | <li>the event [Overdrive the Engine](../events/overdrive_the_engine.md) happens</li> | <li>Country is Roadwarrior</li><li>has reform roadwarrior_great_convoy</li> |
| <a name="roadwarrior_settle_down">§TGreat Convoy:§! Settle the Convoy</a><br />** | <li>capital scope:</li><ul><li>Any of the following:</li><ul><li>has terrain dwarven_hold</li><li>has terrain  dwarven_hold_surface</li></ul></ul><li>None of the following:</li><ul><li>has country modifier roadwarrior_upgrading</li></ul> | <li>the event [Settle the Convoy](../events/settle_the_convoy.md) happens</li> | <li>Country is Roadwarrior</li><li>has reform roadwarrior_great_convoy</li> |