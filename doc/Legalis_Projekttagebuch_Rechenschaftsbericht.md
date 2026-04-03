# Legalis – Projekttagebuch / Rechenschaftsbericht

**Berichtsstand:** 27.03.2026  
**Zweck:** Zusammenfassender Rechenschaftsbericht über die bisherigen Tätigkeiten, Entscheidungen und Bemühungen im Zusammenhang mit dem Projekt **Legalis**.  
**Hinweis:** Bereits separat erzeugte Fach-Markdowns werden hier bewusst **nicht** erneut angehängt, da sie bereits separat gespeichert wurden.

---

## Einordnung

Im bisherigen Verlauf wurde Legalis von einer allgemeinen Produktidee zu einem strukturierten Vorhaben mit klarer Produktphilosophie, Pilotkundenbezug, MVP-Abgrenzung, Modulstruktur, Architekturentscheidungen, Infrastrukturplanung und ersten praktischen Workflow-/BPMN-Tests weiterentwickelt.

Früh wurde festgelegt, dass Legalis **kein beliebiges Kanzlei-Baukastensystem**, sondern ein **standardorientiertes digitales Betriebsmodell für brasilianische Kanzleien** sein soll. Leitprinzipien dabei sind insbesondere:

- Standard zuerst
- Konfiguration vor Customizing
- Workflow vor KI
- klare Trennung zwischen Core, Konfiguration und Erweiterungen
- klare Trennung zwischen Standardprozessen und kundenspezifischen Erweiterungen

---

## 19.03.2026 – Fachliche Grundlegung und Produktmodell

An diesem Tag wurde das Projekt fachlich konsolidiert und in eine belastbare Zielrichtung überführt.

### Erreichte Ergebnisse

- Der **Pilotkunde** wurde präzisiert: **Mychelle Maciel Advogados** als erste Referenzkanzlei mit realem brasilianischem Anwendungskontext.
- Die Produktphilosophie wurde geschärft: **Standard zuerst**, **Konfiguration vor Customizing**, **Workflow vor KI**.
- Es wurde festgelegt, dass Legalis als **Reference Law Firm Brazil v1** modelliert wird und nicht jede historisch gewachsene Kanzlei-Sonderlogik nachbilden soll.

### Inhaltliche Festlegungen

Die Soll-Prozesslandschaft wurde in fachliche Bereiche zerlegt, unter anderem:

- Intake / Erstkontakt
- Konfliktprüfung
- Mandanten- und Mandatsverwaltung
- Dokumentenerzeugung
- Aufgaben- und Fristensteuerung
- Kommunikationslog
- Billing / Finance
- Governance / Audit
- Workflow / BPMN

### Ergebnis

Das **MVP** wurde bewusst auf einen arbeitsfähigen Kern reduziert. Spätere Premium- und Enterprise-Themen wurden logisch vorbereitet, aber nicht in den MVP gezogen.

Ebenfalls an diesem Tag wurden die beiden grundlegenden Strukturdokumente ausgearbeitet:

- **Projektfahrplan v2**
- **Module Catalog v1**

Damit wurde Legalis erstmals als echtes Produktportfolio mit Modulzwecken, Kernobjekten, Paketlogik und MVP-Status beschrieben.

---

## 19.03.2026 – BPMN-Governance, Standardprozesse und Custom-Layer

Parallel zur Produktmodellierung wurde die Governance der künftigen Workflow-Welt festgelegt.

### Erreichte Ergebnisse

- Entscheidung für ein **bewusst eingeschränktes BPMN-v1-Modell**
- Freigabe nur eines kleinen, kontrollierten Satzes von BPMN-Kernelementen
- frühe Festlegung einer **harten Trennung** zwischen Standardprozessen und kundenspezifischen Erweiterungen
- Konzeption eines späteren Freigabemodells für Änderungen an Standardprozessen

### Bedeutung

Diese Entscheidung ist strategisch zentral. Sie verhindert, dass Legalis früh in unkontrolliertes Low-Code- oder BPMN-Chaos abgleitet, und stützt das spätere Beratungs-, Governance- und Haftungsmodell.

---

## 19.03.2026 – Finanzmodul, Liquidität und Session-Control

Ein wesentlicher Fortschritt war die Einordnung des Finanzbereichs.

### Erreichte Ergebnisse

- Es wurde ausdrücklich festgelegt, dass Legalis im MVP **keine klassische Buchhaltungssoftware** sein soll.
- Stattdessen wurde das Zielbild **Financial Operations & Liquidity Management for Law Firms** definiert.
- Für das MVP wurden als Finanzkern festgehalten:
  - Einnahmen und Ausgaben
  - wiederkehrende Kosten
  - manuell gepflegte Bankkontosalden
  - Liquiditätsrechnung auf Kalenderbasis
  - einfache Reports für externe Buchhaltung

### Verfeinerung im Projektverlauf

Zusätzlich wurde die **Session-Control / Zeiterfassung** als fachlich wichtiger Teil der Ablauforganisation herausgearbeitet:

- Zeitbezug zur Bearbeitung eines Mandats
- manuelle Eingriffe nur mit Berechtigung
- Protokollierung jeder Änderung
- Rückverfolgbarkeit und Rückgängigmachung
- Begründungspflicht bei Anpassungen
- Grundlage für spätere Rollen- und Auditlogik

### Bedeutung

Damit wurde die wirtschaftliche und organisatorische Seite des Projekts früh mitgedacht und nicht auf spätere Phasen verschoben.

---

## 19.03.2026 – Dokumentengenerierung und Template-Architektur

Die Dokumentenstrategie wurde verbindlich festgelegt.

### Erreichte Ergebnisse

- Entscheidung für **JSON-first** als interne Datenwahrheit
- Entscheidung für **DOCX/DOTX** als praxistaugliches Template-Format im Kanzleiumfeld
- Entscheidung für **PDF** als verbindliches Endformat
- Festlegung einer minimalen Template-Versionierung mit stabiler Template-ID, Revision/Version, Status und Importmetadaten

### Bedeutung

Damit wurde eine tragfähige Brücke zwischen juristisch alltagstauglichen Vorlagen und sauberer Systemarchitektur geschaffen. Insbesondere wurde vermieden, DOCX selbst zur Systemlogik zu machen.

---

## 19.03.2026 – Sprachliche Aufbereitung für den juristischen Fachbereich

Neben der technischen und fachlichen Modellierung wurde eine portugiesische Fassung für den juristischen Zielkontext vorbereitet.

### Erreichte Ergebnisse

- Inhalte wurden nicht nur übersetzt, sondern für einen **juristischen Fachbereich ohne technischen Tiefgang** aufbereitet.
- Fachbegriffe wurden erläutert oder vereinfacht formuliert.
- Ziel war eine vollständige, verständliche Darstellung des Produkts und der bereits festgelegten Verfahren.

### Bedeutung

Das war wichtig für die spätere Produktvorstellung im Kanzleiumfeld und zeigt, dass Legalis von Anfang an nicht nur technisch, sondern auch kommunikativ und vertrieblich gedacht wurde.

---

## 20.03.2026 – Deployment- und Lizenzstrategie

Am Folgetag wurden die betrieblichen und technischen Rahmenbedingungen vertieft.

### Erreichte Ergebnisse

- Vergleich und Einordnung von **Docker**, **Podman**, **LXC** und **Kubernetes** als potenzielle Betriebsmodelle
- Herausarbeitung eines pragmatischen Wegs für kleine bis mittlere Kanzleien statt unnötiger Plattformkomplexität
- Diskussion, ob Legalis eher als Containerlösung, als Dienst oder als appliance-nahe Auslieferung gedacht werden sollte
- Prüfung von Lizenz- und Nutzungsfragen im kommerziellen Einsatz der ausgewählten Technologien

### Ergänzende Entscheidungen

- Aufnahme einer **Lizenz-Matrix** in die Dokumentation
- Überlegung, das Dateisystem bzw. Dokumentenstorage früh mit **LVM-Wachstumspfad** zu planen, weil gescannte Dokumente und Akten langfristig stark anwachsen können

### Bedeutung

Dieser Tag diente der Härtung des Betriebsmodells. Es ging nicht nur darum, *wie* Legalis entwickelt wird, sondern auch, *wie* es beim Kunden rechtssicher, wartbar und wirtschaftlich betrieben werden kann.

---

## 22.03.2026 – Infrastrukturplanung für Entwicklung und Workflow-Umgebung

An diesem Tag wurde das Vorhaben von der Dokumentationsphase in die konkrete Infrastrukturplanung überführt.

### Erreichte Ergebnisse

- Festlegung, dass für Legalis mindestens zwei getrennte technische Umgebungen sinnvoll sind:
  1. **Legalis-Entwicklungsumgebung** für App- und Backend-Arbeit
  2. **Workflow-/BPMN-Umgebung** für OpenBPMN / Imixs und Prozessentwicklung
- Entscheidung, die Entwicklung in Proxmox strukturiert aufzusetzen
- Erstellung bzw. Anforderung einer präzisen Installationsanleitung für die benötigten CTs/VMs
- Entfernung nicht mehr benötigter Komponenten aus der bisherigen Umgebung, um Ressourcen für Legalis freizumachen

### Technische Richtung

- Debian als konservative, belastbare Basis
- SSH-Key-basierter Zugriff
- Remote-Entwicklung per VS Code oder vergleichbarem Setup
- getrennte Zuständigkeiten für Applikationskern und Workflow-System

### Bedeutung

Damit wechselte das Projekt von der konzeptionellen in die operative Phase: Die Entwicklungsumgebung sollte nun so aufgebaut werden, dass reale Implementierungsarbeit beginnen kann.

---

## 22.03.2026 – VM-Design, GitHub-Anbindung und Systembasis

Im weiteren Verlauf wurden Detailfragen der VM-Struktur und des Repositories bearbeitet.

### Erreichte Ergebnisse

- Diskussion und Klärung relevanter VM-Parameter wie UEFI/OVMF, EFI-Disk und geeignete Systemkonfiguration für moderne Linux-VMs
- Beginn der GitHub-Anbindung des Legalis-Repositories
- erster Push-Versuch zeigte, dass die SSH-Schlüssel-Freigabe noch nicht vollständig eingerichtet war

### Bedeutung

Auch wenn dies noch kein fachlicher Produktfortschritt war, wurde hier die Grundlage für saubere Quellcodeverwaltung und reproduzierbare Entwicklungsarbeit geschaffen.

---

## 23.03.2026 – Hardware- und Beschaffungsplanung für den Pilotbetrieb

An diesem Tag wurde die physische Infrastruktur für den späteren Kanzleibetrieb konkretisiert.

### Erreichte Ergebnisse

- Bewertung einer wirtschaftlichen Büroserver-Konfiguration für den Pilotkunden
- Diskussion von Speicherstrategie, Redundanz und Backup-Rotation
- Erstellung einer konkreten Einkaufsliste mit Ratenpreisen für verfügbare Hardware bei Miranda
- Berücksichtigung einer realistischen Budgetgrenze des Pilotumfelds

### Konkretisierte Richtung

- zwei interne HDDs im Mirror als vernünftiger Startpunkt
- externe USB-Festplatten im Wechsel als günstige Backup-Strategie
- insgesamt bewusst wirtschaftliche statt überdimensionierte Konfiguration

### Bedeutung

Diese Arbeiten waren nicht bloß Hardwareplanung, sondern Teil der Realisierungsstrategie: Legalis sollte nicht nur konzeptionell schlüssig, sondern für eine kleine Kanzlei auch finanziell erreichbar sein.

---

## 24.03.2026 – Beginn der praktischen BPMN-/Workflow-Arbeit

Mit diesem Tag begann die konkrete technische Annäherung an die Workflow-Komponente.

### Erreichte Ergebnisse

- Aufbau eines Zwei-Geräte- bzw. Zwei-Umgebungs-Setups für BPMN- und Workflow-Arbeit
- das **Model 1.0.10** ließ sich erfolgreich starten
- im Event-Editor wurde Business-Rule-Code sichtbar angezeigt, was einen Fortschritt bei Modell- und Plugin-Erkennung signalisiert
- der aktuell in der Engine laufende XML-Code wurde überprüft

### Aufgetretene Probleme

- Beim Öffnen bzw. Absenden von **Lead erfassen** trat ein neuer Fehler auf.
- Es kam erneut zu **HTTP 500**, unabhängig davon, ob das Formular leer oder ausgefüllt abgesendet wurde.
- Ein zwischenzeitlicher Diagnosefehler hing zusätzlich mit einem aktivierten Browser-VPN zusammen und konnte als Störfaktor identifiziert werden.

### Abgeleitete nächste Schritte

- minimalistischen Testprozess erstellen (`test-1.0.bpmn`)
- Start Event, einen Task und ein **Lead erfasst**-Event definieren
- Plugin im Modell registrieren
- einfache Regel in **Lead erfasst** hinterlegen
- Prozess sauber in die Engine laden
- HTTP-500-Ursache auf ein Minimalbeispiel zurückführen

### Bedeutung

Dies markiert den Übergang vom Architektur- zum Integrationsproblem: Die Modellierungsidee steht, aber die Kopplung zwischen Modell, Plugin, Event-Regel und Engine muss technisch stabilisiert werden.

---

## Gesamtbewertung des bisherigen Projektstands

### Bereits belastbar erreicht

1. **Produktidentität geklärt**  
   Legalis ist nicht mehr nur eine Idee, sondern ein standardorientiertes Produktmodell für brasilianische Kanzleien.

2. **MVP fachlich eingegrenzt**  
   Der arbeitsfähige Kern wurde definiert; spätere Module wurden priorisiert statt vorschnell in den MVP gezogen.

3. **Workflow-Strategie sauber verankert**  
   Workflow ist Kernlogik, KI nur Assistenz. BPMN wird kontrolliert und nicht beliebig freigegeben.

4. **Finanz- und Audit-Themen früh integriert**  
   Legalis wurde von Anfang an als betriebsfähiges Kanzleisystem und nicht nur als Aktenablage gedacht.

5. **Dokumentenarchitektur entschieden**  
   JSON-first, DOCX/DOTX als Templateformat, PDF als Endformat.

6. **Infrastrukturpfad vorbereitet**  
   Entwicklungs- und Workflow-Umgebungen wurden geplant und teilweise praktisch aufgebaut.

7. **Erste praktische Workflow-Tests laufen**  
   Die technische Integrationsarbeit hat begonnen; aktuelle Probleme sind nun konkret genug, um reproduzierbar bearbeitet zu werden.

---

## Offene Baustellen zum Berichtsstand

- Stabilisierung der BPMN-/Workflow-Integration mit OpenBPMN / Imixs
- sauberes Laden und Testen eines minimalen Referenzprozesses
- Definition erster Domain-Entities und Datenmodelle im Code
- Rollen- und Rechtemodell auf Implementierungsebene
- Template-Manifest- und Platzhalterkonzept in technischer Form
- Finance-Ops-Basismodell in umsetzbarer Softwarestruktur
- GitHub- und Entwicklungs-Workflow vollständig produktiv machen

---

## Fazit

Im bisherigen Verlauf wurde bereits ein erheblicher Teil der **produktstrategischen Vorarbeit** geleistet. Besonders positiv ist, dass die Arbeit nicht in unscharfer Ideensammlung stecken geblieben ist, sondern früh in verbindliche Entscheidungen überführt wurde: Produktphilosophie, Modulstruktur, Governance, Dokumentenarchitektur, Finanzsicht, Rollen- und Auditdenken, Infrastruktur und Workflow-Strategie sind bereits klar umrissen.

Der aktuelle Schwerpunkt verschiebt sich nun sichtbar von der **Konzeptionsphase** in die **technische Verprobung**. Der wichtigste nächste Meilenstein ist daher nicht mehr ein weiteres Grundsatzpapier, sondern ein **lauffähiger Minimalprozess** in der Workflow-Engine, an dem sich die Architektur praktisch beweisen muss.
