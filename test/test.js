let a = 1;

function outer() {
  console.log(a); // 1

  function inner() {
    console.log(a); // ReferenceError
    // let a = 3; // Variable Shadowing
  }

  inner();
  console.log(a); // 1
}

outer();
console.log(a); // 1
