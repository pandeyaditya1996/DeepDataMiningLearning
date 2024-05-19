function submitTask() {
    const task = document.getElementById('task-select').value;
    const text = document.getElementById('input-text').value;
    const resultDiv = document.getElementById('result-text');

    resultDiv.innerHTML = 'Processing...';

    fetch('http://localhost:5000/perform_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ task, text })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = 'Result: ' + data.result;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = 'Failed to process.';
    });
}
