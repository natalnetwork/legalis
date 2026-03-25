# Legalis – Module Catalog v1

## Zweck dieses Dokuments

Dieses Dokument beschreibt das offizielle Modulportfolio von **Legalis v1**.  
Es dient als Grundlage für:

- Produktstruktur
- MVP-Priorisierung
- Paketierung
- Roadmap-Planung
- spätere Implementierungs- und Vertriebsentscheidungen

Die Moduldefinitionen orientieren sich am Pilotkontext **Mychelle Maciel Advogados** und an der übergeordneten Referenzarchitektur von Legalis.

---

## Katalogstruktur

Jedes Modul wird beschrieben durch:

- **Modulname**
- **Zweck**
- **Hauptfunktionen**
- **Kernobjekte**
- **Paket**
- **MVP-Status**
- **Geschäftlicher Nutzen**
- **Bemerkungen**

---

## M01 – CRM / Intake Basic

**Zweck**  
Erfassung und Vorqualifizierung eingehender Anfragen.

**Hauptfunktionen**
- Lead anlegen
- Kontaktdaten erfassen
- Anfragequelle dokumentieren
- Erstnotizen
- Zuordnung eines nächsten Schritts
- Umwandlung in Mandant / Matter

**Kernobjekte**
- Lead
- Contact
- Intake Note
- Intake Source

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- strukturierter Erstkontakt
- weniger Informationsverlust
- sauberer Übergang in die Mandatsanlage

**Bemerkungen**
Im MVP bewusst schlank, ohne komplexes Kampagnen- oder Funnel-Marketing.

---

## M02 – Intake & Conflict Gate

**Zweck**  
Prüfung, ob ein Mandat angenommen werden darf und soll.

**Hauptfunktionen**
- Konfliktprüfung
- Annahme / Ablehnung
- Entscheidungsnotiz
- Pflichtfelder vor Annahme
- Freigabestatus

**Kernobjekte**
- Conflict Check
- Intake Decision
- Acceptance Status

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- reduziert Risiko
- stärkt Professionalität
- verhindert unsaubere Mandatsaufnahme

**Bemerkungen**
Soll eng mit Mandatsanlage verknüpft sein.

---

## M03 – Client Management

**Zweck**  
Verwaltung von Mandantenstammdaten und Beziehungen.

**Hauptfunktionen**
- natürliche und juristische Personen
- Ansprechpartner
- Kommunikationsdaten
- Identifikationsdaten
- Dokumentreferenzen
- Status des Mandanten

**Kernobjekte**
- Client
- Person
- Company
- Contact Point
- Client Document

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- zentrale Mandantenakte
- bessere Datenqualität
- Grundlage für Dokumente und Workflows

**Bemerkungen**
Muss Immobilien-, Investoren- und Firmenkontexte gut unterstützen.

---

## M04 – Matter Management

**Zweck**  
Formale Verwaltung von Mandaten / Fällen / Akten.

**Hauptfunktionen**
- Matter anlegen
- Mandanten zuordnen
- Rechtsgebiet zuordnen
- Verantwortliche festlegen
- Statusführung
- Aktenbasisdaten

**Kernobjekte**
- Matter
- Matter Role
- Matter Status
- Practice Area

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- zentrale operative Einheit des Systems
- saubere Trennung mehrerer Mandate eines Mandanten

**Bemerkungen**
Matter ist das Rückgrat fast aller Folgeprozesse.

---

## M05 – Engagement & Contract Basics

**Zweck**  
Abbildung der Mandatsgrundlage einschließlich Vollmacht und Honorarmodell.

**Hauptfunktionen**
- Mandatsvertrag referenzieren
- Procuração-Status
- Honorarmodell
- Annahmedatum
- Mandatsbedingungen

**Kernobjekte**
- Engagement
- Engagement Terms
- Power of Attorney
- Fee Arrangement

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- bessere Nachvollziehbarkeit
- wirtschaftliche und formale Klarheit

**Bemerkungen**
Kann anfangs einfach sein, darf aber nicht fehlen.

---

## M06 – Document Store

**Zweck**  
Zentrale Ablage und Zuordnung aller mandatsrelevanten Dokumente.

**Hauptfunktionen**
- Dokument hochladen
- Dokumenttyp zuordnen
- Matter / Client zuordnen
- Version / Datum / Status
- Download / Vorschau
- Tagging

**Kernobjekte**
- Document
- Document Type
- Document Link
- Attachment

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- geordnete Aktenführung
- schnellere Dokumentauffindung

**Bemerkungen**
Noch kein vollwertiges DMS im Enterprise-Sinn, aber operativ belastbar.

---

## M07 – Template Engine Basic

**Zweck**  
Erzeugung standardisierter Dokumente aus Daten und Vorlagen.

**Hauptfunktionen**
- DOCX/DOTX-Vorlagen verwalten
- Variablen einsetzen
- einfache Bedingungen
- Dokument generieren
- PDF finalisieren
- Metadaten speichern

**Kernobjekte**
- Template
- Template Revision
- Template Manifest
- Generated Document

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- schnellere Dokumenterstellung
- geringere Fehlerquote
- Standardisierung

**Bemerkungen**
Minimale Template-Versionierung ist Pflicht.

---

## M08 – Advanced Document Assembly

**Zweck**  
Fortgeschrittene Dokumentlogik und produktivere Vorlagenarbeit.

**Hauptfunktionen**
- komplexere Bedingungen
- Klauselblöcke
- Listen / Wiederholungen
- Vorlagenbibliothek
- Freigabeprozesse
- Varianten nach Rechtsgebiet

**Kernobjekte**
- Clause Block
- Template Variant
- Merge Context
- Approval State

**Paket**
- Premium

**MVP-Status**
- Nein, architektonisch vorbereiten

**Geschäftlicher Nutzen**
- erhebliche Zeitersparnis
- professionellere Standardisierung
- höherer Upsell-Wert

**Bemerkungen**
Später eng mit Knowledge Base verknüpfen.

---

## M09 – Case Workspace / Task Engine

**Zweck**  
Tägliche operative Steuerung der Fallbearbeitung.

**Hauptfunktionen**
- Aufgaben anlegen
- Verantwortliche zuweisen
- Prioritäten
- Wiedervorlagen
- interne Notizen
- Statusführung

**Kernobjekte**
- Task
- Assignment
- Task Status
- Internal Note

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- klare Zuständigkeiten
- weniger vergessene Arbeitsschritte
- bessere Teamkoordination

**Bemerkungen**
Muss für kleine Teams sehr schnell bedienbar sein.

---

## M10 – Prazo & Calendar Basic

**Zweck**  
Steuerung von Fristen, Terminen und Wiedervorlagen.

**Hauptfunktionen**
- Fristen erfassen
- Kalenderansicht
- Warnungen
- Fälligkeitsstatus
- Verknüpfung mit Matter und Task

**Kernobjekte**
- Deadline
- Calendar Event
- Reminder
- Due Status

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- reduziert Fristversäumnisse
- erhöht operative Kontrolle

**Bemerkungen**
Zentrales Pflichtmodul.

---

## M11 – Advanced Prazo Rules & Escalations

**Zweck**  
Erweiterte Regelwerke und Eskalationen für Fristen.

**Hauptfunktionen**
- Eskalationsketten
- Teamregeln
- Mehrstufige Warnungen
- SLA-Logik
- kritische Ereignisse

**Kernobjekte**
- Escalation Rule
- Notification Policy
- SLA Rule

**Paket**
- Premium

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- professionellere Fristenkontrolle
- besser für wachsende Teams

**Bemerkungen**
Später eng mit Workflow Engine koppeln.

---

## M12 – Communications Log

**Zweck**  
Erfassung relevanter Kommunikation im Mandatskontext.

**Hauptfunktionen**
- Kommunikationsereignisse dokumentieren
- E-Mail-/Telefon-/WhatsApp-Notizen
- Zuordnung zu Matter / Client
- Anhänge referenzieren

**Kernobjekte**
- Communication Entry
- Channel
- Communication Attachment

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- bessere Nachvollziehbarkeit
- vollständigerer Aktenkontext

**Bemerkungen**
Im MVP zunächst als Log, nicht als vollintegrierter Omnichannel-Hub.

---

## M13 – Shared Inbox & Smart Routing

**Zweck**  
Zentralisierte Eingangsbearbeitung mit intelligenter Zuordnung.

**Hauptfunktionen**
- gemeinsame Postkörbe
- Routing-Regeln
- Teamzuweisung
- Priorisierung
- SLA-/Bearbeitungsregeln

**Kernobjekte**
- Inbox Item
- Routing Rule
- Queue
- Assignment Policy

**Paket**
- Premium

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- sehr produktiv für Teams
- reduziert Eingangsstau

**Bemerkungen**
Erst sinnvoll, wenn Basiskommunikation stabil läuft.

---

## M14 – Billing Basic

**Zweck**  
Erfassung einfacher mandatsbezogener Einnahmen und Honorarsituationen.

**Hauptfunktionen**
- Forderung erfassen
- Zahlung erfassen
- Zahlungsstatus
- einfache Gebühren-/Auslagenabbildung

**Kernobjekte**
- Receivable
- Payment
- Fee Entry
- Expense Entry

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- wirtschaftliche Sicht auf das Mandat
- Grundlage für Liquiditätssteuerung

**Bemerkungen**
Noch keine Vollabrechnung, aber operativ ausreichend.

---

## M15 – Finance Ops & Liquidity Basic

**Zweck**  
Operative Steuerung von Ein- und Ausgaben sowie Liquidität.

**Hauptfunktionen**
- Einnahmen und Ausgaben
- wiederkehrende Kosten
- Bankkontosaldo manuell pflegen
- Liquiditätskalender
- Fälligkeiten
- einfache Forecast-Sicht

**Kernobjekte**
- Bank Account
- Cash Balance
- Payable
- Receivable
- Recurring Obligation
- Cashflow Entry

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- echte betriebliche Steuerung
- frühzeitige Erkennung enger Liquiditätsphasen

**Bemerkungen**
Im MVP bewusst als einfache operative Finanzsicht.

---

## M16 – Finance Reporting & Handover

**Zweck**  
Aufbereitung der Finanzdaten für interne Auswertung und externe Buchhaltung.

**Hauptfunktionen**
- Monatsreport
- offene Posten
- Zahlungsübersichten
- PDF-Report
- Plaintext-/CSV-Ausgabe

**Kernobjekte**
- Report Batch
- Export File
- Period Close
- Handover Package

**Paket**
- Premium

**MVP-Status**
- Nein, aber früh vorbereiten

**Geschäftlicher Nutzen**
- hoher Nutzen für Steuerbüro-Schnittstelle
- klar vermarktbares Premium-Modul

**Bemerkungen**
Pilotkunde mit externer Buchhaltung macht dieses Modul früh relevant.

---

## M17 – Security / Roles / Audit Core

**Zweck**  
Absicherung des Systems durch Rollen, Rechte und Protokollierung.

**Hauptfunktionen**
- Benutzer
- Rollen
- Rechte
- Audit-Log
- Zugriffsnachweise
- Status kritischer Aktionen

**Kernobjekte**
- User
- Role
- Permission
- Audit Entry
- Access Policy

**Paket**
- Standard

**MVP-Status**
- Ja

**Geschäftlicher Nutzen**
- Professionalität
- Nachvollziehbarkeit
- Grundlage für spätere Governance

**Bemerkungen**
Nicht optional.

---

## M18 – LGPD & Governance Advanced

**Zweck**  
Erweiterte Datenschutz- und Governance-Funktionen.

**Hauptfunktionen**
- Aufbewahrung / Löschung
- Freigabestufen
- Sensitivitätsklassifikation
- Governance-Reports
- stärkere Trennung von Bereichen

**Kernobjekte**
- Retention Rule
- Privacy Event
- Governance Policy
- Compliance Report

**Paket**
- Enterprise

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- stärkt Enterprise-Positionierung
- hilfreich für anspruchsvollere Kanzleien

**Bemerkungen**
Auf Core-Audit aufbauen.

---

## M19 – Management Dashboard

**Zweck**  
Steuerung der Kanzlei über Kennzahlen.

**Hauptfunktionen**
- Fälle
- Aufgaben
- Fristen
- Einnahmen / Ausgaben
- offene Forderungen
- Periodenübersichten

**Kernobjekte**
- KPI Snapshot
- Metric Definition
- Dashboard View

**Paket**
- Premium

**MVP-Status**
- Nein, architektonisch vorbereiten

**Geschäftlicher Nutzen**
- höherer Management-Nutzen
- sehr gutes Premium-Argument

**Bemerkungen**
Reports und Dashboard früh zusammendenken.

---

## M20 – Workflow / BPMN Engine

**Zweck**  
Technische Ausführung standardisierter Arbeitsabläufe.

**Hauptfunktionen**
- Prozessdefinition
- Prozessinstanzen
- Statusübergänge
- automatische Folgeschritte
- kontrollierte Modellierung

**Kernobjekte**
- Workflow Definition
- Workflow Version
- Workflow Instance
- Workflow Step

**Paket**
- Premium / Enterprise

**MVP-Status**
- Nicht als freier Designer, aber Kernlogik früh vorbereiten

**Geschäftlicher Nutzen**
- Hauptdifferenzierungsmerkmal von Legalis
- robuste Unternehmenssteuerung

**Bemerkungen**
Workflow first ist strategischer Kern von Legalis.

---

## M21 – Standard Process Governance

**Zweck**  
Schutz und Kontrolle der offiziellen Legalis-Standardprozesse.

**Hauptfunktionen**
- Standardprozess-Schutz
- Freigabemodell
- Schulungsnachweis
- Zertifikat / Schlüssel
- Trennung zu Custom Extensions

**Kernobjekte**
- Process Lock
- Certification Record
- Access Key
- Standard Workflow Policy

**Paket**
- Enterprise / Partner Layer

**MVP-Status**
- Nein, aber konzeptionell wichtig

**Geschäftlicher Nutzen**
- schützt Produktqualität
- reduziert Haftungsrisiko
- unterstützt Partner-/Consulting-Modell

**Bemerkungen**
Direkt aus der Governance-Strategie abgeleitet.

---

## M22 – Court & Government Connectors

**Zweck**  
Spätere Anbindung externer Plattformen.

**Hauptfunktionen**
- Import / Sync
- Eingangserfassung
- Dokumentübernahme
- externe Statusinformationen

**Kernobjekte**
- Connector
- External Event
- Sync Job
- Imported Document

**Paket**
- Premium / Enterprise

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- hoher Marktwert
- starke Differenzierung

**Bemerkungen**
Beginnt erst, wenn der Core stabil ist.

---

## M23 – Knowledge Base / Playbooks

**Zweck**  
Wiederverwendung von Wissen, Checklisten und Standardabläufen.

**Hauptfunktionen**
- Wissenseinträge
- Playbooks
- Checklisten
- Vorlagenreferenzen
- interne Standards

**Kernobjekte**
- Knowledge Entry
- Playbook
- Checklist
- Knowledge Tag

**Paket**
- Premium

**MVP-Status**
- Nein, aber früh architektonisch vorbereiten

**Geschäftlicher Nutzen**
- Know-how-Sicherung
- Produktivitätsgewinn
- starke Bindungswirkung

**Bemerkungen**
Später eng mit Templates und Research koppeln.

---

## M24 – Legal Reference & Research

**Zweck**  
Mandatsbezogener Zugriff auf Normen, Gesetze und Vorschriften.

**Hauptfunktionen**
- Referenzsuche
- Normverweise
- Speicherung relevanter Funde
- Verknüpfung mit Matter / Dokumenten

**Kernobjekte**
- Legal Reference
- Citation
- Research Note
- Matter Reference Link

**Paket**
- Premium / Enterprise

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- juristische Produktivitätssteigerung
- spätere Differenzierung

**Bemerkungen**
Nicht MVP; erst sinnvoll nach stabilem Core.

---

## M25 – AI Assist & Cost Control

**Zweck**  
Kontrollierte Einbindung externer KI-Dienste im Kanzleikontext.

**Hauptfunktionen**
- Provider-Konten
- Request-Logging
- Kosten / Token
- Budgetgrenzen
- Assistenzfunktionen für Recherche und Zusammenfassung

**Kernobjekte**
- AI Provider Account
- AI Request Log
- AI Usage Metric
- AI Cost Entry
- User AI Budget

**Paket**
- Premium / Enterprise

**MVP-Status**
- Nein, Phase 2

**Geschäftlicher Nutzen**
- starkes Verkaufsargument
- kontrollierte statt wilde KI-Nutzung

**Bemerkungen**
Nur als Assistenz, nie als Ersatz für Workflow-Logik.

---

## M26 – Client Portal

**Zweck**  
Spätere externe Mandanteninteraktion.

**Hauptfunktionen**
- Dokumentbereitstellung
- Upload
- Statussicht
- Kommunikationsfenster

**Kernobjekte**
- Portal User
- Portal Document
- Portal Message
- Portal Access Policy

**Paket**
- Enterprise / Add-on

**MVP-Status**
- Nein

**Geschäftlicher Nutzen**
- Mandantenservice
- Wettbewerbsvorteil

**Bemerkungen**
Nicht vor Stabilisierung des internen Kerns.

---

## M27 – API / Webhooks / External Integration Layer

**Zweck**  
Saubere technische Integrationsfläche.

**Hauptfunktionen**
- API-Zugriffe
- Webhooks
- externe Events
- Integrationsauthentifizierung

**Kernobjekte**
- API Client
- Webhook Endpoint
- Integration Event
- Access Token

**Paket**
- Enterprise

**MVP-Status**
- Nein, aber strukturell wichtig

**Geschäftlicher Nutzen**
- Integrationsfähigkeit
- Zukunftssicherheit

**Bemerkungen**
Für spätere Partner- und Connector-Strategie zentral.

---

## Modul-Priorisierung nach Phase

### Phase MVP
- M01 CRM / Intake Basic
- M02 Intake & Conflict Gate
- M03 Client Management
- M04 Matter Management
- M05 Engagement & Contract Basics
- M06 Document Store
- M07 Template Engine Basic
- M09 Case Workspace / Task Engine
- M10 Prazo & Calendar Basic
- M12 Communications Log
- M14 Billing Basic
- M15 Finance Ops & Liquidity Basic
- M17 Security / Roles / Audit Core

### Phase 1.5 / frühe Premium-Vorbereitung
- M08 Advanced Document Assembly
- M16 Finance Reporting & Handover
- M19 Management Dashboard
- M20 Workflow / BPMN Engine
- M23 Knowledge Base / Playbooks

### Phase 2
- M11 Advanced Prazo Rules & Escalations
- M13 Shared Inbox & Smart Routing
- M24 Legal Reference & Research
- M25 AI Assist & Cost Control

### Phase 3 / Enterprise
- M18 LGPD & Governance Advanced
- M21 Standard Process Governance
- M22 Court & Government Connectors
- M26 Client Portal
- M27 API / Webhooks / External Integration Layer

---

## Paketlogik in einem Satz

- **Standard** macht die Kanzlei arbeitsfähig  
- **Premium** macht sie schneller, transparenter und professioneller  
- **Enterprise** macht sie integrierter, kontrollierter und skalierbarer

---

## Arbeitsfazit

Der Module Catalog v1 übersetzt den Projektfahrplan in ein belastbares Produktportfolio.  
Er eignet sich als Grundlage für:

- GitHub-Dokumentation
- spätere README-/Docs-Struktur
- Priorisierung von Domain-Entities
- Epic-Planung
- Preis- und Paketlogik


---

## Ergänzende Festlegungen zu Paketierung, Signatur und Betrieb (Stand: 2026-03-21)

Diese Ergänzungen präzisieren die Modulstrategie, ohne die fachliche Moduldefinition zu verändern.

### A. Open-Core-Zuordnung
- **Standard-Module** gehören grundsätzlich in den produktiven Kern bzw. in den offen definierbaren Standard-Layer.
- **Premium-Module** werden als **separate, signierte Erweiterungspakete** vorgesehen.
- **Enterprise- und Partner-Module** werden als **separate signierte Add-ons** bzw. kontrollierte Integrationspakete behandelt.

### B. Signatur- und Herkunftsmodell
Für Legalis werden künftig nicht nur Codepakete, sondern auch fachliche Artefakte unterschieden:
- **Extension Packages** für Premium-/Enterprise-Funktionen
- **Process Packs** für offizielle Standardprozesse
- **Template / Policy / Connector Packs** für kontrollierte Zusatzlogik

Diese Artefakte sollen kryptographisch signiert werden. Für v1 ist **Ed25519** als Standard vorgesehen.

### C. Abo- und Aktivierungsmodell
Premium-Funktionen gelten nicht schon durch Installation als freigeschaltet. Maßgeblich ist eine gültige Kombination aus:
- Basislizenz
- Paket-/Manifest-Signatur
- ggf. gültiger Subscription-Lease

Dadurch können Premium- oder Enterprise-Pakete lokal vorhanden, aber ohne gültige Laufzeitfreigabe inaktiv sein.

### D. Architekturkonsequenzen für ausgewählte Module

#### D.1 M20 – Workflow / BPMN Engine
- Der fachliche Workflow-Kern bleibt Produktkern von Legalis.
- Falls Imixs / Open-BPMN eingesetzt werden, erfolgt die technische Umsetzung **isoliert als separater Java-Dienst** mit API-Kopplung an den Python-Core.
- Offizielle Workflow-Definitionen sind als signierte Prozesspakete vorzusehen.

#### D.2 M21 – Standard Process Governance
- Dieses Modul wird zur zentralen Schicht für:
  - Herkunft offizieller Standardprozesse
  - Änderungsfreigaben
  - Schulungs-/Partnernachweise
  - Unlock-Tokens und Zertifikate
  - read-only Schutz offizieller Artefakte
- Standardprozesse und kundenspezifische Erweiterungen müssen technisch klar unterscheidbar bleiben.

#### D.3 M22 – Court & Government Connectors
- Connectoren sind nicht Bestandteil des offenen Kerns.
- Sie werden als separat auslieferbare, signierte Add-ons vorgesehen.
- Je nach externer Plattform können pro Connector zusätzliche Lizenz-, Wartungs- oder API-Nutzungsbedingungen gelten.

#### D.4 M27 – API / Webhooks / External Integration Layer
- Dieses Modul bildet die technische Integrationsschicht für:
  - externe Systeme
  - Partnererweiterungen
  - signierte Add-ons
  - optional den Java-Workflow-Dienst
- Authentifizierung, Schlüsselverwaltung und Auditierbarkeit sind hier besonders streng zu definieren.

### E. Deployment-Bezug des Modulkatalogs
- Referenzbetrieb für den gesamten Modulstack ist zunächst **Linux + Docker/Compose**.
- **Proxmox-VM** ist das primäre On-Prem-Zielszenario.
- **LXC-Appliance** bleibt eine mögliche spätere Komfortdistribution.
- **K3s** ist eine spätere Skalierungsoption für größere oder verteilte Installationen.

### F. Native Verify-Komponenten
Für Signatur-, Manifest- und Lease-Prüfung kann später eine kleine native Bibliothek in **ANSI C oder Rust** ergänzt werden. Diese ist jedoch nur ein optionaler Härtungsbaustein und nicht die fachliche Hauptschicht der Lizenzlogik.
