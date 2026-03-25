# Legalis BPMN-Modellierungshandbuch v1.1

Status: Arbeitsversion / V1.1  
Geltungsbereich: Standardprozesse und kundenspezifische Erweiterungen im Legalis-Kontext  
Zielgruppe: BPMN-Einsteiger, Consultants, Implementierer, interne Produkt- und Prozessverantwortliche

---

## 1. Zweck dieses Dokuments

Dieses Handbuch definiert die verbindlichen Modellierungskonventionen für BPMN in Legalis.

Es verfolgt sechs Ziele:

1. Schulungsmaterial für Einsteiger bereitstellen.
2. Die erlaubte Menge an BPMN-Elementen für Legalis v1 eindeutig festlegen.
3. Standardprozesse von kundenspezifischen Erweiterungen strikt trennen.
4. Eine belastbare Grundlage für spätere technische Workflow-Ausführung schaffen.
5. Einen einheitlichen Werkzeugstandard für Consultants und interne Mitarbeiter festlegen.
6. Die Prozessgranularität so definieren, dass keine fachlich überladenen Riesendiagramme entstehen.

Dieses Dokument ist bewusst konservativ. Es priorisiert Lesbarkeit, Governance, Schulbarkeit, Betriebsstabilität und geringe Fehlerrisiken vor maximaler BPMN-Freiheit.

---

## 2. Grundprinzipien

### 2.1 Wenige Elemente, hohe Disziplin

Legalis verwendet in v1 absichtlich nur einen reduzierten BPMN-Kern. Weniger erlaubte Elemente bedeuten:

- schnellere Schulung
- weniger Modellierungsfehler
- bessere Lesbarkeit
- leichtere Review- und Freigabeprozesse
- geringeres Haftungs- und Wartungsrisiko

### 2.2 Fachmodell vor Implementierungsdetail

Ein BPMN-Modell beschreibt in Legalis zuerst den fachlichen Ablauf.

Das Modell soll beantworten:

- Was löst den Ablauf aus?
- Welche Schritte führt ein Mensch aus?
- Welche Schritte führt das System automatisch aus?
- Wo gibt es Entscheidungen?
- Wann endet der Ablauf?

Das Modell soll zunächst **nicht** beantworten:

- welche Datenbanktabelle verwendet wird
- welcher API-Endpoint aufgerufen wird
- welches konkrete Skript im Hintergrund läuft
- wie eine interne Engine technisch implementiert ist

### 2.3 Standard vor Custom

Legalis unterscheidet strikt zwischen:

- **Standardprozess**: offizieller, von Legalis verantworteter Referenzprozess
- **Custom Extension**: kundenspezifische Erweiterung oder Abweichung

Ein Prozess darf niemals „halb Standard, halb Kunde“ sein. Die Herkunft muss klar sein.

### 2.4 Klarheit vor Vollständigkeit

Ein einfaches, eindeutiges Modell ist besser als ein formal vollständiges, aber schwer lesbares BPMN-Diagramm.

### 2.5 Ein Prozess = genau ein Fall = genau ein Durchlauf

Jedes BPMN-Prozessmodell beschreibt in Legalis **genau einen fachlichen Durchlauf einer Instanz**.

Das bedeutet:

- Ein Modell beschreibt einen Fall von Anfang bis Ende.
- Ein Modell beschreibt **nicht** die gesamte Welt eines Fachbereichs.
- Ein Modell beschreibt **nicht** alle denkbaren Fallarten gleichzeitig.
- Ein Modell beschreibt **nicht** eine Sammelstelle wie „gesamter Posteingang des Unternehmens“ mit allen Varianten in einem Riesendiagramm.

Beispiel:

**Falsch gedacht:**
- „Posteingang bearbeiten“ als riesiger Sammelprozess, in dem anschließend über Gateways alle nur denkbaren Dokumentarten, Mandatsarten, Fristen, Zuständigkeiten und Sonderfälle verteilt werden.

**Richtig gedacht:**
- Ein konkreter Prozess für einen dokumentierten Durchlauf, zum Beispiel:
  - „Eingehende Vollmacht prüfen“
  - „Klageeingang registrieren“
  - „Frist aus gerichtlichem Schreiben erfassen“

Wenn mehrere Fallarten fachlich unterschiedlich sind, werden **mehrere kleine Prozesse** modelliert statt eines gigantischen Universalprozesses.

### 2.6 Schulbarkeit vor individueller Modellierfreiheit

Die Modellierungskonventionen sind ausdrücklich auch für Schulung und Auswahl geeignet.

Das Handbuch soll so klar sein, dass auch Teilnehmer mit heterogenem fachlichen und technischen Hintergrund damit arbeiten können. Deshalb werden Konventionen lieber präzise und eng formuliert als großzügig und interpretationsoffen.

---

## 3. Werkzeugstandard und Arbeitsumgebung

### 3.1 VS Code ist das Standardwerkzeug

Für Legalis ist **Visual Studio Code (VS Code)** das verbindliche Standardwerkzeug für die BPMN-Modellierung.

Das ist nicht primär eine technische Notwendigkeit, sondern eine betriebliche Entscheidung.

### 3.2 Warum VS Code als Standard gesetzt wird

VS Code reduziert im Consulting-Betrieb Komplexität und Supportaufwand.

Praktische Gründe:

- Consultants haben mit einem Werkzeug direkt die gesamte Grundausstattung in der Hand.
- BPMN-Modelle können eingesehen und bearbeitet werden.
- Das aktuelle GitHub-Repository kann lokal geklont und synchronisiert werden.
- Python-basierte kundenspezifische Erweiterungen können je nach Qualifikation direkt im selben Werkzeugumfeld bearbeitet oder installiert werden.
- Linux und Windows werden gleichermaßen gut unterstützt.
- Die Installations- und Bedienfehlerquote sinkt.
- Vor Kundenbesuchen kann einfacher sichergestellt werden, dass sowohl die aktuelle Software-Revision als auch die dazu passenden Standardmodelle bereits lokal synchronisiert wurden.

### 3.3 Keine Werkzeugvielfalt im Feldbetrieb

Standalone-BPMN-Werkzeuge sind in Legalis **nicht** der Standard im Consulting-Betrieb.

Sie sind nicht grundsätzlich verboten, aber:

- sie erhöhen die Vielfalt der Installationswege
- sie erschweren Hotline und Support
- sie erhöhen die Wahrscheinlichkeit von Versions- und Bedienfehlern
- sie trennen BPMN-Modellierung unnötig vom übrigen Projekt- und Customizing-Workflow

Für Schulung, Feldbetrieb und Support gilt deshalb:

- **Modellierung in VS Code**
- **Versionsverwaltung per Git**
- **Repository-Synchronisation vor Kundenterminen verpflichtend**

### 3.4 Mindestarbeitsplatz eines Consultants

Ein einsatzfähiger Consultant-Arbeitsplatz soll mindestens enthalten:

- VS Code
- Open-BPMN-Extension
- Git
- aktuelle lokale Kopie des freigegebenen Repositories
- definierte Java-Laufzeit für den Modellierer
- optional Python-Umgebung für Custom-Erweiterungen

### 3.5 Schulungsdidaktik und Werkzeugdisziplin

Die Schulung muss davon ausgehen, dass das Qualifikationsniveau im Bewerber- und Teilnehmerfeld stark variiert.

Daraus folgen drei Konsequenzen:

1. Die Modellierungskonventionen müssen einfach, reproduzierbar und eng geführt sein.
2. Das Werkzeugset darf nicht unnötig fragmentiert werden.
3. Das Schulungsmaterial muss didaktisch Schritt für Schritt aufgebaut sein.

---

## 4. Geltungsbereich und Ebenen

### 4.1 Drei Modellierungsstufen

#### Stufe A – Schulungs- und Fachmodelle
Für Schulung, Analyse, Abstimmung mit Fachanwendern.

Merkmale:
- sehr wenige Elemente
- hohe Lesbarkeit
- kaum technische Details

#### Stufe B – Ausführungsnahe Fachmodelle
Für vorbereitete Workflow-Implementierung.

Merkmale:
- User Tasks und Service Tasks klar getrennt
- definierte Gateways
- dokumentierte Rollen
- kontrollierte Subprozesse

#### Stufe C – Erweiterte technische Modelle
Für spätere Ausbaustufen.

Merkmale:
- aktuell in v1 grundsätzlich nicht freigegeben
- nur mit gesonderter Governance

Für Legalis v1 arbeiten wir primär auf **Stufe A** und **Stufe B**.

---

## 5. Erlaubte BPMN-Elemente in v1

Die folgenden Typen sind in Legalis v1 zulässig.

### 5.1 Start Event

**Zweck:** Markiert den Beginn eines Prozesses.

**Regel:**
- Jeder Prozess hat genau ein Start Event.
- Wenn mehrere fachlich unterschiedliche Auslöser existieren, sind in der Regel mehrere Prozesse zu modellieren statt eines überladenen Sammelprozesses.
- Das Start Event erhält eine kurze fachliche Bezeichnung.

**Benennung:**
- „Anfrage eingegangen"
- „Frist ausgelöst"
- „Dokumenteingang registriert"

**Nicht verwenden für:**
- technische Trigger-Details
- kryptische Eventnamen

### 5.2 End Event

**Zweck:** Markiert das Ende eines Prozesses oder Prozesspfades.

**Regel:**
- Jeder Prozess hat mindestens ein End Event.
- Mehrere End Events sind erlaubt, wenn unterschiedliche fachliche Ergebnisse klar benannt werden.

**Benennung:**
- „Mandat eröffnet"
- „Mandat abgelehnt"
- „Prüfung abgeschlossen"

### 5.3 Task

**Zweck:** Allgemeine Aktivität ohne nähere Festlegung.

**Regel:**
- In Legalis v1 soll eine generische Task nur sparsam verwendet werden.
- Bevorzugt werden User Task oder Service Task.
- Eine einfache Task ist nur zulässig, wenn die Automatisierungsverantwortung noch ungeklärt ist.

**Empfehlung:**
Für Schulungsmodelle tolerierbar, für belastbare Standardmodelle möglichst vermeiden.

### 5.4 User Task

**Zweck:** Eine Aktivität, die von einem Menschen im System ausgeführt, bestätigt oder abgeschlossen wird.

**Typische Legalis-Beispiele:**
- Lead erfassen
- Konfliktprüfung durchführen
- Mandat anlegen
- Frist prüfen
- Dokument freigeben

**Regel:**
- Immer verwenden, wenn ein Mensch die Verantwortung trägt.
- Standardtyp für die Mehrzahl der fachlichen Schritte.

**Benennungsmuster:**
Verb im Infinitiv + Objekt.

Beispiele:
- „Lead erfassen"
- „Mandat anlegen"
- „Dokument freigeben"

### 5.5 Service Task

**Zweck:** Vollautomatischer Systemschritt.

**Typische Legalis-Beispiele:**
- Eingangsbestätigung senden
- PDF generieren
- Deadline berechnen
- Dokument referenzieren
- Status synchronisieren

**Regel:**
- Nur verwenden, wenn kein Mensch den Schritt fachlich ausführt.
- Nicht verwenden, wenn der Schritt in Wahrheit noch manuell überprüft oder angestoßen werden muss.

**Benennungsmuster:**
Automatische Systemaktion in klarer Fachsprache.

Beispiele:
- „PDF erzeugen"
- „Frist berechnen"
- „Benachrichtigung senden"

### 5.6 Exclusive Gateway (XOR)

**Zweck:** Genau ein Pfad wird gewählt.

**Typische Legalis-Beispiele:**
- Konflikt vorhanden?
- Vollmacht vollständig?
- Zahlung eingegangen?

**Regel:**
- Standard-Gateway für Ja/Nein- oder Entweder/Oder-Entscheidungen.
- Ausgehende Pfade müssen klar benannt sein.
- Wenn sinnvoll, mit expliziten Labels wie „Ja" / „Nein" arbeiten.

### 5.7 Parallel Gateway (AND)

**Zweck:** Mehrere Pfade laufen parallel.

**Typische Legalis-Beispiele:**
- Mandat anlegen und Bestätigung senden
- Akte erzeugen und Team informieren

**Regel:**
- Nur verwenden, wenn echte Parallelität fachlich gewollt ist.
- Nicht einsetzen, nur um Diagramme optisch zu verteilen.
- Wenn ein Parallel Gateway öffnet, muss die spätere Zusammenführung fachlich nachvollziehbar sein.

### 5.8 Sequence Flow

**Zweck:** Verbindet die Schritte im fachlichen Ablauf.

**Regel:**
- Sequence Flows bilden den Standardfluss innerhalb eines Prozesses.
- Pfeilrichtungen sollen grundsätzlich von links nach rechts verlaufen.
- Rücksprünge vermeiden; wenn nötig, nur mit klarer Begründung.

### 5.9 Subprocess (kontrolliert)

**Zweck:** Kapselt einen zusammengehörenden Teilablauf.

**Regel:**
- Nur verwenden, wenn ein Ablauf logisch gruppierbar ist und als eigener Baustein Sinn ergibt.
- Keine tiefen Schachtelungen.
- In v1 nur ein bis zwei Ebenen, nicht mehr.

**Geeignete Beispiele:**
- „Konfliktprüfung"
- „Mandanten-Onboarding"
- „Dokumentenerzeugung"

### 5.10 Data Object / Dokumentreferenz

**Zweck:** Zeigt an, dass ein Dokument oder Datenobjekt fachlich eine Rolle spielt.

**Regel:**
- Optional.
- Nur verwenden, wenn das Verständnis des Prozesses dadurch besser wird.
- Nicht jedes Feld und nicht jedes Objekt modellieren.

**Geeignete Beispiele:**
- Vollmacht
- Vertragsentwurf
- Identitätsdokument
- Exportdatei

### 5.11 Lane / Role

**Zweck:** Ordnet Aktivitäten einer Rolle oder Funktion zu.

**Regel:**
- Lanes beschreiben Rollen, nicht Personennamen.
- Eine Lane steht für Verantwortungsträger oder Systemrolle.
- Für kleine Modelle maximal so viele Lanes wie fachlich nötig.

**Geeignete Lane-Namen:**
- Sekretariat
- Sachbearbeitung
- Anwalt
- Partner
- System

**Nicht geeignet:**
- „Mychelle"
- „Sebastian"
- „Notebook 1"

---

## 6. Vorläufig nicht erlaubte BPMN-Elemente

Die folgenden Typen sind in Legalis v1 im Standardmodell nicht freigegeben:

- Event-based Gateway
- Inclusive Gateway
- Complex Gateway
- Boundary Events in breiter Nutzung
- Ad-hoc Subprocess
- Choreography
- Conversation
- freie Eskalations- und Kompensationsmuster
- freie Timer-Modellierung durch Fachanwender
- Script Task
- Business Rule Task als Standardtyp

### 6.1 Warum Business Rule Task vorerst nicht?

Obwohl BPMN diesen Typ kennt, ist er in Legalis v1 nicht sinnvoll als Standardinstrument.

Grund:
- Er suggeriert bereits eine formalisierte Regel-Engine.
- Für die frühe Fachmodellierung reicht XOR + dokumentierte Entscheidungslogik.
- Die fachliche Regel kann zunächst textlich dokumentiert werden.

Wenn später echte Decision-Services eingeführt werden, kann dieser Typ kontrolliert freigegeben werden.

---

## 7. Erlaubte Verknüpfungen

### 7.1 Allgemeine Regeln

Zulässig sind in v1 im Kern:
- Start Event → Task / User Task / Service Task / Subprocess
- Task / User Task / Service Task / Subprocess → Task / Gateway / End Event
- Exclusive Gateway → Task / End Event / Subprocess
- Parallel Gateway → Task / Subprocess
- Data Object ↔ Activity als rein fachliche Referenz

### 7.2 Nicht zulässige oder unerwünschte Muster

- Start Event direkt auf End Event ohne fachlichen Schritt
- Gateway auf Gateway ohne verständliche Begründung
- mehrere ungeklärte Kreuzungen von Sequence Flows
- Rücksprung-Schleifen ohne explizite Modellierungsentscheidung
- Mischformen aus manueller und automatischer Aktivität in einem einzigen Task
- Verzweigungen, die nur deshalb entstehen, weil mehrere Fallarten künstlich in einen einzigen Universalprozess gepresst wurden

### 7.3 Bevorzugte Flussrichtung

Modelle werden nach Möglichkeit **von links nach rechts** aufgebaut.  
Vertikale oder rückläufige Flüsse sind nur in Ausnahmefällen zulässig.

---

## 8. Attribute und Pflichtangaben

Jedes Modell soll mindestens die folgenden Informationen tragen.

### 8.1 Prozessebene

Pflichtangaben:
- Prozessname
- Prozess-ID
- Modellversion
- Status
- Herkunftsebene: Standard oder Custom
- Autor oder verantwortliche Stelle
- letztes Änderungsdatum
- Referenz auf Basisprozess, falls es sich um ein Custom-Modell handelt

Empfohlene Statuswerte:
- draft
- review
- approved
- deprecated

### 8.2 Aktivitätsebene

Jede Activity soll mindestens enthalten:
- klare fachliche Bezeichnung
- eindeutiger Typ
- verantwortliche Rolle über Lane oder Metadaten

Optional sinnvoll:
- Kurzbeschreibung
- Eingangsobjekte
- Ausgangsobjekte
- fachliche Vorbedingungen

### 8.3 Gateway-Ebene

Pflicht:
- fachlich verständliche Frage oder Entscheidungslogik
- klar benannte ausgehende Pfade

Beispiel:
- Gateway: „Konflikt vorhanden?"
- Pfade: „Ja" / „Nein"

---

## 9. Benennungskonventionen

### 9.1 Prozessnamen

Format:
`<Domäne> – <fachlicher Ablauf> – v<Version>`

Beispiele:
- `Intake – Lead zu Mandat – v1`
- `Prazo – Fristerfassung – v1`

### 9.2 Dateinamen

Empfohlen:
`<bereich>-<prozessname>-v<nummer>.bpmn`

Beispiele:
- `intake-lead-zu-mandat-v1.bpmn`
- `prazo-fristerfassung-v1.bpmn`

### 9.3 Aktivitätsnamen

Format:
`Verb + Objekt`

Gut:
- „Lead erfassen"
- „Mandat anlegen"
- „Frist berechnen"

Schlecht:
- „Lead"
- „Bearbeitung"
- „Sache prüfen vielleicht"

### 9.4 Gateway-Benennung

Format als Frage.

Gut:
- „Konflikt vorhanden?"
- „Dokument vollständig?"

Schlecht:
- „Prüfung"
- „Entscheidung"

### 9.5 End Events

Das End Event soll das Ergebnis ausdrücken.

Gut:
- „Mandat eröffnet"
- „Mandat abgelehnt"
- „Dokument generiert"

---

## 10. Modellierungsregeln für Einsteiger

1. Jeder Prozess beschreibt genau einen fachlichen Durchlauf.
2. Jeder Prozess beginnt mit genau einem Start Event.
3. Jeder Prozess endet mit mindestens einem End Event.
4. Menschliche Arbeit wird als User Task modelliert.
5. Vollautomatische Arbeit wird als Service Task modelliert.
6. Entscheidungen werden als Exclusive Gateway modelliert.
7. Parallele Pfade nur verwenden, wenn echte Parallelität besteht.
8. Rollen über Lanes ausdrücken, nicht über Personennamen.
9. Keine unnötigen BPMN-Spezialelemente verwenden.
10. Lieber ein zweites kleines Modell als ein überladenes Riesendiagramm.
11. Das Modell muss für einen geschulten Einsteiger in wenigen Minuten lesbar sein.
12. Wenn eine Fallart fachlich anders beginnt oder anders endet, ist oft ein separates Modell besser als ein neuer großer Gateway-Block.

---

## 11. Standardprozess vs. Custom Extension

### 11.1 Standardprozess

Merkmale:
- von Legalis definiert
- von Legalis gepflegt
- Teil des offiziellen Produktstandards
- besonders strenge Freigabe

Ablageempfehlung:
`models/standard/`

### 11.2 Custom Extension

Merkmale:
- kundenspezifische Abweichung oder Ergänzung
- getrennte Verantwortung
- getrennte Versionierung
- klare Kennzeichnung als nicht-offizieller Standard

Ablageempfehlung:
`models/extensions/<kunde-oder-pilot>/`

### 11.3 Vererbungsregel in der Praxis

Ein Custom-Modell darf sich fachlich auf einen Standardprozess beziehen, aber nicht dessen Governance verschleiern.

Daher soll jedes Custom-Modell kenntlich machen:
- von welchem Standardprozess es ausgeht
- was ergänzt, entfernt oder geändert wurde
- wer die Verantwortung trägt

---

## 12. Review-Checkliste

Vor Freigabe eines Modells prüfen:

### Fachlich
- Ist der Auslöser klar?
- Beschreibt das Modell genau einen Durchlauf?
- Sind alle Schritte fachlich verständlich?
- Sind Entscheidungen klar formuliert?
- Ist das Ergebnis eindeutig?

### Formal
- Nur erlaubte Elemente verwendet?
- Genau ein Start Event vorhanden?
- Rollen korrekt über Lanes modelliert?
- Flussrichtung konsistent?
- Keine unnötigen Kreuzungen?

### Granularität
- Wurde versehentlich ein Sammelprozess statt eines Einzelfalls modelliert?
- Enthält das Modell zu viele Fallarten in einem Diagramm?
- Wäre eine Aufteilung in mehrere kleine Prozesse fachlich sauberer?

### Governance
- Standard oder Custom korrekt gekennzeichnet?
- Version vorhanden?
- Verantwortlichkeit dokumentiert?
- Dateiname und Prozessname konsistent?
- Basisprozess bei Custom-Modellen genannt?

### Betrieb
- Wurde das Modell im Standardwerkzeug VS Code erstellt oder geprüft?
- Ist das lokale Repository vor dem Einsatz synchronisiert?

---

## 13. Minimalbeispiel für Legalis

### Prozess: Lead zu Mandat

**Lanes:**
- Sekretariat
- Anwalt
- System

**Ablauf:**
1. Start Event: „Anfrage eingegangen"
2. User Task: „Lead erfassen"
3. User Task: „Konfliktprüfung durchführen"
4. Exclusive Gateway: „Konflikt vorhanden?"
5. Pfad Ja → End Event: „Mandat abgelehnt"
6. Pfad Nein → User Task: „Mandat anlegen"
7. Service Task: „Aktennummer erzeugen"
8. User Task: „Erste Frist erfassen"
9. End Event: „Mandat eröffnet"

### Warum dieses Beispiel gut ist

Es zeigt bereits den Kern der Legalis-Modellierung:
- klarer Start
- menschliche Schritte
- eine fachliche Entscheidung
- ein automatischer Systemschritt
- zwei klare Enden
- genau ein fachlicher Durchlauf

---

## 14. V1-Entscheidungen, die bewusst offen bleiben

Diese Punkte sind nicht ungeklärt, sondern absichtlich auf später verschoben:

- Timer Events als Standardwerkzeug
- Business Rule Tasks
- Nachrichtenflüsse zwischen Pools
- komplexe Eskalationsmuster
- tief verschachtelte Subprozesse
- formale DMN-Kopplung

Diese Themen können in einer späteren Version kontrolliert ergänzt werden.

---

## 15. V2-Ausbau des Schulungsmaterials

Die Version 2 dieser Anleitung soll das Handbuch zu einem deutlich stärkeren Lehr- und Schulungsmedium ausbauen.

Geplante Ergänzungen:

- zahlreiche bebilderte BPMN-Beispiele
- Positiv- und Negativbeispiele pro Elementtyp
- grafische Gegenüberstellung von guten und schlechten Modellen
- Schritt-für-Schritt-Anleitungen wie in einem klassischen Lehrbuch
- Beispielprozesse in steigender Schwierigkeit
- gesonderte Kapitel für Review, typische Fehler und Modellzerlegung

Ziel ist ausdrücklich ein didaktisch starkes Dokument im Stil eines bebilderten Schulungs- und Lehrbuchs.

---

## 16. Repository-Empfehlung

Empfohlene Ablage:

```text
repo/
├── docs/
│   └── bpmn/
│       ├── Legalis_BPMN_Modellierungshandbuch_v1_1.md
│       └── beispiele/
├── models/
│   ├── standard/
│   └── extensions/
│       └── pilot-mychelle/
```

Optional später zusätzlich:

- `docs/bpmn/review-checkliste.md`
- `docs/bpmn/freigabeprozess.md`
- `docs/bpmn/beispielmodelle/`
- `docs/bpmn/bilder/`

---

## 17. Schlussfestlegung für v1.1

Für Legalis v1.1 gelten damit die folgenden praktischen Kernregeln:

- Verwende primär **Start Event, End Event, User Task, Service Task, Exclusive Gateway, Parallel Gateway, Sequence Flow, kontrollierte Subprozesse, Data Objects, Lanes**.
- Verwende **User Task** als Standardtyp für menschliche Arbeit.
- Verwende **Service Task** nur für echte Automatik.
- Verwende **Exclusive Gateway** als Standardentscheidung.
- Verwende **Business Rule Task** in v1 nicht als Standardtyp.
- Verwende **VS Code** als verbindliches Standardwerkzeug im Consulting-Betrieb.
- Synchronisiere vor Kundeneinsatz Software-Revision und Repository-Stand.
- Trenne **Standard** und **Custom** strikt.
- Modelle so, dass sie ein geschulter BPMN-Einsteiger lesen und reviewen kann.
- Modelle immer so, dass **genau ein fachlicher Durchlauf** beschrieben wird.

Damit ist eine belastbare V1.1-Modellierungskonvention für Legalis definiert.
