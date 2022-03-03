import api from "../api/api";

const getAccounts = async () => {
	const users = await api.get("/");
	return users;
};
const sortArray = (isAsc, arr, prop) => {
	const arrCopy = [...arr];
	if (!isAsc) arrCopy.sort((a, b) => b[prop] - a[prop]);
	else arrCopy.sort((a, b) => a[prop] - b[prop]);
	return arrCopy;
};
const capFirstLetter = (string) => {
	return string && string[0].toUpperCase() + string.substring(1);
};
const selectItem = (ref, id) => {
	const refChildren = Array.from(ref.current.children);
	let correctId;
	refChildren.forEach((child) => {
		if (child.getAttribute("userid") !== id) child.classList.remove("selected");
		else {
			correctId = child.getAttribute("userid");
			child.classList.add("selected");
		}
	});
	return correctId;
};
const searchArray = (arr, query) => {
	const newArr = arr.filter((item) => item.name.toLowerCase().includes(query.toLowerCase()));
	return newArr;
};
const doAction = async (action, body) => {
	await api.post(`/${action}`, body);
};
const onNumberInputChange = (e) => {
	const regex = /[\d]+/g;
	const newArr = e.target.value.split("").filter((x) => x.match(regex));
	e.target.value = newArr.join("");
};
const displayErrorMessage = (ref, message, id) => {
	ref.current.innerText = message;
	id = setTimeout(() => {
		ref.current.innerText = "";
	}, 3000);
	return id;
};
export {
	getAccounts,
	sortArray,
	capFirstLetter,
	selectItem,
	searchArray,
	doAction,
	onNumberInputChange,
	displayErrorMessage,
};
