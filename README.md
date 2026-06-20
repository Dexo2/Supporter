# 💕 Supporter Role Bot

Discord bot pro automatické přidávání Supporter role přes tlačítko.

## Nastavení

1. **Nainstaluj závislosti**
   ```
   pip install -r requirements.txt
   ```

2. **Vytvoř `.env` soubor** (podle `.env.example`)
   ```
   BOT_TOKEN=tvuj_token_zde
   ```

3. **Nahraj obrázek** na [imgur.com](https://imgur.com) a vlož URL do `OBRAZEK_URL` v `supporter_bot.py`

4. **Zapni intenty** na Discord Developer Portal → Bot:
   - ✅ Server Members Intent
   - ✅ Message Content Intent

5. **Spusť bota**
   ```
   python supporter_bot.py
   ```

## Oprávnění bota
- `Manage Roles` — pro přidávání rolí
- `Send Messages` — pro odeslání embedu
- `View Channels` — pro přístup ke kanálu

> ⚠️ Role bota musí být v hierarchii **výš** než role Supporter!
