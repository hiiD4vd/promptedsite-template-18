import { useEffect, useState } from "react";
import { createPortal } from "react-dom";
import locations from "../data/locations.json";
export function LocationPopovers() {
  const [active, setActive] = useState<number | null>(null);
  const [targets, setTargets] = useState<HTMLElement[]>([]);
  useEffect(() => {
    const parents = [
      ...document.querySelectorAll<HTMLElement>(".map-marker__inner"),
    ];
    setTargets(parents);
    const listeners = parents.map((p, i) => {
      const b = p.querySelector("button")!;
      b.setAttribute("aria-label", locations[i]?.title || "Location");
      const click = () => setActive((a) => (a === i ? null : i));
      b.addEventListener("click", click);
      return () => b.removeEventListener("click", click);
    });
    const escape = (e: KeyboardEvent) => {
      if (e.key === "Escape") setActive(null);
    };
    window.addEventListener("keydown", escape);
    return () => {
      listeners.forEach((fn) => fn());
      window.removeEventListener("keydown", escape);
    };
  }, []);
  useEffect(() => {
    targets.forEach((p, i) => {
      const b = p.querySelector("button")!;
      b.classList.toggle("is-open", i === active);
      b.setAttribute("aria-expanded", String(i === active));
    });
  }, [active, targets]);
  return active === null || !targets[active]
    ? null
    : createPortal(
        <div
          className="map-marker__popover"
          role="dialog"
          aria-label={locations[active].title}
          data-v-98117538=""
        >
          <div className="map-marker__popover__title">
            {locations[active].title}
          </div>
          <table className="map-marker__popover__table">
            <tbody>
              {locations[active].data.tbody.map((row) => (
                <tr key={row._uid}>
                  {row.body.map((cell) => (
                    <td key={cell._uid}>{cell.value}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>,
        targets[active],
      );
}
