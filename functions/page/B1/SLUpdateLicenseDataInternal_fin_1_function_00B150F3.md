# SLUpdateLicenseDataInternal$fin$1

- RVA: `0x00B150F3`–`0x00B1513B` (길이 `72` bytes)
- VA: `0x0000000140B150F3`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000D4F5C`
- 디코드: `21`개 명령, `72/72` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B1511B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x00B15128` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00B1512D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00B1511B` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x00B15128` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00B1512D` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B150F3  40 53                           push rbx
00B150F5  55                              push rbp
00B150F6  48 83 EC 48                     sub rsp, 0x48
00B150FA  48 8B EA                        mov rbp, rdx
00B150FD  48 8B 9D 10 02 00 00            mov rbx, qword ptr [rbp + 0x210]
00B15104  33 C9                           xor ecx, ecx
00B15106  8D 41 11                        lea eax, [rcx + 0x11]
00B15109  F0 48 0F B1 8B F8 B6 00 00      lock cmpxchg qword ptr [rbx + 0xb6f8], rcx
00B15112  74 0D                           je 0x140b15121
00B15114  48 8D 8B F8 B6 00 00            lea rcx, [rbx + 0xb6f8]
00B1511B  E8 20 E3 74 FF                  call 0x140263440
00B15120  90                              nop
00B15121  48 8D 8B F8 B6 00 00            lea rcx, [rbx + 0xb6f8]
00B15128  E8 D3 C4 7C FF                  call 0x1402e1600
00B1512D  E8 7E 87 74 FF                  call 0x14025d8b0
00B15132  90                              nop
00B15133  48 83 C4 48                     add rsp, 0x48
00B15137  5D                              pop rbp
00B15138  5B                              pop rbx
00B15139  C3                              ret
00B1513A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SLUpdateLicenseDataInternal_fin_1(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (72);
    a1 = 0;
    result = a1 + 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a2 + 528) + 46840;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a2 + 528) + 46840, a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a2 + 528) + 46840, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SLUpdateLicenseDataInternal_fin_1(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (72);
    Arg1 = 0;
    result = Arg1 + 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg2 + 0x210) + 46840;
        result = ExfReleasePushLockShared(Arg1, Arg2, a3, a4);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg2 + 0x210) + 46840, Arg2, a3, a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg2 + 0x210) + 46840, Arg2, a3, a4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x210` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B150F3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B150F3[BB_00B150F3]
  bb_00B15114[BB_00B15114]
  bb_00B15121[BB_00B15121]
  bb_00B1513A[BB_00B1513A]
  bb_00B150F3 -->|branch| bb_00B15121
  bb_00B150F3 -->|fallthrough| bb_00B15114
  bb_00B15114 -->|flow| bb_00B15121
```
