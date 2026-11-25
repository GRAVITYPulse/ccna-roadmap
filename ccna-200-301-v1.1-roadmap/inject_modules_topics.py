from __future__ import annotations

from pathlib import Path

ROOT_NAME = "ccna-200-301-v1.1-roadmap"
START_MARKER = "<!-- TOPICS:START -->"
END_MARKER = "<!-- TOPICS:END -->"

MODULE_TOPICS: dict[tuple[str, str], tuple[str, ...]] = {
    ("01-network-fundamentals", "mod-01-network-components.md"): (
        "Routers, L2 switches, and L3 switches (control plane vs. data plane, SVIs, routed ports)",
        "NGFW and IPS inline vs. passive inspection roles",
        "Access points (autonomous vs. centralized/lightweight), WLC, Catalyst Center (DNA Center), endpoints, servers",
        "PoE standards (802.3af 15.4W, 802.3at 30W, 802.3bt 60W/90W) and PSE/PD negotiation",
    ),
    ("01-network-fundamentals", "mod-02-topology-architectures.md"): (
        "Two-tier (collapsed core) vs. three-tier (core, distribution, access)",
        "Spine-leaf east-west traffic and ECMP",
        "WAN topologies, SOHO, on-premises, and cloud models",
    ),
    ("01-network-fundamentals", "mod-03-physical-media-issues.md"): (
        "Single-mode fiber, multimode fiber, and copper UTP cabling characteristics",
        "Point-to-point vs. shared media segments",
        "Collisions, late collisions, runts, giants, CRC errors, and speed/duplex mismatches",
    ),
    ("01-network-fundamentals", "mod-04-tcp-udp-transport.md"): (
        "TCP 3-way handshake, sequence/ACK numbers, flow control/windowing, and reliability",
        "UDP connectionless delivery, low overhead, and common port use cases",
    ),
    ("01-network-fundamentals", "mod-05-ipv4-addressing-subnetting.md"): (
        "CIDR/VLSM subnet boundaries, usable host ranges, broadcast addresses, and wildcard masks",
        "RFC 1918 private IPv4 ranges and APIPA (169.254.0.0/16)",
    ),
    ("01-network-fundamentals", "mod-06-ipv6-addressing.md"): (
        "IPv6 formatting/compression and prefix lengths",
        "Unicast (Global Unicast, Unique Local, Link-Local), Anycast, Multicast, and Modified EUI-64",
    ),
    ("01-network-fundamentals", "mod-07-client-ip-verification.md"): (
        "IP address, subnet/prefix, default gateway, and DNS verification on Windows, macOS, and Linux",
    ),
    ("01-network-fundamentals", "mod-08-wireless-principles.md"): (
        "Non-overlapping channels (2.4 GHz 1, 6, 11; 5 GHz channel widths), SSID/BSSID, RF behavior (attenuation, reflection, absorption, interference), and encryption basics",
    ),
    ("01-network-fundamentals", "mod-09-virtualization-vrfs.md"): (
        "Hypervisors/server VMs, containers, and Virtual Routing and Forwarding (VRF) isolation",
    ),
    ("01-network-fundamentals", "mod-10-switching-concepts.md"): (
        "MAC address learning, 300s aging timer, frame flooding, frame forwarding, and MAC table lookup",
    ),
    ("02-network-access", "mod-01-vlans-and-intervlan.md"): (
        "Normal-range VLANs (1-1005), data and voice access ports, and default VLAN behavior",
        "Inter-VLAN routing via Router-on-a-Stick and Layer 3 switch SVIs",
    ),
    ("02-network-access", "mod-02-trunks-and-8021q.md"): (
        "Static trunk ports, DTP modes, 802.1Q tagging, allowed VLANs, and Native VLAN untagged frames/mismatches",
    ),
    ("02-network-access", "mod-03-cdp-and-lldp.md"): (
        "CDP and LLDP global/interface enablement and neighbor discovery (show cdp neighbors, show lldp neighbors)",
    ),
    ("02-network-access", "mod-04-etherchannel-lacp.md"): (
        "Layer 2 and Layer 3 EtherChannels, LACP active/passive modes, matching link parameters, and load-balancing methods",
    ),
    ("02-network-access", "mod-05-rapid-pvst-stp.md"): (
        "Root bridge election (primary/secondary), port roles (Root, Designated, Alternate, Backup) and states (Discarding, Learning, Forwarding)",
        "PortFast, BPDU Guard, BPDU Filter, Root Guard, and Loop Guard",
    ),
    ("02-network-access", "mod-06-cisco-wireless-arch.md"): (
        "Autonomous, WLC/CAPWAP, FlexConnect, and Mesh AP modes",
        "Physical wiring of APs and WLCs (access/trunk ports, LAG)",
    ),
    ("02-network-access", "mod-07-device-mgmt-and-wlan-gui.md"): (
        "Console, Telnet, SSH, HTTP/HTTPS, TACACS+/RADIUS, and cloud-managed access",
        "WLC GUI WLAN setup (SSID, security, QoS profiles, and advanced settings)",
    ),
    ("03-ip-connectivity", "mod-01-routing-table-logic.md"): (
        "Route codes, prefix/mask, next hop, Administrative Distance (AD), metric, and gateway of last resort",
        "Forwarding decision order: longest prefix match, lowest AD, lowest metric",
    ),
    ("03-ip-connectivity", "mod-02-ipv4-ipv6-static-routing.md"): (
        "IPv4 and IPv6 default routes, network routes, host routes, and floating static routes",
    ),
    ("03-ip-connectivity", "mod-03-single-area-ospfv2.md"): (
        "OSPFv2 neighbor states and adjacency requirements, Router ID selection, Point-to-Point vs. Broadcast, and DR/BDR election",
    ),
    ("03-ip-connectivity", "mod-04-fhrp-concepts.md"): (
        "First Hop Redundancy Protocol concepts (HSRP, VRRP, GLBP roles, virtual IP/MAC, timers, and preemption)",
    ),
    ("04-ip-services", "mod-01-nat-and-pat.md"): (
        "Inside/outside local and global addresses, ip nat inside/outside, Static NAT, Dynamic NAT pools, and PAT (overload)",
    ),
    ("04-ip-services", "mod-02-ntp-dhcp-dns.md"): (
        "NTP client/server mode and strata",
        "DHCP server/client/relay (ip helper-address) and DNS record/resolution roles",
    ),
    ("04-ip-services", "mod-03-snmp-and-syslog.md"): (
        "SNMPv2c/v3 polling (GET/SET), Traps/Informs, MIB/OIDs",
        "Syslog facilities and severity levels (0-7)",
    ),
    ("04-ip-services", "mod-04-qos-phb-fundamentals.md"): (
        "Classification, CoS/DSCP marking, queuing, congestion management/avoidance, policing, and shaping",
    ),
    ("04-ip-services", "mod-05-ssh-tftp-ftp.md"): (
        "SSHv2 configuration and line/crypto prerequisites",
        "TFTP vs. FTP transport and file transfer use cases",
    ),
    ("05-security-fundamentals", "mod-01-threats-and-sec-programs.md"): (
        "Threats, vulnerabilities, exploits, mitigations, security awareness/training, and physical access controls",
    ),
    ("05-security-fundamentals", "mod-02-access-control-and-aaa.md"): (
        "Local passwords/secrets, password complexity/management, MFA/certificates/biometrics, and AAA (Authentication, Authorization, Accounting)",
    ),
    ("05-security-fundamentals", "mod-03-ipsec-vpns.md"): (
        "Site-to-site vs. remote-access IPsec VPN concepts, IKE/SA phases, ESP/AH, and tunnel/transport modes",
    ),
    ("05-security-fundamentals", "mod-04-access-control-lists.md"): (
        "Standard vs. Extended ACLs, wildcard masks, implicit deny, direction (in/out), and interface placement",
    ),
    ("05-security-fundamentals", "mod-05-layer2-security.md"): (
        "Port Security (max MACs, sticky MACs, violation modes), DHCP Snooping (trusted/untrusted ports), and Dynamic ARP Inspection (DAI)",
    ),
    ("05-security-fundamentals", "mod-06-wireless-security.md"): (
        "WPA, WPA2, and WPA3 security features and configuring a WLAN GUI with WPA2-PSK",
    ),
    ("06-automation-programmability", "mod-01-sdn-and-controllers.md"): (
        "Automation impact on network management, traditional vs. controller-based networking, underlay/overlay/fabric, control vs. data plane separation, and Northbound/Southbound APIs",
    ),
    ("06-automation-programmability", "mod-02-ai-ml-in-netops.md"): (
        "Generative AI vs. predictive AI/ML use cases in network operations",
    ),
    ("06-automation-programmability", "mod-03-rest-apis-and-json.md"): (
        "REST API authentication, CRUD operations, HTTP verbs/status codes, and valid JSON syntax",
    ),
    ("06-automation-programmability", "mod-04-ansible-and-terraform.md"): (
        "Ansible vs. Terraform push/pull, agentless vs. agent, and procedural vs. declarative infrastructure management",
    ),
}


def format_topic_block(topics: tuple[str, ...]) -> str:
    bullet_lines = "\n".join(f"- {topic}" for topic in topics)
    return "\n".join(
        [
            "## Study Topics",
            START_MARKER,
            bullet_lines,
            END_MARKER,
        ]
    )


def inject_topics(base_dir: Path) -> None:
    root = base_dir / ROOT_NAME
    if not root.exists():
        raise FileNotFoundError(f"Roadmap directory not found: {root.resolve()}")

    updated_count = 0
    missing_count = 0

    for (domain, filename), topics in MODULE_TOPICS.items():
        target = root / domain / "01-modules" / filename
        if not target.exists():
            print(f"[MISSING] {target}")
            missing_count += 1
            continue

        content = target.read_text(encoding="utf-8")
        block = format_topic_block(topics)

        if START_MARKER in content and END_MARKER in content:
            start_idx = content.index(START_MARKER)
            end_idx = content.index(END_MARKER) + len(END_MARKER)
            prefix = content[:start_idx].rstrip()
            if prefix.endswith("## Study Topics"):
                prefix = prefix[: -len("## Study Topics")].rstrip()
            suffix = content[end_idx:].lstrip("\r\n")
            new_content = f"{prefix}\n\n{block}\n\n{suffix}" if suffix else f"{prefix}\n\n{block}\n"
        else:
            new_content = f"{content.rstrip()}\n\n{block}\n"

        if new_content != content:
            target.write_text(new_content, encoding="utf-8")
            updated_count += 1

    print(f"Done. Updated {updated_count} module files ({missing_count} missing).")


if __name__ == "__main__":
    inject_topics(Path.cwd())