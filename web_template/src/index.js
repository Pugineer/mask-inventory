$.getJSON("data.json", function(data) {
    var items = [];
    var itemsKey = "";
    var prices = [];
    var pricesKey = "";
    $.each(data, function(key, val) {
      if (key === "Title") {
        itemsKey = key;
        items = val;
      } else if (key === "Price") {
        pricesKey = key;
        prices = val;
      }
    });
    console.log(items)
    for (var i = 0; i < items.length; i++) {
      var htmlStr = '<div class="col mb-4">'
      htmlStr += '<div class="card">'
      htmlStr += '<div class="card-body">'
      htmlStr += '<h5 class="card-title">' + items[i] + '</h5>'
      htmlStr += '<p class="card-text">' + prices[i] + '</p>'
      htmlStr += '</div></div></div>'
      $("#cardbodycontent").append(htmlStr);
    }
  });