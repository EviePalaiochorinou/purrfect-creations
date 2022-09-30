export const fetchOrderData = async () => {
	const response = await fetch(
		"http://127.0.0.1:8000/dashboard/"
	);
	return await response.json();
};

