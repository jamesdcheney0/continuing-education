return {
	"github/copilot.vim",
	config = function()
		vim.g.copilot_filetypes = {
			markdown = false,
			yaml = false,
		}
	end,
}

vim.api.nvim_create_autocmd("FileType", {
  pattern = "markdown",
  callback = function()
    local cmp_ok, cmp = pcall(require, "cmp")
    if cmp_ok then
      cmp.setup.buffer { enabled = false }
    end
  end,
})

