import React from 'react';
import Header from '../components/Header';
import Footer from '../components/Footer';

class About extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            content: "NFT is a type of digital asset that represents a wide range of unique tangible and intangible items, from collectible sports cards to virtual real estate and even digital sneakers."
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
                <div>{this.state.content}</div>
                <Footer />
            </div>
        );
    }
}

export default About;