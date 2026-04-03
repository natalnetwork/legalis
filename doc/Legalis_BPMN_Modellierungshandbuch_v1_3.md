# Legalis BPMN-Modellierungshandbuch v1.3

Status: Arbeitsversion / V1.3  
Geltungsbereich: Offizielle Legalis-Standardprozesse und deren Test in Imixs / Imixs-Forms  
Zielgruppe: BPMN-Einsteiger, Consultants, Implementierer, interne Produkt- und Prozessverantwortliche

---

## 1. Zweck dieses Dokuments

Dieses Handbuch definiert die verbindlichen Modellierungskonventionen für BPMN in Legalis.

Es verfolgt sieben Ziele:

1. ein einheitliches Schulungs- und Review-Niveau herstellen,
2. die für Legalis erlaubte BPMN-Untermenge verbindlich festlegen,
3. die Modellierung auf die dokumentierte Arbeitsweise von Imixs ausrichten,
4. Standardprozesse eng, lesbar und wartbar halten,
5. die Fehlerquote im Consulting-Betrieb senken,
6. die technische Ausführung vorbereiten,
7. die Testbarkeit in Imixs-Forms sicherstellen.

Dieses Dokument ist bewusst konservativ. Es priorisiert Lesbarkeit, Governance, Schulbarkeit, Betriebsstabilität und geringe Fehlerrisiken vor maximaler BPMN-Freiheit.

---

## 2. Grundprinzipien

### 2.1 Wenige Elemente, hohe Disziplin

Legalis verwendet absichtlich nur einen reduzierten BPMN-Kern. Weniger erlaubte Elemente bedeuten:

- schnellere Schulung,
- weniger Modellierungsfehler,
- bessere Lesbarkeit,
- leichtere Review- und Freigabeprozesse,
- geringeres Haftungs- und Wartungsrisiko.

### 2.2 Ein offizielles Profil für Standardprozesse

Für offizielle Legalis-Standardprozesse gilt **ein einziges verbindliches BPMN-Profil**.

Das offizielle Profil orientiert sich direkt an der dokumentierten Imixs-Arbeitsweise:

- ein Prozesszustand wird als **Task** modelliert,
- ein Zustandsübergang wird als **Intermediate Catch Event** modelliert,
- alternative Events an einem Task werden mit einem **Event Gateway** modelliert,
- Formulare werden als **Data Object `Form`** modelliert und per **Association** an einen Task gebunden.

### 2.3 Ein Prozess = genau ein Fall = genau ein Durchlauf

Jedes BPMN-Prozessmodell beschreibt in Legalis **genau einen fachlichen Durchlauf einer Instanz**.

Das bedeutet:

- Ein Modell beschreibt einen Fall von Anfang bis Ende.
- Ein Modell beschreibt **nicht** die gesamte Welt eines Fachbereichs.
- Ein Modell beschreibt **nicht** alle denkbaren Fallarten gleichzeitig.
- Ein Modell beschreibt **nicht** eine Sammelstelle wie „gesamter Posteingang“ mit allen Varianten in einem Riesendiagramm.

Wenn mehrere Fallarten fachlich unterschiedlich sind, werden **mehrere kleine Prozesse** modelliert statt eines gigantischen Universalprozesses.

### 2.4 Modellierung für Menschen, nicht für XML

Ein Legalis-BPMN-Modell muss von Fachanwendern, Consultants und Reviewern lesbar sein. Deshalb gelten folgende Prioritäten:

1. eindeutiger fachlicher Ablauf,
2. klare Zuständigkeiten,
3. saubere technische Mindestattribute,
4. testbare Formulare,
5. erst danach zusätzliche Engine- oder Automationsdetails.

### 2.5 Standard vor Custom

Legalis unterscheidet strikt zwischen:

- **Standardprozess**: offizieller, von Legalis verantworteter Referenzprozess,
- **Custom Extension**: kundenspezifische Erweiterung oder Abweichung.

Ein Prozess darf niemals „halb Standard, halb Kunde“ sein.

---

## 3. Werkzeugstandard und Arbeitsumgebung

### 3.1 VS Code ist das Standardwerkzeug

Für Legalis ist **Visual Studio Code (VS Code)** das verbindliche Standardwerkzeug für die BPMN-Modellierung.

### 3.2 Technische Mindestbasis

Ein einsatzfähiger Arbeitsplatz für die BPMN-Modellierung enthält mindestens:

- VS Code,
- Open-BPMN-Extension,
- Java 17 oder höher,
- Git,
- aktuelle lokale oder Remote-Arbeitskopie des freigegebenen Repositories.

---

## 4. Offizielles Legalis-v1.3-Profil

### 4.1 Erlaubte BPMN-Elemente

In offiziellen Legalis-Standardprozessen sind genau diese Elemente erlaubt:

1. **Start Event**
2. **End Event**
3. **Task**
4. **Intermediate Catch Event**
5. **Event Gateway**
6. **Exclusive Gateway** nur kontrolliert für regelbasierte Verzweigungen
7. **Sequence Flow**
8. **Lane**
9. **Data Object** ausschließlich für `Form`
10. **Association** ausschließlich zur Verbindung `Form` ↔ Task

### 4.2 Nicht freigegebene Elemente

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
- sonstige Data Objects außerhalb von `Form`,
- Choreography- oder Conversation-Elemente.

### 4.3 Warum Pools nicht erlaubt sind

Pools sind in BPMN und Imixs grundsätzlich möglich, werden in Legalis v1.3 aber **nicht** verwendet.

Begründung:

- Die Schulungslast wäre höher.
- Die Fehlerrate bei Einsteigern würde steigen.
- Für die ersten Legalis-Standardprozesse reichen Lanes zur Darstellung von Zuständigkeiten aus.
- Externe Beteiligte dürfen in v1.3 bei Bedarf als eigene **Lane** dargestellt werden, solange damit nur Verantwortungszonen und Übergabepunkte beschrieben werden.

### 4.4 Warum User Task und Service Task nicht erlaubt sind

Für die offizielle Legalis-Untermenge verwenden wir bewusst nur das generische **Task**-Element.

Begründung:

- Die dokumentierte Imixs-Erweiterung wird auf **Task** und **Catch Event** angewendet.
- Ein zusätzlicher Typenmix aus Task, User Task und Service Task würde Schulung und Review unnötig erschweren.
- Die Rolle einer Aufgabe wird primär durch **Lane**, Namen, Dokumentation und spätere Actor-/ACL-Konfiguration vermittelt.

---

## 5. Semantik der erlaubten Elemente

### 5.1 Start Event

**Zweck:** Markiert den Beginn eines Prozesses.

**Regeln:**

- Jeder Prozess hat genau ein Start Event.
- Wenn mehrere fachlich unterschiedliche Auslöser existieren, sind in der Regel mehrere Prozesse zu modellieren.
- Das Start Event erhält eine kurze fachliche Bezeichnung.

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
- Der Task-Name beschreibt einen stabilen Zustand, nicht bloß einen Klick.

### 5.4 Intermediate Catch Event

**Zweck:** Beschreibt in Legalis einen **Zustandsübergang** von einem Task in einen anderen.

**Regeln:**

- Jeder engine-relevante Übergang wird mit der Imixs-Workflow-Erweiterung annotiert.
- Jedes Event benötigt eine eindeutige **Event ID** innerhalb des zugehörigen Tasks.
- Event-Namen beschreiben eine erkennbare fachliche Aktion oder Entscheidung.

### 5.5 Event Gateway

**Zweck:** Modelliert alternative Workflow-Events, die von demselben Task ausgehen.

**Regeln:**

- Ein Event Gateway wird verwendet, wenn ein Task mehr als ein mögliches Workflow-Event hat.
- Das Event Gateway ist in Legalis der Standardfall für alternative Imixs-Events.

### 5.6 Lane

**Zweck:** Gliedert das Modell in Verantwortungszonen oder Rollen.

**Regeln:**

- Lanes sind das **einzige erlaubte Mittel**, um Zuständigkeiten visuell zu trennen.
- Eine Lane steht für eine Rolle, Funktion oder Verantwortungszone.
- Wenn ein Prozess ohne Lanes klar und lesbar bleibt, sind Lanes optional.

### 5.7 Data Object `Form`

**Zweck:** Trägt die Imixs-Forms-Definition eines Tasks.

**Regeln:**

- Der Name des Data Objects lautet **genau `Form`**.
- Ein `Form`-Data-Object wird per **Association** mit genau einem Task verbunden.
- Jede Task, die in Imixs-Forms direkt geöffnet oder getestet werden soll, benötigt ein eigenes `Form`-Data-Object.
- Weitere Data Objects sind in v1.3 nicht freigegeben.

### 5.8 Association

**Zweck:** Verbindet `Form` mit dem zugehörigen Task.

**Regeln:**

- Associations werden in v1.3 ausschließlich für `Form` verwendet.
- Andere dekorative oder semantisch unklare Associations sind nicht erlaubt.

---

## 6. Pflichtattribute für offizielle Standardprozesse

### 6.1 Modell-Ebene

Jedes offizielle Standardmodell benötigt:

- **Model Version**

**Beispiel:**
- `mandatsaufnahme-de-1.0.4`

### 6.2 Task-Ebene

Jeder Task benötigt mindestens:

- **Name**
- **Process ID**
- optional, aber empfohlen: **Documentation**

### 6.3 Event-Ebene

Jedes Event benötigt mindestens:

- **Name**
- **Event ID**
- Sichtbarkeit bewusst gesetzt
- optional, aber empfohlen: **Documentation**

### 6.4 Form-Ebene

Jede testbare Form benötigt mindestens:

- Wurzelelement **`imixs-form`**
- mindestens eine **`imixs-form-section`**
- pro Eingabefeld ein **`item`** mit mindestens `name` und `type`

---

## 7. Formkonventionen für Imixs-Forms

### 7.1 Mindeststruktur

Jede Form beginnt mit:

```xml
<?xml version="1.0"?>
<imixs-form>
  <imixs-form-section label="...">
    <item name="..." type="..." label="..." />
  </imixs-form-section>
</imixs-form>
```

### 7.2 Benennung der Items

Für Legalis gilt:

- Standardfelder aus Imixs können übernommen werden, z. B. `_subject`.
- Eigene Fachfelder folgen möglichst dem **dot.Case**-Muster, z. B. `matter.number`, `deadline.first`, `conflict.result`.
- Freie Fantasienamen ohne Systematik sind zu vermeiden.

### 7.3 Pflichtfelder in Forms

Legalis verwendet `required="true"` **selektiv** für geschäftskritische Felder, z. B.:

- Betreff,
- Mandant,
- Eingangsdatum,
- Konfliktentscheidung,
- Mandatsnummer,
- Fristdatum.

Nicht jedes Feld muss Pflichtfeld sein.

### 7.4 Feldtypen

In Legalis v1.3 sind für Standardprozesse bevorzugt:

- `text`
- `textarea`
- `date`
- `selectOneMenu`

HTML/RichText wird in v1.3 nur zurückhaltend eingesetzt.

### 7.5 Auswahlfelder

Für kontrollierte Werte sollen bevorzugt Auswahlfelder statt Freitext verwendet werden, z. B.:

- Sprache,
- Konfliktergebnis,
- Mandatsart,
- Fristart,
- Status.

---

## 8. Review- und Schulungsregeln

Vor Freigabe eines Standardprozesses muss geklärt sein:

- ist der Prozess engine-tauglich,
- ist der Prozess forms-tauglich,
- sind Task- und Event-Namen fachlich lesbar,
- sind die Formfelder knapp, nachvollziehbar und wiederverwendbar,
- ist der Prozess klein genug für Schulung und Review.

---

## 9. Minimalbeispiel Mandatsaufnahme

Das aktuelle Referenzmodell ist:

- `mandatsaufnahme-de-1.0.4.bpmn`

Es dient als Referenz für:

- Task/Event-Semantik,
- Event Gateway an der Konfliktprüfung,
- Form-Definitionen pro Task,
- selektive Pflichtfelder,
- kontrollierte Auswahlfelder.
