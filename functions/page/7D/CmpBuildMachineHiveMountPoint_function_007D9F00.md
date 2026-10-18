# CmpBuildMachineHiveMountPoint

- RVA: `0x007D9F00`–`0x007D9F6A` (길이 `106` bytes)
- VA: `0x00000001407D9F00`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `27`개 명령, `106/106` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007D9F1E` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007D9F39` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007D9F54` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)

### Direct callers
- [CmpFindMachineHiveByMountPoint](../7E/CmpFindMachineHiveByMountPoint_function_007E1DF8.md) at `0x007E1E4B`
- [CmpMachineHiveListInitialize](../AD/CmpMachineHiveListInitialize_function_00AD4B98.md) at `0x00AD4C2A`

### Static image references
- `0x007D9F17` → RVA `0x00B08FE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007D9F2A` → RVA `0x00E098A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007D9F1E` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007D9F39` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007D9F54` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D9F00  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
007D9F05  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
007D9F0A  57                              push rdi
007D9F0B  48 83 EC 20                     sub rsp, 0x20
007D9F0F  48 8B FA                        mov rdi, rdx
007D9F12  8B D9                           mov ebx, ecx
007D9F14  48 8B CF                        mov rcx, rdi
007D9F17  48 8D 15 C2 F0 32 00            lea rdx, [rip + 0x32f0c2]
007D9F1E  E8 6D 5A C3 FF                  call 0x14040f990
007D9F23  48 69 DB B8 00 00 00            imul rbx, rbx, 0xb8
007D9F2A  48 8D 35 6F F9 62 00            lea rsi, [rip + 0x62f96f]
007D9F31  48 8B CF                        mov rcx, rdi
007D9F34  48 8B 54 33 08                  mov rdx, qword ptr [rbx + rsi + 8]
007D9F39  E8 52 5A C3 FF                  call 0x14040f990
007D9F3E  48 8B 54 33 10                  mov rdx, qword ptr [rbx + rsi + 0x10]
007D9F43  48 85 D2                        test rdx, rdx
007D9F46  75 09                           jne 0x1407d9f51
007D9F48  48 8B 14 33                     mov rdx, qword ptr [rbx + rsi]
007D9F4C  48 89 54 33 10                  mov qword ptr [rbx + rsi + 0x10], rdx
007D9F51  48 8B CF                        mov rcx, rdi
007D9F54  E8 37 5A C3 FF                  call 0x14040f990
007D9F59  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
007D9F5E  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
007D9F63  48 83 C4 20                     add rsp, 0x20
007D9F67  5F                              pop rdi
007D9F68  C3                              ret
007D9F69  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpBuildMachineHiveMountPoint(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = RtlAppendUnicodeToString(a2, v_rip + 3338434, a3, a4);
    v_rbx = ((unsigned int)(a1)) * ((unsigned int)(a1));
    result = RtlAppendUnicodeToString(a2, *(unsigned __int64 *)(v_rbx + v_rip + 6486383 * 1 + 8), a3, a4);
    if (*(unsigned __int64 *)(v_rbx + v_rip + 6486383 * 1 + 16) == 0) {
        a2 = *(unsigned __int64 *)(v_rbx + v_rip + 6486383 * 1);
        *(unsigned __int64 *)(v_rbx + v_rip + 6486383 * 1 + 16) = a2;
    }
    result = RtlAppendUnicodeToString(a2, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpBuildMachineHiveMountPoint(void *Arg1, int64_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = RtlAppendUnicodeToString(Arg2, v_rip + 3338434, a3, a4);
    local_rbx = ((uint32_t)(Arg1)) * ((uint32_t)(Arg1));
    result = RtlAppendUnicodeToString(Arg2, *(uint64_t *)(local_rbx + v_rip + 0x62F96F * 1 + 0x8), a3, a4);
    if (*(uint64_t *)(local_rbx + v_rip + 0x62F96F * 1 + 0x10) == 0) {
        Arg2 = *(uint64_t *)(local_rbx + v_rip + 0x62F96F * 1);
        *(uint64_t *)(local_rbx + v_rip + 0x62F96F * 1 + 0x10) = Arg2;
    }
    result = RtlAppendUnicodeToString(Arg2, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0 + rsi*1` | `64` | `R` |
| `Arg1` | `+ 0x8 + rsi*1` | `64` | `R` |
| `Arg1` | `+ 0x10 + rsi*1` | `64` | `R` |
| `Arg1` | `+ 0x10 + rsi*1` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D9F00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D9F00[BB_007D9F00]
  bb_007D9F48[BB_007D9F48]
  bb_007D9F51[BB_007D9F51]
  bb_007D9F69[BB_007D9F69]
  bb_007D9F00 -->|branch| bb_007D9F51
  bb_007D9F00 -->|fallthrough| bb_007D9F48
  bb_007D9F48 -->|flow| bb_007D9F51
```
