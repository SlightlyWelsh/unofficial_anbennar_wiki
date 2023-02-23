#Information
 - Title: Chess Tournament - Start
 - ID: flavor_toarnen.30
#Description
Chess Tournament - Start
#Options

___
##Everyone is ready! Let's go!

###Available if:
<li>has country flag [chess_tournament_tmp_flag](../flags/chess_tournament_tmp_flag.md)</li>

###Efects:<ul><li>hidden effect:</li><ul><li>clr country flag [chess_tournament_tmp_flag](../flags/chess_tournament_tmp_flag.md)</li></ul><li>If every country has country flag is [chess_tournament_participant](../flags/chess_tournament_participant.md):</li><ul><li>the event [Choose your Move](../events/choose_your_move.md) happens</li><li>hidden effect:</li><ul><li>the event [Chess Match Result](../events/chess_match_result.md) happens</li></ul></ul><li>hidden effect:</li><ul><li>the event [Chess Tournament - Second Round Begins](../events/chess_tournament_second_round_begins.md) happens</li></ul></ul>

___
##We are still looking for participants.

###Available if:
<li>None of the following:</li><ul><li>has country flag [chess_tournament_tmp_flag](../flags/chess_tournament_tmp_flag.md)</li></ul><li>any known country:</li><ul><li>capital scope:</li><ul><li>continent is europe</li></ul><li>None of the following:</li><ul><li>has country flag [chess_tournament_got_invitation](../flags/chess_tournament_got_invitation.md)</li></ul><li>NOT:</li><ul><li>has country modifier monstrous_nation</li></ul></ul>

###Efects:<ul><li>the event [Chess Tournament - Start](../events/chess_tournament_start.md) happens</li></ul>

___
##There is not enough countries left.

###Available if:
<li>None of the following:</li><ul><li>has country flag [chess_tournament_tmp_flag](../flags/chess_tournament_tmp_flag.md)</li></ul><li>NOT:</li><ul><li>any known country:</li><ul><li>capital scope:</li><ul><li>continent is europe</li></ul><li>None of the following:</li><ul><li>has country flag [chess_tournament_got_invitation](../flags/chess_tournament_got_invitation.md)</li></ul><li>NOT:</li><ul><li>has country modifier monstrous_nation</li></ul></ul></ul>
