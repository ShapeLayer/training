var rockBack = document.getElementById('ps-rock_back');
var lighthouse = document.getElementById('ps-lighthouse');
var rockFront = document.getElementById('ps-rock_front');
var fogWater = document.getElementById('ps-fog_water');
var fog = document.getElementById('ps-fog');
var exploreBtn = document.getElementById('ps-explore_btn');
var header = document.querySelector('header');

window.addEventListener('scroll', function() {
    var nowScroll = window.scrollY;
    rockBack.style.top = nowScroll * 0.5 + 'px';
    lighthouse.style.top = nowScroll * 0.7 + 'px';
    rockFront.style.top = nowScroll * 0.4 + 'px';
    fogWater.style.top = nowScroll * 0.4 + 'px';
    fog.style.top = nowScroll * 0.3 + 'px';
    exploreBtn.style.marginTop = nowScroll * 2 + 'px';
    header.style.top = nowScroll * 0.5 + 'px';
})