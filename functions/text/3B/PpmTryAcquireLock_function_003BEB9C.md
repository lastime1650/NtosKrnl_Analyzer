# PpmTryAcquireLock

- RVA: `0x003BEB9C`–`0x003BEC25` (길이 `137` bytes)
- VA: `0x00000001403BEB9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008DE88`
- 디코드: `33`개 명령, `137/137` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x003BEBCA` → [KiSetSystemPriorityThread](../2D/KiSetSystemPriorityThread_function_002D9FF8.md) (function, `0x002D9FF8`)
- `0x003BEBE8` → [KeWaitForSingleObject](../20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x003BEC19` → [KiClearSystemPriority](../2C/KiClearSystemPriority_function_002C05A8.md) (function, `0x002C05A8`)
- `0x003BEC1E` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [PoLatencySensitivityHint](PoLatencySensitivityHint_function_003BE9B0.md) at `0x003BEAA5`

### Static image references
- `0x003BEBE1` → RVA `0x00F0CC08` (`.data`; read)
- `0x003BEBFC` → RVA `0x00F0CC00` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003BEB9C  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003BEBA1  53                              push rbx
003BEBA2  48 83 EC 30                     sub rsp, 0x30
003BEBA6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
003BEBAF  33 DB                           xor ebx, ebx
003BEBB1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
003BEBB8  8D 53 16                        lea edx, [rbx + 0x16]
003BEBBB  90                              nop
003BEBBC  48 89 5C 24 48                  mov qword ptr [rsp + 0x48], rbx
003BEBC1  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003BEBCA  E8 29 B4 F1 FF                  call 0x1402d9ff8
003BEBCF  48 8D 44 24 48                  lea rax, [rsp + 0x48]
003BEBD4  45 33 C9                        xor r9d, r9d
003BEBD7  45 33 C0                        xor r8d, r8d
003BEBDA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
003BEBDF  33 D2                           xor edx, edx
003BEBE1  48 8D 0D 20 E0 B4 00            lea rcx, [rip + 0xb4e020]
003BEBE8  E8 C3 FA E4 FF                  call 0x14020e6b0
003BEBED  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
003BEBF6  85 C0                           test eax, eax
003BEBF8  75 12                           jne 0x1403bec0c
003BEBFA  B3 01                           mov bl, 1
003BEBFC  48 89 0D FD DF B4 00            mov qword ptr [rip + 0xb4dffd], rcx
003BEC03  8A C3                           mov al, bl
003BEC05  48 83 C4 30                     add rsp, 0x30
003BEC09  5B                              pop rbx
003BEC0A  C3                              ret
003BEC0B  CC                              int3
003BEC0C  48 8D 54 24 40                  lea rdx, [rsp + 0x40]
003BEC11  C7 44 24 40 16 00 00 00         mov dword ptr [rsp + 0x40], 0x16
003BEC19  E8 8A 19 F0 FF                  call 0x1402c05a8
003BEC1E  E8 8D EC E9 FF                  call 0x14025d8b0
003BEC23  EB DE                           jmp 0x1403bec03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmTryAcquireLock(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (48);
    v_rbx = 0;
    v_stack_p10 = 0;
    result = KiSetSystemPriorityThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_rbx + 22, a3, a4);
    a4 = 0;
    a3 = 0;
    v_stack_m18 = v_stack_p10;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 11853856, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_003BEC0C;
    *(unsigned __int64 *)(v_rip + 11853821) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_003BEC03:
    v_rsp = (v_rsp) + (48);
    return 1;
loc_003BEC0C:
    v_stack_p40 = 22;
    result = KiClearSystemPriority(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p40, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_p40, a3, a4);
    goto loc_003BEC03;
}
```

## 5. (Beta) C Style

```c
int64_t PpmTryAcquireLock(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p40;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (48);
    local_rbx = 0;
    v_stack_p10 = 0;
    result = KiSetSystemPriorityThread(*(uint64_t *)(gs_base + (0 + 0x188)), local_rbx + 22, Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    v_stack_m18 = v_stack_p10;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 11853856, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_003BEC0C;
    *(uint64_t *)(v_rip + 0xB4DFFD) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_003BEC03:
    local_rsp = (local_rsp) + (48);
    return 1;
loc_003BEC0C:
    v_stack_p40 = 22;
    result = KiClearSystemPriority(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p40, Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_p40, Arg3, Arg4);
    goto loc_003BEC03;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003BEB9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003BEB9C[BB_003BEB9C]
  bb_003BEBFA[BB_003BEBFA]
  bb_003BEC03[BB_003BEC03]
  bb_003BEC0B[BB_003BEC0B]
  bb_003BEC0C[BB_003BEC0C]
  bb_003BEB9C -->|branch| bb_003BEC0C
  bb_003BEB9C -->|fallthrough| bb_003BEBFA
  bb_003BEBFA -->|flow| bb_003BEC03
  bb_003BEC0B -->|flow| bb_003BEC0C
  bb_003BEC0C -->|branch| bb_003BEC03
```
