import React from "react";

function Footer() {
  return (
    <footer>
      <div className="row bg-dark py-5 mx-0 card card-header  flex-row align-items-center text-center text-md-start">
        <div className="col-md-5 mb-3 mb-md-0">
          <div className="text-primary-hover text-white">
            {new Date().getFullYear()}{" "}
            <a
              href="https://EdwinDev.com/"
              className="text-reset btn-link ms-2 me-2 "
              target="_blank"
            >
              Edwin Gonzalez
            </a>
            | All rights reserved
          </div>
        </div>
        <div className="col-md-3 mb-3 mb-md-0">
          <img
            src="/images/Logo1.png"
            style={{
              maxWidth: "100px",
              height: "auto",
              objectFit: "contain",
            }}
            alt="footer logo"
          />
        </div>
        <div className="col-md-4">
          <ul className="nav text-primary-hover justify-content-center justify-content-md-end">
            <li className="nav-item">
              <a
                className="nav-link text-white px-2 fs-5"
                href="https://facebook.com/desphixs"
              >
                <i className="fab fa-facebook-square" />
              </a>
            </li>
            <li className="nav-item">
              <a
                className="nav-link text-white px-2 fs-5"
                href="https://twitter.com/desphixs"
              >
                <i className="fab fa-twitter-square" />
              </a>
            </li>

            <li className="nav-item">
              <a
                className="nav-link text-white px-2 fs-5"
                href="https://youtube.com/@desphixs"
              >
                <i className="fab fa-youtube-square" />
              </a>
            </li>
          </ul>
        </div>
      </div>
    </footer>
  );
}

export default Footer;
