export const fetchOrderData = async () => {
	console.log("!£%^%$")
	const response = await fetch(
		"http://127.0.0.0:8000/dashboard/"
	);
	return await response.json();
};

