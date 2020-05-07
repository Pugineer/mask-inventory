//$.getJSON("data.json", function (data) {
//    var items = [];
//    var itemsKey = "";
//    var prices = [];
//    var pricesKey = "";
//    $.each(data, function (key, val) {
//        if (key === "Title") {
//            itemsKey = key;
//            items = val;
//        } else if (key === "Price") {
//            pricesKey = key;
//            prices = val;
//        }
//    });
//    for (var i = 0; i < items.length; i++) {
//        var htmlStr = '<div class="col mb-4">'
//        htmlStr += '<div class="card">'
//        htmlStr += '<div class="card-body">'
//        htmlStr += '<h5 class="card-title">' + items[i] + '</h5>'
//        htmlStr += '<p class="card-text">' + prices[i] + '</p>'
//        htmlStr += '</div></div></div>'
//        $("#cardbodycontent").append(htmlStr);
//    }
//});

  $(document).ready(function() {
            $('#table_id').DataTable({
                ajax: {
                    url: data_change(inputData),
                    dataSrc: ''
                },
                "columns": [{
                        "data": "Title"
                    },
                    {
                        "data": "Price"
                    },
                    {
                        "data": "URL",
                        render: function(data, type, full, meta) {
                            return '<a class= "btn btn-primary" href=' + data + ' role="button">Click me</a>';
                        }
                    }
                ]
            });
        });

        var inputData = "hktv"

        function changeInput(str) {
            inputData = str
            var optData = data_change(inputData)
            changeTitle(inputData)

            //-----------Refresh Process Start----------
            $('#table_id').DataTable().clear() //must need
            $('#table_id').DataTable().ajax.url(optData).load();//must need
            $('#table_id').DataTable().ajax.reload()//must need
            //-----------Refresh Process Start----------
        }

        function changeTitle(a) {
            var element = document.getElementById("a1").innerHTML = a;
        }

        function data_change(data) {
            if (data == "hktv") {
                return "hktv.json"
            } else if (data == "watsons") {
                return "watsons.json"
            }
        }