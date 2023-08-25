import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      content: 'Welcome to our NFT platform!'
    };
  }

  componentDidMount() {
    this.setState({
      content: this.state.content.replace('NFT', 'Independent Game')
    });
  }

  render() {
    return (
      <div>
        <Header />
        <main>
          <h1>{this.state.content}</h1>
        </main>
        <Footer />
      </div>
    );
  }
}

export default Home;