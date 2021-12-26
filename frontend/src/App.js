import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author';

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'authors': []
    }
  }

  componentDidMount() {
    const authors = [
      {
        'first_name': 'Владимир',
        'last_name': 'Буковский',
        'birthday_year': 1942,
      },
      {
        'first_name': 'Владимир',
        'last_name': 'Набоков',
        'birthday_year': 1899,
      }
    ]
    this.setState(
      {
        'authors': authors
      }
    )
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
