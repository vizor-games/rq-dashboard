# Working with oauth2_token

## Installation of oauth2 extension:

```bash
pip install 'rq-dashboard[oauth2]'
```

## Usage of oauth2 extension

To turn on token verification you need to set OAUTH2_TOKEN_VERIFICATION_KEY in env variables
or --oauth2-token-verification-key option in cli
Our extension will validate jwt token sent in headers from some kind of oauth2 proxy
You should also set OAUTH2_TOKEN_VERIFICATION_HEADER (--oauth2-token-verification-header) containing 
name of header used to pass jwt token

## Local development

If you use oauth2_proxy+keycloak you can use oauth-docker-compose.yml and Dockerfile-oauth2 for local development
See documentation for correct keycloak setup
https://oauth2-proxy.github.io/oauth2-proxy/configuration/providers/keycloak_oidc