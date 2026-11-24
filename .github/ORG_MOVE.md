# Repo naar een GitHub-organisatie (voorbereid 2026-11-24)

Waarom: een tweede eigenaar kan alleen via een organisatie. Op een persoonlijk account kan die hoogstens schrijfrechten krijgen.

Wat er nu staat (gelezen 2026-11-24):
- `hidde-ancient-trees/ancienttrees`: public, Pages via de deploy-workflow, custom domain ancienttrees.app, omgeving `github-pages`, 25 secrets, geen webhooks en geen rulesets.
- `hidde-ancient-trees/ancienttrees-open`: Pages (legacy), domein open.ancienttrees.app.
- www.ancienttrees.app wijst nog naar `burgmanshidde-ancienttrees.github.io`, het oude account.
- De Supabase-trigger gebruikt een fine-grained token (Vault `github_dispatch_token`) die alleen voor repo's van hidde-ancient-trees geldt. **Die token werkt na de verhuizing niet meer.**
- `SELF_DISPATCH_TOKEN` doet niets (self-chaining staat uit).

## Stappen van Hidde

1. Maak een organisatie aan, ingelogd als hidde-ancient-trees:
   https://github.com/account/organizations/new?plan=free
   Naam: `ancient-trees-app`. Een andere naam mag ook; zeg welke.
2. Geef het seintje: "verhuis".

## Stappen van mij (in één sessie, ongeveer een half uur)

1. Wachten tot er geen deploy draait: `gh run list -R hidde-ancient-trees/ancienttrees -s in_progress`
2. `python3 scripts/move_to_org.py <org> --write` (7 bestanden), dan committen en pushen.
3. Beide repo's overzetten met `gh api -X POST repos/hidde-ancient-trees/<repo>/transfer -f new_owner=<org>`. Secrets, Pages, de omgeving en de issues gaan mee, en GitHub stuurt de oude URL door.
4. `git remote set-url origin https://github.com/<org>/ancienttrees.git` op de Mac.
5. De Claude GitHub-app op de organisatie installeren (jouw klik, ik geef de link).
6. Controleren dat Pages nog op ancienttrees.app en open.ancienttrees.app staat, en een deploy en een reader-judge dispatch draaien.

## Daarna, jouw klikken (ik geef de links met de waarden)

1. **Nieuwe dispatch-token**: maak een fine-grained token aan met de organisatie als resource owner, alleen voor de repo ancienttrees, met de rechten Contents en Actions op read and write. Zet hem in de Supabase Vault als `github_dispatch_token`, dan plak ik de nieuwe trigger-SQL. Tot die tijd vangt de poll elke 15 minuten het op.
2. **www bij TransIP**: zet de CNAME van `www` op `<org>.github.io.`
3. **Domein verifiëren** voor Pages op de organisatie: een TXT-record dat GitHub opgeeft bij Settings > Pages van de organisatie.
4. **De tweede eigenaar** maakt een eigen GitHub-account aan. Jij nodigt dat account uit als **Owner**: `https://github.com/orgs/<org>/people`
5. **Tweestapsverificatie verplicht** maken voor de organisatie: `https://github.com/organizations/<org>/settings/security`

## Terugdraaien

Een repo kan terug met dezelfde transfer-call naar `hidde-ancient-trees`, en de bestanden met een `git revert` van de commit uit stap 2.
