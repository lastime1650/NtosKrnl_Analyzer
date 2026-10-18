# RtlpHpVsSubsegmentFree

- RVA: `0x002E7D9C`–`0x002E7DE3` (길이 `71` bytes)
- VA: `0x00000001402E7D9C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `19`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x002E7DD1` → [RtlpHpSegLfhVsFree](RtlpHpSegLfhVsFree_function_002E7DF0.md) (function, `0x002E7DF0`)
- `0x002E7DDC` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [sub_002E6E90](Unknown_function_002E6E90.md) at `0x002E7202`
- [RtlpHpVsSlotFreeList](../36/RtlpHpVsSlotFreeList_function_00361ACC.md) at `0x00361CC8`
- [RtlpHpVsContextCleanup](../60/RtlpHpVsContextCleanup_function_00605644.md) at `0x006056AF`

### Static image references
- `0x002E7DAB` → RVA `0x00E28300` (`.data`; read)
- `0x002E7DBE` → RVA `0x002E7DF0` (`RtlpHpSegLfhVsFree`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002E7D9C  48 83 EC 28                     sub rsp, 0x28
002E7DA0  48 8B 41 18                     mov rax, qword ptr [rcx + 0x18]
002E7DA4  4C 8B C9                        mov r9, rcx
002E7DA7  4C 33 49 08                     xor r9, qword ptr [rcx + 8]
002E7DAB  48 33 05 4E 05 B4 00            xor rax, qword ptr [rip + 0xb4054e]
002E7DB2  44 0F B7 42 20                  movzx r8d, word ptr [rdx + 0x20]
002E7DB7  48 33 C1                        xor rax, rcx
002E7DBA  41 83 C0 03                     add r8d, 3
002E7DBE  48 8D 0D 2B 00 00 00            lea rcx, [rip + 0x2b]
002E7DC5  41 C1 E0 04                     shl r8d, 4
002E7DC9  48 3B C1                        cmp rax, rcx
002E7DCC  49 8B C9                        mov rcx, r9
002E7DCF  75 0B                           jne 0x1402e7ddc
002E7DD1  E8 1A 00 00 00                  call 0x1402e7df0
002E7DD6  48 83 C4 28                     add rsp, 0x28
002E7DDA  C3                              ret
002E7DDB  CC                              int3
002E7DDC  E8 EF 2C 3D 00                  call 0x1406baad0
002E7DE1  EB F3                           jmp 0x1402e7dd6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVsSubsegmentFree(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a4 = (a1) ^ (*(unsigned __int64 *)(a1 + 8));
    result = (*(unsigned __int64 *)(a1 + 24)) ^ (*(unsigned __int64 *)(v_rip + 11797838));
    result = (result) ^ (a1);
    a3 = (unsigned int)((*(unsigned __int16 *)(a2 + 32)) + (3));
    a3 = (unsigned int)((a3) << (4));
    if (result != (v_rip + 43)) goto loc_002E7DDC;
    result = RtlpHpSegLfhVsFree(a4, a2, a3, a4);
loc_002E7DD6:
    v_rsp = (v_rsp) + (40);
    return result;
loc_002E7DDC:
    result = guard_dispatch_icall(a4, a2, a3, a4);
    goto loc_002E7DD6;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVsSubsegmentFree(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    a4 = (Arg1) ^ (*(uint64_t *)(arg1 + 0x8));
    result = (*(uint64_t *)(arg1 + 0x18)) ^ (*(uint64_t *)(v_rip + 0xB4054E));
    result = (result) ^ (Arg1);
    a3 = (uint32_t)((*(uint16_t *)(arg2 + 0x20)) + (3));
    a3 = (uint32_t)((a3) << (4));
    if (result != (v_rip + 43)) goto loc_002E7DDC;
    result = RtlpHpSegLfhVsFree(a4, Arg2, a3, a4);
loc_002E7DD6:
    local_rsp = (local_rsp) + (40);
    return result;
loc_002E7DDC:
    result = guard_dispatch_icall(a4, Arg2, a3, a4);
    goto loc_002E7DD6;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg2` | `+ 0x20` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002E7D9C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002E7D9C[BB_002E7D9C]
  bb_002E7DD1[BB_002E7DD1]
  bb_002E7DD6[BB_002E7DD6]
  bb_002E7DDB[BB_002E7DDB]
  bb_002E7DDC[BB_002E7DDC]
  bb_002E7D9C -->|branch| bb_002E7DDC
  bb_002E7D9C -->|fallthrough| bb_002E7DD1
  bb_002E7DD1 -->|flow| bb_002E7DD6
  bb_002E7DDB -->|flow| bb_002E7DDC
  bb_002E7DDC -->|branch| bb_002E7DD6
```
