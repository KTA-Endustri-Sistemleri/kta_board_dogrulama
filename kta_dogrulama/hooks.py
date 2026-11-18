app_name = "kta_dogrulama"
app_title = "KTA Dogrulama"
app_publisher = "KTA Endüstri"
app_description = "KTA doğrulama ve üretim takip formları"
app_email = "info@kta.com.tr"
app_license = "MIT"
app_version = "1.0.0"

fixtures = [
    {
        "doctype": "Module Def",
        "filters": [["module_name", "in", ["KTA Dogrulama", "KTA Uretim Takip"]]]
    }
]

after_install = "kta_dogrulama.setup.after_install"
