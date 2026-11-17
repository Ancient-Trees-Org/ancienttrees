# Optional: reader judge within seconds instead of up to 15 minutes

Not needed: reader-judge.yml already polls every 15 minutes. This makes Supabase start it at once.

1. https://github.com/settings/personal-access-tokens/new
   Name `reader-judge`, expiration one year, Only select repositories: `ancienttrees`, Repository permissions: Contents = Read and write. Generate, copy.
2. https://supabase.com/dashboard/project/caimvxiyrtifilimlkqw/integrations/vault/secrets
   Add new secret. Name `github_dispatch_token`, value: the token.
3. https://supabase.com/dashboard/project/caimvxiyrtifilimlkqw/sql/new
   Paste supabase/reader-judge-trigger.sql, Run.

The token expires in a year; the 15-minute poll keeps working without it.
