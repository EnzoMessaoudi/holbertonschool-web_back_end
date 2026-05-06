export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve({ data: "Response from API", status: 200 });
    }, 1000);
  });
};
