function checkinfo() {
    var pwd1 = document.getElementsByName("login_pwd")[0].value;
    var pwd2 = document.getElementsByName("pwd")[0].value;
    if(pwd1 != pwd2) {
        alert("两次密码输入不一致，请重新输入！");
        return false;
    }
    else {
        return true;
    }
}