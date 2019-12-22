function onSubmit() {
    let datasets = getDatasets();

    renderChart(datasets);
}

function renderChart(datasets) {
    let ctx = document.getElementById('myChart').getContext('2d');
    let myChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: datasets
        },
        options: {
            responsive: false,
            scales: {
                xAxes: [{
                    ticks: {
                        userCallback: function (label, index, labels) {
                            return moment(label).format("YYYY-MM-DD HH:mm");
                        }
                    }
                }]
            }
        }
    });
}

function getRawChartData() {
    // placeholder
    let data = [
        {
            pingTime: "2019-12-15 19:20:32",
            server: {
                id: 0,
                name: "ATM3R"
            },
            players: {
                online: 10,
                max: 100
            }
        },
        {
            pingTime: "2019-12-15 19:22:00",
            server: {
                id: 1,
                name: "Beyond"
            },
            players: {
                online: 7,
                max: 100
            }
        }
    ]

    return data;
}

function getListOfUniqueIds(rawData) {

    let uniqueIds = [...new Set(rawData.map(p => p.server.id))]
    let arr = [];

    uniqueIds.forEach(element => {
        var obj = {
            id: element,
            color: random_rgba()
        }

        arr.push(obj);
    });

    return arr;
}

function getPoints(id, rawData) {
    let arr = [];

    rawData.forEach(p => {
        if (p.server.id == id) {
            const point = {
                x: moment(p.pingTime),
                y: p.players.online
            }

            arr.push(point);
        }
    });

    return arr;
}

function getLabel(id, rawData) {
    for(let i = 0; i < rawData.length; i++) {
        if (rawData[i].server.id == id) {
            return rawData[i].server.name;
        }
    }
}

function getDatasets() {
    let rawData = getRawChartData();
    let uniqueIds = getListOfUniqueIds(rawData);
    let datasets = [];

    uniqueIds.forEach(id => {
        const l = getLabel(id.id, rawData);
        const d = getPoints(id.id, rawData);

        const dataset = {
            label: l,
            borderColor: id.color,
            backgroundColor: id.color,
            data: d
        }

        datasets.push(dataset);
    });

    return datasets;
}



function random_rgba() {
    let o = Math.round, r = Math.random, s = 255;
    return 'rgba(' + o(r() * s) + ',' + o(r() * s) + ',' + o(r() * s) + ',' + r().toFixed(1) + ')';
}