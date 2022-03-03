const axios = require("axios");
const baseURL = process.env.NODE_ENV === "production" ? "api" : "http://127.0.0.1:5000";
export default axios.create({
	baseURL,
});
