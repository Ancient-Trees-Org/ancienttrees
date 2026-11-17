# Instant reader judge: Hidde's one-time setup (about 5 minutes)

What it does: when a reader sends a tree or shares a photo, Supabase tells GitHub, and the Reader judge workflow puts it live in about 20 to 30 minutes. Until you do these three steps, nothing changes: the two-hourly knock still picks readers' trees up, now with their photos on the machine.

## 1. A GitHub token that may only start workflows (GitHub, 2 minutes)

1. github.com, signed in as burgmanshidde-ancienttrees. Click your avatar (top right), then **Settings**.
2. Bottom of the left column: **Developer settings**, then **Personal access tokens**, then **Fine-grained tokens**, then **Generate new token**.
3. Token name: `reader-judge`. Expiration: **Custom**, one year from today (GitHub's maximum).
4. Repository access: **Only select repositories**, pick **ancienttrees**.
5. Permissions, Repository permissions: **Contents: Read and write**. Leave everything else on No access.
6. **Generate token**, then copy it (it starts with `github_pat_`). You see it only once.

## 2. Store it in Supabase's Vault (Supabase, 1 minute)

1. supabase.com, open the Ancient Trees project.
2. Left menu: **Integrations**, then **Vault** (in older menus: Project Settings, then Vault). Enable it if it asks.
3. **Add new secret**. Name: `github_dispatch_token` (exactly this). Secret: paste the token. Save.

## 3. Paste the trigger (Supabase, 1 minute)

1. Left menu: **SQL Editor**, **New query**.
2. Paste the whole of `supabase/reader-judge-trigger.sql` and press **Run**. It should say "Success. No rows returned".

## Then

Tell me it's done. I start the workflow once by hand to check it runs, and the first real tree a reader sends shows up in GitHub's Actions tab as "Reader judge" within a few seconds.

The token expires in a year (2027-11). The trigger then simply stops pinging and the knock takes over again; a new token in the same Vault slot brings it back.
