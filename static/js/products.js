$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
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