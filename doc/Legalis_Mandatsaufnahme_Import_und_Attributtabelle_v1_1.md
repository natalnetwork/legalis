# Legalis Mandatsaufnahme – Import- und Attributtabelle v1.1

Status: passend zu Modell `mandatsaufnahme-de-1.0.2.bpmn`

---

## 1. Zweck

Dieses Dokument beschreibt den offiziellen Standardprozess „Mandatsaufnahme“ in der Form, in der er nach dem Legalis-v1.2-Profil modelliert ist.

Das Modell verwendet:

- keine Pools,
- nur Lanes,
- Tasks als Zustände,
- Intermediate Catch Events als Zustandsübergänge,
- ein Event Gateway für alternative Events an der Konfliktprüfung.

---

## 2. Modell-Ebene

| Attribut | Wert |
|---|---|
| Prozessname | Mandatsaufnahme |
| Model Version | `mandatsaufnahme-de-1.0.2` |
| Lanes | `Kanzleiassistenz`, `Anwalt / Sachbearbeitung` |

---

## 3. Verwendete Objekte

| Nr. | Typ | Name | Technischer Schlüssel | Lane |
|---|---|---|---|---|
| 1 | Start Event | Anfrage eingegangen | – | Kanzleiassistenz |
| 2 | Task | Lead offen | `processid=1000` | Kanzleiassistenz |
| 3 | Intermediate Catch Event | Lead erfasst | `activityid=10` | Kanzleiassistenz |
| 4 | Task | Konfliktprüfung offen | `processid=1100` | Anwalt / Sachbearbeitung |
| 5 | Event Gateway | Ergebnis Konfliktprüfung? | – | Anwalt / Sachbearbeitung |
| 6 | Intermediate Catch Event | Konflikt festgestellt | `activityid=20` | Anwalt / Sachbearbeitung |
| 7 | Task | Mandat abgelehnt | `processid=1900` | Anwalt / Sachbearbeitung |
| 8 | End Event | Vorgang beendet – abgelehnt | – | Anwalt / Sachbearbeitung |
| 9 | Intermediate Catch Event | Kein Konflikt | `activityid=10` | Kanzleiassistenz |
| 10 | Task | Mandat anlegen | `processid=1200` | Kanzleiassistenz |
| 11 | Intermediate Catch Event | Mandat angelegt | `activityid=10` | Kanzleiassistenz |
| 12 | Task | Erste Frist erfassen | `processid=1300` | Kanzleiassistenz |
| 13 | Intermediate Catch Event | Frist erfasst | `activityid=10` | Kanzleiassistenz |
| 14 | Task | Mandat aktiv | `processid=1400` | Anwalt / Sachbearbeitung |
| 15 | End Event | Vorgang beendet – aktiv | – | Anwalt / Sachbearbeitung |

---

## 4. Pflichtattribute

### 4.1 Prozess

| Attribut | Pflicht | Wert |
|---|---|---|
| Model Version | ja | `mandatsaufnahme-de-1.0.2` |

### 4.2 Tasks

| Task | Pflichtattribute |
|---|---|
| Lead offen | Name, Process ID, Documentation empfohlen |
| Konfliktprüfung offen | Name, Process ID, Documentation empfohlen |
| Mandat abgelehnt | Name, Process ID, Documentation empfohlen |
| Mandat anlegen | Name, Process ID, Documentation empfohlen |
| Erste Frist erfassen | Name, Process ID, Documentation empfohlen |
| Mandat aktiv | Name, Process ID, Documentation empfohlen |

### 4.3 Events

| Event | Pflichtattribute |
|---|---|
| Lead erfasst | Name, Event ID, Public Event, Documentation empfohlen |
| Konflikt festgestellt | Name, Event ID, Public Event, Documentation empfohlen |
| Kein Konflikt | Name, Event ID, Public Event, Documentation empfohlen |
| Mandat angelegt | Name, Event ID, Public Event, Documentation empfohlen |
| Frist erfasst | Name, Event ID, Public Event, Documentation empfohlen |

---

## 5. Nummerierung

| Bereich | Nummern |
|---|---|
| Intake | 1000 |
| Konfliktprüfung | 1100 |
| Mandatsanlage | 1200 |
| Fristen | 1300 |
| aktiver Status | 1400 |
| Ablehnung | 1900 |

Event-IDs im Modell:

- `10` = Standard-Weiterverarbeitung
- `20` = alternative Ablehnung nach Konfliktprüfung
