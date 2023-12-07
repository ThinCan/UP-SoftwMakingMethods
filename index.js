const webdriver = require('selenium-webdriver');
const By = webdriver.By;
const until = webdriver.until;

const driver = new webdriver.Builder()
    .forBrowser('firefox')
    .build();

async function test() {
    try {
        await driver.get('http://localhost:5500');

        const element1 = await driver.wait(until.elementLocated(By.css('.book-row span:nth-child(1)')), 10000);
        const text1 = await element1.getText();

        const element2 = await driver.wait(until.elementLocated(By.css('.book-row span:nth-child(2)')), 10000);
        const text2 = await element2.getText();

        const element3 = await driver.wait(until.elementLocated(By.css('.book-row span:nth-child(3)')), 10000);
        const text3 = await element3.getText();

        if (text1 === 'a' && text2 === 'a' && text3 === 'c') {
            console.log('The book-row element has three spans next to each other with values: a, b, c');
        } else {
            throw 'The book-row element does not have three spans next to each other with values: a, b, c';
        }

    } finally {
        await driver.quit();
    }
}

test()
