import frappe
from frappe import _
from frappe.model.document import Document


class OtomatikKontakBasmaTakipKaydi(Document):
    def validate(self):
        if self.adet is not None and self.adet < 0:
            frappe.throw(_("Adet negatif olamaz."))

        if self.basilan_baski_sayisi is not None and self.basilan_baski_sayisi < 0:
            frappe.throw(_("Basılan baskı sayısı negatif olamaz."))
