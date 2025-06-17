"""
Lux_MySQLBackup

Copyright (c) 2025 LuxCoding

This script is licensed under the MIT License.
For full details, see the LICENSE file in the repository.
"""
# Import required Libs
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry
import json
import os
import base64
import ctypes
from ctypes import wintypes
from datetime import datetime, timedelta
import caldav

# Tranlations
translations = {
    "Deutsch": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Hauptfunktion",
        "settings_tab": "Einstellungen",
        "start_date": "Startdatum:",
        "end_date": "Zieldatum:",
        "move_events": "Termine verschieben",
        "save_settings": "Einstellungen speichern",
        "saved": "Gespeichert",
        "settings_saved": "Einstellungen wurden gespeichert. Bitte App neu starten.",
        "error": "Fehler",
        "no_calendar": "Kein Kalender gefunden.",
        "success": "Erfolg",
        "events_moved": "{} Termine verschoben.",
        "missing_dates": "Beide Daten müssen gesetzt sein.",
        "username": "Benutzername:",
        "password": "Passwort:",
        "url": "CalDAV-URL:",
        "language": "Sprache:"
    },
    "English": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Main",
        "settings_tab": "Settings",
        "start_date": "Start Date:",
        "end_date": "Target Date:",
        "move_events": "Shift Events",
        "save_settings": "Save Settings",
        "saved": "Saved",
        "settings_saved": "Settings have been saved. Please restart the App ",
        "error": "Error",
        "no_calendar": "No calendar found.",
        "success": "Success",
        "events_moved": "{} events shifted.",
        "missing_dates": "Both dates must be set.",
        "username": "Username:",
        "password": "Password:",
        "url": "CalDAV URL:",
        "language": "Language:"
    },
    "Español": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Principal",
        "settings_tab": "Configuración",
        "start_date": "Fecha de inicio:",
        "end_date": "Fecha objetivo:",
        "move_events": "Mover eventos",
        "save_settings": "Guardar configuración",
        "saved": "Guardado",
        "settings_saved": "Configuración guardada. Reinicie la aplicación.",
        "error": "Error",
        "no_calendar": "No se encontró calendario.",
        "success": "Éxito",
        "events_moved": "{} eventos movidos.",
        "missing_dates": "Ambas fechas deben establecerse.",
        "username": "Nombre de usuario:",
        "password": "Contraseña:",
        "url": "URL de CalDAV:",
        "language": "Idioma:"
    },
    "Français": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Principal",
        "settings_tab": "Paramètres",
        "start_date": "Date de début :",
        "end_date": "Date cible :",
        "move_events": "Déplacer les événements",
        "save_settings": "Enregistrer les paramètres",
        "saved": "Enregistré",
        "settings_saved": "Paramètres enregistrés. Veuillez redémarrer l'application.",
        "error": "Erreur",
        "no_calendar": "Aucun calendrier trouvé.",
        "success": "Succès",
        "events_moved": "{} événements déplacés.",
        "missing_dates": "Les deux dates doivent être définies.",
        "username": "Nom d'utilisateur :",
        "password": "Mot de passe :",
        "url": "URL CalDAV :",
        "language": "Langue :"
    },
    "Italiano": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Principale",
        "settings_tab": "Impostazioni",
        "start_date": "Data d'inizio:",
        "end_date": "Data di destinazione:",
        "move_events": "Sposta eventi",
        "save_settings": "Salva impostazioni",
        "saved": "Salvato",
        "settings_saved": "Impostazioni salvate. Riavvia l'app.",
        "error": "Errore",
        "no_calendar": "Nessun calendario trovato.",
        "success": "Successo",
        "events_moved": "{} eventi spostati.",
        "missing_dates": "Entrambe le date devono essere impostate.",
        "username": "Nome utente:",
        "password": "Password:",
        "url": "URL CalDAV:",
        "language": "Lingua:"
    },
    "Português": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Principal",
        "settings_tab": "Configurações",
        "start_date": "Data de início:",
        "end_date": "Data-alvo:",
        "move_events": "Mover eventos",
        "save_settings": "Salvar configurações",
        "saved": "Salvo",
        "settings_saved": "Configurações salvas. Reinicie o aplicativo.",
        "error": "Erro",
        "no_calendar": "Nenhum calendário encontrado.",
        "success": "Sucesso",
        "events_moved": "{} eventos movidos.",
        "missing_dates": "Ambas as datas devem ser definidas.",
        "username": "Nome de usuário:",
        "password": "Senha:",
        "url": "URL do CalDAV:",
        "language": "Idioma:"
    },
    "中文": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "主功能",
        "settings_tab": "设置",
        "start_date": "开始日期：",
        "end_date": "目标日期：",
        "move_events": "移动事件",
        "save_settings": "保存设置",
        "saved": "已保存",
        "settings_saved": "设置已保存。请重新启动应用程序。",
        "error": "错误",
        "no_calendar": "未找到日历。",
        "success": "成功",
        "events_moved": "已移动 {} 个事件。",
        "missing_dates": "必须设置两个日期。",
        "username": "用户名：",
        "password": "密码：",
        "url": "CalDAV 地址：",
        "language": "语言："
    },
    "Русский": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Главная",
        "settings_tab": "Настройки",
        "start_date": "Дата начала:",
        "end_date": "Целевая дата:",
        "move_events": "Переместить события",
        "save_settings": "Сохранить настройки",
        "saved": "Сохранено",
        "settings_saved": "Настройки сохранены. Перезапустите приложение.",
        "error": "Ошибка",
        "no_calendar": "Календарь не найден.",
        "success": "Успешно",
        "events_moved": "Перемещено {} событий.",
        "missing_dates": "Обе даты должны быть установлены.",
        "username": "Имя пользователя:",
        "password": "Пароль:",
        "url": "CalDAV URL:",
        "language": "Язык:"
    },
    "Türkçe": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Ana Sayfa",
        "settings_tab": "Ayarlar",
        "start_date": "Başlangıç Tarihi:",
        "end_date": "Hedef Tarih:",
        "move_events": "Etkinlikleri Taşı",
        "save_settings": "Ayarları Kaydet",
        "saved": "Kaydedildi",
        "settings_saved": "Ayarlar kaydedildi. Uygulamayı yeniden başlatın.",
        "error": "Hata",
        "no_calendar": "Takvim bulunamadı.",
        "success": "Başarılı",
        "events_moved": "{} etkinlik taşındı.",
        "missing_dates": "Her iki tarih de ayarlanmalıdır.",
        "username": "Kullanıcı adı:",
        "password": "Şifre:",
        "url": "CalDAV URL’si:",
        "language": "Dil:"
    },
    "Nederlands": {
        "app_title": "Lux_Rescheduler",
        "main_tab": "Hoofdfunctie",
        "settings_tab": "Instellingen",
        "start_date": "Startdatum:",
        "end_date": "Doeldatum:",
        "move_events": "Evenementen verplaatsen",
        "save_settings": "Instellingen opslaan",
        "saved": "Opgeslagen",
        "settings_saved": "Instellingen opgeslagen. Start de app opnieuw.",
        "error": "Fout",
        "no_calendar": "Geen kalender gevonden.",
        "success": "Succes",
        "events_moved": "{} evenementen verplaatst.",
        "missing_dates": "Beide datums moeten ingesteld zijn.",
        "username": "Gebruikersnaam:",
        "password": "Wachtwoord:",
        "url": "CalDAV-URL:",
        "language": "Taal:"
    }
}

# Struckture for DATA_BLOB
class DATA_BLOB(ctypes.Structure):
    _fields_ = [("cbData", wintypes.DWORD), ("pbData", ctypes.POINTER(ctypes.c_byte))]

# Funcstion helps to create DATA_BLOP ot of Bytes
def _blob(data):
    blob = DATA_BLOB()
    blob.cbData = len(data)
    blob.pbData = ctypes.cast(ctypes.create_string_buffer(data), ctypes.POINTER(ctypes.c_byte))
    return blob

# Function to Encryt Data with DAPAPI and returns Base64-coded Data
def encrypt(data):
    data_blob_in = _blob(data.encode('utf-8'))
    data_blob_out = DATA_BLOB()
    if ctypes.windll.crypt32.CryptProtectData(
        ctypes.byref(data_blob_in), None, None, None, None, 0, ctypes.byref(data_blob_out)
    ):
        # Convert data in Base64 and return them
        encrypted_data = ctypes.string_at(data_blob_out.pbData, data_blob_out.cbData)
        ctypes.windll.kernel32.LocalFree(data_blob_out.pbData)
        return base64.b64encode(encrypted_data).decode('utf-8')
    else:
        raise ctypes.WinError()

# Funcstion to Decrypt Base64-coded Data with DAPAPI
def decrypt(encrypted_data):
    try:
        data_blob_in = _blob(base64.b64decode(encrypted_data))
        data_blob_out = DATA_BLOB()
        if ctypes.windll.crypt32.CryptUnprotectData(
            ctypes.byref(data_blob_in), None, None, None, None, 0, ctypes.byref(data_blob_out)
        ):
            # reutrn Decrypted data
            decrypted_data = ctypes.string_at(data_blob_out.pbData, data_blob_out.cbData)
            ctypes.windll.kernel32.LocalFree(data_blob_out.pbData)
            return decrypted_data.decode('utf-8')
    except:
        return ""

# Settings Variable
default_settings = {"url": "", "username": "", "password": "", "language": "English"}

# Function to Load Settings from json
def load_settings():
    if os.path.exists("settings.json"):
        with open("settings.json", "r") as f:
            raw = json.load(f)
            raw["username"] = decrypt(raw.get("username", ""))
            raw["password"] = decrypt(raw.get("password", ""))
            return {**default_settings, **raw}
    return default_settings

# Function to Save Settings to json
def save_settings(data):
    safe_data = {
        "url": data.get("url", ""),
        "username": encrypt(data.get("username", "")),
        "password": encrypt(data.get("password", "")),
        "language": data.get("language", "English")
    }
    with open("settings.json", "w") as f:
        json.dump(safe_data, f, indent=4)

# Function to Shift Events
def shift_events(start_date, end_date, settings, progress_callback=None, update_ui_callback=None):
    try:
        # Format Dates
        source_date = datetime.strptime(start_date, "%Y-%m-%d")
        target_date = datetime.strptime(end_date, "%Y-%m-%d")
        date_diff = target_date - source_date

        # Creates Calldav Client and Connects
        client = caldav.DAVClient(
            url=settings["url"],
            username=settings["username"],
            password=settings["password"]
        )
        principal = client.principal()
        calendars = principal.calendars()
        if not calendars:
            messagebox.showerror(t["error"], t["no_calendar"])
            return

        calendar = calendars[0]
        events = calendar.date_search(start=source_date, end=source_date + timedelta(days=1))
        total = len(events)

        # Loop for every event von selected date
        for idx, event in enumerate(events):
            vevent = event.vobject_instance.vevent
            if hasattr(vevent, "dtstart") and hasattr(vevent, "dtend"):
                start_old = vevent.dtstart.value
                end_old = vevent.dtend.value
                start_new = start_old + date_diff
                end_new = end_old + date_diff

                vevent.dtstart.value = start_new
                vevent.dtend.value = end_new
                event.vobject_instance.vevent = vevent
                event.save()

            if progress_callback:
                progress = (idx + 1) / total
                progress_callback(progress)

            if update_ui_callback:
                update_ui_callback()

        messagebox.showinfo(t["success"], t["events_moved"].format(total))
    except Exception as e:
        messagebox.showerror(t["error"], str(e))

# === GUI ===
class CalDAVApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.settings = load_settings()
        self.language = self.settings.get("language", "English")
        global t
        t = translations[self.language]

        self.title(t["app_title"])
        self.geometry("500x450")
        self.resizable(False, False)
        self.progress_value = 0.0

        self.tabview = ctk.CTkTabview(self, width=480)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)

        self.main_tab = self.tabview.add(t["main_tab"])
        self.settings_tab = self.tabview.add(t["settings_tab"])

        self.build_main_tab()
        self.build_settings_tab()

    def animate_progress(self, target_value):
        current = self.progress_value
        steps = 10
        delta = (target_value - current) / steps

        for _ in range(steps):
            current += delta
            self.progressbar.set(current)
            self.update_idletasks()
            self.after(10)

        self.progress_value = target_value

    def build_main_tab(self):
        ctk.CTkLabel(self.main_tab, text=t["start_date"]).pack(pady=(20, 0))
        self.start_date = DateEntry(self.main_tab, date_pattern="yyyy-mm-dd")
        self.start_date.pack(pady=5)

        ctk.CTkLabel(self.main_tab, text=t["end_date"]).pack(pady=(20, 0))
        self.end_date = DateEntry(self.main_tab, date_pattern="yyyy-mm-dd")
        self.end_date.pack(pady=5)

        self.progressbar = ctk.CTkProgressBar(self.main_tab, width=300)
        self.progressbar.pack(pady=(10, 0))
        self.progressbar.set(0)

        ctk.CTkButton(self.main_tab, text=t["move_events"], command=self.run_shift).pack(pady=25)

    def build_settings_tab(self):
        ctk.CTkLabel(self.settings_tab, text=t["language"]).pack(pady=(20, 0))

        available_languages = sorted(translations.keys())
        self.language_option = ctk.CTkOptionMenu(
            self.settings_tab,
            width=200,
            values=available_languages,
            command=self.change_language
        )
        self.language_option.set(self.language)
        self.language_option.pack(pady=(0, 20))

        ctk.CTkLabel(self.settings_tab, text=t["url"]).pack(pady=(10, 0))
        self.url_entry = ctk.CTkEntry(self.settings_tab, width=400)
        self.url_entry.pack()
        self.url_entry.insert(0, self.settings.get("url", ""))

        ctk.CTkLabel(self.settings_tab, text=t["username"]).pack(pady=(20, 0))
        self.user_entry = ctk.CTkEntry(self.settings_tab, width=400)
        self.user_entry.pack()
        self.user_entry.insert(0, self.settings.get("username", ""))

        ctk.CTkLabel(self.settings_tab, text=t["password"]).pack(pady=(20, 0))
        self.pass_entry = ctk.CTkEntry(self.settings_tab, show="*", width=400)
        self.pass_entry.pack()
        self.pass_entry.insert(0, self.settings.get("password", ""))

        ctk.CTkButton(self.settings_tab, text=t["save_settings"], command=self.save_settings).pack(pady=20)

    def change_language(self, lang):
        self.settings["language"] = lang
        save_settings(self.settings)
        messagebox.showinfo(t["saved"], t["settings_saved"])

    def save_settings(self):
        self.settings["url"] = self.url_entry.get()
        self.settings["username"] = self.user_entry.get()
        self.settings["password"] = self.pass_entry.get()
        save_settings(self.settings)
        messagebox.showinfo(t["saved"], t["settings_saved"])

    def run_shift(self):
        self.progressbar.set(0)
        self.progress_value = 0.0

        start = self.start_date.get_date().strftime("%Y-%m-%d")
        end = self.end_date.get_date().strftime("%Y-%m-%d")
        if not start or not end:
            messagebox.showwarning(t["error"], t["missing_dates"])
            return

        self.progressbar.set(0)
        shift_events(
            start, end, self.settings,
            progress_callback=self.animate_progress,
            update_ui_callback=self.update_idletasks
        )

if __name__ == "__main__":
    app = CalDAVApp()
    app.mainloop()
