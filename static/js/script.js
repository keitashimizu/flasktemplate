//alert("Hello Jinja2");
var mydata = [
  {
    address: "Minato-ku",
    id: 2,
    mail: "mizugokoro@gmail.com",
    name: "清水敬太",
    tel: "08051303621",
  },
];

$.ajax({
  type: "GET",
  dataType: "json",
  scriptCharset: "UTF-8",
  timeout: 10000,
  url: "/api/users" + $(location).attr('search'),
}).done(function (data, status, xhr) {
  user_data = data["users"];
  //alert(JSON.stringify(user_data))
  $("#main_table").bootstrapTable({
    data: user_data,
  });
});

var parseJson = function (data) {
  var returnJson = {};
  for (idx = 0; idx < data.length; idx++) {
    returnJson[data[idx].name] = data[idx].value;
  }
  return returnJson;
};

$(document).ready(function () {
  $("#user_form").submit(function () {
    var data = $("#user_form").serializeArray();
    data = parseJson(data);
    $.ajax({
      type: "post",
      dataType: "json",
      contentType: "application/json",
      scriptCharset: "utf-8",
      data: JSON.stringify(data),
      url: "/api/users",
    });
  });
});
