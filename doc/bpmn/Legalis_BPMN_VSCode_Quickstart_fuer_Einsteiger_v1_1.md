# Legalis BPMN VS Code Quickstart für Einsteiger v1.1

Status: Arbeitsversion / V1.1  
Zielgruppe: BPMN-Einsteiger im Legalis-Kontext  
Zweck: Schnellstart für die ersten offiziellen Legalis-Standardprozesse in VS Code

---

## 1. Ziel dieses Dokuments

Dieses Dokument zeigt den schnellsten sauberen Weg, um in VS Code ein Legalis-konformes BPMN-Modell anzulegen.

Wichtig: Für offizielle Legalis-Standardprozesse gilt das **Legalis-v1.2-Profil**.

---

## 2. Voraussetzungen

- VS Code ist installiert.
- Open-BPMN ist installiert.
- Java 17 oder höher ist installiert.
- Das passende Git-Repository ist aktuell synchronisiert.

---

## 3. Neue Datei anlegen

1. Arbeitsverzeichnis im Repository öffnen.
2. Neue Datei mit Endung `.bpmn` anlegen.
3. Datei im Open-BPMN-Editor öffnen.

Empfehlung für Standardprozesse:

- `workflow/models/standard/<prozessname>.bpmn`

---

## 4. Reihenfolge für das erste Modell

Lege Elemente in dieser Reihenfolge an:

1. Start Event
2. benötigte Lanes
3. erster Task
4. erstes Intermediate Catch Event
5. nächster Task
6. Event Gateway nur falls mehrere alternative Events vorhanden sind
7. weitere Events und Tasks
8. End Event(s)
9. Sequence Flows verbinden

---

## 5. Welche Elemente Du in v1.2 verwenden darfst

Erlaubt:

- Start Event
- End Event
- Task
- Intermediate Catch Event
- Event Gateway
- Exclusive Gateway nur kontrolliert
- Lane
- Sequence Flow

Nicht erlaubt:

- Pool
- User Task
- Service Task
- Business Rule Task
- Message Flow
- Timer Event

---

## 6. Imixs-Erweiterung setzen

Für jeden engine-relevanten **Task** und jedes engine-relevante **Intermediate Catch Event**:

1. Im Toolbereich die Imixs-Workflow-Erweiterung wählen.
2. Auf das Ziel-Element ziehen.
3. Im Property Panel die Mindestattribute setzen.

### 6.1 Mindestattribute pro Task

- Name
- Process ID
- optional Documentation

### 6.2 Mindestattribute pro Event

- Name
- Event ID
- Public Event = ja, sofern es eine sichtbare Benutzeraktion ist
- optional Documentation

### 6.3 Mindestattribut pro Modell

- Model Version

---

## 7. Lanes richtig verwenden

In Legalis v1.2 gilt:

- **Lanes ja**
- **Pools nein**

Verwende eine Lane für:

- Rolle,
- Verantwortungszone,
- organisatorische Funktion.

Beispiele:

- Kanzleiassistenz
- Anwalt / Sachbearbeitung
- Externe Buchhaltung

---

## 8. Standarddenkweise für Legalis

Merksätze:

- **Task = Zustand**
- **Event = Übergang**
- **Lane = Verantwortung**
- **Ein Prozess = ein Durchlauf**
- **Mehrere Events an einem Task = Event Gateway prüfen**

---

## 9. Vor dem Speichern prüfen

- genau ein fachlicher Durchlauf?
- keine Pools?
- keine losen Shapes?
- Tasks als Zustände benannt?
- Events als Übergänge benannt?
- IDs sauber vergeben?

Wenn alle Antworten positiv sind, kann das Modell gespeichert und committed werden.
