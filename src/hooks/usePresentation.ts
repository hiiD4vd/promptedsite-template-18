import { mediaUrl } from "../config/media";
import { useEffect } from "react";
import { Rive, RuntimeLoader } from "@rive-app/canvas";
import lottie from "lottie-web/build/player/lottie_light";
RuntimeLoader.setWasmUrl("/rive/rive.wasm");
const riveEnabled = import.meta.env.VITE_MCP_PREVIEW !== "1";
export function usePresentation(started: boolean) {
  useEffect(() => {
    const instances: Rive[] = [];
    let stepper: Rive | undefined;
    const animations: ReturnType<typeof lottie.loadAnimation>[] = [];
    const attach = (
      canvas: HTMLCanvasElement,
      artboard: string,
      stateMachines = "State Machine 1",
      text?: string,
    ) => {
      const r = new Rive({
        src: mediaUrl("/rive/rive.riv"),
        canvas,
        artboard,
        stateMachines,
        autoplay: true,
        autoBind: !artboard.includes("loader") && !artboard.includes("contact"),
        onLoad: () => {
          r.resizeDrawingSurfaceToCanvas();
          if (artboard === "sound_animation_reworked") {
            const sound = r.viewModelInstance?.boolean("isAudioEnabled");
            if (sound) sound.value = true;
          }
          if (artboard === "stepper_animation_reworked") {
            const id = r.viewModelInstance?.number("id");
            let previous = id?.value ?? 0;
            id?.on(() => {
              const selected = id.value;
              const clicked = previous === -1 && selected >= 0;
              previous = selected;
              if (clicked) {
                const section = document.querySelector<HTMLElement>(
                  ".section-process__scroll-offset",
                )!;
                scrollTo({
                  top:
                    section.getBoundingClientRect().top +
                    scrollY -
                    innerHeight * 0.2 +
                    (section.offsetHeight - innerHeight * 0.8) *
                      [0.215, 0.4, 0.58, 0.85][selected],
                  behavior: "smooth",
                });
              }
            });
          }
          if (text) {
            const value = r.viewModelInstance?.string("text");
            if (value) value.value = text;
          }
          if (artboard === "loader_animation") {
            const input = r
              .stateMachineInputs("Loader02")
              .find((v) => v.name === "CheckLoad");
            if (input) input.value = true;
          }
        },
      });
      instances.push(r);
      if (artboard === "stepper_animation_reworked") stepper = r;
      return r;
    };
    if (riveEnabled) {
      document
        .querySelectorAll<HTMLCanvasElement>(".the-nav__item__rive")
        .forEach((canvas) => {
          const a = canvas.closest("a");
          const mobile = !!canvas.closest(".the-header-mobile");
          attach(
            canvas,
            a?.classList.contains("--email")
              ? "contact_animation" + (mobile ? "_mobile" : "")
              : "menu_animation" + (mobile ? "_mobile" : ""),
            "State Machine 1",
            a?.textContent?.trim(),
          );
        });
      document
        .querySelectorAll<HTMLCanvasElement>(".the-sound-switcher__rive")
        .forEach((c) => attach(c, "sound_animation_reworked"));
    }
    const step = document.querySelector<HTMLCanvasElement>(".stepper__rive");
    if (riveEnabled && step)
      attach(step, "stepper_animation_reworked", "State Machine");
    document
      .querySelectorAll<HTMLElement>(".decoration-bubble__inner")
      .forEach((container, i) => {
        const a = lottie.loadAnimation({
          container,
          renderer: "svg",
          path: mediaUrl(`/lottie/bubble0${i + 1}.json`),
          autoplay: !matchMedia("(prefers-reduced-motion: reduce)").matches,
          loop: true,
        });
        a.setSpeed(0.33);
        animations.push(a);
      });
    const progress = (event: Event) => {
      const value = (event as CustomEvent<number>).detail;
      const step = stepper;
      const id = step?.viewModelInstance?.number("id");
      if (id && id.value !== -1) {
        const next = value < 0.22 ? 0 : value < 0.42 ? 1 : value < 0.62 ? 2 : 3;
        if (id.value !== next) id.value = next;
      }
    };
    window.addEventListener("cosmic-progress", progress);
    document.querySelectorAll<HTMLElement>('.map__stars').forEach((container,index)=>{const animation=lottie.loadAnimation({container,renderer:'svg',path:mediaUrl(`/lottie/${index===0?'northern':'southern'}.json`),autoplay:!matchMedia('(prefers-reduced-motion: reduce)').matches,loop:true});animations.push(animation)});
    const resize = () =>
      instances.forEach((r) => r.resizeDrawingSurfaceToCanvas());
    window.addEventListener("resize", resize);
    return () => {
      window.removeEventListener("cosmic-progress", progress);
      window.removeEventListener("resize", resize);
      instances.forEach((r) => r.cleanup());
      animations.forEach((a) => a.destroy());
      document
        .querySelectorAll(
          ".the-header-desktop__logo__inner canvas,.the-header-mobile__logo__inner canvas",
        )
        .forEach((c) => c.remove());
    };
  }, []);
  useEffect(() => {
    if (!started) return;
    const ambient = new Audio(mediaUrl("/sounds/ambient.mp3"));
    ambient.loop = true;
    ambient.volume = 0.25;
    void ambient.play().catch(() => {});
    const buttons = [
      ...document.querySelectorAll<HTMLButtonElement>(
        ".the-sound-switcher,.the-sound-switcher-mobile",
      ),
    ];
    const toggle = () => {
      ambient.muted = !ambient.muted;
      buttons.forEach((b) => {
        b.setAttribute(
          "aria-label",
          ambient.muted ? "Enable sound" : "Mute sound",
        );
        b.setAttribute("aria-pressed", String(!ambient.muted));
      });
    };
    buttons.forEach((b) => {
      b.setAttribute("aria-label", "Mute sound");
      b.addEventListener("click", toggle);
    });
    return () => {
      ambient.pause();
      buttons.forEach((b) => b.removeEventListener("click", toggle));
    };
  }, [started]);
}
