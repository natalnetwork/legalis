# Legalis – Mandatsaufnahme Validierungsstrategie v1

## Ziel
Die Pflichtfelder der Mandatsaufnahme sollen nicht nur in der Form dargestellt, sondern beim Wechsel in den nächsten Workflow-Zustand technisch erzwungen werden.

## Technischer Ansatz
Die reine Formular-Definition in Imixs-Forms ist für Legalis nicht ausreichend, um Pflichtfelder belastbar durchzusetzen. Deshalb wird die Validierung über Business Rules direkt an den BPMN-Events umgesetzt.

## Umsetzungsprinzip
Für die Ereignisse des Prozesses werden Imixs-Regeln hinterlegt:

- `txtBusinessRuleEngine = javascript`
- `txtBusinessRule = <Regelskript>`

Wenn das Skript `result.isValid = false` setzt, blockiert Imixs den Event-Übergang.

## In 1.0.5 validierte Ereignisse

### Event 1010 – Lead erfasst
Pflichtfelder:
- `_subject`
- `mandant.name`
- `gegenseite.name`
- `lead.received`

### Event 1110 – Kein Konflikt
Pflichtfelder:
- `conflict.checked`
- `conflict.result = keinKonflikt`

### Event 1120 – Konflikt festgestellt
Pflichtfelder:
- `conflict.checked`
- `conflict.result = konflikt`
- `rejection.date`
- `rejection.reason`

### Event 1210 – Mandat angelegt
Pflichtfelder:
- `_subject`
- `mandant.name`
- `matter.number`
- `matter.type`
- `matter.opened`

### Event 1310 – Frist erfasst
Pflichtfelder:
- `matter.number`
- `deadline.first`
- `deadline.kind`

## Empfehlung
Die Formularattribute wie `required="true"` können für bessere Benutzerführung im Modell verbleiben. Die fachlich verbindliche Validierung soll in Legalis jedoch über die Event-Regeln erfolgen.

## Nächster Test
1. `mandatsaufnahme-de-1.0.5.bpmn` in `runtime/imixs-forms/models/` kopieren
2. per API hochladen
3. Workflow erneut durchklicken
4. prüfen, ob fehlende Pflichtfelder jetzt den Übergang blockieren
