$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                 var newHTML = resp.data.map(d => {
                     return `<div class="product_box">
                                <a class="single_product" href="/products/${d.id}">
                                    <img class="product-img" src="${d.firstImage}" />
                                    <h4 class="product-name">${d.name}</h4>
                                    <p class="product-price">${d.price} kr</p>
                                </a>
                            </div>
                    `
                 });
                 $('.products').html(newHTML.join(''));
                 $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    })
});

$(document).ready(function() {
    $('#search-hist-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = document.getElementById("search-hist").value;
        $.ajax({
            url: '/products?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                 var newHTML = resp.data.map(d => {
                     return `<div class="well products">
                                <a href="/products/${d.id}">
                                    <img class="product-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>
                    `
                 });
                 $('.products').html(newHTML.join(''));
                 $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error);
            }
        })
    })
})