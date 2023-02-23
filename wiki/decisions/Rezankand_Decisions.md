This is a list of all [decisions](decisions.md) in the category "Rezankand_Decisions"

| Decision | Completion requirements | Effects | Requirements to appear |
| ----- | ------ | ----- | ------ |
| <a name="capital_census_decision">Military Census</a><br />*Establishing an efficient and centralized census is essential to maintain an effective army* | <li>is not at war</li><li>mil power is at least 75</li><li>years of income is at least 0.5</li><li>None of the following:</li><ul><li>has country modifier militarizing_the_capital</li></ul> | <li>add mil power = -75</li><li>add years of income = -0.5</li><li>capital scope:</li><ul><li>add province modifier:</li><ul><li>name = rezankand_militarize_census</li><li>duration = -1</li></ul></ul><li>country gets the modifier militarizing_the_capital for 2 years</li><li>hidden effect:</li><ul><li>set country flag [rezankand_militarize_census](../flags/rezankand_militarize_census.md)</li></ul> | <li>Country is Rezankand</li><li>has country flag [rezankand_militarize_capital](../flags/rezankand_militarize_capital.md)</li><li>None of the following:</li><ul><li>has country flag [rezankand_militarize_census](../flags/rezankand_militarize_census.md)</li></ul> |
| <a name="capital_fortified_wall_decision">Fortify the Outer Wall</a><br />*In order to protect our capital in all circumstances, we must build strong walls around it.* | <li>is not at war</li><li>mil power is at least 75</li><li>years of income is at least 0.5</li><li>None of the following:</li><ul><li>has country modifier militarizing_the_capital</li></ul> | <li>add mil power = -75</li><li>add years of income = -0.5</li><li>capital scope:</li><ul><li>add province modifier:</li><ul><li>name = rezankand_militarize_wall</li><li>duration = -1</li></ul></ul><li>country gets the modifier militarizing_the_capital for 2 years</li><li>hidden effect:</li><ul><li>set country flag [rezankand_militarize_wall](../flags/rezankand_militarize_wall.md)</li></ul> | <li>Country is Rezankand</li><li>has country flag [rezankand_militarize_capital](../flags/rezankand_militarize_capital.md)</li><li>None of the following:</li><ul><li>has country flag [rezankand_militarize_wall](../flags/rezankand_militarize_wall.md)</li></ul> |
| <a name="capital_officier_corp_decision">The Rezan Military Academy</a><br />*What is an army if it is not led by the cream of the crop. Let's make sure we never miss an officer.* | <li>is not at war</li><li>mil power is at least 75</li><li>years of income is at least 0.5</li><li>None of the following:</li><ul><li>has country modifier militarizing_the_capital</li></ul> | <li>add mil power = -75</li><li>add years of income = -0.5</li><li>capital scope:</li><ul><li>add province modifier:</li><ul><li>name = rezankand_officier_academy</li><li>duration = -1</li></ul></ul><li>country gets the modifier militarizing_the_capital for 2 years</li><li>hidden effect:</li><ul><li>set country flag [rezankand_officier_academy](../flags/rezankand_officier_academy.md)</li></ul> | <li>Country is Rezankand</li><li>has country flag [rezankand_militarize_capital](../flags/rezankand_militarize_capital.md)</li><li>None of the following:</li><ul><li>has country flag [rezankand_officier_academy](../flags/rezankand_officier_academy.md)</li></ul> |
| <a name="forge_dazinare_decision">Forge Dazinare</a><br />*We need a Sword fit for our [Root.Monarch.GetTitle]* | <li>is not at war</li><li>mil power is at least 75</li><li>dip power is at least 75</li><li>adm power is at least 75</li><li>years of income is at least 0.3</li><li>None of the following:</li><ul><li>has country modifier militarizing_the_capital</li></ul> | <li>add mil power = -75</li><li>add dip power = -75</li><li>add adm power = -75</li><li>add years of income = -0.3</li><li>custom tooltip = §GForging this sword will allow us to further increase the power of our [Root.Monarch.GetTitle]§!</li><li>hidden effect:</li><ul><li>set country flag [rezankand_sword_done](../flags/rezankand_sword_done.md)</li></ul> | <li>Country is Rezankand</li><li>has country flag [rezankand_can_forge_sword](../flags/rezankand_can_forge_sword.md)</li><li>None of the following:</li><ul><li>has country flag [rezankand_sword_done](../flags/rezankand_sword_done.md)</li></ul> |