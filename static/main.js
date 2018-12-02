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
            data: [
                15339,
                21345,
                18483,
                24003,
                23489,
                24092,
                12034,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000,
                20000
            ],
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
                    beginAtZero: false
                }
            }]
        },
        legend: {
            display: false,
        }
    }
});
$('#table').bootstrapTable({
    columns: [{
        field: 'id',
        title: 'ID'
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
function m_fun(json) {
    console.log(json)
    //         // console.log(data.responseText)
    //         // seats = JSON.parse(data)["seats"];
    //         seats = data["seats"];
    //         $('#table').bootstrapTable('load', seats);
}
function getData(m_url) {
    $.ajax({
        url: m_url,
        // crossOrigin: true,
        // proxy: "/static/proxy.php", //to overide default proxy
        dataType: "json",
        method: "GET",
        timeout: 1000,
        // jsonpCallback: "m_fun"
        statusCode: {
            200: function (data, textStatus, jqXHR) {
                // console.log(data.responseText)
                // seats = JSON.parse(data)["seats"];
                seats = data["seats"];
                $('#table').bootstrapTable('load', seats);
                for (let index = 0; index < seats.length; index++) {
                    if (seats[index]["status"] == "occupied") {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "red",
                            "color": "rgb(194, 74, 80)",
                            "border": "2px solid rgb(194, 74, 80)"
                        })
                        // console.log(document.getElementsByClassName(".m_btn".concat(seats[index]['seat_id'])).style);
                        // document.getElementsByClassName(".m_btn".concat(seats[index]['seat_id'])).style["background-color"] = "rgba(0, 0, 0, 1)";
                    } else if (seats[index]["status"] == "unoccupied") {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "green",
                            "color": "rgba(62, 155, 90)",
                            "border": "2px solid rgb(62, 155, 90)"
                        })
                        // document.getElementsByClassName(".m_btn".concat(seats[index]['seat_id'])).style["background-color"] = "rgba(254, 254, 254, 1)";
                    } else {
                        $(".m_btn".concat(seats[index]['seat_id'])).css({
                            "background-color": "grey",
                            "color": "rgba(128, 138, 131)",
                            "border": "2px solid rgb(128, 138, 131)"
                        })
                        // document.getElementsByClassName(".m_btn".concat(seats[index]['seat_id'])).style["background-color"] = "rgba(192, 192, 192, 1)"
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
    setInterval(function test() {
        getData("http://shijingz.eecs.umich.edu:5000/seats_info");
    }, 1000)
})
$('#table').addClass("table table-striped table-sm");
