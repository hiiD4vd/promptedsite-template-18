import { Preloader } from "./components/Preloader";
import { LocationPopovers } from "./components/LocationPopovers";
import { useMobileMenu } from "./hooks/useMobileMenu";
import { usePresentation } from "./hooks/usePresentation";
import { useEffect, useRef, useState } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { CosmicEngine } from "./scene/engine";
import { state } from "./scene/runtime";
import { Header } from "./components/Header";
import { Hero } from "./components/Hero";
import { Process } from "./components/Process";
import { Locations } from "./components/Locations";
import { Contacts } from "./components/Contacts";
import "./styles/index.css";
gsap.registerPlugin(ScrollTrigger);
export default function App() {
  const canvas = useRef<HTMLCanvasElement>(null);
  const engine = useRef<CosmicEngine | null>(null);
  const [error, setError] = useState("");
  const [ready, setReady] = useState(false);
  const [started, setStarted] = useState(false);
  const [slide, setSlide] = useState(0);
  const [scene, setScene] = useState("hero");
  usePresentation(started);
  useMobileMenu();
  useEffect(() => {
    const failure = () =>
      setError("A 3D asset could not load. Reload to retry.");
    window.addEventListener("cosmic-asset-error", failure);
    try {
      engine.current = new CosmicEngine(canvas.current);
    } catch (e) {
      setError(String(e));
    }
    document.querySelector<HTMLElement>(".stepper")!.style.visibility =
      "hidden";
    document.body.classList.add("__body");
    document.body.style.backgroundColor = "var(--color-primary)";
    const buttons =
      document.querySelectorAll<HTMLButtonElement>(".button-controls");
    const previous = () => setSlide((i) => (i + 2) % 3);
    const next = () => setSlide((i) => (i + 1) % 3);
    buttons[0]?.addEventListener("click", previous);
    buttons[1]?.addEventListener("click", next);
    const deadline = setTimeout(
      () =>
        setError("The experience is taking too long to load. Reload to retry."),
      45000,
    );
    const timer = setInterval(() => {
      if (state.isThreeSliderLoaded && state.isThreeScrollLoaded) {
        setReady(true);
        clearTimeout(deadline);
        clearInterval(timer);
      }
    }, 100);
    const scroll = ScrollTrigger.create({
      trigger: ".section-process__scroll-offset",
      start: "top 20%",
      end: "bottom bottom",
      onUpdate: ({ progress }) => {
        engine.current?.updateOnScroll(progress);
        document.body.style.backgroundColor =
          progress > 0 ? "var(--color-red)" : "var(--color-primary)";
        document.body.classList.toggle("is-scrolled", progress > 0);
        window.dispatchEvent(
          new CustomEvent("cosmic-progress", { detail: progress }),
        );
        if (progress > 0) {
          engine.current?.switchToScrollScene();
          setScene(progress >= 1 ? "location" : "process");
          document.querySelector<HTMLElement>(".stepper")!.style.visibility =
            progress >= 1 ? "hidden" : "visible";
        } else {
          engine.current?.switchToSliderScene();
          setScene("hero");
          document.querySelector<HTMLElement>(".stepper")!.style.visibility =
            "hidden";
        }
      },
    });
    return () => {
      clearTimeout(deadline);
      clearInterval(timer);
      window.removeEventListener("cosmic-asset-error", failure);
      buttons[0]?.removeEventListener("click", previous);
      buttons[1]?.removeEventListener("click", next);
      scroll.kill();
      engine.current?.destroy();
    };
  }, []);
  useEffect(() => {
    if (!started) return;
    engine.current?.world?.slider.slide(slide, state.sliderActiveIndex, 1);
    state.sliderActiveIndex = slide;
    document.querySelectorAll(".swiper-slide").forEach((e, i) => {
      Object.assign((e as HTMLElement).style, {
        opacity: i === slide ? "1" : "0",
        visibility: i === slide ? "visible" : "hidden",
        position: i === slide ? "relative" : "absolute",
        top: "0",
        left: "0",
        width: "100%",
      });
    });
    document
      .querySelectorAll<HTMLElement>(".section-hero__inner > .decoration")
      .forEach((e, i) => {
        e.style.opacity = i % 3 === slide ? "1" : "0";
        e.querySelectorAll<HTMLElement>(".decoration-bubble,.star").forEach(
          (child) => {
            child.style.opacity = "1";
            child.style.transform = "scale(1)";
          },
        );
      });
    document
      .querySelectorAll(".hero-slider-progress-item")
      .forEach((e, i) => e.classList.toggle("is-active", i === slide));
  }, [slide, started]);
  useEffect(() => {
    if (
      !started ||
      matchMedia("(prefers-reduced-motion: reduce)").matches ||
      new URLSearchParams(location.search).get("autoplay") === "0"
    )
      return;
    const timer = setInterval(() => {
      if (scrollY < innerHeight * 0.5) setSlide((i) => (i + 1) % 3);
    }, 5000);
    return () => clearInterval(timer);
  }, [started]);
  return (
    <>
      <Header />
      <main>
        <Hero />
        <Process />
        <Locations />
        <LocationPopovers />
        <Contacts />
      </main>
      <div
        className={`canvas is-view-${scene}`}
        data-v-cf2d6355=""
        style={{
          position: "fixed",
          inset: 0,
          pointerEvents: "none",
          zIndex: 0,
          visibility: scene === "location" ? "hidden" : "visible",
          transform: "none",
          top: scene === "hero" ? "5vh" : "0",
        }}
      >
        <canvas ref={canvas} data-v-cf2d6355="" />
        <div
          className={`canvas__ellipse --color-${slide}`}
          data-v-cf2d6355=""
        />
        <div className="canvas__ellipse-border --left" data-v-cf2d6355="" />
        <div className="canvas__ellipse-border --right" data-v-cf2d6355="" />
      </div>
      {!started ? (
        <Preloader
          ready={ready}
          error={error}
          onStart={() => {
            if (error) {
              location.reload();
              return;
            }
            state.sliderActiveIndex = -1;
            setStarted(true);
          }}
        />
      ) : (
        <nav aria-label="Product slider" style={{ display: "none" }}>
          <button
            onClick={() => setSlide((slide + 2) % 3)}
            aria-label="Previous product"
          >
            ←
          </button>
          <button
            onClick={() => setSlide((slide + 1) % 3)}
            aria-label="Next product"
          >
            →
          </button>
        </nav>
      )}
    </>
  );
}
