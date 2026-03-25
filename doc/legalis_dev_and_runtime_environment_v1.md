# Legalis – Development and Runtime Environment v1

## Zweck dieses Dokuments

Dieses Dokument definiert die vorläufig verbindliche Entwicklungs- und Betriebsumgebung für **Legalis v1**.
Es konkretisiert die bereits getroffenen Architekturentscheidungen aus:

- Projektfahrplan v3
- Module Catalog v2
- Licensing and Extension Architecture v1
- License Matrix v1

Das Ziel ist eine technische Arbeitsgrundlage, mit der Entwicklungsserver, IDEs, Repositories, Container-Stacks und spätere Kundeninstallationen konsistent aufgebaut werden können.

**Status:** vorläufig final für Startphase / MVP-Umsetzung  
**Stand:** 2026-03-21

---

## 1. Zielsetzung und Abgrenzung

Dieses Dokument beantwortet insbesondere folgende Fragen:

- Auf welchen Zielplattformen wird Legalis v1 betrieben?
- In welcher Form wird Legalis ausgeliefert?
- Welche Backend-, Datenbank- und Laufzeitkomponenten sind gesetzt?
- Wie wird ein möglicher Java-basierter Workflow-Dienst technisch eingeordnet?
- Welche Speicher- und Backup-Grundsätze gelten?
- Welche Entscheidungen sind bewusst vertagt?

Dieses Dokument ersetzt keine spätere Betriebsdokumentation pro Kunde, sondern definiert den **kanonischen Referenzpfad**.

---

## 2. Leitprinzipien

### 2.1 Linux-only im Serverbetrieb
Legalis v1 wird als **Linux-only-Serveranwendung** geplant.

Gründe:
- kontrollierter Betrieb durch Legalis oder geschulte Partner
- Webbrowser-Zugriff für Kanzleimitarbeiter statt lokaler Windows-Installation
- geringere Zielplattformkomplexität
- einfachere Härtung, Backups und Automatisierung
- bessere Eignung für Proxmox-, VM- und Containerbetrieb

### 2.2 Browser-first
Die Arbeitsplätze der Kanzlei greifen per **Webbrowser** auf Legalis zu.
Lokale Client-Installationen auf Mitarbeiterrechnern sind nicht Bestandteil des Referenzpfads.

### 2.3 Standardisierte Auslieferung
Legalis wird nicht als unstrukturierter Quellcode-Ordner ausgeliefert, sondern als definierter, reproduzierbarer Stack mit:
- Container-Images
- Compose-Dateien
- Migrationslogik
- dokumentierten Volumes
- nachvollziehbarer Konfiguration

### 2.4 Modularer Monolith als Startarchitektur
Legalis v1 wird als **modularer Monolith** im Python-Core geplant.
Ein möglicher Java-basierter Workflow-Dienst wird technisch isoliert angebunden.

Keine Zielarchitektur für v1:
- verteilte Microservice-Landschaft
- Kubernetes-first
- mehrere voneinander abhängige Kleinstservices ohne zwingenden Fachgrund

---

## 3. Zielplattformen

## 3.1 Referenzbetrieb
Primäre Zielplattform für den Referenzbetrieb ist:

- **Proxmox VE** als Virtualisierungsplattform
- darin eine **dedizierte VM** für Legalis
- innerhalb der VM ein Linux-Server mit Container-Runtime

## 3.2 Unterstützte Grundmodelle
Für Legalis v1 werden drei Betriebsmodelle unterschieden:

### A. Referenzmodell v1
- Proxmox-VM
- Linux-Server
- Docker Engine + Compose

### B. Spätere Appliance-Option
- Proxmox-LXC
- nur als spätere, vereinfachte On-Prem-Variante
- nicht kanonischer Primärpfad

### C. Spätere Skalierungsoption
- K3s / Kubernetes
- nur für größere Installationen, Partnerbetrieb oder Cloud-Skalierung
- nicht Bestandteil des MVP-Referenzbetriebs

## 3.3 Nicht unterstützt im Referenzpfad
- Docker direkt auf dem Proxmox-Host als Produktstandard
- Windows-Server als Zielplattform
- macOS-Serverbetrieb
- Desktop-/Fat-Client-Auslieferung

---

## 4. Betriebssystem- und Laufzeitbasis

## 4.1 Server-Basis
Für die Legalis-VM wird ein konservatives Linux-System empfohlen:

- **Debian Stable** oder
- **Ubuntu LTS**

Für die frühe Projektphase ist eine der beiden Distributionen als Referenz verbindlich festzulegen. Bis zur endgültigen Festlegung gilt:

- Debian bevorzugt für minimalistische, stabile Serverumgebungen
- Ubuntu LTS bevorzugt, wenn breitere Dokumentation oder bestimmte Pakete im Partnerbetrieb benötigt werden

## 4.2 Python-Laufzeit
Legalis Core wird auf geplantem Stand betrieben mit:

- **Python 3.12** als Referenzversion

Abweichungen sind nur zulässig, wenn sie explizit in Build- und Testpipeline freigegeben wurden.

## 4.3 Java-Laufzeit
Falls Imixs/Open-BPMN oder ein anderer Java-basierter Workflow-Dienst eingesetzt wird:

- **Eclipse Temurin / OpenJDK**
- bevorzugt **JDK 17+**

Oracle-JDK ist nicht Bestandteil des Referenzpfads.

---

## 5. Container- und Auslieferungsstrategie

## 5.1 Kanonisches Auslieferungsformat
Legalis v1 wird in erster Linie als **Docker-/OCI-basierter Compose-Stack** geplant.

Gründe:
- gute Portabilität zwischen lokaler Entwicklung, VM-Betrieb und späterem Cloud-Hosting
- saubere Abbildung mehrerer Dienste
- einfache Reproduzierbarkeit
- klare Trennung von Anwendung und Hostsystem

## 5.2 Referenz-Runtime
Primäre Referenz-Runtime:
- **Docker Engine auf Linux**
- **Docker Compose Plugin**

## 5.3 Podman
Podman bleibt eine mögliche spätere Alternative, ist aber **nicht** der primäre Referenzpfad für v1.

Ziel ist, OCI-saubere Images und möglichst runtime-neutrale Containerdefinitionen zu bauen, damit ein späterer Podman-Betrieb grundsätzlich möglich bleibt.

## 5.4 LXC
LXC wird **nicht** als kanonisches Produktformat verwendet.
Es kann später als vereinfachte Appliance-Variante für kleine On-Prem-Kanzleien angeboten werden.

## 5.5 K3s / Kubernetes
K3s wird ausdrücklich als spätere Skalierungsoption mitgedacht, aber **nicht** als Standard für den Start.

---

## 6. Referenz-Compose-Stack

Der Referenzstack für Legalis v1 soll mindestens logisch aus folgenden Diensten bestehen:

- `reverse-proxy`
- `app`
- `postgres`
- `worker` (falls Hintergrundjobs getrennt betrieben werden)
- optional `workflow-java`

### 6.1 Reverse Proxy
Empfohlene Erstentscheidung:
- **Caddy** als Standard für v1

Begründung:
- einfache Konfiguration
- guter Fit für kleine bis mittlere Installationen
- schnelle, saubere TLS-/Reverse-Proxy-Einrichtung

**Nginx OSS** bleibt eine zulässige Alternative, wenn ein späterer Betriebspartner ausdrücklich darauf standardisieren möchte.

### 6.2 App-Service
Enthält den Python-Core von Legalis:
- FastAPI-Anwendung
- API-Endpunkte
- Authentifizierung / Autorisierung
- Kernlogik
- Signatur- und Lizenzlogik
- Modulregistrierung

### 6.3 Datenbank-Service
- PostgreSQL als primäre relationale Datenbank
- keine SQLite-Produktionslinie

### 6.4 Worker-Service
Optional getrennt für:
- Fristenläufe
- Reports
- Erinnerungen
- asynchrone Dokumentprozesse
- geplante Exporte / Imports

### 6.5 Workflow-Java-Service
Nur wenn fachlich aktiviert:
- separater Java-Dienst
- keine harte Vermischung mit Python-Core
- Kommunikation per HTTP/REST und klaren Schnittstellen

---

## 7. Backend-Entscheidungen

## 7.1 Core-Framework
Für Legalis v1 wird als Referenz festgelegt:

- **FastAPI**

Gründe:
- API-zentrierter Ansatz
- gute Passung zu modularer, serviceorientierter Architektur
- starke Schema-/Validierungsintegration
- gute Eignung für Browser-Frontend und externe Integrationen

## 7.2 Nicht gewählter Hauptpfad
- Django wird nicht als primäres Fundament von Legalis v1 gesetzt.

Django bleibt als bekanntes Framework theoretisch möglich, ist aber für den aktuellen Produktansatz nicht Referenzstandard.

## 7.3 ORM / Datenzugriff
- **SQLAlchemy 2** als Referenz für ORM und DB-Zugriff
- Pydantic für Datenmodelle / Validierung

## 7.4 API-Stil
- HTTP/JSON als Primärschnittstelle
- klar versionierbare interne und externe APIs
- keine implizite Kopplung an Desktop- oder Thick-Client-Protokolle

---

## 8. Datenbank- und Speicherstrategie

## 8.1 Primäre Datenbank
Legalis v1 setzt produktiv auf:

- **PostgreSQL**

SQLite ist höchstens für isolierte Tests, lokale Experimente oder sehr frühe Einzelmodule zulässig.

## 8.2 Dokumente nicht als primäre BLOB-Strategie
Gescannten Dokumente, PDFs, Anhänge und ähnliche Artefakte sollen **nicht** primär als große Binärdaten in PostgreSQL gespeichert werden.

Stattdessen gilt:
- Metadaten, Verweise, Status, Tags und Governance-Daten in PostgreSQL
- Dateien im getrennten Dokumenten-Storage

## 8.3 Speicherklassen
Von Anfang an werden mindestens drei Speicherklassen unterschieden:

### A. System / OS / Runtime
- kleines Root-Filesystem
- Betriebssystem
- Container-Runtime
- Compose-Dateien
- Logs / temporäre Systemdaten

### B. Datenbank-Storage
- PostgreSQL-Daten
- getrennt vom Dokumentenbestand

### C. Dokumenten-Storage
- Scans
- PDFs
- Uploads
- erzeugte Dokumente
- OCR-/Preview-Artefakte
- Exportdateien nach definierter Policy

## 8.4 Grundsatz für Wachstum
Nicht das Root-Filesystem soll wachsen, sondern die datenintensiven Bereiche werden **separat skaliert**.

---

## 9. VM-, Disk- und Filesystem-Strategie

## 9.1 Grundmodell
Für die Referenz-VM wird eine Trennung in mehrere virtuelle Disks empfohlen:

- **Disk 1:** OS / App / Runtime
- **Disk 2:** PostgreSQL Data
- **Disk 3:** Document Store
- optional **Disk 4:** Backup-Staging / temporäre Render- oder Archivdaten

## 9.2 LVM innerhalb der VM
LVM wird **als empfohlene Option für Datenvolumes** vorgesehen, insbesondere für:
- PostgreSQL-Disk
- Dokumenten-Disk
- spätere Archive / temporäre Renderbereiche

LVM ist **nicht zwingend** für die komplette Root-Systemdisk erforderlich.

## 9.3 Ziel der LVM-Option
- flexiblere Erweiterung von Datenbereichen
- saubere Trennung von Datenklassen
- bessere Vorbereitung auf wachsende Scan- und Dokumentenmengen
- weniger Risiko, das Gesamtsystem durch volllaufende Root-Volumes zu destabilisieren

## 9.4 Filesystem-Richtung
Vorläufige Empfehlung:
- Root-System: **ext4**
- Datenvolumes: **ext4 oder XFS**
- große, dauerhaft wachsende Dokumentenvolumes: **XFS** ist zulässig, wenn keine Schrumpfung geplant ist

Die konkrete Festlegung pro Kundenumgebung kann später im Betriebsprofil erfolgen.

---

## 10. Dokumenten- und Dateispeicher

## 10.1 v1-Standard
Für Legalis v1 gilt zunächst:
- lokaler oder VM-seitig angebundener Dateispeicher
- klar definierte Mountpoints / Volumes
- dokumentierte Pfadstruktur
- keine implizite Speicherung „irgendwo im Container“

## 10.2 Zukunftsoption
Der Dokumenten-Storage soll so abstrahiert werden, dass später ein Wechsel auf:
- externen Storage-Server
- NAS
- S3-kompatiblen Objektstorage
- Archiv-Storage

prinzipiell möglich bleibt.

## 10.3 Container-Grundsatz
Persistente Dokumente dürfen **nicht** ausschließlich innerhalb flüchtiger Container-Dateisysteme liegen.

---

## 11. Workflow- und Java-Dienstgrenze

## 11.1 Grundsatz
Der Legalis Core bleibt Python-basiert.

Falls eine BPMN-/Workflow-Engine wie Imixs eingesetzt wird, erfolgt dies als:
- separater Dienst
- klar abgegrenzter Integrationspunkt
- eigener Container / eigenes Deployment-Artefakt

## 11.2 Keine Vermischung im Core
Der Java-basierte Workflow-Dienst wird nicht als impliziter Kern des gesamten Systems modelliert.

Legalis bleibt fachlich und technisch führend; der Workflow-Dienst ist eine spezialisierte Laufzeit- oder Automatisierungskomponente.

## 11.3 Gründe für diese Trennung
- Python bleibt Hauptentwicklungssprache
- reduzierte Kopplung an Copyleft-/Lizenzgrenzen einzelner Workflow-Projekte
- isolierbare Betriebs- und Upgrade-Pfade
- klarere Fehlerdiagnose und Supportgrenzen

---

## 12. Hintergrundjobs und zeitgesteuerte Prozesse

## 12.1 Startansatz
Für v1 wird ein pragmatisches Job-Modell bevorzugt:
- einfacher Worker-Service
- definierte Jobtypen
- kein unnötig komplexes verteiltes Queue-System im MVP

## 12.2 Typische Jobs
- Prazo-/Fristenprüfungen
- Erinnerungen / Wiedervorlagen
- Report-Erzeugung
- periodische Datenimporte / Datenexporte
- Dokumenten-Nachbearbeitung

## 12.3 Vertagte Detailentscheidung
Die konkrete Wahl des Worker-/Queue-Frameworks bleibt vorläufig offen, solange die Schnittstelle sauber gekapselt wird.

---

## 13. Konfiguration, Secrets und Umgebungen

## 13.1 Umgebungsmodell
Mindestens zu unterscheiden:
- `dev`
- `test`
- `staging` (später)
- `prod`

## 13.2 Konfigurationsprinzip
Konfiguration erfolgt möglichst über:
- Umgebungsvariablen
- versionierte Konfigurationsdateien ohne Geheimnisse
- getrennte Secret-Mechanismen

## 13.3 Secrets
Geheimnisse wie:
- Datenbankpasswörter
- API-Schlüssel
- Signaturmaterial
- SMTP-/Connector-Zugangsdaten

dürfen nicht hart im Quellcode oder in allgemeinen Compose-Dateien stehen.

## 13.4 Signatur- und Lizenzschlüssel
Private Signaturschlüssel gehören **nicht** in Kundencontainer oder allgemeine Repositories.
Im Runtime-System liegen nur die notwendigen öffentlichen Schlüssel bzw. vertrauenswürdigen Fingerprints.

---

## 14. Logging, Audit und Beobachtbarkeit

## 14.1 Fachliches Audit
Audit ist Kernbestandteil von Legalis und nicht optionales Zusatz-Logging.

## 14.2 Technisches Logging
Mindestens zu unterscheiden:
- Applikationslog
- Reverse-Proxy-Log
- Datenbanklog (im sinnvollen Rahmen)
- Sicherheits-/Lizenzereignisse
- Job-/Scheduler-Log

## 14.3 Persistenz
Logs und Audit-Daten sind so zu planen, dass sie:
- nicht unkontrolliert das Root-Volume füllen
- sinnvoll rotieren
- im Fehlerfall auswertbar bleiben

Monitoring- und zentrale Observability-Stacks sind für v1 noch nicht verbindlich festgelegt.

---

## 15. Backup- und Wiederherstellungsgrundsätze

## 15.1 Grundsatz
VM-Snapshots allein sind **nicht** das vollständige Backup-Modell.

## 15.2 Mindestanforderungen
Erforderlich sind getrennte Strategien für:
- PostgreSQL-Backups
- Dokumenten-Backups
- Konfigurations- und Compose-Dateien
- optional Signatur-/Lizenz-Metadaten

## 15.3 Dokumentenwachstum
Da eingescannte und grafiklastige Dokumente langfristig sehr große Volumina erreichen können, muss der Dokumentenbestand so geplant werden, dass:
- separates Backup möglich ist
- Archivierung möglich ist
- Restore-Szenarien nicht unnötig die gesamte VM umfassen müssen

## 15.4 Zielbild
- konsistente Datenbanksicherung
- dateibasierte Dokumentensicherung
- nachvollziehbare Restore-Dokumentation

---

## 16. Entwicklungsumgebung

## 16.1 Primäre Entwicklungsplattform
Bevorzugt:
- Linux-Entwicklungsumgebungen
- VS Code oder vergleichbare IDEs
- Container- oder venv-basierter lokaler Entwicklungsablauf

## 16.2 Nicht voraussetzen
Nicht vorausgesetzt werden sollen:
- Docker Desktop als Pflichtwerkzeug
- proprietäre lokale Spezialwerkzeuge ohne Ersatzpfad

## 16.3 Lokale Entwicklung
Für lokale Entwicklung gelten als Zielbild:
- Python-Projekt mit sauberem Dependency-Management
- lokale Testdatenbank in PostgreSQL
- optional Compose-basierte lokale Gesamtumgebung
- reproduzierbare Start- und Testbefehle

## 16.4 Partner- und Schulungsfähigkeit
Die Entwicklungsumgebung soll so dokumentiert werden, dass:
- neue Entwickler zügig onboarded werden können
- spätere Vertriebspartner oder Implementierungspartner technische Schulungen erhalten können

---

## 17. Sicherheitsgrundsätze für den Betrieb

## 17.1 Trennung von Rollen
Produktiver Betrieb, Entwicklung und Signatur-/Release-Prozesse sind organisatorisch zu trennen.

## 17.2 Premium- und Lizenzlogik
Die im separaten Dokument definierte Signatur- und Extension-Architektur ist Bestandteil der Runtime-Umgebung.

Das betrifft insbesondere:
- Basislizenz
- Lease-Modell
- signierte Erweiterungspakete
- signierte Prozesspakete
- Auditpflichten bei Aktivierung und Ablauf

## 17.3 Keine Speicherorte im Container verstecken
Persistente Daten, Lizenzartefakte, Prozesspakete und relevante Konfigurationszustände müssen nachvollziehbar gespeichert und gesichert werden.

---

## 18. Bewusst vertagte Entscheidungen

Folgende Punkte bleiben vorläufig offen, ohne den Start zu blockieren:

- endgültige Entscheidung Debian vs. Ubuntu LTS als Referenz-Gast-OS
- konkretes Worker-/Queue-Framework
- endgültige Monitoring-/Observability-Tools
- exakte Frontend-Technologie
- S3-/Objektstorage-Einführung
- K3s als spätere Betriebsoption
- LXC-Appliance als offizielles Zusatzformat
- optionale native Verify-Bibliothek in C oder Rust

---

## 19. Vorläufig verbindliche Architekturentscheidungen

Für die Startphase von Legalis gelten damit als festgezogene Grundentscheidungen:

1. **Linux-only im Serverbetrieb**
2. **Browserbasierter Zugriff**
3. **Proxmox-VM als Referenzdeployment**
4. **Docker Engine + Compose als kanonisches Auslieferungsformat**
5. **FastAPI als Python-Core-Framework**
6. **PostgreSQL als produktive Datenbank**
7. **Dokumenten-Storage getrennt von PostgreSQL und Root-Dateisystem**
8. **Mehrere virtuelle Disks statt eines einzigen großen Root-Filesystems**
9. **LVM als empfohlene Option für Datenvolumes**
10. **Java nur als isolierter Workflow-/BPMN-Dienst, falls benötigt**
11. **Caddy als vorläufiger Standard-Reverse-Proxy**
12. **LXC und K3s nur als spätere Zusatzpfade, nicht als Primärmodell von v1**

---

## 20. Nächste unmittelbare Arbeitsschritte

1. Referenz-Gast-OS verbindlich wählen
2. Entwicklungsserver / Dev-VMs einrichten
3. IDE- und Projektstruktur festlegen
4. Compose-Basisstack erzeugen
5. PostgreSQL-Volume-Layout definieren
6. Dokumenten-Volume-Layout definieren
7. Repository- und Modulstruktur initial anlegen
8. Basis für Build-, Start- und Testkommandos dokumentieren

---

## 21. Schlussformel

Dieses Dokument definiert die **vorläufig finale technische Startumgebung** für Legalis.

Es ist bewusst so angelegt, dass:
- kleine bis mittlere Kanzleien pragmatisch bedient werden können
- On-Prem-Betrieb auf Proxmox sauber unterstützt wird
- spätere Skalierungspfade offen bleiben
- die technische Komplexität des MVP nicht unnötig entgleist

Legalis startet damit nicht als maximales Infrastrukturprojekt, sondern als **kontrolliert wachsendes, modular aufgebautes Produkt mit reproduzierbarem Betriebsmodell**.
