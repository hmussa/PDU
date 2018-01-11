# fullrun.py

top_of_rack_switch_name = 'r07r12-tors.sjc23.lint'
top_of_rack_switch_interface = 'Gi1/0/36'



#find_this_IP = '00c0.b7c8.8295'
location_of_rack = 'R07R12'
Which_PDU = 'PDU2'
#IP_for_infoblox = '100.119.12.118'
#MAC_for_infoblox = '00c0.b7c8.8258'

import cmdrunner
mac_address = cmdrunner.get_mac_addr_from_TORS(top_of_rack_switch_name, top_of_rack_switch_interface)
print ("The MAC Address is " + mac_address)

import Core_script
#Making a temporary hack to deal with the stpuid core outage we have all the time. BOO CORE.
#Bad_IP_address = '100.119.15.170'
Bad_IP_address = Core_script.get_IP_from_MAC(MAC_for_infoblox)
print ("The IP for this MAC " + Bad_IP_address)

import Check_apc_type
Check_model = Check_apc_type.checking_pw_model(Bad_IP_address)
#print ("This PDU is " + Check_model)

import csv_file
Good_IP_address = csv_file.get_intended_IP_add(location_of_rack, Which_PDU)
print ("The intended IP is " + Good_IP_address)

from apceditinfoblox import editHostIPv4AddrForDHCPFromIP
status = editHostIPv4AddrForDHCPFromIP('infoblox.lint', 'hmussa', 'Ty91g3!6' ,Good_IP_address, mac_address)
if status:
  print ("Success!")
else:
  print ("Fail")   



#reset after 