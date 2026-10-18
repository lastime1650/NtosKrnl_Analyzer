# PpmParkComputeUnparkMaskEx

- RVA: `0x005E05E0`–`0x005E143D` (길이 `3,677` bytes)
- VA: `0x00000001405E05E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CD9B0`
- 디코드: `881`개 명령, `3,677/3,677` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **108**; 고유 호출 대상: **25**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **14**

### Outgoing calls
- `0x005E0665` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0773` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E078D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E07B0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E07CC` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E07F0` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E080E` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E082F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0852` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E087C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E089F` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E08C2` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E08E9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0906` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0927` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0951` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E095B` → [Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline](../5D/Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline_function_005DFB8C.md) (function, `0x005DFB8C`)
- `0x005E0981` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E09B0` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E09D3` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E09E6` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0A02` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0A70` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005E0A9A` → [PpmEventParkNodePreferenceEx](../5D/PpmEventParkNodePreferenceEx_function_005DE8D8.md) (function, `0x005DE8D8`)
- `0x005E0AB4` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0ADC` → [KiOrAffinityEx](../39/KiOrAffinityEx_function_0039A84C.md) (function, `0x0039A84C`)
- `0x005E0AEF` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B02` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B13` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B23` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B33` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B43` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0B53` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0B62` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0B84` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0BA1` → [Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline](../5D/Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline_function_005DFB8C.md) (function, `0x005DFB8C`)
- `0x005E0BBD` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0BE6` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0BF4` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0C0E` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0C28` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0C46` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0C5D` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0C7C` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0C91` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0CA2` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0CB3` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0CC3` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0CE7` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E0D02` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0D0A` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E0D28` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0D84` → [PpmHeteroRestrictToFavoredClassEx](../4E/PpmHeteroRestrictToFavoredClassEx_function_004EF940.md) (function, `0x004EF940`)
- `0x005E0D9A` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E0DD0` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E0DED` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E0E00` → [PpmEventHeteroFavoredCoreRotationChange](../47/PpmEventHeteroFavoredCoreRotationChange_function_0047ACB0.md) (function, `0x0047ACB0`)
- `0x005E0E13` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E0E1B` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E0E3B` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0E58` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0E60` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E0E7E` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0EA7` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E0EBA` → [KeFindFirstSetRightAffinityEx](../47/KeFindFirstSetRightAffinityEx_function_004701E0.md) (function, `0x004701E0`)
- `0x005E0EC1` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x005E0EDB` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E0F0D` → [KeAddGroupAffinityEx](../25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x005E0F1C` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E0F3D` → [KeOrAffinityEx2](../2C/KeOrAffinityEx2_function_002CF930.md) (function, `0x002CF930`)
- `0x005E0F54` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E0F88` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E0FA8` → [KeFindFirstSetRightAffinityEx](../47/KeFindFirstSetRightAffinityEx_function_004701E0.md) (function, `0x004701E0`)
- `0x005E0FD7` → [KeRemoveProcessorAffinityEx](../30/KeRemoveProcessorAffinityEx_function_00304E10.md) (function, `0x00304E10`)
- `0x005E0FE3` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E104C` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E108E` → [KeEnumerateNextProcessor](../41/KeEnumerateNextProcessor_function_00415480.md) (function, `0x00415480`)
- `0x005E10AB` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E10BF` → [KeCountSetBitsAffinityEx](../2C/KeCountSetBitsAffinityEx_function_002CE6E0.md) (function, `0x002CE6E0`)
- `0x005E112C` → [PpmEventTraceCoreParkingSelectionEx](../4F/PpmEventTraceCoreParkingSelectionEx_function_004F09D0.md) (function, `0x004F09D0`)
- `0x005E1144` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E115C` → [KeSubtractAffinityEx2](../2D/KeSubtractAffinityEx2_function_002D5BA0.md) (function, `0x002D5BA0`)
- `0x005E1170` → [KeGetTopologySiblingAffinityForProcessor](../4A/KeGetTopologySiblingAffinityForProcessor_function_004A946C.md) (function, `0x004A946C`)
- `0x005E11A1` → [KiSubtractAffinityEx](../2D/KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)
- `0x005E11BD` → [KiComplementAffinityEx](../3C/KiComplementAffinityEx_function_003C05E0.md) (function, `0x003C05E0`)
- `0x005E11D0` → [PpmParkBuildTopologyCandidatesEx](../4F/PpmParkBuildTopologyCandidatesEx_function_004F3038.md) (function, `0x004F3038`)
- `0x005E11E9` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E1206` → [KeGetTopologySiblingAffinityForProcessor](../4A/KeGetTopologySiblingAffinityForProcessor_function_004A946C.md) (function, `0x004A946C`)
- `0x005E1237` → [KiSubtractAffinityEx](../2D/KiSubtractAffinityEx_function_002D61E8.md) (function, `0x002D61E8`)
- `0x005E1253` → [KiComplementAffinityEx](../3C/KiComplementAffinityEx_function_003C05E0.md) (function, `0x003C05E0`)
- `0x005E1266` → [PpmParkBuildTopologyCandidatesEx](../4F/PpmParkBuildTopologyCandidatesEx_function_004F3038.md) (function, `0x004F3038`)
- `0x005E1282` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x005E12E2` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E12F2` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E1302` → [KeIsEmptyAffinityEx](../2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x005E1319` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E1333` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E135A` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E136E` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E1388` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E13A6` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E13B2` → [KiAndAffinityExNoResult](../2C/KiAndAffinityExNoResult_function_002CF84C.md) (function, `0x002CF84C`)
- `0x005E13C1` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E13CD` → [KiAndAffinityExNoResult](../2C/KiAndAffinityExNoResult_function_002CF84C.md) (function, `0x002CF84C`)
- `0x005E13DC` → [KeAndAffinityEx2](../3C/KeAndAffinityEx2_function_003C0740.md) (function, `0x003C0740`)
- `0x005E13EC` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E140D` → [KiCopyAffinityEx](../2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x005E141C` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PpmParkCalculateCoreParkingMaskEx](../5D/PpmParkCalculateCoreParkingMaskEx_function_005DFBE0.md) at `0x005E0415`

### Static image references
- `0x005E05FF` → RVA `0x00E0A740` (`.data`; read)
- `0x005E066A` → RVA `0x00E08380` (`.data`; read)
- `0x005E0674` → RVA `0x00F0CE0C` (`.data`; read)
- `0x005E06BE` → RVA `0x00E67A80` (`.data`; read)
- `0x005E0964` → RVA `0x00FC501C` (`ALMOSTRO`; read)
- `0x005E0A2C` → RVA `0x00F0E280` (`.data`; read)
- `0x005E0A47` → RVA `0x00F0B260` (`.data`; read)
- `0x005E0D2D` → RVA `0x00FC6B40` (`ALMOSTRO`; read)
- `0x005E0EE6` → RVA `0x00F083C1` (`.data`; read)
- `0x005E0F59` → RVA `0x00F083C8` (`.data`; read)
- `0x005E0F6D` → RVA `0x00F083B8` (`.data`; read)
- `0x005E0FAF` → RVA `0x00F083B0` (`.data`; read)
- `0x005E0FC1` → RVA `0x00F083C0` (`.data`; write)
- `0x005E0FD1` → RVA `0x00F083B0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E05E0  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
005E05E5  55                              push rbp
005E05E6  56                              push rsi
005E05E7  57                              push rdi
005E05E8  41 54                           push r12
005E05EA  41 55                           push r13
005E05EC  41 56                           push r14
005E05EE  41 57                           push r15
005E05F0  48 8D AC 24 50 FE FF FF         lea rbp, [rsp - 0x1b0]
005E05F8  48 81 EC B0 02 00 00            sub rsp, 0x2b0
005E05FF  48 8B 05 3A A1 82 00            mov rax, qword ptr [rip + 0x82a13a]
005E0606  48 33 C4                        xor rax, rsp
005E0609  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
005E0610  48 8B 85 20 02 00 00            mov rax, qword ptr [rbp + 0x220]
005E0617  48 8B D9                        mov rbx, rcx
005E061A  48 8B BD 40 02 00 00            mov rdi, qword ptr [rbp + 0x240]
005E0621  48 8B B5 30 02 00 00            mov rsi, qword ptr [rbp + 0x230]
005E0628  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
005E062C  48 8B 85 28 02 00 00            mov rax, qword ptr [rbp + 0x228]
005E0633  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
005E0637  48 8B 85 38 02 00 00            mov rax, qword ptr [rbp + 0x238]
005E063E  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
005E0642  41 B8 00 01 00 00               mov r8d, 0x100
005E0648  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
005E064C  33 D2                           xor edx, edx
005E064E  48 89 4D E8                     mov qword ptr [rbp - 0x18], rcx
005E0652  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
005E0659  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
005E065D  4C 89 4D 30                     mov qword ptr [rbp + 0x30], r9
005E0661  48 89 7D 60                     mov qword ptr [rbp + 0x60], rdi
005E0665  E8 D6 65 0E 00                  call 0x1406c6c40
005E066A  48 8B 0D 0F 7D 82 00            mov rcx, qword ptr [rip + 0x827d0f]
005E0671  45 33 C0                        xor r8d, r8d
005E0674  48 63 05 91 C7 92 00            movsxd rax, dword ptr [rip + 0x92c791]
005E067B  45 8B F8                        mov r15d, r8d
005E067E  48 69 C0 E8 01 00 00            imul rax, rax, 0x1e8
005E0685  44 89 45 02                     mov dword ptr [rbp + 2], r8d
005E0689  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
005E068D  66 44 89 45 06                  mov word ptr [rbp + 6], r8w
005E0692  44 89 45 88                     mov dword ptr [rbp - 0x78], r8d
005E0696  41 B8 00 01 00 00               mov r8d, 0x100
005E069C  8A 94 08 F0 01 00 00            mov dl, byte ptr [rax + rcx + 0x1f0]
005E06A3  8A 84 08 F1 01 00 00            mov al, byte ptr [rax + rcx + 0x1f1]
005E06AA  88 45 82                        mov byte ptr [rbp - 0x7e], al
005E06AD  0F B7 83 E4 04 00 00            movzx eax, word ptr [rbx + 0x4e4]
005E06B4  89 45 08                        mov dword ptr [rbp + 8], eax
005E06B7  48 8B 83 E8 04 00 00            mov rax, qword ptr [rbx + 0x4e8]
005E06BE  48 8B 1D BB 73 88 00            mov rbx, qword ptr [rip + 0x8873bb]
005E06C5  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
005E06C9  48 89 4D C0                     mov qword ptr [rbp - 0x40], rcx
005E06CD  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
005E06D4  88 55 83                        mov byte ptr [rbp - 0x7d], dl
005E06D7  33 D2                           xor edx, edx
005E06D9  48 8D 83 48 09 00 00            lea rax, [rbx + 0x948]
005E06E0  48 C7 85 90 00 00 00 01 00 20 00  mov qword ptr [rbp + 0x90], 0x200001
005E06EB  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
005E06EF  4C 8D B3 58 0B 00 00            lea r14, [rbx + 0xb58]
005E06F6  48 8D 83 50 0A 00 00            lea rax, [rbx + 0xa50]
005E06FD  4C 89 75 68                     mov qword ptr [rbp + 0x68], r14
005E0701  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
005E0705  4C 8D A3 70 0E 00 00            lea r12, [rbx + 0xe70]
005E070C  48 8D 83 60 0C 00 00            lea rax, [rbx + 0xc60]
005E0713  4C 89 65 28                     mov qword ptr [rbp + 0x28], r12
005E0717  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
005E071B  4C 8D AB B0 16 00 00            lea r13, [rbx + 0x16b0]
005E0722  48 8D 83 78 0F 00 00            lea rax, [rbx + 0xf78]
005E0729  4C 89 6D 70                     mov qword ptr [rbp + 0x70], r13
005E072D  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
005E0731  48 8D 83 80 10 00 00            lea rax, [rbx + 0x1080]
005E0738  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
005E073C  48 8D 83 90 12 00 00            lea rax, [rbx + 0x1290]
005E0743  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
005E0747  48 8D 83 98 13 00 00            lea rax, [rbx + 0x1398]
005E074E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
005E0752  48 8D 83 A0 14 00 00            lea rax, [rbx + 0x14a0]
005E0759  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
005E075D  48 8D 83 A8 15 00 00            lea rax, [rbx + 0x15a8]
005E0764  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
005E0768  48 8D 83 B8 17 00 00            lea rax, [rbx + 0x17b8]
005E076F  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
005E0773  E8 C8 64 0E 00                  call 0x1406c6c40
005E0778  48 8D 83 48 09 00 00            lea rax, [rbx + 0x948]
005E077F  33 D2                           xor edx, edx
005E0781  44 0F B7 00                     movzx r8d, word ptr [rax]
005E0785  48 8D 48 08                     lea rcx, [rax + 8]
005E0789  49 C1 E0 03                     shl r8, 3
005E078D  E8 AE 64 0E 00                  call 0x1406c6c40
005E0792  48 8D 83 50 0A 00 00            lea rax, [rbx + 0xa50]
005E0799  66 C7 83 48 09 00 00 01 00      mov word ptr [rbx + 0x948], 1
005E07A2  44 0F B7 00                     movzx r8d, word ptr [rax]
005E07A6  48 8D 48 08                     lea rcx, [rax + 8]
005E07AA  49 C1 E0 03                     shl r8, 3
005E07AE  33 D2                           xor edx, edx
005E07B0  E8 8B 64 0E 00                  call 0x1406c6c40
005E07B5  66 C7 83 50 0A 00 00 01 00      mov word ptr [rbx + 0xa50], 1
005E07BE  49 8D 4E 08                     lea rcx, [r14 + 8]
005E07C2  45 0F B7 06                     movzx r8d, word ptr [r14]
005E07C6  33 D2                           xor edx, edx
005E07C8  49 C1 E0 03                     shl r8, 3
005E07CC  E8 6F 64 0E 00                  call 0x1406c6c40
005E07D1  48 8D 83 60 0C 00 00            lea rax, [rbx + 0xc60]
005E07D8  66 41 C7 06 01 00               mov word ptr [r14], 1
005E07DE  44 0F B7 00                     movzx r8d, word ptr [rax]
005E07E2  48 8D 48 08                     lea rcx, [rax + 8]
005E07E6  49 C1 E0 03                     shl r8, 3
005E07EA  33 D2                           xor edx, edx
005E07EC  48 89 4D 78                     mov qword ptr [rbp + 0x78], rcx
005E07F0  E8 4B 64 0E 00                  call 0x1406c6c40
005E07F5  66 C7 83 60 0C 00 00 01 00      mov word ptr [rbx + 0xc60], 1
005E07FE  49 8D 4C 24 08                  lea rcx, [r12 + 8]
005E0803  45 0F B7 04 24                  movzx r8d, word ptr [r12]
005E0808  33 D2                           xor edx, edx
005E080A  49 C1 E0 03                     shl r8, 3
005E080E  E8 2D 64 0E 00                  call 0x1406c6c40
005E0813  48 8D 83 78 0F 00 00            lea rax, [rbx + 0xf78]
005E081A  66 41 C7 04 24 01 00            mov word ptr [r12], 1
005E0821  44 0F B7 00                     movzx r8d, word ptr [rax]
005E0825  48 8D 48 08                     lea rcx, [rax + 8]
005E0829  49 C1 E0 03                     shl r8, 3
005E082D  33 D2                           xor edx, edx
005E082F  E8 0C 64 0E 00                  call 0x1406c6c40
005E0834  48 8D 83 80 10 00 00            lea rax, [rbx + 0x1080]
005E083B  66 C7 83 78 0F 00 00 01 00      mov word ptr [rbx + 0xf78], 1
005E0844  44 0F B7 00                     movzx r8d, word ptr [rax]
005E0848  48 8D 48 08                     lea rcx, [rax + 8]
005E084C  49 C1 E0 03                     shl r8, 3
005E0850  33 D2                           xor edx, edx
005E0852  E8 E9 63 0E 00                  call 0x1406c6c40
005E0857  48 8D 83 90 12 00 00            lea rax, [rbx + 0x1290]
005E085E  66 C7 83 80 10 00 00 01 00      mov word ptr [rbx + 0x1080], 1
005E0867  44 0F B7 00                     movzx r8d, word ptr [rax]
005E086B  48 8D 48 08                     lea rcx, [rax + 8]
005E086F  49 C1 E0 03                     shl r8, 3
005E0873  33 D2                           xor edx, edx
005E0875  48 89 8D 80 00 00 00            mov qword ptr [rbp + 0x80], rcx
005E087C  E8 BF 63 0E 00                  call 0x1406c6c40
005E0881  48 8D 83 98 13 00 00            lea rax, [rbx + 0x1398]
005E0888  66 C7 83 90 12 00 00 01 00      mov word ptr [rbx + 0x1290], 1
005E0891  44 0F B7 00                     movzx r8d, word ptr [rax]
005E0895  48 8D 48 08                     lea rcx, [rax + 8]
005E0899  49 C1 E0 03                     shl r8, 3
005E089D  33 D2                           xor edx, edx
005E089F  E8 9C 63 0E 00                  call 0x1406c6c40
005E08A4  48 8D 83 A0 14 00 00            lea rax, [rbx + 0x14a0]
005E08AB  66 C7 83 98 13 00 00 01 00      mov word ptr [rbx + 0x1398], 1
005E08B4  44 0F B7 00                     movzx r8d, word ptr [rax]
005E08B8  48 8D 48 08                     lea rcx, [rax + 8]
005E08BC  49 C1 E0 03                     shl r8, 3
005E08C0  33 D2                           xor edx, edx
005E08C2  E8 79 63 0E 00                  call 0x1406c6c40
005E08C7  48 8D 83 A8 15 00 00            lea rax, [rbx + 0x15a8]
005E08CE  66 C7 83 A0 14 00 00 01 00      mov word ptr [rbx + 0x14a0], 1
005E08D7  44 0F B7 00                     movzx r8d, word ptr [rax]
005E08DB  48 8D 48 08                     lea rcx, [rax + 8]
005E08DF  49 C1 E0 03                     shl r8, 3
005E08E3  33 D2                           xor edx, edx
005E08E5  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
005E08E9  E8 52 63 0E 00                  call 0x1406c6c40
005E08EE  66 C7 83 A8 15 00 00 01 00      mov word ptr [rbx + 0x15a8], 1
005E08F7  49 8D 4D 08                     lea rcx, [r13 + 8]
005E08FB  45 0F B7 45 00                  movzx r8d, word ptr [r13]
005E0900  33 D2                           xor edx, edx
005E0902  49 C1 E0 03                     shl r8, 3
005E0906  E8 35 63 0E 00                  call 0x1406c6c40
005E090B  48 8D 83 B8 17 00 00            lea rax, [rbx + 0x17b8]
005E0912  66 41 C7 45 00 01 00            mov word ptr [r13], 1
005E0919  44 0F B7 00                     movzx r8d, word ptr [rax]
005E091D  48 8D 48 08                     lea rcx, [rax + 8]
005E0921  49 C1 E0 03                     shl r8, 3
005E0925  33 D2                           xor edx, edx
005E0927  E8 14 63 0E 00                  call 0x1406c6c40
005E092C  66 C7 83 B8 17 00 00 01 00      mov word ptr [rbx + 0x17b8], 1
005E0935  48 81 C3 68 0D 00 00            add rbx, 0xd68
005E093C  48 89 9D 88 00 00 00            mov qword ptr [rbp + 0x88], rbx
005E0943  48 8D 4B 08                     lea rcx, [rbx + 8]
005E0947  44 0F B7 03                     movzx r8d, word ptr [rbx]
005E094B  33 D2                           xor edx, edx
005E094D  49 C1 E0 03                     shl r8, 3
005E0951  E8 EA 62 0E 00                  call 0x1406c6c40
005E0956  66 C7 03 01 00                  mov word ptr [rbx], 1
005E095B  E8 2C F2 FF FF                  call 0x1405dfb8c
005E0960  85 C0                           test eax, eax
005E0962  74 51                           je 0x1405e09b5
005E0964  8B 05 B2 46 9E 00               mov eax, dword ptr [rip + 0x9e46b2]
005E096A  A8 08                           test al, 8
005E096C  74 37                           je 0x1405e09a5
005E096E  33 D2                           xor edx, edx
005E0970  48 C7 03 01 00 20 00            mov qword ptr [rbx], 0x200001
005E0977  41 B8 00 01 00 00               mov r8d, 0x100
005E097D  48 8D 4B 08                     lea rcx, [rbx + 8]
005E0981  E8 BA 62 0E 00                  call 0x1406c6c40
005E0986  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
005E098A  48 8B 90 00 05 00 00            mov rdx, qword ptr [rax + 0x500]
005E0991  48 63 42 04                     movsxd rax, dword ptr [rdx + 4]
005E0995  4C 8D 42 10                     lea r8, [rdx + 0x10]
005E0999  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
005E09A0  4C 03 C1                        add r8, rcx
005E09A3  EB 04                           jmp 0x1405e09a9
005E09A5  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
005E09A9  0F B7 53 02                     movzx edx, word ptr [rbx + 2]
005E09AD  48 8B CB                        mov rcx, rbx
005E09B0  E8 AB DE CE FF                  call 0x1402ce860
005E09B5  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
005E09B9  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
005E09BD  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
005E09C1  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
005E09C5  8A 84 01 F2 01 00 00            mov al, byte ptr [rcx + rax + 0x1f2]
005E09CC  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
005E09D0  88 45 84                        mov byte ptr [rbp - 0x7c], al
005E09D3  E8 68 FD DD FF                  call 0x1403c0740
005E09D8  44 0F B7 06                     movzx r8d, word ptr [rsi]
005E09DC  48 8D 4E 08                     lea rcx, [rsi + 8]
005E09E0  49 C1 E0 03                     shl r8, 3
005E09E4  33 D2                           xor edx, edx
005E09E6  E8 55 62 0E 00                  call 0x1406c6c40
005E09EB  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
005E09EF  33 D2                           xor edx, edx
005E09F1  66 C7 06 01 00                  mov word ptr [rsi], 1
005E09F6  44 0F B7 00                     movzx r8d, word ptr [rax]
005E09FA  48 8D 48 08                     lea rcx, [rax + 8]
005E09FE  49 C1 E0 03                     shl r8, 3
005E0A02  E8 39 62 0E 00                  call 0x1406c6c40
005E0A07  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
005E0A0B  33 C9                           xor ecx, ecx
005E0A0D  66 C7 00 01 00                  mov word ptr [rax], 1
005E0A12  39 8D 18 02 00 00               cmp dword ptr [rbp + 0x218], ecx
005E0A18  0F 84 E4 09 00 00               je 0x1405e1402
005E0A1E  8B 95 10 02 00 00               mov edx, dword ptr [rbp + 0x210]
005E0A24  85 D2                           test edx, edx
005E0A26  0F 84 D6 09 00 00               je 0x1405e1402
005E0A2C  48 8B 05 4D D8 92 00            mov rax, qword ptr [rip + 0x92d84d]
005E0A33  48 85 C0                        test rax, rax
005E0A36  0F 84 CB 00 00 00               je 0x1405e0b07
005E0A3C  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
005E0A40  44 8B C2                        mov r8d, edx
005E0A43  4C 8B 4D A0                     mov r9, qword ptr [rbp - 0x60]
005E0A47  48 8B 15 12 A8 92 00            mov rdx, qword ptr [rip + 0x92a812]
005E0A4E  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
005E0A53  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
005E0A57  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
005E0A5C  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
005E0A60  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
005E0A65  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
005E0A69  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
005E0A6E  33 C9                           xor ecx, ecx
005E0A70  E8 5B A0 0D 00                  call 0x1406baad0
005E0A75  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
005E0A79  4C 8B 4D D0                     mov r9, qword ptr [rbp - 0x30]
005E0A7D  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
005E0A81  0F B7 95 10 02 00 00            movzx edx, word ptr [rbp + 0x210]
005E0A88  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
005E0A8C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005E0A91  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
005E0A95  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005E0A9A  E8 39 DE FF FF                  call 0x1405de8d8
005E0A9F  44 0F B7 85 90 00 00 00         movzx r8d, word ptr [rbp + 0x90]
005E0AA7  48 8D 8D 98 00 00 00            lea rcx, [rbp + 0x98]
005E0AAE  49 C1 E0 03                     shl r8, 3
005E0AB2  33 D2                           xor edx, edx
005E0AB4  E8 87 61 0E 00                  call 0x1406c6c40
005E0AB9  44 0F B7 8D 92 00 00 00         movzx r9d, word ptr [rbp + 0x92]
005E0AC1  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E0AC8  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005E0ACC  B8 01 00 00 00                  mov eax, 1
005E0AD1  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
005E0AD5  66 89 85 90 00 00 00            mov word ptr [rbp + 0x90], ax
005E0ADC  E8 6B 9D DB FF                  call 0x14039a84c
005E0AE1  4C 8B 45 C8                     mov r8, qword ptr [rbp - 0x38]
005E0AE5  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
005E0AEC  49 8B C8                        mov rcx, r8
005E0AEF  E8 AC 50 CF FF                  call 0x1402d5ba0
005E0AF4  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
005E0AF8  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
005E0AFF  49 8B C8                        mov rcx, r8
005E0B02  E8 99 50 CF FF                  call 0x1402d5ba0
005E0B07  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
005E0B0B  48 8B 55 98                     mov rdx, qword ptr [rbp - 0x68]
005E0B0F  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
005E0B13  E8 88 50 CF FF                  call 0x1402d5ba0
005E0B18  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
005E0B1C  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005E0B20  49 8B C8                        mov rcx, r8
005E0B23  E8 78 50 CF FF                  call 0x1402d5ba0
005E0B28  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
005E0B2C  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
005E0B30  49 8B C8                        mov rcx, r8
005E0B33  E8 68 50 CF FF                  call 0x1402d5ba0
005E0B38  4C 8B 45 E0                     mov r8, qword ptr [rbp - 0x20]
005E0B3C  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
005E0B40  49 8B C8                        mov rcx, r8
005E0B43  E8 58 50 CF FF                  call 0x1402d5ba0
005E0B48  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
005E0B4C  48 8B CE                        mov rcx, rsi
005E0B4F  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
005E0B53  E8 08 DD CE FF                  call 0x1402ce860
005E0B58  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005E0B5C  4D 8B C4                        mov r8, r12
005E0B5F  48 8B CE                        mov rcx, rsi
005E0B62  E8 D9 FB DD FF                  call 0x1403c0740
005E0B67  B9 00 02 00 00                  mov ecx, 0x200
005E0B6C  85 C0                           test eax, eax
005E0B6E  74 0A                           je 0x1405e0b7a
005E0B70  09 0F                           or dword ptr [rdi], ecx
005E0B72  44 8B F9                        mov r15d, ecx
005E0B75  E9 C1 00 00 00                  jmp 0x1405e0c3b
005E0B7A  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
005E0B7E  4D 8B C4                        mov r8, r12
005E0B81  48 8B CE                        mov rcx, rsi
005E0B84  E8 B7 FB DD FF                  call 0x1403c0740
005E0B89  85 C0                           test eax, eax
005E0B8B  74 0A                           je 0x1405e0b97
005E0B8D  B8 00 04 00 00                  mov eax, 0x400
005E0B92  E9 9F 00 00 00                  jmp 0x1405e0c36
005E0B97  8B 05 7F 44 9E 00               mov eax, dword ptr [rip + 0x9e447f]
005E0B9D  A8 08                           test al, 8
005E0B9F  74 63                           je 0x1405e0c04
005E0BA1  E8 E6 EF FF FF                  call 0x1405dfb8c
005E0BA6  85 C0                           test eax, eax
005E0BA8  75 41                           jne 0x1405e0beb
005E0BAA  33 D2                           xor edx, edx
005E0BAC  48 C7 03 01 00 20 00            mov qword ptr [rbx], 0x200001
005E0BB3  41 B8 00 01 00 00               mov r8d, 0x100
005E0BB9  48 8D 4B 08                     lea rcx, [rbx + 8]
005E0BBD  E8 7E 60 0E 00                  call 0x1406c6c40
005E0BC2  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
005E0BC6  48 8B 90 00 05 00 00            mov rdx, qword ptr [rax + 0x500]
005E0BCD  48 63 42 04                     movsxd rax, dword ptr [rdx + 4]
005E0BD1  4C 8D 42 10                     lea r8, [rdx + 0x10]
005E0BD5  0F B7 53 02                     movzx edx, word ptr [rbx + 2]
005E0BD9  48 69 C8 08 01 00 00            imul rcx, rax, 0x108
005E0BE0  4C 03 C1                        add r8, rcx
005E0BE3  48 8B CB                        mov rcx, rbx
005E0BE6  E8 75 DC CE FF                  call 0x1402ce860
005E0BEB  4D 8B C4                        mov r8, r12
005E0BEE  48 8B D3                        mov rdx, rbx
005E0BF1  48 8B CE                        mov rcx, rsi
005E0BF4  E8 47 FB DD FF                  call 0x1403c0740
005E0BF9  85 C0                           test eax, eax
005E0BFB  74 3E                           je 0x1405e0c3b
005E0BFD  B8 00 00 40 00                  mov eax, 0x400000
005E0C02  EB 32                           jmp 0x1405e0c36
005E0C04  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
005E0C08  4D 8B C4                        mov r8, r12
005E0C0B  48 8B CE                        mov rcx, rsi
005E0C0E  E8 2D FB DD FF                  call 0x1403c0740
005E0C13  85 C0                           test eax, eax
005E0C15  74 07                           je 0x1405e0c1e
005E0C17  B8 00 08 00 00                  mov eax, 0x800
005E0C1C  EB 18                           jmp 0x1405e0c36
005E0C1E  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
005E0C22  4D 8B C4                        mov r8, r12
005E0C25  48 8B CE                        mov rcx, rsi
005E0C28  E8 13 FB DD FF                  call 0x1403c0740
005E0C2D  85 C0                           test eax, eax
005E0C2F  74 0A                           je 0x1405e0c3b
005E0C31  B8 00 00 08 00                  mov eax, 0x80000
005E0C36  09 07                           or dword ptr [rdi], eax
005E0C38  44 8B F8                        mov r15d, eax
005E0C3B  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
005E0C40  4D 8B C4                        mov r8, r12
005E0C43  49 8B CD                        mov rcx, r13
005E0C46  E8 15 DC CE FF                  call 0x1402ce860
005E0C4B  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
005E0C4F  33 D2                           xor edx, edx
005E0C51  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
005E0C55  44 0F B7 03                     movzx r8d, word ptr [rbx]
005E0C59  49 C1 E0 03                     shl r8, 3
005E0C5D  E8 DE 5F 0E 00                  call 0x1406c6c40
005E0C62  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
005E0C69  33 D2                           xor edx, edx
005E0C6B  66 C7 03 01 00                  mov word ptr [rbx], 1
005E0C70  48 8B 5D B8                     mov rbx, qword ptr [rbp - 0x48]
005E0C74  44 0F B7 03                     movzx r8d, word ptr [rbx]
005E0C78  49 C1 E0 03                     shl r8, 3
005E0C7C  E8 BF 5F 0E 00                  call 0x1406c6c40
005E0C81  66 C7 03 01 00                  mov word ptr [rbx], 1
005E0C86  4D 8B C5                        mov r8, r13
005E0C89  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005E0C8E  49 8B CE                        mov rcx, r14
005E0C91  E8 CA DB CE FF                  call 0x1402ce860
005E0C96  4C 8B 45 40                     mov r8, qword ptr [rbp + 0x40]
005E0C9A  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
005E0C9E  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
005E0CA2  E8 99 FA DD FF                  call 0x1403c0740
005E0CA7  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
005E0CAB  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
005E0CAF  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
005E0CB3  E8 E8 4E CF FF                  call 0x1402d5ba0
005E0CB8  4C 8B 45 10                     mov r8, qword ptr [rbp + 0x10]
005E0CBC  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
005E0CC0  49 8B C8                        mov rcx, r8
005E0CC3  E8 78 FA DD FF                  call 0x1403c0740
005E0CC8  33 DB                           xor ebx, ebx
005E0CCA  B0 FF                           mov al, 0xff
005E0CCC  88 45 81                        mov byte ptr [rbp - 0x7f], al
005E0CCF  88 45 80                        mov byte ptr [rbp - 0x80], al
005E0CD2  89 5D A8                        mov dword ptr [rbp - 0x58], ebx
005E0CD5  89 5D C0                        mov dword ptr [rbp - 0x40], ebx
005E0CD8  39 9D 18 02 00 00               cmp dword ptr [rbp + 0x218], ebx
005E0CDE  0F 86 2E 07 00 00               jbe 0x1405e1412
005E0CE4  49 8B CE                        mov rcx, r14
005E0CE7  E8 94 08 CF FF                  call 0x1402d1580
005E0CEC  85 C0                           test eax, eax
005E0CEE  0F 85 1E 07 00 00               jne 0x1405e1412
005E0CF4  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
005E0CF8  49 8B CE                        mov rcx, r14
005E0CFB  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
005E0CFF  4C 8B C3                        mov r8, rbx
005E0D02  E8 39 FA DD FF                  call 0x1403c0740
005E0D07  48 8B CB                        mov rcx, rbx
005E0D0A  E8 71 08 CF FF                  call 0x1402d1580
005E0D0F  85 C0                           test eax, eax
005E0D11  75 1A                           jne 0x1405e0d2d
005E0D13  B8 00 00 02 00                  mov eax, 0x20000
005E0D18  4C 8B C3                        mov r8, rbx
005E0D1B  09 07                           or dword ptr [rdi], eax
005E0D1D  44 0B F8                        or r15d, eax
005E0D20  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005E0D25  49 8B CE                        mov rcx, r14
005E0D28  E8 33 DB CE FF                  call 0x1402ce860
005E0D2D  8B 0D 0D 5E 9E 00               mov ecx, dword ptr [rip + 0x9e5e0d]
005E0D33  8D 41 FD                        lea eax, [rcx - 3]
005E0D36  A9 FC FF FF FF                  test eax, 0xfffffffc
005E0D3B  0F 85 C8 00 00 00               jne 0x1405e0e09
005E0D41  83 F9 04                        cmp ecx, 4
005E0D44  0F 84 BF 00 00 00               je 0x1405e0e09
005E0D4A  44 8A 8D 60 02 00 00            mov r9b, byte ptr [rbp + 0x260]
005E0D51  48 8D 55 80                     lea rdx, [rbp - 0x80]
005E0D55  44 8A 85 58 02 00 00            mov r8b, byte ptr [rbp + 0x258]
005E0D5C  B8 00 80 00 00                  mov eax, 0x8000
005E0D61  09 07                           or dword ptr [rdi], eax
005E0D63  44 0B F8                        or r15d, eax
005E0D66  8B 85 68 02 00 00               mov eax, dword ptr [rbp + 0x268]
005E0D6C  49 8B CE                        mov rcx, r14
005E0D6F  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005E0D73  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
005E0D76  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
005E0D7A  8B 85 50 02 00 00               mov eax, dword ptr [rbp + 0x250]
005E0D80  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005E0D84  E8 B7 EB F0 FF                  call 0x1404ef940
005E0D89  8A 45 81                        mov al, byte ptr [rbp - 0x7f]
005E0D8C  38 45 80                        cmp byte ptr [rbp - 0x80], al
005E0D8F  74 78                           je 0x1405e0e09
005E0D91  8A 45 80                        mov al, byte ptr [rbp - 0x80]
005E0D94  49 8B CE                        mov rcx, r14
005E0D97  88 45 81                        mov byte ptr [rbp - 0x7f], al
005E0D9A  E8 41 D9 CE FF                  call 0x1402ce6e0
005E0D9F  8B C8                           mov ecx, eax
005E0DA1  33 D2                           xor edx, edx
005E0DA3  89 45 98                        mov dword ptr [rbp - 0x68], eax
005E0DA6  48 8B 85 48 02 00 00            mov rax, qword ptr [rbp + 0x248]
005E0DAD  48 8B 00                        mov rax, qword ptr [rax]
005E0DB0  48 F7 F1                        div rcx
005E0DB3  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
005E0DB7  33 C0                           xor eax, eax
005E0DB9  48 8B DA                        mov rbx, rdx
005E0DBC  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
005E0DC0  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005E0DC4  66 89 45 00                     mov word ptr [rbp], ax
005E0DC8  48 8D 4D C0                     lea rcx, [rbp - 0x40]
005E0DCC  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
005E0DD0  E8 AB 46 E3 FF                  call 0x140415480
005E0DD5  85 C0                           test eax, eax
005E0DD7  75 21                           jne 0x1405e0dfa
005E0DD9  44 8D 60 01                     lea r12d, [rax + 1]
005E0DDD  48 85 DB                        test rbx, rbx
005E0DE0  74 14                           je 0x1405e0df6
005E0DE2  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005E0DE6  49 2B DC                        sub rbx, r12
005E0DE9  48 8D 4D C0                     lea rcx, [rbp - 0x40]
005E0DED  E8 8E 46 E3 FF                  call 0x140415480
005E0DF2  85 C0                           test eax, eax
005E0DF4  74 E7                           je 0x1405e0ddd
005E0DF6  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
005E0DFA  8B 55 C0                        mov edx, dword ptr [rbp - 0x40]
005E0DFD  8B 4D 98                        mov ecx, dword ptr [rbp - 0x68]
005E0E00  E8 AB 9E E9 FF                  call 0x14047acb0
005E0E05  48 8B 5D 48                     mov rbx, qword ptr [rbp + 0x48]
005E0E09  48 8B 55 10                     mov rdx, qword ptr [rbp + 0x10]
005E0E0D  4C 8B C3                        mov r8, rbx
005E0E10  49 8B CE                        mov rcx, r14
005E0E13  E8 28 F9 DD FF                  call 0x1403c0740
005E0E18  48 8B CB                        mov rcx, rbx
005E0E1B  E8 60 07 CF FF                  call 0x1402d1580
005E0E20  33 C9                           xor ecx, ecx
005E0E22  85 C0                           test eax, eax
005E0E24  75 1C                           jne 0x1405e0e42
005E0E26  B8 00 10 00 00                  mov eax, 0x1000
005E0E2B  4C 8B C3                        mov r8, rbx
005E0E2E  09 07                           or dword ptr [rdi], eax
005E0E30  49 8B CE                        mov rcx, r14
005E0E33  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005E0E38  44 0B F8                        or r15d, eax
005E0E3B  E8 20 DA CE FF                  call 0x1402ce860
005E0E40  33 C9                           xor ecx, ecx
005E0E42  48 8B 85 48 02 00 00            mov rax, qword ptr [rbp + 0x248]
005E0E49  38 48 10                        cmp byte ptr [rax + 0x10], cl
005E0E4C  75 35                           jne 0x1405e0e83
005E0E4E  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
005E0E52  4C 8B C3                        mov r8, rbx
005E0E55  49 8B CE                        mov rcx, r14
005E0E58  E8 43 4D CF FF                  call 0x1402d5ba0
005E0E5D  48 8B CB                        mov rcx, rbx
005E0E60  E8 1B 07 CF FF                  call 0x1402d1580
005E0E65  85 C0                           test eax, eax
005E0E67  75 1A                           jne 0x1405e0e83
005E0E69  B8 00 20 00 00                  mov eax, 0x2000
005E0E6E  4C 8B C3                        mov r8, rbx
005E0E71  09 07                           or dword ptr [rdi], eax
005E0E73  44 0B F8                        or r15d, eax
005E0E76  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005E0E7B  49 8B CE                        mov rcx, r14
005E0E7E  E8 DD D9 CE FF                  call 0x1402ce860
005E0E83  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
005E0E87  33 DB                           xor ebx, ebx
005E0E89  66 89 5D 00                     mov word ptr [rbp], bx
005E0E8D  48 89 45 F8                     mov qword ptr [rbp - 8], rax
005E0E91  4C 89 75 F0                     mov qword ptr [rbp - 0x10], r14
005E0E95  EB 08                           jmp 0x1405e0e9f
005E0E97  8B 45 88                        mov eax, dword ptr [rbp - 0x78]
005E0E9A  3B 45 C0                        cmp eax, dword ptr [rbp - 0x40]
005E0E9D  73 13                           jae 0x1405e0eb2
005E0E9F  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005E0EA3  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E0EA7  E8 D4 45 E3 FF                  call 0x140415480
005E0EAC  85 C0                           test eax, eax
005E0EAE  74 E7                           je 0x1405e0e97
005E0EB0  EB 05                           jmp 0x1405e0eb7
005E0EB2  83 F8 FF                        cmp eax, -1
005E0EB5  75 08                           jne 0x1405e0ebf
005E0EB7  49 8B CE                        mov rcx, r14
005E0EBA  E8 21 F3 E8 FF                  call 0x1404701e0
005E0EBF  8B C8                           mov ecx, eax
005E0EC1  E8 0A 77 CF FF                  call 0x1402d85d0
005E0EC6  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
005E0ECA  48 8B D8                        mov rbx, rax
005E0ECD  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
005E0ED1  33 D2                           xor edx, edx
005E0ED3  44 0F B7 00                     movzx r8d, word ptr [rax]
005E0ED7  49 C1 E0 03                     shl r8, 3
005E0EDB  E8 60 5D 0E 00                  call 0x1406c6c40
005E0EE0  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
005E0EE4  33 C9                           xor ecx, ecx
005E0EE6  38 0D D5 74 92 00               cmp byte ptr [rip + 0x9274d5], cl
005E0EEC  66 C7 00 01 00                  mov word ptr [rax], 1
005E0EF1  74 09                           je 0x1405e0efc
005E0EF3  4C 8B 83 60 8E 00 00            mov r8, qword ptr [rbx + 0x8e60]
005E0EFA  EB 07                           jmp 0x1405e0f03
005E0EFC  4C 8B 83 C8 00 00 00            mov r8, qword ptr [rbx + 0xc8]
005E0F03  0F B6 93 D0 00 00 00            movzx edx, byte ptr [rbx + 0xd0]
005E0F0A  48 8B C8                        mov rcx, rax
005E0F0D  E8 AE A7 C7 FF                  call 0x14025b6c0
005E0F12  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
005E0F16  4C 8B C6                        mov r8, rsi
005E0F19  48 8B CE                        mov rcx, rsi
005E0F1C  E8 7F 4C CF FF                  call 0x1402d5ba0
005E0F21  8B 4D A8                        mov ecx, dword ptr [rbp - 0x58]
005E0F24  8B 95 10 02 00 00               mov edx, dword ptr [rbp + 0x210]
005E0F2A  3B CA                           cmp ecx, edx
005E0F2C  0F 82 CF 00 00 00               jb 0x1405e1001
005E0F32  4C 8B 45 20                     mov r8, qword ptr [rbp + 0x20]
005E0F36  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
005E0F3A  49 8B C8                        mov rcx, r8
005E0F3D  E8 EE E9 CE FF                  call 0x1402cf930
005E0F42  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
005E0F46  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E0F4D  0F B7 95 92 00 00 00            movzx edx, word ptr [rbp + 0x92]
005E0F54  E8 07 D9 CE FF                  call 0x1402ce860
005E0F59  48 8B 05 68 74 92 00            mov rax, qword ptr [rip + 0x927468]
005E0F60  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
005E0F64  48 85 C0                        test rax, rax
005E0F67  0F 84 4E 01 00 00               je 0x1405e10bb
005E0F6D  48 8B 05 44 74 92 00            mov rax, qword ptr [rip + 0x927444]
005E0F74  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
005E0F78  48 85 C0                        test rax, rax
005E0F7B  0F 84 3A 01 00 00               je 0x1405e10bb
005E0F81  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E0F88  E8 F3 05 CF FF                  call 0x1402d1580
005E0F8D  85 C0                           test eax, eax
005E0F8F  0F 85 26 01 00 00               jne 0x1405e10bb
005E0F95  48 8B 7D 38                     mov rdi, qword ptr [rbp + 0x38]
005E0F99  44 8D 70 01                     lea r14d, [rax + 1]
005E0F9D  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
005E0FA1  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E0FA8  E8 33 F2 E8 FF                  call 0x1404701e0
005E0FAD  8B D0                           mov edx, eax
005E0FAF  8B 05 FB 73 92 00               mov eax, dword ptr [rip + 0x9273fb]
005E0FB5  89 55 88                        mov dword ptr [rbp - 0x78], edx
005E0FB8  41 89 04 94                     mov dword ptr [r12 + rdx*4], eax
005E0FBC  3B 04 97                        cmp eax, dword ptr [rdi + rdx*4]
005E0FBF  74 07                           je 0x1405e0fc8
005E0FC1  44 88 35 F8 73 92 00            mov byte ptr [rip + 0x9273f8], r14b
005E0FC8  FF C0                           inc eax
005E0FCA  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E0FD1  89 05 D9 73 92 00               mov dword ptr [rip + 0x9273d9], eax
005E0FD7  E8 34 3E D2 FF                  call 0x140304e10
005E0FDC  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E0FE3  E8 98 05 CF FF                  call 0x1402d1580
005E0FE8  85 C0                           test eax, eax
005E0FEA  74 B5                           je 0x1405e0fa1
005E0FEC  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
005E0FF0  4C 8B 75 68                     mov r14, qword ptr [rbp + 0x68]
005E0FF4  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
005E0FF8  4C 8B 6D 70                     mov r13, qword ptr [rbp + 0x70]
005E0FFC  E9 BA 00 00 00                  jmp 0x1405e10bb
005E1001  45 33 C0                        xor r8d, r8d
005E1004  4C 39 45 58                     cmp qword ptr [rbp + 0x58], r8
005E1008  0F 84 AD 00 00 00               je 0x1405e10bb
005E100E  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
005E1012  83 B8 D0 04 00 00 03            cmp dword ptr [rax + 0x4d0], 3
005E1019  0F 85 9C 00 00 00               jne 0x1405e10bb
005E101F  8B 45 08                        mov eax, dword ptr [rbp + 8]
005E1022  2B C1                           sub eax, ecx
005E1024  66 44 89 45 00                  mov word ptr [rbp], r8w
005E1029  8D 4A FF                        lea ecx, [rdx - 1]
005E102C  03 C8                           add ecx, eax
005E102E  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005E1032  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
005E1036  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
005E1039  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E103D  48 8B 00                        mov rax, qword ptr [rax]
005E1040  48 89 45 F8                     mov qword ptr [rbp - 8], rax
005E1044  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
005E1048  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
005E104C  E8 2F 44 E3 FF                  call 0x140415480
005E1051  85 C0                           test eax, eax
005E1053  75 52                           jne 0x1405e10a7
005E1055  8B 7D 98                        mov edi, dword ptr [rbp - 0x68]
005E1058  4C 8B 65 E8                     mov r12, qword ptr [rbp - 0x18]
005E105C  4C 8B 6D 58                     mov r13, qword ptr [rbp + 0x58]
005E1060  41 0F B7 44 24 0A               movzx eax, word ptr [r12 + 0xa]
005E1066  3B F8                           cmp edi, eax
005E1068  73 1A                           jae 0x1405e1084
005E106A  8B 4D 88                        mov ecx, dword ptr [rbp - 0x78]
005E106D  8B C7                           mov eax, edi
005E106F  41 39 4C 85 00                  cmp dword ptr [r13 + rax*4], ecx
005E1074  74 0E                           je 0x1405e1084
005E1076  41 89 4C 85 00                  mov dword ptr [r13 + rax*4], ecx
005E107B  41 C6 84 24 E6 04 00 00 01      mov byte ptr [r12 + 0x4e6], 1
005E1084  48 8D 55 F0                     lea rdx, [rbp - 0x10]
005E1088  FF CF                           dec edi
005E108A  48 8D 4D 88                     lea rcx, [rbp - 0x78]
005E108E  E8 ED 43 E3 FF                  call 0x140415480
005E1093  85 C0                           test eax, eax
005E1095  74 C9                           je 0x1405e1060
005E1097  48 8B 7D 60                     mov rdi, qword ptr [rbp + 0x60]
005E109B  4C 8B 75 68                     mov r14, qword ptr [rbp + 0x68]
005E109F  4C 8B 65 28                     mov r12, qword ptr [rbp + 0x28]
005E10A3  4C 8B 6D 70                     mov r13, qword ptr [rbp + 0x70]
005E10A7  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
005E10AB  E8 30 D6 CE FF                  call 0x1402ce6e0
005E10B0  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
005E10B4  66 01 81 E4 04 00 00            add word ptr [rcx + 0x4e4], ax
005E10BB  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
005E10BF  E8 1C D6 CE FF                  call 0x1402ce6e0
005E10C4  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
005E10C7  48 8B 4D A0                     mov rcx, qword ptr [rbp - 0x60]
005E10CB  03 D0                           add edx, eax
005E10CD  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
005E10D1  44 8B CA                        mov r9d, edx
005E10D4  44 8B 85 18 02 00 00            mov r8d, dword ptr [rbp + 0x218]
005E10DB  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
005E10E0  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
005E10E5  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
005E10E9  4C 89 64 24 60                  mov qword ptr [rsp + 0x60], r12
005E10EE  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
005E10F3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
005E10F8  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
005E10FC  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
005E1101  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
005E1105  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
005E110A  8B 85 50 02 00 00               mov eax, dword ptr [rbp + 0x250]
005E1110  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
005E1115  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
005E111A  89 55 A8                        mov dword ptr [rbp - 0x58], edx
005E111D  8B 95 10 02 00 00               mov edx, dword ptr [rbp + 0x210]
005E1123  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
005E1128  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
005E112C  E8 9F F8 F0 FF                  call 0x1404f09d0
005E1131  45 0F B7 06                     movzx r8d, word ptr [r14]
005E1135  49 8D 4E 08                     lea rcx, [r14 + 8]
005E1139  33 C0                           xor eax, eax
005E113B  49 C1 E0 03                     shl r8, 3
005E113F  33 D2                           xor edx, edx
005E1141  44 8B F8                        mov r15d, eax
005E1144  E8 F7 5A 0E 00                  call 0x1406c6c40
005E1149  48 8D 93 10 8C 00 00            lea rdx, [rbx + 0x8c10]
005E1150  66 41 C7 06 01 00               mov word ptr [r14], 1
005E1156  4D 8B C5                        mov r8, r13
005E1159  49 8B CD                        mov rcx, r13
005E115C  E8 3F 4A CF FF                  call 0x1402d5ba0
005E1161  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E1168  BA 05 00 00 00                  mov edx, 5
005E116D  48 8B CB                        mov rcx, rbx
005E1170  E8 F7 82 EC FF                  call 0x1404a946c
005E1175  0F B6 4D 82                     movzx ecx, byte ptr [rbp - 0x7e]
005E1179  85 C9                           test ecx, ecx
005E117B  74 5A                           je 0x1405e11d7
005E117D  83 E9 01                        sub ecx, 1
005E1180  74 26                           je 0x1405e11a8
005E1182  83 F9 01                        cmp ecx, 1
005E1185  75 50                           jne 0x1405e11d7
005E1187  44 0F B7 8D 92 00 00 00         movzx r9d, word ptr [rbp + 0x92]
005E118F  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E1196  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
005E119A  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E11A1  E8 42 50 CF FF                  call 0x1402d61e8
005E11A6  EB 1A                           jmp 0x1405e11c2
005E11A8  0F B7 95 92 00 00 00            movzx edx, word ptr [rbp + 0x92]
005E11AF  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E11B6  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E11BD  E8 1E F4 DD FF                  call 0x1403c05e0
005E11C2  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
005E11C6  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
005E11CD  4C 8B C6                        mov r8, rsi
005E11D0  E8 63 1E F1 FF                  call 0x1404f3038
005E11D5  EB 20                           jmp 0x1405e11f7
005E11D7  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
005E11DB  33 D2                           xor edx, edx
005E11DD  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
005E11E1  44 0F B7 00                     movzx r8d, word ptr [rax]
005E11E5  49 C1 E0 03                     shl r8, 3
005E11E9  E8 52 5A 0E 00                  call 0x1406c6c40
005E11EE  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
005E11F2  66 C7 00 01 00                  mov word ptr [rax], 1
005E11F7  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E11FE  BA 02 00 00 00                  mov edx, 2
005E1203  48 8B CB                        mov rcx, rbx
005E1206  E8 61 82 EC FF                  call 0x1404a946c
005E120B  0F B6 4D 83                     movzx ecx, byte ptr [rbp - 0x7d]
005E120F  85 C9                           test ecx, ecx
005E1211  74 5A                           je 0x1405e126d
005E1213  83 E9 01                        sub ecx, 1
005E1216  74 26                           je 0x1405e123e
005E1218  83 F9 01                        cmp ecx, 1
005E121B  75 50                           jne 0x1405e126d
005E121D  44 0F B7 8D 92 00 00 00         movzx r9d, word ptr [rbp + 0x92]
005E1225  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E122C  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
005E1230  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E1237  E8 AC 4F CF FF                  call 0x1402d61e8
005E123C  EB 1A                           jmp 0x1405e1258
005E123E  0F B7 95 92 00 00 00            movzx edx, word ptr [rbp + 0x92]
005E1245  4C 8D 85 90 00 00 00            lea r8, [rbp + 0x90]
005E124C  48 8D 8D 90 00 00 00            lea rcx, [rbp + 0x90]
005E1253  E8 88 F3 DD FF                  call 0x1403c05e0
005E1258  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
005E125C  48 8D 95 90 00 00 00            lea rdx, [rbp + 0x90]
005E1263  4C 8B C6                        mov r8, rsi
005E1266  E8 CD 1D F1 FF                  call 0x1404f3038
005E126B  EB 23                           jmp 0x1405e1290
005E126D  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
005E1271  33 D2                           xor edx, edx
005E1273  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
005E127A  44 0F B7 00                     movzx r8d, word ptr [rax]
005E127E  49 C1 E0 03                     shl r8, 3
005E1282  E8 B9 59 0E 00                  call 0x1406c6c40
005E1287  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
005E128B  66 C7 00 01 00                  mov word ptr [rax], 1
005E1290  0F B6 4D 84                     movzx ecx, byte ptr [rbp - 0x7c]
005E1294  85 C9                           test ecx, ecx
005E1296  74 28                           je 0x1405e12c0
005E1298  83 E9 01                        sub ecx, 1
005E129B  74 23                           je 0x1405e12c0
005E129D  83 E9 01                        sub ecx, 1
005E12A0  74 1E                           je 0x1405e12c0
005E12A2  83 F9 01                        cmp ecx, 1
005E12A5  75 19                           jne 0x1405e12c0
005E12A7  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
005E12AE  66 41 39 04 24                  cmp word ptr [r12], ax
005E12B3  76 2A                           jbe 0x1405e12df
005E12B5  8B C8                           mov ecx, eax
005E12B7  48 8B 83 C8 00 00 00            mov rax, qword ptr [rbx + 0xc8]
005E12BE  EB 17                           jmp 0x1405e12d7
005E12C0  0F B6 83 D0 00 00 00            movzx eax, byte ptr [rbx + 0xd0]
005E12C7  66 41 39 04 24                  cmp word ptr [r12], ax
005E12CC  76 11                           jbe 0x1405e12df
005E12CE  8B C8                           mov ecx, eax
005E12D0  48 8B 83 60 8E 00 00            mov rax, qword ptr [rbx + 0x8e60]
005E12D7  48 F7 D0                        not rax
005E12DA  49 21 44 CC 08                  and qword ptr [r12 + rcx*8 + 8], rax
005E12DF  49 8B CE                        mov rcx, r14
005E12E2  E8 99 02 CF FF                  call 0x1402d1580
005E12E7  85 C0                           test eax, eax
005E12E9  0F 84 02 01 00 00               je 0x1405e13f1
005E12EF  49 8B CD                        mov rcx, r13
005E12F2  E8 89 02 CF FF                  call 0x1402d1580
005E12F7  85 C0                           test eax, eax
005E12F9  0F 84 E2 00 00 00               je 0x1405e13e1
005E12FF  49 8B CC                        mov rcx, r12
005E1302  E8 79 02 CF FF                  call 0x1402d1580
005E1307  85 C0                           test eax, eax
005E1309  0F 84 8C 00 00 00               je 0x1405e139b
005E130F  48 8B 55 D0                     mov rdx, qword ptr [rbp - 0x30]
005E1313  4D 8B C4                        mov r8, r12
005E1316  48 8B CE                        mov rcx, rsi
005E1319  E8 22 F4 DD FF                  call 0x1403c0740
005E131E  85 C0                           test eax, eax
005E1320  74 07                           je 0x1405e1329
005E1322  B8 00 02 00 00                  mov eax, 0x200
005E1327  EB 6D                           jmp 0x1405e1396
005E1329  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
005E132D  4D 8B C4                        mov r8, r12
005E1330  48 8B CE                        mov rcx, rsi
005E1333  E8 08 F4 DD FF                  call 0x1403c0740
005E1338  85 C0                           test eax, eax
005E133A  74 07                           je 0x1405e1343
005E133C  B8 00 04 00 00                  mov eax, 0x400
005E1341  EB 53                           jmp 0x1405e1396
005E1343  8B 05 D3 3C 9E 00               mov eax, dword ptr [rip + 0x9e3cd3]
005E1349  4D 8B C4                        mov r8, r12
005E134C  48 8B CE                        mov rcx, rsi
005E134F  A8 08                           test al, 8
005E1351  74 17                           je 0x1405e136a
005E1353  48 8B 95 88 00 00 00            mov rdx, qword ptr [rbp + 0x88]
005E135A  E8 E1 F3 DD FF                  call 0x1403c0740
005E135F  85 C0                           test eax, eax
005E1361  74 38                           je 0x1405e139b
005E1363  B8 00 00 40 00                  mov eax, 0x400000
005E1368  EB 2C                           jmp 0x1405e1396
005E136A  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
005E136E  E8 CD F3 DD FF                  call 0x1403c0740
005E1373  85 C0                           test eax, eax
005E1375  74 07                           je 0x1405e137e
005E1377  B8 00 08 00 00                  mov eax, 0x800
005E137C  EB 18                           jmp 0x1405e1396
005E137E  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
005E1382  4D 8B C4                        mov r8, r12
005E1385  48 8B CE                        mov rcx, rsi
005E1388  E8 B3 F3 DD FF                  call 0x1403c0740
005E138D  85 C0                           test eax, eax
005E138F  74 0A                           je 0x1405e139b
005E1391  B8 00 00 08 00                  mov eax, 0x80000
005E1396  09 07                           or dword ptr [rdi], eax
005E1398  44 8B F8                        mov r15d, eax
005E139B  41 0F B7 55 02                  movzx edx, word ptr [r13 + 2]
005E13A0  4D 8B C4                        mov r8, r12
005E13A3  49 8B CD                        mov rcx, r13
005E13A6  E8 B5 D4 CE FF                  call 0x1402ce860
005E13AB  48 8B 55 B0                     mov rdx, qword ptr [rbp - 0x50]
005E13AF  49 8B CD                        mov rcx, r13
005E13B2  E8 95 E4 CE FF                  call 0x1402cf84c
005E13B7  85 C0                           test eax, eax
005E13B9  74 0B                           je 0x1405e13c6
005E13BB  4D 8B C5                        mov r8, r13
005E13BE  49 8B CD                        mov rcx, r13
005E13C1  E8 7A F3 DD FF                  call 0x1403c0740
005E13C6  48 8B 55 B8                     mov rdx, qword ptr [rbp - 0x48]
005E13CA  49 8B CD                        mov rcx, r13
005E13CD  E8 7A E4 CE FF                  call 0x1402cf84c
005E13D2  85 C0                           test eax, eax
005E13D4  74 0B                           je 0x1405e13e1
005E13D6  4D 8B C5                        mov r8, r13
005E13D9  49 8B CD                        mov rcx, r13
005E13DC  E8 5F F3 DD FF                  call 0x1403c0740
005E13E1  41 0F B7 56 02                  movzx edx, word ptr [r14 + 2]
005E13E6  4D 8B C5                        mov r8, r13
005E13E9  49 8B CE                        mov rcx, r14
005E13EC  E8 6F D4 CE FF                  call 0x1402ce860
005E13F1  8B 85 18 02 00 00               mov eax, dword ptr [rbp + 0x218]
005E13F7  39 45 A8                        cmp dword ptr [rbp - 0x58], eax
005E13FA  0F 82 E4 F8 FF FF               jb 0x1405e0ce4
005E1400  EB 10                           jmp 0x1405e1412
005E1402  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
005E1406  48 8B CE                        mov rcx, rsi
005E1409  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
005E140D  E8 4E D4 CE FF                  call 0x1402ce860
005E1412  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
005E1419  48 33 CC                        xor rcx, rsp
005E141C  E8 1F B2 0C 00                  call 0x1406ac640
005E1421  48 8B 9C 24 00 03 00 00         mov rbx, qword ptr [rsp + 0x300]
005E1429  48 81 C4 B0 02 00 00            add rsp, 0x2b0
005E1430  41 5F                           pop r15
005E1432  41 5E                           pop r14
005E1434  41 5D                           pop r13
005E1436  41 5C                           pop r12
005E1438  5F                              pop rdi
005E1439  5E                              pop rsi
005E143A  5D                              pop rbp
005E143B  C3                              ret
005E143C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkComputeUnparkMaskEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int16 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, unsigned int a13, unsigned __int8 a14, unsigned __int8 a15, unsigned int a16)
{
    __int64 result;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m150;
    unsigned __int16 v_stack_m156;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int16 v_stack_m1E2;
    unsigned int v_stack_m1E6;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m260;
    unsigned __int8 v_stack_m264;
    unsigned __int8 v_stack_m265;
    unsigned __int8 v_stack_m266;
    unsigned __int8 v_stack_m267;
    unsigned __int8 v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 8560954)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m250 = a7;
    v_stack_m218 = a8;
    v_stack_m1B0 = a3;
    v_stack_m248 = a2;
    a2 = 0;
    v_stack_m200 = a1;
    v_stack_m1C8 = a10;
    v_stack_m1B8 = a4;
    v_stack_m188 = a11;
    result = memset(v_stack_m150, a2, 256, a4);
    a3 = 0;
    result = ((int)(*(unsigned int *)(v_rip + 9619345))) * ((int)(*(unsigned int *)(v_rip + 9619345)));
    v_stack_m1E6 = 0;
    v_stack_m240 = result;
    v_stack_m1E2 = 0;
    v_stack_m260 = 0;
    v_stack_m266 = (unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 8551695) * 1 + 497));
    v_stack_m1E0 = (unsigned int)(*(unsigned __int16 *)(a1 + 1252));
    v_stack_m190 = *(unsigned __int64 *)(a1 + 1256);
    v_stack_m228 = *(unsigned __int64 *)(v_rip + 8551695);
    v_stack_m265 = (unsigned __int8)(*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_rip + 8551695) * 1 + 496));
    a2 = 0;
    v_stack_m158 = 0x200001ULL;
    v_stack_m1A8 = *(unsigned __int64 *)(v_rip + 8942523) + 2376;
    v_stack_m180 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
    v_stack_m1D8 = *(unsigned __int64 *)(v_rip + 8942523) + 2640;
    v_stack_m1C0 = *(unsigned __int64 *)(v_rip + 8942523) + 3696;
    v_stack_m238 = *(unsigned __int64 *)(v_rip + 8942523) + 3168;
    v_stack_m178 = *(unsigned __int64 *)(v_rip + 8942523) + 5808;
    v_stack_m1D0 = *(unsigned __int64 *)(v_rip + 8942523) + 3960;
    v_stack_m1A0 = *(unsigned __int64 *)(v_rip + 8942523) + 4224;
    v_stack_m230 = *(unsigned __int64 *)(v_rip + 8942523) + 4752;
    v_stack_m208 = *(unsigned __int64 *)(v_rip + 8942523) + 5016;
    v_stack_m220 = *(unsigned __int64 *)(v_rip + 8942523) + 5280;
    v_stack_m258 = *(unsigned __int64 *)(v_rip + 8942523) + 5544;
    v_stack_m210 = *(unsigned __int64 *)(v_rip + 8942523) + 6072;
    result = memset(v_stack_m150, a2, 256, a4);
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2376)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 2376 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2376) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2640)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 2640 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2640) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3168)) << (3);
    a2 = 0;
    v_stack_m170 = *(unsigned __int64 *)(v_rip + 8942523) + 3168 + 8;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 3168 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3168) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3696)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 3696 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3696) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3960)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 3960 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 3960) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 4224)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 4224 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 4224) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 4752)) << (3);
    a2 = 0;
    v_stack_m168 = *(unsigned __int64 *)(v_rip + 8942523) + 4752 + 8;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 4752 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 4752) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5016)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 5016 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5016) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5280)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 5280 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5280) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5544)) << (3);
    a2 = 0;
    v_stack_m198 = *(unsigned __int64 *)(v_rip + 8942523) + 5544 + 8;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 5544 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5544) = 1;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5808)) << (3);
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 5808 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5808) = 1;
    a3 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 6072)) << (3);
    a2 = 0;
    result = memset(*(unsigned __int64 *)(v_rip + 8942523) + 6072 + 8, a2, a3, a4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 6072) = 1;
    v_rbx = (*(unsigned __int64 *)(v_rip + 8942523)) + (0xD68ULL);
    v_stack_m160 = v_rbx;
    a2 = 0;
    a3 = (*(unsigned __int16 *)(v_rbx)) << (3);
    result = memset(v_rbx + 8, a2, a3, a4);
    *(unsigned __int16 *)(v_rbx) = 1;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(v_rbx + 8, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_005E09B5;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10372786)))) & (8)) == 0) goto loc_005E09A5;
    a2 = 0;
    *(unsigned __int64 *)(v_rbx) = 0x200001ULL;
    result = memset(v_rbx + 8, a2, 256, a4);
    a1 = (v_rbx + 8) * ((int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m200 + 1280) + 4)));
    a3 = (*(unsigned __int64 *)(v_stack_m200 + 1280) + 16) + (a1);
    goto loc_005E09A9;
loc_005E09A5:
loc_005E09A9:
    result = KiCopyAffinityEx(v_rbx, *(unsigned __int16 *)(v_rbx + 2), v_stack_m248, a4);
loc_005E09B5:
    v_stack_m264 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m240 + v_stack_m228 * 1 + 498));
    result = KeAndAffinityEx2(v_stack_m1B0, v_stack_m248, v_stack_m1D0, a4);
    a3 = (*(unsigned __int16 *)(a9)) << (3);
    a2 = 0;
    result = memset(a9 + 8, a2, a3, a4);
    a2 = 0;
    *(unsigned __int16 *)(a9) = 1;
    a3 = (*(unsigned __int16 *)(v_stack_m1C8)) << (3);
    result = memset(v_stack_m1C8 + 8, a2, a3, a4);
    a1 = 0;
    *(unsigned __int16 *)(v_stack_m1C8) = 1;
    if (a6 == 0) goto loc_005E1402;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_005E1402;
    result = *(unsigned __int64 *)(v_rip + 9623629);
    if (*(unsigned __int64 *)(v_rip + 9623629) != 0) {
        a1 = v_stack_m210;
        a3 = (unsigned int)((unsigned int)(a5));
        a4 = v_stack_m248;
        a2 = *(unsigned __int64 *)(v_rip + 9611282);
        v_stack_m2B0 = a1;
        a1 = v_stack_m220;
        v_stack_m2B8 = a1;
        a1 = v_stack_m218;
        v_stack_m2C0 = a1;
        a1 = v_stack_m250;
        v_stack_m2C8 = a1;
        a1 = 0;
        result = guard_dispatch_icall(a1, a2, a3, a4);
        result = v_stack_m210;
        a4 = v_stack_m218;
        a3 = v_stack_m250;
        a2 = a5;
        a1 = v_stack_m248;
        v_stack_m2C0 = result;
        result = v_stack_m220;
        v_stack_m2C8 = result;
        result = PpmEventParkNodePreferenceEx(a1, a2, a3, a4);
        a3 = v_stack_m158;
        a1 = v_stack_m150;
        a3 = (a3) << (3);
        a2 = 0;
        result = memset(a1, a2, a3, a4);
        a4 = v_stack_m156;
        a3 = v_stack_m158;
        a2 = v_stack_m218;
        result = 1;
        a1 = v_stack_m250;
        v_stack_m158 = (unsigned __int16)(result);
        result = KiOrAffinityEx(a1, a2, a3, a4);
        a3 = v_stack_m220;
        a2 = v_stack_m158;
        a1 = a3;
        result = KeSubtractAffinityEx2(a1, a2, a3, a4);
        a3 = v_stack_m210;
        a2 = v_stack_m158;
        a1 = a3;
        result = KeSubtractAffinityEx2(a1, a2, a3, a4);
    }
    result = KeSubtractAffinityEx2(v_stack_m248, v_stack_m250, v_stack_m208, a4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m218, v_stack_m208, a4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m220, v_stack_m208, a4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m210, v_stack_m208, a4);
    result = KiCopyAffinityEx(a9, *(unsigned __int16 *)(a9 + 2), v_stack_m248, a4);
    result = KeAndAffinityEx2(a9, v_stack_m218, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) goto loc_005E0B7A;
    goto loc_005E0C3B;
loc_005E0B7A:
    result = KeAndAffinityEx2(a9, v_stack_m210, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) goto loc_005E0B97;
    goto loc_005E0C36;
loc_005E0B97:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10372223)))) & (8)) == 0) goto loc_005E0C04;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(a9, v_stack_m210, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) {
        a2 = 0;
        *(unsigned __int64 *)(v_rbx) = 0x200001ULL;
        a3 = 256;
        a1 = v_rbx + 8;
        result = memset(a1, a2, a3, a4);
        result = v_stack_m200;
        a2 = *(unsigned __int64 *)(result + 1280);
        result = (int)(*(unsigned int *)(a2 + 4));
        a3 = a2 + 16;
        a2 = *(unsigned __int16 *)(v_rbx + 2);
        a1 = (a1) * (result);
        a3 = (a3) + (a1);
        a1 = v_rbx;
        result = KiCopyAffinityEx(a1, a2, a3, a4);
    }
    result = KeAndAffinityEx2(a9, v_rbx, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) goto loc_005E0C3B;
    goto loc_005E0C36;
loc_005E0C04:
    result = KeAndAffinityEx2(a9, v_stack_m208, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) goto loc_005E0C1E;
    goto loc_005E0C36;
loc_005E0C1E:
    result = KeAndAffinityEx2(a9, v_stack_m220, *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    if ((unsigned int)(result) == 0) goto loc_005E0C3B;
loc_005E0C36:
loc_005E0C3B:
    result = KiCopyAffinityEx(*(unsigned __int64 *)(v_rip + 8942523) + 5808, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 5808 + 2), *(unsigned __int64 *)(v_rip + 8942523) + 3696, a4);
    a2 = 0;
    a3 = (*(unsigned __int16 *)(v_stack_m238)) << (3);
    result = memset(v_stack_m170, a2, a3, a4);
    a2 = 0;
    *(unsigned __int16 *)(v_stack_m238) = 1;
    a3 = (*(unsigned __int16 *)(v_stack_m230)) << (3);
    result = memset(v_stack_m168, a2, a3, a4);
    *(unsigned __int16 *)(v_stack_m230) = 1;
    result = KiCopyAffinityEx(*(unsigned __int64 *)(v_rip + 8942523) + 2904, *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 2), *(unsigned __int64 *)(v_rip + 8942523) + 5808, a4);
    result = KeAndAffinityEx2(v_stack_m1D0, v_stack_m1B8, v_stack_m1A8, a4);
    result = KeSubtractAffinityEx2(v_stack_m248, v_stack_m1D0, v_stack_m1D8, a4);
    result = KeAndAffinityEx2(v_stack_m1D8, v_stack_m1B8, v_stack_m1D8, a4);
    v_rbx = 0;
    v_stack_m267 = 255;
    v_stack_m268 = 255;
    v_stack_m240 = 0;
    v_stack_m228 = 0;
    if (a6 <= 0) goto loc_005E1412;
loc_005E0CE4:
    result = KeIsEmptyAffinityEx(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m1B8, v_stack_m1D8, a4);
    if ((unsigned int)(result) != 0) goto loc_005E1412;
    result = KeAndAffinityEx2(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m1A8, v_stack_m1A0, a4);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1A8, v_stack_m1A0, a4);
    v_r15 = (unsigned int)((unsigned int)((unsigned int)(0x80000ULL)));
    if ((unsigned int)(result) == 0) {
        result = 0x20000ULL;
        a3 = v_stack_m1A0;
        v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0x80000ULL)))) | ((unsigned int)(result)));
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 2);
        a1 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
        result = KiCopyAffinityEx(a1, a2, a3, a4);
    }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10378765)) - 3)) & (0xFFFFFFFCULL)) != 0) goto loc_005E0E09;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10378765)))) == 4) goto loc_005E0E09;
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)((unsigned int)(0x8000ULL))));
    v_stack_m2B8 = (unsigned int)((unsigned int)(a16));
    v_stack_m2C0 = (unsigned int)((unsigned int)(v_stack_m240));
    v_stack_m2C8 = (unsigned int)((unsigned int)(a13));
    result = PpmHeteroRestrictToFavoredClassEx(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m268, a14, a15);
    if (v_stack_m268 == ((unsigned __int8)(v_stack_m267))) goto loc_005E0E09;
    v_stack_m267 = (unsigned __int8)(v_stack_m268);
    result = KeCountSetBitsAffinityEx(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m268, a14, a15);
    a2 = 0;
    v_stack_m250 = (unsigned int)(result);
    result = 0;
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 8);
    v_stack_m1E8 = 0;
    v_stack_m1F8 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
    result = KeEnumerateNextProcessor(v_stack_m228, v_stack_m1F8, a14, a15);
    if ((unsigned int)(result) != 0) goto loc_005E0DFA;
loc_005E0DDD:
    if (0 == 0) goto loc_005E0DF6;
    v_rbx = (0) - (result + 1);
    result = KeEnumerateNextProcessor(v_stack_m228, v_stack_m1F8, a14, a15);
    if ((unsigned int)(result) == 0) goto loc_005E0DDD;
loc_005E0DF6:
loc_005E0DFA:
    result = PpmEventHeteroFavoredCoreRotationChange((unsigned int)(v_stack_m250), (unsigned int)(v_stack_m228), a14, a15);
loc_005E0E09:
    result = KeAndAffinityEx2(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m1D8, v_stack_m1A0, a15);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1D8, v_stack_m1A0, a15);
    a1 = 0;
    if ((unsigned int)(result) == 0) {
        result = 0x1000ULL;
        a3 = v_stack_m1A0;
        a1 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 2);
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
        result = KiCopyAffinityEx(a1, a2, a3, a15);
        a1 = 0;
    }
    if ((*(unsigned __int8 *)(a12 + 16)) != 0) goto loc_005E0E83;
    result = KeSubtractAffinityEx2(*(unsigned __int64 *)(v_rip + 8942523) + 2904, v_stack_m1D0, v_stack_m1A0, a15);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1D0, v_stack_m1A0, a15);
    if ((unsigned int)(result) == 0) {
        result = 0x2000ULL;
        a3 = v_stack_m1A0;
        v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
        a2 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 2);
        a1 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
        result = KiCopyAffinityEx(a1, a2, a3, a15);
    }
    v_rbx = 0;
    v_stack_m1E8 = 0;
    v_stack_m1F0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8942523) + 2904 + 8);
    v_stack_m1F8 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
    goto loc_005E0E9F;
loc_005E0E97:
    if (((unsigned int)((unsigned int)(v_stack_m260))) >= v_stack_m228) goto loc_005E0EB2;
loc_005E0E9F:
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, a3, a15);
    if ((unsigned int)(result) == 0) goto loc_005E0E97;
    goto loc_005E0EB7;
loc_005E0EB2:
    if (((unsigned int)(result)) == -1) {
        a1 = *(unsigned __int64 *)(v_rip + 8942523) + 2904;
        result = KeFindFirstSetRightAffinityEx(a1, v_stack_m1F8, a3, a15);
    }
    result = KeGetPrcb((unsigned int)((unsigned int)(result)), v_stack_m1F8, a3, a15);
    a2 = 0;
    a3 = (*(unsigned __int16 *)(v_stack_m258)) << (3);
    result = memset(v_stack_m198, a2, a3, a15);
    a1 = 0;
    *(unsigned __int16 *)(v_stack_m258) = 1;
    if ((*(unsigned __int8 *)(v_rip + 9598165)) == 0) goto loc_005E0EFC;
    goto loc_005E0F03;
loc_005E0EFC:
loc_005E0F03:
    result = KeAddGroupAffinityEx(v_stack_m258, *(unsigned __int8 *)(result + 208), *(unsigned __int64 *)(result + 200), a15);
    result = KeSubtractAffinityEx2(a9, v_stack_m258, a9, a15);
    if (((unsigned int)((unsigned int)(v_stack_m240))) < ((unsigned int)((unsigned int)(a5)))) goto loc_005E1001;
    result = KeOrAffinityEx2(v_stack_m1C8, v_stack_m258, v_stack_m1C8, a15);
    result = KiCopyAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, a15);
    v_stack_m250 = *(unsigned __int64 *)(v_rip + 9598056);
    if (*(unsigned __int64 *)(v_rip + 9598056) == 0) goto loc_005E10BB;
    v_stack_m1B0 = *(unsigned __int64 *)(v_rip + 9598020);
    if (*(unsigned __int64 *)(v_rip + 9598020) == 0) goto loc_005E10BB;
    result = KeIsEmptyAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, a15);
    if ((unsigned int)(result) != 0) goto loc_005E10BB;
loc_005E0FA1:
    result = KeFindFirstSetRightAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, a15);
    v_stack_m260 = (unsigned int)((unsigned int)((unsigned int)(result)));
    *(unsigned int *)(v_stack_m250 + (unsigned int)((unsigned int)(result)) * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9597947)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9597947)))) != (*(unsigned int *)(v_stack_m1B0 + (unsigned int)((unsigned int)(result)) * 4))) {
        *(unsigned __int8 *)(v_rip + 9597944) = (unsigned __int8)(result + 1);
    }
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9597947))) + 1);
    *(unsigned int *)(v_rip + 9597913) = (unsigned int)(result);
    result = KeRemoveProcessorAffinityEx(v_stack_m158, (unsigned int)((unsigned int)(result)), v_stack_m258, a15);
    result = KeIsEmptyAffinityEx(v_stack_m158, (unsigned int)((unsigned int)(result)), v_stack_m258, a15);
    if ((unsigned int)(result) == 0) goto loc_005E0FA1;
    goto loc_005E10BB;
loc_005E1001:
    a3 = 0;
    if (v_stack_m190 == 0) goto loc_005E10BB;
    if ((*(unsigned int *)(v_stack_m200 + 1232)) != 3) goto loc_005E10BB;
    result = (unsigned int)(((unsigned int)(v_stack_m1E0)) - ((unsigned int)(v_stack_m158)));
    v_stack_m1E8 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result)) - 1) + ((unsigned int)(result)));
    v_stack_m250 = (unsigned int)(a1);
    v_stack_m1F0 = *(unsigned __int64 *)(v_stack_m198);
    v_stack_m1F8 = v_stack_m258;
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, a3, a15);
    if ((unsigned int)(result) != 0) goto loc_005E10A7;
loc_005E1060:
    if (((unsigned int)((unsigned int)(v_stack_m250))) >= ((unsigned int)(*(unsigned __int16 *)(v_stack_m200 + 10)))) goto loc_005E1084;
    if ((*(unsigned int *)(v_stack_m190 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m250))) * 4)) != ((unsigned int)((unsigned int)(v_stack_m260)))) {
        *(unsigned int *)(v_stack_m190 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m250))) * 4) = (unsigned int)((unsigned int)(v_stack_m260));
        *(unsigned __int8 *)(v_stack_m200 + 1254) = 1;
    }
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m250)) - 1);
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, a3, a15);
    if ((unsigned int)(result) == 0) goto loc_005E1060;
loc_005E10A7:
    result = KeCountSetBitsAffinityEx(v_stack_m258, v_stack_m1F8, a3, a15);
loc_005E10BB:
    result = KeCountSetBitsAffinityEx(v_stack_m258, v_stack_m1F8, a3, a15);
    a2 = (unsigned int)(((unsigned int)(v_stack_m240)) + ((unsigned int)(result)));
    v_stack_m278 = v_stack_m248;
    v_stack_m280 = v_stack_m1B8;
    v_stack_m288 = v_stack_m1C0;
    v_stack_m290 = v_stack_m178;
    v_stack_m298 = v_stack_m230;
    v_stack_m2A0 = v_stack_m238;
    v_stack_m2A8 = v_stack_m258;
    v_stack_m2B0 = a9;
    v_stack_m2B8 = v_stack_m180;
    v_stack_m240 = (unsigned int)(a2);
    v_stack_m2C0 = (unsigned int)(v_r15);
    v_stack_m2C8 = (unsigned int)((unsigned int)(a13));
    result = PpmEventTraceCoreParkingSelectionEx(v_stack_m248, (unsigned int)(a5), (unsigned int)(a6), (unsigned int)((unsigned int)(a2)));
    result = 0;
    a3 = (*(unsigned __int16 *)(v_stack_m180)) << (3);
    a2 = 0;
    result = memset(v_stack_m180 + 8, a2, a3, (unsigned int)((unsigned int)(a2)));
    *(unsigned __int16 *)(v_stack_m180) = 1;
    result = KeSubtractAffinityEx2(v_stack_m178, result + 35856, v_stack_m178, (unsigned int)((unsigned int)(a2)));
    result = KeGetTopologySiblingAffinityForProcessor(result, 5, v_stack_m158, (unsigned int)((unsigned int)(a2)));
    if ((unsigned int)(v_stack_m266) == 0) goto loc_005E11D7;
    a1 = (unsigned int)((v_stack_m266) - (1));
    if (condition_is_equal) goto loc_005E11A8;
    if (((unsigned int)(a1)) != 1) goto loc_005E11D7;
    result = KiSubtractAffinityEx(v_stack_m158, v_stack_m258, v_stack_m158, v_stack_m156);
    goto loc_005E11C2;
loc_005E11A8:
    result = KiComplementAffinityEx(v_stack_m158, v_stack_m156, v_stack_m158, v_stack_m156);
loc_005E11C2:
    result = PpmParkBuildTopologyCandidatesEx(v_stack_m238, v_stack_m158, a9, v_stack_m156);
    goto loc_005E11F7;
loc_005E11D7:
    a2 = 0;
    a3 = (*(unsigned __int16 *)(v_stack_m238)) << (3);
    result = memset(v_stack_m170, a2, a3, v_stack_m156);
    *(unsigned __int16 *)(v_stack_m238) = 1;
loc_005E11F7:
    result = KeGetTopologySiblingAffinityForProcessor(result, 2, v_stack_m158, v_stack_m156);
    if ((unsigned int)(v_stack_m265) == 0) goto loc_005E126D;
    a1 = (unsigned int)((v_stack_m265) - (1));
    if (condition_is_equal) goto loc_005E123E;
    if (((unsigned int)(a1)) != 1) goto loc_005E126D;
    result = KiSubtractAffinityEx(v_stack_m158, v_stack_m258, v_stack_m158, v_stack_m156);
    goto loc_005E1258;
loc_005E123E:
    result = KiComplementAffinityEx(v_stack_m158, v_stack_m156, v_stack_m158, v_stack_m156);
loc_005E1258:
    result = PpmParkBuildTopologyCandidatesEx(v_stack_m230, v_stack_m158, a9, v_stack_m156);
    goto loc_005E1290;
loc_005E126D:
    a2 = 0;
    a3 = (*(unsigned __int16 *)(v_stack_m230)) << (3);
    result = memset(v_stack_m168, a2, a3, v_stack_m156);
    *(unsigned __int16 *)(v_stack_m230) = 1;
loc_005E1290:
    if ((unsigned int)(v_stack_m264) == 0) goto loc_005E12C0;
    a1 = (unsigned int)((v_stack_m264) - (1));
    if (condition_is_equal) goto loc_005E12C0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_005E12C0;
    if (((unsigned int)(a1)) != 1) goto loc_005E12C0;
    if ((*(unsigned __int16 *)(v_stack_m1C0)) <= ((unsigned __int16)(*(unsigned __int8 *)(result + 208)))) goto loc_005E12DF;
    goto loc_005E12D7;
loc_005E12C0:
    if ((*(unsigned __int16 *)(v_stack_m1C0)) <= ((unsigned __int16)(*(unsigned __int8 *)(result + 208)))) goto loc_005E12DF;
loc_005E12D7:
    result = ~(*(unsigned __int64 *)(result + 36448));
loc_005E12DF:
    result = KeIsEmptyAffinityEx(v_stack_m180, a2, a3, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E13F1;
    result = KeIsEmptyAffinityEx(v_stack_m178, a2, a3, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E13E1;
    result = KeIsEmptyAffinityEx(v_stack_m1C0, a2, a3, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E139B;
    result = KeAndAffinityEx2(a9, v_stack_m218, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E1329;
    goto loc_005E1396;
loc_005E1329:
    result = KeAndAffinityEx2(a9, v_stack_m210, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E1343;
    goto loc_005E1396;
loc_005E1343:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10370259)))) & (8)) == 0) goto loc_005E136A;
    result = KeAndAffinityEx2(a9, v_stack_m160, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E139B;
    goto loc_005E1396;
loc_005E136A:
    result = KeAndAffinityEx2(a9, v_stack_m208, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E137E;
    goto loc_005E1396;
loc_005E137E:
    result = KeAndAffinityEx2(a9, v_stack_m220, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) == 0) goto loc_005E139B;
loc_005E1396:
loc_005E139B:
    result = KiCopyAffinityEx(v_stack_m178, *(unsigned __int16 *)(v_stack_m178 + 2), v_stack_m1C0, v_stack_m156);
    result = KiAndAffinityExNoResult(v_stack_m178, v_stack_m238, v_stack_m1C0, v_stack_m156);
    if ((unsigned int)(result) != 0) {
        a3 = v_stack_m178;
        a1 = v_stack_m178;
        result = KeAndAffinityEx2(a1, v_stack_m238, a3, v_stack_m156);
    }
    result = KiAndAffinityExNoResult(v_stack_m178, v_stack_m230, a3, v_stack_m156);
    if ((unsigned int)(result) != 0) {
        a3 = v_stack_m178;
        a1 = v_stack_m178;
        result = KeAndAffinityEx2(a1, v_stack_m230, a3, v_stack_m156);
    }
    result = KiCopyAffinityEx(v_stack_m180, *(unsigned __int16 *)(v_stack_m180 + 2), v_stack_m178, v_stack_m156);
loc_005E13F1:
    if (v_stack_m240 < ((unsigned int)((unsigned int)(a6)))) goto loc_005E0CE4;
    goto loc_005E1412;
loc_005E1402:
    result = KiCopyAffinityEx(a9, *(unsigned __int16 *)(a9 + 2), v_stack_m248, v_stack_m156);
loc_005E1412:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int16 *)(a9 + 2), v_stack_m248, v_stack_m156);
    v_rsp = (v_rsp) + (688);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkComputeUnparkMaskEx(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, void *Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, void *Arg9, int64_t Arg10, void *Arg11, void *Arg12, uint32_t Arg13, uint8_t Arg14, uint8_t Arg15, uint32_t Arg16)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg12 = (uint8_t *)Arg12;

    int64_t result;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m150;
    uint16_t v_stack_m156;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint16_t v_stack_m1E2;
    uint32_t v_stack_m1E6;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m260;
    uint8_t v_stack_m264;
    uint8_t v_stack_m265;
    uint8_t v_stack_m266;
    uint8_t v_stack_m267;
    uint8_t v_stack_m268;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x82A13A)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m250 = Arg7;
    v_stack_m218 = Arg8;
    v_stack_m1B0 = Arg3;
    v_stack_m248 = Arg2;
    Arg2 = 0;
    v_stack_m200 = Arg1;
    v_stack_m1C8 = Arg10;
    v_stack_m1B8 = Arg4;
    v_stack_m188 = Arg11;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    Arg3 = 0;
    result = ((int32_t)(*(uint32_t *)(v_rip + 0x92C791))) * ((int32_t)(*(uint32_t *)(v_rip + 0x92C791)));
    v_stack_m1E6 = 0;
    v_stack_m240 = result;
    v_stack_m1E2 = 0;
    v_stack_m260 = 0;
    v_stack_m266 = (uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0x827D0F) * 1 + 0x1F1));
    v_stack_m1E0 = (uint32_t)(*(uint16_t *)(arg1 + 0x4E4));
    v_stack_m190 = *(uint64_t *)(arg1 + 0x4E8);
    v_stack_m228 = *(uint64_t *)(v_rip + 0x827D0F);
    v_stack_m265 = (uint8_t)(*(uint8_t *)(result + *(uint64_t *)(v_rip + 0x827D0F) * 1 + 0x1F0));
    Arg2 = 0;
    v_stack_m158 = 0x200001ULL;
    v_stack_m1A8 = *(uint64_t *)(v_rip + 0x8873BB) + 2376;
    v_stack_m180 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
    v_stack_m1D8 = *(uint64_t *)(v_rip + 0x8873BB) + 2640;
    v_stack_m1C0 = *(uint64_t *)(v_rip + 0x8873BB) + 3696;
    v_stack_m238 = *(uint64_t *)(v_rip + 0x8873BB) + 3168;
    v_stack_m178 = *(uint64_t *)(v_rip + 0x8873BB) + 5808;
    v_stack_m1D0 = *(uint64_t *)(v_rip + 0x8873BB) + 3960;
    v_stack_m1A0 = *(uint64_t *)(v_rip + 0x8873BB) + 4224;
    v_stack_m230 = *(uint64_t *)(v_rip + 0x8873BB) + 4752;
    v_stack_m208 = *(uint64_t *)(v_rip + 0x8873BB) + 5016;
    v_stack_m220 = *(uint64_t *)(v_rip + 0x8873BB) + 5280;
    v_stack_m258 = *(uint64_t *)(v_rip + 0x8873BB) + 5544;
    v_stack_m210 = *(uint64_t *)(v_rip + 0x8873BB) + 6072;
    result = memset(v_stack_m150, Arg2, 256, Arg4);
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x948)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 2376 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x948) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xA50)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 2640 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xA50) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 2904 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xC60)) << (3);
    Arg2 = 0;
    v_stack_m170 = *(uint64_t *)(v_rip + 0x8873BB) + 3168 + 8;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 3168 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xC60) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xE70)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 3696 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xE70) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xF78)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 3960 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xF78) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1080)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 4224 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1080) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1290)) << (3);
    Arg2 = 0;
    v_stack_m168 = *(uint64_t *)(v_rip + 0x8873BB) + 4752 + 8;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 4752 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1290) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1398)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 5016 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x1398) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x14A0)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 5280 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x14A0) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x15A8)) << (3);
    Arg2 = 0;
    v_stack_m198 = *(uint64_t *)(v_rip + 0x8873BB) + 5544 + 8;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 5544 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x15A8) = 1;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x16B0)) << (3);
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 5808 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x16B0) = 1;
    Arg3 = (*(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x17B8)) << (3);
    Arg2 = 0;
    result = memset(*(uint64_t *)(v_rip + 0x8873BB) + 6072 + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x17B8) = 1;
    local_rbx = (*(uint64_t *)(v_rip + 0x8873BB)) + (0xD68ULL);
    v_stack_m160 = local_rbx;
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(local_rbx)) << (3);
    result = memset(local_rbx + 8, Arg2, Arg3, Arg4);
    *(uint16_t *)(local_rbx) = 1;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(local_rbx + 8, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E09B5;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E46B2)))) & (8)) == 0) goto loc_005E09A5;
    Arg2 = 0;
    *(uint64_t *)(local_rbx) = 0x200001ULL;
    result = memset(local_rbx + 8, Arg2, 256, Arg4);
    Arg1 = (local_rbx + 8) * ((int32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m200 + 0x500) + 0x4)));
    Arg3 = (*(uint64_t *)(v_stack_m200 + 0x500) + 16) + (Arg1);
    goto loc_005E09A9;
loc_005E09A5:
loc_005E09A9:
    result = KiCopyAffinityEx(local_rbx, *(uint16_t *)(local_rbx + 0x2), v_stack_m248, Arg4);
loc_005E09B5:
    v_stack_m264 = (uint8_t)(*(uint8_t *)(v_stack_m240 + v_stack_m228 * 1 + 0x1F2));
    result = KeAndAffinityEx2(v_stack_m1B0, v_stack_m248, v_stack_m1D0, Arg4);
    Arg3 = (*(uint16_t *)(arg9)) << (3);
    Arg2 = 0;
    result = memset(Arg9 + 8, Arg2, Arg3, Arg4);
    Arg2 = 0;
    *(uint16_t *)(arg9) = 1;
    Arg3 = (*(uint16_t *)(v_stack_m1C8)) << (3);
    result = memset(v_stack_m1C8 + 8, Arg2, Arg3, Arg4);
    Arg1 = 0;
    *(uint16_t *)(v_stack_m1C8) = 1;
    if (Arg6 == 0) goto loc_005E1402;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_005E1402;
    result = *(uint64_t *)(v_rip + 0x92D84D);
    if (*(uint64_t *)(v_rip + 0x92D84D) != 0) {
        Arg1 = v_stack_m210;
        Arg3 = (uint32_t)((uint32_t)(Arg5));
        Arg4 = v_stack_m248;
        Arg2 = *(uint64_t *)(v_rip + 0x92A812);
        v_stack_m2B0 = Arg1;
        Arg1 = v_stack_m220;
        v_stack_m2B8 = Arg1;
        Arg1 = v_stack_m218;
        v_stack_m2C0 = Arg1;
        Arg1 = v_stack_m250;
        v_stack_m2C8 = Arg1;
        Arg1 = 0;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m210;
        Arg4 = v_stack_m218;
        Arg3 = v_stack_m250;
        Arg2 = Arg5;
        Arg1 = v_stack_m248;
        v_stack_m2C0 = result;
        result = v_stack_m220;
        v_stack_m2C8 = result;
        result = PpmEventParkNodePreferenceEx(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_m158;
        Arg1 = v_stack_m150;
        Arg3 = (Arg3) << (3);
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg4 = v_stack_m156;
        Arg3 = v_stack_m158;
        Arg2 = v_stack_m218;
        result = 1;
        Arg1 = v_stack_m250;
        v_stack_m158 = (uint16_t)(result);
        result = KiOrAffinityEx(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_m220;
        Arg2 = v_stack_m158;
        Arg1 = Arg3;
        result = KeSubtractAffinityEx2(Arg1, Arg2, Arg3, Arg4);
        Arg3 = v_stack_m210;
        Arg2 = v_stack_m158;
        Arg1 = Arg3;
        result = KeSubtractAffinityEx2(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeSubtractAffinityEx2(v_stack_m248, v_stack_m250, v_stack_m208, Arg4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m218, v_stack_m208, Arg4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m220, v_stack_m208, Arg4);
    result = KeSubtractAffinityEx2(v_stack_m208, v_stack_m210, v_stack_m208, Arg4);
    result = KiCopyAffinityEx(Arg9, *(uint16_t *)(arg9 + 0x2), v_stack_m248, Arg4);
    result = KeAndAffinityEx2(Arg9, v_stack_m218, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0B7A;
    goto loc_005E0C3B;
loc_005E0B7A:
    result = KeAndAffinityEx2(Arg9, v_stack_m210, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0B97;
    goto loc_005E0C36;
loc_005E0B97:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E447F)))) & (8)) == 0) goto loc_005E0C04;
    result = Feature_PpmFixContainmentCandidateListInitialization__private_IsEnabledDeviceUsageNoInline(Arg9, v_stack_m210, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) {
        Arg2 = 0;
        *(uint64_t *)(local_rbx) = 0x200001ULL;
        Arg3 = 256;
        Arg1 = local_rbx + 8;
        result = memset(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m200;
        Arg2 = *(uint64_t *)(result + 0x500);
        result = (int32_t)(*(uint32_t *)(Arg2 + 0x4));
        Arg3 = Arg2 + 16;
        Arg2 = *(uint16_t *)(local_rbx + 0x2);
        Arg1 = (Arg1) * (result);
        Arg3 = (Arg3) + (Arg1);
        Arg1 = local_rbx;
        result = KiCopyAffinityEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAndAffinityEx2(Arg9, local_rbx, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0C3B;
    goto loc_005E0C36;
loc_005E0C04:
    result = KeAndAffinityEx2(Arg9, v_stack_m208, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0C1E;
    goto loc_005E0C36;
loc_005E0C1E:
    result = KeAndAffinityEx2(Arg9, v_stack_m220, *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    if ((uint32_t)(result) == 0) goto loc_005E0C3B;
loc_005E0C36:
loc_005E0C3B:
    result = KiCopyAffinityEx(*(uint64_t *)(v_rip + 0x8873BB) + 5808, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0x16B0 + 0x2), *(uint64_t *)(v_rip + 0x8873BB) + 3696, Arg4);
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(v_stack_m238)) << (3);
    result = memset(v_stack_m170, Arg2, Arg3, Arg4);
    Arg2 = 0;
    *(uint16_t *)(v_stack_m238) = 1;
    Arg3 = (*(uint16_t *)(v_stack_m230)) << (3);
    result = memset(v_stack_m168, Arg2, Arg3, Arg4);
    *(uint16_t *)(v_stack_m230) = 1;
    result = KiCopyAffinityEx(*(uint64_t *)(v_rip + 0x8873BB) + 2904, *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x2), *(uint64_t *)(v_rip + 0x8873BB) + 5808, Arg4);
    result = KeAndAffinityEx2(v_stack_m1D0, v_stack_m1B8, v_stack_m1A8, Arg4);
    result = KeSubtractAffinityEx2(v_stack_m248, v_stack_m1D0, v_stack_m1D8, Arg4);
    result = KeAndAffinityEx2(v_stack_m1D8, v_stack_m1B8, v_stack_m1D8, Arg4);
    local_rbx = 0;
    v_stack_m267 = 255;
    v_stack_m268 = 255;
    v_stack_m240 = 0;
    v_stack_m228 = 0;
    if (Arg6 <= 0) goto loc_005E1412;
loc_005E0CE4:
    result = KeIsEmptyAffinityEx(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m1B8, v_stack_m1D8, Arg4);
    if ((uint32_t)(result) != 0) goto loc_005E1412;
    result = KeAndAffinityEx2(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m1A8, v_stack_m1A0, Arg4);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1A8, v_stack_m1A0, Arg4);
    local_r15 = (uint32_t)((uint32_t)((uint32_t)(0x80000ULL)));
    if ((uint32_t)(result) == 0) {
        result = 0x20000ULL;
        Arg3 = v_stack_m1A0;
        local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0x80000ULL)))) | ((uint32_t)(result)));
        Arg2 = *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x2);
        Arg1 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
        result = KiCopyAffinityEx(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E5E0D)) - 3)) & (0xFFFFFFFCULL)) != 0) goto loc_005E0E09;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E5E0D)))) == 4) goto loc_005E0E09;
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)((uint32_t)(0x8000ULL))));
    v_stack_m2B8 = (uint32_t)((uint32_t)(Arg16));
    v_stack_m2C0 = (uint32_t)((uint32_t)(v_stack_m240));
    v_stack_m2C8 = (uint32_t)((uint32_t)(Arg13));
    result = PpmHeteroRestrictToFavoredClassEx(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m268, Arg14, Arg15);
    if (v_stack_m268 == ((uint8_t)(v_stack_m267))) goto loc_005E0E09;
    v_stack_m267 = (uint8_t)(v_stack_m268);
    result = KeCountSetBitsAffinityEx(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m268, Arg14, Arg15);
    Arg2 = 0;
    v_stack_m250 = (uint32_t)(result);
    result = 0;
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x8);
    v_stack_m1E8 = 0;
    v_stack_m1F8 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
    result = KeEnumerateNextProcessor(v_stack_m228, v_stack_m1F8, Arg14, Arg15);
    if ((uint32_t)(result) != 0) goto loc_005E0DFA;
loc_005E0DDD:
    if (0 == 0) goto loc_005E0DF6;
    local_rbx = (0) - (result + 1);
    result = KeEnumerateNextProcessor(v_stack_m228, v_stack_m1F8, Arg14, Arg15);
    if ((uint32_t)(result) == 0) goto loc_005E0DDD;
loc_005E0DF6:
loc_005E0DFA:
    result = PpmEventHeteroFavoredCoreRotationChange((uint32_t)(v_stack_m250), (uint32_t)(v_stack_m228), Arg14, Arg15);
loc_005E0E09:
    result = KeAndAffinityEx2(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m1D8, v_stack_m1A0, Arg15);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1D8, v_stack_m1A0, Arg15);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) {
        result = 0x1000ULL;
        Arg3 = v_stack_m1A0;
        Arg1 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
        Arg2 = *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x2);
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
        result = KiCopyAffinityEx(Arg1, Arg2, Arg3, Arg15);
        Arg1 = 0;
    }
    if ((*(uint8_t *)(arg12 + 0x10)) != 0) goto loc_005E0E83;
    result = KeSubtractAffinityEx2(*(uint64_t *)(v_rip + 0x8873BB) + 2904, v_stack_m1D0, v_stack_m1A0, Arg15);
    result = KeIsEmptyAffinityEx(v_stack_m1A0, v_stack_m1D0, v_stack_m1A0, Arg15);
    if ((uint32_t)(result) == 0) {
        result = 0x2000ULL;
        Arg3 = v_stack_m1A0;
        local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
        Arg2 = *(uint16_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x2);
        Arg1 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
        result = KiCopyAffinityEx(Arg1, Arg2, Arg3, Arg15);
    }
    local_rbx = 0;
    v_stack_m1E8 = 0;
    v_stack_m1F0 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x8873BB) + 0xB58 + 0x8);
    v_stack_m1F8 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
    goto loc_005E0E9F;
loc_005E0E97:
    if (((uint32_t)((uint32_t)(v_stack_m260))) >= v_stack_m228) goto loc_005E0EB2;
loc_005E0E9F:
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, Arg3, Arg15);
    if ((uint32_t)(result) == 0) goto loc_005E0E97;
    goto loc_005E0EB7;
loc_005E0EB2:
    if (((uint32_t)(result)) == -1) {
        Arg1 = *(uint64_t *)(v_rip + 0x8873BB) + 2904;
        result = KeFindFirstSetRightAffinityEx(Arg1, v_stack_m1F8, Arg3, Arg15);
    }
    result = KeGetPrcb((uint32_t)((uint32_t)(result)), v_stack_m1F8, Arg3, Arg15);
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(v_stack_m258)) << (3);
    result = memset(v_stack_m198, Arg2, Arg3, Arg15);
    Arg1 = 0;
    *(uint16_t *)(v_stack_m258) = 1;
    if ((*(uint8_t *)(v_rip + 0x9274D5)) == 0) goto loc_005E0EFC;
    goto loc_005E0F03;
loc_005E0EFC:
loc_005E0F03:
    result = KeAddGroupAffinityEx(v_stack_m258, *(uint8_t *)(result + 0xD0), *(uint64_t *)(result + 0xC8), Arg15);
    result = KeSubtractAffinityEx2(Arg9, v_stack_m258, Arg9, Arg15);
    if (((uint32_t)((uint32_t)(v_stack_m240))) < ((uint32_t)((uint32_t)(Arg5)))) goto loc_005E1001;
    result = KeOrAffinityEx2(v_stack_m1C8, v_stack_m258, v_stack_m1C8, Arg15);
    result = KiCopyAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, Arg15);
    v_stack_m250 = *(uint64_t *)(v_rip + 0x927468);
    if (*(uint64_t *)(v_rip + 0x927468) == 0) goto loc_005E10BB;
    v_stack_m1B0 = *(uint64_t *)(v_rip + 0x927444);
    if (*(uint64_t *)(v_rip + 0x927444) == 0) goto loc_005E10BB;
    result = KeIsEmptyAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, Arg15);
    if ((uint32_t)(result) != 0) goto loc_005E10BB;
loc_005E0FA1:
    result = KeFindFirstSetRightAffinityEx(v_stack_m158, v_stack_m156, v_stack_m258, Arg15);
    v_stack_m260 = (uint32_t)((uint32_t)((uint32_t)(result)));
    *(uint32_t *)(v_stack_m250 + (uint32_t)((uint32_t)(result)) * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9273FB)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9273FB)))) != (*(uint32_t *)(v_stack_m1B0 + (uint32_t)((uint32_t)(result)) * 4))) {
        *(uint8_t *)(v_rip + 0x9273F8) = (uint8_t)(result + 1);
    }
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9273FB))) + 1);
    *(uint32_t *)(v_rip + 0x9273D9) = (uint32_t)(result);
    result = KeRemoveProcessorAffinityEx(v_stack_m158, (uint32_t)((uint32_t)(result)), v_stack_m258, Arg15);
    result = KeIsEmptyAffinityEx(v_stack_m158, (uint32_t)((uint32_t)(result)), v_stack_m258, Arg15);
    if ((uint32_t)(result) == 0) goto loc_005E0FA1;
    goto loc_005E10BB;
loc_005E1001:
    Arg3 = 0;
    if (v_stack_m190 == 0) goto loc_005E10BB;
    if ((*(uint32_t *)(v_stack_m200 + 0x4D0)) != 3) goto loc_005E10BB;
    result = (uint32_t)(((uint32_t)(v_stack_m1E0)) - ((uint32_t)(v_stack_m158)));
    v_stack_m1E8 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result)) - 1) + ((uint32_t)(result)));
    v_stack_m250 = (uint32_t)(Arg1);
    v_stack_m1F0 = *(uint64_t *)(v_stack_m198);
    v_stack_m1F8 = v_stack_m258;
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, Arg3, Arg15);
    if ((uint32_t)(result) != 0) goto loc_005E10A7;
loc_005E1060:
    if (((uint32_t)((uint32_t)(v_stack_m250))) >= ((uint32_t)(*(uint16_t *)(v_stack_m200 + 0xA)))) goto loc_005E1084;
    if ((*(uint32_t *)(v_stack_m190 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m250))) * 4)) != ((uint32_t)((uint32_t)(v_stack_m260)))) {
        *(uint32_t *)(v_stack_m190 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m250))) * 4) = (uint32_t)((uint32_t)(v_stack_m260));
        *(uint8_t *)(v_stack_m200 + 0x4E6) = 1;
    }
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m250)) - 1);
    result = KeEnumerateNextProcessor(v_stack_m260, v_stack_m1F8, Arg3, Arg15);
    if ((uint32_t)(result) == 0) goto loc_005E1060;
loc_005E10A7:
    result = KeCountSetBitsAffinityEx(v_stack_m258, v_stack_m1F8, Arg3, Arg15);
loc_005E10BB:
    result = KeCountSetBitsAffinityEx(v_stack_m258, v_stack_m1F8, Arg3, Arg15);
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m240)) + ((uint32_t)(result)));
    v_stack_m278 = v_stack_m248;
    v_stack_m280 = v_stack_m1B8;
    v_stack_m288 = v_stack_m1C0;
    v_stack_m290 = v_stack_m178;
    v_stack_m298 = v_stack_m230;
    v_stack_m2A0 = v_stack_m238;
    v_stack_m2A8 = v_stack_m258;
    v_stack_m2B0 = Arg9;
    v_stack_m2B8 = v_stack_m180;
    v_stack_m240 = (uint32_t)(Arg2);
    v_stack_m2C0 = (uint32_t)(local_r15);
    v_stack_m2C8 = (uint32_t)((uint32_t)(Arg13));
    result = PpmEventTraceCoreParkingSelectionEx(v_stack_m248, (uint32_t)(Arg5), (uint32_t)(Arg6), (uint32_t)((uint32_t)(Arg2)));
    result = 0;
    Arg3 = (*(uint16_t *)(v_stack_m180)) << (3);
    Arg2 = 0;
    result = memset(v_stack_m180 + 8, Arg2, Arg3, (uint32_t)((uint32_t)(Arg2)));
    *(uint16_t *)(v_stack_m180) = 1;
    result = KeSubtractAffinityEx2(v_stack_m178, result + 35856, v_stack_m178, (uint32_t)((uint32_t)(Arg2)));
    result = KeGetTopologySiblingAffinityForProcessor(result, 5, v_stack_m158, (uint32_t)((uint32_t)(Arg2)));
    if ((uint32_t)(v_stack_m266) == 0) goto loc_005E11D7;
    Arg1 = (uint32_t)((v_stack_m266) - (1));
    if (condition_is_equal) goto loc_005E11A8;
    if (((uint32_t)(Arg1)) != 1) goto loc_005E11D7;
    result = KiSubtractAffinityEx(v_stack_m158, v_stack_m258, v_stack_m158, v_stack_m156);
    goto loc_005E11C2;
loc_005E11A8:
    result = KiComplementAffinityEx(v_stack_m158, v_stack_m156, v_stack_m158, v_stack_m156);
loc_005E11C2:
    result = PpmParkBuildTopologyCandidatesEx(v_stack_m238, v_stack_m158, Arg9, v_stack_m156);
    goto loc_005E11F7;
loc_005E11D7:
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(v_stack_m238)) << (3);
    result = memset(v_stack_m170, Arg2, Arg3, v_stack_m156);
    *(uint16_t *)(v_stack_m238) = 1;
loc_005E11F7:
    result = KeGetTopologySiblingAffinityForProcessor(result, 2, v_stack_m158, v_stack_m156);
    if ((uint32_t)(v_stack_m265) == 0) goto loc_005E126D;
    Arg1 = (uint32_t)((v_stack_m265) - (1));
    if (condition_is_equal) goto loc_005E123E;
    if (((uint32_t)(Arg1)) != 1) goto loc_005E126D;
    result = KiSubtractAffinityEx(v_stack_m158, v_stack_m258, v_stack_m158, v_stack_m156);
    goto loc_005E1258;
loc_005E123E:
    result = KiComplementAffinityEx(v_stack_m158, v_stack_m156, v_stack_m158, v_stack_m156);
loc_005E1258:
    result = PpmParkBuildTopologyCandidatesEx(v_stack_m230, v_stack_m158, Arg9, v_stack_m156);
    goto loc_005E1290;
loc_005E126D:
    Arg2 = 0;
    Arg3 = (*(uint16_t *)(v_stack_m230)) << (3);
    result = memset(v_stack_m168, Arg2, Arg3, v_stack_m156);
    *(uint16_t *)(v_stack_m230) = 1;
loc_005E1290:
    if ((uint32_t)(v_stack_m264) == 0) goto loc_005E12C0;
    Arg1 = (uint32_t)((v_stack_m264) - (1));
    if (condition_is_equal) goto loc_005E12C0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_005E12C0;
    if (((uint32_t)(Arg1)) != 1) goto loc_005E12C0;
    if ((*(uint16_t *)(v_stack_m1C0)) <= ((uint16_t)(*(uint8_t *)(result + 0xD0)))) goto loc_005E12DF;
    goto loc_005E12D7;
loc_005E12C0:
    if ((*(uint16_t *)(v_stack_m1C0)) <= ((uint16_t)(*(uint8_t *)(result + 0xD0)))) goto loc_005E12DF;
loc_005E12D7:
    result = ~(*(uint64_t *)(result + 0x8E60));
loc_005E12DF:
    result = KeIsEmptyAffinityEx(v_stack_m180, Arg2, Arg3, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E13F1;
    result = KeIsEmptyAffinityEx(v_stack_m178, Arg2, Arg3, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E13E1;
    result = KeIsEmptyAffinityEx(v_stack_m1C0, Arg2, Arg3, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E139B;
    result = KeAndAffinityEx2(Arg9, v_stack_m218, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E1329;
    goto loc_005E1396;
loc_005E1329:
    result = KeAndAffinityEx2(Arg9, v_stack_m210, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E1343;
    goto loc_005E1396;
loc_005E1343:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E3CD3)))) & (8)) == 0) goto loc_005E136A;
    result = KeAndAffinityEx2(Arg9, v_stack_m160, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E139B;
    goto loc_005E1396;
loc_005E136A:
    result = KeAndAffinityEx2(Arg9, v_stack_m208, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E137E;
    goto loc_005E1396;
loc_005E137E:
    result = KeAndAffinityEx2(Arg9, v_stack_m220, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) == 0) goto loc_005E139B;
loc_005E1396:
loc_005E139B:
    result = KiCopyAffinityEx(v_stack_m178, *(uint16_t *)(v_stack_m178 + 0x2), v_stack_m1C0, v_stack_m156);
    result = KiAndAffinityExNoResult(v_stack_m178, v_stack_m238, v_stack_m1C0, v_stack_m156);
    if ((uint32_t)(result) != 0) {
        Arg3 = v_stack_m178;
        Arg1 = v_stack_m178;
        result = KeAndAffinityEx2(Arg1, v_stack_m238, Arg3, v_stack_m156);
    }
    result = KiAndAffinityExNoResult(v_stack_m178, v_stack_m230, Arg3, v_stack_m156);
    if ((uint32_t)(result) != 0) {
        Arg3 = v_stack_m178;
        Arg1 = v_stack_m178;
        result = KeAndAffinityEx2(Arg1, v_stack_m230, Arg3, v_stack_m156);
    }
    result = KiCopyAffinityEx(v_stack_m180, *(uint16_t *)(v_stack_m180 + 0x2), v_stack_m178, v_stack_m156);
loc_005E13F1:
    if (v_stack_m240 < ((uint32_t)((uint32_t)(Arg6)))) goto loc_005E0CE4;
    goto loc_005E1412;
loc_005E1402:
    result = KiCopyAffinityEx(Arg9, *(uint16_t *)(arg9 + 0x2), v_stack_m248, v_stack_m156);
loc_005E1412:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint16_t *)(arg9 + 0x2), v_stack_m248, v_stack_m156);
    local_rsp = (local_rsp) + (688);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4E4` | `16` | `R` |
| `Arg1` | `+ 0x4E8` | `64` | `R` |
| `Arg5` | `- 0x1` | `32` | `R` |
| `Arg9` | `+ 0x0` | `16` | `R` |
| `Arg9` | `+ 0x0` | `16` | `W` |
| `Arg9` | `+ 0x2` | `16` | `R` |
| `Arg9` | `+ 0x8` | `64` | `R` |
| `Arg11` | `+ 0x0` | `32` | `R/W` |
| `Arg12` | `+ 0x0` | `64` | `R` |
| `Arg12` | `+ 0x10` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E05E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
