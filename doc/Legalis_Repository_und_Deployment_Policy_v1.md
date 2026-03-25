# Legalis – Repository- und Deployment-Policy v1

## Zweck dieses Dokuments

Dieses Dokument definiert die verbindliche Ablage-, Versions- und Deployment-Strategie für den Legalis-Core sowie für kundenspezifische Erweiterungen.

Es dient als Arbeitsgrundlage für:

- Entwicklung
- Consulting
- Schulung
- Release-Vorbereitung
- Test- und Pilotumgebungen
- spätere Kundeninstallationen

Die Policy soll verhindern, dass Standardprozesse, kundenspezifische Prozesslogik, produktiver Code, Schulungsmaterial und sensible Kundendaten ungeordnet vermischt werden.

---

## 1. Grundsatz

Legalis verfolgt eine klare Trennung zwischen:

- **Core**
- **Standardprozessen**
- **Schulungs- und Governance-Dokumentation**
- **kundenspezifischen Erweiterungen**
- **kundenspezifischen Betriebsdaten**

Dabei gilt:

> **Der Legalis-Core und die offiziellen Standardprozesse sind gemeinsame Produktartefakte. Kundenspezifische Erweiterungen sind davon organisatorisch, rechtlich und technisch getrennt zu behandeln.**

---

## 2. Zentrales Core-Repository

### 2.1 Verbindliches Core-Repository

Das zentrale Repository für den Produktkern lautet:

`natalnetwork/legalis`

Dieses Repository ist die maßgebliche Quelle für:

- Backend-Code
- allgemeine Projektdokumentation
- BPMN-Governance und Schulungsmaterial
- offizielle Legalis-Standardprozesse
- allgemeine Workflow-Beispiele
- technische Deploy- und Testhilfen für den Produktkern

### 2.2 Ein Repository, mehrere Arbeitskopien

Dasselbe Repository darf und soll auf mehreren Entwicklungs- oder Testsystemen geklont werden.

Beispiel:

- `legalis-dev` als Arbeitsumgebung für Backend, Dokumentation und Architektur
- `legalis-workflow` als Arbeitsumgebung für BPMN-Modellierung, Workflow-Tests und Runtime-Experimente

Dabei gilt ausdrücklich:

- diese Hosts sind **keine separaten Wahrheiten**
- sie sind **nur unterschiedliche Arbeitskopien desselben Repositories**
- die Git-Historie bleibt zentral
- Änderungen werden über Git synchronisiert

---

## 3. Kundenspezifische Repositories

### 3.1 Keine produktiven Customer Extensions im Core-Repository

Produktive kundenspezifische Erweiterungen gehören **nicht** in das zentrale Core-Repository.

Dazu zählen insbesondere:

- kundenspezifische BPMN-Modelle
- kundenspezifische Prozessvarianten
- kundenspezifische Python-Erweiterungen
- kundenspezifische Konfigurationen
- kundenspezifische Templates
- projektspezifische Integrationslogik
- kundenbezogene technische Mapping-Dateien

### 3.2 Begründung

Kundenspezifische Erweiterungen können enthalten:

- interne Organisationsstrukturen des Kunden
- vertrauliche Freigabe- und Eskalationswege
- wirtschaftlich sensible Prozesslogik
- betriebliche Besonderheiten
- projektspezifisches Know-how
- Betriebsgeheimnisse

Deshalb gelten sie nicht als allgemeines Produktmaterial, sondern als gesondert zu behandelnde Kundenartefakte.

### 3.3 Verbindliche Regel

Für jede produktive kundenspezifische Erweiterung ist ein **separates privates Repository** zu verwenden.

Beispiele:

- `legalis-customer-mychelle`
- `legalis-customer-pilot-a`
- `legalis-customer-xyz`

### 3.4 Keine Customer-Branches im Core-Repo

Kundenspezifische Erweiterungen dürfen **nicht** über langfristige Customer-Branches im Core-Repository organisiert werden.

Gründe:

- erhöhte Verwechslungsgefahr
- höhere Merge-Komplexität
- erhöhtes Risiko versehentlicher Offenlegung
- unklare Verantwortlichkeit
- unsaubere Release-Zuordnung

Die bevorzugte Lösung ist immer:

> **separates privates Kunden-Repository statt Customer-Branch im Core-Repository**

---

## 4. Verzeichnisstrategie im Core-Repository

Die folgende Zielstruktur wird für `natalnetwork/legalis` empfohlen.

```text
legalis/
├── backend/
├── workflow/
│   ├── models/
│   │   └── standard/
│   ├── examples/
│   └── deploy/
├── doc/
│   └── bpmn/
└── .gitignore
```

### 4.1 `backend/`

Enthält den produktiven Code des Legalis-Kerns, insbesondere:

- Python-Backend
- API
- Domain-Logik
- allgemeine Integrationspunkte
- generische Erweiterungsschnittstellen

### 4.2 `workflow/models/standard/`

Enthält nur offizielle Legalis-Standardprozesse.

Dort liegen ausschließlich:

- freigegebene Standardmodelle
- versionierte Core-Prozessmodelle
- keine kundenspezifischen produktiven Varianten

### 4.3 `workflow/examples/`

Enthält didaktische, technische oder interne Demonstrationsmodelle.

Dort können liegen:

- Schulungsbeispiele
- Minimalbeispiele
- Testmodelle ohne Produktstatus
- Anschauungsmaterial für BPMN-Einsteiger

### 4.4 `workflow/deploy/`

Enthält Hilfsmittel zur lokalen oder technischen Workflow-Erprobung.

Zum Beispiel:

- Docker-Compose-Dateien
- Test-Setups
- Engine-bezogene Startskripte
- Runtime-Readmes

### 4.5 `doc/`

Enthält Projektdokumentation und Produktdokumentation.

### 4.6 `doc/bpmn/`

Enthält die verbindlichen BPMN-Dokumente, insbesondere:

- Modellierungshandbuch
- Review-Checklisten
- Quickstarts
- Schulungsunterlagen
- spätere PDF-Fassungen
- bebildertes Lehrmaterial

---

## 5. Verzeichnisstrategie in Kunden-Repositories

Für private Kunden-Repositories wird folgende Grundstruktur empfohlen:

```text
legalis-customer-<kunde>/
├── customer/
│   ├── workflow/
│   │   └── models/
│   │       └── extensions/
│   ├── backend/
│   │   └── extensions/
│   ├── templates/
│   └── config/
└── README.md
```

### 5.1 `customer/workflow/models/extensions/`

Enthält nur kundenspezifische Prozessmodelle oder Varianten.

### 5.2 `customer/backend/extensions/`

Enthält nur kundenspezifischen Code.

### 5.3 `customer/templates/`

Enthält kundenspezifische Dokumentvorlagen.

### 5.4 `customer/config/`

Enthält kundenspezifische Konfigurationsdateien, soweit diese versionierbar und nicht geheimhaltungsbedürftig im engeren Sinne sind.

### 5.5 Secrets

Geheimnisse und Zugangsdaten gehören **nicht** in Git-Repositories.

Dazu zählen insbesondere:

- Passwörter
- API-Keys
- Zertifikate
- private Schlüssel
- produktive Zugangstoken
- Kundensecrets aller Art

Diese gehören in sichere Laufzeitkonfiguration oder Secret-Management.

---

## 6. Deployment-Prinzip

### 6.1 Overlay-Modell

Produktive oder pilotnahe Installationen folgen dem Prinzip:

- **Core-Basis** aus `natalnetwork/legalis`
- **Customer-Overlay** aus dem passenden privaten Kunden-Repository

Das bedeutet:

1. Zuerst wird der Core-Stand bereitgestellt.
2. Danach werden autorisierte kundenspezifische Erweiterungen ergänzt.
3. Die Zielumgebung arbeitet mit der Kombination beider Stände.

### 6.2 Reihenfolge

Verbindliche Reihenfolge:

1. Core synchronisieren
2. Core-Version prüfen
3. passendes Kunden-Repository synchronisieren
4. Kompatibilität prüfen
5. Testen
6. erst dann Demo, Workshop oder Deployment

### 6.3 Keine Vermischung vor Rückführung in den Core

Allgemein nutzbare Verbesserungen aus Kundenprojekten dürfen erst dann in den Core übernommen werden, wenn sie:

- verallgemeinert wurden
- fachlich entkundenspezifiziert wurden
- keine vertraulichen Prozessdetails mehr enthalten
- die Governance-Prüfung bestanden haben

---

## 7. Arbeitsregeln für Consultants und Entwickler

### 7.1 Verbindliche Werkzeuglinie

Für Modellierung, Dokumentation, Repository-Arbeit und technische Erweiterungen ist **VS Code** das Standardwerkzeug.

Das dient der Vereinheitlichung von:

- Schulung
- Support
- Bedienung
- Erweiterungsarbeit
- Git-Synchronisation
- BPMN-Modellierung

### 7.2 Vor jedem Kundeneinsatz oder Workshop

Vor jedem Einsatz ist sicherzustellen, dass die lokale Arbeitskopie aktuell ist.

Mindestens auszuführen:

```bash
git fetch --all --tags
git status
git pull --ff-only
```

Falls ein Kunden-Repository verwendet wird, gilt dieselbe Regel auch dort.

### 7.3 Keine Offline-Wildstände

Consultants dürfen nicht mit unkontrollierten lokalen Sonderständen in Kundentermine gehen.

Verboten sind insbesondere:

- lokale ungepushte Standardprozessänderungen ohne Freigabe
- lokale Kundenvarianten ohne Versionsstand
- Schulungsdateien, die nicht mit dem aktuellen Core-Stand übereinstimmen

### 7.4 Rollenverständnis der Arbeitsumgebungen

Arbeitsumgebungen dürfen unterschiedliche Rollen haben, zum Beispiel:

- `legalis-dev` für Backend und Doku
- `legalis-workflow` für Modellierung und Runtime-Tests

Sie bleiben dennoch nur **Arbeitskopien** desselben Core-Repositories.

---

## 8. Release- und Governance-Regeln

### 8.1 Core-Änderungen

Änderungen am Core-Repository unterliegen der Produkt- und Governance-Kontrolle.

Dazu zählen besonders:

- Änderungen an Standardprozessen
- Änderungen an erlaubten Modellierungskonventionen
- Änderungen an Workflow-Definitionen mit Produktstatus
- Änderungen an Core-APIs oder Kernobjekten

### 8.2 Standardprozesse

Offizielle Standardprozesse dürfen nur nach den jeweils gültigen BPMN-Governance-Regeln geändert werden.

### 8.3 Customer Extensions

Für kundenspezifische Extensions gilt:

- klare Kennzeichnung
- separate Versionierung
- separate Verantwortlichkeit
- keine automatische Haftungsübernahme durch den Legalis-Core

### 8.4 Rückführung in den Standard

Eine Rückführung von Kundenlogik in den Standard ist nur erlaubt, wenn sie produktstrategisch sinnvoll, rechtlich unkritisch und fachlich generalisierbar ist.

---

## 9. Dokumentationspflichten

Jedes Repository soll mindestens enthalten:

### 9.1 Core-Repository

- README
- Strukturhinweise
- Setup-Hinweise
- Governance-Dokumente
- gegebenenfalls Workflow- und Deploy-Readmes

### 9.2 Kunden-Repository

- knappe Projektbeschreibung
- Kompatibilität zum Core-Stand
- Installationshinweise
- besondere Abhängigkeiten
- Ansprechpartner oder Verantwortungsbereich

### 9.3 Setup Guide

Der Setup Guide muss künftig ausdrücklich dokumentieren:

- dass dasselbe Core-Repository auf mehreren Hosts geklont werden kann
- dass `legalis-dev` und `legalis-workflow` nur unterschiedliche Arbeitsrollen sind
- dass produktive Customer Extensions aus separaten privaten Repositories kommen
- dass Core und Kunden-Overlay vor Einsätzen synchronisiert werden müssen

---

## 10. Mindestregeln für `.gitignore`

Mindestens auszuschließen sind:

- lokale virtuelle Umgebungen
- Build-Artefakte
- temporäre Exportdateien
- lokale Testdaten
- Laufzeitordner von Containern
- Secret-Dateien
- Editor-spezifische lokale Artefakte, soweit nicht absichtlich versioniert

Beispiele:

```gitignore
.venv/
__pycache__/
*.pyc
.env
.env.*
*.log
.DS_Store
```

Weitere Regeln sind projektspezifisch zu ergänzen.

---

## 11. Verbindliche Kurzfassung

1. `natalnetwork/legalis` ist das zentrale Core-Repository.
2. `legalis-dev` und `legalis-workflow` sind nur unterschiedliche Arbeitskopien desselben Repositories.
3. Offizielle Standardprozesse liegen im Core.
4. Produktive kundenspezifische Extensions liegen **nicht** im Core.
5. Für jeden Kunden oder Piloten ist ein separates privates Repository zu verwenden.
6. Deployment erfolgt nach dem Prinzip **Core + Customer Overlay**.
7. Kundenspezifische Prozesse und Erweiterungen sind als potenzielle Betriebsgeheimnisse zu behandeln.
8. Vor jedem Einsatz müssen Core und gegebenenfalls Kunden-Overlay synchronisiert werden.

---

## 12. Status dieser Policy

**Version:** v1  
**Status:** Arbeitsfassung / verbindliche Richtlinie für die aktuelle Aufbauphase  
**Nächste sinnvolle Erweiterungen:**

- genauere Branching-Regeln
- Release-Tagging für Workflow-Versionen
- Kompatibilitätsmatrix Core ↔ Customer-Overlay
- Import-/Export-Regeln für Standard- und Extension-Modelle
- formalisierte Schulungs- und Freigabestufen
