$(document).ready(function(){
  var host = "thesmartmotion.pythonanywhere.com";

$(".submenu > a").click(function(e) {
  e.preventDefault();
  var $li = $(this).parent("li");
  var $ul = $(this).next("ul");

  if($li.hasClass("open")) {
    $ul.slideUp(350);
    $li.removeClass("open");
  } else {
    $(".nav > li > ul").slideUp(350);
    $(".nav > li").removeClass("open");
    $ul.slideDown(350);
    $li.addClass("open");
  }
});

  var randomScalingFactor = function() {
    return Math.round(Math.random() * 100);
};

var chartColors = window.chartColors;
var color = Chart.helpers.color;
var sconfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Interest'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

var tconfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Moment'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

var econfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Feelings'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

var puconfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Public Figure'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

var prconfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Tips'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

var stconfig = {
  data: {
    datasets: [{
      data: [],
      backgroundColor: [
        color(chartColors.red).alpha(0.5).rgbString(),
        color(chartColors.orange).alpha(0.5).rgbString(),
        color(chartColors.yellow).alpha(0.5).rgbString(),
        color(chartColors.green).alpha(0.5).rgbString(),
        color(chartColors.blue).alpha(0.5).rgbString(),
      ],
      label: 'My dataset' // for legend
    }],
    labels: []
  },
  options: {
    responsive: true,
    legend: {
      position: 'right',
    },
    title: {
      display: true,
      text: 'Story'
    },
    scale: {
      ticks: {
        beginAtZero: true
      },
      reverse: false
    },
    animation: {
      animateRotate: false,
      animateScale: true
    }
  }
};

function drawSocialCurrencyChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('sc-table');
      window.scPolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.scPolarArea.update();
  }
      });
}

function drawTriggerChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('t-table');
      window.tPolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.tPolarArea.update();
  }
      });
}

function drawEmotionChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('e-table');
      window.ePolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.ePolarArea.update();
  }
      });
}

function drawPublicChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('pu-table');
      window.puPolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.puPolarArea.update();
  }
      });
}

function drawPracticalValueChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('pr-table');
      window.prPolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.prPolarArea.update();
  }
      });
}

function drawStoryChart(scUrl, config, init){
    var jsonData = $.ajax({
        url: scUrl,
        dataType: 'json',
      }).done(function (results) {
        // Split timestamp and data into separate arrays
        var labels = [], data=[];
        results.forEach(function(packet) {
          labels.push(packet.keyword);
          data.push(parseFloat(packet.px_low)*100);
        });
  config.data.datasets.forEach(function(piece, i) {
    config.data.datasets[i].data = data;
    config.data.labels = labels;
  });
  if(init == '1'){
      var ctx = document.getElementById('st-table');
      window.stPolarArea = Chart.PolarArea(ctx, config);
  }
  else{
      window.stPolarArea.update();
  }
      });
}

window.onload = function() {
  drawSocialCurrencyChart('http://'+ host + '/sc/get/', sconfig, 1);
  drawTriggerChart('http://'+ host + '/t/get/', tconfig, 1);
  drawEmotionChart('http://'+ host + '/e/get/', econfig, 1);
  drawPublicChart('http://'+ host + '/pu/get/', puconfig, 1);
  drawPracticalValueChart('http://'+ host + '/pr/get/', prconfig, 1);
  drawStoryChart('http://'+ host + '/st/get/', stconfig, 1);
};

document.getElementById('today-filter').addEventListener('click', function() {
    drawSocialCurrencyChart('http://'+ host + '/sc/get/?filter=today', sconfig, 0);
    drawTriggerChart('http://'+ host + '/t/get/?filter=today', tconfig, 0);
    drawEmotionChart('http://'+ host + '/e/get/?filter=today', econfig, 0);
  drawPublicChart('http://'+ host + '/pu/get/?filter=today', puconfig, 0);
  drawPracticalValueChart('http://'+ host + '/pr/get/?filter=today', prconfig, 0);
  drawStoryChart('http://'+ host + '/st/get/?filter=today', stconfig, 0);
});

document.getElementById('week-filter').addEventListener('click', function() {
    drawSocialCurrencyChart('http://'+ host + '/sc/get/?filter=week', sconfig, 0);
    drawTriggerChart('http://'+ host + '/t/get/?filter=week', tconfig, 0);
    drawEmotionChart('http://'+ host + '/e/get/?filter=week', econfig, 0);
  drawPublicChart('http://'+ host + '/pu/get/?filter=week', puconfig, 0);
  drawPracticalValueChart('http://'+ host + '/pr/get/?filter=week', prconfig, 0);
  drawStoryChart('http://'+ host + '/st/get/?filter=week', stconfig, 0);
});

document.getElementById('month-filter').addEventListener('click', function() {
    drawSocialCurrencyChart('http://'+ host + '/sc/get/?filter=month', sconfig, 0);
    drawTriggerChart('http://'+ host + '/t/get/?filter=month', tconfig, 0);
    drawEmotionChart('http://'+ host + '/e/get/?filter=month', econfig, 0);
  drawPublicChart('http://'+ host + '/pu/get/?filter=month', puconfig, 0);
  drawPracticalValueChart('http://'+ host + '/pr/get/?filter=month', prconfig, 0);
  drawStoryChart('http://'+ host + '/st/get/?filter=month', stconfig, 0);
});

document.getElementById('default-filter').addEventListener('click', function() {
    drawSocialCurrencyChart('http://'+ host + '/sc/get/', sconfig, 0);
    drawTriggerChart('http://'+ host + '/t/get/', tconfig, 0);
    drawEmotionChart('http://'+ host + '/e/get/', econfig, 0);
  drawPublicChart('http://'+ host + '/pu/get/', puconfig, 0);
  drawPracticalValueChart('http://'+ host + '/pr/get/', prconfig, 0);
  drawStoryChart('http://'+ host + '/st/get/', stconfig, 0);
});

});