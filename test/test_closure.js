var toggle = (function () {
    var isShow = false;
    
    // ① 클로저를 반환
    return function () {
        // ③ 상태 변경
        isShow = !isShow;
        console.log(isShow);
    };
  })();

for (let i = 0; i < 5; i++) {
    toggle();
}

// 즉시 실행 함수는 정의되자마자 즉시 실행되고, 이후 소멸(한번만 실행) -> 변수 'isShow'는 재차 초기화될 일 X
// IIFE를 변수에 할당하면 IIFE 자체는 저장되지 않고, 함수가 실행된 결과만 저장 -> IIFE가 반환한 함수가 변수 'toggle'에 할당
// 변수 'isShow'는 클로저에 의해 참조됨
// 변수 'isShow'는 자신을 참조하는 함수가 소멸될 때까지 유지
// 변수 'isShow'는 외부에서 직접 접근할 수 없는 private 변수 -> 전역 변수를 사용했을 때와 같이 의도되지 않은 변경을 걱정할 필요도 없기 때문에 보다 안정적인 프로그래밍이 가능
