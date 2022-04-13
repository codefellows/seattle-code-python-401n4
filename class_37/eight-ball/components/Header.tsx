import type { NextPage } from 'next'

const Header: NextPage = (props) => {

    return(
        <header className="flex items-center justify-between p-4 bg-gray-500 text-gray-50">
            <h1 className="text-4xl">Eight Ball</h1>
            <p>{ props.count } Answered Question</p>
        </header>
        )
    }

export default Header
