export const fetchOrderData = async () => {
	console.log("!£%^%$")
	// 5 second timeout:
	const controller = new AbortController()
	const timeoutId = setTimeout(() => controller.abort(), 5000)
	const response = await fetch(
		"http://127.0.0.1:8000/dashboard/",
		{signal: controller.signal},
	);
	return await response.json();
};

