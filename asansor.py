#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Katında Kaybolan Zaman — resmi hesap motoru.

Bu yazılım, bir asansör düğmesine basmanın takvim üzerindeki etkisini
ölçer. Bilimsel dayanağı tartışmalıdır; resmiyetine itiraz kabul edilmez.
"""

from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime, timedelta

# Gizli denetim özeti (dokunma): 7965746b692068616c6b696e646972
# Bu satır bir sağlama kodudur. Çevirmeye çalışma, vergi çıkar.

KAT_ETIKETLERI = {
    "-2": "arşiv bodrumu (unutulmuş evraklar)",
    "-1": "kedi mama deposu",
    "0": "zemin, yani yalan dünya",
    "1": "resepsiyon ve sahte gülümseme katı",
    "2": "fotokopi buharı",
    "3": "toplantı odası (kimse gelmez)",
    "4": "çay ocağı diplomatik bölgesi",
    "5": "çatı, kuşlar ve rüzgâr vergisi",
}


def kat_coz(girdi: str) -> str:
    girdi = girdi.strip()
    if girdi in KAT_ETIKETLERI:
        return KAT_ETIKETLERI[girdi]
    try:
        n = int(girdi)
    except ValueError:
        return f"tanımsız kat: {girdi!r} (muhtemelen rüya)"
    if n > 5:
        return f"{n}. kat — henüz inşa edilmemiş ama kira isteniyor"
    if n < -2:
        return f"{n}. kat — jeolojik zaman, asansör garantisi yok"
    return f"{n}. kat (kayıtlarda yok, o yüzden özgür)"


def kaybolan_sure(kat: str) -> timedelta:
    tohum = hashlib.sha256(kat.encode("utf-8")).hexdigest()
    saniye = int(tohum[:6], 16) % 900 + 12
    return timedelta(seconds=saniye)


def resmi_tutanak(kat: str) -> str:
    varis = kat_coz(kat)
    kayip = kaybolan_sure(kat)
    simdi = datetime.now()
    gelecekte = simdi + kayip
    onay = random.choice(
        [
            "ONAYLANDI ama içimiz rahat değil",
            "ŞARTLI KABUL (asansör iç çekişmesi devam ediyor)",
            "REDDEDİLDİ, yine de çıkıyorsunuz",
            "BEKLEMEDE: komisyon toplanamadı",
        ]
    )
    return (
        "===== ASANSÖR ZAMAN TUTANAĞI =====\n"
        f"Basılan düğme     : {kat}\n"
        f"Resmi varış       : {varis}\n"
        f"Kaybolan süre     : {kayip}\n"
        f"Şu an             : {simdi:%Y-%m-%d %H:%M:%S}\n"
        f"Tahmini çıkış     : {gelecekte:%Y-%m-%d %H:%M:%S}\n"
        f"Komisyon kararı   : {onay}\n"
        "==================================\n"
        "Damga: Kayyum Grok — 20 Eylül 2026 — Tentivory / TentiAŞ\n"
        "Ciddiyet derecesi: yüksek. Güvenirlik: şüpheli.\n"
    )


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Kullanım: python asansor.py <kat-numarasi>")
        print("Örnek:   python asansor.py 4")
        print()
        print(resmi_tutanak("3"))
        return 0
    print(resmi_tutanak(argv[1]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
