import { useEffect } from "react";
export function useMobileMenu() {
  useEffect(() => {
    const menu = document.querySelector<HTMLElement>(".the-header-mobile")!;
    const button = menu.querySelector<HTMLElement>(".the-hamburger")!;
    let opened = false;
    button.setAttribute("role", "button");
    button.tabIndex = 0;
    button.setAttribute("aria-label", "Open menu");
    button.setAttribute("aria-expanded", "false");
    const set = (value: boolean) => {
      opened = value;
      menu.classList.toggle("is-open", value);
      button.setAttribute("aria-expanded", String(value));
      button.setAttribute("aria-label", value ? "Close menu" : "Open menu");
      if (value) menu.querySelector<HTMLElement>("nav a")?.focus();
      else button.focus();
    };
    const click = () => set(!opened);
    const key = (e: KeyboardEvent) => {
      if (e.key === "Escape" && opened) set(false);
      if (e.target === button && (e.key === "Enter" || e.key === " ")) {
        e.preventDefault();
        click();
      }
    };
    const nav = (e: Event) => {
      if ((e.target as Element).closest("a") && opened) set(false);
    };
    button.addEventListener("click", click);
    window.addEventListener("keydown", key);
    menu.addEventListener("click", nav);
    return () => {
      button.removeEventListener("click", click);
      window.removeEventListener("keydown", key);
      menu.removeEventListener("click", nav);
    };
  }, []);
}
