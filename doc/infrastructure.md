# Legalis – Infrastruktur und Betriebsumgebung

## Entwicklungsumgebung (Homelab)

### Proxmox-Host
- Interne Domain: `homenet.dev.br`
- DNS via Cloudflare (API Token in `/etc/cloudflare/credentials.ini`)
- Wildcard-Zertifikat `*.homenet.dev.br` via Certbot/Cloudflare-Plugin

### legalis-dev
- **Hostname:** `legalis-dev.homenet.dev.br`
- **IP:** `192.168.10.50`
- **OS:** Debian 13 (Trixie)
- **Zweck:** Python-Core, FastAPI, PostgreSQL, alle App-Dienste
- **SSH-Aliase (lokal):**
  - `legalis-dev` → User `s_schwiebert`
  - `legalis-dev-claude` → User `claude-code`
- **Projektverzeichnis:** `~/legalis` (Git Sparse Checkout, nur `doc/`)

### legalis-workflow
- **Hostname:** `legalis-workflow.homenet.dev.br`
- **IP:** `192.168.10.51`
- **OS:** Debian 13 (Trixie)
- **Zweck:** Imixs/Open-BPMN Laufzeit, BPMN-Entwicklungs- und Testumgebung
- **SSH-Aliase (lokal):**
  - `legalis-workflow` → User `s_schwiebert`
  - `legalis-workflow-claude` → User `claude-code`

## User-Setup (beide VMs)

| User | Gruppe | Sudo | SSH-Key |
|---|---|---|---|
| `s_schwiebert` | sudo | NOPASSWD | `~/.ssh/id_ed25519` (lokal) |
| `claude-code` | sudo | via Gruppe | `~/.ssh/claude_code_id_ed25519` (lokal) |

## Bekannte Eigenheiten

- **DNS:** `/etc/resolv.conf` wird nicht automatisch befüllt (dhcpcd-Artefakt). Fix: `nameserver 8.8.8.8` manuell eingetragen. Bei VM-Neuerstellung prüfen.
- **Locale:** Locale-Warnungen bei apt (de_DE + pt_BR gemischt, noch nicht bereinigt).
- **sudo:** Muss manuell installiert werden — auf frischen Debian-VMs nicht vorinstalliert.

## Lokale SSH-Config (`~/.ssh/config`)

```
Host legalis-dev
    HostName legalis-dev.homenet.dev.br
    User s_schwiebert
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host legalis-dev-claude
    HostName legalis-dev.homenet.dev.br
    User claude-code
    IdentityFile ~/.ssh/claude_code_id_ed25519
    IdentitiesOnly yes

Host legalis-workflow
    HostName legalis-workflow.homenet.dev.br
    User s_schwiebert
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes

Host legalis-workflow-claude
    HostName legalis-workflow.homenet.dev.br
    User claude-code
    IdentityFile ~/.ssh/claude_code_id_ed25519
    IdentitiesOnly yes
```

## Stand (2026-04-03)

- SSH-Zugang für beide User auf beiden VMs eingerichtet
- git installiert auf legalis-dev, Repo `natalnetwork/legalis` geklont (Sparse: `doc/`)
- Dev-Stack (Docker, Python, PostgreSQL) noch nicht installiert
- legalis-workflow noch nicht weiter konfiguriert (nur User-Setup)
