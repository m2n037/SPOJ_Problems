#!/usr/bin/tclsh

# This code is for SPOJ TEST problem. This uses the for loop. This is not an 
# accepted solution as it doesn't ask for an input which is necessary to pass 
# the test.

set lst_1 [list 1 2 88 42 99]

set lst_2 [list ]

for {set i 0} {[lindex $lst_1 $i] != 42} {incr i} {
	lappend lst_2 [lindex $lst_1 $i]
}

puts $lst_2
