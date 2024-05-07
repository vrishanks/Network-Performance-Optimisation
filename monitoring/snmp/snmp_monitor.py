from pysnmp.hlapi import *

def get_snmp_data(oid, host="localhost", community="public", port=161):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=0),
        UdpTransportTarget((host, port)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        return {'error': errorIndication}
    elif errorStatus:
        return {'error': '%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?')}
    else:
        results = {}
        for varBind in varBinds:
            oid_str = varBind[0].prettyPrint()
            value_str = varBind[1].prettyPrint()
            results[oid_str] = value_str
        return results

if __name__ == "__main__":
    oid = '1.3.6.1.2.1.1.3.0'
    host = '172.20.10.2'
    community = 'public'
    port = 161

    result = get_snmp_data(oid, host, community, port)

    if 'error' in result:
        print("Error:", result['error'])
    else:
        print("SNMP Data:")
        for oid, value in result.items():
            print(f"{oid} = {value}")