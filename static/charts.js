Chart.defaults.color = "#FBFEF9";


let ctx = document.getElementById("incomevsexpensesline")
let ctx1 = document.getElementById("incomevsexpensesbar")
const data = {
    labels:['monday', 'tuesday','wednesday','thursday','saturday','friday','sunday'],
    datasets: [{
        label: 'My First dataset',
        backgroundColor: '#FF4D4D',
        borderColor: '#FF4D4D',
        data: [0, 10, 5, 2, 20, 30, 45],
      },{
        label: 'My First dataset',
        backgroundColor: '#6DFF8C',
        borderColor: '#6DFF8C',
        data: [10, 15, 50, 20, 2, 35, 40],
      }]
}

const ivel = new Chart(
    ctx,
    config = {
        type: 'line',
        data: data,
        options:{

            
            scales: {
                x: {
                  grid: {
                    color: '#fbfef952',

                  }
                },
              
            y:{
                grid: {
                    color: '#fbfef952',

                  }
            },},
            responsive:true,
        },
    }
);

const data1 = {
    labels:['monday', 'tuesday'],
    datasets: [{
        label: 'My First dataset',
        backgroundColor: ['#6DFF8C','#FF4D4D'],
        borderColor: ['#6DFF8C','#FF4D4D'],
        data: [25, 5],
        
      }]
}

const iveb = new Chart(
    ctx1,
    config = {
        type: 'bar',
        data: data1,
        options:{

            responsive:true,
        },
    }
);