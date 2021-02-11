<?
/**
 * Class EmailAuthor
 * When ->update is called it should email the author of the blog post id.
 *
 */
class EmailAuthor implements SplObserver
{
    public function update(SplSubject $subject)
    {
        echo __METHOD__ . " Emailing the author of post id: " . $subject->post_id . " that someone commented with : " . $subject->comment_text . "\n";
    }
}
/**
 * Class EmailOtherCommentators
 * When ->update() is called it should email other comment authors who have also commented on this blog post
 */
class EmailOtherCommentators implements SplObserver
{
    public function update(SplSubject $subject)
    {
        echo __METHOD__ . " Emailing all other comment authors who commented on " . $subject->post_id . " that someone commented with : " . $subject->comment_text . "\n";
    }
}
/**
 * Class IncrementCommentCount
 * Add 1 to the comment count column for the blog post.
 *
 * update blogposts.comment_count = comment_count + 1 where id = ?
 */
class IncrementCommentCount implements SplObserver
{
    public function update(SplSubject $subject)
    {
        echo __METHOD__ . " Updating comment count to + 1 for blog post id: " . $subject->post_id ."\n";
    }
}