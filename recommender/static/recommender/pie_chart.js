document.addEventListener("DOMContentLoaded", function() {

    var very_high = parseInt(document.getElementById('pieChart').getAttribute('data-very_high'));
    var high = parseInt(document.getElementById('pieChart').getAttribute('data-high'));
    var medium = parseInt(document.getElementById('pieChart').getAttribute('data-medium'));
    var low = parseInt(document.getElementById('pieChart').getAttribute('data-low'));

    new Chart(document.getElementById('pieChart'), {
        type: 'pie',
        data: {
            labels: ['Very High', 'High', 'Medium', 'Low'],
            datasets: [{
                data: [very_high, high, medium, low],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.5)',
                    'rgba(255, 159, 64, 0.5)',
                    'rgba(255, 205, 86, 0.5)',
                    'rgba(54, 162, 235, 0.5)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 205, 86, 1)',
                    'rgba(54, 162, 235, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Similarity Score Distribution'
            }
        }
    });
});