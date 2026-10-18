# ViInitSystemPhase0

- RVA: `0x00C4C1B0`–`0x00C4C5F1` (길이 `1,089` bytes)
- VA: `0x0000000140C4C1B0`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008C20C`
- 디코드: `250`개 명령, `1,089/1,089` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **11**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **42**

### Outgoing calls
- `0x00C4C21A` → [KiInitializeMutant](../../text/45/KiInitializeMutant_function_00456E9C.md) (function, `0x00456E9C`)
- `0x00C4C336` → [strstr](../../text/4F/strstr_function_004FF680.md) (function, `0x004FF680`)
- `0x00C4C353` → [VfTriageSystem](VfTriageSystem_function_00C4CB34.md) (function, `0x00C4CB34`)
- `0x00C4C384` → [VfInitSetVerifyDriverTargets](VfInitSetVerifyDriverTargets_function_00C4C010.md) (function, `0x00C4C010`)
- `0x00C4C3DB` → [ViDisableVerification](../../pagevrfy/B9/ViDisableVerification_function_00B93AFC.md) (function, `0x00B93AFC`)
- `0x00C4C40D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00C4C4F4` → [ViInitPickRandomTargets](ViInitPickRandomTargets_function_00C4C064.md) (function, `0x00C4C064`)
- `0x00C4C517` → [VfSetVerifierRunningMode](../../pagevrfy/BA/VfSetVerifierRunningMode_function_00BAB1E8.md) (function, `0x00BAB1E8`)
- `0x00C4C581` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (function, `0x00932A20`)
- `0x00C4C5C1` → [VfInitSystemNoRebootNeeded](../../pagevrfy/B9/VfInitSystemNoRebootNeeded_function_00B93970.md) (function, `0x00B93970`)
- `0x00C4C5CE` → [ViDisableVerification](../../pagevrfy/B9/ViDisableVerification_function_00B93AFC.md) (function, `0x00B93AFC`)

### Direct callers
- [VerifierInitSystem](VerifierInitSystem_function_00C4BC84.md) at `0x00C4BCF8`

### Static image references
- `0x00C4C1E6` → RVA `0x00F04900` (`.data`; read)
- `0x00C4C20C` → RVA `0x00E681B0` (`.data`; write)
- `0x00C4C213` → RVA `0x00E681B8` (`.data`; write)
- `0x00C4C21F` → RVA `0x00F049E0` (`.data`; read)
- `0x00C4C22A` → RVA `0x00E0E944` (`.data`; read)
- `0x00C4C236` → RVA `0x00F049E8` (`.data`; write)
- `0x00C4C23D` → RVA `0x00F049E0` (`.data`; write)
- `0x00C4C244` → RVA `0x00F04940` (`.data`; read)
- `0x00C4C24B` → RVA `0x00F04948` (`.data`; write)
- `0x00C4C252` → RVA `0x00F04940` (`.data`; write)
- `0x00C4C259` → RVA `0x00F048C0` (`.data`; read)
- `0x00C4C260` → RVA `0x00F048C8` (`.data`; write)
- `0x00C4C267` → RVA `0x00F048C0` (`.data`; write)
- `0x00C4C270` → RVA `0x00E681A0` (`.data`; read)
- `0x00C4C284` → RVA `0x00E0E944` (`.data`; write)
- `0x00C4C28A` → RVA `0x00F04AA4` (`.data`; write)
- `0x00C4C290` → RVA `0x00E0E950` (`.data`; read)
- `0x00C4C2A1` → RVA `0x00E681A0` (`.data`; write)
- `0x00C4C2B3` → RVA `0x00FFDA30` (`PAGEVRFD`; write)
- `0x00C4C2BE` → RVA `0x00FFDA38` (`PAGEVRFD`; write)
- `0x00C4C2C9` → RVA `0x00FFDA40` (`PAGEVRFD`; write)
- `0x00C4C2D4` → RVA `0x00FFDA48` (`PAGEVRFD`; write)
- `0x00C4C2DF` → RVA `0x00FFDA50` (`PAGEVRFD`; write)
- `0x00C4C2E6` → RVA `0x00F04980` (`.data`; read)
- `0x00C4C2F7` → RVA `0x00F049D0` (`.data`; write)
- `0x00C4C305` → RVA `0x01008150` (`INITDATA`; read)
- `0x00C4C311` → RVA `0x00FFDA08` (`PAGEVRFD`; read)
- `0x00C4C329` → RVA `0x00C79180` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4C330` → RVA `0x00F04350` (`.data`; write)
- `0x00C4C344` → RVA `0x00F04350` (`.data`; read)
- `0x00C4C37D` → RVA `0x00C7CFA0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C4C39B` → RVA `0x00FFDA08` (`PAGEVRFD`; write)
- `0x00C4C3AF` → RVA `0x00FFDA2C` (`PAGEVRFD`; write)
- `0x00C4C3B5` → RVA `0x00FFDA0A` (`PAGEVRFD`; write)
- `0x00C4C412` → RVA `0x00FFDBA4` (`PAGEVRFD`; write)
- `0x00C4C418` → RVA `0x00F04A04` (`.data`; read)
- `0x00C4C427` → RVA `0x01008150` (`INITDATA`; write)
- `0x00C4C468` → RVA `0x0100B1D0` (`INITDATA`; read)
- `0x00C4C4CD` → RVA `0x00F04A04` (`.data`; write)
- `0x00C4C4D4` → RVA `0x00F04ABC` (`.data`; write)
- `0x00C4C4DB` → RVA `0x00F044F8` (`.data`; write)
- `0x00C4C577` → RVA `0x00B8B038` (`VfKernelImageName`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00C4C21A` → [KiInitializeMutant](../../text/45/KiInitializeMutant_function_00456E9C.md) (`INIT` → `.text`)
  - `0x00C4C336` → [strstr](../../text/4F/strstr_function_004FF680.md) (`INIT` → `.text`)
  - `0x00C4C3DB` → [ViDisableVerification](../../pagevrfy/B9/ViDisableVerification_function_00B93AFC.md) (`INIT` → `PAGEVRFY`)
  - `0x00C4C40D` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`INIT` → `.text`)
  - `0x00C4C517` → [VfSetVerifierRunningMode](../../pagevrfy/BA/VfSetVerifierRunningMode_function_00BAB1E8.md) (`INIT` → `PAGEVRFY`)
  - `0x00C4C581` → [RtlEqualUnicodeString](../../page/93/RtlEqualUnicodeString_function_00932A20.md) (`INIT` → `PAGE`)
  - `0x00C4C5C1` → [VfInitSystemNoRebootNeeded](../../pagevrfy/B9/VfInitSystemNoRebootNeeded_function_00B93970.md) (`INIT` → `PAGEVRFY`)
  - `0x00C4C5CE` → [ViDisableVerification](../../pagevrfy/B9/ViDisableVerification_function_00B93AFC.md) (`INIT` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C4C1B0  48 8B C4                        mov rax, rsp
00C4C1B3  48 89 58 08                     mov qword ptr [rax + 8], rbx
00C4C1B7  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00C4C1BB  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00C4C1BF  57                              push rdi
00C4C1C0  41 54                           push r12
00C4C1C2  41 55                           push r13
00C4C1C4  41 56                           push r14
00C4C1C6  41 57                           push r15
00C4C1C8  48 83 EC 30                     sub rsp, 0x30
00C4C1CC  41 BC 02 00 00 00               mov r12d, 2
00C4C1D2  0F 57 C0                        xorps xmm0, xmm0
00C4C1D5  0F 11 40 C8                     movups xmmword ptr [rax - 0x38], xmm0
00C4C1D9  48 8B 81 F0 00 00 00            mov rax, qword ptr [rcx + 0xf0]
00C4C1E0  48 8B F1                        mov rsi, rcx
00C4C1E3  45 33 C9                        xor r9d, r9d
00C4C1E6  48 8D 0D 13 87 2B 00            lea rcx, [rip + 0x2b8713]
00C4C1ED  45 8D 74 24 FF                  lea r14d, [r12 - 1]
00C4C1F2  33 D2                           xor edx, edx
00C4C1F4  45 8D 6C 24 1E                  lea r13d, [r12 + 0x1e]
00C4C1F9  45 8A C6                        mov r8b, r14b
00C4C1FC  8B B8 84 00 00 00               mov edi, dword ptr [rax + 0x84]
00C4C202  48 8B 98 18 01 00 00            mov rbx, qword ptr [rax + 0x118]
00C4C209  41 23 FC                        and edi, r12d
00C4C20C  44 88 35 9D BF 21 00            mov byte ptr [rip + 0x21bf9d], r14b
00C4C213  44 89 2D 9E BF 21 00            mov dword ptr [rip + 0x21bf9e], r13d
00C4C21A  E8 7D AC 80 FF                  call 0x140456e9c
00C4C21F  48 8D 05 BA 87 2B 00            lea rax, [rip + 0x2b87ba]
00C4C226  41 83 CF FF                     or r15d, 0xffffffff
00C4C22A  44 39 3D 13 27 1C 00            cmp dword ptr [rip + 0x1c2713], r15d
00C4C231  BA FE FF FF FF                  mov edx, 0xfffffffe
00C4C236  48 89 05 AB 87 2B 00            mov qword ptr [rip + 0x2b87ab], rax
00C4C23D  48 89 05 9C 87 2B 00            mov qword ptr [rip + 0x2b879c], rax
00C4C244  48 8D 05 F5 86 2B 00            lea rax, [rip + 0x2b86f5]
00C4C24B  48 89 05 F6 86 2B 00            mov qword ptr [rip + 0x2b86f6], rax
00C4C252  48 89 05 E7 86 2B 00            mov qword ptr [rip + 0x2b86e7], rax
00C4C259  48 8D 05 60 86 2B 00            lea rax, [rip + 0x2b8660]
00C4C260  48 89 05 61 86 2B 00            mov qword ptr [rip + 0x2b8661], rax
00C4C267  48 89 05 52 86 2B 00            mov qword ptr [rip + 0x2b8652], rax
00C4C26E  75 20                           jne 0x140c4c290
00C4C270  8B 05 2A BF 21 00               mov eax, dword ptr [rip + 0x21bf2a]
00C4C276  25 00 00 40 00                  and eax, 0x400000
00C4C27B  F7 D8                           neg eax
00C4C27D  1B C9                           sbb ecx, ecx
00C4C27F  23 CA                           and ecx, edx
00C4C281  83 C1 04                        add ecx, 4
00C4C284  89 0D BA 26 1C 00               mov dword ptr [rip + 0x1c26ba], ecx
00C4C28A  89 0D 14 88 2B 00               mov dword ptr [rip + 0x2b8814], ecx
00C4C290  8B 0D BA 26 1C 00               mov ecx, dword ptr [rip + 0x1c26ba]
00C4C296  33 ED                           xor ebp, ebp
00C4C298  41 3B CF                        cmp ecx, r15d
00C4C29B  0F 84 2C 01 00 00               je 0x140c4c3cd
00C4C2A1  89 0D F9 BE 21 00               mov dword ptr [rip + 0x21bef9], ecx
00C4C2A7  85 FF                           test edi, edi
00C4C2A9  75 3B                           jne 0x140c4c2e6
00C4C2AB  48 85 DB                        test rbx, rbx
00C4C2AE  74 36                           je 0x140c4c2e6
00C4C2B0  8B 43 38                        mov eax, dword ptr [rbx + 0x38]
00C4C2B3  48 89 05 76 17 3B 00            mov qword ptr [rip + 0x3b1776], rax
00C4C2BA  48 8B 43 40                     mov rax, qword ptr [rbx + 0x40]
00C4C2BE  48 89 05 73 17 3B 00            mov qword ptr [rip + 0x3b1773], rax
00C4C2C5  48 8B 43 48                     mov rax, qword ptr [rbx + 0x48]
00C4C2C9  48 89 05 70 17 3B 00            mov qword ptr [rip + 0x3b1770], rax
00C4C2D0  48 8B 43 50                     mov rax, qword ptr [rbx + 0x50]
00C4C2D4  48 89 05 6D 17 3B 00            mov qword ptr [rip + 0x3b176d], rax
00C4C2DB  48 8B 43 58                     mov rax, qword ptr [rbx + 0x58]
00C4C2DF  48 89 05 6A 17 3B 00            mov qword ptr [rip + 0x3b176a], rax
00C4C2E6  F7 05 90 86 2B 00 10 04 00 00   test dword ptr [rip + 0x2b8690], 0x410
00C4C2F0  48 8B 05 A9 BE 21 00            mov rax, qword ptr [rip + 0x21bea9]
00C4C2F7  48 89 05 D2 86 2B 00            mov qword ptr [rip + 0x2b86d2], rax
00C4C2FE  74 20                           je 0x140c4c320
00C4C300  41 3B CF                        cmp ecx, r15d
00C4C303  74 1B                           je 0x140c4c320
00C4C305  8B 05 45 BE 3B 00               mov eax, dword ptr [rip + 0x3bbe45]
00C4C30B  FF C0                           inc eax
00C4C30D  85 C2                           test edx, eax
00C4C30F  75 08                           jne 0x140c4c319
00C4C311  39 2D F1 16 3B 00               cmp dword ptr [rip + 0x3b16f1], ebp
00C4C317  76 07                           jbe 0x140c4c320
00C4C319  41 8B C6                        mov eax, r14d
00C4C31C  85 FF                           test edi, edi
00C4C31E  74 02                           je 0x140c4c322
00C4C320  8B C5                           mov eax, ebp
00C4C322  48 8B 8E D8 00 00 00            mov rcx, qword ptr [rsi + 0xd8]
00C4C329  48 8D 15 50 CE 02 00            lea rdx, [rip + 0x2ce50]
00C4C330  89 05 1A 80 2B 00               mov dword ptr [rip + 0x2b801a], eax
00C4C336  E8 45 33 8B FF                  call 0x1404ff680
00C4C33B  48 85 C0                        test rax, rax
00C4C33E  0F 85 87 02 00 00               jne 0x140c4c5cb
00C4C344  39 2D 06 80 2B 00               cmp dword ptr [rip + 0x2b8006], ebp
00C4C34A  0F 85 78 02 00 00               jne 0x140c4c5c8
00C4C350  48 8B CE                        mov rcx, rsi
00C4C353  E8 DC 07 00 00                  call 0x140c4cb34
00C4C358  8B 05 F2 25 1C 00               mov eax, dword ptr [rip + 0x1c25f2]
00C4C35E  41 3B C7                        cmp eax, r15d
00C4C361  74 3F                           je 0x140c4c3a2
00C4C363  39 2D 9F 16 3B 00               cmp dword ptr [rip + 0x3b169f], ebp
00C4C369  75 1E                           jne 0x140c4c389
00C4C36B  44 39 3D DE BD 3B 00            cmp dword ptr [rip + 0x3bbdde], r15d
00C4C372  75 15                           jne 0x140c4c389
00C4C374  A8 04                           test al, 4
00C4C376  75 11                           jne 0x140c4c389
00C4C378  BA 04 00 00 00                  mov edx, 4
00C4C37D  48 8D 0D 1C 0C 03 00            lea rcx, [rip + 0x30c1c]
00C4C384  E8 87 FC FF FF                  call 0x140c4c010
00C4C389  8B 05 C1 25 1C 00               mov eax, dword ptr [rip + 0x1c25c1]
00C4C38F  41 3B C7                        cmp eax, r15d
00C4C392  74 0E                           je 0x140c4c3a2
00C4C394  A9 04 00 40 00                  test eax, 0x400004
00C4C399  74 07                           je 0x140c4c3a2
00C4C39B  44 89 35 66 16 3B 00            mov dword ptr [rip + 0x3b1666], r14d
00C4C3A2  8B 05 60 16 3B 00               mov eax, dword ptr [rip + 0x3b1660]
00C4C3A8  85 C0                           test eax, eax
00C4C3AA  74 5F                           je 0x140c4c40b
00C4C3AC  C1 E8 10                        shr eax, 0x10
00C4C3AF  89 05 77 16 3B 00               mov dword ptr [rip + 0x3b1677], eax
00C4C3B5  66 89 2D 4E 16 3B 00            mov word ptr [rip + 0x3b164e], bp
00C4C3BC  83 F8 03                        cmp eax, 3
00C4C3BF  73 3B                           jae 0x140c4c3fc
00C4C3C1  C7 05 61 16 3B 00 00 01 00 00   mov dword ptr [rip + 0x3b1661], 0x100
00C4C3CB  EB 3E                           jmp 0x140c4c40b
00C4C3CD  39 2D CD BD 21 00               cmp dword ptr [rip + 0x21bdcd], ebp
00C4C3D3  0F 84 CE FE FF FF               je 0x140c4c2a7
00C4C3D9  33 C9                           xor ecx, ecx
00C4C3DB  E8 1C 77 F4 FF                  call 0x140b93afc
00C4C3E0  F7 05 96 85 2B 00 10 04 00 00   test dword ptr [rip + 0x2b8596], 0x410
00C4C3EA  0F 84 E3 01 00 00               je 0x140c4c5d3
00C4C3F0  44 89 35 59 7F 2B 00            mov dword ptr [rip + 0x2b7f59], r14d
00C4C3F7  E9 D7 01 00 00                  jmp 0x140c4c5d3
00C4C3FC  B9 00 02 00 00                  mov ecx, 0x200
00C4C401  3B C1                           cmp eax, ecx
00C4C403  76 06                           jbe 0x140c4c40b
00C4C405  89 0D 21 16 3B 00               mov dword ptr [rip + 0x3b1621], ecx
00C4C40B  33 C9                           xor ecx, ecx
00C4C40D  E8 CE 23 73 FF                  call 0x14037e7e0
00C4C412  89 05 8C 17 3B 00               mov dword ptr [rip + 0x3b178c], eax
00C4C418  8B 05 E6 85 2B 00               mov eax, dword ptr [rip + 0x2b85e6]
00C4C41E  41 3B C6                        cmp eax, r14d
00C4C421  0F 85 A1 00 00 00               jne 0x140c4c4c8
00C4C427  89 2D 23 BD 3B 00               mov dword ptr [rip + 0x3bbd23], ebp
00C4C42D  89 2D D5 15 3B 00               mov dword ptr [rip + 0x3b15d5], ebp
00C4C433  8B 05 47 85 2B 00               mov eax, dword ptr [rip + 0x2b8547]
00C4C439  41 84 C6                        test r14b, al
00C4C43C  74 0C                           je 0x140c4c44a
00C4C43E  39 2D C4 15 3B 00               cmp dword ptr [rip + 0x3b15c4], ebp
00C4C444  0F 84 5A 01 00 00               je 0x140c4c5a4
00C4C44A  39 2D B4 85 2B 00               cmp dword ptr [rip + 0x2b85b4], ebp
00C4C450  0F 85 55 01 00 00               jne 0x140c4c5ab
00C4C456  39 2D AC 15 3B 00               cmp dword ptr [rip + 0x3b15ac], ebp
00C4C45C  0F 85 49 01 00 00               jne 0x140c4c5ab
00C4C462  8B 05 E8 BC 3B 00               mov eax, dword ptr [rip + 0x3bbce8]
00C4C468  48 8D 0D 61 ED 3B 00            lea rcx, [rip + 0x3bed61]
00C4C46F  49 2B C4                        sub rax, r12
00C4C472  BE 00 30 00 00                  mov esi, 0x3000
00C4C477  48 D1 E8                        shr rax, 1
00C4C47A  49 BF 01 26 00 00 01 00 00 00   movabs r15, 0x100002601
00C4C484  48 8D 3C 41                     lea rdi, [rcx + rax*2]
00C4C488  48 3B CF                        cmp rcx, rdi
00C4C48B  0F 83 1A 01 00 00               jae 0x140c4c5ab
00C4C491  0F B7 11                        movzx edx, word ptr [rcx]
00C4C494  66 41 3B D5                     cmp dx, r13w
00C4C498  77 0A                           ja 0x140c4c4a4
00C4C49A  49 0F A3 D7                     bt r15, rdx
00C4C49E  0F 82 EF 00 00 00               jb 0x140c4c593
00C4C4A4  66 3B D6                        cmp dx, si
00C4C4A7  0F 84 E6 00 00 00               je 0x140c4c593
00C4C4AD  83 FA 2A                        cmp edx, 0x2a
00C4C4B0  0F 84 EE 00 00 00               je 0x140c4c5a4
00C4C4B6  48 8D 59 02                     lea rbx, [rcx + 2]
00C4C4BA  83 FA 22                        cmp edx, 0x22
00C4C4BD  0F 85 85 00 00 00               jne 0x140c4c548
00C4C4C3  48 8B CB                        mov rcx, rbx
00C4C4C6  EB 5F                           jmp 0x140c4c527
00C4C4C8  41 3B C4                        cmp eax, r12d
00C4C4CB  75 1A                           jne 0x140c4c4e7
00C4C4CD  44 89 35 30 85 2B 00            mov dword ptr [rip + 0x2b8530], r14d
00C4C4D4  44 89 35 E1 85 2B 00            mov dword ptr [rip + 0x2b85e1], r14d
00C4C4DB  44 89 35 16 80 2B 00            mov dword ptr [rip + 0x2b8016], r14d
00C4C4E2  E9 40 FF FF FF                  jmp 0x140c4c427
00C4C4E7  44 39 3D 62 BC 3B 00            cmp dword ptr [rip + 0x3bbc62], r15d
00C4C4EE  0F 85 39 FF FF FF               jne 0x140c4c42d
00C4C4F4  E8 6B FB FF FF                  call 0x140c4c064
00C4C4F9  85 C0                           test eax, eax
00C4C4FB  0F 84 D2 00 00 00               je 0x140c4c5d3
00C4C501  44 39 25 3C 24 1C 00            cmp dword ptr [rip + 0x1c243c], r12d
00C4C508  89 2D 42 BC 3B 00               mov dword ptr [rip + 0x3bbc42], ebp
00C4C50E  0F 8E 1F FF FF FF               jle 0x140c4c433
00C4C514  41 8B CC                        mov ecx, r12d
00C4C517  E8 CC EC F5 FF                  call 0x140bab1e8
00C4C51C  E9 12 FF FF FF                  jmp 0x140c4c433
00C4C521  66 83 3B 22                     cmp word ptr [rbx], 0x22
00C4C525  74 26                           je 0x140c4c54d
00C4C527  49 03 DC                        add rbx, r12
00C4C52A  48 3B DF                        cmp rbx, rdi
00C4C52D  72 F2                           jb 0x140c4c521
00C4C52F  EB 7A                           jmp 0x140c4c5ab
00C4C531  0F B7 13                        movzx edx, word ptr [rbx]
00C4C534  66 41 3B D5                     cmp dx, r13w
00C4C538  77 06                           ja 0x140c4c540
00C4C53A  49 0F A3 D7                     bt r15, rdx
00C4C53E  72 0D                           jb 0x140c4c54d
00C4C540  66 3B D6                        cmp dx, si
00C4C543  74 08                           je 0x140c4c54d
00C4C545  49 03 DC                        add rbx, r12
00C4C548  48 3B DF                        cmp rbx, rdi
00C4C54B  72 E4                           jb 0x140c4c531
00C4C54D  48 8B D3                        mov rdx, rbx
00C4C550  48 2B D1                        sub rdx, rcx
00C4C553  48 D1 FA                        sar rdx, 1
00C4C556  03 D2                           add edx, edx
00C4C558  74 30                           je 0x140c4c58a
00C4C55A  41 8D 04 14                     lea eax, [r12 + rdx]
00C4C55E  66 89 54 24 20                  mov word ptr [rsp + 0x20], dx
00C4C563  66 89 44 24 22                  mov word ptr [rsp + 0x22], ax
00C4C568  66 3B C2                        cmp ax, dx
00C4C56B  72 3E                           jb 0x140c4c5ab
00C4C56D  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00C4C572  48 8D 54 24 20                  lea rdx, [rsp + 0x20]
00C4C577  48 8D 0D BA EA F3 FF            lea rcx, [rip - 0xc1546]
00C4C57E  45 8A C6                        mov r8b, r14b
00C4C581  E8 9A 64 CE FF                  call 0x140932a20
00C4C586  84 C0                           test al, al
00C4C588  75 11                           jne 0x140c4c59b
00C4C58A  48 8D 4B 02                     lea rcx, [rbx + 2]
00C4C58E  E9 F5 FE FF FF                  jmp 0x140c4c488
00C4C593  49 03 CC                        add rcx, r12
00C4C596  E9 ED FE FF FF                  jmp 0x140c4c488
00C4C59B  44 89 35 1A 85 2B 00            mov dword ptr [rip + 0x2b851a], r14d
00C4C5A2  EB 07                           jmp 0x140c4c5ab
00C4C5A4  44 89 35 59 84 2B 00            mov dword ptr [rip + 0x2b8459], r14d
00C4C5AB  F7 05 CB 83 2B 00 00 20 00 00   test dword ptr [rip + 0x2b83cb], 0x2000
00C4C5B5  74 07                           je 0x140c4c5be
00C4C5B7  44 89 35 FE 84 2B 00            mov dword ptr [rip + 0x2b84fe], r14d
00C4C5BE  41 8B D6                        mov edx, r14d
00C4C5C1  E8 AA 73 F4 FF                  call 0x140b93970
00C4C5C6  EB 0B                           jmp 0x140c4c5d3
00C4C5C8  48 85 C0                        test rax, rax
00C4C5CB  0F 95 C1                        setne cl
00C4C5CE  E8 29 75 F4 FF                  call 0x140b93afc
00C4C5D3  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
00C4C5D8  48 8B 6C 24 68                  mov rbp, qword ptr [rsp + 0x68]
00C4C5DD  48 8B 74 24 70                  mov rsi, qword ptr [rsp + 0x70]
00C4C5E2  48 83 C4 30                     add rsp, 0x30
00C4C5E6  41 5F                           pop r15
00C4C5E8  41 5E                           pop r14
00C4C5EA  41 5D                           pop r13
00C4C5EC  41 5C                           pop r12
00C4C5EE  5F                              pop rdi
00C4C5EF  C3                              ret
00C4C5F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ViInitSystemPhase0(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int16 v_stack_m36;
    unsigned __int16 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 56) = v_xmm0;
    a4 = 0;
    a2 = 0;
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 240) + 132))) & (2));
    *(unsigned __int8 *)(v_rip + 2211741) = (unsigned __int8)(2 - 1);
    *(unsigned int *)(v_rip + 2211742) = (unsigned int)(2 + 30);
    result = KiInitializeMutant(v_rip + 2852627, a2, (unsigned __int8)(2 - 1), a4);
    v_r15 = (unsigned int)((v_r15) | (0xFFFFFFFFULL));
    *(unsigned __int64 *)(v_rip + 2852779) = v_rip + 2852794;
    *(unsigned __int64 *)(v_rip + 2852764) = v_rip + 2852794;
    *(unsigned __int64 *)(v_rip + 2852598) = v_rip + 2852597;
    *(unsigned __int64 *)(v_rip + 2852583) = v_rip + 2852597;
    *(unsigned __int64 *)(v_rip + 2852449) = v_rip + 2852448;
    *(unsigned __int64 *)(v_rip + 2852434) = v_rip + 2852448;
    result = v_rip + 2852448;
    if ((*(unsigned int *)(v_rip + 1845011)) == ((unsigned int)(v_r15))) {
        result = *(unsigned int *)(v_rip + 2211626);
        result = (unsigned int)((result) & (0x400000ULL));
        result = (unsigned int)(-(result));
        a1 = (unsigned int)((v_rip + 2852627) & ((unsigned int)((unsigned int)(0xFFFFFFFEULL))));
        a1 = (unsigned int)((a1) + (4));
        *(unsigned int *)(v_rip + 1844922) = (unsigned int)(a1);
        *(unsigned int *)(v_rip + 2852884) = (unsigned int)(a1);
    }
    v_rbp = 0;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844922)))) == ((unsigned int)(v_r15))) goto loc_00C4C3CD;
    *(unsigned int *)(v_rip + 2211577) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844922)));
loc_00C4C2A7:
    if ((unsigned int)(v_rdi) != 0) goto loc_00C4C2E6;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) + 56);
        *(unsigned __int64 *)(v_rip + 3872630) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) + 64);
        *(unsigned __int64 *)(v_rip + 3872627) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) + 72);
        *(unsigned __int64 *)(v_rip + 3872624) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) + 80);
        *(unsigned __int64 *)(v_rip + 3872621) = result;
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 240) + 280) + 88);
        *(unsigned __int64 *)(v_rip + 3872618) = result;
    }
    *(unsigned __int64 *)(v_rip + 2852562) = *(unsigned __int64 *)(v_rip + 2211497);
    if (((*(unsigned int *)(v_rip + 2852496)) & (0x410ULL)) == 0) goto loc_00C4C320;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844922)))) == ((unsigned int)(v_r15))) goto loc_00C4C320;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3915333))) + 1);
    if ((((unsigned int)((unsigned int)(0xFFFFFFFEULL))) & ((unsigned int)(result))) != 0) goto loc_00C4C319;
    if ((*(unsigned int *)(v_rip + 3872497)) <= 0) goto loc_00C4C320;
loc_00C4C319:
    result = (unsigned int)((unsigned int)(2 - 1));
    if ((unsigned int)(v_rdi) != 0) {
        result = 0;
    }
    *(unsigned int *)(v_rip + 2850842) = (unsigned int)(result);
    result = strstr(*(unsigned __int64 *)(a1 + 216), v_rip + 183888, (unsigned __int8)(2 - 1), a4);
    if (result != 0) goto loc_00C4C5CB;
    if ((*(unsigned int *)(v_rip + 2850822)) != 0) goto loc_00C4C5C8;
    result = VfTriageSystem(a1, v_rip + 183888, (unsigned __int8)(2 - 1), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844722)))) == ((unsigned int)(v_r15))) goto loc_00C4C3A2;
    if ((*(unsigned int *)(v_rip + 3872415)) != 0) goto loc_00C4C389;
    if ((*(unsigned int *)(v_rip + 3915230)) != ((unsigned int)(v_r15))) goto loc_00C4C389;
    result = (unsigned int)(*(unsigned int *)(v_rip + 1844722));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 1844722)))) & (4)) == 0) {
        a2 = 4;
        a1 = v_rip + 199708;
        result = VfInitSetVerifyDriverTargets(a1, a2, (unsigned __int8)(2 - 1), a4);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844673)))) == ((unsigned int)(v_r15))) goto loc_00C4C3A2;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 1844673)))) & (0x400004ULL)) != 0) {
        *(unsigned int *)(v_rip + 3872358) = (unsigned int)(2 - 1);
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3872352))) == 0) goto loc_00C4C40B;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 3872352))) >> (16));
    *(unsigned int *)(v_rip + 3872375) = (unsigned int)(result);
    *(unsigned __int16 *)(v_rip + 3872334) = 0;
    if (((unsigned int)(result)) >= 3) goto loc_00C4C3FC;
    *(unsigned int *)(v_rip + 3872353) = 256;
    goto loc_00C4C40B;
loc_00C4C3CD:
    if ((*(unsigned int *)(v_rip + 2211277)) == 0) goto loc_00C4C2A7;
    a1 = 0;
    result = ViDisableVerification(a1, a2, (unsigned __int8)(2 - 1), a4);
    if (((*(unsigned int *)(v_rip + 2852246)) & (0x410ULL)) == 0) goto loc_00C4C5D3;
    *(unsigned int *)(v_rip + 2850649) = (unsigned int)(2 - 1);
    goto loc_00C4C5D3;
loc_00C4C3FC:
    if (((unsigned int)(result)) >= = 512) {
        *(unsigned int *)(v_rip + 3872289) = 512;
    }
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, a2, (unsigned __int8)(2 - 1), a4);
    *(unsigned int *)(v_rip + 3872652) = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 2852326)))) != ((unsigned int)(2 - 1))) goto loc_00C4C4C8;
loc_00C4C427:
    *(unsigned int *)(v_rip + 3915043) = 0;
loc_00C4C42D:
    *(unsigned int *)(v_rip + 3872213) = 0;
loc_00C4C433:
    if ((((unsigned __int8)(2 - 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 2852167))))) == 0) goto loc_00C4C44A;
    if ((*(unsigned int *)(v_rip + 3872196)) == 0) goto loc_00C4C5A4;
loc_00C4C44A:
    if ((*(unsigned int *)(v_rip + 2852276)) != 0) goto loc_00C4C5AB;
    if ((*(unsigned int *)(v_rip + 3872172)) != 0) goto loc_00C4C5AB;
    result = ((unsigned int)(*(unsigned int *)(v_rip + 3914984))) - (2);
    result = (result) >> (1);
loc_00C4C488:
    if ((v_rip + 3927393) >= (v_rip + 3927393 + result * 2)) goto loc_00C4C5AB;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3927393))) > ((unsigned __int16)(2 + 30))) goto loc_00C4C4A4;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3927393))) < ((unsigned __int16)(2 + 30))) goto loc_00C4C593;
loc_00C4C4A4:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rip + 3927393))) == ((unsigned __int16)((unsigned int)(0x3000ULL)))) goto loc_00C4C593;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 3927393))) == 42) goto loc_00C4C5A4;
    if (((unsigned int)(*(unsigned __int16 *)(v_rip + 3927393))) != 34) goto loc_00C4C548;
    goto loc_00C4C527;
loc_00C4C4C8:
    if (((unsigned int)(result)) != 2) goto loc_00C4C4E7;
    *(unsigned int *)(v_rip + 2852144) = (unsigned int)(2 - 1);
    *(unsigned int *)(v_rip + 2852321) = (unsigned int)(2 - 1);
    *(unsigned int *)(v_rip + 2850838) = (unsigned int)(2 - 1);
    goto loc_00C4C427;
loc_00C4C4E7:
    if ((*(unsigned int *)(v_rip + 3914850)) != ((unsigned int)(v_r15))) goto loc_00C4C42D;
    result = ViInitPickRandomTargets(v_rip + 3927393 + 2, *(unsigned __int16 *)(v_rip + 3927393), (unsigned __int8)(2 - 1), a4);
    if ((unsigned int)(result) == 0) goto loc_00C4C5D3;
    *(unsigned int *)(v_rip + 3914818) = 0;
    if ((*(unsigned int *)(v_rip + 1844284)) <= 2) goto loc_00C4C433;
    result = VfSetVerifierRunningMode(2, *(unsigned __int16 *)(v_rip + 3927393), (unsigned __int8)(2 - 1), a4);
    goto loc_00C4C433;
loc_00C4C521:
    if ((*(unsigned __int16 *)(v_rip + 3927393 + 2)) == 34) goto loc_00C4C54D;
loc_00C4C527:
    v_rbx = (v_rip + 3927393 + 2) + (2);
    if (v_rbx < (v_rip + 3927393 + result * 2)) goto loc_00C4C521;
    goto loc_00C4C5AB;
loc_00C4C531:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) > ((unsigned __int16)(2 + 30))) goto loc_00C4C540;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) < ((unsigned __int16)(2 + 30))) goto loc_00C4C54D;
loc_00C4C540:
    if (((unsigned __int16)(*(unsigned __int16 *)(v_rbx))) == ((unsigned __int16)((unsigned int)(0x3000ULL)))) goto loc_00C4C54D;
    v_rbx = (v_rbx) + (2);
loc_00C4C548:
    if (v_rbx < (v_rip + 3927393 + result * 2)) goto loc_00C4C531;
loc_00C4C54D:
    a2 = (v_rbx) - (2);
    a2 = (a2) >> (1);
    a2 = (unsigned int)((a2) + (a2));
    if (condition_is_equal) goto loc_00C4C58A;
    v_stack_m38 = (unsigned __int16)(a2);
    v_stack_m36 = (unsigned __int16)(2 + a2 * 1);
    if (((unsigned __int16)(2 + a2 * 1)) < ((unsigned __int16)(a2))) goto loc_00C4C5AB;
    v_stack_m30 = 2;
    result = RtlEqualUnicodeString(v_rip - 791878, v_stack_m38, (unsigned __int8)(2 - 1), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00C4C59B;
loc_00C4C58A:
    goto loc_00C4C488;
loc_00C4C593:
    a1 = (v_rbx + 2) + (2);
    goto loc_00C4C488;
loc_00C4C59B:
    *(unsigned int *)(v_rip + 2852122) = (unsigned int)(2 - 1);
    goto loc_00C4C5AB;
loc_00C4C5A4:
    *(unsigned int *)(v_rip + 2851929) = (unsigned int)(2 - 1);
loc_00C4C5AB:
    if (((*(unsigned int *)(v_rip + 2851787)) & (0x2000ULL)) != 0) {
        *(unsigned int *)(v_rip + 2852094) = (unsigned int)(2 - 1);
    }
    result = VfInitSystemNoRebootNeeded(a1, (unsigned int)((unsigned int)(2 - 1)), (unsigned __int8)(2 - 1), a4);
    goto loc_00C4C5D3;
loc_00C4C5C8:
loc_00C4C5CB:
    a1 = (result != 0) ? 1 : 0;
    result = ViDisableVerification(a1, (unsigned int)((unsigned int)(2 - 1)), (unsigned __int8)(2 - 1), a4);
loc_00C4C5D3:
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ViInitSystemPhase0(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint16_t v_stack_m36;
    uint16_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x38) = v_xmm0;
    Arg4 = 0;
    Arg2 = 0;
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x84))) & (2));
    *(uint8_t *)(v_rip + 0x21BF9D) = (uint8_t)(2 - 1);
    *(uint32_t *)(v_rip + 0x21BF9E) = (uint32_t)(2 + 30);
    result = KiInitializeMutant(v_rip + 2852627, Arg2, (uint8_t)(2 - 1), Arg4);
    local_r15 = (uint32_t)((local_r15) | (0xFFFFFFFFULL));
    *(uint64_t *)(v_rip + 0x2B87AB) = v_rip + 2852794;
    *(uint64_t *)(v_rip + 0x2B879C) = v_rip + 2852794;
    *(uint64_t *)(v_rip + 0x2B86F6) = v_rip + 2852597;
    *(uint64_t *)(v_rip + 0x2B86E7) = v_rip + 2852597;
    *(uint64_t *)(v_rip + 0x2B8661) = v_rip + 2852448;
    *(uint64_t *)(v_rip + 0x2B8652) = v_rip + 2852448;
    result = v_rip + 2852448;
    if ((*(uint32_t *)(v_rip + 0x1C2713)) == ((uint32_t)(local_r15))) {
        result = *(uint32_t *)(v_rip + 0x21BF2A);
        result = (uint32_t)((result) & (0x400000ULL));
        result = (uint32_t)(-(result));
        Arg1 = (uint32_t)((v_rip + 2852627) & ((uint32_t)((uint32_t)(0xFFFFFFFEULL))));
        Arg1 = (uint32_t)((Arg1) + (4));
        *(uint32_t *)(v_rip + 0x1C26BA) = (uint32_t)(Arg1);
        *(uint32_t *)(v_rip + 0x2B8814) = (uint32_t)(Arg1);
    }
    local_rbp = 0;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C26BA)))) == ((uint32_t)(local_r15))) goto loc_00C4C3CD;
    *(uint32_t *)(v_rip + 0x21BEF9) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C26BA)));
loc_00C4C2A7:
    if ((uint32_t)(local_rdi) != 0) goto loc_00C4C2E6;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) + 0x38);
        *(uint64_t *)(v_rip + 0x3B1776) = result;
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) + 0x40);
        *(uint64_t *)(v_rip + 0x3B1773) = result;
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) + 0x48);
        *(uint64_t *)(v_rip + 0x3B1770) = result;
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) + 0x50);
        *(uint64_t *)(v_rip + 0x3B176D) = result;
        result = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xF0) + 0x118) + 0x58);
        *(uint64_t *)(v_rip + 0x3B176A) = result;
    }
    *(uint64_t *)(v_rip + 0x2B86D2) = *(uint64_t *)(v_rip + 0x21BEA9);
    if (((*(uint32_t *)(v_rip + 0x2B8690)) & (0x410ULL)) == 0) goto loc_00C4C320;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C26BA)))) == ((uint32_t)(local_r15))) goto loc_00C4C320;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3BBE45))) + 1);
    if ((((uint32_t)((uint32_t)(0xFFFFFFFEULL))) & ((uint32_t)(result))) != 0) goto loc_00C4C319;
    if ((*(uint32_t *)(v_rip + 0x3B16F1)) <= 0) goto loc_00C4C320;
loc_00C4C319:
    result = (uint32_t)((uint32_t)(2 - 1));
    if ((uint32_t)(local_rdi) != 0) {
        result = 0;
    }
    *(uint32_t *)(v_rip + 0x2B801A) = (uint32_t)(result);
    result = strstr(*(uint64_t *)(arg1 + 0xD8), v_rip + 183888, (uint8_t)(2 - 1), Arg4);
    if (result != 0) goto loc_00C4C5CB;
    if ((*(uint32_t *)(v_rip + 0x2B8006)) != 0) goto loc_00C4C5C8;
    result = VfTriageSystem(Arg1, v_rip + 183888, (uint8_t)(2 - 1), Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C25F2)))) == ((uint32_t)(local_r15))) goto loc_00C4C3A2;
    if ((*(uint32_t *)(v_rip + 0x3B169F)) != 0) goto loc_00C4C389;
    if ((*(uint32_t *)(v_rip + 0x3BBDDE)) != ((uint32_t)(local_r15))) goto loc_00C4C389;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x1C25F2));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C25F2)))) & (4)) == 0) {
        Arg2 = 4;
        Arg1 = v_rip + 199708;
        result = VfInitSetVerifyDriverTargets(Arg1, Arg2, (uint8_t)(2 - 1), Arg4);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C25C1)))) == ((uint32_t)(local_r15))) goto loc_00C4C3A2;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x1C25C1)))) & (0x400004ULL)) != 0) {
        *(uint32_t *)(v_rip + 0x3B1666) = (uint32_t)(2 - 1);
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3B1660))) == 0) goto loc_00C4C40B;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x3B1660))) >> (16));
    *(uint32_t *)(v_rip + 0x3B1677) = (uint32_t)(result);
    *(uint16_t *)(v_rip + 0x3B164E) = 0;
    if (((uint32_t)(result)) >= 3) goto loc_00C4C3FC;
    *(uint32_t *)(v_rip + 0x3B1661) = 256;
    goto loc_00C4C40B;
loc_00C4C3CD:
    if ((*(uint32_t *)(v_rip + 0x21BDCD)) == 0) goto loc_00C4C2A7;
    Arg1 = 0;
    result = ViDisableVerification(Arg1, Arg2, (uint8_t)(2 - 1), Arg4);
    if (((*(uint32_t *)(v_rip + 0x2B8596)) & (0x410ULL)) == 0) goto loc_00C4C5D3;
    *(uint32_t *)(v_rip + 0x2B7F59) = (uint32_t)(2 - 1);
    goto loc_00C4C5D3;
loc_00C4C3FC:
    if (((uint32_t)(result)) >= = 512) {
        *(uint32_t *)(v_rip + 0x3B1621) = 512;
    }
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, Arg2, (uint8_t)(2 - 1), Arg4);
    *(uint32_t *)(v_rip + 0x3B178C) = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2B85E6)))) != ((uint32_t)(2 - 1))) goto loc_00C4C4C8;
loc_00C4C427:
    *(uint32_t *)(v_rip + 0x3BBD23) = 0;
loc_00C4C42D:
    *(uint32_t *)(v_rip + 0x3B15D5) = 0;
loc_00C4C433:
    if ((((uint8_t)(2 - 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2B8547))))) == 0) goto loc_00C4C44A;
    if ((*(uint32_t *)(v_rip + 0x3B15C4)) == 0) goto loc_00C4C5A4;
loc_00C4C44A:
    if ((*(uint32_t *)(v_rip + 0x2B85B4)) != 0) goto loc_00C4C5AB;
    if ((*(uint32_t *)(v_rip + 0x3B15AC)) != 0) goto loc_00C4C5AB;
    result = ((uint32_t)(*(uint32_t *)(v_rip + 0x3BBCE8))) - (2);
    result = (result) >> (1);
loc_00C4C488:
    if ((v_rip + 3927393) >= (v_rip + 3927393 + result * 2)) goto loc_00C4C5AB;
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x3BED61))) > ((uint16_t)(2 + 30))) goto loc_00C4C4A4;
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x3BED61))) < ((uint16_t)(2 + 30))) goto loc_00C4C593;
loc_00C4C4A4:
    if (((uint16_t)(*(uint16_t *)(v_rip + 0x3BED61))) == ((uint16_t)((uint32_t)(0x3000ULL)))) goto loc_00C4C593;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x3BED61))) == 42) goto loc_00C4C5A4;
    if (((uint32_t)(*(uint16_t *)(v_rip + 0x3BED61))) != 34) goto loc_00C4C548;
    goto loc_00C4C527;
loc_00C4C4C8:
    if (((uint32_t)(result)) != 2) goto loc_00C4C4E7;
    *(uint32_t *)(v_rip + 0x2B8530) = (uint32_t)(2 - 1);
    *(uint32_t *)(v_rip + 0x2B85E1) = (uint32_t)(2 - 1);
    *(uint32_t *)(v_rip + 0x2B8016) = (uint32_t)(2 - 1);
    goto loc_00C4C427;
loc_00C4C4E7:
    if ((*(uint32_t *)(v_rip + 0x3BBC62)) != ((uint32_t)(local_r15))) goto loc_00C4C42D;
    result = ViInitPickRandomTargets(v_rip + 3927393 + 2, *(uint16_t *)(v_rip + 0x3BED61), (uint8_t)(2 - 1), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00C4C5D3;
    *(uint32_t *)(v_rip + 0x3BBC42) = 0;
    if ((*(uint32_t *)(v_rip + 0x1C243C)) <= 2) goto loc_00C4C433;
    result = VfSetVerifierRunningMode(2, *(uint16_t *)(v_rip + 0x3BED61), (uint8_t)(2 - 1), Arg4);
    goto loc_00C4C433;
loc_00C4C521:
    if ((*(uint16_t *)(v_rip + 0x3BED61 + 0x2)) == 34) goto loc_00C4C54D;
loc_00C4C527:
    local_rbx = (v_rip + 3927393 + 2) + (2);
    if (local_rbx < (v_rip + 3927393 + result * 2)) goto loc_00C4C521;
    goto loc_00C4C5AB;
loc_00C4C531:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) > ((uint16_t)(2 + 30))) goto loc_00C4C540;
    if (((uint16_t)(*(uint16_t *)(local_rbx))) < ((uint16_t)(2 + 30))) goto loc_00C4C54D;
loc_00C4C540:
    if (((uint16_t)(*(uint16_t *)(local_rbx))) == ((uint16_t)((uint32_t)(0x3000ULL)))) goto loc_00C4C54D;
    local_rbx = (local_rbx) + (2);
loc_00C4C548:
    if (local_rbx < (v_rip + 3927393 + result * 2)) goto loc_00C4C531;
loc_00C4C54D:
    Arg2 = (local_rbx) - (2);
    Arg2 = (Arg2) >> (1);
    Arg2 = (uint32_t)((Arg2) + (Arg2));
    if (condition_is_equal) goto loc_00C4C58A;
    v_stack_m38 = (uint16_t)(Arg2);
    v_stack_m36 = (uint16_t)(2 + Arg2 * 1);
    if (((uint16_t)(2 + Arg2 * 1)) < ((uint16_t)(Arg2))) goto loc_00C4C5AB;
    v_stack_m30 = 2;
    result = RtlEqualUnicodeString(v_rip - 791878, v_stack_m38, (uint8_t)(2 - 1), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00C4C59B;
loc_00C4C58A:
    goto loc_00C4C488;
loc_00C4C593:
    Arg1 = (local_rbx + 2) + (2);
    goto loc_00C4C488;
loc_00C4C59B:
    *(uint32_t *)(v_rip + 0x2B851A) = (uint32_t)(2 - 1);
    goto loc_00C4C5AB;
loc_00C4C5A4:
    *(uint32_t *)(v_rip + 0x2B8459) = (uint32_t)(2 - 1);
loc_00C4C5AB:
    if (((*(uint32_t *)(v_rip + 0x2B83CB)) & (0x2000ULL)) != 0) {
        *(uint32_t *)(v_rip + 0x2B84FE) = (uint32_t)(2 - 1);
    }
    result = VfInitSystemNoRebootNeeded(Arg1, (uint32_t)((uint32_t)(2 - 1)), (uint8_t)(2 - 1), Arg4);
    goto loc_00C4C5D3;
loc_00C4C5C8:
loc_00C4C5CB:
    Arg1 = (result != 0) ? 1 : 0;
    result = ViDisableVerification(Arg1, (uint32_t)((uint32_t)(2 - 1)), (uint8_t)(2 - 1), Arg4);
loc_00C4C5D3:
    local_rsp = (local_rsp) + (48);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xD8` | `64` | `R` |
| `Arg1` | `+ 0xF0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C4C1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
