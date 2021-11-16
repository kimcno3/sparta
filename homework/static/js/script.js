$(document).ready(function () {
    dollar_to_won()
    order_listing();
});

function openClose_orderBox() {
    if ($('#order-box').css('display') == 'block') {
        $('#order-box').hide();
        $('#orderbox-button').text('주문서 열기');
    } else if ($('#orderlist-table').css('display') == 'table') {
        $('#orderlist-table').hide();
        $('#orderlist-button').text('주문현황 열기');
        $('#order-box').show();
        $('#orderbox-button').text('주문서 닫기');
    }else {
        $('#order-box').show();
        $('#orderbox-button').text('주문서 닫기');
    }

}

function openClose_orderlist() {
    if ($('#orderlist-table').css('display') == 'table') {
        $('#orderlist-table').hide();
        $('#orderlist-button').text('주문현황 열기');
    } else if ($('#order-box').css('display') == 'block') {
        $('#order-box').hide();
        $('#orderbox-button').text('주문서 열기');
        $('#orderlist-table').show();
        $('#orderlist-button').text('주문현황 닫기');
    } else {
        $('#orderlist-table').show();
        $('#orderlist-button').text('주문현황 닫기');
    }

}
function checkBlank(name, count, address, phoneNumber){
    if(name === '' || count === '' || address === '' || phoneNumber === ''){
        alert('모든 정보를 입력해주세요');
        return false;
    }
}
function ordered() {
    let name = $('#name-text').val()
    let count = $('#count-text').val()
    let address = $('#address-text').val()
    let phoneNumber = $('#phoneNumber-text').val()

    if (checkBlank(name, count, address, phoneNumber) === false) return;

    $.ajax({
        type: "POST",
        url: "/order",
        data: {
            name_give: name,
            count_give: count,
            address_give: address,
            phoneNumber_give: phoneNumber
        },
        success: function (response) {
            alert(response["msg"]);
            window.location.reload();
        }
    })
}

function order_listing() {
    $.ajax({
        type: "GET",
        url: "/order",
        data: {},
        success: function (response) {
            let orders = response['order_list'] // 서버로 부터 받아온 딕셔너리가 response 안에 있으니 'order_list'로 다시 변수 지정
            for (let i = 0; i < orders.length; i++) {
                let address = orders[i]['address']
                let count = orders[i]['count']
                let name = orders[i]['name']
                let phoneNumber = orders[i]['phoneNumber']

                let temp_html = `<tr>
                                        <th scope="row">${name}</th>
                                        <td>${count}</td>
                                        <td>${address}</td>
                                        <td>${phoneNumber}</td>
                                    </tr>`
                $('#order-list').append(temp_html)
            }
        }
    })
}

function dollar_to_won() {
    $.ajax({
        type: "GET",
        url: "http://spartacodingclub.shop/sparta_api/rate",
        data: {},
        success: function (response) {
            let rate = response['rate'];
            let temp_html = `${rate}`;
            $('#dollarToWon').append(temp_html);

        }
    })
}
