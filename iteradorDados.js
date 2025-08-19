const items = $input.all();
const output = [];

for (const item of items) {
  //Query na base de dados do TikTok
  output.push({
    perfil: item.json.profile,
    video: item.json.post,
    views: item.json.views,
    likes: item.json.likes,
    data_criação_do_post: item.json.created_at,
    data_da_postagem: item.json.posted_at,
    seguidores: item.json.followers,
    favoritos: item.json.favorites,
    

  });
}

return output;