const { fake } = require('faker');
var faker = require('faker');
var fakerRu = require('faker');



const genData = function () {
  fakerRu.locale = 'en';
  const list = []
  for (let i=0; i<15; i++) {
    list.push({
      foreign: faker.lorem.word(),
      meaning: '',
      context: faker.lorem.sentence(20)
    })
  }
  fakerRu.locale = 'ru';
  list.forEach(i => {
    i.meaning = fakerRu.lorem.word();
  })
  return list
}

const data = genData()

console.log(data);