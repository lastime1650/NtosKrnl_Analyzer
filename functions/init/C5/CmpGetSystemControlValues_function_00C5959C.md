# CmpGetSystemControlValues

- RVA: `0x00C5959C`–`0x00C59AC4` (길이 `1,320` bytes)
- VA: `0x0000000140C5959C`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D664C`
- 디코드: `330`개 명령, `1,320/1,320` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **40**; 고유 호출 대상: **19**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x00C5961C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C59625` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x00C5963C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C59644` → [CmpInitSecurityCache](../../page/87/CmpInitSecurityCache_function_0087B870.md) (function, `0x0087B870`)
- `0x00C5964C` → [HvHiveInitialize](../../page/87/HvHiveInitialize_function_0087B8AC.md) (function, `0x0087B8AC`)
- `0x00C596B3` → [HvHiveStartMemoryBacked](../../page/87/HvHiveStartMemoryBacked_function_0087BF38.md) (function, `0x0087BF38`)
- `0x00C596CF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C596F6` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C596FD` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C59719` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C59728` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (function, `0x00A49D58`)
- `0x00C5974D` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C59762` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C59774` → [CmpFindControlSet](../../page/7F/CmpFindControlSet_function_007F1A34.md) (function, `0x007F1A34`)
- `0x00C59799` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C597AF` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C597B6` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C597D2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C597E1` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (function, `0x00A49D58`)
- `0x00C5980B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C59811` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5983C` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x00C5985B` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C59862` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5987B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C5988A` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C598A1` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C598A8` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C598DD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C598E4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C59921` → [CmpGetBootValueData](CmpGetBootValueData_function_00C5D610.md) (function, `0x00C5D610`)
- `0x00C5994E` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C59955` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C59980` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5998A` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C599AA` → [CmpConvertLangId](CmpConvertLangId_function_00C59538.md) (function, `0x00C59538`)
- `0x00C599E1` → [CmpConvertLangId](CmpConvertLangId_function_00C59538.md) (function, `0x00C59538`)
- `0x00C59A01` → [CmSelectQualifiedInstallLanguage](CmSelectQualifiedInstallLanguage_function_00C58F58.md) (function, `0x00C58F58`)
- `0x00C59A43` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00C59A9D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmInitSystem0](CmInitSystem0_function_00C58E88.md) at `0x00C58E9F`
- [CmInitSystem0](CmInitSystem0_function_00C58E88.md) at `0x00C58EC4`

### Static image references
- `0x00C595C2` → RVA `0x00E0A740` (`.data`; read)
- `0x00C595D5` → RVA `0x00C83540` (`CmControlVector`; read)
- `0x00C5962A` → RVA `0x0100D5D0` (`INITDATA`; read)
- `0x00C59659` → RVA `0x0100D608` (`INITDATA`; write)
- `0x00C596E4` → RVA `0x0100D65C` (`INITDATA`; reference)
- `0x00C5970E` → RVA `0x00C7E3B0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C59757` → RVA `0x00C7E390` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C597C7` → RVA `0x00C7E3A0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C598CB` → RVA `0x0100D65C` (`INITDATA`; read)
- `0x00C59994` → RVA `0x01008160` (`INITDATA`; read)
- `0x00C5999D` → RVA `0x01008164` (`INITDATA`; read)
- `0x00C599A3` → RVA `0x01008748` (`INITDATA`; read)
- `0x00C599B3` → RVA `0x00FD9A98` (`PAGEDATA`; write)
- `0x00C599CB` → RVA `0x01008168` (`INITDATA`; read)
- `0x00C599D4` → RVA `0x0100816C` (`INITDATA`; read)
- `0x00C599DA` → RVA `0x01008760` (`INITDATA`; read)
- `0x00C599E6` → RVA `0x00FD9A60` (`PAGEDATA`; write)
- `0x00C599F2` → RVA `0x00FD9A60` (`PAGEDATA`; read)
- `0x00C59A1F` → RVA `0x010086E8` (`INITDATA`; write)
- `0x00C59A28` → RVA `0x00FD9FEC` (`PAGEDATA`; read)
- `0x00C59A49` → RVA `0x00FD9A98` (`PAGEDATA`; read)
- `0x00C59A57` → RVA `0x00FD9A70` (`PAGEDATA`; read)
- `0x00C59A64` → RVA `0x00FD9C74` (`PAGEDATA`; write)
- `0x00C59A78` → RVA `0x00FD9A70` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **36**
  - `0x00C5961C` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C59625` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`INIT` → `.text`)
  - `0x00C5963C` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C59644` → [CmpInitSecurityCache](../../page/87/CmpInitSecurityCache_function_0087B870.md) (`INIT` → `PAGE`)
  - `0x00C5964C` → [HvHiveInitialize](../../page/87/HvHiveInitialize_function_0087B8AC.md) (`INIT` → `PAGE`)
  - `0x00C596B3` → [HvHiveStartMemoryBacked](../../page/87/HvHiveStartMemoryBacked_function_0087BF38.md) (`INIT` → `PAGE`)
  - `0x00C596CF` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C596F6` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C596FD` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C59719` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C59728` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (`INIT` → `PAGE`)
  - `0x00C5974D` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C59762` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C59774` → [CmpFindControlSet](../../page/7F/CmpFindControlSet_function_007F1A34.md) (`INIT` → `PAGE`)
  - `0x00C59799` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C597AF` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C597B6` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C597D2` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C597E1` → [CmpFindSubKeyByName](../../page/A4/CmpFindSubKeyByName_function_00A49D58.md) (`INIT` → `PAGE`)
  - `0x00C5980B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C59811` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5983C` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (`INIT` → `PAGE`)
  - `0x00C5985B` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C59862` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5987B` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C5988A` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C598A1` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C598A8` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C598DD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C598E4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5994E` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C59955` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C59980` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5998A` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C59A43` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`INIT` → `.text`)
  - `0x00C59A9D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C5959C  48 8B C4                        mov rax, rsp
00C5959F  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00C595A3  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C595A7  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00C595AB  55                              push rbp
00C595AC  41 54                           push r12
00C595AE  41 55                           push r13
00C595B0  41 56                           push r14
00C595B2  41 57                           push r15
00C595B4  48 8D A8 48 FE FF FF            lea rbp, [rax - 0x1b8]
00C595BB  48 81 EC 90 02 00 00            sub rsp, 0x290
00C595C2  48 8B 05 77 11 1B 00            mov rax, qword ptr [rip + 0x1b1177]
00C595C9  48 33 C4                        xor rax, rsp
00C595CC  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
00C595D3  33 F6                           xor esi, esi
00C595D5  48 8D 1D 64 9F 02 00            lea rbx, [rip + 0x29f64]
00C595DC  0F 57 C0                        xorps xmm0, xmm0
00C595DF  89 75 94                        mov dword ptr [rbp - 0x6c], esi
00C595E2  45 8A F8                        mov r15b, r8b
00C595E5  40 88 75 81                     mov byte ptr [rbp - 0x7f], sil
00C595E9  48 8B F9                        mov rdi, rcx
00C595EC  40 88 75 80                     mov byte ptr [rbp - 0x80], sil
00C595F0  33 C0                           xor eax, eax
00C595F2  89 75 98                        mov dword ptr [rbp - 0x68], esi
00C595F5  41 83 CE FF                     or r14d, 0xffffffff
00C595F9  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
00C595FD  41 B8 A8 01 00 00               mov r8d, 0x1a8
00C59603  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
00C59607  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00C5960B  44 89 75 88                     mov dword ptr [rbp - 0x78], r14d
00C5960F  33 D2                           xor edx, edx
00C59611  89 75 8C                        mov dword ptr [rbp - 0x74], esi
00C59614  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00C59618  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00C5961C  E8 1F D6 A6 FF                  call 0x1406c6c40
00C59621  48 8D 4D B0                     lea rcx, [rbp - 0x50]
00C59625  E8 46 28 7A FF                  call 0x1403fbe70
00C5962A  4C 8D 2D 9F 3F 3B 00            lea r13, [rip + 0x3b3f9f]
00C59631  33 D2                           xor edx, edx
00C59633  49 8B CD                        mov rcx, r13
00C59636  41 B8 D8 12 00 00               mov r8d, 0x12d8
00C5963C  E8 FF D5 A6 FF                  call 0x1406c6c40
00C59641  49 8B CD                        mov rcx, r13
00C59644  E8 27 22 C2 FF                  call 0x14087b870
00C59649  49 8B CD                        mov rcx, r13
00C5964C  E8 5B 22 C2 FF                  call 0x14087b8ac
00C59651  48 8D 45 D0                     lea rax, [rbp - 0x30]
00C59655  4C 89 6D D0                     mov qword ptr [rbp - 0x30], r13
00C59659  48 89 05 A8 3F 3B 00            mov qword ptr [rip + 0x3b3fa8], rax
00C59660  44 8D 66 01                     lea r12d, [rsi + 1]
00C59664  48 8D 45 D0                     lea rax, [rbp - 0x30]
00C59668  45 33 C9                        xor r9d, r9d
00C5966B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00C59670  8D 56 04                        lea edx, [rsi + 4]
00C59673  48 89 74 24 70                  mov qword ptr [rsp + 0x70], rsi
00C59678  48 8D 45 80                     lea rax, [rbp - 0x80]
00C5967C  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00C59681  45 8B C4                        mov r8d, r12d
00C59684  48 89 74 24 60                  mov qword ptr [rsp + 0x60], rsi
00C59689  49 8B CD                        mov rcx, r13
00C5968C  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00C59691  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
00C59696  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00C5969B  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
00C5969F  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
00C596A4  44 89 64 24 30                  mov dword ptr [rsp + 0x30], r12d
00C596A9  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00C596AE  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00C596B3  E8 80 28 C2 FF                  call 0x14087bf38
00C596B8  85 C0                           test eax, eax
00C596BA  79 19                           jns 0x140c596d5
00C596BC  48 98                           cdqe
00C596BE  8D 4E 74                        lea ecx, [rsi + 0x74]
00C596C1  4D 8B CD                        mov r9, r13
00C596C4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C596C9  45 8B C4                        mov r8d, r12d
00C596CC  41 8B D4                        mov edx, r12d
00C596CF  E8 8C 3F 8A FF                  call 0x1404fd660
00C596D4  CC                              int3
00C596D5  48 89 35 2C 3F 3B 00            mov qword ptr [rip + 0x3b3f2c], rsi
00C596DC  8B 7F 24                        mov edi, dword ptr [rdi + 0x24]
00C596DF  45 3A FC                        cmp r15b, r12b
00C596E2  75 73                           jne 0x140c59757
00C596E4  44 84 25 71 3F 3B 00            test byte ptr [rip + 0x3b3f71], r12b
00C596EB  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C596EF  8B D7                           mov edx, edi
00C596F1  49 8B CD                        mov rcx, r13
00C596F4  74 07                           je 0x140c596fd
00C596F6  E8 65 B5 BF FF                  call 0x140854c60
00C596FB  EB 05                           jmp 0x140c59702
00C596FD  E8 AE B5 BF FF                  call 0x140854cb0
00C59702  48 8B F8                        mov rdi, rax
00C59705  48 85 C0                        test rax, rax
00C59708  0F 84 71 03 00 00               je 0x140c59a7f
00C5970E  48 8D 15 9B 4C 02 00            lea rdx, [rip + 0x24c9b]
00C59715  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C59719  E8 62 10 7D FF                  call 0x14042a780
00C5971E  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C59722  48 8B D7                        mov rdx, rdi
00C59725  49 8B CD                        mov rcx, r13
00C59728  E8 2B 06 DF FF                  call 0x140a49d58
00C5972D  44 8B F0                        mov r14d, eax
00C59730  83 F8 FF                        cmp eax, -1
00C59733  0F 84 46 03 00 00               je 0x140c59a7f
00C59739  44 84 25 1C 3F 3B 00            test byte ptr [rip + 0x3b3f1c], r12b
00C59740  48 8D 55 88                     lea rdx, [rbp - 0x78]
00C59744  49 8B CD                        mov rcx, r13
00C59747  0F 84 C4 00 00 00               je 0x140c59811
00C5974D  E8 CE 34 C0 FF                  call 0x14085cc20
00C59752  E9 BF 00 00 00                  jmp 0x140c59816
00C59757  48 8D 15 32 4C 02 00            lea rdx, [rip + 0x24c32]
00C5975E  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C59762  E8 19 10 7D FF                  call 0x14042a780
00C59767  4C 8D 4D 81                     lea r9, [rbp - 0x7f]
00C5976B  8B D7                           mov edx, edi
00C5976D  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C59771  49 8B CD                        mov rcx, r13
00C59774  E8 BB 82 B9 FF                  call 0x1407f1a34
00C59779  8B D0                           mov edx, eax
00C5977B  41 3B C6                        cmp eax, r14d
00C5977E  75 1F                           jne 0x140c5979f
00C59780  41 B8 02 00 00 00               mov r8d, 2
00C59786  48 8D 45 A0                     lea rax, [rbp - 0x60]
00C5978A  4D 8B CD                        mov r9, r13
00C5978D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C59792  49 8B D4                        mov rdx, r12
00C59795  41 8D 48 72                     lea ecx, [r8 + 0x72]
00C59799  E8 C2 3E 8A FF                  call 0x1404fd660
00C5979E  CC                              int3
00C5979F  44 84 25 B6 3E 3B 00            test byte ptr [rip + 0x3b3eb6], r12b
00C597A6  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C597AA  49 8B CD                        mov rcx, r13
00C597AD  74 07                           je 0x140c597b6
00C597AF  E8 AC B4 BF FF                  call 0x140854c60
00C597B4  EB 05                           jmp 0x140c597bb
00C597B6  E8 F5 B4 BF FF                  call 0x140854cb0
00C597BB  48 8B F8                        mov rdi, rax
00C597BE  48 85 C0                        test rax, rax
00C597C1  0F 84 B8 02 00 00               je 0x140c59a7f
00C597C7  48 8D 15 D2 4B 02 00            lea rdx, [rip + 0x24bd2]
00C597CE  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C597D2  E8 A9 0F 7D FF                  call 0x14042a780
00C597D7  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C597DB  48 8B D7                        mov rdx, rdi
00C597DE  49 8B CD                        mov rcx, r13
00C597E1  E8 72 05 DF FF                  call 0x140a49d58
00C597E6  44 8B F0                        mov r14d, eax
00C597E9  83 F8 FF                        cmp eax, -1
00C597EC  0F 85 47 FF FF FF               jne 0x140c59739
00C597F2  41 B8 03 00 00 00               mov r8d, 3
00C597F8  48 8D 45 A0                     lea rax, [rbp - 0x60]
00C597FC  4C 8B CF                        mov r9, rdi
00C597FF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C59804  49 8B D4                        mov rdx, r12
00C59807  41 8D 48 71                     lea ecx, [r8 + 0x71]
00C5980B  E8 50 3E 8A FF                  call 0x1404fd660
00C59810  CC                              int3
00C59811  E8 2A C7 BF FF                  call 0x140855f40
00C59816  4C 8B 03                        mov r8, qword ptr [rbx]
00C59819  4D 85 C0                        test r8, r8
00C5981C  0F 84 72 01 00 00               je 0x140c59994
00C59822  45 3A FC                        cmp r15b, r12b
00C59825  75 0C                           jne 0x140c59833
00C59827  40 38 73 28                     cmp byte ptr [rbx + 0x28], sil
00C5982B  75 06                           jne 0x140c59833
00C5982D  48 83 C3 30                     add rbx, 0x30
00C59831  EB E3                           jmp 0x140c59816
00C59833  41 8B D6                        mov edx, r14d
00C59836  49 8B CD                        mov rcx, r13
00C59839  83 CF FF                        or edi, 0xffffffff
00C5983C  E8 7B 9E B9 FF                  call 0x1407f36bc
00C59841  3B C7                           cmp eax, edi
00C59843  0F 84 13 01 00 00               je 0x140c5995c
00C59849  44 84 25 0C 3E 3B 00            test byte ptr [rip + 0x3b3e0c], r12b
00C59850  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C59854  8B D0                           mov edx, eax
00C59856  49 8B CD                        mov rcx, r13
00C59859  74 07                           je 0x140c59862
00C5985B  E8 00 B4 BF FF                  call 0x140854c60
00C59860  EB 05                           jmp 0x140c59867
00C59862  E8 49 B4 BF FF                  call 0x140854cb0
00C59867  48 8B F0                        mov rsi, rax
00C5986A  48 85 C0                        test rax, rax
00C5986D  0F 84 0C 02 00 00               je 0x140c59a7f
00C59873  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00C59877  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C5987B  E8 00 0F 7D FF                  call 0x14042a780
00C59880  4C 8D 45 A0                     lea r8, [rbp - 0x60]
00C59884  48 8B D6                        mov rdx, rsi
00C59887  49 8B CD                        mov rcx, r13
00C5988A  E8 8D B5 BE FF                  call 0x140844e1c
00C5988F  44 84 25 C6 3D 3B 00            test byte ptr [rip + 0x3b3dc6], r12b
00C59896  48 8D 55 88                     lea rdx, [rbp - 0x78]
00C5989A  8B F0                           mov esi, eax
00C5989C  49 8B CD                        mov rcx, r13
00C5989F  74 07                           je 0x140c598a8
00C598A1  E8 7A 33 C0 FF                  call 0x14085cc20
00C598A6  EB 05                           jmp 0x140c598ad
00C598A8  E8 93 C6 BF FF                  call 0x140855f40
00C598AD  83 FE FF                        cmp esi, -1
00C598B0  0F 84 A4 00 00 00               je 0x140c5995a
00C598B6  4C 8B 63 18                     mov r12, qword ptr [rbx + 0x18]
00C598BA  4D 85 E4                        test r12, r12
00C598BD  75 08                           jne 0x140c598c7
00C598BF  41 BC 04 00 00 00               mov r12d, 4
00C598C5  EB 04                           jmp 0x140c598cb
00C598C7  45 8B 24 24                     mov r12d, dword ptr [r12]
00C598CB  F6 05 8A 3D 3B 00 01            test byte ptr [rip + 0x3b3d8a], 1
00C598D2  4C 8D 45 90                     lea r8, [rbp - 0x70]
00C598D6  8B D6                           mov edx, esi
00C598D8  49 8B CD                        mov rcx, r13
00C598DB  74 07                           je 0x140c598e4
00C598DD  E8 7E B3 BF FF                  call 0x140854c60
00C598E2  EB 05                           jmp 0x140c598e9
00C598E4  E8 C7 B3 BF FF                  call 0x140854cb0
00C598E9  48 8B F0                        mov rsi, rax
00C598EC  48 85 C0                        test rax, rax
00C598EF  0F 84 8A 01 00 00               je 0x140c59a7f
00C598F5  8B 40 04                        mov eax, dword ptr [rax + 4]
00C598F8  B9 00 00 00 80                  mov ecx, 0x80000000
00C598FD  3B C1                           cmp eax, ecx
00C598FF  0F 93 45 80                     setae byte ptr [rbp - 0x80]
00C59903  8D B8 00 00 00 80               lea edi, [rax - 0x80000000]
00C59909  0F 42 F8                        cmovb edi, eax
00C5990C  44 3B E7                        cmp r12d, edi
00C5990F  41 0F 42 FC                     cmovb edi, r12d
00C59913  85 FF                           test edi, edi
00C59915  74 13                           je 0x140c5992a
00C59917  4C 8B 43 10                     mov r8, qword ptr [rbx + 0x10]
00C5991B  44 8B CF                        mov r9d, edi
00C5991E  48 8B D6                        mov rdx, rsi
00C59921  E8 EA 3C 00 00                  call 0x140c5d610
00C59926  84 C0                           test al, al
00C59928  74 46                           je 0x140c59970
00C5992A  48 8B 4B 20                     mov rcx, qword ptr [rbx + 0x20]
00C5992E  48 85 C9                        test rcx, rcx
00C59931  74 05                           je 0x140c59938
00C59933  8B 46 0C                        mov eax, dword ptr [rsi + 0xc]
00C59936  89 01                           mov dword ptr [rcx], eax
00C59938  41 BC 01 00 00 00               mov r12d, 1
00C5993E  48 8D 55 90                     lea rdx, [rbp - 0x70]
00C59942  44 84 25 13 3D 3B 00            test byte ptr [rip + 0x3b3d13], r12b
00C59949  49 8B CD                        mov rcx, r13
00C5994C  74 07                           je 0x140c59955
00C5994E  E8 CD 32 C0 FF                  call 0x14085cc20
00C59953  EB 05                           jmp 0x140c5995a
00C59955  E8 E6 C5 BF FF                  call 0x140855f40
00C5995A  33 F6                           xor esi, esi
00C5995C  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00C59960  48 85 C0                        test rax, rax
00C59963  0F 84 C4 FE FF FF               je 0x140c5982d
00C59969  89 38                           mov dword ptr [rax], edi
00C5996B  E9 BD FE FF FF                  jmp 0x140c5982d
00C59970  F6 05 E5 3C 3B 00 01            test byte ptr [rip + 0x3b3ce5], 1
00C59977  48 8D 55 90                     lea rdx, [rbp - 0x70]
00C5997B  49 8B CD                        mov rcx, r13
00C5997E  74 0A                           je 0x140c5998a
00C59980  E8 9B 32 C0 FF                  call 0x14085cc20
00C59985  E9 F5 00 00 00                  jmp 0x140c59a7f
00C5998A  E8 B1 C5 BF FF                  call 0x140855f40
00C5998F  E9 EB 00 00 00                  jmp 0x140c59a7f
00C59994  44 39 25 C5 E7 3A 00            cmp dword ptr [rip + 0x3ae7c5], r12d
00C5999B  75 1F                           jne 0x140c599bc
00C5999D  8B 15 C1 E7 3A 00               mov edx, dword ptr [rip + 0x3ae7c1]
00C599A3  48 8D 0D 9E ED 3A 00            lea rcx, [rip + 0x3aed9e]
00C599AA  E8 89 FB FF FF                  call 0x140c59538
00C599AF  44 0F B7 D8                     movzx r11d, ax
00C599B3  44 89 1D DE 00 38 00            mov dword ptr [rip + 0x3800de], r11d
00C599BA  EB 0F                           jmp 0x140c599cb
00C599BC  45 84 FF                        test r15b, r15b
00C599BF  75 0A                           jne 0x140c599cb
00C599C1  C7 05 CD 00 38 00 09 04 00 00   mov dword ptr [rip + 0x3800cd], 0x409
00C599CB  44 39 25 96 E7 3A 00            cmp dword ptr [rip + 0x3ae796], r12d
00C599D2  75 19                           jne 0x140c599ed
00C599D4  8B 15 92 E7 3A 00               mov edx, dword ptr [rip + 0x3ae792]
00C599DA  48 8D 0D 7F ED 3A 00            lea rcx, [rip + 0x3aed7f]
00C599E1  E8 52 FB FF FF                  call 0x140c59538
00C599E6  66 89 05 73 00 38 00            mov word ptr [rip + 0x380073], ax
00C599ED  45 84 FF                        test r15b, r15b
00C599F0  75 65                           jne 0x140c59a57
00C599F2  44 0F B7 0D 66 00 38 00         movzx r9d, word ptr [rip + 0x380066]
00C599FA  4C 8D 45 98                     lea r8, [rbp - 0x68]
00C599FE  41 8B D6                        mov edx, r14d
00C59A01  E8 52 F5 FF FF                  call 0x140c58f58
00C59A06  85 C0                           test eax, eax
00C59A08  75 1E                           jne 0x140c59a28
00C59A0A  0F B7 05 4F 00 38 00            movzx eax, word ptr [rip + 0x38004f]
00C59A11  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
00C59A14  3B C1                           cmp eax, ecx
00C59A16  74 3F                           je 0x140c59a57
00C59A18  66 89 0D 41 00 38 00            mov word ptr [rip + 0x380041], cx
00C59A1F  44 89 25 C2 EC 3A 00            mov dword ptr [rip + 0x3aecc2], r12d
00C59A26  EB 2F                           jmp 0x140c59a57
00C59A28  39 35 BE 05 38 00               cmp dword ptr [rip + 0x3805be], esi
00C59A2E  75 19                           jne 0x140c59a49
00C59A30  44 8B C0                        mov r8d, eax
00C59A33  45 33 C9                        xor r9d, r9d
00C59A36  49 8B D4                        mov rdx, r12
00C59A39  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00C59A3E  B9 2A 01 00 00                  mov ecx, 0x12a
00C59A43  E8 18 3C 8A FF                  call 0x1404fd660
00C59A48  CC                              int3
00C59A49  0F B7 05 48 00 38 00            movzx eax, word ptr [rip + 0x380048]
00C59A50  66 89 05 09 00 38 00            mov word ptr [rip + 0x380009], ax
00C59A57  66 39 35 12 00 38 00            cmp word ptr [rip + 0x380012], si
00C59A5E  8B 05 34 00 38 00               mov eax, dword ptr [rip + 0x380034]
00C59A64  89 05 0A 02 38 00               mov dword ptr [rip + 0x38020a], eax
00C59A6A  74 05                           je 0x140c59a71
00C59A6C  45 3A FC                        cmp r15b, r12b
00C59A6F  75 0E                           jne 0x140c59a7f
00C59A71  0F B7 05 E8 FF 37 00            movzx eax, word ptr [rip + 0x37ffe8]
00C59A78  66 89 05 F1 FF 37 00            mov word ptr [rip + 0x37fff1], ax
00C59A7F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00C59A88  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
00C59A8C  48 89 81 E8 06 00 00            mov qword ptr [rcx + 0x6e8], rax
00C59A93  48 8B 8D 80 01 00 00            mov rcx, qword ptr [rbp + 0x180]
00C59A9A  48 33 CC                        xor rcx, rsp
00C59A9D  E8 9E 2B A5 FF                  call 0x1406ac640
00C59AA2  4C 8D 9C 24 90 02 00 00         lea r11, [rsp + 0x290]
00C59AAA  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00C59AAE  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00C59AB2  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00C59AB6  49 8B E3                        mov rsp, r11
00C59AB9  41 5F                           pop r15
00C59ABB  41 5E                           pop r14
00C59ABD  41 5D                           pop r13
00C59ABF  41 5C                           pop r12
00C59AC1  5D                              pop rbp
00C59AC2  C3                              ret
00C59AC3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpGetSystemControlValues(__int64 a1, int a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (656);
    result = (*(unsigned __int64 *)(v_rip + 1773943)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 440 + 384) = result;
    v_rsi = 0;
    *(unsigned int *)(v_rsp - 440 - 108) = 0;
    *(unsigned __int8 *)(v_rsp - 440 - 127) = 0;
    *(unsigned __int8 *)(v_rsp - 440 - 128) = 0;
    result = 0;
    *(unsigned int *)(v_rsp - 440 - 104) = 0;
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rsp - 440 - 64) = 0;
    *(unsigned int *)(v_rsp - 440 - 112) = (unsigned int)(v_r14);
    *(unsigned int *)(v_rsp - 440 - 120) = (unsigned int)(v_r14);
    a2 = 0;
    *(unsigned int *)(v_rsp - 440 - 116) = 0;
    *(unsigned __int64 *)(v_rsp - 440 - 80) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 440 - 96) = v_xmm0;
    result = memset(v_rsp - 440 - 40, a2, 424, a4);
    result = CmpInitializeThreadInfo(v_rsp - 440 - 80, a2, 424, a4);
    a2 = 0;
    result = memset(v_rip + 3882911, a2, (unsigned int)(0x12D8ULL), a4);
    result = CmpInitSecurityCache(v_rip + 3882911, a2, (unsigned int)(0x12D8ULL), a4);
    result = HvHiveInitialize(v_rip + 3882911, a2, (unsigned int)(0x12D8ULL), a4);
    *(unsigned __int64 *)(v_rsp - 440 - 48) = v_rip + 3882911;
    *(unsigned __int64 *)(v_rip + 3882920) = v_rsp - 440 - 48;
    a4 = 0;
    v_stack_m240 = v_rsp - 440 - 48;
    v_stack_m248 = 0;
    v_stack_m250 = v_rsp - 440 - 128;
    v_stack_m258 = 0;
    v_stack_m260 = 0;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = (unsigned int)(v_rsi + 1);
    v_stack_m290 = 0;
    v_stack_m298 = a1;
    result = HvHiveStartMemoryBacked(v_rip + 3882911, v_rsi + 4, (unsigned int)((unsigned int)(v_rsi + 1)), a4);
    if (sign_flag) {
        a1 = v_rsi + 116;
        a4 = v_rip + 3882911;
        v_stack_m298 = result;
        a3 = (unsigned int)(v_rsi + 1);
        a2 = (unsigned int)(v_rsi + 1);
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(v_rip + 3882796) = 0;
    if (a3 != ((unsigned __int8)(v_rsi + 1))) goto loc_00C59757;
    if (((*(unsigned __int8 *)(v_rip + 3882865)) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00C596FD;
    result = HvpGetCellFlat(v_rip + 3882911, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)))), v_rsp - 440 - 120, a4);
    goto loc_00C59702;
loc_00C596FD:
    result = HvpGetCellPaged(v_rip + 3882911, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 36)))), v_rsp - 440 - 120, a4);
loc_00C59702:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(v_rsp - 440 - 96, v_rip + 150683, v_rsp - 440 - 120, a4);
    result = CmpFindSubKeyByName(v_rip + 3882911, result, v_rsp - 440 - 96, a4);
    if (((unsigned int)(result)) == -1) goto loc_00C59A7F;
loc_00C59739:
    if (((*(unsigned __int8 *)(v_rip + 3882780)) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00C59811;
    result = HvpReleaseCellFlat(v_rip + 3882911, v_rsp - 440 - 120, v_rsp - 440 - 96, a4);
    goto loc_00C59816;
loc_00C59757:
    result = RtlInitUnicodeString(v_rsp - 440 - 96, v_rip + 150578, v_rsp - 440 - 96, a4);
    result = CmpFindControlSet(v_rip + 3882911, (unsigned int)((unsigned int)(result)), v_rsp - 440 - 96, v_rsp - 440 - 127);
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        a3 = 2;
        result = v_rsp - 440 - 96;
        a4 = v_rip + 3882911;
        v_stack_m298 = result;
        a2 = v_rsi + 1;
        a1 = a3 + 114;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_rip + 3882678)) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00C597B6;
    result = HvpGetCellFlat(v_rip + 3882911, a2, v_rsp - 440 - 120, a4);
    goto loc_00C597BB;
loc_00C597B6:
    result = HvpGetCellPaged(v_rip + 3882911, a2, v_rsp - 440 - 120, a4);
loc_00C597BB:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(v_rsp - 440 - 96, v_rip + 150482, v_rsp - 440 - 120, a4);
    result = CmpFindSubKeyByName(v_rip + 3882911, result, v_rsp - 440 - 96, a4);
    if (((unsigned int)(result)) != -1) goto loc_00C59739;
    v_stack_m298 = v_rsp - 440 - 96;
    result = KeBugCheckEx(3 + 113, v_rsi + 1, 3, result);
loc_00C59811:
    result = HvpReleaseCellPaged(3 + 113, v_rsi + 1, 3, result);
loc_00C59816:
    if (*(unsigned __int64 *)(v_rip + 171876) == 0) goto loc_00C59994;
    if (a3 != ((unsigned __int8)(v_rsi + 1))) goto loc_00C59833;
    if ((*(unsigned __int8 *)(v_rip + 171876 + 40)) != 0) goto loc_00C59833;
loc_00C5982D:
    v_rbx = (v_rip + 171876) + (48);
    goto loc_00C59816;
loc_00C59833:
    v_rdi = (unsigned int)((result) | (0xFFFFFFFFULL));
    result = CmpWalkPath(v_rip + 3882911, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), *(unsigned __int64 *)(v_rip + 171876), result);
    if (((unsigned int)(result)) == ((unsigned int)(v_rdi))) goto loc_00C5995C;
    if (((*(unsigned __int8 *)(v_rip + 3882508)) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00C59862;
    result = HvpGetCellFlat(v_rip + 3882911, (unsigned int)((unsigned int)(result)), v_rsp - 440 - 120, result);
    goto loc_00C59867;
loc_00C59862:
    result = HvpGetCellPaged(v_rip + 3882911, (unsigned int)((unsigned int)(result)), v_rsp - 440 - 120, result);
loc_00C59867:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(v_rsp - 440 - 96, *(unsigned __int64 *)(v_rbx + 8), v_rsp - 440 - 120, result);
    result = CmpFindValueByName(v_rip + 3882911, result, v_rsp - 440 - 96, result);
    if (((*(unsigned __int8 *)(v_rip + 3882438)) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00C598A8;
    result = HvpReleaseCellFlat(v_rip + 3882911, v_rsp - 440 - 120, v_rsp - 440 - 96, result);
    goto loc_00C598AD;
loc_00C598A8:
    result = HvpReleaseCellPaged(v_rip + 3882911, v_rsp - 440 - 120, v_rsp - 440 - 96, result);
loc_00C598AD:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == -1) goto loc_00C5995A;
    if (*(unsigned __int64 *)(v_rbx + 24) != 0) goto loc_00C598C7;
    goto loc_00C598CB;
loc_00C598C7:
loc_00C598CB:
    if (((*(unsigned __int8 *)(v_rip + 3882378)) & (1)) == 0) goto loc_00C598E4;
    result = HvpGetCellFlat(v_rip + 3882911, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 440 - 112, result);
    goto loc_00C598E9;
loc_00C598E4:
    result = HvpGetCellPaged(v_rip + 3882911, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 440 - 112, result);
loc_00C598E9:
    if (result == 0) goto loc_00C59A7F;
    v_rdi = (unsigned int)(*(unsigned int *)(result + 4)) - 2147483648;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) < ((unsigned int)((unsigned int)(0x80000000ULL)))) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4))); }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(4)))) < ((unsigned int)(v_rdi))) { v_rdi = (unsigned int)((unsigned int)(*(unsigned int *)(4))); }
    if ((unsigned int)(v_rdi) == 0) goto loc_00C5992A;
    result = CmpGetBootValueData((unsigned int)(0x80000000ULL), result, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
    if ((unsigned __int8)(result) == 0) goto loc_00C59970;
loc_00C5992A:
    if (*(unsigned __int64 *)(v_rbx + 32) != 0) {
        result = *(unsigned int *)(result + 12);
        *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 32)) = (unsigned int)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 3882259)) & (1)) == 0) goto loc_00C59955;
    result = HvpReleaseCellFlat(v_rip + 3882911, v_rsp - 440 - 112, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
    goto loc_00C5995A;
loc_00C59955:
    result = HvpReleaseCellPaged(v_rip + 3882911, v_rsp - 440 - 112, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
loc_00C5995A:
    v_rsi = 0;
loc_00C5995C:
    if (*(unsigned __int64 *)(v_rbx + 24) == 0) goto loc_00C5982D;
    *(unsigned int *)(*(unsigned __int64 *)(v_rbx + 24)) = (unsigned int)(v_rdi);
    goto loc_00C5982D;
loc_00C59970:
    if (((*(unsigned __int8 *)(v_rip + 3882213)) & (1)) == 0) goto loc_00C5998A;
    result = HvpReleaseCellFlat(v_rip + 3882911, v_rsp - 440 - 112, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
    goto loc_00C59A7F;
loc_00C5998A:
    result = HvpReleaseCellPaged(v_rip + 3882911, v_rsp - 440 - 112, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
    goto loc_00C59A7F;
loc_00C59994:
    if ((*(unsigned int *)(v_rip + 3860421)) != 1) goto loc_00C599BC;
    result = CmpConvertLangId(v_rip + 3861918, (unsigned int)(*(unsigned int *)(v_rip + 3860417)), *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
    *(unsigned int *)(v_rip + 3670238) = (unsigned int)((unsigned __int16)(result));
    goto loc_00C599CB;
loc_00C599BC:
    if (a3 == 0) {
        *(unsigned int *)(v_rip + 3670221) = 0x409ULL;
    }
    if ((*(unsigned int *)(v_rip + 3860374)) == 1) {
        a2 = *(unsigned int *)(v_rip + 3860370);
        a1 = v_rip + 3861887;
        result = CmpConvertLangId(a1, a2, *(unsigned __int64 *)(v_rbx + 16), (unsigned int)((unsigned int)(v_rdi)));
        *(unsigned __int16 *)(v_rip + 3670131) = (unsigned __int16)(result);
    }
    if (a3 != 0) goto loc_00C59A57;
    result = CmSelectQualifiedInstallLanguage(a1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_rsp - 440 - 104, *(unsigned __int16 *)(v_rip + 3670118));
    if ((unsigned int)(result) != 0) goto loc_00C59A28;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 3670095))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 440 - 104))))) goto loc_00C59A57;
    *(unsigned __int16 *)(v_rip + 3670081) = (unsigned __int16)((unsigned int)(*(unsigned int *)(v_rsp - 440 - 104)));
    *(unsigned int *)(v_rip + 3861698) = 1;
    goto loc_00C59A57;
loc_00C59A28:
    result = *(unsigned __int16 *)(v_rip + 3670095);
    if ((*(unsigned int *)(v_rip + 3671486)) == 0) {
        a3 = (unsigned int)(*(unsigned __int16 *)(v_rip + 3670095));
        a4 = 0;
        a2 = 1;
        v_stack_m298 = 0;
        a1 = 298;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    *(unsigned __int16 *)(v_rip + 3670025) = (unsigned __int16)(*(unsigned __int16 *)(v_rip + 3670088));
loc_00C59A57:
    *(unsigned int *)(v_rip + 3670538) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3670068)));
    if ((*(unsigned __int16 *)(v_rip + 3670034)) == 0) goto loc_00C59A71;
    result = (unsigned int)(*(unsigned int *)(v_rip + 3670068));
    if (a3 == 1) {
        result = *(unsigned __int16 *)(v_rip + 3669992);
        *(unsigned __int16 *)(v_rip + 3670001) = (unsigned __int16)(result);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1768) = *(unsigned __int64 *)(v_rsp - 440 - 80);
    a1 = (*(unsigned __int64 *)(v_rsp - 440 + 384)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpGetSystemControlValues(void *Arg1, int32_t Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (656);
    result = (*(uint64_t *)(v_rip + 0x1B1177)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1B8 + 0x180) = result;
    local_rsi = 0;
    *(uint32_t *)(local_rsp - 0x1B8 - 0x6C) = 0;
    *(uint8_t *)(local_rsp - 0x1B8 - 0x7F) = 0;
    *(uint8_t *)(local_rsp - 0x1B8 - 0x80) = 0;
    result = 0;
    *(uint32_t *)(local_rsp - 0x1B8 - 0x68) = 0;
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    *(uint64_t *)(local_rsp - 0x1B8 - 0x40) = 0;
    *(uint32_t *)(local_rsp - 0x1B8 - 0x70) = (uint32_t)(local_r14);
    *(uint32_t *)(local_rsp - 0x1B8 - 0x78) = (uint32_t)(local_r14);
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x1B8 - 0x74) = 0;
    *(uint64_t *)(local_rsp - 0x1B8 - 0x50) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1B8 - 0x60) = v_xmm0;
    result = memset(local_rsp - 440 - 40, Arg2, 424, Arg4);
    result = CmpInitializeThreadInfo(local_rsp - 440 - 80, Arg2, 424, Arg4);
    Arg2 = 0;
    result = memset(v_rip + 3882911, Arg2, (uint32_t)(0x12D8ULL), Arg4);
    result = CmpInitSecurityCache(v_rip + 3882911, Arg2, (uint32_t)(0x12D8ULL), Arg4);
    result = HvHiveInitialize(v_rip + 3882911, Arg2, (uint32_t)(0x12D8ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x1B8 - 0x30) = v_rip + 3882911;
    *(uint64_t *)(v_rip + 0x3B3FA8) = local_rsp - 440 - 48;
    Arg4 = 0;
    v_stack_m240 = local_rsp - 440 - 48;
    v_stack_m248 = 0;
    v_stack_m250 = local_rsp - 440 - 128;
    v_stack_m258 = 0;
    v_stack_m260 = 0;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 0;
    v_stack_m288 = (uint32_t)(local_rsi + 1);
    v_stack_m290 = 0;
    v_stack_m298 = Arg1;
    result = HvHiveStartMemoryBacked(v_rip + 3882911, local_rsi + 4, (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
    if (sign_flag) {
        Arg1 = local_rsi + 116;
        Arg4 = v_rip + 3882911;
        v_stack_m298 = result;
        Arg3 = (uint32_t)(local_rsi + 1);
        Arg2 = (uint32_t)(local_rsi + 1);
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(v_rip + 0x3B3F2C) = 0;
    if (Arg3 != ((uint8_t)(local_rsi + 1))) goto loc_00C59757;
    if (((*(uint8_t *)(v_rip + 0x3B3F71)) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00C596FD;
    result = HvpGetCellFlat(v_rip + 3882911, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)))), local_rsp - 440 - 120, Arg4);
    goto loc_00C59702;
loc_00C596FD:
    result = HvpGetCellPaged(v_rip + 3882911, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x24)))), local_rsp - 440 - 120, Arg4);
loc_00C59702:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(local_rsp - 440 - 96, v_rip + 150683, local_rsp - 440 - 120, Arg4);
    result = CmpFindSubKeyByName(v_rip + 3882911, result, local_rsp - 440 - 96, Arg4);
    if (((uint32_t)(result)) == -1) goto loc_00C59A7F;
loc_00C59739:
    if (((*(uint8_t *)(v_rip + 0x3B3F1C)) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00C59811;
    result = HvpReleaseCellFlat(v_rip + 3882911, local_rsp - 440 - 120, local_rsp - 440 - 96, Arg4);
    goto loc_00C59816;
loc_00C59757:
    result = RtlInitUnicodeString(local_rsp - 440 - 96, v_rip + 150578, local_rsp - 440 - 96, Arg4);
    result = CmpFindControlSet(v_rip + 3882911, (uint32_t)((uint32_t)(result)), local_rsp - 440 - 96, local_rsp - 440 - 127);
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        Arg3 = 2;
        result = local_rsp - 440 - 96;
        Arg4 = v_rip + 3882911;
        v_stack_m298 = result;
        Arg2 = local_rsi + 1;
        Arg1 = Arg3 + 114;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(v_rip + 0x3B3EB6)) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00C597B6;
    result = HvpGetCellFlat(v_rip + 3882911, Arg2, local_rsp - 440 - 120, Arg4);
    goto loc_00C597BB;
loc_00C597B6:
    result = HvpGetCellPaged(v_rip + 3882911, Arg2, local_rsp - 440 - 120, Arg4);
loc_00C597BB:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(local_rsp - 440 - 96, v_rip + 150482, local_rsp - 440 - 120, Arg4);
    result = CmpFindSubKeyByName(v_rip + 3882911, result, local_rsp - 440 - 96, Arg4);
    if (((uint32_t)(result)) != -1) goto loc_00C59739;
    v_stack_m298 = local_rsp - 440 - 96;
    result = KeBugCheckEx(3 + 113, local_rsi + 1, 3, result);
loc_00C59811:
    result = HvpReleaseCellPaged(3 + 113, local_rsi + 1, 3, result);
loc_00C59816:
    if (*(uint64_t *)(v_rip + 0x29F64) == 0) goto loc_00C59994;
    if (Arg3 != ((uint8_t)(local_rsi + 1))) goto loc_00C59833;
    if ((*(uint8_t *)(v_rip + 0x29F64 + 0x28)) != 0) goto loc_00C59833;
loc_00C5982D:
    local_rbx = (v_rip + 171876) + (48);
    goto loc_00C59816;
loc_00C59833:
    local_rdi = (uint32_t)((result) | (0xFFFFFFFFULL));
    result = CmpWalkPath(v_rip + 3882911, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), *(uint64_t *)(v_rip + 0x29F64), result);
    if (((uint32_t)(result)) == ((uint32_t)(local_rdi))) goto loc_00C5995C;
    if (((*(uint8_t *)(v_rip + 0x3B3E0C)) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00C59862;
    result = HvpGetCellFlat(v_rip + 3882911, (uint32_t)((uint32_t)(result)), local_rsp - 440 - 120, result);
    goto loc_00C59867;
loc_00C59862:
    result = HvpGetCellPaged(v_rip + 3882911, (uint32_t)((uint32_t)(result)), local_rsp - 440 - 120, result);
loc_00C59867:
    if (result == 0) goto loc_00C59A7F;
    result = RtlInitUnicodeString(local_rsp - 440 - 96, *(uint64_t *)(local_rbx + 0x8), local_rsp - 440 - 120, result);
    result = CmpFindValueByName(v_rip + 3882911, result, local_rsp - 440 - 96, result);
    if (((*(uint8_t *)(v_rip + 0x3B3DC6)) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00C598A8;
    result = HvpReleaseCellFlat(v_rip + 3882911, local_rsp - 440 - 120, local_rsp - 440 - 96, result);
    goto loc_00C598AD;
loc_00C598A8:
    result = HvpReleaseCellPaged(v_rip + 3882911, local_rsp - 440 - 120, local_rsp - 440 - 96, result);
loc_00C598AD:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == -1) goto loc_00C5995A;
    if (*(uint64_t *)(local_rbx + 0x18) != 0) goto loc_00C598C7;
    goto loc_00C598CB;
loc_00C598C7:
loc_00C598CB:
    if (((*(uint8_t *)(v_rip + 0x3B3D8A)) & (1)) == 0) goto loc_00C598E4;
    result = HvpGetCellFlat(v_rip + 3882911, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 440 - 112, result);
    goto loc_00C598E9;
loc_00C598E4:
    result = HvpGetCellPaged(v_rip + 3882911, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 440 - 112, result);
loc_00C598E9:
    if (result == 0) goto loc_00C59A7F;
    local_rdi = (uint32_t)(*(uint32_t *)(result + 0x4)) - 2147483648;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) < ((uint32_t)((uint32_t)(0x80000000ULL)))) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))); }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(4)))) < ((uint32_t)(local_rdi))) { local_rdi = (uint32_t)((uint32_t)(*(uint32_t *)(4))); }
    if ((uint32_t)(local_rdi) == 0) goto loc_00C5992A;
    result = CmpGetBootValueData((uint32_t)(0x80000000ULL), result, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
    if ((uint8_t)(result) == 0) goto loc_00C59970;
loc_00C5992A:
    if (*(uint64_t *)(local_rbx + 0x20) != 0) {
        result = *(uint32_t *)(result + 0xC);
        *(uint32_t *)(*(uint64_t *)(local_rbx + 0x20)) = (uint32_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0x3B3D13)) & (1)) == 0) goto loc_00C59955;
    result = HvpReleaseCellFlat(v_rip + 3882911, local_rsp - 440 - 112, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
    goto loc_00C5995A;
loc_00C59955:
    result = HvpReleaseCellPaged(v_rip + 3882911, local_rsp - 440 - 112, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
loc_00C5995A:
    local_rsi = 0;
loc_00C5995C:
    if (*(uint64_t *)(local_rbx + 0x18) == 0) goto loc_00C5982D;
    *(uint32_t *)(*(uint64_t *)(local_rbx + 0x18)) = (uint32_t)(local_rdi);
    goto loc_00C5982D;
loc_00C59970:
    if (((*(uint8_t *)(v_rip + 0x3B3CE5)) & (1)) == 0) goto loc_00C5998A;
    result = HvpReleaseCellFlat(v_rip + 3882911, local_rsp - 440 - 112, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
    goto loc_00C59A7F;
loc_00C5998A:
    result = HvpReleaseCellPaged(v_rip + 3882911, local_rsp - 440 - 112, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
    goto loc_00C59A7F;
loc_00C59994:
    if ((*(uint32_t *)(v_rip + 0x3AE7C5)) != 1) goto loc_00C599BC;
    result = CmpConvertLangId(v_rip + 3861918, (uint32_t)(*(uint32_t *)(v_rip + 0x3AE7C1)), *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
    *(uint32_t *)(v_rip + 0x3800DE) = (uint32_t)((uint16_t)(result));
    goto loc_00C599CB;
loc_00C599BC:
    if (Arg3 == 0) {
        *(uint32_t *)(v_rip + 0x3800CD) = 0x409ULL;
    }
    if ((*(uint32_t *)(v_rip + 0x3AE796)) == 1) {
        Arg2 = *(uint32_t *)(v_rip + 0x3AE792);
        Arg1 = v_rip + 3861887;
        result = CmpConvertLangId(Arg1, Arg2, *(uint64_t *)(local_rbx + 0x10), (uint32_t)((uint32_t)(local_rdi)));
        *(uint16_t *)(v_rip + 0x380073) = (uint16_t)(result);
    }
    if (Arg3 != 0) goto loc_00C59A57;
    result = CmSelectQualifiedInstallLanguage(Arg1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), local_rsp - 440 - 104, *(uint16_t *)(v_rip + 0x380066));
    if ((uint32_t)(result) != 0) goto loc_00C59A28;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x38004F))) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x1B8 - 0x68))))) goto loc_00C59A57;
    *(uint16_t *)(v_rip + 0x380041) = (uint16_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x1B8 - 0x68)));
    *(uint32_t *)(v_rip + 0x3AECC2) = 1;
    goto loc_00C59A57;
loc_00C59A28:
    result = *(uint16_t *)(v_rip + 0x38004F);
    if ((*(uint32_t *)(v_rip + 0x3805BE)) == 0) {
        Arg3 = (uint32_t)(*(uint16_t *)(v_rip + 0x38004F));
        Arg4 = 0;
        Arg2 = 1;
        v_stack_m298 = 0;
        Arg1 = 298;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint16_t *)(v_rip + 0x380009) = (uint16_t)(*(uint16_t *)(v_rip + 0x380048));
loc_00C59A57:
    *(uint32_t *)(v_rip + 0x38020A) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x380034)));
    if ((*(uint16_t *)(v_rip + 0x380012)) == 0) goto loc_00C59A71;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x380034));
    if (Arg3 == 1) {
        result = *(uint16_t *)(v_rip + 0x37FFE8);
        *(uint16_t *)(v_rip + 0x37FFF1) = (uint16_t)(result);
    }
    *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x6E8) = *(uint64_t *)(local_rsp - 0x1B8 - 0x50);
    Arg1 = (*(uint64_t *)(local_rsp - 0x1B8 + 0x180)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x24` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C5959C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
