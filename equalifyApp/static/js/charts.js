function createGenderChart(canvasId, labels, data, title) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Define colors based on gender
    const backgroundColors = [
        'rgba(54, 162, 235, 0.7)',  // Male - blue
        'rgba(255, 99, 132, 0.7)',   // Female - pink
        'rgba(75, 192, 192, 0.7)'     // Other - teal
    ];
    
    const borderColors = [
        'rgba(54, 162, 235, 1)',
        'rgba(255, 99, 132, 1)',
        'rgba(75, 192, 192, 1)'
    ];
    
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: title,
                data: data,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Percentage (%)'
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw}%`;
                        }
                    }
                }
            }
        }
    });
}