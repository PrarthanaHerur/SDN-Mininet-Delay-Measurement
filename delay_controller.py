from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
mac_to_port = {}

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", event.dpid)

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    dpid = event.connection.dpid
    in_port = event.port

    mac_to_port.setdefault(dpid, {})
    mac_to_port[dpid][packet.src] = in_port

    ip_packet = packet.find('ipv4')

    # 🚫 BLOCK h1 → h3
    if ip_packet:
        src_ip = str(ip_packet.srcip)
        dst_ip = str(ip_packet.dstip)

        if src_ip == "10.0.0.1" and dst_ip == "10.0.0.3":
            log.info("🚫 Blocking h1 -> h3")

            msg = of.ofp_flow_mod()
            msg.priority = 65535
            msg.match.dl_type = 0x0800
            msg.match.nw_src = ip_packet.srcip
            msg.match.nw_dst = ip_packet.dstip

            # No action = DROP
            event.connection.send(msg)
            return

    # ✅ NORMAL FORWARDING
    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow rule
    msg = of.ofp_flow_mod()
    msg.match.dl_dst = packet.dst
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("🚀 SDN Controller Running (FINAL)")
