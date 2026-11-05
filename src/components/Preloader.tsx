import type React from "react";
export function Preloader({
  ready,
  error,
  onStart,
}: {
  ready: boolean;
  error: string;
  onStart: () => void;
}) {
  return (
    <div className={"the-preloader"} data-v-2fa055d1={""}>
      <canvas className={"the-preloader__logo"} data-v-2fa055d1={""}></canvas>
      <div className={"the-preloader__content"} data-v-2fa055d1={""}>
        <div
          className={"the-preloader__button"}
          data-sound-click={"click"}
          data-v-2fa055d1={""}
        >
          <button
            onClick={onStart}
            disabled={!ready && !error}
            type={"button"}
            className={
              "--button-reset button-main button-shadow --type-undefined"
            }
            data-v-2fa055d1={""}
            data-v-43879b2b={""}
          >
            <span data-v-43879b2b={""}>
              {error ? "Retry" : ready ? "StArt" : "Loading…"}
            </span>
          </button>
        </div>
        <p className={"the-preloader__message"} data-v-2fa055d1={""}>
          <span data-v-2fa055d1={""}>
            {error || "Immersive sound ahead. Use headphones for best effect"}
          </span>
          <svg
            xmlns={"http://www.w3.org/2000/svg"}
            xmlnsXlink={"http://www.w3.org/1999/xlink"}
            aria-hidden={"true"}
            role={"img"}
            className={"iconify iconify--custom"}
            style={{ fontSize: "2.5rem" } as React.CSSProperties}
            width={"1em"}
            height={"1em"}
            viewBox={"0 0 40 40"}
            data-v-2fa055d1={""}
          >
            <g fill={"none"}>
              <rect
                x={"1"}
                y={"6"}
                width={"38"}
                height={"28"}
                rx={"14"}
                stroke={"currentColor"}
                strokeWidth={"2"}
              ></rect>
              <path
                d={
                  "M12 20H15C16.1046 20 17 20.8954 17 22V27C17 28.1046 16.1046 29 15 29H12C10.8954 29 10 28.1046 10 27V20C10 14.4771 14.4771 10 20 10C25.5228 10 30 14.4771 30 20V27C30 28.1046 29.1046 29 28 29H25C23.8954 29 23 28.1046 23 27V22C23 20.8954 23.8954 20 25 20H28C28 15.5817 24.4183 12 20 12C15.5817 12 12 15.5817 12 20Z"
                }
                fill={"currentColor"}
              ></path>
            </g>
          </svg>
        </p>
      </div>
      <div className={"the-preloader__bg"} data-v-2fa055d1={""}></div>
    </div>
  );
}
