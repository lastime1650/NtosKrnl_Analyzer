# BiConvertBootEnvironmentDeviceToNt

- RVA: `0x00823E44`–`0x008248CD` (길이 `2,697` bytes)
- VA: `0x0000000140823E44`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DA2E0`
- 디코드: `717`개 명령, `2,697/2,697` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **59**; 고유 호출 대상: **20**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x00823EEB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00823F0C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00823F39` → [Feature_1741132088__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1741132088__private_IsEnabledDeviceUsageNoInline_function_0069E14C.md) (function, `0x0069E14C`)
- `0x00823F61` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00823F78` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00823FA0` → [Feature_1406898491__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1406898491__private_IsEnabledDeviceUsageNoInline_function_0069E0F8.md) (function, `0x0069E0F8`)
- `0x00823FBF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00823FDA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824028` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00824043` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824066` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (function, `0x00505FB0`)
- `0x0082408A` → [Feature_3887567162__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_3887567162__private_IsEnabledDeviceUsageNoInline_function_0069E398.md) (function, `0x0069E398`)
- `0x008240E7` → [Feature_2209321273__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2209321273__private_IsEnabledDeviceUsageNoInline_function_0069E1F4.md) (function, `0x0069E1F4`)
- `0x0082410C` → [Feature_1807454522__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1807454522__private_IsEnabledDeviceUsageNoInline_function_0069E1A0.md) (function, `0x0069E1A0`)
- `0x0082413A` → [BiGetNtPartitionPath](BiGetNtPartitionPath_function_0082546C.md) (function, `0x0082546C`)
- `0x00824177` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00824192` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008241AF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008241C1` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (function, `0x0069E0A4`)
- `0x008241E7` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (function, `0x0069E0A4`)
- `0x00824223` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (function, `0x0069E0A4`)
- `0x00824281` → [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) (function, `0x00823E44`)
- `0x008242A8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008242C6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008242F7` → [Feature_3887567162__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_3887567162__private_IsEnabledDeviceUsageNoInline_function_0069E398.md) (function, `0x0069E398`)
- `0x0082431C` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (function, `0x005064B0`)
- `0x00824335` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0082435B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00824365` → [Feature_2947256635__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2947256635__private_IsEnabledDeviceUsageNoInline_function_0069E2F0.md) (function, `0x0069E2F0`)
- `0x0082438F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008243AA` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008243E2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008243FD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0082442A` → [BiVerifyBootPartition](BiVerifyBootPartition_function_00825D94.md) (function, `0x00825D94`)
- `0x00824454` → [BiGetNtPartitionPath](BiGetNtPartitionPath_function_0082546C.md) (function, `0x0082546C`)
- `0x00824486` → [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) (function, `0x00823E44`)
- `0x008244AD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008244C8` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824529` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0082455F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0082457A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824597` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008245A4` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (function, `0x0069E29C`)
- `0x008245FA` → [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) (function, `0x00823E44`)
- `0x0082461B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082462B` → [BiConvertBootEnvironmentDeviceToUnknown](BiConvertBootEnvironmentDeviceToUnknown_function_008249C0.md) (function, `0x008249C0`)
- `0x0082465A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0082466D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00824696` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (function, `0x0069E29C`)
- `0x008246C1` → [BiIsBootRamdisk](BiIsBootRamdisk_function_00825AF4.md) (function, `0x00825AF4`)
- `0x008246E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008246FC` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824777` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (function, `0x0069E29C`)
- `0x008247C7` → [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) (function, `0x00823E44`)
- `0x008247EA` → [Feature_255824187__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_255824187__private_IsEnabledDeviceUsageNoInline_function_0069E248.md) (function, `0x0069E248`)
- `0x00824868` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00824883` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00824896` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008248B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)

### Direct callers
- [BiConvertBootEnvironmentDeviceToElement](BiConvertBootEnvironmentDeviceToElement_function_00823DF8.md) at `0x00823E30`
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x00824281`
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x00824486`
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x008245FA`
- [BiConvertBootEnvironmentDeviceToNt](BiConvertBootEnvironmentDeviceToNt_function_00823E44.md) at `0x008247C7`
- [BiVerifyBootPartition](BiVerifyBootPartition_function_00825D94.md) at `0x00825ECB`

### Static image references
- `0x0082470B` → RVA `0x00B0BC90` (` ?? ::NNGAKEGL::`string'`; read)
- `0x0082471A` → RVA `0x00B0BCA0` (`PAGE`; read)
- `0x00824725` → RVA `0x00B0BCB0` (`PAGE`; read)
- `0x00824730` → RVA `0x00B0BCC0` (`PAGE`; read)
- `0x0082473B` → RVA `0x00B0BCD0` (`PAGE`; read)
- `0x00824746` → RVA `0x00B0BCE0` (`PAGE`; read)
- `0x00824751` → RVA `0x00B0BCF0` (`PAGE`; read)
- `0x0082475E` → RVA `0x00B0BCF8` (`PAGE`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **50**
  - `0x00823EEB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00823F0C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00823F39` → [Feature_1741132088__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1741132088__private_IsEnabledDeviceUsageNoInline_function_0069E14C.md) (`PAGE` → `.text`)
  - `0x00823F61` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00823F78` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00823FA0` → [Feature_1406898491__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1406898491__private_IsEnabledDeviceUsageNoInline_function_0069E0F8.md) (`PAGE` → `.text`)
  - `0x00823FBF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00823FDA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824028` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00824043` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824066` → [strcpy_s](../../text/50/strcpy_s_function_00505FB0.md) (`PAGE` → `.text`)
  - `0x0082408A` → [Feature_3887567162__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_3887567162__private_IsEnabledDeviceUsageNoInline_function_0069E398.md) (`PAGE` → `.text`)
  - `0x008240E7` → [Feature_2209321273__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2209321273__private_IsEnabledDeviceUsageNoInline_function_0069E1F4.md) (`PAGE` → `.text`)
  - `0x0082410C` → [Feature_1807454522__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1807454522__private_IsEnabledDeviceUsageNoInline_function_0069E1A0.md) (`PAGE` → `.text`)
  - `0x00824177` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00824192` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008241AF` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008241C1` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (`PAGE` → `.text`)
  - `0x008241E7` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (`PAGE` → `.text`)
  - `0x00824223` → [Feature_1322225978__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_1322225978__private_IsEnabledDeviceUsageNoInline_function_0069E0A4.md) (`PAGE` → `.text`)
  - `0x008242A8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008242C6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008242F7` → [Feature_3887567162__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_3887567162__private_IsEnabledDeviceUsageNoInline_function_0069E398.md) (`PAGE` → `.text`)
  - `0x0082431C` → [wcscpy_s](../../text/50/wcscpy_s_function_005064B0.md) (`PAGE` → `.text`)
  - `0x00824335` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0082435B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00824365` → [Feature_2947256635__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2947256635__private_IsEnabledDeviceUsageNoInline_function_0069E2F0.md) (`PAGE` → `.text`)
  - `0x0082438F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008243AA` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008243E2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008243FD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008244AD` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008244C8` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824529` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0082455F` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0082457A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824597` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008245A4` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (`PAGE` → `.text`)
  - `0x0082461B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082465A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0082466D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00824696` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (`PAGE` → `.text`)
  - `0x008246E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008246FC` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824777` → [Feature_2746716474__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_2746716474__private_IsEnabledDeviceUsageNoInline_function_0069E29C.md) (`PAGE` → `.text`)
  - `0x008247EA` → [Feature_255824187__private_IsEnabledDeviceUsageNoInline](../../text/69/Feature_255824187__private_IsEnabledDeviceUsageNoInline_function_0069E248.md) (`PAGE` → `.text`)
  - `0x00824868` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00824883` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00824896` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008248B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00823E44  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00823E49  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00823E4E  55                              push rbp
00823E4F  56                              push rsi
00823E50  57                              push rdi
00823E51  41 54                           push r12
00823E53  41 55                           push r13
00823E55  41 56                           push r14
00823E57  41 57                           push r15
00823E59  48 8B EC                        mov rbp, rsp
00823E5C  48 83 EC 60                     sub rsp, 0x60
00823E60  33 F6                           xor esi, esi
00823E62  48 8B F9                        mov rdi, rcx
00823E65  8B 09                           mov ecx, dword ptr [rcx]
00823E67  45 8B F0                        mov r14d, r8d
00823E6A  89 75 D4                        mov dword ptr [rbp - 0x2c], esi
00823E6D  44 8B EA                        mov r13d, edx
00823E70  89 75 D8                        mov dword ptr [rbp - 0x28], esi
00823E73  44 8B E6                        mov r12d, esi
00823E76  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
00823E7A  44 8B FE                        mov r15d, esi
00823E7D  48 89 75 E8                     mov qword ptr [rbp - 0x18], rsi
00823E81  40 88 75 40                     mov byte ptr [rbp + 0x40], sil
00823E85  48 89 75 E0                     mov qword ptr [rbp - 0x20], rsi
00823E89  89 75 D0                        mov dword ptr [rbp - 0x30], esi
00823E8C  85 C9                           test ecx, ecx
00823E8E  0F 84 10 07 00 00               je 0x1408245a4
00823E94  83 E9 02                        sub ecx, 2
00823E97  0F 84 74 05 00 00               je 0x140824411
00823E9D  83 E9 03                        sub ecx, 3
00823EA0  0F 84 25 05 00 00               je 0x1408243cb
00823EA6  83 E9 01                        sub ecx, 1
00823EA9  0F 84 62 05 00 00               je 0x140824411
00823EAF  83 E9 01                        sub ecx, 1
00823EB2  0F 84 AD 04 00 00               je 0x140824365
00823EB8  83 E9 01                        sub ecx, 1
00823EBB  0F 84 B8 01 00 00               je 0x140824079
00823EC1  83 E9 01                        sub ecx, 1
00823EC4  0F 84 D6 00 00 00               je 0x140823fa0
00823ECA  83 E9 01                        sub ecx, 1
00823ECD  74 6A                           je 0x140823f39
00823ECF  83 F9 01                        cmp ecx, 1
00823ED2  0F 85 48 07 00 00               jne 0x140824620
00823ED8  8D 46 28                        lea eax, [rsi + 0x28]
00823EDB  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00823EE1  8B D0                           mov edx, eax
00823EE3  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00823EE6  B9 02 01 00 00                  mov ecx, 0x102
00823EEB  E8 00 E2 35 00                  call 0x140b820f0
00823EF0  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00823EF4  48 85 C0                        test rax, rax
00823EF7  75 0A                           jne 0x140823f03
00823EF9  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00823EFE  E9 47 07 00 00                  jmp 0x14082464a
00823F03  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00823F07  33 D2                           xor edx, edx
00823F09  48 8B C8                        mov rcx, rax
00823F0C  E8 2F 2D EA FF                  call 0x1406c6c40
00823F11  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F15  C7 00 0B 00 00 00               mov dword ptr [rax], 0xb
00823F1B  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F1F  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
00823F22  89 48 14                        mov dword ptr [rax + 0x14], ecx
00823F25  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F29  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00823F2D  F3 0F 7F 40 18                  movdqu xmmword ptr [rax + 0x18], xmm0
00823F32  8B DE                           mov ebx, esi
00823F34  E9 FD 06 00 00                  jmp 0x140824636
00823F39  E8 0E A2 E7 FF                  call 0x14069e14c
00823F3E  85 C0                           test eax, eax
00823F40  74 0A                           je 0x140823f4c
00823F42  83 7F 08 24                     cmp dword ptr [rdi + 8], 0x24
00823F46  0F 82 C1 06 00 00               jb 0x14082460d
00823F4C  B8 28 00 00 00                  mov eax, 0x28
00823F51  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00823F57  8B D0                           mov edx, eax
00823F59  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00823F5C  B9 02 01 00 00                  mov ecx, 0x102
00823F61  E8 8A E1 35 00                  call 0x140b820f0
00823F66  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00823F6A  48 85 C0                        test rax, rax
00823F6D  74 8A                           je 0x140823ef9
00823F6F  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00823F73  33 D2                           xor edx, edx
00823F75  48 8B C8                        mov rcx, rax
00823F78  E8 C3 2C EA FF                  call 0x1406c6c40
00823F7D  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F81  C7 00 0A 00 00 00               mov dword ptr [rax], 0xa
00823F87  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F8B  0F 10 47 10                     movups xmm0, xmmword ptr [rdi + 0x10]
00823F8F  F3 0F 7F 40 14                  movdqu xmmword ptr [rax + 0x14], xmm0
00823F94  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823F98  8B 4F 20                        mov ecx, dword ptr [rdi + 0x20]
00823F9B  89 48 24                        mov dword ptr [rax + 0x24], ecx
00823F9E  EB 92                           jmp 0x140823f32
00823FA0  E8 53 A1 E7 FF                  call 0x14069e0f8
00823FA5  85 C0                           test eax, eax
00823FA7  75 4D                           jne 0x140823ff6
00823FA9  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00823FAC  B9 02 01 00 00                  mov ecx, 0x102
00823FB1  83 C0 15                        add eax, 0x15
00823FB4  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00823FBA  8B D0                           mov edx, eax
00823FBC  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00823FBF  E8 2C E1 35 00                  call 0x140b820f0
00823FC4  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00823FC8  48 85 C0                        test rax, rax
00823FCB  0F 84 28 FF FF FF               je 0x140823ef9
00823FD1  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00823FD5  33 D2                           xor edx, edx
00823FD7  48 8B C8                        mov rcx, rax
00823FDA  E8 61 2C EA FF                  call 0x1406c6c40
00823FDF  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00823FE3  C7 00 09 00 00 00               mov dword ptr [rax], 9
00823FE9  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00823FED  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00823FF0  48 83 C1 14                     add rcx, 0x14
00823FF4  EB 6A                           jmp 0x140824060
00823FF6  8B 47 08                        mov eax, dword ptr [rdi + 8]
00823FF9  83 F8 14                        cmp eax, 0x14
00823FFC  0F 82 0B 06 00 00               jb 0x14082460d
00824002  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
00824005  83 C0 EC                        add eax, -0x14
00824008  3B C8                           cmp ecx, eax
0082400A  0F 87 FD 05 00 00               ja 0x14082460d
00824010  83 C1 15                        add ecx, 0x15
00824013  83 F9 15                        cmp ecx, 0x15
00824016  72 58                           jb 0x140824070
00824018  8B D1                           mov edx, ecx
0082401A  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00824020  B9 02 01 00 00                  mov ecx, 0x102
00824025  89 55 D0                        mov dword ptr [rbp - 0x30], edx
00824028  E8 C3 E0 35 00                  call 0x140b820f0
0082402D  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00824031  48 85 C0                        test rax, rax
00824034  0F 84 BF FE FF FF               je 0x140823ef9
0082403A  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
0082403E  33 D2                           xor edx, edx
00824040  48 8B C8                        mov rcx, rax
00824043  E8 F8 2B EA FF                  call 0x1406c6c40
00824048  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0082404C  C7 00 09 00 00 00               mov dword ptr [rax], 9
00824052  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824056  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00824059  48 83 C1 14                     add rcx, 0x14
0082405D  83 C0 EC                        add eax, -0x14
00824060  4C 8D 47 14                     lea r8, [rdi + 0x14]
00824064  8B D0                           mov edx, eax
00824066  E8 45 1F CE FF                  call 0x140505fb0
0082406B  E9 C2 FE FF FF                  jmp 0x140823f32
00824070  83 4D D0 FF                     or dword ptr [rbp - 0x30], 0xffffffff
00824074  E9 94 05 00 00                  jmp 0x14082460d
00824079  48 83 CE FF                     or rsi, 0xffffffffffffffff
0082407D  C7 45 D0 22 00 00 00            mov dword ptr [rbp - 0x30], 0x22
00824084  83 7F 10 01                     cmp dword ptr [rdi + 0x10], 1
00824088  75 5D                           jne 0x1408240e7
0082408A  E8 09 A3 E7 FF                  call 0x14069e398
0082408F  33 D2                           xor edx, edx
00824091  85 C0                           test eax, eax
00824093  75 15                           jne 0x1408240aa
00824095  48 8B CE                        mov rcx, rsi
00824098  48 FF C1                        inc rcx
0082409B  66 39 54 4F 1C                  cmp word ptr [rdi + rcx*2 + 0x1c], dx
008240A0  75 F6                           jne 0x140824098
008240A2  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
008240A5  8D 0C 48                        lea ecx, [rax + rcx*2]
008240A8  EB 38                           jmp 0x1408240e2
008240AA  8B 47 08                        mov eax, dword ptr [rdi + 8]
008240AD  83 F8 1C                        cmp eax, 0x1c
008240B0  0F 86 57 05 00 00               jbe 0x14082460d
008240B6  83 C0 E4                        add eax, -0x1c
008240B9  D1 E8                           shr eax, 1
008240BB  74 15                           je 0x1408240d2
008240BD  48 8D 4F 1C                     lea rcx, [rdi + 0x1c]
008240C1  66 39 11                        cmp word ptr [rcx], dx
008240C4  74 0C                           je 0x1408240d2
008240C6  41 FF C7                        inc r15d
008240C9  48 83 C1 02                     add rcx, 2
008240CD  44 3B F8                        cmp r15d, eax
008240D0  72 EF                           jb 0x1408240c1
008240D2  44 3B F8                        cmp r15d, eax
008240D5  0F 84 32 05 00 00               je 0x14082460d
008240DB  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
008240DE  42 8D 0C 78                     lea ecx, [rax + r15*2]
008240E2  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
008240E5  EB 17                           jmp 0x1408240fe
008240E7  E8 08 A1 E7 FF                  call 0x14069e1f4
008240EC  33 D2                           xor edx, edx
008240EE  85 C0                           test eax, eax
008240F0  74 09                           je 0x1408240fb
008240F2  39 57 10                        cmp dword ptr [rdi + 0x10], edx
008240F5  0F 85 12 05 00 00               jne 0x14082460d
008240FB  8B 4D D0                        mov ecx, dword ptr [rbp - 0x30]
008240FE  8B 5F 18                        mov ebx, dword ptr [rdi + 0x18]
00824101  89 55 D4                        mov dword ptr [rbp - 0x2c], edx
00824104  85 DB                           test ebx, ebx
00824106  0F 84 8F 01 00 00               je 0x14082429b
0082410C  E8 8F A0 E7 FF                  call 0x14069e1a0
00824111  85 C0                           test eax, eax
00824113  74 14                           je 0x140824129
00824115  8D 43 0C                        lea eax, [rbx + 0xc]
00824118  3B C3                           cmp eax, ebx
0082411A  0F 82 ED 04 00 00               jb 0x14082460d
00824120  39 47 08                        cmp dword ptr [rdi + 8], eax
00824123  0F 82 E4 04 00 00               jb 0x14082460d
00824129  41 F6 C6 20                     test r14b, 0x20
0082412D  0F 85 81 00 00 00               jne 0x1408241b4
00824133  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00824137  48 8B CF                        mov rcx, rdi
0082413A  E8 2D 13 00 00                  call 0x14082546c
0082413F  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
00824143  45 33 F6                        xor r14d, r14d
00824146  85 C0                           test eax, eax
00824148  78 6D                           js 0x1408241b7
0082414A  C6 45 40 01                     mov byte ptr [rbp + 0x40], 1
0082414E  48 8B C6                        mov rax, rsi
00824151  48 FF C0                        inc rax
00824154  66 45 39 34 44                  cmp word ptr [r12 + rax*2], r14w
00824159  75 F6                           jne 0x140824151
0082415B  44 8D 34 45 02 00 00 00         lea r14d, [rax*2 + 2]
00824163  B9 02 01 00 00                  mov ecx, 0x102
00824168  41 8D 46 14                     lea eax, [r14 + 0x14]
0082416C  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00824172  8B D0                           mov edx, eax
00824174  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
00824177  E8 74 DF 35 00                  call 0x140b820f0
0082417C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00824180  48 85 C0                        test rax, rax
00824183  0F 84 70 FD FF FF               je 0x140823ef9
00824189  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
0082418D  33 D2                           xor edx, edx
0082418F  48 8B C8                        mov rcx, rax
00824192  E8 A9 2A EA FF                  call 0x1406c6c40
00824197  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0082419B  49 8B D4                        mov rdx, r12
0082419E  45 8B C6                        mov r8d, r14d
008241A1  C7 00 02 00 00 00               mov dword ptr [rax], 2
008241A7  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
008241AB  48 83 C1 14                     add rcx, 0x14
008241AF  E8 8C 26 EA FF                  call 0x1406c6840
008241B4  45 33 F6                        xor r14d, r14d
008241B7  4C 39 75 E8                     cmp qword ptr [rbp - 0x18], r14
008241BB  0F 85 CF 00 00 00               jne 0x140824290
008241C1  E8 DE 9E E7 FF                  call 0x14069e0a4
008241C6  85 C0                           test eax, eax
008241C8  74 19                           je 0x1408241e3
008241CA  8B 47 08                        mov eax, dword ptr [rdi + 8]
008241CD  83 F8 14                        cmp eax, 0x14
008241D0  0F 82 37 04 00 00               jb 0x14082460d
008241D6  48 8D 48 EC                     lea rcx, [rax - 0x14]
008241DA  48 3B D9                        cmp rbx, rcx
008241DD  0F 87 2A 04 00 00               ja 0x14082460d
008241E3  4C 8D 34 1F                     lea r14, [rdi + rbx]
008241E7  E8 B8 9E E7 FF                  call 0x14069e0a4
008241EC  33 C9                           xor ecx, ecx
008241EE  85 C0                           test eax, eax
008241F0  74 0F                           je 0x140824201
008241F2  8B 47 08                        mov eax, dword ptr [rdi + 8]
008241F5  2B C3                           sub eax, ebx
008241F7  41 39 46 08                     cmp dword ptr [r14 + 8], eax
008241FB  0F 87 0C 04 00 00               ja 0x14082460d
00824201  41 39 0E                        cmp dword ptr [r14], ecx
00824204  0F 85 03 04 00 00               jne 0x14082460d
0082420A  41 83 7E 10 06                  cmp dword ptr [r14 + 0x10], 6
0082420F  0F 85 F8 03 00 00               jne 0x14082460d
00824215  8B 47 08                        mov eax, dword ptr [rdi + 8]
00824218  2B C3                           sub eax, ebx
0082421A  83 F8 4C                        cmp eax, 0x4c
0082421D  0F 82 EA 03 00 00               jb 0x14082460d
00824223  E8 7C 9E E7 FF                  call 0x14069e0a4
00824228  45 33 C9                        xor r9d, r9d
0082422B  85 C0                           test eax, eax
0082422D  75 06                           jne 0x140824235
0082422F  41 8D 41 28                     lea eax, [r9 + 0x28]
00824233  EB 35                           jmp 0x14082426a
00824235  44 8D 43 28                     lea r8d, [rbx + 0x28]
00824239  44 3B C3                        cmp r8d, ebx
0082423C  0F 82 CB 03 00 00               jb 0x14082460d
00824242  8B 57 08                        mov edx, dword ptr [rdi + 8]
00824245  41 8D 48 08                     lea ecx, [r8 + 8]
00824249  48 83 C1 04                     add rcx, 4
0082424D  48 3B D1                        cmp rdx, rcx
00824250  0F 82 B7 03 00 00               jb 0x14082460d
00824256  49 83 C6 28                     add r14, 0x28
0082425A  41 2B D0                        sub edx, r8d
0082425D  49 8B C1                        mov rax, r9
00824260  41 39 56 08                     cmp dword ptr [r14 + 8], edx
00824264  0F 87 A3 03 00 00               ja 0x14082460d
0082426A  4A 8D 0C 30                     lea rcx, [rax + r14]
0082426E  45 33 C0                        xor r8d, r8d
00824271  48 8D 45 D4                     lea rax, [rbp - 0x2c]
00824275  41 8B D5                        mov edx, r13d
00824278  4C 8D 4D E8                     lea r9, [rbp - 0x18]
0082427C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00824281  E8 BE FB FF FF                  call 0x140823e44
00824286  8B D8                           mov ebx, eax
00824288  85 C0                           test eax, eax
0082428A  0F 88 75 03 00 00               js 0x140824605
00824290  8B 5D D0                        mov ebx, dword ptr [rbp - 0x30]
00824293  8B 4D D4                        mov ecx, dword ptr [rbp - 0x2c]
00824296  03 CB                           add ecx, ebx
00824298  89 4D D0                        mov dword ptr [rbp - 0x30], ecx
0082429B  8B D1                           mov edx, ecx
0082429D  41 B8 42 43 44 4B               mov r8d, 0x4b444342
008242A3  B9 02 01 00 00                  mov ecx, 0x102
008242A8  E8 43 DE 35 00                  call 0x140b820f0
008242AD  45 33 F6                        xor r14d, r14d
008242B0  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008242B4  48 85 C0                        test rax, rax
008242B7  0F 84 3C FC FF FF               je 0x140823ef9
008242BD  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
008242C1  33 D2                           xor edx, edx
008242C3  48 8B C8                        mov rcx, rax
008242C6  E8 75 29 EA FF                  call 0x1406c6c40
008242CB  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008242CF  C7 00 08 00 00 00               mov dword ptr [rax], 8
008242D5  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008242D9  44 39 77 10                     cmp dword ptr [rdi + 0x10], r14d
008242DD  75 11                           jne 0x1408242f0
008242DF  33 F6                           xor esi, esi
008242E1  89 70 14                        mov dword ptr [rax + 0x14], esi
008242E4  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008242E8  8B 4F 14                        mov ecx, dword ptr [rdi + 0x14]
008242EB  89 48 1C                        mov dword ptr [rax + 0x1c], ecx
008242EE  EB 4C                           jmp 0x14082433c
008242F0  C7 40 14 01 00 00 00            mov dword ptr [rax + 0x14], 1
008242F7  E8 9C A0 E7 FF                  call 0x14069e398
008242FC  33 C9                           xor ecx, ecx
008242FE  85 C0                           test eax, eax
00824300  75 21                           jne 0x140824323
00824302  4C 8D 47 1C                     lea r8, [rdi + 0x1c]
00824306  48 FF C6                        inc rsi
00824309  66 41 39 0C 70                  cmp word ptr [r8 + rsi*2], cx
0082430E  75 F6                           jne 0x140824306
00824310  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824314  48 8D 56 01                     lea rdx, [rsi + 1]
00824318  48 83 C1 20                     add rcx, 0x20
0082431C  E8 8F 21 CE FF                  call 0x1405064b0
00824321  EB 17                           jmp 0x14082433a
00824323  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824327  48 8D 57 1C                     lea rdx, [rdi + 0x1c]
0082432B  45 8B C7                        mov r8d, r15d
0082432E  48 83 C1 20                     add rcx, 0x20
00824332  4D 03 C0                        add r8, r8
00824335  E8 06 25 EA FF                  call 0x1406c6840
0082433A  33 F6                           xor esi, esi
0082433C  48 39 75 E8                     cmp qword ptr [rbp - 0x18], rsi
00824340  0F 84 EC FB FF FF               je 0x140823f32
00824346  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0082434A  8B CB                           mov ecx, ebx
0082434C  89 58 18                        mov dword ptr [rax + 0x18], ebx
0082434F  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
00824353  48 03 4D E0                     add rcx, qword ptr [rbp - 0x20]
00824357  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
0082435B  E8 E0 24 EA FF                  call 0x1406c6840
00824360  E9 CD FB FF FF                  jmp 0x140823f32
00824365  E8 86 9F E7 FF                  call 0x14069e2f0
0082436A  85 C0                           test eax, eax
0082436C  74 0A                           je 0x140824378
0082436E  83 7F 08 30                     cmp dword ptr [rdi + 8], 0x30
00824372  0F 82 95 02 00 00               jb 0x14082460d
00824378  BA 24 00 00 00                  mov edx, 0x24
0082437D  C7 45 D0 24 00 00 00            mov dword ptr [rbp - 0x30], 0x24
00824384  B9 02 01 00 00                  mov ecx, 0x102
00824389  41 B8 42 43 44 4B               mov r8d, 0x4b444342
0082438F  E8 5C DD 35 00                  call 0x140b820f0
00824394  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00824398  48 85 C0                        test rax, rax
0082439B  0F 84 58 FB FF FF               je 0x140823ef9
008243A1  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
008243A5  33 D2                           xor edx, edx
008243A7  48 8B C8                        mov rcx, rax
008243AA  E8 91 28 EA FF                  call 0x1406c6c40
008243AF  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008243B3  C7 00 07 00 00 00               mov dword ptr [rax], 7
008243B9  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008243BD  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
008243C1  F3 0F 7F 40 14                  movdqu xmmword ptr [rax + 0x14], xmm0
008243C6  E9 67 FB FF FF                  jmp 0x140823f32
008243CB  BA 14 00 00 00                  mov edx, 0x14
008243D0  C7 45 D0 14 00 00 00            mov dword ptr [rbp - 0x30], 0x14
008243D7  B9 02 01 00 00                  mov ecx, 0x102
008243DC  41 B8 42 43 44 4B               mov r8d, 0x4b444342
008243E2  E8 09 DD 35 00                  call 0x140b820f0
008243E7  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008243EB  48 85 C0                        test rax, rax
008243EE  0F 84 05 FB FF FF               je 0x140823ef9
008243F4  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
008243F8  33 D2                           xor edx, edx
008243FA  48 8B C8                        mov rcx, rax
008243FD  E8 3E 28 EA FF                  call 0x1406c6c40
00824402  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00824406  C7 00 01 00 00 00               mov dword ptr [rax], 1
0082440C  E9 21 FB FF FF                  jmp 0x140823f32
00824411  48 8D 45 D8                     lea rax, [rbp - 0x28]
00824415  45 33 C9                        xor r9d, r9d
00824418  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0082441D  45 33 C0                        xor r8d, r8d
00824420  33 D2                           xor edx, edx
00824422  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00824427  48 8B CF                        mov rcx, rdi
0082442A  E8 65 19 00 00                  call 0x140825d94
0082442F  8B D8                           mov ebx, eax
00824431  85 C0                           test eax, eax
00824433  0F 88 CC 01 00 00               js 0x140824605
00824439  8B 75 D8                        mov esi, dword ptr [rbp - 0x28]
0082443C  41 F6 C6 20                     test r14b, 0x20
00824440  74 0B                           je 0x14082444d
00824442  85 F6                           test esi, esi
00824444  74 07                           je 0x14082444d
00824446  BB 01 00 00 C0                  mov ebx, 0xc0000001
0082444B  EB 1A                           jmp 0x140824467
0082444D  48 8D 55 F0                     lea rdx, [rbp - 0x10]
00824451  48 8B CF                        mov rcx, rdi
00824454  E8 13 10 00 00                  call 0x14082546c
00824459  4C 8B 65 F0                     mov r12, qword ptr [rbp - 0x10]
0082445D  8B D8                           mov ebx, eax
0082445F  85 C0                           test eax, eax
00824461  0F 89 CC 00 00 00               jns 0x140824533
00824467  85 F6                           test esi, esi
00824469  0F 84 96 01 00 00               je 0x140824605
0082446F  48 8D 45 D4                     lea rax, [rbp - 0x2c]
00824473  45 33 C0                        xor r8d, r8d
00824476  48 8D 0C 37                     lea rcx, [rdi + rsi]
0082447A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0082447F  4C 8D 4D E8                     lea r9, [rbp - 0x18]
00824483  41 8B D5                        mov edx, r13d
00824486  E8 B9 F9 FF FF                  call 0x140823e44
0082448B  33 F6                           xor esi, esi
0082448D  8B D8                           mov ebx, eax
0082448F  85 C0                           test eax, eax
00824491  0F 88 6E 01 00 00               js 0x140824605
00824497  8B 45 D4                        mov eax, dword ptr [rbp - 0x2c]
0082449A  B9 02 01 00 00                  mov ecx, 0x102
0082449F  83 C0 22                        add eax, 0x22
008244A2  41 B8 42 43 44 4B               mov r8d, 0x4b444342
008244A8  8B D0                           mov edx, eax
008244AA  89 45 D0                        mov dword ptr [rbp - 0x30], eax
008244AD  E8 3E DC 35 00                  call 0x140b820f0
008244B2  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008244B6  48 85 C0                        test rax, rax
008244B9  0F 84 3A FA FF FF               je 0x140823ef9
008244BF  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
008244C3  33 D2                           xor edx, edx
008244C5  48 8B C8                        mov rcx, rax
008244C8  E8 73 27 EA FF                  call 0x1406c6c40
008244CD  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008244D1  B9 02 00 00 12                  mov ecx, 0x12000002
008244D6  C7 00 08 00 00 00               mov dword ptr [rax], 8
008244DC  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008244E0  89 70 14                        mov dword ptr [rax + 0x14], esi
008244E3  45 85 ED                        test r13d, r13d
008244E6  74 1F                           je 0x140824507
008244E8  41 81 FD 01 00 00 21            cmp r13d, 0x21000001
008244EF  75 07                           jne 0x1408244f8
008244F1  B9 02 00 00 22                  mov ecx, 0x22000002
008244F6  EB 0F                           jmp 0x140824507
008244F8  41 81 FD 43 00 00 11            cmp r13d, 0x11000043
008244FF  B8 44 00 00 12                  mov eax, 0x12000044
00824504  0F 44 C8                        cmove ecx, eax
00824507  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0082450B  89 48 1C                        mov dword ptr [rax + 0x1c], ecx
0082450E  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00824512  C7 40 18 22 00 00 00            mov dword ptr [rax + 0x18], 0x22
00824519  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0082451D  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
00824521  48 83 C1 22                     add rcx, 0x22
00824525  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
00824529  E8 12 23 EA FF                  call 0x1406c6840
0082452E  E9 03 01 00 00                  jmp 0x140824636
00824533  C6 45 40 01                     mov byte ptr [rbp + 0x40], 1
00824537  48 83 CE FF                     or rsi, 0xffffffffffffffff
0082453B  48 FF C6                        inc rsi
0082453E  66 45 39 3C 74                  cmp word ptr [r12 + rsi*2], r15w
00824543  75 F6                           jne 0x14082453b
00824545  8D 34 75 02 00 00 00            lea esi, [rsi*2 + 2]
0082454C  B9 02 01 00 00                  mov ecx, 0x102
00824551  8D 46 14                        lea eax, [rsi + 0x14]
00824554  41 B8 42 43 44 4B               mov r8d, 0x4b444342
0082455A  8B D0                           mov edx, eax
0082455C  89 45 D0                        mov dword ptr [rbp - 0x30], eax
0082455F  E8 8C DB 35 00                  call 0x140b820f0
00824564  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00824568  48 85 C0                        test rax, rax
0082456B  0F 84 88 F9 FF FF               je 0x140823ef9
00824571  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
00824575  33 D2                           xor edx, edx
00824577  48 8B C8                        mov rcx, rax
0082457A  E8 C1 26 EA FF                  call 0x1406c6c40
0082457F  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00824583  49 8B D4                        mov rdx, r12
00824586  44 8B C6                        mov r8d, esi
00824589  C7 00 02 00 00 00               mov dword ptr [rax], 2
0082458F  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824593  48 83 C1 14                     add rcx, 0x14
00824597  E8 A4 22 EA FF                  call 0x1406c6840
0082459C  41 8B DF                        mov ebx, r15d
0082459F  E9 92 00 00 00                  jmp 0x140824636
008245A4  E8 F3 9C E7 FF                  call 0x14069e29c
008245A9  85 C0                           test eax, eax
008245AB  74 06                           je 0x1408245b3
008245AD  83 7F 08 14                     cmp dword ptr [rdi + 8], 0x14
008245B1  72 5A                           jb 0x14082460d
008245B3  8B 4F 10                        mov ecx, dword ptr [rdi + 0x10]
008245B6  8B C1                           mov eax, ecx
008245B8  83 E8 03                        sub eax, 3
008245BB  0F 84 CC 00 00 00               je 0x14082468d
008245C1  83 E8 02                        sub eax, 2
008245C4  0F 84 C3 00 00 00               je 0x14082468d
008245CA  83 F8 01                        cmp eax, 1
008245CD  75 3E                           jne 0x14082460d
008245CF  8B 47 08                        mov eax, dword ptr [rdi + 8]
008245D2  48 8D 4F 28                     lea rcx, [rdi + 0x28]
008245D6  BE 34 00 00 00                  mov esi, 0x34
008245DB  3B C6                           cmp eax, esi
008245DD  72 2E                           jb 0x14082460d
008245DF  83 C0 D8                        add eax, -0x28
008245E2  39 41 08                        cmp dword ptr [rcx + 8], eax
008245E5  77 26                           ja 0x14082460d
008245E7  48 8D 45 D0                     lea rax, [rbp - 0x30]
008245EB  45 33 C0                        xor r8d, r8d
008245EE  4C 8D 4D E0                     lea r9, [rbp - 0x20]
008245F2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008245F7  41 8B D5                        mov edx, r13d
008245FA  E8 45 F8 FF FF                  call 0x140823e44
008245FF  8B D8                           mov ebx, eax
00824601  85 C0                           test eax, eax
00824603  79 31                           jns 0x140824636
00824605  81 FB 9A 00 00 C0               cmp ebx, 0xc000009a
0082460B  74 25                           je 0x140824632
0082460D  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824611  48 85 C9                        test rcx, rcx
00824614  74 0A                           je 0x140824620
00824616  BA 42 43 44 4B                  mov edx, 0x4b444342
0082461B  E8 50 E2 35 00                  call 0x140b82870
00824620  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00824624  48 8B CF                        mov rcx, rdi
00824627  48 8D 55 E0                     lea rdx, [rbp - 0x20]
0082462B  E8 90 03 00 00                  call 0x1408249c0
00824630  8B D8                           mov ebx, eax
00824632  85 DB                           test ebx, ebx
00824634  78 14                           js 0x14082464a
00824636  48 8B 4D 58                     mov rcx, qword ptr [rbp + 0x58]
0082463A  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0082463E  48 89 01                        mov qword ptr [rcx], rax
00824641  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
00824645  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
00824648  89 01                           mov dword ptr [rcx], eax
0082464A  48 8B 4D E8                     mov rcx, qword ptr [rbp - 0x18]
0082464E  33 FF                           xor edi, edi
00824650  48 85 C9                        test rcx, rcx
00824653  74 0A                           je 0x14082465f
00824655  BA 42 43 44 4B                  mov edx, 0x4b444342
0082465A  E8 11 E2 35 00                  call 0x140b82870
0082465F  40 38 7D 40                     cmp byte ptr [rbp + 0x40], dil
00824663  74 0D                           je 0x140824672
00824665  BA 42 43 44 4B                  mov edx, 0x4b444342
0082466A  49 8B CC                        mov rcx, r12
0082466D  E8 FE E1 35 00                  call 0x140b82870
00824672  8B C3                           mov eax, ebx
00824674  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
0082467C  48 83 C4 60                     add rsp, 0x60
00824680  41 5F                           pop r15
00824682  41 5E                           pop r14
00824684  41 5D                           pop r13
00824686  41 5C                           pop r12
00824688  5F                              pop rdi
00824689  5E                              pop rsi
0082468A  5D                              pop rbp
0082468B  C3                              ret
0082468C  CC                              int3
0082468D  83 F9 03                        cmp ecx, 3
00824690  0F 85 E1 00 00 00               jne 0x140824777
00824696  E8 01 9C E7 FF                  call 0x14069e29c
0082469B  85 C0                           test eax, eax
0082469D  74 0A                           je 0x1408246a9
0082469F  83 7F 08 38                     cmp dword ptr [rdi + 8], 0x38
008246A3  0F 82 64 FF FF FF               jb 0x14082460d
008246A9  83 7F 30 05                     cmp dword ptr [rdi + 0x30], 5
008246AD  0F 85 B9 00 00 00               jne 0x14082476c
008246B3  83 7F 2C 0C                     cmp dword ptr [rdi + 0x2c], 0xc
008246B7  0F 85 AF 00 00 00               jne 0x14082476c
008246BD  48 8D 4F 14                     lea rcx, [rdi + 0x14]
008246C1  E8 2E 14 00 00                  call 0x140825af4
008246C6  84 C0                           test al, al
008246C8  0F 84 9E 00 00 00               je 0x14082476c
008246CE  BA 80 00 00 00                  mov edx, 0x80
008246D3  B9 02 01 00 00                  mov ecx, 0x102
008246D8  41 B8 42 43 44 4B               mov r8d, 0x4b444342
008246DE  89 55 D0                        mov dword ptr [rbp - 0x30], edx
008246E1  E8 0A DA 35 00                  call 0x140b820f0
008246E6  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
008246EA  48 85 C0                        test rax, rax
008246ED  0F 84 06 F8 FF FF               je 0x140823ef9
008246F3  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
008246F7  33 D2                           xor edx, edx
008246F9  48 8B C8                        mov rcx, rax
008246FC  E8 3F 25 EA FF                  call 0x1406c6c40
00824701  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
00824705  C7 00 02 00 00 00               mov dword ptr [rax], 2
0082470B  0F 28 05 7E 75 2E 00            movaps xmm0, xmmword ptr [rip + 0x2e757e]
00824712  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
00824716  0F 11 41 14                     movups xmmword ptr [rcx + 0x14], xmm0
0082471A  0F 28 0D 7F 75 2E 00            movaps xmm1, xmmword ptr [rip + 0x2e757f]
00824721  0F 11 49 24                     movups xmmword ptr [rcx + 0x24], xmm1
00824725  0F 28 05 84 75 2E 00            movaps xmm0, xmmword ptr [rip + 0x2e7584]
0082472C  0F 11 41 34                     movups xmmword ptr [rcx + 0x34], xmm0
00824730  0F 28 0D 89 75 2E 00            movaps xmm1, xmmword ptr [rip + 0x2e7589]
00824737  0F 11 49 44                     movups xmmword ptr [rcx + 0x44], xmm1
0082473B  0F 28 05 8E 75 2E 00            movaps xmm0, xmmword ptr [rip + 0x2e758e]
00824742  0F 11 41 54                     movups xmmword ptr [rcx + 0x54], xmm0
00824746  0F 28 0D 93 75 2E 00            movaps xmm1, xmmword ptr [rip + 0x2e7593]
0082474D  0F 11 49 64                     movups xmmword ptr [rcx + 0x64], xmm1
00824751  F2 0F 10 05 97 75 2E 00         movsd xmm0, qword ptr [rip + 0x2e7597]
00824759  F2 0F 11 41 74                  movsd qword ptr [rcx + 0x74], xmm0
0082475E  8B 05 94 75 2E 00               mov eax, dword ptr [rip + 0x2e7594]
00824764  89 41 7C                        mov dword ptr [rcx + 0x7c], eax
00824767  E9 C6 F7 FF FF                  jmp 0x140823f32
0082476C  4C 8D 77 34                     lea r14, [rdi + 0x34]
00824770  BE 34 00 00 00                  mov esi, 0x34
00824775  EB 1C                           jmp 0x140824793
00824777  E8 20 9B E7 FF                  call 0x14069e29c
0082477C  85 C0                           test eax, eax
0082477E  74 0A                           je 0x14082478a
00824780  83 7F 08 24                     cmp dword ptr [rdi + 8], 0x24
00824784  0F 82 83 FE FF FF               jb 0x14082460d
0082478A  4C 8D 77 20                     lea r14, [rdi + 0x20]
0082478E  BE 20 00 00 00                  mov esi, 0x20
00824793  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00824796  8B C6                           mov eax, esi
00824798  48 83 C0 0C                     add rax, 0xc
0082479C  48 3B C8                        cmp rcx, rax
0082479F  0F 82 68 FE FF FF               jb 0x14082460d
008247A5  2B CE                           sub ecx, esi
008247A7  41 39 4E 08                     cmp dword ptr [r14 + 8], ecx
008247AB  0F 87 5C FE FF FF               ja 0x14082460d
008247B1  48 8D 45 D4                     lea rax, [rbp - 0x2c]
008247B5  45 33 C0                        xor r8d, r8d
008247B8  4C 8D 4D E8                     lea r9, [rbp - 0x18]
008247BC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008247C1  41 8B D5                        mov edx, r13d
008247C4  49 8B CE                        mov rcx, r14
008247C7  E8 78 F6 FF FF                  call 0x140823e44
008247CC  8B D8                           mov ebx, eax
008247CE  85 C0                           test eax, eax
008247D0  0F 88 2F FE FF FF               js 0x140824605
008247D6  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
008247DA  83 38 03                        cmp dword ptr [rax], 3
008247DD  0F 84 2A FE FF FF               je 0x14082460d
008247E3  45 8B 66 08                     mov r12d, dword ptr [r14 + 8]
008247E7  4D 03 E6                        add r12, r14
008247EA  E8 59 9A E7 FF                  call 0x14069e248
008247EF  85 C0                           test eax, eax
008247F1  75 10                           jne 0x140824803
008247F3  48 83 CE FF                     or rsi, 0xffffffffffffffff
008247F7  48 FF C6                        inc rsi
008247FA  66 45 39 3C 74                  cmp word ptr [r12 + rsi*2], r15w
008247FF  75 F6                           jne 0x1408247f7
00824801  EB 2B                           jmp 0x14082482e
00824803  8B 4F 08                        mov ecx, dword ptr [rdi + 8]
00824806  41 2B 4E 08                     sub ecx, dword ptr [r14 + 8]
0082480A  2B CE                           sub ecx, esi
0082480C  41 8B F7                        mov esi, r15d
0082480F  D1 E9                           shr ecx, 1
00824811  74 13                           je 0x140824826
00824813  49 8B C4                        mov rax, r12
00824816  66 44 39 38                     cmp word ptr [rax], r15w
0082481A  74 0A                           je 0x140824826
0082481C  FF C6                           inc esi
0082481E  48 83 C0 02                     add rax, 2
00824822  3B F1                           cmp esi, ecx
00824824  72 F0                           jb 0x140824816
00824826  3B F1                           cmp esi, ecx
00824828  0F 84 DF FD FF FF               je 0x14082460d
0082482E  8D 34 75 02 00 00 00            lea esi, [rsi*2 + 2]
00824835  8D 4E 20                        lea ecx, [rsi + 0x20]
00824838  83 F9 20                        cmp ecx, 0x20
0082483B  0F 82 CC FD FF FF               jb 0x14082460d
00824841  8B 55 D4                        mov edx, dword ptr [rbp - 0x2c]
00824844  8D 04 11                        lea eax, [rcx + rdx]
00824847  3B C1                           cmp eax, ecx
00824849  0F 82 BE FD FF FF               jb 0x14082460d
0082484F  8D 5E 1F                        lea ebx, [rsi + 0x1f]
00824852  B9 02 01 00 00                  mov ecx, 0x102
00824857  83 E3 F8                        and ebx, 0xfffffff8
0082485A  41 B8 42 43 44 4B               mov r8d, 0x4b444342
00824860  8D 04 1A                        lea eax, [rdx + rbx]
00824863  8B D0                           mov edx, eax
00824865  89 45 D0                        mov dword ptr [rbp - 0x30], eax
00824868  E8 83 D8 35 00                  call 0x140b820f0
0082486D  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
00824871  48 85 C0                        test rax, rax
00824874  0F 84 7F F6 FF FF               je 0x140823ef9
0082487A  44 8B 45 D0                     mov r8d, dword ptr [rbp - 0x30]
0082487E  33 D2                           xor edx, edx
00824880  48 8B C8                        mov rcx, rax
00824883  E8 B8 23 EA FF                  call 0x1406c6c40
00824888  48 8B 4D E0                     mov rcx, qword ptr [rbp - 0x20]
0082488C  49 8B D4                        mov rdx, r12
0082488F  48 83 C1 18                     add rcx, 0x18
00824893  44 8B C6                        mov r8d, esi
00824896  E8 A5 1F EA FF                  call 0x1406c6840
0082489B  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0082489F  8B CB                           mov ecx, ebx
008248A1  89 58 14                        mov dword ptr [rax + 0x14], ebx
008248A4  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
008248A8  48 03 4D E0                     add rcx, qword ptr [rbp - 0x20]
008248AC  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
008248B0  E8 8B 1F EA FF                  call 0x1406c6840
008248B5  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
008248B8  83 E8 03                        sub eax, 3
008248BB  F7 D8                           neg eax
008248BD  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
008248C1  1B C9                           sbb ecx, ecx
008248C3  83 C1 04                        add ecx, 4
008248C6  89 08                           mov dword ptr [rax], ecx
008248C8  E9 CF FC FF FF                  jmp 0x14082459c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BiConvertBootEnvironmentDeviceToNt(__int64 a1, int a2, int a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_stack_p20 = a4;
    v_rsp = (v_rsp) - (96);
    v_rsi = 0;
    v_stack_m64 = 0;
    v_stack_m60 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_p8 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1))) == 0) goto loc_008245A4;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) - (2));
    if (condition_is_equal) goto loc_00824411;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_008243CB;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00824411;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00824365;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00824079;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00823FA0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_00823F39;
    if (((unsigned int)(a1)) != 1) goto loc_00824620;
    v_stack_m68 = (unsigned int)(v_rsi + 40);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_rsi + 40)), (unsigned int)(0x4B444342ULL), a4);
    v_stack_m58 = result;
    if (result != 0) goto loc_00823F03;
loc_00823EF9:
    goto loc_0082464A;
loc_00823F03:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), a4);
    *(unsigned int *)(v_stack_m58) = 11;
    *(unsigned int *)(v_stack_m58 + 20) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)));
    *(unsigned __int64 *)(v_stack_m58 + 24) = v_xmm0;
loc_00823F32:
    goto loc_00824636;
loc_00823F39:
    result = Feature_1741132088__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(a1 + 16)), a2, (unsigned int)(v_stack_m68), a4);
    if ((unsigned int)(result) == 0) goto loc_00823F4C;
    if ((*(unsigned int *)(a1 + 8)) < 36) goto loc_0082460D;
loc_00823F4C:
    v_stack_m68 = 40;
    result = ExAllocatePool2(258, 40, (unsigned int)(0x4B444342ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), a4);
    *(unsigned int *)(v_stack_m58) = 10;
    *(unsigned __int64 *)(v_stack_m58 + 20) = v_xmm0;
    *(unsigned int *)(v_stack_m58 + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    goto loc_00823F32;
loc_00823FA0:
    result = Feature_1406898491__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(a1 + 32)), a2, (unsigned int)(v_stack_m68), a4);
    if ((unsigned int)(result) != 0) goto loc_00823FF6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) + (21));
    v_stack_m68 = (unsigned int)(result);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(result)), (unsigned int)(0x4B444342ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), a4);
    *(unsigned int *)(v_stack_m58) = 9;
    a1 = (v_stack_m58) + (20);
    goto loc_00824060;
loc_00823FF6:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) < 20) goto loc_0082460D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) + (-20));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))) > ((unsigned int)(result))) goto loc_0082460D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) + (21));
    if (((unsigned int)(a1)) < 21) goto loc_00824070;
    v_stack_m68 = (unsigned int)((unsigned int)((unsigned int)(a1)));
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(a1)), (unsigned int)(0x4B444342ULL), a4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), a4);
    *(unsigned int *)(v_stack_m58) = 9;
    a1 = (v_stack_m58) + (20);
    result = (unsigned int)(((unsigned int)(v_stack_m68)) + (-20));
loc_00824060:
    result = strcpy_s(a1, (unsigned int)((unsigned int)(result)), a1 + 20, a4);
    goto loc_00823F32;
loc_00824070:
    goto loc_0082460D;
loc_00824079:
    v_rsi = (v_rsi) | (-1);
    v_stack_m68 = 34;
    if ((*(unsigned int *)(a1 + 16)) != 1) goto loc_008240E7;
    result = Feature_3887567162__private_IsEnabledDeviceUsageNoInline(a1, (unsigned int)((unsigned int)(result)), a1 + 20, a4);
    a2 = 0;
    if ((unsigned int)(result) != 0) goto loc_008240AA;
loc_00824098:
    a1 = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(a1 + a1 * 2 + 28)) != 0) goto loc_00824098;
    goto loc_008240E2;
loc_008240AA:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) <= 28) goto loc_0082460D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) + (-28));
    result = (unsigned int)((result) >> (1));
    if (condition_is_equal) goto loc_008240D2;
loc_008240C1:
    if ((*(unsigned __int16 *)(a1 + 28)) == 0) goto loc_008240D2;
    v_r15 = (unsigned int)((0) + 1);
    a1 = (a1 + 28) + (2);
    if (((unsigned int)(v_r15)) < ((unsigned int)(result))) goto loc_008240C1;
loc_008240D2:
    if (((unsigned int)(v_r15)) == ((unsigned int)(result))) goto loc_0082460D;
loc_008240E2:
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m68) + v_r15 * 2);
    goto loc_008240FE;
loc_008240E7:
    result = Feature_2209321273__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_m68) + v_r15 * 2, a2, a1 + 20, a4);
    a2 = 0;
    if ((unsigned int)(result) == 0) goto loc_008240FB;
    if ((*(unsigned int *)(a1 + 16)) != 0) goto loc_0082460D;
loc_008240FB:
loc_008240FE:
    v_stack_m64 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))) == 0) goto loc_0082429B;
    result = Feature_1807454522__private_IsEnabledDeviceUsageNoInline((unsigned int)(v_stack_m68), a2, a1 + 20, a4);
    if ((unsigned int)(result) == 0) goto loc_00824129;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)) + 12)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) goto loc_0082460D;
    if ((*(unsigned int *)(a1 + 8)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)) + 12))) goto loc_0082460D;
loc_00824129:
    if ((((unsigned __int8)((unsigned int)(a3))) & (32)) != 0) goto loc_008241B4;
    result = BiGetNtPartitionPath(a1, v_stack_m48, a1 + 20, a4);
    v_r14 = 0;
    if (sign_flag) goto loc_008241B7;
    v_stack_p8 = 1;
loc_00824151:
    result = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m48 + result * 2)) != 0) goto loc_00824151;
    v_stack_m64 = (unsigned int)(result * 2 + 2 + 20);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(result * 2 + 2 + 20)), (unsigned int)(0x4B444342ULL), a4);
    v_stack_m50 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m64), a4);
    *(unsigned int *)(v_stack_m50) = 2;
    a1 = (v_stack_m50) + (20);
    result = memcpy(a1, v_stack_m48, (unsigned int)((unsigned int)(result * 2 + 2)), a4);
loc_008241B4:
    v_r14 = 0;
loc_008241B7:
    if (v_stack_m50 != 0) goto loc_00824290;
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m48, (unsigned int)((unsigned int)(result * 2 + 2)), a4);
    if ((unsigned int)(result) == 0) goto loc_008241E3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) < 20) goto loc_0082460D;
    if (((unsigned int)(*(unsigned int *)(a1 + 24))) > ((unsigned int)(*(unsigned int *)(a1 + 8)) - 20)) goto loc_0082460D;
loc_008241E3:
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(a1 + 8)) - 20, v_stack_m48, (unsigned int)((unsigned int)(result * 2 + 2)), a4);
    a1 = 0;
    if ((unsigned int)(result) == 0) goto loc_00824201;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if ((*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1 + 8)) > ((unsigned int)(result))) goto loc_0082460D;
loc_00824201:
    if ((*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1)) != 0) goto loc_0082460D;
    if ((*(unsigned int *)(a1 + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1 + 16)) != 6) goto loc_0082460D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)))));
    if (((unsigned int)(result)) < 76) goto loc_0082460D;
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m48, (unsigned int)((unsigned int)(result * 2 + 2)), a4);
    a4 = 0;
    if ((unsigned int)(result) != 0) goto loc_00824235;
    goto loc_0082426A;
loc_00824235:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)) + 40)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24))))) goto loc_0082460D;
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 24)) + 40 + 8) + (4);
    if (((unsigned int)(*(unsigned int *)(a1 + 8))) < a1) goto loc_0082460D;
    v_r14 = (a1 + (unsigned int)(*(unsigned int *)(a1 + 24)) * 1) + (40);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) - ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 24)) + 40)));
    if ((*(unsigned int *)(v_r14 + 8)) > a2) goto loc_0082460D;
loc_0082426A:
    a3 = 0;
    v_stack_m78 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(0 + v_r14 * 1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, v_stack_m50);
    if (sign_flag) goto loc_00824605;
loc_00824290:
    a1 = (unsigned int)(((unsigned int)(v_stack_m64)) + ((unsigned int)((unsigned int)(v_stack_m68))));
    v_stack_m68 = (unsigned int)(a1);
loc_0082429B:
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(a1)), (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_r14 = 0;
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    *(unsigned int *)(v_stack_m58) = 8;
    if ((*(unsigned int *)(a1 + 16)) != 0) goto loc_008242F0;
    v_rsi = 0;
    *(unsigned int *)(v_stack_m58 + 20) = 0;
    *(unsigned int *)(v_stack_m58 + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20)));
    goto loc_0082433C;
loc_008242F0:
    *(unsigned int *)(v_stack_m58 + 20) = 1;
    result = Feature_3887567162__private_IsEnabledDeviceUsageNoInline((unsigned int)(*(unsigned int *)(a1 + 20)), a2, (unsigned int)(v_stack_m68), v_stack_m50);
    a1 = 0;
    if ((unsigned int)(result) != 0) goto loc_00824323;
loc_00824306:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(a1 + 28 + v_rsi * 2)) != 0) goto loc_00824306;
    a1 = (v_stack_m58) + (32);
    result = wcscpy_s(a1, v_rsi + 1, a1 + 28, v_stack_m50);
    goto loc_0082433A;
loc_00824323:
    a1 = (v_stack_m58) + (32);
    a3 = ((unsigned int)((unsigned int)(v_r15))) + ((unsigned int)((unsigned int)(v_r15)));
    result = memcpy(a1, a1 + 28, a3, v_stack_m50);
loc_0082433A:
    v_rsi = 0;
loc_0082433C:
    if (v_stack_m50 == 0) goto loc_00823F32;
    *(unsigned int *)(v_stack_m58 + 24) = (unsigned int)((unsigned int)(v_stack_m68));
    a1 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m68)))) + (v_stack_m58);
    result = memcpy(a1, v_stack_m50, (unsigned int)(v_stack_m64), v_stack_m50);
    goto loc_00823F32;
loc_00824365:
    result = Feature_2947256635__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m50, (unsigned int)(v_stack_m64), v_stack_m50);
    if ((unsigned int)(result) == 0) goto loc_00824378;
    if ((*(unsigned int *)(a1 + 8)) < 48) goto loc_0082460D;
loc_00824378:
    v_stack_m68 = 36;
    result = ExAllocatePool2(258, 36, (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    *(unsigned int *)(v_stack_m58) = 7;
    *(unsigned __int64 *)(v_stack_m58 + 20) = v_xmm0;
    goto loc_00823F32;
loc_008243CB:
    v_stack_m68 = 20;
    result = ExAllocatePool2(258, 20, (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    *(unsigned int *)(v_stack_m58) = 1;
    goto loc_00823F32;
loc_00824411:
    a4 = 0;
    v_stack_m70 = v_stack_m60;
    a3 = 0;
    a2 = 0;
    v_stack_m78 = 0;
    result = BiVerifyBootPartition(a1, a2, a3, a4);
    if (sign_flag) goto loc_00824605;
    if (((0) & (32)) == 0) goto loc_0082444D;
    if ((unsigned int)((unsigned int)(v_stack_m60)) == 0) goto loc_0082444D;
    goto loc_00824467;
loc_0082444D:
    result = BiGetNtPartitionPath(a1, v_stack_m48, a3, a4);
    if (!sign_flag) goto loc_00824533;
loc_00824467:
    if ((unsigned int)((unsigned int)(v_stack_m60)) == 0) goto loc_00824605;
    a3 = 0;
    v_stack_m78 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(a1 + (unsigned int)(v_stack_m60) * 1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, v_stack_m50);
    v_rsi = 0;
    if (sign_flag) goto loc_00824605;
    result = (unsigned int)(((unsigned int)(v_stack_m64)) + (34));
    v_stack_m68 = (unsigned int)(result);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(result)), (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    *(unsigned int *)(v_stack_m58) = 8;
    *(unsigned int *)(v_stack_m58 + 20) = 0;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_00824507;
    if (((unsigned int)((unsigned int)(a2))) != 0x21000001ULL) goto loc_008244F8;
    goto loc_00824507;
loc_008244F8:
    a1 = (unsigned int)(0x22000002ULL);
    if (((unsigned int)((unsigned int)(a2))) == 0x11000043ULL) { a1 = (unsigned int)((unsigned int)(0x12000044ULL)); }
loc_00824507:
    *(unsigned int *)(v_stack_m58 + 28) = (unsigned int)(a1);
    *(unsigned int *)(v_stack_m58 + 24) = 34;
    a1 = (v_stack_m58) + (34);
    result = memcpy(a1, v_stack_m50, (unsigned int)(v_stack_m64), v_stack_m50);
    goto loc_00824636;
loc_00824533:
    v_stack_p8 = 1;
    v_rsi = (v_rsi) | (-1);
loc_0082453B:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_stack_m48 + v_rsi * 2)) != ((unsigned __int16)(v_r15))) goto loc_0082453B;
    v_stack_m68 = (unsigned int)(v_rsi * 2 + 2 + 20);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)(v_rsi * 2 + 2 + 20)), (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    *(unsigned int *)(v_stack_m58) = 2;
    a1 = (v_stack_m58) + (20);
    result = memcpy(a1, v_stack_m48, (unsigned int)((unsigned int)(v_rsi * 2 + 2)), v_stack_m50);
loc_0082459C:
    goto loc_00824636;
loc_008245A4:
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(a1, v_stack_m48, (unsigned int)((unsigned int)(v_rsi * 2 + 2)), v_stack_m50);
    if ((unsigned int)(result) == 0) goto loc_008245B3;
    if ((*(unsigned int *)(a1 + 8)) < 20) goto loc_0082460D;
loc_008245B3:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) - (3));
    if (condition_is_equal) goto loc_0082468D;
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_0082468D;
    if (((unsigned int)(result)) != 1) goto loc_0082460D;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8)))) < 52) goto loc_0082460D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 8))) + (-40));
    if ((*(unsigned int *)(a1 + 40 + 8)) > ((unsigned int)(result))) goto loc_0082460D;
    a3 = 0;
    v_stack_m78 = v_stack_m68;
    result = BiConvertBootEnvironmentDeviceToNt(a1 + 40, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, v_stack_m58);
    if (!sign_flag) goto loc_00824636;
loc_00824605:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0xC000009AULL) goto loc_00824632;
loc_0082460D:
    if (v_stack_m58 != 0) {
        a2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m58, a2, a3, v_stack_m58);
    }
    result = BiConvertBootEnvironmentDeviceToUnknown(a1, v_stack_m58, v_stack_m68, v_stack_m58);
loc_00824632:
    if (!(sign_flag)) {
        a1 = v_stack_p20;
        result = v_stack_m58;
        *(unsigned __int64 *)(a1) = result;
        a1 = a5;
        result = v_stack_m68;
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    v_rdi = 0;
    if (v_stack_m50 != 0) {
        a2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m50, a2, v_stack_m68, v_stack_m58);
    }
    if (v_stack_p8 != 0) {
        a2 = 0x4B444342ULL;
        a1 = v_stack_m48;
        result = ExFreePoolWithTag(a1, a2, v_stack_m68, v_stack_m58);
    }
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_0082468D:
    if (((unsigned int)(a1)) != 3) goto loc_00824777;
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m68, v_stack_m58);
    if ((unsigned int)(result) == 0) goto loc_008246A9;
    if ((*(unsigned int *)(v_rdi + 8)) < 56) goto loc_0082460D;
loc_008246A9:
    if ((*(unsigned int *)(v_rdi + 48)) != 5) goto loc_0082476C;
    if ((*(unsigned int *)(v_rdi + 44)) != 12) goto loc_0082476C;
    result = BiIsBootRamdisk(v_rdi + 20, a2, v_stack_m68, v_stack_m58);
    if ((unsigned __int8)(result) == 0) goto loc_0082476C;
    v_stack_m68 = 128;
    result = ExAllocatePool2(258, 128, (unsigned int)(0x4B444342ULL), v_stack_m58);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m58);
    *(unsigned int *)(v_stack_m58) = 2;
    *(unsigned __int64 *)(v_stack_m58 + 20) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m58 + 36) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m58 + 52) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m58 + 68) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m58 + 84) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m58 + 100) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m58 + 116) = v_xmm0;
    *(unsigned int *)(v_stack_m58 + 124) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3044756)));
    goto loc_00823F32;
loc_0082476C:
    goto loc_00824793;
loc_00824777:
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(v_stack_m58, a2, (unsigned int)(v_stack_m68), v_stack_m58);
    if ((unsigned int)(result) == 0) goto loc_0082478A;
    if ((*(unsigned int *)(v_rdi + 8)) < 36) goto loc_0082460D;
loc_0082478A:
loc_00824793:
    result = (32) + (12);
    if (((unsigned int)(*(unsigned int *)(v_rdi + 8))) < result) goto loc_0082460D;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) - (32));
    if ((*(unsigned int *)(v_rdi + 32 + 8)) > ((unsigned int)(a1))) goto loc_0082460D;
    a3 = 0;
    v_stack_p20 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(v_rdi + 32, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, v_stack_m50);
    if (sign_flag) goto loc_00824605;
    if ((*(unsigned int *)(v_stack_m50)) == 3) goto loc_0082460D;
    v_r12 = ((unsigned int)(*(unsigned int *)(v_rdi + 32 + 8))) + (v_rdi + 32);
    result = Feature_255824187__private_IsEnabledDeviceUsageNoInline(v_rdi + 32, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, v_stack_m50);
    if ((unsigned int)(result) != 0) goto loc_00824803;
    v_rsi = (32) | (-1);
loc_008247F7:
    v_rsi = (v_rsi) + 1;
    if ((*(unsigned __int16 *)(v_r12 + v_rsi * 2)) != ((unsigned __int16)(v_r15))) goto loc_008247F7;
    goto loc_0082482E;
loc_00824803:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) - (*(unsigned int *)(v_rdi + 32 + 8)));
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rsi)));
    a1 = (unsigned int)((a1) >> (1));
    if (condition_is_equal) goto loc_00824826;
loc_00824816:
    if ((*(unsigned __int16 *)(v_r12)) == ((unsigned __int16)(v_r15))) goto loc_00824826;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r15))) + 1);
    result = (v_r12) + (2);
    if (((unsigned int)(v_rsi)) < ((unsigned int)(a1))) goto loc_00824816;
loc_00824826:
    if (((unsigned int)(v_rsi)) == ((unsigned int)(a1))) goto loc_0082460D;
loc_0082482E:
    if (((unsigned int)(v_rsi * 2 + 2 + 32)) < 32) goto loc_0082460D;
    if (((unsigned int)(v_rsi * 2 + 2 + 32 + (unsigned int)(v_stack_m64) * 1)) < ((unsigned int)(v_rsi * 2 + 2 + 32))) goto loc_0082460D;
    v_rbx = (unsigned int)((v_rsi * 2 + 2 + 31) & (0xFFFFFFF8ULL));
    v_stack_m68 = (unsigned int)((unsigned int)(v_stack_m64) + v_rbx * 1);
    result = ExAllocatePool2(258, (unsigned int)((unsigned int)((unsigned int)(v_stack_m64) + v_rbx * 1)), (unsigned int)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    a2 = 0;
    result = memset(result, a2, (unsigned int)(v_stack_m68), v_stack_m50);
    a1 = (v_stack_m58) + (24);
    result = memcpy(a1, v_r12, (unsigned int)((unsigned int)(v_rsi * 2 + 2)), v_stack_m50);
    *(unsigned int *)(v_stack_m58 + 20) = (unsigned int)(v_rbx);
    a1 = ((unsigned int)((unsigned int)(v_rbx))) + (v_stack_m58);
    result = memcpy(a1, v_stack_m50, (unsigned int)(v_stack_m64), v_stack_m50);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 16))) - (3));
    result = (unsigned int)(-(result));
    a1 = (unsigned int)((a1) + (4));
    *(unsigned int *)(v_stack_m58) = (unsigned int)(a1);
    goto loc_0082459C;
}
```

## 5. (Beta) C Style

```c
int64_t BiConvertBootEnvironmentDeviceToNt(void *Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint32_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_p10;
    uint64_t v_stack_p20;
    uint8_t v_stack_p8;

    v_stack_p10 = local_rbx;
    v_stack_p20 = Arg4;
    local_rsp = (local_rsp) - (96);
    local_rsi = 0;
    v_stack_m64 = 0;
    v_stack_m60 = 0;
    v_stack_m48 = 0;
    v_stack_m50 = 0;
    v_stack_p8 = 0;
    v_stack_m58 = 0;
    v_stack_m68 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1))) == 0) goto loc_008245A4;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) - (2));
    if (condition_is_equal) goto loc_00824411;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_008243CB;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00824411;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00824365;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00824079;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00823FA0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_00823F39;
    if (((uint32_t)(Arg1)) != 1) goto loc_00824620;
    v_stack_m68 = (uint32_t)(local_rsi + 40);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_rsi + 40)), (uint32_t)(0x4B444342ULL), Arg4);
    v_stack_m58 = result;
    if (result != 0) goto loc_00823F03;
loc_00823EF9:
    goto loc_0082464A;
loc_00823F03:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), Arg4);
    *(uint32_t *)(v_stack_m58) = 11;
    *(uint32_t *)(v_stack_m58 + 0x14) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    *(uint64_t *)(v_stack_m58 + 0x18) = v_xmm0;
loc_00823F32:
    goto loc_00824636;
loc_00823F39:
    result = Feature_1741132088__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(arg1 + 0x10)), Arg2, (uint32_t)(v_stack_m68), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00823F4C;
    if ((*(uint32_t *)(arg1 + 0x8)) < 36) goto loc_0082460D;
loc_00823F4C:
    v_stack_m68 = 40;
    result = ExAllocatePool2(258, 40, (uint32_t)(0x4B444342ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), Arg4);
    *(uint32_t *)(v_stack_m58) = 10;
    *(uint64_t *)(v_stack_m58 + 0x14) = v_xmm0;
    *(uint32_t *)(v_stack_m58 + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    goto loc_00823F32;
loc_00823FA0:
    result = Feature_1406898491__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(arg1 + 0x20)), Arg2, (uint32_t)(v_stack_m68), Arg4);
    if ((uint32_t)(result) != 0) goto loc_00823FF6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) + (21));
    v_stack_m68 = (uint32_t)(result);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(result)), (uint32_t)(0x4B444342ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), Arg4);
    *(uint32_t *)(v_stack_m58) = 9;
    Arg1 = (v_stack_m58) + (20);
    goto loc_00824060;
loc_00823FF6:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) < 20) goto loc_0082460D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (-20));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10)))) > ((uint32_t)(result))) goto loc_0082460D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x10))) + (21));
    if (((uint32_t)(Arg1)) < 21) goto loc_00824070;
    v_stack_m68 = (uint32_t)((uint32_t)((uint32_t)(Arg1)));
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(Arg1)), (uint32_t)(0x4B444342ULL), Arg4);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), Arg4);
    *(uint32_t *)(v_stack_m58) = 9;
    Arg1 = (v_stack_m58) + (20);
    result = (uint32_t)(((uint32_t)(v_stack_m68)) + (-20));
loc_00824060:
    result = strcpy_s(Arg1, (uint32_t)((uint32_t)(result)), Arg1 + 20, Arg4);
    goto loc_00823F32;
loc_00824070:
    goto loc_0082460D;
loc_00824079:
    local_rsi = (local_rsi) | (-1);
    v_stack_m68 = 34;
    if ((*(uint32_t *)(arg1 + 0x10)) != 1) goto loc_008240E7;
    result = Feature_3887567162__private_IsEnabledDeviceUsageNoInline(Arg1, (uint32_t)((uint32_t)(result)), Arg1 + 20, Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) != 0) goto loc_008240AA;
loc_00824098:
    Arg1 = (local_rsi) + 1;
    if ((*(uint16_t *)(arg1 + arg1 * 2 + 0x1C)) != 0) goto loc_00824098;
    goto loc_008240E2;
loc_008240AA:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) <= 28) goto loc_0082460D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (-28));
    result = (uint32_t)((result) >> (1));
    if (condition_is_equal) goto loc_008240D2;
loc_008240C1:
    if ((*(uint16_t *)(arg1 + 0x1C)) == 0) goto loc_008240D2;
    local_r15 = (uint32_t)((0) + 1);
    Arg1 = (Arg1 + 28) + (2);
    if (((uint32_t)(local_r15)) < ((uint32_t)(result))) goto loc_008240C1;
loc_008240D2:
    if (((uint32_t)(local_r15)) == ((uint32_t)(result))) goto loc_0082460D;
loc_008240E2:
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m68) + local_r15 * 2);
    goto loc_008240FE;
loc_008240E7:
    result = Feature_2209321273__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_m68) + local_r15 * 2, Arg2, Arg1 + 20, Arg4);
    Arg2 = 0;
    if ((uint32_t)(result) == 0) goto loc_008240FB;
    if ((*(uint32_t *)(arg1 + 0x10)) != 0) goto loc_0082460D;
loc_008240FB:
loc_008240FE:
    v_stack_m64 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))) == 0) goto loc_0082429B;
    result = Feature_1807454522__private_IsEnabledDeviceUsageNoInline((uint32_t)(v_stack_m68), Arg2, Arg1 + 20, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00824129;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)) + 12)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))))) goto loc_0082460D;
    if ((*(uint32_t *)(arg1 + 0x8)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)) + 12))) goto loc_0082460D;
loc_00824129:
    if ((((uint8_t)((uint32_t)(Arg3))) & (32)) != 0) goto loc_008241B4;
    result = BiGetNtPartitionPath(Arg1, v_stack_m48, Arg1 + 20, Arg4);
    local_r14 = 0;
    if (sign_flag) goto loc_008241B7;
    v_stack_p8 = 1;
loc_00824151:
    result = (local_rsi) + 1;
    if ((*(uint16_t *)(v_stack_m48 + result * 2)) != 0) goto loc_00824151;
    v_stack_m64 = (uint32_t)(result * 2 + 2 + 20);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(result * 2 + 2 + 20)), (uint32_t)(0x4B444342ULL), Arg4);
    v_stack_m50 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m64), Arg4);
    *(uint32_t *)(v_stack_m50) = 2;
    Arg1 = (v_stack_m50) + (20);
    result = memcpy(Arg1, v_stack_m48, (uint32_t)((uint32_t)(result * 2 + 2)), Arg4);
loc_008241B4:
    local_r14 = 0;
loc_008241B7:
    if (v_stack_m50 != 0) goto loc_00824290;
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m48, (uint32_t)((uint32_t)(result * 2 + 2)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_008241E3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) < 20) goto loc_0082460D;
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x18))) > ((uint32_t)(*(uint32_t *)(arg1 + 0x8)) - 20)) goto loc_0082460D;
loc_008241E3:
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(arg1 + 0x8)) - 20, v_stack_m48, (uint32_t)((uint32_t)(result * 2 + 2)), Arg4);
    Arg1 = 0;
    if ((uint32_t)(result) == 0) goto loc_00824201;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if ((*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1 + 0x8)) > ((uint32_t)(result))) goto loc_0082460D;
loc_00824201:
    if ((*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1)) != 0) goto loc_0082460D;
    if ((*(uint32_t *)(arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1 + 0x10)) != 6) goto loc_0082460D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)))));
    if (((uint32_t)(result)) < 76) goto loc_0082460D;
    result = Feature_1322225978__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m48, (uint32_t)((uint32_t)(result * 2 + 2)), Arg4);
    Arg4 = 0;
    if ((uint32_t)(result) != 0) goto loc_00824235;
    goto loc_0082426A;
loc_00824235:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)) + 40)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18))))) goto loc_0082460D;
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x18)) + 40 + 8) + (4);
    if (((uint32_t)(*(uint32_t *)(arg1 + 0x8))) < Arg1) goto loc_0082460D;
    local_r14 = (Arg1 + (uint32_t)(*(uint32_t *)(arg1 + 0x18)) * 1) + (40);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) - ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x18)) + 40)));
    if ((*(uint32_t *)(local_r14 + 0x8)) > Arg2) goto loc_0082460D;
loc_0082426A:
    Arg3 = 0;
    v_stack_m78 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(0 + local_r14 * 1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, v_stack_m50);
    if (sign_flag) goto loc_00824605;
loc_00824290:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m64)) + ((uint32_t)((uint32_t)(v_stack_m68))));
    v_stack_m68 = (uint32_t)(Arg1);
loc_0082429B:
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(Arg1)), (uint32_t)(0x4B444342ULL), v_stack_m50);
    local_r14 = 0;
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    *(uint32_t *)(v_stack_m58) = 8;
    if ((*(uint32_t *)(arg1 + 0x10)) != 0) goto loc_008242F0;
    local_rsi = 0;
    *(uint32_t *)(v_stack_m58 + 0x14) = 0;
    *(uint32_t *)(v_stack_m58 + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x14)));
    goto loc_0082433C;
loc_008242F0:
    *(uint32_t *)(v_stack_m58 + 0x14) = 1;
    result = Feature_3887567162__private_IsEnabledDeviceUsageNoInline((uint32_t)(*(uint32_t *)(arg1 + 0x14)), Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    Arg1 = 0;
    if ((uint32_t)(result) != 0) goto loc_00824323;
loc_00824306:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(arg1 + 0x1C + local_rsi * 2)) != 0) goto loc_00824306;
    Arg1 = (v_stack_m58) + (32);
    result = wcscpy_s(Arg1, local_rsi + 1, Arg1 + 28, v_stack_m50);
    goto loc_0082433A;
loc_00824323:
    Arg1 = (v_stack_m58) + (32);
    Arg3 = ((uint32_t)((uint32_t)(local_r15))) + ((uint32_t)((uint32_t)(local_r15)));
    result = memcpy(Arg1, Arg1 + 28, Arg3, v_stack_m50);
loc_0082433A:
    local_rsi = 0;
loc_0082433C:
    if (v_stack_m50 == 0) goto loc_00823F32;
    *(uint32_t *)(v_stack_m58 + 0x18) = (uint32_t)((uint32_t)(v_stack_m68));
    Arg1 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m68)))) + (v_stack_m58);
    result = memcpy(Arg1, v_stack_m50, (uint32_t)(v_stack_m64), v_stack_m50);
    goto loc_00823F32;
loc_00824365:
    result = Feature_2947256635__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m50, (uint32_t)(v_stack_m64), v_stack_m50);
    if ((uint32_t)(result) == 0) goto loc_00824378;
    if ((*(uint32_t *)(arg1 + 0x8)) < 48) goto loc_0082460D;
loc_00824378:
    v_stack_m68 = 36;
    result = ExAllocatePool2(258, 36, (uint32_t)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    *(uint32_t *)(v_stack_m58) = 7;
    *(uint64_t *)(v_stack_m58 + 0x14) = v_xmm0;
    goto loc_00823F32;
loc_008243CB:
    v_stack_m68 = 20;
    result = ExAllocatePool2(258, 20, (uint32_t)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    *(uint32_t *)(v_stack_m58) = 1;
    goto loc_00823F32;
loc_00824411:
    Arg4 = 0;
    v_stack_m70 = v_stack_m60;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m78 = 0;
    result = BiVerifyBootPartition(Arg1, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00824605;
    if (((0) & (32)) == 0) goto loc_0082444D;
    if ((uint32_t)((uint32_t)(v_stack_m60)) == 0) goto loc_0082444D;
    goto loc_00824467;
loc_0082444D:
    result = BiGetNtPartitionPath(Arg1, v_stack_m48, Arg3, Arg4);
    if (!sign_flag) goto loc_00824533;
loc_00824467:
    if ((uint32_t)((uint32_t)(v_stack_m60)) == 0) goto loc_00824605;
    Arg3 = 0;
    v_stack_m78 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(Arg1 + (uint32_t)(v_stack_m60) * 1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, v_stack_m50);
    local_rsi = 0;
    if (sign_flag) goto loc_00824605;
    result = (uint32_t)(((uint32_t)(v_stack_m64)) + (34));
    v_stack_m68 = (uint32_t)(result);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(result)), (uint32_t)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    *(uint32_t *)(v_stack_m58) = 8;
    *(uint32_t *)(v_stack_m58 + 0x14) = 0;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_00824507;
    if (((uint32_t)((uint32_t)(Arg2))) != 0x21000001ULL) goto loc_008244F8;
    goto loc_00824507;
loc_008244F8:
    Arg1 = (uint32_t)(0x22000002ULL);
    if (((uint32_t)((uint32_t)(Arg2))) == 0x11000043ULL) { Arg1 = (uint32_t)((uint32_t)(0x12000044ULL)); }
loc_00824507:
    *(uint32_t *)(v_stack_m58 + 0x1C) = (uint32_t)(Arg1);
    *(uint32_t *)(v_stack_m58 + 0x18) = 34;
    Arg1 = (v_stack_m58) + (34);
    result = memcpy(Arg1, v_stack_m50, (uint32_t)(v_stack_m64), v_stack_m50);
    goto loc_00824636;
loc_00824533:
    v_stack_p8 = 1;
    local_rsi = (local_rsi) | (-1);
loc_0082453B:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(v_stack_m48 + local_rsi * 2)) != ((uint16_t)(local_r15))) goto loc_0082453B;
    v_stack_m68 = (uint32_t)(local_rsi * 2 + 2 + 20);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)(local_rsi * 2 + 2 + 20)), (uint32_t)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    *(uint32_t *)(v_stack_m58) = 2;
    Arg1 = (v_stack_m58) + (20);
    result = memcpy(Arg1, v_stack_m48, (uint32_t)((uint32_t)(local_rsi * 2 + 2)), v_stack_m50);
loc_0082459C:
    goto loc_00824636;
loc_008245A4:
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(Arg1, v_stack_m48, (uint32_t)((uint32_t)(local_rsi * 2 + 2)), v_stack_m50);
    if ((uint32_t)(result) == 0) goto loc_008245B3;
    if ((*(uint32_t *)(arg1 + 0x8)) < 20) goto loc_0082460D;
loc_008245B3:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x10))))) - (3));
    if (condition_is_equal) goto loc_0082468D;
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_0082468D;
    if (((uint32_t)(result)) != 1) goto loc_0082460D;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8)))) < 52) goto loc_0082460D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (-40));
    if ((*(uint32_t *)(arg1 + 0x28 + 0x8)) > ((uint32_t)(result))) goto loc_0082460D;
    Arg3 = 0;
    v_stack_m78 = v_stack_m68;
    result = BiConvertBootEnvironmentDeviceToNt(Arg1 + 40, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, v_stack_m58);
    if (!sign_flag) goto loc_00824636;
loc_00824605:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0xC000009AULL) goto loc_00824632;
loc_0082460D:
    if (v_stack_m58 != 0) {
        Arg2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m58, Arg2, Arg3, v_stack_m58);
    }
    result = BiConvertBootEnvironmentDeviceToUnknown(Arg1, v_stack_m58, v_stack_m68, v_stack_m58);
loc_00824632:
    if (!(sign_flag)) {
        Arg1 = v_stack_p20;
        result = v_stack_m58;
        *(uint64_t *)(arg1) = result;
        Arg1 = Arg5;
        result = v_stack_m68;
        *(uint32_t *)(arg1) = (uint32_t)(result);
    }
    local_rdi = 0;
    if (v_stack_m50 != 0) {
        Arg2 = 0x4B444342ULL;
        result = ExFreePoolWithTag(v_stack_m50, Arg2, v_stack_m68, v_stack_m58);
    }
    if (v_stack_p8 != 0) {
        Arg2 = 0x4B444342ULL;
        Arg1 = v_stack_m48;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m68, v_stack_m58);
    }
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_0082468D:
    if (((uint32_t)(Arg1)) != 3) goto loc_00824777;
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m68, v_stack_m58);
    if ((uint32_t)(result) == 0) goto loc_008246A9;
    if ((*(uint32_t *)(local_rdi + 0x8)) < 56) goto loc_0082460D;
loc_008246A9:
    if ((*(uint32_t *)(local_rdi + 0x30)) != 5) goto loc_0082476C;
    if ((*(uint32_t *)(local_rdi + 0x2C)) != 12) goto loc_0082476C;
    result = BiIsBootRamdisk(local_rdi + 20, Arg2, v_stack_m68, v_stack_m58);
    if ((uint8_t)(result) == 0) goto loc_0082476C;
    v_stack_m68 = 128;
    result = ExAllocatePool2(258, 128, (uint32_t)(0x4B444342ULL), v_stack_m58);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m58);
    *(uint32_t *)(v_stack_m58) = 2;
    *(uint64_t *)(v_stack_m58 + 0x14) = v_xmm0;
    *(uint64_t *)(v_stack_m58 + 0x24) = v_xmm1;
    *(uint64_t *)(v_stack_m58 + 0x34) = v_xmm0;
    *(uint64_t *)(v_stack_m58 + 0x44) = v_xmm1;
    *(uint64_t *)(v_stack_m58 + 0x54) = v_xmm0;
    *(uint64_t *)(v_stack_m58 + 0x64) = v_xmm1;
    *(uint64_t *)(v_stack_m58 + 0x74) = v_xmm0;
    *(uint32_t *)(v_stack_m58 + 0x7C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x2E7594)));
    goto loc_00823F32;
loc_0082476C:
    goto loc_00824793;
loc_00824777:
    result = Feature_2746716474__private_IsEnabledDeviceUsageNoInline(v_stack_m58, Arg2, (uint32_t)(v_stack_m68), v_stack_m58);
    if ((uint32_t)(result) == 0) goto loc_0082478A;
    if ((*(uint32_t *)(local_rdi + 0x8)) < 36) goto loc_0082460D;
loc_0082478A:
loc_00824793:
    result = (32) + (12);
    if (((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) < result) goto loc_0082460D;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) - (32));
    if ((*(uint32_t *)(local_rdi + 0x20 + 0x8)) > ((uint32_t)(Arg1))) goto loc_0082460D;
    Arg3 = 0;
    v_stack_p20 = v_stack_m64;
    result = BiConvertBootEnvironmentDeviceToNt(local_rdi + 32, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, v_stack_m50);
    if (sign_flag) goto loc_00824605;
    if ((*(uint32_t *)(v_stack_m50)) == 3) goto loc_0082460D;
    local_r12 = ((uint32_t)(*(uint32_t *)(local_rdi + 0x20 + 0x8))) + (local_rdi + 32);
    result = Feature_255824187__private_IsEnabledDeviceUsageNoInline(local_rdi + 32, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, v_stack_m50);
    if ((uint32_t)(result) != 0) goto loc_00824803;
    local_rsi = (32) | (-1);
loc_008247F7:
    local_rsi = (local_rsi) + 1;
    if ((*(uint16_t *)(local_r12 + local_rsi * 2)) != ((uint16_t)(local_r15))) goto loc_008247F7;
    goto loc_0082482E;
loc_00824803:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) - (*(uint32_t *)(local_rdi + 0x20 + 0x8)));
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rsi)));
    Arg1 = (uint32_t)((Arg1) >> (1));
    if (condition_is_equal) goto loc_00824826;
loc_00824816:
    if ((*(uint16_t *)(local_r12)) == ((uint16_t)(local_r15))) goto loc_00824826;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r15))) + 1);
    result = (local_r12) + (2);
    if (((uint32_t)(local_rsi)) < ((uint32_t)(Arg1))) goto loc_00824816;
loc_00824826:
    if (((uint32_t)(local_rsi)) == ((uint32_t)(Arg1))) goto loc_0082460D;
loc_0082482E:
    if (((uint32_t)(local_rsi * 2 + 2 + 32)) < 32) goto loc_0082460D;
    if (((uint32_t)(local_rsi * 2 + 2 + 32 + (uint32_t)(v_stack_m64) * 1)) < ((uint32_t)(local_rsi * 2 + 2 + 32))) goto loc_0082460D;
    local_rbx = (uint32_t)((local_rsi * 2 + 2 + 31) & (0xFFFFFFF8ULL));
    v_stack_m68 = (uint32_t)((uint32_t)(v_stack_m64) + local_rbx * 1);
    result = ExAllocatePool2(258, (uint32_t)((uint32_t)((uint32_t)(v_stack_m64) + local_rbx * 1)), (uint32_t)(0x4B444342ULL), v_stack_m50);
    v_stack_m58 = result;
    if (result == 0) goto loc_00823EF9;
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(v_stack_m68), v_stack_m50);
    Arg1 = (v_stack_m58) + (24);
    result = memcpy(Arg1, local_r12, (uint32_t)((uint32_t)(local_rsi * 2 + 2)), v_stack_m50);
    *(uint32_t *)(v_stack_m58 + 0x14) = (uint32_t)(local_rbx);
    Arg1 = ((uint32_t)((uint32_t)(local_rbx))) + (v_stack_m58);
    result = memcpy(Arg1, v_stack_m50, (uint32_t)(v_stack_m64), v_stack_m50);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x10))) - (3));
    result = (uint32_t)(-(result));
    Arg1 = (uint32_t)((Arg1) + (4));
    *(uint32_t *)(v_stack_m58) = (uint32_t)(Arg1);
    goto loc_0082459C;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0 + rbx*1` | `64` | `R` |
| `Arg1` | `+ 0x0 + rsi*1` | `64` | `R` |
| `Arg1` | `+ 0x0 + rsi*2` | `16` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x14` | `32` | `R` |
| `Arg1` | `+ 0x14` | `64` | `R` |
| `Arg1` | `+ 0x18` | `32` | `R` |
| `Arg1` | `+ 0x1C` | `64` | `R` |
| `Arg1` | `+ 0x1C + rcx*2` | `16` | `R` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `128` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x2C` | `32` | `R` |
| `Arg1` | `+ 0x30` | `32` | `R` |
| `Arg1` | `+ 0x34` | `64` | `R` |
| `Arg5` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00823E44&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
