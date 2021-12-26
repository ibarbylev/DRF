import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author';
import axios from 'axios'

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8080/api/Authors/').then(
      response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors
          }
        )
      }
    ).catch(error => console.log(error))
//    const authors = [
//      {
//        'first_name': 'Владимир',
//        'last_name': 'Буковский',
//        'birthday_year': 1942,
//      },
//      {
//        'first_name': 'Владимир',
//        'last_name': 'Набоков',
//        'birthday_year': 1899,
//      }
//    ]
  }

  render() {
    return (
      <div>
        <AuthorList authors={this.state.authors}/>
      </div>
    );
  }
}

export default App;
