# MiDecommitSharedPageTail

- RVA: `0x00370240`–`0x00370864` (길이 `1,572` bytes)
- VA: `0x0000000140370240`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A6D8`
- 디코드: `364`개 명령, `1,572/1,572` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **21**; 고유 호출 대상: **18**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00370349` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x003703F1` → [MiCaptureDirtyBitToPfn](MiCaptureDirtyBitToPfn_function_00370DD0.md) (function, `0x00370DD0`)
- `0x00370411` → [MiBadShareCount](MiBadShareCount_function_00370EF8.md) (function, `0x00370EF8`)
- `0x00370458` → [MiPageChargedCommit](../45/MiPageChargedCommit_function_00456B58.md) (function, `0x00456B58`)
- `0x003704B8` → [MiDecommitFreePage](MiDecommitFreePage_function_00370870.md) (function, `0x00370870`)
- `0x00370575` → [MiLockCloneBlockAtDpc](MiLockCloneBlockAtDpc_function_00370FD8.md) (function, `0x00370FD8`)
- `0x003705B4` → [MiReturnCloneCharges](MiReturnCloneCharges_function_00370F50.md) (function, `0x00370F50`)
- `0x003705D3` → [MiChargeCommit](../28/MiChargeCommit_function_00286EB0.md) (function, `0x00286EB0`)
- `0x003705E9` → [MiDeleteMergedPte](MiDeleteMergedPte_function_00371040.md) (function, `0x00371040`)
- `0x0037060A` → [MiReturnCloneCharges](MiReturnCloneCharges_function_00370F50.md) (function, `0x00370F50`)
- `0x00370626` → [MiFreeCombineBlock](MiFreeCombineBlock_function_00372000.md) (function, `0x00372000`)
- `0x003706A7` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x003706B5` → [MiCreateDecayPfn](../2B/MiCreateDecayPfn_function_002B8764.md) (function, `0x002B8764`)
- `0x003706D1` → [KiCheckVpBackingLongSpinWaitHypercall](../30/KiCheckVpBackingLongSpinWaitHypercall_function_0030F490.md) (function, `0x0030F490`)
- `0x003706E1` → [HvlNotifyLongSpinWait](../30/HvlNotifyLongSpinWait_function_0030F460.md) (function, `0x0030F460`)
- `0x003706FB` → [MiDecrementCloneBlockReference](../22/MiDecrementCloneBlockReference_function_0022B9D0.md) (function, `0x0022B9D0`)
- `0x0037073E` → [MiLockCloneBlockAtDpc](MiLockCloneBlockAtDpc_function_00370FD8.md) (function, `0x00370FD8`)
- `0x00370768` → [MiGetPfnPriority](../32/MiGetPfnPriority_function_003226F0.md) (function, `0x003226F0`)
- `0x003707C6` → [MiGetLeafVa](../27/MiGetLeafVa_function_0027C0A0.md) (function, `0x0027C0A0`)
- `0x00370844` → [MiLogCombinedPteDelete](../68/MiLogCombinedPteDelete_function_0068BF1C.md) (function, `0x0068BF1C`)
- `0x0037085A` → [MiReleasePageFileInfo](../28/MiReleasePageFileInfo_function_00283FD0.md) (function, `0x00283FD0`)

### Direct callers
- [MiDecommitFreePagesTail](../41/MiDecommitFreePagesTail_function_0041ECE0.md) at `0x0041EE37`

### Static image references
- `0x003703D4` → RVA `0x00E30088` (`.data`; read)
- `0x00370423` → RVA `0x00FC52AC` (`ALMOSTRO`; reference)
- `0x0037060F` → RVA `0x00FC6B04` (`ALMOSTRO`; read)
- `0x003706C3` → RVA `0x00FC6AB8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00370240  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00370245  53                              push rbx
00370246  55                              push rbp
00370247  56                              push rsi
00370248  57                              push rdi
00370249  41 54                           push r12
0037024B  41 55                           push r13
0037024D  41 56                           push r14
0037024F  41 57                           push r15
00370251  48 81 EC B8 00 00 00            sub rsp, 0xb8
00370258  49 8B F8                        mov rdi, r8
0037025B  4C 8B F1                        mov r14, rcx
0037025E  4C 8B 41 20                     mov r8, qword ptr [rcx + 0x20]
00370262  48 8B C7                        mov rax, rdi
00370265  48 C1 E8 0C                     shr rax, 0xc
00370269  48 B9 FF FF FF FF FF 00 00 00   movabs rcx, 0xffffffffff
00370273  48 23 C1                        and rax, rcx
00370276  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0037027B  48 8D 2C 40                     lea rbp, [rax + rax*2]
0037027F  48 C1 E5 04                     shl rbp, 4
00370283  48 B8 00 00 00 00 00 DE FF FF   movabs rax, 0xffffde0000000000
0037028D  45 33 E4                        xor r12d, r12d
00370290  49 B9 00 00 00 00 80 F6 FF FF   movabs r9, 0xfffff68000000000
0037029A  48 8B CA                        mov rcx, rdx
0037029D  4C 89 A4 24 10 01 00 00         mov qword ptr [rsp + 0x110], r12
003702A5  4C 89 A4 24 18 01 00 00         mov qword ptr [rsp + 0x118], r12
003702AD  41 8B F4                        mov esi, r12d
003702B0  48 C1 E1 19                     shl rcx, 0x19
003702B4  48 03 E8                        add rbp, rax
003702B7  49 8B C1                        mov rax, r9
003702BA  48 8B 5D 08                     mov rbx, qword ptr [rbp + 8]
003702BE  48 C1 E0 19                     shl rax, 0x19
003702C2  48 2B C8                        sub rcx, rax
003702C5  48 B8 00 00 00 00 00 00 00 80   movabs rax, 0x8000000000000000
003702CF  48 C1 F9 10                     sar rcx, 0x10
003702D3  45 39 66 28                     cmp dword ptr [r14 + 0x28], r12d
003702D7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
003702DC  49 8D 88 00 FC FF FF            lea rcx, [r8 - 0x400]
003702E3  49 0F 45 CC                     cmovne rcx, r12
003702E7  48 0B D8                        or rbx, rax
003702EA  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
003702EE  48 0F BA E0 28                  bt rax, 0x28
003702F3  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
003702F8  72 0D                           jb 0x140370307
003702FA  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
003702FE  48 85 C0                        test rax, rax
00370301  0F 89 12 04 00 00               jns 0x140370719
00370307  45 39 66 28                     cmp dword ptr [r14 + 0x28], r12d
0037030B  75 77                           jne 0x140370384
0037030D  49 8B C1                        mov rax, r9
00370310  49 B8 78 FF FF FF 3F 00 00 00   movabs r8, 0x3fffffff78
0037031A  49 03 C0                        add rax, r8
0037031D  48 3B D0                        cmp rdx, rax
00370320  77 62                           ja 0x140370384
00370322  49 8B C1                        mov rax, r9
00370325  48 3B D0                        cmp rdx, rax
00370328  72 5A                           jb 0x140370384
0037032A  4C 8B B9 80 02 00 00            mov r15, qword ptr [rcx + 0x280]
00370331  4D 85 FF                        test r15, r15
00370334  74 4E                           je 0x140370384
00370336  33 D2                           xor edx, edx
00370338  48 89 9C 24 18 01 00 00         mov qword ptr [rsp + 0x118], rbx
00370340  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00370345  44 8D 42 70                     lea r8d, [rdx + 0x70]
00370349  E8 F2 68 35 00                  call 0x1406c6c40
0037034E  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
00370353  49 8B F7                        mov rsi, r15
00370356  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0037035B  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00370360  48 3B 5E 20                     cmp rbx, qword ptr [rsi + 0x20]
00370364  0F 87 36 04 00 00               ja 0x1403707a0
0037036A  48 3B 5E 18                     cmp rbx, qword ptr [rsi + 0x18]
0037036E  73 08                           jae 0x140370378
00370370  48 8B 36                        mov rsi, qword ptr [rsi]
00370373  48 85 F6                        test rsi, rsi
00370376  75 E8                           jne 0x140370360
00370378  48 85 F6                        test rsi, rsi
0037037B  0F 85 D8 02 00 00               jne 0x140370659
00370381  49 8B F4                        mov rsi, r12
00370384  45 8B BE A0 00 00 00            mov r15d, dword ptr [r14 + 0xa0]
0037038B  48 B9 FF FF FF FF FF FF FF 3F   movabs rcx, 0x3fffffffffffffff
00370395  41 F6 C7 04                     test r15b, 4
00370399  0F 85 C9 02 00 00               jne 0x140370668
0037039F  45 89 A6 80 00 00 00            mov dword ptr [r14 + 0x80], r12d
003703A6  49 8B DC                        mov rbx, r12
003703A9  45 8B EC                        mov r13d, r12d
003703AC  F0 48 0F BA 6D 18 3F            lock bts qword ptr [rbp + 0x18], 0x3f
003703B3  72 6B                           jb 0x140370420
003703B5  41 81 E7 91 00 00 00            and r15d, 0x91
003703BC  41 80 FF 81                     cmp r15b, 0x81
003703C0  49 BF FF FF FF FF FF FF FF 3F   movabs r15, 0x3fffffffffffffff
003703CA  0F 84 84 03 00 00               je 0x140370754
003703D0  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
003703D4  48 8B 0D AD FC AB 00            mov rcx, qword ptr [rip + 0xabfcad]
003703DB  48 C1 E8 2B                     shr rax, 0x2b
003703DF  25 FF 03 00 00                  and eax, 0x3ff
003703E4  4C 8B 2C C1                     mov r13, qword ptr [rcx + rax*8]
003703E8  40 F6 C7 42                     test dil, 0x42
003703EC  74 0B                           je 0x1403703f9
003703EE  48 8B CD                        mov rcx, rbp
003703F1  E8 DA 09 00 00                  call 0x140370dd0
003703F6  48 8B D8                        mov rbx, rax
003703F9  41 8B 86 9C 00 00 00            mov eax, dword ptr [r14 + 0x9c]
00370400  A8 20                           test al, 0x20
00370402  74 3D                           je 0x140370441
00370404  0F B6 45 22                     movzx eax, byte ptr [rbp + 0x22]
00370408  24 07                           and al, 7
0037040A  3C 06                           cmp al, 6
0037040C  74 68                           je 0x140370476
0037040E  48 8B CD                        mov rcx, rbp
00370411  E8 E2 0A 00 00                  call 0x140370ef8
00370416  CC                              int3
00370417  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00370420  41 FF C5                        inc r13d
00370423  44 85 2D 82 4E C5 00            test dword ptr [rip + 0xc54e82], r13d
0037042A  0F 84 93 02 00 00               je 0x1403706c3
00370430  F3 90                           pause
00370432  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00370436  48 85 C0                        test rax, rax
00370439  0F 89 6D FF FF FF               jns 0x1403703ac
0037043F  EB DF                           jmp 0x140370420
00370441  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
00370445  85 C0                           test eax, eax
00370447  74 53                           je 0x14037049c
00370449  83 F8 03                        cmp eax, 3
0037044C  0F 84 BA 02 00 00               je 0x14037070c
00370452  48 8B D7                        mov rdx, rdi
00370455  48 8B CD                        mov rcx, rbp
00370458  E8 FB 66 0E 00                  call 0x140456b58
0037045D  85 C0                           test eax, eax
0037045F  0F 85 A7 02 00 00               jne 0x14037070c
00370465  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
00370468  C1 E8 18                        shr eax, 0x18
0037046B  A8 08                           test al, 8
0037046D  74 2D                           je 0x14037049c
0037046F  24 F7                           and al, 0xf7
00370471  88 45 23                        mov byte ptr [rbp + 0x23], al
00370474  EB 26                           jmp 0x14037049c
00370476  48 B8 00 00 00 00 80 F6 FF FF   movabs rax, 0xfffff68000000000
00370480  48 8B C0                        mov rax, rax
00370483  48 8B 4C 24 20                  mov rcx, qword ptr [rsp + 0x20]
00370488  48 3B C8                        cmp rcx, rax
0037048B  0F 83 18 03 00 00               jae 0x1403707a9
00370491  41 83 7E 28 03                  cmp dword ptr [r14 + 0x28], 3
00370496  0F 84 65 03 00 00               je 0x140370801
0037049C  0F B6 45 22                     movzx eax, byte ptr [rbp + 0x22]
003704A0  24 07                           and al, 7
003704A2  3C 06                           cmp al, 6
003704A4  0F 85 64 FF FF FF               jne 0x14037040e
003704AA  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
003704B2  4C 8B C5                        mov r8, rbp
003704B5  49 8B CE                        mov rcx, r14
003704B8  E8 B3 03 00 00                  call 0x140370870
003704BD  8B F8                           mov edi, eax
003704BF  48 B8 FF FF FF FF FF FF FF 7F   movabs rax, 0x7fffffffffffffff
003704C9  F0 48 21 45 18                  lock and qword ptr [rbp + 0x18], rax
003704CE  4C 8B BC 24 10 01 00 00         mov r15, qword ptr [rsp + 0x110]
003704D6  B9 04 00 00 00                  mov ecx, 4
003704DB  4D 85 FF                        test r15, r15
003704DE  75 57                           jne 0x140370537
003704E0  48 85 F6                        test rsi, rsi
003704E3  0F 85 02 02 00 00               jne 0x1403706eb
003704E9  41 8B 46 28                     mov eax, dword ptr [r14 + 0x28]
003704ED  85 C0                           test eax, eax
003704EF  0F 85 45 01 00 00               jne 0x14037063a
003704F5  41 83 BE 80 00 00 00 00         cmp dword ptr [r14 + 0x80], 0
003704FD  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00370501  0F 85 C1 00 00 00               jne 0x1403705c8
00370507  83 FF 03                        cmp edi, 3
0037050A  0F 84 3B 02 00 00               je 0x14037074b
00370510  48 85 DB                        test rbx, rbx
00370513  0F 85 35 03 00 00               jne 0x14037084e
00370519  83 FF 05                        cmp edi, 5
0037051C  0F 84 0B 01 00 00               je 0x14037062d
00370522  48 81 C4 B8 00 00 00            add rsp, 0xb8
00370529  41 5F                           pop r15
0037052B  41 5E                           pop r14
0037052D  41 5D                           pop r13
0037052F  41 5C                           pop r12
00370531  5F                              pop rdi
00370532  5E                              pop rsi
00370533  5D                              pop rbp
00370534  5B                              pop rbx
00370535  C3                              ret
00370536  CC                              int3
00370537  49 8D 47 E0                     lea rax, [r15 - 0x20]
0037053B  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
00370541  48 8B 48 10                     mov rcx, qword ptr [rax + 0x10]
00370545  48 8B 44 24 28                  mov rax, qword ptr [rsp + 0x28]
0037054A  48 8B 31                        mov rsi, qword ptr [rcx]
0037054D  F0 FF 89 88 01 00 00            lock dec dword ptr [rcx + 0x188]
00370554  48 85 C0                        test rax, rax
00370557  0F 84 D6 01 00 00               je 0x140370733
0037055D  0F B7 88 AE 00 00 00            movzx ecx, word ptr [rax + 0xae]
00370564  41 8B EC                        mov ebp, r12d
00370567  48 8B 05 1A FB AB 00            mov rax, qword ptr [rip + 0xabfb1a]
0037056E  48 8B 3C C8                     mov rdi, qword ptr [rax + rcx*8]
00370572  49 8B CF                        mov rcx, r15
00370575  E8 5E 0A 00 00                  call 0x140370fd8
0037057A  48 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdi
00370582  48 3B FE                        cmp rdi, rsi
00370585  0F 85 91 02 00 00               jne 0x14037081c
0037058B  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
0037058F  48 B9 FF FF FF FF FF FF FF 7F   movabs rcx, 0x7fffffffffffffff
00370599  48 FF C8                        dec rax
0037059C  49 89 47 18                     mov qword ptr [r15 + 0x18], rax
003705A0  F0 49 21 4F 10                  lock and qword ptr [r15 + 0x10], rcx
003705A5  BF 04 00 00 00                  mov edi, 4
003705AA  48 85 C0                        test rax, rax
003705AD  74 2E                           je 0x1403705dd
003705AF  8B D5                           mov edx, ebp
003705B1  48 8B CE                        mov rcx, rsi
003705B4  E8 97 09 00 00                  call 0x140370f50
003705B9  45 85 E4                        test r12d, r12d
003705BC  75 51                           jne 0x14037060f
003705BE  B9 04 00 00 00                  mov ecx, 4
003705C3  E9 2D FF FF FF                  jmp 0x1403704f5
003705C8  44 8B C1                        mov r8d, ecx
003705CB  BA 01 00 00 00                  mov edx, 1
003705D0  49 8B CD                        mov rcx, r13
003705D3  E8 D8 68 F1 FF                  call 0x140286eb0
003705D8  E9 33 FF FF FF                  jmp 0x140370510
003705DD  49 8B D7                        mov rdx, r15
003705E0  48 8B CE                        mov rcx, rsi
003705E3  41 BC 01 00 00 00               mov r12d, 1
003705E9  E8 52 0A 00 00                  call 0x140371040
003705EE  8B F8                           mov edi, eax
003705F0  83 F8 03                        cmp eax, 3
003705F3  75 BA                           jne 0x1403705af
003705F5  48 39 B4 24 08 01 00 00         cmp qword ptr [rsp + 0x108], rsi
003705FD  74 B0                           je 0x1403705af
003705FF  83 E5 FE                        and ebp, 0xfffffffe
00370602  8D 78 01                        lea edi, [rax + 1]
00370605  8B D5                           mov edx, ebp
00370607  48 8B CE                        mov rcx, rsi
0037060A  E8 41 09 00 00                  call 0x140370f50
0037060F  8B 05 EF 64 C5 00               mov eax, dword ptr [rip + 0xc564ef]
00370615  A8 01                           test al, 1
00370617  0F 85 24 02 00 00               jne 0x140370841
0037061D  BA 01 00 00 00                  mov edx, 1
00370622  49 8D 4F E0                     lea rcx, [r15 - 0x20]
00370626  E8 D5 19 00 00                  call 0x140372000
0037062B  EB 91                           jmp 0x1403705be
0037062D  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00370631  48 FF 40 10                     inc qword ptr [rax + 0x10]
00370635  E9 E8 FE FF FF                  jmp 0x140370522
0037063A  83 F8 03                        cmp eax, 3
0037063D  74 0F                           je 0x14037064e
0037063F  41 8B 86 9C 00 00 00            mov eax, dword ptr [r14 + 0x9c]
00370646  A8 20                           test al, 0x20
00370648  0F 85 A7 FE FF FF               jne 0x1403704f5
0037064E  83 FF 03                        cmp edi, 3
00370651  0F 44 F9                        cmove edi, ecx
00370654  E9 9C FE FF FF                  jmp 0x1403704f5
00370659  4C 39 66 30                     cmp qword ptr [rsi + 0x30], r12
0037065D  0F 84 1E FD FF FF               je 0x140370381
00370663  E9 1C FD FF FF                  jmp 0x140370384
00370668  4D 39 66 78                     cmp qword ptr [r14 + 0x78], r12
0037066C  0F 85 2D FD FF FF               jne 0x14037039f
00370672  40 F6 C7 42                     test dil, 0x42
00370676  0F 85 23 FD FF FF               jne 0x14037039f
0037067C  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00370680  48 23 C1                        and rax, rcx
00370683  48 83 F8 01                     cmp rax, 1
00370687  0F 85 12 FD FF FF               jne 0x14037039f
0037068D  48 8B 45 28                     mov rax, qword ptr [rbp + 0x28]
00370691  48 85 C0                        test rax, rax
00370694  0F 89 05 FD FF FF               jns 0x14037039f
0037069A  F6 45 22 10                     test byte ptr [rbp + 0x22], 0x10
0037069E  0F 85 FB FC FF FF               jne 0x14037039f
003706A4  48 8B CD                        mov rcx, rbp
003706A7  E8 44 20 FB FF                  call 0x1403226f0
003706AC  83 F8 05                        cmp eax, 5
003706AF  0F 83 EA FC FF FF               jae 0x14037039f
003706B5  E8 AA 80 F4 FF                  call 0x1402b8764
003706BA  49 89 46 78                     mov qword ptr [r14 + 0x78], rax
003706BE  E9 DC FC FF FF                  jmp 0x14037039f
003706C3  8B 05 EF 63 C5 00               mov eax, dword ptr [rip + 0xc563ef]
003706C9  A8 40                           test al, 0x40
003706CB  0F 84 5F FD FF FF               je 0x140370430
003706D1  E8 BA ED F9 FF                  call 0x14030f490
003706D6  84 C0                           test al, al
003706D8  0F 84 52 FD FF FF               je 0x140370430
003706DE  41 8B CD                        mov ecx, r13d
003706E1  E8 7A ED F9 FF                  call 0x14030f460
003706E6  E9 47 FD FF FF                  jmp 0x140370432
003706EB  4C 8B 44 24 30                  mov r8, qword ptr [rsp + 0x30]
003706F0  48 8B CE                        mov rcx, rsi
003706F3  48 8B 94 24 18 01 00 00         mov rdx, qword ptr [rsp + 0x118]
003706FB  E8 D0 B2 EB FF                  call 0x14022b9d0
00370700  8B F8                           mov edi, eax
00370702  B9 04 00 00 00                  mov ecx, 4
00370707  E9 E9 FD FF FF                  jmp 0x1403704f5
0037070C  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00370710  48 FF 40 18                     inc qword ptr [rax + 0x18]
00370714  E9 4C FD FF FF                  jmp 0x140370465
00370719  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0037071D  48 85 C0                        test rax, rax
00370720  0F 84 E1 FB FF FF               je 0x140370307
00370726  48 89 9C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rbx
0037072E  E9 51 FC FF FF                  jmp 0x140370384
00370733  49 8B CF                        mov rcx, r15
00370736  48 89 B4 24 08 01 00 00         mov qword ptr [rsp + 0x108], rsi
0037073E  E8 95 08 00 00                  call 0x140370fd8
00370743  41 8B EC                        mov ebp, r12d
00370746  E9 40 FE FF FF                  jmp 0x14037058b
0037074B  48 FF 40 08                     inc qword ptr [rax + 8]
0037074F  E9 BC FD FF FF                  jmp 0x140370510
00370754  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
00370758  49 23 C7                        and rax, r15
0037075B  48 83 F8 01                     cmp rax, 1
0037075F  0F 85 6B FC FF FF               jne 0x1403703d0
00370765  48 8B CD                        mov rcx, rbp
00370768  E8 83 1F FB FF                  call 0x1403226f0
0037076D  83 C0 FD                        add eax, -3
00370770  83 F8 02                        cmp eax, 2
00370773  0F 87 57 FC FF FF               ja 0x1403703d0
00370779  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
0037077C  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00370783  C1 E8 18                        shr eax, 0x18
00370786  24 FA                           and al, 0xfa
00370788  0C 02                           or al, 2
0037078A  88 84 24 03 01 00 00            mov byte ptr [rsp + 0x103], al
00370791  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
00370798  89 45 20                        mov dword ptr [rbp + 0x20], eax
0037079B  E9 30 FC FF FF                  jmp 0x1403703d0
003707A0  48 8B 76 08                     mov rsi, qword ptr [rsi + 8]
003707A4  E9 CA FB FF FF                  jmp 0x140370373
003707A9  48 B8 FF FF FF FF FF F6 FF FF   movabs rax, 0xfffff6ffffffffff
003707B3  48 3B C8                        cmp rcx, rax
003707B6  0F 87 D5 FC FF FF               ja 0x140370491
003707BC  45 39 66 28                     cmp dword ptr [r14 + 0x28], r12d
003707C0  0F 85 D6 FC FF FF               jne 0x14037049c
003707C6  E8 D5 B8 F0 FF                  call 0x14027c0a0
003707CB  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
003707D5  48 3B C1                        cmp rax, rcx
003707D8  0F 87 BE FC FF FF               ja 0x14037049c
003707DE  48 8B 45 18                     mov rax, qword ptr [rbp + 0x18]
003707E2  49 23 C7                        and rax, r15
003707E5  48 3D 00 00 01 00               cmp rax, 0x10000
003707EB  0F 82 AB FC FF FF               jb 0x14037049c
003707F1  41 C7 86 80 00 00 00 01 00 00 00  mov dword ptr [r14 + 0x80], 1
003707FC  E9 9B FC FF FF                  jmp 0x14037049c
00370801  49 8B 46 18                     mov rax, qword ptr [r14 + 0x18]
00370805  48 FF 40 18                     inc qword ptr [rax + 0x18]
00370809  8B 45 20                        mov eax, dword ptr [rbp + 0x20]
0037080C  C1 E8 18                        shr eax, 0x18
0037080F  A8 08                           test al, 8
00370811  0F 84 85 FC FF FF               je 0x14037049c
00370817  E9 53 FC FF FF                  jmp 0x14037046f
0037081C  49 83 6F 08 01                  sub qword ptr [r15 + 8], 1
00370821  48 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdi
00370829  0F 85 5C FD FF FF               jne 0x14037058b
0037082F  BD 05 00 00 00                  mov ebp, 5
00370834  48 89 BC 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdi
0037083C  E9 4A FD FF FF                  jmp 0x14037058b
00370841  49 8B CF                        mov rcx, r15
00370844  E8 D3 B6 31 00                  call 0x14068bf1c
00370849  E9 CF FD FF FF                  jmp 0x14037061d
0037084E  41 B8 01 00 00 00               mov r8d, 1
00370854  48 8B D3                        mov rdx, rbx
00370857  49 8B CD                        mov rcx, r13
0037085A  E8 71 37 F1 FF                  call 0x140283fd0
0037085F  E9 B5 FC FF FF                  jmp 0x140370519
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDecommitSharedPageTail(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p100;
    unsigned __int8 v_stack_p103;
    unsigned __int64 v_stack_p108;
    unsigned __int64 v_stack_p110;
    unsigned __int64 v_stack_p118;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;

    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (184);
    result = (a3) >> (12);
    result = (result) & (a1);
    v_stack_mD0 = *(unsigned __int64 *)(a1 + 32);
    v_rbp = (result + result * 2) << (4);
    v_r12 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    a1 = (a2) << (25);
    v_rbp = (v_rbp) + (result);
    result = (a4) << (25);
    a1 = (a1) - (result);
    a1 = (a1) >> (16);
    v_stack_mD8 = a1;
    a1 = *(unsigned __int64 *)(a1 + 32) - 1024;
    if ((*(unsigned int *)(a1 + 40)) != 0) { a1 = 0; }
    v_rbx = (*(unsigned __int64 *)(v_rbp + 8)) | (result);
    v_stack_mC8 = a1;
    if (condition_is_below) goto loc_00370307;
    if (!sign_flag) goto loc_00370719;
loc_00370307:
    if ((*(unsigned int *)(a1 + 40)) != 0) goto loc_00370384;
    result = (a4) + (*(unsigned __int64 *)(a1 + 32));
    if (a2 > result) goto loc_00370384;
    if (a2 < a4) goto loc_00370384;
    if (*(unsigned __int64 *)(a1 + 640) == 0) goto loc_00370384;
    a2 = 0;
    v_stack_p20 = v_rbx;
    result = memset(v_stack_mB8, a2, a2 + 112, a4);
    v_stack_mA0 = v_rbx;
    v_stack_m98 = v_rbx;
loc_00370360:
    if (v_rbx > (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 32))) goto loc_003707A0;
    if (v_rbx >= (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640) + 24))) goto loc_00370378;
loc_00370373:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640)) != 0) goto loc_00370360;
loc_00370378:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 640)) != 0) goto loc_00370659;
loc_00370381:
loc_00370384:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 160)))) & (4)) != 0) goto loc_00370668;
loc_0037039F:
    *(unsigned int *)(a1 + 128) = 0;
loc_003703AC:
    if (condition_is_below) goto loc_00370420;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 160))) & (145));
    if (((unsigned __int8)(v_r15)) == 129) goto loc_00370754;
loc_003703D0:
    result = (*(unsigned __int64 *)(v_rbp + 40)) >> (43);
    result = (unsigned int)((result) & (0x3FFULL));
    v_rbx = 0;
    if ((((unsigned __int8)(a3)) & (66)) != 0) {
        a1 = v_rbp;
        result = MiCaptureDirtyBitToPfn(a1, a2, a2 + 112, a4);
        v_rbx = result;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) == 0) goto loc_00370441;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbp + 34)) & (7));
    if (((unsigned __int8)(result)) == 6) goto loc_00370476;
loc_0037040E:
    result = MiBadShareCount(v_rbp, a2, a2 + 112, a4);
loc_00370420:
    v_r13 = (unsigned int)((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11271341) + result * 8)) + 1);
    if (((*(unsigned int *)(v_rip + 12930690)) & ((unsigned int)(v_r13))) == 0) goto loc_003706C3;
loc_00370430:
loc_00370432:
    if (!sign_flag) goto loc_003703AC;
    goto loc_00370420;
loc_00370441:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) == 0) goto loc_0037049C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)))) == 3) goto loc_0037070C;
    result = MiPageChargedCommit(v_rbp, a3, a2 + 112, a4);
    if ((unsigned int)(result) != 0) goto loc_0037070C;
loc_00370465:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rbp + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_0037049C;
loc_0037046F:
    result = (unsigned __int8)((result) & (247));
    *(unsigned __int8 *)(v_rbp + 35) = (unsigned __int8)(result);
    goto loc_0037049C;
loc_00370476:
    if (v_stack_mD8 >= result) goto loc_003707A9;
loc_00370491:
    if ((*(unsigned int *)(a1 + 40)) == 3) goto loc_00370801;
loc_0037049C:
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rbp + 34)) & (7));
    if (((unsigned __int8)(result)) != 6) goto loc_0037040E;
    result = MiDecommitFreePage(a1, v_stack_p10, v_rbp, a4);
    if (v_stack_p18 != 0) goto loc_00370537;
    if (0 != 0) goto loc_003706EB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40))) != 0) goto loc_0037063A;
loc_003704F5:
    if ((*(unsigned int *)(a1 + 128)) != 0) goto loc_003705C8;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 3) goto loc_0037074B;
loc_00370510:
    if (v_rbx != 0) goto loc_0037084E;
loc_00370519:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 5) goto loc_0037062D;
loc_00370522:
    v_rsp = (v_rsp) + (184);
    return *(unsigned __int64 *)(a1 + 24);
loc_00370537:
    result = (v_stack_p18 - 32) & (0xFFFFFFFFFFFFF000ULL);
    if (v_stack_p28 == 0) goto loc_00370733;
    result = MiLockCloneBlockAtDpc(v_stack_p18, v_stack_p10, v_rbp, a4);
    v_stack_p108 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11270938) + *(unsigned __int16 *)(v_stack_p28 + 174) * 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 11270938) + *(unsigned __int16 *)(v_stack_p28 + 174) * 8)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)))) goto loc_0037081C;
loc_0037058B:
    result = (*(unsigned __int64 *)(v_stack_p18 + 24)) - 1;
    *(unsigned __int64 *)(v_stack_p18 + 24) = result;
    if (result == 0) goto loc_003705DD;
loc_003705AF:
    result = MiReturnCloneCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)), 0, v_rbp, a4);
    if (0 != 0) goto loc_0037060F;
loc_003705BE:
    goto loc_003704F5;
loc_003705C8:
    result = MiChargeCommit(v_r13, 1, 4, a4);
    goto loc_00370510;
loc_003705DD:
    result = MiDeleteMergedPte(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)), v_stack_p18, 4, a4);
    if (((unsigned int)(result)) != 3) goto loc_003705AF;
    if (v_stack_p108 == (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)))) goto loc_003705AF;
    v_rbp = (unsigned int)((0) & (0xFFFFFFFEULL));
    result = MiReturnCloneCharges(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)), (unsigned int)((unsigned int)(v_rbp)), 4, a4);
loc_0037060F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12936431)))) & (1)) != 0) goto loc_00370841;
loc_0037061D:
    result = MiFreeCombineBlock(v_stack_p18 - 32, 1, 4, a4);
    goto loc_003705BE;
loc_0037062D:
    goto loc_00370522;
loc_0037063A:
    if (((unsigned int)(*(unsigned __int64 *)(a1 + 24))) == 3) goto loc_0037064E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a1 + 156)))) & (32)) != 0) goto loc_003704F5;
loc_0037064E:
    v_rdi = result + 1;
    if (((unsigned int)(result + 1)) == 3) { v_rdi = (unsigned int)(v_stack_p18 - 32); }
    goto loc_003704F5;
loc_00370659:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)) + 48)) == 1) goto loc_00370381;
    goto loc_00370384;
loc_00370668:
    if ((*(unsigned __int64 *)(a1 + 120)) != 1) goto loc_0037039F;
    if ((((unsigned __int8)(v_rdi)) & (66)) != 0) goto loc_0037039F;
    result = (*(unsigned __int64 *)(v_rbp + 24)) & (v_stack_p18 - 32);
    if (result != 1) goto loc_0037039F;
    if (!sign_flag) goto loc_0037039F;
    if (((*(unsigned __int8 *)(v_rbp + 34)) & (16)) != 0) goto loc_0037039F;
    result = MiGetPfnPriority(v_rbp, 1, 4, a4);
    if (((unsigned int)(result)) >= 5) goto loc_0037039F;
    result = MiCreateDecayPfn(v_rbp, 1, 4, a4);
    *(unsigned __int64 *)(a1 + 120) = result;
    goto loc_0037039F;
loc_003706C3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12936175)))) & (64)) == 0) goto loc_00370430;
    result = KiCheckVpBackingLongSpinWaitHypercall(v_rbp, 1, 4, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00370430;
    result = HvlNotifyLongSpinWait((unsigned int)((unsigned int)(v_r13)), 1, 4, a4);
    goto loc_00370432;
loc_003706EB:
    result = MiDecrementCloneBlockReference(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16)), v_stack_p118, v_stack_p30, a4);
    goto loc_003704F5;
loc_0037070C:
    goto loc_00370465;
loc_00370719:
    if (*(unsigned __int64 *)(v_rbp + 8) == 0) goto loc_00370307;
    v_stack_p110 = v_rbx;
    goto loc_00370384;
loc_00370733:
    v_stack_p108 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16));
    result = MiLockCloneBlockAtDpc(v_stack_p18, v_stack_p118, v_stack_p30, a4);
    goto loc_0037058B;
loc_0037074B:
    goto loc_00370510;
loc_00370754:
    result = (*(unsigned __int64 *)(1 + 24)) & (v_stack_p18);
    if (result != 1) goto loc_003703D0;
    result = MiGetPfnPriority(1, v_stack_p118, v_stack_p30, a4);
    result = (unsigned int)((result) + (-3));
    if (((unsigned int)(result)) > 2) goto loc_003703D0;
    v_stack_p100 = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 32))) >> (24));
    result = (unsigned __int8)((result) & (250));
    result = (unsigned __int8)((result) | (2));
    v_stack_p103 = (unsigned __int8)(result);
    *(unsigned int *)(1 + 32) = (unsigned int)((unsigned int)(v_stack_p100));
    goto loc_003703D0;
loc_003707A0:
    goto loc_00370373;
loc_003707A9:
    if (1 > ((unsigned int)(v_stack_p100))) goto loc_00370491;
    if ((*(unsigned int *)(a1 + 40)) != 1) goto loc_0037049C;
    result = MiGetLeafVa(1, v_stack_p118, v_stack_p30, a4);
    if (result > 1) goto loc_0037049C;
    result = (*(unsigned __int64 *)(1 + 24)) & (v_stack_p18);
    if (result < 0x10000ULL) goto loc_0037049C;
    *(unsigned int *)(a1 + 128) = 1;
    goto loc_0037049C;
loc_00370801:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(1 + 32))) >> (24));
    if ((((unsigned __int8)(result)) & (8)) == 0) goto loc_0037049C;
    goto loc_0037046F;
loc_0037081C:
    v_stack_p108 = (unsigned int)((unsigned int)(result));
    if ((((unsigned __int8)(result)) & (8)) != 0) goto loc_0037058B;
    v_stack_p108 = (unsigned int)((unsigned int)(result));
    goto loc_0037058B;
loc_00370841:
    result = MiLogCombinedPteDelete(v_stack_p18, v_stack_p118, v_stack_p30, a4);
    goto loc_0037061D;
loc_0037084E:
    result = MiReleasePageFileInfo(v_r13, v_rbx, 1, a4);
    goto loc_00370519;
}
```

## 5. (Beta) C Style

```c
int64_t MiDecommitSharedPageTail(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_p10;
    uint32_t v_stack_p100;
    uint8_t v_stack_p103;
    uint64_t v_stack_p108;
    uint64_t v_stack_p110;
    uint64_t v_stack_p118;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;

    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (184);
    result = (Arg3) >> (12);
    result = (result) & (Arg1);
    v_stack_mD0 = *(uint64_t *)(arg1 + 0x20);
    local_rbp = (result + result * 2) << (4);
    local_r12 = 0;
    v_stack_p18 = 0;
    v_stack_p20 = 0;
    Arg1 = (Arg2) << (25);
    local_rbp = (local_rbp) + (result);
    result = (a4) << (25);
    Arg1 = (Arg1) - (result);
    Arg1 = (Arg1) >> (16);
    v_stack_mD8 = Arg1;
    Arg1 = *(uint64_t *)(arg1 + 0x20) - 1024;
    if ((*(uint32_t *)(arg1 + 0x28)) != 0) { Arg1 = 0; }
    local_rbx = (*(uint64_t *)(local_rbp + 0x8)) | (result);
    v_stack_mC8 = Arg1;
    if (condition_is_below) goto loc_00370307;
    if (!sign_flag) goto loc_00370719;
loc_00370307:
    if ((*(uint32_t *)(arg1 + 0x28)) != 0) goto loc_00370384;
    result = (a4) + (*(uint64_t *)(arg1 + 0x20));
    if (Arg2 > result) goto loc_00370384;
    if (Arg2 < a4) goto loc_00370384;
    if (*(uint64_t *)(arg1 + 0x280) == 0) goto loc_00370384;
    Arg2 = 0;
    v_stack_p20 = local_rbx;
    result = memset(v_stack_mB8, Arg2, Arg2 + 112, a4);
    v_stack_mA0 = local_rbx;
    v_stack_m98 = local_rbx;
loc_00370360:
    if (local_rbx > (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x20))) goto loc_003707A0;
    if (local_rbx >= (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280) + 0x18))) goto loc_00370378;
loc_00370373:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280)) != 0) goto loc_00370360;
loc_00370378:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x280)) != 0) goto loc_00370659;
loc_00370381:
loc_00370384:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0xA0)))) & (4)) != 0) goto loc_00370668;
loc_0037039F:
    *(uint32_t *)(arg1 + 0x80) = 0;
loc_003703AC:
    if (condition_is_below) goto loc_00370420;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xA0))) & (145));
    if (((uint8_t)(local_r15)) == 129) goto loc_00370754;
loc_003703D0:
    result = (*(uint64_t *)(local_rbp + 0x28)) >> (43);
    result = (uint32_t)((result) & (0x3FFULL));
    local_rbx = 0;
    if ((((uint8_t)(Arg3)) & (66)) != 0) {
        Arg1 = local_rbp;
        result = MiCaptureDirtyBitToPfn(Arg1, Arg2, Arg2 + 112, a4);
        local_rbx = result;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) == 0) goto loc_00370441;
    result = (uint8_t)((*(uint8_t *)(local_rbp + 0x22)) & (7));
    if (((uint8_t)(result)) == 6) goto loc_00370476;
loc_0037040E:
    result = MiBadShareCount(local_rbp, Arg2, Arg2 + 112, a4);
loc_00370420:
    local_r13 = (uint32_t)((*(uint64_t *)(*(uint64_t *)(v_rip + 0xABFCAD) + result * 8)) + 1);
    if (((*(uint32_t *)(v_rip + 0xC54E82)) & ((uint32_t)(local_r13))) == 0) goto loc_003706C3;
loc_00370430:
loc_00370432:
    if (!sign_flag) goto loc_003703AC;
    goto loc_00370420;
loc_00370441:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) == 0) goto loc_0037049C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)))) == 3) goto loc_0037070C;
    result = MiPageChargedCommit(local_rbp, Arg3, Arg2 + 112, a4);
    if ((uint32_t)(result) != 0) goto loc_0037070C;
loc_00370465:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rbp + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_0037049C;
loc_0037046F:
    result = (uint8_t)((result) & (247));
    *(uint8_t *)(local_rbp + 0x23) = (uint8_t)(result);
    goto loc_0037049C;
loc_00370476:
    if (v_stack_mD8 >= result) goto loc_003707A9;
loc_00370491:
    if ((*(uint32_t *)(arg1 + 0x28)) == 3) goto loc_00370801;
loc_0037049C:
    result = (uint8_t)((*(uint8_t *)(local_rbp + 0x22)) & (7));
    if (((uint8_t)(result)) != 6) goto loc_0037040E;
    result = MiDecommitFreePage(Arg1, v_stack_p10, local_rbp, a4);
    if (v_stack_p18 != 0) goto loc_00370537;
    if (0 != 0) goto loc_003706EB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28))) != 0) goto loc_0037063A;
loc_003704F5:
    if ((*(uint32_t *)(arg1 + 0x80)) != 0) goto loc_003705C8;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 3) goto loc_0037074B;
loc_00370510:
    if (local_rbx != 0) goto loc_0037084E;
loc_00370519:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 5) goto loc_0037062D;
loc_00370522:
    local_rsp = (local_rsp) + (184);
    return *(uint64_t *)(arg1 + 0x18);
loc_00370537:
    result = (v_stack_p18 - 32) & (0xFFFFFFFFFFFFF000ULL);
    if (v_stack_p28 == 0) goto loc_00370733;
    result = MiLockCloneBlockAtDpc(v_stack_p18, v_stack_p10, local_rbp, a4);
    v_stack_p108 = *(uint64_t *)(*(uint64_t *)(v_rip + 0xABFB1A) + *(uint16_t *)(v_stack_p28 + 0xAE) * 8);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0xABFB1A) + *(uint16_t *)(v_stack_p28 + 0xAE) * 8)) != (*(uint64_t *)(*(uint64_t *)(result + 0x10)))) goto loc_0037081C;
loc_0037058B:
    result = (*(uint64_t *)(v_stack_p18 + 0x18)) - 1;
    *(uint64_t *)(v_stack_p18 + 0x18) = result;
    if (result == 0) goto loc_003705DD;
loc_003705AF:
    result = MiReturnCloneCharges(*(uint64_t *)(*(uint64_t *)(result + 0x10)), 0, local_rbp, a4);
    if (0 != 0) goto loc_0037060F;
loc_003705BE:
    goto loc_003704F5;
loc_003705C8:
    result = MiChargeCommit(local_r13, 1, 4, a4);
    goto loc_00370510;
loc_003705DD:
    result = MiDeleteMergedPte(*(uint64_t *)(*(uint64_t *)(result + 0x10)), v_stack_p18, 4, a4);
    if (((uint32_t)(result)) != 3) goto loc_003705AF;
    if (v_stack_p108 == (*(uint64_t *)(*(uint64_t *)(result + 0x10)))) goto loc_003705AF;
    local_rbp = (uint32_t)((0) & (0xFFFFFFFEULL));
    result = MiReturnCloneCharges(*(uint64_t *)(*(uint64_t *)(result + 0x10)), (uint32_t)((uint32_t)(local_rbp)), 4, a4);
loc_0037060F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC564EF)))) & (1)) != 0) goto loc_00370841;
loc_0037061D:
    result = MiFreeCombineBlock(v_stack_p18 - 32, 1, 4, a4);
    goto loc_003705BE;
loc_0037062D:
    goto loc_00370522;
loc_0037063A:
    if (((uint32_t)(*(uint64_t *)(arg1 + 0x18))) == 3) goto loc_0037064E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg1 + 0x9C)))) & (32)) != 0) goto loc_003704F5;
loc_0037064E:
    local_rdi = result + 1;
    if (((uint32_t)(result + 1)) == 3) { local_rdi = (uint32_t)(v_stack_p18 - 32); }
    goto loc_003704F5;
loc_00370659:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x10)) + 0x30)) == 1) goto loc_00370381;
    goto loc_00370384;
loc_00370668:
    if ((*(uint64_t *)(arg1 + 0x78)) != 1) goto loc_0037039F;
    if ((((uint8_t)(local_rdi)) & (66)) != 0) goto loc_0037039F;
    result = (*(uint64_t *)(local_rbp + 0x18)) & (v_stack_p18 - 32);
    if (result != 1) goto loc_0037039F;
    if (!sign_flag) goto loc_0037039F;
    if (((*(uint8_t *)(local_rbp + 0x22)) & (16)) != 0) goto loc_0037039F;
    result = MiGetPfnPriority(local_rbp, 1, 4, a4);
    if (((uint32_t)(result)) >= 5) goto loc_0037039F;
    result = MiCreateDecayPfn(local_rbp, 1, 4, a4);
    *(uint64_t *)(arg1 + 0x78) = result;
    goto loc_0037039F;
loc_003706C3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC563EF)))) & (64)) == 0) goto loc_00370430;
    result = KiCheckVpBackingLongSpinWaitHypercall(local_rbp, 1, 4, a4);
    if ((uint8_t)(result) == 0) goto loc_00370430;
    result = HvlNotifyLongSpinWait((uint32_t)((uint32_t)(local_r13)), 1, 4, a4);
    goto loc_00370432;
loc_003706EB:
    result = MiDecrementCloneBlockReference(*(uint64_t *)(*(uint64_t *)(result + 0x10)), v_stack_p118, v_stack_p30, a4);
    goto loc_003704F5;
loc_0037070C:
    goto loc_00370465;
loc_00370719:
    if (*(uint64_t *)(local_rbp + 0x8) == 0) goto loc_00370307;
    v_stack_p110 = local_rbx;
    goto loc_00370384;
loc_00370733:
    v_stack_p108 = *(uint64_t *)(*(uint64_t *)(result + 0x10));
    result = MiLockCloneBlockAtDpc(v_stack_p18, v_stack_p118, v_stack_p30, a4);
    goto loc_0037058B;
loc_0037074B:
    goto loc_00370510;
loc_00370754:
    result = (*(uint64_t *)(1 + 0x18)) & (v_stack_p18);
    if (result != 1) goto loc_003703D0;
    result = MiGetPfnPriority(1, v_stack_p118, v_stack_p30, a4);
    result = (uint32_t)((result) + (-3));
    if (((uint32_t)(result)) > 2) goto loc_003703D0;
    v_stack_p100 = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x20))) >> (24));
    result = (uint8_t)((result) & (250));
    result = (uint8_t)((result) | (2));
    v_stack_p103 = (uint8_t)(result);
    *(uint32_t *)(1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p100));
    goto loc_003703D0;
loc_003707A0:
    goto loc_00370373;
loc_003707A9:
    if (1 > ((uint32_t)(v_stack_p100))) goto loc_00370491;
    if ((*(uint32_t *)(arg1 + 0x28)) != 1) goto loc_0037049C;
    result = MiGetLeafVa(1, v_stack_p118, v_stack_p30, a4);
    if (result > 1) goto loc_0037049C;
    result = (*(uint64_t *)(1 + 0x18)) & (v_stack_p18);
    if (result < 0x10000ULL) goto loc_0037049C;
    *(uint32_t *)(arg1 + 0x80) = 1;
    goto loc_0037049C;
loc_00370801:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(1 + 0x20))) >> (24));
    if ((((uint8_t)(result)) & (8)) == 0) goto loc_0037049C;
    goto loc_0037046F;
loc_0037081C:
    v_stack_p108 = (uint32_t)((uint32_t)(result));
    if ((((uint8_t)(result)) & (8)) != 0) goto loc_0037058B;
    v_stack_p108 = (uint32_t)((uint32_t)(result));
    goto loc_0037058B;
loc_00370841:
    result = MiLogCombinedPteDelete(v_stack_p18, v_stack_p118, v_stack_p30, a4);
    goto loc_0037061D;
loc_0037084E:
    result = MiReleasePageFileInfo(local_r13, local_rbx, 1, a4);
    goto loc_00370519;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |
| `Arg1` | `+ 0x78` | `64` | `R` |
| `Arg1` | `+ 0x78` | `64` | `W` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x80` | `32` | `W` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00370240&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
