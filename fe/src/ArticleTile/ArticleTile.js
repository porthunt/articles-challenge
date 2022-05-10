import React from "react";
import Card from "react-bootstrap/Card";
import Col from "react-bootstrap/Col";
import { Bookmark, BookmarkFill, Eye } from "react-bootstrap-icons";

const ArticleTile = (props) => {
  return (
    <Col className="d-flex mt-3">
      <Card
        id={props.article._id.$oid}
        key={props.article._id.$oid}
        className="flex-fill"
        style={{ width: "18rm" }}
      >
        <Card.Body>
          <Card.Title className="small">{props.article.title}</Card.Title>
          <Card.Subtitle className="text-muted small">
            {props.article.journal}
          </Card.Subtitle>
          <Card.Text className="text-muted small">
            {props.article.publish_time}
          </Card.Text>
          <Card.Text className="text-muted small">
            {props.article.authors}
          </Card.Text>
        </Card.Body>
        <Card.Footer className="text-muted" style={{ textAlign: "right" }}>
          <Card.Link href={props.article.url} target="_blank">
            <Eye />
          </Card.Link>
          <Card.Link
            href="#"
            onClick={() =>
              props.inReadingList
                ? props.removeFromReadingList(props.article._id.$oid)
                : props.addToReadingList(props.article._id.$oid)
            }
          >
            {props.inReadingList ? <BookmarkFill /> : <Bookmark />}
          </Card.Link>
        </Card.Footer>
      </Card>
    </Col>
  );
};

export default ArticleTile;
