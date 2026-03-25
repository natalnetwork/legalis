# Legalis Deployment-Strategie: ISO und Automation v1

## 1. Zweck dieses Dokuments

Dieses Dokument beschreibt die bevorzugte Deployment-Strategie für Legalis in zwei Ausprägungen:

1. **Standardisierte Installation auf Basis eines offiziellen Debian-Systems mit automatisierter Nachkonfiguration**
2. **Spätere, vertriebsfähige Installations-ISOs für klar definierte Serverrollen**

Ziel ist eine Installations- und Update-Strategie, die auch unter realen Bedingungen im Consulting-Alltag robust funktioniert. Sie soll Fehlbedienung reduzieren, Wiederholbarkeit sicherstellen und die Zahl supportintensiver manueller Schritte so weit wie möglich begrenzen.

Dieses Dokument ergänzt die allgemeine Repository- und Deployment-Policy. Es ersetzt sie nicht.

---

## 2. Ausgangslage und Problemstellung

In der Praxis ist nicht davon auszugehen, dass alle Consultants, Administratoren oder Mitarbeiter auf Kundenseite über ein gleichmäßiges technisches Niveau verfügen. Die Deployment-Strategie von Legalis muss deshalb so gestaltet werden, dass sie:

- mit möglichst wenigen manuellen Schritten auskommt,
- auf Windows- und Linux-geprägten Arbeitsumgebungen verständlich bleibt,
- Fehlkonfigurationen möglichst früh verhindert,
- reproduzierbare Installationen ermöglicht,
- und auch bei personellen Wechseln tragfähig bleibt.

Ein Deployment, das voraussetzt, dass der ausführende Consultant zunächst manuell ein Betriebssystem installiert, danach die Toolchain korrekt einrichtet, anschließend die richtigen Repositories klont und danach noch alle Dienste fehlerfrei konfiguriert, ist langfristig zu fehleranfällig.

Daraus folgt: **Legalis benötigt mittelfristig ein stark standardisiertes Installationsverfahren.**

---

## 3. Strategische Grundentscheidung

Für Legalis gilt folgende Grundentscheidung:

### 3.1 Kurz- und mittelfristig

Die erste produktiv nutzbare Generation von Legalis wird auf einem **offiziellen Debian-Basissystem** aufgebaut. Installation und Konfiguration erfolgen so weit wie möglich automatisiert durch:

- Paketlisten,
- Installationsskripte,
- Konfigurationsmanagement,
- vordefinierte Rollenprofile,
- systemd-Units und Timer,
- sowie dokumentierte Post-Install-Schritte.

### 3.2 Langfristig bzw. für vertriebsfähige Releases

Sobald die Serverrollen stabil definiert und ausreichend getestet sind, sollen für Legalis **eigene rollenbasierte Installations-ISOs** bereitgestellt werden.

Diese ISOs stellen **keine eigene Linux-Distribution** dar, sondern ein angepasstes Installationsmedium auf Debian-Basis.

---

## 4. Warum nicht sofort ein eigenes ISO als erster Schritt?

Ein eigenes Installations-ISO ist attraktiv, aber in der frühen Produktphase kein guter erster Meilenstein.

Dagegen sprechen insbesondere:

- zusätzliche Komplexität bei Build, Test und Pflege,
- höherer Aufwand bei jeder Änderung an Toolchain oder Paketbasis,
- zusätzlicher Dokumentations- und Testaufwand,
- höheres Risiko, Fehler in das Medium selbst einzubauen,
- und ein verfrühter Fokus auf Distributionsmechanik statt auf Produktlogik.

Deshalb wird zunächst das Produkt und seine Rolleninstallation stabilisiert. Erst danach wird aus der funktionierenden Installationsautomatisierung ein standardisiertes ISO abgeleitet.

**Grundsatz:**

> Zuerst muss Legalis zuverlässig automatisiert installierbar sein. Erst danach lohnt sich die Verpackung als ISO.

---

## 5. Zielbild: Rollenbasierte Installationsmedien

Für Legalis werden perspektivisch zwei getrennte Installationsmedien angestrebt:

### 5.1 Legalis App Server ISO

Zweck:

- Backend-Komponenten
- API
- Legalis-Core-Dienste
- Dokumentation
- Betriebs- und Update-Komponenten
- optionale Administrationswerkzeuge

### 5.2 Legalis Workflow Server ISO

Zweck:

- Workflow-Runtime
- BPMN-bezogene Komponenten
- Standardprozessmodelle
- Import- und Laufzeitumgebung für Workflow-Assets
- optional unterstützende Test- und Verwaltungswerkzeuge

Diese Trennung reduziert Komplexität, erleichtert Support und erlaubt eine klare Aufgabenverteilung zwischen Serverrollen.

---

## 6. Zulässige Auslieferungsinhalte einer Legalis-ISO

Eine Legalis-ISO darf enthalten:

- das Debian-Basissystem,
- die für die jeweilige Serverrolle erforderlichen Pakete,
- die standardisierte Toolchain,
- systemd-Units und Timer,
- Legalis-Core-Komponenten,
- offizielle Standardprozesse,
- allgemeine Dokumentation,
- Betriebswerkzeuge,
- und einen First-Boot- oder Post-Install-Mechanismus zur kundenspezifischen Initialisierung.

Eine Legalis-ISO darf **nicht** enthalten:

- kundenspezifische Betriebsgeheimnisse,
- produktive Zugangsdaten,
- private Schlüssel,
- kundenspezifische API-Secrets,
- Mail-Credentials,
- echte Lizenzschlüssel,
- oder private Kundenprozesse und Custom Extensions.

---

## 7. Trennung zwischen Standardinstallation und Kundenspezifik

Legalis folgt auch im Deployment dem Prinzip:

**Core + Customer Overlay**

Das bedeutet:

### 7.1 Core

Der Core umfasst:

- das Debian-basierte Standardsystem,
- die allgemeine Toolchain,
- Legalis-Core-Software,
- Standardprozesse,
- generische Dokumentation,
- und allgemeine Betriebslogik.

### 7.2 Customer Overlay

Das Customer Overlay umfasst ausschließlich kundenspezifische Bestandteile, insbesondere:

- individuelle BPMN-Erweiterungen,
- kundenspezifische Templates,
- kundenspezifische Konfiguration,
- kundenspezifische Python-Erweiterungen,
- und kundenspezifische Zugangsdaten.

Diese Bestandteile dürfen **nicht** in öffentliche oder allgemeine Distributionsmedien eingebettet werden.

---

## 8. First-Boot- und Initialisierungsstrategie

Statt Kundendaten in die ISO einzubetten, wird eine zweistufige Initialisierung vorgesehen.

### 8.1 Installationsphase

Die ISO installiert das Basissystem und die definierte Serverrolle vollständig.

### 8.2 Initialisierungsphase

Beim ersten Start oder in einem kontrollierten Nachkonfigurationsschritt werden abgefragt oder eingespielt:

- Kundenkennung,
- Lizenzdaten,
- lokale Benutzerkonten,
- Rollen- und Zugangskonfiguration,
- Mail- und Integrationsdaten,
- Pfade und Mounts,
- sowie optional das kundenspezifische Overlay.

Damit bleibt das ISO allgemein verwendbar, ohne kundenspezifische Informationen preiszugeben.

---

## 9. Update-Strategie

### 9.1 Grundsatz

Legalis soll **nicht** durch unkontrollierte Git-Pulls auf produktiven Systemen aktualisiert werden.

Produktive Systeme benötigen:

- nachvollziehbare Updates,
- signierbare Quellen,
- definierte Rollback-Strategien,
- und klar trennbare Verantwortlichkeiten.

### 9.2 Debian-Basis

Betriebssystem- und Sicherheitsupdates erfolgen über den regulären Paketmechanismus des Basissystems.

### 9.3 Legalis-Komponenten

Legalis-spezifische Updates sollen mittelfristig über einen kontrollierten Update-Kanal bereitgestellt werden, vorzugsweise:

- über ein signiertes internes oder öffentlich kontrolliertes Paket-Repository,
- oder über reproduzierbare Release-Pakete mit dokumentierter Versionierung.

### 9.4 Automatisierung

Wiederkehrende Prüfungen auf Updates dürfen über systemd-Timer angestoßen werden. Dabei muss klar getrennt werden zwischen:

- reinem Prüfmechanismus,
- automatischer Installation sicherer Updates,
- und kontrollierten größeren Versionswechseln.

Große Release-Sprünge dürfen nicht blind automatisiert werden.

---

## 10. Distribution über GitHub

Für Legalis gilt:

- Quellcode, Doku und Governance-Dokumente liegen im regulären GitHub-Repository.
- Große Binärartefakte wie Installations-ISOs gehören **nicht** in den normalen Git-Verlauf.
- Vertriebsfähige ISOs sollen stattdessen als **Release-Artefakte** veröffentlicht werden.

Damit bleibt das Repository schlank, während installierbare Medien separat versioniert und verteilt werden können.

---

## 11. Ventoy als Consulting-Werkzeug

Ventoy ist als praktisches Transport- und Bootmedium für Consultants sinnvoll.

Vorteile:

- mehrere ISO-Dateien auf einem Medium,
- schneller Wechsel zwischen Serverrollen,
- einfache Aktualisierung der Medien,
- weniger Schreibaufwand für USB-Sticks,
- und hohe Praxistauglichkeit im Außeneinsatz.

Ventoy ist jedoch nur das Transport- und Bootwerkzeug. Es ersetzt weder die Installationslogik noch die Rollendefinition von Legalis.

---

## 12. Auswirkungen auf den Setup Guide

Der Setup Guide von Legalis muss künftig zwei Wege dokumentieren:

### 12.1 Weg A: Entwicklungs- und frühe Pilotinstallation

- offizielles Debian installieren,
- Repositories klonen,
- Toolchain automatisiert einrichten,
- Rollenprofil anwenden,
- Dienste starten und testen.

### 12.2 Weg B: Standardisierte Feldinstallation über ISO

- passendes Rollen-ISO wählen,
- über Ventoy oder alternatives Bootmedium starten,
- Installation durchführen,
- First-Boot-Initialisierung abschließen,
- Kundenspezifik nachladen,
- Update-Kanal prüfen.

Beide Wege müssen dieselbe fachliche Zielkonfiguration herstellen.

---

## 13. Qualitätsanforderungen an ein vertriebsfähiges ISO

Ein Legalis-ISO gilt erst dann als vertriebsfähig, wenn mindestens folgende Punkte erfüllt sind:

- reproduzierbarer Build,
- dokumentierte Paketbasis,
- definierte Serverrolle,
- erfolgreiche Testinstallation auf Referenzhardware,
- dokumentierte First-Boot-Initialisierung,
- definierte Update-Strategie,
- keine eingebetteten produktiven Geheimnisse,
- und klare Versionierung des Mediums.

---

## 14. Sicherheitsgrundsätze

Für die ISO- und Automationsstrategie gelten diese Sicherheitsregeln:

1. Keine produktiven Secrets im Distributionsmedium
2. Keine privaten Kundenprozesse im Core-Image
3. Keine kundenspezifischen Extensions im öffentlichen Core-Repository
4. Trennung zwischen allgemeinem Rollenimage und kundenindividueller Nachkonfiguration
5. Update-Mechanismen müssen kontrollierbar und dokumentiert sein
6. Jede produktive Installation muss einer klaren Release-Version zuordenbar sein

---

## 15. Entscheidung für Version 1

Für die aktuelle Projektphase gilt verbindlich:

### Verbindlich beschlossen

- Legalis setzt zunächst auf **standardisiertes Debian plus Automation**.
- Die ISO-Strategie wird als **geplante, gewünschte und architektonisch sinnvolle Ausbauform** dokumentiert.
- Kundenspezifische Daten und private Prozesse bleiben grundsätzlich außerhalb allgemeiner Installationsmedien.
- Der Setup Guide muss bereits so formuliert werden, dass er später den ISO-Weg sauber aufnehmen kann.

### Noch nicht Bestandteil von v1

- finaler ISO-Build-Prozess,
- eigener Installer-Dialog,
- finale Paketierungsstrategie,
- vollautomatisierte First-Boot-Assistenten,
- und produktionsreife Release-Pipeline für ISOs.

---

## 16. Empfehlung für das weitere Vorgehen

Die nächste sinnvolle Reihenfolge lautet:

1. Rollen auf Basis eines Standard-Debian-Setups sauber definieren
2. Installation und Nachkonfiguration skriptbar machen
3. Update-Logik kontrolliert festlegen
4. Referenzsysteme reproduzierbar aufsetzen
5. Erst danach aus diesem Stand Installations-ISOs ableiten

Damit wird vermieden, dass eine hübsche ISO einen unreifen Installationsprozess lediglich verpackt, statt ihn wirklich zu standardisieren.

---

## 17. Kurzform der Leitentscheidung

> Legalis verfolgt zunächst den Weg „offizielles Debian plus Automation“ und entwickelt daraus später rollenbasierte, vertriebsfähige Installations-ISOs. Kundenspezifische Daten, Prozesse und Secrets werden grundsätzlich nicht in allgemeine Installationsmedien eingebettet, sondern über kontrollierte Initialisierung und private Overlays ergänzt.
