const mongoose = require('mongoose')
require('dotenv').config();
const password = process.env.MONGODB_PWD;
const connection_string = `mongodb+srv://khalfan45:${password}@khalfan1.rd2nmx9.mongodb.net/?retryWrites=true&w=majority`;

main().catch(err => console.log(err));

async function main() {
    await mongoose.connect(connection_string)

        const userSchema = new mongoose.Schema({
            name: {
                type: String,
                required: true,
            },
            phone_number: String,
            age: Number,
            addresses: [
                {
                    street: String,
                    city: String,
                    state: String,
                }
            ],
            favorites: Array
        });

        const User = mongoose.model('User',userSchema);

        await User.create({
            name: "Urban Shix",
            phone: "0712345678",
            age: 88,
            addresses: [
                {street: "123 Main St", city: "New York", state: "NY"},
                {street: "456 Broadway", city: "New York", state: "NY"}
            ],
            favorites: ["Peanut Butter", "Chocolate", "Sherbert"]
        });
    //find all customers
    const docs = await User.find();
    console.log(docs);
}