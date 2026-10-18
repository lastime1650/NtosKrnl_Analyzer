# LocalpConvertStringSidToSid

- RVA: `0x00A17490`–`0x00A179AA` (길이 `1,306` bytes)
- VA: `0x0000000140A17490`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A9FF8`
- 디코드: `312`개 명령, `1,306/1,306` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **7**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A1754A` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (function, `0x005024A0`)
- `0x00A17589` → [wcschr](../../text/50/wcschr_function_00501A60.md) (function, `0x00501A60`)
- `0x00A175CD` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (function, `0x00502674`)
- `0x00A17717` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A17745` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A17787` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A17791` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)
- `0x00A177B0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A17828` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (function, `0x005024A0`)
- `0x00A17899` → [SddlpAlloc](../92/SddlpAlloc_function_00925F88.md) (function, `0x00925F88`)
- `0x00A179A0` → [PdcCloseEvent](../8D/PdcCloseEvent_function_008D2404.md) (function, `0x008D2404`)

### Direct callers
- [SeConvertStringSidToSid](../../text/4C/SeConvertStringSidToSid_function_004C6710.md) at `0x004C6749`
- [LocalConvertStringSDToSD_Rev1](../92/LocalConvertStringSDToSD_Rev1_function_0092656C.md) at `0x0092696D`
- [LocalConvertStringSDToSD_Rev1](../92/LocalConvertStringSDToSD_Rev1_function_0092656C.md) at `0x009269A7`
- [LocalGetAclForString](../92/LocalGetAclForString_function_00927F30.md) at `0x009288DF`
- [LocalGetSidForString](../92/LocalGetSidForString_function_009292B4.md) at `0x00929376`

### Static image references
- `0x00A174AF` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **6**
  - `0x00A1754A` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (`PAGE` → `.text`)
  - `0x00A17589` → [wcschr](../../text/50/wcschr_function_00501A60.md) (`PAGE` → `.text`)
  - `0x00A175CD` → [wcstoxq](../../text/50/wcstoxq_function_00502674.md) (`PAGE` → `.text`)
  - `0x00A17787` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A177B0` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A17828` → [wcstoul](../../text/50/wcstoul_function_005024A0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x00A17939` → [sub_00B370DA + 0x2E](../B3/Unknown_function_00B370DA.md) (`tail-transfer`)
  - `0x00A17943` → [sub_00B370DA](../B3/Unknown_function_00B370DA.md) (`tail-transfer`)
  - `0x00A1794B` → [sub_00B370DA](../B3/Unknown_function_00B370DA.md) (`tail-transfer`)
  - `0x00A17955` → [sub_00B370DA + 0x2E](../B3/Unknown_function_00B370DA.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A17490  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A17495  55                              push rbp
00A17496  56                              push rsi
00A17497  57                              push rdi
00A17498  41 54                           push r12
00A1749A  41 55                           push r13
00A1749C  41 56                           push r14
00A1749E  41 57                           push r15
00A174A0  48 8D AC 24 80 FE FF FF         lea rbp, [rsp - 0x180]
00A174A8  48 81 EC 80 02 00 00            sub rsp, 0x280
00A174AF  48 8B 05 8A 32 3F 00            mov rax, qword ptr [rip + 0x3f328a]
00A174B6  48 33 C4                        xor rax, rsp
00A174B9  48 89 85 70 01 00 00            mov qword ptr [rbp + 0x170], rax
00A174C0  33 F6                           xor esi, esi
00A174C2  4C 89 44 24 60                  mov qword ptr [rsp + 0x60], r8
00A174C7  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00A174CC  4D 8B F8                        mov r15, r8
00A174CF  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00A174D4  48 8B C2                        mov rax, rdx
00A174D7  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00A174DC  8B DE                           mov ebx, esi
00A174DE  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A174E3  44 8D 66 0A                     lea r12d, [rsi + 0xa]
00A174E7  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A174EC  44 8B EE                        mov r13d, esi
00A174EF  48 85 C9                        test rcx, rcx
00A174F2  0F 84 69 03 00 00               je 0x140a17861
00A174F8  48 85 C0                        test rax, rax
00A174FB  0F 84 60 03 00 00               je 0x140a17861
00A17501  4D 85 C0                        test r8, r8
00A17504  0F 84 57 03 00 00               je 0x140a17861
00A1750A  0F B7 01                        movzx eax, word ptr [rcx]
00A1750D  BA DF FF 00 00                  mov edx, 0xffdf
00A17512  66 83 E8 53                     sub ax, 0x53
00A17516  66 85 C2                        test dx, ax
00A17519  0F 85 AD 03 00 00               jne 0x140a178cc
00A1751F  44 8D 76 2D                     lea r14d, [rsi + 0x2d]
00A17523  66 44 39 71 02                  cmp word ptr [rcx + 2], r14w
00A17528  0F 85 9E 03 00 00               jne 0x140a178cc
00A1752E  48 8D 79 04                     lea rdi, [rcx + 4]
00A17532  66 83 3F 30                     cmp word ptr [rdi], 0x30
00A17536  8D 4E 10                        lea ecx, [rsi + 0x10]
00A17539  0F 84 A1 03 00 00               je 0x140a178e0
00A1753F  45 8B C4                        mov r8d, r12d
00A17542  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00A17547  48 8B CF                        mov rcx, rdi
00A1754A  E8 51 AF AE FF                  call 0x1405024a0
00A1754F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00A17553  3D FF 00 00 00                  cmp eax, 0xff
00A17558  0F 87 6E 03 00 00               ja 0x140a178cc
00A1755E  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
00A17563  48 3B C7                        cmp rax, rdi
00A17566  0F 84 60 03 00 00               je 0x140a178cc
00A1756C  66 44 39 30                     cmp word ptr [rax], r14w
00A17570  0F 85 56 03 00 00               jne 0x140a178cc
00A17576  48 8D 78 02                     lea rdi, [rax + 2]
00A1757A  66 39 37                        cmp word ptr [rdi], si
00A1757D  0F 84 49 03 00 00               je 0x140a178cc
00A17583  41 8B D6                        mov edx, r14d
00A17586  48 8B CF                        mov rcx, rdi
00A17589  E8 D2 A4 AE FF                  call 0x140501a60
00A1758E  48 85 C0                        test rax, rax
00A17591  0F 84 35 03 00 00               je 0x140a178cc
00A17597  48 3B C7                        cmp rax, rdi
00A1759A  0F 84 2C 03 00 00               je 0x140a178cc
00A175A0  66 83 3F 30                     cmp word ptr [rdi], 0x30
00A175A4  0F 84 4F 03 00 00               je 0x140a178f9
00A175AA  45 8B CC                        mov r9d, r12d
00A175AD  48 8D 44 24 44                  lea rax, [rsp + 0x44]
00A175B2  89 74 24 44                     mov dword ptr [rsp + 0x44], esi
00A175B6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A175BB  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00A175C0  48 8B D7                        mov rdx, rdi
00A175C3  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00A175CB  33 C9                           xor ecx, ecx
00A175CD  E8 A2 B0 AE FF                  call 0x140502674
00A175D2  48 8B C8                        mov rcx, rax
00A175D5  48 B8 FF FF FF FF FF FF 00 00   movabs rax, 0xffffffffffff
00A175DF  48 3B C8                        cmp rcx, rax
00A175E2  0F 87 E4 02 00 00               ja 0x140a178cc
00A175E8  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00A175ED  4C 3B F7                        cmp r14, rdi
00A175F0  0F 84 D6 02 00 00               je 0x140a178cc
00A175F6  41 B9 2D 00 00 00               mov r9d, 0x2d
00A175FC  66 45 39 0E                     cmp word ptr [r14], r9w
00A17600  0F 85 C6 02 00 00               jne 0x140a178cc
00A17606  66 41 39 76 02                  cmp word ptr [r14 + 2], si
00A1760B  0F 84 BB 02 00 00               je 0x140a178cc
00A17611  48 8B C1                        mov rax, rcx
00A17614  88 4C 24 35                     mov byte ptr [rsp + 0x35], cl
00A17618  48 C1 E8 08                     shr rax, 8
00A1761C  49 8B FE                        mov rdi, r14
00A1761F  88 44 24 34                     mov byte ptr [rsp + 0x34], al
00A17623  41 BA DF FF 00 00               mov r10d, 0xffdf
00A17629  48 8B C1                        mov rax, rcx
00A1762C  48 C1 E8 10                     shr rax, 0x10
00A17630  88 44 24 33                     mov byte ptr [rsp + 0x33], al
00A17634  48 8B C1                        mov rax, rcx
00A17637  48 C1 E8 18                     shr rax, 0x18
00A1763B  88 44 24 32                     mov byte ptr [rsp + 0x32], al
00A1763F  48 8B C1                        mov rax, rcx
00A17642  48 C1 E8 20                     shr rax, 0x20
00A17646  48 C1 E9 28                     shr rcx, 0x28
00A1764A  88 44 24 31                     mov byte ptr [rsp + 0x31], al
00A1764E  45 33 C0                        xor r8d, r8d
00A17651  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
00A17655  48 85 FF                        test rdi, rdi
00A17658  0F 84 8B 00 00 00               je 0x140a176e9
00A1765E  40 80 FE FF                     cmp sil, 0xff
00A17662  0F 84 E8 02 00 00               je 0x140a17950
00A17668  0F B7 0F                        movzx ecx, word ptr [rdi]
00A1766B  66 41 3B C9                     cmp cx, r9w
00A1766F  74 40                           je 0x140a176b1
00A17671  83 F9 3B                        cmp ecx, 0x3b
00A17674  77 14                           ja 0x140a1768a
00A17676  48 BA 01 00 00 00 01 12 00 08   movabs rdx, 0x800120100000001
00A17680  48 0F A3 CA                     bt rdx, rcx
00A17684  0F 82 61 01 00 00               jb 0x140a177eb
00A1768A  66 83 7F 02 3A                  cmp word ptr [rdi + 2], 0x3a
00A1768F  0F 84 3C 01 00 00               je 0x140a177d1
00A17695  8D 41 D0                        lea eax, [rcx - 0x30]
00A17698  66 83 F8 09                     cmp ax, 9
00A1769C  0F 87 78 02 00 00               ja 0x140a1791a
00A176A2  83 F9 44                        cmp ecx, 0x44
00A176A5  0F 84 C0 01 00 00               je 0x140a1786b
00A176AB  48 83 C7 02                     add rdi, 2
00A176AF  EB A4                           jmp 0x140a17655
00A176B1  66 44 39 4F FE                  cmp word ptr [rdi - 2], r9w
00A176B6  74 D2                           je 0x140a1768a
00A176B8  40 FE C6                        inc sil
00A176BB  66 83 7F 02 30                  cmp word ptr [rdi + 2], 0x30
00A176C0  75 E9                           jne 0x140a176ab
00A176C2  0F B7 47 04                     movzx eax, word ptr [rdi + 4]
00A176C6  66 83 E8 58                     sub ax, 0x58
00A176CA  66 41 85 C2                     test r10w, ax
00A176CE  75 DB                           jne 0x140a176ab
00A176D0  48 83 C7 04                     add rdi, 4
00A176D4  EB D5                           jmp 0x140a176ab
00A176D6  40 FE C6                        inc sil
00A176D9  66 41 3B C9                     cmp cx, r9w
00A176DD  49 89 3F                        mov qword ptr [r15], rdi
00A176E0  BB 78 00 00 C0                  mov ebx, 0xc0000078
00A176E5  41 0F 45 D8                     cmovne ebx, r8d
00A176E9  40 8A C6                        mov al, sil
00A176EC  85 DB                           test ebx, ebx
00A176EE  75 47                           jne 0x140a17737
00A176F0  40 8A CE                        mov cl, sil
00A176F3  0F B6 C0                        movzx eax, al
00A176F6  40 FE CE                        dec sil
00A176F9  84 C9                           test cl, cl
00A176FB  40 0F B6 F6                     movzx esi, sil
00A176FF  0F 44 F0                        cmove esi, eax
00A17702  40 84 F6                        test sil, sil
00A17705  0F 84 CB 01 00 00               je 0x140a178d6
00A1770B  40 0F B6 CE                     movzx ecx, sil
00A1770F  49 83 C6 02                     add r14, 2
00A17713  48 C1 E1 02                     shl rcx, 2
00A17717  E8 6C E8 F0 FF                  call 0x140925f88
00A1771C  45 33 C0                        xor r8d, r8d
00A1771F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A17724  4C 8B E8                        mov r13, rax
00A17727  48 85 C0                        test rax, rax
00A1772A  0F 85 D2 00 00 00               jne 0x140a17802
00A17730  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A17735  85 DB                           test ebx, ebx
00A17737  78 53                           js 0x140a1778c
00A17739  40 0F B6 FE                     movzx edi, sil
00A1773D  48 8D 0C BD 0C 00 00 00         lea rcx, [rdi*4 + 0xc]
00A17745  E8 3E E8 F0 FF                  call 0x140925f88
00A1774A  48 8B C8                        mov rcx, rax
00A1774D  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00A17752  48 89 08                        mov qword ptr [rax], rcx
00A17755  48 85 C9                        test rcx, rcx
00A17758  0F 84 4E 01 00 00               je 0x140a178ac
00A1775E  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00A17762  4C 8D 04 BD 00 00 00 00         lea r8, [rdi*4]
00A1776A  88 01                           mov byte ptr [rcx], al
00A1776C  49 8B D5                        mov rdx, r13
00A1776F  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00A17773  89 41 02                        mov dword ptr [rcx + 2], eax
00A17776  0F B7 44 24 34                  movzx eax, word ptr [rsp + 0x34]
00A1777B  66 89 41 06                     mov word ptr [rcx + 6], ax
00A1777F  40 88 71 01                     mov byte ptr [rcx + 1], sil
00A17783  48 83 C1 08                     add rcx, 8
00A17787  E8 B4 F0 CA FF                  call 0x1406c6840
00A1778C  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00A17791  E8 6E AC EB FF                  call 0x1408d2404
00A17796  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
00A1779B  48 85 C0                        test rax, rax
00A1779E  0F 85 F9 01 00 00               jne 0x140a1799d
00A177A4  8B C3                           mov eax, ebx
00A177A6  48 8B 8D 70 01 00 00            mov rcx, qword ptr [rbp + 0x170]
00A177AD  48 33 CC                        xor rcx, rsp
00A177B0  E8 8B 4E C9 FF                  call 0x1406ac640
00A177B5  48 8B 9C 24 D8 02 00 00         mov rbx, qword ptr [rsp + 0x2d8]
00A177BD  48 81 C4 80 02 00 00            add rsp, 0x280
00A177C4  41 5F                           pop r15
00A177C6  41 5E                           pop r14
00A177C8  41 5D                           pop r13
00A177CA  41 5C                           pop r12
00A177CC  5F                              pop rdi
00A177CD  5E                              pop rsi
00A177CE  5D                              pop rbp
00A177CF  C3                              ret
00A177D0  CC                              int3
00A177D1  8D 41 B9                        lea eax, [rcx - 0x47]
00A177D4  BA F3 FF 00 00                  mov edx, 0xfff3
00A177D9  66 85 C2                        test dx, ax
00A177DC  0F 85 B3 FE FF FF               jne 0x140a17695
00A177E2  83 F9 4B                        cmp ecx, 0x4b
00A177E5  0F 84 AA FE FF FF               je 0x140a17695
00A177EB  0F B7 4F FE                     movzx ecx, word ptr [rdi - 2]
00A177EF  66 41 3B C9                     cmp cx, r9w
00A177F3  0F 85 DD FE FF FF               jne 0x140a176d6
00A177F9  48 83 C7 FE                     add rdi, -2
00A177FD  E9 D7 FE FF FF                  jmp 0x140a176d9
00A17802  41 8B F8                        mov edi, r8d
00A17805  44 0F B6 FE                     movzx r15d, sil
00A17809  41 3B FF                        cmp edi, r15d
00A1780C  0F 83 23 FF FF FF               jae 0x140a17735
00A17812  66 41 83 3E 30                  cmp word ptr [r14], 0x30
00A17817  0F 84 3D 01 00 00               je 0x140a1795a
00A1781D  45 8B C4                        mov r8d, r12d
00A17820  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00A17825  49 8B CE                        mov rcx, r14
00A17828  E8 73 AC AE FF                  call 0x1405024a0
00A1782D  8B C8                           mov ecx, eax
00A1782F  8B C7                           mov eax, edi
00A17831  41 89 4C 85 00                  mov dword ptr [r13 + rax*4], ecx
00A17836  4C 8B 74 24 38                  mov r14, qword ptr [rsp + 0x38]
00A1783B  4D 85 F6                        test r14, r14
00A1783E  74 19                           je 0x140a17859
00A17840  41 0F B7 0E                     movzx ecx, word ptr [r14]
00A17844  83 F9 3B                        cmp ecx, 0x3b
00A17847  77 6D                           ja 0x140a178b6
00A17849  48 BA 01 00 00 00 00 32 00 08   movabs rdx, 0x800320000000001
00A17853  48 0F A3 CA                     bt rdx, rcx
00A17857  73 5D                           jae 0x140a178b6
00A17859  49 83 C6 02                     add r14, 2
00A1785D  FF C7                           inc edi
00A1785F  EB A8                           jmp 0x140a17809
00A17861  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A17866  E9 3B FF FF FF                  jmp 0x140a177a6
00A1786B  66 83 7F 02 3A                  cmp word ptr [rdi + 2], 0x3a
00A17870  0F 85 35 FE FF FF               jne 0x140a176ab
00A17876  48 8B C7                        mov rax, rdi
00A17879  4D 8B EE                        mov r13, r14
00A1787C  49 2B C6                        sub rax, r14
00A1787F  48 D1 F8                        sar rax, 1
00A17882  4C 8D 3C 00                     lea r15, [rax + rax]
00A17886  4D 8B E7                        mov r12, r15
00A17889  48 3D 00 01 00 00               cmp rax, 0x100
00A1788F  0F 8C A9 00 00 00               jl 0x140a1793e
00A17895  49 8D 4F 02                     lea rcx, [r15 + 2]
00A17899  E8 EA E6 F0 FF                  call 0x140925f88
00A1789E  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A178A3  48 85 C0                        test rax, rax
00A178A6  0F 85 9C 00 00 00               jne 0x140a17948
00A178AC  BB 17 00 00 C0                  mov ebx, 0xc0000017
00A178B1  E9 D6 FE FF FF                  jmp 0x140a1778c
00A178B6  66 41 83 7E 02 3A               cmp word ptr [r14 + 2], 0x3a
00A178BC  0F 84 BA 00 00 00               je 0x140a1797c
00A178C2  BB 78 00 00 C0                  mov ebx, 0xc0000078
00A178C7  E9 69 FE FF FF                  jmp 0x140a17735
00A178CC  B8 78 00 00 C0                  mov eax, 0xc0000078
00A178D1  E9 D0 FE FF FF                  jmp 0x140a177a6
00A178D6  BB 78 00 00 C0                  mov ebx, 0xc0000078
00A178DB  E9 AC FE FF FF                  jmp 0x140a1778c
00A178E0  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00A178E4  66 83 E8 58                     sub ax, 0x58
00A178E8  66 85 C2                        test dx, ax
00A178EB  44 0F 44 E1                     cmove r12d, ecx
00A178EF  44 89 64 24 40                  mov dword ptr [rsp + 0x40], r12d
00A178F4  E9 46 FC FF FF                  jmp 0x140a1753f
00A178F9  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00A178FD  B9 DF FF 00 00                  mov ecx, 0xffdf
00A17902  66 83 E8 58                     sub ax, 0x58
00A17906  41 B9 10 00 00 00               mov r9d, 0x10
00A1790C  66 85 C1                        test cx, ax
00A1790F  0F 84 98 FC FF FF               je 0x140a175ad
00A17915  E9 90 FC FF FF                  jmp 0x140a175aa
00A1791A  8D 41 9F                        lea eax, [rcx - 0x61]
00A1791D  66 83 F8 05                     cmp ax, 5
00A17921  0F 86 84 FD FF FF               jbe 0x140a176ab
00A17927  8D 41 BF                        lea eax, [rcx - 0x41]
00A1792A  66 83 F8 05                     cmp ax, 5
00A1792E  0F 86 6E FD FF FF               jbe 0x140a176a2
00A17934  BB 78 00 00 C0                  mov ebx, 0xc0000078
00A17939  E9 CA F7 11 00                  jmp 0x140b37108
00A1793E  4C 8D 74 24 70                  lea r14, [rsp + 0x70]
00A17943  E9 92 F7 11 00                  jmp 0x140b370da
00A17948  4C 8B F0                        mov r14, rax
00A1794B  E9 8A F7 11 00                  jmp 0x140b370da
00A17950  BB 95 00 00 C0                  mov ebx, 0xc0000095
00A17955  E9 AE F7 11 00                  jmp 0x140b37108
00A1795A  41 0F B7 46 02                  movzx eax, word ptr [r14 + 2]
00A1795F  B9 DF FF 00 00                  mov ecx, 0xffdf
00A17964  66 83 E8 58                     sub ax, 0x58
00A17968  41 B8 10 00 00 00               mov r8d, 0x10
00A1796E  66 85 C1                        test cx, ax
00A17971  0F 84 A9 FE FF FF               je 0x140a17820
00A17977  E9 A1 FE FF FF                  jmp 0x140a1781d
00A1797C  66 83 E9 44                     sub cx, 0x44
00A17980  66 83 F9 0F                     cmp cx, 0xf
00A17984  0F 87 38 FF FF FF               ja 0x140a178c2
00A1798A  B8 09 88 00 00                  mov eax, 0x8809
00A1798F  0F A3 C8                        bt eax, ecx
00A17992  0F 83 2A FF FF FF               jae 0x140a178c2
00A17998  E9 BC FE FF FF                  jmp 0x140a17859
00A1799D  48 8B C8                        mov rcx, rax
00A179A0  E8 5F AA EB FF                  call 0x1408d2404
00A179A5  E9 FA FD FF FF                  jmp 0x140a177a4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LocalpConvertStringSidToSid(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m274;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m283;
    unsigned __int8 v_stack_m284;
    unsigned __int8 v_stack_m285;
    unsigned __int8 v_stack_m286;
    unsigned __int8 v_stack_m287;
    unsigned __int8 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned int v_stack_m298;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p38;
    unsigned int v_stack_p40;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p70;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (640);
    result = (*(unsigned __int64 *)(v_rip + 4141706)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rsi = 0;
    v_stack_m258 = a3;
    v_stack_m250 = a2;
    v_stack_m268 = 0;
    v_stack_m280 = 0;
    v_stack_m260 = 0;
    v_stack_m278 = (unsigned int)(v_rsi + 10);
    if (a1 == 0) goto loc_00A17861;
    if (a2 == 0) goto loc_00A17861;
    if (a3 == 0) goto loc_00A17861;
    result = (unsigned __int16)((*(unsigned __int16 *)(a1)) - (83));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) != 0) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(a1 + 2)) != ((unsigned __int16)(v_rsi + 45))) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(a1 + 4)) == 48) goto loc_00A178E0;
loc_00A1753F:
    result = wcstoul(a1 + 4, v_stack_m280, (unsigned int)((unsigned int)(v_rsi + 10)), a4);
    v_stack_m270 = (unsigned int)(result);
    if (((unsigned int)(result)) > 255) goto loc_00A178CC;
    if (v_stack_m280 == (a1 + 4)) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(v_stack_m280)) != ((unsigned __int16)(v_rsi + 45))) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(v_stack_m280 + 2)) == 0) goto loc_00A178CC;
    result = wcschr(v_stack_m280 + 2, (unsigned int)((unsigned int)(v_rsi + 45)), (unsigned int)((unsigned int)(v_rsi + 10)), a4);
    if (result == 0) goto loc_00A178CC;
    if (result == (v_stack_m280 + 2)) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(v_stack_m280 + 2)) == 48) goto loc_00A178F9;
loc_00A175AA:
loc_00A175AD:
    v_stack_m274 = 0;
    v_stack_m290 = v_stack_m274;
    v_stack_m298 = 1;
    a1 = 0;
    result = wcstoxq(a1, v_stack_m280 + 2, v_stack_m280, (unsigned int)((unsigned int)(v_rsi + 10)));
    if (result > result) goto loc_00A178CC;
    if (v_stack_m280 == (v_stack_m280 + 2)) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(v_stack_m280)) != 45) goto loc_00A178CC;
    if ((*(unsigned __int16 *)(v_stack_m280 + 2)) == 0) goto loc_00A178CC;
    v_stack_m283 = (unsigned __int8)(result);
    result = (result) >> (8);
    v_stack_m284 = (unsigned __int8)(result);
    result = (result) >> (16);
    v_stack_m285 = (unsigned __int8)(result);
    result = (result) >> (24);
    v_stack_m286 = (unsigned __int8)(result);
    result = (result) >> (32);
    a1 = (result) >> (40);
    v_stack_m287 = (unsigned __int8)(result);
    a3 = 0;
    v_stack_m288 = (unsigned __int8)(a1);
loc_00A17655:
    if (v_stack_m280 == 0) goto loc_00A176E9;
    if (0 == 255) goto loc_00A17950;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m280))) == 45) goto loc_00A176B1;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m280))) > 59) goto loc_00A1768A;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m280))) < 59) goto loc_00A177EB;
loc_00A1768A:
    if ((*(unsigned __int16 *)(v_stack_m280 + 2)) == 58) goto loc_00A177D1;
loc_00A17695:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m280) - 48)) > 9) goto loc_00A1791A;
loc_00A176A2:
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_m280))) == 68) goto loc_00A1786B;
loc_00A176AB:
    v_rdi = (v_stack_m280) + (2);
    goto loc_00A17655;
loc_00A176B1:
    if ((*(unsigned __int16 *)(v_rdi - 2)) == 45) goto loc_00A1768A;
    v_rsi = (unsigned __int8)((v_rsi) + 1);
    if ((*(unsigned __int16 *)(v_rdi + 2)) != 48) goto loc_00A176AB;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + 4)) - (88));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) != 0) goto loc_00A176AB;
    v_rdi = (v_rdi) + (4);
    goto loc_00A176AB;
loc_00A176D6:
    v_rsi = (unsigned __int8)((v_rsi) + 1);
loc_00A176D9:
    *(unsigned __int64 *)(a3) = v_rdi;
    v_rbx = (unsigned int)(0xC0000078ULL);
    if (((unsigned __int16)(*(unsigned __int16 *)(v_stack_m280))) != 45) { v_rbx = 0; }
loc_00A176E9:
    if ((unsigned int)(v_rbx) != 0) goto loc_00A17737;
    v_rsi = (unsigned __int8)((v_rsi) - 1);
    v_rsi = (unsigned __int8)(v_rsi);
    if ((unsigned __int8)((unsigned __int8)(v_rsi)) == 0) { v_rsi = (unsigned int)((unsigned __int8)((unsigned __int8)(v_rsi))); }
    if ((unsigned __int8)(v_rsi) == 0) goto loc_00A178D6;
    v_r14 = (v_stack_m280) + (2);
    a1 = ((unsigned __int8)(v_rsi)) << (2);
    result = SddlpAlloc(a1, v_stack_m280 + 2, a3, 45);
    a3 = 0;
    v_stack_m268 = result;
    if (result != 0) goto loc_00A17802;
loc_00A17735:
loc_00A17737:
    if (sign_flag) goto loc_00A1778C;
    result = SddlpAlloc((unsigned __int8)(v_rsi) * 4 + 12, v_stack_m280 + 2, a3, 45);
    *(unsigned __int64 *)(v_stack_m250) = result;
    if (result == 0) goto loc_00A178AC;
    *(unsigned __int8 *)(result) = (unsigned __int8)((unsigned int)(v_stack_m270));
    *(unsigned int *)(result + 2) = (unsigned int)((unsigned int)(v_stack_m288));
    *(unsigned __int16 *)(result + 6) = (unsigned __int16)(v_stack_m284);
    *(unsigned __int8 *)(result + 1) = (unsigned __int8)(v_rsi);
    a1 = (result) + (8);
    result = memcpy(a1, result, (unsigned __int8)(v_rsi) * 4, 45);
loc_00A1778C:
    result = PdcCloseEvent(v_stack_m268, result, (unsigned __int8)(v_rsi) * 4, 45);
    if (v_stack_m260 != 0) goto loc_00A1799D;
loc_00A177A4:
loc_00A177A6:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, result, (unsigned __int8)(v_rsi) * 4, 45);
    v_rsp = (v_rsp) + (640);
    return result;
loc_00A177D1:
    if ((((unsigned __int16)((unsigned int)(0xFFF3ULL))) & ((unsigned __int16)(a1 - 71))) != 0) goto loc_00A17695;
    if (((unsigned int)(a1)) == 75) goto loc_00A17695;
loc_00A177EB:
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned __int8)(v_rsi) - 2))) != 45) goto loc_00A176D6;
    v_rdi = ((unsigned __int8)(v_rsi)) + (-2);
    goto loc_00A176D9;
loc_00A17802:
loc_00A17809:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) * 4)))) >= ((unsigned int)((unsigned __int8)(v_rsi)))) goto loc_00A17735;
    if ((*(unsigned __int16 *)(v_r14)) == 48) goto loc_00A1795A;
loc_00A1781D:
loc_00A17820:
    result = wcstoul(v_r14, v_stack_p38, (unsigned int)((unsigned int)(v_rsi + 10)), 45);
    *(unsigned int *)(result + (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) * 4)))) * 4) = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (v_stack_p38 == 0) goto loc_00A17859;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p38))) > 59) goto loc_00A178B6;
    if (((unsigned int)(*(unsigned __int16 *)(v_stack_p38))) >= 59) goto loc_00A178B6;
loc_00A17859:
    v_r14 = (v_stack_p38) + (2);
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned __int8)(v_rsi) * 4))) + 1);
    goto loc_00A17809;
loc_00A17861:
    goto loc_00A177A6;
loc_00A1786B:
    if ((*(unsigned __int16 *)(v_rdi + 2)) != 58) goto loc_00A176AB;
    result = (v_rdi) - (v_r14);
    result = (result) >> (1);
    if (result < 256) goto loc_00A1793E;
    result = SddlpAlloc(result + result * 1 + 2, v_stack_p38, (unsigned int)((unsigned int)(v_rsi + 10)), 45);
    v_stack_p58 = result;
    if (result != 0) goto loc_00A17948;
loc_00A178AC:
    goto loc_00A1778C;
loc_00A178B6:
    if ((*(unsigned __int16 *)(v_r14 + 2)) == 58) goto loc_00A1797C;
loc_00A178C2:
    goto loc_00A17735;
loc_00A178CC:
    goto loc_00A177A6;
loc_00A178D6:
    goto loc_00A1778C;
loc_00A178E0:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + 2)) - (88));
    v_r12 = result + result * 1;
    if ((((unsigned __int16)(v_stack_p38)) & ((unsigned __int16)(result))) == 0) { v_r12 = (unsigned int)(result + result * 1 + 2); }
    v_stack_p40 = (unsigned int)(v_r12);
    goto loc_00A1753F;
loc_00A178F9:
    result = (unsigned __int16)((*(unsigned __int16 *)(v_rdi + 2)) - (88));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) == 0) goto loc_00A175AD;
    goto loc_00A175AA;
loc_00A1791A:
    if (((unsigned __int16)((unsigned int)(0xFFDFULL) - 97)) <= 5) goto loc_00A176AB;
    if (((unsigned __int16)((unsigned int)(0xFFDFULL) - 65)) <= 5) goto loc_00A176A2;
loc_00A1793E:
loc_00A17948:
loc_00A17950:
loc_00A1795A:
    result = (unsigned __int16)((*(unsigned __int16 *)((unsigned int)(0xFFDFULL) - 65 + 2)) - (88));
    if ((((unsigned __int16)((unsigned int)(0xFFDFULL))) & ((unsigned __int16)(result))) == 0) goto loc_00A17820;
    goto loc_00A1781D;
loc_00A1797C:
    a1 = (unsigned __int16)(((unsigned int)(0xFFDFULL)) - (68));
    if (((unsigned __int16)(a1)) > 15) goto loc_00A178C2;
    if (((unsigned __int16)(a1)) >= 15) goto loc_00A178C2;
    goto loc_00A17859;
loc_00A1799D:
    result = PdcCloseEvent((unsigned int)(0x8809ULL), v_stack_p38, 16, 16);
    goto loc_00A177A4;
}
```

## 5. (Beta) C Style

```c
int64_t LocalpConvertStringSidToSid(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m274;
    uint32_t v_stack_m278;
    uint64_t v_stack_m280;
    uint8_t v_stack_m283;
    uint8_t v_stack_m284;
    uint8_t v_stack_m285;
    uint8_t v_stack_m286;
    uint8_t v_stack_m287;
    uint8_t v_stack_m288;
    uint64_t v_stack_m290;
    uint32_t v_stack_m298;
    uint64_t v_stack_m48;
    uint64_t v_stack_p20;
    uint64_t v_stack_p38;
    uint32_t v_stack_p40;
    uint64_t v_stack_p58;
    uint64_t v_stack_p70;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (640);
    result = (*(uint64_t *)(v_rip + 0x3F328A)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rsi = 0;
    v_stack_m258 = Arg3;
    v_stack_m250 = Arg2;
    v_stack_m268 = 0;
    v_stack_m280 = 0;
    v_stack_m260 = 0;
    v_stack_m278 = (uint32_t)(local_rsi + 10);
    if (Arg1 == 0) goto loc_00A17861;
    if (Arg2 == 0) goto loc_00A17861;
    if (Arg3 == NULL) goto loc_00A17861;
    result = (uint16_t)((*(uint16_t *)(Arg1)) - (83));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) != 0) goto loc_00A178CC;
    if ((*(uint16_t *)(Arg1 + 0x2)) != ((uint16_t)(local_rsi + 45))) goto loc_00A178CC;
    if ((*(uint16_t *)(Arg1 + 0x4)) == 48) goto loc_00A178E0;
loc_00A1753F:
    result = wcstoul(Arg1 + 4, v_stack_m280, (uint32_t)((uint32_t)(local_rsi + 10)), a4);
    v_stack_m270 = (uint32_t)(result);
    if (((uint32_t)(result)) > 255) goto loc_00A178CC;
    if (v_stack_m280 == (Arg1 + 4)) goto loc_00A178CC;
    if ((*(uint16_t *)(v_stack_m280)) != ((uint16_t)(local_rsi + 45))) goto loc_00A178CC;
    if ((*(uint16_t *)(v_stack_m280 + 0x2)) == 0) goto loc_00A178CC;
    result = wcschr(v_stack_m280 + 2, (uint32_t)((uint32_t)(local_rsi + 45)), (uint32_t)((uint32_t)(local_rsi + 10)), a4);
    if (result == 0) goto loc_00A178CC;
    if (result == (v_stack_m280 + 2)) goto loc_00A178CC;
    if ((*(uint16_t *)(v_stack_m280 + 0x2)) == 48) goto loc_00A178F9;
loc_00A175AA:
loc_00A175AD:
    v_stack_m274 = 0;
    v_stack_m290 = v_stack_m274;
    v_stack_m298 = 1;
    Arg1 = 0;
    result = wcstoxq(Arg1, v_stack_m280 + 2, v_stack_m280, (uint32_t)((uint32_t)(local_rsi + 10)));
    if (result > result) goto loc_00A178CC;
    if (v_stack_m280 == (v_stack_m280 + 2)) goto loc_00A178CC;
    if ((*(uint16_t *)(v_stack_m280)) != 45) goto loc_00A178CC;
    if ((*(uint16_t *)(v_stack_m280 + 0x2)) == 0) goto loc_00A178CC;
    v_stack_m283 = (uint8_t)(result);
    result = (result) >> (8);
    v_stack_m284 = (uint8_t)(result);
    result = (result) >> (16);
    v_stack_m285 = (uint8_t)(result);
    result = (result) >> (24);
    v_stack_m286 = (uint8_t)(result);
    result = (result) >> (32);
    Arg1 = (result) >> (40);
    v_stack_m287 = (uint8_t)(result);
    Arg3 = 0;
    v_stack_m288 = (uint8_t)(Arg1);
loc_00A17655:
    if (v_stack_m280 == 0) goto loc_00A176E9;
    if (0 == 255) goto loc_00A17950;
    if (((uint16_t)(*(uint16_t *)(v_stack_m280))) == 45) goto loc_00A176B1;
    if (((uint32_t)(*(uint16_t *)(v_stack_m280))) > 59) goto loc_00A1768A;
    if (((uint32_t)(*(uint16_t *)(v_stack_m280))) < 59) goto loc_00A177EB;
loc_00A1768A:
    if ((*(uint16_t *)(v_stack_m280 + 0x2)) == 58) goto loc_00A177D1;
loc_00A17695:
    if (((uint16_t)(*(uint16_t *)(v_stack_m280) - 48)) > 9) goto loc_00A1791A;
loc_00A176A2:
    if (((uint32_t)(*(uint16_t *)(v_stack_m280))) == 68) goto loc_00A1786B;
loc_00A176AB:
    local_rdi = (v_stack_m280) + (2);
    goto loc_00A17655;
loc_00A176B1:
    if ((*(uint16_t *)(local_rdi - 0x2)) == 45) goto loc_00A1768A;
    local_rsi = (uint8_t)((local_rsi) + 1);
    if ((*(uint16_t *)(local_rdi + 0x2)) != 48) goto loc_00A176AB;
    result = (uint16_t)((*(uint16_t *)(local_rdi + 0x4)) - (88));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) != 0) goto loc_00A176AB;
    local_rdi = (local_rdi) + (4);
    goto loc_00A176AB;
loc_00A176D6:
    local_rsi = (uint8_t)((local_rsi) + 1);
loc_00A176D9:
    *(uint64_t *)(arg3) = local_rdi;
    local_rbx = (uint32_t)(0xC0000078ULL);
    if (((uint16_t)(*(uint16_t *)(v_stack_m280))) != 45) { local_rbx = 0; }
loc_00A176E9:
    if ((uint32_t)(local_rbx) != 0) goto loc_00A17737;
    local_rsi = (uint8_t)((local_rsi) - 1);
    local_rsi = (uint8_t)(local_rsi);
    if ((uint8_t)((uint8_t)(local_rsi)) == 0) { local_rsi = (uint32_t)((uint8_t)((uint8_t)(local_rsi))); }
    if ((uint8_t)(local_rsi) == 0) goto loc_00A178D6;
    local_r14 = (v_stack_m280) + (2);
    Arg1 = ((uint8_t)(local_rsi)) << (2);
    result = SddlpAlloc(Arg1, v_stack_m280 + 2, Arg3, 45);
    Arg3 = 0;
    v_stack_m268 = result;
    if (result != 0) goto loc_00A17802;
loc_00A17735:
loc_00A17737:
    if (sign_flag) goto loc_00A1778C;
    result = SddlpAlloc((uint8_t)(local_rsi) * 4 + 12, v_stack_m280 + 2, Arg3, 45);
    *(uint64_t *)(v_stack_m250) = result;
    if (result == 0) goto loc_00A178AC;
    *(uint8_t *)(result) = (uint8_t)((uint32_t)(v_stack_m270));
    *(uint32_t *)(result + 0x2) = (uint32_t)((uint32_t)(v_stack_m288));
    *(uint16_t *)(result + 0x6) = (uint16_t)(v_stack_m284);
    *(uint8_t *)(result + 0x1) = (uint8_t)(local_rsi);
    Arg1 = (result) + (8);
    result = memcpy(Arg1, result, (uint8_t)(local_rsi) * 4, 45);
loc_00A1778C:
    result = PdcCloseEvent(v_stack_m268, result, (uint8_t)(local_rsi) * 4, 45);
    if (v_stack_m260 != 0) goto loc_00A1799D;
loc_00A177A4:
loc_00A177A6:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, result, (uint8_t)(local_rsi) * 4, 45);
    local_rsp = (local_rsp) + (640);
    return result;
loc_00A177D1:
    if ((((uint16_t)((uint32_t)(0xFFF3ULL))) & ((uint16_t)(Arg1 - 71))) != 0) goto loc_00A17695;
    if (((uint32_t)(Arg1)) == 75) goto loc_00A17695;
loc_00A177EB:
    if (((uint16_t)(*(uint16_t *)((uint8_t)(local_rsi) - 0x2))) != 45) goto loc_00A176D6;
    local_rdi = ((uint8_t)(local_rsi)) + (-2);
    goto loc_00A176D9;
loc_00A17802:
loc_00A17809:
    if (((uint32_t)((uint32_t)((uint32_t)((uint8_t)(local_rsi) * 4)))) >= ((uint32_t)((uint8_t)(local_rsi)))) goto loc_00A17735;
    if ((*(uint16_t *)(local_r14)) == 48) goto loc_00A1795A;
loc_00A1781D:
loc_00A17820:
    result = wcstoul(local_r14, v_stack_p38, (uint32_t)((uint32_t)(local_rsi + 10)), 45);
    *(uint32_t *)(result + (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint8_t)(local_rsi) * 4)))) * 4) = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (v_stack_p38 == 0) goto loc_00A17859;
    if (((uint32_t)(*(uint16_t *)(v_stack_p38))) > 59) goto loc_00A178B6;
    if (((uint32_t)(*(uint16_t *)(v_stack_p38))) >= 59) goto loc_00A178B6;
loc_00A17859:
    local_r14 = (v_stack_p38) + (2);
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint8_t)(local_rsi) * 4))) + 1);
    goto loc_00A17809;
loc_00A17861:
    goto loc_00A177A6;
loc_00A1786B:
    if ((*(uint16_t *)(local_rdi + 0x2)) != 58) goto loc_00A176AB;
    result = (local_rdi) - (local_r14);
    result = (result) >> (1);
    if (result < 256) goto loc_00A1793E;
    result = SddlpAlloc(result + result * 1 + 2, v_stack_p38, (uint32_t)((uint32_t)(local_rsi + 10)), 45);
    v_stack_p58 = result;
    if (result != 0) goto loc_00A17948;
loc_00A178AC:
    goto loc_00A1778C;
loc_00A178B6:
    if ((*(uint16_t *)(local_r14 + 0x2)) == 58) goto loc_00A1797C;
loc_00A178C2:
    goto loc_00A17735;
loc_00A178CC:
    goto loc_00A177A6;
loc_00A178D6:
    goto loc_00A1778C;
loc_00A178E0:
    result = (uint16_t)((*(uint16_t *)(local_rdi + 0x2)) - (88));
    local_r12 = result + result * 1;
    if ((((uint16_t)(v_stack_p38)) & ((uint16_t)(result))) == 0) { local_r12 = (uint32_t)(result + result * 1 + 2); }
    v_stack_p40 = (uint32_t)(local_r12);
    goto loc_00A1753F;
loc_00A178F9:
    result = (uint16_t)((*(uint16_t *)(local_rdi + 0x2)) - (88));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) == 0) goto loc_00A175AD;
    goto loc_00A175AA;
loc_00A1791A:
    if (((uint16_t)((uint32_t)(0xFFDFULL) - 97)) <= 5) goto loc_00A176AB;
    if (((uint16_t)((uint32_t)(0xFFDFULL) - 65)) <= 5) goto loc_00A176A2;
loc_00A1793E:
loc_00A17948:
loc_00A17950:
loc_00A1795A:
    result = (uint16_t)((*(uint16_t *)((uint32_t)(0xFFDFULL) - 0x41 + 0x2)) - (88));
    if ((((uint16_t)((uint32_t)(0xFFDFULL))) & ((uint16_t)(result))) == 0) goto loc_00A17820;
    goto loc_00A1781D;
loc_00A1797C:
    Arg1 = (uint16_t)(((uint32_t)(0xFFDFULL)) - (68));
    if (((uint16_t)(Arg1)) > 15) goto loc_00A178C2;
    if (((uint16_t)(Arg1)) >= 15) goto loc_00A178C2;
    goto loc_00A17859;
loc_00A1799D:
    result = PdcCloseEvent((uint32_t)(0x8809ULL), v_stack_p38, 16, 16);
    goto loc_00A177A4;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A17490&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
