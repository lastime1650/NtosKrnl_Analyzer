# CmpAccountForLogReservation

- RVA: `0x00842850`–`0x008428D7` (길이 `135` bytes)
- VA: `0x0000000140842850`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068F94`
- 디코드: `34`개 명령, `135/135` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0084286E` → [LockRMLog](LockRMLog_function_00842B88.md) (function, `0x00842B88`)
- `0x008428A3` → `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReserveAndAppendLog` (import, 간접 대상; import `ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReserveAndAppendLog`)
- `0x008428B8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008428BD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- [CmpTransInitializeTransaction](CmpTransInitializeTransaction_function_008422C8.md) at `0x008423C0`
- [CmKtmNotification](../9B/CmKtmNotification_function_009B1950.md) at `0x009B1CCE`

### Static image references
- `0x008428A3` → RVA `0x00151278` (`ext-ms-win-fs-clfs-l1-1-0.dll!ClfsReserveAndAppendLog (IAT)`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008428B8` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008428BD` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00842850  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00842855  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0084285A  57                              push rdi
0084285B  48 83 EC 50                     sub rsp, 0x50
0084285F  41 8A D8                        mov bl, r8b
00842862  48 C7 44 24 68 30 00 00 00      mov qword ptr [rsp + 0x68], 0x30
0084286B  48 8B F9                        mov rdi, rcx
0084286E  E8 15 03 00 00                  call 0x140842b88
00842873  48 8B 4F 60                     mov rcx, qword ptr [rdi + 0x60]
00842877  48 8D 44 24 68                  lea rax, [rsp + 0x68]
0084287C  33 D2                           xor edx, edx
0084287E  45 33 C9                        xor r9d, r9d
00842881  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00842886  45 33 C0                        xor r8d, r8d
00842889  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
0084288D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00842892  C7 44 24 28 01 00 00 00         mov dword ptr [rsp + 0x28], 1
0084289A  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
0084289F  84 DB                           test bl, bl
008428A1  74 2D                           je 0x1408428d0
008428A3  48 FF 15 CE E9 90 FF            call qword ptr [rip - 0x6f1632]
008428AA  0F 1F 44 00 00                  nop dword ptr [rax + rax]
008428AF  48 8B 8F 80 00 00 00            mov rcx, qword ptr [rdi + 0x80]
008428B6  8B D8                           mov ebx, eax
008428B8  E8 53 D1 A1 FF                  call 0x14025fa10
008428BD  E8 EE AF A1 FF                  call 0x14025d8b0
008428C2  8B C3                           mov eax, ebx
008428C4  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008428C9  48 83 C4 50                     add rsp, 0x50
008428CD  5F                              pop rdi
008428CE  C3                              ret
008428CF  CC                              int3
008428D0  48 F7 5C 24 68                  neg qword ptr [rsp + 0x68]
008428D5  EB CC                           jmp 0x1408428a3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpAccountForLogReservation(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (80);
    v_stack_p10 = 48;
    result = LockRMLog(a1, a2, a3, a4);
    a2 = 0;
    a4 = 0;
    v_stack_m18 = 0;
    a3 = 0;
    v_stack_m20 = 0;
    v_stack_m28 = v_stack_p10;
    v_stack_m30 = 1;
    v_stack_m38 = 0;
    if ((unsigned __int8)((unsigned __int8)(a3)) == 0) goto loc_008428D0;
loc_008428A3:
    result = ext_ms_win_fs_clfs_l1_1_0_dll_ClfsReserveAndAppendLog(*(unsigned __int64 *)(a1 + 96), a2, a3, a4);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 128), a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 128), a2, a3, a4);
    v_rsp = (v_rsp) + (80);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_008428D0:
    goto loc_008428A3;
}
```

## 5. (Beta) C Style

```c
int64_t CmpAccountForLogReservation(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_p10;
    uint64_t v_stack_p68;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (80);
    v_stack_p10 = 48;
    result = LockRMLog(Arg1, Arg2, Arg3, Arg4);
    Arg2 = 0;
    Arg4 = 0;
    v_stack_m18 = 0;
    Arg3 = 0;
    v_stack_m20 = 0;
    v_stack_m28 = v_stack_p10;
    v_stack_m30 = 1;
    v_stack_m38 = 0;
    if ((uint8_t)((uint8_t)(Arg3)) == 0) goto loc_008428D0;
loc_008428A3:
    result = kernel_indirect_call(*(uint64_t *)(arg1 + 0x60), Arg2, Arg3, Arg4);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x80), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x80), Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_008428D0:
    goto loc_008428A3;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg1` | `+ 0x80` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00842850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00842850[BB_00842850]
  bb_008428A3[BB_008428A3]
  bb_008428CF[BB_008428CF]
  bb_008428D0[BB_008428D0]
  bb_00842850 -->|branch| bb_008428D0
  bb_00842850 -->|fallthrough| bb_008428A3
  bb_008428CF -->|flow| bb_008428D0
  bb_008428D0 -->|branch| bb_008428A3
```
