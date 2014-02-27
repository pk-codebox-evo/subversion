import sys, re, os, time, shutil, logging

logger = logging.getLogger()
from svntest import err, wc

from prop_tests import binary_mime_type_on_text_file_warning
from svntest.verify import make_diff_header, make_no_diff_deleted_header, \
                           make_diff_header, make_no_diff_deleted_header, \
                           make_git_diff_header, make_diff_prop_header, \
                           make_diff_prop_val, make_diff_prop_deleted, \
                           make_diff_prop_added, make_diff_prop_modified
      logger.warn('Sought: %s' % excluded)
      logger.warn('Found:  %s' % line)
    None, 'diff', '-r', '1', sbox.ospath('A/D'))
    None, 'diff', '-r', '1', '-N', sbox.ospath('A/D'))
    None, 'diff', '-r', '1', sbox.ospath('A/D/G'))
  svntest.main.file_append(sbox.ospath('A/D/foo'), "a new file")
  svntest.actions.run_and_verify_svn(None, None,
                                     'svn: E155010: .*foo\' was not found.',
                                     'diff', sbox.ospath('A/D/foo'))
  theta_path = sbox.ospath('A/theta')
  mu_path = sbox.ospath('A/mu')
  mu_new = sbox.ospath('A/mu.new').replace('\\','/')

  expected_output = [
    'Index: %s\n' % mu_new,
    '===================================================================\n',
    '--- %s\t(.../mu)\t(revision 1)\n' % mu_new,
    '+++ %s\t(.../mu.new)\t(working copy)\n' % mu_new,
    '@@ -1 +1,3 @@\n',
    ' This is the file \'mu\'.\n',
    '+\n',
    '+Actually, it\'s a new mu.\n',
    '\ No newline at end of file\n',
  ]

  svntest.actions.run_and_verify_svn(None, expected_output, [],
  iota_path = sbox.ospath('iota')
  newfile_path = sbox.ospath('A/D/newfile')
  mu_path = sbox.ospath('A/mu')
  A_path = sbox.ospath('A')
  mu_path = sbox.ospath('A/mu')
@Issue(2873)
  A_alpha = sbox.ospath('A/B/E/alpha')
  A2_alpha = sbox.ospath('A2/B/E/alpha')
  A_alpha = sbox.ospath('A/B/E/alpha')
  A2_alpha = sbox.ospath('A2/B/E/alpha')
  A_path = sbox.ospath('A')
  iota_path = sbox.ospath('iota')
  iota_copy_path = sbox.ospath('A/iota')
  iota_path = sbox.ospath('iota')
  prefix_path = sbox.ospath('prefix_mydir')
  other_prefix_path = sbox.ospath('prefix_other')
    logger.warn("src is '%s' instead of '%s' and dest is '%s' instead of '%s'" %

  iota_path = sbox.ospath('iota')
  "show diffs for binary files"
  iota_path = sbox.ospath('iota')
  svntest.main.run_svn(binary_mime_type_on_text_file_warning,
  # Check that we get diff when the first, the second and both files
  # are marked as binary.  First we'll use --force.  Then we'll use
  # the configuration option 'diff-ignore-content-type'.
  for opt in ['--force',
              '--config-option=config:miscellany:diff-ignore-content-type=yes']:
    for range in ['-r1:2', '-r2:1', '-r2:3']:
      exit_code, stdout, stderr = svntest.main.run_svn(None, 'diff', range,
                                                       iota_path, opt)
      for line in stdout:
        if (re_nodisplay.match(line)):
          raise svntest.Failure
  # Check a wc->wc diff
  # Check a repos->wc diff of the moved-here node before commit
  exit_code, diff_output, err_output = svntest.main.run_svn(
    None, 'diff', '-r', '1', '--show-copies-as-adds',
    os.path.join('A', 'D', 'I'))
  if check_diff_output(diff_output,
                       os.path.join('A', 'D', 'I', 'pi'),
                       'A') :
    raise svntest.Failure

  # Check a repos->wc diff of the moved-away node before commit
  exit_code, diff_output, err_output = svntest.main.run_svn(
    None, 'diff', '-r', '1', os.path.join('A', 'D', 'G'))
  if check_diff_output(diff_output,
                       os.path.join('A', 'D', 'G', 'pi'),
                       'D') :
    raise svntest.Failure

  # Each of these returns an expected diff as a list of lines.
  def add_diff_A(r1, r2):
    return (make_diff_header("A", r1, r2) +
            make_diff_prop_header("A") +
            make_diff_prop_added("dirprop", "r2value"))

  def add_diff_iota(r1, r2):
    return (make_diff_header("iota", r1, r2) +
            make_diff_prop_header("iota") +
            make_diff_prop_added("fileprop", "r2value"))

  def del_diff_A(r1, r2):
    return (make_diff_header("A", r1, r2) +
            make_diff_prop_header("A") +
            make_diff_prop_deleted("dirprop", "r2value"))

  def del_diff_iota(r1, r2):
    return (make_diff_header("iota", r1, r2) +
            make_diff_prop_header("iota") +
            make_diff_prop_deleted("fileprop", "r2value"))

  # Each of these is an expected diff as a list of lines.
  expected_output_r1_r2 =   (add_diff_A('revision 1', 'revision 2') +
                             add_diff_iota('revision 1', 'revision 2'))
  expected_output_r2_r1 =   (del_diff_A('revision 2', 'revision 1') +
                             del_diff_iota('revision 2', 'revision 1'))
  expected_output_r1 =      (add_diff_A('revision 1', 'working copy') +
                             add_diff_iota('revision 1', 'working copy'))
  expected_output_base_r1 = (del_diff_A('working copy', 'revision 1') +
                             del_diff_iota('working copy', 'revision 1'))
                                                "nonexistent") + [
                                                "nonexistent") + [
  "@@ -1 +0,0 @@\n",
  "-xxx\n",
  expected_output_base_r2 = make_diff_header("foo", "nonexistent",
  "@@ -0,0 +1 @@\n",
  "+xxx\n",
  expected_output_r1_base = make_diff_header("foo", "nonexistent",
                                                "nonexistent") + [
  expected_output_base_working[3] = "+++ foo\t(nonexistent)\n"
  svntest.actions.run_and_verify_svn2(None, None,
                                      binary_mime_type_on_text_file_warning, 0,
                                      'propset', 'svn:mime-type',
  diff_X_r1_base = make_diff_header("X", "nonexistent",
  diff_X_base_r3 = make_diff_header("X", "nonexistent",
  diff_foo_r1_base = make_diff_header("foo", "nonexistent",
  diff_foo_base_r3 = make_diff_header("foo", "nonexistent",
  diff_X_bar_r1_base = make_diff_header("X/bar", "nonexistent",
  diff_X_bar_base_r3 = make_diff_header("X/bar", "nonexistent",
  expected_output_r1_BASE = make_diff_header("X/bar", "nonexistent",
  expected_output_r1_WORKING = make_diff_header("X/bar", "nonexistent",
                                                "working copy") + [
  svntest.main.file_write(sbox.ospath('A/mu'),
  C_path = sbox.ospath('A/C')
  D_path = sbox.ospath('A/D')
  sbox.wc_dir = ''
  B_path = os.path.join('A', 'B')
  sbox.simple_propset('foo1', 'bar1', '.')
  sbox.simple_propset('foo2', 'bar2', 'iota')
  sbox.simple_propset('foo3', 'bar3', 'A')
  sbox.simple_propset('foo4', 'bar4', 'A/B')

  def create_expected_diffs(r1, r2):
    diff_dot = \
      make_diff_header(".", r1, r2) + \
      make_diff_prop_header(".") + \
      make_diff_prop_added("foo1", "bar1")
    diff_iota = \
      make_diff_header('iota', r1, r2) + \
      make_diff_prop_header("iota") + \
      make_diff_prop_added("foo2", "bar2")
    diff_A = \
      make_diff_header('A', r1, r2) + \
      make_diff_prop_header("A") + \
      make_diff_prop_added("foo3", "bar3")
    diff_AB = \
      make_diff_header(B_path, r1, r2) + \
      make_diff_prop_header("A/B") + \
      make_diff_prop_added("foo4", "bar4")

    expected = {}
    expected['empty'] =      svntest.verify.UnorderedOutput(diff_dot)
    expected['files'] =      svntest.verify.UnorderedOutput(diff_dot +
                                                            diff_iota)
    expected['immediates'] = svntest.verify.UnorderedOutput(diff_dot +
                                                            diff_iota +
                                                            diff_A)
    expected['infinity'] =   svntest.verify.UnorderedOutput(diff_dot +
                                                            diff_iota +
                                                            diff_A +
                                                            diff_AB)
    return expected
  expected_diffs = create_expected_diffs("revision 1", "working copy")
  for depth in ['empty', 'files', 'immediates', 'infinity']:
    svntest.actions.run_and_verify_svn(None, expected_diffs[depth], [],
                                       'diff', '--depth', depth)
  expected_diffs = create_expected_diffs("revision 1", "revision 2")
  for depth in ['empty', 'files', 'immediates', 'infinity']:
    svntest.actions.run_and_verify_svn(None, expected_diffs[depth], [],
                                       'diff', '-c2', '--depth', depth)

  def create_expected_repos_wc_diffs():
    diff_AB = \
      make_diff_header("A/B", "revision 2", "working copy") + \
      make_diff_prop_header("A/B") + \
      make_diff_prop_modified("foo4", "bar4", "baz4")
    diff_A = \
      make_diff_header("A", "revision 2", "working copy") + \
      make_diff_prop_header("A") + \
      make_diff_prop_modified("foo3", "bar3", "baz3")
    diff_mu = \
      make_diff_header("A/mu", "revision 2", "working copy") + [
      "@@ -1 +1,2 @@\n",
      " This is the file 'mu'.\n",
      "+new text\n",]
    diff_iota = \
      make_diff_header("iota", "revision 2", "working copy") + [
      "@@ -1 +1,2 @@\n",
      " This is the file 'iota'.\n",
      "+new text\n",
      ] + make_diff_prop_header("iota") + \
      make_diff_prop_modified("foo2", "bar2", "baz2")
    diff_dot = \
      make_diff_header(".", "revision 2", "working copy") + \
      make_diff_prop_header(".") + \
      make_diff_prop_modified("foo1", "bar1", "baz1")

    expected = {}
    expected['empty'] = svntest.verify.UnorderedOutput(diff_dot)
    expected['files'] = svntest.verify.UnorderedOutput(diff_iota +
                                                       diff_dot)
    expected['immediates'] = svntest.verify.UnorderedOutput(diff_A +
                                                            diff_iota +
                                                            diff_dot)
    expected['infinity'] = svntest.verify.UnorderedOutput(diff_AB +
                                                          diff_A +
                                                          diff_mu +
                                                          diff_iota +
                                                          diff_dot)
    return expected
  sbox.simple_propset('foo1', 'baz1', '.')
  sbox.simple_propset('foo2', 'baz2', 'iota')
  sbox.simple_propset('foo3', 'baz3', 'A')
  sbox.simple_propset('foo4', 'baz4', 'A/B')
  expected_diffs = create_expected_repos_wc_diffs()
  for depth in ['empty', 'files', 'immediates', 'infinity']:
    svntest.actions.run_and_verify_svn(None, expected_diffs[depth], [],
                                       'diff', '-rHEAD', '--depth', depth)
  diff_repos_wc = make_diff_header("A/mucopy", "revision 2", "nonexistent")
  svntest.main.file_append(sbox.ospath('A/mu'), "New mu content")
                       sbox.ospath('iota'))
  tau_path = sbox.ospath('A/D/G/tau')
  newfile_path = sbox.ospath('newfile')
  svntest.main.run_svn(None, "mkdir", sbox.ospath('newdir'))
  # 3) Test working copy summarize
  paths = ['A/mu', 'iota', 'A/D/G/tau', 'newfile', 'A/B/lambda',
           'newdir',]
  items = ['modified', 'none', 'modified', 'added', 'deleted', 'added',]
  kinds = ['file','file','file','file','file', 'dir',]
  props = ['none', 'modified', 'modified', 'none', 'none', 'none',]

  svntest.actions.run_and_verify_diff_summarize_xml(
    [], wc_dir, paths, items, props, kinds, wc_dir)

  paths_iota = ['iota',]
  items_iota = ['none',]
  kinds_iota = ['file',]
  props_iota = ['modified',]
    [], wc_dir, paths_iota, items_iota, props_iota, kinds_iota, '-c2',
    sbox.ospath('iota'))
  iota_path = sbox.ospath('iota')
  make_file_edit_del_add(A)
  make_file_edit_del_add(A2)

  # Diff Path of A against working copy of A2.
  # Output using arbritrary diff handling should be empty.
  expected_output = []
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--old', A, '--new', A2)
  iota_path = sbox.ospath('iota')
  mu_path = sbox.ospath('A/mu')
  new_path = sbox.ospath('new')
  lambda_path = sbox.ospath('A/B/lambda')
  lambda_copied_path = sbox.ospath('A/B/lambda_copied')
  alpha_path = sbox.ospath('A/B/E/alpha')
  alpha_copied_path = sbox.ospath('A/B/E/alpha_copied')
  expected_output = make_git_diff_header(
                         alpha_copied_path, "A/B/E/alpha_copied",
                         "nonexistent", "working copy",
                         copyfrom_path="A/B/E/alpha",
                         copyfrom_rev='1', cp=True,
                         text_changes=True) + [
    "@@ -1 +1,2 @@\n",
    " This is the file 'alpha'.\n",
    "+This is a copy of 'alpha'.\n",
  ] + make_git_diff_header(lambda_copied_path,
                                         copyfrom_path="A/B/lambda",
                                         copyfrom_rev='1', cp=True,
                                         "nonexistent",
  ] + make_git_diff_header(iota_path, "iota", "revision 1",
  ] + make_git_diff_header(new_path, "new", "nonexistent",
                           "working copy", add=True) + [
    "@@ -0,0 +1 @@\n",
    "+This is the file 'new'.\n",
  expected = expected_output
                                         "revision 1", "nonexistent",
                           "revision 1", "nonexistent",
                           "revision 1", "nonexistent",
                           copyfrom_path="A/D/G/pi", copyfrom_rev='1', text_changes=False) \
                         copyfrom_path="A/D/G/rho", copyfrom_rev='1', text_changes=False) \
                         copyfrom_path="A/D/G/tau", copyfrom_rev='1', text_changes=False)
  expected = expected_output
  iota_path = sbox.ospath('iota')
  mu_path = sbox.ospath('A/mu')
  new_path = sbox.ospath('new')
  expected_output = make_git_diff_header(new_path, "new", "nonexistent",
  ] + make_git_diff_header(mu_path, "A/mu", "revision 1", "nonexistent",
  iota_path = sbox.ospath('iota')
  mu_path = sbox.ospath('A/mu')
  new_path = sbox.ospath('new')
                                         "nonexistent",
    ] + make_git_diff_header("new", "new", "nonexistent", "revision 2",
  iota_path = sbox.ospath('iota')
  iota_path = sbox.ospath('iota')
  iota_path = sbox.ospath('iota')
  new_path = sbox.ospath('new')
  expected_output = make_git_diff_header(new_path, "new", "nonexistent",
  iota_path = sbox.ospath('iota')
  new_path = sbox.ospath('new')
                                         "nonexistent", "working copy",
                                         "revision 2", "working copy",
@Issue(4010)
def diff_correct_wc_base_revnum(sbox):
  "diff WC-WC shows the correct base rev num"

  sbox.build()
  wc_dir = sbox.wc_dir
  iota_path = sbox.ospath('iota')
  svntest.main.file_write(iota_path, "")

  # Commit a local mod, creating rev 2.
  expected_output = svntest.wc.State(wc_dir, {
    'iota' : Item(verb='Sending'),
    })
  expected_status = svntest.actions.get_virginal_state(wc_dir, 1)
  expected_status.add({
    'iota' : Item(status='  ', wc_rev=2),
    })
  svntest.actions.run_and_verify_commit(wc_dir, expected_output,
                                        expected_status, None, wc_dir)

  # Child's base is now 2; parent's is still 1.
  # Make a local mod.
  svntest.main.run_svn(None, 'propset', 'svn:keywords', 'Id', iota_path)

  expected_output = make_git_diff_header(iota_path, "iota",
                                         "revision 2", "working copy") + \
                    make_diff_prop_header("iota") + \
                    make_diff_prop_added("svn:keywords", "Id")

  # Diff the parent.
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff',
                                     '--git', wc_dir)

  # The same again, but specifying the target explicity. This should
  # give the same output.
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff',
                                     '--git', iota_path)

    'A' : Item(verb='Sending'),
  expected_status.tweak('A', wc_rev=2)
  sbox.simple_propset('k','v', '', 'A')
  expected_output = make_git_diff_header("A", "A", "revision 1",
                                         "revision 2",
                                         add=False, text_changes=False) + \
                    make_diff_prop_header("A") + \
                    make_diff_prop_added("k", "v") + \
                    make_git_diff_header(".", "", "revision 1",
                    make_diff_prop_added("k", "v")
  A_path = sbox.ospath('A')
  B_abs_path = os.path.abspath(sbox.ospath('A/B'))
def diff_two_working_copies(sbox):
  "diff between two working copies"
  sbox.build()
  wc_dir = sbox.wc_dir

  # Create a pristine working copy that will remain mostly unchanged
  wc_dir_old = sbox.add_wc_path('old')
  svntest.main.run_svn(None, 'co', sbox.repo_url, wc_dir_old)
  # Add a property to A/B/F in the pristine working copy
  svntest.main.run_svn(None, 'propset', 'newprop', 'propval-old\n',
                       os.path.join(wc_dir_old, 'A', 'B', 'F'))

  # Make changes to the first working copy:

  # removed nodes
  sbox.simple_rm('A/mu')
  sbox.simple_rm('A/D/H')

  # new nodes
  sbox.simple_mkdir('newdir')
  svntest.main.file_append(sbox.ospath('newdir/newfile'), 'new text\n')
  sbox.simple_add('newdir/newfile')
  sbox.simple_mkdir('newdir/newdir2') # should not show up in the diff

  # modified nodes
  sbox.simple_propset('newprop', 'propval', 'A/D')
  sbox.simple_propset('newprop', 'propval', 'A/D/gamma')
  svntest.main.file_append(sbox.ospath('A/B/lambda'), 'new text\n')

  # replaced nodes (files vs. directories) with property mods
  sbox.simple_rm('A/B/F')
  svntest.main.file_append(sbox.ospath('A/B/F'), 'new text\n')
  sbox.simple_add('A/B/F')
  sbox.simple_propset('newprop', 'propval-new\n', 'A/B/F')
  sbox.simple_rm('A/D/G/pi')
  sbox.simple_mkdir('A/D/G/pi')
  sbox.simple_propset('newprop', 'propval', 'A/D/G/pi')

  src_label = os.path.basename(wc_dir_old)
  dst_label = os.path.basename(wc_dir)
  expected_output = make_diff_header('newdir/newfile', 'nonexistent',
                                     'working copy',
                                     src_label, dst_label) + [
                      "@@ -0,0 +1 @@\n",
                      "+new text\n",
                    ] + make_diff_header('A/mu', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'mu'.\n",
                    ] + make_diff_header('A/B/F', 'nonexistent',
                                         'working copy',
                                         src_label, dst_label) + [
                      "@@ -0,0 +1 @@\n",
                      "+new text\n",
                    ] + make_diff_prop_header('A/B/F') + \
                        make_diff_prop_added("newprop",
                                                "propval-new\n") + \
                    make_diff_header('A/B/lambda', 'working copy',
                                         'working copy',
                                         src_label, dst_label) + [
                      "@@ -1 +1,2 @@\n",
                      " This is the file 'lambda'.\n",
                      "+new text\n",
                    ] + make_diff_header('A/D', 'working copy', 'working copy',
                                         src_label, dst_label) + \
                        make_diff_prop_header('A/D') + \
                        make_diff_prop_added("newprop", "propval") + \
                    make_diff_header('A/D/gamma', 'working copy',
                                         'working copy',
                                         src_label, dst_label) + \
                        make_diff_prop_header('A/D/gamma') + \
                        make_diff_prop_added("newprop", "propval") + \
                    make_diff_header('A/D/G/pi', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'pi'.\n",
                    ] + make_diff_header('A/D/G/pi', 'nonexistent',
                                         'working copy',
                                         src_label, dst_label) + \
                        make_diff_prop_header('A/D/G/pi') + \
                        make_diff_prop_added("newprop", "propval") + \
                    make_diff_header('A/D/H/chi', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'chi'.\n",
                    ] + make_diff_header('A/D/H/omega', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'omega'.\n",
                    ] + make_diff_header('A/D/H/psi', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'psi'.\n",
                    ] + make_diff_header('A/B/F', 'working copy',
                                         'nonexistent',
                                         src_label, dst_label) + \
                        make_diff_prop_header('A/B/F') + \
                        make_diff_prop_deleted('newprop', 'propval-old\n')


  # Files in diff may be in any order. #### Not any more, but test order is wrong.
  expected_output = svntest.verify.UnorderedOutput(expected_output)
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--old', wc_dir_old,
                                     '--new', wc_dir)
  expected_output = make_diff_header("chi", "revision 1", "nonexistent") + [
                                         "nonexistent") + [
                                         "nonexistent") + [
def diff_arbitrary_files_and_dirs(sbox):
  "diff arbitrary files and dirs"
  sbox.build()
  wc_dir = sbox.wc_dir

  # diff iota with A/mu
  expected_output = make_diff_header("iota", "working copy", "working copy",
                                     "iota", "A/mu") + [
                      "@@ -1 +1 @@\n",
                      "-This is the file 'iota'.\n",
                      "+This is the file 'mu'.\n"
                    ]
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--old', sbox.ospath('iota'),
                                     '--new', sbox.ospath('A/mu'))

  # diff A/B/E with A/D
  expected_output = make_diff_header("G/pi", "nonexistent", "working copy",
                                     "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'pi'.\n"
                    ] + make_diff_header("G/rho", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'rho'.\n"
                    ] + make_diff_header("G/tau", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'tau'.\n"
                    ] + make_diff_header("H/chi", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'chi'.\n"
                    ] + make_diff_header("H/omega", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'omega'.\n"
                    ] + make_diff_header("H/psi", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'psi'.\n"
                    ] + make_diff_header("alpha", "working copy",
                                         "nonexistent", "B/E", "D") + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'alpha'.\n"
                    ] + make_diff_header("beta", "working copy",
                                         "nonexistent", "B/E", "D") + [
                      "@@ -1 +0,0 @@\n",
                      "-This is the file 'beta'.\n"
                    ] + make_diff_header("gamma", "nonexistent",
                                         "working copy", "B/E", "D") + [
                      "@@ -0,0 +1 @@\n",
                      "+This is the file 'gamma'.\n"
                    ]

  # Files in diff may be in any order.
  expected_output = svntest.verify.UnorderedOutput(expected_output)
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--old', sbox.ospath('A/B/E'),
                                     '--new', sbox.ospath('A/D'))

def diff_properties_only(sbox):
  "diff --properties-only"

  sbox.build()
  wc_dir = sbox.wc_dir

  expected_output = \
    make_diff_header("iota", "revision 1", "revision 2") + \
    make_diff_prop_header("iota") + \
    make_diff_prop_added("svn:eol-style", "native")

  expected_reverse_output = \
    make_diff_header("iota", "revision 2", "revision 1") + \
    make_diff_prop_header("iota") + \
    make_diff_prop_deleted("svn:eol-style", "native")

  expected_rev1_output = \
    make_diff_header("iota", "revision 1", "working copy") + \
    make_diff_prop_header("iota") + \
    make_diff_prop_added("svn:eol-style", "native")

  # Make a property change and a content change to 'iota'
  # Only the property change should be displayed by diff --properties-only
  sbox.simple_propset('svn:eol-style', 'native', 'iota')
  svntest.main.file_append(sbox.ospath('iota'), 'new text')

  sbox.simple_commit() # r2

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--properties-only', '-r', '1:2',
                                     sbox.repo_url + '/iota')

  svntest.actions.run_and_verify_svn(None, expected_reverse_output, [],
                                     'diff', '--properties-only', '-r', '2:1',
                                     sbox.repo_url + '/iota')

  os.chdir(wc_dir)
  svntest.actions.run_and_verify_svn(None, expected_rev1_output, [],
                                     'diff', '--properties-only', '-r', '1',
                                     'iota')

  svntest.actions.run_and_verify_svn(None, expected_rev1_output, [],
                                     'diff', '--properties-only',
                                     '-r', 'PREV', 'iota')

def diff_properties_no_newline(sbox):
  "diff props; check no-newline-at-end messages"

  sbox.build()
  old_cwd = os.getcwd()
  os.chdir(sbox.wc_dir)
  sbox.wc_dir = ''

  no_nl = "\\ No newline at end of property\n"
  propchange_header = "Modified: p.*\n"

  subtests = [
    ('p1', 'val1',   'val2'  ),
    ('p2', 'val1',   'val2\n'),
    ('p3', 'val1\n', 'val2'  ),
    ('p4', 'val1\n', 'val2\n'),
  ]

  # The "before" state.
  for pname, old_val, new_val in subtests:
    sbox.simple_propset(pname, old_val, 'iota')
  sbox.simple_commit() # r2

  # Test one change at a time. (Because, with multiple changes, the order
  # may not be predictable.)
  for pname, old_val, new_val in subtests:
    expected_output = \
      make_diff_header("iota", "revision 2", "working copy") + \
      make_diff_prop_header("iota") + \
      make_diff_prop_modified(pname, old_val, new_val)

    sbox.simple_propset(pname, new_val, 'iota')
    svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff')
    svntest.actions.run_and_verify_svn(None, None, [], 'revert', 'iota')

  os.chdir(old_cwd)

def diff_arbitrary_same(sbox):
  "diff arbitrary files and dirs but same"

  sbox.build(read_only = True)

  sbox.simple_propset('k', 'v', 'A', 'A/mu', 'A/D/G/pi')

  svntest.main.file_write(sbox.ospath('A/mu'), "new mu")

  sbox.simple_copy('A', 'A2')

  svntest.actions.run_and_verify_svn(None, [], [],
                                     'diff',
                                     '--old', sbox.ospath('A'),
                                     '--new', sbox.ospath('A2'))

  svntest.actions.run_and_verify_svn(None, [], [],
                                     'diff', '--summarize',
                                     '--old', sbox.ospath('A'),
                                     '--new', sbox.ospath('A2'))

def simple_ancestry(sbox):
  "diff some simple ancestry changes"

  sbox.build()
  sbox.simple_copy('A/B/E', 'A/B/E_copied')
  sbox.simple_copy('A/D/G/pi', 'A/D/G/pi-2')
  sbox.simple_copy('A/D/G/rho', 'A/D/G/rho-2')
  sbox.simple_rm('A/B/F', 'A/B/E', 'A/D/G/rho', 'A/D/G/tau')
  sbox.simple_add_text('new', 'new')

  line = '===================================================================\n'

  expected_output = svntest.verify.UnorderedOutput([
    'Index: %s (added)\n' % sbox.path('new'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/E_copied/beta'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/E_copied/alpha'),
    line,
    'Index: %s (added)\n' % sbox.path('A/D/G/pi-2'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/rho'),
    line,
    'Index: %s (added)\n' % sbox.path('A/D/G/rho-2'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/tau'),
    line,
  ])

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', sbox.wc_dir,
                                        '-r', '1',
                                        '--notice-ancestry',
                                        '--no-diff-deleted',
                                        '--show-copies-as-adds',
                                        '--no-diff-added')

  # And try the same thing in reverse
  sbox.simple_commit()
  sbox.simple_update(revision=1)

  expected_output = svntest.verify.UnorderedOutput([
    'Index: %s (deleted)\n' % sbox.path('new'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E_copied/beta'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E_copied/alpha'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/pi-2'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/D/G/rho'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/rho-2'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/D/G/tau'),
    line,
  ])

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', sbox.wc_dir,
                                        '-r', 'HEAD',
                                        '--notice-ancestry',
                                        '--no-diff-deleted',
                                        '--show-copies-as-adds',
                                        '--no-diff-added')

  # Now introduce a replacements and some delete-deletes
  sbox.simple_update()
  sbox.simple_mkdir('A/B/E')
  sbox.simple_add_text('New alpha', 'A/B/E/alpha')
  sbox.simple_add_text('New beta', 'A/B/E/beta')
  sbox.simple_add_text('New rho', 'A/D/G/rho')
  sbox.simple_add_text('New tau', 'A/D/G/tau')
  sbox.simple_rm('A/B/E_copied', 'A/D/G/pi-2', 'A/D/G/rho-2')

  expected_output = svntest.verify.UnorderedOutput([
    'Index: %s (added)\n'   % sbox.path('new'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/rho'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/D/G/rho'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/D/G/tau'),
    line,
    'Index: %s (added)\n'   % sbox.path('A/D/G/tau'),
    line,
  ])

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', sbox.wc_dir,
                                        '-r', '1',
                                        '--notice-ancestry',
                                        '--no-diff-deleted',
                                        '--show-copies-as-adds',
                                        '--no-diff-added')

  sbox.simple_commit()
  sbox.simple_update()

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', sbox.wc_dir,
                                        '-r', '1',
                                        '--notice-ancestry',
                                        '--no-diff-deleted',
                                        '--show-copies-as-adds',
                                        '--no-diff-added')

def local_tree_replace(sbox):
  "diff a replaced tree"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_add_text('extra', 'A/B/F/extra')
  sbox.simple_commit()

  svntest.actions.run_and_verify_svn(None, None, [],
                                     'rm', '--keep-local',
                                     sbox.ospath('A/B'))
  svntest.actions.run_and_verify_svn(None, None, [],
                                     'add', sbox.ospath('A/B'))

  # And now check with ancestry

  line = '===================================================================\n'

  expected_output = svntest.verify.UnorderedOutput([
    'Index: %s (deleted)\n' % sbox.path('A/B/lambda'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (deleted)\n' % sbox.path('A/B/F/extra'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/lambda'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/E/alpha'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/E/beta'),
    line,
    'Index: %s (added)\n' % sbox.path('A/B/F/extra'),
    line,
  ])

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', wc_dir,
                                     '-r', '2',
                                     '--notice-ancestry',
                                     '--show-copies-as-adds',
                                     '--no-diff-added',
                                     '--no-diff-deleted')

  # Now create patches to verify the tree ordering
  patch = os.path.abspath(os.path.join(wc_dir, 'ancestry.patch'))

  cwd = os.getcwd()
  os.chdir(wc_dir)
  _, out, _ = svntest.actions.run_and_verify_svn(None, None, [],
                                                 'diff', '.',
                                                 '-r', '2',
                                                 '--notice-ancestry',
                                                 '--show-copies-as-adds')
  svntest.main.file_append(patch, ''.join(out))
  os.chdir(cwd)

  # And try to apply it
  svntest.actions.run_and_verify_svn(None, None, [], 'revert', '-R', wc_dir)

  expected_output = svntest.verify.UnorderedOutput([
    'D         %s\n' % sbox.ospath('A/B/F/extra'),
    'D         %s\n' % sbox.ospath('A/B/F'),
    'D         %s\n' % sbox.ospath('A/B/E/beta'),
    'D         %s\n' % sbox.ospath('A/B/E/alpha'),
    'D         %s\n' % sbox.ospath('A/B/E'),
    'D         %s\n' % sbox.ospath('A/B/lambda'),
    'D         %s\n' % sbox.ospath('A/B'),
    'A         %s\n' % sbox.ospath('A/B'),
    'A         %s\n' % sbox.ospath('A/B/lambda'),
    'A         %s\n' % sbox.ospath('A/B/F'),
    'A         %s\n' % sbox.ospath('A/B/F/extra'),
    'A         %s\n' % sbox.ospath('A/B/E'),
    'A         %s\n' % sbox.ospath('A/B/E/beta'),
    'A         %s\n' % sbox.ospath('A/B/E/alpha'),
  ])
  # And this currently fails because the ordering is broken, but also
  # because it hits an issue in 'svn patch'
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'patch', patch, wc_dir)

def diff_dir_replaced_by_file(sbox):
  "diff a directory replaced by a file"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_rm('A/B/E')
  sbox.simple_add_text('text', 'A/B/E')

  expected_output = [
    'Index: %s\n' % sbox.path('A/B/E/alpha'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/alpha'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
    '@@ -1 +0,0 @@\n',
    '-This is the file \'alpha\'.\n',
    'Index: %s\n' % sbox.path('A/B/E/beta'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/beta'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '@@ -1 +0,0 @@\n',
    '-This is the file \'beta\'.\n',
    'Index: %s\n' % sbox.path('A/B/E'),
    '===================================================================\n',
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E'),
    '+++ %s\t(working copy)\n' % sbox.path('A/B/E'),
    '@@ -0,0 +1 @@\n',
    '+text\n',
    '\ No newline at end of file\n',
  ]

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', wc_dir)

def diff_dir_replaced_by_dir(sbox):
  "diff a directory replaced by a directory tree"

  sbox.build()
  wc_dir = sbox.wc_dir

  sbox.simple_rm('A/B/E')
  sbox.simple_mkdir('A/B/E')
  sbox.simple_propset('a', 'b\n', 'A/B/E')
  sbox.simple_add_text('New beta\n', 'A/B/E/beta')

  # First check with ancestry (Tree replace)

  expected_output = [
    'Index: %s\n' % sbox.path('A/B/E/alpha'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/alpha'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
    '@@ -1 +0,0 @@\n',
    '-This is the file \'alpha\'.\n',
    'Index: %s\n' % sbox.path('A/B/E/beta'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/beta'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '@@ -1 +0,0 @@\n',
    '-This is the file \'beta\'.\n',
    'Index: %s\n' % sbox.path('A/B/E/beta'),
    '===================================================================\n',
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E/beta'),
    '+++ %s\t(working copy)\n' % sbox.path('A/B/E/beta'),
    '@@ -0,0 +1 @@\n',
    '+New beta\n',
    'Index: %s\n' % sbox.path('A/B/E'),
    '===================================================================\n',
    '--- %s\t(nonexistent)\n' % sbox.path('A/B/E'),
    '+++ %s\t(working copy)\n' % sbox.path('A/B/E'),
    '\n',
    'Property changes on: %s\n' % sbox.path('A/B/E'),
    '___________________________________________________________________\n',
    'Added: a\n',
    '## -0,0 +1 ##\n',
    '+b\n',
  ]

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--notice-ancestry', wc_dir)

  # And summarized. Currently produces directory adds after their children
  expected_output = svntest.verify.UnorderedOutput([
    'D       %s\n' % sbox.ospath('A/B/E/alpha'),
    'D       %s\n' % sbox.ospath('A/B/E/beta'),
    'D       %s\n' % sbox.ospath('A/B/E'),
    'A       %s\n' % sbox.ospath('A/B/E'),
    'A       %s\n' % sbox.ospath('A/B/E/beta'),
  ])
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--summarize', wc_dir,
                                     '--notice-ancestry')

  # And now without (file delete, change + properties)
  expected_output = [
    'Index: %s\n' % sbox.path('A/B/E/alpha'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/alpha'),
    '+++ %s\t(nonexistent)\n' % sbox.path('A/B/E/alpha'),
    '@@ -1 +0,0 @@\n',
    '-This is the file \'alpha\'.\n',
    'Index: %s\n' % sbox.path('A/B/E/beta'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E/beta'),
    '+++ %s\t(working copy)\n' % sbox.path('A/B/E/beta'),
    '@@ -1 +1 @@\n',
    '-This is the file \'beta\'.\n',
    '+New beta\n',
    'Index: %s\n' % sbox.path('A/B/E'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('A/B/E'),
    '+++ %s\t(working copy)\n' % sbox.path('A/B/E'),
    '\n',
    'Property changes on: %s\n' % sbox.path('A/B/E'),
    '___________________________________________________________________\n',
    'Added: a\n',
    '## -0,0 +1 ##\n',
    '+b\n',
  ]

  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', wc_dir)

  expected_output = [
    'D       %s\n' % sbox.ospath('A/B/E/alpha'),
    'M       %s\n' % sbox.ospath('A/B/E/beta'),
    ' M      %s\n' % sbox.ospath('A/B/E'),
  ]
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '--summarize', wc_dir)


@Issue(4366)
def diff_repos_empty_file_addition(sbox):
  "repos diff of rev which adds empty file"

  sbox.build()
  wc_dir = sbox.wc_dir

  # Add and commit an empty file.
  svntest.main.file_append(sbox.ospath('newfile'), "")
  svntest.main.run_svn(None, 'add', sbox.ospath('newfile'))
  expected_output = svntest.wc.State(sbox.wc_dir, {
    'newfile': Item(verb='Adding'),
    })
  expected_status = svntest.actions.get_virginal_state(sbox.wc_dir, 1)
  expected_status.add({
    'newfile' : Item(status='  ', wc_rev=2),
    })
  svntest.actions.run_and_verify_commit(sbox.wc_dir, expected_output,
                                        expected_status, None, sbox.wc_dir)

  # Now diff the revision that added the empty file.
  expected_output = [
    'Index: newfile\n',
    '===================================================================\n',
    ]
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '-c', '2', sbox.repo_url)

def diff_missing_tree_conflict_victim(sbox):
  "diff with missing tree-conflict victim in wc"

  sbox.build()
  wc_dir = sbox.wc_dir

  # Produce an 'incoming edit vs. local missing' tree conflict:
  # r2: edit iota and commit the change
  svntest.main.file_append(sbox.ospath('iota'), "This is a change to iota.\n")
  sbox.simple_propset('k', 'v', 'A/C')
  sbox.simple_commit()
  # now remove iota
  sbox.simple_rm('iota', 'A/C')
  sbox.simple_commit()
  # update to avoid mixed-rev wc warning
  sbox.simple_update()
  # merge r2 into wc and verify that a tree conflict is flagged on iota
  expected_output = wc.State(wc_dir, {
      'iota' : Item(status='  ', treeconflict='C'),
      'A/C' : Item(status='  ', treeconflict='C')
  })
  expected_mergeinfo_output = wc.State(wc_dir, {})
  expected_elision_output = wc.State(wc_dir, {})
  expected_disk = svntest.main.greek_state.copy()
  expected_disk.remove('iota','A/C')
  expected_status = svntest.actions.get_virginal_state(wc_dir, 3)
  expected_status.tweak('iota', 'A/C',
                        status='! ', treeconflict='C', wc_rev=None)
  expected_skip = wc.State('', { })
  svntest.actions.run_and_verify_merge(wc_dir, '1', '2',
                                       sbox.repo_url, None,
                                       expected_output,
                                       expected_mergeinfo_output,
                                       expected_elision_output,
                                       expected_disk,
                                       expected_status,
                                       expected_skip,
                                       None, None, None, None, None, None,
                                       False, '--ignore-ancestry', wc_dir)

  # 'svn diff' should show no change for the working copy
  # This currently fails because svn errors out with a 'node not found' error
  expected_output = [ ]
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff', wc_dir)

@Issue(4396)
def diff_local_missing_obstruction(sbox):
  "diff local missing and obstructed files"

  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  os.unlink(sbox.ospath('iota'))
  os.unlink(sbox.ospath('A/mu'))
  os.mkdir(sbox.ospath('A/mu'))

  # Expect no output for missing and obstructed files
  expected_output = [
  ]
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff', wc_dir)

  sbox.simple_propset('K', 'V', 'iota', 'A/mu')
  sbox.simple_append('IotA', 'Content')

  # But do expect a proper property diff
  expected_output = [
    'Index: %s\n' % (sbox.path('A/mu'),),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % (sbox.path('A/mu'),),
    '+++ %s\t(working copy)\n' % (sbox.path('A/mu'),),
    '\n',
    'Property changes on: %s\n' % (sbox.path('A/mu'),),
    '___________________________________________________________________\n',
    'Added: K\n',
    '## -0,0 +1 ##\n',
    '+V\n',
    '\ No newline at end of property\n',
    'Index: %s\n' % (sbox.path('iota'),),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % (sbox.path('iota'),),
    '+++ %s\t(working copy)\n' % (sbox.path('iota'),),
    '\n',
    'Property changes on: %s\n' % (sbox.path('iota'),),
    '___________________________________________________________________\n',
    'Added: K\n',
    '## -0,0 +1 ##\n',
    '+V\n',
    '\ No newline at end of property\n',
  ]
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff', wc_dir)

  # Create an external. This produces an error in 1.8.0.
  sbox.simple_propset('svn:externals', 'AA/BB ' + sbox.repo_url + '/A', '.')
  sbox.simple_update()

  svntest.actions.run_and_verify_svn(None, svntest.verify.AnyOutput, [],
                                     'diff', wc_dir)


@Issue(4444)
def diff_move_inside_copy(sbox):
  "diff copied-along child that contains a moved file"
  sbox.build(read_only=True)
  wc_dir = sbox.wc_dir

  d_path = 'A/D'
  d_copy = 'A/D-copy'
  h_path = 'A/D-copy/H'
  chi_path = '%s/chi' % h_path
  chi_moved = '%s/chi-moved' % h_path

  sbox.simple_copy(d_path, d_copy)
  sbox.simple_move(chi_path, chi_moved)
  sbox.simple_append(chi_moved, 'a new line')

  # Bug: Diffing the copied-along parent directory asserts
  svntest.actions.run_and_verify_svn(None, svntest.verify.AnyOutput, [],
                                     'diff', sbox.ospath(h_path))
@XFail()
@Issue(4464)
def diff_repo_wc_copies(sbox):
  "diff repo to wc of a copy"
  sbox.build()
  wc_dir = sbox.wc_dir
  iota_copy = sbox.ospath('iota_copy')
  iota_url = sbox.repo_url + '/iota'

  sbox.simple_copy('iota', 'iota_copy')
  expected_output = make_diff_header(iota_copy, "nonexistent", "working copy",
                                     iota_url, iota_copy) + [
                                       "@@ -0,0 +1 @@\n",
                                       "+This is the file 'iota'.\n" ]
  svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff',
                                     '--show-copies-as-adds',
                                     iota_url, iota_copy)

  expected_output = make_diff_header(iota, 'working copy', 'revision 1') + \
                    [ '@@ -1,2 +1 @@\n',
                      " This is the file 'iota'.\n",
                      "-second line\n", ] + \
                    make_diff_prop_header(iota) + \
                    make_diff_prop_deleted('svn:mime-type', 'text/plain')
    # remove line with the same content.  Fortunately, it doesn't
    expected_output = make_diff_header(newfile, 'nonexistent', 'revision 2') + \
    expected_output = make_diff_header(newfile, 'revision 2', 'nonexistent') + \
                      [ '@@ -1 +0,0 @@\n',
                        "-This is the file 'newfile'.\n",
                        '\n',
                        'Property changes on: %s\n' % sbox.path('newfile'),
                        '__________________________________________________' +
                              '_________________\n',
                        'Deleted: svn:mime-type\n',
                        '## -1 +0,0 ##\n',
                        '-text/plain\n',
                        '\ No newline at end of property\n']
    svntest.actions.run_and_verify_svn(None, expected_output, [], 'diff',
def diff_switched_file(sbox):
  "diff a switched file against repository"

  sbox.build()
  svntest.actions.run_and_verify_svn(None, None, [], 'switch',
                                     sbox.repo_url + '/A/mu',
                                     sbox.ospath('iota'), '--ignore-ancestry')
  sbox.simple_append('iota', 'Mu????')

  # This diffs the file against its origin
  expected_output = [
    'Index: %s\n' % sbox.path('iota'),
    '===================================================================\n',
    '--- %s\t(.../A/mu)\t(revision 1)\n' % sbox.path('iota'),
    '+++ %s\t(.../iota)\t(working copy)\n' % sbox.path('iota'),
    '@@ -1 +1,2 @@\n',
    ' This is the file \'mu\'.\n',
    '+Mu????\n',
    '\ No newline at end of file\n',
  ]
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '-r', '1', sbox.ospath('iota'))

  # And this undoes the switch for the diff
  expected_output = [
    'Index: %s\n' % sbox.path('iota'),
    '===================================================================\n',
    '--- %s\t(revision 1)\n' % sbox.path('iota'),
    '+++ %s\t(working copy)\n' % sbox.path('iota'),
    '@@ -1 +1,2 @@\n',
    '-This is the file \'iota\'.\n',
    '+This is the file \'mu\'.\n',
    '+Mu????\n',
    '\ No newline at end of file\n',
  ]
  svntest.actions.run_and_verify_svn(None, expected_output, [],
                                     'diff', '-r', '1', sbox.ospath(''))


              diff_correct_wc_base_revnum,
              diff_two_working_copies,
              diff_arbitrary_files_and_dirs,
              diff_properties_only,
              diff_properties_no_newline,
              diff_arbitrary_same,
              simple_ancestry,
              local_tree_replace,
              diff_dir_replaced_by_file,
              diff_dir_replaced_by_dir,
              diff_repos_empty_file_addition,
              diff_missing_tree_conflict_victim,
              diff_local_missing_obstruction,
              diff_move_inside_copy,
              diff_repo_wc_copies,
              diff_switched_file,