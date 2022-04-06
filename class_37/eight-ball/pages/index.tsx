import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'
import Link from 'next/Link'
import { replies } from '../data'
import { useState } from 'react'
import Header from '../components/Header'

const Home: NextPage = () => {

    // const [reply, setReply] = useState('Ask Me Anything');
    const [answeredQuestions, setAnsweredQuestions] = useState([])

    function questionAskedHandler(event){
        event.preventDefault();
        const randomReply = replies[Math.floor(Math.random() * replies.length)]
        // alert(randomReply);
        // setReply(randomReply)

        const answeredQuestion = {
            question: event.target.question.value,
            reply: randomReply,
            id: answeredQuestions.length,
        }

        setAnsweredQuestions([...answeredQuestions, answeredQuestion]);
  }
    function getLatestReply() {
        if (answeredQuestions.length === 0){
            return 'Ask me anything'
        }

        return answeredQuestions[answeredQuestions.length -1].reply;
    }


  return (
    <div className="">
      <Head>
        <title>Eight Ball</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
        {/* <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
            <h1 className="text-4xl">Eight Ball</h1>
            <p>{ answeredQuestions.length } Answered Question</p>
        </header> */}

      <Header count={answeredQuestions.length}/>

      <main className="">
        <form onSubmit={ questionAskedHandler }className="flex w-1/2 p-2 mx-auto my-4 bg-gray-200" >
            <input name="question" className="flex-auto pl-1"></input>
            <button className="px-2 py-1 bg-gray-500 text-gray-50">Ask</button>
        </form>

        <div className="mx-auto my-4 bg-gray-900 rounded-full w-96 h-96">
            <div className="relative flex items-center justify-center w-48 h-48 rounded-full bg-gray-50 top-16 left-16">
                <p className="text-xl text-center">{ getLatestReply() }</p>
            </div>
        </div>

        <table className="w-1/2 mx-auto my-4">
            <thead>
                <tr>
                    <th className="border border-gray-700">No.</th>
                    <th className="border border-gray-700">Question</th>
                    <th className="border border-gray-700">Responce</th>
                </tr>
            </thead>
            <tbody>
            {answeredQuestions.map(item => {
                return (<tr>
                    <td className="pl-2 border border-gray-700">{item.id +1}</td>
                    <td className="pl-2 border border-gray-700">{item.question}</td>
                    <td className="pl-2 border border-gray-700">{item.reply}</td>
                    </tr>);
            })}
            </tbody>
        </table>
      </main>

      <footer className="p-4 mt-8 bg-gray-500 text-gray-50">
        <nav>
            <Link href="/careers">
                <a>Careers</a>
            </Link>

        </nav>
      </footer>
    </div>
  )
}

export default Home
