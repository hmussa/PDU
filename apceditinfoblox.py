from pyinfoblox import InfobloxWAPI

def getHostIPv4AddrIdentFromIP(infoblox_url, infoblox_username, infoblox_password, target_ipv4, infoblox_verify_ssl = False):
    try:
        infoblox = InfobloxWAPI(username=infoblox_username, password=infoblox_password, wapi='https://'+ infoblox_url + '/wapi/v2.7/', verify=infoblox_verify_ssl)
        host_ipv4addr = infoblox.record_host_ipv4addr.get()
    except:
        # For some reason we can't connect to Infoblox
        return False

    found_target_ipv4 = False
    for entry in host_ipv4addr:
        if entry['ipv4addr'] == target_ipv4:
            return entry['_ref']
    # Unable to find the IPv4 address in the returned array. That's an issue
    return False

def editHostIPv4AddrForDHCP(infoblox_url, infoblox_username, infoblox_password, record_host_ipv4_reference, mac_address, infoblox_verify_ssl = False):
    try:
        infoblox = InfobloxWAPI(username=infoblox_username, password=infoblox_password, wapi='https://'+ infoblox_url + '/wapi/v2.7/', verify=infoblox_verify_ssl)
        return_ref = infoblox.record_host_ipv4addr.update(objref=record_host_ipv4_reference, configure_for_dhcp=True, mac=mac_address)
        return return_ref
    except:
        # For some reason we can't connect to Infoblox
        return False

def restartInfobloxGrid(infoblox_url, infoblox_username, infoblox_password, infoblox_verify_ssl = False):
    try:
        infoblox = InfobloxWAPI(username=infoblox_username, password=infoblox_password, wapi='https://'+ infoblox_url + '/wapi/v2.7/', verify=infoblox_verify_ssl)
        grids = infoblox.grid.get()
        grid = grids[0]['_ref']
        return_ref = infoblox.grid.function(objref=grid, _function='restartservices', member_order='SEQUENTIALLY', restart_option='RESTART_IF_NEEDED', sequential_delay=10, service_option='ALL')
        if return_ref == {}:
            return True
        else:
            return False
    except:
        return False

def editHostIPv4AddrForDHCPFromIP(infoblox_url, infoblox_username, infoblox_password, target_ipv4, mac_address, infoblox_verify_ssl = False):
    reference_get = getHostIPv4AddrIdentFromIP(infoblox_url, infoblox_username, infoblox_password, target_ipv4)
    if not reference_get:
        print ("Getting the record:host_ipv4addr reference failed.")
        return False
    reference_edit = editHostIPv4AddrForDHCP(infoblox_url, infoblox_username, infoblox_password, reference_get, mac_address)
    if not reference_edit:
        print ("Editing the record:host_ipv4addr reference failed.")
        return False
    reference_restart = restartInfobloxGrid(infoblox_url, infoblox_username, infoblox_password)
    if not reference_restart:
        print ("Restarting the Grid failed.")
        return False
    return True

# Testing Section. Leave commented for normal operation
#uname = 'username'
#passw = 'password'
#infbl = 'infoblox.lint'
#infbl = 'bad-infoblox.lint'
#targe = '100.119.12.117'
#macad = '00:c0:b7:c8:82:95'

#reference = getHostIPv4AddrIdentFromIP(infbl, uname, passw, targe)
#response = editHostIPv4AddrForDHCP(infbl, uname, passw, reference, macad)
#restartInfobloxGrid(infbl, uname, passw)
#main_ref = editHostIPv4AddrForDHCPFromIP(infbl, uname, passw, targe, macad)