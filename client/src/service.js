function singup() {
    fetch('http://127.0.0.1:8000/singup')
    .then(response => {
        if (!response.ok) {
            throw new Error('Malote');
        }
        return response.json(); 
    })
    .then(data => {
        console.log(data); 
    })
    .catch(error => {
        console.error('Error:', error);
    });
} 




