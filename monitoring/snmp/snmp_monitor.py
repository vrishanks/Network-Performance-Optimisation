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
        print(errorIndication)
        return None
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        return None
    else:
        results = []
        for varBind in varBinds:
            result = f'{varBind[0].prettyPrint()} = {varBind[1].prettyPrint()}'
            print(result)
            results.append(result)
        return results

if __name__ == "__main__":
    get_snmp_data('1.3.6.1.2.1.1.3.0')