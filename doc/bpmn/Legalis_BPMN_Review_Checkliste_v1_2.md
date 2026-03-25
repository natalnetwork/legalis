# Legalis BPMN Review-Checkliste v1.2

Status: Arbeitsversion / V1.2  
Zielgruppe: Consultants, Reviewer, interne Produktverantwortliche  
Zweck: Schnelle fachliche und formale Prüfung eines BPMN-Modells vor Freigabe, Schulung oder Kundenverwendung

---

## 1. Pflichtfragen vor jeder Freigabe

### 1.1 Prozesszuschnitt

- Beschreibt das Modell **genau einen fachlichen Durchlauf**?
- Wurde ein Universal- oder Sammelprozess vermieden?
- Ist der Prozess fachlich klein genug, um in einer Schulung erklärt werden zu können?

### 1.2 Elementauswahl

- Verwendet das Modell nur freigegebene Elemente?
- Enthält das Modell **keine Pools**?
- Werden Zuständigkeiten ausschließlich mit **Lanes** dargestellt, falls überhaupt eine visuelle Rollenaufteilung nötig ist?
- Sind engine-relevante Zustände als **Task** modelliert?
- Sind engine-relevante Übergänge als **Intermediate Catch Event** modelliert?
- Werden Data Objects ausschließlich für **`Form`** verwendet?
- Werden Associations ausschließlich für **`Form` ↔ Task** verwendet?

### 1.3 Gateway-Nutzung

- Wird ein **Event Gateway** verwendet, wenn ein Task mehrere alternative Events hat?
- Wurde auf ein Exclusive Gateway verzichtet, wenn eigentlich nur alternative Workflow-Events gemeint sind?
- Falls ein Exclusive Gateway vorhanden ist: ist dessen Einsatz fachlich begründet und dokumentiert?

### 1.4 Technische Mindestattribute

- Ist die **Model Version** gesetzt und eindeutig?
- Haben alle Tasks eine eindeutige **Process ID**?
- Haben alle Events eine sinnvolle **Event ID**?
- Sind sichtbare Benutzeraktionen als öffentliche Events modelliert?

### 1.5 Forms-Tauglichkeit

- Hat jede in Imixs-Forms testbare Task ein Data Object **`Form`**?
- Ist jede Form per Association mit genau einem Task verbunden?
- Enthält jede Form mindestens eine `imixs-form-section`?
- Hat jedes `item` mindestens `name` und `type`?
- Sind geschäftskritische Felder sinnvoll als `required="true"` markiert?
- Wurden kontrollierte Werte möglichst als `selectOneMenu` statt Freitext modelliert?

### 1.6 Struktur und Lesbarkeit

- Gibt es genau ein Start Event?
- Gibt es mindestens ein End Event?
- Gibt es lose, unverbundene oder rein dekorative Shapes? Falls ja: entfernen.
- Sind Task-Namen Zustände und Event-Namen Übergänge?
- Sind Formlabels für Nicht-Techniker verständlich?

---

## 2. Mindestfreigabe für Standardprozesse

Ein Standardprozess darf nur freigegeben werden, wenn alle folgenden Aussagen mit **Ja** beantwortet werden können:

- Das Modell folgt dem offiziellen Legalis-v1.3-Profil.
- Das Modell ist mit der dokumentierten Imixs-Arbeitsweise kompatibel.
- Es wurden keine Pools verwendet.
- Es wurden keine User Tasks oder Service Tasks verwendet.
- Task-, Event- und Modell-IDs sind konsistent.
- Die Formdefinitionen sind für den UI-Test ausreichend.
- Das Modell ist grafisch sauber und fachlich nachvollziehbar.

---

## 3. Schnellprüfung für Einsteiger

Vor dem ersten Commit einmal laut oder gedanklich prüfen:

1. Ein Fall oder zehn Fälle?  
   Wenn zehn Fälle: Modell zu groß.
2. Zustand oder Tätigkeit?  
   Für Legalis: **Zustand = Task**.
3. Übergang oder Entscheidungstext?  
   Für Legalis: **Übergang = Intermediate Catch Event**.
4. Brauche ich wirklich eine Lane?  
   Wenn nein: weglassen. Wenn ja: Lane statt Pool.
5. Kann die Task in Imixs-Forms geöffnet werden?  
   Wenn ja: **`Form`-Data-Object prüfen**.
6. Sind die wichtigsten Felder Pflichtfelder?  
   Nur selektiv, nicht inflationär.
