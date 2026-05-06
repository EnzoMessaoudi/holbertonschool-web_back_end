export default function handleResponseFromAPI(promise) {
    return promise
        .then(response => {
            return {status: 200, body: 'Success'};
        })
        .catch(err => {
            return new Error('Empty');
        })
        .finally(() => {
            console.log('Got a response from the API');
        });
};
