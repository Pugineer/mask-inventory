let storeData = [];
let table;
$(document).ready(function () {
    let defaultStore = "Amazon";
    let countryShow;
    storeData = changeStore(defaultStore)
    let storeName = $('#storeName').text(storeData[1]);
    let table = $('#ajaxTable').dataTable({
        dom: 'Pfrtip',
        order: [[ 4, "asc" ]],
        searchPanes:{
            cascadePanes: true,
            threshold: 0.7
        },
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
                defaultContent: "",
            },
            {
                data: "Title",
                defaultContent: "",
                searchPanes:{
                    show: false
                },
            },
            {
                 data: "Country",
                 defaultContent: "",
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
            }],


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

}

function changeHandler(name) {
    table = $('#ajaxTable').DataTable();
    let storeData = changeStore(name)
    let type;
    if ($("#btn1").hasClass("active")){
        type = "mask"
    }
    else if ($("#btn2").hasClass("active")){
        type = "pig"
    }
    changeItemType(type)
    $('#storeName').text(storeData[1]);
    table.clear();
    table.ajax.url(storeData[0]).load()
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