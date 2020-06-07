let storeData = [];
$(document).ready(function () {
    let defaultStore = "HKTVMall";
    storeData = changeStore(defaultStore)
    $('#storeName').text(storeData[1]);
    $('#ajaxTable').dataTable({
        dom: 'Pfrtip',

        ajax: {
            url: storeData[0],
            dataSrc: "",
        },
        columns: [
            {
                data: "RetrieveTime",
                defaultContent: "",
                searchPanes:{
                    show: false,
                },
            },
            {
                data: "Store",
                defaultContent: ""
            },
            {
                data: "Title",
                defaultContent: ""
            },
            {
                 data: "Country",
                 defaultContent: ""
            },
            {
                data: "Price",
                defaultContent: ""
            },
            {
                data: "URL",
                render: function (data, type, full, meta) {
                    return '<a class= "btn btn-outline-primary" href=' + data + ' role="button">Click me</a>';
                }
            }]
    });


})

function changeItemType(type){
    if (type == "mask") {
        switch (storeData[1]) {
            case "HKTVMall":
                storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/HKTVMall.json';
                break;
            case "Watsons":
                storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/watsons.json';
                break;
            case "Amazon":
                storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/amazon.json';
                break;
        }
    }

    if (type == "pig") {
        switch (storeData[1]) {
            case "HKTVMall":
                storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/HKTVMallPig.json';
                break;
            case "Amazon":
                storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/amazonPig.json';
                break;
        }
    }

    $('#ajaxTable').DataTable().clear() //must need
    $('#ajaxTable').DataTable().ajax.url(storeData[0]).load();//must need
    $('#ajaxTable').DataTable().ajax.reload()//must need
}

function changeHandler(name) {
    let storeData = changeStore(name)
    if ($("#btn1").class == "active"){
        type = "mask"
    }
    else{
        type = "pig"
    }
    changeItemType(type)
    $('#storeName').text(storeData[1]);
    $("#btnGroup").button('reset')
};


function changeStore(name){
    switch (name) {
        case "HKTVMall":
            storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/HKTVMall.json';
            storeData[1] = "HKTVMall";
            break;
        case "Watsons":
            storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/watsons.json';
            storeData[1] = "Watsons";
            break;
        case "Amazon":
            storeData[0] = 'https://peachrara.s3-ap-northeast-1.amazonaws.com/mask-inventory/amazon.json';
            storeData[1] = "Amazon";
            break;
    }
    return storeData;
}