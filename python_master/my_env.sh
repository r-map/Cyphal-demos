export UAVCAN__NODE__ID=43                            # Set the local node-ID 43 (anonymous by default)
export UAVCAN__SUB__VOLTAGE__ID=2347                  # Subject "tempe"    on ID 2347
export UAVCAN__PUB__TEMPERATURE__ID=2346              # Subject "voltage"          on ID 2346
export UAVCAN__MODEL__ENVIRONMENT__TEMPERATURE=300.0  # Service "least_squares"           on ID 123
export UAVCAN__DIAGNOSTIC__SEVERITY=2                 # This is optional to enable logging via Cyphal

export UAVCAN__CAN__IFACE="socketcan:vcan0"
export UAVCAN__SERIAL__IFACE=""
#export UAVCAN__UDP__IFACE=127.9.0.0                  # Use Cyphal/UDP transport via 127.9.0.43 (sic!)
export UAVCAN__UDP__IFACE=""                          # Use Cyphal/UDP transport via 127.9.0.43 (sic!)
