# fullrun.py

top_of_rack_switch_name = 'r07r13-tors.sjc23.lint'
top_of_rack_switch_interface = 'Gi1/0/35'

#find_this_IP = '00c0.b7c8.8295'
location_of_rack = 'R07R13'
Which_PDU = 'PDU1'
#IP_for_infoblox = '100.119.12.118'
#MAC_for_infoblox = '00c0.b7c8.8258'

import cmdrunner
mac_address = cmdrunner.get_mac_addr_from_TORS(top_of_rack_switch_name, top_of_rack_switch_interface)
print ("The MAC Address is " + mac_address)

import Core_script
# Making a temporary hack to deal with the stpuid core outage we have all the time. BOO CORE.
IP_address = '100.119.15.171'
#IP_address = Core_script.get_IP_from_MAC(mac_address)

print ("The IP for this MAC " + IP_address)

import csv_file
Intended_IP = csv_file.get_intended_IP_add(location_of_rack, Which_PDU)
print ("The intended IP is " + Intended_IP)

import API_request
Infoblox = API_request.Assign_on_infoblox(IP_address, mac_address)
print ("The output for Infoblox " + Infoblox)

import check_apc_type
Check_model = check_apc_type.checking_pw_model(IP_address)
print ("This PDU is " + Check_model)


#try and except 
