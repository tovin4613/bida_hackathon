(function(){

    var Msg = {
        success: 'Logined your account.',
        fail: 'Check your account.',
    }

    var Event = {
        login: function(){
            $('#login-btn').on('click', function(){
                var params = {
                    email: $('#email').val(),
                    pw: $('#pw').val(),
                };
                if(params.email === 'admin@kt.com' && params.pw === '1234'){
                    $('.msg').text(Msg.success).show();
                    location.href = 'contents.html';
                }else{
                    $('.msg').text(Msg.fail).show();
                };
            })
        },
    }
    Event.login();
})();

