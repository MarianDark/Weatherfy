document.getElementById('weather-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = document.getElementById('city').value;
    const resultDiv = document.getElementById('weather-result');
    resultDiv.innerHTML = 'Buscando...';

    try {
        const response = await fetch('/get_weather', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ city })
        });
        const data = await response.json();
        if (response.ok) {
            resultDiv.innerHTML = `
                <h2>${data.city}</h2>
                <p>${data.temperature}°C, ${data.description}</p>
                <img src="https://openweathermap.org/img/wn/${data.icon}@2x.png">
            `;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch {
        resultDiv.innerHTML = `<p>Error al obtener el clima.</p>`;
    }
});
