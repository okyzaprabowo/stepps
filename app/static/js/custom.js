$(document).ready(function(){
  var host = "192.168.10.10:8000";

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
  var socialCurrencyTable = new Tabulator("#sc-table", {
      ajaxURL:"http://"+host+"/sc/get/", //ajax URL
      layout:"fitColumns",
      columns:[                 //define the table columns
        {title:"Keyword", field:"keyword"},
        {title:"Freq(H)", field:"freq_high"},
        {title:"P(X|H)", field:"px_high"},
        {title:"Freq(M)", field:"freq_medium"},
        {title:"P(X|M)", field:"px_medium"},
        {title:"Freq(L)", field:"freq_low"},
        {title:"P(X|L)", field:"px_low"},
      ],
  });

  var triggerCurrencyTable = new Tabulator("#t-table", {
    ajaxURL:"http://"+host+"/t/get/", //ajax URL
    layout:"fitColumns",
    columns:[                 //define the table columns
      {title:"Keyword", field:"keyword"},
      {title:"Freq(H)", field:"freq_high"},
      {title:"P(X|H)", field:"px_high"},
      {title:"Freq(M)", field:"freq_medium"},
      {title:"P(X|M)", field:"px_medium"},
      {title:"Freq(L)", field:"freq_low"},
      {title:"P(X|L)", field:"px_low"},
    ],
});

var emotionCurrencyTable = new Tabulator("#e-table", {
  ajaxURL:"http://"+host+"/e/get/", //ajax URL
  layout:"fitColumns",
  columns:[                 //define the table columns
    {title:"Keyword", field:"keyword"},
    {title:"Freq(H)", field:"freq_high"},
    {title:"P(X|H)", field:"px_high"},
    {title:"Freq(M)", field:"freq_medium"},
    {title:"P(X|M)", field:"px_medium"},
    {title:"Freq(L)", field:"freq_low"},
    {title:"P(X|L)", field:"px_low"},
  ],
});

var publicCurrencyTable = new Tabulator("#pu-table", {
  ajaxURL:"http://"+host+"/pu/get/", //ajax URL
  layout:"fitColumns",
  columns:[                 //define the table columns
    {title:"Keyword", field:"keyword"},
    {title:"Freq(H)", field:"freq_high"},
    {title:"P(X|H)", field:"px_high"},
    {title:"Freq(M)", field:"freq_medium"},
    {title:"P(X|M)", field:"px_medium"},
    {title:"Freq(L)", field:"freq_low"},
    {title:"P(X|L)", field:"px_low"},
  ],
});

var practicalCurrencyTable = new Tabulator("#pr-table", {
  ajaxURL:"http://"+host+"/pr/get/", //ajax URL
  layout:"fitColumns",
  columns:[                 //define the table columns
    {title:"Keyword", field:"keyword"},
    {title:"Freq(H)", field:"freq_high"},
    {title:"P(X|H)", field:"px_high"},
    {title:"Freq(M)", field:"freq_medium"},
    {title:"P(X|M)", field:"px_medium"},
    {title:"Freq(L)", field:"freq_low"},
    {title:"P(X|L)", field:"px_low"},
  ],
});

var storyCurrencyTable = new Tabulator("#st-table", {
  ajaxURL:"http://"+host+"/st/get/", //ajax URL
  layout:"fitColumns",
  columns:[                 //define the table columns
    {title:"Keyword", field:"keyword"},
    {title:"Freq(H)", field:"freq_high"},
    {title:"P(X|H)", field:"px_high"},
    {title:"Freq(M)", field:"freq_medium"},
    {title:"P(X|M)", field:"px_medium"},
    {title:"Freq(L)", field:"freq_low"},
    {title:"P(X|L)", field:"px_low"},
  ],
});

  // var table = new Tabulator("#example-table", {
  //   data:socialCurrencyTable,           //load row data from array
  //   layout:"fitColumns",      //fit columns to width of table
  //   responsiveLayout:"hide",  //hide columns that dont fit on the table
  //   tooltips:true,            //show tool tips on cells
  //   addRowPos:"top",          //when adding a new row, add it to the top of the table
  //   history:true,             //allow undo and redo actions on the table
  //   pagination:"local",       //paginate the data
  //   paginationSize:7,         //allow 7 rows per page of data
  //   movableColumns:true,      //allow column order to be changed
  //   resizableRows:true,       //allow row order to be changed
  //   initialSort:[             //set the initial sort order of the data
  //     {column:"name", dir:"asc"},
  //   ],
  //   columns:[                 //define the table columns
  //     {title:"Name", field:"name", editor:"input"},
  //     {title:"Task Progress", field:"progress", align:"left", formatter:"progress", editor:true},
  //     {title:"Gender", field:"gender", width:95, editor:"select", editorParams:{"Male":"male", "Female":"female"}},
  //     {title:"Rating", field:"rating", formatter:"star", align:"center", width:100, editor:true},
  //     {title:"Color", field:"col", width:130, editor:"input"},
  //     {title:"Date Of Birth", field:"dob", width:130, sorter:"date", align:"center"},
  //     {title:"Driver", field:"car", width:90,  align:"center", formatter:"tickCross", sorter:"boolean", editor:true},
  //   ],
  // });
  
});