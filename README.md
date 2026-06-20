# 💕 Supporter Role Bot

Discord bot pro automatické přidávání Supporter role přes tlačítko.

## Soubory v repozitáři
- `supporter_bot.py` — hlavní kód bota
- `requirements.txt` — závislosti
- `Procfile` — start příkaz pro Railway
- `nixpacks.toml` — konfigurace buildu
- `.gitignore` — ignoruje .env soubor

## Nastavení na Railway

1. Nahraj všechny soubory na GitHub
2. Připoj repozitář na Railway.app
3. V Railway → Variables přidej:
   - `BOT_TOKEN` = tvůj Discord bot token
4. Deploy se spustí automaticky

## Nastavení obrázku

V `supporter_bot.py` nahraď `OBRAZEK_URL` přímým odkazem na obrázek (např. z imgur.com).

## Oprávnění bota na Discord Developer Portal

- Zapni: `Server Members Intent` + `Message Content Intent`
- Bot musí mít právo `Manage Roles`
- Role bota musí být výš než role Supporter
