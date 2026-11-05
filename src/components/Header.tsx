import { mediaUrl } from "../config/media";
import type React from "react";
export function Header() {
  return (
    <header
      className={"the-header"}
      data-allow-mismatch={""}
      style={{} as React.CSSProperties}
      data-v-4df3a5f8={""}
    >
      <div
        className={"the-header-desktop container"}
        data-v-4df3a5f8={""}
        data-v-d87ca48c={""}
      >
        <nav
          className={"the-nav the-header-desktop__nav --start"}
          data-v-d87ca48c={""}
          data-v-bacbfa46={""}
        >
          <a
            className={"the-nav__item"}
            href={"#how"}
            data-sound-hover={"hover"}
            data-sound-click={"click"}
            data-v-d87ca48c={""}
            data-v-01873299={""}
          >
            <span className={"the-nav__item__text"} data-v-01873299={""}>
              {"PrompTedSite"}
            </span>
            <canvas
              className={"the-nav__item__rive"}
              width={"200"}
              height={"100"}
              data-v-01873299={""}
            ></canvas>
          </a>
          <a
            className={"the-nav__item"}
            href={"#locations"}
            data-sound-hover={"hover"}
            data-sound-click={"click"}
            data-v-d87ca48c={""}
            data-v-01873299={""}
          >
            <span className={"the-nav__item__text"} data-v-01873299={""}>
              {"Locations"}
            </span>
            <canvas
              className={"the-nav__item__rive"}
              width={"200"}
              height={"100"}
              data-v-01873299={""}
            ></canvas>
          </a>
        </nav>
        <a
          className={"the-header-desktop__logo"}
          href={"#hero"}
          data-v-d87ca48c={""}
        >
          <span
            className={"the-header-desktop__logo__inner"}
            data-v-d87ca48c={""}
          >
            <div
              className={"the-logo"}
              data-v-d87ca48c={""}
              data-v-cfbd04aa={""}
            >
              <img
                src={mediaUrl("/images/logo.svg")}
                alt={"PrompTedSpace"}
                data-v-cfbd04aa={""}
              />
            </div>
          </span>
        </a>
        <nav
          className={"the-nav the-header-desktop__nav --end"}
          data-v-d87ca48c={""}
          data-v-bacbfa46={""}
        >
          <a
            className={"the-nav__item --email"}
            href={"mailto:contact@promptedsite.com"}
            data-sound-hover={"hover"}
            data-sound-click={"click"}
            data-v-d87ca48c={""}
            data-v-ed701962={""}
            data-v-01873299={""}
          >
            <span className={"the-nav__item__text"} data-v-01873299={""}>
              {"Contact"}
            </span>
            <canvas
              className={"the-nav__item__rive"}
              width={"200"}
              height={"100"}
              data-v-01873299={""}
            ></canvas>
          </a>
          <button
            className={"the-sound-switcher"}
            data-sound-hover={"hover"}
            data-sound-click={"click"}
            data-v-d87ca48c={""}
            data-v-ccbc99a5={""}
          >
            <span
              className={"the-sound-switcher__sizer"}
              data-v-ccbc99a5={""}
            ></span>
            <canvas
              className={"the-sound-switcher__rive"}
              width={"200"}
              height={"100"}
              data-v-ccbc99a5={""}
            ></canvas>
          </button>
        </nav>
        <div className={"the-header-desktop__bg"} data-v-d87ca48c={""}></div>
      </div>
      <div
        className={"the-header-mobile"}
        data-v-4df3a5f8={""}
        data-v-3e1a866d={""}
      >
        <div
          className={"the-header-mobile__bar container"}
          data-v-3e1a866d={""}
        >
          <a
            href={"#hero"}
            className={"the-header-mobile__logo"}
            data-sound-click={"click"}
            data-v-3e1a866d={""}
          >
            <span
              className={"the-header-mobile__logo__inner"}
              data-v-3e1a866d={""}
            >
              <div
                className={"the-logo"}
                data-v-3e1a866d={""}
                data-v-cfbd04aa={""}
              >
                <img
                  src={mediaUrl("/images/logo.svg")}
                  alt={"PrompTedSpace"}
                  data-v-cfbd04aa={""}
                />
              </div>
            </span>
          </a>
          <button
            className={"the-sound-switcher-mobile"}
            data-v-3e1a866d={""}
            data-v-af638566={""}
          >
            <svg
              id={"mute-control"}
              viewBox={"0 0 60 40"}
              xmlns={"http://www.w3.org/2000/svg"}
              data-v-af638566={""}
            >
              <rect
                className={"btn-bg"}
                x={"10"}
                y={"5"}
                width={"40"}
                height={"30"}
                fill={"none"}
                stroke={"black"}
                strokeWidth={"2"}
                rx={"15"}
                data-v-af638566={""}
              ></rect>
              <path
                d={
                  "M20 24H23.8889L29.1834 28.3319C29.2727 28.405 29.3846 28.4449 29.5 28.4449C29.7761 28.4449 30 28.2211 30 27.9449V12.0552C30 11.9398 29.9601 11.8279 29.887 11.7386C29.7121 11.5248 29.3971 11.4933 29.1834 11.6682L23.8889 16.0001H20C19.4477 16.0001 19 16.4478 19 17.0001V23.0001C19 23.5524 19.4477 24.0001 20 24.0001Z"
                }
                fill={"black"}
                data-v-af638566={""}
              ></path>
              <path
                className={"wave"}
                d={"M 33 16 Q 37 20 33 24"}
                stroke={"black"}
                strokeWidth={"2"}
                fill={"none"}
                stroke-linecap={"butt"}
                data-v-af638566={""}
              ></path>
              <path
                className={"wave"}
                d={"M 37 13 Q 44 20 37 27"}
                stroke={"black"}
                strokeWidth={"2"}
                fill={"none"}
                stroke-linecap={"butt"}
                data-v-af638566={""}
              ></path>
            </svg>
          </button>
          <div
            className={"the-hamburger button-shadow"}
            data-sound-click={"click"}
            data-v-3e1a866d={""}
            data-v-e64997e2={""}
          >
            <span data-v-e64997e2={""}>{"menu"}</span>
          </div>
          <div className={"the-header-mobile__nav"} data-v-3e1a866d={""}>
            <div
              className={"the-header-mobile__nav__inner container"}
              data-v-3e1a866d={""}
            >
              <nav
                className={"the-nav"}
                data-v-3e1a866d={""}
                data-v-bacbfa46={""}
              >
                <a
                  className={"the-nav__item"}
                  href={"#how"}
                  data-sound-hover={"hover"}
                  data-sound-click={"click"}
                  data-v-3e1a866d={""}
                  data-v-01873299={""}
                >
                  <span className={"the-nav__item__text"} data-v-01873299={""}>
                    {"PrompTedSite"}
                  </span>
                  <canvas
                    className={"the-nav__item__rive"}
                    width={"200"}
                    height={"100"}
                    data-v-01873299={""}
                  ></canvas>
                </a>
                <a
                  className={"the-nav__item"}
                  href={"#locations"}
                  data-sound-hover={"hover"}
                  data-sound-click={"click"}
                  data-v-3e1a866d={""}
                  data-v-01873299={""}
                >
                  <span className={"the-nav__item__text"} data-v-01873299={""}>
                    {"Locations"}
                  </span>
                  <canvas
                    className={"the-nav__item__rive"}
                    width={"200"}
                    height={"100"}
                    data-v-01873299={""}
                  ></canvas>
                </a>
                <a
                  className={"the-nav__item --email"}
                  href={"mailto:contact@promptedsite.com"}
                  data-sound-hover={"hover"}
                  data-sound-click={"click"}
                  data-v-3e1a866d={""}
                  data-v-ed701962={""}
                  data-v-01873299={""}
                >
                  <span className={"the-nav__item__text"} data-v-01873299={""}>
                    {"Contact"}
                  </span>
                  <canvas
                    className={"the-nav__item__rive"}
                    width={"200"}
                    height={"100"}
                    data-v-01873299={""}
                  ></canvas>
                </a>
              </nav>
              <div data-v-3e1a866d={""}>
                <svg
                  className={"star"}
                  viewBox={"0 0 46 51"}
                  xmlns={"http://www.w3.org/2000/svg"}
                  data-v-3e1a866d={""}
                  data-v-ac0760ef={""}
                >
                  <path
                    d={
                      "M21.8002 8.10889C22.8599 4.24885 28.2656 4.18798 29.4613 7.92725L29.515 8.10889L30.7064 12.4507C31.4691 15.2291 31.7604 16.2413 32.1791 17.1011C33.2341 19.2667 34.9709 21.0268 37.1225 22.1099C37.9762 22.5396 38.9833 22.8418 41.7523 23.6411C42.1231 23.7481 42.4815 23.8519 42.8285 23.9517C46.7045 25.0656 46.7045 30.6053 42.8285 31.7192C42.4816 31.8189 42.1231 31.9218 41.7523 32.0288C38.9832 32.8281 37.9762 33.1313 37.1225 33.561C35.1053 34.5765 33.4521 36.1866 32.3842 38.1685L32.1791 38.5698C31.7604 39.4296 31.4691 40.4417 30.7064 43.2202L29.515 47.562C28.4383 51.483 22.8769 51.483 21.8002 47.562L20.6088 43.2202C19.9415 40.7893 19.635 39.7105 19.2885 38.9028L19.1361 38.5698C18.0812 36.4041 16.3444 34.6441 14.1928 33.561C13.339 33.1313 12.332 32.8281 9.56289 32.0288C9.19187 31.9217 8.83297 31.819 8.48575 31.7192C4.60957 30.6055 4.60957 25.0654 8.48575 23.9517C8.78495 23.8657 9.09266 23.7769 9.40944 23.6854L9.56289 23.6411C12.3319 22.8418 13.339 22.5396 14.1928 22.1099C16.3443 21.0268 18.0812 19.2667 19.1361 17.1011C19.5549 16.2413 19.8462 15.2291 20.6088 12.4507L21.8002 8.10889Z"
                    }
                    fill={"black"}
                    data-v-ac0760ef={""}
                  ></path>
                  <path
                    d={
                      "M18.2466 3.50537C18.8985 1.13135 22.1812 1.05711 22.9976 3.28271L23.0688 3.50537L24.2603 7.84717C25.0075 10.5694 25.3364 11.7427 25.8306 12.7573C27.0294 15.2185 29.0035 17.2189 31.4487 18.4497C32.4565 18.9568 33.6242 19.2997 36.3364 20.0825C36.7076 20.1897 37.0667 20.2931 37.4146 20.3931C39.8429 21.091 39.8429 24.5799 37.4146 25.2778C37.0668 25.3778 36.7076 25.4812 36.3364 25.5884C33.6242 26.3713 32.4565 26.714 31.4487 27.2212C29.0035 28.452 27.0293 30.4524 25.8306 32.9136C25.3365 33.9281 25.0074 35.1009 24.2603 37.8228V37.8237L23.0688 42.1646C22.396 44.6154 18.9195 44.6153 18.2466 42.1646L17.0552 37.8237V37.8228C16.3081 35.1009 15.9789 33.9281 15.4849 32.9136L15.2515 32.4575C14.0379 30.2051 12.1592 28.3752 9.8667 27.2212C8.85893 26.714 7.69125 26.3713 4.979 25.5884C4.60751 25.4811 4.248 25.3769 3.8999 25.2769C1.47157 24.5789 1.47145 21.0909 3.8999 20.3931C4.248 20.293 4.60753 20.1897 4.979 20.0825C7.69119 19.2997 8.85894 18.9568 9.8667 18.4497C12.3119 17.2189 14.2861 15.2185 15.4849 12.7573C15.979 11.7427 16.308 10.5694 17.0552 7.84717L18.2466 3.50537Z"
                    }
                    fill={"#F7F2E5"}
                    stroke={"black"}
                    strokeWidth={"3"}
                    data-v-ac0760ef={""}
                  ></path>
                </svg>
                <svg
                  className={"star"}
                  viewBox={"0 0 46 51"}
                  xmlns={"http://www.w3.org/2000/svg"}
                  data-v-3e1a866d={""}
                  data-v-ac0760ef={""}
                >
                  <path
                    d={
                      "M21.8002 8.10889C22.8599 4.24885 28.2656 4.18798 29.4613 7.92725L29.515 8.10889L30.7064 12.4507C31.4691 15.2291 31.7604 16.2413 32.1791 17.1011C33.2341 19.2667 34.9709 21.0268 37.1225 22.1099C37.9762 22.5396 38.9833 22.8418 41.7523 23.6411C42.1231 23.7481 42.4815 23.8519 42.8285 23.9517C46.7045 25.0656 46.7045 30.6053 42.8285 31.7192C42.4816 31.8189 42.1231 31.9218 41.7523 32.0288C38.9832 32.8281 37.9762 33.1313 37.1225 33.561C35.1053 34.5765 33.4521 36.1866 32.3842 38.1685L32.1791 38.5698C31.7604 39.4296 31.4691 40.4417 30.7064 43.2202L29.515 47.562C28.4383 51.483 22.8769 51.483 21.8002 47.562L20.6088 43.2202C19.9415 40.7893 19.635 39.7105 19.2885 38.9028L19.1361 38.5698C18.0812 36.4041 16.3444 34.6441 14.1928 33.561C13.339 33.1313 12.332 32.8281 9.56289 32.0288C9.19187 31.9217 8.83297 31.819 8.48575 31.7192C4.60957 30.6055 4.60957 25.0654 8.48575 23.9517C8.78495 23.8657 9.09266 23.7769 9.40944 23.6854L9.56289 23.6411C12.3319 22.8418 13.339 22.5396 14.1928 22.1099C16.3443 21.0268 18.0812 19.2667 19.1361 17.1011C19.5549 16.2413 19.8462 15.2291 20.6088 12.4507L21.8002 8.10889Z"
                    }
                    fill={"black"}
                    data-v-ac0760ef={""}
                  ></path>
                  <path
                    d={
                      "M18.2466 3.50537C18.8985 1.13135 22.1812 1.05711 22.9976 3.28271L23.0688 3.50537L24.2603 7.84717C25.0075 10.5694 25.3364 11.7427 25.8306 12.7573C27.0294 15.2185 29.0035 17.2189 31.4487 18.4497C32.4565 18.9568 33.6242 19.2997 36.3364 20.0825C36.7076 20.1897 37.0667 20.2931 37.4146 20.3931C39.8429 21.091 39.8429 24.5799 37.4146 25.2778C37.0668 25.3778 36.7076 25.4812 36.3364 25.5884C33.6242 26.3713 32.4565 26.714 31.4487 27.2212C29.0035 28.452 27.0293 30.4524 25.8306 32.9136C25.3365 33.9281 25.0074 35.1009 24.2603 37.8228V37.8237L23.0688 42.1646C22.396 44.6154 18.9195 44.6153 18.2466 42.1646L17.0552 37.8237V37.8228C16.3081 35.1009 15.9789 33.9281 15.4849 32.9136L15.2515 32.4575C14.0379 30.2051 12.1592 28.3752 9.8667 27.2212C8.85893 26.714 7.69125 26.3713 4.979 25.5884C4.60751 25.4811 4.248 25.3769 3.8999 25.2769C1.47157 24.5789 1.47145 21.0909 3.8999 20.3931C4.248 20.293 4.60753 20.1897 4.979 20.0825C7.69119 19.2997 8.85894 18.9568 9.8667 18.4497C12.3119 17.2189 14.2861 15.2185 15.4849 12.7573C15.979 11.7427 16.308 10.5694 17.0552 7.84717L18.2466 3.50537Z"
                    }
                    fill={"#F7F2E5"}
                    stroke={"black"}
                    strokeWidth={"3"}
                    data-v-ac0760ef={""}
                  ></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}
