window.onload = function () {
    updateSummary();
};

// 윈도우 크기가 변경될 때 실행되는 함수
window.onresize = function () {
    updateSummary();
};

function updateSummary() {
    var summaryElement = document.getElementById('summary');
    var windowWidth = window.innerWidth;

    // 화면 크기에 따라 다른 내용을 설정
    if (windowWidth <= 768) {
        summaryElement.innerHTML = '<p class="logo">스며듦은...</p>';
    } else {
        summaryElement.innerHTML = '<p class="logo">스며듦은 기성세대, MZ세대로 분류되는 세대 차이, 개발자와 디자이너로 나뉘는 직무 차이 등<br>개인 별로 다양한 백그라운드 차이로 인한 커뮤니케이션 상의 소모적인 비용을 감소시키고자 합니다.<br>스며듦이라는 서비스를 제공하고자 하는데 홈페이지의 소개 부분에 어떤걸 넣으면 좋을까?</p>';
    }
}