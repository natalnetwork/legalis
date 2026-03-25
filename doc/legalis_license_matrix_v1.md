
# Legalis – License Matrix v1

## Zweck dieses Dokuments

Diese Matrix dokumentiert den aktuell favorisierten technischen Stack von Legalis im Hinblick auf:

- Lizenztyp
- kommerzielle Nutzbarkeit
- mögliche Kostenfallen
- Compliance-Risiken
- empfohlene Einsatzstrategie

**Stand der Prüfung:** 2026-03-21  
**Wichtiger Hinweis:** Dieses Dokument ist eine technische Arbeitsgrundlage und keine anwaltliche Rechtsberatung. Vor Produktivvertrieb und Partnerprogramm sollte eine formale OSS-Compliance-Prüfung erfolgen.

---

## Bewertungslegende

- **Ja** = kommerzielle Nutzung grundsätzlich unkritisch
- **Ja, aber** = kommerzielle Nutzung grundsätzlich möglich, aber mit Zusatzpflichten oder Kostenrisiken
- **Prüfen** = nicht primär Kostenproblem, aber erhöhtes Compliance- oder Kopplungsrisiko

---

## Lizenz-Matrix

| Komponente | Rolle in Legalis | Upstream-Lizenz / Modell | Kommerzielle Nutzung | Laufende Lizenzkosten für Kunden? | Haupt-Risiko / Hinweis | Empfehlung |
|---|---|---|---|---|---|---|
| Python | Kernsprache | PSF License v2 | Ja | Nein | Lizenzhinweise bei Distribution beachten | Freigeben |
| FastAPI | API-Framework | MIT | Ja | Nein | Lizenzhinweise beibehalten | Freigeben |
| SQLAlchemy | ORM / Datenzugriff | MIT | Ja | Nein | Lizenzhinweise beibehalten | Freigeben |
| Pydantic / pydantic-core | Validierung / Schemas | MIT | Ja | Nein | Lizenzhinweise beibehalten | Freigeben |
| Uvicorn | ASGI-Server | BSD-3-Clause | Ja | Nein | Lizenzhinweise beibehalten | Freigeben |
| PostgreSQL | Primäre Datenbank | PostgreSQL License | Ja | Nein | operative Härtung und Backup wichtiger als Lizenzthema | Freigeben |
| Eclipse Temurin / OpenJDK | Java-Runtime für Workflow-Dienst | OpenJDK-basiert, frei nutzbar | Ja | Nein | Oracle-JDK-Sonderfall vermeiden | Temurin standardisieren |
| Docker Engine auf Linux | Container-Runtime | OSS-Komponenten; Desktop-Regelung nicht einschlägig | Ja, aber | Nein | Build-/Runtime-Pakete sauber dokumentieren | Für Serverbetrieb geeignet |
| Docker Compose Plugin | Multi-Container-Stack | Im Docker/Linux-Serverkontext unkritisch | Ja, aber | Nein | nicht mit Docker Desktop verwechseln | Referenzpfad für v1 |
| Docker Desktop | lokale Entwickler-Workstation | Docker Subscription Service Agreement | Ja, aber | **Teilweise** | ab Größen-/Umsatzgrenze kostenpflichtig | Nicht voraussetzen |
| Podman | alternative Container-Runtime | Apache-2.0 | Ja | Nein | Tooling- und Supportpfad definieren | Gute Alternative, aber nicht v1-Referenz |
| Caddy | Reverse Proxy | Apache-2.0 | Ja | Nein | Modul-/Plugin-Auswahl dokumentieren | Sehr gut geeignet |
| NGINX Open Source | Reverse Proxy | BSD-2-Clause | Ja | Nein | NGINX OSS vs. NGINX Plus trennen | Ebenfalls gut geeignet |
| Proxmox VE | On-Prem-Virtualisierung | Open Source, Subscription optional | Ja | Nein, Subscription optional | Enterprise-Repository und Support kosten extra | Als Zielplattform freigeben |
| K3s | spätere Orchestrierung | Apache-2.0 | Ja | Nein | höhere Betriebs- und Supportkomplexität | Später für größere Setups |
| Imixs Workflow | möglicher BPMN-/Workflow-Dienst | EPL-2.0 (aktueller Stand) | Ja, aber | Nein | weak-copyleft / Separationsdisziplin erforderlich | Nur isoliert als separater Dienst |
| Open-BPMN | Modellierung / BPMN-Tooling | EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0 | Prüfen | Nein | Dual-/Copyleft-Kontext sauber trennen | Nur gezielt und isoliert einsetzen |

---

## Konkrete Arbeitsregeln für Legalis

### 1. Lizenzsauberer Basiskern
Für den produktiven Basiskern sind derzeit lizenzseitig am unkritischsten:
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL
- Eclipse Temurin
- Caddy oder NGINX OSS
- Podman oder Docker Engine auf Linux

### 2. Docker Desktop nicht voraussetzen
Docker Desktop soll **nicht** Voraussetzung für Entwickler, Partner oder Kunden sein. Dadurch entfällt die wichtigste kommerzielle Kostenfalle im Container-Umfeld.

### 3. Java sauber von Oracle-Lizenzpfaden trennen
Für alle Java-bezogenen Teile ist **Eclipse Temurin / OpenJDK** zu bevorzugen. Oracle-JDK soll nicht Bestandteil des Referenzpfads sein.

### 4. Copyleft-Sensibilität bei BPMN-Komponenten
Imixs und insbesondere Open-BPMN sollen:
- möglichst **unmodifiziert** verwendet werden
- technisch **getrennt** vom proprietären Zusatzcode bleiben
- nicht gedankenlos in den Core hineinkopiert oder hart eingebettet werden
- vor Produktivvertrieb noch einmal separat compliance-geprüft werden

### 5. SBOM und Lizenzscan vor Releases
Vor Beta, Partnervertrieb oder kundenseitiger Auslieferung soll ein reproduzierbarer Prozess eingeführt werden für:
- Abhängigkeitsinventar
- Lizenzscan
- Third-Party-Notices
- Dokumentation der verwendeten Paketversionen

---

## Ampelbewertung für kleine bis mittlere Kanzleien

### Grün
Ohne besondere Lizenzkosten pro Kunde einsetzbar:
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- PostgreSQL
- Eclipse Temurin
- Podman
- Caddy
- NGINX OSS
- Proxmox VE ohne Support-Subscription
- K3s

### Gelb
Einsetzbar, aber organisatorisch bewusst steuern:
- Docker Engine / Compose im Linux-Serverbetrieb
- Docker Desktop auf Entwicklergeräten
- Imixs Workflow

### Orange
Nicht verbieten, aber bewusst nur mit zusätzlicher Prüfung einsetzen:
- Open-BPMN

---

## Vorläufiges Fazit

Der für Legalis favorisierte Basis-Stack ist für den kommerziellen Einsatz bei kleinen bis mittleren Kanzleien **weitgehend ohne zwingende zusätzliche Laufzeit-Lizenzkosten** nutzbar.

Die wichtigsten Sonderfälle sind:
- **Docker Desktop** auf Entwickler- oder Admin-Workstations
- **optionale Proxmox-Subscriptions** für Support und Enterprise-Repository
- **Copyleft-/Dual-Lizenzfragen** bei Imixs und Open-BPMN

---

## Quellenbasis der Prüfung

Die Matrix wurde gegen die offiziellen Projektseiten bzw. offiziellen Lizenzseiten der betroffenen Komponenten abgeglichen. Für die nächste Compliance-Runde sollte zusätzlich ein versionierter Link-Anhang im Build-/Release-Prozess gepflegt werden.
