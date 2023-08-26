import React from 'react';
import styled from 'styled-components'; // Import styled-components

const HeaderContainer = styled.header`
    background-color: #405de6;
    color: white;
    text-align: center;
    padding: 1rem 0;
`;

function Header() {
    return (
        <HeaderContainer>
            {/* Your header content */}
        </HeaderContainer>
    );
}

export default Header;
