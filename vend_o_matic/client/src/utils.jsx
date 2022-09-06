import axios from "axios";

export const IS_DEV = process.env.NODE_ENV !== "production";

export const DOMAIN = IS_DEV ? `http://127.0.0.1:8000` : `${window.location.origin}`;

export const getInitialData = () =>
    new Promise(async (resolve, reject) => {
        let initialData = document.getElementById("initialData");

        if (!initialData && IS_DEV) {
            // This will not run in production
            console.log(`Getting page shared data in ${process.env.NODE_ENV} mode`);

            const base = new URL(window.location.href);
            const url = `${DOMAIN}${base.pathname}${base.search}`;

            let res;
            try {
                res = await axios.get(`${url}`);
            } catch (err) {
                return reject(err);
            }

            if (!res || res.status !== 200) return reject("No data");

            if (res.headers["content-type"].includes("text")) {
                const parser = new DOMParser();
                const doc = parser.parseFromString(res.data, "text/html");
                initialData = doc.getElementById("initialData");
            }
        }
        if (initialData) {
            return resolve(JSON.parse(initialData.textContent));
        }

        return reject("No data");
    });