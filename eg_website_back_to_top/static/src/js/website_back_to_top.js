/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Interaction } from "@web/public/interaction";

export class WebsiteBackToTop extends Interaction {
    static selector = ".o_website_back_to_top";

    dynamicContent = {
        _root: {
            "t-on-click.prevent": this.onClick,
            "t-att-class": () => ({
                o_website_back_to_top_visible: this.isVisible,
            }),
            "t-att-aria-hidden": () => (this.isVisible ? "false" : "true"),
            "t-att-tabindex": () => (this.isVisible ? "0" : "-1"),
        },
        _window: {
            "t-on-scroll": this.onWindowScroll,
            "t-on-resize": this.onWindowResize,
        },
    };

    setup() {
        this.isVisible = false;
        this.scrollThreshold = 300;
    }

    start() {
        const configuredThreshold = Number.parseInt(
            this.el.dataset.scrollThreshold || "300",
            10
        );
        this.scrollThreshold = Number.isFinite(configuredThreshold)
            ? Math.max(0, configuredThreshold)
            : 300;
        this.updateVisibility();
        this.updateContent();
    }

    onWindowScroll() {
        this.updateVisibility();
    }

    onWindowResize() {
        this.updateVisibility();
    }

    updateVisibility() {
        this.isVisible = window.scrollY > this.scrollThreshold;
    }

    onClick() {
        const reduceMotion = window.matchMedia(
            "(prefers-reduced-motion: reduce)"
        ).matches;
        window.scrollTo({
            top: 0,
            left: 0,
            behavior: reduceMotion ? "auto" : "smooth",
        });
        this.el.blur();
    }
}

registry
    .category("public.interactions")
    .add("eg_website_back_to_top.website_back_to_top", WebsiteBackToTop);
