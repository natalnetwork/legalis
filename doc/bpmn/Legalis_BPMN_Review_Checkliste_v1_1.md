# Legalis BPMN Review-Checkliste v1.1

Status: Arbeitsversion / V1.1  
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
- Werden Zuständigkeiten ausschließlich mit **Lanes** dargestellt?
- Sind engine-relevante Zustände als **Task** modelliert?
- Sind engine-relevante Übergänge als **Intermediate Catch Event** modelliert?

### 1.3 Gateway-Nutzung

- Wird ein **Event Gateway** nur dort eingesetzt, wo ein Task mehrere alternative Events hat?
- Wurde auf ein Exclusive Gateway verzichtet, wenn eigentlich nur alternative Workflow-Events gemeint sind?
- Falls ein Exclusive Gateway vorhanden ist: ist dessen Einsatz fachlich begründet und dokumentiert?

### 1.4 Technische Mindestattribute

- Ist die **Model Version** gesetzt und eindeutig?
- Haben alle Tasks eine eindeutige **Process ID**?
- Haben alle Events eine sinnvolle **Event ID**?
- Sind sichtbare Benutzeraktionen als öffentliche Events modelliert?

### 1.5 Struktur und Lesbarkeit

- Gibt es genau ein Start Event?
- Gibt es mindestens ein End Event?
- Gibt es lose, unverbundene oder rein dekorative Shapes? Falls ja: entfernen.
- Sind Lane-Namen klar und stabil benannt?
- Sind Task-Namen Zustände und Event-Namen Übergänge?

---

## 2. Mindestfreigabe für Standardprozesse

Ein Standardprozess darf nur freigegeben werden, wenn alle folgenden Aussagen mit **Ja** beantwortet werden können:

- Das Modell folgt dem offiziellen Legalis-v1.2-Profil.
- Das Modell ist mit der dokumentierten Imixs-Arbeitsweise kompatibel.
- Es wurden keine Pools verwendet.
- Es wurden keine User Tasks oder Service Tasks verwendet.
- Task-, Event- und Modell-IDs sind konsistent.
- Das Modell ist grafisch sauber und fachlich nachvollziehbar.

---

## 3. Schnellprüfung für Einsteiger

Vor dem ersten Commit einmal laut oder gedanklich prüfen:

1. Ein Fall oder zehn Fälle?  
   Wenn zehn Fälle: Modell zu groß.
2. Zustände als Task oder als Tätigkeit modelliert?  
   Für Legalis v1.2: **Zustand = Task**.
3. Übergänge als Event modelliert?  
   Für Legalis v1.2: **Übergang = Intermediate Catch Event**.
4. Verantwortlichkeiten klar?  
   Wenn nein: **Lane ergänzen**, nicht Pool.
5. Zwei Alternativen am selben Task?  
   Dann zuerst an **Event Gateway** denken.
