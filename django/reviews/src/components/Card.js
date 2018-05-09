import React from 'react';
import { Card, CardImg, CardText, CardBody,
  CardTitle, CardSubtitle, Button, CardDeck, CardLink,
  CardGroup } from 'reactstrap';
import PropTypes from "prop-types";
import shortid from "shortid";
import DataProvider from "./DataProvider"
import LocationNamer from "./LocationNamer"
import UserNamer from "./UserNamer"

const cardStyle = {
  minWidth: "33%"
}

const NameEl = ({id}) => (
   <DataProvider endpoint="api/location/" render={data => <LocationNamer data={data.slice(id,id+1)} />} />
 );

const AuthorName = ({id}) => (
   <DataProvider endpoint="api/user/" render={data => <UserNamer data={data.slice(id,id+1)} />} />
 );

var i = -1;
function counter() {
  if (i = 1) {
    i = 0;
  } else {
  i = 1;
  }
  return i;
}
const uuid = shortid.generate;


const ReviewCard = ({ data, term }) =>  
  !data.length ? (
    <p>Nothing to show</p>
  ) : (
<div>
  <div>
    {term ? null : "All Reviews:"} 
  </div>
  <CardGroup>
    {data.map( (data, location) => (
        <Card style={cardStyle}>
            {/* <CardImg top width="100%" src="https://thumbs.dreamstime.com/b/beautiful-view-green-fields-meadows-sunset-tuscany-italy-46410906.jpg" alt="Card image cap" /> */}
                <CardBody>
                    <CardTitle key={uuid()}>{data.title}</CardTitle>
                    <CardSubtitle><AuthorName id={data.author}/></CardSubtitle>
                    <CardSubtitle><NameEl id={data.location}/></CardSubtitle>
                    <CardText>{data.text}</CardText>
                    <CardLink>Written by: {data.author}</CardLink><br/>
                    <Button href={"/reviews/"+data.slug+"/"}>Read More</Button>
                </CardBody>
            </Card> 
       ))}
 </CardGroup></div>);


export default ReviewCard;
