function count() {
    $.ajax({
        url: "http://shijingz.eecs.umich.edu/seats_count",
        dataType: "json",
        method: "GET",
        timeout: 1000,
        statusCode: {
            200: function (data, textStatus, jqXHR) {
                myChart.data.datasets[1].data = [];
                for (let index = 0; index < data['counts'].length; index++) {
                    myChart.data.datasets[1].data[index] = data['counts'][index];
                }
                myChart.update();
            }
        }
    });
}

function count_today() {
    $.ajax({
        url: "http://shijingz.eecs.umich.edu/seats_count_today",
        dataType: "json",
        method: "GET",
        timeout: 1000,
        statusCode: {
            200: function (data, textStatus, jqXHR) {
                myChart.data.datasets[0].data = [];
                for (let index = 0; index < data['counts'].length; index++) {
                    myChart.data.datasets[0].data[index] = data['counts'][index];
                }
                myChart.update();
            }
        }
    });
}

var ctx = document.getElementById("myChart");
 
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00"
        ],
        datasets: [{
            label: 'Today',
            data: [],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#ff0000',
            borderWidth: 4,
            pointBackgroundColor: '#ff0000'
        }, {
            label: 'Yesterday',
            data: [],
            lineTension: 0,
            backgroundColor: 'transparent',
            borderColor: '#007bff',
            borderWidth: 4,
            pointBackgroundColor: '#007bff'
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
        legend: {
            display: true,
            // labels:
        }
    }
});
count();
count_today();

$('#table').bootstrapTable({
    columns: [{
        field: 'id',
        title: 'ID'
    }, {
        field: 'seat_id',
        title: 'Seat ID'
    }, {
        field: 'location',
        title: 'Location'
    }, {
        field: 'status',
        title: 'Status'
    }, {
        field: 'temp',
        title: 'Temperature'
    }, {
        field: 'battery',
        title: 'Battery Level'
    }]
});

function getData(m_url) {
    $.ajax({
        url: m_url,
        dataType: "json",
        method: "GET",
        timeout: 1000,
        statusCode: {
            200: function (data, textStatus, jqXHR) {
                seats = data["seats"];
                $('#table').bootstrapTable('load', seats);
                for (let index = 0; index < seats.length; index++) {
                    if (seats[index]["status"] == "occupied") {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "red",
                            "color": "rgb(194, 74, 80)",
                            "border": "2px solid rgb(194, 74, 80)"
                        });
                        $(".m_btn".concat(seats[index]['seat_id'])).hover(function () {
                            $(this).css({
                                "background-color": "rgba(245, 245, 245, 1)",
                                "color": "rgba(125, 0, 0, 1)",
                                "border": "2px solid rgb(128, 138, 131)"
                            })
                        });
                    } else if (seats[index]["status"] == "unoccupied") {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "green",
                            "color": "rgba(62, 155, 90)",
                            "border": "2px solid rgb(62, 155, 90)"
                        });
                        $(".m_btn".concat(seats[index]['seat_id'])).hover(function () {
                            $(this).css({
                                "background-color": "rgba(245, 245, 245, 1)",
                                "color": "rgba(125, 0, 0, 1)",
                                "border": "2px solid rgb(128, 138, 131)"
                            })
                        });
                    } else {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "grey",
                            "color": "rgba(128, 138, 131)",
                            "border": "2px solid rgb(128, 138, 131)"
                        });
                        $(".m_btn".concat(seats[index]['seat_id'])).hover(function () {
                            $(this).css({
                                "background-color": "rgba(245, 245, 245, 1)",
                                "color": "rgba(125, 0, 0, 1)",
                                "border": "2px solid rgb(128, 138, 131)"
                            })
                        });
                    }
                }
            }
            // 204: function (data, textStatus, jqXHR) {
            //     console.log(textStatus)
            //     console.log("No seat in DB")
            // },
        }
    });
}

$(function () {
    setInterval(function load_seats() {
        getData("http://shijingz.eecs.umich.edu/seats_info");
    }, 1000)
})

$(function () {
    setInterval(function load_count() {
        count();
    }, 20000)
})

$(function () {
    setInterval(function load_count_today() {
        count_today();
    }, 10000)
})

$('#table').addClass("table table-striped table-sm");
