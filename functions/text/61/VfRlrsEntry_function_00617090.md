# VfRlrsEntry

- RVA: `0x00617090`–`0x006174BE` (길이 `1,070` bytes)
- VA: `0x0000000140617090`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D242C`
- 디코드: `170`개 명령, `1,070/1,070` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **34**

### Outgoing calls
- `0x0061747D` → [DifRegisterPlugin](DifRegisterPlugin_function_0061ABE0.md) (function, `0x0061ABE0`)
- `0x00617484` → [VfFaultsInitPhase0](../../pagevrfy/BA/VfFaultsInitPhase0_function_00BA6328.md) (function, `0x00BA6328`)
- `0x00617492` → [VfFaultsInitPhase1](../../pagevrfy/BA/VfFaultsInitPhase1_function_00BA6458.md) (function, `0x00BA6458`)
- `0x006174A3` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x006170AA` → RVA `0x00E0A740` (`.data`; read)
- `0x006170C5` → RVA `0x00617590` (`ViRlrsUnload`; read)
- `0x006170D1` → RVA `0x00F03F08` (`.data`; write)
- `0x006170D8` → RVA `0x006CE390` (` ?? ::FNODOBFM::`string'`; read)
- `0x006170E4` → RVA `0x006CE330` (` ?? ::FNODOBFM::`string'`; read)
- `0x006170F0` → RVA `0x006CE310` (` ?? ::FNODOBFM::`string'`; read)
- `0x006170FC` → RVA `0x006CE3B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617107` → RVA `0x006CE3A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617112` → RVA `0x006CF950` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061711D` → RVA `0x00BAF7C0` (`ViRlrsMmProbeAndLockPages_Entry`; read)
- `0x00617128` → RVA `0x006CF980` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061713E` → RVA `0x006CF970` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617149` → RVA `0x006CE3C0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617154` → RVA `0x006CE510` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061715F` → RVA `0x006CE4B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061716A` → RVA `0x006CE440` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617178` → RVA `0x006CE490` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617186` → RVA `0x006CE590` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617194` → RVA `0x006CE570` (` ?? ::FNODOBFM::`string'`; read)
- `0x006171A2` → RVA `0x006CE550` (` ?? ::FNODOBFM::`string'`; read)
- `0x006172A9` → RVA `0x00F03F00` (`.data`; read)
- `0x006172B0` → RVA `0x006CE5B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x006172CB` → RVA `0x006CF8F0` (` ?? ::FNODOBFM::`string'`; read)
- `0x006172E4` → RVA `0x00BAF760` (`ViRlrsMmMapLockedPages_Entry`; read)
- `0x006172FE` → RVA `0x006CF8D0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617316` → RVA `0x006CF930` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617324` → RVA `0x006CF910` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617332` → RVA `0x006CF880` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617340` → RVA `0x006CF860` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061734E` → RVA `0x006CE300` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061735C` → RVA `0x006CF8B0` (` ?? ::FNODOBFM::`string'`; read)
- `0x0061736A` → RVA `0x006CF890` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617378` → RVA `0x006CF9A0` (` ?? ::FNODOBFM::`string'`; read)
- `0x00617489` → RVA `0x00F048B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00617484` → [VfFaultsInitPhase0](../../pagevrfy/BA/VfFaultsInitPhase0_function_00BA6328.md) (`.text` → `PAGEVRFY`)
  - `0x00617492` → [VfFaultsInitPhase1](../../pagevrfy/BA/VfFaultsInitPhase1_function_00BA6458.md) (`.text` → `PAGEVRFY`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00617090  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00617095  48 89 7C 24 10                  mov qword ptr [rsp + 0x10], rdi
0061709A  55                              push rbp
0061709B  48 8D AC 24 70 FD FF FF         lea rbp, [rsp - 0x290]
006170A3  48 81 EC 90 03 00 00            sub rsp, 0x390
006170AA  48 8B 05 8F 36 7F 00            mov rax, qword ptr [rip + 0x7f368f]
006170B1  48 33 C4                        xor rax, rsp
006170B4  48 89 85 80 02 00 00            mov qword ptr [rbp + 0x280], rax
006170BB  33 FF                           xor edi, edi
006170BD  C7 44 24 28 9D 01 00 00         mov dword ptr [rsp + 0x28], 0x19d
006170C5  48 8D 05 C4 04 00 00            lea rax, [rip + 0x4c4]
006170CC  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
006170D1  48 89 05 30 CE 8E 00            mov qword ptr [rip + 0x8ece30], rax
006170D8  48 8D 05 B1 72 0B 00            lea rax, [rip + 0xb72b1]
006170DF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
006170E4  48 8D 05 45 72 0B 00            lea rax, [rip + 0xb7245]
006170EB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
006170F0  48 8D 05 19 72 0B 00            lea rax, [rip + 0xb7219]
006170F7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
006170FC  48 8D 05 AD 72 0B 00            lea rax, [rip + 0xb72ad]
00617103  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
00617107  48 8D 05 92 72 0B 00            lea rax, [rip + 0xb7292]
0061710E  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
00617112  48 8D 05 37 88 0B 00            lea rax, [rip + 0xb8837]
00617119  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
0061711D  48 8D 05 9C 86 59 00            lea rax, [rip + 0x59869c]
00617124  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00617128  48 8D 05 51 88 0B 00            lea rax, [rip + 0xb8851]
0061712F  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00617133  48 8D 05 86 86 59 00            lea rax, [rip + 0x598686]
0061713A  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0061713E  48 8D 05 2B 88 0B 00            lea rax, [rip + 0xb882b]
00617145  48 89 45 00                     mov qword ptr [rbp], rax
00617149  48 8D 05 70 72 0B 00            lea rax, [rip + 0xb7270]
00617150  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
00617154  48 8D 05 B5 73 0B 00            lea rax, [rip + 0xb73b5]
0061715B  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
0061715F  48 8D 05 4A 73 0B 00            lea rax, [rip + 0xb734a]
00617166  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0061716A  48 8D 05 CF 72 0B 00            lea rax, [rip + 0xb72cf]
00617171  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
00617178  48 8D 05 11 73 0B 00            lea rax, [rip + 0xb7311]
0061717F  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
00617186  48 8D 05 03 74 0B 00            lea rax, [rip + 0xb7403]
0061718D  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
00617194  48 8D 05 D5 73 0B 00            lea rax, [rip + 0xb73d5]
0061719B  48 89 85 E0 00 00 00            mov qword ptr [rbp + 0xe0], rax
006171A2  48 8D 05 A7 73 0B 00            lea rax, [rip + 0xb73a7]
006171A9  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
006171AE  C7 44 24 48 9E 01 00 00         mov dword ptr [rsp + 0x48], 0x19e
006171B6  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
006171BB  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
006171C0  C7 44 24 68 9F 01 00 00         mov dword ptr [rsp + 0x68], 0x19f
006171C8  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
006171CD  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
006171D2  C7 45 88 A3 01 00 00            mov dword ptr [rbp - 0x78], 0x1a3
006171D9  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
006171DD  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
006171E1  C7 45 A8 A2 01 00 00            mov dword ptr [rbp - 0x58], 0x1a2
006171E8  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
006171EC  48 89 7D B8                     mov qword ptr [rbp - 0x48], rdi
006171F0  C7 45 C8 D9 00 00 00            mov dword ptr [rbp - 0x38], 0xd9
006171F7  48 89 7D D8                     mov qword ptr [rbp - 0x28], rdi
006171FB  C7 45 E8 D8 00 00 00            mov dword ptr [rbp - 0x18], 0xd8
00617202  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
00617206  C7 45 08 DD 00 00 00            mov dword ptr [rbp + 8], 0xdd
0061720D  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
00617211  48 89 7D 18                     mov qword ptr [rbp + 0x18], rdi
00617215  C7 45 28 E9 00 00 00            mov dword ptr [rbp + 0x28], 0xe9
0061721C  48 89 7D 30                     mov qword ptr [rbp + 0x30], rdi
00617220  48 89 7D 38                     mov qword ptr [rbp + 0x38], rdi
00617224  C7 45 48 EE 00 00 00            mov dword ptr [rbp + 0x48], 0xee
0061722B  48 89 7D 50                     mov qword ptr [rbp + 0x50], rdi
0061722F  48 89 7D 58                     mov qword ptr [rbp + 0x58], rdi
00617233  C7 45 68 EB 00 00 00            mov dword ptr [rbp + 0x68], 0xeb
0061723A  48 89 7D 70                     mov qword ptr [rbp + 0x70], rdi
0061723E  48 89 7D 78                     mov qword ptr [rbp + 0x78], rdi
00617242  C7 85 88 00 00 00 EC 00 00 00   mov dword ptr [rbp + 0x88], 0xec
0061724C  48 89 BD 90 00 00 00            mov qword ptr [rbp + 0x90], rdi
00617253  48 89 BD 98 00 00 00            mov qword ptr [rbp + 0x98], rdi
0061725A  C7 85 A8 00 00 00 EA 00 00 00   mov dword ptr [rbp + 0xa8], 0xea
00617264  48 89 BD B0 00 00 00            mov qword ptr [rbp + 0xb0], rdi
0061726B  48 89 BD B8 00 00 00            mov qword ptr [rbp + 0xb8], rdi
00617272  C7 85 C8 00 00 00 E7 00 00 00   mov dword ptr [rbp + 0xc8], 0xe7
0061727C  48 89 BD D0 00 00 00            mov qword ptr [rbp + 0xd0], rdi
00617283  48 89 BD D8 00 00 00            mov qword ptr [rbp + 0xd8], rdi
0061728A  C7 85 E8 00 00 00 E6 00 00 00   mov dword ptr [rbp + 0xe8], 0xe6
00617294  48 89 BD F0 00 00 00            mov qword ptr [rbp + 0xf0], rdi
0061729B  48 89 BD F8 00 00 00            mov qword ptr [rbp + 0xf8], rdi
006172A2  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
006172A9  4C 8D 0D 50 CC 8E 00            lea r9, [rip + 0x8ecc50]
006172B0  48 8D 05 F9 72 0B 00            lea rax, [rip + 0xb72f9]
006172B7  C7 85 08 01 00 00 E5 00 00 00   mov dword ptr [rbp + 0x108], 0xe5
006172C1  48 89 85 20 01 00 00            mov qword ptr [rbp + 0x120], rax
006172C8  8D 57 1B                        lea edx, [rdi + 0x1b]
006172CB  48 8D 05 1E 86 0B 00            lea rax, [rip + 0xb861e]
006172D2  48 89 BD 10 01 00 00            mov qword ptr [rbp + 0x110], rdi
006172D9  48 89 85 40 01 00 00            mov qword ptr [rbp + 0x140], rax
006172E0  44 8D 47 02                     lea r8d, [rdi + 2]
006172E4  48 8D 05 75 84 59 00            lea rax, [rip + 0x598475]
006172EB  48 89 BD 18 01 00 00            mov qword ptr [rbp + 0x118], rdi
006172F2  48 89 85 50 01 00 00            mov qword ptr [rbp + 0x150], rax
006172F9  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
006172FE  48 8D 05 CB 85 0B 00            lea rax, [rip + 0xb85cb]
00617305  C7 85 28 01 00 00 E8 00 00 00   mov dword ptr [rbp + 0x128], 0xe8
0061730F  48 89 85 60 01 00 00            mov qword ptr [rbp + 0x160], rax
00617316  48 8D 05 13 86 0B 00            lea rax, [rip + 0xb8613]
0061731D  48 89 85 80 01 00 00            mov qword ptr [rbp + 0x180], rax
00617324  48 8D 05 E5 85 0B 00            lea rax, [rip + 0xb85e5]
0061732B  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
00617332  48 8D 05 47 85 0B 00            lea rax, [rip + 0xb8547]
00617339  48 89 85 C0 01 00 00            mov qword ptr [rbp + 0x1c0], rax
00617340  48 8D 05 19 85 0B 00            lea rax, [rip + 0xb8519]
00617347  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
0061734E  48 8D 05 AB 6F 0B 00            lea rax, [rip + 0xb6fab]
00617355  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
0061735C  48 8D 05 4D 85 0B 00            lea rax, [rip + 0xb854d]
00617363  48 89 85 20 02 00 00            mov qword ptr [rbp + 0x220], rax
0061736A  48 8D 05 1F 85 0B 00            lea rax, [rip + 0xb851f]
00617371  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
00617378  48 8D 05 21 86 0B 00            lea rax, [rip + 0xb8621]
0061737F  48 89 85 60 02 00 00            mov qword ptr [rbp + 0x260], rax
00617386  48 89 BD 30 01 00 00            mov qword ptr [rbp + 0x130], rdi
0061738D  48 89 BD 38 01 00 00            mov qword ptr [rbp + 0x138], rdi
00617394  C7 85 48 01 00 00 DC 00 00 00   mov dword ptr [rbp + 0x148], 0xdc
0061739E  48 89 BD 58 01 00 00            mov qword ptr [rbp + 0x158], rdi
006173A5  C7 85 68 01 00 00 71 01 00 00   mov dword ptr [rbp + 0x168], 0x171
006173AF  48 89 BD 70 01 00 00            mov qword ptr [rbp + 0x170], rdi
006173B6  48 89 BD 78 01 00 00            mov qword ptr [rbp + 0x178], rdi
006173BD  C7 85 88 01 00 00 70 01 00 00   mov dword ptr [rbp + 0x188], 0x170
006173C7  48 89 BD 90 01 00 00            mov qword ptr [rbp + 0x190], rdi
006173CE  48 89 BD 98 01 00 00            mov qword ptr [rbp + 0x198], rdi
006173D5  C7 85 A8 01 00 00 3A 01 00 00   mov dword ptr [rbp + 0x1a8], 0x13a
006173DF  48 89 BD B0 01 00 00            mov qword ptr [rbp + 0x1b0], rdi
006173E6  48 89 BD B8 01 00 00            mov qword ptr [rbp + 0x1b8], rdi
006173ED  C7 85 C8 01 00 00 6E 01 00 00   mov dword ptr [rbp + 0x1c8], 0x16e
006173F7  48 89 BD D0 01 00 00            mov qword ptr [rbp + 0x1d0], rdi
006173FE  48 89 BD D8 01 00 00            mov qword ptr [rbp + 0x1d8], rdi
00617405  C7 85 E8 01 00 00 6C 01 00 00   mov dword ptr [rbp + 0x1e8], 0x16c
0061740F  48 89 BD F0 01 00 00            mov qword ptr [rbp + 0x1f0], rdi
00617416  48 89 BD F8 01 00 00            mov qword ptr [rbp + 0x1f8], rdi
0061741D  C7 85 08 02 00 00 6D 01 00 00   mov dword ptr [rbp + 0x208], 0x16d
00617427  48 89 BD 10 02 00 00            mov qword ptr [rbp + 0x210], rdi
0061742E  48 89 BD 18 02 00 00            mov qword ptr [rbp + 0x218], rdi
00617435  C7 85 28 02 00 00 F0 00 00 00   mov dword ptr [rbp + 0x228], 0xf0
0061743F  48 89 BD 30 02 00 00            mov qword ptr [rbp + 0x230], rdi
00617446  48 89 BD 38 02 00 00            mov qword ptr [rbp + 0x238], rdi
0061744D  C7 85 48 02 00 00 F1 00 00 00   mov dword ptr [rbp + 0x248], 0xf1
00617457  48 89 BD 50 02 00 00            mov qword ptr [rbp + 0x250], rdi
0061745E  48 89 BD 58 02 00 00            mov qword ptr [rbp + 0x258], rdi
00617465  C7 85 68 02 00 00 20 01 00 00   mov dword ptr [rbp + 0x268], 0x120
0061746F  48 89 BD 70 02 00 00            mov qword ptr [rbp + 0x270], rdi
00617476  48 89 BD 78 02 00 00            mov qword ptr [rbp + 0x278], rdi
0061747D  E8 5E 37 00 00                  call 0x14061abe0
00617482  8B D8                           mov ebx, eax
00617484  E8 9F EE 58 00                  call 0x140ba6328
00617489  40 38 3D 28 D4 8E 00            cmp byte ptr [rip + 0x8ed428], dil
00617490  74 05                           je 0x140617497
00617492  E8 C1 EF 58 00                  call 0x140ba6458
00617497  8B C3                           mov eax, ebx
00617499  48 8B 8D 80 02 00 00            mov rcx, qword ptr [rbp + 0x280]
006174A0  48 33 CC                        xor rcx, rsp
006174A3  E8 98 51 09 00                  call 0x1406ac640
006174A8  4C 8D 9C 24 90 03 00 00         lea r11, [rsp + 0x390]
006174B0  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
006174B4  49 8B 7B 18                     mov rdi, qword ptr [r11 + 0x18]
006174B8  49 8B E3                        mov rsp, r11
006174BB  5D                              pop rbp
006174BC  C3                              ret
006174BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VfRlrsEntry(void)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned int v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned int v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned int v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned int v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned int v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned int v_stack_m350;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned int v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m8;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned int v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rdi;
    v_rsp = (v_rsp) - (912);
    result = (*(unsigned __int64 *)(v_rip + 8337039)) ^ (v_rsp);
    v_stack_m18 = result;
    v_rdi = 0;
    v_stack_m370 = 413;
    v_stack_m368 = 0;
    *(unsigned __int64 *)(v_rip + 9358896) = v_rip + 1220;
    v_stack_m378 = v_rip + 750257;
    v_stack_m358 = v_rip + 750149;
    v_stack_m338 = v_rip + 750105;
    v_stack_m318 = v_rip + 750253;
    v_stack_m2F8 = v_rip + 750226;
    v_stack_m2D8 = v_rip + 755767;
    v_stack_m2C8 = v_rip + 5867164;
    v_stack_m2B8 = v_rip + 755793;
    v_stack_m2A8 = v_rip + 5867142;
    v_stack_m298 = v_rip + 755755;
    v_stack_m278 = v_rip + 750192;
    v_stack_m258 = v_rip + 750517;
    v_stack_m238 = v_rip + 750410;
    v_stack_m218 = v_rip + 750287;
    v_stack_m1F8 = v_rip + 750353;
    v_stack_m1D8 = v_rip + 750595;
    v_stack_m1B8 = v_rip + 750549;
    v_stack_m360 = 0;
    v_stack_m350 = 414;
    v_stack_m348 = 0;
    v_stack_m340 = 0;
    v_stack_m330 = 415;
    v_stack_m328 = 0;
    v_stack_m320 = 0;
    v_stack_m310 = 419;
    v_stack_m308 = 0;
    v_stack_m300 = 0;
    v_stack_m2F0 = 418;
    v_stack_m2E8 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2D0 = 217;
    v_stack_m2C0 = 0;
    v_stack_m2B0 = 216;
    v_stack_m2A0 = 0;
    v_stack_m290 = 221;
    v_stack_m288 = 0;
    v_stack_m280 = 0;
    v_stack_m270 = 233;
    v_stack_m268 = 0;
    v_stack_m260 = 0;
    v_stack_m250 = 238;
    v_stack_m248 = 0;
    v_stack_m240 = 0;
    v_stack_m230 = 235;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m210 = 236;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m1F0 = 234;
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D0 = 231;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B0 = 230;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = v_rip + 750503;
    v_stack_m190 = 229;
    v_stack_m178 = v_rip + 750329;
    v_stack_m188 = 0;
    v_stack_m158 = v_rip + 755230;
    v_stack_m180 = 0;
    v_stack_m148 = v_rip + 5866613;
    v_stack_m170 = 232;
    v_stack_m138 = v_rip + 755147;
    v_stack_m118 = v_rip + 755219;
    v_stack_mF8 = v_rip + 755173;
    v_stack_mD8 = v_rip + 755015;
    v_stack_mB8 = v_rip + 754969;
    v_stack_m98 = v_rip + 749483;
    v_stack_m78 = v_rip + 755021;
    v_stack_m58 = v_rip + 754975;
    v_stack_m38 = v_rip + 755233;
    v_stack_m168 = 0;
    v_stack_m160 = 0;
    v_stack_m150 = 220;
    v_stack_m140 = 0;
    v_stack_m130 = 369;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_m110 = 368;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_mF0 = 314;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mD0 = 366;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mB0 = 364;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    v_stack_m90 = 365;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 240;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m50 = 241;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m30 = 288;
    v_stack_m28 = 0;
    v_stack_m20 = 0;
    result = DifRegisterPlugin(v_stack_m378, v_rdi + 27, v_rdi + 2, v_rip + 9358416);
    result = VfFaultsInitPhase0(v_stack_m378, v_rdi + 27, v_rdi + 2, v_rip + 9358416);
    if ((*(unsigned __int8 *)(v_rip + 9360424)) != 0) {
        result = VfFaultsInitPhase1(v_stack_m378, v_rdi + 27, v_rdi + 2, v_rip + 9358416);
    }
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rdi + 27, v_rdi + 2, v_rip + 9358416);
    return result;
}
```

## 5. (Beta) C Style

```c
void VfRlrsEntry(void)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m18;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint32_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint32_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m20;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint32_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint32_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint32_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint32_t v_stack_m30;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint32_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint32_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint32_t v_stack_m350;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint32_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint32_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m8;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint32_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rdi;
    local_rsp = (local_rsp) - (912);
    result = (*(uint64_t *)(v_rip + 0x7F368F)) ^ (local_rsp);
    v_stack_m18 = result;
    local_rdi = 0;
    v_stack_m370 = 413;
    v_stack_m368 = 0;
    *(uint64_t *)(v_rip + 0x8ECE30) = v_rip + 1220;
    v_stack_m378 = v_rip + 750257;
    v_stack_m358 = v_rip + 750149;
    v_stack_m338 = v_rip + 750105;
    v_stack_m318 = v_rip + 750253;
    v_stack_m2F8 = v_rip + 750226;
    v_stack_m2D8 = v_rip + 755767;
    v_stack_m2C8 = v_rip + 5867164;
    v_stack_m2B8 = v_rip + 755793;
    v_stack_m2A8 = v_rip + 5867142;
    v_stack_m298 = v_rip + 755755;
    v_stack_m278 = v_rip + 750192;
    v_stack_m258 = v_rip + 750517;
    v_stack_m238 = v_rip + 750410;
    v_stack_m218 = v_rip + 750287;
    v_stack_m1F8 = v_rip + 750353;
    v_stack_m1D8 = v_rip + 750595;
    v_stack_m1B8 = v_rip + 750549;
    v_stack_m360 = 0;
    v_stack_m350 = 414;
    v_stack_m348 = 0;
    v_stack_m340 = 0;
    v_stack_m330 = 415;
    v_stack_m328 = 0;
    v_stack_m320 = 0;
    v_stack_m310 = 419;
    v_stack_m308 = 0;
    v_stack_m300 = 0;
    v_stack_m2F0 = 418;
    v_stack_m2E8 = 0;
    v_stack_m2E0 = 0;
    v_stack_m2D0 = 217;
    v_stack_m2C0 = 0;
    v_stack_m2B0 = 216;
    v_stack_m2A0 = 0;
    v_stack_m290 = 221;
    v_stack_m288 = 0;
    v_stack_m280 = 0;
    v_stack_m270 = 233;
    v_stack_m268 = 0;
    v_stack_m260 = 0;
    v_stack_m250 = 238;
    v_stack_m248 = 0;
    v_stack_m240 = 0;
    v_stack_m230 = 235;
    v_stack_m228 = 0;
    v_stack_m220 = 0;
    v_stack_m210 = 236;
    v_stack_m208 = 0;
    v_stack_m200 = 0;
    v_stack_m1F0 = 234;
    v_stack_m1E8 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1D0 = 231;
    v_stack_m1C8 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B0 = 230;
    v_stack_m1A8 = 0;
    v_stack_m1A0 = 0;
    v_stack_m198 = v_rip + 750503;
    v_stack_m190 = 229;
    v_stack_m178 = v_rip + 750329;
    v_stack_m188 = 0;
    v_stack_m158 = v_rip + 755230;
    v_stack_m180 = 0;
    v_stack_m148 = v_rip + 5866613;
    v_stack_m170 = 232;
    v_stack_m138 = v_rip + 755147;
    v_stack_m118 = v_rip + 755219;
    v_stack_mF8 = v_rip + 755173;
    v_stack_mD8 = v_rip + 755015;
    v_stack_mB8 = v_rip + 754969;
    v_stack_m98 = v_rip + 749483;
    v_stack_m78 = v_rip + 755021;
    v_stack_m58 = v_rip + 754975;
    v_stack_m38 = v_rip + 755233;
    v_stack_m168 = 0;
    v_stack_m160 = 0;
    v_stack_m150 = 220;
    v_stack_m140 = 0;
    v_stack_m130 = 369;
    v_stack_m128 = 0;
    v_stack_m120 = 0;
    v_stack_m110 = 368;
    v_stack_m108 = 0;
    v_stack_m100 = 0;
    v_stack_mF0 = 314;
    v_stack_mE8 = 0;
    v_stack_mE0 = 0;
    v_stack_mD0 = 366;
    v_stack_mC8 = 0;
    v_stack_mC0 = 0;
    v_stack_mB0 = 364;
    v_stack_mA8 = 0;
    v_stack_mA0 = 0;
    v_stack_m90 = 365;
    v_stack_m88 = 0;
    v_stack_m80 = 0;
    v_stack_m70 = 240;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m50 = 241;
    v_stack_m48 = 0;
    v_stack_m40 = 0;
    v_stack_m30 = 288;
    v_stack_m28 = 0;
    v_stack_m20 = 0;
    result = DifRegisterPlugin(v_stack_m378, local_rdi + 27, local_rdi + 2, v_rip + 9358416);
    result = VfFaultsInitPhase0(v_stack_m378, local_rdi + 27, local_rdi + 2, v_rip + 9358416);
    if ((*(uint8_t *)(v_rip + 0x8ED428)) != 0) {
        result = VfFaultsInitPhase1(v_stack_m378, local_rdi + 27, local_rdi + 2, v_rip + 9358416);
    }
    a1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(a1, local_rdi + 27, local_rdi + 2, v_rip + 9358416);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00617090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00617090[BB_00617090]
  bb_00617492[BB_00617492]
  bb_00617497[BB_00617497]
  bb_006174BD[BB_006174BD]
  bb_00617090 -->|branch| bb_00617497
  bb_00617090 -->|fallthrough| bb_00617492
  bb_00617492 -->|flow| bb_00617497
```
