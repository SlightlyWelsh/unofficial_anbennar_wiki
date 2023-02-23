This page has the same name as others. For full listing see bottom of [the base page](dummy_text22222.md).

#Information
 - Title: Dummy text
 - ID: kobold_tolerance_events.0
#Description
Dummy text
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 10 if has country modifier is racial focus kobold

#Options

___
##Unnamed Option

###One of the following randomly happens:
Outcome 1:

Available if <li>any owned province:</li><ul><li>has kobold minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier kobold_bands_recruited</li></ul><li>NOT:</li><ul><li>has province modifier kobold_scared_into_submission</li></ul><li>NOT:</li><ul><li>has province modifier kobold_angered_by_attempts_to_submit</li></ul></ul>

The weight of this outcome is 1
 - Multiplied by 0.5 if has high tolerance kobold race trigger is yes

The weight of this outcome is 1
 - Multiplied by 1.5 if does not have stability is 0

This outcome causes the following effects:<ul><li>the event [Kobold Bands](../events/kobold_bands.md) happens</li></ul>
Outcome 2:

Available if <li>is at war</li><li>any owned province:</li><ul><li>None of the following:</li><ul><li>has province modifier kobold_bands_punished_harshly</li></ul><li>NOT:</li><ul><li>has province modifier kobold_bands_punished</li></ul><li>NOT:</li><ul><li>has province modifier kobold_bands_not_punished</li></ul><li>has kobold minority trigger yes</li></ul>

The weight of this outcome is 1 
 - Multiplied by 0.5 if has high tolerance kobold race trigger is yes

The weight of this outcome is 1 
 - Multiplied by 1.5 if does not have stability is 1

The weight of this outcome is 1 
 - Multiplied by 1.5 if does not have manpower percentage is 0.5

This outcome causes the following effects:<ul><li>the event [Kobold Sabotage Recruitment in [kobold_hindering_military_operations.GetName]](../events/kobold_sabotage_recruitment_in_kobold_hindering_military_operations_getname.md) happens</li></ul>
Outcome 3:

Available if <li>any owned province:</li><ul><li>has kobold minority trigger yes</li></ul>

The weight of this outcome is 1  
 - Multiplied by 1.5 if has low tolerance kobold race trigger is yes

The weight of this outcome is 1  
 - Multiplied by 0.5 if has high tolerance kobold race trigger is yes

This outcome causes the following effects:<ul><li>the event [Kobolds Treated Like Pests](../events/kobolds_treated_like_pests.md) happens</li></ul>
Outcome 4:

The weight of this outcome is 1   
 - Multiplied by 1.5 if has medium tolerance kobold race trigger is yes

The weight of this outcome is 1   
 - Multiplied by 2 if has high tolerance kobold race trigger is yes

This outcome causes the following effects:<ul><li>the event [Kobold Minister](../events/kobold_minister.md) happens</li></ul>
Outcome 5:

The weight of this outcome is 1    
 - Multiplied by 1.1 if has years of income is 0.5

The weight of this outcome is 1    
 - Multiplied by 1.2 if has years of income is 1

The weight of this outcome is 1    
 - Multiplied by 1.5 if has years of income is 2

This outcome causes the following effects:<ul><li>the event [Kobolds Rob a Bank!](../events/kobolds_rob_a_bank.md) happens</li></ul>
Outcome 6:

Available if <li>any owned province:</li><ul><li>has any kobold pop trigger yes</li><li>None of the following:</li><ul><li>has province modifier kobold_inventions_unsafe</li></ul><li>NOT:</li><ul><li>has province modifier kobold_inventions_OSHA_approved</li></ul></ul><li>has estate estate_artificers</li>

The weight of this outcome is 1     
 - Multiplied by 0.1 if does not have year is 1500

The weight of this outcome is 1     
 - Multiplied by 1.25 if is year is 1600

The weight of this outcome is 1     
 - Multiplied by 1.5 if is year is 1700

This outcome causes the following effects:<ul><li>the event [Kobold Tinkers Release New Invention](../events/kobold_tinkers_release_new_invention.md) happens</li></ul>
Outcome 7:

The weight of this outcome is 1      
 - Multiplied by 1.5 if has low tolerance kobold race trigger is yes

This outcome causes the following effects:<ul><li>the event [Kobold Hoard Found by Mob](../events/kobold_hoard_found_by_mob.md) happens</li></ul>
Outcome 8:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Kobold Tunnels Cause Building Collapse](../events/kobold_tunnels_cause_building_collapse.md) happens</li></ul>
Outcome 9:

Available if <li>any owned province:</li><ul><li>has kobold minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier kobold_burrows</li></ul></ul>

The weight of this outcome is 1        
 - Multiplied by 2 if has any owned province has construction is building, and any owned province has kobold minority trigger is yes

This outcome causes the following effects:<ul><li>the event [Burrows in the Way of New Building](../events/burrows_in_the_way_of_new_building.md) happens</li></ul>
Outcome 10:

Available if <li>any owned province:</li><ul><li>has kobold minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier kobold_pesky_traps</li></ul></ul>

The weight of this outcome is 1         
 - Multiplied by 1.5 if has low tolerance kobold race trigger is yes

The weight of this outcome is 1         
 - Multiplied by 0.1 if has high tolerance kobold race trigger is yes

The weight of this outcome is 1         
 - Multiplied by 1.5 if does not have stability is 0

This outcome causes the following effects:<ul><li>the event [Pesky Kobold Traps!](../events/pesky_kobold_traps.md) happens</li></ul>
