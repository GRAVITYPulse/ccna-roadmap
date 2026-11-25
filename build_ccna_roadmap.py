from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

ROOT_NAME = "ccna-200-301-v1.1-roadmap"


@dataclass(frozen=True)
class ModuleSpec:
    filename: str
    title: str
    objectives: tuple[str, ...]
    verify_commands: tuple[str, ...]


ROADMAP: dict[str, tuple[ModuleSpec, ...]] = {
    "00-study-workflow": (
        ModuleSpec(
            filename="8-week-sprint-tracker.md",
            title="8-Week Sprint Tracker (CCNA 200-301 v1.1)",
            objectives=(
                "60-90m Weekday CIR",
                "Friday Multi-Protocol Lab",
                "Sunday Hard Shutdown",
            ),
            verify_commands=("show clock", "show version"),
        ),
        ModuleSpec(
            filename="daily-75min-checklist.md",
            title="Daily 75-Minute Micro-Workflow Checklist",
            objectives=(
                "Block 1: Concept Ingestion (20m)",
                "Block 2: CLI Lab Execution (40m)",
                "Block 3: Active Recall & Anki Flush (15m)",
            ),
            verify_commands=("show running-config", "show ip interface brief"),
        ),
    ),
    "01-network-fundamentals": (
        ModuleSpec(
            filename="mod-01-network-components.md",
            title="Network Components & PoE (1.1)",
            objectives=(
                "1.1.a Routers",
                "1.1.b Layer 2 and Layer 3 switches",
                "1.1.c Next-generation firewalls and IPS",
                "1.1.d Access points",
                "1.1.e Controllers",
                "1.1.f Endpoints",
                "1.1.g Servers",
                "1.1.h PoE",
            ),
            verify_commands=("show inventory", "show power inline", "show ip route"),
        ),
        ModuleSpec(
            filename="mod-02-topology-architectures.md",
            title="Network Topology Architectures (1.2)",
            objectives=(
                "1.2.a Two-tier",
                "1.2.b Three-tier",
                "1.2.c Spine-leaf",
                "1.2.d WAN",
                "1.2.e Small office/home office (SOHO)",
                "1.2.f On-premises and cloud",
            ),
            verify_commands=("show cdp neighbors detail", "show ip protocols"),
        ),
        ModuleSpec(
            filename="mod-03-physical-media-issues.md",
            title="Physical Interfaces, Cabling & Link Issues (1.3 - 1.4)",
            objectives=(
                "1.3.a Single-mode fiber, multimode fiber, copper",
                "1.3.b Connections (Ethernet shared media and point-to-point)",
                "1.4 Identify interface and cable issues (collisions, errors, mismatch duplex, and/or speed)",
            ),
            verify_commands=(
                "show interfaces status",
                "show interfaces counters errors",
                "show controllers",
            ),
        ),
        ModuleSpec(
            filename="mod-04-tcp-udp-transport.md",
            title="TCP vs UDP Comparison (1.5)",
            objectives=("1.5 Compare TCP to UDP",),
            verify_commands=("show tcp brief", "show udp"),
        ),
        ModuleSpec(
            filename="mod-05-ipv4-addressing-subnetting.md",
            title="IPv4 Addressing, Subnetting & Private Ranges (1.6 - 1.7)",
            objectives=(
                "1.6 Configure and verify IPv4 addressing and subnetting",
                "1.7 Describe private IPv4 addressing",
            ),
            verify_commands=(
                "show ip interface brief",
                "show running-config | include ip address",
            ),
        ),
        ModuleSpec(
            filename="mod-06-ipv6-addressing.md",
            title="IPv6 Addressing, Prefixes & Address Types (1.8 - 1.9)",
            objectives=(
                "1.8 Configure and verify IPv6 addressing and prefix",
                "1.9.a Unicast (global, unique local, and link local)",
                "1.9.b Anycast",
                "1.9.c Multicast",
                "1.9.d Modified EUI 64",
            ),
            verify_commands=("show ipv6 interface brief", "show ipv6 route"),
        ),
        ModuleSpec(
            filename="mod-07-client-ip-verification.md",
            title="Client OS IP Verification (1.10)",
            objectives=(
                "1.10 Verify IP parameters for Client OS (Windows, Mac OS, Linux)",
            ),
            verify_commands=(
                "ipconfig /all",
                "ifconfig / if addr",
                "netstat -rn / ip route",
            ),
        ),
        ModuleSpec(
            filename="mod-08-wireless-principles.md",
            title="Wireless Principles (1.11)",
            objectives=(
                "1.11.a Nonoverlapping Wi-Fi channels",
                "1.11.b SSID",
                "1.11.c RF",
                "1.11.d Encryption",
            ),
            verify_commands=("show dot11 associations", "show controllers dot11Radio 0"),
        ),
        ModuleSpec(
            filename="mod-09-virtualization-vrfs.md",
            title="Virtualization Fundamentals & VRFs (1.12)",
            objectives=(
                "1.12 Explain virtualization fundamentals (server virtualization, containers, and VRFs)",
            ),
            verify_commands=("show vrf", "show ip route vrf all"),
        ),
        ModuleSpec(
            filename="mod-10-switching-concepts.md",
            title="Switching Concepts (1.13)",
            objectives=(
                "1.13.a MAC learning and aging",
                "1.13.b Frame switching",
                "1.13.c Frame flooding",
                "1.13.d MAC address table",
            ),
            verify_commands=(
                "show mac address-table",
                "show mac address-table aging-time",
            ),
        ),
    ),
    "02-network-access": (
        ModuleSpec(
            filename="mod-01-vlans-and-intervlan.md",
            title="VLANs & InterVLAN Connectivity (2.1)",
            objectives=(
                "2.1.a Access ports (data and voice)",
                "2.1.b Default VLAN",
                "2.1.c InterVLAN connectivity",
            ),
            verify_commands=(
                "show vlan brief",
                "show interfaces switchport",
                "show ip interface brief",
            ),
        ),
        ModuleSpec(
            filename="mod-02-trunks-and-8021q.md",
            title="Interswitch Connectivity, Trunks, 802.1Q & Native VLAN (2.2)",
            objectives=(
                "2.2.a Trunk ports",
                "2.2.b 802.1Q",
                "2.2.c Native VLAN",
            ),
            verify_commands=(
                "show interfaces trunk",
                "show interfaces gig0/1 switchport",
            ),
        ),
        ModuleSpec(
            filename="mod-03-cdp-and-lldp.md",
            title="Layer 2 Discovery Protocols: CDP & LLDP (2.3)",
            objectives=(
                "2.3 Configure and verify Layer 2 discovery protocols (Cisco Discovery Protocol and LLDP)",
            ),
            verify_commands=("show cdp neighbors", "show lldp neighbors detail"),
        ),
        ModuleSpec(
            filename="mod-04-etherchannel-lacp.md",
            title="Layer 2 / Layer 3 EtherChannel with LACP (2.4)",
            objectives=(
                "2.4 Configure and verify (Layer 2/Layer 3) EtherChannel (LACP)",
            ),
            verify_commands=("show etherchannel summary", "show lacp neighbor"),
        ),
        ModuleSpec(
            filename="mod-05-rapid-pvst-stp.md",
            title="Rapid PVST+ Spanning Tree Protocol (2.5)",
            objectives=(
                "2.5.a Root port, root bridge (primary/secondary), and other port names",
                "2.5.b Port states and roles",
                "2.5.c PortFast",
                "2.5.d Root guard, loop guard, BPDU filter, and BPDU guard",
            ),
            verify_commands=(
                "show spanning-tree",
                "show spanning-tree root",
                "show spanning-tree summary",
            ),
        ),
        ModuleSpec(
            filename="mod-06-cisco-wireless-arch.md",
            title="Cisco Wireless Architectures & Physical Infrastructure (2.6 - 2.7)",
            objectives=(
                "2.6 Describe Cisco Wireless Architectures and AP modes",
                "2.7 Describe physical infrastructure connections of WLAN components (AP, WLC, access/trunk ports, and LAG)",
            ),
            verify_commands=("show etherchannel summary", "show interfaces trunk"),
        ),
        ModuleSpec(
            filename="mod-07-device-mgmt-and-wlan-gui.md",
            title="Device Management Access & WLAN GUI Configuration (2.8 - 2.9)",
            objectives=(
                "2.8 Describe network device management access (Telnet, SSH, HTTP, HTTPS, console, TACACS+/RADIUS, and cloud managed)",
                "2.9 Interpret the wireless LAN GUI configuration for client connectivity, such as WLAN creation, security settings, QoS profiles, and advanced settings",
            ),
            verify_commands=(
                "show ip ssh",
                "show running-config | section line vty",
            ),
        ),
    ),
    "03-ip-connectivity": (
        ModuleSpec(
            filename="mod-01-routing-table-logic.md",
            title="Routing Table Components & Forwarding Decisions (3.1 - 3.2)",
            objectives=(
                "3.1.a Routing protocol code",
                "3.1.b Prefix",
                "3.1.c Network mask",
                "3.1.d Next hop",
                "3.1.e Administrative distance",
                "3.1.f Metric",
                "3.1.g Gateway of last resort",
                "3.2.a Longest prefix match",
                "3.2.b Administrative distance",
                "3.2.c Routing protocol metric",
            ),
            verify_commands=("show ip route", "show ip cef"),
        ),
        ModuleSpec(
            filename="mod-02-ipv4-ipv6-static-routing.md",
            title="IPv4 & IPv6 Static Routing (3.3)",
            objectives=(
                "3.3.a Default route",
                "3.3.b Network route",
                "3.3.c Host route",
                "3.3.d Floating static",
            ),
            verify_commands=("show ip route static", "show ipv6 route static"),
        ),
        ModuleSpec(
            filename="mod-03-single-area-ospfv2.md",
            title="Single-Area OSPFv2 (3.4)",
            objectives=(
                "3.4.a Neighbor adjacencies",
                "3.4.b Point-to-point",
                "3.4.c Broadcast (DR/BDR selection)",
                "3.4.d Router ID",
            ),
            verify_commands=(
                "show ip ospf neighbor",
                "show ip ospf interface brief",
                "show ip protocols",
            ),
        ),
        ModuleSpec(
            filename="mod-04-fhrp-concepts.md",
            title="First Hop Redundancy Protocols (3.5)",
            objectives=(
                "3.5 Describe the purpose, functions, and concepts of first hop redundancy protocols",
            ),
            verify_commands=("show standby brief", "show standby"),
        ),
    ),
    "04-ip-services": (
        ModuleSpec(
            filename="mod-01-nat-and-pat.md",
            title="Inside Source NAT: Static, Pools & PAT (4.1)",
            objectives=(
                "4.1 Configure and verify inside source NAT using static and pools",
            ),
            verify_commands=("show ip nat translations", "show ip nat statistics"),
        ),
        ModuleSpec(
            filename="mod-02-ntp-dhcp-dns.md",
            title="NTP, DHCP Client/Relay & DNS (4.2 - 4.3, 4.6)",
            objectives=(
                "4.2 Configure and verify NTP operating in a client and server mode",
                "4.3 Explain the role of DHCP and DNS within the network",
                "4.6 Configure and verify DHCP client and relay",
            ),
            verify_commands=(
                "show ntp status",
                "show ntp associations",
                "show ip dhcp binding",
            ),
        ),
        ModuleSpec(
            filename="mod-03-snmp-and-syslog.md",
            title="SNMP & Syslog Operations (4.4 - 4.5)",
            objectives=(
                "4.4 Explain the function of SNMP in network operations",
                "4.5 Describe the use of syslog features, including facilities and severity levels",
            ),
            verify_commands=("show snmp", "show logging"),
        ),
        ModuleSpec(
            filename="mod-04-qos-phb-fundamentals.md",
            title="QoS Per-Hop Behavior (PHB) Fundamentals (4.7)",
            objectives=(
                "4.7 Explain the forwarding per-hop behavior (PHB) for QoS such as classification, marking, queuing, congestion, policing, and shaping",
            ),
            verify_commands=("show policy-map interface", "show class-map"),
        ),
        ModuleSpec(
            filename="mod-05-ssh-tftp-ftp.md",
            title="Remote Access via SSH & TFTP/FTP File Transfers (4.8 - 4.9)",
            objectives=(
                "4.8 Configure network devices for remote access using SSH",
                "4.9 Describe the capabilities and functions of TFTP/FTP in the network",
            ),
            verify_commands=("show ip ssh", "show users"),
        ),
    ),
    "05-security-fundamentals": (
        ModuleSpec(
            filename="mod-01-threats-and-sec-programs.md",
            title="Security Concepts & Program Elements (5.1 - 5.2)",
            objectives=(
                "5.1 Define key security concepts (threats, vulnerabilities, exploits, and mitigation techniques)",
                "5.2 Describe security program elements (user awareness, training, and physical access control)",
            ),
            verify_commands=("show running-config | include banner",),
        ),
        ModuleSpec(
            filename="mod-02-access-control-and-aaa.md",
            title="Device Access Control, Password Policies & AAA (5.3 - 5.4, 5.8)",
            objectives=(
                "5.3 Configure and verify device access control using local passwords",
                "5.4 Describe security password policy elements, such as management, complexity, and password alternatives (multifactor authentication, certificates, and biometrics)",
                "5.8 Compare authentication, authorization, and accounting concepts",
            ),
            verify_commands=(
                "show aaa servers",
                "show running-config | include username|enable",
            ),
        ),
        ModuleSpec(
            filename="mod-03-ipsec-vpns.md",
            title="IPsec Remote Access & Site-to-Site VPNs (5.5)",
            objectives=(
                "5.5 Describe IPsec remote access and site-to-site VPNs",
            ),
            verify_commands=("show crypto isakmp sa", "show crypto ipsec sa"),
        ),
        ModuleSpec(
            filename="mod-04-access-control-lists.md",
            title="Access Control Lists (5.6)",
            objectives=("5.6 Configure and verify access control lists",),
            verify_commands=("show access-lists", "show ip interface"),
        ),
        ModuleSpec(
            filename="mod-05-layer2-security.md",
            title="Layer 2 Security: DHCP Snooping, DAI & Port Security (5.7)",
            objectives=(
                "5.7 Configure and verify Layer 2 security features (DHCP snooping, dynamic ARP inspection, and port security)",
            ),
            verify_commands=(
                "show port-security interface",
                "show ip dhcp snooping",
                "show ip arp inspection",
            ),
        ),
        ModuleSpec(
            filename="mod-06-wireless-security.md",
            title="Wireless Security Protocols & WPA2-PSK WLAN GUI (5.9 - 5.10)",
            objectives=(
                "5.9 Describe wireless security protocols (WPA, WPA2, and WPA3)",
                "5.10 Configure and verify WLAN within the GUI using WPA2 PSK",
            ),
            verify_commands=("show running-config | include dot11",),
        ),
    ),
    "06-automation-programmability": (
        ModuleSpec(
            filename="mod-01-sdn-and-controllers.md",
            title="Network Automation & Controller-Based SDN Architecture (6.1 - 6.3)",
            objectives=(
                "6.1 Explain how automation impacts network management",
                "6.2 Compare traditional networks with controller-based networking",
                "6.3 Describe controller-based, software defined architecture (overlay, underlay, and fabric)",
                "6.3.a Separation of control plane and data plane",
                "6.3.b Northbound and Southbound APIs",
            ),
            verify_commands=("show control-plane host open-ports",),
        ),
        ModuleSpec(
            filename="mod-02-ai-ml-in-netops.md",
            title="AI & Machine Learning in Network Operations (6.4)",
            objectives=(
                "6.4 Explain AI (generative and predictive) and machine learning in network operations",
            ),
            verify_commands=("show logging | include %",),
        ),
        ModuleSpec(
            filename="mod-03-rest-apis-and-json.md",
            title="REST-Based APIs & JSON Data Encoding (6.5, 6.7)",
            objectives=(
                "6.5 Describe characteristics of REST-based APIs (authentication types, CRUD, HTTP verbs, and data encoding)",
                "6.7 Recognize components of JSON-encoded data",
            ),
            verify_commands=("python -m json.tool payload.json",),
        ),
        ModuleSpec(
            filename="mod-04-ansible-and-terraform.md",
            title="Configuration Management: Ansible & Terraform (6.6)",
            objectives=(
                "6.6 Recognize the capabilities of configuration management mechanisms such as Ansible and Terraform",
            ),
            verify_commands=(
                "ansible-playbook --syntax-check site.yml",
                "terraform validate",
            ),
        ),
    ),
}


def render_module(spec: ModuleSpec) -> str:
    lines: list[str] = [
        f"# {spec.title}",
        "",
        "## Blueprint Objectives",
    ]
    lines.extend(f"- [ ] {item}" for item in spec.objectives)
    lines.extend(
        [
            "",
            "## 1. Control-Plane Logic (20m)",
            "- ",
            "",
            "## 2. CLI Lab & Verification Commands (40m)",
            "```ios",
            *spec.verify_commands,
            "```",
            "",
            "## 3. Active Recall & Failure Modes (15m)",
            "- ",
            "",
        ]
    )
    return "\n".join(lines)


def render_cheat_sheet(domain: str, modules: tuple[ModuleSpec, ...]) -> str:
    header = [
        f"# {domain} — Quick Recall Sheet",
        "",
        "| Module | Topic | Primary Verification | Ready |",
        "| :--- | :--- | :--- | :---: |",
    ]
    rows = [
        f"| `{mod.filename}` | {mod.title} | {', '.join(mod.verify_commands[:2])} | [ ] |"
        for mod in modules
    ]
    return "\n".join([*header, *rows, ""])


def build_roadmap(base_dir: Path) -> None:
    root = base_dir / ROOT_NAME
    (root / "07-exam-readiness" / "01-anki-exports").mkdir(parents=True, exist_ok=True)
    (root / "07-exam-readiness" / "02-practice-exam-logs").mkdir(parents=True, exist_ok=True)

    remediation_file = root / "07-exam-readiness" / "03-weak-area-remediation.md"
    if not remediation_file.exists():
        remediation_file.write_text("# Weak Area Remediation Log\n\n- \n", encoding="utf-8")

    readme_file = root / "README.md"
    if not readme_file.exists():
        readme_lines = [
            "# CCNA 200-301 v1.1 Study Repository",
            "",
            "- **Daily Cadence:** 75m max (20m concept / 40m CLI lab / 15m active recall)",
            "- **Weekly Guardrail:** Friday integration lab, Saturday recall drill, Sunday full shutdown",
            "",
        ]
        readme_file.write_text("\n".join(readme_lines), encoding="utf-8")

    for domain, modules in ROADMAP.items():
        domain_path = root / domain
        for sub in ("01-modules", "02-labs", "03-study-notes"):
            (domain_path / sub).mkdir(parents=True, exist_ok=True)

        if domain != "00-study-workflow":
            cheat_sheet = domain_path / "03-study-notes" / f"{domain}-cheat-sheet.md"
            if not cheat_sheet.exists():
                cheat_sheet.write_text(render_cheat_sheet(domain, modules), encoding="utf-8")

        for mod in modules:
            mod_file = domain_path / "01-modules" / mod.filename
            if not mod_file.exists():
                mod_file.write_text(render_module(mod), encoding="utf-8")

    print(f"Roadmap generated cleanly at: {root.resolve()}")


if __name__ == "__main__":
    build_roadmap(Path.cwd())