function setClock(){
    const today = new Date();
    const year = today.getFullYear();
    const month = today.getMonth()+1; 
    const day = today.getDate();
    const hour = modifyNumber(today.getHours());
    const min = modifyNumber(today.getMinutes());
    const sec = modifyNumber(today.getSeconds());
    const formatDate = year+"."+(("00"+month.toString()).slice(-2))+"."+(("00"+day.toString()).slice(-2));

    document.getElementById("date").innerHTML = formatDate
    document.getElementById("time").innerHTML = hour + ":" + min + ":" + sec;
    }

    function modifyNumber(time){
    if(parseInt(time)<10){
    return "0" + time;
    }
    else return time;
    }

    window.onload = function(){
    setClock();
    setInterval(setClock,1000); // 1초 간격으로 secClock 함수 실행.
    }
