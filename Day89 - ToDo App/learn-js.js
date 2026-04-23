// kalo mau export, harus bikin kayak gini
export default function doSomething(){

}
function doSomething(){

}

const doSomething = () => {

}

// react components is like this
// const MyComponent = () => {
//     return <div></div>
// }

<button onClick = { () => 
    {console.log("hello world")}}>
</button>


// ternary operator
let age = 10;
// && this is true, || this is false in ternary
let name = age > 5 && "Pedro";
let name = age > 5 ? "Pedro": "Jack";

const Component = () => {
    return age >10 ? <div>pedro</div>: <div>alejandro</div>
}

// kalo misalnya mau assign, bisa pek langsung nama
const name = 'pedro'
const person = {
    name,
    age: 20,
    isMarried: false,
};

// kalo misal kita mau grab each variable harus kek gini
const name2 = person.name
const age = person.age
const isMarried = person.isMarried

// di react bisa kek gini
const {name3, age, isMarried} = person

// inherit semuanya kecuali nama
const person2 = {...person, name: "Jack"};

const names = ['pedrp', 'jack', 'jessica', 'jack', 'jack'];
const name2 = [...names, 'joel'];

// functions (map, filter, reduce)
names.map((name) => {
    return name+'1';
    return <h1>{name}</h1>
});

// how to remove jack misalnya
names.filter((name) => {
    return name !== 'jack';
});

// learn async, await-promise, fetch