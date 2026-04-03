# Legalis BPMN-Modellierungshandbuch v1.2

Status: Arbeitsversion / V1.2  
Geltungsbereich: Offizielle Legalis-Standardprozesse und deren modellnahe Schulung  
Zielgruppe: BPMN-Einsteiger, Consultants, Implementierer, interne Produkt- und Prozessverantwortliche

---

## 1. Zweck dieses Dokuments

Dieses Handbuch definiert die verbindlichen Modellierungskonventionen für BPMN in Legalis.

Es verfolgt sechs Ziele:

1. ein einheitliches Schulungs- und Review-Niveau herstellen,
2. die für Legalis v1 erlaubte BPMN-Untermenge verbindlich festlegen,
3. die Modellierung auf die dokumentierte Arbeitsweise von Imixs ausrichten,
4. Standardprozesse eng, lesbar und wartbar halten,
5. die Fehlerquote im Consulting-Betrieb senken,
6. die spätere technische Ausführung vorbereiten, ohne das Modell mit unnötiger BPMN-Komplexität zu überladen.

Dieses Dokument ist bewusst konservativ. Es priorisiert Lesbarkeit, Governance, Schulbarkeit, Betriebsstabilität und geringe Fehlerrisiken vor maximaler BPMN-Freiheit.

---

## 2. Grundprinzipien

### 2.1 Wenige Elemente, hohe Disziplin

Legalis verwendet in v1.2 absichtlich nur einen reduzierten BPMN-Kern. Weniger erlaubte Elemente bedeuten:

- schnellere Schulung,
- weniger Modellierungsfehler,
- bessere Lesbarkeit,
- leichtere Review- und Freigabeprozesse,
- geringeres Haftungs- und Wartungsrisiko.

### 2.2 Ein offizielles Profil für Standardprozesse

Für offizielle Legalis-Standardprozesse gilt **ein einziges verbindliches BPMN-Profil**.

Wir trennen in v1.2 **nicht** zwischen einem allgemeinen Fachprofil und einem technischen Ausführungsprofil. Der Grund ist didaktisch: zwei Profile würden Schulung, Review und Hotline unnötig verkomplizieren.

Das offizielle Profil orientiert sich daher direkt an der dokumentierten Imixs-Arbeitsweise:

- ein Prozesszustand wird als **Task** modelliert,
- ein Zustandsübergang wird als **Intermediate Catch Event** modelliert,
- alternative Events an einem Task werden mit einem **Event Gateway** modelliert,
- Verantwortlichkeiten werden mit **Lanes** gegliedert.

### 2.3 Ein Prozess = genau ein Fall = genau ein Durchlauf

Jedes BPMN-Prozessmodell beschreibt in Legalis **genau einen fachlichen Durchlauf einer Instanz**.

Das bedeutet:

- Ein Modell beschreibt einen Fall von Anfang bis Ende.
- Ein Modell beschreibt **nicht** die gesamte Welt eines Fachbereichs.
- Ein Modell beschreibt **nicht** alle denkbaren Fallarten gleichzeitig.
- Ein Modell beschreibt **nicht** eine Sammelstelle wie „gesamter Posteingang des Unternehmens“ mit allen Varianten in einem Riesendiagramm.

Wenn mehrere Fallarten fachlich unterschiedlich sind, werden **mehrere kleine Prozesse** modelliert statt eines gigantischen Universalprozesses.

### 2.4 Modellierung für Menschen, nicht für XML

Ein Legalis-BPMN-Modell muss von Fachanwendern, Consultants und Reviewern lesbar sein. Deshalb gelten folgende Prioritäten:

1. eindeutiger fachlicher Ablauf,
2. klare Zuständigkeiten,
3. saubere technische Mindestattribute,
4. erst danach zusätzliche Engine- oder Automationsdetails.

### 2.5 Standard vor Custom

Legalis unterscheidet strikt zwischen:

- **Standardprozess**: offizieller, von Legalis verantworteter Referenzprozess,
- **Custom Extension**: kundenspezifische Erweiterung oder Abweichung.

Ein Prozess darf niemals „halb Standard, halb Kunde“ sein.

### 2.6 Schulbarkeit vor individueller Modellierfreiheit

Die Modellierungskonventionen sind ausdrücklich auch für Schulung und Auswahl geeignet. Das Handbuch muss so klar sein, dass auch Teilnehmer mit heterogenem fachlichen und technischen Hintergrund reproduzierbar modellieren können.

---

## 3. Werkzeugstandard und Arbeitsumgebung

### 3.1 VS Code ist das Standardwerkzeug

Für Legalis ist **Visual Studio Code (VS Code)** das verbindliche Standardwerkzeug für die BPMN-Modellierung.

### 3.2 Warum VS Code als Standard gesetzt wird

VS Code reduziert im Consulting-Betrieb Komplexität und Supportaufwand.

Praktische Gründe:

- BPMN-Modelle können grafisch eingesehen und bearbeitet werden.
- Das Git-Repository kann im selben Werkzeug geklont, synchronisiert und versioniert werden.
- Python-basierte Erweiterungen können im selben Werkzeugumfeld bearbeitet werden.
- Linux und Windows werden gleichermaßen gut unterstützt.
- Vor Kundenbesuchen kann einfacher sichergestellt werden, dass Softwarestand und Modellstand synchron sind.

### 3.3 Technische Mindestbasis

Ein einsatzfähiger Arbeitsplatz für die BPMN-Modellierung enthält mindestens:

- VS Code,
- Open-BPMN-Extension,
- Java 17 oder höher,
- Git,
- aktuelle lokale oder Remote-Arbeitskopie des freigegebenen Repositories.

---

## 4. Offizielles Legalis-v1.2-Profil

### 4.1 Erlaubte BPMN-Elemente

In offiziellen Legalis-Standardprozessen sind in v1.2 genau diese Elemente erlaubt:

1. **Start Event**  
2. **End Event**  
3. **Task**  
4. **Intermediate Catch Event**  
5. **Event Gateway**  
6. **Exclusive Gateway** nur kontrolliert für regelbasierte Verzweigungen  
7. **Sequence Flow**  
8. **Lane**

### 4.2 Nicht freigegebene Elemente in v1.2

Die folgenden Elemente sind in offiziellen Legalis-Standardprozessen **nicht** freigegeben:

- Pool,
- User Task,
- Service Task,
- Business Rule Task,
- Inclusive Gateway,
- Complex Gateway,
- Boundary Events,
- Timer Events,
- Message Flows,
- Data Objects,
- Choreography- oder Conversation-Elemente.

### 4.3 Warum Pools in v1.2 nicht erlaubt sind

Pools sind in BPMN und Imixs grundsätzlich möglich, werden in Legalis v1.2 aber **nicht** verwendet.

Begründung:

- Die Schulungslast wäre höher.
- Die Fehlerrate bei Einsteigern würde steigen.
- Für die ersten Legalis-Standardprozesse reichen Lanes zur Darstellung von Zuständigkeiten aus.
- Externe Beteiligte dürfen in v1.2 bei Bedarf als eigene **Lane** dargestellt werden, solange damit nur Verantwortungszonen und Übergabepunkte beschrieben werden.

### 4.4 Warum User Task und Service Task in v1.2 nicht erlaubt sind

Für die offizielle Legalis-v1.2-Untermenge verwenden wir bewusst nur das generische **Task**-Element.

Begründung:

- Die dokumentierte Imixs-Erweiterung wird auf **Task** und **Catch Event** angewendet.
- Ein zusätzlicher Typenmix aus Task, User Task und Service Task würde Schulung und Review unnötig erschweren.
- Die Rolle einer Aufgabe wird in v1.2 primär durch **Lane**, Namen, Dokumentation und spätere Actor-/ACL-Konfiguration vermittelt.

---

## 5. Semantik der erlaubten Elemente

### 5.1 Start Event

**Zweck:** Markiert den Beginn eines Prozesses.

**Regeln:**

- Jeder Prozess hat genau ein Start Event.
- Wenn mehrere fachlich unterschiedliche Auslöser existieren, sind in der Regel mehrere Prozesse zu modellieren.
- Das Start Event erhält eine kurze fachliche Bezeichnung.

**Beispiele:**

- „Anfrage eingegangen"
- „Klageeingang registriert"
- „Fristdokument eingegangen"

### 5.2 End Event

**Zweck:** Markiert das Ende eines Prozesses oder Prozesspfades.

**Regeln:**

- Jeder Prozess hat mindestens ein End Event.
- Mehrere End Events sind erlaubt, wenn unterschiedliche fachliche Ergebnisse klar benannt werden.

### 5.3 Task

**Zweck:** Beschreibt in Legalis den **aktuellen Prozesszustand** bzw. den Status einer laufenden Instanz.

**Regeln:**

- Jeder engine-relevante Task wird mit der Imixs-Workflow-Erweiterung annotiert.
- Jeder Task benötigt eine eindeutige **Process ID**.
- Die Task-ID ist innerhalb des Modells eindeutig.
- Der Task-Name beschreibt einen stabilen Zustand, nicht bloß einen Klick.

**Gute Beispiele:**

- „Lead offen"
- „Konfliktprüfung offen"
- „Mandat aktiv"

**Schlechte Beispiele:**

- „Button klicken"
- „Maske öffnen"
- „Weiter"

### 5.4 Intermediate Catch Event

**Zweck:** Beschreibt in Legalis einen **Zustandsübergang** von einem Task in einen anderen.

**Regeln:**

- Jeder engine-relevante Übergang wird mit der Imixs-Workflow-Erweiterung annotiert.
- Jedes Event benötigt eine eindeutige **Event ID** innerhalb des zugehörigen Tasks.
- Event-Namen beschreiben eine erkennbare fachliche Aktion oder Entscheidung.

**Gute Beispiele:**

- „Lead erfasst"
- „Kein Konflikt"
- „Frist erfasst"

### 5.5 Event Gateway

**Zweck:** Modelliert alternative Workflow-Events, die von demselben Task ausgehen.

**Regeln:**

- Ein Event Gateway wird verwendet, wenn ein Task mehr als ein mögliches Workflow-Event hat.
- In Legalis v1.2 wird es mit **einer eingehenden** und **zwei oder mehr ausgehenden** Sequence Flows modelliert.
- Das Event Gateway ist der Standardfall für alternative Imixs-Events.

**Beispiel:**

- Task „Konfliktprüfung offen"
- Event Gateway „Ergebnis Konfliktprüfung?"
- ausgehend zu „Konflikt festgestellt“ und „Kein Konflikt“

### 5.6 Exclusive Gateway

**Zweck:** Modelliert eine regelbasierte Verzweigung, typischerweise nach einer Bedingungsprüfung.

**Regeln:**

- Exclusive Gateways sind in v1.2 **nur kontrolliert** erlaubt.
- Sie sind **nicht** das Standardmittel, um mehrere Workflow-Events eines Tasks darzustellen.
- Sie kommen nur dort zum Einsatz, wo eine explizite Regel oder Bedingung modelliert werden muss.

### 5.7 Lane

**Zweck:** Gliedert das Modell in Verantwortungszonen oder Rollen.

**Regeln:**

- Lanes sind in v1.2 das **einzige erlaubte Mittel**, um Zuständigkeiten visuell zu trennen.
- Eine Lane steht für eine Rolle, Funktion oder Verantwortungszone.
- Lanes sollen knapp und stabil benannt werden.

**Gute Beispiele:**

- „Kanzleiassistenz"
- „Anwalt / Sachbearbeitung"
- „Externe Buchhaltung"

---

## 6. Pflichtattribute für offizielle Standardprozesse

### 6.1 Modell-Ebene

Jedes offizielle Standardmodell benötigt:

- **Model Version**  
  Eindeutiger technischer Modellschlüssel.

**Beispiel:**
- `mandatsaufnahme-de-1.0.2`

### 6.2 Task-Ebene

Jeder Task benötigt mindestens:

- **Name**
- **Process ID**
- optional, aber empfohlen: **Documentation**

**Regeln:**

- Process IDs sind ganze Zahlen.
- Jede Process ID ist innerhalb des Modells eindeutig.
- Nummernblöcke sollen fachlich gegliedert sein.

### 6.3 Event-Ebene

Jedes Event benötigt mindestens:

- **Name**
- **Event ID**
- Sichtbarkeit bewusst gesetzt
- optional, aber empfohlen: **Documentation**

**Regeln:**

- Event IDs müssen nur innerhalb des zugehörigen Tasks eindeutig sein.
- Sichtbare Benutzeraktionen werden als öffentliche Events modelliert.
- Versteckte technische Folgeereignisse sind in v1.2 für Standardprozesse nicht vorgesehen.

---

## 7. Nummerierungskonventionen

Empfohlene Nummernblöcke für Legalis:

- **1000er** = Eingang / Intake
- **1100er** = Konfliktprüfung
- **1200er** = Mandatsanlage
- **1300er** = Fristen / Wiedervorlage
- **1400er** = aktiver Status
- **1900er** = Ablehnung / Abbruch

Event-IDs innerhalb eines Tasks:

- `10`, `20`, `30` …

---

## 8. Benennungskonventionen

### 8.1 Allgemein

- kurze, fachlich verständliche Namen,
- keine Abkürzungsorgien,
- keine technischen Implementierungsdetails im sichtbaren Elementnamen.

### 8.2 Task-Namen

Task-Namen beschreiben einen **Status**.

### 8.3 Event-Namen

Event-Namen beschreiben einen **Übergang**, eine Aktion oder ein Ergebnis.

### 8.4 Gateway-Namen

Gateway-Namen sollen eine Frage oder Entscheidung ausdrücken.

---

## 9. Modellierungsregeln für Reviews

Ein offizieller Legalis-Standardprozess ist nur dann freigabefähig, wenn:

1. genau ein fachlicher Durchlauf modelliert ist,
2. keine Pools verwendet wurden,
3. Zuständigkeiten ausschließlich mit Lanes dargestellt wurden,
4. alle engine-relevanten Zustände als Tasks modelliert wurden,
5. alle engine-relevanten Übergänge als Intermediate Catch Events modelliert wurden,
6. Event Gateways nur dort verwendet wurden, wo ein Task mehrere alternative Events hat,
7. Exclusive Gateways nur kontrolliert und begründet eingesetzt wurden,
8. Model Version, Process IDs und Event IDs sauber gepflegt sind,
9. keine losen, unverbundenen oder rein dekorativen Shapes vorhanden sind.

---

## 10. Beispielprozess v1.2

**Mandatsaufnahme – ein Durchlauf**

Lanes:

- Kanzleiassistenz
- Anwalt / Sachbearbeitung

Ablauf:

1. Anfrage eingegangen
2. Lead offen
3. Lead erfasst
4. Konfliktprüfung offen
5. Event Gateway: Ergebnis Konfliktprüfung?
6. Pfad A: Konflikt festgestellt → Mandat abgelehnt → Ende
7. Pfad B: Kein Konflikt → Mandat anlegen → Mandat angelegt → Erste Frist erfassen → Frist erfasst → Mandat aktiv → Ende

---

## 11. Ausblick auf spätere Versionen

Mögliche spätere Erweiterungen, aber **nicht** Bestandteil von v1.2:

- Pools,
- User Task / Service Task,
- Boundary Events,
- Timer Events,
- Message Flows,
- Split-Events mit Parallel Gateway,
- technische Folge- und Async-Events,
- umfangreiche Rule- und Mail-Konfiguration.
