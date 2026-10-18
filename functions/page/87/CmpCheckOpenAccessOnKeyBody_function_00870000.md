# CmpCheckOpenAccessOnKeyBody

- RVA: `0x00870000`–`0x00870AB3` (길이 `2,739` bytes)
- VA: `0x0000000140870000`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2B0`
- 디코드: `680`개 명령, `2,739/2,739` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **34**; 고유 호출 대상: **24**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00870114` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00870168` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x0087024D` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00870274` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008702CA` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0087031F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0087032C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00870399` → [SeOpenObjectAuditAlarmWithTransaction](../86/SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)
- `0x008703B0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008703BE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008703D0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008703DE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008703F5` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x00870487` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x008704C7` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x0087053F` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x00870583` → [CmpStartKcbStackForTopLayerKcb](../84/CmpStartKcbStackForTopLayerKcb_function_00848390.md) (function, `0x00848390`)
- `0x0087065E` → [SeSinglePrivilegeCheckEx](SeSinglePrivilegeCheckEx_function_00871AC0.md) (function, `0x00871AC0`)
- `0x00870681` → [SeSinglePrivilegeCheckEx](SeSinglePrivilegeCheckEx_function_00871AC0.md) (function, `0x00871AC0`)
- `0x008706B6` → [SepAdjustAccessStateForConstraints](../94/SepAdjustAccessStateForConstraints_function_00947E10.md) (function, `0x00947E10`)
- `0x00870723` → [CmpIsSystemEntity](../8B/CmpIsSystemEntity_function_008B4E90.md) (function, `0x008B4E90`)
- `0x0087073F` → [CmpCheckAdminAccess](../9A/CmpCheckAdminAccess_function_009A87A0.md) (function, `0x009A87A0`)
- `0x00870770` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (function, `0x0047C7E0`)
- `0x0087077B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00870783` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (function, `0x0045ED00`)
- `0x0087078D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x008707AE` → [CmpCheckKeyOwnerForPca](../8C/CmpCheckKeyOwnerForPca_function_008C7130.md) (function, `0x008C7130`)
- `0x008708AF` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x0087092E` → [CmpTransUowIsEqual](../70/CmpTransUowIsEqual_function_007049CC.md) (function, `0x007049CC`)
- `0x00870991` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008709B4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008709BF` → [SepConcatenatePrivileges](../9D/SepConcatenatePrivileges_function_009D7AD0.md) (function, `0x009D7AD0`)
- `0x008709D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00870A32` → [CmpCheckKeyBodyAccess](../86/CmpCheckKeyBodyAccess_function_0086FA00.md) (function, `0x0086FA00`)

### Direct callers
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x00860129`

### Static image references
- `0x008702A3` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x00870657` → RVA `0x00FD9AC0` (`PAGEDATA`; read)
- `0x00870672` → RVA `0x00FD9AE0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **20**
  - `0x00870114` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00870168` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x0087024D` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00870274` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008702CA` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0087031F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0087032C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x008703B0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008703BE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008703D0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008703DE` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008703F5` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x00870770` → [PsGetCurrentThreadProcess](../../text/47/PsGetCurrentThreadProcess_function_0047C7E0.md) (`PAGE` → `.text`)
  - `0x0087077B` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00870783` → [PsGetServerSiloServiceSessionId](../../text/45/PsGetServerSiloServiceSessionId_function_0045ED00.md) (`PAGE` → `.text`)
  - `0x0087078D` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x008708AF` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x00870991` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008709B4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008709D0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00870000  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00870005  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0087000A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0087000F  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00870014  55                              push rbp
00870015  56                              push rsi
00870016  57                              push rdi
00870017  41 54                           push r12
00870019  41 55                           push r13
0087001B  41 56                           push r14
0087001D  41 57                           push r15
0087001F  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00870024  48 81 EC 90 00 00 00            sub rsp, 0x90
0087002B  0F B7 7A 02                     movzx edi, word ptr [rdx + 2]
0087002F  4C 8D 79 04                     lea r15, [rcx + 4]
00870033  45 33 F6                        xor r14d, r14d
00870036  C6 45 C7 00                     mov byte ptr [rbp - 0x39], 0
0087003A  49 8B F1                        mov rsi, r9
0087003D  4C 8B E9                        mov r13, rcx
00870040  45 8D 46 FF                     lea r8d, [r14 - 1]
00870044  66 85 FF                        test di, di
00870047  78 5D                           js 0x1408700a6
00870049  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
0087004D  4C 8B 7D 4F                     mov r15, qword ptr [rbp + 0x4f]
00870051  0F B7 FF                        movzx edi, di
00870054  83 FF 02                        cmp edi, 2
00870057  0F 83 C8 05 00 00               jae 0x140870625
0087005D  49 8B 5C FF 08                  mov rbx, qword ptr [r15 + rdi*8 + 8]
00870062  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
00870067  74 06                           je 0x14087006f
00870069  80 7B 41 01                     cmp byte ptr [rbx + 0x41], 1
0087006D  74 33                           je 0x1408700a2
0087006F  83 7B 28 FF                     cmp dword ptr [rbx + 0x28], -1
00870073  0F 84 21 04 00 00               je 0x14087049a
00870079  48 8B 93 F0 00 00 00            mov rdx, qword ptr [rbx + 0xf0]
00870080  48 85 D2                        test rdx, rdx
00870083  0F 85 D9 03 00 00               jne 0x140870462
00870089  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
0087008E  4C 8B F3                        mov r14, rbx
00870091  74 06                           je 0x140870099
00870093  80 7B 41 00                     cmp byte ptr [rbx + 0x41], 0
00870097  75 09                           jne 0x1408700a2
00870099  41 0F B7 C0                     movzx eax, r8w
0087009D  66 03 F8                        add di, ax
008700A0  79 AF                           jns 0x140870051
008700A2  4D 8D 7D 04                     lea r15, [r13 + 4]
008700A6  4D 85 FF                        test r15, r15
008700A9  74 09                           je 0x1408700b4
008700AB  41 0F B7 46 42                  movzx eax, word ptr [r14 + 0x42]
008700B0  66 41 89 07                     mov word ptr [r15], ax
008700B4  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
008700B8  4D 8B 7E 58                     mov r15, qword ptr [r14 + 0x58]
008700BC  4D 85 E4                        test r12, r12
008700BF  0F 85 17 04 00 00               jne 0x1408704dc
008700C5  44 0F B6 75 6F                  movzx r14d, byte ptr [rbp + 0x6f]
008700CA  45 84 F6                        test r14b, r14b
008700CD  0F 85 71 05 00 00               jne 0x140870644
008700D3  49 8B 7D 08                     mov rdi, qword ptr [r13 + 8]
008700D7  0F 57 C0                        xorps xmm0, xmm0
008700DA  8B 56 18                        mov edx, dword ptr [rsi + 0x18]
008700DD  B8 FF FF FF FF                  mov eax, 0xffffffff
008700E2  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
008700E6  66 89 45 E1                     mov word ptr [rbp - 0x1f], ax
008700EA  48 8B 4F 20                     mov rcx, qword ptr [rdi + 0x20]
008700EE  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
008700F2  F7 81 A0 00 00 00 00 00 10 00   test dword ptr [rcx + 0xa0], 0x100000
008700FC  0F 85 48 04 00 00               jne 0x14087054a
00870102  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00870106  45 33 FF                        xor r15d, r15d
00870109  41 8B DF                        mov ebx, r15d
0087010C  48 85 D2                        test rdx, rdx
0087010F  74 08                           je 0x140870119
00870111  48 8B CA                        mov rcx, rdx
00870114  E8 67 5C C0 FF                  call 0x140475d80
00870119  85 DB                           test ebx, ebx
0087011B  0F 88 F5 06 00 00               js 0x140870816
00870121  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
00870124  48 8B 7D 57                     mov rdi, qword ptr [rbp + 0x57]
00870128  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
0087012B  23 C1                           and eax, ecx
0087012D  3B C1                           cmp eax, ecx
0087012F  0F 85 E1 06 00 00               jne 0x140870816
00870135  45 84 F6                        test r14b, r14b
00870138  0F 85 06 07 00 00               jne 0x140870844
0087013E  85 C9                           test ecx, ecx
00870140  0F 84 F6 02 00 00               je 0x14087043c
00870146  0F 57 C0                        xorps xmm0, xmm0
00870149  44 89 7D CF                     mov dword ptr [rbp - 0x31], r15d
0087014D  B8 FF FF FF FF                  mov eax, 0xffffffff
00870152  4C 89 7D D7                     mov qword ptr [rbp - 0x29], r15
00870156  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
0087015A  49 8B D4                        mov rdx, r12
0087015D  66 89 45 E1                     mov word ptr [rbp - 0x1f], ax
00870161  49 8B CD                        mov rcx, r13
00870164  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00870168  E8 13 93 35 00                  call 0x140bc9480
0087016D  84 C0                           test al, al
0087016F  0F 85 DE 06 00 00               jne 0x140870853
00870175  49 8B 7D 08                     mov rdi, qword ptr [r13 + 8]
00870179  4D 8B F7                        mov r14, r15
0087017C  0F BF 5F 42                     movsx ebx, word ptr [rdi + 0x42]
00870180  83 FB 02                        cmp ebx, 2
00870183  7C 0B                           jl 0x140870190
00870185  8B C3                           mov eax, ebx
00870187  83 E8 01                        sub eax, 1
0087018A  0F 85 0E 07 00 00               jne 0x14087089e
00870190  48 0F BF 47 42                  movsx rax, word ptr [rdi + 0x42]
00870195  66 89 5D DF                     mov word ptr [rbp - 0x21], bx
00870199  4C 89 75 F7                     mov qword ptr [rbp - 9], r14
0087019D  66 89 45 E1                     mov word ptr [rbp - 0x1f], ax
008701A1  66 85 C0                        test ax, ax
008701A4  0F 85 B8 06 00 00               jne 0x140870862
008701AA  48 89 7C C5 E7                  mov qword ptr [rbp + rax*8 - 0x19], rdi
008701AF  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
008701B3  0F B7 7D E1                     movzx edi, word ptr [rbp - 0x1f]
008701B7  41 8B C7                        mov eax, r15d
008701BA  89 45 CB                        mov dword ptr [rbp - 0x35], eax
008701BD  66 85 FF                        test di, di
008701C0  78 5B                           js 0x14087021d
008701C2  41 BD FF FF FF FF               mov r13d, 0xffffffff
008701C8  0F B7 FF                        movzx edi, di
008701CB  83 FF 02                        cmp edi, 2
008701CE  0F 83 F7 04 00 00               jae 0x1408706cb
008701D4  48 8B 5C FD E7                  mov rbx, qword ptr [rbp + rdi*8 - 0x19]
008701D9  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
008701DE  74 06                           je 0x1408701e6
008701E0  80 7B 41 01                     cmp byte ptr [rbx + 0x41], 1
008701E4  74 33                           je 0x140870219
008701E6  83 7B 28 FF                     cmp dword ptr [rbx + 0x28], -1
008701EA  0F 84 E4 02 00 00               je 0x1408704d4
008701F0  48 8B 93 F0 00 00 00            mov rdx, qword ptr [rbx + 0xf0]
008701F7  48 85 D2                        test rdx, rdx
008701FA  0F 85 A2 02 00 00               jne 0x1408704a2
00870200  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
00870205  4C 8B FB                        mov r15, rbx
00870208  74 06                           je 0x140870210
0087020A  80 7B 41 00                     cmp byte ptr [rbx + 0x41], 0
0087020E  75 09                           jne 0x140870219
00870210  41 0F B7 C5                     movzx eax, r13w
00870214  66 03 F8                        add di, ax
00870217  79 AF                           jns 0x1408701c8
00870219  4C 8B 6D 47                     mov r13, qword ptr [rbp + 0x47]
0087021D  49 8B 5F 58                     mov rbx, qword ptr [r15 + 0x58]
00870221  4D 85 E4                        test r12, r12
00870224  0F 85 A5 06 00 00               jne 0x1408708cf
0087022A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00870233  4C 8D 73 20                     lea r14, [rbx + 0x20]
00870237  B2 01                           mov dl, 1
00870239  4C 89 75 47                     mov qword ptr [rbp + 0x47], r14
0087023D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00870244  90                              nop
00870245  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00870249  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0087024D  E8 6E 19 9A FF                  call 0x140211bc0
00870252  48 83 7E 20 00                  cmp qword ptr [rsi + 0x20], 0
00870257  74 20                           je 0x140870279
00870259  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00870262  B2 01                           mov dl, 1
00870264  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0087026B  90                              nop
0087026C  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
00870270  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00870274  E8 47 19 9A FF                  call 0x140211bc0
00870279  44 8B 4E 10                     mov r9d, dword ptr [rsi + 0x10]
0087027D  48 8D 4D CB                     lea rcx, [rbp - 0x35]
00870281  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00870286  48 8D 56 20                     lea rdx, [rsi + 0x20]
0087028A  33 C0                           xor eax, eax
0087028C  48 8D 4D CF                     lea rcx, [rbp - 0x31]
00870290  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00870295  41 B0 01                        mov r8b, 1
00870298  0F B6 4D 67                     movzx ecx, byte ptr [rbp + 0x67]
0087029C  89 45 CF                        mov dword ptr [rbp - 0x31], eax
0087029F  48 89 45 D7                     mov qword ptr [rbp - 0x29], rax
008702A3  48 8B 05 16 68 75 00            mov rax, qword ptr [rip + 0x756816]
008702AA  88 4C 24 38                     mov byte ptr [rsp + 0x38], cl
008702AE  48 83 C0 4C                     add rax, 0x4c
008702B2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008702B7  49 8B CE                        mov rcx, r14
008702BA  48 8D 45 D7                     lea rax, [rbp - 0x29]
008702BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008702C3  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
008702C6  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008702CA  E8 F1 68 B3 FF                  call 0x1403a6bc0
008702CF  48 8B 7D D7                     mov rdi, qword ptr [rbp - 0x29]
008702D3  44 0F B6 F8                     movzx r15d, al
008702D7  48 85 FF                        test rdi, rdi
008702DA  74 5D                           je 0x140870339
008702DC  4C 8B 66 48                     mov r12, qword ptr [rsi + 0x48]
008702E0  44 8B 07                        mov r8d, dword ptr [rdi]
008702E3  49 8B 1C 24                     mov rbx, qword ptr [r12]
008702E7  8B 13                           mov edx, dword ptr [rbx]
008702E9  41 8D 0C 10                     lea ecx, [r8 + rdx]
008702ED  83 F9 03                        cmp ecx, 3
008702F0  0F 87 60 06 00 00               ja 0x140870956
008702F6  48 85 DB                        test rbx, rbx
008702F9  0F 84 5B 01 00 00               je 0x14087045a
008702FF  85 D2                           test edx, edx
00870301  0F 85 27 05 00 00               jne 0x14087082e
00870307  41 BE 08 00 00 00               mov r14d, 8
0087030D  47 8D 04 40                     lea r8d, [r8 + r8*2]
00870311  41 8B CE                        mov ecx, r14d
00870314  41 C1 E0 02                     shl r8d, 2
00870318  48 8D 57 08                     lea rdx, [rdi + 8]
0087031C  48 03 CB                        add rcx, rbx
0087031F  E8 1C 65 E5 FF                  call 0x1406c6840
00870324  8B 07                           mov eax, dword ptr [rdi]
00870326  01 03                           add dword ptr [rbx], eax
00870328  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
0087032C  E8 4F 5A C0 FF                  call 0x140475d80
00870331  4C 8B 75 47                     mov r14, qword ptr [rbp + 0x47]
00870335  4C 8B 65 77                     mov r12, qword ptr [rbp + 0x77]
00870339  45 84 FF                        test r15b, r15b
0087033C  74 0F                           je 0x14087034d
0087033E  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
00870341  09 46 14                        or dword ptr [rsi + 0x14], eax
00870344  0F BA E8 19                     bts eax, 0x19
00870348  F7 D0                           not eax
0087034A  21 46 10                        and dword ptr [rsi + 0x10], eax
0087034D  66 41 83 4D 30 02               or word ptr [r13 + 0x30], 2
00870353  4D 85 E4                        test r12, r12
00870356  0F 85 9A 04 00 00               jne 0x1408707f6
0087035C  0F B6 55 67                     movzx edx, byte ptr [rbp + 0x67]
00870360  84 D2                           test dl, dl
00870362  74 3A                           je 0x14087039e
00870364  48 8D 46 0A                     lea rax, [rsi + 0xa]
00870368  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0087036D  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00870372  88 54 24 38                     mov byte ptr [rsp + 0x38], dl
00870376  48 8B 0D 43 67 75 00            mov rcx, qword ptr [rip + 0x756743]
0087037D  4D 8B CE                        mov r9, r14
00870380  44 88 7C 24 30                  mov byte ptr [rsp + 0x30], r15b
00870385  48 83 C1 10                     add rcx, 0x10
00870389  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0087038E  45 33 C0                        xor r8d, r8d
00870391  49 8B D5                        mov rdx, r13
00870394  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00870399  E8 F2 E3 FF FF                  call 0x14086e790
0087039E  B8 FD FF 00 00                  mov eax, 0xfffd
008703A3  66 41 21 45 30                  and word ptr [r13 + 0x30], ax
008703A8  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
008703AC  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008703B0  E8 5B F6 9E FF                  call 0x14025fa10
008703B5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008703BE  E8 2D EC 9E FF                  call 0x14025eff0
008703C3  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
008703C7  48 85 C9                        test rcx, rcx
008703CA  74 17                           je 0x1408703e3
008703CC  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008703D0  E8 3B F6 9E FF                  call 0x14025fa10
008703D5  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008703DE  E8 0D EC 9E FF                  call 0x14025eff0
008703E3  44 0F B6 75 6F                  movzx r14d, byte ptr [rbp + 0x6f]
008703E8  48 8B 7D 57                     mov rdi, qword ptr [rbp + 0x57]
008703EC  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
008703F0  48 85 C9                        test rcx, rcx
008703F3  74 05                           je 0x1408703fa
008703F5  E8 86 59 C0 FF                  call 0x140475d80
008703FA  45 84 FF                        test r15b, r15b
008703FD  0F 84 D2 02 00 00               je 0x1408706d5
00870403  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0087040A  B2 01                           mov dl, 1
0087040C  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00870410  C7 00 00 00 00 00               mov dword ptr [rax], 0
00870416  48 8B 4D 7F                     mov rcx, qword ptr [rbp + 0x7f]
0087041A  0F B6 C2                        movzx eax, dl
0087041D  48 8B 9C 24 E8 00 00 00         mov rbx, qword ptr [rsp + 0xe8]
00870425  44 88 01                        mov byte ptr [rcx], r8b
00870428  48 81 C4 90 00 00 00            add rsp, 0x90
0087042F  41 5F                           pop r15
00870431  41 5E                           pop r14
00870433  41 5D                           pop r13
00870435  41 5C                           pop r12
00870437  5F                              pop rdi
00870438  5E                              pop rsi
00870439  5D                              pop rbp
0087043A  C3                              ret
0087043B  CC                              int3
0087043C  F7 07 00 10 00 00               test dword ptr [rdi], 0x1000
00870442  0F 84 FE FC FF FF               je 0x140870146
00870448  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0087044F  B2 01                           mov dl, 1
00870451  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00870455  44 89 38                        mov dword ptr [rax], r15d
00870458  EB BC                           jmp 0x140870416
0087045A  45 33 F6                        xor r14d, r14d
0087045D  E9 AB FE FF FF                  jmp 0x14087030d
00870462  4D 85 E4                        test r12, r12
00870465  74 33                           je 0x14087049a
00870467  4C 3B E2                        cmp r12, rdx
0087046A  0F 84 19 FC FF FF               je 0x140870089
00870470  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
00870475  48 85 C9                        test rcx, rcx
00870478  0F 85 D3 05 00 00               jne 0x140870a51
0087047E  48 83 C2 58                     add rdx, 0x58
00870482  49 8D 4C 24 58                  lea rcx, [r12 + 0x58]
00870487  E8 40 45 E9 FF                  call 0x1407049cc
0087048C  41 B8 FF FF FF FF               mov r8d, 0xffffffff
00870492  84 C0                           test al, al
00870494  0F 85 EF FB FF FF               jne 0x140870089
0087049A  41 8B C0                        mov eax, r8d
0087049D  E9 FB FB FF FF                  jmp 0x14087009d
008704A2  4D 85 E4                        test r12, r12
008704A5  74 2D                           je 0x1408704d4
008704A7  4C 3B E2                        cmp r12, rdx
008704AA  0F 84 50 FD FF FF               je 0x140870200
008704B0  49 8B 4C 24 38                  mov rcx, qword ptr [r12 + 0x38]
008704B5  48 85 C9                        test rcx, rcx
008704B8  0F 85 C4 05 00 00               jne 0x140870a82
008704BE  48 83 C2 58                     add rdx, 0x58
008704C2  49 8D 4C 24 58                  lea rcx, [r12 + 0x58]
008704C7  E8 00 45 E9 FF                  call 0x1407049cc
008704CC  84 C0                           test al, al
008704CE  0F 85 2C FD FF FF               jne 0x140870200
008704D4  41 8B C5                        mov eax, r13d
008704D7  E9 38 FD FF FF                  jmp 0x140870214
008704DC  49 81 C6 D0 00 00 00            add r14, 0xd0
008704E3  49 8B 5E 08                     mov rbx, qword ptr [r14 + 8]
008704E7  4C 3B F3                        cmp r14, rbx
008704EA  75 33                           jne 0x14087051f
008704EC  33 FF                           xor edi, edi
008704EE  66 90                           nop
008704F0  48 85 FF                        test rdi, rdi
008704F3  0F 84 CC FB FF FF               je 0x1408700c5
008704F9  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
008704FD  48 85 C9                        test rcx, rcx
00870500  74 0F                           je 0x140870511
00870502  49 3B CC                        cmp rcx, r12
00870505  75 22                           jne 0x140870529
00870507  83 7F 44 09                     cmp dword ptr [rdi + 0x44], 9
0087050B  0F 84 DC 02 00 00               je 0x1408707ed
00870511  48 85 DB                        test rbx, rbx
00870514  75 04                           jne 0x14087051a
00870516  49 8B 5E 08                     mov rbx, qword ptr [r14 + 8]
0087051A  4C 3B F3                        cmp r14, rbx
0087051D  74 CD                           je 0x1408704ec
0087051F  48 8D 7B E0                     lea rdi, [rbx - 0x20]
00870523  48 8B 5B 08                     mov rbx, qword ptr [rbx + 8]
00870527  EB C7                           jmp 0x1408704f0
00870529  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
0087052D  48 85 D2                        test rdx, rdx
00870530  0F 85 33 05 00 00               jne 0x140870a69
00870536  49 8D 54 24 58                  lea rdx, [r12 + 0x58]
0087053B  48 83 C1 58                     add rcx, 0x58
0087053F  E8 88 44 E9 FF                  call 0x1407049cc
00870544  84 C0                           test al, al
00870546  74 C9                           je 0x140870511
00870548  EB BD                           jmp 0x140870507
0087054A  F7 C2 26 00 0D 00               test edx, 0xd0026
00870550  0F 84 AC FB FF FF               je 0x140870102
00870556  F7 C2 02 00 0D 00               test edx, 0xd0002
0087055C  0F 85 D1 00 00 00               jne 0x140870633
00870562  F7 81 10 10 00 00 00 20 00 00   test dword ptr [rcx + 0x1010], 0x2000
0087056C  0F 84 C1 00 00 00               je 0x140870633
00870572  80 7F 41 00                     cmp byte ptr [rdi + 0x41], 0
00870576  0F 85 B7 00 00 00               jne 0x140870633
0087057C  48 8B D7                        mov rdx, rdi
0087057F  48 8D 4D DF                     lea rcx, [rbp - 0x21]
00870583  E8 08 7E FD FF                  call 0x140848390
00870588  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
0087058C  8B D8                           mov ebx, eax
0087058E  85 C0                           test eax, eax
00870590  0F 88 A6 00 00 00               js 0x14087063c
00870596  44 0F B7 47 42                  movzx r8d, word ptr [rdi + 0x42]
0087059B  66 41 FF C8                     dec r8w
0087059F  66 45 85 C0                     test r8w, r8w
008705A3  0F 88 93 00 00 00               js 0x14087063c
008705A9  49 0F BF C0                     movsx rax, r8w
008705AD  66 41 83 F8 02                  cmp r8w, 2
008705B2  0F 8D 8B 03 00 00               jge 0x140870943
008705B8  4C 8B 4C C5 E7                  mov r9, qword ptr [rbp + rax*8 - 0x19]
008705BD  66 44 89 45 E1                  mov word ptr [rbp - 0x1f], r8w
008705C2  41 0F B7 C0                     movzx eax, r8w
008705C6  66 85 C0                        test ax, ax
008705C9  78 6C                           js 0x140870637
008705CB  48 0F BF C8                     movsx rcx, ax
008705CF  66 83 F8 02                     cmp ax, 2
008705D3  0F 8D 60 03 00 00               jge 0x140870939
008705D9  48 8B 4C CD E7                  mov rcx, qword ptr [rbp + rcx*8 - 0x19]
008705DE  66 83 79 42 00                  cmp word ptr [rcx + 0x42], 0
008705E3  74 06                           je 0x1408705eb
008705E5  80 79 41 01                     cmp byte ptr [rcx + 0x41], 1
008705E9  74 4C                           je 0x140870637
008705EB  83 79 28 FF                     cmp dword ptr [rcx + 0x28], -1
008705EF  0F 84 E5 01 00 00               je 0x1408707da
008705F5  49 8B 41 20                     mov rax, qword ptr [r9 + 0x20]
008705F9  F7 80 A0 00 00 00 00 00 10 00   test dword ptr [rax + 0xa0], 0x100000
00870603  0F 84 D9 01 00 00               je 0x1408707e2
00870609  48 8B 47 20                     mov rax, qword ptr [rdi + 0x20]
0087060D  F7 80 10 10 00 00 00 20 00 00   test dword ptr [rax + 0x1010], 0x2000
00870617  74 1E                           je 0x140870637
00870619  80 7F 41 00                     cmp byte ptr [rdi + 0x41], 0
0087061D  0F 84 78 FF FF FF               je 0x14087059b
00870623  EB 12                           jmp 0x140870637
00870625  49 8B 5F 18                     mov rbx, qword ptr [r15 + 0x18]
00870629  48 8B 5C FB F0                  mov rbx, qword ptr [rbx + rdi*8 - 0x10]
0087062E  E9 2F FA FF FF                  jmp 0x140870062
00870633  48 8B 55 F7                     mov rdx, qword ptr [rbp - 9]
00870637  BB 22 00 00 C0                  mov ebx, 0xc0000022
0087063C  45 33 FF                        xor r15d, r15d
0087063F  E9 C8 FA FF FF                  jmp 0x14087010c
00870644  0F B6 7D 67                     movzx edi, byte ptr [rbp + 0x67]
00870648  48 8D 56 20                     lea rdx, [rsi + 0x20]
0087064C  C7 46 14 00 00 00 00            mov dword ptr [rsi + 0x14], 0
00870653  44 0F B6 C7                     movzx r8d, dil
00870657  48 8B 0D 62 94 76 00            mov rcx, qword ptr [rip + 0x769462]
0087065E  E8 5D 14 00 00                  call 0x140871ac0
00870663  84 C0                           test al, al
00870665  74 0B                           je 0x140870672
00870667  83 4E 0C 02                     or dword ptr [rsi + 0xc], 2
0087066B  81 4E 14 19 00 02 01            or dword ptr [rsi + 0x14], 0x1020019
00870672  48 8B 0D 67 94 76 00            mov rcx, qword ptr [rip + 0x769467]
00870679  48 8D 56 20                     lea rdx, [rsi + 0x20]
0087067D  44 0F B6 C7                     movzx r8d, dil
00870681  E8 3A 14 00 00                  call 0x140871ac0
00870686  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
00870689  84 C0                           test al, al
0087068B  74 0D                           je 0x14087069a
0087068D  83 4E 0C 04                     or dword ptr [rsi + 0xc], 4
00870691  81 C9 06 00 0F 01               or ecx, 0x10f0006
00870697  89 4E 14                        mov dword ptr [rsi + 0x14], ecx
0087069A  89 4E 18                        mov dword ptr [rsi + 0x18], ecx
0087069D  85 C9                           test ecx, ecx
0087069F  0F 84 71 01 00 00               je 0x140870816
008706A5  48 8B 0D 14 64 75 00            mov rcx, qword ptr [rip + 0x756414]
008706AC  49 8D 57 20                     lea rdx, [r15 + 0x20]
008706B0  4C 8B CE                        mov r9, rsi
008706B3  41 B0 01                        mov r8b, 1
008706B6  E8 55 77 0D 00                  call 0x140947e10
008706BB  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
008706BE  F7 D0                           not eax
008706C0  23 46 18                        and eax, dword ptr [rsi + 0x18]
008706C3  89 46 10                        mov dword ptr [rsi + 0x10], eax
008706C6  E9 08 FA FF FF                  jmp 0x1408700d3
008706CB  49 8B 5C FE F0                  mov rbx, qword ptr [r14 + rdi*8 - 0x10]
008706D0  E9 04 FB FF FF                  jmp 0x1408701d9
008706D5  45 84 F6                        test r14b, r14b
008706D8  0F 85 60 01 00 00               jne 0x14087083e
008706DE  49 8B 5D 08                     mov rbx, qword ptr [r13 + 8]
008706E2  44 88 75 6F                     mov byte ptr [rbp + 0x6f], r14b
008706E6  66 83 7B 42 00                  cmp word ptr [rbx + 0x42], 0
008706EB  75 62                           jne 0x14087074f
008706ED  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008706F0  A8 10                           test al, 0x10
008706F2  75 5B                           jne 0x14087074f
008706F4  8B 83 B8 00 00 00               mov eax, dword ptr [rbx + 0xb8]
008706FA  A8 40                           test al, 0x40
008706FC  75 51                           jne 0x14087074f
008706FE  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
00870702  8B 88 10 10 00 00               mov ecx, dword ptr [rax + 0x1010]
00870708  F6 C1 10                        test cl, 0x10
0087070B  74 42                           je 0x14087074f
0087070D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00870716  4C 8D 47 10                     lea r8, [rdi + 0x10]
0087071A  33 D2                           xor edx, edx
0087071C  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
00870723  E8 68 47 04 00                  call 0x1408b4e90
00870728  84 C0                           test al, al
0087072A  75 23                           jne 0x14087074f
0087072C  48 8B 53 58                     mov rdx, qword ptr [rbx + 0x58]
00870730  4C 8D 46 20                     lea r8, [rsi + 0x20]
00870734  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
00870737  4C 8D 4D 6F                     lea r9, [rbp + 0x6f]
0087073B  48 83 C2 20                     add rdx, 0x20
0087073F  E8 5C 80 13 00                  call 0x1409a87a0
00870744  89 45 77                        mov dword ptr [rbp + 0x77], eax
00870747  85 C0                           test eax, eax
00870749  0F 89 B4 02 00 00               jns 0x140870a03
0087074F  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
00870752  85 C0                           test eax, eax
00870754  0F 89 A9 FC FF FF               jns 0x140870403
0087075A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00870763  80 B8 32 02 00 00 01            cmp byte ptr [rax + 0x232], 1
0087076A  0F 85 CE 00 00 00               jne 0x14087083e
00870770  E8 6B C0 C0 FF                  call 0x14047c7e0
00870775  48 8B C8                        mov rcx, rax
00870778  48 8B F8                        mov rdi, rax
0087077B  E8 60 B7 BD FF                  call 0x14044bee0
00870780  48 8B C8                        mov rcx, rax
00870783  E8 78 E5 BE FF                  call 0x14045ed00
00870788  48 8B CF                        mov rcx, rdi
0087078B  8B D8                           mov ebx, eax
0087078D  E8 5E F1 9B FF                  call 0x14022f8f0
00870792  3B C3                           cmp eax, ebx
00870794  0F 84 A4 00 00 00               je 0x14087083e
0087079A  F7 46 10 26 00 0D 00            test dword ptr [rsi + 0x10], 0xd0026
008707A1  0F 84 97 00 00 00               je 0x14087083e
008707A7  48 8B 4D 4F                     mov rcx, qword ptr [rbp + 0x4f]
008707AB  49 8B D4                        mov rdx, r12
008707AE  E8 7D 69 05 00                  call 0x1408c7130
008707B3  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
008707B7  84 C0                           test al, al
008707B9  45 0F B6 C0                     movzx r8d, r8b
008707BD  B9 01 00 00 00                  mov ecx, 1
008707C2  44 0F 45 C1                     cmovne r8d, ecx
008707C6  48 8B 8D 87 00 00 00            mov rcx, qword ptr [rbp + 0x87]
008707CD  32 D2                           xor dl, dl
008707CF  C7 01 22 00 00 C0               mov dword ptr [rcx], 0xc0000022
008707D5  E9 3C FC FF FF                  jmp 0x140870416
008707DA  66 FF C8                        dec ax
008707DD  E9 E4 FD FF FF                  jmp 0x1408705c6
008707E2  45 33 FF                        xor r15d, r15d
008707E5  41 8B DF                        mov ebx, r15d
008707E8  E9 1F F9 FF FF                  jmp 0x14087010c
008707ED  4C 8B 7F 58                     mov r15, qword ptr [rdi + 0x58]
008707F1  E9 CF F8 FF FF                  jmp 0x1408700c5
008707F6  48 8D 46 0A                     lea rax, [rsi + 0xa]
008707FA  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008707FF  49 8D 54 24 58                  lea rdx, [r12 + 0x58]
00870804  0F B6 45 67                     movzx eax, byte ptr [rbp + 0x67]
00870808  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0087080D  88 44 24 38                     mov byte ptr [rsp + 0x38], al
00870811  E9 60 FB FF FF                  jmp 0x140870376
00870816  48 8B 85 87 00 00 00            mov rax, qword ptr [rbp + 0x87]
0087081D  32 D2                           xor dl, dl
0087081F  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00870823  C7 00 22 00 00 C0               mov dword ptr [rax], 0xc0000022
00870829  E9 E8 FB FF FF                  jmp 0x140870416
0087082E  8D 04 52                        lea eax, [rdx + rdx*2]
00870831  44 8D 34 85 08 00 00 00         lea r14d, [rax*4 + 8]
00870839  E9 CF FA FF FF                  jmp 0x14087030d
0087083E  44 8B 45 C7                     mov r8d, dword ptr [rbp - 0x39]
00870842  EB 82                           jmp 0x1408707c6
00870844  83 7E 10 00                     cmp dword ptr [rsi + 0x10], 0
00870848  0F 85 F0 F8 FF FF               jne 0x14087013e
0087084E  E9 F5 FB FF FF                  jmp 0x140870448
00870853  C7 45 CB 7C 01 00 C0            mov dword ptr [rbp - 0x35], 0xc000017c
0087085A  45 32 FF                        xor r15b, r15b
0087085D  E9 8A FB FF FF                  jmp 0x1408703ec
00870862  48 8B 8F C0 00 00 00            mov rcx, qword ptr [rdi + 0xc0]
00870869  48 85 C9                        test rcx, rcx
0087086C  0F 84 41 F9 FF FF               je 0x1408701b3
00870872  48 8B 51 10                     mov rdx, qword ptr [rcx + 0x10]
00870876  4C 0F BF C0                     movsx r8, ax
0087087A  66 83 F8 02                     cmp ax, 2
0087087E  0F 8D C3 01 00 00               jge 0x140870a47
00870884  4A 89 54 C5 E7                  mov qword ptr [rbp + r8*8 - 0x19], rdx
00870889  4C 8B 75 F7                     mov r14, qword ptr [rbp - 9]
0087088D  48 8B 49 18                     mov rcx, qword ptr [rcx + 0x18]
00870891  66 FF C8                        dec ax
00870894  48 85 C9                        test rcx, rcx
00870897  75 D9                           jne 0x140870872
00870899  E9 15 F9 FF FF                  jmp 0x1408701b3
0087089E  8B D0                           mov edx, eax
008708A0  B9 00 01 00 00                  mov ecx, 0x100
008708A5  48 C1 E2 03                     shl rdx, 3
008708A9  41 B8 43 4D 36 35               mov r8d, 0x35364d43
008708AF  E8 50 CC B5 FF                  call 0x1403cd504
008708B4  4C 8B F0                        mov r14, rax
008708B7  48 85 C0                        test rax, rax
008708BA  0F 85 D0 F8 FF FF               jne 0x140870190
008708C0  C7 45 CB 9A 00 00 C0            mov dword ptr [rbp - 0x35], 0xc000009a
008708C7  45 32 FF                        xor r15b, r15b
008708CA  E9 14 FB FF FF                  jmp 0x1408703e3
008708CF  49 81 C7 D0 00 00 00            add r15, 0xd0
008708D6  49 8B 7F 08                     mov rdi, qword ptr [r15 + 8]
008708DA  4C 3B FF                        cmp r15, rdi
008708DD  75 2F                           jne 0x14087090e
008708DF  45 33 F6                        xor r14d, r14d
008708E2  4D 85 F6                        test r14, r14
008708E5  0F 84 3F F9 FF FF               je 0x14087022a
008708EB  49 8B 4E 38                     mov rcx, qword ptr [r14 + 0x38]
008708EF  48 85 C9                        test rcx, rcx
008708F2  74 0C                           je 0x140870900
008708F4  49 3B CC                        cmp rcx, r12
008708F7  75 1F                           jne 0x140870918
008708F9  41 83 7E 44 09                  cmp dword ptr [r14 + 0x44], 9
008708FE  74 4D                           je 0x14087094d
00870900  48 85 FF                        test rdi, rdi
00870903  75 04                           jne 0x140870909
00870905  49 8B 7F 08                     mov rdi, qword ptr [r15 + 8]
00870909  4C 3B FF                        cmp r15, rdi
0087090C  74 D1                           je 0x1408708df
0087090E  4C 8D 77 E0                     lea r14, [rdi - 0x20]
00870912  48 8B 7F 08                     mov rdi, qword ptr [rdi + 8]
00870916  EB CA                           jmp 0x1408708e2
00870918  48 8B 51 38                     mov rdx, qword ptr [rcx + 0x38]
0087091C  48 85 D2                        test rdx, rdx
0087091F  0F 85 75 01 00 00               jne 0x140870a9a
00870925  49 8D 54 24 58                  lea rdx, [r12 + 0x58]
0087092A  48 83 C1 58                     add rcx, 0x58
0087092E  E8 99 40 E9 FF                  call 0x1407049cc
00870933  84 C0                           test al, al
00870935  74 C9                           je 0x140870900
00870937  EB C0                           jmp 0x1408708f9
00870939  48 8B 4C CA F0                  mov rcx, qword ptr [rdx + rcx*8 - 0x10]
0087093E  E9 9B FC FF FF                  jmp 0x1408705de
00870943  4C 8B 4C C2 F0                  mov r9, qword ptr [rdx + rax*8 - 0x10]
00870948  E9 70 FC FF FF                  jmp 0x1408705bd
0087094D  49 8B 5E 58                     mov rbx, qword ptr [r14 + 0x58]
00870951  E9 D4 F8 FF FF                  jmp 0x14087022a
00870956  41 BE 08 00 00 00               mov r14d, 8
0087095C  45 85 C0                        test r8d, r8d
0087095F  0F 84 7D 00 00 00               je 0x1408709e2
00870965  43 8D 04 40                     lea eax, [r8 + r8*2]
00870969  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
00870970  48 85 DB                        test rbx, rbx
00870973  74 72                           je 0x1408709e7
00870975  85 D2                           test edx, edx
00870977  74 72                           je 0x1408709eb
00870979  8D 04 52                        lea eax, [rdx + rdx*2]
0087097C  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
00870983  8D 14 01                        lea edx, [rcx + rax]
00870986  41 B8 53 65 50 72               mov r8d, 0x72506553
0087098C  B9 00 01 00 00                  mov ecx, 0x100
00870991  E8 5A 17 31 00                  call 0x140b820f0
00870996  48 8B D8                        mov rbx, rax
00870999  48 85 C0                        test rax, rax
0087099C  0F 84 86 F9 FF FF               je 0x140870328
008709A2  49 8B 14 24                     mov rdx, qword ptr [r12]
008709A6  48 85 D2                        test rdx, rdx
008709A9  75 45                           jne 0x1408709f0
008709AB  45 33 F6                        xor r14d, r14d
008709AE  45 8B C6                        mov r8d, r14d
008709B1  48 8B CB                        mov rcx, rbx
008709B4  E8 87 5E E5 FF                  call 0x1406c6840
008709B9  4C 8B C7                        mov r8, rdi
008709BC  48 8B CB                        mov rcx, rbx
008709BF  E8 0C 71 16 00                  call 0x1409d7ad0
008709C4  80 7E 0B 00                     cmp byte ptr [rsi + 0xb], 0
008709C8  74 0B                           je 0x1408709d5
008709CA  49 8B 0C 24                     mov rcx, qword ptr [r12]
008709CE  33 D2                           xor edx, edx
008709D0  E8 9B 1E 31 00                  call 0x140b82870
008709D5  49 89 1C 24                     mov qword ptr [r12], rbx
008709D9  C6 46 0B 01                     mov byte ptr [rsi + 0xb], 1
008709DD  E9 46 F9 FF FF                  jmp 0x140870328
008709E2  41 8B CE                        mov ecx, r14d
008709E5  EB 89                           jmp 0x140870970
008709E7  33 C0                           xor eax, eax
008709E9  EB 98                           jmp 0x140870983
008709EB  41 8B C6                        mov eax, r14d
008709EE  EB 93                           jmp 0x140870983
008709F0  8B 02                           mov eax, dword ptr [rdx]
008709F2  85 C0                           test eax, eax
008709F4  74 B8                           je 0x1408709ae
008709F6  8D 04 40                        lea eax, [rax + rax*2]
008709F9  44 8D 34 85 08 00 00 00         lea r14d, [rax*4 + 8]
00870A01  EB AB                           jmp 0x1408709ae
00870A03  80 7D 6F 00                     cmp byte ptr [rbp + 0x6f], 0
00870A07  0F 84 4D FD FF FF               je 0x14087075a
00870A0D  44 0F B6 4D 67                  movzx r9d, byte ptr [rbp + 0x67]
00870A12  48 8D 45 77                     lea rax, [rbp + 0x77]
00870A16  4C 8B C6                        mov r8, rsi
00870A19  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00870A1E  49 8B D4                        mov rdx, r12
00870A21  C7 46 10 00 00 00 02            mov dword ptr [rsi + 0x10], 0x2000000
00870A28  49 8B CD                        mov rcx, r13
00870A2B  C7 46 18 00 00 00 02            mov dword ptr [rsi + 0x18], 0x2000000
00870A32  E8 C9 EF FF FF                  call 0x14086fa00
00870A37  84 C0                           test al, al
00870A39  0F 85 C4 F9 FF FF               jne 0x140870403
00870A3F  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00870A42  E9 0B FD FF FF                  jmp 0x140870752
00870A47  4B 89 54 C6 F0                  mov qword ptr [r14 + r8*8 - 0x10], rdx
00870A4C  E9 3C FE FF FF                  jmp 0x14087088d
00870A51  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
00870A55  48 85 C0                        test rax, rax
00870A58  0F 84 20 FA FF FF               je 0x14087047e
00870A5E  48 3B C8                        cmp rcx, rax
00870A61  0F 94 C0                        sete al
00870A64  E9 29 FA FF FF                  jmp 0x140870492
00870A69  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
00870A6E  48 85 C0                        test rax, rax
00870A71  0F 84 BF FA FF FF               je 0x140870536
00870A77  48 3B D0                        cmp rdx, rax
00870A7A  0F 94 C0                        sete al
00870A7D  E9 C2 FA FF FF                  jmp 0x140870544
00870A82  48 8B 42 38                     mov rax, qword ptr [rdx + 0x38]
00870A86  48 85 C0                        test rax, rax
00870A89  0F 84 2F FA FF FF               je 0x1408704be
00870A8F  48 3B C8                        cmp rcx, rax
00870A92  0F 94 C0                        sete al
00870A95  E9 32 FA FF FF                  jmp 0x1408704cc
00870A9A  49 8B 44 24 38                  mov rax, qword ptr [r12 + 0x38]
00870A9F  48 85 C0                        test rax, rax
00870AA2  0F 84 7D FE FF FF               je 0x140870925
00870AA8  48 3B D0                        cmp rdx, rax
00870AAB  0F 94 C0                        sete al
00870AAE  E9 80 FE FF FF                  jmp 0x140870933
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpCheckOpenAccessOnKeyBody(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6, unsigned int a7, __int64 a8, __int64 a9)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int16 v_stack_m5E;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned __int8 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int8 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p8;

    v_stack_p20 = v_rbx;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (144);
    v_r14 = 0;
    v_stack_m78 = 0;
    if (sign_flag) goto loc_008700A6;
loc_00870051:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int16 *)(a2 + 2)))) >= 2) goto loc_00870625;
loc_00870062:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 66)) == 0) goto loc_0087006F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 65)) == 1) goto loc_008700A2;
loc_0087006F:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 40)) == -1) goto loc_0087049A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 240) != 0) goto loc_00870462;
loc_00870089:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 66)) == 0) goto loc_00870099;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 65)) != 0) goto loc_008700A2;
loc_00870099:
loc_0087009D:
    v_rdi = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) + ((unsigned __int16)((unsigned __int16)(v_r14 - 1))));
    if (!sign_flag) goto loc_00870051;
loc_008700A2:
loc_008700A6:
    result = (unsigned __int16)(v_r14 - 1);
    if (a1 + 4 != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + (unsigned __int16)(*(unsigned __int16 *)(a2 + 2)) * 8 + 8) + 66);
        *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(result);
    }
    if (a7 != 0) goto loc_008704DC;
loc_008700C5:
    if (a6 != 0) goto loc_00870644;
loc_008700D3:
    v_stack_m60 = v_xmm0;
    v_stack_m5E = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m50 = v_xmm0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) != 0) goto loc_0087054A;
loc_00870102:
    v_r15 = 0;
loc_0087010C:
    result = (unsigned int)(0xFFFFFFFFULL);
    if (v_stack_m48 != 0) {
        a1 = v_stack_m48;
        result = CmSiFreeMemory(a1, v_stack_m48, v_r14 - 1, a4);
    }
    if (sign_flag) goto loc_00870816;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_p18 + 96))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 24)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 24))))) goto loc_00870816;
    if (a6 != 0) goto loc_00870844;
loc_0087013E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 24))) == 0) goto loc_0087043C;
loc_00870146:
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m5E = (unsigned __int16)((unsigned int)(0xFFFFFFFFULL));
    v_stack_m50 = v_xmm0;
    result = CmpIsKeyDeletedForKeyBody(a1, a7, v_r14 - 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00870853;
    if (((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)))) < 2) goto loc_00870190;
    result = (unsigned int)(((unsigned int)((unsigned int)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))))) - (1));
    if (condition_is_not_equal) goto loc_0087089E;
loc_00870190:
    v_stack_m60 = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    v_stack_m48 = 0;
    v_stack_m5E = (unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)));
    if ((unsigned __int16)((__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66))) != 0) goto loc_00870862;
    *(unsigned __int64 *)(v_stack_m3F + (__int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) * 8 - 25) = *(unsigned __int64 *)(a1 + 8);
loc_008701B3:
    v_stack_m74 = 0;
    if (sign_flag) goto loc_0087021D;
loc_008701C8:
    if (((unsigned int)((unsigned __int16)(v_stack_m5E))) >= 2) goto loc_008706CB;
loc_008701D9:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 66)) == 0) goto loc_008701E6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 65)) == 1) goto loc_00870219;
loc_008701E6:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 40)) == -1) goto loc_008704D4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 240) != 0) goto loc_008704A2;
loc_00870200:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 66)) == 0) goto loc_00870210;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 65)) != 0) goto loc_00870219;
loc_00870210:
loc_00870214:
    v_rdi = (unsigned __int16)(((unsigned __int16)(v_stack_m5E)) + ((unsigned __int16)((unsigned __int16)((unsigned int)(0xFFFFFFFFULL)))));
    if (!sign_flag) goto loc_008701C8;
loc_00870219:
loc_0087021D:
    if (a7 != 0) goto loc_008708CF;
loc_0087022A:
    v_stack_p8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 88) + 32;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 48) + 48), 1, v_r14 - 1, a4);
    if ((*(unsigned __int64 *)(a4 + 32)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(a4 + 32);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, v_r14 - 1, a4);
    }
    v_stack_m80 = v_stack_m74;
    result = 0;
    v_stack_m88 = v_stack_m70;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m90 = a5;
    result = (*(unsigned __int64 *)(v_rip + 7694358)) + (76);
    v_stack_m98 = result;
    v_stack_mA0 = v_stack_m68;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20)));
    result = SeAccessCheck(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m3F + (unsigned __int16)(v_stack_m5E) * 8 - 25) + 88) + 32, a4 + 32, 1, (unsigned int)(*(unsigned int *)(a4 + 16)));
    if (v_stack_m68 == 0) goto loc_00870339;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68)) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)))) * 1)) > 3) goto loc_00870956;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)) == 0) goto loc_0087045A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72))))) != 0) goto loc_0087082E;
loc_0087030D:
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m68)) + (unsigned int)(*(unsigned int *)(v_stack_m68)) * 2) << (2));
    a1 = (8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)));
    result = memcpy(a1, v_stack_m68 + 8, a3, (unsigned int)(*(unsigned int *)(a4 + 16)));
loc_00870328:
    result = CmSiFreeMemory(v_stack_m68, v_stack_m68 + 8, a3, (unsigned int)(*(unsigned int *)(a4 + 16)));
loc_00870339:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        result = v_stack_m70;
        result = (unsigned int)(~(result));
    }
    if (a7 != 0) goto loc_008707F6;
    if (a5 == 0) goto loc_0087039E;
    v_stack_m80 = a4 + 10;
    v_stack_m88 = a7;
    v_stack_m90 = a5;
loc_00870376:
    v_stack_m98 = (unsigned __int8)((unsigned __int8)(result));
    a1 = (*(unsigned __int64 *)(v_rip + 7694147)) + (16);
    v_stack_mA0 = 0;
    a3 = 0;
    v_stack_mA8 = a4;
    result = SeOpenObjectAuditAlarmWithTransaction(a1, v_stack_p8, a3, v_stack_p8);
loc_0087039E:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 48) + 48), v_stack_p8, a3, v_stack_p8);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p8, a3, v_stack_p8);
    if (*(unsigned __int64 *)(a4 + 32) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 48);
        result = ExReleaseResourceLite(a1, v_stack_p8, a3, v_stack_p8);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, v_stack_p8, a3, v_stack_p8);
    }
loc_008703EC:
    if (v_stack_m48 != 0) {
        result = CmSiFreeMemory(v_stack_m48, v_stack_p8, a3, v_stack_p8);
    }
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_008706D5;
loc_00870403:
    *(unsigned int *)(a9) = 0;
loc_00870416:
    *(unsigned __int8 *)(a8) = (unsigned __int8)((unsigned int)(v_stack_m78));
    v_rsp = (v_rsp) + (144);
    return 1;
loc_0087043C:
    if (((*(unsigned int *)(v_stack_p18)) & (0x1000ULL)) == 0) goto loc_00870146;
loc_00870448:
    *(unsigned int *)(a9) = (unsigned int)((unsigned __int8)(result));
    goto loc_00870416;
loc_0087045A:
    v_r14 = 0;
    goto loc_0087030D;
loc_00870462:
    if (a7 == 0) goto loc_0087049A;
    if (a7 == 1) goto loc_00870089;
    if (*(unsigned __int64 *)(a7 + 56) != 0) goto loc_00870A51;
loc_0087047E:
    a2 = (1) + (88);
    result = CmpTransUowIsEqual(a7 + 88, a2, (unsigned int)(v_stack_m78), v_stack_p8);
loc_00870492:
    if ((unsigned __int8)(result) != 0) goto loc_00870089;
loc_0087049A:
    goto loc_0087009D;
loc_008704A2:
    if (a7 == 0) goto loc_008704D4;
    if (a7 == a2) goto loc_00870200;
    if (*(unsigned __int64 *)(a7 + 56) != 0) goto loc_00870A82;
loc_008704BE:
    a2 = (a2) + (88);
    result = CmpTransUowIsEqual(a7 + 88, a2, (unsigned int)(0xFFFFFFFFULL), v_stack_p8);
loc_008704CC:
    if ((unsigned __int8)(result) != 0) goto loc_00870200;
loc_008704D4:
    goto loc_00870214;
loc_008704DC:
    v_r14 = (v_r14) + (208);
    if (v_r14 != (*(unsigned __int64 *)(v_r14 + 8))) goto loc_0087051F;
loc_008704EC:
    v_rdi = 0;
loc_008704F0:
    if (0 == 0) goto loc_008700C5;
    if (*(unsigned __int64 *)(v_rdi + 56) == 0) goto loc_00870511;
    if ((*(unsigned __int64 *)(v_rdi + 56)) != a7) goto loc_00870529;
loc_00870507:
    if ((*(unsigned int *)(v_rdi + 68)) == 9) goto loc_008707ED;
loc_00870511:
    v_rbx = *(unsigned __int64 *)(v_r14 + 8);
    if (*(unsigned __int64 *)(v_r14 + 8) == 0) {
        v_rbx = *(unsigned __int64 *)(v_r14 + 8);
    }
    if (v_r14 == v_rbx) goto loc_008704EC;
loc_0087051F:
    goto loc_008704F0;
loc_00870529:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 56) + 56) != 0) goto loc_00870A69;
loc_00870536:
    a1 = (*(unsigned __int64 *)(v_rdi + 56)) + (88);
    result = CmpTransUowIsEqual(a1, a7 + 88, (unsigned int)(0xFFFFFFFFULL), v_stack_p8);
loc_00870544:
    if ((unsigned __int8)(result) == 0) goto loc_00870511;
    goto loc_00870507;
loc_0087054A:
    if ((((unsigned int)(a7 + 88)) & (0xD0026ULL)) == 0) goto loc_00870102;
    if ((((unsigned int)(a7 + 88)) & (0xD0002ULL)) != 0) goto loc_00870633;
    if (((*(unsigned int *)(a1 + 4112)) & (0x2000ULL)) == 0) goto loc_00870633;
    if ((*(unsigned __int8 *)(v_rbx - 32 + 65)) != 0) goto loc_00870633;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m60, v_rbx - 32, (unsigned int)(0xFFFFFFFFULL), v_stack_p8);
    if (sign_flag) goto loc_0087063C;
loc_0087059B:
    a3 = (unsigned __int16)((*(unsigned __int16 *)(v_rbx - 32 + 66)) - 1);
    if (sign_flag) goto loc_0087063C;
    if (((unsigned __int16)(a3)) >= 2) goto loc_00870943;
loc_008705BD:
    v_stack_m5E = (unsigned __int16)(a3);
loc_008705C6:
    if (sign_flag) goto loc_00870637;
    if (((unsigned __int16)((unsigned __int16)(a3))) >= 2) goto loc_00870939;
loc_008705DE:
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)((unsigned __int16)(a3))) * 8 - 25) + 66)) == 0) goto loc_008705EB;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)((unsigned __int16)(a3))) * 8 - 25) + 65)) == 1) goto loc_00870637;
loc_008705EB:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)((unsigned __int16)(a3))) * 8 - 25) + 40)) == -1) goto loc_008707DA;
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)(a3)) * 8 - 25) + 32) + 160)) & (0x100000ULL)) == 0) goto loc_008707E2;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rbx - 32 + 32) + 4112)) & (0x2000ULL)) == 0) goto loc_00870637;
    if ((*(unsigned __int8 *)(v_rbx - 32 + 65)) == 0) goto loc_0087059B;
    goto loc_00870637;
loc_00870625:
    goto loc_00870062;
loc_00870633:
loc_00870637:
loc_0087063C:
    v_r15 = 0;
    goto loc_0087010C;
loc_00870644:
    *(unsigned int *)(a4 + 20) = 0;
    result = SeSinglePrivilegeCheckEx(*(unsigned __int64 *)(v_rip + 7771234), a4 + 32, a5, *(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)(a3)) * 8 - 25));
    if ((unsigned __int8)(result) != 0) {
    }
    result = SeSinglePrivilegeCheckEx(*(unsigned __int64 *)(v_rip + 7771239), a4 + 32, a5, *(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)(a3)) * 8 - 25));
    if ((unsigned __int8)(result) != 0) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 20))) | (0x10F0006ULL));
        *(unsigned int *)(a4 + 20) = (unsigned int)(a1);
    }
    *(unsigned int *)(a4 + 24) = (unsigned int)(a1);
    if ((unsigned int)(a1) == 0) goto loc_00870816;
    result = SepAdjustAccessStateForConstraints(*(unsigned __int64 *)(v_rip + 7693332), v_r15 + 32, 1, a4);
    result = (unsigned int)(~((unsigned int)(*(unsigned int *)(a4 + 20))));
    result = (unsigned int)((result) & (*(unsigned int *)(a4 + 24)));
    *(unsigned int *)(a4 + 16) = (unsigned int)(result);
    goto loc_008700D3;
loc_008706CB:
    goto loc_008701D9;
loc_008706D5:
    if ((unsigned __int8)(v_r14) != 0) goto loc_0087083E;
    v_stack_p30 = (unsigned __int8)(v_r14);
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 66)) != 0) goto loc_0087074F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a5 + 24)))) & (16)) != 0) goto loc_0087074F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 184)))) & (64)) != 0) goto loc_0087074F;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 32) + 4112)))) & (16)) == 0) goto loc_0087074F;
    a2 = 0;
    result = CmpIsSystemEntity(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2, a5 + 16, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0087074F;
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p8 + 8) + 88)) + (32);
    result = CmpCheckAdminAccess((unsigned int)(*(unsigned int *)(a4 + 16)), a2, a4 + 32, a6);
    v_stack_p38 = (unsigned int)(result);
    if (!sign_flag) goto loc_00870A03;
loc_0087074F:
loc_00870752:
    if (!sign_flag) goto loc_00870403;
loc_0087075A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 1) goto loc_0087083E;
    result = PsGetCurrentThreadProcess((unsigned int)(*(unsigned int *)(a4 + 16)), a2, a4 + 32, a6);
    result = PsGetProcessServerSilo(result, a2, a4 + 32, a6);
    result = PsGetServerSiloServiceSessionId(result, a2, a4 + 32, a6);
    result = PsGetProcessSessionIdEx(result, a2, a4 + 32, a6);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_0087083E;
    if (((*(unsigned int *)(a4 + 16)) & (0xD0026ULL)) == 0) goto loc_0087083E;
    result = CmpCheckKeyOwnerForPca(v_stack_p10, a7, a4 + 32, a6);
    a3 = (unsigned __int8)((unsigned int)(v_stack_m78));
    if ((unsigned __int8)(result) != 0) { a3 = 1; }
loc_008707C6:
    a2 = 0;
    *(unsigned int *)(a9) = 0xC0000022ULL;
    goto loc_00870416;
loc_008707DA:
    result = (unsigned __int16)((result) - 1);
    goto loc_008705C6;
loc_008707E2:
    v_r15 = 0;
    goto loc_0087010C;
loc_008707ED:
    goto loc_008700C5;
loc_008707F6:
    v_stack_p48 = a4 + 10;
    v_stack_p40 = a7 + 88;
    v_stack_p38 = a5;
    goto loc_00870376;
loc_00870816:
    a2 = 0;
    *(unsigned int *)(a9) = 0xC0000022ULL;
    goto loc_00870416;
loc_0087082E:
    goto loc_0087030D;
loc_0087083E:
    goto loc_008707C6;
loc_00870844:
    if ((*(unsigned int *)(a4 + 16)) != 0) goto loc_0087013E;
    goto loc_00870448;
loc_00870853:
    v_stack_m74 = 0xC000017CULL;
    v_r15 = 0;
    goto loc_008703EC;
loc_00870862:
    if (*(unsigned __int64 *)(result + 192) == 0) goto loc_008701B3;
loc_00870872:
    if (((unsigned __int16)(a2 + a2 * 2)) >= 2) goto loc_00870A47;
    *(unsigned __int64 *)(v_stack_m3F + (__int16)((unsigned __int16)(a2 + a2 * 2)) * 8 - 25) = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + 16);
loc_0087088D:
    result = (unsigned __int16)((a2 + a2 * 2) - 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 192) + 24) != 0) goto loc_00870872;
    goto loc_008701B3;
loc_0087089E:
    a2 = ((unsigned int)((unsigned int)(result))) << (3);
    result = CmpAllocatePool(256, a2, (unsigned int)(0x35364D43ULL), a6);
    if (result != 0) goto loc_00870190;
    v_stack_m74 = 0xC000009AULL;
    v_r15 = 0;
    goto loc_008703E3;
loc_008708CF:
    v_r15 = (v_r15) + (208);
    if (v_r15 != (*(unsigned __int64 *)(v_r15 + 8))) goto loc_0087090E;
loc_008708DF:
    v_r14 = 0;
loc_008708E2:
    if (0 == 0) goto loc_0087022A;
    if (*(unsigned __int64 *)(v_r14 + 56) == 0) goto loc_00870900;
    if ((*(unsigned __int64 *)(v_r14 + 56)) != a7) goto loc_00870918;
loc_008708F9:
    if ((*(unsigned int *)(v_r14 + 68)) == 9) goto loc_0087094D;
loc_00870900:
    v_rdi = *(unsigned __int64 *)(v_r15 + 8);
    if (*(unsigned __int64 *)(v_r15 + 8) == 0) {
        v_rdi = *(unsigned __int64 *)(v_r15 + 8);
    }
    if (v_r15 == v_rdi) goto loc_008708DF;
loc_0087090E:
    goto loc_008708E2;
loc_00870918:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 56) + 56) != 0) goto loc_00870A9A;
loc_00870925:
    a1 = (*(unsigned __int64 *)(v_r14 + 56)) + (88);
    result = CmpTransUowIsEqual(a1, a7 + 88, (unsigned int)(0x35364D43ULL), a6);
loc_00870933:
    if ((unsigned __int8)(result) == 0) goto loc_00870900;
    goto loc_008708F9;
loc_00870939:
    goto loc_008705DE;
loc_00870943:
    goto loc_008705BD;
loc_0087094D:
    goto loc_0087022A;
loc_00870956:
    if ((unsigned int)((unsigned int)(0x35364D43ULL)) == 0) goto loc_008709E2;
loc_00870970:
    if (*(unsigned __int64 *)(v_rdi - 32 + 88) == 0) goto loc_008709E7;
    if ((unsigned int)(a7 + 88) == 0) goto loc_008709EB;
loc_00870983:
    result = ExAllocatePool2(256, (unsigned int)(0x35364D43ULL) + (unsigned int)(0x35364D43ULL) * 2 * 4 + 8 + a7 + 88 + a7 + 88 * 2 * 4 + 8 * 1, (unsigned int)(0x72506553ULL), *(unsigned __int64 *)(a7 + 88 + result * 8 - 16));
    if (result == 0) goto loc_00870328;
    if (*(unsigned __int64 *)(a7) != 0) goto loc_008709F0;
    v_r14 = 0;
loc_008709AE:
    result = memcpy(result, *(unsigned __int64 *)(a7), 0, *(unsigned __int64 *)(a7 + 88 + result * 8 - 16));
    result = SepConcatenatePrivileges(result, *(unsigned __int64 *)(a7), *(unsigned __int64 *)(v_rdi + 8), *(unsigned __int64 *)(a7 + 88 + result * 8 - 16));
    if ((*(unsigned __int8 *)(a4 + 11)) != 0) {
        a1 = *(unsigned __int64 *)(a7);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, *(unsigned __int64 *)(v_rdi + 8), *(unsigned __int64 *)(a7 + 88 + result * 8 - 16));
    }
    *(unsigned __int64 *)(a7) = result;
    *(unsigned __int8 *)(a4 + 11) = 1;
    goto loc_00870328;
loc_008709E2:
    goto loc_00870970;
loc_008709E7:
    result = 0;
    goto loc_00870983;
loc_008709EB:
    goto loc_00870983;
loc_008709F0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_008709AE;
    goto loc_008709AE;
loc_00870A03:
    if (a6 == 0) goto loc_0087075A;
    v_stack_p20 = a7;
    *(unsigned int *)(a4 + 16) = 0x2000000ULL;
    *(unsigned int *)(a4 + 24) = 0x2000000ULL;
    result = CmpCheckKeyBodyAccess(v_stack_p8, a7, a4, a5);
    if ((unsigned __int8)(result) != 0) goto loc_00870403;
    goto loc_00870752;
loc_00870A47:
    *(unsigned __int64 *)((unsigned int)(*(unsigned int *)(a2)) + (unsigned int)(*(unsigned int *)(a2)) * 2 * 4 + 8 + a4 * 8 - 16) = a7;
    goto loc_0087088D;
loc_00870A51:
    if (*(unsigned __int64 *)(a7 + 56) == 0) goto loc_0087047E;
    result = (v_stack_p8 == (*(unsigned __int64 *)(a7 + 56))) ? 1 : 0;
    goto loc_00870492;
loc_00870A69:
    if (*(unsigned __int64 *)(a7 + 56) == 0) goto loc_00870536;
    result = (a7 == (*(unsigned __int64 *)(a7 + 56))) ? 1 : 0;
    goto loc_00870544;
loc_00870A82:
    if (*(unsigned __int64 *)(a7 + 56) == 0) goto loc_008704BE;
    result = (v_stack_p8 == (*(unsigned __int64 *)(a7 + 56))) ? 1 : 0;
    goto loc_008704CC;
loc_00870A9A:
    if (*(unsigned __int64 *)(a7 + 56) == 0) goto loc_00870925;
    result = (a7 == (*(unsigned __int64 *)(a7 + 56))) ? 1 : 0;
    goto loc_00870933;
}
```

## 5. (Beta) C Style

```c
int64_t CmpCheckOpenAccessOnKeyBody(void *Arg1, void *Arg2, int64_t Arg3, void *Arg4, uint8_t Arg5, uint8_t Arg6, uint32_t Arg7, void *Arg8, void *Arg9)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg8 = (uint8_t *)Arg8;
    uint8_t *arg9 = (uint8_t *)Arg9;

    int64_t result;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint16_t v_stack_m5E;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint8_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint8_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p8;

    v_stack_p20 = local_rbx;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (144);
    local_r14 = 0;
    v_stack_m78 = 0;
    if (sign_flag) goto loc_008700A6;
loc_00870051:
    if (((uint32_t)((uint16_t)(*(uint16_t *)(arg2 + 0x2)))) >= 2) goto loc_00870625;
loc_00870062:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x42)) == 0) goto loc_0087006F;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x41)) == 1) goto loc_008700A2;
loc_0087006F:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x28)) == -1) goto loc_0087049A;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0xF0) != 0) goto loc_00870462;
loc_00870089:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x42)) == 0) goto loc_00870099;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x41)) != 0) goto loc_008700A2;
loc_00870099:
loc_0087009D:
    local_rdi = (uint16_t)(((uint16_t)(*(uint16_t *)(arg2 + 0x2))) + ((uint16_t)((uint16_t)(local_r14 - 1))));
    if (!sign_flag) goto loc_00870051;
loc_008700A2:
loc_008700A6:
    result = (uint16_t)(local_r14 - 1);
    if (Arg1 + 4 != 0) {
        result = *(uint16_t *)(*(uint64_t *)(v_stack_p10 + (uint16_t)(*(uint16_t *)(arg2 + 0x2)) * 8 + 0x8) + 0x42);
        *(uint16_t *)(arg1 + 0x4) = (uint16_t)(result);
    }
    if (Arg7 != 0) goto loc_008704DC;
loc_008700C5:
    if (Arg6 != 0) goto loc_00870644;
loc_008700D3:
    v_stack_m60 = v_xmm0;
    v_stack_m5E = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m50 = v_xmm0;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) != 0) goto loc_0087054A;
loc_00870102:
    local_r15 = 0;
loc_0087010C:
    result = (uint32_t)(0xFFFFFFFFULL);
    if (v_stack_m48 != 0) {
        Arg1 = v_stack_m48;
        result = CmSiFreeMemory(Arg1, v_stack_m48, local_r14 - 1, Arg4);
    }
    if (sign_flag) goto loc_00870816;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_p18 + 0x60))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x18)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x18))))) goto loc_00870816;
    if (Arg6 != 0) goto loc_00870844;
loc_0087013E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x18))) == 0) goto loc_0087043C;
loc_00870146:
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m5E = (uint16_t)((uint32_t)(0xFFFFFFFFULL));
    v_stack_m50 = v_xmm0;
    result = CmpIsKeyDeletedForKeyBody(Arg1, Arg7, local_r14 - 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00870853;
    if (((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)))) < 2) goto loc_00870190;
    result = (uint32_t)(((uint32_t)((uint32_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42))))) - (1));
    if (condition_is_not_equal) goto loc_0087089E;
loc_00870190:
    v_stack_m60 = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)));
    v_stack_m48 = 0;
    v_stack_m5E = (uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)));
    if ((uint16_t)((int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42))) != 0) goto loc_00870862;
    *(uint64_t *)(v_stack_m3F + (int16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)) * 8 - 0x19) = *(uint64_t *)(arg1 + 0x8);
loc_008701B3:
    v_stack_m74 = 0;
    if (sign_flag) goto loc_0087021D;
loc_008701C8:
    if (((uint32_t)((uint16_t)(v_stack_m5E))) >= 2) goto loc_008706CB;
loc_008701D9:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x42)) == 0) goto loc_008701E6;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x41)) == 1) goto loc_00870219;
loc_008701E6:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x28)) == -1) goto loc_008704D4;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0xF0) != 0) goto loc_008704A2;
loc_00870200:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x42)) == 0) goto loc_00870210;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x41)) != 0) goto loc_00870219;
loc_00870210:
loc_00870214:
    local_rdi = (uint16_t)(((uint16_t)(v_stack_m5E)) + ((uint16_t)((uint16_t)((uint32_t)(0xFFFFFFFFULL)))));
    if (!sign_flag) goto loc_008701C8;
loc_00870219:
loc_0087021D:
    if (Arg7 != 0) goto loc_008708CF;
loc_0087022A:
    v_stack_p8 = *(uint64_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x58) + 32;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg4 + 0x30) + 0x30), 1, local_r14 - 1, Arg4);
    if ((*(uint64_t *)(arg4 + 0x20)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(arg4 + 0x20);
        Arg1 = *(uint64_t *)(arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, local_r14 - 1, Arg4);
    }
    v_stack_m80 = v_stack_m74;
    result = 0;
    v_stack_m88 = v_stack_m70;
    v_stack_m70 = 0;
    v_stack_m68 = 0;
    v_stack_m90 = Arg5;
    result = (*(uint64_t *)(v_rip + 0x756816)) + (76);
    v_stack_m98 = result;
    v_stack_mA0 = v_stack_m68;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg4 + 0x14)));
    result = SeAccessCheck(*(uint64_t *)(*(uint64_t *)(v_stack_m3F + (uint16_t)(v_stack_m5E) * 8 - 0x19) + 0x58) + 32, Arg4 + 32, 1, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
    if (v_stack_m68 == 0) goto loc_00870339;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68)) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg4 + 0x48)))) * 1)) > 3) goto loc_00870956;
    if (*(uint64_t *)(*(uint64_t *)(arg4 + 0x48)) == 0) goto loc_0087045A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg4 + 0x48))))) != 0) goto loc_0087082E;
loc_0087030D:
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m68)) + (uint32_t)(*(uint32_t *)(v_stack_m68)) * 2) << (2));
    Arg1 = (8) + (*(uint64_t *)(*(uint64_t *)(arg4 + 0x48)));
    result = memcpy(Arg1, v_stack_m68 + 8, Arg3, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
loc_00870328:
    result = CmSiFreeMemory(v_stack_m68, v_stack_m68 + 8, Arg3, (uint32_t)(*(uint32_t *)(arg4 + 0x10)));
loc_00870339:
    if ((uint8_t)((uint8_t)(result)) != 0) {
        result = v_stack_m70;
        result = (uint32_t)(~(result));
    }
    if (Arg7 != 0) goto loc_008707F6;
    if (Arg5 == 0) goto loc_0087039E;
    v_stack_m80 = Arg4 + 10;
    v_stack_m88 = Arg7;
    v_stack_m90 = Arg5;
loc_00870376:
    v_stack_m98 = (uint8_t)((uint8_t)(result));
    Arg1 = (*(uint64_t *)(v_rip + 0x756743)) + (16);
    v_stack_mA0 = 0;
    Arg3 = 0;
    v_stack_mA8 = Arg4;
    result = SeOpenObjectAuditAlarmWithTransaction(Arg1, v_stack_p8, Arg3, v_stack_p8);
loc_0087039E:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(arg4 + 0x30) + 0x30), v_stack_p8, Arg3, v_stack_p8);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p8, Arg3, v_stack_p8);
    if (*(uint64_t *)(arg4 + 0x20) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg4 + 0x20) + 0x30);
        result = ExReleaseResourceLite(Arg1, v_stack_p8, Arg3, v_stack_p8);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, v_stack_p8, Arg3, v_stack_p8);
    }
loc_008703EC:
    if (v_stack_m48 != 0) {
        result = CmSiFreeMemory(v_stack_m48, v_stack_p8, Arg3, v_stack_p8);
    }
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_008706D5;
loc_00870403:
    *(uint32_t *)(arg9) = 0;
loc_00870416:
    *(uint8_t *)(arg8) = (uint8_t)((uint32_t)(v_stack_m78));
    local_rsp = (local_rsp) + (144);
    return 1;
loc_0087043C:
    if (((*(uint32_t *)(v_stack_p18)) & (0x1000ULL)) == 0) goto loc_00870146;
loc_00870448:
    *(uint32_t *)(arg9) = (uint32_t)((uint8_t)(result));
    goto loc_00870416;
loc_0087045A:
    local_r14 = 0;
    goto loc_0087030D;
loc_00870462:
    if (Arg7 == 0) goto loc_0087049A;
    if (Arg7 == 1) goto loc_00870089;
    if (*(uint64_t *)(Arg7 + 0x38) != 0) goto loc_00870A51;
loc_0087047E:
    Arg2 = (1) + (88);
    result = CmpTransUowIsEqual(Arg7 + 88, Arg2, (uint32_t)(v_stack_m78), v_stack_p8);
loc_00870492:
    if ((uint8_t)(result) != 0) goto loc_00870089;
loc_0087049A:
    goto loc_0087009D;
loc_008704A2:
    if (Arg7 == 0) goto loc_008704D4;
    if (Arg7 == Arg2) goto loc_00870200;
    if (*(uint64_t *)(Arg7 + 0x38) != 0) goto loc_00870A82;
loc_008704BE:
    Arg2 = (Arg2) + (88);
    result = CmpTransUowIsEqual(Arg7 + 88, Arg2, (uint32_t)(0xFFFFFFFFULL), v_stack_p8);
loc_008704CC:
    if ((uint8_t)(result) != 0) goto loc_00870200;
loc_008704D4:
    goto loc_00870214;
loc_008704DC:
    local_r14 = (local_r14) + (208);
    if (local_r14 != (*(uint64_t *)(local_r14 + 0x8))) goto loc_0087051F;
loc_008704EC:
    local_rdi = 0;
loc_008704F0:
    if (0 == 0) goto loc_008700C5;
    if (*(uint64_t *)(local_rdi + 0x38) == 0) goto loc_00870511;
    if ((*(uint64_t *)(local_rdi + 0x38)) != Arg7) goto loc_00870529;
loc_00870507:
    if ((*(uint32_t *)(local_rdi + 0x44)) == 9) goto loc_008707ED;
loc_00870511:
    local_rbx = *(uint64_t *)(local_r14 + 0x8);
    if (*(uint64_t *)(local_r14 + 0x8) == 0) {
        local_rbx = *(uint64_t *)(local_r14 + 0x8);
    }
    if (local_r14 == local_rbx) goto loc_008704EC;
loc_0087051F:
    goto loc_008704F0;
loc_00870529:
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x38) + 0x38) != 0) goto loc_00870A69;
loc_00870536:
    Arg1 = (*(uint64_t *)(local_rdi + 0x38)) + (88);
    result = CmpTransUowIsEqual(Arg1, Arg7 + 88, (uint32_t)(0xFFFFFFFFULL), v_stack_p8);
loc_00870544:
    if ((uint8_t)(result) == 0) goto loc_00870511;
    goto loc_00870507;
loc_0087054A:
    if ((((uint32_t)(Arg7 + 88)) & (0xD0026ULL)) == 0) goto loc_00870102;
    if ((((uint32_t)(Arg7 + 88)) & (0xD0002ULL)) != 0) goto loc_00870633;
    if (((*(uint32_t *)(arg1 + 0x1010)) & (0x2000ULL)) == 0) goto loc_00870633;
    if ((*(uint8_t *)(local_rbx - 0x20 + 0x41)) != 0) goto loc_00870633;
    result = CmpStartKcbStackForTopLayerKcb(v_stack_m60, local_rbx - 32, (uint32_t)(0xFFFFFFFFULL), v_stack_p8);
    if (sign_flag) goto loc_0087063C;
loc_0087059B:
    Arg3 = (uint16_t)((*(uint16_t *)(local_rbx - 0x20 + 0x42)) - 1);
    if (sign_flag) goto loc_0087063C;
    if (((uint16_t)(Arg3)) >= 2) goto loc_00870943;
loc_008705BD:
    v_stack_m5E = (uint16_t)(Arg3);
loc_008705C6:
    if (sign_flag) goto loc_00870637;
    if (((uint16_t)((uint16_t)(Arg3))) >= 2) goto loc_00870939;
loc_008705DE:
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)((uint16_t)(Arg3))) * 8 - 0x19) + 0x42)) == 0) goto loc_008705EB;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)((uint16_t)(Arg3))) * 8 - 0x19) + 0x41)) == 1) goto loc_00870637;
loc_008705EB:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)((uint16_t)(Arg3))) * 8 - 0x19) + 0x28)) == -1) goto loc_008707DA;
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)(Arg3)) * 8 - 0x19) + 0x20) + 0xA0)) & (0x100000ULL)) == 0) goto loc_008707E2;
    if (((*(uint32_t *)(*(uint64_t *)(local_rbx - 0x20 + 0x20) + 0x1010)) & (0x2000ULL)) == 0) goto loc_00870637;
    if ((*(uint8_t *)(local_rbx - 0x20 + 0x41)) == 0) goto loc_0087059B;
    goto loc_00870637;
loc_00870625:
    goto loc_00870062;
loc_00870633:
loc_00870637:
loc_0087063C:
    local_r15 = 0;
    goto loc_0087010C;
loc_00870644:
    *(uint32_t *)(arg4 + 0x14) = 0;
    result = SeSinglePrivilegeCheckEx(*(uint64_t *)(v_rip + 0x769462), Arg4 + 32, Arg5, *(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)(Arg3)) * 8 - 0x19));
    if ((uint8_t)(result) != 0) {
    }
    result = SeSinglePrivilegeCheckEx(*(uint64_t *)(v_rip + 0x769467), Arg4 + 32, Arg5, *(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)(Arg3)) * 8 - 0x19));
    if ((uint8_t)(result) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg4 + 0x14))) | (0x10F0006ULL));
        *(uint32_t *)(arg4 + 0x14) = (uint32_t)(Arg1);
    }
    *(uint32_t *)(arg4 + 0x18) = (uint32_t)(Arg1);
    if ((uint32_t)(Arg1) == 0) goto loc_00870816;
    result = SepAdjustAccessStateForConstraints(*(uint64_t *)(v_rip + 0x756414), local_r15 + 32, 1, Arg4);
    result = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg4 + 0x14))));
    result = (uint32_t)((result) & (*(uint32_t *)(arg4 + 0x18)));
    *(uint32_t *)(arg4 + 0x10) = (uint32_t)(result);
    goto loc_008700D3;
loc_008706CB:
    goto loc_008701D9;
loc_008706D5:
    if ((uint8_t)(local_r14) != 0) goto loc_0087083E;
    v_stack_p30 = (uint8_t)(local_r14);
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x42)) != 0) goto loc_0087074F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(Arg5 + 0x18)))) & (16)) != 0) goto loc_0087074F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0xB8)))) & (64)) != 0) goto loc_0087074F;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x20) + 0x1010)))) & (16)) == 0) goto loc_0087074F;
    Arg2 = 0;
    result = CmpIsSystemEntity(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2, Arg5 + 16, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0087074F;
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p8 + 0x8) + 0x58)) + (32);
    result = CmpCheckAdminAccess((uint32_t)(*(uint32_t *)(arg4 + 0x10)), Arg2, Arg4 + 32, Arg6);
    v_stack_p38 = (uint32_t)(result);
    if (!sign_flag) goto loc_00870A03;
loc_0087074F:
loc_00870752:
    if (!sign_flag) goto loc_00870403;
loc_0087075A:
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 1) goto loc_0087083E;
    result = PsGetCurrentThreadProcess((uint32_t)(*(uint32_t *)(arg4 + 0x10)), Arg2, Arg4 + 32, Arg6);
    result = PsGetProcessServerSilo(result, Arg2, Arg4 + 32, Arg6);
    result = PsGetServerSiloServiceSessionId(result, Arg2, Arg4 + 32, Arg6);
    result = PsGetProcessSessionIdEx(result, Arg2, Arg4 + 32, Arg6);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_0087083E;
    if (((*(uint32_t *)(arg4 + 0x10)) & (0xD0026ULL)) == 0) goto loc_0087083E;
    result = CmpCheckKeyOwnerForPca(v_stack_p10, Arg7, Arg4 + 32, Arg6);
    Arg3 = (uint8_t)((uint32_t)(v_stack_m78));
    if ((uint8_t)(result) != 0) { Arg3 = 1; }
loc_008707C6:
    Arg2 = 0;
    *(uint32_t *)(arg9) = 0xC0000022ULL;
    goto loc_00870416;
loc_008707DA:
    result = (uint16_t)((result) - 1);
    goto loc_008705C6;
loc_008707E2:
    local_r15 = 0;
    goto loc_0087010C;
loc_008707ED:
    goto loc_008700C5;
loc_008707F6:
    v_stack_p48 = Arg4 + 10;
    v_stack_p40 = Arg7 + 88;
    v_stack_p38 = Arg5;
    goto loc_00870376;
loc_00870816:
    Arg2 = 0;
    *(uint32_t *)(arg9) = 0xC0000022ULL;
    goto loc_00870416;
loc_0087082E:
    goto loc_0087030D;
loc_0087083E:
    goto loc_008707C6;
loc_00870844:
    if ((*(uint32_t *)(arg4 + 0x10)) != 0) goto loc_0087013E;
    goto loc_00870448;
loc_00870853:
    v_stack_m74 = 0xC000017CULL;
    local_r15 = 0;
    goto loc_008703EC;
loc_00870862:
    if (*(uint64_t *)(result + 0xC0) == 0) goto loc_008701B3;
loc_00870872:
    if (((uint16_t)(Arg2 + Arg2 * 2)) >= 2) goto loc_00870A47;
    *(uint64_t *)(v_stack_m3F + (int16_t)((uint16_t)(arg2 + arg2 * 2)) * 8 - 0x19) = *(uint64_t *)(*(uint64_t *)(result + 0xC0) + 0x10);
loc_0087088D:
    result = (uint16_t)((Arg2 + Arg2 * 2) - 1);
    if (*(uint64_t *)(*(uint64_t *)(result + 0xC0) + 0x18) != 0) goto loc_00870872;
    goto loc_008701B3;
loc_0087089E:
    Arg2 = ((uint32_t)((uint32_t)(result))) << (3);
    result = CmpAllocatePool(256, Arg2, (uint32_t)(0x35364D43ULL), Arg6);
    if (result != 0) goto loc_00870190;
    v_stack_m74 = 0xC000009AULL;
    local_r15 = 0;
    goto loc_008703E3;
loc_008708CF:
    local_r15 = (local_r15) + (208);
    if (local_r15 != (*(uint64_t *)(local_r15 + 0x8))) goto loc_0087090E;
loc_008708DF:
    local_r14 = 0;
loc_008708E2:
    if (0 == 0) goto loc_0087022A;
    if (*(uint64_t *)(local_r14 + 0x38) == 0) goto loc_00870900;
    if ((*(uint64_t *)(local_r14 + 0x38)) != Arg7) goto loc_00870918;
loc_008708F9:
    if ((*(uint32_t *)(local_r14 + 0x44)) == 9) goto loc_0087094D;
loc_00870900:
    local_rdi = *(uint64_t *)(local_r15 + 0x8);
    if (*(uint64_t *)(local_r15 + 0x8) == 0) {
        local_rdi = *(uint64_t *)(local_r15 + 0x8);
    }
    if (local_r15 == local_rdi) goto loc_008708DF;
loc_0087090E:
    goto loc_008708E2;
loc_00870918:
    if (*(uint64_t *)(*(uint64_t *)(local_r14 + 0x38) + 0x38) != 0) goto loc_00870A9A;
loc_00870925:
    Arg1 = (*(uint64_t *)(local_r14 + 0x38)) + (88);
    result = CmpTransUowIsEqual(Arg1, Arg7 + 88, (uint32_t)(0x35364D43ULL), Arg6);
loc_00870933:
    if ((uint8_t)(result) == 0) goto loc_00870900;
    goto loc_008708F9;
loc_00870939:
    goto loc_008705DE;
loc_00870943:
    goto loc_008705BD;
loc_0087094D:
    goto loc_0087022A;
loc_00870956:
    if ((uint32_t)((uint32_t)(0x35364D43ULL)) == 0) goto loc_008709E2;
loc_00870970:
    if (*(uint64_t *)(local_rdi - 0x20 + 0x58) == 0) goto loc_008709E7;
    if ((uint32_t)(Arg7 + 88) == 0) goto loc_008709EB;
loc_00870983:
    result = ExAllocatePool2(256, (uint32_t)(0x35364D43ULL) + (uint32_t)(0x35364D43ULL) * 2 * 4 + 8 + Arg7 + 88 + Arg7 + 88 * 2 * 4 + 8 * 1, (uint32_t)(0x72506553ULL), *(uint64_t *)(Arg7 + 0x58 + result * 8 - 0x10));
    if (result == 0) goto loc_00870328;
    if (*(uint64_t *)(Arg7) != 0) goto loc_008709F0;
    local_r14 = 0;
loc_008709AE:
    result = memcpy(result, *(uint64_t *)(Arg7), 0, *(uint64_t *)(Arg7 + 0x58 + result * 8 - 0x10));
    result = SepConcatenatePrivileges(result, *(uint64_t *)(Arg7), *(uint64_t *)(local_rdi + 0x8), *(uint64_t *)(Arg7 + 0x58 + result * 8 - 0x10));
    if ((*(uint8_t *)(arg4 + 0xB)) != 0) {
        Arg1 = *(uint64_t *)(Arg7);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, *(uint64_t *)(local_rdi + 0x8), *(uint64_t *)(Arg7 + 0x58 + result * 8 - 0x10));
    }
    *(uint64_t *)(Arg7) = result;
    *(uint8_t *)(arg4 + 0xB) = 1;
    goto loc_00870328;
loc_008709E2:
    goto loc_00870970;
loc_008709E7:
    result = 0;
    goto loc_00870983;
loc_008709EB:
    goto loc_00870983;
loc_008709F0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg2))) == 0) goto loc_008709AE;
    goto loc_008709AE;
loc_00870A03:
    if (Arg6 == 0) goto loc_0087075A;
    v_stack_p20 = Arg7;
    *(uint32_t *)(arg4 + 0x10) = 0x2000000ULL;
    *(uint32_t *)(arg4 + 0x18) = 0x2000000ULL;
    result = CmpCheckKeyBodyAccess(v_stack_p8, Arg7, Arg4, Arg5);
    if ((uint8_t)(result) != 0) goto loc_00870403;
    goto loc_00870752;
loc_00870A47:
    *(uint64_t *)((uint32_t)(*(uint32_t *)(arg2)) + (uint32_t)(*(uint32_t *)(arg2)) * 2 * 4 + 0x8 + arg4 * 8 - 0x10) = Arg7;
    goto loc_0087088D;
loc_00870A51:
    if (*(uint64_t *)(Arg7 + 0x38) == 0) goto loc_0087047E;
    result = (v_stack_p8 == (*(uint64_t *)(Arg7 + 0x38))) ? 1 : 0;
    goto loc_00870492;
loc_00870A69:
    if (*(uint64_t *)(Arg7 + 0x38) == 0) goto loc_00870536;
    result = (Arg7 == (*(uint64_t *)(Arg7 + 0x38))) ? 1 : 0;
    goto loc_00870544;
loc_00870A82:
    if (*(uint64_t *)(Arg7 + 0x38) == 0) goto loc_008704BE;
    result = (v_stack_p8 == (*(uint64_t *)(Arg7 + 0x38))) ? 1 : 0;
    goto loc_008704CC;
loc_00870A9A:
    if (*(uint64_t *)(Arg7 + 0x38) == 0) goto loc_00870925;
    result = (Arg7 == (*(uint64_t *)(Arg7 + 0x38))) ? 1 : 0;
    goto loc_00870933;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x2` | `16` | `R` |
| `Arg4` | `+ 0xA` | `64` | `R` |
| `Arg4` | `+ 0xB` | `8` | `R` |
| `Arg4` | `+ 0xB` | `8` | `W` |
| `Arg4` | `+ 0xC` | `32` | `R/W` |
| `Arg4` | `+ 0x10` | `32` | `R` |
| `Arg4` | `+ 0x10` | `32` | `R/W` |
| `Arg4` | `+ 0x10` | `32` | `W` |
| `Arg4` | `+ 0x14` | `32` | `R` |
| `Arg4` | `+ 0x14` | `32` | `R/W` |
| `Arg4` | `+ 0x14` | `32` | `W` |
| `Arg4` | `+ 0x18` | `32` | `R` |
| `Arg4` | `+ 0x18` | `32` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x30` | `64` | `R` |
| `Arg4` | `+ 0x48` | `64` | `R` |
| `Arg8` | `+ 0x0` | `8` | `W` |
| `Arg9` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00870000&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
