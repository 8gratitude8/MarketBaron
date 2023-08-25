import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

class Contact extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            content: "Contact us for more information about our NFTs."
        };
    }

    componentDidMount() {
        this.setState({
            content: this.state.content.replace(/NFT/g, 'Independent Game')
        });
    }

    render() {
        return (
            <div>
                <Header />
                <p>{this.state.content}</p>
                <Footer />
            </div>
        );
    }
}

export default Contact;