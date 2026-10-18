# CmSelectQualifiedInstallLanguage

- RVA: `0x00C58F58`–`0x00C59530` (길이 `1,496` bytes)
- VA: `0x0000000140C58F58`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6678`
- 디코드: `381`개 명령, `1,496/1,496` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **47**; 고유 호출 대상: **17**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00C5900C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C5901A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C5902B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C59055` → [DownLevelLangIDToLanguageName](../../text/4B/DownLevelLangIDToLanguageName_function_004BBAA8.md) (function, `0x004BBAA8`)
- `0x00C5907E` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x00C590A3` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C590AA` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C590C6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C590D5` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C590F7` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C590FE` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C59129` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C59149` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C59154` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (function, `0x004C3748`)
- `0x00C59170` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C59177` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5918C` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C59193` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C591A8` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C591AF` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C591C1` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (function, `0x007F36BC`)
- `0x00C591DD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C591E4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C5921B` → [CmpFindSubKeyByNumber](../../page/85/CmpFindSubKeyByNumber_function_0085C930.md) (function, `0x0085C930`)
- `0x00C59249` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C59250` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C59268` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (function, `0x0042A780`)
- `0x00C5927B` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (function, `0x00844E1C`)
- `0x00C592A2` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x00C592A9` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x00C592DC` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (function, `0x007F3934`)
- `0x00C59304` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5930B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C59329` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C59330` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5936C` → [CmpCopyCompressedName](../../page/84/CmpCopyCompressedName_function_0084E0D0.md) (function, `0x0084E0D0`)
- `0x00C5938D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00C593A2` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C593A9` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C593CF` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (function, `0x004C3748`)
- `0x00C5940C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00C59484` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C5948B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5949F` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (function, `0x004F5FDC`)
- `0x00C594B2` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x00C594B9` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x00C5950F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpGetSystemControlValues](CmpGetSystemControlValues_function_00C5959C.md) at `0x00C59A01`

### Static image references
- `0x00C58F77` → RVA `0x00E0A740` (`.data`; read)
- `0x00C5906A` → RVA `0x0100D5D0` (`INITDATA`; read)
- `0x00C59077` → RVA `0x00C7E400` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C59091` → RVA `0x0100D65C` (`INITDATA`; reference)
- `0x00C590BB` → RVA `0x00C7E420` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C59159` → RVA `0x00FD9A70` (`PAGEDATA`; write)
- `0x00C591B4` → RVA `0x00C7E3E0` (` ?? ::PBOPGDP::`string'`; read)
- `0x00C5925D` → RVA `0x00C7A3E0` (` ?? ::PBOPGDP::`string'`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **47**
  - `0x00C5900C` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C5901A` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C5902B` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C59055` → [DownLevelLangIDToLanguageName](../../text/4B/DownLevelLangIDToLanguageName_function_004BBAA8.md) (`INIT` → `.text`)
  - `0x00C5907E` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (`INIT` → `PAGE`)
  - `0x00C590A3` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C590AA` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C590C6` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C590D5` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C590F7` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C590FE` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C59129` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C59149` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C59154` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (`INIT` → `.text`)
  - `0x00C59170` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C59177` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5918C` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C59193` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C591A8` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C591AF` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C591C1` → [CmpWalkPath](../../page/7F/CmpWalkPath_function_007F36BC.md) (`INIT` → `PAGE`)
  - `0x00C591DD` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C591E4` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C5921B` → [CmpFindSubKeyByNumber](../../page/85/CmpFindSubKeyByNumber_function_0085C930.md) (`INIT` → `PAGE`)
  - `0x00C59249` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C59250` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C59268` → [RtlInitUnicodeString](../../text/42/RtlInitUnicodeString_function_0042A780.md) (`INIT` → `.text`)
  - `0x00C5927B` → [CmpFindValueByName](../../page/84/CmpFindValueByName_function_00844E1C.md) (`INIT` → `PAGE`)
  - `0x00C592A2` → [HvpGetCellFlat](../../page/85/HvpGetCellFlat_function_00854C60.md) (`INIT` → `PAGE`)
  - `0x00C592A9` → [HvpGetCellPaged](../../page/85/HvpGetCellPaged_function_00854CB0.md) (`INIT` → `PAGE`)
  - `0x00C592DC` → [CmpValueToData](../../page/7F/CmpValueToData_function_007F3934.md) (`INIT` → `PAGE`)
  - `0x00C59304` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5930B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C59329` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C59330` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5936C` → [CmpCopyCompressedName](../../page/84/CmpCopyCompressedName_function_0084E0D0.md) (`INIT` → `PAGE`)
  - `0x00C5938D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`INIT` → `.text`)
  - `0x00C593A2` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C593A9` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C593CF` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (`INIT` → `.text`)
  - `0x00C5940C` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`INIT` → `.text`)
  - `0x00C59484` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C5948B` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5949F` → [_report_rangecheckfailure](../../text/4F/_report_rangecheckfailure_function_004F5FDC.md) (`INIT` → `.text`)
  - `0x00C594B2` → [HvpReleaseCellFlat](../../page/85/HvpReleaseCellFlat_function_0085CC20.md) (`INIT` → `PAGE`)
  - `0x00C594B9` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`INIT` → `PAGE`)
  - `0x00C5950F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C58F58  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C58F5D  55                              push rbp
00C58F5E  56                              push rsi
00C58F5F  57                              push rdi
00C58F60  41 54                           push r12
00C58F62  41 55                           push r13
00C58F64  41 56                           push r14
00C58F66  41 57                           push r15
00C58F68  48 8D AC 24 40 FE FF FF         lea rbp, [rsp - 0x1c0]
00C58F70  48 81 EC C0 02 00 00            sub rsp, 0x2c0
00C58F77  48 8B 05 C2 17 1B 00            mov rax, qword ptr [rip + 0x1b17c2]
00C58F7E  48 33 C4                        xor rax, rsp
00C58F81  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
00C58F88  45 33 ED                        xor r13d, r13d
00C58F8B  44 89 4C 24 34                  mov dword ptr [rsp + 0x34], r9d
00C58F90  44 8B F2                        mov r14d, edx
00C58F93  44 89 6C 24 68                  mov dword ptr [rsp + 0x68], r13d
00C58F98  83 CA FF                        or edx, 0xffffffff
00C58F9B  44 89 6C 24 4C                  mov dword ptr [rsp + 0x4c], r13d
00C58FA0  49 8B D8                        mov rbx, r8
00C58FA3  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00C58FA7  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00C58FAB  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00C58FAF  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00C58FB3  0F 57 C0                        xorps xmm0, xmm0
00C58FB6  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00C58FBA  BF AA 00 00 00                  mov edi, 0xaa
00C58FBF  89 54 24 78                     mov dword ptr [rsp + 0x78], edx
00C58FC3  44 8B C7                        mov r8d, edi
00C58FC6  89 54 24 70                     mov dword ptr [rsp + 0x70], edx
00C58FCA  41 8B F1                        mov esi, r9d
00C58FCD  33 D2                           xor edx, edx
00C58FCF  48 89 5D 80                     mov qword ptr [rbp - 0x80], rbx
00C58FD3  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
00C58FD7  44 89 6C 24 3C                  mov dword ptr [rsp + 0x3c], r13d
00C58FDC  45 8A E5                        mov r12b, r13b
00C58FDF  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
00C58FE4  44 89 6C 24 44                  mov dword ptr [rsp + 0x44], r13d
00C58FE9  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
00C58FEE  44 88 6C 24 31                  mov byte ptr [rsp + 0x31], r13b
00C58FF3  44 89 6C 24 58                  mov dword ptr [rsp + 0x58], r13d
00C58FF8  44 89 6C 24 54                  mov dword ptr [rsp + 0x54], r13d
00C58FFD  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
00C59002  44 89 6C 24 7C                  mov dword ptr [rsp + 0x7c], r13d
00C59007  44 89 6C 24 74                  mov dword ptr [rsp + 0x74], r13d
00C5900C  E8 2F DC A6 FF                  call 0x1406c6c40
00C59011  44 8B C7                        mov r8d, edi
00C59014  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C59018  33 D2                           xor edx, edx
00C5901A  E8 21 DC A6 FF                  call 0x1406c6c40
00C5901F  44 8B C7                        mov r8d, edi
00C59022  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
00C59029  33 D2                           xor edx, edx
00C5902B  E8 10 DC A6 FF                  call 0x1406c6c40
00C59030  48 85 DB                        test rbx, rbx
00C59033  0F 84 C7 04 00 00               je 0x140c59500
00C59039  44 89 2B                        mov dword ptr [rbx], r13d
00C5903C  85 F6                           test esi, esi
00C5903E  74 25                           je 0x140c59065
00C59040  45 33 C9                        xor r9d, r9d
00C59043  45 8D 45 55                     lea r8d, [r13 + 0x55]
00C59047  48 8D 95 00 01 00 00            lea rdx, [rbp + 0x100]
00C5904E  0F B7 CE                        movzx ecx, si
00C59051  41 8D 7D 46                     lea edi, [r13 + 0x46]
00C59055  E8 4E 2A 86 FF                  call 0x1404bbaa8
00C5905A  85 C0                           test eax, eax
00C5905C  75 0C                           jne 0x140c5906a
00C5905E  44 89 6C 24 34                  mov dword ptr [rsp + 0x34], r13d
00C59063  EB 05                           jmp 0x140c5906a
00C59065  BF 26 00 00 00                  mov edi, 0x26
00C5906A  4C 8D 3D 5F 45 3B 00            lea r15, [rip + 0x3b455f]
00C59071  41 8B D6                        mov edx, r14d
00C59074  49 8B CF                        mov rcx, r15
00C59077  4C 8D 05 82 53 02 00            lea r8, [rip + 0x25382]
00C5907E  E8 39 A6 B9 FF                  call 0x1407f36bc
00C59083  BB 01 00 00 00                  mov ebx, 1
00C59088  83 F8 FF                        cmp eax, -1
00C5908B  0F 84 23 01 00 00               je 0x140c591b4
00C59091  84 1D C5 45 3B 00               test byte ptr [rip + 0x3b45c5], bl
00C59097  4C 8D 44 24 38                  lea r8, [rsp + 0x38]
00C5909C  8B D0                           mov edx, eax
00C5909E  49 8B CF                        mov rcx, r15
00C590A1  74 07                           je 0x140c590aa
00C590A3  E8 B8 BB BF FF                  call 0x140854c60
00C590A8  EB 05                           jmp 0x140c590af
00C590AA  E8 01 BC BF FF                  call 0x140854cb0
00C590AF  48 8B F0                        mov rsi, rax
00C590B2  48 85 C0                        test rax, rax
00C590B5  0F 84 F9 00 00 00               je 0x140c591b4
00C590BB  48 8D 15 5E 53 02 00            lea rdx, [rip + 0x2535e]
00C590C2  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00C590C6  E8 B5 16 7D FF                  call 0x14042a780
00C590CB  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C590CF  48 8B D6                        mov rdx, rsi
00C590D2  49 8B CF                        mov rcx, r15
00C590D5  E8 42 BD BE FF                  call 0x140844e1c
00C590DA  8B F0                           mov esi, eax
00C590DC  83 F8 FF                        cmp eax, -1
00C590DF  0F 84 B3 00 00 00               je 0x140c59198
00C590E5  84 1D 71 45 3B 00               test byte ptr [rip + 0x3b4571], bl
00C590EB  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00C590F0  8B D0                           mov edx, eax
00C590F2  49 8B CF                        mov rcx, r15
00C590F5  74 07                           je 0x140c590fe
00C590F7  E8 64 BB BF FF                  call 0x140854c60
00C590FC  EB 05                           jmp 0x140c59103
00C590FE  E8 AD BB BF FF                  call 0x140854cb0
00C59103  48 85 C0                        test rax, rax
00C59106  0F 84 8C 00 00 00               je 0x140c59198
00C5910C  83 78 0C 07                     cmp dword ptr [rax + 0xc], 7
00C59110  75 6A                           jne 0x140c5917c
00C59112  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00C59117  4C 8B C0                        mov r8, rax
00C5911A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C5911F  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00C59124  49 8B CF                        mov rcx, r15
00C59127  8B D6                           mov edx, esi
00C59129  E8 06 A8 B9 FF                  call 0x1407f3934
00C5912E  48 85 C0                        test rax, rax
00C59131  74 49                           je 0x140c5917c
00C59133  81 7C 24 50 A8 00 00 00         cmp dword ptr [rsp + 0x50], 0xa8
00C5913B  73 23                           jae 0x140c59160
00C5913D  44 8B 44 24 50                  mov r8d, dword ptr [rsp + 0x50]
00C59142  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00C59146  48 8B D0                        mov rdx, rax
00C59149  E8 F2 D6 A6 FF                  call 0x1406c6840
00C5914E  33 D2                           xor edx, edx
00C59150  48 8D 4D 50                     lea rcx, [rbp + 0x50]
00C59154  E8 EF A5 86 FF                  call 0x1404c3748
00C59159  66 89 05 10 09 38 00            mov word ptr [rip + 0x380910], ax
00C59160  84 1D F6 44 3B 00               test byte ptr [rip + 0x3b44f6], bl
00C59166  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00C5916B  49 8B CF                        mov rcx, r15
00C5916E  74 07                           je 0x140c59177
00C59170  E8 AB 3A C0 FF                  call 0x14085cc20
00C59175  EB 05                           jmp 0x140c5917c
00C59177  E8 C4 CD BF FF                  call 0x140855f40
00C5917C  84 1D DA 44 3B 00               test byte ptr [rip + 0x3b44da], bl
00C59182  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00C59187  49 8B CF                        mov rcx, r15
00C5918A  74 07                           je 0x140c59193
00C5918C  E8 8F 3A C0 FF                  call 0x14085cc20
00C59191  EB 05                           jmp 0x140c59198
00C59193  E8 A8 CD BF FF                  call 0x140855f40
00C59198  84 1D BE 44 3B 00               test byte ptr [rip + 0x3b44be], bl
00C5919E  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
00C591A3  49 8B CF                        mov rcx, r15
00C591A6  74 07                           je 0x140c591af
00C591A8  E8 73 3A C0 FF                  call 0x14085cc20
00C591AD  EB 05                           jmp 0x140c591b4
00C591AF  E8 8C CD BF FF                  call 0x140855f40
00C591B4  4C 8D 05 25 52 02 00            lea r8, [rip + 0x25225]
00C591BB  41 8B D6                        mov edx, r14d
00C591BE  49 8B CF                        mov rcx, r15
00C591C1  E8 F6 A4 B9 FF                  call 0x1407f36bc
00C591C6  83 F8 FF                        cmp eax, -1
00C591C9  74 28                           je 0x140c591f3
00C591CB  84 1D 8B 44 3B 00               test byte ptr [rip + 0x3b448b], bl
00C591D1  4C 8D 44 24 60                  lea r8, [rsp + 0x60]
00C591D6  8B D0                           mov edx, eax
00C591D8  49 8B CF                        mov rcx, r15
00C591DB  74 07                           je 0x140c591e4
00C591DD  E8 7E BA BF FF                  call 0x140854c60
00C591E2  EB 05                           jmp 0x140c591e9
00C591E4  E8 C7 BA BF FF                  call 0x140854cb0
00C591E9  33 F6                           xor esi, esi
00C591EB  4C 8B E8                        mov r13, rax
00C591EE  48 85 C0                        test rax, rax
00C591F1  75 07                           jne 0x140c591fa
00C591F3  8B C7                           mov eax, edi
00C591F5  E9 0B 03 00 00                  jmp 0x140c59505
00C591FA  83 E7 FD                        and edi, 0xfffffffd
00C591FD  44 8B FE                        mov r15d, esi
00C59200  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00C59205  EB 02                           jmp 0x140c59209
00C59207  33 F6                           xor esi, esi
00C59209  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
00C5920E  45 8B C7                        mov r8d, r15d
00C59211  49 8B D5                        mov rdx, r13
00C59214  48 8D 0D B5 43 3B 00            lea rcx, [rip + 0x3b43b5]
00C5921B  E8 10 37 C0 FF                  call 0x14085c930
00C59220  8B 54 24 68                     mov edx, dword ptr [rsp + 0x68]
00C59224  48 8D 0D A5 43 3B 00            lea rcx, [rip + 0x3b43a5]
00C5922B  44 03 FB                        add r15d, ebx
00C5922E  44 89 7C 24 38                  mov dword ptr [rsp + 0x38], r15d
00C59233  83 FA FF                        cmp edx, -1
00C59236  0F 84 69 02 00 00               je 0x140c594a5
00C5923C  84 1D 1A 44 3B 00               test byte ptr [rip + 0x3b441a], bl
00C59242  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00C59247  74 07                           je 0x140c59250
00C59249  E8 12 BA BF FF                  call 0x140854c60
00C5924E  EB 05                           jmp 0x140c59255
00C59250  E8 5B BA BF FF                  call 0x140854cb0
00C59255  4C 8B F0                        mov r14, rax
00C59258  48 85 C0                        test rax, rax
00C5925B  74 A3                           je 0x140c59200
00C5925D  48 8D 15 7C 11 02 00            lea rdx, [rip + 0x2117c]
00C59264  48 8D 4D 88                     lea rcx, [rbp - 0x78]
00C59268  E8 13 15 7D FF                  call 0x14042a780
00C5926D  4C 8D 45 88                     lea r8, [rbp - 0x78]
00C59271  49 8B D6                        mov rdx, r14
00C59274  48 8D 0D 55 43 3B 00            lea rcx, [rip + 0x3b4355]
00C5927B  E8 9C BB BE FF                  call 0x140844e1c
00C59280  44 8B F8                        mov r15d, eax
00C59283  83 F8 FF                        cmp eax, -1
00C59286  0F 84 E1 01 00 00               je 0x140c5946d
00C5928C  84 1D CA 43 3B 00               test byte ptr [rip + 0x3b43ca], bl
00C59292  4C 8D 44 24 48                  lea r8, [rsp + 0x48]
00C59297  8B D0                           mov edx, eax
00C59299  48 8D 0D 30 43 3B 00            lea rcx, [rip + 0x3b4330]
00C592A0  74 07                           je 0x140c592a9
00C592A2  E8 B9 B9 BF FF                  call 0x140854c60
00C592A7  EB 05                           jmp 0x140c592ae
00C592A9  E8 02 BA BF FF                  call 0x140854cb0
00C592AE  48 85 C0                        test rax, rax
00C592B1  0F 84 B6 01 00 00               je 0x140c5946d
00C592B7  83 78 0C 04                     cmp dword ptr [rax + 0xc], 4
00C592BB  75 55                           jne 0x140c59312
00C592BD  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00C592C2  41 8B D7                        mov edx, r15d
00C592C5  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00C592CA  4C 8D 3D FF 42 3B 00            lea r15, [rip + 0x3b42ff]
00C592D1  49 8B CF                        mov rcx, r15
00C592D4  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
00C592D9  4C 8B C0                        mov r8, rax
00C592DC  E8 53 A6 B9 FF                  call 0x1407f3934
00C592E1  8B 00                           mov eax, dword ptr [rax]
00C592E3  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00C592E7  A8 03                           test al, 3
00C592E9  74 09                           je 0x140c592f4
00C592EB  A8 10                           test al, 0x10
00C592ED  40 0F B6 F6                     movzx esi, sil
00C592F1  0F 45 F3                        cmovne esi, ebx
00C592F4  84 1D 62 43 3B 00               test byte ptr [rip + 0x3b4362], bl
00C592FA  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00C592FF  49 8B CF                        mov rcx, r15
00C59302  74 07                           je 0x140c5930b
00C59304  E8 17 39 C0 FF                  call 0x14085cc20
00C59309  EB 0E                           jmp 0x140c59319
00C5930B  E8 30 CC BF FF                  call 0x140855f40
00C59310  EB 07                           jmp 0x140c59319
00C59312  4C 8D 3D B7 42 3B 00            lea r15, [rip + 0x3b42b7]
00C59319  84 1D 3D 43 3B 00               test byte ptr [rip + 0x3b433d], bl
00C5931F  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00C59324  49 8B CF                        mov rcx, r15
00C59327  74 07                           je 0x140c59330
00C59329  E8 F2 38 C0 FF                  call 0x14085cc20
00C5932E  EB 05                           jmp 0x140c59335
00C59330  E8 0B CC BF FF                  call 0x140855f40
00C59335  40 84 F6                        test sil, sil
00C59338  0F 84 36 01 00 00               je 0x140c59474
00C5933E  41 F6 46 02 20                  test byte ptr [r14 + 2], 0x20
00C59343  41 0F B7 4E 48                  movzx ecx, word ptr [r14 + 0x48]
00C59348  74 29                           je 0x140c59373
00C5934A  0F B7 C1                        movzx eax, cx
00C5934D  66 03 C0                        add ax, ax
00C59350  0F B7 F0                        movzx esi, ax
00C59353  81 FE A8 00 00 00               cmp esi, 0xa8
00C59359  0F 87 15 01 00 00               ja 0x140c59474
00C5935F  44 8B C9                        mov r9d, ecx
00C59362  4D 8D 46 4C                     lea r8, [r14 + 0x4c]
00C59366  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C5936A  8B D6                           mov edx, esi
00C5936C  E8 5F 4D BF FF                  call 0x14084e0d0
00C59371  EB 1F                           jmp 0x140c59392
00C59373  48 8B F1                        mov rsi, rcx
00C59376  81 F9 A8 00 00 00               cmp ecx, 0xa8
00C5937C  0F 87 F2 00 00 00               ja 0x140c59474
00C59382  4C 8B C1                        mov r8, rcx
00C59385  49 8D 56 4C                     lea rdx, [r14 + 0x4c]
00C59389  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C5938D  E8 AE D4 A6 FF                  call 0x1406c6840
00C59392  84 1D C4 42 3B 00               test byte ptr [rip + 0x3b42c4], bl
00C59398  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C5939D  49 8B CF                        mov rcx, r15
00C593A0  74 07                           je 0x140c593a9
00C593A2  E8 79 38 C0 FF                  call 0x14085cc20
00C593A7  EB 05                           jmp 0x140c593ae
00C593A9  E8 92 CB BF FF                  call 0x140855f40
00C593AE  8B C6                           mov eax, esi
00C593B0  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00C593B4  48 3D AA 00 00 00               cmp rax, 0xaa
00C593BA  0F 83 DF 00 00 00               jae 0x140c5949f
00C593C0  45 33 F6                        xor r14d, r14d
00C593C3  48 8D 4D A0                     lea rcx, [rbp - 0x60]
00C593C7  33 D2                           xor edx, edx
00C593C9  66 44 89 74 05 A0               mov word ptr [rbp + rax - 0x60], r14w
00C593CF  E8 74 A3 86 FF                  call 0x1404c3748
00C593D4  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
00C593D9  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00C593DE  0F B7 F0                        movzx esi, ax
00C593E1  85 F6                           test esi, esi
00C593E3  0F 84 1E FE FF FF               je 0x140c59207
00C593E9  83 FE 7F                        cmp esi, 0x7f
00C593EC  0F 84 15 FE FF FF               je 0x140c59207
00C593F2  45 33 FF                        xor r15d, r15d
00C593F5  45 85 F6                        test r14d, r14d
00C593F8  74 22                           je 0x140c5941c
00C593FA  44 38 7C 24 31                  cmp byte ptr [rsp + 0x31], r15b
00C593FF  75 1B                           jne 0x140c5941c
00C59401  48 8D 55 A0                     lea rdx, [rbp - 0x60]
00C59405  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
00C5940C  E8 6F 6C 8A FF                  call 0x140500080
00C59411  85 C0                           test eax, eax
00C59413  75 07                           jne 0x140c5941c
00C59415  88 5C 24 31                     mov byte ptr [rsp + 0x31], bl
00C59419  83 E7 BF                        and edi, 0xffffffbf
00C5941C  44 38 7C 24 30                  cmp byte ptr [rsp + 0x30], r15b
00C59421  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
00C59426  75 25                           jne 0x140c5944d
00C59428  45 84 E4                        test r12b, r12b
00C5942B  0F 85 D6 FD FF FF               jne 0x140c59207
00C59431  F6 44 24 54 02                  test byte ptr [rsp + 0x54], 2
00C59436  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00C5943A  74 08                           je 0x140c59444
00C5943C  44 8A E3                        mov r12b, bl
00C5943F  E9 C3 FD FF FF                  jmp 0x140c59207
00C59444  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
00C59448  E9 BA FD FF FF                  jmp 0x140c59207
00C5944D  45 84 E4                        test r12b, r12b
00C59450  0F 85 B1 FD FF FF               jne 0x140c59207
00C59456  F6 44 24 54 02                  test byte ptr [rsp + 0x54], 2
00C5945B  0F 84 A6 FD FF FF               je 0x140c59207
00C59461  44 8A E3                        mov r12b, bl
00C59464  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00C59468  E9 9A FD FF FF                  jmp 0x140c59207
00C5946D  4C 8D 3D 5C 41 3B 00            lea r15, [rip + 0x3b415c]
00C59474  84 1D E2 41 3B 00               test byte ptr [rip + 0x3b41e2], bl
00C5947A  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
00C5947F  49 8B CF                        mov rcx, r15
00C59482  74 07                           je 0x140c5948b
00C59484  E8 97 37 C0 FF                  call 0x14085cc20
00C59489  EB 05                           jmp 0x140c59490
00C5948B  E8 B0 CA BF FF                  call 0x140855f40
00C59490  44 8B 7C 24 38                  mov r15d, dword ptr [rsp + 0x38]
00C59495  44 8B 74 24 34                  mov r14d, dword ptr [rsp + 0x34]
00C5949A  E9 68 FD FF FF                  jmp 0x140c59207
00C5949F  E8 38 CB 89 FF                  call 0x1404f5fdc
00C594A4  CC                              int3
00C594A5  84 1D B1 41 3B 00               test byte ptr [rip + 0x3b41b1], bl
00C594AB  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00C594B0  74 07                           je 0x140c594b9
00C594B2  E8 69 37 C0 FF                  call 0x14085cc20
00C594B7  EB 05                           jmp 0x140c594be
00C594B9  E8 82 CA BF FF                  call 0x140855f40
00C594BE  40 8A 74 24 30                  mov sil, byte ptr [rsp + 0x30]
00C594C3  33 D2                           xor edx, edx
00C594C5  40 84 F6                        test sil, sil
00C594C8  75 05                           jne 0x140c594cf
00C594CA  45 84 E4                        test r12b, r12b
00C594CD  74 03                           je 0x140c594d2
00C594CF  83 E7 FB                        and edi, 0xfffffffb
00C594D2  38 54 24 31                     cmp byte ptr [rsp + 0x31], dl
00C594D6  74 09                           je 0x140c594e1
00C594D8  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00C594DC  44 89 30                        mov dword ptr [rax], r14d
00C594DF  EB 18                           jmp 0x140c594f9
00C594E1  45 84 E4                        test r12b, r12b
00C594E4  75 09                           jne 0x140c594ef
00C594E6  40 84 F6                        test sil, sil
00C594E9  0F 84 04 FD FF FF               je 0x140c591f3
00C594EF  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
00C594F3  8B 4C 24 58                     mov ecx, dword ptr [rsp + 0x58]
00C594F7  89 08                           mov dword ptr [rax], ecx
00C594F9  8B FA                           mov edi, edx
00C594FB  E9 F3 FC FF FF                  jmp 0x140c591f3
00C59500  B8 01 00 00 00                  mov eax, 1
00C59505  48 8B 8D B0 01 00 00            mov rcx, qword ptr [rbp + 0x1b0]
00C5950C  48 33 CC                        xor rcx, rsp
00C5950F  E8 2C 31 A5 FF                  call 0x1406ac640
00C59514  48 8B 9C 24 00 03 00 00         mov rbx, qword ptr [rsp + 0x300]
00C5951C  48 81 C4 C0 02 00 00            add rsp, 0x2c0
00C59523  41 5F                           pop r15
00C59525  41 5E                           pop r14
00C59527  41 5D                           pop r13
00C59529  41 5C                           pop r12
00C5952B  5F                              pop rdi
00C5952C  5E                              pop rsi
00C5952D  5D                              pop rbp
00C5952E  C3                              ret
00C5952F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSelectQualifiedInstallLanguage(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m27C;
    unsigned int v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned int v_stack_m290;
    unsigned int v_stack_m294;
    unsigned int v_stack_m298;
    unsigned int v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned int v_stack_m2A8;
    unsigned int v_stack_m2AC;
    unsigned int v_stack_m2B0;
    unsigned int v_stack_m2B4;
    unsigned int v_stack_m2B8;
    unsigned int v_stack_m2BC;
    unsigned int v_stack_m2C0;
    unsigned int v_stack_m2C4;
    unsigned __int8 v_stack_m2C7;
    unsigned __int8 v_stack_m2C8;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (704);
    result = (*(unsigned __int64 *)(v_rip + 1775554)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r13 = 0;
    v_stack_m2C4 = a4;
    v_stack_m290 = 0;
    a2 = (unsigned int)((a2) | (0xFFFFFFFFULL));
    v_stack_m2AC = 0;
    v_stack_m2B0 = a2;
    v_stack_m2C0 = a2;
    v_stack_m298 = a2;
    v_stack_m2B8 = a2;
    v_stack_m280 = a2;
    v_stack_m288 = a2;
    a2 = 0;
    v_stack_m278 = a3;
    v_stack_m270 = v_xmm0;
    v_stack_m2BC = 0;
    v_stack_m294 = 0;
    v_stack_m2B4 = 0;
    v_stack_m2C8 = 0;
    v_stack_m2C7 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2A4 = 0;
    v_stack_m2A8 = 0;
    v_stack_m27C = 0;
    v_stack_m284 = 0;
    result = memset(v_stack_m1A8, a2, 170, a4);
    a2 = 0;
    result = memset(v_stack_m258, a2, 170, a4);
    a2 = 0;
    result = memset(v_stack_mF8, a2, 170, a4);
    if (a3 == 0) goto loc_00C59500;
    *(unsigned int *)(a3) = 0;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00C59065;
    a4 = 0;
    result = DownLevelLangIDToLanguageName((unsigned __int16)((unsigned int)(a4)), v_stack_mF8, v_r13 + 85, a4);
    if ((unsigned int)(result) != 0) goto loc_00C5906A;
    v_stack_m2C4 = 0;
    goto loc_00C5906A;
loc_00C59065:
loc_00C5906A:
    result = CmpWalkPath(v_rip + 3884383, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 152450, a4);
    if (((unsigned int)(result)) == -1) goto loc_00C591B4;
    if (((*(unsigned __int8 *)(v_rip + 3884485)) & (1)) == 0) goto loc_00C590AA;
    result = HvpGetCellFlat(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m2C0, a4);
    goto loc_00C590AF;
loc_00C590AA:
    result = HvpGetCellPaged(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m2C0, a4);
loc_00C590AF:
    if (result == 0) goto loc_00C591B4;
    result = RtlInitUnicodeString(v_stack_m270, v_rip + 152414, v_stack_m2C0, a4);
    result = CmpFindValueByName(v_rip + 3884383, result, v_stack_m270, a4);
    if (((unsigned int)(result)) == -1) goto loc_00C59198;
    if (((*(unsigned __int8 *)(v_rip + 3884401)) & (1)) == 0) goto loc_00C590FE;
    result = HvpGetCellFlat(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m2B0, a4);
    goto loc_00C59103;
loc_00C590FE:
    result = HvpGetCellPaged(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m2B0, a4);
loc_00C59103:
    if (result == 0) goto loc_00C59198;
    if ((*(unsigned int *)(result + 12)) != 7) goto loc_00C5917C;
    v_stack_m2D8 = v_stack_m288;
    result = CmpValueToData(v_rip + 3884383, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m2A8);
    if (result == 0) goto loc_00C5917C;
    if (v_stack_m2A8 < 168) {
        a3 = v_stack_m2A8;
        a1 = v_stack_m1A8;
        a2 = result;
        result = memcpy(a1, a2, a3, v_stack_m2A8);
        a2 = 0;
        a1 = v_stack_m1A8;
        result = DownLevelLanguageNameToLangID(a1, a2, a3, v_stack_m2A8);
        *(unsigned __int16 *)(v_rip + 3672336) = (unsigned __int16)(result);
    }
    if (((*(unsigned __int8 *)(v_rip + 3884278)) & (1)) == 0) goto loc_00C59177;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m288, a3, v_stack_m2A8);
    goto loc_00C5917C;
loc_00C59177:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m288, a3, v_stack_m2A8);
loc_00C5917C:
    if (((*(unsigned __int8 *)(v_rip + 3884250)) & (1)) == 0) goto loc_00C59193;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m2B0, a3, v_stack_m2A8);
    goto loc_00C59198;
loc_00C59193:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m2B0, a3, v_stack_m2A8);
loc_00C59198:
    if (((*(unsigned __int8 *)(v_rip + 3884222)) & (1)) == 0) goto loc_00C591AF;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m2C0, a3, v_stack_m2A8);
    goto loc_00C591B4;
loc_00C591AF:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m2C0, a3, v_stack_m2A8);
loc_00C591B4:
    result = CmpWalkPath(v_rip + 3884383, (unsigned int)((unsigned int)((unsigned int)(a2))), v_rip + 152101, v_stack_m2A8);
    if (((unsigned int)(result)) == -1) goto loc_00C591F3;
    if (((*(unsigned __int8 *)(v_rip + 3884171)) & (1)) == 0) goto loc_00C591E4;
    result = HvpGetCellFlat(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m298, v_stack_m2A8);
    goto loc_00C591E9;
loc_00C591E4:
    result = HvpGetCellPaged(v_rip + 3884383, (unsigned int)((unsigned int)(result)), v_stack_m298, v_stack_m2A8);
loc_00C591E9:
    v_rsi = 0;
    if (result != 0) goto loc_00C591FA;
loc_00C591F3:
    goto loc_00C59505;
loc_00C591FA:
    v_rdi = (unsigned int)((38) & (0xFFFFFFFDULL));
loc_00C59200:
    goto loc_00C59209;
loc_00C59207:
    v_rsi = 0;
loc_00C59209:
    result = CmpFindSubKeyByNumber(v_rip + 3883957, result, 0, v_stack_m290);
    v_r15 = (unsigned int)((0) + (1));
    v_stack_m2C0 = (unsigned int)(v_r15);
    if (((unsigned int)((unsigned int)(v_stack_m290))) == -1) goto loc_00C594A5;
    if (((*(unsigned __int8 *)(v_rip + 3884058)) & (1)) == 0) goto loc_00C59250;
    result = HvpGetCellFlat(v_rip + 3883941, (unsigned int)(v_stack_m290), v_stack_m2B8, v_stack_m290);
    goto loc_00C59255;
loc_00C59250:
    result = HvpGetCellPaged(v_rip + 3883941, (unsigned int)(v_stack_m290), v_stack_m2B8, v_stack_m290);
loc_00C59255:
    if (result == 0) goto loc_00C59200;
    result = RtlInitUnicodeString(v_stack_m270, v_rip + 135548, v_stack_m2B8, v_stack_m290);
    result = CmpFindValueByName(v_rip + 3883861, result, v_stack_m270, v_stack_m290);
    if (((unsigned int)(result)) == -1) goto loc_00C5946D;
    if (((*(unsigned __int8 *)(v_rip + 3883978)) & (1)) == 0) goto loc_00C592A9;
    result = HvpGetCellFlat(v_rip + 3883824, (unsigned int)((unsigned int)(result)), v_stack_m2B0, v_stack_m290);
    goto loc_00C592AE;
loc_00C592A9:
    result = HvpGetCellPaged(v_rip + 3883824, (unsigned int)((unsigned int)(result)), v_stack_m2B0, v_stack_m290);
loc_00C592AE:
    if (result == 0) goto loc_00C5946D;
    if ((*(unsigned int *)(result + 12)) != 4) goto loc_00C59312;
    v_stack_m2D8 = v_stack_m280;
    result = CmpValueToData(v_rip + 3883775, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), result, v_stack_m2A8);
    v_stack_m2A4 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (3)) != 0) {
        v_rsi = 0;
        if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result)))) & (16)) != 0) { v_rsi = 1; }
    }
    if (((*(unsigned __int8 *)(v_rip + 3883874)) & (1)) == 0) goto loc_00C5930B;
    result = HvpReleaseCellFlat(v_rip + 3883775, v_stack_m280, result, v_stack_m2A8);
    goto loc_00C59319;
loc_00C5930B:
    result = HvpReleaseCellPaged(v_rip + 3883775, v_stack_m280, result, v_stack_m2A8);
    goto loc_00C59319;
loc_00C59312:
loc_00C59319:
    if (((*(unsigned __int8 *)(v_rip + 3883837)) & (1)) == 0) goto loc_00C59330;
    result = HvpReleaseCellFlat(v_rip + 3883703, v_stack_m2B0, result, v_stack_m2A8);
    goto loc_00C59335;
loc_00C59330:
    result = HvpReleaseCellPaged(v_rip + 3883703, v_stack_m2B0, result, v_stack_m2A8);
loc_00C59335:
    if ((unsigned __int8)(v_rsi) == 0) goto loc_00C59474;
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_00C59373;
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(result + 72))) + ((unsigned __int16)((unsigned __int16)(*(unsigned __int16 *)(result + 72)))));
    if (((unsigned int)((unsigned __int16)(result))) > 168) goto loc_00C59474;
    result = CmpCopyCompressedName(v_stack_m258, (unsigned int)((unsigned int)((unsigned __int16)(result))), result + 76, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    goto loc_00C59392;
loc_00C59373:
    if (((unsigned int)(v_stack_m258)) > 168) goto loc_00C59474;
    result = memcpy(v_stack_m258, result + 76, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
loc_00C59392:
    if (((*(unsigned __int8 *)(v_rip + 3883716)) & (1)) == 0) goto loc_00C593A9;
    result = HvpReleaseCellFlat(v_rip + 3883703, v_stack_m2B8, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    goto loc_00C593AE;
loc_00C593A9:
    result = HvpReleaseCellPaged(v_rip + 3883703, v_stack_m2B8, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
loc_00C593AE:
    result = ((unsigned int)((unsigned int)(v_stack_m258))) & (-2);
    if (result >= 170) goto loc_00C5949F;
    v_r14 = 0;
    a2 = 0;
    *(unsigned __int16 *)(v_stack_m1F8 + result * 1 - 96) = 0;
    result = DownLevelLanguageNameToLangID(v_stack_m258, a2, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    if ((unsigned int)((unsigned __int16)(result)) == 0) goto loc_00C59207;
    if (((unsigned int)((unsigned __int16)(result))) == 127) goto loc_00C59207;
    v_r15 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m2C4)) == 0) goto loc_00C5941C;
    if (v_stack_m2C7 != 0) goto loc_00C5941C;
    result = wcsicmp(v_stack_mF8, v_stack_m258, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    if ((unsigned int)(result) == 0) {
        v_stack_m2C7 = 1;
        v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFBFULL));
    }
    if (v_stack_m2C8 != 0) goto loc_00C5944D;
    if (0 != 0) goto loc_00C59207;
    v_stack_m2A0 = (unsigned int)((unsigned __int16)(result));
    if (((v_stack_m2A4) & (2)) == 0) goto loc_00C59444;
    goto loc_00C59207;
loc_00C59444:
    v_stack_m2C8 = 1;
    goto loc_00C59207;
loc_00C5944D:
    if (1 != 0) goto loc_00C59207;
    if (((v_stack_m2A4) & (2)) == 0) goto loc_00C59207;
    v_stack_m2A0 = (unsigned int)((unsigned __int16)(result));
    goto loc_00C59207;
loc_00C5946D:
loc_00C59474:
    if (((*(unsigned __int8 *)(v_rip + 3883490)) & (1)) == 0) goto loc_00C5948B;
    result = HvpReleaseCellFlat(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    goto loc_00C59490;
loc_00C5948B:
    result = HvpReleaseCellPaged(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
loc_00C59490:
    goto loc_00C59207;
loc_00C5949F:
    result = _report_rangecheckfailure(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
loc_00C594A5:
    if (((*(unsigned __int8 *)(v_rip + 3883441)) & (1)) == 0) goto loc_00C594B9;
    result = HvpReleaseCellFlat(v_rip + 3883356, v_stack_m298, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    goto loc_00C594BE;
loc_00C594B9:
    result = HvpReleaseCellPaged(v_rip + 3883356, v_stack_m298, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
loc_00C594BE:
    a2 = 0;
    if ((unsigned __int8)(v_stack_m2C8) != 0) goto loc_00C594CF;
    if (1 != 0) {
        v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFBULL));
    }
    if (v_stack_m2C7 == 0) goto loc_00C594E1;
    *(unsigned int *)(v_stack_m278) = (unsigned int)((unsigned int)(v_stack_m2C4));
    goto loc_00C594F9;
loc_00C594E1:
    if (1 != 0) goto loc_00C594EF;
    if ((unsigned __int8)(v_stack_m2C8) == 0) goto loc_00C591F3;
loc_00C594EF:
    *(unsigned int *)(v_stack_m278) = (unsigned int)((unsigned int)(v_stack_m2A0));
loc_00C594F9:
    goto loc_00C591F3;
loc_00C59500:
loc_00C59505:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m258, (unsigned int)((unsigned int)(*(unsigned __int16 *)(result + 72))));
    v_rsp = (v_rsp) + (704);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSelectQualifiedInstallLanguage(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m258;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m27C;
    uint32_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint32_t v_stack_m290;
    uint32_t v_stack_m294;
    uint32_t v_stack_m298;
    uint32_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint32_t v_stack_m2A8;
    uint32_t v_stack_m2AC;
    uint32_t v_stack_m2B0;
    uint32_t v_stack_m2B4;
    uint32_t v_stack_m2B8;
    uint32_t v_stack_m2BC;
    uint32_t v_stack_m2C0;
    uint32_t v_stack_m2C4;
    uint8_t v_stack_m2C7;
    uint8_t v_stack_m2C8;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m48;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (704);
    result = (*(uint64_t *)(v_rip + 0x1B17C2)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r13 = 0;
    v_stack_m2C4 = Arg4;
    v_stack_m290 = 0;
    Arg2 = (uint32_t)((Arg2) | (0xFFFFFFFFULL));
    v_stack_m2AC = 0;
    v_stack_m2B0 = Arg2;
    v_stack_m2C0 = Arg2;
    v_stack_m298 = Arg2;
    v_stack_m2B8 = Arg2;
    v_stack_m280 = Arg2;
    v_stack_m288 = Arg2;
    Arg2 = 0;
    v_stack_m278 = Arg3;
    v_stack_m270 = v_xmm0;
    v_stack_m2BC = 0;
    v_stack_m294 = 0;
    v_stack_m2B4 = 0;
    v_stack_m2C8 = 0;
    v_stack_m2C7 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2A4 = 0;
    v_stack_m2A8 = 0;
    v_stack_m27C = 0;
    v_stack_m284 = 0;
    result = memset(v_stack_m1A8, Arg2, 170, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m258, Arg2, 170, Arg4);
    Arg2 = 0;
    result = memset(v_stack_mF8, Arg2, 170, Arg4);
    if (Arg3 == 0) goto loc_00C59500;
    *(uint32_t *)(Arg3) = 0;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00C59065;
    Arg4 = 0;
    result = DownLevelLangIDToLanguageName((uint16_t)((uint32_t)(Arg4)), v_stack_mF8, local_r13 + 85, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00C5906A;
    v_stack_m2C4 = 0;
    goto loc_00C5906A;
loc_00C59065:
loc_00C5906A:
    result = CmpWalkPath(v_rip + 3884383, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 152450, Arg4);
    if (((uint32_t)(result)) == -1) goto loc_00C591B4;
    if (((*(uint8_t *)(v_rip + 0x3B45C5)) & (1)) == 0) goto loc_00C590AA;
    result = HvpGetCellFlat(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m2C0, Arg4);
    goto loc_00C590AF;
loc_00C590AA:
    result = HvpGetCellPaged(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m2C0, Arg4);
loc_00C590AF:
    if (result == 0) goto loc_00C591B4;
    result = RtlInitUnicodeString(v_stack_m270, v_rip + 152414, v_stack_m2C0, Arg4);
    result = CmpFindValueByName(v_rip + 3884383, result, v_stack_m270, Arg4);
    if (((uint32_t)(result)) == -1) goto loc_00C59198;
    if (((*(uint8_t *)(v_rip + 0x3B4571)) & (1)) == 0) goto loc_00C590FE;
    result = HvpGetCellFlat(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m2B0, Arg4);
    goto loc_00C59103;
loc_00C590FE:
    result = HvpGetCellPaged(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m2B0, Arg4);
loc_00C59103:
    if (result == 0) goto loc_00C59198;
    if ((*(uint32_t *)(result + 0xC)) != 7) goto loc_00C5917C;
    v_stack_m2D8 = v_stack_m288;
    result = CmpValueToData(v_rip + 3884383, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m2A8);
    if (result == 0) goto loc_00C5917C;
    if (v_stack_m2A8 < 168) {
        Arg3 = v_stack_m2A8;
        Arg1 = v_stack_m1A8;
        Arg2 = result;
        result = memcpy(Arg1, Arg2, Arg3, v_stack_m2A8);
        Arg2 = 0;
        Arg1 = v_stack_m1A8;
        result = DownLevelLanguageNameToLangID(Arg1, Arg2, Arg3, v_stack_m2A8);
        *(uint16_t *)(v_rip + 0x380910) = (uint16_t)(result);
    }
    if (((*(uint8_t *)(v_rip + 0x3B44F6)) & (1)) == 0) goto loc_00C59177;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m288, Arg3, v_stack_m2A8);
    goto loc_00C5917C;
loc_00C59177:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m288, Arg3, v_stack_m2A8);
loc_00C5917C:
    if (((*(uint8_t *)(v_rip + 0x3B44DA)) & (1)) == 0) goto loc_00C59193;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m2B0, Arg3, v_stack_m2A8);
    goto loc_00C59198;
loc_00C59193:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m2B0, Arg3, v_stack_m2A8);
loc_00C59198:
    if (((*(uint8_t *)(v_rip + 0x3B44BE)) & (1)) == 0) goto loc_00C591AF;
    result = HvpReleaseCellFlat(v_rip + 3884383, v_stack_m2C0, Arg3, v_stack_m2A8);
    goto loc_00C591B4;
loc_00C591AF:
    result = HvpReleaseCellPaged(v_rip + 3884383, v_stack_m2C0, Arg3, v_stack_m2A8);
loc_00C591B4:
    result = CmpWalkPath(v_rip + 3884383, (uint32_t)((uint32_t)((uint32_t)(Arg2))), v_rip + 152101, v_stack_m2A8);
    if (((uint32_t)(result)) == -1) goto loc_00C591F3;
    if (((*(uint8_t *)(v_rip + 0x3B448B)) & (1)) == 0) goto loc_00C591E4;
    result = HvpGetCellFlat(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m298, v_stack_m2A8);
    goto loc_00C591E9;
loc_00C591E4:
    result = HvpGetCellPaged(v_rip + 3884383, (uint32_t)((uint32_t)(result)), v_stack_m298, v_stack_m2A8);
loc_00C591E9:
    local_rsi = 0;
    if (result != 0) goto loc_00C591FA;
loc_00C591F3:
    goto loc_00C59505;
loc_00C591FA:
    local_rdi = (uint32_t)((38) & (0xFFFFFFFDULL));
loc_00C59200:
    goto loc_00C59209;
loc_00C59207:
    local_rsi = 0;
loc_00C59209:
    result = CmpFindSubKeyByNumber(v_rip + 3883957, result, 0, v_stack_m290);
    local_r15 = (uint32_t)((0) + (1));
    v_stack_m2C0 = (uint32_t)(local_r15);
    if (((uint32_t)((uint32_t)(v_stack_m290))) == -1) goto loc_00C594A5;
    if (((*(uint8_t *)(v_rip + 0x3B441A)) & (1)) == 0) goto loc_00C59250;
    result = HvpGetCellFlat(v_rip + 3883941, (uint32_t)(v_stack_m290), v_stack_m2B8, v_stack_m290);
    goto loc_00C59255;
loc_00C59250:
    result = HvpGetCellPaged(v_rip + 3883941, (uint32_t)(v_stack_m290), v_stack_m2B8, v_stack_m290);
loc_00C59255:
    if (result == 0) goto loc_00C59200;
    result = RtlInitUnicodeString(v_stack_m270, v_rip + 135548, v_stack_m2B8, v_stack_m290);
    result = CmpFindValueByName(v_rip + 3883861, result, v_stack_m270, v_stack_m290);
    if (((uint32_t)(result)) == -1) goto loc_00C5946D;
    if (((*(uint8_t *)(v_rip + 0x3B43CA)) & (1)) == 0) goto loc_00C592A9;
    result = HvpGetCellFlat(v_rip + 3883824, (uint32_t)((uint32_t)(result)), v_stack_m2B0, v_stack_m290);
    goto loc_00C592AE;
loc_00C592A9:
    result = HvpGetCellPaged(v_rip + 3883824, (uint32_t)((uint32_t)(result)), v_stack_m2B0, v_stack_m290);
loc_00C592AE:
    if (result == 0) goto loc_00C5946D;
    if ((*(uint32_t *)(result + 0xC)) != 4) goto loc_00C59312;
    v_stack_m2D8 = v_stack_m280;
    result = CmpValueToData(v_rip + 3883775, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), result, v_stack_m2A8);
    v_stack_m2A4 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (3)) != 0) {
        local_rsi = 0;
        if ((((uint8_t)((uint32_t)(*(uint32_t *)(result)))) & (16)) != 0) { local_rsi = 1; }
    }
    if (((*(uint8_t *)(v_rip + 0x3B4362)) & (1)) == 0) goto loc_00C5930B;
    result = HvpReleaseCellFlat(v_rip + 3883775, v_stack_m280, result, v_stack_m2A8);
    goto loc_00C59319;
loc_00C5930B:
    result = HvpReleaseCellPaged(v_rip + 3883775, v_stack_m280, result, v_stack_m2A8);
    goto loc_00C59319;
loc_00C59312:
loc_00C59319:
    if (((*(uint8_t *)(v_rip + 0x3B433D)) & (1)) == 0) goto loc_00C59330;
    result = HvpReleaseCellFlat(v_rip + 3883703, v_stack_m2B0, result, v_stack_m2A8);
    goto loc_00C59335;
loc_00C59330:
    result = HvpReleaseCellPaged(v_rip + 3883703, v_stack_m2B0, result, v_stack_m2A8);
loc_00C59335:
    if ((uint8_t)(local_rsi) == 0) goto loc_00C59474;
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_00C59373;
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(result + 0x48))) + ((uint16_t)((uint16_t)(*(uint16_t *)(result + 0x48)))));
    if (((uint32_t)((uint16_t)(result))) > 168) goto loc_00C59474;
    result = CmpCopyCompressedName(v_stack_m258, (uint32_t)((uint32_t)((uint16_t)(result))), result + 76, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    goto loc_00C59392;
loc_00C59373:
    if (((uint32_t)(v_stack_m258)) > 168) goto loc_00C59474;
    result = memcpy(v_stack_m258, result + 76, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
loc_00C59392:
    if (((*(uint8_t *)(v_rip + 0x3B42C4)) & (1)) == 0) goto loc_00C593A9;
    result = HvpReleaseCellFlat(v_rip + 3883703, v_stack_m2B8, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    goto loc_00C593AE;
loc_00C593A9:
    result = HvpReleaseCellPaged(v_rip + 3883703, v_stack_m2B8, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
loc_00C593AE:
    result = ((uint32_t)((uint32_t)(v_stack_m258))) & (-2);
    if (result >= 170) goto loc_00C5949F;
    local_r14 = 0;
    Arg2 = 0;
    *(uint16_t *)(v_stack_m1F8 + result * 1 - 0x60) = 0;
    result = DownLevelLanguageNameToLangID(v_stack_m258, Arg2, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    if ((uint32_t)((uint16_t)(result)) == 0) goto loc_00C59207;
    if (((uint32_t)((uint16_t)(result))) == 127) goto loc_00C59207;
    local_r15 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m2C4)) == 0) goto loc_00C5941C;
    if (v_stack_m2C7 != 0) goto loc_00C5941C;
    result = wcsicmp(v_stack_mF8, v_stack_m258, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    if ((uint32_t)(result) == 0) {
        v_stack_m2C7 = 1;
        local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFBFULL));
    }
    if (v_stack_m2C8 != 0) goto loc_00C5944D;
    if (0 != 0) goto loc_00C59207;
    v_stack_m2A0 = (uint32_t)((uint16_t)(result));
    if (((v_stack_m2A4) & (2)) == 0) goto loc_00C59444;
    goto loc_00C59207;
loc_00C59444:
    v_stack_m2C8 = 1;
    goto loc_00C59207;
loc_00C5944D:
    if (1 != 0) goto loc_00C59207;
    if (((v_stack_m2A4) & (2)) == 0) goto loc_00C59207;
    v_stack_m2A0 = (uint32_t)((uint16_t)(result));
    goto loc_00C59207;
loc_00C5946D:
loc_00C59474:
    if (((*(uint8_t *)(v_rip + 0x3B41E2)) & (1)) == 0) goto loc_00C5948B;
    result = HvpReleaseCellFlat(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    goto loc_00C59490;
loc_00C5948B:
    result = HvpReleaseCellPaged(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
loc_00C59490:
    goto loc_00C59207;
loc_00C5949F:
    result = _report_rangecheckfailure(v_rip + 3883356, v_stack_m2B8, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
loc_00C594A5:
    if (((*(uint8_t *)(v_rip + 0x3B41B1)) & (1)) == 0) goto loc_00C594B9;
    result = HvpReleaseCellFlat(v_rip + 3883356, v_stack_m298, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    goto loc_00C594BE;
loc_00C594B9:
    result = HvpReleaseCellPaged(v_rip + 3883356, v_stack_m298, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
loc_00C594BE:
    Arg2 = 0;
    if ((uint8_t)(v_stack_m2C8) != 0) goto loc_00C594CF;
    if (1 != 0) {
        local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFBULL));
    }
    if (v_stack_m2C7 == 0) goto loc_00C594E1;
    *(uint32_t *)(v_stack_m278) = (uint32_t)((uint32_t)(v_stack_m2C4));
    goto loc_00C594F9;
loc_00C594E1:
    if (1 != 0) goto loc_00C594EF;
    if ((uint8_t)(v_stack_m2C8) == 0) goto loc_00C591F3;
loc_00C594EF:
    *(uint32_t *)(v_stack_m278) = (uint32_t)((uint32_t)(v_stack_m2A0));
loc_00C594F9:
    goto loc_00C591F3;
loc_00C59500:
loc_00C59505:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m258, (uint32_t)((uint32_t)(*(uint16_t *)(result + 0x48))));
    local_rsp = (local_rsp) + (704);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C58F58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
