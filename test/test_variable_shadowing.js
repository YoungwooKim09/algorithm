function func() {
	var a = 'Geeks';
	let b = 'Geeks';
	
	if (true) {
		let a = 'GeeksforGeeks'; // Legal Shadowing
		var b = 'Geeks';         // Illegal Shadowing
		console.log(a);          // It will print 'GeeksforGeeks'
		console.log(b);          // It will print error
	}
}
func();


// Variable Shadowing이 가능한 이유 - 블록 레벨 스코프, 호이스팅, 실행 컨텍스트, 스코프 체인의 특성과 연관지어 생각해보기
// var는 함수 레벨 스코프이므로 위 경우, Illegal Shadowing
// 'let a = 3'이 'console.log(a)' 밑에 작성되어 있는 경우를 가정해보자. 함수 inner()에서 호이스팅이 이루어질 때, 변수 a는 해당 스코프의 최상단으로 끌어올려진다.
// 변수 a에 대한 선언문을 만나기 전까지 초기화가 이루어지지 않으므로 Reference Error 발생