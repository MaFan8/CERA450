const {Configuration, OpenAIApi} = require('openai')
require('dotenv').config();

const Configuration = new Configuration({
    apiKey:  process.env.OPEN_AI_KEY
});

const openai = new OpenAIApi(configuration);

moduele.exports = openai