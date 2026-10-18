# FsRtlNotifyCleanup$fin$0

- RVA: `0x00B1150B`–`0x00B1154E` (길이 `67` bytes)
- VA: `0x0000000140B1150B`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000AD428`
- 디코드: `24`개 명령, `67/67` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B11524` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x00B11536` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00B11540` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00B11524` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x00B11540` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B1150B  40 53                           push rbx
00B1150D  55                              push rbp
00B1150E  48 83 EC 28                     sub rsp, 0x28
00B11512  48 8B EA                        mov rbp, rdx
00B11515  48 8B 4D 40                     mov rcx, qword ptr [rbp + 0x40]
00B11519  83 69 40 01                     sub dword ptr [rcx + 0x40], 1
00B1151D  75 0B                           jne 0x140b1152a
00B1151F  48 83 61 38 00                  and qword ptr [rcx + 0x38], 0
00B11524  E8 77 EE 73 FF                  call 0x1402503a0
00B11529  90                              nop
00B1152A  48 8B 5D 58                     mov rbx, qword ptr [rbp + 0x58]
00B1152E  48 85 DB                        test rbx, rbx
00B11531  74 13                           je 0x140b11546
00B11533  48 8B CB                        mov rcx, rbx
00B11536  E8 D5 A1 D5 FF                  call 0x14086b710
00B1153B  33 D2                           xor edx, edx
00B1153D  48 8B CB                        mov rcx, rbx
00B11540  E8 2B 13 07 00                  call 0x140b82870
00B11545  90                              nop
00B11546  48 83 C4 28                     add rsp, 0x28
00B1154A  5D                              pop rbp
00B1154B  5B                              pop rbx
00B1154C  C3                              ret
00B1154D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall FsRtlNotifyCleanup_fin_0(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (!(condition_is_not_equal)) {
        result = ExReleaseFastMutexUnsafe(*(unsigned __int64 *)(a2 + 64), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a2 + 88) != 0) {
        a1 = *(unsigned __int64 *)(a2 + 88);
        result = SeReleaseSubjectContext(a1, a2, a3, a4);
        a2 = 0;
        a1 = *(unsigned __int64 *)(a2 + 88);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t FsRtlNotifyCleanup_fin_0(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (!(condition_is_not_equal)) {
        result = ExReleaseFastMutexUnsafe(*(uint64_t *)(arg2 + 0x40), Arg2, a3, a4);
    }
    if (*(uint64_t *)(arg2 + 0x58) != 0) {
        Arg1 = *(uint64_t *)(arg2 + 0x58);
        result = SeReleaseSubjectContext(Arg1, Arg2, a3, a4);
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg2 + 0x58);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x58` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B1150B&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B1150B[BB_00B1150B]
  bb_00B1151F[BB_00B1151F]
  bb_00B1152A[BB_00B1152A]
  bb_00B11533[BB_00B11533]
  bb_00B11546[BB_00B11546]
  bb_00B1154D[BB_00B1154D]
  bb_00B1150B -->|branch| bb_00B1152A
  bb_00B1150B -->|fallthrough| bb_00B1151F
  bb_00B1151F -->|flow| bb_00B1152A
  bb_00B1152A -->|branch| bb_00B11546
  bb_00B1152A -->|fallthrough| bb_00B11533
  bb_00B11533 -->|flow| bb_00B11546
```
