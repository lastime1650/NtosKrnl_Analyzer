# FsRtlpOplockFsctrlInternal$fin$1

- RVA: `0x00B10D70`–`0x00B10DB3` (길이 `67` bytes)
- VA: `0x0000000140B10D70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A5F14`
- 디코드: `22`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B10D8D` → [FsRtlpClearOwner](../../text/26/FsRtlpClearOwner_function_00265BE8.md) (function, `0x00265BE8`)
- `0x00B10D98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B10DA5` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B10D8D` → [FsRtlpClearOwner](../../text/26/FsRtlpClearOwner_function_00265BE8.md) (`PAGE` → `.text`)
  - `0x00B10D98` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B10DA5` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B10D70  40 53                           push rbx
00B10D72  55                              push rbp
00B10D73  48 83 EC 48                     sub rsp, 0x48
00B10D77  48 8B EA                        mov rbp, rdx
00B10D7A  48 8B 55 50                     mov rdx, qword ptr [rbp + 0x50]
00B10D7E  48 8B 9D A8 00 00 00            mov rbx, qword ptr [rbp + 0xa8]
00B10D85  48 85 D2                        test rdx, rdx
00B10D88  74 14                           je 0x140b10d9e
00B10D8A  48 8B CB                        mov rcx, rbx
00B10D8D  E8 56 4E 75 FF                  call 0x140265be8
00B10D92  33 D2                           xor edx, edx
00B10D94  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
00B10D98  E8 D3 1A 07 00                  call 0x140b82870
00B10D9D  90                              nop
00B10D9E  48 8B 8B 98 00 00 00            mov rcx, qword ptr [rbx + 0x98]
00B10DA5  E8 F6 F5 73 FF                  call 0x1402503a0
00B10DAA  90                              nop
00B10DAB  48 83 C4 48                     add rsp, 0x48
00B10DAF  5D                              pop rbp
00B10DB0  5B                              pop rbx
00B10DB1  C3                              ret
00B10DB2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlpOplockFsctrlInternal_fin_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(a2 + 80) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 168);
        result = FsRtlpClearOwner(a1, *(unsigned __int64 *)(a2 + 80), a3, a4);
        a2 = 0;
        a1 = *(unsigned __int64 *)(a2 + 80);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 168) + 152), a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlpOplockFsctrlInternal_fin_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(arg2 + 0x50) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0xA8);
        result = FsRtlpClearOwner(Arg1, *(uint64_t *)(arg2 + 0x50), a3, a4);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg2 + 0x50);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    result = ExReleaseFastMutexUnsafe(*(uint64_t *)(*(uint64_t *)(arg2 + 0xA8) + 0x98), Arg2, a3, a4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0xA8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B10D70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B10D70[BB_00B10D70]
  bb_00B10D8A[BB_00B10D8A]
  bb_00B10D9E[BB_00B10D9E]
  bb_00B10DB2[BB_00B10DB2]
  bb_00B10D70 -->|branch| bb_00B10D9E
  bb_00B10D70 -->|fallthrough| bb_00B10D8A
  bb_00B10D8A -->|flow| bb_00B10D9E
```
