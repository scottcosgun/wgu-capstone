document.addEventListener("DOMContentLoaded", function() {

    var yes_count = parseInt(document.getElementById('satisfactionChart').getAttribute('data-yes_count'));
    var no_count = parseInt(document.getElementById('satisfactionChart').getAttribute('data-no_count'));

    new Chart(document.getElementById('satisfactionChart'), {
        type: 'pie',
        data: {
            labels: ['Satisfied', 'Unsatisfied'],
            datasets: [{
                data: [yes_count, no_count],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.5)',
                    'rgba(54, 162, 235, 0.5)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)'
                ],
                borderWidth: 1
            }]
        },
        plugins: [ChartDataLabels],
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Customer Satisfaction'
            },
            plugins: {
                datalabels: {
                    formatter: function(value, ctx) {
                        let sum = 0;
                        let dataArr = ctx.chart.data.datasets[0].data;
                        dataArr.map(data => {
                            sum += data;
                        });
                        let percentage = (value*100 / sum).toFixed(2)+"%";
                        return percentage;
                    },
                    color: '#666',
                }
            }
        }
    });
});