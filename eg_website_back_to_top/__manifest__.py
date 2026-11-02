{
    "name": "Website Back to Top",
    "version": "1.0",
    "category": "Extra Tools, Website",
    "summary": "Website Back to Top improves website usability by reducing the effort required to navigate long product pages, blogs, catalogues, landing pages, and information sections. The responsive floating button becomes visible only after the visitor crosses the configured scrolling distance and smoothly returns the page to the top with one click. Its accessible, lightweight, mobile-friendly design improves browsing convenience while maintaining compatibility with different website themes and screen sizes Responsive One-Click Page Navigation website back to top scroll to top button floating navigation button smooth page scrolling responsive website navigation one click page navigation long page navigation mobile scroll button accessible website button website usability improvement floating arrow button return to page top responsive scroll control website navigation enhancement page scrolling utility mobile friendly navigation keyboard accessible button smooth scroll navigation ecommerce page navigation website user experience",
    "description": "Website Back to Top adds a floating navigation button that helps visitors instantly return to the beginning of long website pages. The button automatically appears after the visitor scrolls down and remains hidden when it is not required, keeping the page design clean and distraction-free. It supports smooth scrolling, responsive positioning, keyboard navigation, screen readers, mobile safe areas, and reduced-motion preferences. Administrators can enable or disable the complete feature from the centralized INKERP settings without modifying website templates or source code.",
    "author": "INKERP",
    "website": "www.inkerp.com",
    "license": "OPL-1",
    "depends": [
        "website",
    ],
    "data": [
        "views/res_config_settings_views.xml",
        "views/website_templates.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "eg_website_back_to_top/static/src/js/website_back_to_top.js",
            "eg_website_back_to_top/static/src/scss/website_back_to_top.scss"
        ]
    },
    "post_init_hook": "post_init_enable_eg_website_back_to_top",
    "images": [
        "static/description/banner.gif"
    ],
    "price": "0.0",
    "currency": "EUR",
    "installable": True,
    "application": True,
    "auto_install": False
}