async function onSubmit() {
    let datasets = await getDatasets();

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

async function getRawChartData() {
    let from = document.getElementById("from").value;
    let to = document.getElementById("to").value;
    let url = `https://poller.moddedminecraft.club/get_pings.php?start_date${from}=&end_date=${to}`;

    let response = await fetch(url);

    if (response.ok) {
        let json = await response.json();
        
        return json;
    } else {
        alert("HTTP-Error: " + response.status);

        return null;
    }
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
    for (let i = 0; i < rawData.length; i++) {
        if (rawData[i].server.id == id) {
            return rawData[i].server.name;
        }
    }
}

async function getDatasets() {
    let rawData = await getRawChartData();
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