# Legalis – Projektfahrplan, Produktmodell und Architekturgrundlagen (v2)

## Zweck dieses Dokuments

Dieses Dokument hält den derzeitigen fachlichen und technischen Stand für **Legalis** fest.  
Es dient als verbindliche Arbeitsgrundlage für die nächsten Entwicklungsphasen und soll in die Projektquellen übernommen werden.

Der Fokus liegt auf:

- Produktphilosophie
- Referenz-Prozessmodell einer brasilianischen Soll-Kanzlei
- Modulstruktur
- Paketlogik
- MVP-Abgrenzung
- Technologieentscheidungen
- offene Architekturfragen
- konkretisierte Annahmen aus dem Pilotkundenkontext

---

## 1. Grundannahme und Produktphilosophie

Legalis soll **nicht** jede gewachsene Sonderlogik einzelner Kanzleien nachbilden.

Stattdessen folgt Legalis einem bewusst standardorientierten Ansatz:

> **Legalis definiert eine generische brasilianische Soll-Kanzlei mit belastbaren Standardprozessen.**  
> Kanzleien übernehmen diese Best Practices oder entscheiden sich bewusst für klar abgegrenzte Erweiterungen.

Dieser Ansatz folgt dem Grundsatz:

- **Standard zuerst**
- **Konfiguration vor Customizing**
- **Workflow vor KI**
- **Erweiterbarkeit nur an klar definierten Schnittstellen**

Legalis ist damit nicht nur „Kanzleisoftware“, sondern ein:

> **digitales Betriebsmodell für brasilianische Kanzleien**

---

## 2. Pilotkunde und Zielsegment v1

### 2.1 Primärer Startzielkunde
**Mychelle Maciel Advogados**

### 2.2 Organisationsprofil
- 3 festangestellte Anwälte
- 1 Sekretärin
- externe Buchhaltung / Steuerberatung durch Steuerbüro
- Implementierung und erste Produktbegleitung direkt durch den Gründer

### 2.3 Fachlicher Schwerpunkt des Pilotbetriebs
- Immobilienrecht
- Geschäftsgründungen
- Golden Visa / ausländische Investoren
- arbeitsrechtliche Streitigkeiten im Umfeld von Kundenunternehmen
- typische Fälle rund um Kündigung, Urlaubstage, Überstunden, Abfindungen

### 2.4 Produktstrategische Bedeutung
Der Pilotkunde ist groß genug, um echte Kanzleiprozesse abzubilden, aber klein genug, um ein **strikt standardisiertes MVP** sauber einzuführen.  
Damit eignet sich die Kanzlei sehr gut als Referenzumgebung für die erste belastbare „Legalis Reference Law Firm Brazil v1“.

---

## 3. Strategische Leitprinzipien

### 3.1 Workflow first, AI later
Die primäre Intelligenz von Legalis liegt im **modellierten Workflow**, nicht in KI.

- Workflow ist deterministisch
- Workflow ist auditierbar
- Workflow ist trainierbar
- Workflow ist reproduzierbar
- Workflow ist robuster als probabilistische Assistenz

KI darf später unterstützen, aber nicht steuern.

### 3.2 Standardprozess statt Sonderfalllogik
Das MVP basiert auf einer **kanzleineutralen Referenzorganisation**.  
Sonderfälle werden erst später und nur gezielt berücksichtigt.

### 3.3 Core vs. Configuration vs. Extension
Legalis trennt klar zwischen:

- **Core**: unverzichtbare Kernfunktionen
- **Configuration**: ohne Code anpassbare Parameter
- **Extensions**: spätere Premium-/Enterprise-Funktionen

### 3.4 Operative Führung statt Vollsubstitution externer Spezialsoftware
Legalis soll betriebliche und operative Kanzleisteuerung ermöglichen, ohne im MVP sofort alle angrenzenden Disziplinen vollständig zu ersetzen, etwa:

- Steuerberatung
- Vollbuchhaltung
- komplexe externe Gerichtssystemintegration
- juristische KI-Expertensysteme

---

## 4. Legalis Reference Law Firm Brazil v1

Die folgende Prozesslandkarte bildet die fachliche Soll-Kanzlei für das MVP und die spätere Produktentwicklung ab.

### 4.1 Mandantengewinnung und Erstkontakt
**Ziel:** Aus Interessenten strukturierte, dokumentierte Anfragen machen.  
**Modul:** CRM / Intake  
**Paket:** Standard

### 4.2 Konfliktprüfung und Annahmeentscheidung
**Ziel:** Vor Mandatsannahme Interessenkonflikte und Annahmefähigkeit prüfen.  
**Modul:** Intake & Compliance Gate  
**Paket:** Standard

### 4.3 Onboarding des Mandanten
**Ziel:** Stammdaten, Ansprechpartner, Kommunikationskanäle und Dokumente erfassen.  
**Modul:** Client Management  
**Paket:** Standard

### 4.4 Mandatsanlage und Vertragsgrundlagen
**Ziel:** Aus einer Anfrage einen formellen Fall machen.  
**Modul:** Matters / Engagements  
**Paket:** Standard

### 4.5 Dokumentenerzeugung und Vorlagenarbeit
**Ziel:** Standarddokumente reproduzierbar und effizient erzeugen.  
**Modul:** Document Assembly & Templates  
**Paket:** Standard (Basis), Premium (fortgeschritten)

### 4.6 Fallbearbeitung und Aufgabensteuerung
**Ziel:** Tägliche operative Bearbeitung eines Mandats steuern.  
**Modul:** Case Workspace / Task Engine  
**Paket:** Standard

### 4.7 Fristen- und Terminmanagement
**Ziel:** Keine Frist versäumen, Wiedervorlagen systematisch steuern.  
**Modul:** Prazo & Calendar Control  
**Paket:** Standard, Premium für erweiterte Regeln

### 4.8 Eingangs- und Kommunikationsmanagement
**Ziel:** E-Mails, Uploads, Zustellungen und Nachrichten fallbezogen bündeln.  
**Modul:** Inbox / Communications Hub  
**Paket:** Standard (Basis), Premium (fortgeschritten)

### 4.9 Externe Verfahrens- und Plattformanbindung
**Ziel:** Anbindung an gerichtliche und behördliche Plattformen.  
**Modul:** Court & Government Connectors  
**Paket:** Premium / Enterprise

### 4.10 Honorare, Auslagen, cobrança und Zahlungsstatus
**Ziel:** Juristische Arbeit wirtschaftlich sauber abbilden.  
**Modul:** Billing & Finance  
**Paket:** Standard (Basis), Premium (fortgeschritten)

### 4.11 Wissensmanagement und Standardisierung
**Ziel:** Vorlagen, Checklisten und Standardwissen wiederverwendbar machen.  
**Modul:** Knowledge Base  
**Paket:** Premium

### 4.12 LGPD, Rechte, Audit und Governance
**Ziel:** Datenschutz, Nachvollziehbarkeit und Rollensteuerung sichern.  
**Modul:** Security, Audit & LGPD  
**Paket:** Standard (Core), Enterprise (erweitert)

### 4.13 Management, KPIs und Kanzleisteuerung
**Ziel:** Die Kanzlei als Unternehmen führen.  
**Modul:** Management Dashboard  
**Paket:** Premium

### 4.14 Automatisierungen und Workflow-Engine
**Ziel:** Wiederkehrende Kanzleiarbeit standardisieren.  
**Modul:** Workflow / BPMN Engine  
**Paket:** Premium / Enterprise

### 4.15 Verbindlichkeiten- und Kostenmanagement
**Ziel:** Alle laufenden und fallbezogenen Kosten strukturiert erfassen.  
**Modul:** Finance Ops & Liquidity  
**Paket:** Standard

### 4.16 Zahlungsplanung und Liquiditätskalender
**Ziel:** Ein- und Ausgänge auf Kalenderbasis vorhersehbar machen.  
**Modul:** Finance Ops & Liquidity  
**Paket:** Standard (Basis), Premium (Forecast / Reporting)

### 4.17 Monatsabschluss und Reportübergabe
**Ziel:** Finanzdaten für interne oder externe Buchhaltung exportierbar aufbereiten.  
**Modul:** Finance Reporting & Handover  
**Paket:** Premium / Enterprise

### 4.18 Juristische Recherche und Referenzzugriff
**Ziel:** Relevante Normen, Gesetze und Vorschriften im Mandatskontext auffindbar machen.  
**Modul:** Legal Reference & Research  
**Paket:** nicht MVP, später Premium / Enterprise

### 4.19 KI-gestützte Assistenz und Kostenkontrolle
**Ziel:** Externe KI-Dienste kontrolliert nutzbar machen.  
**Modul:** Legal Research & AI Assist  
**Paket:** nicht MVP, später Premium / Enterprise

---

## 5. Produktpakete

### 5.1 Standardpaket
Das Standardpaket muss eine Kanzlei **voll arbeitsfähig** machen.

Enthalten:
- CRM / Intake Basic
- Client Management
- Matter Management
- Task & Case Workspace
- Prazo & Calendar Basic
- Document Management Basic
- Template Basic
- Billing Basic
- Finance Ops Basic
- Security / Roles / Audit Core
- Basic Communications Log

### Ziel
Eine kleine bis mittlere Kanzlei soll mit dem Standardpaket real arbeiten können.

### 5.2 Premiumpaket
Premium verkauft nicht bloß mehr Funktionen, sondern:

- Zeitersparnis
- geringeres Fehlerrisiko
- mehr Transparenz
- bessere Standardisierung
- bessere wirtschaftliche Steuerung

Enthalten:
- Advanced Templates & Document Assembly
- Shared Inbox & Smart Routing
- Advanced Prazo Rules & Escalations
- Knowledge Base / Playbooks
- Management Dashboard / KPIs
- Workflow Automation
- Advanced Billing / cobrança / repasse
- Finance Reporting & Handover
- Team Collaboration / Approval Flows

### 5.3 Enterprise / Add-ons
Hier liegen Integrationen, Governance und hohe Marge.

Enthalten:
- Court & Government Connectors
- Mandantenportal
- Multi-Office / Filialstruktur
- Governance / Compliance Reporting
- API / Webhooks / Fremdsystemanbindung
- rechtsgebietsspezifische Prozesspakete
- BPMN Designer für Consultants / Partner
- AI Governance / AI Cost Control / private AI infrastructure

---

## 6. MVP-Abgrenzung

### 6.1 Unbedingt in den MVP
Diese Funktionen bilden den arbeitsfähigen Kern:

- Client Management
- Matter Management
- Task Engine
- Deadline / Prazo Management
- Document Store
- Basic Template Engine
- Billing Basic
- Finance Ops Basic
- Roles / Permissions / Audit Core
- Basic Communications Log

### 6.2 Bewusst nicht voll im MVP
Diese Themen werden architektonisch vorbereitet, aber nicht vollständig ausgebaut:

- BPMN Designer für freie Modellierung
- Mandantenportal
- tiefe externe Gerichtssystem-Connectoren
- KI-Assistenz
- juristische Referenzbibliothek
- komplexe BI / Forecasting
- Fachmodule je Rechtsgebiet
- tiefe Bankintegration
- Vollbuchhaltung / Steuerdeklaration

### 6.3 Früh als Premium vorbereiten
Diese Funktionen sollten architektonisch früh mitgedacht werden:

- Workflow Engine
- Knowledge Base
- KPI Dashboard
- Smart Intake
- Shared Inbox
- Advanced Template Rendering
- Finance Reporting
- AI Request / Cost Logging

---

## 7. BPMN- und Workflow-Governance

### 7.1 Grundsatz
Die Modellierung bleibt zu Beginn **absichtlich eng**.  
Es ist einfacher, später fehlende Elemente kontrolliert hinzuzufügen, als bereits etablierte Modellierungsfreiheiten wieder einzuschränken.

### 7.2 Erlaubte BPMN-Kernelemente für v1
Für das reduzierte Modell sollen zunächst nur folgende Konzepte vorgesehen werden:

- Start Event
- End Event
- Task
- User Task
- Service Task
- Exclusive Gateway (XOR)
- Parallel Gateway (AND)
- Sequence Flow
- Subprocess (nur kontrolliert)
- Data Object / Dokumentreferenz (optional einfach gehalten)
- Lane / Role

### 7.3 Zunächst nicht freigeben
Vorerst nicht im Standardmodell:

- Event-based Gateway
- Inclusive Gateway
- Complex Gateway
- Boundary Events in voller Breite
- Ad-hoc Subprocesses
- Choreography / Conversation
- freie Eskalations- und Kompensationsmuster
- freie Timer-Modellierung durch Fachanwender

### 7.4 Strikte Trennung
Es gilt eine harte Trennung zwischen:

- **Standardprozessen**
- **kundenspezifischen Erweiterungen**

Standardprozesse bleiben Eigentum und Verantwortungsbereich von Legalis.  
Kundenspezifische Erweiterungen werden logisch und vertraglich separat behandelt.

### 7.5 Änderungszugriff auf Standardprozesse
Änderungen an Standardprozessen sollen nur nach spezifischer Schulung möglich sein.  
Dafür wird ein kontrolliertes Freigabemodell vorgesehen:

- Pflichtschulung
- erfolgreicher Abschluss
- formale Freischaltung
- technischer Schlüssel / Zertifikat / Berechtigungsstufe für Änderungszugriff

### 7.6 Haftung und Governance
Für kundenspezifische Erweiterungen außerhalb des Legalis-Standards gilt:

- Verantwortung liegt beim jeweiligen Implementierer
- keine automatische Haftungsübernahme durch Legalis
- klare Kennzeichnung als Extension / Custom Layer
- separate Versionierung und Exportierbarkeit

---

## 8. Finanzmodul: strategische Einordnung

Legalis soll **keine klassische Buchhaltungssoftware im MVP** werden.

Stattdessen ist das Ziel:

> **Financial Operations & Liquidity Management for Law Firms**

Damit unterstützt Legalis die operative Kanzleiführung durch:

- Forderungen
- Verbindlichkeiten
- Auslagen
- Gebühren
- Gehälter
- wiederkehrende Kosten
- Fälligkeitskalender
- Liquiditätsvorschau
- Bankkontenübersicht
- Reportübergabe an Buchhaltung / Steuerberatung

### 8.1 Finanzsicht im MVP
Im MVP startet Legalis bewusst einfach mit einer **Ein- und Ausgabenführung**:

- Einnahmen
- Ausgaben
- wiederkehrende Ausgaben
- manuell gepflegte Bankkontosalden
- einfache Liquiditätsrechnung auf Kalenderbasis

### 8.2 Wiederkehrende Ausgaben
Wiederkehrende Kosten werden über einen Scheduler automatisch in die Folgemonate fortgeschrieben.

### 8.3 Bankkontosalden
Für die Liquiditätsberechnung werden Bankkontosalden bereits im MVP berücksichtigt.  
Es reicht zunächst, den letzten bekannten Kontoauszug bzw. Saldo manuell vorzugeben.

### 8.4 Was noch nicht MVP ist
Nicht Teil des MVP:

- automatisches Einscannen von Kontoauszügen
- automatischer Import ganzer Kontobewegungen
- tiefe Bankintegration
- vollwertige Buchhaltung / Steuerlogik

### 8.5 Exportformate im MVP
Für externe Buchhaltung / Steuerberatung werden zunächst nur einfache Ausgabeformen unterstützt:

- PDF-Report
- Plaintext / CSV-artige Klartextausgabe

---

## 9. Dokumentengenerierung: Architekturentscheidung

Für workflow-gesteuerte Kanzleidokumente gilt:

> **JSON-first mit DOCX/DOTX als Kanzlei-Templateformat und PDF als verbindlichem Endformat**

### 9.1 Entscheidung
- **Internes Zwischenformat:** JSON
- **Template-Autorenformat im MVP:** DOCX oder DOTX
- **Verbindliches Ausgabeformat:** PDF

### 9.2 Begründung
DOCX/DOTX ist für Kanzleien praxistauglich, bearbeitbar und weit verbreitet.  
PDF ist für finale, unveränderliche Ausgabe und Archivierung geeignet.  
JSON trennt Fachlogik sauber von Layoutlogik.

### 9.3 Minimal erforderliche Template-Versionierung
Ja, eine **minimale Template-Versionierung ist weiterhin nötig**.

Nur eine UID im Dateinamen reicht langfristig nicht aus, weil zusätzlich steuerbar bleiben muss:

- welche Revision aktiv ist
- welche Revision durch welchen Workflow referenziert wird
- ob ein Dokument aus einer älteren oder neueren Vorlage erzeugt wurde
- welche Vorlagen importiert, archiviert oder ersetzt wurden

Daher sollte jedes Template mindestens folgende Metadaten besitzen:

- `template_id` (stabil)
- `revision` oder `version`
- `document_type`
- `status` (draft / active / retired)
- `source_filename`
- `imported_at`
- optional Prüfsumme / Hash

### 9.4 Praktischer Importansatz
Beim Import von DOCX/DOTX-Dateien kann zusätzlich eine UID vor den Dateinamen gestellt werden.  
Außerdem können Template-Metadaten im Dokument selbst und in der Datenbank gespeichert werden.  
Der Dateiname allein ist jedoch **nicht** die maßgebliche Wahrheit.

### 9.5 PDF-Rendering
Für Reports und HTML-nahe Ausgaben ist **HTML → WeasyPrint → PDF** ein sehr guter Startweg.  
Für workflowbasierte DOCX-Templates soll PDF jedoch nicht über denselben Weg erzwungen werden.

Pragmatische Entscheidung:

- **Reports / Auswertungen / Finanzberichte:** HTML + WeasyPrint
- **klassische Kanzleidokumente aus DOCX-Templates:** zunächst DOCX-Ausgabe, PDF-Finalisierung als separater Rendering-Schritt

### 9.6 Was nicht Hauptweg sein soll
- **LaTeX** nicht als primäres Autorenformat
- **Markdown allein** nicht als zentrales Kanzleiformat
- **DOCX als Systemlogik** vermeiden

### 9.7 Gewünschte Architektur
1. **Document Schema**  
   Strukturierte Datenobjekte

2. **Template Manifest**  
   Metadaten, Versionen, Pflichtfelder, Varianten

3. **Template Content**  
   DOCX/DOTX-Vorlagen mit kontrollierter Platzhalterlogik

4. **Renderer**  
   DOCX, PDF, später HTML / Typst / Spezialrenderer

---

## 10. KI: strategische Einordnung

Legalis soll KI **nicht** als primären Steuerungsmechanismus verwenden.

### Grundsatz
> **Nicht KI führt die Kanzlei, sondern der Prozess. KI darf nur helfen.**

### KI ist in Legalis:
- optional
- kontrolliert
- kostenüberwacht
- klar gekennzeichnet
- nie Ersatz für Workflow-Logik

### Phase-2-Ausgangspunkt
Im aktuellen Pilotumfeld nutzt die Kanzlei bereits **ChatGPT Plus** für alle Mitarbeiter.  
Damit ist für Phase 2 besonders relevant:

- Anbindung externer KI-Nutzung
- Logging / Budget / Kostenübersicht
- kontrollierte Recherche- und Assistenzfunktionen

### Provider-Strategie
Welche weiteren Provider unterstützt werden, wird erst nach Marktvalidierung entschieden.  
Eine spätere Umfrage im Kanzleiumfeld kann dafür Input liefern.

### Spätere sinnvolle KI-Funktionen
- Zusammenfassungen
- Dokumentanalyse
- Recherchehilfe
- Suchvorschläge
- Entwurfshilfen
- Klassifikation mit Nutzerprüfung

### Ergänzend erforderlich
Wenn KI integriert wird, dann nur mit:

- Provider-Verknüpfung
- Request-Logging
- Token-Verbrauch
- Kostenübersicht
- Budgetgrenzen
- Nutzer- und Teamrichtlinien

---

## 11. Zielarchitektur auf einen Blick

### 11.1 Operativer Kern
Mandant → Mandat → Aufgabe → Frist → Dokument → Abrechnung → Audit

### 11.2 Premium-Mehrwert
Standardisierung → Automatisierung → Transparenz → Wissensnutzung → Steuerung

### 11.3 Enterprise-Mehrwert
Integration → Governance → Skalierung → Spezialisierung

---

## 12. Technologierichtung

### 12.1 Backend
- Python als bevorzugte Kernsprache
- modulare serviceorientierte Architektur, aber MVP zunächst pragmatisch
- Workflow- und Regelorientierung im Kern

### 12.2 Workflow
- Workflow Engine als zentrales Steuerungsprinzip
- BPMN nur in kontrolliertem, reduziertem Umfang
- kein freies Low-Code-Chaos im MVP

### 12.3 Dokumente
- JSON als Datenwahrheit
- DOCX/DOTX-Vorlagen
- PDF-Ausgabe
- später optional zusätzliche Renderer

### 12.4 Daten und Governance
- saubere Rollen- und Rechtearchitektur
- Auditierbarkeit
- Versionierung von Templates und Workflows
- konfigurierbare, aber kontrollierte Erweiterungspunkte

---

## 13. Noch offene Fragen

Das Grundmodell steht. Offen sind vor allem noch Ausgestaltungsfragen.

### 13.1 Produkt und Markt
- Wie weit wird das Pilotmodell später auf andere Kanzleien verallgemeinert?
- Welche Rechtsgebiete werden nach dem Piloten als Nächstes unterstützt?
- Wie stark wird der Beratungs-/Customizing-Anteil in Phase 1 tatsächlich sein?

### 13.2 Workflow und BPMN
- Wie genau wird der technische Schlüssel für Standardprozess-Änderungen umgesetzt?
- Wie werden Standardprozesse von kundenspezifischen Prozesslayers getrennt versioniert?
- Wie strikt wird der Freigabeprozess für neue BPMN-Elemente organisiert?

### 13.3 Dokumente
- Welche Platzhalter- und Bedingungssyntax wird im DOCX/DOTX-Template offiziell erlaubt?
- Wie erfolgt die PDF-Finalisierung klassischer DOCX-Dokumente im ersten lauffähigen Setup?
- Welche Vorlagen werden zuerst praktisch benötigt?

### 13.4 Finanzen
- Welche minimalen Konten-/Kategorienstrukturen braucht der Pilotkunde?
- Welche Form sollen die PDF-/Plaintext-Reports für die externe Buchhaltung zuerst haben?
- Ab wann wird Forecasting über das Basisniveau hinaus sinnvoll?

### 13.5 Integrationen
- Welche externen Plattformen werden als Erste wirklich priorisiert?
- Welche Kommunikationskanäle werden zuerst angebunden?
- Wie wird Import / Export nach außen technisch standardisiert?

### 13.6 KI und Research
- Welche konkreten Assistenzfälle bringen dem Pilotkunden zuerst echten Nutzen?
- Wie wird die Kostenübersicht bei ChatGPT-/Provider-Nutzung technisch modelliert?
- Ab wann lohnt sich die Research-Bibliothek praktisch genug für Phase 2?

---

## 14. Nächste sinnvolle Arbeitsschritte

### Kurzfristig
1. Modulportfolio als offizielles Produktdokument formulieren  
2. MVP-Systemgrenzen endgültig festziehen  
3. erste Domain-Entities definieren  
4. Workflow-Kernprozesse priorisieren  
5. Dokument-Rendering-Pipeline technisch skizzieren

### Danach
6. Datenmodell für Client / Matter / Task / Deadline / Document / Finance entwerfen  
7. Rollen- und Rechtemodell definieren  
8. Template-Manifeste und Platzhalterkonzept festlegen  
9. Standard-Workflows je Kernprozess definieren  
10. Finance Ops Basismodell spezifizieren

---

## 15. Arbeitsfazit

Das heutige Ergebnis reicht aus, um Legalis nicht nur als Idee, sondern als **strukturiertes Produktvorhaben** festzuschreiben.

Wesentliche Festlegungen:

- Legalis ist ein digitales Betriebsmodell für brasilianische Kanzleien
- Standardisierung geht vor Individualisierung
- Workflow steht über KI
- MVP zuerst arbeitsfähig, nicht maximal vollständig
- Finanz- und Liquiditätssicht gehören in den Kern
- Dokumentengenerierung folgt dem Prinzip:
  **JSON-first, DOCX/DOTX für Templates, PDF für finale Ausgabe**
- spätere Premium- und Enterprise-Module sind bereits logisch angelegt
- BPMN bleibt im Standard zunächst bewusst eingeschränkt
- Standardprozesse und kundenspezifische Erweiterungen werden strikt getrennt

Dieses Dokument bildet damit die Grundlage für:
- Produktstrategie
- Architekturentscheidungen
- Modulplanung
- Priorisierung der Entwicklung
- spätere GitHub-/Projektquellen-Dokumentation


---

## 16. Finalisierte Architekturentscheidungen (Stand: 2026-03-21)

Die folgenden Punkte gelten für die nächste Projektphase als **vorläufig festgezogen** und ersetzen frühere offene Grundsatzdiskussionen, soweit unten nicht ausdrücklich wieder geöffnet.

### 16.1 Entwicklungs- und Kernsprache
- **Python** bleibt die bevorzugte Kernsprache von Legalis.
- Ziel ist ein **modularer Monolith** für v1, nicht sofort eine breite Microservice-Landschaft.
- **FastAPI** wird als bevorzugtes Backend-Framework für den Core angenommen.
- **SQLAlchemy 2** wird als ORM-/Datenzugriffsschicht vorgesehen.
- Eine optionale kleine native Verify-Bibliothek in **ANSI C oder Rust** bleibt möglich, ist aber **nicht** Voraussetzung für v1.

### 16.2 Datenbank
- **PostgreSQL** ist die primäre Datenbank für Entwicklung, Test und Produktion.
- **SQLite** ist höchstens noch als Hilfsoption für isolierte lokale Tests oder sehr frühe Experimente vorgesehen, nicht mehr als strategische Produktdatenbank.
- PostgreSQL-spezifische Fähigkeiten dürfen bewusst genutzt werden, sofern sie die Architektur vereinfachen oder stabiler machen.

### 16.3 Betriebssystem und Zugriffsmodell
- Legalis wird für den Serverbetrieb zunächst **Linux-only** geplant.
- Mitarbeitende greifen primär per **Webbrowser** auf die Anwendung zu.
- Der Application Server wird durch Legalis selbst oder durch geschulte Partner aufgesetzt und betreut.
- Dieses Modell vereinfacht Backup, Härtung, Monitoring und Support.

### 16.4 Deployment- und Betriebsmodell
- Das **kanonische Auslieferungsformat** für Legalis ist zunächst ein **Docker-/Compose-Stack**.
- Das **Referenzdeployment auf Proxmox** ist eine **VM mit Docker/Compose**.
- Eine **LXC-Appliance** bleibt als spätere Komfortvariante für kleinere On-Prem-Installationen möglich, ist aber **nicht** die primäre Quelle der Wahrheit für Packaging und Betrieb.
- **K3s / leichtgewichtiges Kubernetes** ist eine spätere Skalierungsoption für größere Kanzleien, Partnerbetrieb oder Cloud-Szenarien, aber **nicht** der Standardpfad für v1.

### 16.5 Reverse Proxy
- Für den ersten belastbaren Setup-Pfad sind **Caddy oder NGINX Open Source** als Reverse Proxy akzeptiert.
- Die endgültige Auswahl kann nach Prototyping entschieden werden.
- Zertifikate, TLS, Routing und Upstream-Absicherung werden zentral über diesen Proxy geführt.

### 16.6 Workflow- und BPMN-Architektur
- Legalis bleibt im Kern **Python-basiert**.
- Falls **Imixs / Open-BPMN** eingesetzt werden, geschieht das **isoliert als separater Java-Dienst**.
- Die Kopplung zwischen Python-Core und BPMN-/Workflow-Dienst erfolgt über klar definierte APIs, nicht durch Vermischung beider Laufzeiten in einem unklaren Mischkern.
- Die reduzierte BPMN-Governance aus Kapitel 7 bleibt weiterhin maßgeblich.

### 16.7 Produkt- und Lizenzmodell
- Legalis wird für die nächste Phase als **Open-Core-Produktmodell** gedacht.
- Der **Core** bleibt logisch von **Premium-/Enterprise-Erweiterungen** getrennt.
- Premium- und Enterprise-Funktionen werden als **separate, signierte Erweiterungspakete** konzipiert.
- Offizielle Standardprozesse, Prozesspakete, Governance-Pakete und sensible Add-ons werden zusätzlich **kryptographisch signiert**.
- Als Signaturstandard wird zunächst **Ed25519** vorgesehen.

### 16.8 Lizenzbetrieb ohne permanenten Lizenzserver
- Es wird **kein permanent verfügbarer Lizenzserver** vorausgesetzt.
- Stattdessen gilt ein **offline-first Modell** mit:
  - Basislizenz
  - signierten Erweiterungspaketen
  - signierten Prozesspaketen
  - optionalen Unlock-Tokens
  - zeitlich begrenzten Subscription-Leases für Abo-Module
- Damit kann ein Kunde Premium-Erweiterungen zwar lokal installiert haben, aber nur mit gültiger Lease aktiv betreiben.

### 16.9 Ablauf- und Downgrade-Verhalten
- Bei Ablauf einer Premium-Lease dürfen Daten **nicht zerstört** werden.
- Bestehende Daten und frühere Premium-Artefakte bleiben sichtbar.
- Nach Ablauf werden Premium-Funktionen kontrolliert auf **read-only**, **deaktiviert** oder **nicht ladbar** gestellt.
- Dieses Verhalten ist Teil des Produktdesigns und kein nachträglicher Notbehelf.

### 16.10 Sicherheitsprinzip
- Der primäre Schutzmechanismus ist **nicht** Code-Obfuskation.
- Der primäre Schutz besteht aus:
  - Trennung von Core und Erweiterungen
  - Signaturen
  - kontrolliertem Laden von Modulen
  - Rollen- und Rechtemodell
  - Auditierbarkeit
  - klarer Herkunft offizieller Standardprozesse
- Native Komponenten in C oder Rust sind nur ergänzende Härtung, kein Ersatz für Architekturdisziplin.

---

## 17. Eingrenzung der noch offenen Fragen

Durch die vorstehenden Architekturentscheidungen sind einige frühere Grundsatzfragen nun **vorläufig beantwortet**. Offen bleiben vor allem noch Ausgestaltungsdetails.

### 17.1 Weiterhin offen
- genaue API-Verträge zwischen Python-Core und einem möglichen Java-Workflow-Dienst
- endgültige Wahl zwischen Caddy und NGINX nach erstem Betriebstest
- genaue Template- und Render-Toolchain für DOCX → PDF im ersten produktiven Setup
- konkrete Struktur der Lizenzdateien, Leases, Tokens und Manifeste
- Definition der ersten offiziellen Standardprozesspakete
- Ausgestaltung eines Partner-/Schulungsmodells für Standardprozessänderungen

### 17.2 Vorläufig nicht mehr als Grundsatzfrage offen
- Python vs. vollständiger Java-Produktkern
- Linux-only vs. Multi-OS-Serverbetrieb
- PostgreSQL vs. SQLite als strategische Hauptdatenbank
- Docker/Compose als Primär-Packaging für v1
- Open Core vs. Vollauslieferung aller Premium-Funktionen im selben Paket

---

## 18. Ergänzende nächste Arbeitsschritte

### Kurz- bis mittelfristig zusätzlich
11. Entwicklungs- und Laufzeitumgebung als separates Referenzdokument festziehen  
12. Lizenz- und Erweiterungsarchitektur technisch konkretisieren  
13. Lizenz-Matrix und OSS-Compliance-Regeln in die Projektdokumentation übernehmen  
14. SBOM-/Lizenz-Scan für Python- und Java-Abhängigkeiten für spätere Releases vorsehen  
15. Packaging-Prototyp für Docker/Compose und optionalen Java-Workflow-Dienst entwerfen
