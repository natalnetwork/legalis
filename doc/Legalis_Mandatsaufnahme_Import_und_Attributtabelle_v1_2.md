# Legalis Mandatsaufnahme – Import- und Attributtabelle v1.2

Status: passend zu Modell `mandatsaufnahme-de-1.0.4.bpmn`

---

## 1. Zweck

Dieses Dokument beschreibt den offiziellen Standardprozess „Mandatsaufnahme“ in der Form, in der er nach dem Legalis-v1.3-Profil modelliert ist.

Das Modell verwendet:

- keine Pools,
- Tasks als Zustände,
- Intermediate Catch Events als Zustandsübergänge,
- ein Event Gateway für alternative Events an der Konfliktprüfung,
- pro testbarer Task ein Data Object `Form`.

---

## 2. Modell-Ebene

| Attribut | Wert |
|---|---|
| Prozessname | Mandatsaufnahme |
| Model Version | `mandatsaufnahme-de-1.0.4` |
| Lanes | keine im Pilotmodell |
| UI-Status | in Imixs-Forms erfolgreich getestet |

---

## 3. Verwendete Objekte

| Nr. | Typ | Name | Technischer Schlüssel |
|---|---|---|---|
| 1 | Start Event | Anfrage eingegangen | – |
| 2 | Task | Lead offen | `processid=1000` |
| 3 | Intermediate Catch Event | Lead erfasst | `activityid=10` |
| 4 | Task | Konfliktprüfung offen | `processid=1100` |
| 5 | Event Gateway | Ergebnis Konfliktprüfung? | – |
| 6 | Intermediate Catch Event | Konflikt festgestellt | `activityid=20` |
| 7 | Task | Mandat abgelehnt | `processid=1900` |
| 8 | End Event | Vorgang beendet – abgelehnt | – |
| 9 | Intermediate Catch Event | Kein Konflikt | `activityid=10` |
| 10 | Task | Mandat anlegen | `processid=1200` |
| 11 | Intermediate Catch Event | Mandat angelegt | `activityid=10` |
| 12 | Task | Erste Frist erfassen | `processid=1300` |
| 13 | Intermediate Catch Event | Frist erfasst | `activityid=10` |
| 14 | Task | Mandat aktiv | `processid=1400` |
| 15 | End Event | Vorgang beendet – aktiv | – |

---

## 4. Pflichtattribute

### 4.1 Prozess

| Attribut | Pflicht | Wert |
|---|---|---|
| Model Version | ja | `mandatsaufnahme-de-1.0.4` |

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

### 4.4 Forms

| Task | Form vorhanden | Bemerkung |
|---|---|---|
| 1000 Lead offen | ja | Intake-Felder mit selektiven Pflichtfeldern |
| 1100 Konfliktprüfung offen | ja | Konfliktergebnis als Auswahlfeld |
| 1900 Mandat abgelehnt | ja | Ablehnungsgrund als Pflichtfeld |
| 1200 Mandat anlegen | ja | Mandatsart als Auswahlfeld |
| 1300 Erste Frist erfassen | ja | Fristart als Auswahlfeld |
| 1400 Mandat aktiv | ja | Status als Auswahlfeld |

---

## 5. Härtungsschritte in v1.0.4

Gegenüber `1.0.3` wurden folgende Punkte geschärft:

1. geschäftskritische Kernfelder als `required="true"` markiert,
2. mehrere Freitextfelder durch kontrollierte Auswahlfelder ersetzt,
3. HTML-Felder auf einfache `textarea` reduziert,
4. Feldnamen an einer einheitlichen `dot.Case`-Logik ausgerichtet,
5. Referenzmodell explizit als UI-getesteter Stand festgehalten.

---

## 6. Nummerierung

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
