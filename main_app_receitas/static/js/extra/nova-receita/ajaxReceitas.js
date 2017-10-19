$(document).ready(
    function listarReceitas() {
        $.ajax({
            type: 'GET',
            url: 'http://jsonstub.com/receita/lista',
            contentType: 'application/json',
            beforeSend: function (request) {
                request.setRequestHeader('JsonStub-User-Key', 'a4ed75a2-3733-4107-aacb-68a12165b258');
                request.setRequestHeader('JsonStub-Project-Key', '322cfc5d-3c67-40a3-bb76-d4d40e59d94a');
            }
        }).done(function (data) {
            $.each(data, function (indexInArray, valueOfElement) {
                var row = $("<tr />")
                $("#tableReceitas").append(row); //this will append tr element to table... keep its reference for a while since we will add cels into it
                row.append($("<td>" + valueOfElement.nome_receita + "</td>"));
                row.append($("<td>" + valueOfElement.classificacao + "</td>"));
                row.append($("<td>" + valueOfElement.setor + "</td>"));
            });
        });
    });